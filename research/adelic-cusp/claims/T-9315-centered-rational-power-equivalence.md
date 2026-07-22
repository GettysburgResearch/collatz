# T-9315 — Centered rational-power equivalence

**Claim ID:** T-9315  
**Title:** Nontrivial ordinary binary-chart orbits are exactly critical centered rational-power orbits  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** elementary nearest-integer arithmetic; `D-9302` for the `64 -> 81` notation crosswalk  
**Scope:** every coprime expanding binary chart and the ordinary section of the `64 -> 81` subsystem  
**Related counterexample candidates:** none

## 1. General chart

Fix coprime integers

\[
2\le M<N
\]

and put

\[
\beta=\frac NM.
\]

A **nontrivial ordinary binary-chart orbit** is a pair of sequences

\[
A_n\in\mathbb Z_{\ge2},
\qquad
\varepsilon_n\in\{0,1\},
\qquad n\ge0,
\]

satisfying

\[
\boxed{
M A_{n+1}
=
N A_n-(N-M)\varepsilon_n
}
\tag{1}
\]

for every `n`. Reducing `(1)` modulo `M` and using `gcd(M,N)=1` gives

\[
\boxed{A_n\equiv\varepsilon_n\pmod M.}
\tag{2}
\]

Define the critical centered power set

\[
\boxed{
\mathcal Z^{\rm ctr}_{M,N}
=
\left\{
\xi>0:
\left\|\xi\beta^n\right\|
\le\frac1N
\text{ for every }n\ge0
\right\},
}
\tag{3}
\]

where `||y||` is distance to the nearest integer.

## 2. The equivalence

There is a bijection

\[
\boxed{
\{
\text{nontrivial ordinary binary-chart orbits}
\}
\longleftrightarrow
\mathcal Z^{\rm ctr}_{M,N}.
}
\tag{4}
\]

More explicitly:

### From an ordinary orbit to a centered power orbit

For an itinerary `epsilon`, define its bounded real companion tails

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
\tag{5}
\]

They satisfy the same affine recurrence

\[
M x_{n+1}
=
N x_n-(N-M)\varepsilon_n.
\tag{6}
\]

For a nontrivial ordinary orbit, in fact

\[
0<x_n<1
\tag{7}
\]

for every `n`. Put

\[
\boxed{
\xi
=
\frac{A_0-x_0}{M}>0.
}
\tag{8}
\]

Then

\[
\boxed{
\left\|\xi\beta^n\right\|
<\frac1N
}
\tag{9}
\]

for every `n`.

### From a centered power orbit to an ordinary orbit

Conversely, let `xi` lie in `(3)`. For each `n`, let `B_n` be the unique nearest integer to

\[
y_n=\xi\beta^n
\]

and write

\[
u_n=y_n-B_n,
\qquad
|u_n|\le\frac1N.
\tag{10}
\]

Then no `u_n` is zero, and the endpoint values `+-1/N` never occur. Define

\[
\boxed{
\varepsilon_n
=
\begin{cases}
1,&u_n>0,\\
0,&u_n<0,
\end{cases}
}
\tag{11}
\]

\[
\boxed{
A_n=M B_n+\varepsilon_n
=
\left\lceil
M\xi\beta^n
\right\rceil,
}
\tag{12}
\]

and

\[
\boxed{
x_n
=
\varepsilon_n-Mu_n
=
A_n-M\xi\beta^n.
}
\tag{13}
\]

Then `0<x_n<1`, every `A_n>=2`, and `(1)` holds for every `n`.

The two constructions are inverse.

## 3. Forward proof

Write

\[
A_n=M B_n+\varepsilon_n
\tag{14}
\]

using `(2)`. Subtract `(6)` from `(1)`:

\[
A_n-x_n
=
\beta^n(A_0-x_0).
\tag{15}
\]

After division by `M`,

\[
\xi\beta^n
=
B_n+rac{\varepsilon_n-x_n}{M}.
\tag{16}
\]

