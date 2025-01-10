def score(last, y, x, heights, found):
    if not (0 <= y < len(heights) and 0 <= x < len(heights[0])):
        return 0

    if heights[y][x] - last != 1:
        return 0
    
    if heights[y][x] == 9 and (y, x) not in found:
        found.add((y, x))
        return 1
    
    return (
            score(heights[y][x], y - 1, x, heights, found) + 
            score(heights[y][x], y + 1, x, heights, found) + 
            score(heights[y][x], y, x - 1, heights, found) + 
            score(heights[y][x], y, x + 1, heights, found)
    )

def score_p2(last, y, x, heights, found):
    if not (0 <= y < len(heights) and 0 <= x < len(heights[0])):
        return 0

    if heights[y][x] - last != 1:
        return 0
    
    if heights[y][x] == 9:
        found.add((y, x))
        return 1
    
    return (
            score_p2(heights[y][x], y - 1, x, heights, found) + 
            score_p2(heights[y][x], y + 1, x, heights, found) + 
            score_p2(heights[y][x], y, x - 1, heights, found) + 
            score_p2(heights[y][x], y, x + 1, heights, found)
    )

if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        while True:
            l = f.readline().strip()
            if not l:
                break
            lines.append([int(c) for c in l])

    total_p1 = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 0:
                total_p1 += score(-1, i, j, lines, set())

    print(total_p1)

    total_p2 = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 0:
                total_p2 += score_p2(-1, i, j, lines, set())
    print(total_p2)