"""Exact controls for multiple-lap lifting and ordinary chronological rise charges."""
from fractions import Fraction
from itertools import product


def require(ok, message):
    if not ok:
        raise ValueError(message)


def cyclic_runs(word, r):
    p = len(word)
    good = [word[i] == word[(i+r) % p] for i in range(p)]
    if all(good):
        return [(0, p)]
    runs = []
    for i in range(p):
        if good[i] and not good[(i-1) % p]:
            length = 1
            while good[(i+length) % p]:
                length += 1
            runs.append((i, length))
    return sorted(runs, key=lambda pair: -pair[1])


def lift_test(word, r, K, take):
    p = len(word)
    d = K*p+r
    selected = cyclic_runs(word, r)[:take]
    marked = { (i+h) % p for i, length in selected for h in range(length) }
    total = sum(length for _, length in selected)
    serialized = [i % p in marked for i in range(K*p)]
    lifted_runs = 0
    for lap in range(K):
        previous = False
        for i in range(lap*p, (lap+1)*p):
            if serialized[i]:
                require(word[i%p] == word[(i+d)%p], 'lift changed native agreement')
                lifted_runs += not previous
            previous = serialized[i]
    require(sum(serialized) == K*total and lifted_runs <= 2*K*take,
            'seam count or mass changed')
    rises = word.count(1)
    require(sum(word[i%p] == 1 for i in range(2*d)) <= (2*K+2)*rises,
            'rise count escaped lap allowance')
    return any(i+length>p for i,length in selected)


def path_test(start, steps):
    y = [start]
    a = []
    B = [Fraction(1)]
    for _ in range(steps):
        raw = 3*y[-1]+1
        e = (raw & -raw).bit_length()-1
        a.append(e)
        y.append(raw >> e)
        B.append(B[-1] * Fraction(1 << e, 3))
    H = [z*b for z,b in zip(y,B)]
    for left in range(steps):
        count = 0
        partial = Fraction(0)
        for right in range(left+1,steps+1):
            count += a[right-1] == 1
            partial += B[right-1]
            growth = Fraction(3,2)**count
            require(B[left]/B[right] <= growth, 'slope rise bound')
            require(y[right]+1 <= growth*(y[left]+1), 'height rise bound')
            require(H[right]-H[left] == partial/3, 'chronological identity')
            require((H[right]-H[left])/B[right] <= (right-left)*growth/3,
                    'chronological rise charge')
    return steps*(steps+1)//2


def main():
    lifts = wrapped = 0
    for p in range(3, 9):
        for word in product((1,2),repeat=p):
            for r in range(1,p):
                for K in (1,2,4):
                    for k in (1,2,3):
                        wrapped += lift_test(word,r,K,k)
                        lifts += 1
    intervals = sum(path_test(x,16) for x in range(1,200,2))
    require(wrapped > 1000 and intervals == 13600, 'insufficient controls')
    print(f'{lifts} symbolic multiple-lap lifts ({wrapped} seam-crossing selections), '
          f'{intervals} actual positive-integer chronological intervals')


if __name__ == '__main__':
    main()