The real recurrence can also be written

\[
x_n
=
\frac{N-M}{N}\varepsilon_n
+
\frac MN x_{n+1}.
\tag{17}
\]

Therefore

\[
\frac{\varepsilon_n-x_n}{M}
=
\frac{\varepsilon_n-x_{n+1}}{N}.
\tag{18}
\]

Since `0<=x_(n+1)<=1`, equation `(18)` gives

\[
\left|
\frac{\varepsilon_n-x_n}{M}
\right|
\le\frac1N.
\tag{19}
\]

For a nontrivial ordinary orbit the inequalities are strict. If a real tail were `0`, every future digit would be zero; integrality of the expanding recurrence would force the ordinary tail to be zero. If a real tail were `1`, every future digit would be one; integrality would force the ordinary tail to be the trivial fixed state `1`. Both contradict `A_n>=2`.

Thus `B_n` is the unique nearest integer to `xi beta^n`, and `(9)` follows.

## 4. No-zero lemma for the converse

Assume `(3)`. Because `1/N<1/2`, each nearest integer `B_n` is unique.

Suppose `u_n=0` for some `n`. Then

\[
y_n=B_n>0
\]

is an ordinary integer. Since

\[
y_{n+k}
=
B_n\frac{N^k}{M^k},
\]

consider `k=1`. If `M` did not divide `B_n`, the reduced rational would have nonzero denominator dividing `M`, so its distance to the nearest integer would be at least `1/M>1/N`, contradicting `(3)`. Hence `M|B_n`.

Repeating at every later step gives

\[
M^k\mid B_n
\]

for all `k`, forcing `B_n=0`, contrary to `y_n>0`. Therefore

\[
\boxed{u_n\ne0\quad\text{for every }n.}
\tag{20}
\]

The same argument combined with the transition below rules out `u_n=+-1/N`; hence the critical bound is automatically strict for positive infinite orbits.

## 5. Integral carry and sign table

Define

\[
\boxed{
c_n
=N u_n-Mu_{n+1}.}
\tag{21}
\]

Because `M y_(n+1)=N y_n`,

\[
c_n
=M B_{n+1}-N B_n
\in\mathbb Z.
\tag{22}
\]

Moreover,

\[
|c_n|
\le
N|u_n|+M|u_{n+1}|
\le
1+\frac MN
<2.
\tag{23}
\]

Thus

\[
c_n\in\{-1,0,1\}.
\tag{24}
\]

The signs determine the carry exactly:

\[
\begin{array}{c|c|c}
\operatorname{sgn}(u_n)&\operatorname{sgn}(u_{n+1})&c_n\\
\hline
+&+&0\\
-&-&0\\
+&-&1\\
-&+&-1
\end{array}
\tag{25}
\]

For example, if both errors are positive, `c_n=1` would require `N u_n>1`, impossible except at the excluded endpoint, while `c_n=-1` would force `M u_(n+1)>1`. The other same-sign case is analogous. Opposite signs determine the sign of the nonzero integer `c_n`.

With `(11)`, the table is

\[
\boxed{
c_n=\varepsilon_n-\varepsilon_{n+1}.}
\tag{26}
\]

Combining `(22)` and `(26)` gives

\[
M B_{n+1}+\varepsilon_{n+1}
=
N B_n+\varepsilon_n.
\tag{27}
\]

Multiplication by `M` and the definition `(12)` yield

\[
M A_{n+1}
=
N A_n-(N-M)\varepsilon_n,
\]

which is `(1)`.

Equation `(13)` and `(26)` similarly give the real companion recurrence `(6)`.

## 6. Positivity and nontriviality

Because `y_n>0`, if `u_n<0` then `B_n>=1` and `A_n>=M`. If `u_n>0`, then `B_n>=0`. The only possible state below `2` is `A_n=1`, which would mean `B_n=0` and `epsilon_n=1`.

But `(1)` would then force `A_(n+1)=1`, and inductively every future state would be `1`. Equivalently, the positive errors would satisfy

