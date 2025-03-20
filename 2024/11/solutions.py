from functools import lru_cache
from collections import defaultdict
@lru_cache(maxsize=128)
def get_stones(x):
    if x == 0:
        return (1, None)
    elif len(str(x)) % 2 == 0:
        n = str(x)
        return (int(n[:len(n) // 2]), int(n[len(n) // 2:]))
    else:
        return (x * 2024, None)

if __name__ == "__main__":
    rocks = defaultdict(int)
    with open("input.txt") as f:
        for x in f.readline().split():
            rocks[int(x)] += 1

    for i in range(75):
        if i == 25:
            print(sum(rocks.values())) # part 1
        updated = defaultdict(int)

        for r, value in rocks.items():
            if value != 0:
                result = get_stones(r)
                updated[result[0]] += value
                if result[1] is not None:
                    updated[result[1]] += value
        rocks = updated
    print(sum(rocks.values())) # part 2