def solve_p2(fn, fs):
    for i in range(len(fn) - 1, 0, -1):
        j = 0
        while j < i and fs[j][0] < len(fn[i]):
            j += 1
        if j == i:
            continue

        fill_length = len(fn[i])
        fs[j][1].extend(fn[i])
        fs[j][0] -= fill_length
        fn[i] = []

        if i < len(fn) - 1:
            fs[i - 1][0] += fill_length

    result = []
    for j in range(len(fn) - 1):
        result += fn[j]
        result += fs[j][1] + [0 for _ in range(fs[j][0])]

    result += fn[len(fn) - 1]

    total = 0
    for i in range(len(result)):
        total += i * result[i]
    print(total)
    
if __name__ == "__main__":
    fn = []
    fs = []
    with open("input.txt") as f:
        line = f.readline()
        for i in range(len(line)):
            if i % 2 == 0:
                fn.append([i // 2 for _ in range(int(line[i]))])
                continue
            if i == len(line) - 1:
                break
            fs.append([int(line[i]), []])

    solve_p2(fn, fs)