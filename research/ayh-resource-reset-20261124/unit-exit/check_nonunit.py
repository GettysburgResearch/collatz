"""Independent modular and rational-shadow reconstruction of the finite suffix filter."""
from __future__ import annotations

from hashlib import sha256

WIDTH = 22
WALK = 512
EXPECTED_ROWS = 4218
EXPECTED_MAX = 1320285513209306106119482796965456045622649209648

def merges(numerator: int, denominator: int, horizon: int) -> bool:
    """Replay the two rational starts, keeping their relative homogeneous slopes."""
    left, right = numerator, 3 * numerator
    grade_gap = -1
    for step in range(horizon + 1):
        if left == right and grade_gap == 0:
            return True
        if step == horizon:
            break
        lbits, rbits = left % 2, right % 2
        grade_gap += lbits - rbits
        left = (3 * left + denominator) // 2 if lbits else left // 2
        right = (3 * right + denominator) // 2 if rbits else right // 2
    return False

def rational_words(width: int) -> set[int]:
    leaves = set()
    # The shadow starts at 1; its rational value is positive, including where
    # the actual integer itinerary requires a different high part of the start.
    stack = [(0, 0, 1, 1, 1)]
    while stack:
        depth, mask, numerator, denominator, precision = stack.pop()
        if merges(numerator, denominator, precision):
            continue
        if depth == width:
            leaves.add(mask)
            continue
        for digit, exponent in enumerate((4, 5)):
            stack.append((depth+1, 2*mask+digit,
                          (numerator << exponent) + 3*denominator,
                          3*denominator, precision+exponent))
    return leaves

def modular_words(width: int) -> set[int]:
    # Starting with all branches of one length, remove a prefix immediately
    # if the ordinary least-residue replay produces an affine identity.
    current = {0: (1,1)}
    for _ in range(width):
        following = {}
        for mask, (residue, precision) in current.items():
            for digit, exponent in enumerate((4, 5)):
                bits = precision+exponent
                modulus = 1 << bits
                out = (1 + (residue << exponent)*pow(3, -1, modulus)) % modulus
                left, right, p, q = out, 3*out, 0, 1
                for step in range(bits+1):
                    if (left,p) == (right,q):
                        break
                    if step == bits:
                        following[2*mask+digit] = (out,bits)
                        break
                    lodd, rodd = left&1, right&1
                    p += lodd
                    q += rodd
                    left = (left*(1+2*lodd)+lodd)//2
                    right = (right*(1+2*rodd)+rodd)//2
        current = following
    return set(current)

def main():
    rational = rational_words(WIDTH)
    modular = modular_words(WIDTH)
    if rational != modular or len(rational) != EXPECTED_ROWS:
        raise RuntimeError("independent suffix reconstructions disagree")
    mask = (1 << WIDTH)-1
    desc = {v: tuple(vnext for bit in (0,1) if (vnext := (2*v+bit)&mask) in rational)
            for v in rational}
    # Row sums of the powers of the overlap graph's adjacency matrix.
    walks = {v: 1 for v in rational}
    for _ in range(WALK):
        walks = {v: sum(walks[w] for w in children) for v,children in desc.items()}
    top = max(walks.values())
    if top != EXPECTED_MAX or not top**5 < 3**WALK:
        raise RuntimeError("walk-count certificate failed")
    # Weighted pressure at sigma=2/5. These integer inequalities certify
    # 652/1000 and 860/1000 dominate (2^e/3)^sigma / 3.
    numerators = (652, 860)
    if any(w**5 * 3**7 <= 1000**5 * 2**(2*e)
           for w,e in zip(numerators,(4,5))):
        raise RuntimeError("rational weight rounding failed")
    # The same weights certify the explicit stronger exponent 2001/5000.
    # Raising w/1000 > (2^e/3)^(2001/5000)/3 to the 5000th
    # power leaves precisely this integer comparison; no floats are used.
    if any(w**5000 * 3**7001 <= 1000**5000 * 2**(2001*e)
           for w,e in zip(numerators,(4,5))):
        raise RuntimeError("explicit pressure exponent failed")
    scores = {v: 1 for v in rational}
    for _ in range(86):
        scores = {v: sum(numerators[b]*scores.get((2*v+b)&mask,0)
                         for b in (0,1)) for v in rational}
    pressure = max(scores.values())
    if pressure >= 1000**86:
        raise RuntimeError("weighted overlap graph failed to contract")
    print("weighted_86_step_maximum", pressure)
    print("weighted_row_sums_strictly_below_1000_to_86",pressure < 1000**86)
    print("certified_pressure_exponent", "2001/5000")
    h = sha256(b''.join(v.to_bytes(3,'big') for v in sorted(rational))).hexdigest()
    print("width", WIDTH, "vertices", len(rational), "edges", sum(map(len,desc.values())))
    print("sorted_3byte_vertex_sha256",h)
    print("walk_length",WALK,"maximum",top)
    print("fifth_power_strictly_below_3_to_walk_length",top**5<3**WALK)

if __name__ == '__main__':
    main()
