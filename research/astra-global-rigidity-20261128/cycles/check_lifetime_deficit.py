"""Exact finite-height and constant controls for LIFETIME_LOWER_DEFICIT.md."""

from fractions import Fraction as F
from hashlib import sha256
import json


def require(ok, label):
    if not ok:
        raise ValueError(label)


def constant_controls():
    theta_lo, theta_hi = F(15849, 10000), F(15850, 10000)
    sqrt3_lo, sqrt3_hi = F(17320, 10000), F(17321, 10000)
    for t, low in [(theta_lo, True), (theta_hi, False)]:
        exact = 2**t.numerator < 3**t.denominator
        require(exact == low, 'theta interval')
    require(sqrt3_lo**2 < 3 < sqrt3_hi**2, 'sqrt three')
    mlo = (1-theta_hi/2-F(1,8))/(2*theta_hi*sqrt3_hi)
    mhi = (1-theta_lo/2-F(1,8))/(2*theta_lo*sqrt3_lo)
    require(F(1,68) < mlo < mhi < F(152,10000), 'm0 interval')
    require(F(47,48) < F(95,96)**2, 'square-root geometric decay')
    require(F(141,100)**2 < 2, 'square-root two')
    Ahi = mhi*96/F(141,100)
    require(Ahi < F(104,100), 'A upper endpoint')
    require(2*23**16 > 24**16, 'E less than twelve')
    lifetime_exponent = F(32,25*68**2)
    chernoff_exponent = F(201,100*8191)
    require(lifetime_exponent > chernoff_exponent, 'Chernoff margin')
    require(F(1, 2*(F(1,4)-F(1,10000)**2)) < F(201,100), 'local divergence bound')
    budget = F(4,5)*Ahi+F(4,25)
    require(budget < F(992,1000), 'retained deficit bound')
    return {'record_constant_bracket': [str(mlo), str(mhi)],
            'geometric_sum_upper': str(Ahi), 'absorbed_lifetime_fraction': str(budget),
            'quadratic_exponent_margin': str(lifetime_exponent-chernoff_exponent)}


def native_controls():
    paths = steps = negative_records = 0
    max_drop = (0, 1, 0)
    transcript = sha256()
    for n in range(1, 4097):
        y = n
        q = 0
        doubled_min = 0
        for t in range(193):
            if t:
                bit = y%2
                q += bit
                y = (3*y+1)//2 if bit else y//2
                steps += 1
            # Avoid logs and compare the exact product at each true clock.
            require((2**t)*y <= n*4**q, 'height cap')
            require(2**t <= n*4**q, 'lifetime cap')
            doubled = 2*q-t
            if doubled < doubled_min:
                negative_records += 1
                doubled_min = doubled
                if -doubled > max_drop[0]:
                    max_drop = (-doubled, n, t)
        transcript.update(f'{n},{y},{q},{doubled_min}\n'.encode())
        paths += 1
    return {'starts': paths, 'positive_native_steps': steps, 'fixed_horizon': 192,
            'strict_negative_records': negative_records,
            'largest_doubled_deficit_and_first_source_clock': max_drop,
            'endpoint_and_record_sha256': transcript.hexdigest()}


if __name__ == '__main__':
    print(json.dumps({'scope': 'Finite constants and ordinary prefix cap; the infinite lifetime bound uses the written record proof.',
                      'constants': constant_controls(), 'native': native_controls()}, sort_keys=True, indent=2))
