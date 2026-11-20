#!/usr/bin/env python3
"""Independent bounded reconstruction of GA-001--005; no author-code import."""

from collections import Counter
from hashlib import sha256
from math import comb, gcd
from pathlib import Path
import argparse
import json


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def v2(n):
    need(n > 0, "positive valuation argument")
    result = 0
    while n % 2 == 0:
        n //= 2
        result += 1
    return result


def run_count(n):
    bits = bin(n)[2:]
    return sum(bit == "1" and (i == 0 or bits[i - 1] == "0")
               for i, bit in enumerate(bits))


def physical_odd_step(n):
    value, divisions = 3 * n + 1, 0
    while value % 2 == 0:
        value //= 2
        divisions += 1
    return value, divisions


def clock(n):
    return v2(n + 1) - 1


def product(values):
    result = 1
    for value in values:
        result *= value
    return result


def dispersed_parameter(m, length, multiplier):
    """Different candidate order from the production SHAKE construction."""
    state = 0xA57A20261120 ^ m ^ length ^ (multiplier & (2**64 - 1))
    assembled = 0
    for _ in range((length + 63) // 64):
        state = (6364136223846793005 * state + 1442695040888963407) % 2**64
        assembled = (assembled << 64) | state
    low_mask = 2 ** (length - 1) - 1
    start = (assembled & low_mask) | 1
    for trial in range(2 ** (length - 2)):
        v = 2 ** (length - 1) | ((start + 2 * trial) & low_mask)
        if all(run_count((3**i * multiplier * v - 1) % 2**length) >= length // 8
               for i in range(m)):
            return v, trial + 1
    raise RuntimeError("finite entropy witness absent")


def prime_power(n, p):
    result = 1
    while n % p == 0:
        n //= p
        result *= p
    return result


def run():
    root = Path(__file__).resolve().parents[2]
    expected = {
        "research/global-closure-20261120/arithmetic.md": "ed2b9c627fe7b9000934ac6c0231f55f0cbafca1cbc6283b0d48b5758dc7860c",
        "experiments/global_closure_arithmetic.py": "5c928688397bd8b4f1d3b9b357e1646ec27cc8973c43a54abc3c714f84040269",
        "reports/2026-11-20-global-closure/arithmetic-report.json": "8d27838b5023b399736350d7659ba49cf62273f97e4261feaee5c779fe79336a",
    }
    for path, expected_hash in expected.items():
        need(sha256((root / path).read_bytes()).hexdigest() == expected_hash,
             "reviewed source changed: " + path)

    even_words = 0
    for length in range(1, 17):
        counts = Counter()
        for n in range(0, 2**length, 2):
            counts[run_count(n)] += 1
            even_words += 1
        for r in range(length + 1):
            need(counts[r] == (comb(length, 2 * r) if 2 * r <= length else 0),
                 "even-word combinatorial count")
    entropy_checks = 0
    for m in range(2, 65):
        length = 16 * m
        bad = sum(comb(length, 2 * r) for r in range(length // 8))
        need(m * bad < 2 ** (length - 2), "exact union bound")
        need(4 * m * 16 ** (length // 4) < 27 ** (length // 4),
             "printed entropy margin")
        entropy_checks += 1

    accounting_edges = 0
    for start in range(1, 4096, 2):
        n, ones, recharge = start, 0, 0
        initial = clock(start)
        for _ in range(32):
            following, a = physical_odd_step(n)
            ones += a == 1
            if a >= 2:
                recharge += clock(following)
                need(clock(n) == 0, "reset source clock")
            else:
                need(clock(following) == clock(n) - 1, "valuation-one clock")
            need(ones == initial - clock(following) + recharge,
                 "arbitrary-source exact clock account")
            n = following
            accounting_edges += 1

    cases = []
    edges = pair_checks = prime_block_checks = 0
    chosen_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 43, 211)
    for coprime in (False, True):
        for m in (2, 3, 4, 7, 11, 17, 25):
            length = 16 * m * m if coprime else 16 * m
            q = product(3**d - 2**d for d in range(1, m)) if coprime else 1
            if coprime:
                q *= product(2 * k - 1 for k in range(1, m + 1))
                need(q < 2 ** (2 * m * m - m), "quadratic multiplier height")
            v, trials = dispersed_parameter(m, length, q)
            need(v.bit_length() == length and v % 2 == 1, "parameter domain")
            nodes = [3**i * 2 ** (m - i) * q * v - 1 for i in range(m)]
            for i, n in enumerate(nodes):
                need(run_count(n) >= length // 8 + 1, "run lower bound")
                need(10 * run_count(n) > n.bit_length(), "dense run proportion")
                need(n.bit_length() <= (18 * m * m + m - 1 if coprime else 18 * m - 1),
                     "state height bound")
                if i + 1 < m:
                    following, a = physical_odd_step(n)
                    need((following, a) == (nodes[i + 1], 1), "literal legal block edge")
                    edges += 1
            need(clock(nodes[0]) == m - 1 and physical_odd_step(nodes[-1])[1] >= 2,
                 "exact finite block lifetime")
            if not coprime:
                need(nodes[0].bit_length() == 17 * m, "linear source bitlength")
            for i in range(m):
                for j in range(i + 1, m):
                    d = j - i
                    correction = 3**d - 2**d
                    need(2**d * nodes[j] == 3**d * nodes[i] + correction,
                         "affine gcd identity")
                    common = gcd(nodes[i], nodes[j])
                    need(correction % common == 0, "full gcd divisor")
                    if coprime:
                        need(common == 1, "pairwise coprimality")
                    width = nodes[j] - nodes[i]
                    need(3**d < 2**d * (width + 1), "translated interval consequence")
                    pair_checks += 1
            if coprime:
                for n in nodes:
                    need(gcd(n, q) == 1, "complete selected multiplier exclusion")
            else:
                block_length = 1
                while block_length * block_length < m:
                    block_length += 1
                for offset in range(0, m, block_length):
                    block = nodes[offset:offset + block_length]
                    for p in chosen_primes:
                        powers = [prime_power(n, p) for n in block]
                        highest = max(range(len(block)), key=lambda j: powers[j])
                        for j, value in enumerate(powers):
                            if j != highest:
                                d = abs(j - highest)
                                need((3**d - 2**d) % value == 0,
                                     "adversarial maximum-valuation prime bound")
                        prime_block_checks += 1
            cases.append({"m": m, "mode": "coprime" if coprime else "linear",
                          "attempts": trials, "source_bits": nodes[0].bit_length(),
                          "maximum_state_bits": max(n.bit_length() for n in nodes),
                          "minimum_runs": min(run_count(n) for n in nodes),
                          "source_sha256": sha256(nodes[0].to_bytes((nodes[0].bit_length() + 7) // 8, "big")).hexdigest()})

    recharge_edges = recharge_families = 0
    for m in tuple(range(1, 65)) + (128, 256, 1024):
        for u in (1, 3, 5, 11):
            z, x = 2 ** (m + 3) * u - 3, 3 * 2**m * u - 1
            need(physical_odd_step(z) == (x, 3), "fixed reset valuation")
            need(clock(z) == 0 and clock(x) == m - 1 and x < z < 4 * x,
                 "recharge budget and height ratio")
            if u == 1:
                need(run_count(z) == run_count(x) == 2, "constant binary run resource")
                need(z.bit_count() == m + 2 and x.bit_count() == m + 1,
                     "popcount resource difference")
            current = x
            for _ in range(m - 1):
                current, a = physical_odd_step(current)
                need(a == 1, "recharged actual valuation-one step")
            need(current == 2 * 3**m * u - 1 and physical_odd_step(current)[1] >= 2,
                 "recharged exact terminal state")
            recharge_edges += m
            recharge_families += 1
    return {
        "status": "PASS", "schema": "arithmetic-independent-review-v1",
        "reviewed_source_sha256": expected,
        "review_checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "complete_even_word_lengths": [1, 16], "complete_even_words": even_words,
        "exact_entropy_checks": entropy_checks,
        "arbitrary_source_clock_accounting_edges": accounting_edges,
        "independently_constructed_blocks": cases,
        "literal_block_edges": edges, "distinct_state_pair_checks": pair_checks,
        "selected_prime_block_checks": prime_block_checks,
        "selected_primes": list(chosen_primes),
        "recharge_families": recharge_families, "literal_recharge_edges": recharge_edges,
        "limits": ["No production code imported.",
                   "Uniform prime-set claims rest on the separately reconstructed written proof, not selected primes.",
                   "Finite ordinary sources vary with requested block length.",
                   "No all-time ordinary orbit or global convergence conclusion."]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compare", type=Path)
    args = parser.parse_args()
    result = run()
    if args.compare:
        need(json.loads(args.compare.read_text()) == result, "independent report mismatch")
    if args.output:
        args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "complete_even_words": result["complete_even_words"],
                      "independent_blocks": len(result["independently_constructed_blocks"]),
                      "block_edges": result["literal_block_edges"],
                      "pair_checks": result["distinct_state_pair_checks"],
                      "clock_accounting_edges": result["arbitrary_source_clock_accounting_edges"],
                      "recharge_edges": result["literal_recharge_edges"]}, sort_keys=True))


if __name__ == "__main__":
    main()
