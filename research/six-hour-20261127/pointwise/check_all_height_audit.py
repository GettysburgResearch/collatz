"""Independent exact finite controls for the all-height Collatz census and refinements."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, gcd
import json


def require(test, message):
    if not test:
        raise ValueError(message)


def valuation(x, prime):
    count = 0
    while x % prime == 0:
        x //= prime
        count += 1
    return count


def shortcut(x):
    return (3*x+1)//2 if x % 2 else x//2


def accelerated(x):
    v = 3*x+1
    e = (v & -v).bit_length()-1
    return v >> e, e


def source_octave(k):
    return range((1 << k)+1, 1 << (k+1), 2)


def actual_parities(x, length):
    bits = []
    for _ in range(length):
        bits.append(x % 2)
        x = shortcut(x)
    return tuple(bits)


def geometric_terminal_laws(depth):
    """Solve the exact infinite geometric tail via its one-step cyclic equation."""
    layers = [[Fraction(1)]]
    for d in range(1, depth+1):
        prev = layers[-1]
        modulus = 3**d
        order = 2*(modulus//3)
        residues = [pow(2, i, modulus) for i in range(order)]
        require(len(set(residues)) == order, "unit orbit")
        injection = [prev[(r-1)//3] if r % 3 == 1 else Fraction(0) for r in residues]
        # z_i = [injection_(i+1) + z_(i+1)]/2, indices cyclic.
        z0 = sum((1 << (order-j))*injection[j % order] for j in range(1, order+1))
        z0 /= (1 << order)-1
        masses = [Fraction(0)]*modulus
        masses[1] = z0
        for i in range(order-1):
            masses[residues[i+1]] = 2*masses[residues[i]]-injection[i+1]
        require(2*masses[residues[-1]] == z0+injection[0], "cyclic closure")
        require(sum(masses) == 1 and min(masses) >= 0, "probability law")
        require(max(masses) <= Fraction(2, 3)**d, "parity envelope")
        layers.append(masses)
    return layers


def reflected_first_hit(layers):
    """Search ordinary negative inverses, cutting the full sum by total exponent."""
    summaries = []
    for s in range(1, len(layers)):
        cap = 6*s
        terminals = {}
        def walk(u, length, cost):
            if length == s:
                require(u not in terminals, "deterministic first-hit multiplicity")
                terminals[u] = cost
                return
            if u % 3 == 0:
                return
            for e in range(1, cap-cost-(s-length-1)+1):
                scaled = (u << e)+1
                if scaled % 3:
                    continue
                previous = scaled//3
                if previous == 1:
                    continue
                require(accelerated(-previous) == (-u, e), "reflected forward path")
                walk(previous, length+1, cost+e)
        walk(1, 0, 0)
        reduced_mass = sum(Fraction(1 << s, 1 << e) for e in terminals.values())
        increment = (1 << s)*layers[s][-1]-(1 << (s-1))*layers[s-1][-1]
        remainder_majorant = Fraction(1 << s, 1 << cap)*sum(comb(cap,j) for j in range(s))
        require(0 <= increment-reduced_mass <= remainder_majorant, "exact first-hit remainder")
        require(increment >= 0 and layers[s][-1] >= Fraction(1, 1 << s), "nested mass")
        summaries.append({"s": s, "starts": len(terminals),
                          "normalized_mass_millionths": int((1 << s)*layers[s][-1]*10**6)})
    return summaries


def source_transfer(layers):
    comparisons = 0
    class_count = 0
    stop_tests = 0
    source_count = 0
    depth = len(layers)-1
    for k in range(5, 14):
        sources = source_octave(k)
        n_sources = len(sources)
        source_count += n_sources
        m = 3*k//4
        jmax = k//3
        stopped = [[Counter() for _ in range(depth+1)] for _ in range(jmax+1)]
        word_classes = {}
        stopping_counts = [0]*(jmax+1)
        bit_words = set()
        for n in sources:
            parities = actual_parities(n,k)
            bit_words.add(parities)
            expect_indices = [i for i,p in enumerate(parities) if p]
            trajectory = [(n,0,())]
            while len(trajectory) <= jmax:
                x, cost, word = trajectory[-1]
                y,e = accelerated(x)
                trajectory.append((y,cost+e,word+(e,)))
            for j,(y,e_total,word) in enumerate(trajectory):
                if e_total > m:
                    stopping_counts[j] += 1
                    continue
                require(expect_indices[j] == e_total, "terminal odd index")
                word_classes.setdefault(word,[]).append((n,y))
                if trajectory[-1][1] <= m:
                    for d in range(depth+1):
                        stopped[j][d][y % 3**d] += 1
        require(len(bit_words) == n_sources and all(x[0] for x in bit_words), "source parity bijection")
        for j in range(jmax+1):
            expected = Fraction(sum(comb(m,i) for i in range(j)),1 << m)
            require(Fraction(stopping_counts[j],n_sources) == expected, "finite stopping law")
            stop_tests += 1
            for d in range(depth+1):
                for r in range(3**d):
                    if d <= j:
                        bound = layers[d][r]
                    else:
                        bound = layers[j][r % 3**j]/3**(d-j) + Fraction(1 << (m+1), 1 << k)
                    require(Fraction(stopped[j][d][r],n_sources) <= bound, "B3 transfer")
                    comparisons += 1
        for word,points in word_classes.items():
            exponent = sum(word)
            require(len(points) == n_sources >> exponent, "word exact mass")
            require(all((b-a,d-c) == (1 << (exponent+1),2*3**len(word))
                        for (a,c),(b,d) in zip(points,points[1:])), "synchronized source progression")
            class_count += 1
    return {"ordinary_sources":source_count, "stopping_laws":stop_tests,
            "stopped_residue_comparisons":comparisons, "full_word_progressions":class_count}


def all_height_cutoffs():
    instances = witnesses = 0
    for k in range(3, 9):
        for x in source_octave(k):
            for a,b in [(2,1),(5,2),(3,1),(4,1)]:
                hmax = 0
                while (2**a)*(hmax+1)**(a-b) < (x+1)**b:
                    hmax += 1
                actual = set()
                by_congruence = set()
                for h in range(1,hmax+1):
                    d = 0
                    while 3**(d*b) <= (2*h)**a:
                        d += 1
                    for q in range(1,h+1):
                        if q % 3 == 0:
                            continue
                        ps = range(1,h+1) if q == h else [h]
                        for p in ps:
                            if gcd(p,q) == 1 and 3**(b*valuation(q*x+p,3)) > (2*h)**a:
                                actual.add((p,q))
                        residue = (-q*x) % 3**d
                        for p in range(residue if residue else 3**d,h+1,3**d):
                            if max(p,q) == h and gcd(p,q) == 1:
                                by_congruence.add((p,q))
                require(actual == by_congruence, "complete all-height residue count")
                require(2**a*(hmax+1)**(a-b) >= (x+1)**b, "infinite height exclusion")
                instances += 1
                witnesses += len(actual)
    return {"all_height_cutoffs":instances,"qualifying_reduced_pairs":witnesses}


def marker_and_clocks():
    moment_cases = marker_events = 0
    for size in range(5, 13):
        for d in range(1,min(size-1,5)):
            pattern = (0,) + (1,)*(d+1)
            length = len(pattern)
            total = square = hits = 0
            for bits in product(range(2),repeat=size):
                count = sum(bits[i:i+length] == pattern for i in range(size-length+1))
                total += count
                square += count**2
                hits += bool(count)
            average = Fraction(total,1 << size)
            require(average == Fraction(size-length+1,1 << length), "marker mean")
            require(Fraction(square,1 << size) <= average+average**2, "marker second moment")
            require(Fraction(hits,1 << size) >= average/(1+average), "marker lower bound")
            moment_cases += 1
    for k in range(6,14):
        size = 2*k//3
        for n in source_octave(k):
            x=n
            dates=0
            last_zero=False
            ones=0
            for i in range(size):
                if not x%2:
                    last_zero=True
                    ones=0
                elif last_zero:
                    ones+=1
                    if ones >= 2:
                        d=ones-1
                        require((x+1) % 3**d == 0 and dates <= i, "physical marked endpoint")
                        marker_events += 1
                dates += x%2
                x=shortcut(x)
    return {"marker_moment_cases":moment_cases,"physical_marked_endpoints":marker_events}


def barrier_and_obstruction():
    max_tests = early_exits = crt_states = 0
    for k in range(3, 13):
        maxima = []
        for n in source_octave(k):
            odd = 0
            x = n
            maximum = Fraction(1)
            additive = 0
            for s in range(1,k+1):
                bit = x%2
                odd += bit
                additive = (3 if bit else 1)*additive+bit*(1 << (s-1))
                x = shortcut(x)
                require((x << s) == n*3**odd+additive, "physical affine decomposition")
                require(additive <= 3**s-(1 << s), "translation bound")
                maximum=max(maximum,Fraction(3**odd,1 << s))
                barrier = 1 << (k+2)
                if x >= barrier:
                    require(maximum >= Fraction(barrier,2*n),"maximal barrier witness")
                    early_exits += 1
            maxima.append(maximum)
        for num in range(2,26):
            threshold=Fraction(num,2)
            require(Fraction(sum(v>=threshold for v in maxima),len(maxima))*threshold
                    <= Fraction(3,2), "finite physical martingale maximal bound")
            max_tests += 1
    for k in [1,2,3,7,23,73,223,641]:
        for s in [1,7,k.bit_length()**2]:
            x=(1 << (k+1))*3**s-1
            for j in range(k+1):
                require(x+1 == (1 << (k+1-j))*3**(s+j),"CRT exact state")
                require(valuation(x+1,3) == s+j,"CRT exact valuation")
                if j<k:
                    x,e = accelerated(x)
                    require(e == 1,"CRT physical gap")
                crt_states+=1
    return {"finite_martingale_maximal_checks":max_tests,
            "completed_early_barrier_hits":early_exits,"CRT_states":crt_states}


def main():
    layers=geometric_terminal_laws(7)
    report = {"exact_geometric_residues":sum(map(len,layers)),
              "reflected_first_hit":reflected_first_hit(layers)}
    for section in [source_transfer(layers),all_height_cutoffs(),marker_and_clocks(),
                    barrier_and_obstruction()]:
        report.update(section)
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
