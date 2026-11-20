# Independent review of the arbitrary-tail c=3 descent

**Verdict: PASS for the stated guarded reduction, witness reconstruction,
and nonvacuity theorem. The resource exchange is a correct conditional
transformation, with the stated missing global induction. This is not a
review verdict that Collatz is proved.**

The reviewed artifacts have SHA-256 hashes:

| Artifact | SHA-256 |
|---|---|
| `C3_ARBITRARY_TAIL_DESCENT.md` | `ee2cd5973d50b88af5056be3af654d1e287ff8f0a831eaa335fef04f64552c11` |
| `check_c3_arbitrary_tail.py` | `d11595cace6337f12304445a1920351c198a1dbed40bf76131e1bfb7245919e2` |

This review includes the final addition proving nonvacuity at every
positive tail rank. It uses the pinned PR163 height theorem and PR164
canonical P/Q definitions cited by the author. It does not reprove the
separate 71-path H1--H2 atlas.

The independent implementation is `check_c3_tail_independent_review.py`.
It imports no functions from the author's checker. It reconstructs
witnesses backwards, selects nonvacuity parameters by incremental ternary
lifting, explicitly checks all 26 P/Q steps in each reviewed chain, and
uses a different integer induction to prove the all-tail height bound.

## 1. Source and target witness splices

Let \(z=2^a q-1\), where \(a\ge1\) and \(q\) is odd, and let
\(3^a q-1=2^e w\), where \(w\) is odd. Before the last source jump,
the actual odd values are

\[
3^i2^{a-i}q-1,\qquad 0\le i<a.
\]

For \(i<a-1\), the next accelerated exponent is exactly one. At the
last input, \(3n+1=2^{e+1}w\), so its exact exponent is \(e+1\).
This proves the source prefix \((1^{a-1},e+1)\), with no assumption
about the remaining certificate. The c=3 kernel excludes \(z=1\), so
the first arrival at 1 cannot truncate this prefix prematurely.

On the target arm, the first \(a\) values after \(2z+1\) have odd
successors and end at \(2^{e+1}w+1\). The author's accelerated prefix
\((2,2,2,1),1^a\) is therefore exact.

For odd \(e=2b+1\), the next \(b\) exponent-two steps reach
\(4R+1\), with \(R=3^b w\). If the next exponent at \(R\) is
\(d_1\), then

\[
3(4R+1)+1=4(3R+1)
\]

proves that the next exponent at \(4R+1\) is exactly \(d_1+2\),
and both jumps have the same next odd state. This validates the splice
\((d_1+2,d_2,\ldots)\). The empty certificate at \(R=1\) is correctly
replaced by \((2)\), giving the actual \(5\to1\) jump of exponent
four. In particular the direct case \(e=1\) is valid.

For even \(e=2b\), the next \(b\) exponent-two steps end at
\(R=2\cdot3^b w+1\) itself. Concatenation of the supplied certificate
for \(R\) is therefore literal. No multiplication-invariance assumption
is present in either parity case.

The independent checker reconstructed the exact original starts \(X,Y\)
from the complete spliced words on 40 positive c=3 instances, covering
both parities and the direct \(e=1\) case.

## 2. Independent proof of the universal all-tail height inequality

The author's squared-ratio proof is correct: its use of
\(3^5<4^4\) gives \((3/4)^{80}<2^{-32}\), and the final integer
comparison is exactly \(528318^2\cdot243<2^{46}\).

For an independent check, one can prove the same result directly with
integer differences, including every additive term. Write \(H=176106\)
and define

\[
D(a,e,w)=81\,3^a(X-HR).
\]

From the exact formulas in the note,

\[
D(a,e,w)=(A-B)w+C,
\]

where \(A=2^{a+e+9}\), and

\[
(B,C)=
\begin{cases}
\left(81H3^{a+(e-1)/2},\ 2^{a+9}-687\,3^a\right),&e\text{ odd},\\
\left(162H3^{a+e/2},\ 2^{a+9}-(687+81H)3^a\right),&e\text{ even}.
\end{cases}
\]

In each case \(C<0\) for all \(a\ge1\). It is enough to prove
\(D(a,e,1)>0\): then \(A-B>0\), and increasing \(w\ge1\) only
increases the difference.

There are four integer induction bases:

| \(a\) | \(e\) | \(D(a,e,1)\) |
|---:|---:|---:|
| 1 | 83 | 8342703733783518841193320281 |
| 1 | 84 | 10442141145568944250345157945 |
| 2 | 86 | 74172229681554413854977201667 |
| 2 | 87 | 274770602383570219708184640411 |

Let \(c_0=687\) in the odd case and \(c_0=687+81H\) in the even
case, so that \(C=2^{a+9}-c_0 3^a\). The exact recurrences are

\[
D(a,e+2,1)=3D(a,e,1)+A-2C>0
\]

whenever \(D(a,e,1)>0\), and

\[
\begin{split}
D(a+2,e+6,1)
={}&243D(a,e,1)+13A\\
&-239\,2^{a+9}+234c_0 3^a>0.
\end{split}
\]

The last positivity follows already from \(e\ge5\), since
\(13\cdot2^5>239\), and the remaining term is positive. Every
\((a,e)\) with \(a\ge1\) and \(e\ge3a+80\) is reached from one of
the four bases by these two increments. This proves

