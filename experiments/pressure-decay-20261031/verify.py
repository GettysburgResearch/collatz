"""Standalone exact checker: no producer or repository imports; raw shortcut clocks."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def pairs(items: list[tuple[str, object]]) -> dict:
    result = {}
    for k, v in items:
        require(k not in result, "duplicate JSON key")
        result[k] = v
    return result


def integer(x: object) -> int:
    require(type(x) is int, "integer, not bool, required")
    return x


def rational(pair: list) -> Fraction:
    require(type(pair) is list and len(pair) == 2, "rational pair required")
    a, b = map(integer, pair)
    require(b > 0, "positive denominator required")
    q = Fraction(a, b)
    require([q.numerator, q.denominator] == pair, "canonical rational required")
    return q


def encode(q: Fraction) -> list[int]:
    return [q.numerator, q.denominator]


def canonical(x: object) -> bytes:
    return (json.dumps(x, sort_keys=True, separators=(",", ":")) + "\n").encode()


def algebra(data: dict) -> None:
    require(set(data) == {"schema", "status", "parent", "bank", "shadows", "power_barriers", "norms", "controls", "energy"}, "top-level schema")
    require(data["schema"] == "pressure-decay-20261031/v2", "schema version")
    require(data["status"] == "FINITE_REGRESSIONS_ONLY", "evidence status")
    require(data["parent"] == "6bee3183ff7f29f2e20ca88ab94bc7745c1af602", "parent pin")
    require(data["bank"]["cutoff"] == 4095 and data["bank"]["sources"] == 2048, "bank inventory")
    require(data["bank"]["root_residual"] == [1, 4], "cycle is not a fixed vector")
    require(data["bank"]["uniform_missing_source_error"] == [1, 8192], "source-tail bound")
    expected = [(m, k) for m in range(1, 33) for k in range(1, 25)]
    require(len(data["shadows"]) == len(expected), "shadow inventory")
    for row, key in zip(data["shadows"], expected):
        require(len(row) == 6, "shadow row width")
        m, k, x, t, jn, jd = map(integer, row)
        require((m, k) == key, "shadow order")
        require(x == 2*m*2**k-1 and t == 2*m*3**k-1, "ordinary shadow sources")
        z = x
        for _ in range(k):
            require(z % 2 == 1, "literal odd shortcut event")
            z = (3*z+1)//2
            require(z % 2 == 1, "no hidden halving in all-one block")
        require(z == t and (jn, jd) == (3**k, 2**k), "literal shadow endpoint/weight")
        require(x % m == t % m, "common residue")
    labels = [(m,k,p,d) for m in range(1,33) for k in (1,2,4)
              for p,d in ((0,1),(1,2),(1,1),(3,2),(7,4),(15,8))]
    require(len(data["power_barriers"]) == len(labels), "power inventory")
    for row, label in zip(data["power_barriers"], labels):
        require(len(row) == 7, "power row width")
        m,k,p,d,u,x,t = map(integer, row)
        require((m,k,p,d) == label and 1 <= u <= 16384, "power labels")
        require((x,t) == (2*m*u*2**k-1, 2*m*u*3**k-1), "power sources")
        ratio = Fraction(3**k,2**k)**(2*d) * Fraction(x,t)**p
        require(ratio > 1 and x % m == t % m, "strict non-contraction")
        for old in range(1,u):
            require(Fraction(3**k,2**k)**(2*d) * Fraction(2*m*old*2**k-1,2*m*old*3**k-1)**p <= 1, "canonical first witness")
    require(len(data["norms"]) == 32, "norm inventory")
    for seed, row in enumerate(data["norms"], 1):
        require(row[0] == seed and len(row) == 4, "norm row")
        direct = Fraction(0)
        finite = Fraction(0)
        for t in range(1,128,2):
            f = Fraction((seed*37+t*11)%19-9,7)
            for a in range(1,19):
                numerator = 2**a*t-1
                if numerator % 3 == 0:
                    x = numerator//3
                    require(x > 0 and x % 2 == 1, "inverse positivity/parity")
                    finite += Fraction(9,4**a)*f*f
            if t % 3:
                first = 1 if t % 3 == 2 else 2
                direct += Fraction(9,4**first) / (1-Fraction(1,16)) * f*f
        require(rational(row[1]) == direct and rational(row[2]) == finite, "complete norm identity")
        require(rational(row[3]) == direct-finite, "exact infinite tail")
    control = data["controls"]
    require(set(control) == {"toy", "cycles"} and len(control["toy"]) == 80, "controls inventory")
    for r, row in enumerate(control["toy"], 1):
        require(row[0] == r and len(row) == 3, "toy row")
        t = 2**r-1
        target, weight, total = t, 1, Fraction(0)
        while target > 0 and target % 2:
            total += Fraction(weight*weight,t*t)
            if target % 4 != 3:
                break
            target = (target-1)//2
            weight *= 2
        require(total == rational(row[1:]) == Fraction(4**r-1,3*t*t), "toy nondecay control")
    require(len(control["cycles"]) == 2, "cycle inventory")
    for row, expected in zip(control["cycles"], ((3,[1]),(5,[13,33,83]))):
        p, nodes, multiplier = row
        require((p,nodes) == expected, "cycle identity")
        actual = Fraction(1)
        for i,n in enumerate(nodes):
            y = p*n+1
            actual *= p
            while y % 2 == 0:
                y //= 2
                actual /= 2
            require(y == nodes[(i+1)%len(nodes)], "literal cycle path")
        require(rational(multiplier) == actual and 0 < actual < 1, "cycle kills fixed vectors")


def rebuild(data: dict, supplied_profile: list) -> dict:
    profile: dict[int,Fraction] = {}
    boundary: dict[int,Fraction] = {}
    raw_steps = 0
    count_records = 0
    checks = 0
    for source in range(1,4096,2):
        n = source
        weight = Fraction(1)
        seen: dict[int,Fraction] = {}
        clock = 0
        while True:
            if n % 2:
                if n in seen:
                    require(n == 1, "unclassified finite source")
                    break
                seen[n] = weight
                profile[n] = profile.get(n,Fraction(0)) + weight*weight
                require(weight*source <= n, "source bound")
                count_records += 1
                n = (3*n+1)//2
                weight *= Fraction(3,2)
            else:
                n //= 2
                weight /= 2
            clock += 1
            require(clock <= 100000, "raw replay resource cap")
        raw_steps += clock
        for t,j in seen.items():
            v = seen[1]/j
            require(t not in boundary or boundary[t] == v, "cross-source first-hit agreement")
            boundary[t] = v
        for exponent in range(17):
            y = 2**exponent
            count = sum(t <= y for t in seen)
            require(count**40 <= 5**40*y**39, "path packing")
            checks += 1
    rows = [[t,*encode(q)] for t,q in sorted(profile.items())]
    require(rows == supplied_profile, "full profile differs from raw-clock reconstruction")
    bank = data["bank"]
    require(hashlib.sha256(canonical(rows)).hexdigest() == bank["profile_sha256"], "profile digest")
    require(bank["profile_entries"] == len(rows) and bank["max_target"] == max(profile), "profile inventory")
    require(bank["odd_records"] == count_records and bank["packing_checks"] == checks, "replay counts")
    require(bank["dirichlet_edges"] == len(boundary), "Dirichlet inventory")
    for n,v in boundary.items():
        endpoint = 3*n+1
        coefficient = Fraction(3)
        while endpoint % 2 == 0:
            endpoint //= 2
            coefficient /= 2
        require(v-coefficient*boundary[endpoint] == (Fraction(1,4) if n == 1 else 0), "first-hit versus harmonic control")
    require(bank["mean_floor_bits"] == 60 and len(bank["mean_rows"]) == 17, "mean inventory")
    for exponent,row in enumerate(bank["mean_rows"]):
        y = 2**exponent
        terms = [h/Fraction(t*t) for t,h in profile.items() if t <= y]
        low = sum((q*(2**60)).numerator//(q*(2**60)).denominator for q in terms)
        require(row == [y,low,len(terms)], "exact mean enclosure")
    return {"raw_shortcut_steps": raw_steps, "odd_records": count_records,
            "profile_entries": len(rows), "packing_checks": checks,
            "dirichlet_edges": len(boundary)}



def rebuild_energy() -> tuple[dict, int]:
    """Separate raw shortcut replay; reconstruct sums by integer power scaling."""
    cutoff, horizon, bits = 4095, 40, 80
    snapshots = [dict() for _ in range(horizon+1)]
    e_floor = [0]*(horizon+1)
    maxima = [cutoff]*(horizon+1)
    active = [0]*(horizon+1)
    raw_steps = 0
    spike = None
    for source in range(1, cutoff+1, 2):
        n, divisions, maximum = source, 0, source
        hit = source == 1
        for clock in range(horizon+1):
            numerator, denominator = 9**clock, 4**divisions
            e_floor[clock] += (numerator*(1<<bits))//(denominator*n*n)
            snapshots[clock][n] = snapshots[clock].get(n,Fraction(0)) + Fraction(numerator,denominator)
            maxima[clock] = max(maxima[clock], maximum)
            active[clock] += not hit
            if source == 27 and clock == 32:
                j = Fraction(3**clock,2**divisions)
                require(j == Fraction(1853020188851841,17592186044416), "literal excursion multiplier")
                lower = j**4/(n*n)
                require(n == 3077 and lower > 13, "literal moment excursion")
                spike = [source,clock,n,encode(j*j),encode(lower)]
            if clock == horizon:
                break
            # One shortcut odd event, then all subsequent even events.
            require(n % 2 == 1, "odd clock boundary")
            n = (3*n+1)//2
            divisions += 1
            raw_steps += 1
            while n % 2 == 0:
                n //= 2
                divisions += 1
                raw_steps += 1
            hit |= n == 1
            maximum = max(maximum,n)
    rows = []
    for clock, population in enumerate(snapshots):
        s_floor = 0
        for n, weight in population.items():
            scaled = weight*weight*(1<<bits)/(n*n)
            s_floor += scaled.numerator//scaled.denominator
        e_upper = Fraction(e_floor[clock]+2048,1<<bits)
        s_upper = Fraction(s_floor+len(population),1<<bits)
        theta = e_upper+Fraction(1,8192)
        full_upper = 2*s_upper+Fraction(12,5)**clock/4096
        rows.append([clock,e_floor[clock],s_floor,len(population),maxima[clock],active[clock],
                     encode(theta),encode(full_upper)])
    return {"cutoff":cutoff,"horizon":horizon,"dyadic_bits":bits,
            "source_count":2048,"rows":rows,"spike":spike,
            "decrement_checks":2048*horizon}, raw_steps


def energy_match(data: dict, expected: dict) -> None:
    supplied = data["energy"]
    require(type(supplied) is dict and supplied.keys() == expected.keys(), "energy schema")
    require(supplied == expected, "energy differs from complete raw-clock reconstruction")
    for row in supplied["rows"]:
        require(len(row) == 8, "energy row width")
        for value in row[:6]:
            integer(value)
        rational(row[6])
        rational(row[7])
    for key in ("cutoff","horizon","dyadic_bits","source_count","decrement_checks"):
        integer(supplied[key])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(), object_pairs_hook=pairs)
    profile_path = args.input.with_suffix(args.input.suffix+".profile.json")
    profile = json.loads(profile_path.read_text(), object_pairs_hook=pairs)
    algebra(data)
    replay = rebuild(data,profile)
    expected_energy, energy_raw_steps = rebuild_energy()
    energy_match(data,expected_energy)
    mutations = [
        ("shadow source", lambda d: d["shadows"][0].__setitem__(2,5)),
        ("shadow target", lambda d: d["shadows"][0].__setitem__(3,7)),
        ("shadow derivative", lambda d: d["shadows"][0].__setitem__(4,4)),
        ("missing power row", lambda d: d["power_barriers"].pop()),
        ("infinite norm tail", lambda d: d["norms"][0].__setitem__(3,[0,1])),
        ("toy pressure", lambda d: d["controls"]["toy"][2].__setitem__(1,999)),
        ("cycle multiplier", lambda d: d["controls"]["cycles"][0].__setitem__(2,[1,1])),
        ("false proof status", lambda d: d.__setitem__("status","PROVED_COLL ATZ")),
    ]
    rejected = []
    for name,change in mutations:
        bad = copy.deepcopy(data)
        change(bad)
        try:
            algebra(bad)
        except (ValueError,TypeError,KeyError):
            rejected.append(name)
        else:
            raise ValueError("mutation accepted: "+name)
    try:
        json.loads('{"x":1,"x":2}',object_pairs_hook=pairs)
    except ValueError:
        rejected.append("duplicate JSON key")
    else:
        raise ValueError("duplicate-key control accepted")
    for name,change in [
        ("energy clock",lambda d: d["energy"]["rows"][32].__setitem__(0,33)),
        ("energy upper bound",lambda d: d["energy"]["rows"][32].__setitem__(6,[0,1])),
        ("moment excursion",lambda d: d["energy"]["spike"].__setitem__(4,[1,1])),
        ("missing energy row",lambda d: d["energy"]["rows"].pop()),
    ]:
        bad=copy.deepcopy(data)
        change(bad)
        try:
            energy_match(bad,expected_energy)
        except (ValueError,TypeError,KeyError):
            rejected.append(name)
        else:
            raise ValueError("energy mutation accepted: "+name)
    print(json.dumps({"status":"PASS", "replay":replay,
                      "energy_raw_steps":energy_raw_steps,"energy_clocks":41,
                      "energy_source_clock_pairs":2048*41,
                      "shadow_rows":len(data["shadows"]), "power_rows":len(data["power_barriers"]),
                      "norm_rows":len(data["norms"]), "mutations_rejected":rejected},sort_keys=True))


if __name__ == "__main__":
    main()