\[
u_{n+k}=\beta^k u_n,
\]

contradicting their uniform bound unless `u_n=0`, already excluded. Hence

\[
\boxed{A_n\ge2\quad\text{for every }n.}
\tag{28}
\]

Unrolling the bounded real recurrence shows that `(13)` is exactly the series `(5)`, so the reconstruction returns the same real companion. Equations `(12)` and `(13)` then show that the forward and converse maps are inverse.

## 7. The `64 -> 81` specialization

For

\[
M=64,
\qquad
N=81,
\qquad
\beta=\frac{81}{64},
\]

the theorem becomes

\[
\boxed{
\begin{aligned}
&\exists\text{ a nontrivial infinite ordinary }64\to81\text{ survivor}\\
&\qquad\Longleftrightarrow\\
&\exists\xi>0\text{ such that }
\left\|\xi\left(\frac{81}{64}\right)^n\right\|
\le\frac1{81}
\quad\forall n\ge0.
\end{aligned}
}
\tag{29}
\]

The reconstruction is explicit:

\[
\boxed{
A_n
=
\left\lceil
64\xi\left(\frac{81}{64}\right)^n
\right\rceil,
}
\tag{30}
\]

\[
\boxed{
\varepsilon_n
=A_n\bmod64
\in\{0,1\},
}
\tag{31}
\]

and, because `1<81/64<2`,

\[
\boxed{
A_{n+1}
=
\left\lfloor\frac{81A_n}{64}\right\rfloor.
}
\tag{32}
\]

The initial room is recovered from the centered parameter by

\[
\boxed{A_0=\lceil64\xi\rceil,}
\tag{33}
\]

while

\[
x_n
=A_n-64\xi(81/64)^n
\in(0,1)
\tag{34}
\]

is exactly the bounded real companion tail.

The two trivial section points `A=0` and `A=1` both collapse to the degenerate parameter `xi=0`; positive `xi` parametrizes exactly the nontrivial section.

## 8. Relationship to the existing packet

`D-9302` previously recorded four objects:

1. the ordinary integral tails `A_n`;
2. the symbolic digits `epsilon_n`;
3. the bounded real companions `x_n`;
4. the expanding difference `A_n-x_n`.

This theorem shows that they are not separate constraints. They are four reconstructions of the single centered orbit

\[
\xi(81/64)^n.
\]

It removes the remaining finite-versus-adic ambiguity at the level of the ordinary section: once a positive centered parameter exists, the ordinary integer orbit is recovered by the ceiling formula `(30)`.

## 9. Literature boundary

The result creates an exact native generalized `Z`-number problem, but it does not identify it with Mahler's classical one-sided interval problem. The condition is centered and uses two arcs around the circle origin.

The repository literature audit remains applicable:

- Mahler and Flatto--Lagarias--Pollington supply methodology and nearby range obstructions;
- no imported theorem in the current literature packet excludes the exact critical radius `1/81` for the ratio `81/64`;
- replacing the centered two-arc condition by one Euclidean interval would be an invalid transfer.

No external theorem is used in the proof above.

## 10. Gap audit

- `T-9315` is a reformulation theorem, not a nonexistence theorem.
- The centered set `Z_ctr_(64,81)` may still be nonempty; proving it empty is exactly the remaining ordinary-section problem.
- The critical inequality is closed in the definition, but every positive infinite orbit automatically satisfies it strictly.
- The theorem concerns the induced `64 -> 81` subsystem. Translation to every possible ordinary Collatz counterexample remains branch-qualified.
- Every proof-looking statement remains `PROPOSED` pending independent reconstruction.

## 11. Suggested next attack

Exploit the fourth-power identity

\[
\frac{81}{64}=\left(\frac32\right)^4.
\]

`L-9312` converts `(29)` into a four-phase scheduled trapping problem for the complete `3/2` orbit. The next theorem should use the transition restrictions between those phases, rather than only the total length of their union.