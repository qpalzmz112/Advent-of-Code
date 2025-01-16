import os
import pathlib

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split('\n')
registers = {}
program = None
for row in txt:
    if row == '':
        continue

    row = row.split()
    if row[0][0] == 'R':
        register = row[1][:len(row[1]) - 1]
        num = int(row[2])
        registers[register] = num
    else:
        program = list(map(int, row[1].split(',')))

### OPCODES
# 0: division: combo operand - reg(A) := reg(A) // 2^(operand)
# 1: bitwise XOR: literal operand - reg(B) := reg(B) ^ (operand)
# 2: combo operand - reg(B) := (operand) % 8
# 3: literal operand - if reg(A) == 0: pass; else: i_ptr := (operand)
# 4: reg(B) := reg(B) ^ reg(C)
# 5: combo operand - output += (operand) % 8
# 6: 0 but value is put in reg(B)
# 7: 0 but value is put in reg(C)

### COMBO OPERANDS
# 0-3: 0-3
# 4: reg(A)
# 5: reg(B)
# 6: reg(C)
# 7: invalid

def combo(operand):
    if operand <= 3:
        return operand
    return registers[chr(ord('A') + operand - 4)]

def solution():
    output = []
    i_ptr = 0
    while i_ptr < len(program):
        operator = program[i_ptr]
        operand = program[i_ptr + 1]
        i_ptr += 2

        match operator:
            case 1:
                registers['B'] = registers['B'] ^ operand
            case 2:
                registers['B'] = combo(operand) % 8
            case 3:
                if registers['A'] == 0:
                    continue
                else:
                    i_ptr -= 2
                    i_ptr = operand
            case 4:
                registers['B'] = registers['B'] ^ registers['C']
            case 5:
                output.append(str(combo(operand) % 8))
            case _:
                match operator:
                    case 0:
                        register = 'A'
                    case 6:
                        register = 'B'
                    case 7:
                        register = 'C'
                num = registers['A']
                denom = pow(2, combo(operand))
                registers[register] = num // denom

    return ','.join(output)

print(solution())