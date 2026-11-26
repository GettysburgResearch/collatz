"""Replay the rational necklace control and the general positive coalescence."""

from fractions import Fraction


def shortcut(numerator, denominator=1):
    """The signed numerator after one shortcut at fixed odd denominator."""
    if numerator % 2:
        return (3 * numerator + denominator) // 2
    return numerator // 2


def positive_coalescence():
    checked = 0
    for h in range(1, 32):
        for z in range(1, 300, 2):
            n = 2**h * z - 2
            w = 3 ** (h - 1) * z
            if n <= 0 or w % 4 != 3:
                continue
            a, b = n, n + 1
            odd_a = odd_b = 0
            for _ in range(h + 2):
                odd_a += a % 2
                odd_b += b % 2
                a, b = shortcut(a), shortcut(b)
            assert a == b == (3 * w - 1) // 4 and odd_a == odd_b
            checked += 1
    return checked


def joint_cycle(word):
    q = 2 ** len(word) - 1
    a = -int(word, 2)
    b = a + q
    seen = {}
    clock = odd_a = odd_b = 0
    while (a, b) not in seen:
        assert a != b or odd_a != odd_b
        seen[a, b] = clock, odd_a, odd_b
        odd_a += a % 2
        odd_b += b % 2
        clock += 1
        a, b = shortcut(a, q), shortcut(b, q)
    entry, initial_a, initial_b = seen[a, b]
    assert odd_a - initial_a == odd_b - initial_b > 0
    return entry, clock - entry, odd_a - initial_a


def ordinary_lift(word, odd_target):
    """Check an actual two-level lift around 11 + the indicated period."""
    h = len(word)
    z = Fraction(int(word, 2), 2**h - 1)
    q = z.denominator
    A = 11 * q + z.numerator
    signed = [-z.numerator, q - z.numerator]
    data = []
    for r in signed:
        u, count, i = r, 0, 0
        while count < odd_target:
            count += u % 2
            u = shortcut(u, q)
            i += 1
        k = i + (-i % h)
        n, rem = divmod(2**k * A + r, q)
        assert rem == 0 and n > 0
        a = n
        for _ in range(i):
            a = shortcut(a)
        assert q * a == 2 ** (k - i) * 3**odd_target * A + u
        data.append((a, k - i, u))
    cap = max(c for _, c, _ in data)
    left, right = [a * 2 ** (cap - c) for a, c, _ in data]
    assert q * (right - left) == sum(
        sign * u * 2 ** (cap - c) for sign, (_, c, u) in zip((-1, 1), data)
    )


def counted_adjacent(residue, depth):
    a, b = residue, residue + 1
    difference = 0
    for _ in range(depth):
        difference += (a % 2) - (b % 2)
        a, b = shortcut(a), shortcut(b)
        if a == b:
            return difference == 0
    return False


def explicit_necklace_obstruction():
    modulus = 255
    period_bits = 87
    for right, phase, clock, required in (
        (False, 7, 100, 1527),
        (True, 5, 101, 159),
    ):
        residue = (period_bits * 2**phase) % modulus
        a = modulus - residue if right else -residue
        odds = 0
        for i in range(clock + 201):
            if i == clock:
                assert (a, odds) == (required, 57)
            if i == clock + 200:
                assert (a, odds) == (required, 169)
                break
            odds += a % 2
            a = shortcut(a, modulus)

    # A is odd following the breaking left bit. All 32 possible cosets occur.
    base = 2**9
    possible = {
        ((8 * 3**57 * A + 1272) * pow(modulus, -1, base)) % base
        for A in range(1, 128, 2)
    }
    assert possible == set(range(0, base, 16))
    # A single witness at depth at most 24 is sufficient per coset.
    witnessed = {}
    for depth in range(9, 25):
        for coset in sorted(possible - witnessed.keys()):
            for residue in range(coset, 2**depth, base):
                if counted_adjacent(residue, depth):
                    witnessed[coset] = (residue, depth)
                    break
    assert witnessed.keys() == possible
    assert max(depth for _, depth in witnessed.values()) == 24
    # 3^112 generates 1+2^6 Z_2, by successive squaring.
    assert (3**112 - 1) % 128 == 64
    largest_index = 2**(24 - 9) - 1
    required_bits = 103 + 200 * largest_index
    repetitions = (required_bits + 7) // 8
    assert repetitions == 819188
    print("All 32 cosets have counted fusion by precision 24.")
    print("Explicit forbidden repetitions after a breaking bit:", repetitions)


def main():
    print("Positive paired coalescences:", positive_coalescence())
    word = "01010111"
    entries = (21, 22, 23, 24, 25, 26, 27, 20)
    for i, expected in enumerate(entries):
        phase = word[i:] + word[:i]
        entry, period, odds = joint_cycle(phase)
        assert entry == expected and period == 100
        print(phase, "entry", entry, "period", period, "odd departures", odds)
    for q in (25, 70, 125):
        for w in (word, "0111"):
            ordinary_lift(w, q)
    print("Six exact two-level ordinary lifts checked.")
    explicit_necklace_obstruction()


if __name__ == "__main__":
    main()
