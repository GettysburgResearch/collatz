"""Finite source-preserving selector and independent ordinary inverse replays."""
from dataclasses import dataclass
from functools import cache
from itertools import product


def require(condition, message):
    if not condition:
        raise ValueError(message)


@dataclass(frozen=True)
class Row:
    delta: int
    mirror: int
    signed_word: str
    inverse: str
    residue: int
    modulus: int

    @property
    def extra(self):
        return self.inverse.count('O')


def mirror_origins(cap):
    """Every odd positive magnitude first hitting 1 after at most cap evens."""
    for m in range(1, 2**cap + 1, 2):
        x, even, odd = m, 0, 0
        word = []
        while x != 1 and even <= cap and odd <= 3 * cap:
            if x % 2:
                word.append('O')
                x = (3*x - 1) // 2
                odd += 1
            else:
                word.append('E')
                x //= 2
                even += 1
        if x == 1 and even <= cap:
            yield m, even, ''.join(word)


@cache
def registry(budget):
    """All first strict coefficient crossings over every allowed scale."""
    cap = (3**budget // 2**budget).bit_length() - 1
    origins = list(mirror_origins(cap))
    rows = []
    for a in range(cap + 1):
        frontier = [('', 0, 0)]
        while frontier:
            word, grade, carry = frontier.pop()
            d = len(word)
            if 2**(a+d) < 3**grade:
                modulus = 3**grade
                unit = pow(2**(a+d), -1, modulus)
                for m, even, signed in origins:
                    if even <= a:
                        residue = ((carry + 2**d*m)*unit - 1) % modulus
                        rows.append(Row(a-even, m, signed, word, residue, modulus))
                continue
            if grade == budget or 2**(a+d+budget-grade) >= 3**budget:
                continue
            frontier.append((word+'E', grade, 2*carry))
            frontier.append((word+'O', grade+1, 2*carry+3**grade))
    return sorted(rows, key=lambda r: (r.extra, len(r.inverse), r.delta, r.mirror))


def trace(x, word):
    """Check a claimed native word and return its actual endpoint."""
    for c in word:
        require(c in 'EO' and (x % 2 == 1) == (c == 'O'), f'invalid native letter {c} at {x}')
        x = (3*x+1)//2 if c == 'O' else x//2
    return x


def select(n, j, delta, budget):
    """Yield a checked smaller ordinary source of minimum extra odd grade."""
    require(n > 0 and 2*n >= budget*(1+3**budget), 'source below the selector cutoff')
    require((2**delta * (n+1)) % 2**j == 0, 'nonintegral virtual ramp')
    target = 3**j * ((2**delta*(n+1)) // 2**j) - 1
    for row in registry(budget):
        if row.delta != delta or n % row.modulus != row.residue:
            continue
        signed_odd = row.signed_word.count('O')
        if signed_odd > j:
            continue
        signed = row.signed_word + 'O'*(j-signed_odd)
        z = (n+1) * 2**(delta + signed.count('E')) - row.mirror
        m = z
        for c in row.inverse:
            if c == 'E':
                m *= 2
            else:
                require(m % 3 == 2, f'nonintegral inverse odd from {m}')
                m = (2*m-1)//3
        word = row.inverse[::-1] + signed
        require(0 < m < n and trace(m, word) == target, 'invalid smaller witness or endpoint')
        return row.extra, m, word, row
    return None


def direct(n, y, max_grade):
    """Independent finite DFS of actual inverses, minimizing the odd grade.

    E increases x+1, and O multiplies it by 2/3, hence each fixed-grade
    search can stop once even all its remaining O instructions fail.
    """
    for limit in range(max_grade + 1):
        frontier = [(y, 0)]
        while frontier:
            x, used = frontier.pop()
            if x < n:
                return used
            left = limit - used
            if 2**left * (x+1) >= 3**left * (n+1):
                continue
            frontier.append((2*x, used))
            if x % 3 == 2 and left:
                frontier.append(((2*x-1)//3, used+1))
    return None


def offset(word):
    a, p = 0, 0
    for c in reversed(word):
        a *= 2
        if c == 'O':
            a += 3**p
            p += 1
    return a-3**p


def tail(x, t):
    word = ''
    for _ in range(t):
        c = 'O' if x % 2 else 'E'
        word += c
        x = trace(x, c)
    return word, x


def post_select(n, H, t, budget):
    v, remainder = divmod(n+1, 2**H)
    require(remainder == 0 and v > 0, 'invalid positive cofactor')
    w, y = tail(3**H*v-1, t)
    f = w.count('O')
    require(H >= 21*(t-f)+9*budget+3, 'height outside the maximal-word cone')
    fibre = [''.join(s) for s in product('EO', repeat=t)
             if offset(''.join(s)) == offset(w)]
    require(all(beta.count('O') <= f for beta in fibre), 'upper word is not maximal')
    choices = []
    for beta in fibre:
        delta = f-beta.count('O')
        hit = select(n, H+delta, delta, budget)
        if hit is not None:
            b, m, path, row = hit
            require(trace(m, path+beta) == y, 'postpeak endpoint mismatch')
            choices.append((b, m, path+beta, row))
    return min(choices, key=lambda h: h[0]) if choices else None


def controls():
    for k in range(1, 7):
        total = positive = 0
        for r in range(3**k):
            for j, delta in [(0,0), (1,0), (2,0), (1,1), (2,2), (4,0), (7,1)]:
                H = max(j-delta, 1)
                v = (pow(2**H,-1,3**k)*(r+1)) % 3**k + (k+1)*3**k
                n = 2**H*v-1
                y = (2**delta*(n+1)//2**j)*3**j-1
                expected = direct(n, y, j+k)
                hit = select(n, j, delta, k)
                actual = None if hit is None else j+hit[0]
                require(actual == expected, ('pure grade mismatch', k,n,j,delta,expected,hit))
                total += 1
                positive += hit is not None
        print('pure',k,'rows',len(registry(k)),'compared',total,'productive',positive)
    for k in range(1, 5):
        positive = rows = scale_only = 0
        for r in range(3**k):
            t, H = 2, 21*2+9*k+3
            v = (pow(2**H,-1,3**k)*(r+1)) % 3**k + 3**k
            wanted = 3*pow(3,-H,4) % 4
            v += ((wanted-v)*pow(3**k,-1,4) % 4)*3**k
            n = 2**H*v-1
            w, y = tail(3**H*v-1, t)
            require(w == 'EO', ('unexpected test word', k, r, w))
            hit = post_select(n, H, t, k)
            possible = direct(n,y,H+w.count('O')+k)
            actual = None if hit is None else H+w.count('O')+hit[0]
            require(actual == possible, ('postpeak grade mismatch', k, r, actual, possible))
            rows += 1
            positive += hit is not None
            scale_only += hit is not None and select(n,H,0,k) is None
        print('postpeak',k,'compared',rows,'productive',positive,'positive only at scaled predecessor',scale_only)

if __name__ == '__main__':
    controls()
