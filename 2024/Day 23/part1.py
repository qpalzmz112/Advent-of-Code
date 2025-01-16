import os
import pathlib
from collections import defaultdict

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split()
txt = list(map(lambda s: s.split('-'), txt))

def parse_connections():
    conns = defaultdict(set)
    for row in txt:
        l, r = row
        conns[l].add(r)
        conns[r].add(l)
    return conns

def get_3_cycles():
    conns = parse_connections()
    res = set()
    done = set()
    for host in conns:
        for l, r in txt:
            if l not in done and r not in done and l in conns[host] and r in conns[host]:
                res.add((host, l, r))
        done.add(host)
    return res

def narrow_down():
    sets = get_3_cycles()
    res = []
    for s in sets:
        for host in s:
            if host[0] == 't':
                res.append(s)
                break
    return res

print(len(narrow_down()))