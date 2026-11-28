"""Cross-check bounded target certificates with independent positive inverse trees."""

from fractions import Fraction


def word(start, clock):
    state = start
    bits = []
    for _ in range(clock):
        odd = state % 2
        bits.append(odd)
        state = (state * (1 + 2*odd) + odd) // 2
    return state, tuple(bits)


def candidate_balls(clock, threshold):
    modulus2 = 2**clock
    result = []
    for source in range(modulus2):
        lower_start_end, first = word(source, clock)
        upper_start_end, second = word(source + 1, clock)
        grade = sum(first)
        if sum(second) != grade or abs(lower_start_end - upper_start_end) != 1:
            continue
        modulus3 = 3**grade
        if Fraction(modulus3, modulus2) <= threshold:
            continue
        if lower_start_end < upper_start_end:
            target = lower_start_end
            orientation, target_word = 1, first
        else:
            target = upper_start_end
            orientation, target_word = -1, second
        result.append((clock, orientation, target_word, modulus3, target % modulus3))
    return result


def visitors(target, depth):
    """All words, including possible later visits; odd inverse precedes its parent."""
    frontier = [(target, ())]
    visits = {}
    for clock in range(depth + 1):
        following = []
        for source, bits in frontier:
            visits.setdefault(source, []).append((clock, bits))
            following.append((2*source, (0,) + bits))
            if source % 3 == 2:
                following.append(((2*source - 1)//3, (1,) + bits))
        frontier = following
    return visits


def exact_union(balls):
    retained = []
    for modulus, residue in sorted({row[-2:] for row in balls}):
        if any(residue % small == value for small, value in retained):
            continue
        retained.append((modulus, residue))
    return sum((Fraction(1, modulus) for modulus, _ in retained), Fraction(0))


def main():
    if not (5**40 < 2**55 * 3**24 and 3**24 < 2**39):
        raise ArithmeticError("entropy bounds")
    depth = 15
    base = 10**15
    triples_checked = 0
    for gain, visit_floor in ((Fraction(1), lambda y: y),
                              (Fraction(3, 2), lambda y: Fraction(2*y + 1, 3))):
        balls = []
        for clock in range(depth + 1):
            balls.extend(candidate_balls(clock, gain))
        targets = set(range(base, base + 145))
        for _, _, _, modulus, residue in balls:
            targets.add(base + (residue - base) % modulus)
        for target in targets:
            first = visitors(target, depth)
            second = visitors(target + 1, depth)
            actual = set()
            for m, records in first.items():
                for delta in (-1, 1):
                    if max(m, m + delta) >= visit_floor(target):
                        continue
                    for left_clock, bits in records:
                        for right_clock, _ in second.get(m + delta, ()):
                            actual.add((left_clock, right_clock, delta, bits))
            expected = {
                (t, t, delta, bits) for t, delta, bits, modulus, residue in balls
                if target % modulus == residue
            }
            if actual != expected:
                raise ArithmeticError((target, actual, expected))
            triples_checked += len(actual)
        print(f"gain>{gain}, clocks through {depth}, tested {len(targets)} targets, "
              f"{len(balls)} marked words, exact truncated Haar mass {exact_union(balls)}")
    print(f"verified {triples_checked} actual marked visits including both independent clocks")


if __name__ == "__main__":
    main()
