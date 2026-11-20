#!/usr/bin/env python3
"""Independent finite trajectory controls for the pinned HT1--HT5 review."""
import argparse
from hashlib import sha256
import json
from pathlib import Path

PROOF_SHA = "f2872fad5c04e3aba9219f4b54576ef438d2922d7dcad9b0a8423974c4d2c31b"


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def shortcut(n):
    return (3*n+1)//2 if n % 2 else n//2


def odd_edge(n):
    need(n > 0 and n % 2, "ordinary odd input")
    v, a = 3*n+1, 0
    while v % 2 == 0:
        v //= 2
        a += 1
    return v, a


def reconstructed_target(correction, count, clock):
    # This is the reviewed algebraic criterion; the oracle below instead
    # follows both literal ordinary paths and counts their odd inputs.
    residue, gaps = 5*correction, []
    for remaining in range(count, 1, -1):
        residue -= 3**(remaining-1)
        if residue <= 0 or residue % 2:
            return None
        gap = 0
        while residue % 2 == 0:
            residue //= 2
            gap += 1
        gaps.append(gap)
    if residue != 1 or sum(gaps) >= clock:
        return None
    return gaps + [clock-sum(gaps)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proof", type=Path,
                        default=Path(__file__).with_name("HOMOGENEOUS_FIVE_TRANSPORT.md"))
    args = parser.parse_args()
    need(sha256(args.proof.read_bytes()).hexdigest() == PROOF_SHA,
         "reviewed proof bytes changed")
    controls = accepted = unresolved = 0
    accepted_unit = accepted_nonunit = 0
    for x in range(1, 2048, 2):
        source, target = x, 5*x
        B = L = target_clock = target_odd_count = previous_target_odd = 0
        source_word, literal_target_word = [], []
        for p in range(1, 9):
            source, a = odd_edge(source)
            B, L = 3*B + 2**L, L+a
            source_word.append(a)
            need(3**p*x+B == 2**L*source, "independent prefix affine recurrence")
            while target_clock < L:
                target_odd_count += target % 2
                target = shortcut(target)
                target_clock += 1
                if target % 2:
                    literal_target_word.append(target_clock-previous_target_odd)
                    previous_target_odd = target_clock
            actual_match = target == 5*source and target_odd_count == p
            proposal = reconstructed_target(B, p, L)
            need((proposal is not None) == actual_match,
                 "recognition disagrees with literal paired trajectories")
            if actual_match:
                need(proposal == literal_target_word,
                     "unique target gaps disagree with the literal target path")
                accepted += 1
                accepted_unit += x % 3 != 0
                accepted_nonunit += x % 3 == 0
            else:
                unresolved += 1
            controls += 1
    need(accepted and unresolved and accepted_unit and accepted_nonunit,
         "finite controls omit an intended domain or outcome")
    need(controls == 8192, "finite control census")
    # An affine coefficient check, valid for every nonnegative lift t.
    cylinder_rows = ((271,512,1,64,43), (135,256,2,16,43), (87,1024,4,16,7))
    cylinders = []
    for r, m, a, divisor, offset in cylinder_rows:
        intercept, slope = r, m
        states = []
        for gap in (1,1,a):
            need((3*intercept+1) % 2**gap == 0 and
                 ((3*intercept+1)//2**gap) % 2,
                 "constant term has the specified exact valuation")
            need(3*slope % 2**(gap+1) == 0,
                 "every lift preserves the exact valuation")
            intercept, slope = (3*intercept+1)//2**gap, 3*slope//2**gap
            states.append([intercept,slope])
        need(3*intercept+1 == divisor*offset and 3*slope == divisor*81,
             "universal final divisibility identity")
        cylinders.append({"residue":r,"modulus":m,"three_odd_states":states,
                          "final_numerator":[divisor,offset,81]})
    x, y, pair = 7, 35, []
    for t in range(1,14):
        x, y = shortcut(x), shortcut(y)
        need(y != 5*x, "source seven unexpectedly has a synchronized five return")
        pair.append([t,x,y])
    need(pair[9:] == [[10,2,1],[11,1,2],[12,2,1],[13,1,2]],
         "exact terminal pair cycle")
    print(json.dumps({
        "status":"PASS: finite independent controls for the pinned written review",
        "proof_sha256":PROOF_SHA,
        "review_checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "literal_prefix_controls":controls,"accepted":accepted,"unresolved":unresolved,
        "accepted_unit_sources":accepted_unit,"accepted_nonunit_sources":accepted_nonunit,
        "source_limit":2047,"maximum_odd_prefix_length":8,
        "universal_cylinder_coefficients":cylinders,"source7_pair":pair,
        "scope":[
            "The literal oracle does not import the author checker.",
            "These are finite controls; arbitrary exponents and lengths use the written proof.",
            "Valid unresolved prefixes make no assertion of nonconvergence."]
    },indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
