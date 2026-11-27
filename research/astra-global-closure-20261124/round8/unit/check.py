"""Independent ordinary replay of ternary steering, grade barriers, and explicit rays."""

from collections import defaultdict
import json


def require(ok, detail):
    if not ok:
        raise ArithmeticError(detail)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def trace(n, clocks):
    positives = 0
    for _ in range(clocks):
        positives += n % 2
        n = step(n)
    return n, positives


def valuation(n, p):
    require(n > 0, 'valuation at zero')
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result


def short_route(q, p):
    route = []
    current = q
    for _ in range(p):
        for a in range(1, 5):
            y, remainder = divmod((current << a) - 1, 3)
            if not remainder and y % 3:
                require(trace(y, a) == (current, 1), 'illegal short step')
                route.append(a)
                current = y
                break
        else:
            raise ArithmeticError('no short route')
    return current, sum(route)


def shoot(q, p):
    y, raw = short_route(q, p)
    r = 5 * p + 13
    modulus = 3 ** r
    t = -(y + 1) * pow(2 ** raw, -1, modulus) % modulus
    return y, raw, r, t


def cell_replay():
    result = {'cell_count': 0, 'physical_lifts': 0, 'maximum_prefix_length': 0}
    for p in range(7):
        for q in range(1, 3 ** p + 1):
            if q % 3 == 0:
                continue
            y, raw, r, t = shoot(q, p)
            require(raw <= 4 * p, 'raw budget')
            result['cell_count'] += 1
            result['maximum_prefix_length'] = max(result['maximum_prefix_length'], raw)
            for ell in (0, 1, 3):
                lift = t + 3 ** r * ell
                target = q + 3 ** p * lift
                shifted_y = y + (lift << raw)
                m, remainder = divmod(shifted_y + 1, 3 ** r)
                z = (m << r) - 1
                require(not remainder and 0 < 171 * z < target, 'height or legality')
                require(trace(z, r + raw) == (target, r + p), 'incorrect physical path')
                result['physical_lifts'] += 1
    return result


def directed_replay():
    count = {'forward': 0, 'reverse': 0}
    for k in range(1, 5):
        for root in range(1, 2 * 3 ** k, 2):
            if root % 3 == 0:
                continue
            for mode in count:
                forward = mode == 'forward'
                p = k + 2 if forward else k
                q = step(3 * root) if forward else root
                y, raw, r, t = shoot(q, p)
                for ell in (0, 1, 2):
                    lift = t + 3 ** r * ell
                    u = root + 3 ** k * lift * (2 if forward else 1)
                    if not u % 2:
                        continue
                    target = q + 3 ** p * lift
                    m, rem = divmod(y + (lift << raw) + 1, 3 ** r)
                    z = (m << r) - 1
                    require(not rem and u % 3, 'unit eligibility')
                    require(target == (step(3 * u) if forward else u), 'wrong directed arm')
                    require(trace(z, raw + r) == (target, r + p), 'wrong directed path')
                    if forward:
                        require(5 * 167 * z < 27 * u, 'forward ratio')
                    else:
                        require(8 * 2351 * z < 123 * u, 'reverse ratio')
                    count[mode] += 1
    return count


def log4(residue, depth):
    """Solve 4^x = residue modulo 3^depth by lifting one ternary digit."""
    require(residue % 3 == 1, 'not a principal unit')
    x = 0
    order = 1
    for j in range(1, depth):
        modulus = 3 ** (j + 1)
        choices = [x + d * order for d in range(3)
                   if pow(4, x + d * order, modulus) == residue % modulus]
        require(len(choices) == 1, 'unexpected discrete-log multiplicity')
        x, = choices
        order *= 3
    return x


def special_rays():
    periods = []
    for s in range(1, 41):
        r = s + 13
        modulus = 3 ** (s + r)
        residue = (1 - 3 ** s * pow(4 ** s, -1, modulus)) % modulus
        j = log4(residue, s + r)
        d = 1 + 2 * j
        require(valuation(d - 1, 3) == s - 1, 'wrong exponent grade')
        require(s == 1 or (d + 1) % 3, 'one-odd unit condition')
        qmod = (pow(2, d, modulus) - 1) % modulus
        a = (qmod - 1) // (3 ** s)
        require(a % 3 and (2 + 4 ** s * a) % 3 ** r == 0, 'wrong lifted digit')
        require(171 * (2 ** r) * (4 ** s) < 3 ** (r + s), 'wrong ray budget')
        if s <= 3:
            periods.append({'s': s, 'r': r, 'first_d': d, 'period_d': 2 * 3 ** (s + r - 1)})
    return {'symbolically_checked_exponent_classes': 40, 'first_classes': periods}


def all_odd_meetings():
    # Enumerate actual paths from smaller z, index exact clocks and odd counts by endpoint.
    seen = defaultdict(list)
    results = {'smaller_meetings': 0, 'positive_reference_comparisons': 0, 'sources': 0,
               'largest_odd_excess': 0, 'pinned_sharp_example': None}
    for q in range(1, 401):
        if q > 1 and q % 2:
            results['sources'] += 1
            y = q
            for i in range(valuation(q + 1, 2) + 1):
                for z, h, p in seen[y]:
                    require(h > i and p > i, 'raw or odd excess')
                    require(p - i > valuation(q - 1, 3), 'strict relative grade')
                    results['smaller_meetings'] += 1
                    results['largest_odd_excess'] = max(results['largest_odd_excess'], p - i)
                    mod = 3 ** (p - i)
                    b = (q - 1) % mod + 1
                    require(2 * (q + 1) <= (b + 1) * (z + 1), 'reference bound')
                    results['positive_reference_comparisons'] += 1
                    if p - i == 1 + valuation(q - 1, 3) and q % 3 == 1 and z > 1 and i:
                        if results['pinned_sharp_example'] is None:
                            results['pinned_sharp_example'] = [q, z, i, h, p]
                y = step(y)
        y, odds = q, 0
        for h in range(42):
            seen[y].append((q, h, odds))
            odds += y % 2
            y = step(y)
    require(results['pinned_sharp_example'] is not None, 'expected sharp grade example')
    return results


def main():
    require(2 ** 122 < 3 ** 77 and 171 * 2 ** 13 < 3 ** 13, 'certificate conversion')
    print(json.dumps({'general_cells': cell_replay(), 'directed_arms': directed_replay(),
                      'mersenne': special_rays(), 'grade_barrier': all_odd_meetings()},
                     sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
