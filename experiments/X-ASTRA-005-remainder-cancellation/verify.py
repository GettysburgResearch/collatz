#!/usr/bin/env python3
"""Separate physical reconstruction of X-ASTRA-005; imports no generator."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path

D = 16
LIMIT = 65536


def require(condition: bool, explanation: str) -> None:
    if not condition:
        raise ValueError(explanation)


def sha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, separators=(",", ":"), sort_keys=True).encode()).hexdigest()


def t(n: int) -> int:
    require(n > 0, "positive input")
    if n % 2 == 0:
        return n >> 1
    return (n + (n << 1) + 1) >> 1


def depth(n: int) -> int:
    z, power, exponent = 2*n+1, 3, 0
    while z % power == 0:
        exponent += 1
        power *= 3
    return exponent


def p(n: int) -> int:
    require(n >= 1, "global rank domain")
    z = 2*n+1
    return z*z // (3**depth(n))


def physical(n: int, steps: int) -> tuple[str, int]:
    bits = []
    for _ in range(steps):
        bits.append(str(n % 2))
        n = t(n)
    return "".join(bits), n


def check_word(n: int, expected: str) -> int:
    actual, endpoint = physical(n, len(expected))
    require(actual == expected, "wrong physical word")
    return endpoint


def to_section(n: int) -> tuple[int, str]:
    # At least one physical step, unlike a test for membership at time zero.
    y, bits = n, []
    for _ in range(n.bit_length()+4):
        bits.append(str(y % 2))
        y = t(y)
        if y % 3 == 1:
            return y, "".join(bits)
    raise ValueError("finite first-section bound violated")


def inverse_mod(a: int, m: int) -> int:
    old_r, r, old_s, s = a, m, 1, 0
    while r:
        q = old_r // r
        old_r, r = r, old_r-q*r
        old_s, s = s, old_s-q*s
    require(old_r == 1, "non-coprime CRT moduli")
    return old_s % m


def join(a: int, m: int, b: int, k: int) -> int:
    return (a + m*((b-a)*inverse_mod(m, k) % k)) % (m*k)


def lift(r: int, j: int, h: int, unit: int, shift: int) -> int:
    modulus = 3**(h+1)
    twice = unit*3**h-1
    if twice % 2:
        twice += modulus
    residue = (twice//2) % modulus
    n = join(r, 2**j, residue, modulus)
    if not n:
        n = 2**j*modulus
    return n + shift*2**j*modulus


def reconstruct_basis() -> tuple[list[dict], list[list[int]]]:
    tiles, layers = [], []
    for j in range(1, D+1):
        records = []
        groups: dict[int, dict[int, int]] = {}
        codes = set()
        # Exhaust the actual odd source residue classes at this depth.
        for source in range(1, 2**j, 2):
            bits, endpoint = physical(source, j)
            q = bits.count("1")
            code = int(bits[::-1], 2)
            require(code not in codes, "physical parity bijection")
            codes.add(code)
            # B is reconstructed from endpoints, NOT the affine B recurrence.
            b = 2**j*(2*endpoint+1) - 3**q*(2*source+1)
            require(2**j-1 <= b <= 3**j-2**j, "shifted remainder range")
            groups.setdefault(b, {})
            groups[b][q] = min(code, groups[b].get(q, code))
            records.append((code, source, bits, q, b))
        fresh, hits = [], 0
        for code, r, v, q, b in sorted(records):
            if q+2 not in groups[b]:
                continue
            hits += 1
            # Prefix coverage is tested in SOURCE residues rather than word codes.
            if any(r % (2**old["j"]) == old["r"] for old in tiles):
                continue
            w = format(groups[b][q+2], "0"+str(j)+"b")[::-1]
            n0 = join(r, 2**j, 4, 9)
            require(n0 >= 13, "ordinary positive quotient")
            fresh.append(dict(j=j, r=r, v=v, w=w, B=b, q=q,
                              n0=n0, x0=(n0-4)//9,
                              source_step=9*2**j, quotient_step=2**j))
        fresh.sort(key=lambda row: row["r"])
        layers.append([j, len(records), len(groups), hits, len(fresh)])
        tiles.extend(fresh)
    return tiles, layers


def rule_trials(tiles: list[dict]) -> dict:
    cases = []
    for index, rule in enumerate(tiles):
        for h in [2, 3, 12]:
            for unit in [1, 2]:
                for shift in [0, 1]:
                    n = lift(rule["r"], rule["j"], h, unit, shift)
                    require(n % 9 == 4 and n % 2 == 1 and depth(n) == h, "CRT guards")
                    x = (n-4)//9
                    require(x >= 1 and x % 2 == 1 and p(n) == 9*p(x), "ternary quotient rank")
                    endpoint = check_word(x, rule["w"])
                    require(check_word(n, rule["v"]) == endpoint, "ordinary shared endpoint")
                    if h == 2:
                        y, bits = to_section(x)
                        require(check_word(x, bits) == y and p(y) < p(x), "return of nonsection witness")
                    cases.append([index, h, unit, shift, n, x, endpoint])
    return dict(cases=len(cases), sha256=sha(cases))


def normalize_all(tiles: list[dict]) -> dict:
    rows, remaining_h2 = [], []
    counts: Counter = Counter()
    for n in range(1, LIMIT+1):
        h = depth(n)
        v, w = "", ""
        if n == 1:
            tag, x = "base", 1
        elif h == 0:
            tag = "h0"
            if n % 2:
                x, v = to_section(n)
            else:
                x, v = t(n), "0"
        elif h == 1:
            tag = "h1"
            x, v = to_section(n)
        elif n % 2 == 0:
            tag, x, v, w = "even_high", (n-1)//3, "0", "1"
        else:
            x = (n-4)//9
            matches = [rule for rule in tiles if n % 2**rule["j"] == rule["r"]]
            require(len(matches) <= 1, "prefix-free cylinder coverage")
            if matches:
                rule = matches[0]
                tag, v, w = "homogeneous", rule["v"], rule["w"]
                if h == 2 and n % 1296 in [139, 427, 571, 859, 1003]:
                    remaining_h2.append(n)
            else:
                tag = "unresolved_lift"  # Not a certificate of convergence or merging.
            require(x > 0 and p(n) == 9*p(x), "lower rank alone is only an obligation")
        if tag != "base" and tag != "unresolved_lift":
            require(p(x) < p(n), "strict rank decrease")
            require(check_word(n, v) == check_word(x, w), "valid finite merging diagram")
        rows.append([n, tag, x, v, w])
        counts[tag] += 1
    return dict(cutoff=LIMIT, counts=dict(sorted(counts.items())), sha256=sha(rows),
                previous_h2_residual_hits=remaining_h2)


def shield_trials() -> dict:
    cases = []
    for length in [1, 2, 4, 8, 16, 32, 64]:
        h = 3*length
        for shift in [0, 1, 7]:
            n = lift(21, 7, h, 1, shift)
            x = (n-4)//9
            require(depth(n) == h and p(n) == 9*p(x), "shield source rank")
            require(check_word(n, "1000001") == check_word(x, "1011100"), "fixed diagram")
            y = n
            for j in range(1, length+1):
                y = t(y)
                require(depth(y) < j, "bounded valuation at arbitrary physical prefix")
                require(p(y)*4**length > p(n)*3*9**length, "forward barrier with exact constants")
            cases.append([length, h, shift, n, x, y])
    return dict(cases=len(cases), forward_steps=sum(row[0] for row in cases),
                sha256=sha(cases), rows=cases)


def phases() -> list[dict]:
    def path(n: int) -> list[int]:
        seen = set()
        sequence = [n]
        while sequence[-1] != 1:
            require(sequence[-1] not in seen and len(sequence) <= 1000, "phase test does not terminate")
            seen.add(sequence[-1])
            sequence.append(t(sequence[-1]))
        return sequence
    controls = []
    for n in [13, 859]:
        x = (n-4)//9
        a, b = path(n), path(x)
        pairs = [(i, k, u) for i, u in enumerate(a) for k, v in enumerate(b) if u == v]
        first = min(pairs)
        require((len(a)-len(b)) % 2 == 1, "opposite phase not proved")
        left, right = n, x
        for _ in range(max(len(a), len(b))+2):
            require(left != right, "false synchronization control")
            left, right = t(left), t(right)
        controls.append(dict(n=n, x=x, Pn=p(n), Px=p(x), tau_n=len(a)-1, tau_x=len(b)-1,
                             first_merge=list(first), paths_sha256=sha([a, b])))
    return controls


def reconstruct() -> dict:
    tiles, layers = reconstruct_basis()
    trials = rule_trials(tiles)
    core, shield, controls = normalize_all(tiles), shield_trials(), phases()
    # Enumerate the residue union directly; don't use the generator's weighted sum.
    covered = {r for row in tiles for r in range(row["r"], 2**D, 2**row["j"])}
    require(all(r % 2 for r in covered), "odd-source coverage")
    h2_count = len([r for r in covered if r % 16 == 11])
    scope = dict(collatz_proved=False, complete_merging_cover=False,
                 max_word_length=D, rank_domain="all positive integers",
                 quotient="(n-4)/9", exact_depths_for_rule_replay=[2, 3, 12])
    counts = dict(prefix_free_rules=len(tiles), covered_odd_residues=len(covered),
                  odd_residues=2**(D-1), covered_h2_dyadic_factor=h2_count,
                  h2_dyadic_factor=2**(D-4), rule_replay_cases=trials["cases"],
                  shield_cases=shield["cases"], shield_forward_steps=shield["forward_steps"])
    full = dict(schema=1, scope=scope, counts=counts, word_layers=layers, tiles=tiles,
                rule_tests=trials, core=core, shield=shield, phase_controls=controls)
    examples = [row for j, r in [(7, 21), (10, 587)]
                for row in tiles if row["j"] == j and row["r"] == r]
    report = dict(schema=1, scope=scope, counts=counts, word_layers=layers,
                  examples=examples, core=core, rule_tests=trials,
                  shield={k: v for k, v in shield.items() if k != "rows"},
                  phase_controls=controls, tiles_sha256=sha(tiles),
                  full_payload_sha256=sha(full))
    report["semantic_sha256"] = sha(report)
    return report


def validate(report: dict, expected: dict) -> None:
    body = dict(report)
    claimed = body.pop("semantic_sha256", None)
    require(claimed == sha(body), "report digest mismatch")
    require(report == expected, "physical, mathematical, coverage, or scope mismatch")


def self_test(expected: dict) -> int:
    changed = []
    for k in range(8):
        obj = copy.deepcopy(expected)
        if k == 0:
            obj["scope"]["collatz_proved"] = True
        elif k == 1:
            obj["scope"]["max_word_length"] = 15
        elif k == 2:
            obj["counts"]["prefix_free_rules"] -= 1
        elif k == 3:
            obj["examples"][0]["B"] += 2
        elif k == 4:
            obj["examples"][1]["w"] = "0"+obj["examples"][1]["w"][1:]
        elif k == 5:
            obj["word_layers"].pop()
        elif k == 6:
            obj["phase_controls"][1]["first_merge"][0] += 1
        else:
            obj["core"]["counts"]["unresolved_lift"] = 0
        obj.pop("semantic_sha256")
        obj["semantic_sha256"] = sha(obj)  # Reseal: rejection cannot rely on stale hash.
        changed.append(obj)
    for obj in changed:
        try:
            validate(obj, expected)
        except ValueError:
            continue
        raise ValueError("resealed false report was accepted")
    return len(changed)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    expected = reconstruct()
    validate(json.loads(args.report.read_text()), expected)
    if args.self_test:
        print("RESEALED TAMPER REJECTIONS", self_test(expected))
    print("PHYSICAL RECONSTRUCTION PASS", expected["semantic_sha256"])


if __name__ == "__main__":
    main()
