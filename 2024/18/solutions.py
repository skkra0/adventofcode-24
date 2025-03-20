import collections
def solve_p1(grid, start, end):
    visited = set()
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    de = collections.deque([(start[0], start[1], 0)])
    while de:
        y, x, distance = de.popleft()
        if y == end[0] and x == end[1]:
            return distance
    
        for d in directions:
            new_y = y + d[0]
            new_x = x + d[1]
            if (
                (new_y, new_x) in visited or
                not (0 <= new_y < len(grid) and 0 <= new_x < len(grid[0])) or
                grid[new_y][new_x] == "#"
                ):
                continue
            de.append((new_y, new_x, distance + 1))
            visited.add((new_y, new_x))
    return -1

if __name__ == "__main__":
    width = 71
    height = 71
    grid = [["." for _ in range(width)] for _ in range(height)]

    with open("input.txt") as f:
        for _ in range(1024):
            x, y = f.readline().split(",")
            grid[int(y)][int(x)] = "#"
    
        print(solve_p1(grid, (0, 0), (70, 70))) # part 1
        for l in f.readlines():
            x, y = l.split(",")
            grid[int(y)][int(x)] = "#"
            if solve_p1(grid, (0, 0), (70, 70)) == -1:
                print(f"{x},{y}") # part 2
                break