"""One exact mixed-clock fixture, with integer full-lap replay. Standard library."""
from math import gcd
import json


def check(condition, message):
    if not condition:
        raise ArithmeticError(message)


def run():
    g, n, S = 6, 572, 905
    seed = tuple(v for j in range(g) for v in
                 (1+(j % 3 == 1), 2-(j % 3 == 1), 1+(j % 2 == 1), 2-(j % 2 == 1), 2))
    # Horner arithmetic modulo Y^10 - 256Y^5 + 65536, the unlifted H_6.
    rem, pos = [0]*10, 0
    for gap in seed:
        lead = rem[-1]
        rem = [2**pos] + rem[:-1]
        rem[0] -= 65536*lead
        rem[5] += 256*lead
        pos += gap
    check(not any(rem), 'seed polynomial remainder')
    prefix = tuple((i+1)*S//(n-1)-i*S//(n-1) for i in range(n-1))
    word = tuple(x for last in seed for x in (*prefix,last))
    a, b = 8+5*S, 5*n
    A, p = g*a, g*b
    check(gcd(a,b)==1 and len(word)==p and set(word)=={1,2},'clocks')
    # A repeat count must divide both clocks and hence divide six.
    for q in (2,3):
        check(word != word[p//q:]+word[:p//q], 'proper power')
    C = pos = 0
    for gap in word:
        C = 3*C + (1 << pos)
        pos += gap
    D = (1 << A) - 3**p
    H = 3**(2*b) - 2**a*3**b + 2**(2*a)
    check(pos==A and D>0 and C%H==D%H==0,'top evaluation')
    common = gcd(C,D)
    d, numerator = D//common, C//common
    first = minimum = numerator
    for gap in word:
        check(numerator>0 and numerator%2==d%2==1,'positive odd reduced state')
        quotient, remainder = divmod(3*numerator+d,1 << gap)
        check(remainder==0 and quotient%2==1,'literal gap')
        numerator = quotient
        minimum = min(minimum,numerator)
    check(numerator==first and 3**p>30*D and minimum>10*d,'closure or floor')
    check(d.bit_length()==18127 and H.bit_length()==9066,'denominator sizes')
    return dict(g=g,n=n,S=S,A=A,p=p,top_bits=H.bit_length(),denominator_bits=d.bit_length(),
                minimum_floor=minimum//d,product_minimum_floor=3**p//(3*D))


if __name__ == '__main__':
    print(json.dumps(run(),sort_keys=True))
