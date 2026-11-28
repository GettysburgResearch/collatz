"""Exact finite controls for the native-rotation proof. No asymptotic ST claim is tested."""
from fractions import Fraction
from itertools import product
from math import gcd, prod


def require(test, message):
    if not test:
        raise ValueError(message)


def valuation(n, p):
    if isinstance(n, Fraction):
        return valuation(n.numerator, p) - valuation(n.denominator, p)
    require(n != 0, 'zero has no finite valuation')
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def local_norm(n, p):
    return Fraction(p) ** -valuation(n, p)


def cycle(word):
    total = 0
    carry = 0
    for a in word:
        carry = 3 * carry + (1 << total)
        total += a
    divisor = (1 << total) - 3 ** len(word)
    if divisor <= 0:
        return None
    common = gcd(carry, divisor)
    y0, q = carry // common, divisor // common
    states = [y0]
    for a in word:
        nxt, remainder = divmod(3 * states[-1] + q, 1 << a)
        require(remainder == 0 and nxt % 2, 'illegal native cycle')
        states.append(nxt)
    require(states[0] == states[-1], 'cycle failed to close')
    return (states, q) if len(set(states[:-1])) == len(word) else None


def matching_runs(word, r):
    start = None
    runs = []
    for i in range(r + 1):
        match = i < r and word[i] == word[i + r]
        if match and start is None:
            start = i
        if not match and start is not None:
            runs.append((start, i))
            start = None
    return runs


def check_circle(r, intervals):
    # Group intervals of arbitrary nonnegative enlargement by their left residue.
    # Circle atoms are the r unit half-open cells; empty intervals cover none.
    longest = {}
    original = set()
    for left, end, enlargement in intervals:
        root = (left - enlargement) % r
        size = end - left + enlargement
        longest[root] = max(longest.get(root, 0), size)
        original.update(range(left, end))
    covered = { (root + i) % r for root, size in longest.items()
                for i in range(min(r, size)) }
    require(original <= covered, 'representative circle lost a physical interval')
    require(sum(longest.values()) >= len(original), 'representative gain too small')
    return len(longest) < len(intervals)


def check_path(word, states, q, r):
    S = [0]
    for a in word[:2*r]:
        S.append(S[-1] + a)
    B = [Fraction(1 << total, 3 ** i) for i, total in enumerate(S)]
    H = [b * y for b, y in zip(B, states)]
    runs = matching_runs(word, r)
    circles = []
    endpoints = []
    for b, c in runs:
        e = valuation(states[b] - states[b + r], 3)
        circles.append((b, c, e))
        lam = B[b+r] / B[b]
        protected = H[b] - H[b+r] / lam
        for t in range(b, c + 1):
            require(H[t] - H[t+r] / lam == protected, 'translated difference moved')
            require(valuation(states[t] - states[t+r], 3) == e + t - b,
                    'incorrect exact ternary gain')
            require((states[b] - states[b+r]) % (1 << (S[t] - S[b])) == 0,
                    'missing dyadic source divisor')
        # Numerical product check needs distinct interior-half endpoint labels.
        terminal = min(c, r-1)
        if terminal > 0 and terminal >= b:
            endpoints.append(terminal)
    check_circle(r, circles)
    return B, H, endpoints


def check_local_product(states, q, r, B, H, starts):
    # Small formal exponent box; its numerical factors may specialize to
    # rationally proportional values. Only the local-form product is tested.
    m = len(starts)
    dates = sorted(starts + [t+r for t in starts])
    require(len(set(dates)) == 2*m, 'endpoint labels repeated')
    lambdas = [B[t+r]/B[t] for t in starts]
    ternary = [valuation(states[t+r] - states[t], 3) for t in starts]
    box = list(product(range(2), repeat=m))
    actual = Fraction(1)
    for n in box:
        scale = prod(lam**a for lam, a in zip(lambdas, n))
        previous = None
        for l in dates:
            z = scale * H[l]
            real_factor = z if previous is None else z - scale*H[previous]
            finite3 = z
            if l >= r:
                j = starts.index(l-r)
                if n[j] == 0:
                    finite3 -= scale*lambdas[j]*H[l-r]
            actual *= abs(real_factor)*local_norm(z, 2)*local_norm(finite3, 3)
            previous = l
    row = Fraction(states[dates[0]])
    for a, b in zip(dates, dates[1:]):
        row *= (H[b] - H[a])/B[b]
    require(row <= (states[0]+q)*(2*r*q)**(2*m-1)*Fraction(3, 2)**dates[-1],
            'chronological height charge failed')
    expected = row**len(box) / 3**((len(box)//2)*sum(ternary))
    require(actual == expected, 'fixed-form product disagrees with exact valuation gain')


def main():
    paths = 0
    products_checked = 0
    saw_two = False
    for p in range(4, 9):
        # Count each distinct word at its supplied phase, including all rotations.
        for word in product((1, 2, 3), repeat=p):
            data = cycle(word)
            if data is None:
                continue
            states, q = data
            for r in range(2, p//2 + 1):
                B, H, starts = check_path(word, states, q, r)
                paths += 1
                if starts and (products_checked < 400 or
                               (len(starts) >= 2 and products_checked < 800)):
                    check_local_product(states, q, r, B, H, starts)
                    products_checked += 1
                    saw_two |= len(starts) >= 2
    synthetic = 0
    collapsed = 0
    for r in range(3, 11):
        for u in range(1, r):
            for e, f in product(range(2*r+1), repeat=2):
                collapsed += check_circle(r, [(0, u, e), (u, r, f)])
                synthetic += 1
    require(paths > 20000 and products_checked == 800 and saw_two,
            'insufficient ordinary/positive-rational local-product cases')
    require(collapsed > 1000, 'missing coincident effective circle starts')
    print(f'{paths} exact adjacent native path checks, {products_checked} full local-form products, '
          f'{synthetic} synthetic circle covers ({collapsed} coincident starts)')


if __name__ == '__main__':
    main()
