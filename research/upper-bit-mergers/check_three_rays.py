"""Replay the finite certificates in the variation and tripling-window proofs."""

from check import walk


def verify_seeds():
    # base inputs, clock, expected common endpoint, common odd-step count
    seeds = [(2, 3, 4, 2, 2), (4, 5, 3, 2, 1),
             (49, 50, 7, 11, 3), (5, 6, 5, 2, 2)]
    for lo, hi, clock, endpoint, odds in seeds:
        if walk(lo, clock) != (endpoint, odds) or walk(hi, clock) != (endpoint, odds):
            raise AssertionError(("base word", lo, hi, clock))
        for lift in (1, 7, 2**40):
            shift = 2**clock * lift
            expected = (endpoint + 3**odds * lift, odds)
            if walk(lo + shift, clock) != expected or walk(hi + shift, clock) != expected:
                raise AssertionError(("lifted word", lo, hi, lift))
    for u in range(1, 128, 2):
        minus = [3**j * u for j in range(2, 6)]
        plus = [3**j * u for j in range(2, 34)]
        if not any(y % 16 in (3, 5) for y in minus):
            raise AssertionError(("minus class", u))
        if not any(y % 128 == 49 or y % 32 == 5 for y in plus):
            raise AssertionError(("plus class", u))
    return len(seeds)


def verify_offset_chain():
    offsets = [0, 18, 24, 32, 33, 36, 48, 64, 63,
               72, 96, 99, 108, 144, 192, 198, 216, 288]
    counts = {"plus": 0, "minus": 0, "odd": 0}
    for left, right in zip(offsets, offsets[1:]):
        lo, hi = sorted((left, right))
        scale = hi - lo
        if 288 % scale or lo % scale:
            raise AssertionError(("nonintegral normalization", left, right))
        core = scale
        for prime in (2, 3):
            while core % prime == 0:
                core //= prime
        if core != 1:
            raise AssertionError(("unexpected scale", scale))
        # The normalized arguments are affine in n with slope 288 / scale.
        slope, lower = 288 // scale, lo // scale
        if slope % 16 == 0 and lower % 16 == 0:
            counts["plus"] += 1
        elif slope % 4 == 0 and (lower + 1) % 4 == 0:
            counts["minus"] += 1
        elif slope % 6 == 0 and lower % 6 == 3:
            counts["odd"] += 1
        else:
            raise AssertionError(("unjustified edge", left, right, slope, lower))
    if counts != {"plus": 4, "minus": 11, "odd": 2}:
        raise AssertionError(counts)
    return counts


if __name__ == "__main__":
    print(f"{verify_seeds()} common words, their affine lifts, and 64 odd residue classes replayed")
    print(f"17 symbolic edges from 288n to 288(n+1) verified: {verify_offset_chain()}")
