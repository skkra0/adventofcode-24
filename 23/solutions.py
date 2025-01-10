from collections import defaultdict, deque
def solve(fname):
    connections = defaultdict(set)
    with open(fname) as f:
        for line in f.readlines():
            a, b = line.strip().split("-")
            connections[a].add(b)
            connections[b].add(a)

    ct = 0
    for c in connections:
        if c[0] != "t":
            continue

        links = list(connections[c])
        for i in range(len(links)):
            for j in range(i + 1, len(links)):
                if links[j] in connections[links[i]]:
                    ct += 1
                    # print(f"{c} {links[i]} {links[j]}")
            connections[c].remove(links[i])
            connections[links[i]].remove(c)
    return ct

def solve_p2(fname):
    computers = defaultdict(set)
    with open(fname) as f:
        for line in f.readlines():
            a, b = line.strip().split("-")
            computers[a].add(b)
            computers[b].add(a)
    
    def is_connected_to_party(computer, party):
        for p in party:
            if computer not in computers[p]:
                return False
        return True
    
    largest_party = set()
    for cm in computers:
        de = deque()
        de.append((cm, set()))
        while de:
            computer, party = de.popleft()
            if is_connected_to_party(computer, party):
                party.add(computer)
                for link in computers[computer]:
                    de.append((link, party))
            else:
                if len(party) > len(largest_party):
                    largest_party = party

    largest_party = list(largest_party)
    largest_party.sort()
    return ",".join(largest_party)

def solve_p2_kb(fname):
    computers = defaultdict(set)
    with open(fname) as f:
        for line in f.readlines():
            a, b = line.strip().split("-")
            computers[a].add(b)
            computers[b].add(a)
    
    def get_largest_party(largest_party, party, candidates, exclude):
        if not candidates and not exclude:
            if len(party) > len(largest_party):
                largest_party.clear()
                largest_party.update(party)
            return
        
        while candidates:
            c = candidates.pop()
            get_largest_party(largest_party, party | {c}, candidates & computers[c], exclude & computers[c])
            exclude.add(c)
    
    largest_party = set()
    get_largest_party(largest_party, set(), set(computers.keys()), set())
    return ",".join(sorted(largest_party))

if __name__ == "__main__":
    print(solve("sample.txt"))
    print(solve("input.txt"))

    print(solve_p2("sample.txt"))
    print(solve_p2("input.txt"))
    
    print(solve_p2_kb("sample.txt"))
    print(solve_p2_kb("input.txt"))
