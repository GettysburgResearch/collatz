"""Replay one shaped rational family exactly, using no floating point."""
from fractions import Fraction
from math import gcd, prod


def require(ok, label):
    if not ok:
        raise ValueError(label)


def carry(word):
    total = fixed = 0
    for a in word:
        fixed = 3*fixed + (1 << total)
        total += a
    return fixed


def example(b, primes):
    n = (3**b).bit_length()
    require(gcd(n,b) == 1, 'noncoprime template')
    u = b//b.bit_length()
    low = [(j+1)*n//b - j*n//b for j in range(u)]
    markers = []
    for j in range(1,u-2):
        if low[j:j+2] == [1,2] and (not markers or j > markers[-1]+2):
            markers.append(j)
            if len(markers) == len(primes):
                break
    require(len(markers) == len(primes), 'too few separated markers')
    word = low + [1]*(2*b-n-low.count(1)) + [2]*(n-b-low.count(2))
    require(len(word) == b and sum(word) == n, 'wrong shaped clocks')
    N = prod(primes)
    A, B = 1 << n, 3**b
    c0 = carry(word)
    change = []
    for t in markers:
        swapped = word[:]
        swapped[t:t+2] = [2,1]
        change.append(carry(swapped) - c0)
    cycle_start = Fraction(c0,A-B)
    factors = []
    for prime, shift in zip(primes,change):
        F = (A**prime-B**prime)//(A-B)
        factors.append(F)
        cycle_start += Fraction(shift*B**(prime-1),(A-B)*F)
    q = cycle_start.denominator
    mean = N*c0 + sum((N//l)*d for l,d in zip(primes,change))
    require(q == ((A-B)//gcd(A-B,mean))*prod(factors), 'wrong full reduced denominator')
    y = cycle_start.numerator
    words = []
    min_y = y
    max_y = y
    for cell in range(N):
        w = word[:]
        for prime,t in zip(primes,markers):
            if cell%prime == 0:
                w[t:t+2] = [2,1]
        require(carry(w) == c0 + sum(d for l,d in zip(primes,change) if cell%l == 0),
                'diagonal superposition lost')
        words.append(bytes(w))
        for a in w:
            min_y,max_y = min(min_y,y),max(max_y,y)
            y, rem = divmod(3*y+q,1<<a)
            require(rem == 0 and y%2, 'invalid physical native transition')
    require(y == cycle_start.numerator and q>1, 'failed exact closure')
    require(max_y>2**(b//10)*min_y, 'missing shaped width')
    for i,l in enumerate(primes):
        lag = N//l
        distance = sum(sum(a != b_ for a,b_ in zip(w,words[(j+lag)%N]))
                       for j,w in enumerate(words))
        require(distance == 4*N//l, 'wrong full native Hamming distance')
    return N*b, q.bit_length(), (max_y//min_y).bit_length()


def main():
    # A coprime upper cell suffices for arithmetic controls; the proof takes
    # an infinite convergent subsequence for the asymptotic gap.
    b = next(b for b in range(270,330) if gcd((3**b).bit_length(),b)==1)
    results = [example(b,(5,7,11)), example(b,(7,17))]
    print('exact shaped native periods, denominator bits, integer width bits:', results)


if __name__ == '__main__':
    main()
