"""Exact integer controls for physical steering and attained-clock word packets."""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb
import json


def need(condition, reason):
    if not condition:
        raise ArithmeticError(reason)


def step(value):
    return (3*value+1)//2 if value % 2 else value//2


def trace(value, length):
    word = []
    for _ in range(length):
        word.append(value % 2)
        value = step(value)
    return tuple(word), value


def valuation(value):
    need(value != 0, "valuation of zero")
    return (abs(value) & -abs(value)).bit_length()-1


class Cylinder:
    """Common binary parameter for a list of physical, grade-labelled forms."""

    def __init__(self, count):
        self.residue = self.clock = 0
        self.forms = [(0, arm) for arm in range(count)]

    def expose(self, arm, desired):
        self.digit(desired ^ (self.forms[arm][1] % 2))

    def digit(self, digit):
        self.residue += digit << self.clock
        self.clock += 1
        updated = []
        for p, b in self.forms:
            current = b+digit*3**p
            updated.append((p+(current % 2), step(current)))
        self.forms = updated

    def merge(self, left, right, cases):
        while self.forms[left] != self.forms[right]:
            p, x = self.forms[left]
            q, y = self.forms[right]
            if (p, x) > (q, y):
                left, right = right, left
                continue
            s = q-p
            d = y-3**s*x
            if s:
                cases["positive_grade"] += 1
                cases["signed_disparity_"+str((d > 0)-(d < 0))] += 1
                limit = valuation(3**s-1)
                if d % 2 == 0:
                    if d and valuation(d) <= limit:
                        for _ in range(valuation(d)):
                            self.expose(left, 0)
                    else:
                        self.expose(left, 1)
                        for _ in range(limit-1):
                            self.expose(left, 0)
                self.expose(left, 1)
                need(self.forms[right][0]-self.forms[left][0] == s-1, "grade drop")
            elif d % 2 == 0:
                cases["equal_even"] += 1
                self.expose(left, 0)
                need(self.forms[right][1]-self.forms[left][1] == d//2, "equal halving")
            else:
                cases["equal_odd"] += 1
                self.expose(left, 0)
                c = (3*d+1)//2
                for _ in range(valuation(c)):
                    self.expose(left, 0)
                self.expose(left, 1)
                new_gap = self.forms[right][1]-self.forms[left][1]
                need(self.forms[left][0] == self.forms[right][0], "restored grades")
                need(2**valuation(c)*(4*new_gap+2) == 3*d+1, "equal macro")
                need(0 <= 4*new_gap < 3*d, "strict contraction")


def steering():
    cases = Counter()
    rows = []
    for count in [2, 3, 4, 7, 12, 18]:
        cylinder = Cylinder(count)
        cylinder.expose(0, 1)
        for arm in range(1, count):
            cylinder.merge(0, arm, cases)
            need(len(set(cylinder.forms[:arm+1])) == 1, "lost an earlier merger")
        p, endpoint = cylinder.forms[0]
        for lift in [0, 1, 5]:
            start = cylinder.residue+(lift << cylinder.clock)
            for arm in range(count):
                word, actual = trace(start+arm, cylinder.clock)
                need((sum(word), actual) == (p, 3**p*lift+endpoint), "ordinary lift mismatch")
        rows.append({"arms": count, "clock": cylinder.clock, "odd_count": p, "lifts": 3})
    for disparity in [-11, 0, 13]:
        cylinder = Cylinder(2)
        cylinder.forms = [(0, 20), (2, 9*20+disparity)]
        cylinder.merge(0, 1, cases)
        for lift in [0, 3]:
            start = 20+cylinder.residue+(lift << cylinder.clock)
            low, y = trace(start, cylinder.clock)
            high, z = trace(9*start+disparity, cylinder.clock)
            need(y == z and sum(low) == 2+sum(high), "generic signed profile")
    need(all(cases["signed_disparity_"+str(x)] for x in [-1, 0, 1]), "signed cases missing")
    return {"blocks": rows, "steering_cases": dict(sorted(cases.items()))}


def numerator(word):
    carry = 0
    for i, bit in enumerate(word):
        if bit:
            carry = 3*carry+(1 << i)
    return carry


def central_words(k, h, r):
    prefix = trace(r, h)[0]
    n = k-sum(prefix)-1
    need(n > 0, "central word length")
    for selected in combinations(range(2*n), n):
        bits = [0]*(2*n)
        for j in selected:
            bits[j] = 1
        word = prefix + tuple(bits)
        d = (1 << len(word))+3*numerator(word)
        yield word, d


def physical_packet(a, k, h, r, v, j, s, packet, i):
    """Record actual integer gates, parities, both residues, and rational widths."""
    x_values = set()
    for word, d in packet:
        numerator_x = a*(1 << s)-d
        x, rem = divmod(numerator_x, 3**k)
        need(rem == 0 and x > 0 and x % (1 << h) == r and x % 3**j == v, "mixed source")
        need(x not in x_values, "different words share a source at the same clock")
        x_values.add(x)
        actual_word, y = trace(x, len(word))
        need(actual_word == word and (3*y+1) == a << (s-len(word)), "real pre-pad prefix")
        gate_word, actual_gate = trace(x, s)
        need(sum(gate_word) == k and actual_gate == a, "actual long pad")
        need(a*(1 << s)-3**k*x == d and d <= 32*(1 << len(word)), "actual width")
        ray_word, q = trace(a, i)
        need(all(ray_word), "finite gate control was chosen to climb")
        b = k+i
        need(s+i == 2*b and len(gate_word)+len(ray_word) == 2*b, "balanced row clock")
        need(sum(gate_word)+sum(ray_word) == b, "balanced row grade")
        need((3*a+1)*3**b*x <= 3*a*4**b*q, "relative carry")
    return x_values


def complete_phase_sweep():
    k, h, r, v, j = 6, 2, 1, 2, 1
    p = 2*3**(k+j-1)
    lo = 2*k+20
    a = (1 << (2*p+lo+5))-1
    need(a % 3 != 0, "gate unit")
    words = list(central_words(k, h, r))
    admissible = [(w, d) for w, d in words if d <= 32*(1 << len(w))]
    n = k-sum(trace(r, h)[0])-1
    need(len(words) == comb(2*n, n) and len(admissible)*2 >= len(words), "central cut")
    classes = defaultdict(list)
    for w, d in admissible:
        classes[(d+3**k*v) % (3**(k+j))].append((w, d))
    mass = 0
    zero = 0
    phase_histogram = Counter()
    for s in range(lo, lo+p):
        label = (a*pow(2, s, 3**(k+j))) % 3**(k+j)
        packet = classes.get(label, [])
        phase_histogram[len(packet)] += 1
        if not packet:
            zero += 1
            continue
        sources = physical_packet(a, k, h, r, v, j, s, packet, s-2*k)
        shifted = physical_packet(a, k, h, r, v, j, s+p, packet, s+p-2*k)
        translation = (a*(1 << s)*((1 << p)-1))//3**k
        need(translation % ((1 << h)*3**j) == 0, "mixed translate")
        need({x+translation for x in sources} == shifted, "exact period translation")
        mass += len(packet)
    need(mass == len(admissible) and zero > 0, "complete phase ledger")
    return {"grade": k, "binary_depth": h, "ternary_depth": j, "period": p,
            "full_words": len(words), "retained_words": mass,
            "clock_histogram": dict(sorted(phase_histogram.items())),
            "rows_decoded_across_two_periods": 2*(p-zero),
            "sources_decoded_across_two_periods": 2*mass,
            "gate": "2^(2*period+initial_clock+5)-1; finite all-odd climb only"}


def mixed_block_example():
    # Search a short synchronization class independently by literal traversal.
    count = 4
    chosen = None
    for h in range(1, 20):
        for r in range(1, 1 << h, 2):
            profiles = [(sum(w), y) for w, y in [trace(r+j, h) for j in range(count)]]
            if len(set(profiles)) == 1:
                chosen = (h, r, profiles[0][0])
                break
        if chosen:
            break
    need(chosen is not None, "short block control missing")
    h, r, grade = chosen
    # Literal starts separated by 3*2^h retain both source moduli. After the
    # synchronization clock their forms differ by 3^(grade+1). Merge that
    # pair too and complete its shared tail to the exact central clock.
    spacing = 3*(1 << h)
    twin = Cylinder(2)
    twin.forms = [(0, 0), (0, spacing)]
    for bit in trace(r, h)[0]:
        twin.expose(0, bit)
    need(twin.residue == r and twin.forms[1][0] == grade, "spaced blocks share prefix")
    twin.merge(0, 1, Counter())
    paired = twin.clock-h
    gained = twin.forms[0][0]-grade
    n = max(90, paired)
    k = grade+1+n
    need(h+1 <= k//10, "linear-depth cell constraint")
    shared = [1]*(n-gained)+[0]*(n-paired+gained)
    packet = []
    for delta in [0, spacing]:
        front = trace(twin.residue+delta, twin.clock)[0]
        w = front+tuple(shared)
        d = (1 << len(w))+3*numerator(w)
        need(sum(w) == k-1 and len(w) == h+2*n, "central grade/clock")
        need(d <= 32*(1 << len(w)), "bounded endpoint offset")
        packet.append((w, d))
    modulus = 3**(k+1)
    labels = {(d+3**k) % modulus for w, d in packet}
    need(len(labels) == 1, "joint packet phase")
    label = next(iter(labels))
    s = max(2*k, h+2*n)+20
    i = s-2*k
    lift = ((label*pow(2, -s, modulus)+1)*pow(2, -(i+1), modulus)) % modulus
    a = (lift+modulus)*(1 << (i+1))-1
    need(a % 3 != 0, "finite control gate")
    convergence_clock = 0
    gate_orbit = a
    while gate_orbit != 1 and convergence_clock < 20_000:
        gate_orbit = step(gate_orbit)
        convergence_clock += 1
    need(gate_orbit == 1, "finite control gate has an actual path to one")
    sources = physical_packet(a, k, h, r, 1, 1, s, packet, i)
    need(max(sources)-min(sources) == spacing, "two literal disjoint blocks")
    q = trace(a, i)[1]
    for x in sources:
        for j in range(count):
            word, endpoint = trace(x+j, 2*(i+k))
            need(endpoint == q and sum(word) == i+k, "whole block at actual row")
            gate, endpoint = trace(x+j, s)
            need(endpoint == a and sum(gate) == k, "whole block at actual gate")
            distance = a*(1 << s)-3**k*(x+j)
            need(0 < distance <= 32*(1 << (h+2*n)), "ordinary block band")
    return {"arms": count, "binary_depth": h, "binary_residue": r,
            "start_grade": grade, "pre_gate_grade": k, "pre_gate_clock": s,
            "balanced_grade": i+k, "starts_examined": count*len(sources),
            "distinct_blocks": len(sources), "gate_bitlength": a.bit_length(),
            "gate_clock_to_one": convergence_clock}


def known_climbs():
    controls = []
    for m in range(2, 8):
        d = 3**m
        top = 1 << d
        u, rem = divmod(top+1, 3**m)
        need(rem == 0 and u % 3 == 0, "known gate unit lift")
        a = (u << m)-1
        w, stop = trace(a, m)
        need(all(w) and stop == top, "known odd climb")
        need(valuation(3*trace(a, m-1)[1]+1) == d+1, "last accelerated gap")
        rest, end = trace(stop, d)
        need(not any(rest) and end == 1, "known literal return to one")
        controls.append({"climb": m, "halvings": d, "source_bits": a.bit_length()})
    return controls


def family_control(offsets, binary_depth, odd_modulus, prescribed):
    last = max(offsets)
    representative = prescribed+(1 << binary_depth)*odd_modulus*(last+1)
    first_bits = binary_depth+3
    base_odd = 11+162*(representative-last)
    native_prefix = pow(3, base_odd, 1 << first_bits)
    c = Cylinder(len(offsets))
    grades = [162*(last-i) for i in offsets]
    c.forms = [(grade, -1) for grade in grades]
    for j in range(first_bits):
        c.digit((native_prefix >> j) & 1)
    for arm in range(1, len(grades)):
        c.merge(0, arm, Counter())
        need(len(set(c.forms[:arm+1])) == 1, "family previously merged arms")
    h = c.clock
    modulus = 1 << h
    need(c.residue % (1 << first_bits) == native_prefix, "original index cylinder")
    for lift in [0, 1, 3]:
        n = c.residue+(lift << h)
        actual = []
        for grade in grades:
            w, y = trace(3**grade*n-1, h)
            actual.append((y, grade+sum(w)))
        need(len(set(actual)) == 1, "complete physical post-peak bank")
    # Solve B^t = r/n_base in the full principal binary unit group. Keep a
    # multiplicative inverse residual so each exposed index bit is certified.
    native = pow(3, base_odd, modulus)
    residual = c.residue*pow(native, -1, modulus) % modulus
    reverse_power = pow(3, -162, modulus)
    t = 0
    for j in range(h-3):
        if ((residual-1) >> (j+3)) & 1:
            t += 1 << j
            residual = residual*reverse_power % modulus
        reverse_power = reverse_power**2 % modulus
    need(residual == 1 and t % (1 << binary_depth) == 0, "exponent reconstruction")
    period = 1 << (h-3)
    m_res = (representative+t) % period
    m = m_res+period*((prescribed-m_res)*pow(period, -1, odd_modulus) % odd_modulus)
    if m < last:
        m += period*odd_modulus
    for index in [m, m+period*odd_modulus]:
        need(index % ((1 << binary_depth)*odd_modulus) == prescribed % ((1 << binary_depth)*odd_modulus), "original parameter CRT")
        need(pow(3, 11+162*(index-last), modulus) == c.residue, "actual tower residue")
    return {"offsets": offsets, "initial_binary_depth": binary_depth,
            "odd_modulus": odd_modulus, "prescribed": prescribed, "post_peak_clock": h,
            "augmented_grade": c.forms[0][0], "verified_positive_lifts": 3,
            "first_checked_parameter_bitlength": m.bit_length()}


if __name__ == "__main__":
    print(json.dumps({"status": "finite controls only", "steering": steering(),
                      "full_phase_sweep": complete_phase_sweep(),
                      "actual_row_block": mixed_block_example(), "convergent_climbs": known_climbs(),
                      "canonical_family": [family_control(*args) for args in [
                          ([0, 1], 5, 9, 7), ([0, 1, 3], 3, 25, 11),
                          ([0, 1, 2, 3], 8, 7, 62)]]}, indent=2, sort_keys=True))
