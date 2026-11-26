"""Exact integer supersolutions for Béhani's Bergman inverse-slope operator."""
import argparse
from fractions import Fraction
import hashlib
import json
from math import isqrt
from pathlib import Path


def upper_certificate(depth, scale=10**11, iterations=640, vector_path=None):
    if depth < 1 or scale < 1 or iterations < 0:
        raise ValueError("Depth and scale must be positive and iteration count nonnegative")
    modulus = 3**depth
    even = [(2*r) % modulus for r in range(modulus)]
    branch = list(range(2, modulus, 3))
    first = [(2*r-1)//3 for r in branch]
    lift = [tuple((x+j*(modulus//3)) % modulus for j in range(3))
            for x in first]
    unit = [r for r in range(modulus) if r % 3]
    def image(v):
        y = [6*v[e] for e in even]
        for r, (a,b,c) in zip(branch, lift):
            y[r] += 2*max(v[a], v[b], v[c])
        return y
    v = [scale if r%3 else 1 for r in range(modulus)]
    for _ in range(iterations):
        y = image(v)
        peak = max(y)
        den = 2*peak
        u = [1]*modulus
        for r in unit:
            u[r] = max(1, (peak*v[r]+scale*y[r])//den)
        v = u
    y = image(v)
    best = max(Fraction(m, 3*n) for m,n in zip(y,v))
    # This comparison is the certificate. The iteration need not converge.
    if any(m*best.denominator > 3*n*best.numerator for m,n in zip(y,v)):
        raise ArithmeticError("A residue failed the generated supersolution bound")
    if depth == 10 and best > Fraction(5516102802, 2482245023):
        raise ArithmeticError("The generated depth-ten table exceeds the published bound")
    lower = Fraction(20,9)
    bound = isqrt((best.numerator*10**16)//best.denominator)+1
    if bound**2*best.denominator < 10**16*best.numerator:
        raise ArithmeticError("The outward-rounded upper radius is too small")
    data = ''.join(f'{z}\n' for z in v).encode('ascii')
    digest = hashlib.sha256(data).hexdigest()
    if depth == 10 and scale == 10**11 and iterations == 640:
        expected = '91170eb02223527b842d0e06d8370ba6e8278f71f5a108f33075660de54dae88'
        if digest != expected:
            raise ArithmeticError('The published certificate digest differs')
    if vector_path is not None:
        Path(vector_path).write_bytes(data)
    return dict(depth=depth, residues=modulus, integer_scale=scale,
                iterations=iterations, vector_sha256=digest,
                upper_squared=str(best), squared_lower=str(lower),
                lower_radius_floor_8=isqrt((lower.numerator*10**16)//lower.denominator),
                upper_radius_ceiling_8=bound)


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--depth',type=int,nargs='+',default=[1,3,6,8,10])
    parser.add_argument('--write-vector', metavar='PATH',
                        help='Write one integer per line for a single selected depth')
    args=parser.parse_args()
    if args.write_vector is not None and len(args.depth) != 1:
        parser.error('--write-vector requires exactly one --depth')
    print(json.dumps([upper_certificate(h, vector_path=args.write_vector)
                      for h in args.depth],indent=2))
