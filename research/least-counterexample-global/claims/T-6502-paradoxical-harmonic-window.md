# T-6502 — Distinct-orbit paradoxical harmonic window

**Claim ID:** `T-6502`  
**Title:** Every acyclic no-descent coefficient crossing obeys a logarithmic harmonic window  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #78  
**Dependencies:** `D-6501`, `L-6501`; elementary logarithmic inequalities  
**Scope:** acyclic positive ordinary orbit segments, including a divergent least-counterexample first crossing and one rotation of a positive cycle

## 1. Statement

Let

\[
x_i=T^i(n)
\qquad(0\le i\le j)
\]

be a positive ordinary shortcut-Collatz segment satisfying:

1. `x_i>=n` for every `0<=i<=j`;
2. the source values `x_0,...,x_(j-1)` are distinct;
3. if `q` of the first `j` sources are odd, then
   \[
   C={3^q\over2^j}<1;
   \]
4. the endpoint does not descend:
   \[
   x_j\ge n.
   \]

Put

\[
\lambda=j\log2-q\log3=-\log C>0.
\]

Then

\[
\boxed{
\lambda
\le
\min\left\{
{q\over3n},
{1\over3n}+{1\over6}
\log\left(1+{2(q-1)\over n}\right),
{7\over9}+{1\over9}\log q
\right\}.}
\tag{1}
\]

Consequently, with

\[
\alpha={\log2\over\log3},
\]

one has the exact one-sided rational-approximation window

\[
\boxed{
0<\alpha-{q\over j}
\le
{1\over j\log3}
\min\left\{
{q\over3n},
{1\over3n}+{1\over6}
\log\left(1+{2(q-1)\over n}\right),
{7\over9}+{1\over9}\log q
\right\}.}
\tag{2}
\]

The second and third bounds become substantially smaller than the usual `q/(3n)` estimate when the crossing length is much larger than the initial value.

## 2. Product identity and no descent

By `L-6501`,

\[
{x_j\over n}
=C
\prod_{\substack{0\le i<j\\x_i\text{ odd}}}
\left(1+{1\over3x_i}\right)
=:CP.
\tag{3}
\]

Because `x_j>=n`,

\[
1\le CP.
\]

Since `C=e^{-lambda}`,

\[
\boxed{\lambda\le\log P.}
\tag{4}
\]

## 3. Three harmonic estimates

### 3.1 Uniform no-descent estimate

Every odd source is at least `n`, so

\[
\log P
\le{1\over3}\sum_{x_i\text{ odd}}{1\over x_i}
\le{q\over3n}.
\tag{5}
\]

This is the coefficient window used in the first Farey-gate argument of PR #76.

### 3.2 Distinct odd-integer estimate above the same floor

Arrange the `q` distinct odd sources increasingly:

\[
y_1<\cdots<y_q.
\]

They are odd integers at least `n`, hence

\[
y_r\ge n+2(r-1).
\]

Therefore

\[
\begin{aligned}
\sum_{r=1}^q{1\over y_r}
&\le {1\over n}
 +\int_0^{q-1}{dt\over n+2t}\\
&={1\over n}
 +{1\over2}\log\left(1+{2(q-1)\over n}\right).
\end{aligned}
\tag{6}
\]

Dividing by three proves the second entry of `(1)`.

### 3.3 Prime-to-six estimate

For a segment beginning with an odd source, every later orbit value is nonzero modulo three. Apart from the possible initial exception, the odd sources are distinct integers coprime to six. The proof of `L-6501` gives

\[
\sum_{x_i\text{ odd}}{1\over x_i}
\le{7\over3}+{1\over3}\log q,
\]

and hence

\[
\log P\le{7\over9}+{1\over9}\log q.
\tag{7}
\]

Taking the minimum of `(5)--(7)` in `(4)` proves `(1)`, and division by `j log 3` proves `(2)`.

## 4. Applicability to a false Collatz conjecture

If a least counterexample has a divergent orbit, the orbit values are distinct. Its first finite coefficient crossing therefore satisfies `(1)--(2)`.

If a nontrivial positive cycle exists, rotate it to its least value and use one period. The period sources are distinct, the endpoint equals the start, and the positive affine toll forces the period coefficient below one. Thus the rotated period also satisfies `(1)--(2)`.

Accordingly, every finite-crossing or cycle lane in the least-counterexample framework must obey this cofinal harmonic window.

## 5. Relation to current literature

Rozier--Terracol express paradoxicality through the same product of odd-source correction factors and obtain harmonic-mean restrictions. Equation `(1)` is the ordinary distinct-source specialization needed by the repository's least-counterexample lane: the same no-descent floor and the same individual orbit values are used, rather than an average symbolic schedule.

## 6. Gap audit

- The window does not by itself exclude all rational approximants to `log_3 2`.
- For very large `j`, the right side still permits sufficiently good continued-fraction approximants.
- Distinctness is required. For an eventually periodic orbit, apply the theorem to one period rotated at its minimum, not to repeated copies of the period.
- No finite numerical verification is promoted to a cofinal conclusion.
- Closing Lane B still requires a lower bound on the canonical least representative of each crossing cylinder, or a whole-denominator cycle contradiction.
