def solve_p1(a, b, c, program):
    output = []
    def get_combo_operand(o):
        if o <= 3:
            return o
        elif o == 4:
            return a
        elif o == 5:
            return b
        elif o == 6:
            return c
        return -1
    
    i = 0
    while i < len(program):
        if program[i] == 0:
            denominator = 2 ** get_combo_operand(program[i + 1])
            a = a // denominator
        elif program[i] == 1:
            b ^= program[i + 1]
        elif program[i] == 2:
            b = get_combo_operand(program[i + 1]) % 8
        elif program[i] == 3:
            if a != 0:
                i = program[i + 1]
                continue
        elif program[i] == 4:
            b ^= c
        elif program[i] == 5:
            output.append(get_combo_operand(program[i + 1]) % 8)
        elif program[i] == 6:
            denominator = 2 ** get_combo_operand(program[i + 1])
            b = a // denominator
        elif program[i] == 7:
            denominator = 2 ** get_combo_operand(program[i + 1])
            c = a // denominator
        i += 2
    return output

def solve_p2(b, c, program):
    a = 0
    for i in range(len(program) - 1, -1, -1):
        a <<= 3
        while solve_p1(a, b, c, program) != program[i:]:
            a += 1
    return a

if __name__ == "__main__":
    a = 0
    b = 0
    c = 0
    program = []
    with open("input.txt") as f:
        a = int(f.readline().strip().split()[2])
        b = int(f.readline().strip().split()[2])
        c = int(f.readline().strip().split()[2])
        f.readline()

        p = f.readline().split(" ")[1]
        program = [int(c) for c in p.strip().split(",")]
    print(",".join([str(n) for n in solve_p1(a, b, c, program)]))
    print(solve_p2(b, c, program))