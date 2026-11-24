"""Exact finite controls. Run with python -B or python -O -B."""
import json
from fractions import Fraction


def check(condition, message):
    if not condition:
        raise ValueError(message)


def ordinary(start):
    q, a = [start], []
    while q[-1] != 1:
        y = 3 * q[-1] + 1
        twos = (y & -y).bit_length() - 1
        a.append(twos)
        q.append(y >> twos)
        if len(a) > 10000:
            raise ValueError("oracle guard exhausted")
    h = [Fraction(1)]
    for digit in reversed(a):
        h.append((digit + h[-1]) / 3)
    h.reverse()
    c = [-((-(value - Fraction(1, 2))) // 1) - 1 for value in h]
    b = [a[i] + c[i+1] - 3*c[i] for i in range(len(a))]
    check(all(x in (1, 2, 3) for x in b), "canonical digit")
    return q, a, b, c


def log_floor(t):
    if t < 0:
        return -pow(3,-t).bit_length()
    return pow(3,t).bit_length()-1


def baseline(size, shift=0):
    # floor(t log_2(3)) exactly, including t=0.
    return [log_floor(t+1)-log_floor(t)
            for t in range(shift,shift+size)]


def past_residue(word):
    A, C = 0, 0
    for digit in word:
        C = 3*C + (1 << A)
        A += digit
    mod = 3**len(word)
    return C*pow(1 << A, -1, mod) % mod


def piece_marks(word, language):
    n=len(word)
    cost=[0]+[n+1]*n
    cut=[0]*(n+1)
    for j in range(1,n+1):
        for i in range(j):
            if j-i==1 or tuple(word[i:j]) in language[j-i]:
                if cost[i]+1<cost[j]:
                    cost[j],cut[j]=cost[i]+1,i
    marks=set()
    j=n
    while j:
        j=cut[j]
        marks.add(j)
    check(len(marks)==cost[n],"piece traceback")
    return marks


def alignment(word, ref):
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def solve(i,j):
        if i==0:
            return j, frozenset({0} if j else set())
        if j==0:
            return i, frozenset(range(i))
        same=word[i-1]==ref[j-1]
        choices=[]
        for ii,jj,mark,delta in ((i-1,j-1,i-1,int(not same)),
                                  (i-1,j,i-1,1),(i,j-1,i,1)):
            prior, marks=solve(ii,jj)
            choices.append((prior+delta,marks|({mark} if delta and mark<len(word) else set())))
        return min(choices,key=lambda pair:pair[0])
    return solve(len(word),len(ref))


def main():
    prefixes = ordinary_windows = exceptional = low_level_tests = dirty_tests = 0
    for start in range(1, 1000, 2):
        q, a, b, c = ordinary(start)
        N0 = len(a)
        if not N0:
            continue
        P, E, K = [Fraction(1)], [Fraction(1)], [0]
        for i, gap in enumerate(a):
            P.append(P[-1]*Fraction(3,1 << b[i]))
            E.append(E[-1]*(1+Fraction(1,3*q[i])))
            K.append(K[-1]+c[i])
            diff = c[i+1]-2*K[-1]-c[0]
            check(q[i+1] == start*P[-1]*E[-1]*Fraction(2)**diff, "telescope")
        for N in sorted({1, N0//2+1, N0}):
            prefixes += 1
            m=1
            while 3**m <= max(q[:N]):
                m+=1
            marks={i for i in range(N) if c[i]}
            def touched(marks):
                return {j for i in marks for j in range(max(i,m),min(N,i+m+1))}
            bad=touched(marks)
            check(len(bad)<=(m+1)*K[N], "dirty-window cost")
            words=set()
            for j in range(m,N):
                word=tuple(a[j-m:j])
                check(past_residue(word)==q[j], "past endpoint")
                ordinary_windows+=1
                if j not in bad:
                    check(word==tuple(b[j-m:j]) and word not in words, "clean word")
                    words.add(word)
            check(N<=m+(m+1)*K[N]+len(words), "finite dictionary")
            for shift in (0,2,11):
                base=baseline(N,shift)
                for word, positive in ((b,marks),(a,set())):
                    mismatch={i for i in range(N) if word[i]!=base[i]}
                    bad=touched(mismatch|positive)
                    clean={tuple(a[j-m:j]) for j in range(m,N) if j not in bad}
                    check(len(clean)==max(0,N-m)-len(bad), "clean injectivity")
                    check(len(clean)<=m+1, "baseline language")
                    check(N<=m+(m+1)*(len(mismatch)+len(positive)+1), "Hamming")
                    dirty_tests+=1
            ex=[i for i in range(N) if c[i]>2*K[i]+c[0]]
            exceptional+=len(ex)
            for X in (1,2,8,32,max(q[:N])):
                small=[i for i in range(N) if P[i]<=X]
                picked=[i for i in ex if P[i]<=X]
                C=start*E[N]
                check(len(small)<=sum(t<=C*X for t in q[:N])+len(picked), "charge")
                for t,i in enumerate(picked):
                    check(3**t<=2*K[i]+1, "geometric mass")
                low_level_tests+=1
    piece_tests = edit_tests = 0
    limit=30
    language={m:{tuple(baseline(m,-k)) for k in range(m+1)} for m in range(1,limit+1)}
    for m,words in language.items():
        check(len(words)==m+1,"joint mechanical language size")
    for start in range(3,130,2):
        q,a,b,c=ordinary(start)
        N=min(len(a),limit)
        m=1
        while 3**m<=max(q[:N]):
            m+=1
        for digits,carry in ((a,set()),(b,{i for i in range(N) if c[i]})):
            w=digits[:N]
            def test_marks(marks,budget,slack):
                check(len(marks)<=budget,"mark budget")
                for j in range(N+1):
                    check(3**j<=2**(sum(w[:j])+budget+slack),"prefix discrepancy")
                for j in range(m,N):
                    if not any(i in marks|carry for i in range(j-m,j+1)):
                        check(tuple(a[j-m:j]) in language[m],"clean mechanical factor")
                check(N<=m+(m+1)*(len(carry)+budget+1),"finite comparison")
            marks=piece_marks(w,language)
            test_marks(marks,len(marks),0)
            piece_tests+=1
            for size,shift in ((max(0,N-3),2),(N,0),(N+2,7)):
                e,marks=alignment(w,baseline(size,shift))
                test_marks(marks,e,1)
                edit_tests+=1
    # Finite abstract carry words with maximum-growth bursts and complete resets.
    # These exercise local bounds only and do not assume an infinite ordinary source.
    c=K=0
    ex=[]
    for action in (['burst']*2+['reset']+['zero']*23+['burst']*15+['reset']+
                   ['zero']*64):
        if c>2*K:
            ex.append(K)
        new=3*c+2 if action=='burst' else 0
        b=3 if action=='burst' else 1
        a=b+3*c-new
        check(a>=1 and new+a==b+3*c,"synthetic carry")
        K,c=K+c,new
    check(len(ex)>=4 and any(v>100 for v in ex),"adversarial resets")
    for t,v in enumerate(ex):
        check(3**t<=2*v+1,"synthetic exceptional mass")
    print(json.dumps(dict(ordinary_sources=500,injective_prefixes=prefixes,
                          past_residue_tests=ordinary_windows,hamming_tests=dirty_tests,
                          low_level_tests=low_level_tests,ordinary_exception_occurrences=exceptional,
                          minimum_piece_tests=piece_tests, edit_alignment_tests=edit_tests,
                          synthetic_exceptional_masses=ex),indent=2))


if __name__=="__main__":
    main()
