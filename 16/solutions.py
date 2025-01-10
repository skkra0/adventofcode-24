from heapq import heapify, heappush, heappop
def get_distances_p1(maze, start_y, start_x, start_dir):
    # cost of the best path
    directions = ((1, 0), (-1, 0), (0, -1), (0, 1))
    distances = { (start_y, start_x, start_dir): 0 }
    pq = [(0, start_y, start_x, start_dir)]
    heapify(pq)

    while pq:
        current_dist, y, x, current_dir = heappop(pq)

        if current_dist > distances[(y, x, current_dir)]:
            continue
        for dir in directions:
            new_y, new_x = y + dir[0], x + dir[1]
            if not (0 <= new_y < len(maze) and 0 <= new_x < len(maze[0])) or maze[new_y][new_x] == "#":
                continue

            new_dist = current_dist
            if dir == current_dir:
                new_dist += 1
            else:
                # turning left or right
                new_dist += 1001
            position = (new_y, new_x, dir)
            if position not in distances or new_dist < distances[position]:
                distances[position] = new_dist
            
            heappush(pq, (new_dist, new_y, new_x, dir))
    return distances

def add_shortest_paths(y, x, dir, distances, found):
    for new_dir in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        new_y = y - dir[0]
        new_x = x - dir[1]
        if (new_y, new_x, new_dir) not in distances:
            continue
        expected_cost = 1 if dir == new_dir else 1001
        cost = distances[(y, x, dir)] - distances[(new_y, new_x, new_dir)]
        if expected_cost == cost:
            found.add((new_y, new_x))
            add_shortest_paths(new_y, new_x, new_dir, distances, found)


if __name__ == "__main__":
    maze = []
    start_y = 0
    start_x = 0
    target = ()
    start_dir = (0, 1)
    with open("input.txt") as f:
        ct = 0
        for l in f.readlines():
            l = l.strip()
            line = []
            for i in range(len(l)):
                line.append(l[i])
                if l[i] == "S":
                    start_y = ct
                    start_x = i
                elif l[i] == "E":
                    target = (ct, i)
            maze.append(line)
            ct += 1
    distances = get_distances_p1(maze, start_y, start_x, start_dir)
    target_distances = {}
    for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if (target[0], target[1], d) in distances:
            target_distances[d] = distances[(target[0], target[1], d)]
    min_distance = min(target_distances.values())
    target_distances = {k: v for k, v in target_distances.items() if v == min_distance}
    print(target_distances)
    
    found = set()
    for d in target_distances:
        add_shortest_paths(target[0], target[1], d, distances, found)
    print(1 + len(found))