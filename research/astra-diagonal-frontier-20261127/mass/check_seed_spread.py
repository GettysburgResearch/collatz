"""Exact residue and ordinary-source controls for tight-prefix leakage."""

import json
from itertools import product


SELECTED = tuple(tuple(map(int, s)) for s in (
    '11211134', '11212214', '11111144', '11212232', '12211142',
   '12221222', '11211242', '12121214', '11114132', '11111126',
   '12112142', '12121142', '11311214', '12111134',
))


def require(claim, message):
    if not claim:
        raise ArithmeticError(message)


def tight_words(depth, prefix=(), clock=0):
    i = len(prefix)
    if i == depth:
        if 4 * clock == 7 * depth:
            yield prefix
        return
    for e in range(1, 7 * (i + 1) // 4 - clock + 1):
        yield from tight_words(depth, prefix + (e,), clock + e)


def affine(word):
    carry = clock = 0
    for e in word:
        carry = 3 * carry + (1 << clock)
        clock += e
    return 3 ** len(word), clock, carry


def terminal_residue(word):
    modulus, clock, carry = affine(word)
    return (carry * pow(2, -clock, modulus)) % modulus


def principal(word):
    gain, clock, carry = affine(word)
    mod = 1 << (clock + 1)
    root = (pow(gain, -1, mod) * ((1 << clock) - carry)) % mod
    terminal, remainder = divmod(gain * root + carry, 1 << clock)
    require(not remainder and 0 < root < mod and terminal % 2, "principal affine pair")
    return root, terminal


def physical(word):
    root, target = principal(word)
    y = root
    for expected in word:
        raw = 3 * y + 1
        bits = (raw & -raw).bit_length() - 1
        require(bits == expected, "ordinary source exponent")
        y = raw >> bits
    require(y == target, "ordinary terminal")
    return root, target


def gap_control(residues):
    q = 3 ** 8
    worst = 0
    witness = None
    min_half = len(residues)
    for a in range(1, q):
        if a % 3 == 0:
            continue
        points = sorted(a * r % q for r in residues)
        gaps = [y - x for x, y in zip(points, points[1:] + [points[0] + q])]
        maximum = max(gaps)
        if maximum > worst:
            worst, witness = maximum, a
        # A half interval of the smaller integral length has at least this
        # many points. Its minimum is achieved immediately after a point.
        extended = points + [x + q for x in points]
        j = 0
        for i, x in enumerate(points):
            j = max(j, i + 1)
            while extended[j] <= x + q // 2:
                j += 1
            min_half = min(min_half, j - i - 1)
    return {"dilations": 4374, "residues": len(residues), "max_gap": worst,
            "witness": witness, "min_half_interval_count": min_half}


def main():
    all_prefixes = list(tight_words(8))
    require(set(SELECTED) <= set(all_prefixes), "all selected words are tight")
    records = {}
    for label, prefixes in (("all", all_prefixes), ("selected", SELECTED)):
        records[label] = gap_control(set(map(terminal_residue, prefixes)))
    require(records["all"]["max_gap"] == 2860, "all-prefix max gap")
    require(records["selected"]["max_gap"] == 2982, "selected max gap")
    physical_replay = []
    for d in (0, 4, 8):
        min_kill, max_kill = len(SELECTED), 0
        count = 0
        for suffix in tight_words(d):
            # Replay forward independently from each *least* dyadic root.
            endpoints = [physical(prefix + suffix)[1] for prefix in SELECTED]
            kills = sum(y % 4 == 1 for y in endpoints)
            require(0 < kills < len(SELECTED), "both next-step possibilities")
            min_kill, max_kill = min(min_kill, kills), max(max_kill, kills)
            count += 1
        physical_replay.append({"suffix_length": d, "suffixes": count,
                                "root_replays": count * len(SELECTED),
                                "min_kills": min_kill, "max_kills": max_kill})
    records["physical"] = physical_replay
    records["selected_tight_prefixes"] = len(SELECTED)
    records["total_tight_prefixes"] = len(all_prefixes)
    records["pair_carries"] = [affine(w)[2] for w in ((1,2), (2,1), (1,3), (2,2))]
    switched = []
    block_options = [a + b for a in ((1, 2), (2, 1)) for b in ((1, 3), (2, 2))]
    for rounds in (1, 3, 6):
        counts = [[0] * 4 for _ in range(4)]
        for blocks in product(block_options, repeat=rounds):
            w = (1,) + sum(blocks, ()) + (2, 2, 2)
            m, y = physical(w)
            mod, a, carry = affine(w)
            require(4 * a == 7 * len(w), "programmed tight clock")
            require((1 << len(w)) * carry <= (1 << a) * (mod - (1 << len(w))),
                    "normalized source-terminal alignment")
            counts[(4 * m) // (1 << (a + 1))][(y // 2) % 4] += 1
        switched.append({"switch_rounds": rounds, "root_replays": 4 ** rounds,
                         "source_quartile_by_terminal_odd_class_mod8": counts})
    records["switched"] = switched
    print(json.dumps(records, indent=2))


if __name__ == "__main__":
    main()
