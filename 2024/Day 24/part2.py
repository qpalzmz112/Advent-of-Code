import os
import pathlib
from collections import defaultdict

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()

input_wires, gates = txt.split('\n\n')
input_wires = input_wires.split('\n')
gates = gates.split('\n')

def parse_input_wires():
    wires = {}
    for row in input_wires:
        wire, val = row.split()
        wire = wire[:len(wire) - 1]
        val = int(val)
        wires[wire] = val
    return wires

def resolve_wire(wire, gate_wires, z_dict, z_num):
    op1 = gate_wires[wire][0]
    op2 = gate_wires[wire][2]

    if op1[0] in ('x', 'y') and op2[0] in ('x', 'y'):
        if int(op1[1:]) == int(z_num):
            z_dict[f"z{z_num}"]["main bits"] = gate_wires[wire]
        else:
            return gate_wires[wire]
    else:
        l = resolve_wire(op1, gate_wires, z_dict, z_num)
        r = resolve_wire(op2, gate_wires, z_dict, z_num)
        if l is None or r is None:
            z_dict[f"z{z_num}"]["carry bit"] = (l if r is None else r)
            z_dict[f"z{z_num}"]["main/carry bit op"] = gate_wires[wire][1]
        return (l, gate_wires[wire][1], r)


def parse_gates():
    gate_wires = {}
    for gate in gates:
        in1, op, in2, _, out = gate.split()
        gate_wires[out] = (in1, op, in2)

    z_dict = defaultdict(dict)
    for i in range(45):
        wire = f"z{i}" if i >= 10 else f"z0{i}"
        resolve_wire(wire, gate_wires, z_dict, wire[1:])

    for key in z_dict:
        print(key, z_dict[key], '\n')
    return gate_wires

def main_op_is_valid(z, z_dict):
    # check if z_i = (x_i XOR y_i) XOR carry_bit
    x = f"x{z[1:]}"
    y = f"y{z[1:]}"

    for i in [0, 2]:
        #if z_dict[z]["main bits"][i]
        pass


# idea: for each z, have a set of the tmp wires that contribute to it
# need a function to validate a z based on its gates in the z dict
# then, starting at z00, if z_i is valid, remove its contributing tmp wires from later zs' dicts of contributing wires
# when we reach a z_i that is invalid, try all swaps of its contributing wires that weren't already ruled out by switching keys in gate_wires, and then
    # re-running the code that makes the z dict until z_i is valid - then, the wires that were swapped can be added to a result s et

# assumptions: only tmp wires are swapped, and tmp wires are only swapped for the same z_i (these seem to be true based on a couple tests)
# also, at most one pair of tmp wires is swapped per z_i (haven't tested this, just hope it's true)

parse_gates()