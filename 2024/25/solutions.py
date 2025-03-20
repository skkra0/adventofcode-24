def solve(fname):
    locks = []
    keys = []
    with open(fname) as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            schem = [0, 0, 0, 0, 0]
            for j in range(i + 1, i + 6):
                for k in range(len(lines[j])):
                    if lines[j][k] == "#":
                        schem[k] += 1
            
            if lines[i][0] == "#":
                locks.append(schem)
            else:
                keys.append(schem)
            i += 8
    
    def lock_fits_key(lock, key):
        for i in range(5):
            if lock[i] + key[i] >= 6:
                return False
        return True

    ct = 0
    for lock in locks:
        for key in keys:
            if lock_fits_key(lock, key):
                ct += 1
                    
    return ct

if __name__ == "__main__":
    print(solve("sample.txt"))
    print(solve("input.txt"))