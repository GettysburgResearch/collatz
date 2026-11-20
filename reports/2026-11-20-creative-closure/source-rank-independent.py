#!/usr/bin/env python3
"""Independent literal carry-block controls for CSR-001; no target convergence."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


SWAPS = {"ae": "ea", "af": "eb", "ag": "fa", "be": "fb", "bf": "ga", "bg": "gb"}


def cross(prefix, token="g"):
    remaining = list(prefix.translate(str.maketrans("01", "ab")))
    exceptional = 0
    emitted = []
    while remaining:
        pair = remaining.pop() + token
        result = SWAPS[pair]
        token = result[0]
        emitted.append(result[1])
        exceptional += pair == "af"
    return token, exceptional


def first_hit(n, cap):
    start, odd = n, 0
    for clock in range(cap + 1):
        if n == 1:
            return clock, odd
        require(clock < cap, "supplied finite certificate exhausted")
        if n % 2:
            odd += 1
            n = (3 * n + 1) // 2
        else:
            n //= 2
    raise ValueError("unreachable: " + str(start))


def run():
    base = 1 << 54
    quotient = (base - 1) // 81
    require(81 * quotient == base - 1, "54-bit integer quotient")
    w, v = format(13 * quotient, "054b"), format(13 * quotient - 2, "054b")
    require(w == "001010010001011000011111100110101101110100111100000011", "W transcription")
    require(v == "001010010001011000011111100110101101110100111100000001", "V transcription")
    rows = [{"block": "V without final one", "start": "g", "result": cross(v[:-1])}]
    require(cross(v[:-1]) == ("e", 9), "first block")
    for token in "efg":
        result = cross(w, token)
        require(result == ("e", 9), "repeating block")
        rows.append({"block": "W", "start": token, "result": result})
    require(cross("1", "e") == ("f", 0), "leftmost binary digit")
    rank_four = []
    for j in range(1, 7):
        numerator = (1 << (54 * j + 8)) - 175
        require(numerator % 81 == 0, "rank-four integrality")
        n = numerator // 81
        require(bin(n)[2:] == "11" + w * (j - 1) + v, "rank-four binary identity")
        require(cross(bin(n)[3:-1]) == ("f", 9 * j), "rank-four marked carry")
        clock, odd = first_hit(n, 54 * j + 8)
        require((clock, odd) == (54 * j + 8, 4), "rank-four first-hit certificate")
        rank_four.append({"j": j, "first_hit_clock": clock, "odd_inputs": odd, "forced_first_token_carries": 9 * j})
    rank_two = []
    for t in range(1, 13):
        n = ((1 << (6 * t + 4)) - 7) // 9
        require(bin(n)[2:] == "111000" * t + "1", "rank-two binary identity")
        require(cross(bin(n)[3:-1]) == ("g", t), "rank-two marked carry")
        require(first_hit(n, 6 * t + 4) == (6 * t + 4, 2), "rank-two first-hit certificate")
        rank_two.append({"t": t, "forced_first_token_carries": t})

    target_residue_witnesses = []
    for t in range(1, 4):
        bits, target = 6 * t + 1, ((1 << (6 * t + 4)) - 7) // 9
        modulus, order = 1 << bits, 1 << (bits - 3)
        require(pow(9, order, modulus) == 1 and pow(9, order // 2, modulus) != 1, "order control")
        residue = 1
        for exponent in range(order):
            if residue == target:
                break
            residue = residue * 9 % modulus
        else:
            raise ValueError("missing 1-mod-8 residue")
        q = ((exponent - 13) * pow(27, -1, order)) % order + order
        j = 2 * q + 1
        power = 27 * j - 1
        require(power > bits and pow(3, power, modulus) == target, "pure-power target residue")
        require(cross(("111000" * t), "g") == ("g", t), "whole low blocks")
        target_residue_witnesses.append({"t": t, "j": j, "power_of_three_exponent": power,
                                        "modulus_bits": bits, "low_bits_value": target,
                                        "convergence_tested": False})
    return {"schema": "collatz-creative-source-rank-independent/v1", "status": "PASS",
            "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
            "scope": "fixed literal-rule block certificate and bounded ordinary first-hit controls; no pure-power convergence tested",
            "blocks": rows, "rank_two_controls": rank_two, "rank_four_controls": rank_four,
            "target_residue_witnesses": target_residue_witnesses,
            "universal_arguments": "marked-token ordering and valuation proof are in the manuscript and review"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--output", type=Path)
    modes.add_argument("--compare", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.output:
        with args.output.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(rendered)
    if args.compare:
        require(args.compare.read_text(encoding="utf-8") == rendered, "frozen report mismatch")
    print(json.dumps({"status": "PASS", "ordinary_first_hit_controls": 18,
                      "pure_power_residue_controls": 3, "target_convergence_tested": False,
                      "report_sha256": sha256(rendered.encode()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
