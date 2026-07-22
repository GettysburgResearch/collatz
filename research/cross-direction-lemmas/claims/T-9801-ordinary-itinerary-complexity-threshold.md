# T-9801 -- Ordinary-itinerary complexity threshold

Claim ID: `T-9801`
Title: Every ordinary binary-chart itinerary has an explicit linear factor-complexity floor, giving a finite certificate for critical equality languages
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave13-adelic-bridge`
Reviewing agents: `gpt56-synthesis-01-wave13-cap-head`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: elementary binary-chart recurrence; branch-qualified source interface `PR #16/T-9315` and context `PR #16/L-9311`, `L-9315`, `T-9316`, `T-9317` at live head `1bb8c6b`; branch-qualified predecessor `PR #20/T-9402`, `T-9405` at `ed1ee9d`
Scope: every coprime expanding binary chart; the critical centered-power equality bridge for the ordinary `64 -> 81` section
Related counterexample candidates: none

## 1. General binary chart

Fix coprime integers

\[
2\le M<N,
\qquad
\beta={N\over M},
\qquad
\delta=\log_M\beta,
\qquad
\kappa={1\over\delta}={\log M\over\log(N/M)}.
\tag{1}
\]

Let

\[
A_n\in\mathbb Z_{\ge2},
\qquad
e_n\in\{0,1\},
\tag{2}
\]

be an infinite ordinary binary-chart orbit:

\[
\boxed{
M A_{n+1}=N A_n-(N-M)e_n
}
\qquad(n\ge0).
\tag{3}
\]

For `ell>=1`, write

\[
p_e(\ell)
=
\#\left\{
e_re_{r+1}\cdots e_{r+\ell-1}:r\ge0
\right\}
\tag{4}
\]

for the one-sided factor complexity of the itinerary.

## 2. Exact prefix-diversity theorem

Every ordinary orbit in (3) satisfies

\[
\boxed{
p_e(\ell)
\ge
1+
\max\left\{
0,
\left\lfloor
{\ell-\log_M A_0\over\delta}
\right\rfloor
\right\}.
}
\tag{5}
\]

In particular,

\[
\boxed{
\liminf_{\ell\to\infty}{p_e(\ell)\over\ell}
\ge\kappa.
}
\tag{6}
\]

This is a universal structural restriction on an ordinary itinerary. It is
not merely a nonperiodicity statement: the itinerary must create at least
`kappa` asymptotically distinct length-`ell` factors per unit length.

### Proof

First note from (3) that

\[
A_{n+1}\le\beta A_n,
\qquad
A_{n+1}-A_n
={N-M\over M}(A_n-e_n)>0.
\tag{7}
\]

Thus the ordinary orbit is strictly increasing and

\[
A_t\le\beta^tA_0.
\tag{8}
\]

Suppose equal length-`ell` factors begin at `0<=r<t`:

\[
e_{r+i}=e_{t+i}
\qquad(0\le i<\ell).
\tag{9}
\]

Put

\[
D_i=A_{t+i}-A_{r+i}>0.
\tag{10}
\]

Subtracting (3) at the two starts gives

\[
M D_{i+1}=N D_i
\qquad(0\le i<\ell).
\tag{11}
\]

Because `gcd(M,N)=1` and every `D_i` is integral, repeated divisibility in
(11) gives

\[
M^\ell\mid D_0.
\tag{12}
\]

Consequently

\[
M^\ell
\le D_0
=A_t-A_r
<A_t
\le\beta^tA_0,
\tag{13}
\]

and hence every repeated factor obeys the strict inequality

\[
\boxed{
\ell<\delta t+\log_M A_0.
}
\tag{14}
\]

If

\[
\ell<\log_M A_0,
\tag{15}
\]

then (5) is just the trivial inequality `p_e(ell)>=1`. Otherwise, set

\[
H_\ell
=
\left\lfloor
{\ell-\log_M A_0\over\delta}
\right\rfloor
\ge0.
\tag{16}
\]

The factors of length `ell` starting at

\[
0,1,\ldots,H_\ell
\tag{17}
\]

are pairwise distinct. Indeed, a repetition with second start `t<=H_ell`
would give

\[
\ell
<\delta t+\log_M A_0
\le\delta H_\ell+\log_M A_0
\le\ell,
\tag{18}
\]

which is impossible. There are `H_ell+1` factors in (17), proving (5).
Division by `ell` and passage to the lower limit proves (6). QED

## 3. The exact `64 -> 81` threshold

For the centered ordinary section,

\[
M=64,
\qquad
N=81,
\qquad
\boxed{
\kappa_{64,81}
={\log64\over\log(81/64)}
=17.6548475770\ldots .
}
\tag{19}
\]

The comparison needed below is exact:

\[
\boxed{\kappa_{64,81}>16.}
\tag{20}
\]

Indeed, (20) is equivalent to

\[
(81/64)^{16}<64
\iff
3^{64}<2^{102}.
\tag{21}
\]

