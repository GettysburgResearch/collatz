# Exact ordinary reductions at signed-five targets

**PROPOSED, unconditional.** The four claims below are written proofs, not a
proof of the Collatz conjecture.
This note works with the target set in PR 146 at the exact source head
`561d48a4d3a793a59b1cdf0406062ae1a6d47515`. It derives a finite ordinary reduction
and an explicit separation theorem. Neither conclusion excludes an infinite
sequence of sufficiently separated visits with unbounded signed complexity.

Use

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd},\end{cases}
\qquad
S(x)=\begin{cases}x/2&x\text{ even},\\(3x-1)/2&x\text{ odd}.\end{cases}
\]

All starting values in this note are positive ordinary integers. Let
\(\mathcal C_{2k}\), for \(k\ge1\), consist of the integers

\[
c=5\,2^b-M>0
\]

for which the **first** visit of the signed-magnitude orbit from \(M\) to 5
occurs after \(b+3k\) steps and has exactly \(2k\) odd inputs. Here \(b\ge0\).
The set \(\mathcal C\) is the union of these sets. Membership need not have a
unique representation. Every statement below holds for each qualifying
representation separately.

The original signed-target identity and its phase interpretation are in
[EXCESS_DENSITY.md](https://github.com/GettysburgResearch/collatz/blob/561d48a4d3a793a59b1cdf0406062ae1a6d47515/research/upper-bit-mergers/EXCESS_DENSITY.md).
The signed multiplicative estimate is in
[NEGATIVE_FIVE_CHECKPOINT.md](https://github.com/GettysburgResearch/collatz/blob/561d48a4d3a793a59b1cdf0406062ae1a6d47515/research/upper-bit-mergers/NEGATIVE_FIVE_CHECKPOINT.md).

## STA1. Dyadic normalization preserves the signed complexity

For every \(k\ge1\),

\[
c\in\mathcal C_{2k}\quad\Longleftrightarrow\quad
2c\in\mathcal C_{2k}.
\tag{1}
\]

For the forward implication, prepend the even step \(2M\mapsto M\). This
increases the first-hit length and \(b\) by one, preserves the odd count, and
replaces \(c\) by \(2c\). Conversely, apply the following argument to any even
target. Since every signed magnitude reaching 5 is at least 5, positivity of
\(5\,2^b-M\) implies \(b\ge1\). If \(c\) is even then \(M\) is even, so remove
its first even step. The resulting data are \(M/2,b-1,2k\), with target \(c/2\).
The first-hit property is preserved in both directions.

In particular, on an escaping orbit, infinitely many distinct visits to
\(\mathcal C\) imply infinitely many distinct **odd** visits to \(\mathcal C\).
Each stretch of consecutive even inputs is finite; all its targets normalize
to its last, odd state. A nonrepeating orbit cannot use the same odd state for
two different such stretches.

This normalization is necessary when measuring visit separation by odd-step
counts: consecutive even targets can have identical odd-step count.

## STA2. A finite ordinary target set for every fixed signed odd count

For \(k\ge1\), let

\[
\mathcal F_k=\left\{
5\,3^{2k-q}-u>0:\ S^{3k}(u)=5,
\ q=\#\{\text{odd inputs in these }3k\text{ steps}\}
\right\}.
\tag{2}
\]

The exponent in this definition is nonnegative. Indeed, the signed estimate

\[
2^{3k}\ge (u/5)\,8^{q/2},\qquad u\ge5
\]

gives \(q\le2k\). Each inverse step has at most two positive integer
preimages, so \(\mathcal F_k\) is finite and can be listed exactly.

**Finite reduction theorem.** For every \(k\ge1\), every \(b\ge0\), and every
representation \(c=5\,2^b-M\in\mathcal C_{2k}\),

\[
T^b(c)\in\mathcal F_k
\quad\text{and}\quad
1\le T^b(c)\le5(9^k-8^k).
\tag{3}
\]

To prove this, let \(r\) count the odd inputs in the first \(b\) signed steps,
put \(u=S^b(M)\), and put \(q=2k-r\). The starts \(c\) and \(-M\) differ by
\(5\,2^b\). Therefore they have the same first \(b\) parity bits. The exact
affine difference at the end is \(5\,3^r\), giving

\[
T^b(c)=5\,3^r-u=5\,3^{2k-q}-u>0.
\tag{4}
\]

The remaining signed path from \(u\) reaches 5 in \(3k\) steps with \(q\) odd
inputs, proving membership. To prove the numerical bound, write that signed
word as

\[
3^q u-B=5\,2^{3k},\qquad B\ge0.
\]

Multiplying (4) by \(3^q\) gives

\[
3^q T^b(c)=5\,9^k-5\,8^k-B\le5(9^k-8^k).
\]

This also proves

\[
\max\mathcal F_k=5(9^k-8^k),
\tag{5}
\]

because the all-even signed preimage \(u=5\,8^k,q=0\) attains the bound.
Appending one lap \(5\to7\to10\to5\) increases the signed length by three and
the odd count by two; hence

\[
\mathcal F_k\subseteq\mathcal F_{k+1}.
\tag{6}
\]

An immediate all-parameter descent family follows: **every**
\(c\in\mathcal C_{2k}\) with \(c>5(9^k-8^k)\) strictly descends by clock \(b\)
of each qualifying representation. The claim applies even when \(b\) and
\(c\) vary without bound. It does not assert that every intermediate iterate
is smaller, or that this descent already reaches 1.

## STA3. Two infinite families that provably reach 1

The complete three-step signed preimages are

| \(u\) | Signed path | \(q\) | \(5\,3^{2-q}-u\) |
|---:|---|---:|---:|
| 40 | \(40\to20\to10\to5\) | 0 | 5 |
| 14 | \(14\to7\to10\to5\) | 1 | 1 |
| 5 | \(5\to7\to10\to5\) | 2 | 0 |

Consequently

\[
\mathcal F_1=\{1,5\}.
\tag{7}
\]

Every member of \(\mathcal C_2\), for every allowed \(b\), reaches 1 within
\(b+4\) shortcut steps. If the member exceeds 5, (3) is an explicit strict
descent. For example, \(M=143,b=5\) has two signed odd inputs before its first
hit of 5 and gives \(c=17\), with \(T^5(17)=5\).

At the next level, exact inverse enumeration gives

\[
\mathcal F_2=\{1,2,5,7,23,27,28,85\}.
\tag{8}
\]

The shortcut hitting times of 1 for these eight targets, in the same order,
are \(0,1,4,11,11,70,13,8\). Thus every member of \(\mathcal C_4\) reaches 1
within \(b+70\) steps. This is a finite arithmetic check supporting an
infinite family in \(b\); it is not a numerical extrapolation in \(k\).
The attached checker independently enumerates the inverse tree and replays
these eight positive orbits with integer arithmetic.

Proving convergence of every \(\mathcal F_k\) would prove convergence of every
\(\mathcal C\)-target. No induction in \(k\) is established here. In
particular, nesting in (6) is not a descent relation on newly appearing
targets.

## STA4. Uniform separation of odd signed-target visits on an escaping orbit

Here an **escaping** positive orbit is one that is not eventually periodic.
Its states are distinct and tend to infinity. Let \(J_1<J_2\) be two clocks
at which the states \(c_1,c_2\) are odd members of \(\mathcal C\). Let

\[
d=s_{J_2}(\beta)-s_{J_1}(\beta)\ge1,
\]

and suppose every state from clock \(J_1\) onward is at least \(F\ge1\).
There is no restriction on the two signed complexities or their lengths.

**Explicit spacing theorem.** Under these hypotheses,

\[
\boxed{\quad F\le2^{448}\,3^{64d}.\quad}
\tag{9}
\]

All constants are absolute; no seed-dependent limiting phase is used.

### Signed error

Put \(\theta=13/(9\sqrt2)>1\). The first-hit signed bound gives, for any
representation of \(c_i\) with \(h_i\ge2\) even signed odd inputs,

\[
u_i:=\frac{M_i}{5\,2^{b_i}}\le\theta^{1-h_i}.
\]

The exact shared-parity identity gives

\[
F\le T^{b_i}(c_i)<5\,3^{h_i}.
\]

The exact integer inequality \(169^{32}>3\,162^{32}\) proves
\(\theta^{64}>3\). Also \(\theta\,5^{1/64}<2\). Consequently, for
\(F\ge2^{128}\),

\[
0<u_i<2F^{-1/64}\le\tfrac12,
\qquad
-4F^{-1/64}<\log(1-u_i)<0.
\tag{10}
\]

The two signed logarithmic errors therefore differ in absolute value by at
most \(4F^{-1/64}\), rather than by an error involving an unknown limit.

### Ordinary error

Write

\[
D_J=\frac{T^J(\beta)}{3^{s_J(\beta)}2^{-J}}.
\]

It is multiplied by \(1+1/(3x)\) at an odd input \(x\), and stays unchanged
at an even input. The explicit orbit-packing lemma

\[
\sum_{\substack{x\text{ odd state}\\\text{of the forward tail}}}\frac1x
\le160F^{-1/40}
\tag{11}
\]

is proved in [ORBIT_MELLIN.md](https://github.com/GettysburgResearch/collatz/blob/561d48a4d3a793a59b1cdf0406062ae1a6d47515/research/astra-three-routes/pass2/ORBIT_MELLIN.md),
Section 3. Its hypothesis holds here: every iterate of the odd map is
injective on the odd states of a nonrepeating orbit. It follows that

\[
0\le\log(D_{J_2}/D_{J_1})\le\frac{160}{3}F^{-1/40}.
\tag{12}
\]

### Cancellation and integer separation

The exact identity at each visit is

\[
\log(c_i/2^{b_i})=
\log D_{J_i}+s_{J_i}(\beta)\log3-(J_i+b_i)\log2.
\]

Subtract it at the two visits and put
\(B=J_2+b_2-J_1-b_1\in\mathbb Z\). By (10)--(12),

\[
|d\log3-B\log2|\le64F^{-1/64}.
\tag{13}
\]

For \(F\ge2^{448}\) the right side is at most \(1/2\). Thus \(B>0\), and
\(2^B<2\,3^d\). Unique factorization makes the two integers \(3^d\) and
\(2^B\) distinct. The integral of \(1/x\) between them gives

\[
|d\log3-B\log2|
\ge\frac1{\max(3^d,2^B)}
>\frac1{2\,3^d}.
\]

Combining this with (13) yields (9). For \(1\le F<2^{448}\), (9) is
immediate. This completes the proof.

The conclusion is equivalently a lower bound

\[
d\ge\frac{\log F-448\log2}{64\log3}.
\]

It quantitatively strengthens the divergence of successive same-orbit visit
gaps, but does not bound the number of visits. A fixed two-logarithm lower
bound of the kind explicitly imported in PR 146's EXCESS_RATE note would
replace this logarithmic spacing by a positive power of \(F\). That further
statement would carry the same external dependency; it is not needed here.

## 5. The remaining arithmetic obstruction

Equations (3) and (9) leave a precise possibility: the signed odd counts can
increase without bound, the finite target sets can introduce new positive
states, and the odd-clock separations can increase fast enough to satisfy
(9). Neither integer denominator separation nor the explicit reciprocal
budget forbids this combination.

In particular, (13) compares two exact visits. It does **not** replace the
limit of the ordinary correction product by an algebraic number, and it
does not interchange a fixed binary horizon with the moving representation
length \(b_i\). A finite computation at bounded \(k\) cannot decide all the
sets in (2). Those are the missing uniform steps, not consequences of the
lemmas proved here.

## Verification

Run `python -B check_signed_target_reduction.py` in this directory. By default
the report goes only to standard output; add `--output PATH` to save it. The
checker uses exact integer arithmetic, verifies the small complete inverse
sets and their terminal positive trajectories, replays many signed first-hit
representations, and checks the exact power inequalities used in the
constants. Its finite replay does not certify the infinite spacing theorem;
the all-parameter proof is the argument above.
