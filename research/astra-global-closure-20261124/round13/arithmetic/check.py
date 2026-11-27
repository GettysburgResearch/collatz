"""Replay post-peak merger certificates and parameter arithmetic with exact integers."""

from fractions import Fraction
from pathlib import Path
import re


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def track(n, h, grade=0):
    for _ in range(h):
        grade += n % 2
        n = step(n)
    return n, grade


def signed_hit(n):
    odd_count = 0
    for h in range(2000):
        if n == 1:
            return h, odd_count
        odd = n.numerator % 2
        odd_count += odd
        n = (3 * n + 1) / 2 if odd else n / 2
    raise RuntimeError("Unclassified signed reference")


def constants():
    lean = Path(__file__).with_name("PostPeakMerger.lean").read_text()
    return {
        name: int(value)
        for name, value in re.findall(
            r"(?:private )?def (anchor|carry|seed|terminal) : Nat := ([0-9]+)", lean
        )
    }


def binary_index(laps, exponent, seed):
    """Compute the unique odd normalized index, one certified bit at a time."""
    precision = 1379
    index_v2 = exponent - 3
    modulus = 1 << (exponent + precision)
    unit = seed * pow(3, -laps, 1 << precision) % (1 << precision)
    target = 1 + (unit << exponent)
    current = 1
    power = pow(3, 162 << index_v2, modulus)
    normalized = 0
    for bit in range(precision):
        bitmask = 1 << (exponent + bit)
        require((power - 1) % (2 * bitmask) == bitmask, "square has wrong order")
        if (current - target) & bitmask:
            current = (current * power) % modulus
            normalized |= 1 << bit
        power = (power * power) % modulus
    require(current == target and normalized % 2 == 1, "bad exponent solution")
    return normalized


def main():
    c = constants()
    require(set(c) == {"anchor", "carry", "seed", "terminal"}, "missing literals")
    seed = c["seed"]
    require(0 < seed < 2**1379 and seed % 2 == 1, "seed range or parity")
    require(c["anchor"] == pow(3, -475, 2**947), "native anchor")
    require(3**475 * c["anchor"] == 1 + 2**947 * c["carry"], "native carry")

    rows = ((11, 89, 45), (-151, 327, 151), (-475, 947, 475))
    for e, h, p in rows:
        require(signed_hit(Fraction(3) ** e - 1) == (h, p), "signed first hit")
    for horizon, offsets, exponents in ((327, (0, 1), (175, 0)),
                                        (947, (0, 1, 3), (485, 310, 0))):
        den = 162 * offsets[-1] - 11
        anchor = pow(3, -den, 2**horizon)
        for v in (0, 1, 17):
            base = anchor + (v << horizon)
            t, rem = divmod(3**den * base - 1, 2**horizon)
            require(rem == 0, "native representative division")
            for i, g in zip(offsets, exponents):
                shift = 162 * (offsets[-1] - i)
                source = 3**shift * base - 1
                require(track(source, horizon, shift) == (1 + 3**g*t, den+g),
                        "ordinary prefix endpoint or grade")
    for b in (0, 1, 37):
        for g in (0, 175, 310, 485):
            w = 3**g * (seed + (b << 1379))
            require(track(w, 1379, g) == (c["terminal"] + 3**658 * b, 658),
                    "ordinary unshifted tower cylinder")
            require(track(3*w + 1, 1379)[0] == track(w, 1379)[0],
                    "forward transfer to unshifted tower")
    for L in (0, 1, 2, 10, 63, 128):
        for horizon in (327, 947):
            e = horizon + 2 + 2 * L
            k = e - 3
            v = binary_index(L, e, seed)
            modulus = 1 << (e + 1379)
            period = 1 << (k + 1379)
            for odd_mod, target in ((1, 0), (3**11, 0), (5 * 3**7, 47)):
                m0 = v << k
                offset = ((target - m0) * pow(period, -1, odd_mod)) % odd_mod
                m = m0 + period * offset
                require(m >= 3 and m % odd_mod == target, "index CRT")
                for index in (m, m + period * odd_mod):
                    residue = pow(3, 162 * index, modulus)
                    u, rem = divmod(residue - 1, 2**e)
                    require(rem == 0 and u % 2 == 1, "index valuation")
                    require(pow(3, L, 2**1379) * u % 2**1379 == seed, "index gate")
    require((3**310 - 1) % 16 == 8 and seed % 2 == 1, "overlap valuation")
    for m in (0, 1, 2, 3, 4):
        j = 11 + 162 * m
        z, rem = divmod(2**(j+7) - 271, 81)
        require(rem == 0 and z % 48 == 17 and z > 0, "canonical parent")
        require(track(z, 7)[0] == 2**j - 1, "parent lower entry")
        x = 3 * z
        for h in range(j + 7):
            require(x != 1, "premature upper hit")
            x = step(x)
        require(x == 1 and track(3*z, j+7)[1] == 3, "canonical upper certificate")
    print("Signed first hits (clock, odd count): (89,45), (327,151), (947,475).")
    print("15 positive first-stage lifts; 12 complete 1379-clock tower checks and their physical transfers.")
    print("12 binary-index inversions, 36 odd-CRT intersections and 72 exact modular gate replays.")
    print("Five actual small canonical parents passed both arms and upper first-hit checks.")


if __name__ == "__main__":
    main()
