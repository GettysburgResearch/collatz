"""All physical minimum phases below 2^71 for the restricted bounded cycle."""
from bisect import bisect_left, bisect_right
from collections import defaultdict
from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def possible_prefix(j, total, backwards):
    p, q = 3**j, 1 << total
    if backwards:
        return p <= q and 1000*q <= 5335*p
    return 1000*p <= 5335*q and 1001*p >= 1000*q


def past_residues(k):
    modulus = 3**k
    row = {0: [0]}
    for j in range(1, k+1):
        nxt = defaultdict(list)
        for grade, words in row.items():
            for e in (1, 2):
                after = grade+e
                if possible_prefix(j, after, True):
                    addend = 3**(j-1)*pow(1 << after, -1, modulus) % modulus
                    nxt[after].extend((x+addend) % modulus for x in words)
        row = nxt
    return [x for words in row.values() for x in words]


def future_residues(f):
    # Each list initially holds the exact affine carry.
    row = {0: [0]}
    for j in range(1, f+1):
        nxt = defaultdict(list)
        for grade, carries in row.items():
            for e in (1, 2):
                after = grade+e
                if possible_prefix(j, after, False):
                    addend = 1 << grade
                    nxt[after].extend(3*c+addend for c in carries)
        row = nxt
    for grade, words in row.items():
        q = 1 << (grade+1)
        inverse = pow(3**f, -1, q)
        for i, carry in enumerate(words):
            words[i] = ((1 << grade)-carry)*inverse % q
    return row


def first_exit(s, limit):
    x, top = s, (16*s+7)//3
    for edge in range(1, limit+1):
        z = 3*x+1
        power = z & -z
        if power > 4:
            return edge
        x = z//power
        if x < s or x > top:
            return edge
    return None


def census(k, f, low, high, edge_limit, record=False):
    p = 3**k
    past = past_residues(k)
    future = future_residues(f)
    by_grade = []
    observed = [] if record else None
    for grade, future_sources in sorted(future.items()):
        q = 1 << (grade+1)
        inverse = pow(q, -1, p)
        require(high < p*q, "only the first CRT period is searched")
        # Keep all words. Agreement of residues would only duplicate a test.
        ordered = sorted(a*inverse % p for a in past)
        count, last_exit, checksum = 0, 0, 0
        for b in future_sources:
            if b > high:
                continue
            start = b*inverse % p
            stop = start+(high-b)//q
            # t = (ordered[i]-start) mod p. Both inclusive runs are disjoint.
            for left, right, origin in ((start, min(p-1, stop), start),
                                        (0, stop-p, start-p)):
                if right < left:
                    continue
                i0 = bisect_left(ordered, left)
                i1 = bisect_right(ordered, right)
                for i in range(i0, i1):
                    s = b+(ordered[i]-origin)*q
                    if s < low:
                        continue
                    require(s <= high and s % 2 == 1, "physical source")
                    count += 1
                    checksum = (checksum+s) % (2**61-1)
                    if observed is not None:
                        observed.append(s)
                    if edge_limit:
                        exit_edge = first_exit(s, edge_limit)
                        require(exit_edge is not None, "surviving physical minimum")
                        last_exit = max(last_exit, exit_edge)
        by_grade.append({"future_grade": grade, "future_words": len(future_sources),
                         "physical_candidates": count, "latest_exit": last_exit,
                         "sum_of_sources_mod_2^61_minus_1": checksum})
    return len(past), by_grade, observed


def literal_window(s, depth, backwards):
    x, grade = s, 0
    for j in range(1, depth+1):
        if backwards:
            if x % 3 == 0:
                return False
            e = 2 if x % 3 == 1 else 1
            x = ((1 << e)*x-1)//3
        else:
            z = 3*x+1
            e = (z & -z).bit_length()-1
            if e not in (1, 2):
                return False
            x = z >> e
        grade += e
        ratio = Fraction(1 << grade, 3**j)
        if backwards and not 1 <= ratio <= Fraction(5335, 1000):
            return False
        if not backwards and not Fraction(1000, 5335) <= ratio <= Fraction(1001, 1000):
            return False
    return True


def checks():
    cut, k, f = 1 << 20, 30, 30
    gain = Fraction(3*cut, 3*cut-max(k, f))
    require(gain < Fraction(1001, 1000), "forward affine correction")
    require(Fraction(16*cut+7, 3*cut)*gain < Fraction(5335, 1000),
            "full backward homogeneous ceiling")
    # A separate direct scanner compares each small source, including failure
    # of a ternary predecessor, to the whole sorted CRT enumeration.
    _, _, small = census(5, 6, 3, 32767, 0, True)
    literal = [s for s in range(3, 32768, 2)
               if literal_window(s, 5, True) and literal_window(s, 6, False)]
    require(sorted(small) == literal, "literal source-by-source census")
    last_small_exit = 0
    for s in range(3, cut, 2):
        exit_edge = first_exit(s, 256)
        require(exit_edge is not None, "small surviving minimum")
        last_small_exit = max(last_small_exit, exit_edge)
    past, bands, _ = census(k, f, cut, (1 << 71)-1, 256)
    return {"small_literal_candidates": len(literal), "small_minima_directly_traced": cut//2-1,
            "last_small_exit": last_small_exit, "middle_height_floor": cut,
            "exclusive_height_ceiling": 1 << 71, "past_odd_depth": k,
            "future_odd_depth": f, "past_words": past, "future_grades": bands,
            "all_middle_candidates": sum(g["physical_candidates"] for g in bands)}


if __name__ == "__main__":
    print(json.dumps(checks(), indent=2))
