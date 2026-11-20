#!/usr/bin/env python3
"""Exact finite support for CR1--CR2 and TP1--TP2; not a Collatz proof."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def pair(value: F) -> list[int]:
    return [value.numerator, value.denominator]


def v2(n: int) -> int:
    require(n > 0, "valuation needs a positive numerator")
    return (n & -n).bit_length() - 1


def odd_step(n: int) -> tuple[int, int]:
    require(n > 0 and n % 2 == 1, "odd state domain")
    numerator = 3 * n + 1
    a = v2(numerator)
    return numerator >> a, a


def replay(n: int, exponents: list[int]) -> int:
    for a in exponents:
        require(a >= 1, "positive exponent")
        n, actual = odd_step(n)
        require(actual == a, "wrong exact accelerated valuation")
    return n


def inverse_affine(a: int, z: tuple[F, F]) -> tuple[F, F]:
    return F(2**a, 3) * z[0], (2**a * z[1] - 1) / 3


def word_correction(word: list[int]) -> tuple[int, int]:
    B = A = 0
    for a in word:
        require(a >= 1, "formal word exponent")
        B = 3*B + 2**A
        A += a
    return B, A


def carry_algebra() -> dict:
    E = [2, 1, 1, 1, 2, 1, 7]
    V = [3, 6, 1, 2, 1, 1, 1]
    Be, Ae = word_correction(E)
    Bv, Av = word_correction(V)
    require((Be, Ae) == (3709, 15), "carry source prefix")
    require((Bv, Av) == (149617, 15), "carry target prefix")
    require(Bv == 5*Be+4*2**15, "carry four creation")
    # All expressions are affine in the actual odd state z.
    middle_source = (F(3, 2), F(1, 2))
    middle_target = (F(15, 2), F(13, 2))
    require(middle_target == (5*middle_source[0],
                              5*middle_source[1]+4), "carry preservation")
    # Formal common denominator 2^(b+3), for source(3,b), target(4,b-1).
    require((9*5, 9*4+19) == (5*9, 5*11), "carry killing")
    require((31*pow(16, -1, 27)) % 27 == 7, "run-positive exit residue")
    require((1417*pow(1024, -1, 27)) % 27 == 7, "run-zero exit residue")
    C = F(2**20, 3**9)-(F(1351, 81)+F(65536, 19683))/5
    require(C == F(4849051, 98415) and C > 49, "safe carry height")
    rows = []
    for r in range(25):
        b = r+2
        B, A = word_correction(E+[1]*r+[3, b])
        target_B, target_A = word_correction(V+[1]*r+[4, b-1])
        require(B == 1351*3**(r+5)+2**(r+16), "full carry correction")
        require(A == r+b+18 and target_A == A, "full carry clocks")
        require(target_B == 5*B, "full proportional endpoint correction")
        rows.append([r, b, B, A])
    return {"source_prefix": E, "target_prefix": V,
            "prefix_corrections": [Be, Bv], "prefix_clock": 15,
            "safe_height_constant": pair(C),
            "checked_run_lengths": [0, 24],
            "correction_formula": "1351*3^(r+5)+2^(r+16)",
            "correction_transcript_sha256": hashlib.sha256(
                json.dumps(rows, separators=(",", ":")).encode()).hexdigest()}


def block_affines(target_prefix: tuple[int, ...] = (1, 2, 5)) -> dict:
    # Formal variable t=2^b*q, b>=6. No finite substitution in b is used.
    source = (F(1, 3), F(-1, 3))
    for a in (1, 1, 1):
        source = inverse_affine(a, source)
    target = (F(5, 96), F(-1, 3))
    for a in reversed(target_prefix):
        target = inverse_affine(a, target)
    require(source == (F(8, 81), F(-65, 81)), "source formal identity")
    require(target == tuple(5 * z for z in source), "target formal identity")
    require(sum(target_prefix) - 5 == 3, "same total shortcut clock")
    return {"source_in_t": [pair(z) for z in source],
            "target_in_t": [pair(z) for z in target],
            "odd_count_each": 4, "common_clock": "b+3",
            "formal_variable": "t=2^b*q; b>=6"}


def root_upper(base: F, power_num: int = 21, power_den: int = 25,
               bits: int = 60) -> F:
    """An exact rational upper enclosure of base**(power_num/power_den)."""
    require(0 < base <= 1, "root enclosure domain")
    denominator = 1 << bits
    lo, hi = 0, denominator
    rhs = base.numerator**power_num * denominator**power_den
    scale = base.denominator**power_num
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**power_den * scale >= rhs:
            hi = mid
        else:
            lo = mid
    require(hi**power_den * scale >= rhs, "upper root enclosure failed")
    return F(hi, denominator)


def coefficients() -> dict:
    comparisons = [(3, 4, 393, 500), (15, 76, 13, 50),
                   (5, 52, 7, 50), (81, 499, 11, 50),
                   (81, 32755, 1, 125), (98415, 4849051, 1, 25),
                   (1, 2, 9, 16)]
    rows = []
    for n, d, u, v in comparisons:
        require(n**21 * v**25 < d**21 * u**25,
                "rational power comparison failed")
        rows.append({"base": [n, d], "power": [21, 25],
                     "strict_upper": [u, v],
                     "integer_test": "n^21*v^25 < d^21*u^25",
                     "passed": True})
    require(F(126, 25) > 5, "geometric tail exponent")
    require(13 * 2**54 > 499, "new harmonic coefficient <1/6")
    a = F(393, 500)
    old = F(32, 31) * F(13, 50) * a / (1 - a)
    require(old == F(81744, 82925), "old ladder rational sum")
    new_restricted = F(32, 31) * F(1, 125)
    require(new_restricted < F(1, 100), "restricted new kernel")
    coupled = old + F(1, 100)
    other = F(32, 31) * (
        F(13, 50) * a + F(7, 50) * a * a / (1 - a) + F(11, 50))
    require(coupled == F(330293, 331700), "coupled coefficient")
    require(other == F(8865224, 10365625), "other endpoint coefficient")
    require(0 < other < coupled < 1, "positive subcritical contraction")
    require(F(16, 21) + F(1, 6) == F(13, 14), "harmonic coefficient")
    t, G0 = F(9, 16), F(65536, 65535)
    require(F(21, 25)*2*3**8 > 16, "carry inverse period factor")
    carry_rows = []
    for b0, bound in [(0, F(1, 300)), (6, F(1, 8)), (12, F(1, 8))]:
        S = sum((a**j*t**((b0-j-2) % 18) for j in range(18)), F(0))/(1-a**18)
        K = G0*S/25
        require(K < bound, "coupled carry rational polynomial")
        carry_rows.append({"b0": b0, "exact_rational_upper": pair(K),
                           "strict_simple_upper": pair(bound)})
    full = coupled+F(1, 300)
    require(full == F(248549, 248775) and full < 1, "three-family coefficient")
    require(other+F(1, 8) < full, "q16/25 full comparison")
    last = F(32, 31)*(F(7, 50)*a/(1-a)+F(11, 50))+G0/(25*(1-a))
    require(last == F(1026910336, 1086897975) and last < full,
            "other endpoint full comparison")
    require(5**25 < 6**4*4**25, "harmonic exponent interpolation")
    return {"power_comparisons": rows,
            "two_family_q_7_mod_27_coefficient": pair(coupled),
            "two_family_other_q_coefficient": pair(other),
            "two_family_harmonic_coefficient": [13, 14],
            "new_restricted_bound": pair(new_restricted),
            "carry_rational_polynomials": carry_rows,
            "three_family_q7_coefficient": pair(full),
            "three_family_q16_or25_bound": pair(other+F(1, 8)),
            "three_family_other_bound": pair(last),
            "three_family_subcritical_margin": pair(1-full),
            "three_family_harmonic_coefficient": [4, 5]}


def residue_checks() -> dict:
    require(len({pow(2, j, 81) for j in range(54)}) == 54,
            "order modulo81")
    require(pow(2, 54, 81) == 1, "return modulo81")
    require(len({pow(2, j, 27) for j in range(18)}) == 18,
            "order modulo27")
    require(pow(2, 18, 27) == 1, "return modulo27")
    require(pow(2, 15, 27) == 17, "restricted exponent15")
    require((7 * 17 - 65) % 27 == 0, "restricted endpoint equation")
    data = []
    restricted = []
    for q in range(1, 81):
        if q % 3 == 0:
            continue
        clocks = [L for L in range(9, 63) if (2**L * q - 65) % 81 == 0]
        require(len(clocks) == 1, "one complete inverse clock class")
        L = clocks[0]
        if q % 27 == 7:
            require(L >= 15 and L % 18 == 15, "endpoint-coupled guard")
            restricted.append([q, L])
        data.append([q, L])
    require([q for q in range(27) if (4*q - 1) % 27 == 0] == [7],
            "ladder b4 requires q7 mod27")
    carry = []
    for q in range(1, 27):
        if q % 3 == 0:
            continue
        b0s = [b for b in range(18) if (2**b*q-7) % 27 == 0]
        require(len(b0s) == 1, "carry endpoint clock residue")
        carry.append([q, b0s[0]])
    require([row for row in carry if row[0] % 9 == 7]
            == [[7, 0], [16, 12], [25, 6]], "carry three special cases")
    require([q for q in range(9) if (4*q-1) % 9 == 0] == [7],
            "all ladder runs b4 need q7 mod9")
    return {"unit_residues_mod81": len(data),
            "clock_classes": data,
            "restricted_classes": restricted,
            "ladder_b4_residue_mod27": 7,
            "carry_endpoint_classes": carry}


def actual_new_block() -> dict:
    rows = []
    for k in range(256):
        x = 271 + 512 * k
        if x % 3 == 0:
            continue
        z = x
        word = []
        for _ in range(4):
            z, a = odd_step(z)
            word.append(a)
        require(word[:3] == [1, 1, 1] and word[3] >= 6, "new cylinder word")
        q, b = z, word[3]
        require(q % 3 != 0 and q % 2 == 1, "actual endpoint domain")
        require(replay(5*x, [1, 2, 5, b-5]) == 5*q, "new target path")
        require(sum(word) == sum([1, 2, 5, b-5]), "clock equality")
        require(6*q <= x, "new height contraction")
        L = b + 3
        require(81*x + 65 == 2**L*q, "new inverse equality")
        require((2**(L+54)*q - 65)//81
                == 2**54*x + 65*(2**54-1)//81, "geometric fiber")
        rows.append([x, q, b])
    return {"checked_sources": len(rows), "parameter_k_range": [0, 255],
            "first_rows": rows[:6],
            "transcript_sha256": hashlib.sha256(
                json.dumps(rows, separators=(",", ":")).encode()).hexdigest()}


def classify_source(x: int) -> tuple[str, int] | None:
    require(x > 0 and x % 2 and x % 3, "source classifier domain")
    if x % 512 == 271:
        q = replay(x, [1, 1, 1])
        q, b = odd_step(q)
        require(b >= 6, "new source classifier")
        return "new", q
    z, r = x, 0
    while z != 1:
        q, a = odd_step(z)
        if a == 2:
            r += 1
            z = q
            continue
        if r and a >= 4:
            return "ladder", q
        break
    z = x
    for expected in [2, 1, 1, 1, 2, 1, 7]:
        z, actual = odd_step(z)
        if actual != expected:
            return None
    r = 0
    while True:
        z, actual = odd_step(z)
        if actual == 1:
            r += 1
            continue
        if actual != 3:
            return None
        z, b = odd_step(z)
        return ("carry", z) if b >= r+2 else None
    return None


def carry_lift(r: int, b: int) -> tuple[int, int]:
    require(r >= 0 and b >= 2, "carry lift domain")
    A = r+b+18
    modulus = 3**(r+9)
    B = 1351*3**(r+5)+2**(r+16)
    q = (B*pow(2**A, -1, modulus)) % modulus
    if q % 2 == 0:
        q += modulus
    while q < 5:
        q += 2*modulus
    for _ in range(3):
        require((2**A*q-B) % modulus == 0, "carry lift integrality")
        x = (2**A*q-B)//modulus
        if x > 0 and x % 3:
            return x, q
        q += 2*modulus
    raise RuntimeError("carry unit lift missing")


def actual_carry() -> dict:
    E = [2, 1, 1, 1, 2, 1, 7]
    V = [3, 6, 1, 2, 1, 1, 1]
    rows = []
    for r in range(25):
        for extra in (0, 1, 3):
            b = r+2+extra
            x, q = carry_lift(r, b)
            require(replay(x, E+[1]*r+[3, b]) == q, "actual carry source")
            require(replay(5*x, V+[1]*r+[4, b-1]) == 5*q, "actual carry target")
            require(classify_source(x) == ("carry", q), "carry classification")
            require(49*q < x, "safe carry actual height")
            require((2**b*q-7) % 27 == 0, "actual coupled exit")
            rows.append([r, b, x, q])
    # The omitted exit region is a real issue: this entire fixed word expands.
    r, b = 20, 2
    x, q = carry_lift(r, b)
    require(replay(x, E+[1]*r+[3, b]) == q, "unsafe carry source")
    require(replay(5*x, V+[1]*r+[4, b-1]) == 5*q, "unsafe carry target")
    require(3**(r+9) > 2**(r+b+18) and q > x, "unsafe expanding control")
    require(classify_source(x) is None, "unsafe exit must not enter safe kernel")
    return {"safe_actual_sources": len(rows),
            "safe_run_lengths": [0, 24], "extra_exit_values": [0, 1, 3],
            "first_safe_rows": rows[:3],
            "safe_transcript_sha256": hashlib.sha256(
                json.dumps(rows, separators=(",", ":")).encode()).hexdigest(),
            "unsafe_expanding_example": {"r": r, "b": b, "x": x, "q": q},
            "scope": "finite replay; the written formulas prove all r"}


def rank_family_review() -> dict:
    """Independent CF4 arithmetic and one unshared large first-hit fixture."""
    modulus = 3**10
    base = pow(4, 81, modulus)
    require(base == (1+178*3**5) % modulus, "CF4 base congruence")
    require((178*88*2**16-1351-81) % 243 == 0, "CF4 unit coefficient")
    modular_rows = []
    for r in range(13):
        m = 3**(r+10)
        t = 88*pow(2, -r, 243) % 243
        b = 2*3**(r+4)*t-2
        residue = (pow(2, r+b+18, m)-1351*3**(r+5)-pow(2, r+16, m)) % m
        require(residue == 3**(r+9), "CF4 whole numerator congruence")
        modular_rows.append([r, t, b])
    r = 4
    t = 88*pow(2, -r, 243) % 243
    b = 2*3**(r+4)*t-2
    numerator = 2**(r+b+18)-1351*3**(r+5)-2**(r+16)
    require(numerator % 3**(r+9) == 0, "CF4 fixture full divisibility")
    x = numerator//3**(r+9)
    require(x > 0 and x % 2 and x % 3 == 1, "CF4 fixture domain")
    source = [2, 1, 1, 1, 2, 1, 7]+[1]*r+[3, b]
    target = [3, 6, 1, 2, 1, 1, 1]+[1]*r+[4, b-1, 4]
    for initial, word in [(x, source), (5*x, target)]:
        z = initial
        for a in word:
            require(z > 1, "CF4 fixture premature first hit")
            z = replay(z, [a])
        require(z == 1, "CF4 fixture final endpoint")
    require(len(source) == r+9 and len(target) == r+10, "CF4 first-hit ranks")
    require(sum(target) == sum(source)+4, "CF4 clocks")
    return {"base_congruence_modulus": modulus, "base_residue": base,
            "modular_indices": [0, 12], "modular_rows": modular_rows,
            "independent_first_hit_fixture": {
                "r": r, "t": t, "b": b, "source_bits": x.bit_length(),
                "source_rank": len(source), "target_rank": len(target),
                "source_clock": sum(source), "target_clock": sum(target)},
            "large_values_omitted": True,
            "scope": "independent finite fixture, not all-rank enumeration"}


def finite_fibers() -> dict:
    cutoff = 16384
    fibers: dict[int, list[int]] = {}
    counts = {"ladder": 0, "new": 0, "carry": 0, "zero_endpoint_sources": 0}
    for x in range(1, cutoff+1, 2):
        if x % 3 == 0:
            continue
        result = classify_source(x)
        if result is None:
            continue
        kind, q = result
        counts[kind] += 1
        require(6*q <= x and q <= cutoff//6, "finite cutoff retained")
        if q == 1:
            counts["zero_endpoint_sources"] += 1
            continue
        fibers.setdefault(q, []).append(x)
    exact_harmonic_max = F(0)
    enclosed_subcritical_max = F(0)
    for q, sources in fibers.items():
        require(len(sources) == len(set(sources)), "source multiplicity")
        harmonic = sum((F(q, x) for x in sources), F(0))
        subcritical = sum((root_upper(F(q, x)) for x in sources), F(0))
        require(harmonic < F(4, 5), "finite harmonic fiber bound")
        require(subcritical < F(248549, 248775),
                "finite subcritical upper-enclosed fiber bound")
        exact_harmonic_max = max(exact_harmonic_max, harmonic)
        enclosed_subcritical_max = max(enclosed_subcritical_max, subcritical)
    return {"cutoff": cutoff, "counts": counts, "distinct_endpoints": len(fibers),
            "max_harmonic_finite_fiber": pair(exact_harmonic_max),
            "max_subcritical_finite_fiber_rational_upper":
                pair(enclosed_subcritical_max),
            "root_enclosures": "integer 25th-power comparisons, 60 binary places",
            "scope": "finite actual fibers; not the all-source proof"}


def first_hit(n: int, budget: int) -> tuple[int, int]:
    L = p = 0
    while n != 1:
        require(L < budget, "certified replay budget exhausted")
        p += n % 2
        n = (3*n+1)//2 if n % 2 else n//2
        L += 1
    return L, p


def phase_checks() -> dict:
    seeds = []
    for n, expected in [(1, (0, 0)), (5, (4, 1)), (25, (16, 7))]:
        L, p = first_hit(n, 32)
        require((L, p) == expected, "literal seed certificate")
        seeds.append([n, L, p, L-2*p])
    prefix_rows = []
    for a in range(2, 41):
        x = (4**a - 1)//3
        require(replay(x, [2*a]) == 1, "rank-one source certificate")
        require((x % 3 != 0) == (a % 3 != 0), "rank-one unit condition")
        y = 5*x
        word = [2] + [1]*(2*a-3) + [3]
        require(len(word) == 2*a-1, "target prefix odd count")
        z = y
        for power in word:
            require(z > 1, "premature target first hit")
            z = replay(z, [power])
        require(z == (5*9**(a-1)-1)//4 and z > 1, "target prefix endpoint")
        require(sum(word) == 2*a+2, "target prefix clock")
        prefix_rows.append([a, x, z])
    require(F(20, 3) < 8 and F(6, 5)**4 > 2, "phase rational constants")
    terminal_rows = []
    for D in range(-30, 16):
        a = max(2, 7-2*D)
        while a % 3 == 0:
            a += 1
        require(F(13-2*a, 4) < D, "explicit terminal phase cutoff")
        require(F(20, 3)*F(5, 6)**(2*a-1) < F(2)**D,
                "exact phase upper bound excludes terminal")
        terminal_rows.append([D, a])
    family_rows = []
    for k in range(13):
        L = 17 + 18*k
        require((5*2**L - 7) % 9 == 0, "family integrality")
        x = (5*2**L - 7)//9
        require(x % 2 and x % 3 and x % 64 == 49, "family source domain")
        require(replay(x, [2, L-2]) == 5, "family first arm")
        require(replay(5*x, [5, L-5]) == 25, "family second arm")
        first = first_hit(x, L+17)
        second = first_hit(5*x, L+17)
        require(first == (L+4, 3), "family first exact first-hit data")
        require(second == (L+16, 9), "family second exact first-hit data")
        Hx, Hy = first[0]-2*first[1], second[0]-2*second[1]
        require(Hx == Hy == L-2, "family zero phase")
        family_rows.append([k, L, x, Hx, Hy])
    # Four ordinary edge types: alpha=3^j/2^k, H(start)-H(end)=k-2j.
    signed_edges = [
        {"kind": "forward_even", "j": 0, "k": 1, "slope": [1, 2], "grade": 1},
        {"kind": "forward_odd", "j": 1, "k": 1, "slope": [3, 2], "grade": -1},
        {"kind": "reverse_even", "j": 0, "k": -1, "slope": [2, 1], "grade": -1},
        {"kind": "reverse_odd", "j": -1, "k": -1, "slope": [2, 3], "grade": 1},
    ]
    for row in signed_edges:
        require(F(3)**row["j"]/F(2)**row["k"] == F(*row["slope"]),
                "signed edge slope")
        require(row["k"]-2*row["j"] == row["grade"], "signed edge grade")
    return {"literal_seed_certificates": seeds,
            "rank_one_prefix_a_range": [2, 40],
            "rank_one_prefixes": len(prefix_rows),
            "rank_one_transcript_sha256": hashlib.sha256(
                json.dumps(prefix_rows, separators=(",", ":")).encode()).hexdigest(),
            "terminal_cutoff_tests": terminal_rows,
            "certified_zero_phase_family": family_rows,
            "signed_native_edges": signed_edges,
            "scope": "no unproved target convergence used"}


def negative_controls() -> list[str]:
    rejected = []
    for bad in [(1, 2, 4), (1, 3, 5)]:
        try:
            block_affines(bad)
        except RuntimeError:
            rejected.append("incorrect target prefix "+repr(bad))
        else:
            raise RuntimeError("incorrect target prefix accepted")
    try:
        replay(271, [1, 1, 1, 5])
    except RuntimeError:
        rejected.append("incorrect exact final source valuation")
    else:
        raise RuntimeError("incorrect source valuation accepted")
    require((pow(2, 14, 27)*7-65) % 27 != 0, "bad coupled clock control")
    rejected.append("clock14 cannot serve q7 mod27")
    require((4*16-1) % 27 != 0, "bad ladder residue control")
    rejected.append("b4 cannot serve q16 mod27 at run length>=2")
    return rejected


def main() -> None:
    report = {
        "schema": "collatz-coupled-renewal-phase-check/v1",
        "status": "PASS",
        "scope": "exact algebra, rational inequalities and stated finite replays; not Collatz",
        "sources": {
            "PR146": "fd991063721e9c157d318e40bb20131762f7d750",
            "PR157": "64361ecca770092d6c8242dc6211e38818af2e50",
            "PR163": "051237135a34ae7d4b973ee5fcf5da04ded6f0fc",
            "PR166": "5996b9f525ca50978bc34f423192c36a87765bf3"},
        "block_affine_identity": block_affines(),
        "carry_algebra": carry_algebra(),
        "rational_coefficients": coefficients(),
        "endpoint_congruences": residue_checks(),
        "actual_new_block": actual_new_block(),
        "actual_carry_blocks": actual_carry(),
        "independent_rank_family_review": rank_family_review(),
        "finite_inverse_fibers": finite_fibers(),
        "phase_checks": phase_checks(),
        "negative_controls_rejected": negative_controls(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
