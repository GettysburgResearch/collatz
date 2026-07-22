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
\beta=\frac{N}{M}.
\tag{1}
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
\tag{2}
\]

for every `n`.

Reduction modulo `M` gives

\[
N(A_n-\varepsilon_n)\equiv0\pmod M.
\]

Since `gcd(M,N)=1`,

\[
\boxed{A_n\equiv\varepsilon_n\pmod M.}
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
\le\frac1N
\text{ for every }n\ge0
\right\},
}
\tag{4}
\]

where `||y||` denotes distance to the nearest integer.

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

The maps in both directions are explicit.

### Ordinary orbit to centered parameter

Given an ordinary orbit, define the bounded real companion tails

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
\tag{6}
\]

Then

\[
M x_{n+1}
=
N x_n-(N-M)\varepsilon_n.
\tag{7}
\]

For a nontrivial orbit, every `x_n` lies strictly between `0` and `1`. Put

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
\quad(n\ge0).
}
\tag{9}
\]

### Centered parameter to ordinary orbit

Conversely, let `xi` lie in `(4)`. For each `n`, let `B_n` be the unique nearest integer to

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

Every `u_n` is nonzero, and the endpoint values `+-1/N` do not occur. Define

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
A_n
=M B_n+\varepsilon_n
=
\left\lceil M\xi\beta^n\right\rceil,
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

Then

\[
0<x_n<1,
\qquad
A_n\ge2,
\]

and `(2)` holds at every step. These constructions are inverse.

## 3. Forward proof

By `(3)`, write

\[
A_n=M B_n+\varepsilon_n.
\tag{14}
\]

Subtracting `(7)` from `(2)` gives

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

The real recurrence can be rewritten as

\[
x_n
=
\frac{N-M}{N}\varepsilon_n
+
\frac MN x_{n+1}.
\tag{17}
\]

Consequently,

\[
\boxed{
\frac{\varepsilon_n-x_n}{M}
=
\frac{\varepsilon_n-x_{n+1}}{N}.
}
\tag{18}
\]

Since `0<=x_(n+1)<=1`,

\[
\left|
\frac{\varepsilon_n-x_n}{M}
\right|
\le\frac1N.
\tag{19}
\]

The inequality is strict for a nontrivial ordinary orbit.

- If `x_n=0`, every future digit is zero. Equation `(2)` then forces `M^k|A_n` for every `k`, hence `A_n=0`.
- If `x_n=1`, every future digit is one. Applying the preceding argument to `A_n-1` forces `A_n=1`.

Both contradict `A_n>=2`. Thus `(16)` identifies `B_n` as the unique nearest integer and proves `(9)`.

## 4. No-zero lemma for the converse

Assume `(4)`. Because `N>=3`,

\[
1/N<1/2,
\]

so every nearest integer `B_n` is unique.

Suppose `u_n=0`. Then

\[
y_n=B_n>0
\]

is an integer and

\[
y_{n+k}=B_n\frac{N^k}{M^k}.
\tag{20}
\]

If `M` did not divide `B_n`, the reduced rational `N B_n/M` would have a nontrivial denominator dividing `M`; its distance to the nearest integer would be at least `1/M>1/N`, contradicting `(4)`. Hence `M|B_n`.

Repeating this argument at all later powers gives

\[
M^k|B_n
\quad\text{for every }k,
\]

so `B_n=0`, contrary to `y_n>0`. Therefore

\[
\boxed{u_n\ne0\quad(n\ge0).}
\tag{21}
\]

The transition analysis below also excludes `u_n=+-1/N`, so every positive centered orbit lies strictly inside the critical strip.

## 5. Integral carry and sign table

Define

\[
\boxed{
c_n=N u_n-Mu_{n+1}.}
\tag{22}
\]

Since `M y_(n+1)=N y_n`,

\[
\boxed{
c_n=M B_{n+1}-N B_n\in\mathbb Z.}
\tag{23}
\]

Moreover,

\[
|c_n|
\le
N|u_n|+M|u_{n+1}|
\le
1+rac MN
<2.
\tag{24}
\]

Hence

\[
c_n\in\{-1,0,1\}.
\]

The signs determine the carry exactly:

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
\tag{25}
\]

