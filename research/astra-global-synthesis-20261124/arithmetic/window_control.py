"""Check every short-clock competitor before the analytic long-clock cutoff."""

from fractions import Fraction
from itertools import combinations


def require(test, msg):
    if not test:
        raise ValueError(msg)


def inverse_word(target, word):
    x = target
    for e in reversed(word):
        numerator = 2**e*x - 1
        if numerator % 3:
            return None
        x = numerator // 3
        require(x % 2 == 1, 'odd inverse')
    return x


def compositions(total, h):
    for cuts in combinations(range(1, total), h-1):
        ends = (0, *cuts, total)
        yield tuple(b-a for a, b in zip(ends, ends[1:]))


def main():
    windows = candidates = 0
    for horizon in range(1, 14):
        a = [1+(i % 2) for i in range(horizon)]
        time = [0]
        for e in a:
            time.append(time[-1]+e)
        c = [-5-(i % 2)*2 for i in range(horizon+1)]
        for t in (1, 43):
            values = [x + 2**(time[-1]+1-time[j])*3**(horizon+1+j)*t
                      for j, x in enumerate(c)]
            require(min(values)>2*Fraction(3,2)**horizon, 'uniform carry gate')
            for i, e in enumerate(a):
                require(3*values[i]+1 == 2**e*values[i+1], 'literal map')
                require(3*(values[i]-c[i]) == 2**e*(values[i+1]-c[i+1]), 'height law')
            for j in range(1, horizon+1):
                for i in range(j):
                    h = j-i
                    A = time[j]-time[i]
                    baseline = tuple(a[i:j])
                    for E in range(h, A+1):
                        for word in compositions(E, h):
                            candidates += 1
                            real = inverse_word(values[j], word)
                            signed = inverse_word(c[j], word)
                            require((real is None) == (signed is None), 'finite triadic legality')
                            if word == baseline:
                                require(real == values[i] and signed == c[i], 'unique clock minimizer')
                            else:
                                require(real is None, 'illegal short competitor')
                    windows += 1
    require(Fraction(1,3)+Fraction(2,3)*7 == 5, 'clock one deficit')
    require(Fraction(1,3)+Fraction(4,3)*5 == 7, 'clock two deficit')
    print('all finite windows and short-clock inverse words tested:', windows, candidates)


if __name__ == '__main__':
    main()
