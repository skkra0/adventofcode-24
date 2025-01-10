directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
def get_ap(y, x, ptype, regions, visited):
    if (y, x) in visited:
        return (0, 0)
    visited.add((y, x))
    area = 1
    perimeter = 0
    for d in directions:
        new_y = y + d[0]
        new_x = x + d[1]
        if not (0 <= new_y < len(regions) and 0 <= new_x < len(regions[0])) or regions[new_y][new_x] != ptype:
            perimeter += 1
        else:
            a, p = get_ap(new_y, new_x, ptype, regions, visited)
            area += a
            perimeter += p
    return area, perimeter
    
def solve_p1(lines):
    plants = []
    visited = set()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
                if (i, j) not in visited:
                    plants.append(get_ap(i, j, lines[i][j], lines, visited))
        
    price = 0
    for p in plants:
        price += p[0] * p[1]
    return price

def add_edges(edges, y, x, ptype, regions, visited):
    if (y, x) in visited:
        return 0
    visited.add((y, x))
    area = 1
    for i in range(len(directions)):
        new_y = y + directions[i][0]
        new_x = x + directions[i][1]
        if not (0 <= new_y < len(regions) and 0 <= new_x < len(regions[0])) or regions[new_y][new_x] != ptype:
            edges[i].append((y, x))
        else:
            area += add_edges(edges, new_y, new_x, ptype, regions, visited)
    return area

def get_sides(edges):
    sides = 4
    for i in range(2):
        e = edges[i]
        e.sort(key=lambda p:(p[0], p[1]))
        for k in range(1, len(e)):
            if e[k][0] != e[k - 1][0] or e[k][1] - e[k - 1][1] != 1:
                sides += 1

    for i in range(2, 4):
        e = edges[i]
        e.sort(key=lambda p:(p[1], p[0]))
        for k in range(1, len(e)):
            if e[k][1] != e[k - 1][1] or e[k][0] - e[k - 1][0] != 1:
                sides += 1
    return sides

def solve_p2(lines):
    total = 0
    visited = set()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if (i, j) not in visited:
                edges = ([], [], [], [])
                area = add_edges(edges, i, j, lines[i][j], lines, visited)
                sides = get_sides(edges)
                total += area * sides

    return total
                
                    

if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        for l in f.readlines():
            lines.append([c for c in l.rstrip()])

    print(solve_p1(lines))
    print(solve_p2(lines))