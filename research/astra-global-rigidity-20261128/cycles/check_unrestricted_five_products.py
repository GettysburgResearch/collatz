"""Exhaust the combinatorial B5 dichotomy, allowing unrestricted index multiplicities."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from check_unrestricted_triple_products import require


def sign_sequence(c):
    return [sum(c[:i]) for i in range(len(c)-1,0,-1)]


def check_shape(c):
    ds = sign_sequence(c)
    if all(not(x>0 and y<0) for i,x in enumerate(ds) for y in ds[i+1:]):
        return False
    first = next(i for i,x in enumerate(ds) if x>0)
    require(all(x in (-1,0,1) for x in ds[first:]), 'post-crossing multiplicity')
    for gaps in ([1]*len(ds), [1,2,501,1,97,3,1,5,401,1,2]*len(ds)):
        exponent = 0
        numerator = 0
        for i,d in enumerate(ds):
            gap = 0 if i==0 else gaps[i]
            exponent += gap
            numerator = numerator * (2**gap) + d*3**i
            require(numerator != 0, 'lost prefix')
            if i>=first and d:
                require(numerator%2 == 1, 'failed odd terminal coefficient')
    return True


def main():
    total = double = aligned = 0
    for m in range(2,10):
        for early in combinations_with_replacement(range(m),2):
            for opposite in combinations_with_replacement(range(m),5):
                if set(early) & set(opposite):
                    continue
                c = [early.count(i)-opposite.count(i) for i in range(m)]+[3]
                if not c[0]:
                    continue
                total += 1
                has_two = check_shape(c)
                double += has_two
                aligned += has_two and sum(i*d for i,d in enumerate(c)) == 0
    six_prefix = sum(F(d*3**b, 2**e) for b,(d,e) in enumerate(zip((-3,-1,1,2),(0,1,3,4))))
    require(six_prefix == 0, 'order-six prefix control')
    require(aligned>0, 'missing aligned double crossings')
    print(f'{total} trimmed terminal-three B5 shapes, {double} returning below zero, '
          f'{aligned} such shapes indexed-aligned; B6 zero-prefix control passed')


if __name__ == '__main__':
    main()
