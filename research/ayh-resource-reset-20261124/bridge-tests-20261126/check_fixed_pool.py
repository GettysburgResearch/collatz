# Exact Python extracted from FIXED_POOL.md; finite controls only.
def check(j, a, B):
    targets = [3**u * 2**(j-u) * a - 1 for u in range(j+1)]
    modulus = 3**16
    residues = {target % modulus for target in targets}
    peak, best = B, 0
    smooth = {}
    for d in range(49):
        v, u = 2**d, 0
        while v <= 2**48:
            if v > 1:
                smooth[v-1] = (u+d, u)
            v, u = 3*v, u+1
    labels = {pair for v, pair in smooth.items() if v <= B}

    def inspect(v):
        nonlocal peak, best
        peak = max(peak, v)
        if v >= 2**48:
            raise ValueError("smooth-label scan bound exceeded")
        if v in smooth:
            labels.add(smooth[v])
        if v % modulus not in residues:
            return
        for target in targets:
            d, difference = 0, abs(target-v)
            if difference == 0:
                raise ValueError("exact ordinary intersection")
            while difference % 3 == 0:
                d += 1
                difference //= 3
            best = max(best, d)

    for r in residues:
        for w in range(r or modulus, B+1, modulus):
            inspect(w)
    exits, steps, longest = 0, 0, 0
    for e in range(1, B+1, 2):
        v = (3*e+1)//2
        if v <= B:
            continue
        exits += 1
        h = 1
        while v > B:
            inspect(v)
            v = (3*v+1)//2 if v%2 else v//2
            h += 1
        steps += h
        longest = max(longest, h)
    expected = {(k, u) for k in range(1, 26) for u in range(k+1)}
    if labels != expected:
        raise ValueError("unexpected pure Mersenne ascent labels")
    return peak, best+1, exits, steps, longest, len(labels)

print(check(65, 1, 53024287))
print(check(11, 1+243*2**46, 3*2**24))
