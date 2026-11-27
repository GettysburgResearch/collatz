"""Independent modular controls for the local weight obstruction."""

if not __debug__:
    raise SystemExit("This independent assertion-based replay requires Python without -O or -OO.")

from math import prod


def exponent_mod_ternary(target, precision):
    # Lift the discrete logarithm one ternary digit at a time.
    exponent = 1
    period = 2
    for digits in range(2, precision + 1):
        modulus = 3**digits
        choices = [exponent + i * period for i in range(3)]
        exponent, = [e for e in choices if pow(2, e, modulus) == target % modulus]
        period *= 3
    return exponent, period


def local_values(exponent, k, mod, r=2, d=3, e=1):
    # Here mod is prime to three. All rational divisions in (4) are units.
    z = ((pow(2, exponent, mod) + 1) * pow(2, r, mod) * pow(3, -r, mod) - 1) % mod
    y = (pow(2, d, mod) * z + 1) * pow(3, -k, mod) % mod
    n = (pow(2, k, mod) * y - 1) % mod
    x = (pow(2, e, mod) * n - 1) * pow(3, -1, mod) % mod
    return x, z


def valuation(value, prime):
    result = 0
    while value % prime == 0:
        result += 1
        value //= prime
    return result


def run():
    primes = (5, 7, 13, 19)
    # The factor (19-1) and the (7-1) deliberately share factors with the ternary progression.
    B = prod(p-1 for p in primes)
    count = 0
    for k in (1, 2, 3, 7, 15, 25):
        r, d = 2, 3
        mod3 = 3 ** (2*k+r)
        target = (-1 + (2**d-1) * 3**r * pow(2, -(d+r), mod3)) % mod3
        L0, initial_period = exponent_mod_ternary(target, 2*k+r)
        J = initial_period * B
        assert initial_period == 2 * 3 ** (2*k+r-1)
        choices = []
        for p in primes:
            c = valuation(2**(2*B)-1, p)
            mod = p ** (c+1)
            residues = {pow(2, L0+J*t, mod) for t in range(p)}
            assert len(residues) == p and pow(2, J*p, mod) == 1
            # Exclude two deliberately chosen endpoint classes wherever classes differ.
            forbidden = {local_values(L0, k, mod)[0], local_values(L0+J, k, mod)[1]}
            legal = [t for t in range(p) if not (set(local_values(L0+J*t,k,mod)) & forbidden)]
            assert legal
            choices.append((legal[0], p, c, forbidden))
        # Explicit CRT, selecting each prime residue independently.
        total = prod(primes)
        t = sum(a*(total//p)*pow(total//p,-1,p) for a,p,_,_ in choices) % total
        for j in range(3):
            L = L0 + J*(t+j*total)
            assert pow(2,L,mod3)==target
            for a,p,c,forbidden in choices:
                assert not (set(local_values(L,k,p**(c+1))) & forbidden)
            count += 1
    print(f"verified {count} CRT-compatible exponents, 6 reset budgets and 4 simultaneous auxiliary primes")


if __name__ == "__main__":
    run()
