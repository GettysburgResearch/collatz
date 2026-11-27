"""Independent finite controls for ordinary ramp descent and its inverse price."""

from itertools import combinations


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    return (3*x+1)//2 if x % 2 else x//2


def hit_price(x, max_odds):
    """First hit or no hit within the promised odd-time budget."""
    y, clock, odds = x, 0, 0
    while y != 1 and odds < max_odds:
        y = 3*y+1
        gap = (y & -y).bit_length()-1
        y >>= gap
        clock += gap
        odds += 1
    return (odds, clock) if y == 1 else None


def prices(last):
    # A physical record with P odd departures and T clocks can be padded by
    # the 1->2->1 cycle up to every K>=P. Any source that improves the
    # resulting clock bound has u <= 2^clock/3^K by the positive carry.
    records = [(0, 1)] * (last+1)
    scanned = 0
    cap = 4000
    while True:
        for u in range(scanned+1+(scanned % 2), cap+1, 2):
            first = hit_price(u, last)
            if first is None:
                continue
            odds, clock = first
            surplus = 2*odds-clock
            if surplus > records[odds][0]:
                records[odds] = surplus, u
        scanned = cap
        best, result = (0, 1), []
        for k in range(last+1):
            if records[k][0] > best[0]:
                best = records[k]
            e = 2*k-best[0]
            b = 0
            while 2**(e+b) >= 3**(k+b):
                b += 1
            result.append((k, e, b, best[1], 2**e//3**k))
        needed = max(row[-1] for row in result)
        if needed <= scanned:
            return result, scanned
        # Increasing the preliminary sample in bounded batches keeps the
        # first weak clock witnesses from dictating an enormous first scan.
        cap = min(needed, 4*scanned)


def eligible_word(terminal, gaps):
    x = terminal
    for gap in reversed(gaps):
        numerator = 2**gap*x-1
        if numerator % 3:
            return False
        x = numerator//3
        if x <= 0 or x % 2 == 0:
            return False
    return True


def check_short_rows(prices_table):
    rows = 0
    for k, e, _, _, _ in prices_table[1:8]:
        earlier = False
        equality = False
        for clock in range(k, e+1):
            for cuts in combinations(range(1, clock), k-1):
                marks = (0, *cuts, clock)
                gaps = [marks[i+1]-marks[i] for i in range(k)]
                legal = eligible_word(1, gaps)
                rows += 1
                if legal and clock < e:
                    earlier = True
                if legal and clock == e:
                    equality = True
        require(equality and not earlier, "short row minimum")
    return rows


def check_ramps():
    cap, limit = 512, 72
    contacts = 0
    for n in range(2, cap+1):
        s = n % 3
        if s not in (0, 1):
            continue
        q, k = n-s, 0
        while q % 3 == 0:
            q //= 3
            k += 1
        y, j = n, 0
        phases = {y: j}
        while y % 2:
            y, j = step(y), j+1
            phases[y] = j
        for m in range(1, n):
            x, odds = m, 0
            for _ in range(limit+1):
                if x in phases:
                    require(odds > k+phases[x], "visitor under true price")
                    contacts += 1
                odds += x%2
                x = step(x)
    return contacts


def log_two_unit(a, precision):
    """Discrete log by ternary lifting, with no large exponent enumeration."""
    require(precision >= 1 and a % 3, "unit required")
    e = 0 if a % 3 == 1 else 1
    m, period = 3, 2
    for _ in range(1, precision):
        m *= 3
        opts = [e+i*period for i in range(3) if pow(2, e+i*period, m) == a % m]
        require(len(opts) == 1, "unique lift")
        e = opts[0]
        period *= 3
    return e, period


def check_mersenne(prices_table):
    data = []
    for K, E, b, u, _ in prices_table[1:5]:
        modulus = 3**(K+b)
        residue = (2-3**K*(u+1)*pow(2**E,-1,modulus)) % modulus
        h, period = log_two_unit(residue, K+b)
        if h < 12:
            h += period
        n = 2**h-1
        z, rem = divmod(n-1,3**K)
        require(not rem, "source-1 fibre")
        y = u+2**E*z
        t, rem = divmod(y+1,3**b)
        require(not rem, "terminal congruence")
        m = 2**b*t-1
        require(0<m<n, "strict actual decrease")
        state, count = m, 0
        for _ in range(E+b):
            count += state % 2
            state = step(state)
        require((state,count) == (n,K+b), "first contact not assumed")
        for j in range(h):
            require(state%2 == 1, "positive all-odd extension")
            state=step(state)
        require(state == 3**h-1, "Mersenne apex")
        data.append((K,E,b,u,h))
    return data


def check_postpeak():
    tested = contacts = residuals = 0
    for height in range(5, 11):
        for cofactor in range(1, 64, 2):
            n = (1 << height)*cofactor-1
            peak = 3**height*cofactor-1
            if peak % 4:
                continue
            tested += 1
            m = 3*(1 << (height-2))*cofactor-1
            state, count = m, 0
            for _ in range(height):
                count += state % 2
                state = step(state)
            require(m<n and (state,count)==(peak//4,height-1), "sharp postpeak witness")
            if n>2048:
                continue
            for small in range(1,n):
                state, count = small, 0
                for _ in range(65):
                    if state==peak//4:
                        contacts += 1
                        require(count>=height-1, "second-halving grade minimum")
                    count += state % 2
                    state = step(state)
    for g in range(30):
        for t in range(3):
            v = (147*pow(27*3**g,-1,256))%256+256*t
            a = (27*3**g*v-147)//256
            n, m = 32*2**g*v-1, 27*2**g*v-1
            require(m<n and 3**(g+5)*v%256==43, "residual class")
            for source, clock, odds in ((n,g+13,g+7),(m,g+8,g+4)):
                state, count = source, 0
                for _ in range(clock):
                    count += state % 2
                    state = step(state)
                require((state,count)==(81*a+47,odds), "eight-clock physical route")
            residuals += 1
    require(step(13)==20 and 3**4-1==4*20, "H=4 guard")
    return tested, contacts, residuals


if __name__ == "__main__":
    rows, scanned = prices(120)
    short = check_short_rows(rows)
    print("All minima through K=120. Largest source cap scanned:", scanned)
    print("K, e_K, b_K, minimizing source, sufficient cap")
    for row in (*rows[1:8], *rows[10::10]):
        print(*row)
    print("Independent inverse compositions tested:", short)
    print("Ordinary ramp contacts, n<=512 and e<=72:", check_ramps())
    print("Physical Mersenne lifts (K,E,b,u,h):", check_mersenne(rows))
    print("Second-halving explicit witnesses, bounded contacts, residual routes:", check_postpeak())
