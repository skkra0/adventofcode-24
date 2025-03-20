from collections import deque, defaultdict
def get_next(n):
    n = (n ^ (n * 64)) % 16777216
    n = (n ^ (n // 32)) % 16777216
    n = (n ^ (n * 2048)) % 16777216
    return n

def solve(fname):
    numbers = []
    with open(fname) as f:
        for line in f.readlines():
            numbers.append(int(line.strip()))

    total = 0
    for n in numbers:
        for _ in range(2000):
            n = get_next(n)
        total += n
    print(total)

def solve_p2(fname):
    numbers = []
    with open(fname) as f:
        for line in f.readlines():
            numbers.append(int(line.strip()))

    total_results = defaultdict(int)
    for n in numbers:
        results = {}
        sequence = deque()
        last = n
        for _ in range(4):
            n = get_next(n)
            sequence.append(n % 10 - last % 10)
            last = n
        n = get_next(n)
        results[tuple(sequence)] = n % 10
        for _ in range(1995):
            sequence.popleft()
            sequence.append(n % 10 - last % 10)
            if tuple(sequence) not in results:
                results[tuple(sequence)] = n % 10
            last = n
            n = get_next(n)
        for seq in results.keys():
            total_results[seq] += results[seq]

    print(max(total_results.values()))
if __name__ == "__main__":
    solve("sample.txt")
    solve("input.txt")
    solve_p2("sample2.txt")
    solve_p2("input.txt")