#!/usr/bin/env python3
"""Exact finite controls for HT1--HT5; no full Collatz coverage claim."""
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def positive_integer(n):
    return type(n) is int and n > 0


def v2(n):
    need(positive_integer(n), "positive valuation input")
    return (n & -n).bit_length() - 1


def T(n):
    need(positive_integer(n), "positive ordinary source")
    return n // 2 if n % 2 == 0 else (3*n + 1) // 2


def U(n):
    need(positive_integer(n) and n % 2, "positive odd source")
    a = v2(3*n + 1)
    return (3*n + 1) >> a, a


def correction(word):
    need(bool(word) and all(positive_integer(a) for a in word), "positive nonempty word")
    p = len(word)
    A = 0
    B = 0
    for j, a in enumerate(word):
        B += 3**(p-1-j) * 2**A
        A += a
    return B, A


def decode_correction(C, p):
    need(positive_integer(C) and positive_integer(p), "positive decoder domain")
    gaps = []
    R = C
    for r in range(p, 1, -1):
        difference = R - 3**(r-1)
        if difference <= 0 or difference % 2:
            return None
        e = v2(difference)
        gaps.append(e)
        R = difference >> e
    return gaps if R == 1 else None


def recognize(word):
    B, L = correction(word)
    gaps = decode_correction(5*B, len(word))
    if gaps is None or sum(gaps) >= L:
        return None
    return gaps + [L-sum(gaps)]


def literal_word(n, word, endpoint, first_hit=False):
    original = n
    clocks = 0
    for a in word:
        if first_hit:
            need(n != 1, "source witness was not first-hit")
        actual, actual_a = U(n)
        need(actual_a == a, "incorrect exact odd exponent")
        literal = n
        for _ in range(a):
            literal = T(literal)
            clocks += 1
        need(literal == actual and literal % 2, "literal shortcut disagreement")
        n = literal
    need(n == endpoint, "wrong ordinary endpoint")
    B, L = correction(word)
    need(clocks == L and 3**len(word)*original+B == 2**L*endpoint,
         "full path identity")
    return clocks


def compile_first_hit(x, word):
    if x == 1:
        need(word == [], "empty source is exactly1")
        return [4]
    literal_word(x, word, 1, first_hit=True)
    target = recognize(word)
    if target is None:
        return None
    answer = target + [4]
    literal_word(5*x, answer, 1, first_hit=True)
    return answer


FAMILIES = (
    (1, 6, 65, 512, 271, [1, 2, 5], 5, 28),
    (2, 4, 73, 256, 135, [1, 5, 1], 3, 26),
    (4, 4, 121, 1024, 87, [1, 3, 5], 3, 20),
)


def prepend_legal_block(q, prefix, minimum):
    p = len(prefix) + 1
    for b in range(minimum, minimum + 162):
        w = prefix + [b]
        B, L = correction(w)
        numerator = 2**L*q - B
        if numerator > 0 and numerator % 3**p == 0:
            x = numerator // 3**p
            if x % 3:
                literal_word(x, w, q)
                need(recognize(w) is not None, "fixture block not transported")
                return x, w
    raise ValueError("finite fixture inverse lift not found")


