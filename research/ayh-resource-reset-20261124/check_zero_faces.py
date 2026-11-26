"""Replay the 515 all-rule trace and census all monotone maps on the Boolean square."""
from itertools import product

RULES = dict(z.split(":") for z in
             "ad:d bd:gd ae:ea af:eb ag:fa be:fb bf:ga bg:gb ce:cb cf:caa cg:cab".split())


def binary_word(x):
    return "c" + bin(x)[3:].translate(str.maketrans("01", "ab")) + "d"


def numeric_value(word):
    n = 1
    for ch in word[1:-1]:
        if ch in "ab":
            n = 2 * n + "ab".index(ch)
        else:
            n = 3 * n + "efg".index(ch)
    return n


def replay(n, end):
    w = binary_word(n)
    used = set()
    steps = 0
    dynamics = 0
    while w != binary_word(end):
        if steps > 1000 or w == "cd":
            raise RuntimeError("Target not reached on the stipulated finite replay")
        i = next(i for i in range(len(w)-1) if w[i:i+2] in RULES)
        lhs = w[i:i+2]
        if lhs in ("ad", "bd"):
            dynamics += 1
            n = n//2 if n%2 == 0 else (3*n+1)//2
        w = w[:i] + RULES[lhs] + w[i+2:]
        if numeric_value(w) != n:
            raise RuntimeError("Incorrect rule or decoded trajectory")
        used.add(lhs)
        steps += 1
    if used != RULES.keys():
        raise RuntimeError("The witness misses at least one rule")
    return steps, dynamics


def included(a, b):
    return a & b == a


def support_census():
    count = 0
    max_preperiod = 0
    cycles = set()
    for f in product(range(4), repeat=4):
        if not all(not included(i,j) or included(f[i],f[j]) for i in range(4) for j in range(4)):
            continue
        count += 1
        for start in range(4):
            path = []
            x = start
            while x not in path:
                path.append(x)
                x = f[x]
            k = path.index(x)
            max_preperiod = max(max_preperiod, k)
            cycles.add(frozenset(path[k:]))
    if count != 36 or max_preperiod > 3 or {c for c in cycles if len(c)>1} != {frozenset({1,2})}:
        raise RuntimeError("The Boolean-support classification failed")
    return count, max_preperiod


if __name__ == "__main__":
    for start,end,depth,gain,wanted in [
        (515,2051,7,2,(308,52)), (259,2051,6,3,(306,51)),
        (1042601,8906921,0,4,(150,8))]:
        w = binary_word(start)
        matches = [j for j in range(1,len(w)) if w[j:j+depth] == "a"*depth
                   and w[:j] + "a"*gain + w[j:] == binary_word(end)]
        if not matches or replay(start,end) != wanted:
            raise RuntimeError("Incorrect zero insertion or trace length")
        print(f"{start} -> {end}: {wanted[0]} rewrites, {wanted[1]} shortcut steps, all eleven rules")
    print("Support census (number of maps, maximum transient):", support_census())
