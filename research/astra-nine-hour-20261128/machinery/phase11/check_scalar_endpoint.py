"""Directed enclosure of the scalar AC threshold, using the phase-four log kernel."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

source = Path(__file__).resolve().parents[1] / "phase4" / "check_tilted_interval.py"
spec = spec_from_file_location("directed_interval", source)
log = module_from_spec(spec)
spec.loader.exec_module(log)


def scalar_gap(theta_num, theta_den):
    """Return scaled lower and upper bounds for Delta minus the envelope integral."""
    n, d = theta_num, theta_den
    qn = d - n
    c_lo = (d * log.LOG2_LO * log.SCALE) // (n * log.LOG3_HI)
    c_hi = log.ceiling(d * log.LOG2_HI * log.SCALE, n * log.LOG3_LO)
    if not log.SCALE < c_lo <= c_hi < 4 * log.SCALE // 3:
        raise ArithmeticError("the linear entropy envelope does not apply")
    ent1_lo, ent1_hi = log.log_bounds(d, n)
    ent2_lo, ent2_hi = log.log_bounds(d, qn)
    entropy_lo = ent1_lo + qn * ent2_lo // n
    entropy_hi = ent1_hi + log.ceiling(qn * ent2_hi, n)
    phi_lo = c_lo - log.SCALE - log.log_bounds(c_lo, log.SCALE)[1]
    phi_hi = c_hi - log.SCALE - log.log_bounds(c_hi, log.SCALE)[0]
    if phi_lo <= 0:
        raise ArithmeticError("positivity of c-1-log c")
    gain_lo = 4 * log.LOG2_LO * phi_lo // (3 * log.SCALE)
    gain_hi = log.ceiling(4 * log.LOG2_HI * phi_hi, 3 * log.SCALE)
    return (entropy_lo - log.ceiling(log.LOG2_HI * d, n) + gain_lo,
            entropy_hi - log.LOG2_LO * d // n + gain_hi)


if __name__ == "__main__":
    denominator = 10**12
    left = 550024419420
    right = 550024419422
    low, _ = scalar_gap(left, denominator)
    _, high = scalar_gap(right, denominator)
    if not low > 0 > high:
        raise ArithmeticError(("critical bracket failed", low, high))
    print("theta endpoints", left, right, "denominator", denominator)
    print("scaled positive lower, negative upper", low, high, "scale", log.SCALE)
