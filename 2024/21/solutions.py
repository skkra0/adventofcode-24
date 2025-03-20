from functools import lru_cache
from collections import deque
def count_shortest_strokes(sequence, mid_robots):
    numpad = (
        ("7", "8", "9"),
        ("4", "5", "6"),
        ("1", "2", "3"),
        ("", "0", "A")
    )
    directions = {
        (-1, 0): "^",
        (1, 0): "v",
        (0, 1): ">",
        (0, -1): "<"
    }
    keypad = (
        ("", "^", "A"),
        ("<", "v", ">")
    )

    numpad_start = (3, 2)
    keypad_start = (0, 2)

    @lru_cache
    def get_paths(code, start, pad):
        position = start
        paths = []
        for char in code:
            found = []
            de = deque()
            de.append((position[0], position[1], "", set((position))))
            while de:
                y, x, keystrokes, visited = de.popleft()
                if found and len(keystrokes) > len(found[0]):
                    break
                if pad[y][x] == char:
                    found.append(keystrokes + "A")
                    position = (y, x)
                    continue

                for dir in directions.keys():
                    new_y, new_x = y + dir[0], x + dir[1]
                    if (
                        (new_y, new_x) not in visited and
                        0 <= new_y < len(pad) and
                        0 <= new_x < len(pad[0]) and 
                        pad[new_y][new_x]
                        ):
                        new_visited = visited.copy()
                        new_visited.add((new_y, new_x))
                        de.append((new_y, new_x, keystrokes + directions[dir], new_visited))
            paths.append(found)
        return paths
    
    @lru_cache
    def get_expanded_length(paths, mid_robots):
        if mid_robots == 0:
            return len(paths[0])

        min_length = None
        for path in paths:
            total = 0
            expanded_path = get_paths(path, keypad_start, keypad)
            for ep in expanded_path:
                total += get_expanded_length(tuple(ep), mid_robots - 1)
            if not min_length or total < min_length:
                min_length = total
        return min_length
    
    ct = 0
    paths = get_paths(sequence, numpad_start, numpad)
    for p in paths:
        ct += get_expanded_length(tuple(p), mid_robots)

    return ct

def solve(fname, mid_robots):
    with open(fname) as f:
        sequences = []
        for line in f.readlines():
            sequences.append(line.strip())
    
    sum = 0
    for seq in sequences:
        c = count_shortest_strokes(seq, mid_robots)
        sum += c * int(seq[:-1])
    print(sum)
if __name__ == "__main__":
    solve("sample.txt", 2)
    solve("input.txt", 2)
    solve("sample.txt", 25)
    solve("input.txt", 25)