"""Exact finite record table and finite-stage replay for Vasilyev Q7.3."""


def require(ok, message):
    if not ok:
        raise ValueError(message)


def up(x):
    return (3*x + 1)//2


def down(x):
    return (x + 1)//2


def script(x):
    r = x % 128
    if r % 4 == 3:
        return 'U'
    if r % 16 == 1:
        return 'UUU'
    if r % 16 == 13:
        return 'DUU'
    if r % 32 == 9:
        return 'UDUU'
    for residues, word in [((5, 57, 69, 121), 'UUUUU'), ((21, 85), 'DUUUU'),
                           ((25,), 'DUUDUU'), ((37, 101), 'UUDUU'),
                           ((53, 89), 'UUUDUU'), ((117,), 'UUUUUU')]:
        if r in residues:
            return word
    raise ValueError('expected an odd input')


def run(x, word):
    path = [x]
    for ch in word:
        x = up(x) if ch == 'U' else down(x)
        path.append(x)
    return path


def record_table():
    gaps = []
    for r in range(1, 128, 2):
        word = script(r)
        states = run(r, word)
        slopes = [128]
        for ch in word:
            require(slopes[-1] % 2 == 0, 'invalid affine transport')
            slopes.append(slopes[-1] * (3 if ch == 'U' else 1)//2)
        gaps.append(states[-1] - max(states[:-1]))
        require(slopes[-1] > max(slopes[:-1]), 'not a uniform strict record')
        require(states[-1] % 6 == 5 and slopes[-1] % 6 == 0, 'unexpected terminal residue')
        for q in (1, 7, 10**8):
            require(run(r+128*q, word) == [a+q*b for a,b in zip(states, slopes)], 'affine replay')
    require(min(gaps) == 2, 'incorrect minimum intercept excess')


def loop_erase(walk):
    out = []
    for x in walk:
        if x in out:
            del out[out.index(x)+1:]
        else:
            out.append(x)
    return out


def stage(m):
    walk = [m]
    while walk[-1] <= 64*(3*m+1) or walk[-1]%2 == 0:
        walk.append(up(walk[-1]))
    walk.extend(run(walk[-1], script(walk[-1]))[1:])
    path = loop_erase(walk)
    end = path[-1]
    require(end % 6 == 5 and end > max(path[:-1]), 'bad endpoint')
    require(min(path[1:]) > m and len(path)==len(set(path)), 'bad stage')
    require(all(y in (up(x),down(x)) for x,y in zip(path,path[1:])), 'illegal erased edge')
    return path


def cycle(m):
    seen = {}
    x = m+1
    while x not in seen:
        seen[x] = len(seen)
        require(m < x < 3*m and x != 2*m, 'left trapping region')
        x = up(x) if x < 2*m else down(x)
    return list(seen)[seen[x]:]


def check():
    record_table()
    m = 5
    for _ in range(3):
        path = stage(m)
        closed = cycle(m)
        require(set(closed).isdisjoint(path), 'cycle meets path')
        require(all(y in (up(x),down(x)) for x,y in zip(closed,closed[1:]+closed[:1])), 'illegal cycle')
        m = path[-1]
    print('64 affine residue certificates and three disjoint cycle/ray stages checked')


if __name__ == '__main__':
    check()
