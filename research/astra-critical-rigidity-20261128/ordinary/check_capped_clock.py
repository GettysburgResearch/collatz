"""Exact finite native gate, parity, and fixed-root splicing controls."""

from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def path_to_one(n):
    path = [n]
    while path[-1] != 1:
        require(len(path) < 2000, "finite trajectory exceeded the control budget")
        path.append(step(path[-1]))
    return path


def odd_tape(n):
    values, dates = [n], [0]
    while values[-1] != 1:
        numerator = 3 * values[-1] + 1
        gap = (numerator & -numerator).bit_length() - 1
        require(gap >= 1, "odd step has no factor two")
        values.append(numerator >> gap)
        dates.append(dates[-1] + gap)
    return values, dates


def word_ledger(path):
    grade = [0]
    carry = [0]
    for k, x in enumerate(path[:-1]):
        odd = x % 2
        grade.append(grade[-1] + odd)
        carry.append((3 if odd else 1) * carry[-1] + (odd << k))
        require((path[k + 1] << (k + 1)) == 3**grade[-1] * path[0] + carry[-1],
                "prefix integer carry failed")
    return grade, carry


def gates(n, cuts, counts):
    raw = path_to_one(n)
    odds, dates = odd_tape(n)
    require([raw[i] for i in dates] == odds, "accelerated tape disagrees with native tape")
    grade, carry = word_ledger(raw)
    max_gap = max((v-u for u, v in zip(dates, dates[1:])), default=0)
    previous_u = previous_j = 0
    for cut in sorted(cuts, reverse=True):
        d = next(i for i, x in enumerate(raw) if x <= cut)
        j = next(i for i, x in enumerate(odds) if x <= cut)
        u = dates[j]
        require(0 <= u-d <= max_gap, "native/odd crossing outlasts a whole gap")
        require(odds[j] << (u-d) == raw[d], "first odd entrance is not exact halving")
        require(len([x for x in raw[:u] if x % 2]) == j, "odd clock date failed")
        require(d == 0 or cut < 2 * raw[d] <= 2 * cut, "native entrance undershoot")
        require(max_gap == 0 or cut < (odds[j] << (max_gap + 1)),
                "odd entrance undershoot exceeds true longest gap")
        v = previous_u
        g = j - previous_j
        require(u >= v and (grade[u] - grade[v]) == g, "nonmonotone gate or grade")
        local = carry[u] - 3**g * carry[v]
        require(local >= 0 and local % (1 << v) == 0, "segment correction not integral")
        require((raw[u] << (u-v)) == 3**g * raw[v] + (local >> v), "segment product")
        from_gate = next(k for k, x in enumerate(odds[previous_j:]) if x <= cut)
        require(previous_j + from_gate == j, "buffered gate failed to concatenate")
        counts["overshot_grid_gates"] += j == previous_j and cut < n
        counts["delayed_odd_gates"] += d < u
        counts["odd_native_grid_checks"] += 1
        previous_u, previous_j = u, j


def shared_root_tests(counts):
    by_landing = defaultdict(dict)
    for n in range(33, 4096, 2):
        raw = path_to_one(n)
        odds, dates = odd_tape(n)
        for a in (5, 7, 10, 13, 17, 20, 23, 26):
            if a not in raw:
                continue
            finish = raw.index(a)
            for upper, lower in ((511, 127), (127, 31), (31, 15)):
                ju = next(k for k, x in enumerate(odds) if x <= upper)
                jl = next(k for k, x in enumerate(odds) if x <= lower)
                u, v = dates[ju], dates[jl]
                if v > finish:
                    continue
                qu = sum(x % 2 for x in raw[u:finish])
                ql = sum(x % 2 for x in raw[v:finish])
                require(qu - ql == jl - ju, "fixed-root shared-gate difference ledger")
                key = (a, lower, odds[jl])
                suffix = tuple(raw[v:finish+1])
                previous = by_landing[key].get("suffix")
                if previous is None:
                    by_landing[key]["suffix"] = suffix
                else:
                    require(previous == suffix, "equal true landings have different ordered suffixes")
                    counts["shared_landing_root_suffixes"] += 1
                counts["fixed_root_gate_differences"] += 1


def parity_dictionary(counts):
    for bits in range(1, 13):
        seen = set()
        for n in range(1, 2**bits, 2):
            x, word = n, 0
            for t in range(bits):
                word |= (x % 2) << t
                x = step(x)
            require(word % 2 == 1 and word not in seen, "odd-source parity dictionary collision")
            seen.add(word)
        require(len(seen) == 2**(bits-1), "incomplete native parity dictionary")
        counts["complete_odd_word_cells"] += len(seen)


def main():
    counts = Counter()
    for n in range(1, 2049, 2):
        cuts = set(range(1, n+1)) if n <= 129 else {n, 1, 2, 3, 5, 13, 31, 127}
        cuts.update(max(1, n // t) for t in (2, 3, 5, 8, 11))
        gates(n, {x for x in cuts if x <= n}, counts)
        counts["positive_odd_sources"] += 1
    shared_root_tests(counts)
    parity_dictionary(counts)
    require(min(counts.values()) > 0, "a named branch never occurred")
    folder = Path(__file__).resolve().parent
    sources = ("CAPPED_FUNCTIONAL_MODERATE_DEVIATIONS.md", "FIXED_ROOT_ITERATED_LOGARITHM.md")
    print(json.dumps({"scope": "finite exact path comparisons, no statistical limit test",
                      "counts": dict(counts),
                      "manuscript_hashes": {s: sha256((folder/s).read_bytes()).hexdigest()
                                            for s in sources}}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