def main():
    expansion_controls = 0
    for p in range(1, 7):
        seen = {}
        for tail in combinations(range(1, 15), p-1):
            positions = (0,) + tail
            B = sum(3**(p-1-j)*2**d for j, d in enumerate(positions))
            need(B not in seen, "two independently enumerated expansions collide")
            seen[B] = positions
            decoded = decode_correction(B, p)
            recovered = [0]
            for gap in decoded:
                recovered.append(recovered[-1]+gap)
            need(tuple(recovered) == positions, "decoder differs from direct expansion")
            expansion_controls += 1

    classification_controls = 0
    for b in range(1, 25):
        need(recognize([1, b]) is None, "forbidden two-input transport")
        classification_controls += 1
    for c in range(1, 33):
        for b in range(1, 17):
            need(recognize([1, c, b]) is None, "forbidden three-input transport")
            classification_controls += 1
    for c in range(1, 25):
        for d in range(1, 25):
            for b in range(1, 13):
                answer = recognize([1, c, d, b])
                row = next((r for r in FAMILIES if c == 1 and d == r[0]), None)
                expected = row is not None and b >= row[1]
                need((answer is not None) == expected, "four-input classification failed")
                if expected:
                    need(answer == row[5] + [b-row[6]], "wrong unique target word")
                classification_controls += 1

    block_controls = cylinder_controls = literal_clocks = 0
    unit_sources = nonunit_sources = 0
    closed_families = []
    for a, b0, B, modulus, residue, target_prefix, delta, first_b in FAMILIES:
        need((-B*pow(81, -1, modulus)) % modulus == residue,
             "source cylinder residue")
        for b in range(b0, b0+16):
            L = a+2+b
            q0 = (B*pow(2, -L, 81)) % 81
            if q0 % 2 == 0:
                q0 += 81
            for j in range(4):
                q = q0+162*j
                x = (2**L*q-B)//81
                source = [1, 1, a, b]
                target = target_prefix+[b-delta]
                need(x > 0 and x % 2 and q % 2 and q % 3, "ordinary domains")
                need(3*q <= x, "smaller-antecedent inequality")
                need(x % modulus == residue, "whole source cylinder")
                need(recognize(source) == target, "recognizer disagrees with exact family")
                literal_clocks += literal_word(x, source, q)
                literal_clocks += literal_word(5*x, target, 5*q)
                unit_sources += x % 3 != 0
                nonunit_sources += x % 3 == 0
                block_controls += 1
        for j in range(65):
            x = residue+modulus*j
            n = x
            actual = []
            for _ in range(4):
                n, gap = U(n)
                actual.append(gap)
            need(actual[:3] == [1, 1, a] and actual[3] >= b0,
                 "literal cylinder exponent pattern")
            need(3*n <= x, "cylinder endpoint bound")
            cylinder_controls += 1
        for j in range(5):
            b = first_b+54*j
            source = [1, 1, a, b]
            L = sum(source)
            need((2**L-B) % 81 == 0, "closed family integrality")
            x = (2**L-B)//81
            answer = compile_first_hit(x, source)
            need(answer == target_prefix+[b-delta, 4], "closed first-hit family")
            closed_families.append({"a":a,"j":j,"source_bits":x.bit_length(),
                                    "source_clock":L,"target_clock":sum(answer),
                                    "source_odd_count":4,"target_odd_count":5})

    mixed = []
    for seeds in (
        [([1,1,1],6),([2],4)],
        [([1,1,2],4),([1,1,4],4)],
        [([2,2,2],4),([1,1,1],6),([1,1,2],4)],
        [([1,1,4],4),([2,2],4),([1,1,2],4),([1,1,1],6)],
    ):
        source, word = 1, []
        for prefix, minimum in reversed(seeds):
            source, block = prepend_legal_block(source, prefix, minimum)
            word = block+word
        answer = compile_first_hit(source, word)
        need(answer is not None, "whole-word recognizer missed composed blocks")
        need(len(answer) == len(word)+1 and sum(answer) == sum(word)+4,
             "complete compiler resources")
        mixed.append({"source_bits":source.bit_length(),"source_word":word,
                      "target_word":answer})

    # The complete actual pair proof is finite, followed by its period two.
    x, y = 7, 35
    pair = []
    for t in range(1, 14):
        x, y = T(x), T(y)
        need(y != 5*x, "unexpected positive homogeneous return")
        pair.append([t,x,y])
    need(pair[9:] == [[10,2,1],[11,1,2],[12,2,1],[13,1,2]], "terminal pair cycle")
    literal_word(7, [1,1,2,3,4], 1, first_hit=True)
    literal_word(35, [1,5,4], 1, first_hit=True)
    need(compile_first_hit(7, [1,1,2,3,4]) is None, "unresolved7 falsely accepted")
    need(compile_first_hit(17, [2,3,4]) is None, "unresolved17 falsely accepted")
    literal_word(85, [8], 1, first_hit=True)

    rejected = []
    controls = [
        ("nonpositive decoder", lambda: decode_correction(0,2)),
        ("zero term count", lambda: decode_correction(5,0)),
        ("zero exponent", lambda: recognize([1,0,2])),
        ("boolean exponent", lambda: recognize([True,2])),
        ("wrong supplied exponent", lambda: compile_first_hit(17,[2,2,4])),
        ("padded first-hit witness", lambda: compile_first_hit(17,[2,3,4,2])),
        ("wrong endpoint", lambda: literal_word(17,[2,3,4],5)),
    ]
    for name, action in controls:
        try:
            action()
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError("invalid control accepted: "+name)
    need(compile_first_hit(1,[]) == [4], "base source1")

    report = {
        "status":"PASS: exact finite controls for HT1--HT5",
        "proof_sha256":sha256(Path(__file__).with_name("HOMOGENEOUS_FIVE_TRANSPORT.md").read_bytes()).hexdigest(),
        "checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "independent_correction_expansions":expansion_controls,
        "minimal_depth_classification_controls":classification_controls,
        "physical_four_input_blocks":block_controls,
        "unit_source_blocks":unit_sources,
        "nonunit_source_blocks":nonunit_sources,
        "literal_shortcut_edges":literal_clocks,
        "literal_source_cylinder_controls":cylinder_controls,
        "closed_rank_four_families":closed_families,
        "mixed_complete_certificates":mixed,
        "complete_no_return_pair7_35":pair,
        "malformed_controls_rejected":rejected,
        "valid_unresolved_sources":[7,17],
        "scope":[
            "The decoder theorem and complete four-input classification use the written proofs.",
            "The finite expansion table is not an all-word census.",
            "No homogeneous first-return coverage or full five-closure is claimed.",
            "Different-clock and different-odd-count transformations remain possible.",
        ],
    }
    print(json.dumps(report,sort_keys=True,indent=2))


if __name__ == "__main__":
    main()