The latter follows by squaring the exact integer inequality

\[
3^{32}
=1853020188851841
<2251799813685248
=2^{51}.
\tag{22}
\]

Thus every hypothetical nontrivial ordinary `64 -> 81` itinerary satisfies

\[
\boxed{
\liminf_{\ell\to\infty}{p_e(\ell)\over\ell}
\ge\kappa_{64,81}>16.
}
\tag{23}
\]

## 4. Critical source-equality closure

The complexity floor gives the following exact source interface. Assume an
external nearest-integer theorem, in a scope containing every centered
parameter reconstructed from a hypothetical ordinary orbit, proves

\[
\limsup_{n\to\infty}
\left\|\xi(81/64)^n\right\|
\ge {1\over81}.
\tag{24}
\]

Assume also that whenever all powers lie in the closed critical strip and
equality holds in (24), the nearest-error sign itinerary belongs to a class
denoted `mathcal E`. If

\[
\boxed{
\text{every }e\in\mathcal E\text{ satisfies }
\liminf_{\ell\to\infty}{p_e(\ell)\over\ell}
<\kappa_{64,81},
}
\tag{25}
\]

then the nontrivial ordinary `64 -> 81` section is empty.

More generally, let `X` be any one-sided subshift and let

\[
P_X(\ell)
=\#\{\text{length-`ell` words occurring in }X\}.
\tag{26}
\]

It is enough that every equality itinerary lie in some subshift `X` for
which

\[
\boxed{
\liminf_{\ell\to\infty}{P_X(\ell)\over\ell}
<\kappa_{64,81}.
}
\tag{27}
\]

### Proof

Suppose an ordinary survivor exists. The centered equivalence in
`PR #16/T-9315` reconstructs `xi>0` with

\[
\left\|\xi(81/64)^n\right\|<1/81
\qquad(n\ge0).
\tag{28}
\]

Its limit superior is at most `1/81`; (24) forces equality. The asserted
source classification puts its sign itinerary in the classified class.
Equation (25)
then contradicts (23).

For the subshift form, an itinerary `e in X` has

\[
p_e(\ell)\le P_X(\ell)
\tag{29}
\]

at every length, so (27) implies (25). QED

No particular external theorem is asserted to satisfy (24), and no
uninspected equality classification is imported here.

## 5. Finite certificate for uniform-morphic equality languages

There is an elementary finite test for a large family of possible equality
languages. Let

\[
\mu:\mathcal A\longrightarrow\mathcal A^L,
\qquad L\ge2,
\tag{30}
\]

be an `L`-uniform morphism, let `x=mu(x)` be a one-sided fixed point, and let
`c` be a letter coding from `mathcal A` to `{0,1}`. Put

\[
B=p_x(L+1).
\tag{31}
\]

Here `p_x` counts factors over the source alphabet `mathcal A`.

Every binary word `y` in the shift-orbit closure of `c(x)` satisfies

\[
\boxed{
p_y(n)\le Bn
\qquad(n\ge1).
}
\tag{32}
\]

Consequently, if

\[
\boxed{B<\kappa_{64,81},}
\tag{33}
\]

the entire orbit closure is disjoint from the set of ordinary itineraries.

### Proof

Choose `k>=0` so that

\[
L^k\le n<L^{k+1}.
\tag{34}
\]

The identity `x=mu^k(x)` partitions `x` into aligned level-`k` supertiles
of length `L^k`. A length-`n` factor meets at most `L+1` consecutive
supertiles. It is therefore determined by

1. one allowed length-`L+1` factor of `x`, after extending a shorter context
   to the right if necessary; and
2. its starting offset in `0,...,L^k-1`.

There are at most `B L^k<=Bn` such choices. Letter coding can only identify
factors, not create new choices, so the same bound holds for `c(x)`. Every
factor of a point in its shift-orbit closure is a factor of `c(x)`, proving
(32). Equations (23) and (33) are incompatible. QED

If the substitution alphabet itself is binary, then trivially

\[
B\le2^{L+1}.
\tag{35}
\]

Together with (20), this gives the unconditional structural consequence

\[
\boxed{
\begin{aligned}
&\text{no point in the orbit closure of any binary 2-uniform}\\
&\text{or binary 3-uniform morphic fixed point is an ordinary}\\
&\text{64-to-81 itinerary.}
\end{aligned}
}
\tag{36}
\]

Indeed, the two crude finite bounds are `2^3=8` and `2^4=16`, both strictly
below the threshold in (20). Fixed shifts and bitwise complements preserve the
same complexity bound. Changing a finite prefix adds only a bounded number
of exceptional factors at each length and does not alter the limiting slope.

In particular, (36) excludes the whole Thue--Morse orbit closure, not only
the literal finite shifts and complements treated by the explicit-square
argument in `PR #16/T-9316`.

## 6. What is genuinely added

