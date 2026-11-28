"""Directed-rational pressure bound and native complete plateau controls."""
from fractions import Fraction
from math import ceil, gcd
import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def log_lower(x, terms=16):
    """Truncate ln(x) = 2 atanh((x-1)/(x+1)) from below for x>=1."""
    v = Fraction(x-1, x+1)
    return 2 * sum(v**(2*k+1)/(2*k+1) for k in range(terms))


def pressure_certificate():
    bins, scale = 8192, 10**12
    ln2_lower = Fraction(693147, 10**6)
    ln3_lower = Fraction(109861, 10**5)
    require(log_lower(2) > ln2_lower and log_lower(3) > ln3_lower,
            "positive-series rational logarithm lower bounds")
    a = 3*ln2_lower/bins
    # exp(-a) <= 1-a+a^2/2 on nonnegative a.
    ratio = ceil(scale*(1-a+a*a/2))
    q = scale//8
    units = 0
    for j in range(bins):
        # x=1+j/bins. q/scale bounds 2^(-3x) from above.
        power = Fraction(q, scale)
        s = power if 2*j >= bins else power+power**2+power**3
        # The cubic upper log polynomial is increasing for s>=0.
        upper_log = s-s*s/2+s**3/3
        v = 1+Fraction(j, bins)
        # Positive integrands decrease on both bins split at x=3/2.
        units += ceil(scale*upper_log/(v*ln2_lower))
        q = (q*ratio+scale-1)//scale
    cap = Fraction(units, bins*scale)
    c0 = (ln3_lower/Fraction(5116201, 1000000)-cap)/3
    require(c0 > Fraction(2, 39), "complete plateau ratio strictly below 38")
    return {"quadrature_bins": bins, "directed_scale": scale,
            "pressure_upper": str(cap), "drift_lower": str(c0),
            "ratio_upper": str((2-c0)/c0)}


def round_step(z, b):
    return (3*z+(1<<b)-1) >> b


def one_component(n):
    z = n
    seen = {}
    trace = []
    while z not in seen:
        seen[z] = len(trace)
        b = 1 if 3*z <= 2*n else 2
        d = (1<<b)*round_step(z,b)-3*z
        trace.append((z,b,d))
        z = round_step(z,b)
    return trace[seen[z]:]


def cyclic_pattern(word, length, start):
    return tuple(word[(start+j)%len(word)] for j in range(length))


def check_native(maximum=1023):
    previous = None
    switches = repeat = origins = 0
    for n in range(3, maximum+1, 2):
        trace = one_component(n)
        p = len(trace)
        A = sum(b for _,b,_ in trace)
        require(gcd(A,p)==1 and all(n < 2*z <= 2*n for z,_,_ in trace),
                "reduced primitive calendar and all native labels")
        ranks = {z:r for r,z in enumerate(sorted(z for z,_,_ in trace))}
        clock = Fraction(A,p)
        if previous is not None:
            require(clock <= previous, "all complete cutoff clocks are ordered")
            switches += clock < previous
            repeat += clock == previous
        previous = clock
        k = 1
        while 3**k <= 2*n:
            k += 1
        k += 1
        bs = [b for _,b,_ in trace]
        digits = [d for _,_,d in trace]
        # Adding spatial bin boundaries still costs only O(k) calendar cuts.
        contexts = [(3*ranks[z]//p,b) for z,b,_ in trace]
        words = set()
        environment = set()
        for i,(z,_,_) in enumerate(trace):
            history = cyclic_pattern(bs,k,i)
            require(sum(history)==(ranks[z]+k*A)//p and 2**sum(history)>n,
                    "true clock and source-separating window")
            word = (history,cyclic_pattern(digits,k,i))
            require(word not in words, "distinct actual starts have distinct window codes")
            words.add(word)
            environment.add(cyclic_pattern(contexts,k,i))
            origins += 1
        require(len(environment)<=4*k+1, "joint angle/calendar partition grows linearly")
    return {"max_odd_cutoff":maximum, "origins":origins,
            "strict_cutoff_switches":switches,"equal_cutoff_steps":repeat}


if __name__ == "__main__":
    print(json.dumps({"pressure":pressure_certificate(), "native":check_native()},
                     indent=2, sort_keys=True))
