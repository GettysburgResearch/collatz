"""Independent ordinary mirror paths and exact common-class cost controls."""
from fractions import Fraction as F


def require(test, message):
    if not test:
        raise ValueError(message)


def reverse_levels(limit):
    levels = [{1}]
    for _ in range(limit):
        row = {2*x for x in levels[-1]}
        pending = list(row)
        while pending:
            x = pending.pop()
            if x % 3 == 1:
                parent = (2*x+1)//3
                if parent not in row:
                    row.add(parent)
                    pending.append(parent)
        levels.append(row)
    return levels


def physical_levels(limit):
    rows = [set() for _ in range(limit+1)]
    for source in range(1, 2**limit+1):
        x, evens = source, 0
        seen = set()
        while x != 1 and evens <= limit and x not in seen:
            seen.add(x)
            if x % 2:
                x = (3*x-1)//2
            else:
                x //= 2
                evens += 1
        if x == 1 and evens <= limit:
            rows[evens].add(source)
    return rows


def crossing(scale, word, expected_residue):
    coefficient = F(2**scale)
    probability = F(1)
    odds = 0
    for i, letter in enumerate(word):
        coefficient *= F(2, 3) if letter == 'O' else 2
        probability *= F(3, 4) if letter == 'O' else F(1, 4)
        odds += letter == 'O'
        require((coefficient < 1) == (i == len(word)-1), 'not a first crossing')
    modulus = 3**odds
    residues = []
    for n in range(modulus):
        x = F(2**scale*(n+1)-1)
        for letter in word:
            x = (2*x-1)/3 if letter == 'O' else 2*x
        if x.denominator == 1:
            residues.append(n)
    require(residues == [expected_residue], 'wrong native ternary cylinder')
    return F(1, 4**scale)*probability-F(1, modulus)


def main():
    levels = reverse_levels(14)
    require(levels == physical_levels(14), 'inverse census differs from actual mirror orbits')
    odd = [sorted(x for x in row if x % 2) for row in levels[:8]]
    require(odd == [[1], [], [3], [], [11], [15], [29, 43], [39, 59]],
            'seven-even origin table changed')
    first = {0: F(0), 1: F(1, 5), 2: F(4, 5)}
    gamma = {0: F(1), 1: F(1, 5), 2: F(4, 5)}
    zero, common = F(1, 3)-F(1, 192), F(2, 3)-F(1, 192)
    for ell, row in enumerate(odd):
        for m in row:
            zero -= (F(16, 15)*first[(2**ell-m) % 3]
                     + F(4, 15)*first[(-2**ell-m) % 3])/4**ell
            common -= F(4, 3)*gamma[m % 3]/4**ell
    require(zero == F(74839, 307200) and common == F(6257, 20480), 'row-cost total')
    c1 = crossing(1, 'EOOOO', 60)
    c0 = crossing(0, 'EOO', 4)
    require(c1 == F(2465, 331776) and c0 == F(17, 576), 'strict overshoot')
    zero += c1
    common += c1+c0
    require(zero == F(1041139, 4147200) and zero > F(1, 4), 'zero protection margin')
    require(common == F(284051, 829440) and common > F(1, 3), 'joint protection margin')
    print('ordinary mirror origins checked:', 2**14, 'even budgets: 0 through 14')
    print('odd origin table through seven evens:', odd)
    print('full-space protected lower bounds: joint', common, 'zero class', zero)
    print('strict crossing cylinders: n=4 mod9; n=60 mod81')


if __name__ == '__main__':
    main()
