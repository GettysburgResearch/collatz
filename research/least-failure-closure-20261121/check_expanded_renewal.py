#!/usr/bin/env python3
"""Exact finite certificates for the expanded five-energy renewal."""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

SCALE = 10**9
BLOCKS = ((1, 6, 65, (1, 2, 5)),
          (2, 4, 73, (1, 5, 1)),
          (4, 4, 121, (1, 3, 5)))

def need(ok, message):
    if not ok:
        raise ValueError(message)

def pow_upper(value, numerator=21, denominator=25):
    value = F(value)
    need(value > 0, "positive rational power input")
    target = value.numerator**numerator * SCALE**denominator
    divisor = value.denominator**numerator
    lo, hi = 0, 1
    while hi**denominator * divisor < target:
        hi *= 2
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid**denominator * divisor >= target:
            hi = mid
        else:
            lo = mid
    need(hi**denominator * divisor >= target, "upper power certificate")
    need((hi-1)**denominator * divisor < target, "least upper grid point")
    return F(hi, SCALE)

def ceil_scaled(value):
    value = F(value)*SCALE
    return (value.numerator+value.denominator-1)//value.denominator

def least_b(c, modulus, lower, clock_offset=0, correction=None):
    period = 2*modulus//3
    found = []
    for b in range(lower, lower+period):
        rhs = 1 if correction is None else correction
        exponent = b-2 if correction is None else b+clock_offset
        if (pow(2, exponent, modulus)*c-rhs) % modulus == 0:
            found.append(b)
    need(len(found) == 1, "unique inverse exponent class")
    return found[0]

def coefficient_row(c):
    need(0 < c < 81 and c % 3, "ternary unit residue")
    qmin = c
    while qmin < 5 or qmin % 2 == 0:
        qmin += 81
    bs = [least_b(c, 3**(r+1), 4) for r in (1, 2, 3)]
    powers = [F(3**(r+1), 1) /
              (2**(2*r+b)-F(4**(r+1)-3**(r+1), qmin))
              for r, b in zip((1, 2), bs)]
    tail_base = F(3, 1)/(2**bs[2]-F(4, qmin))
    new_bs, new_powers = [], []
    for a, lower, correction, target_prefix in BLOCKS:
        b = least_b(c, 81, lower, a+2, correction)
        new_bs.append(b)
        new_powers.append(F(81, 1)/(2**(a+2+b)-F(correction, qmin)))
    harmonic = sum(p/(1-F(1, 2**period))
                   for p, period in zip(powers, (6, 18)))
    harmonic += tail_base*F(3,4)**3/(1-F(3,4))/(1-F(1,2**54))
    harmonic += sum(new_powers)/(1-F(1,2**54))
    z = pow_upper(F(3,4))
    subcritical = sum(pow_upper(p)/(1-pow_upper(F(1,2**period)))
                      for p, period in zip(powers, (6,18)))
    subcritical += pow_upper(tail_base)*z**3/(1-z)/(1-pow_upper(F(1,2**54)))
    subcritical += sum(pow_upper(p) for p in new_powers)/(1-pow_upper(F(1,2**54)))
    high_a = 4 if c % 3 == 1 else 3
    high = F(3)/(2**high_a-F(1,qmin))/(1-F(1,4))
    bridge = harmonic+high
    need(bridge < F(7,8), "harmonic 7/8 residual bridge")
    need(harmonic < F(5,8), "harmonic 5/8 bound")
    need(subcritical < F(91,100), "subcritical 91/100 bound")
    return {"residue":c,"least_contributing_endpoint":qmin,
            "ladder_first_exponents_r123":bs,"new_first_exponents_a124":new_bs,
            "harmonic_upper_grid":ceil_scaled(harmonic),
            "harmonic_bridge_upper_grid":ceil_scaled(bridge),
            "subcritical_upper_grid":ceil_scaled(subcritical)}, harmonic, subcritical

def odd_step(n):
    need(type(n) is int and n > 0 and n % 2, "positive odd source")
    z, a = 3*n+1, 0
    while z % 2 == 0:
        z //= 2
        a += 1
    return z, a

def word(n, letters):
    for expected in letters:
        n, got = odd_step(n)
        need(got == expected, "actual division exponent")
    return n

def correction(prefix):
    positions = [0]
    for a in prefix:
        positions.append(positions[-1]+a)
    p = len(positions)
    return sum(3**(p-1-j)*2**v for j,v in enumerate(positions))

