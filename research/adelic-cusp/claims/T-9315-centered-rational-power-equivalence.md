# T-9315 — Centered rational-power equivalence

**Claim ID:** T-9315  
**Title:** Nontrivial ordinary binary-chart orbits are exactly critical centered rational-power orbits  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** elementary nearest-integer arithmetic; `D-9302` for the `64 -> 81` crosswalk  
**Scope:** every coprime expanding binary chart and the ordinary section of the `64 -> 81` subsystem  
**Related counterexample candidates:** none

## 1. General binary chart

Fix coprime integers

\[
2\le M<N,
\qquad
\beta=N/M.
\tag{1}
\]

A **nontrivial ordinary binary-chart orbit** is a pair of sequences

\[
A_n\in\mathbb Z_{\ge2},
\qquad
e_n\in\{0,1\},
\qquad n\ge0,
\]

satisfying

\[
\boxed{
M A_{n+1}=N A_n-(N-M)e_n
}
\tag{2}
\]

for every `n`.

Reduction modulo `M` gives

\[
N(A_n-e_n)\equiv0\pmod M.
\]

Since `gcd(M,N)=1`,

\[
\boxed{A_n\equiv e_n\pmod M.}
\tag{3}
\]

Define

\[
\boxed{
\mathcal Z^{\rm ctr}_{M,N}
=
\left\{
\xi>0:
\left\|\xi\beta^n\right\|
\le 1/N
\text{ for every }n\ge0
\right\}.
}
\tag{4}
\]

Here `||y||` is distance to the nearest integer.

## 2. The theorem

There is a bijection

\[
\boxed{
\{
\text{nontrivial ordinary binary-chart orbits}
\}
\longleftrightarrow
\mathcal Z^{\rm ctr}_{M,N}.
}
\tag{5}
\]

### Ordinary orbit to centered parameter

Define the bounded real companion tails

\[
\boxed{
x_n
=
((N-M)/N)
\sum_{k\ge0}
e_{n+k}(M/N)^k
\in[0,1].
}
\tag{6}
\]

They satisfy

\[
M x_{n+1}=N x_n-(N-M)e_n.
\tag{7}
\]

For a nontrivial ordinary orbit, every `x_n` lies strictly between `0` and `1`. Put

\[
\boxed{
\xi=(A_0-x_0)/M>0.
}
\tag{8}
\]

Then

\[
\boxed{
\left\|\xi\beta^n\right\|<1/N
\quad(n\ge0).
}
\tag{9}
\]

### Centered parameter to ordinary orbit

Conversely, let `xi` lie in `(4)`. Let `B_n` be the unique nearest integer to

\[
y_n=\xi\beta^n
\]

and write

\[
u_n=y_n-B_n,
\qquad
|u_n|\le1/N.
\tag{10}
\]

Every `u_n` is nonzero, and the endpoint values `+-1/N` do not occur. Define

\[
\boxed{
e_n=\mathbf1_{u_n>0},
}
\tag{11}
\]

\[
\boxed{
A_n=M B_n+e_n=\left\lceil M\xi\beta^n\right\rceil,
}
\tag{12}
\]

and

\[
\boxed{
x_n=e_n-Mu_n=A_n-M\xi\beta^n.
}
\tag{13}
\]

Then

\[
0<x_n<1,
\qquad
A_n\ge2,
\]

and `(2)` holds at every step. The two constructions are inverse.

## 3. Forward proof

By `(3)`, write

\[
A_n=M B_n+e_n.
\tag{14}
\]

Subtracting `(7)` from `(2)` gives

\[
A_n-x_n=\beta^n(A_0-x_0).
\tag{15}
\]

After division by `M`,

\[
\boxed{
\xi\beta^n=B_n+M^{-1}(e_n-x_n).
}
\tag{16}
\]

The real recurrence can be written

\[
x_n=((N-M)/N)e_n+(M/N)x_{n+1}.
\tag{17}
\]

Therefore

\[
\boxed{
M^{-1}(e_n-x_n)=N^{-1}(e_n-x_{n+1}).
}
\tag{18}
\]

Since `0<=x_(n+1)<=1`, the last term has absolute value at most `1/N`.

The inequality is strict for a nontrivial orbit.

- If `x_n=0`, every future digit is zero. Equation `(2)` forces `M^k|A_n` for all `k`, hence `A_n=0`.
- If `x_n=1`, every future digit is one. Applying the same argument to `A_n-1` gives `A_n=1`.

Both contradict `A_n>=2`. Thus `(16)` identifies `B_n` as the nearest integer and proves `(9)`.

## 4. No-zero lemma for the converse

Because `N>=3`, the radius `1/N` is below `1/2`, so every nearest integer is unique.

Suppose `u_n=0`. Then

\[
y_n=B_n>0
\]

is an integer and

\[
y_{n+k}=B_nN^k/M^k.
\tag{19}
\]

If `M` did not divide `B_n`, the reduced rational `NB_n/M` would have a nontrivial denominator dividing `M`; its distance to the nearest integer would be at least `1/M>1/N`, contradicting `(4)`. Hence `M|B_n`.