`PR #16/L-9311` and `T-9316` expose the zero-carry mechanism and use one
explicit family of early repeated factors.  `PR #20/T-9402` and `T-9405`
already prove the same asymptotic factor-complexity threshold by a
pigeonhole/periodic-approximant route.  Thus (5)--(6) are an independent
recurrence-level reconstruction and exact integer restatement of that known
threshold, not a new global complexity barrier.

The genuinely new interface here is the finite uniform-morphism certificate
(31)--(33), coupled to the critical equality closure in Section 4.  It is
complementary to current `PR #16/L-9315`: that lemma transfers one explicit
efficient recurrence through possibly nonuniform bounded-distortion morphisms,
whereas (32) controls the entire orbit closure of a uniform-morphic fixed
point by its finite source language.  In particular, the orbit-closure
conclusion is strictly broader than checking a listed family of shifts: it
also covers limit points and every other sequence with the same substitution
language, without locating a particular square in each sequence.

## 7. Dependency audit

- Equations (5)--(23) are proved directly from the ordinary recurrence,
  coprimality, and exact integer comparison. They do not depend on an
  external nearest-integer theorem.
- `PR #16/T-9315` is used only for the conditional centered-parameter
  crosswalk in Section 4.
- `PR #16/L-9311`, `L-9315`, and `T-9316` are contextual predecessors, not
  proof dependencies for the calculation.  At live head `1bb8c6b`,
  `T-9316` uses the sharpened adjacent square at starts `2^m,2^(m+1)`, and
  `L-9315` consequently reaches morphic length distortion below
  `1/(2 delta)=8.8274...`; neither supplies the orbit-closure count (32).
- `PR #16/T-9317` motivates the critical equality interface; its unverified
  source hypotheses are restated explicitly in (24)--(25).
- `PR #20/T-9402` and `T-9405` are prior statements of the same lower
  factor-complexity slope.  They are cited for novelty accounting; the direct
  proof of (5) does not invoke them.
- The uniform-morphism bound is proved from aligned supertiles. No
  automatic-sequence theorem, recurrence theorem, entropy theorem, or
  computation is imported.
- The candidate Dubickas formula in
  `DUBICKAS_SPECIALIZATION_PREAUDIT.md` is not used.

## 8. Gap and scope audit

- No external source is claimed to attain the critical lower bound (24) or
  to have a particular equality language.
- If the verified scalar source constant is strictly below `1/81`, as the
  current conditional candidate suggests, Section 4 does not apply without
  a sharper scheduled/two-interval theorem or a near-extremal rigidity
  theorem.
- A binary word can have factor-complexity slope at least
  the threshold in (19) while still having zero entropy. The theorem does not
  exclude such high-complexity equality languages.
- Failure of the finite certificate (33) does not produce an
  ordinary orbit; it only leaves that morphic presentation unresolved.
- The theorem concerns the induced ordinary `64 -> 81` section. The
  branch-qualified translation to every possible Collatz counterexample is
  separate.
- The trivial ordinary states `0` and `1` are outside hypothesis (2) and are
  not contradicted by their constant itineraries.

## 9. Adversarial checks

1. **Overlaps.** The divisibility proof allows `r+ell>t`; no disjointness of
   the repeated factors is used.
2. **Absolute versus relative return time.** Inequality (14) uses the second
   absolute start `t`. The prefix-diversity window is chosen accordingly;
   no stronger gap-only assertion is smuggled into (5).
3. **Floor endpoint.** If the quotient in (16) is an integer, the strict
   inequality in (14) still contradicts a repetition at the endpoint.
4. **Coprimality.** The implication `M^ell | D_0` uses `gcd(M,N)=1` at every
   step. The theorem is not stated for a nonreduced chart.
5. **One-sided boundary.** A level-`k` context meeting fewer than `L+1`
   supertiles can always be extended to the right because the fixed point is
   infinite; no two-sided extension is assumed.
6. **Orbit closure.** Closure adds no new finite factors, so (32) remains a
   language bound. It is stronger than a claim only about literal shifts.
7. **Source scope.** The conditional closure requires (24) to cover the
   actual reconstructed `xi`, including any rational/irrational exceptions
   in the source theorem. An abstract or formula snippet is insufficient.
8. **No Thue--Morse import.** The theorem never assumes that a Dubickas
   equality word is Thue--Morse. It only supplies a ready implication if a
   fully audited source classification lands in that orbit closure or any
   other language satisfying (25).

## 10. Suggested next attack

Acquire the exact rational-base source theorem and preserve its whole
equality presentation. If the critical equality language is uniform
morphic, enumerate only its allowed length-`L+1` source contexts and compare
the resulting integer `B` with the threshold in (19).

If the verified scalar constant is subcritical, target a scheduled or
two-interval sharpening that reaches `1/81`, or prove that every ordinary
near-extremal word lies in a subshift whose language slope is below
the threshold in (19). Either result plugs directly into Sections 4--5 and closes
the ordinary section without any new large computation.