def main():
    rows = [coefficient_row(c) for c in range(1,81) if c % 3]
    need(len(rows) == 54, "complete endpoint cover")
    physical_cases = 0
    cylinders = []
    for a, lower, B, target_prefix in BLOCKS:
        source_prefix = (1,1,a)
        need(correction(source_prefix) == B, "source affine correction")
        need(correction(target_prefix) == 5*B, "target affine correction")
        shift = sum(target_prefix)-sum(source_prefix)
        need(lower-shift >= 1, "positive terminal target exponent")
        modulus = 2**(a+2+lower)
        residue = (-B*pow(81,-1,modulus))%modulus
        cylinders.append([a,lower,residue,modulus])
        affine_a, affine_b = modulus, residue
        for exponent in source_prefix:
            need(affine_a % 2 == 0 and affine_b % 2 == 1, "universal odd affine input")
            need(3*affine_a % 2**(exponent+1) == 0, "universal exact slope valuation")
            need((3*affine_b+1) % 2**exponent == 0 and
                 ((3*affine_b+1)//2**exponent) % 2 == 1,
                 "universal exact intercept valuation")
            affine_a = 3*affine_a//2**exponent
            affine_b = (3*affine_b+1)//2**exponent
        need(3*affine_a % 2**lower == 0 and (3*affine_b+1) % 2**lower == 0,
             "universal terminal valuation lower bound")
        for lift in (0,1,2,3,7,19,2**40,2**40+1):
            x = residue+modulus*lift
            z = word(x, source_prefix)
            q,b = odd_step(z)
            need(b >= lower and q % 3, "source endpoint and terminal guard")
            need(word(5*x, target_prefix+(b-shift,)) == 5*q, "physical paired target")
            need(3*q <= x, "smaller actual endpoint")
            need(81*x+B == 2**(a+2+b)*q, "inverse affine identity")
            physical_cases += 1
        for q in (5,7,13,43,61,163):
            b0 = least_b(q%81,81,lower,a+2,B)
            for k in (0,1,3,17):
                b = b0+54*k
                x = (2**(a+2+b)*q-B)//81
                need(81*x+B == 2**(a+2+b)*q, "complete large-gap source integrality")
                need(word(x, source_prefix+(b,)) == q, "large-gap actual source")
                need(word(5*x,target_prefix+(b-shift,)) == 5*q, "large-gap actual target")
                if k:
                    x0 = (2**(a+2+b0)*q-B)//81
                    need(x >= 2**(54*k)*x0, "geometric inverse tail")
                physical_cases += 1
    need(cylinders == [[1,6,271,512],[2,4,135,256],[4,4,87,1024]], "exact source cylinders")
    residues = [set(range(r,1024,m)) for _,_,r,m in cylinders]
    need(all(not residues[i]&residues[j] for i in range(3) for j in range(i)), "new cylinders disjoint")
    need(all(all(x%16 != 1 for x in c) for c in residues), "disjoint from full old ladder")
    density = F(1,24)+sum(F(2,m) for _,_,_,m in cylinders)
    need(density == F(85,1536), "relative source density")
    negative = []
    for wrong in ((1,2,4),(1,4,1),(1,3,4)):
        index=len(negative)
        need(correction(wrong) != 5*BLOCKS[index][2], "corruption not detected")
        negative.append(list(wrong))
    high_cases = 0
    for q in range(1,82,2):
        if q % 3 == 0:
            continue
        for a in range(3,25):
            numerator = 2**a*q-1
            if numerator % 3:
                continue
            x = numerator//3
            if x % 3 == 0:
                continue
            need(odd_step(x) == (q,a), "high-valuation actual source")
            v = 5*x
            for j in range(2):
                v = (3*v+1)//2 if v % 2 else v//2
            need(v == 5*2**(a-2)*q-1, "high-valuation residual identity")
            need(2*q <= x, "high-valuation smaller endpoint")
            high_cases += 1
    need(F(5,8) < 1 and F(91,100) < 1 and F(7,8) < 1, "strict contraction")
    output={
      "status":"PASS: exact finite certificates for the written renewal proof",
      "source_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
      "endpoint_classes":54,"grid_scale":SCALE,
      "harmonic_constant":[5,8],"subcritical_exponent":[21,25],
      "subcritical_constant":[91,100],"harmonic_residual_bridge_constant":[7,8],
      "largest_harmonic_row":max((r[0] for r in rows),key=lambda x:x['harmonic_upper_grid']),
      "largest_subcritical_row":max((r[0] for r in rows),key=lambda x:x['subcritical_upper_grid']),
      "largest_harmonic_bridge_row":max((r[0] for r in rows),key=lambda x:x["harmonic_bridge_upper_grid"]),
      "coefficient_rows":[r[0] for r in rows],
      "source_cylinders":cylinders,"relative_source_density":[85,1536],
      "physical_family_controls":physical_cases,"high_valuation_residual_controls":high_cases,
      "universal_source_prefix_affine_steps":9,"rejected_correction_controls":negative,
      "scope":["All rational-power enclosures use integer comparisons, without floating point.",
        "The finite residue cover certifies uniform constants; geometric tails and all-source domains are proved in the note.",
        "The uncovered five-energy remainder is not bounded here."]}
    print(json.dumps(output,indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
