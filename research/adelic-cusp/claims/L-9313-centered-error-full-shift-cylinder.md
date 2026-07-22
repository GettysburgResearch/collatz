# L-9313 — Centered error full shift and nearest-integer cylinder

**Claim ID:** L-9313  
**Title:** Every binary itinerary has one bounded centered-error path, while ordinary realization is exactly stabilization of a nested nearest-integer cylinder  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** elementary affine recurrence; `T-9315` for the centered-orbit crosswalk  
**Scope:** every coprime binary expanding chart; nearest-integer stabilization for `64 -> 81`  
**Related counterexample candidates:** none

## 1. Setup

Fix coprime integers

\[
2\le M<N
\]

and a binary itinerary

\[
\varepsilon=(\varepsilon_n)_{n\ge0}
\in\{0,1\}^{\mathbb N}.
\]

Define the bounded real companion

\[
\boxed{
x_n
=
\frac{N-M}{N}
\sum_{k\ge0}
\varepsilon_{n+k}
\left(\frac MN\right)^k
\in[0,1].
}
\tag{1}
\]

Put

\[
\boxed{
u_n
=
\frac{\varepsilon_n-x_n}{M}
=
\frac{\varepsilon_n-x_{n+1}}{N}.
}
\tag{2}
\]

Then

\[
|u_n|\le\frac1N
\tag{3}
\]

and

\[
\boxed{
N u_n-Mu_{n+1}
=
\varepsilon_n-\varepsilon_{n+1}.
}
\tag{4}
\]

## 2. Unique bounded error path

The sequence `(u_n)` is the unique bounded real sequence satisfying `(4)` for the fixed itinerary.

Indeed, if `(u_n)` and `(v_n)` are bounded solutions, their difference obeys

\[
N(u_n-v_n)
=M(u_{n+1}-v_{n+1}).
\]

Hence

\[
u_{n+k}-v_{n+k}
=
\left(\frac NM\right)^k(u_n-v_n).
\]

Because `N/M>1`, boundedness forces `u_n=v_n`.

Equivalently, the backward transition

\[
\boxed{
u_n
=
\frac{M u_{n+1}+\varepsilon_n-\varepsilon_{n+1}}{N}
}
\tag{5}
\]

is a contraction of ratio `M/N`. Every infinite binary itinerary therefore carries exactly one bounded centered-error path.

For every itinerary that is not eventually all zero or eventually all one at a tail, the corresponding errors are nonzero and satisfy

\[
|u_n|<1/N.
\]

The sign recovers the digit:

\[
\varepsilon_n=\mathbf1_{u_n>0}.
\tag{6}
\]

## 3. The real graph is a full shift

Equation `(5)` shows that no symbolic itinerary is removed by the real centered-error condition alone.

In absolute-value coordinates `r_n=|u_n|`, the two transition types are

\[
\boxed{
r_{n+1}=\frac NM r_n}
\tag{7}
\]

when the sign is unchanged, and

\[
\boxed{
r_{n+1}=\frac{1-Nr_n}{M}}
\tag{8}
\]

when the sign flips.

Their inverse branches are contractions

\[
\boxed{
r_n=\frac MN r_{n+1}}
\tag{9}
\]

and

\[
\boxed{
r_n=\frac{1-Mr_{n+1}}{N}.}
\tag{10}
\]

Each inverse branch maps the critical interval `(0,1/N)` into itself. Thus the error coordinate realizes the full two-shift. A proof based only on showing that real scheduled cylinders become empty cannot succeed.

## 4. Nearest-integer recurrence

To lift the error path to a centered power orbit, one needs ordinary integers `B_n` satisfying

\[
\xi(N/M)^n=B_n+u_n.
\]

The required integer recurrence is

\[
\boxed{
M B_{n+1}
=N B_n+\varepsilon_n-\varepsilon_{n+1}.
}
\tag{11}
\]

For a finite itinerary prefix

\[
\varepsilon_0,\ldots,\varepsilon_K,
\]

iteration gives

\[
M^K B_K
=
N^K B_0
+
\sum_{i=0}^{K-1}
N^{K-1-i}M^i
(\varepsilon_i-\varepsilon_{i+1}).
\tag{12}
\]

Because `N` is invertible modulo `M^K`, integrality through time `K` selects exactly one residue class

\[
\boxed{
B_0\equiv R_K(\varepsilon)\pmod{M^K}.
}
\tag{13}
\]

The classes are nested as `K` grows. Therefore every infinite itinerary selects one point

