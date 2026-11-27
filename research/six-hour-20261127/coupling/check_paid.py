"""Verify ordinary affine lifts and the five delayed residue progressions."""
import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def trace(x, h):
    grade = 0
    for _ in range(h):
        bit = x % 2
        grade += bit
        x = ((3 * x + 1) if bit else x) // 2
    return x, grade


def seed(r, e, a, k0, j0, h, grade, shift, leading, center):
    """Check a seed at two adjacent lifts, and its full original clock class."""
    n = r + e
    ternary = 3**(r + 1)
    address_period = 3**(r - 4)
    m0 = 11 + 162*j0
    require((12*pow(2, 18*k0, 2 * 3**r)-1-m0) % (2*3**r) == 0,
            "original delayed class maps to the stated hard exponent")
    require(pow(2, 18*address_period, 3**(r-1)) == 1, "delayed period")
    require(pow(2, 162*address_period, ternary) == 1, "seed period")
    x0 = pow(2, m0+shift, ternary)
    require(h == n-shift, "common lift precision")
    w0, rem = divmod(2**h*x0-a, 3**r)
    require(rem == 0 and w0 % 48 == 17, "canonical seed")
    require(81*2**n < 128*3**r and 2**min(m0,64) > 271*3**r,
            "strict leading margin pays original correction")
    for v in (0, 1):
        x = x0+ternary*v
        w = w0+3*2**h*v
        require(trace(w,n) == (2**(-shift)*x-1,r), "physical lower prefix")
        require(trace(3*w,h) == (leading*x+center,grade), "physical upper prefix")
    return {"rank": r, "source_offset": a, "source_power_offset": n,
            "delayed_k_residue": k0, "hard_j_residue": j0,
            "index_modulus": address_period, "first_hard_exponent": m0,
            "X_residue": x0, "W_at_X_residue": w0,
            "lower_clock": n, "lower_odds": r, "upper_clock": h,
            "upper_odds": grade, "upper_X_factor": leading,
            "upper_offset": center, "X_exponent_offset": shift}


def check_phases():
    specs = [(13,29,0),(14,68,1),(15,23,0),(16,71,0),(17,229,0)]
    out = []
    require(trace(2031,11) == (2170,7), "negative seventeen turn")
    require(pow(2,90,11) == 1, "five-step period in k")
    for base, clock, shift in specs:
        m = 12*2**(18*base)-1
        turns, remainder = divmod(m-3,11)
        center, odds = trace(-17,remainder)
        earlier = 7*turns+3+odds-shift
        modulus = 2**clock
        residue = pow(3,earlier,modulus)
        require(clock <= 18*base, "phase period keeps low bits")
        require(pow(3,modulus,modulus) == 1, "odd-power period")
        require(earlier+40<m and 0<residue and 3**shift*residue+center>0,
                "phase size and positivity")
        # At a later k=base+5v, the number 2^(18k) changes by a multiple
        # of 11*modulus. The phase is fixed and the exponent changes by a
        # multiple of modulus. One base pair checks every such lift.
        target, g = trace(3**shift*residue+center,clock)
        other, q = trace(residue-1,clock)
        require(target == other and g+shift == q, "equal intercepts and slopes")
        out.append({"k_mod_five": base%5, "first_base": base,
                    "remainder": remainder, "phase_center": center,
                    "remainder_odds": odds, "earlier_exponent_shift": shift,
                    "merge_clock": clock, "checkpoint_odds": g,
                    "earlier_peak_odds": q, "low_binary_residue": str(residue)})
    require({row["k_mod_five"] for row in out} == set(range(5)), "all phase classes")
    return out


def main():
    positive = seed(8,5,28927,64,50,20,7,-7,1,1)
    negative = [seed(11,6,962197,1429,1772,20,13,-3,27,-17),
                seed(11,7,1786613,376,881,21,13,-3,27,-17)]
    require(2**40*(3**100+1) < 2**7*4**100, "positive-turn payment")
    require(trace(4*17+1,2) == (3*17+1,1), "positive turn")
    print(json.dumps({"positive_seed": positive, "negative_seeds": negative,
                      "negative_phases": check_phases()},indent=2))


if __name__ == "__main__":
    main()
