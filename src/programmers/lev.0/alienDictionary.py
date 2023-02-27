

#외계어 사전


from itertools import permutations

def solution(spell, dic):
    for p in permutations(spell, len(spell)):
        if "".join(p) in dic:
            return 1

    return 2


def solution2(spell, dic):
    spell.sort()

    for d in dic:
        if spell == sorted(d):
            return 1

    return 2


