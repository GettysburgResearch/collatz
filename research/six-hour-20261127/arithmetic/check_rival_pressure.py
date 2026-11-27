"""Exact forbidden ordinary inverse contexts and their two-copy pressure."""
from collections import deque
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory

from check_four_copy_tails import log_bounds

MAX_LENGTH = 22
ANCHOR = Fraction(1, 400)
RETURN_LIMIT = 665
SLOPES = (Fraction(584_962_500_720, 10**12), Fraction(584_962_500_723, 10**12))
SCALE = 1 << 48
WEIGHT = (2, 5, 20)


def require(condition, reason):
    if not condition:
        raise ArithmeticError(reason)


def unit_residue(state, native):
    d, offset = state
    u, v = max(d, 0), max(-d, 0)
    return (((-1)**(u+native)+offset)*(-1)**v) % 3


@lru_cache(None)
def moves(state, native):
    d, offset = state
    v = max(-d, 0)
    residue = unit_residue(state, native)
    if residue == 0:
        return ()
    first = 2 if residue == 1 else 1
    result = []
    for alternate in range(first, 11-d+native+1, 2):
        new_d = d+alternate-native
        if new_d < -3:
            continue
        w = max(-new_d, 0)
        digit = (1 << (w+new_d))+(1 << (w+alternate-v))*offset-(1 << w)
        require(digit % 3 == 0, "affine exact update")
        if abs(digit//3) <= 300:
            result.append(((new_d, digit//3), alternate))
    return tuple(result)


def conflict(state, native, layer):
    d, offset = state
    return (d+layer < 0 or (d+layer < 1 and unit_residue(state, native) == 0)
            or (d < 0 and abs(offset) == 1) or state == (1, -1))


def forbidden_words():
    # States are actual relative affine coefficients. Bitsets only accelerate
    # unions of their independently valid inverse paths.
    states = [(0, 0)]
    ids = {(0, 0): 0}
    for state in states:
        for a in (1, 2):
            for nxt, _ in moves(state, a):
                if nxt not in ids:
                    ids[nxt] = len(states)
                    states.append(nxt)
    step = [[sum(1 << ids[v] for v, _ in moves(u, a)) for u in states] for a in (1, 2)]
    veto = [[sum(1 << i for i, u in enumerate(states) if conflict(u, a, k))
             for a in (1, 2)] for k in (0, 1)]

    @lru_cache(None)
    def advance(mask, a):
        result = 0
        while mask:
            bit = mask & -mask
            mask -= bit
            result |= step[a-1][bit.bit_length()-1]
        return result

    found = {}
    visits = 0

    def visit(word, mask, height, low, high):
        nonlocal visits
        visits += 1
        for a in (1, 2):
            h = height+a*1_000_000-1_584_962
            bottom, top = min(low, h), max(high, h)
            if top-bottom > 2_010_000:
                continue
            k = next((k for k in (1, 0) if mask & veto[k][a-1]), -1)
            if k >= 0 and height-bottom < (k+1)*1_000_000+10_000:
                found[(word+str(a))[::-1]] = k
            if len(word)+1 < MAX_LENGTH:
                following = advance(mask, a)
                if following:
                    visit(word+str(a), following, h, bottom, top)

    for a in (1, 2):
        h = a*1_000_000-1_584_962
        visit(str(a), step[a-1][0] & ~1, h, min(0, h), max(0, h))
    # A shorter chronological prefix ends at the same detection cut when read
    # backwards. A larger layer limit vetoes both of the smaller limits.
    minimal = {}
    for word, k in sorted(found.items(), key=lambda item: len(item[0])):
        if all(minimal.get(word[:i], -1) < k for i in range(1, len(word))):
            minimal[word] = k
    return minimal, visits, len(states)


def actual_checks(words):
    count = 0
    for word, layer in words.items():
        native = tuple(map(int, word))
        # Obtain one actual alternate word, retaining its endpoints separately
        # from the bitset code. The last native symbol tests the current residue.
        paths = {(0, 0): ()}
        for index, a in enumerate(native[:0:-1]):
            paths = {new: path+(b,) for old, path in paths.items()
                     for new, b in moves(old, a) if index or b != a}
        state, rival = next((state, path) for state, path in paths.items()
                            if conflict(state, native[0], layer))
        power, affine = 1, 0
        for a in native:
            affine = 3*affine+power
            power <<= a
        modulus = 2*power
        representative = ((power-affine)*pow(3**len(native), -1, modulus)) % modulus
        for lift in (100, 101):
            x = representative+lift*modulus
            real = [x]
            for a in native:
                value = 3*real[-1]+1
                require((value & -value) == 1 << a, "literal native valuation")
                real.append(value >> a)
            y = real[-1]
            for b in rival:
                numerator = (y << b)-1
                require(numerator % 3 == 0, "literal inverse divisibility")
                y = numerator//3
                require(y > 0 and y % 2 == 1, "literal positive odd ancestor")
            d, offset = state
            require(y << max(-d, 0) == (real[1] << max(d, 0))+offset,
                    "literal relative affinity")
            require(y % 3 == unit_residue(state, native[0]), "literal terminal residue")
            count += 1
    return count


def automaton(words):
    trie, output = [{}], [-1]
    for word, k in sorted(words.items()):
        state = 0
        for symbol in word[::-1]:
            a = int(symbol)-1
            if a not in trie[state]:
                trie[state][a] = len(trie)
                trie.append({})
                output.append(-1)
            state = trie[state][a]
        output[state] = max(output[state], k)
    failure = [0]*len(trie)
    queue = deque()
    for a in (0, 1):
        if a in trie[0]:
            queue.append(trie[0][a])
        else:
            trie[0][a] = 0
    while queue:
        state = queue.popleft()
        output[state] = max(output[state], output[failure[state]])
        for a in (0, 1):
            if a in trie[state]:
                child = trie[state][a]
                failure[child] = trie[failure[state]][a]
                queue.append(child)
            else:
                trie[state][a] = trie[failure[state]][a]
    # Equal Moore states have equal current output and equal successor classes.
    classes = output[:]
    while True:
        new_ids, refined = {}, []
        for i, k in enumerate(output):
            signature = (k, classes[trie[i][0]], classes[trie[i][1]])
            refined.append(new_ids.setdefault(signature, len(new_ids)))
        if refined == classes:
            break
        classes = refined
    table = [None]*len(new_ids)
    for i, group in enumerate(classes):
        table[group] = (output[i], classes[trie[i][0]], classes[trie[i][1]])
    return table, classes[0]


def cuts(slope):
    floors = []
    clipped = [(Fraction(0), ("left", 0)), (ANCHOR, ("right", 0))]
    for j in range(1, RETURN_LIMIT+1):
        for kind, v in (("wrap", Fraction(0)), ("entry", ANCHOR)):
            x = v+j*slope
            whole = x//1
            floors.append(whole)
            x -= whole
            if 0 <= x <= ANCHOR:
                clipped.append((x, (kind, j)))
    clipped.sort()
    require(len({x for x, _ in clipped}) == len(clipped), "distinct clipped cuts")
    return floors, clipped


def schedules():
    l2, l3 = log_bounds(3), log_bounds(2)
    lo, hi = SLOPES
    require((1+lo)*l2[1] < l3[0] and l3[1] < (1+hi)*l2[0], "strict slope bracket")
    flo, clo = cuts(lo)
    fhi, chi = cuts(hi)
    require(flo == fhi and [v for _, v in clo] == [v for _, v in chi],
            "affine clipped arrangement")
    # For fixed floors a cut could move from below 0 to above ANCHOR while
    # omitted at both endpoints only if its displacement reached ANCHOR.
    require(RETURN_LIMIT*(hi-lo) < ANCHOR, "uncounted crossing")
    mid = (lo+hi)/2
    ranks = [v for v, _ in cuts(mid)[1]]
    result = set()
    for a, b in zip(ranks, ranks[1:]):
        for p in (a, (a+b)/2):
            word = []
            for _ in range(RETURN_LIMIT):
                wrap = p < mid
                word.append(str(1+int(wrap)))
                p = (p-mid) % 1
                if p < ANCHOR:
                    break
            else:
                raise ArithmeticError("uncovered anchor")
            result.add("".join(word))
    require(sorted(map(len, result)) == [306, 359, 665], "return lengths")
    return sorted(result, key=len)


def literal_matrix(words, schedule):
    starts = ((0, 0, 0, 0), (0, 1, 0, 1), (1, 1, 1, 1))
    equal_pairs = [s for s in product((0, 1), repeat=4) if s[0]+s[1] == s[2]+s[3]]
    reversed_words = [(w[::-1], k) for w, k in words.items()]
    answer = []
    for start in starts:
        histories = [(start, "", "")]
        for b in map(int, schedule):
            new_histories = []
            for terminal, p, q in histories:
                for earlier in equal_pairs:
                    actual = tuple(b+x-y for x, y in zip(earlier, terminal))
                    if not all(a in (1, 2) for a in actual):
                        continue
                    new = (p+str(actual[0]), q+str(actual[1]))
                    if any(h.endswith(w) and terminal[i] <= k
                           for i, h in enumerate(new) for w, k in reversed_words):
                        continue
                    new_histories.append((earlier, *new))
            histories = new_histories
        answer.extend(sum(s[0]+s[1] == k for s, _, _ in histories) for k in (0, 1, 2))
    return answer


def execute(cases):
    data = [str(len(cases))]
    for rounded, (table, root), words in cases:
        data.append(f"{rounded} {len(table)} {root} {len(words)}")
        data.extend(" ".join(map(str, row)) for row in table)
        data.extend(words)
    with TemporaryDirectory() as directory:
        binary = Path(directory)/"rival_pressure"
        subprocess.run(["c++", "-std=c++17", "-O3", "-Wall", "-Wextra", "-Werror",
                        str(Path(__file__).with_name("rival_pressure.cpp")), "-o", str(binary)],
                       check=True)
        result = subprocess.run([str(binary)], input="\n".join(data)+"\n", text=True,
                                capture_output=True, check=True)
    return [list(map(int, row.split())) for row in result.stdout.splitlines()]


def check():
    words, visits, reachable = forbidden_words()
    actual = actual_checks(words)
    machine = automaton(words)
    returns = schedules()
    toy = {"11": 0, "212": 1}
    short = ["121212", "221121"]
    output = execute([(0, automaton(toy), short), (1, machine, returns)])
    require(output[:2] == [literal_matrix(toy, w) for w in short], "literal four-path count")
    require(len(output) == 5 and all(len(row) == 9 for row in output), "complete matrices")
    record = []
    for w, flat in zip(returns, output[2:]):
        matrix = [flat[3*i:3*i+3] for i in range(3)]
        for i, row in enumerate(matrix):
            lhs = sum(x*y for x, y in zip(row, WEIGHT))
            require(10*lhs < 9*SCALE*WEIGHT[i], "weighted return contraction")
        record.append({"length": len(w), "word_sha256": sha256(w.encode()).hexdigest(),
                       "normalized_integer_upper_matrix": matrix})
    require(9**10000*3**RETURN_LIMIT < 10**10000, "strict per-site exponent")
    canonical = "".join(f"{w} {k}\n" for w, k in sorted(words.items()))
    return {"maximum_odd_context": MAX_LENGTH, "retained_affine_states": reachable,
            "explored_native_prefixes": visits, "forbidden_contexts": len(words),
            "contexts_sha256": sha256(canonical.encode()).hexdigest(),
            "actual_ordinary_two_lift_checks": actual, "minimized_veto_states": len(machine[0]),
            "anchor_length": str(ANCHOR), "fixed_point_scale": SCALE, "weights": list(WEIGHT),
            "literal_toy_matrices": output[:2], "returns": record,
            "strict_log3_energy_exponent": "9999/10000"}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
