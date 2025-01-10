import re

def solve(eqs):
    total = 0
    for e in eqs:
        a1, b1, t1, a2, b2, t2 = e
        a = (t1 - b1 * t2 / b2) / (a1 - b1 * a2 / b2)
        b = (t1 - a1 * a) / b1
        a = round(a)
        b = round(b)
        if a1 * a + b1 * b == t1 and a2 * a + b2 * b == t2:
            total += 3 * a + b
    return int(total)
            
def solve_p2(eqs):
    total = 0
    for e in eqs:
        a1, b1, t1, a2, b2, t2 = e
        t1 += 10000000000000
        t2 += 10000000000000
        a = (t1 - b1 * t2 / b2) / (a1 - b1 * a2 / b2)
        b = (t1 - a1 * a) / b1
        a = round(a)
        b = round(b)
        if a1 * a + b1 * b == t1 and a2 * a + b2 * b == t2:
            total += 3 * a + b
    return int(total)
if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
        eqs = []
        for i in range(0, len(lines), 4):
            line_a = lines[i]
            line_b = lines[i + 1]
            targets = lines[i + 2]
            
            s = re.search(r"X\+([0-9]+), Y\+([0-9]+)", line_a)
            a1 = int(s.group(1))
            a2 = int(s.group(2))

            s = re.search(r"X\+([0-9]+), Y\+([0-9]+)", line_b)
            b1 = int(s.group(1))
            b2 = int(s.group(2))

            s = re.search(r"X=([0-9]+), Y=([0-9]+)", targets)
            t1 = int(s.group(1))
            t2 = int(s.group(2))
            
            eqs.append((a1, b1, t1, a2, b2, t2))
    
    print(solve(eqs))
    print(solve_p2(eqs))