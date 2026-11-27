"""Exact finite physical controls for the critical permanent-safe entry argument."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from hashlib import sha256
import json


def require(condition, name):
    if not condition:
        raise ArithmeticError(name)


def step(x):
    u = 3*x+1
    e = (u & -u).bit_length()-1
    return u >> e, e


def small_words(length, budget, prefix=()):
    if length == 0:
        yield prefix
        return
    for e in range(1,budget-length+2):
        yield from small_words(length-1,budget-e,prefix+(e,))


def affine(word):
    h, N = 0, 0
    for e in word:
        N = 3*N+(1 << h)
        h += e
    return h,N


def finite_octaves():
    octaves = rows = word_checks = overflow = low_offsets = target_trials = 0
    max_low_ratio = Q(0)
    max_markov_ratio = Q(0)
    for m in range(6,15):
        x0 = 1 << m
        size = x0//2
        for s in range(1,min(5,m//2)+1):
            octaves += 1
            # Different levels of overflow are useful for the finite identities.
            H = min(m-1,2*s + max(1,m//6))
            words = Counter()
            high = Counter()
            target = defaultdict(list)
            K = (Q(1),Q(3,2),Q(2),Q(4))[s % 4]
            for x in range(x0+1,2*x0,2):
                y, eword = x,[]
                for _ in range(s):
                    y,e = step(y)
                    eword.append(e)
                word = tuple(eword)
                h,N = affine(word)
                require((y << h) == 3**s*x+N,'finite actual forward affine')
                if h > H:
                    overflow += 1
                    continue
                words[word] += 1
                if N > K*(1 << h):
                    high[h] += 1
                    continue
                target[(h,y)].append((x,N))
            exact_words = list(small_words(s,H))
            require(set(exact_words)==set(words),'complete stopped cylinders')
            complement = Q(1)
            for w in exact_words:
                prob = Q(1,1 << sum(w))
                require(Q(words[w],size)==prob,'physical stopped word mass')
                complement -= prob
                word_checks += 1
            require(size-sum(words.values())==complement*size,'overflow complement')
            high_prob = Q(sum(high.values()),size)
            require(high_prob <= s/(3*K),'Markov real offset on true octave')
            max_markov_ratio = max(max_markov_ratio,high_prob*3*K/s)
            for (h,y),pairs in target.items():
                Ns = [n for _,n in pairs]
                require(len(set(Ns))==len(pairs),'fixed y,h source uniqueness')
                modulus = 3**s
                require(all(3**(s-1)<=n<=K*(1<<h) and (n-(y<<h))%modulus==0
                            for n in Ns),'true numerator progression')
                normalized = Q(modulus*len(pairs),1<<h)
                require(normalized <= 4*K,'low offset row')
                for x,n in pairs:
                    require(Q(modulus*x,(1<<h)*y)==Q((y<<h)-n,y<<h),
                            'harmonic survival formula')
                max_low_ratio = max(max_low_ratio,normalized/(4*K))
                rows += 1
                low_offsets += len(pairs)
            # Several nonstationary sets, including a set of future exceptions.
            sites = {y for h,y in target}
            for choices in (set(y for y in sites if y%19==3),
                            set(y for y in sites if step(y)[1]>=4),
                            set(y for y in sites if min(y,step(y)[0])<x0//3)):
                left = sum(Q(3**s*len(pairs), (1<<h)*y)
                           for (h,y),pairs in target.items() if y in choices)
                right = 4*K*(H+1)*sum((Q(1,y) for y in choices),Q(0))
                require(left<=right,'arbitrary future-set physical transfer')
                target_trials += 1
    return dict(octave_block_pairs=octaves,actual_stopped_word_cylinders=word_checks,
                overflow_source_rows=overflow,low_offset_physical_sources=low_offsets,
                positive_endpoint_total_rows=rows,arbitrary_future_set_tests=target_trials,
                worst_fraction_of_low_row_bound=str(max_low_ratio),
                worst_fraction_of_offset_markov_bound=str(max_markov_ratio))


def sequential_restarts():
    starts = joins = tested = 0
    # Evaluate deterministic future-failure sets by both a flat trajectory walk
    # and a memoized backward recursion with changing, nonindependent endpoint tests.
    sizes = (2,3,2)
    predicates = (lambda j,y:(y%47)==9,lambda j,y:step(y)[1]>=7,
                  lambda j,y:y%43==5)
    for k in range(9,15):
        paths=[]
        Hs=(k-3,k-2,k-4)
        for x in range((1<<k)+1,1<<(k+1),2):
            current = x
            line = []
            flat = False
            for i,length in enumerate(sizes):
                z = current
                exceeded = False
                h = 0
                observed = []
                for j in range(length+1):
                    observed.append(current)
                    if j<length:
                        current, e = step(current)
                        h += e
                        exceeded = exceeded or h>Hs[i]
                local = exceeded or any(predicates[i](j,y) for j,y in enumerate(observed))
                flat |= local
                line.append((z,current,local))
            paths.append((x,line,flat))
        failure = set()
        for i in reversed(range(len(sizes))):
            outcomes={}
            for _,line,_ in paths:
                z,y,local = line[i]
                flag = local or y in failure
                require(z not in outcomes or outcomes[z]==flag,'physical shared endpoint')
                outcomes[z]=flag
            joins += len(paths)-len(outcomes)
            failure={z for z,f in outcomes.items() if f}
        for x,_,flat in paths:
            require((x in failure)==flat,'backward physical recursion')
            tested+=bool(flat)
        starts+=len(paths)
    return dict(ordinary_start_rows=starts,merged_shared_sources=joins,
                full_path_future_events=tested)


def finite_debt_suffixes():
    source_tests = positive_min_time = nonempty_suffix = 0
    record = (0,0,0)
    for n in range(3,32768,2):
        y = n
        debt = [0]
        # Finite surrogate: enforce actual n>=3 throughout this simple horizon.
        for j in range(1,41):
            y2,e = step(y)
            if y2 == 1:
                break
            debt.append(debt[-1]+7-4*e)
            y=y2
        t = debt.index(min(debt))
        require(all(v>=debt[t] for v in debt[t:]),'actual accepted suffix')
        require((1 << (7*t))*3**(4*t+4) <= n**4*10**(4*t),'finite minimum clock bound')
        positive_min_time += t>0
        nonempty_suffix += len(debt)-1-t>=5
        source_tests += 1
        record = max(record,(t,n,len(debt)-1-t))
    return dict(finite_ordinary_sources=source_tests,strictly_later_minimum=positive_min_time,
                five_or_more_remaining_safe_letters=nonempty_suffix,
                longest_first_minimum_with_seed_and_remaining_letters=record)


if __name__ == '__main__':
    print(json.dumps({"finite_octaves":finite_octaves(),"sequential_restarts":sequential_restarts(),
                      "finite_debt_suffixes":finite_debt_suffixes()},sort_keys=True,indent=2))
