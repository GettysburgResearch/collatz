# Review of the exact-valuation strip reduction

**Verdict.** The reduction to marked odd integers with integer excess in
the interval from zero to seven is valid. Its finer section has at most
one representative per exact odd endpoint. An endpoint may have none.

Let \(d=\lfloor\log_2 n\rfloor\), \(e=v_2(3n+1)\), and write
\(\sigma=5e-(d+1)\) as an integer. The previously verified section S
is the set of marked odd n with \(\sigma\ge0\). The marking inequality is
\((d+1)(n-2^d)\le70\,2^d\).

Take \(n\in S\) with \(n>1\) and \(\sigma\ge8\). If \(e\le1\),
then \(\sigma<8\). If \(e=2\), then \(n\equiv1\pmod4\) and
\(n>1\) gives \(n\ge5\), so \(d\ge2\) and \(\sigma\le7\).
Therefore \(e\ge3\), which forces \(n\equiv5\pmod8\). Set
\(m=(n-1)/4\). This is a positive odd integer strictly smaller than n.
The equalities \(n=4m+1\) and \(3n+1=4(3m+1)\) give
\[
 d(m)=d-2,\qquad e(m)=e-2,\qquad \sigma(m)=\sigma(n)-8\ge0 .
\]
Indeed \(2^{d(m)}\le m\le2^{d(m)+1}-1\) gives the claimed digit change
including the upper-edge case. The mark passes to m since
\[
 (d-1)(m-2^{d-2})
 \le (d+1)(n-2^d)/4\le70\,2^{d-2}.
\]
The usual shortcut clocks satisfy
\(T(m)=(3m+1)/2=(3n+1)/8=T^3(n)\).
Thus convergence of m implies convergence of n. Both have precisely
the same odd endpoint after their entire respective halving runs.

Strong induction on n now proves convergence on S from convergence
on marked n with \(0\le\sigma\le7\). The separate base n=1 is
essential: it is marked, \(d=0,e=2,\sigma=9\), and is already at one.
The unconditional equivalence for S then gives the universal equivalence
for the smaller strip. The forward implication is restriction.

For uniqueness fix a positive odd endpoint u. Any representing exponent
satisfies \(2^e u\equiv1\pmod3\), so u is not divisible by 3 and all
representing exponents have the same parity. Incrementing e by two sends
\(x=(2^eu-1)/3\) to \(4x+1\), adds two to its logarithmic floor, and
adds eight to its excess. No two positive representatives can belong to
the strip, even before imposing the mark. For example, u=1 has
representatives beginning at x=1 with excess 9, and its strip is empty.
Cofinality over each fixed ternary-unit target is proved separately below.

Review basis: independent ordinary-integer reconstruction from the
new statement and the previously checked marked-section definitions.

## Frozen statement and evidence

| Reviewed file | SHA-256 |
|---|---|
| `CriticalSection.lean` | `447fef46cf13518b32f68fadb21c9ad2907718c6440f1023a0f714fc13218610` |
| `CRITICAL_SECTION.md` | `0f950d72941b5a3a967aa3028ed480ca5bcf687f17eac68c64e819c3bf759b86` |
| `check_critical_section.py` | `39494fc81ed79da245e84d5d8e8620790a9c2f4152c78dab80c5d846f6d6099c` |

The Lean declaration `CriticalMark` requires a *positive odd* cofactor
(the displayed odd natural is automatically positive) and the pair of
inequalities \(d+1\le5e\le d+8\). This correctly realizes exact
valuation and all eight signed excesses. The two formal declarations are
the quarter reduction (including mark, cofactor, clocks and exact
excess change) and the closed global equivalence. I inspected the
declarations and their proof branches, including the small inputs 1
and 3. This review relies on the separately reported Lean build.
Uniqueness, finite marked fibers, cofinality of the strip, the endpoint
bounds and the occurrence of all eight excesses receive written checks
here. They are not claimed as declarations of this Lean module.

### Cofinality preserves the specified ordinary target

For a fixed exact odd endpoint u, all positive odd inverse
representatives form a single chain \(x_{j+1}=4x_j+1\). Consequently
\(d_j=d_0+2j\). For \(j\ge1\) the relative distance of \(x_j\) above
its octave's lower edge is at least \(1/(4\cdot 2^{d_0})\), by
summing the geometric series of added ones. It cannot satisfy the mark
\(70/(d_j+1)\) for arbitrarily large j. Missing fibers are empty, so
the union of all marked fibers with \(u\le K\) is finite.

Fix a positive q with \(3\nmid q\), including even q. From the old
cofinal predecessor theorem, choose an old marked-power source
\(x>q\) outside that finite union, with \(K\ge\max(1,q)\).
The noninitial states through its next odd value form a descending
sequence of powers of two times \(U(x)\); every one is at least
\(U(x)>K\ge q\). Therefore its known hit of q comes later, so
\(U(x)\) itself hits q. Quarter-reduce x to y. Since \(U(y)=U(x)>1\),
this reduction cannot terminate at 1. It terminates in the strip,
whose member y hits the *same* q via that common odd endpoint.
\(3y+1\ge2U(y)>2K\) implies \(y>(2K-1)/3\). Letting K grow proves
the claimed cofinality without any control on the previous inverse
row's index or on the time at which it hits q. It does not give smaller
strip representatives for every q.

### Endpoint bounds and the eight attained values

For a strip member, \(2^e\le2^{8/5}n^{1/5}\) follows from
\(5e\le d+8\) and \(2^d\le n\). Also \(2^e>n^{1/5}\) follows
from \(5e\ge d+1\) and \(n<2^{d+1}\). Applying both to
\(U(n)=(3n+1)/2^e\) gives the written two-sided bounds.

For prescribed surplus s from 0 to 7, the congruence
\(3r+1\equiv2^e\pmod{2^{e+1}}\) has one odd representative
\(0<r<2^{e+1}\). For all sufficiently large e, take
\(d=5e-1-s\ge e+1\). Then \(2^d+r\) lies in octave d and retains
exact valuation e. Its mark holds since
\((d+1)2^{e+1}/2^d\to0\). This proves infinitely many occurrences
of every listed excess without claiming any distribution among them.

I ran the finite checker with Python's optimized mode. It reported
17,809 marked-power sources through 250,000, including the base case 1,
6,090 reducible sources, and 11,718 strip members with distinct endpoints.