For example, when both errors are positive, `c_n=-1` is impossible by sign, while `c_n=1` would require `Nu_n>1` except at the excluded endpoint. The other same-sign case is analogous; opposite signs force the corresponding nonzero integer.

By `(11)`,

\[
\boxed{
c_n=\varepsilon_n-\varepsilon_{n+1}.}
\tag{26}
\]

Combining `(23)` and `(26)` gives

\[
M B_{n+1}+arepsilon_{n+1}
=
N B_n+arepsilon_n.
\tag{27}
\]

Using `(12)`, equation `(27)` is equivalent to `(2)`.

Similarly, `(13)` and `(26)` imply the real recurrence `(7)`.

## 6. Positivity and nontriviality

If `u_n<0`, then `y_n>0` forces `B_n>=1`, so `A_n>=M>=2`.

If `u_n>0`, then `B_n>=0`. The only possible state below `2` is `A_n=1`, which means `B_n=0` and `epsilon_n=1`. Equation `(2)` would then force `A_(n+1)=1`, and inductively every future state would be `1`. Equivalently,

\[
u_{n+k}=\beta^k u_n,
\]

contradicting the uniform bound unless `u_n=0`, already excluded. Thus

\[
\boxed{A_n\ge2\quad(n\ge0).}
\tag{28}
\]

Unrolling the bounded recurrence `(7)` recovers exactly the series `(6)`. Finally,

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
\beta=\frac{81}{64}.
\]

Then

\[
\boxed{
\begin{aligned}
&\exists\text{ a nontrivial infinite ordinary }64\to81\text{ survivor}\\
&\qquad\Longleftrightarrow\\
&\exists\xi>0:
\left\|\xi\left(\frac{81}{64}\right)^n\right\|
\le\frac1{81}
\quad\forall n\ge0.
\end{aligned}
}
\tag{29}
\]

The reconstruction is

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
\varepsilon_n=A_n\bmod64\in\{0,1\},
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

The initial room and real companion are

\[
\boxed{A_0=\lceil64\xi\rceil,}
\tag{33}
\]

\[
\boxed{
x_n=A_n-64\xi(81/64)^n\in(0,1).}
\tag{34}
\]

The trivial section points `A=0` and `A=1` both correspond to the degenerate parameter `xi=0`; positive `xi` parametrizes exactly the nontrivial section.

## 8. Structural meaning

`D-9302` records four objects:

1. ordinary integral tails `A_n`;
2. symbolic digits `epsilon_n`;
3. bounded real companions `x_n`;
4. the expanding difference `A_n-x_n`.

`T-9315` shows they are four reconstructions of

\[
\xi(81/64)^n.
\]

Once a positive centered parameter exists, there is no remaining ambiguity about the ordinary orbit: it is recovered by the ceiling formula `(30)`.

`L-9313` then supplies the complementary audit: every binary itinerary has a bounded real error path, but only an itinerary whose nested nearest-integer cylinder stabilizes gives an ordinary centered parameter.

## 9. Literature boundary

This is an exact native generalized `Z`-number problem, but it is not Mahler's classical one-sided interval problem.

- The condition is centered around the circle origin.
- `81/64=(3/2)^4` creates the scheduled intermediate geometry of `L-9312`.
- The real error language has full symbolic support.
- Ordinary realization is an inverse-limit nearest-integer stabilization property.

`CENTERED_LITERATURE_AUDIT.md` records the precise near misses. No external theorem is used in this proof.

## 10. Gap audit

- `T-9315` is a reformulation theorem, not a nonexistence theorem.
- The centered set may still be nonempty.
- The closed critical inequality in `(29)` is automatically strict for every positive infinite orbit.
- The theorem concerns the induced `64 -> 81` subsystem; translation to every possible Collatz counterexample remains branch-qualified.
- Every proof-looking statement remains `PROPOSED` pending independent reconstruction.

## 11. Correct next attack

By `L-9313`, pure real interval-cylinder emptiness is impossible as a proof strategy. The exact target is the appended nearest-integer block sequence of `L-9314`:

\[
R_{K+1}=R_K+q_K64^K.
\]

Proving infinitely many `q_K` are nonzero for every nontrivial itinerary would make the centered set empty and close the ordinary section.