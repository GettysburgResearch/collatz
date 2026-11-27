"""Exact binary-prefix harmonic controls; no infinite vanishing assertion."""
from fractions import Fraction
import json


SCALE = 1 << 80
DEPTH = 22


def require(test, description):
    if not test:
        raise ArithmeticError(description)


def step(x):
    return (3*x+1)//2 if x % 2 else x//2


def literal(N, r):
    x, grade = r, 0
    for j in range(1, N+1):
        grade += x % 2
        x = step(x)
        if 5*j > 8*grade:
            return None
    return x, grade


def controls():
    # The unique empty parity cylinder is a generation placeholder.
    # The formal positive-source sum at depth zero is empty.
    rows = [(0, 0, 0)]
    debt_counts = {0: 1}
    output = []
    previous_upper = Fraction(5)
    all_good_clocks = []
    for r in range(1, 33):
        x, clock = r, 0
        while x != 1:
            x = step(x)
            clock += 1
            require(clock <= 128, "small ordinary source")
        all_good_clocks.append(clock)
    for N in range(1, DEPTH+1):
        old_modulus = 1 << (N-1)
        current = []
        harmonic_low = 0
        birth_low = 0
        births = 0
        for r, x, grade in rows:
            new_cost = Fraction()
            for bit in (0, 1):
                source = r + old_modulus*bit
                incoming = x + 3**grade*bit
                p = grade + incoming % 2
                if 5*N > 8*p:
                    continue
                endpoint = step(incoming)
                require(0 < source < 2**N and source % 2 == 1, "principal binary source")
                current.append((source, endpoint, p))
                harmonic_low += SCALE//source
                if bit:
                    births += 1
                    birth_low += SCALE//source
                    new_cost += Fraction(1, source)
            require(new_cost <= Fraction(1, old_modulus), "parent harmonic birth cap")
        require(len(current) == len({r for r, _, _ in current}), "distinct actual sources")
        if N <= 11:
            expected = {(r, *answer) for r in range(1, 2**N)
                        if (answer := literal(N, r)) is not None}
            require(set(current) == expected, "independent full residue enumeration")
        next_debts = {}
        for d, count in debt_counts.items():
            next_debts[d+3] = next_debts.get(d+3, 0)+count
            if d >= 5:
                next_debts[d-5] = next_debts.get(d-5, 0)+count
        debt_counts = next_debts
        observed = {}
        for _, _, grade in current:
            d = 8*grade-5*N
            observed[d] = observed.get(d, 0)+1
        require(observed == debt_counts, "native parity bijection and debt recurrence")
        reserve = sum((Fraction(count*(d+5), 2**N) for d, count in debt_counts.items()),
                      Fraction())
        upper = Fraction(harmonic_low+len(current), SCALE)+reserve
        # The first exact step has equality. Use exact rational arithmetic
        # there; later outward bounds are strictly separated.
        if N == 1:
            require(sum((Fraction(1,r) for r, _, _ in current), Fraction())+reserve
                    == previous_upper, "initial reserve equality")
        else:
            require(upper <= previous_upper, "monotone harmonic reserve")
        previous_upper = Fraction(harmonic_low, SCALE)+reserve
        output.append({
            "binary_clock": N,
            "accepted_words": len(current),
            "smallest_principal_source": min(r for r, _, _ in current),
            "harmonic_enclosure_scaled": [harmonic_low, harmonic_low+len(current)],
            "new_sources": births,
            "birth_enclosure_scaled": [birth_low, birth_low+births],
            "gate_probability": str(Fraction(len(current), 2**N)),
            "rational_reserve": str(reserve),
        })
        rows = current
    require(4**8*100**8 < 3**3*5**5*97**8, "rational Chernoff ceiling")
    return {
        "scope": "finite exact binary-prefix sums, actual residues, and harmonic birth reserve",
        "scale": SCALE,
        "depth_zero_formal_mass": 0,
        "small_input_first_clocks_1_through_32": all_good_clocks,
        "direct_residue_crosscheck_through_binary_clock": 11,
        "rows": output,
    }


if __name__ == "__main__":
    print(json.dumps(controls(), indent=2))
