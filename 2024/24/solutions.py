import re
def solve(fname):
    wires = {}
    gates = []
    with open(fname) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            s = re.search(r"(...): (\d)", line)
            wires[s.group(1)] = int(s.group(2))
    
        for line in f.readlines():
            s = re.search(r"(...) (..+) (...) -> (...)", line)
            gates.append( (s.group(1), s.group(2), s.group(3), s.group(4)) )
    while gates:
        for g in gates[:]:
            x, op, y, out = g
            if x in wires and y in wires:
                match op:
                    case "AND":
                        wires[out] = wires[x] & wires[y]
                    case "OR":
                        wires[out] = wires[x] | wires[y]
                    case "XOR":
                        wires[out] = wires[x] ^ wires[y]
                gates.remove(g)
    
    num = 0
    for w in wires:
        if w[0] != "z":
            continue
        num += wires[w] << int(w[1:])
    return num

def create_dotfile(fname, out):
    gates = []
    with open(fname) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
        for line in f.readlines():
            s = re.search(r"(...) (..+) (...) -> (...)", line)
            gates.append( (s.group(1), s.group(2), s.group(3), s.group(4)) )
    with open(out, "w") as o:
        o.write("digraph G {\n")
        for i in range(len(gates)):
            a, op, b, result = gates[i]
            o.write(f"{a} -> {op}{i}\n")
            o.write(f"{b} -> {op}{i}\n")
            o.write(f"{op}{i} -> {result}\n")
        o.write("}")

if __name__ == "__main__":
    print(solve("sample.txt"))
    print(solve("sample2.txt"))
    print(solve("input.txt"))
    
    create_dotfile("input.txt", "out.dot")
    # refer to graphviz graph
    
    # modified input file after noticing some swaps through graphviz
    num = bin(solve("input copy.txt"))[2:]
    for i in range(len(num)):
        if num[len(num) - i - 1] != '1':
            print(i)