"""Exact binary control for the sharp 499-clock odd-base threshold."""
import json


def require(condition, description):
    if not condition:
        raise ValueError(description)


def word(x, h):
    p, c = 0, -1
    for i in range(h):
        if x % 2:
            p += 1
            c = 3*c + (1 << i)
            x = (3*x+1)//2
        else:
            x //= 2
    return x, p, c


def dyadic_log(g, target, valuation, bits):
    """Unique logarithm modulo 2^(bits-valuation) in 1+2^valuation Z_2."""
    modulus = 1 << bits
    require(valuation >= 2 and (g-1) % (2 << valuation) == 1 << valuation,
            "generator valuation")
    current, factor, exponent = 1, g % modulus, 0
    for i in range(bits-valuation):
        if (current-target) & (1 << (valuation+i)):
            exponent += 1 << i
            current = current*factor % modulus
        factor = factor*factor % modulus
    require(current == target % modulus, "dyadic logarithm")
    return exponent


def lift_example(d, H, p, c):
    modulus = 1 << H
    X = -c*pow(3, -p, modulus) % modulus
    A = 3**162
    m = dyadic_log(A, X*pow(3, -11, modulus) % modulus, 3, H)
    require((m-1) % (1 << 495) == 0, "odd-power image")
    ell = dyadic_log(5, m, 2, H-3)
    require(ell % (1 << d) == 0, "root exponent")
    b = pow(5, ell >> d, 1 << (H-3))
    require(pow(b, 1 << d, 1 << (H-3)) == m, "original ordinary power")
    require(pow(3, 11+162*m, modulus) == X, "complete physical residue")
    return dict(d=d, H=H, odd_base=b, parameter_modulus_bits=H-3,
                parameter_residue=m)


def main():
    h = 498
    x = 3**173-1
    y, p, c = word(x, h)
    require((1 << h)*y == 3**(173+p)+c and p == 240, "native affine identity")
    require((c+3).bit_length() == 497, "last possible odd position")
    modulus = 1 << h
    X = -c*pow(3, -p, modulus) % modulus
    require(X == 3**173, "native binary control")
    candidates = []
    for gap in range(1, 258):
        R = X*pow(3, -gap, modulus) % modulus
        endpoint, q, other = word(R-1, h)
        require((1 << h)*endpoint == 3**q*R+other, "earlier affine identity")
        if q == p+gap:
            require(other != c, "same signed constant")
            candidates.append(gap)
    print(json.dumps(dict(clock=h, source_exponent=173, odds=p, signed_carry=c,
                         carry_plus_three_bit_length=(c+3).bit_length(),
                         admissible_savings_scan=[1,257],
                         savings_with_correct_grade=candidates,
                         savings_with_correct_grade_and_carry=[],
                         ordinary_examples=[lift_example(493, 600, p, c),
                                            lift_example(0, 750, p, c)]), indent=2))


if __name__ == "__main__":
    main()
