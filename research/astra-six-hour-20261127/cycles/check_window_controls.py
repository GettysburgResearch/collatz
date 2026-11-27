"""Construct unbounded positive all-good controls for finite two-sided native data."""

from collections import Counter
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
STEERING = ROOT / "research/astra-global-closure-20261124/round13/trace/check.py"
spec = importlib.util.spec_from_file_location("pinned_collatz_steering", STEERING)
steering = importlib.util.module_from_spec(spec)
spec.loader.exec_module(steering)
MARKS = ((1, 0), (1, -1), (1, 1), (2, -1), (3, 0))


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def carry(word):
    h = c = 0
    for exponent in word:
        c = 3*c + 2**h
        h += exponent
    return h,c


def profile(r, n):
    forward = [(3**i).bit_length()-1 for i in range(n+1)]
    f = [b-a for a,b in zip(forward,forward[1:])]
    # First r backward edges have cost two, then one. Continue in one
    # homogeneous octave, with all real height multipliers strictly above one.
    g = int(r >= 4)
    reverse = [2]*r+[1]
    for i in range(r+1,n):
        reverse.append((3**(i+1)).bit_length()-(3**i).bit_length())
    require(sum(reverse) == (3**n).bit_length()+g, "reverse floor schedule")
    return f,reverse


def source_class(forward, reverse):
    h,c = carry(forward)
    m2 = 2**(h+1)
    a = ((2**h-c)*pow(3**len(forward), -1, m2)) % m2
    A,C = carry(reversed(reverse))
    m3 = 3**len(reverse)
    b = pow(2**A, -1, m3)*C % m3
    x = a+m2*((b-a)*pow(m2, -1, m3) % m3)
    return x,m2*m3


def discrete_log_two(unit, k):
    """Solve 2^e = unit modulo 3^k by successive ternary digits."""
    require(unit%3 != 0 and k > 0, "unit for power-of-two landing")
    m,period = 3,2
    e = 0 if unit%3 == 1 else 1
    while m < 3**k:
        m *= 3
        e = next(z for z in (e,e+period,e+2*period) if pow(2,z,m) == unit % m)
        period *= 3
    require(pow(2,e,m) == unit%m and pow(2,period,m) == 1, "terminal exponent")
    return e,period


def control(r, n, all_marks=False):
    f,b = profile(r,n)
    x,modulus = source_class(f,b)
    phases = {0: (modulus,x)}
    base,off = modulus,x
    for i,e in enumerate(f,1):
        require((3*off+1)%(2**(e+1)) == 2**e, "exact native forward edge")
        base,off = 3*base//2**e,(3*off+1)//2**e
        phases[i] = (base,off)
    base,off = modulus,x
    for i,e in enumerate(b,1):
        require((2**e*off-1)%3 == 0, "exact native reverse edge")
        base,off = 2**e*base//3,(2**e*off-1)//3
        phases[-i] = (base,off)
    for i,(base,off) in phases.items():
        require(i == 0 or x < off and modulus < base, "strict minimum for every lift")
        require(3*base < 16*modulus and 3*off <= 16*x+7, "physical strip for every lift")
        require(off % 2 == 1 and base%2 == 0, "odd phase")
    require((x-1)%3**r == 0 and (x-1)%3**(r+1) != 0, "exact minimum valuation")
    require(phases[-r][1]%48 == 17, "canonical descending-run start")

    chosen = sorted(phases) if all_marks else sorted({-r,0,n})
    forms,rows = [],[]
    for i in chosen:
        base,off = phases[i]
        for A,B in MARKS:
            slope,beta = A*base,A*off+B
            k = steering.valuation(slope)
            bits,beta = steering.trace(beta,k)
            slope = slope//2**k*3**sum(bits)
            grade = 0
            while slope%3 == 0:
                grade += 1
                slope //= 3
            require(slope == 1,"normalized free slope")
            forms.append((grade,beta))
            rows.append((i,A,B,k,sum(bits),grade))
    cylinder = steering.Cylinder(len(rows))
    cylinder.forms = forms.copy()
    cases = Counter()
    for j in range(1,len(rows)):
        cylinder.merge(0,j,cases)
        require(len(set(cylinder.forms[:j+1])) == 1,"common lift preserved")
    cylinder.expose(0,1)
    grade,terminal = cylinder.forms[0]
    require(terminal%3 == 2, "common forced odd step gives ternary unit")
    e,period = discrete_log_two(terminal,grade)
    bounds = []
    for z in (0,1,3):
        center = x+modulus*(cylinder.residue+2**cylinder.clock*z)
        for i,A,B,k,p,startgrade in rows:
            slope,off = phases[i]
            actual = A*(off+slope*((center-x)//modulus))+B
            script,endpoint = steering.trace(actual,k+cylinder.clock)
            require(endpoint == 3**grade*z+terminal,"literal endpoint")
            bound = p+grade-startgrade
            require(sum(script) == bound,"physical grades")
            bounds.append(bound)
    return {"reverse_twos_into_center":r,"odd_steps_on_each_side":n,
            "all_phases_marked":all_marks,"marked_phase_range":[min(chosen),max(chosen)],
            "marked_ordinary_starts":len(rows),
            "prefix_alignment_and_steering_max_clock":max(row[3] for row in rows)+cylinder.clock,
            "max_odds_to_common_endpoint":max(bounds),"terminal_slope_exponent":grade,
            "terminal_exponent_residue":str(e),"terminal_exponent_period":str(period),
            "literal_lifts_checked":[0,1,3]}


def main():
    data = [control(r,16,True) for r in range(2,6)]
    data.append(control(5,64,True))
    print(json.dumps(data,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