Repeating at all later powers gives

\[
M^k|B_n
\quad\text{for every }k,
\]

so `B_n=0`, contrary to `y_n>0`. Therefore

\[
\boxed{u_n\ne0\quad(n\ge0).}
\tag{20}
\]

The transition analysis below also excludes `u_n=+-1/N`, so every positive centered orbit lies strictly inside the critical strip.

## 5. Integral carry and sign table

Define

\[
\boxed{c_n=N u_n-Mu_{n+1}.}
\tag{21}
\]

Since `M y_(n+1)=N y_n`,

\[
\boxed{c_n=M B_{n+1}-N B_n\in\mathbb Z.}
\tag{22}
\]

Also,

\[
|c_n|
\le N|u_n|+M|u_{n+1}|
\le1+M/N<2.
\tag{23}
\]

Hence `c_n` belongs to `{-1,0,1}`. Its value is determined by the signs:

\[
\boxed{
\begin{array}{c|c|c}
\operatorname{sgn}(u_n)&\operatorname{sgn}(u_{n+1})&c_n\\
\hline
+&+&0\\
-&-&0\\
+&-&1\\
-&+&-1.
\end{array}
}
\tag{24}
\]

For instance, with two positive errors, `c_n=-1` is impossible by sign, while `c_n=1` would require `Nu_n>1` except at the excluded endpoint. The other same-sign case is analogous; opposite signs force the corresponding nonzero integer.

By `(11)`,

\[
\boxed{c_n=e_n-e_{n+1}.}
\tag{25}
\]

Combining `(22)` and `(25)` gives

\[
M B_{n+1}+e_{n+1}=N B_n+e_n.
\tag{26}
\]

Using `(12)`, this is equivalent to `(2)`. Equations `(13)` and `(25)` similarly imply the real recurrence `(7)`.

## 6. Positivity and inverse maps

If `u_n<0`, then `y_n>0` forces `B_n>=1`, so `A_n>=M>=2`.

If `u_n>0`, then `B_n>=0`. The only possible state below `2` is `A_n=1`. Equation `(2)` would then force every future state to remain `1`; equivalently,

\[
u_{n+k}=\beta^k u_n,
\]

contradicting the uniform bound unless `u_n=0`, already excluded. Therefore

\[
\boxed{A_n\ge2\quad(n\ge0).}
\tag{27}
\]

Unrolling `(7)` recovers exactly the series `(6)`. Finally,

\[
A_0-x_0=M(B_0+u_0)=M\xi,
\]

so the forward and converse maps are inverse.

## 7. The `64 -> 81` specialization

Set

\[
M=64,
\qquad
N=81,
\qquad
\beta=81/64.
\]

Then

\[
\boxed{
\begin{aligned}
&\exists\text{ a nontrivial infinite ordinary }64\to81\text{ survivor}\\
&\qquad\Longleftrightarrow\\
&\exists\xi>0:
\left\|\xi(81/64)^n\right\|
\le1/81
\quad\forall n\ge0.
\end{aligned}
}
\tag{28}
\]

The reconstruction is

\[
\boxed{A_n=\left\lceil64\xi(81/64)^n\right\rceil,}
\tag{29}
\]

\[
\boxed{e_n=A_n\bmod64\in\{0,1\},}
\tag{30}
\]

and, since `1<81/64<2`,

\[
\boxed{A_{n+1}=\left\lfloor81A_n/64\right\rfloor.}
\tag{31}
\]

The initial room and real companion are

\[
\boxed{A_0=\lceil64\xi\rceil,}
\tag{32}
\]

\[
\boxed{x_n=A_n-64\xi(81/64)^n\in(0,1).}
\tag{33}
\]

The trivial section points `A=0` and `A=1` correspond to `xi=0`; positive `xi` parametrizes exactly the nontrivial section.

## 8. Structural meaning and boundary

The ordinary tails, digits, bounded real companions, and expanding differences are reconstructions of the single orbit

\[
\xi(81/64)^n.
\]

Once a positive centered parameter exists, the ordinary orbit is recovered by `(29)`.

However, `L-9313` proves that every binary itinerary has a bounded real error path. Only an itinerary whose nested nearest-integer cylinder stabilizes gives an ordinary centered parameter. Thus `T-9315` is a reformulation theorem, not a nonexistence theorem.

`CENTERED_LITERATURE_AUDIT.md` records the precise external near misses. No external theorem is used in this proof.

## 9. Correct next attack

By `L-9313`, pure real interval-cylinder emptiness cannot work. The exact target is the appended nearest-integer block sequence of `L-9314`:

\[
R_{K+1}=R_K+q_K64^K.
\]

Proving infinitely many `q_K` are nonzero for every nontrivial itinerary would make the centered set empty and close the ordinary section.

## 10. Gap audit

- The centered set may still be nonempty.
- The critical inequality in `(28)` is automatically strict for every positive infinite orbit.
- The theorem concerns the induced `64 -> 81` subsystem; translation to every possible Collatz counterexample remains branch-qualified.
- Every proof-looking statement remains `PROPOSED` pending independent reconstruction.