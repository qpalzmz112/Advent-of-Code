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

def solution():
    conns = parse_connections()
    cliques = list(map(set, txt))
    max_clique = {}

    clique_changed = True
    while clique_changed:
        clique_changed = False
        for host in conns:
            for clique in cliques:
                for other_host in clique:
                    if other_host not in conns[host]:
                        break
                else:
                    clique.add(host)
                    clique_changed = True
                    if len(clique) > len(max_clique):
                        max_clique = clique
    return ','.join(sorted(list(max_clique)))

print(solution())