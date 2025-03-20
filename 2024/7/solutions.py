lines = []
with open("input.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        l = line.split(':')
        lines.append((int(l[0]), list(map(int, l[1].split()))))

def test_line_p1(line_num, start, index=1):
    if start > lines[line_num][0]:
        return False
    
    if index == len(lines[line_num][1]):
        return start == lines[line_num][0]
    
    return test_line_p1(line_num, start + values[index], index + 1) or test_line_p1(line_num, start * values[index], index + 1)

def test_line_p2(line_num, start, index=1):
    if start > lines[line_num][0]:
        return False
    
    if index == len(lines[line_num][1]):
        return start == lines[line_num][0]
    
    return test_line_p2(line_num, start + values[index], index + 1) or test_line_p2(line_num, start * values[index], index + 1) or test_line_p2(line_num, int(str(start) + str(values[index])), index + 1)


if __name__ == '__main__':
    total_p1 = 0
    for i in range(len(lines)):
        target, values = lines[i]
        if test_line_p1(i, values[0]):
            total_p1 += target

    print(total_p1)

    total_p2 = 0
    for i in range(len(lines)):
        target, values = lines[i]
        if test_line_p2(i, values[0]):
            total_p2 += target

    print(total_p2)