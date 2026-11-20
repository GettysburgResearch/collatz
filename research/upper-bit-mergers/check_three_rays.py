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


def verify_affine_word(modulus, residue, word, target_mod, target_residue, expected_tests):
    """Verify every step and extra-edge hypothesis for all lifts of the residue."""
    slope, offset = modulus, residue
    targets = []
    for action in word:
        if action == "D":
            slope, offset = 2 * slope, 2 * offset
        elif action == "I":
            if (2 * slope) % 3 or (2 * offset - 1) % 3:
                raise AssertionError(("nonintegral inverse", slope, offset))
            slope, offset = 2 * slope // 3, (2 * offset - 1) // 3
            if slope % 2 or offset % 2 != 1:
                raise AssertionError(("inverse parity", slope, offset))
        elif action in ("M", "V"):
            if action == "V":
                if slope % 3 or offset % 3:
                    raise AssertionError(("nonintegral quotient", slope, offset))
                slope, offset = slope // 3, offset // 3
            if slope % target_mod or offset % target_mod != target_residue:
                raise AssertionError(("wrong test class", slope, offset))
            targets.append((slope, offset))
            if action == "M":
                slope, offset = 3 * slope, 3 * offset
        else:
            if slope % 2 or offset % 2 != int(action == "O") or action not in ("O", "E"):
                raise AssertionError(("wrong word", action, slope, offset))
            if action == "O":
                slope, offset = 3 * slope, 3 * offset + 1
            slope, offset = slope // 2, offset // 2
        if min(slope, offset) <= 0:
            raise AssertionError(("nonpositive progression", slope, offset))
    if (slope, offset) != (3 * modulus, 3 * residue) or targets != expected_tests:
        raise AssertionError(("tripling certificate", slope, offset, targets))


def verify_one_residue_rules():
    """Check the fixed words and the residue decisions in the valuation descent."""
    if walk(23, 5) != (20, 3) or walk(69, 5) != (20, 2):
        raise AssertionError("the 23 mod 32 direct tripling word")
    # On the rational pivot the shortcut map acts on the numerator over 29.
    for numerator, expected_odds in ((5, 19), (15, 18)):
        odds = 0
        for _ in range(35):
            odd = numerator % 2
            odds += odd
            numerator = (3 * numerator + 29) // 2 if odd else numerator // 2
        if (numerator, odds) != (22, expected_odds):
            raise AssertionError(("class 9 bounded-clock pivot", numerator, odds))

    verify_affine_word(432, 173, "DDDDDDDDIIVOEOEOOEOEODDIIVOEOEEI",
                       16, 1, [(16384, 6561), (6912, 2769)])
    verify_affine_word(162, 67, "ODDIIDDIMOOOEEEEI", 18, 9, [(1152, 477)])
    verify_affine_word(648, 443, "DDDDIVOOOEOOEEIDI", 18, 9, [(2304, 1575)])

    # Traverse the directed certificate from x to 3x. Its four extra edges
    # all multiply positive odd multiples of three in the forward direction.
    verify_affine_word(31104, 5831, "ODDIMMOEEIIDIDDIDDIMMOEEEEOEEEEI", 6, 3,
                       [(124416, 23325), (373248, 69975),
                        (1769472, 331725), (5308416, 995175)])

    # 144 is lcm(16, 9); z modulo 16 depends only on x modulo 48.
    # Checking the ternary valuations themselves uses the exact affine identities.
    for x in range(17, 17 + 144, 2):
        residue = x % 16
        if residue not in (7, 9, 13) or x % 3 == 0:
            continue
        j = 2 if residue == 13 else 3
        y = 3**j * x
        if y % 8 != 5 and y % 16 != 3:
            raise AssertionError(("adjacent class", x, y))
        power = 4 if x % 3 == 1 else 8
        z, rem = divmod(power * x - 1, 3)
        wanted = {7: 9, 9: 1, 13: 1}[residue] if power == 4 else 13
        if rem or z % 16 != wanted or not x < z < 3 * x:
            raise AssertionError(("larger input", x, z))
        if residue == 7 and (8 * x - 1) % 32 != 23:
            raise AssertionError(("intrinsic successor", x))
        if residue == 13 and power == 8 and 3 * (5*z - 1) != 8 * (5*x - 1):
            raise AssertionError(("first valuation", x))
        if residue == 9 and power == 4:
            next_x = (32*x - 5) // 3
            if next_x % 16 != 9 or 3 * (29*next_x - 5) != 32 * (29*x - 5):
                raise AssertionError(("second valuation", x))


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
    verify_one_residue_rules()
    print("single-residue words, directed certificate, both recurrent pivots and ternary transitions verified")
    print(f"{verify_seeds()} common words, their affine lifts, and 64 odd residue classes replayed")
    print(f"17 symbolic edges from 288n to 288(n+1) verified: {verify_offset_chain()}")
