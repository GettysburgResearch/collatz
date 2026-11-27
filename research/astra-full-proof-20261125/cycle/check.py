"""Replay excursion budgets on ordinary windows and two strict exponent comparisons."""
import json
from fractions import Fraction
from itertools import product


def require(ok, label):
    if not ok:
        raise ArithmeticError(label)


def odd_step(x):
    y = 3 * x + 1
    a = (y & -y).bit_length() - 1
    return y >> a, a


def replay():
    tested = high_visits = repeated_words = 0
    terminal_by_word, small_by_word = {}, {}
    for source in range(1, 5002, 2):
        values, gaps = [source], []
        for _ in range(12):
            y, a = odd_step(values[-1])
            values.append(y)
            gaps.append(a)
        for n in range(1, 13):
            m = min(values[:n + 1])
            H = 12 * m // 5
            ends = [i for i in range(1, n + 1) if values[i] > H]
            R, A = len(ends), sum(gaps[i - 1] for i in ends)
            left = m**R * (1 << A) * max(H, values[n])
            right = (3*m + 1)**R * max(H, source)
            require(left <= right, ("clipped product", source, n))
            if source <= H:
                require(m**R * (1 << A) <= (3*m + 1)**R,
                        ("initially low budget", source, n))
            word = tuple(gaps[:n])
            if word in terminal_by_word:
                difference = values[n] - terminal_by_word[word]
                require(difference % 3**n == 0, ("terminal congruence", source, n))
                repeated_words += 1
            else:
                terminal_by_word[word] = values[n]
            if values[n] < 3**n:
                require(small_by_word.setdefault(word, values[n]) == values[n],
                        ("ordinary terminal", source, n))
            tested += 1
            high_visits += R
    return dict(windows=tested, marked_endpoints_with_multiplicity=high_visits,
                repeated_valuation_word_congruences=repeated_words)


def bounds():
    # ln(K/2)/ln(3) + 15/596 < u/v, using exact integer powers.
    params = [(6, 5, 50, 261), (7, 5, 100, 301)]
    for num, den, u, v in params:
        exponent = 596*u - 15*v
        require(exponent > 0 and num**(596*v) < den**(596*v) * 3**exponent,
                ("strict entropy margin", num, den, u, v))
    require((298 * 3 * 3)**2 < 3**15, "entropy overhead")
    require(3**63 < 2**100 and 9**6 > 2*8**6, "adjacent ambiguity margin")
    require(12*1998 < 3**10, "rare mark overhead for two gaps")
    require(Fraction(37, 100) - Fraction(13, 300) + Fraction(10, 1998)
            < Fraction(100, 301), "paired-clock exponent margin")
    for advance in (1, 2):
        allowed = sum(advance + hi - lo in (1, 2) for lo in (0, 1) for hi in (0, 1))
        require(allowed == 3, "three legal clock pairs")
    return len(params) + 1


def block_edges(p, h):
    delta, wrap = h - p, 2*p - h
    free = set(range(1, wrap))
    intermediate = set(range(wrap + 1, delta))
    upper = {r for r in range(p) if 3*p < 5*r and 25*r < 18*p}
    cells, role = [], {}

    def add(ranks, choices):
        require(not set(ranks).intersection(role), "disjoint rank blocks")
        for i, rank in enumerate(ranks):
            role[rank] = (len(cells), i)
        cells.append(choices)

    for v in sorted(upper):
        P, N = v - delta, v - wrap
        S = P + wrap
        require(P in free and N in free and S in intermediate, "block roles")
        choices = [w for w in product((0, 1), repeat=4)
                   if w[0] <= w[1] and w[2] <= w[1] and w[2] <= w[3]]
        require(len(choices) == 8, "eight four-site assignments")
        add((S, P, v, N), choices)
    for i in sorted(intermediate.difference(role)):
        add((i, i - wrap), [(0, 0), (0, 1), (1, 1)])
    for f in sorted(free.difference(role)):
        add((f,), [(0,), (1,)])
    for r in sorted(set(range(p)).difference(role)):
        add((r,), [(0,)])
    assignments = 1
    for choices in cells:
        assignments *= len(choices)
    exact_count = 2**len(free) * Fraction(3, 2)**len(intermediate) * Fraction(4, 3)**len(upper)
    require(assignments == exact_count, "factorized count")
    for r in range(p):
        b, u = divmod(r + h, p)
        first, i = role[r]
        second, j = role[u]
        for left in cells[first]:
            right_choices = [left] if first == second else cells[second]
            for right in right_choices:
                require(b + left[i] - right[j] in (1, 2), ("illegal edge", p, r))
    return dict(period=p, checked_edges=p, four_site_cells=len(upper),
                count=assignments, exceeds_ternary_threshold=(assignments**3 > 3**p))


if __name__ == "__main__":
    require(2**158 < 3**100 < 2**159 and 2**147 > 3**88, "order entropy margin")
    census = [block_edges(41, 65), block_edges(306, 485)]
    print(json.dumps({**replay(), "strict_exponent_checks": bounds(),
                      "four_site_count": census}, sort_keys=True))
