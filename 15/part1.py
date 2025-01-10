def move(y, x, dir, wh):    
    new_y = y + dir[0]
    new_x = x + dir[1]
    if not (0 <= new_y < len(wh) and 0 <= new_x < len(wh[0])) or wh[new_y][new_x] == "#":
        return False
    elif wh[new_y][new_x] == "." or move(new_y, new_x, dir, wh):
        wh[new_y][new_x] = wh[y][x]
        wh[y][x] = "."
        return True

    return False

if __name__ == "__main__":
    directions = {
        "<": (0,-1),
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0)
    }

    wh = []
    robot_moves = ""
    position = (0, 0)
    with open("input.txt") as f:
        ct = 0
        while True:
            l = f.readline()[:-1]
            if not l: 
                break
            line = []
            for i in range(len(l)):
                line.append(l[i])
                if l[i] == "@":
                    position = (ct, i)

            wh.append(line)
            ct += 1
        for l in f.readlines():
            robot_moves += l.strip()
    
    for m in robot_moves:
        dir = directions[m]
        if move(position[0], position[1], dir, wh):
            position = (position[0] + dir[0], position[1] + dir[1])

    total = 0
    for i in range(len(wh)):
        for j in range(len(wh[0])):
            if wh[i][j] == "O":
                total += 100 * i + j
    print(total)