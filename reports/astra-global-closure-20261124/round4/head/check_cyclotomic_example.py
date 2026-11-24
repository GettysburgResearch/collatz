"""Independent non-Paley degree-two test with a squared prime in the actual gcd."""

from math import gcd
import json
import sympy as sp


def require(test):
    if not test:
        raise ValueError('cyclotomic example failed')


def carry(bits):
    positions = [i for i, digit in enumerate(bits) if digit == '1']
    return sum(2**position * 3**(len(positions)-1-j) for j, position in enumerate(positions))


def main():
    n, length, weight = 5, 17, 6
    q, p = 2**length, 3**weight
    seed, near, far = '11001010100000100', '11111100000000000', '11111010000000000'
    replacement = '11001001000001100'
    ref = [seed, near, far, far, near]
    alt = [*ref[:4], replacement]
    require(all(len(word) == length and word.count('1') == weight for word in ref + alt))
    S = (q**n-p**n)//(q-p)
    C, Cref = carry(''.join(alt)), carry(''.join(ref))
    g, gref = gcd(S, C), gcd(S, Cref)
    d = (q**n-p**n)//gcd(q**n-p**n, C)
    require(g % (31**2) == 0 and gref % (31**2) == 0 and d % (S//g) == 0)

    x, y = sp.symbols('x y')
    V = sum(carry(word)*x**i for i, word in enumerate(ref))
    cyclotomic = sp.cyclotomic_poly(n, x)
    all_conjugates = sp.resultant(cyclotomic, y - V, x)
    coeff, factors = sp.factor_list(all_conjugates)
    require(coeff == 1 and len(factors) == 1)
    minimal, multiplicity = factors[0]
    require(sp.degree(minimal, y) == 2 and multiplicity == 2)
    require(int(minimal.subs(y, 0)) % gref == 0)

    error = carry(replacement) - carry(near)
    require(error != 0 and C - Cref == q**4 * error)
    # One damaged position a=4 becomes s=-2 with u=2, K=2, modulo N=5.
    G = sp.Poly(sp.expand(x**4 * minimal.subs(y, -error/x**2)), x)
    t = q * pow(p, -1, g) % g
    z = pow(t, 3, g)
    require((p*z*z-q) % g == 0 and int(G.eval(z)) % g == 0)
    resultant = int(sp.resultant(p*x**2-q, G.as_expr(), x))
    norm = int(sum(abs(c) for c in G.all_coeffs()))
    require(resultant != 0 and resultant % g == 0)
    require(abs(resultant) <= q**int(G.degree())*norm**2)
    print(json.dumps({'N':n, 'length':length, 'weight':weight, 'reference_carries':[carry(w) for w in ref],
                      'replacement_carry':carry(replacement), 'minimal_polynomial':str(minimal),
                      'reference_gcd':gref, 'altered_gcd':g, 'full_reduced_denominator':d,
                      'resultant':resultant, 'sympy_version':sp.__version__}, indent=2))


if __name__ == '__main__':
    main()
