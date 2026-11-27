"""Exact finite period and full-denominator screens for the bounded odd strip."""
from bisect import bisect_right
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json


PERIOD_LIMIT = 10**1000
SCALE = 1 << 6900
MIN_HEIGHT = 1 << 30
MAX_WINDOW = 10_000
STRIP_NUM, STRIP_DEN = 53336, 10000
GAIN_NUM, GAIN_DEN = 100001, 100000
COARSE_BINS = (2, 4, 6, 8, 12, 16, 20, 24, 32, 48, 64)
RANK_BINS = (4, 8, 12, 16, 20, 24, 28, 32, 40, 48, 64)
DENOMINATOR_TESTS = ((100, 3), (250, 12), (500, 27))


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def ceil_div(n, d):
    return -(-n // d)


def log_interval(reciprocal):
    """Scaled bounds for 2 atanh(1/reciprocal) by downward integer powers."""
    power = SCALE // reciprocal
    total, j = 0, 0
    while power:
        total += power // (2*j + 1)
        power //= reciprocal**2
        j += 1
    return 2*total, 2*(total + 4*j + 4)


class AboveLog:
    def __init__(self):
        a, b = log_interval(2)
        c, d = log_interval(3)
        self.lower, self.upper = Fraction(a, d), Fraction(b, c)
        n, den = self.lower.as_integer_ratio()
        old_num, old_den = 0, 1
        cur_num, cur_den = 1, 0
        self.den, self.num = [0], [1]
        while cur_den <= PERIOD_LIMIT:
            coefficient, residue = divmod(n, den)
            old_num, cur_num = cur_num, old_num + coefficient*cur_num
            old_den, cur_den = cur_den, old_den + coefficient*cur_den
            self.num.append(cur_num)
            self.den.append(cur_den)
            require(residue != 0 or cur_den > PERIOD_LIMIT, 'log precision')
            n, den = den, residue

    def first_above(self, limit):
        """Right neighbor of the rational lower enclosure in Farey order limit."""
        j = bisect_right(self.den, limit)-1
        k = (limit-self.den[j-1]) // self.den[j]
        cut = Fraction(self.num[j-1]+k*self.num[j], self.den[j-1]+k*self.den[j])
        convergent = Fraction(self.num[j], self.den[j])
        return max(cut, convergent)


def next_fraction(q, limit):
    a, b = q.as_integer_ratio()
    residue = -pow(a, -1, b) % b
    den = residue + b*((limit-residue)//b)
    return Fraction((a*den+1)//b, den)


def layers(bins, steps, backwards):
    """Lists of path counts by total exponent in each starting-height bin."""
    states = [{0: 1} for _ in range(bins, bins*STRIP_NUM//STRIP_DEN+1)]
    yield states
    for j in range(1, steps+1):
        m = POW3[j]
        base = m.bit_length()
        windows = []
        for grade in range(max(j, base-4), min(2*j, base+3)+1):
            power = 1 << grade
            if backwards:
                lo = ceil_div(bins*m, power)-1
                hi = bins*m*STRIP_NUM // (power*STRIP_DEN)
            else:
                lo = ceil_div(bins*power*GAIN_DEN, m*GAIN_NUM)-1
                hi = bins*power*STRIP_NUM // (m*STRIP_DEN)
            windows.append((grade, lo, hi))
        for l, old in enumerate(states, start=bins):
            states[l-bins] = {g: old.get(g-1, 0)+old.get(g-2, 0)
                              for g, lo, hi in windows if lo <= l <= hi}
        yield states


def log3_floor(n):
    return bisect_right(POW3, n)-1


def possible_pairs(log, totals, max_bit, min_bit, min_period, denominator_bound):
    """All reduced slopes still allowed by the whole-strip ternary count."""
    candidates = defaultdict(list)
    active_bins = 0
    for k in range(min_bit, max_bit+1):
        width = denominator_bound << (k+1)
        center = log3_floor(width)
        cap = min(totals[b][l]*ceil_div(width, 2*b*POW3[l])
                  for b in COARSE_BINS for l in range(max(1, center-8), center+2))
        limit = min(PERIOD_LIMIT, cap)
        if limit < min_period:
            continue
        active_bins += 1
        rational = log.first_above(limit)
        roof = log.upper + Fraction(1, 1 << (k+1))
        while rational <= roof:
            if rational.denominator >= min_period:
                candidates[rational].append(k)
            rational = next_fraction(rational, limit)
    return candidates, active_bins


def literal_word_test():
    """Joint spacing on the five-phase rational counterexample."""
    nums = [283, 431, 653, 493, 373]
    exps = [1, 1, 2, 2, 2]
    for i, e in enumerate(exps):
        require(3*nums[i]+13 == (1 << e)*nums[(i+1)%5], 'fixed rational cycle')
    a, b = 3, 4
    require(exps[a-1] == exps[b-1] == exps[a] == exps[b] == 2,
            'one common backward and forward edge')
    modulus, gap = 3*8, abs(nums[a]-nums[b])
    require(gap % modulus == 0 and gap < 13*modulus, 'physical denominator matters')
    return {'denominator': 13, 'numerator_pair': [nums[a], nums[b]],
            'joint_modulus': modulus, 'numerator_gap': gap}


def joint_capacity(width, b, index, rev, fwd):
    """Optimize over actual two-sided cylinders at one supplied rank interval."""
    center = log3_floor(max(1, width//b))
    best = None
    for n in range(max(1, center-4), center+3):
        for j in range(n+1):
            i = n-j
            factor = 2*b*POW3[i]
            modes = fwd[b][j][index]
            subtotal = sum(c*ceil_div(width, factor << grade) for grade, c in modes)
            cnt = rev[b][i][index]*subtotal
            if best is None or cnt < best:
                best = cnt
    return best


def rank_sieve(log, survivors):
    upper_k = max(max(ks) for ks in survivors.values())
    n = log3_floor(1 << (upper_k+2))+5
    bins = set(b >> j for b in RANK_BINS for j in range(3))
    rev, fwd = {}, {}
    for b in bins:
        rev[b] = [[sum(s.values()) for s in row] for row in layers(b, n, True)]
        fwd[b] = [[tuple(s.items()) for s in row] for row in layers(b, n, False)]
    retained = []
    for slope, ks in sorted(survivors.items(), key=lambda pair: pair[0].denominator):
        p = slope.denominator
        floor = 1 << min(ks)
        require(1000 <= p <= floor//100, 'rank distortion and Riemann sum')
        require(slope > log.upper, 'pointwise upper height from slope')
        height = min(1 << (1+max(ks)), ceil_div(7*(slope-log.upper).denominator,
                                                 20*(slope-log.upper).numerator))
        allowed = True
        for b in RANK_BINS:
            for a in range(b, 2*b):
                cap = 0
                for j in (0, 1, 2):
                    den = b >> j
                    if a*STRIP_DEN <= den*STRIP_NUM:
                        cap += joint_capacity(height, den, a-den, rev, fwd)
                # log((a+1)/a) >= 2/(2a+1) by the atanh series.
                lower_count = Fraction(2884*p, 1000*(2*a+1))-Fraction(p*p, floor)-2
                if cap < lower_count:
                    allowed = False
                    break
            if not allowed:
                break
        if allowed:
            retained.append([slope.numerator, p])
    return retained


def small_checks(log):
    """Compare the two enumerators with literal finite lists at small depth."""
    for limit in range(2, 100):
        expected = min(Fraction(log.lower.numerator*k//log.lower.denominator+1, k)
                       for k in range(1, limit+1))
        require(log.first_above(limit) == expected, 'literal Farey right boundary')
        neighbor = next_fraction(expected, limit)
        require(neighbor > expected and
                all(Fraction(expected.numerator*k//expected.denominator+1, k) >= neighbor
                    for k in range(1, limit+1)), 'literal next rational')
    trials = 0
    for b in (1, 3, 5):
        for reverse in (False, True):
            for size, states in enumerate(layers(b, 6, reverse)):
                for a, row in enumerate(states, start=b):
                    counted = defaultdict(int)
                    for word in product((1, 2), repeat=size):
                        grade = 0
                        for i, e in enumerate(word, start=1):
                            grade += e
                            twos, threes = 1 << grade, POW3[i]
                            if reverse:
                                fits = ((a+1)*twos >= b*threes and
                                        a*twos*STRIP_DEN <= b*threes*STRIP_NUM)
                            else:
                                fits = ((a+1)*threes*GAIN_NUM >= b*twos*GAIN_DEN and
                                        a*threes*STRIP_DEN <= b*twos*STRIP_NUM)
                            if not fits:
                                break
                        else:
                            counted[grade] += 1
                    require(dict(counted) == {g: c for g, c in row.items() if c},
                            'literal strip words')
                    trials += 1
    return trials


def checks():
    require(STRIP_NUM*STRIP_DEN > 0 and STRIP_NUM < 8*STRIP_DEN, 'three bands')
    require((16*MIN_HEIGHT+7)*GAIN_NUM*STRIP_DEN < 3*MIN_HEIGHT*GAIN_DEN*STRIP_NUM,
            'maximum with multiplicative error')
    require(GAIN_DEN*3*MIN_HEIGHT <= GAIN_NUM*(3*MIN_HEIGHT-MAX_WINDOW),
            'finite accumulated error')
    lo2, hi2 = log_interval(3)
    require(1000*lo2 > 693*SCALE and 1442*hi2 < 1000*SCALE, 'log two constants')
    ell = Fraction(693, 1000)
    require((1/(2*ell)+Fraction(1,1000))*Fraction(1200,1199)/(3*ell) < Fraction(7,20),
            'rank-averaged upper height')
    log = AboveLog()
    literal_counts = small_checks(log)
    best = log.first_above(PERIOD_LIMIT)
    require(best > log.upper, 'strict Farey enclosure at full period cutoff')
    difference = best-log.upper
    max_height = ceil_div(difference.denominator, 2*difference.numerator)
    max_bit = max_height.bit_length()-1
    max_num = 10**max(x[1] for x in DENOMINATOR_TESTS) << (max_bit+1)
    max_depth = log3_floor(max_num)+2
    require(POW3[-1] > max_num and max_depth < MAX_WINDOW, 'global horizon')
    totals = {b: [sum(sum(s.values()) for s in row) for row in layers(b, max_depth, True)]
              for b in COARSE_BINS}
    raw, active = possible_pairs(log, totals, max_bit, 71, 1, 1)
    ranked = rank_sieve(log, raw)
    require((16*(1 << 71)+7)//3 < ranked[-1][1], 'small ordinary minima')
    rational = []
    for period_exponent, denominator_exponent in DENOMINATOR_TESTS:
        min_period, d = 10**period_exponent, 10**denominator_exponent
        require(6*MIN_HEIGHT*d < min_period, 'small minima and denominator floor')
        pairs, used = possible_pairs(log, totals, max_bit, 30, min_period, d)
        require(not pairs, 'rational denominator floor')
        rational.append({'min_period_power_of_ten': period_exponent,
                         'max_denominator_power_of_ten': denominator_exponent,
                         'active_height_bins': used, 'surviving_pairs': len(pairs)})
    return {'period_limit': '10^1000', 'height_log2_upper_bin': max_bit,
            'global_prefix_depth': max_depth, 'ordinary_height_bins': active,
            'ordinary_ternary_pairs': len(raw), 'ordinary_joint_pairs': ranked,
            'literal_farey_orders': 98, 'literal_word_cells': literal_counts,
            'denominator_tests': rational, 'fixed_denominator_control': literal_word_test()}


POW3 = [1]
for i in range(MAX_WINDOW):
    POW3.append(3*POW3[-1])

if __name__ == '__main__':
    print(json.dumps(checks(), indent=2))
