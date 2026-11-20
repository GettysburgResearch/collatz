#!/usr/bin/env python3
"""Independent physical-affine and congruence review; imports no reviewed code."""

from fractions import Fraction
from pathlib import Path
import argparse
import json


HERE = Path(__file__).resolve().parent
DEFAULT_PACKET = HERE / "expanding_return_certificate.json"
M, K = 2**38, 3**24
D = K - M


def require(ok, label):
    if not ok:
        raise RuntimeError(label)


def vp2(n):
    if not n:
        raise ValueError("zero has infinite valuation")
    n = abs(n)
    return (n & -n).bit_length() - 1


def physical_rows(a0, stride, clocks):
    """Replay both ordinary arms as literal affine polynomials in u>=0."""
    arms = [(a0, stride), (3 * a0 - 1, 3 * stride)]
    rows = []
    for h in range(clocks + 1):
        rows.append(tuple(arms))
        if h == clocks:
            break
        next_arms = []
        for constant, coefficient in arms:
            require(coefficient % 2 == 0, "parity varies on claimed cylinder")
            require(constant > 0 and coefficient > 0, "positive cylinder lost")
            parity = constant % 2
            multiplier = 3 if parity else 1
            next_arms.append(((multiplier * constant + parity) // 2,
                              multiplier * coefficient // 2))
        arms = next_arms
    return rows


def zero_at_nonnegative_real(c, d):
    if not d:
        return c == 0
    return Fraction(-c, d) >= 0


def inspect_macro(payload):
    a0 = payload["source"]
    require(payload["source_stride"] == 2*M, "wrong stated cylinder stride")
    require(vp2(a0+2) < 39, "shadow valuation is not fixed on the full cylinder")
    rows = physical_rows(a0, 2 * M, 38)
    supplied = payload["rows"]
    require(len(supplied) == 39, "wrong number of supplied physical rows")
    word = ""
    for h, ((xc, xs), (yc, ys)) in enumerate(rows):
        require(supplied[h]["X"] == [xc, xs] and supplied[h]["Y"] == [yc, ys],
                "physical affine coefficient mismatch")
        level, offset, orientation = supplied[h]["state"]
        base, other = rows[h][orientation], rows[h][1 - orientation]
        require(other == (3**level * base[0] + offset, 3**level * base[1]),
                "reported canonical state fails its physical identity")
        if h < 38:
            word += str(base[0] % 2)
        if 0 < h < 38:
            for left, right in ((rows[h][0], rows[h][1]),
                                (rows[h][1], rows[h][0])):
                require(not zero_at_nonnegative_real(left[0] - 3*right[0] + 1,
                                                     left[1] - 3*right[1]),
                        "earlier physical section possible")
        require((level, offset) != (0, 0), "affine merger state")
        if 0 < h < 38:
            require((level, offset) != (1, -1), "earlier symbolic return")
    require(word == payload["word"], "word disagrees with physical base parities")
    require(supplied[-1]["state"] == [1, -1, 0], "wrong final orientation")
    b0 = payload["endpoint"]
    require(rows[-1] == ((b0, 2*K), (3*b0 - 1, 6*K)), "wrong return endpoints")
    c = payload["C"]
    require(M * b0 - K * a0 == c > 0 and K > M, "expansion formula")
    require(a0 == (-c * pow(D, -1, 2*M)) % (2*M), "domain valuation class")

    floor = (2*a0-1, 4*M)
    margins = [(y[0]-floor[0], y[1]-floor[1]) for x, y in rows]
    require(all(c > 0 and d > 0 for c, d in margins), "physical floor violation")
    require(margins[18] == tuple(payload["minimum_margin"]), "wrong minimum row")
    require(all(c >= margins[18][0] and d >= margins[18][1] for c, d in margins),
            "row 18 does not dominate all floor margins")
    for j, (x, y) in enumerate(rows):
        k = j
        while rows[k][1][0] % 2 == 0:
            k += 1
            require(k <= 38, "oddpart needs an unseen endpoint digit")
        require(y == (2**(k-j)*rows[k][1][0], 2**(k-j)*rows[k][1][1]),
                "oddpart was not an actual halving run")

    for i in range(39):
        for j in range(39):
            x, y = rows[i][0], rows[j][1]
            require(not zero_at_nonnegative_real(x[0]-y[0], x[1]-y[1]),
                    "independent-clock meeting possible on macro cylinder")
    ordered = sorted((arm[0], arm[1], label+str(h))
                     for h, pair in enumerate(rows)
                     for label, arm in zip(("X", "Y"), pair))
    require(len({z[0] for z in ordered}) == 78, "joint constants not all distinct")
    require(all(left[1] <= right[1] for left, right in zip(ordered, ordered[1:])),
            "slopes do not preserve joint constant ordering")
    return {"source_shadow_valuation": vp2(a0+2),
            "full_cylinder_shadow_valuation": vp2(a0+2),
            "physical_rows": 39, "cross_arm_equations": 1521,
            "section_equations": 74, "minimum_margin": margins[18],
            "domain_is_resource_at_least": 39,
            "joint_strict_order": [z[2] for z in ordered]}


def build_schedule(names, cylinders):
    """Independent construction by modular inverses at macro boundaries."""
    first = cylinders[names[0]]
    residue, stride = first["source"], 2*M
    endpoint, coefficient = first["endpoint"], 2*K
    for name in names[1:]:
        target = cylinders[name]
        require(endpoint % 2 == target["source"] % 2 == 0, "wrong boundary parity")
        lift = (((target["source"]-endpoint)//2)
                * pow(coefficient//2, -1, M)) % M
        residue += stride * lift
        stride *= M
        input_base = endpoint + coefficient * lift
        numerator = K * input_base + target["C"]
        require(numerator % M == 0, "boundary does not give an integral return")
        endpoint = numerator // M
        coefficient *= K
    r = len(names)
    require(stride == 2*M**r and coefficient == 2*K**r, "schedule stride")
    require(0 < residue < stride, "not a least positive source class")
    rows = physical_rows(residue, stride, 38*r)
    require(rows[-1][0] == (endpoint, coefficient), "schedule endpoint identity")
    base = residue
    bases = [base]
    for k, name in enumerate(names):
        macro = cylinders[name]
        require(base >= macro["source"]
                and (base-macro["source"]) % (2*M) == 0, "macro domain incompatibility")
        next_base = (K*base + macro["C"]) // M
        require(next_base > base, "boundary does not expand")
        require(rows[38*(k+1)][0][0] == next_base, "physical boundary mismatch")
        base = next_base
        bases.append(base)
    original_floor = 2*residue-1, 2*stride
    for x, y in rows:
        require(y[0] > original_floor[0] and y[1] > original_floor[1],
                "concatenation loses original floor")

    # Equal slopes at different physical clocks are impossible by the
    # independent powers of two in 3^q/2^clock. Any remaining cross-block
    # equality excludes at most one rational lift, hence finitely many.
    forbidden = []
    equations = 0
    for i, (x, _) in enumerate(rows):
        for j, (_, y) in enumerate(rows):
            equations += 1
            dc, ds = x[0]-y[0], x[1]-y[1]
            if ds == 0:
                require(i == j, "equal cross-arm slopes at unequal clocks")
                require(dc != 0, "identical cross-arm affine maps")
            elif zero_at_nonnegative_real(dc, ds):
                forbidden.append(Fraction(-dc, ds))
    lower_lift = max([0] + [v.numerator//v.denominator + 1 for v in forbidden])
    for i, (x, _) in enumerate(rows):
        for j, (_, y) in enumerate(rows):
            require(x[0]+x[1]*lower_lift != y[0]+y[1]*lower_lift,
                    "selected large ordinary lift meets within horizon")

    c_f, c_g = cylinders["F"]["C"], cylinders["G"]["C"]
    pairs = [[vp2(D*a+c_f), vp2(D*a+c_g)] for a in bases]
    return {"names": names, "source": residue, "stride": stride,
            "bases": bases, "valuation_pairs": pairs,
            "cross_horizon_equations": equations,
            "nonnegative_real_roots": len(forbidden),
            "all_lifts_from_this_bound_avoid_cross_meetings": lower_lift}


def inspect_control(control):
    a = control["a"]
    floor = 2*a-1
    require(floor == control["original_floor"], "wrong control floor")
    xs, ys = control["X_orbit_to_1"], control["Y_orbit_to_1"]
    require(xs[0] == a and ys[0] == 3*a-1, "wrong control sources")
    for label, values in (("X", xs), ("Y", ys)):
        require(values[-1] == 1 and 1 not in values[:-1], "control first hitting time")
        require(len(values)-1 == control[label+"_hitting_time"] == 236,
                "wrong control hitting clock")
        for n, next_n in zip(values, values[1:]):
            require(n > 0 and next_n == ((3*n+1)//2 if n % 2 else n//2),
                    "control orbit contains a nonordinary edge")
    literal = next(j for j, y in enumerate(ys) if y < floor)
    oddpart = next(j for j, y in enumerate(ys) if y//(y & -y) < floor)
    require(literal == control["first_literal_bad_arm_descent"] == 42,
            "wrong first literal descent")
    require(oddpart == control["first_oddpart_bad_arm_descent"] == 40,
            "wrong first oddpart descent")
    meetings = [(max(i,j), i+j, i, j, x) for i, x in enumerate(xs)
                for j, y in enumerate(ys) if x == y]
    first = min(meetings)
    require(control["first_meeting_by_max_clock"]
            == {"X_clock": first[2], "Y_clock": first[3], "value": first[4]}
            == {"X_clock": 65, "Y_clock": 65, "value": 7710330710},
            "wrong first independent-clock control meeting")
    return {"X_hitting_time": 236, "Y_hitting_time": 236,
            "first_literal_descent": literal, "first_oddpart_descent": oddpart,
            "first_meeting_by_max_clock": control["first_meeting_by_max_clock"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT_PACKET,
                        help="committed certificate JSON; defaults to neighboring fixture")
    args = parser.parse_args()
    payload = json.loads(args.certificate.read_text())
    cylinders = payload["cylinders"]
    require(payload["M"] == M and payload["K"] == K and payload["D"] == D,
            "wrong declared common constants")
    macros = {name: inspect_macro(data) for name, data in cylinders.items()}
    for name in macros:
        require(macros[name]["joint_strict_order"]
                == payload["summaries"][name]["joint_strict_order"],
                "joint-order certificate disagrees with independent ordering")
    names = ["F", "G", "FF", "FG", "GF", "GG", "FGF", "GFG", "FGFG", "FGGF", "GFFG"]
    schedules = {name: build_schedule(name, cylinders) for name in names}
    exact = schedules["FGFG"]
    require(exact["source"] == payload["finite_alternating_path"]["source"],
            "independent construction disagrees with reported alternating source")
    require(exact["valuation_pairs"][:3] == [[47, 9], [9, 47], [47, 9]],
            "claimed resource-pair cycle fails")
    c_f, c_g = cylinders["F"]["C"], cylinders["G"]["C"]
    require(vp2(c_g-c_f) == 9, "wrong separation valuation")

    # Exact composite arithmetic for every reviewed finite block. The written
    # proof applies the same identity to arbitrary period length.
    periodic = {}
    for name in names:
        numerator_slope, constant, denominator = 1, 0, 1
        for letter in name:
            constant = K*constant + cylinders[letter]["C"]*denominator
            numerator_slope *= K
            denominator *= M
        gap = numerator_slope - denominator
        require(gap > 0 and constant > 0 and gap % 2, "wrong composite fixed point")
        a = schedules[name]["source"]
        b = schedules[name]["bases"][-1]
        require(denominator*(gap*b+constant)
                == numerator_slope*(gap*a+constant), "composite valuation identity")
        require(vp2(gap*b+constant) == vp2(gap*a+constant)-38*len(name),
                "composite resource does not decrease exactly")
        periodic[name] = {"length": len(name), "valuation_drop": 38*len(name),
                          "negative_fixed_point": str(Fraction(-constant, gap))}
    report = {"status": "independent physical and congruence review passed",
              "macros": macros, "finite_schedules": schedules,
              "periodic_composite_checks": periodic,
              "convergent_control": inspect_control(payload["convergent_control"]),
              "claim_boundary": "finite schedules only; infinite aperiodic positive schedules not excluded"}
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
