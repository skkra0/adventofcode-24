from functools import lru_cache
def solve_p1(patterns, targets):
    @lru_cache
    def test_design(target):
        if target == "":
            return True

        result = False
        for p in patterns:
            if target.startswith(p):
                result = test_design(target[len(p):])
                if result:
                    break
        return result
    
    ct = 0
    for t in targets:
        if test_design(t):
            ct += 1
    return ct

def solve_p2(patterns, targets):
    ct = 0

    @lru_cache
    def count(target):
        if target == "":
            return 1

        result = 0
        for p in patterns:
            if target.startswith(p):
                result += count(target[len(p):])
        return result
    
    for t in targets:
        ct += count(t)
    return ct

if __name__ == "__main__":
    targets = []
    with open("input.txt") as f:
        patterns = set(f.readline().strip().split(", "))
        f.readline()

        for l in f.readlines():
            targets.append(l.strip())
    print(solve_p1(patterns, targets))
    print(solve_p2(patterns, targets))