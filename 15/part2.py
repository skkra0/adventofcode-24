def move(y, x, dir, wh, peek=False):    
    new_y = y + dir[0]
    new_x = x + dir[1]

    if not (0 <= new_y < len(wh) and 0 <= new_x < len(wh[0])) or wh[new_y][new_x] == "#":
        return False
    
    if wh[new_y][new_x] == ".":
        if not peek:
            wh[new_y][new_x] = wh[y][x]
            wh[y][x] = "."
        return True

    if dir[0] != 0:
        result: bool
        if wh[new_y][new_x] == "[":
            result = move(new_y, new_x, dir, wh, peek) and move(new_y, new_x + 1, dir, wh, peek)
        else: # wh[new_y][new_x] == "]"
            result = move(new_y, new_x - 1, dir, wh, peek) and move(new_y, new_x, dir, wh, peek)
        
        if result:
            if not peek:
                wh[new_y][new_x] = wh[y][x]
                wh[y][x] = "."
            return True
        
        return result
    elif move(new_y, new_x, dir, wh, peek):
        # push the box horizontally as usual
        if not peek:
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
                if l[i] == "@":
                    position = (ct, i * 2)
                    line.append("@")
                    line.append(".")
                elif l[i] == "O":
                    line.append("[")
                    line.append("]")
                else:
                    line.append(l[i])
                    line.append(l[i])
            wh.append(line)
            ct += 1

        for l in f.readlines():
            robot_moves += l.strip()
    
    for m in robot_moves:
        dir = directions[m]
        if dir[0] != 0:
            if move(position[0], position[1], dir, wh, True):
                move(position[0], position[1], dir, wh)
                position = (position[0] + dir[0], position[1] + dir[1])
        else:
            if move(position[0], position[1], dir, wh):
                position = (position[0] + dir[0], position[1] + dir[1])

    total = 0
    for i in range(len(wh)):
        for j in range(len(wh[0])):
            if wh[i][j] == "[":
                total += 100 * i + j
    print(total)