def solve_p1(fn):
    start = 0
    end = len(fn) - 1
    while True:
        while start < len(fn) and fn[start] != -1:
            start += 1

        while end >= 0 and fn[end] == -1:
            end -= 1
        if start >= end:
            break
            
        fn[start] = fn[end]
        end -= 1
        start += 1

    fn = fn[:end + 1]
    total = 0
    for i in range(len(fn)):
        if fn[i] == -1: break
        total += i * fn[i]
    return total

if __name__ == "__main__":
    fn = []
    with open("input.txt") as f:
        line = f.readline()
        for i in range(len(line)):
            if i % 2 == 0:
                for _ in range(int(line[i])): fn.append(i // 2)
                continue
            if i == len(line) - 1: break
            for _ in range(int(line[i])): fn.append(-1)
    print(solve_p1(fn))