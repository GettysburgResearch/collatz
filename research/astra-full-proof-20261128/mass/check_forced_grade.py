"""Exact bounded controls for the forced-grade comparison and terminal phase."""
from fractions import Fraction


def require(condition, description):
    if not condition:
        raise ArithmeticError(description)


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def valuation(n, prime):
    value = 0
    while n % prime == 0:
        n //= prime
        value += 1
    return value


def odd_count(n, steps):
    answer = 0
    for _ in range(steps):
        answer += n % 2
        n = shortcut(n)
    return answer


def forced_grade(a, b):
    return valuation(a, 3) + odd_count(b, valuation(a, 2))


def check_grade():
    steps = 0
    for a in range(2, 150, 2):
        for b in range(-30, 31):
            coefficient = a * (3 if b % 2 else 1) // 2
            require(forced_grade(a, b) == forced_grade(coefficient, shortcut(b)),
                    "a physical affine step changed the grade")
            steps += 1
    rows = 0
    for precision in range(8):
        modulus = 2 ** precision
        for level in range(9):
            for offset in range(-7, 8):
                gaps = [forced_grade(modulus * 3 ** level, 3 ** level * r + offset)
                        - forced_grade(modulus, r) for r in range(modulus)]
                require(Fraction(sum(gaps), modulus) == level,
                        "the mean signed grade difference changed")
                rows += 1
    return steps, rows


def first_hit(start, target=1):
    n = start
    for t in range(10_000):
        if n == target:
            return t
        n = shortcut(n)
    raise ArithmeticError("bounded ordinary fixture did not hit its target")


def check_phase():
    phase = {n: (-1) ** first_hit(n) for n in range(1, 1026)}
    for n in range(1, 340):
        require(phase[shortcut(n)] == -phase[n], "terminal phase transport")
        require(phase[2 * n] == -phase[n], "halving phase transport")
        require(phase[2 * n + 1] == -phase[3 * n + 2], "odd phase transport")
    # This true pair exhibits both complete first hits and permanent synchronous
    # separation via the phase certificate, without extrapolating a simulation.
    require(phase[1] != phase[2] and shortcut(1) == 2 and shortcut(2) == 1,
            "physical cycle-phase control")
    return len(phase)


if __name__ == "__main__":
    steps, rows = check_grade()
    phases = check_phase()
    print(f"PASS {steps} affine steps, {rows} averaged rows, {phases} finite phases")
