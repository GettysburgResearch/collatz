# L-9313 — Centered error full shift and nearest-integer cylinder

**Claim ID:** L-9313  
**Title:** Every binary itinerary has one bounded centered-error path, while ordinary realization is exactly stabilization of a nested nearest-integer cylinder  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** elementary affine recurrence; `T-9315` for the centered-orbit crosswalk  
**Scope:** every coprime expanding binary chart; nearest-integer stabilization for `64 -> 81`  
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
\varepsilon_n-arepsilon_{n+1}.
}
\tag{4}
\]

## 2. Unique bounded error path

The sequence `(u_n)` is the unique bounded real solution of `(4)` for the fixed itinerary.

Indeed, if `(u_n)` and `(v_n)` are bounded solutions, then

\[
N(u_n-v_n)
=M(u_{n+1}-v_{n+1}),
\]

so

\[
u_{n+k}-v_{n+k}
=
\left(\frac NM\right)^k(u_n-v_n).
\]

Since `N/M>1`, boundedness forces `u_n=v_n`.

Equivalently, the backward transition

\[
\boxed{
u_n
=
\frac{M u_{n+1}+\varepsilon_n-arepsilon_{n+1}}{N}
}
\tag{5}
\]

is a contraction of ratio `M/N`.

For any tail that is not identically all zero or all one, the corresponding error is nonzero and

\[
|u_n|<1/N.
\]

Its sign recovers the digit:

\[
\boxed{
\varepsilon_n=\mathbf1_{u_n>0}.
}
\tag{6}
\]

## 3. The real error system is a full shift

Equation `(5)` shows that no binary itinerary is removed by the real centered-error condition alone.

In absolute-value coordinates

\[
r_n=|u_n|,
\]

the forward transition is

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

The inverse branches are

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

Both map the critical interval `(0,1/N)` into itself. Thus every infinite symbolic path has a nonempty real centered-error cylinder.

This rules out any proof that uses only real interval emptiness. `R-9303` records that method closure.

## 4. Nearest-integer recurrence

A centered power orbit additionally needs ordinary integers `B_n` satisfying

\[
\xi(N/M)^n=B_n+u_n.
\]

They must obey

\[
\boxed{
M B_{n+1}
=N B_n+arepsilon_n-arepsilon_{n+1}.
}
\tag{11}
\]

For a finite prefix

\[
\varepsilon_0,\ldots,arepsilon_K,
\]

iteration gives

\[
M^K B_K
=
N^K B_0
+
\sum_{i=0}^{K-1}
N^{K-1-i}M^i
(\varepsilon_i-arepsilon_{i+1}).
\tag{12}
\]

Because `N` is invertible modulo `M^K`, integrality through time `K` selects exactly one class

\[
\boxed{
B_0\equiv R_K(\varepsilon)\pmod{M^K}.
}
\tag{13}
\]

The classes are nested. Every infinite itinerary therefore selects one point

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

Solving `(11)` backward in the `M`-adic completion gives

\[
\boxed{
B_0^*(\varepsilon)
=
-
\sum_{n\ge0}
(\varepsilon_n-arepsilon_{n+1})
\frac{M^n}{N^{n+1}}.
}
\tag{15}
\]

The series converges because `M^n` tends to zero at every prime dividing `M`, while `N` is a unit there.

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

The itinerary admits a positive centered parameter exactly when its selected completion point is an ordinary positive integer:

\[
\boxed{
\exists\xi>0
\text{ with itinerary }\varepsilon
\iff
B_0^*(\varepsilon)\in\mathbb Z_{\ge1}.
}
\tag{18}
\]

### Forward implication

A centered orbit has ordinary nearest integers `B_n`; its first nearest integer lies in every cylinder `(13)`, so it equals `(14)`.

### Converse implication

If `B_0^*` is an ordinary integer, recurrence `(11)` produces ordinary integers `B_n` at every shift. Put

\[
\boxed{
\xi=B_0^*+u_0.
}
\tag{19}
\]

Induction using `(4)` and `(11)` gives

\[
\xi(N/M)^n=B_n+u_n
\]

for all `n`. If `B_0^*>=1`, then `xi>0`, and `T-9315` reconstructs the nontrivial ordinary chart orbit.

The two constant itineraries select `B_0^*=0` and the degenerate parameter `xi=0`.

## 7. Least-representative stabilization

Let

\[
0\le R_K<M^K
\]

be the least representative of `(13)`. Then

\[
\boxed{
B_0^*(\varepsilon)
\in\mathbb Z_{\ge0}
\iff
R_K\text{ is eventually constant.}
}
\tag{20}
\]

- If `R_K` stabilizes at `R`, then `R` belongs to every cylinder and equals the inverse-limit point.
- If the inverse-limit point is an ordinary nonnegative integer `R`, then once `M^K>R`, its least representative modulo `M^K` is exactly `R`.

This is the finite-versus-adic boundary also isolated in PR #20's active-cylinder theorem and in the H-frontier ghost/carry program.

## 8. Consequence for the proof program

The ordinary-section problem is not

> show that the centered real error cylinders are empty.

Every binary itinerary has one such real path.

It is

> show that no nontrivial itinerary's nested nearest-integer cylinders stabilize at an ordinary positive integer.

The required invariant must couple:

1. the full-shift real error path `(u_n)`;
2. the nested arithmetic cylinder `R_K mod M^K`;
3. sign changes of the itinerary;
4. ordinary least-representative growth.

## 9. Dependency audit

- The real companion and error recurrence are elementary geometric-series algebra.
- Finite-cylinder uniqueness uses only `gcd(M,N)=1`.
- The completion series is direct backward iteration.
- `T-9315` is used only to identify a positive ordinary cylinder lift with a centered power orbit.
- PR #20 and PR #19 are cross-program parallels, not proof dependencies.

## 10. Gap audit

- The lemma does not prove nonstabilization.
- Full symbolic support means entropy or real interval length alone cannot exclude an ordinary lift.
- Every finite cylinder contains positive ordinary representatives, but their inverse-limit point may be nonordinary.
- Excluding one structured itinerary class does not cover all binary itineraries.
- Translation to all possible Collatz counterexamples remains separate.

## 11. Correct next attack

Write

\[
R_{K+1}=R_K+q_KM^K,
\qquad
q_K\in\{0,\ldots,M-1\}.
\]

`L-9314` computes `q_K` exactly. Proving infinitely many `q_K` are nonzero for every nontrivial itinerary would close the ordinary section.