"""Exact finite interfaces of the elementary binary reachability witness."""

import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def valuation(n, prime):
    require(n > 0, 'valuation at a nonpositive integer')
    count = 0
    while n % prime == 0:
        n //= prime
        count += 1
    return count


def step(n):
    return (3*n+1)//2 if n % 2 else n//2


def odd_prefix(x):
    state, count = x, 0
    while state % 2:
        state = step(state)
        count += 1
    return state, count


def main():
    prefix_cases = 0
    power_endpoints = 0
    for x in range(1, 1 << 16, 2):
        y, k = odd_prefix(x)
        require(k == valuation(x+1, 2), 'wrong first-even clock')
        u = (x+1) >> k
        require(y+1 == 3**k*u, 'odd-run affine identity')
        if y > 2 and y & (y-1) == 0:
            a = y.bit_length()-1
            require(a >= 3 and a % 2 and a % (3**(k-1)) == 0,
                    'projected valuation relation failed')
            power_endpoints += 1
        prefix_cases += 1
    exponent_pairs = accepted = 0
    for a in range(2, 257):
        y = 1 << a
        require(valuation(y+1, 3) == (1+valuation(a, 3) if a % 2 else 0),
                'lifting valuation identity')
        for k in range(1, a+1):
            divisible = (y+1) % 3**k == 0
            predicted = a % 2 == 1 and a % 3**(k-1) == 0
            require(divisible == predicted, 'wrong projected pair')
            if divisible:
                x = (1 << k)*((y+1)//3**k)-1
                require(x > 0 and x % 2, 'nonpositive or nonodd witness')
                require(odd_prefix(x) == (y, k), 'constructed word is not physical')
                accepted += 1
            exponent_pairs += 1
    minima = []
    for k in range(2, 9):
        bound = 3**(k-1)
        found = next(a for a in range(2, bound+1)
                     if a % 2 and a % 3**(k-1) == 0)
        require(found == bound, 'wrong least target exponent')
        x = (1 << k)*(((1 << found)+1)//3**k)-1
        require(odd_prefix(x) == (1 << found, k), 'least-target orbit failed')
        # Pumping's arithmetic contradiction for each shorter positive insertion.
        for added in range(1, min(bound, 101)):
            require((bound+added) % bound != 0, 'pumped exponent still divisible')
        minima.append([k, found])
    print(json.dumps({'odd_prefix_cases':prefix_cases,
                      'power_two_endpoints':power_endpoints,
                      'exponent_pairs':exponent_pairs,
                      'accepted_pairs':accepted,
                      'least_target_exponents':minima,
                      'scope':'finite exact identities; not an infinite automata proof'},
                     sort_keys=True))


if __name__ == '__main__':
    main()
