import os
import pathlib

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split('\n')
def parse_wires():
    global txt
    wires = {}
    while txt[0] != '':
        wire, val = txt[0].split()
        wires[wire[:len(wire) - 1]] = int(val)
        txt = txt[1:]
    txt = txt[1:]
    return wires

def parse_gates():
    gates = []
    for row in txt:
        row = row.split()
        row.pop(3)
        gates.append(row)
    return gates

def solution():
    wires = parse_wires()
    gates = parse_gates()
    z_bits = []

    while gates:
        for i, gate in enumerate(gates):
            if gate[0] in wires and gate[2] in wires:
                val = None
                match gate[1]:
                    case 'AND':
                        val = wires[gate[0]] & wires[gate[2]]
                    case 'OR':
                        val = wires[gate[0]] | wires[gate[2]]
                    case 'XOR':
                        val = wires[gate[0]] ^ wires[gate[2]]
                wires[gate[3]] = val
                gates.pop(i)

    for wire in wires:
        if wire[0] == 'z':
            z_bits.append((int(wire[1:]), str(wires[wire])))
    z_bits = sorted(z_bits, key=lambda x: x[0])
    z_bits = list(map(lambda x: x[1], z_bits))
    z_bits = z_bits[::-1]
    return int(''.join(z_bits), 2)

print(solution())