\[
\boxed{
B_0^*(\varepsilon)
\in
\varprojlim_K\mathbb Z/M^K\mathbb Z.
}
\tag{14}
\]

When `M` is a power of `2`, this inverse limit is `Z_2`.

## 5. Exact completion series

In the `M`-adic completion, equation `(11)` can be solved backward:

\[
\boxed{
B_0^*(\varepsilon)
=
-
\sum_{n\ge0}
(\varepsilon_n-\varepsilon_{n+1})
\frac{M^n}{N^{n+1}}.
}
\tag{15}
\]

The series converges because the numerator contains `M^n` and every denominator is a unit at the primes dividing `M`.

For `M=64,N=81`, telescoping gives

\[
\boxed{
B_0^*(\varepsilon)
=
-rac{\varepsilon_0}{81}
+
\frac{17}{81^2}
\sum_{n\ge0}
\varepsilon_{n+1}
\left(\frac{64}{81}\right)^n
\quad\text{in }\mathbb Z_2.
}
\tag{16}
\]

Equivalently,

\[
\boxed{
B_0^*(\varepsilon)
=
\frac{\Phi(\varepsilon)-\varepsilon_0}{64}.
}
\tag{17}
\]

## 6. Ordinary realization criterion

The itinerary admits a positive centered parameter if and only if the selected completion point is an ordinary positive integer:

\[
\boxed{
\exists\xi>0
\text{ with centered itinerary }\varepsilon
\iff
B_0^*(\varepsilon)\in\mathbb Z_{\ge1}.
}
\tag{18}
\]

### Forward implication

A centered orbit has ordinary nearest integers `B_n`; its first nearest integer belongs to every cylinder `(13)`, so it equals the completion point `(14)`.

### Converse implication

If `B_0^*` is an ordinary integer, recurrence `(11)` produces ordinary integers `B_n` at every shift. Put

\[
\boxed{
\xi=B_0^*+u_0.
}
\tag{19}
\]

Then induction using `(4)` and `(11)` gives

\[
\xi(N/M)^n=B_n+u_n
\]

for every `n`. If `B_0^*>=1`, then `xi>0`, and `T-9315` reconstructs the nontrivial ordinary chart orbit.

The two trivial itineraries have `B_0^*=0` and centered parameter `xi=0`.

## 7. Least-representative stabilization

Let

\[
0\le R_K<M^K
\]

be the least representative of the finite cylinder `(13)`. Then

\[
\boxed{
B_0^*(\varepsilon)
\in\mathbb Z_{\ge0}
\iff
R_K\text{ is eventually constant.}
}
\tag{20}
\]

This is the same finite-versus-adic boundary isolated in PR #20's active-cylinder theorem and in the H-frontier ghost/carry program.

Thus the centered-power equivalence does not remove the stabilization wall. It gives the stabilization wall a canonical real error coordinate.

## 8. Consequence for the proof program

The ordinary-section problem is not:

> show that the centered real error cylinders are empty.

They are never empty for a prescribed binary itinerary.

It is:

> show that no nontrivial itinerary's nested nearest-integer cylinders stabilize at an ordinary positive integer.

The strongest next invariant must couple:

1. the full-shift real error path `(u_n)`;
2. the nested `2`-adic integer cylinder `(R_K mod M^K)`;
3. the sign/digit transition;
4. ordinary least-representative growth.

## 9. Dependency audit

- The real companion formula and bounded-error recurrence are elementary geometric-series algebra.
- Finite cylinder uniqueness uses only `gcd(M,N)=1`.
- The completion series is direct backward iteration.
- `T-9315` is used only to identify a positive ordinary cylinder lift with the centered power orbit.
- PR #20 and PR #19 are cross-program parallels, not proof dependencies.

## 10. Gap audit

- The lemma does not prove nonstabilization.
- Full symbolic support of the real error system means entropy or interval length alone cannot exclude an ordinary lift.
- An itinerary may select a nonordinary `2`-adic integer even though every finite cylinder has positive ordinary representatives.
- A proof that a particular structured itinerary is nonordinary does not cover all binary itineraries.
- The chart translation to all possible Collatz counterexamples remains separate.

## 11. Suggested next attack

Analyze the new base-`M` block digits

\[
q_K
=
\frac{R_{K+1}-R_K}{M^K}
\in\{0,\ldots,M-1\}.
\]

Use the centered errors to derive an exact recurrence or sign restriction for `q_K`. Proving infinitely many `q_K` are nonzero for every nontrivial itinerary would close the ordinary section.