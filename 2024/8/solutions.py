from collections import defaultdict

def add_antinodes(a1, a2, grid, nodes):
    y_diff = a1[0] - a2[0]
    x_diff = a1[1] - a2[1]

    y1 = a1[0] + y_diff
    x1 = a1[1] + x_diff

    if 0 <= y1 < len(grid) and 0 <= x1 < len(grid[y1]):
        nodes.add((y1, x1))
    
    y2 = a2[0] - y_diff
    x2 = a2[1] - x_diff

    if y2 >= 0 and y2 < len(grid) and x2 >= 0 and x2 < len(grid[y2]):
        nodes.add((y2, x2))
    
def add_antinodes_p2(a1, a2, grid, nodes):
    y_diff = a1[0] - a2[0]
    x_diff = a1[1] - a2[1]

    y, x = a1
    while 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        nodes.add((y, x))
        y += y_diff
        x += x_diff
    
    y, x = a2
    while 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        nodes.add((y, x))
        y -= y_diff
        x -= x_diff
    


if __name__ == "__main__":
    antennas = defaultdict(list)
    with open("input.txt") as f:
        line_number = 0
        grid = [list(x.strip()) for x in f.readlines()]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '.':
                    antennas[grid[i][j]].append((i, j))
            
    nodes = set()
    for c in antennas:
        coords = antennas[c]
        for i in range(len(coords)):
            for j in range(i+1, len(coords)):
                add_antinodes(coords[i], coords[j], grid, nodes)

    print(len(nodes)) # part 1

    nodes = set()
    for c in antennas:
        coords = antennas[c]
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                add_antinodes_p2(coords[i], coords[j], grid, nodes)

    for n in nodes:
        grid[n[0]][n[1]] = '#'

    print(len(nodes)) # part 2