"""Exact infinite-cylinder certificates for two expanding ordinary Q returns.

No floating point and no sampled-source assertion is used by this verifier.
The default run reads the committed certificate and prints JSON to stdout.
Only --write-certificate regenerates the explicit certificate fixture.
"""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import argparse
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
M = 2**38
K = 3**24
D = K - M
SPECS = {
    "F": {
        "word": "01111111110101110011011011101111110000",
        "source": 210578993150,
        "endpoint": 216364159964,
        "C": 610948284866,
        "minimum_constant": 5745969920,
    },
    "G": {
        "word": "01111111101110110011011011101111110000",
        "source": 341135408638,
        "endpoint": 350507308538,
        "C": 613397164994,
        "minimum_constant": 9308401408,
    },
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def v2(n):
    require(n != 0, "v2(0) is not a finite resource")
    return (abs(n) & -abs(n)).bit_length() - 1


def T(n):
    require(n > 0, "literal positive orbit left its domain")
    return (3*n+1)//2 if n % 2 else n//2


def affine_step(z):
    c, q = z
    require(q % 2 == 0, "parity is not fixed on this cylinder")
    return ((3*c+1)//2, 3*q//2) if c % 2 else (c//2, q//2)


def canonical_step(s, d, e, bit):
    if d % 2 == 0:
        return s, (3*d+1-3**s)//2 if bit else d//2, e
    if s > 0:
        return (s-1, (d-3**(s-1))//2, e) if bit else (s+1, (3*d+1)//2, e)
    return (1, (1-3*d)//2, e ^ 1) if bit else (1, (3*d+1)//2, e)


def same_affine_relation(x, y, s, d, e):
    b, other = (x, y) if e == 0 else (y, x)
    return other == (3**s*b[0]+d, 3**s*b[1])


def no_nonnegative_real_root(c, q):
    # c+q*u cannot vanish for any real u >= 0.
    return c != 0 and (q == 0 or (c > 0) == (q > 0))


def build(name):
    p = SPECS[name]
    x = (p["source"], 2*M)
    y = (3*p["source"]-1, 6*M)
    s, d, e = 1, -1, 0
    rows = []
    for h in range(39):
        rows.append({"clock": h, "X": list(x), "Y": list(y), "state": [s,d,e]})
        if h < 38:
            bit = (x if e == 0 else y)[0] % 2
            s,d,e = canonical_step(s,d,e,bit)
            x,y = affine_step(x),affine_step(y)
    return {
        "name": name, "word": p["word"], "source": p["source"],
        "source_stride": 2*M, "endpoint": p["endpoint"], "C": p["C"],
        "minimum_margin": [p["minimum_constant"], 15000928256], "rows": rows,
    }


def validate(data):
    name = data["name"]
    require(name in SPECS, "unrecognized macro")
    p = SPECS[name]
    for key in ("word", "source", "endpoint", "C"):
        require(data[key] == p[key], f"changed declared {key}")
    require(data["source_stride"] == 2*M, "changed cylinder stride")
    require(len(data["rows"]) == 39, "wrong number of affine rows")
    x = (p["source"], 2*M)
    y = (3*p["source"]-1, 6*M)
    s,d,e = 1,-1,0
    word = ""
    xs,ys,states = [],[],[]
    for h,row in enumerate(data["rows"]):
        require(row == {"clock": h, "X": list(x), "Y": list(y), "state": [s,d,e]},
                f"bad affine/state row {h}")
        require(same_affine_relation(x,y,s,d,e), f"canonical relation failed at {h}")
        xs.append(x); ys.append(y); states.append((s,d,e))
        if h < 38:
            bit = (x if e == 0 else y)[0] % 2
            word += str(bit)
            s,d,e = canonical_step(s,d,e,bit)
            x,y = affine_step(x),affine_step(y)
    require(word == p["word"], "parity word mismatch")
    require(states[-1] == (1,-1,0), "not an unchanged Q return")
    require(all(z[:2] != (1,-1) for z in states[1:-1]), "earlier canonical return")
    require(all(z[:2] != (0,0) for z in states), "an affine meeting occurred")
    require(xs[-1] == (p["endpoint"], 2*K), "endpoint formula mismatch")
    require(ys[-1] == (3*p["endpoint"]-1, 6*K), "bad-arm endpoint mismatch")
    require(p["endpoint"]*M-K*p["source"] == p["C"], "wrong affine offset")
    require(K > M and p["C"] > 0, "return is not strictly expanding")
    floor = (2*p["source"]-1, 4*M)
    margins = [(y[0]-floor[0], y[1]-floor[1]) for y in ys]
    require(all(c > 0 and q > 0 for c,q in margins), "a bad-arm floor guard survives")
    minimum = (min(c for c,q in margins), min(q for c,q in margins))
    require(minimum == margins[18] == tuple(data["minimum_margin"]), "bad minimum margin")
    require(minimum == (p["minimum_constant"],15000928256), "changed minimum claim")
    # Every even run finishes at a fixed odd row within the certificate.
    require(ys[-1][0] % 2 == 1 and ys[-1][1] % 2 == 0, "unseen endpoint halvings")
    oddpart_targets = []
    for j in range(39):
        k = next(k for k in range(j,39) if ys[k][0] % 2)
        require(ys[j] == (ys[k][0]*2**(k-j),ys[k][1]*2**(k-j)),
                f"bad oddpart certificate at {j}")
        oddpart_targets.append(k)
    # These are algebraic identities/inequalities in a real free parameter,
    # not tests at finitely many ordinary source values.
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            require(no_nonnegative_real_root(x[0]-y[0],x[1]-y[1]),
                    f"possible nonnegative cross-arm meeting: {i},{j}")
    joint = sorted((z[0],z[1],f"{arm}{j}") for arm,zs in (("X",xs),("Y",ys))
                   for j,z in enumerate(zs))
    require(all(a[0] < b[0] and a[1] <= b[1] for a,b in zip(joint,joint[1:])),
            "joint strict-order certificate failed")
    for h in range(1,38):
        x,y = xs[h],ys[h]
        for z,t in ((y,x),(x,y)):
            require(no_nonnegative_real_root(z[0]-3*t[0]+1,z[1]-3*t[1]),
                    f"possible earlier numerical section: {h}")
    return {
        "name": name, "clocks": 38, "cross_arm_equations": 1521,
        "intermediate_section_equations": 74, "minimum_margin": list(minimum),
        "minimum_clock": 18, "source_v2_a_plus_2": v2(p["source"]+2),
        "oddpart_targets": oddpart_targets,
        "physical_X_word": "".join(str(x[0]%2) for x in xs[:-1]),
        "physical_Y_word": "".join(str(y[0]%2) for y in ys[:-1]),
        "joint_strict_order": [z[2] for z in joint],
        "fixed_point": str(Fraction(-p["C"],D)),
    }


def decode_word(word):
    # Independent lift construction: choose one new original source bit
    # at each canonical step. Intermediate x,y may be signed at residue 0.
    r,x,y,ax,ay,s,d,e = 0,0,-1,1,3,1,-1,0
    for h,ch in enumerate(word):
        bit = int(ch)
        lift = (bit-(x if e == 0 else y)) % 2
        r += lift*2**h; x += lift*ax; y += lift*ay
        ox,oy = x%2,y%2
        x = (3*x+1)//2 if ox else x//2
        y = (3*y+1)//2 if oy else y//2
        ax *= 3**ox; ay *= 3**oy
        s,d,e = canonical_step(s,d,e,bit)
    modulus = 2**len(word)
    # One additional bit makes the final good arm even and bad arm odd.
    r += (x%2)*modulus
    return r,2*modulus


def macro_path(names):
    word = "".join(SPECS[n]["word"] for n in names)
    a,stride = decode_word(word)
    require(a > 0, "constructed finite source is not positive")
    bases = [a]
    for name in names:
        p = SPECS[name]
        require((a-p["source"]) % (2*M) == 0 and a >= p["source"], "invalid macro cylinder")
        b,nrem = divmod(K*a+p["C"],M)
        require(nrem == 0 and b > a, "macro did not strictly increase")
        bases.append(b);a=b
    return {"names": names, "source": bases[0], "stride": stride,
            "bases": bases, "valuation_pairs": [[v2(D*b+SPECS["F"]["C"]),
              v2(D*b+SPECS["G"]["C"])] for b in bases]}


def orbit(n, budget=10000):
    out=[n]
    for _ in range(budget):
        if out[-1] == 1:
            return out
        out.append(T(out[-1]))
    raise ValueError("modest orbit certificate budget exceeded")


def convergence_certificate():
    a=SPECS["F"]["source"];floor=2*a-1
    xs,ys=orbit(a),orbit(3*a-1)
    literal=next(j for j,y in enumerate(ys) if y < floor)
    oddpart=next(j for j,y in enumerate(ys) if y//(y&-y) < floor)
    positions={}
    for i,x in enumerate(xs):positions.setdefault(x,i)
    meetings=[(max(positions[y],j),positions[y]+j,positions[y],j,y)
              for j,y in enumerate(ys) if y in positions]
    first=min(meetings)
    return {"a": a, "original_floor": floor, "X_orbit_to_1": xs,
            "Y_orbit_to_1": ys, "X_hitting_time": len(xs)-1,
            "Y_hitting_time": len(ys)-1, "first_literal_bad_arm_descent": literal,
            "first_oddpart_bad_arm_descent": oddpart,
            "first_meeting_by_max_clock": {"X_clock": first[2],"Y_clock": first[3],"value": first[4]}}


def reconstruct():
    data={name:build(name) for name in SPECS}
    summaries={name:validate(payload) for name,payload in data.items()}
    corruptions=[]
    for label in ("affine_row","word","minimum","offset"):
        bad=deepcopy(data["F"])
        if label=="affine_row":bad["rows"][18]["Y"][0]+=1
        if label=="word":bad["word"]="1"+bad["word"][1:]
        if label=="minimum":bad["minimum_margin"][0]+=1
        if label=="offset":bad["C"]+=2
        try:validate(bad)
        except ValueError:corruptions.append(label)
        else:raise ValueError(f"corrupted {label} was accepted")
    require(v2(SPECS["F"]["source"]+2)==12,"wrong source shadow depth")
    require(v2(SPECS["G"]["C"]-SPECS["F"]["C"])==9,"wrong resource separation")
    for p in SPECS.values():
        require((D*p["source"]+p["C"])%(2*M)==0,"safe cylinder is not the exact resource zero class")
    alternating=macro_path("FGFG")
    require(alternating["valuation_pairs"][:3]==[[47,9],[9,47],[47,9]],"valuation cycle failed")
    repeats=[macro_path("F"*r) for r in (1,2,3,4)]
    for p in repeats:
        a=p["source"];r=len(p["names"])
        require(r <= v2(D*a+SPECS["F"]["C"])//38,"repetition budget failed")
    convergence=convergence_certificate()
    payload={"M":M,"K":K,"D":D,"cylinders":data,"summaries":summaries,
             "corruptions_rejected":corruptions,"finite_repetitions":repeats,
             "finite_alternating_path":alternating,"convergent_control":convergence}
    report_summaries={name:{k:v for k,v in s.items() if k not in ("oddpart_targets","joint_strict_order")}
                      for name,s in summaries.items()}
    report={"status":"exact affine cylinder verification passed","summaries":report_summaries,
            "corruptions_rejected":corruptions,
            "alternating_valuation_pairs":alternating["valuation_pairs"],
            "convergent_control":{k:v for k,v in convergence.items() if "orbit" not in k}}
    return payload,report


def validate_literal_control(control):
    require(control["a"]==SPECS["F"]["source"],"wrong convergent control source")
    for key,start in (("X_orbit_to_1",control["a"]),("Y_orbit_to_1",3*control["a"]-1)):
        values=control[key]
        require(values and values[0]==start and values[-1]==1,"wrong literal orbit endpoints")
        require(all(type(n) is int and n>0 for n in values),"nonordinary literal orbit value")
        require(all(T(n)==m for n,m in zip(values,values[1:])),"invalid literal ordinary step")
        require(1 not in values[:-1],"literal control does not stop at its first 1")


def validate_supplied_schedule(path):
    names=path["names"]
    require(names and all(n in SPECS for n in names),"bad supplied macro schedule")
    bases=path["bases"]
    require(len(bases)==len(names)+1 and bases[0]==path["source"],"bad supplied schedule bases")
    require(path["stride"]==2*M**len(names),"bad supplied schedule stride")
    for name,a,b in zip(names,bases,bases[1:]):
        p=SPECS[name]
        require(type(a) is int and a>=p["source"] and (a-p["source"])%(2*M)==0,
                "supplied macro source outside safe cylinder")
        require(M*b==K*a+p["C"] and b>a,"supplied return equation failed")
        x,y=a,3*a-1
        for _ in range(38):x,y=T(x),T(y)
        require((x,y)==(b,3*b-1),"supplied macro not realized by literal ordinary motion")
    require(path["valuation_pairs"]==[[v2(D*a+SPECS["F"]["C"]),
                v2(D*a+SPECS["G"]["C"])] for a in bases],"bad supplied valuation vector")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-certificate",action="store_true",
                        help="explicitly regenerate expanding_return_certificate.json")
    args=parser.parse_args()
    expected,report=reconstruct()
    fixture=OUT/"expanding_return_certificate.json"
    if args.write_certificate:
        fixture.write_text(json.dumps(expected,indent=2)+"\n")
    supplied=json.loads(fixture.read_text())
    require(set(supplied["cylinders"])==set(SPECS),"changed cylinder menu")
    for data in supplied["cylinders"].values():validate(data)
    validate_literal_control(supplied["convergent_control"])
    for path in supplied["finite_repetitions"]+[supplied["finite_alternating_path"]]:
        validate_supplied_schedule(path)
    require(supplied==expected,"committed certificate differs from exact reconstruction")
    # Also reject corruption of supplied orbit and schedule evidence.
    bad=deepcopy(supplied["convergent_control"]);bad["Y_orbit_to_1"][40]+=1
    try:validate_literal_control(bad)
    except ValueError:report["corruptions_rejected"].append("literal_control_orbit")
    else:raise ValueError("corrupted literal orbit was accepted")
    bad=deepcopy(supplied["finite_alternating_path"]);bad["bases"][1]+=1
    try:validate_supplied_schedule(bad)
    except ValueError:report["corruptions_rejected"].append("finite_schedule")
    else:raise ValueError("corrupted schedule was accepted")
    report["mode"]="regenerated_then_verified" if args.write_certificate else "verified_committed_fixture"
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
