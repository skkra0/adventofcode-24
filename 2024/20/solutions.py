import collections
def get_path(grid, start, end):
    # one possible path
    visited = set()
    visited.add(start)
    path = [start]
    y, x = start
    while (y, x) != end:
        for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_y = y + d[0]
            new_x = x + d[1]
            if (
                (new_y, new_x) in visited or
                not (0 <= new_y < len(grid) and 0 <= new_x < len(grid[0])) or
                grid[new_y][new_x] == "#"
            ):
                continue

            path.append((new_y, new_x))
            visited.add((new_y, new_x))
            y = new_y
            x = new_x
    return { path[i]: i for i in range(len(path)) }

def solve_p1(fname, save_min):
    grid = []
    start = ()
    end = ()
    with open(fname) as f:
        ct = 0
        while True:
            line = []
            l = f.readline()
            if not l:
                break
            for i in range(len(l)):
                line.append(l[i])
                if l[i] == "S":
                    start = (ct, i)
                if l[i] == "E":
                    end = (ct, i)
            grid.append(line)
            ct += 1
    
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    distances = get_path(grid, start, end)
    cheats = set()

    for p in distances.keys():
        y, x = p
        for d in directions:
            cheat_start_y, cheat_start_x = y + d[0], x + d[1]
            if not (0 <= cheat_start_y < len(grid) and 0 <= cheat_start_x < len(grid[0])) or grid[cheat_start_y][cheat_start_x] != "#":
                continue
            
            for di in directions:
                cy, cx = cheat_start_y + di[0], cheat_start_x + di[1]
                if (cy, cx) in distances:
                    dist_with_cheat = distances[(y, x)] + 2 + (len(distances) - distances[(cy, cx)])
                    if len(distances) - dist_with_cheat >= save_min:
                        cheats.add((cheat_start_y, cheat_start_x, cy, cx))
    return len(cheats)

def solve_p2(fname, save_min):
    grid = []
    start = ()
    end = ()
    with open(fname) as f:
        ct = 0
        while True:
            line = []
            l = f.readline()
            if not l:
                break
            for i in range(len(l)):
                line.append(l[i])
                if l[i] == "S":
                    start = (ct, i)
                if l[i] == "E":
                    end = (ct, i)
            grid.append(line)
            ct += 1

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    distances = get_path(grid, start, end)
    max_cheat_time = 20
    cheats = set()
    def add_cheats_from(start, current, time_remaining, visited):
        if current in distances:
            dist_with_cheat = distances[start] + max_cheat_time - time_remaining + len(distances) - distances[current]
            if len(distances) - dist_with_cheat >= save_min:
                cheats.add((start[0], start[1], current[0], current[1]))

        if time_remaining == 0:
            return
        
        for d in directions:
            y, x = current[0] + d[0], current[1] + d[1]
            if (y, x, time_remaining - 1) not in visited and 0 <= y < len(grid) and 0 <= x < len(grid[0]):
                visited.add((y, x, time_remaining - 1))
                add_cheats_from(start, (y, x), time_remaining - 1, visited)

    for p in distances.keys():
        add_cheats_from(p, p, max_cheat_time, set((p[0], p[1], max_cheat_time)))
    return len(cheats)


if __name__ == "__main__":
    print(solve_p1("sample.txt", 1))
    print(solve_p1("input.txt", 100))

    print(solve_p2("sample.txt", 50))
    print(solve_p2("input.txt", 100))