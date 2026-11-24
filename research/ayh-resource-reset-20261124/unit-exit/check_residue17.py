"""Exact local-word and pressure certificate for ternary-unit residue 17 mod 48."""
from hashlib import sha256

EXPONENTS = (2, 4, 5)
OFFSETS = (-1, 3, 3)
WEIGHTS = (3388, 3659, 3802)
BASE = 10_000
WIDTH = 9


def ordinary_survives(x, h):
    a, b, p, q = x, 3*x, 0, 1
    for j in range(h + 1):
        if (a, p) == (b, q):
            return False
        if j < h:
            s, t = a % 2, b % 2
            a, b = (a*(1 + 2*s) + s)//2, (b*(1 + 2*t) + t)//2
            p, q = p+s, q+t
    return True


def rational_survives(p, d, h):
    left, right, gap = p, 3*p, -1
    for j in range(h + 1):
        if left == right and gap == 0:
            return False
        if j < h:
            s, t = left % 2, right % 2
            gap += s - t
            left = (3*left+d)//2 if s else left//2
            right = (3*right+d)//2 if t else right//2
    return True


def dictionary():
    rational = set()
    stack = [(0, 0, 1, 1, 4)]
    while stack:
        length, word, p, d, h = stack.pop()
        if not rational_survives(p, d, h):
            continue
        if length == WIDTH:
            rational.add(word)
        else:
            for c,(e,b) in enumerate(zip(EXPONENTS,OFFSETS)):
                stack.append((length+1,3*word+c,(p<<e)+b*d,3*d,h+e))

    ordinary = {0:(1,4)}
    for _ in range(WIDTH):
        following = {}
        for word,(r,h) in ordinary.items():
            for c,(e,b) in enumerate(zip(EXPONENTS,OFFSETS)):
                hh = h+e
                modulus = 1 << hh
                rr = ((r<<e)+b)*pow(3,-1,modulus) % modulus
                if ordinary_survives(rr,hh):
                    following[3*word+c] = (rr,hh)
        ordinary = following
    if rational != set(ordinary) or len(rational) != 12969:
        raise RuntimeError("dictionary disagreement")
    return rational


def main():
    rows = dictionary()
    if any(3**19 * w**18 <= BASE**18 * 2**e for w,e in zip(WEIGHTS,EXPONENTS)):
        raise RuntimeError("weight must strictly dominate the one-digit cost")
    if any(3**3799 * w**3599 <= BASE**3599 * 2**(200*e)
           for w,e in zip(WEIGHTS,EXPONENTS)):
        raise RuntimeError("explicit 200/3599 one-digit cost too large")
    out = {v:tuple((c,(3*v+c) % 3**WIDTH) for c in range(3)
                   if (3*v+c) % 3**WIDTH in rows) for v in rows}
    scores = {v:1 for v in rows}
    for _ in range(34):
        scores = {v:sum(WEIGHTS[c]*scores[z] for c,z in children)
                  for v,children in out.items()}
    score = max(scores.values())
    if score >= BASE**34:
        raise RuntimeError("pressure bound failed")
    walks = {v:1 for v in rows}
    for _ in range(96):
        walks = {v:sum(walks[z] for c,z in ch) for v,ch in out.items()}
    top = max(walks.values())
    if top**100 >= 3**(96*93):
        raise RuntimeError("strict source power bound failed")
    print("width",WIDTH,"vertices",len(rows),"edges",sum(map(len,out.values())))
    print("vertices_sha256",sha256(b''.join(v.to_bytes(2,'big') for v in sorted(rows))).hexdigest())
    print("maximum_34_step_weighted_row",score)
    print("maximum_96_step_count",top)
    print("strict_weight_and_pressure_certificates_passed",True)
    print("pressure_exponent", "200/3599")


if __name__ == "__main__":
    main()