\[
HR<X
\]

for every positive tail \(w\) in the claimed domain. It is an
independent all-parameter proof, not a finite scan over possible tails.
The checker also evaluates the exact recurrence identities on 112 bounded
instances as implementation checks.

## 3. One global minimum, with no change of rank minimum

The application to a least failure uses the same \(X_*\) in the source
kernel, the inequality \(HR<X_*\), and the PR163 initial interval. H2
then certifies \(R\), and the explicit target splice certifies \(Y\),
contradicting that one global least failure.

The conclusion is therefore correctly scoped:

\[
\text{a global least c=3 failure has }e\le3a+79,
\quad\text{and }e\ne1.
\]

It is not an unconditional convergence theorem for every larger source in
the displayed language. The separate compiler statement properly assumes
all eligible reverse calls whose upper sources are below the given fixed
\(X\). It does not bound ordinary intermediate heights by \(X\), and
does not need such a bound.

## 4. Nonvacuity at every positive tail rank

The new nonvacuity argument is valid, including its rank-one extension.
For

\[
w_{r,h}=1+\frac{4^{r+1}(4^{3^r h}-1)}{3^{r+1}},
\qquad r\ge0,\ h\ge1,
\]

the exact first-hit word is \((2^r,2+2\cdot3^r h)\), where \(2^r\)
means repeated letters equal to two. Every preterminal value exceeds 1.
For \(r=0\), this is simply
\(w=(4^{h+1}-1)/3\) with one odd jump to 1.

For distinct nonnegative \(h,h'\), factor the difference of the two
powers of four. The elementary identity
\(\nu_3(4^n-1)=1+\nu_3(n)\) gives exactly

\[
\nu_3(w_{r,h}-w_{r,h'})=\nu_3(h-h').
\]

This proves both well-definedness and bijectivity of the induced map on
residues modulo \(3^L\). The chosen congruence for \(w\) is a ternary
unit and forces the desired \(z\equiv41\pmod{81}\). The quotient
\(q=(2^e w+1)/3^a\) is odd, so both valuations \(a,e\) are exact.
There are infinitely many positive representatives in the selected
\(h\)-class, giving distinct actual sources with the prescribed tail
rank. The use of \(h=0\) for residue bookkeeping does not assert a
positive-rank first-hit certificate at 1.

The independent checker selected parameters by lifting one ternary digit
at a time and reconstructed the tail values from their inverse witnesses.
It checked 20 actual sources with exact tail ranks one through five,
covering both exponent parities. The infinite conclusion follows from the
valuation identity and the explicit formulas, not this finite count.

## 5. Resource exchange and the exact 26-level guard

For \(a\ge4\), the congruence \(2^e w\equiv-1\pmod{81}\) makes

\[
m=(2^{e+27}w-1)/81
\]

a positive odd integer. The new source \(X'=256m+1\) has the explicit
prefix

\[
(2,2,2,e+29)
\]

followed by the original tail witness. Thus its source rank decreases by
\(a\), and its total exponent changes by \(26-a\), exactly as claimed.
The source \(X'\) is larger than \(X\); no least-value descent is
available from this operation.

At canonical level \(2j\), the value is \(A_j=3^j w\); at level
\(2j-1\), it is \(B_j=2\cdot3^j w+1\). With
\(m_j=3^{j-3}w\), the downward calls are literally

\[
A_j=27m_j\xrightarrow{P(m_j)}54m_j+1=B_j,
\]

\[
B_j=54m_j+1\xrightarrow{Q(m_j)}9m_j=A_{j-1}.
\]

The returned canonical value is at level \(e+25\), and the requested
one is at level \(e-1\). The 26 source levels are therefore
\(e+25,e+24,\ldots,e\). They all satisfy the mechanism's domain
exactly when \(e\ge5\). At \(e=5\), the last call is \(Q(w)\),
ending at \(9w\); at \(e=6\), the last call is \(P(w)\), ending at
\(54w+1\). The low exponents two, three, and four do not satisfy this
guard. In the actual source language \(w\) is a ternary unit, so the
missing powers of three cannot be supplied by dividing \(w\).

The checker verifies 24 complete chains, totaling 624 individual P/Q
calls, and explicitly rejects the same chain at exponents one through
four. It also reconstructs four actual exchanged source witnesses.

The author correctly leaves the final inference open: a smaller known
source exponent for the first call gives no bound on the witness returned
for its target. Consequently the subsequent 26 calls have not been proved
smaller in that source-exponent measure. Their numerical upper sources
have not been proved below the original \(X\) either. The resource
exchange is not marked as a completed global induction.

## Replay and scope

If the reviewed source files are placed beside the independent checker:

```bash
python -B check_c3_tail_independent_review.py
python -OO -B check_c3_tail_independent_review.py
```

Otherwise pass their directory with `--source-dir`. Both runs passed on
the pinned files. Reports are `c3_tail_independent_review_report.json` and
`c3_tail_independent_review_optimized_report.json`.

No correctness defect was found in the reviewed claims. The unresolved
part remains the global coverage and well-foundedness of recursive calls
outside the proved height guard.
