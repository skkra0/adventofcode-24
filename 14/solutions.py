import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
def move_robots(robots, width, height, time):
    for i in range(len(robots)):
        x, y, vx, vy = robots[i]
        x = (x + vx * time) % width
        y = (y + vy * time) % height
        robots[i][0] = x
        robots[i][1] = y

def get_safety_p1(robots, width, height):
    # width and height are odd
    quadrants = [0, 0, 0, 0]
    for robot in robots:
        x, y = robot[0], robot[1]
        if x < width // 2 and y < height // 2:
            quadrants[0] += 1
        elif x > width // 2 and y < height // 2:
            quadrants[1] += 1
        elif x < width // 2 and y > height // 2:
            quadrants[2] += 1
        elif x > width // 2 and y > height // 2:
            quadrants[3] += 1
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
if __name__ == "__main__":
    robots = []
    with open("input.txt") as f:
        for line in f.readlines():
            s = re.search(r"p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)", line)
            x = int(s.group(1))
            y = int(s.group(2))
            vx = int(s.group(3))
            vy = int(s.group(4))
            robots.append([x, y, vx, vy])
    
    width = 101
    height = 103
    move_robots(robots, width, height, 100)
    print(get_safety_p1(robots, width, height))

    move_robots(robots, width, height, -100)
    nrows, ncols = 4, 4
    plots_per_page = nrows * ncols
    N = 300
    move_robots(robots, width, height, 60)
    pdf = PdfPages("14.pdf")
    for i in range(N):
        grid = [[0 for _ in range(width)] for _ in range(height)]
        for robot in robots:
            grid[robot[1]][robot[0]] = 1

        if i % plots_per_page == 0:
            fig, axes = plt.subplots(nrows, ncols, figsize=(12, 12))
            axes = axes.flatten() 

        subplot_idx = i % plots_per_page
        
        axes[subplot_idx].imshow(grid)
        axes[subplot_idx].plot()
        axes[subplot_idx].set_title(f"Plot #{60 + i * 103}")

        if (i + 1) % plots_per_page == 0 or i == N - 1:
            pdf.savefig(fig) 
            plt.close()
        move_robots(robots, width, height, 103)
    pdf.close()