# Near-linear populations inside the actual forward Collatz section

## Status and scope

This is a written analytic consequence of the selected-density construction in
PR180, `LINEAR_BLOCK_ATOM_FLOOR.md`, and its stated input, Tao's published
fine-scale Syracuse mixing theorem. It is not yet a Lean formalization of that
analytic input. The new argument does **not** assume mixing conditional on a
fixed valuation total. It keeps a bounded real affine offset while smoothing,
then chooses one total by a finite pigeonhole argument.

The conclusion places actual, distinct, equal-clock predecessors of every
positive ternary-unit target inside the **shrinking dyadic section itself**:
there is an absolute constant `gamma > 0` such that, for every positive integer
`a` with `3` not dividing `a`, there are arbitrarily large integers `d` and a
finite set `P` satisfying

\[
 P\subseteq\left\{n\text{ odd}:2^d\le n,
 (d+1)(n-2^d)\le10\,2^d\right\},
 \qquad |P|\ge\gamma\frac{2^d}{(d+1)^2},                 \tag{M}
\]

and all `n in P` reach the supplied `a` at one common ordinary shortcut clock
at most `15(d+1)`.
The constant `gamma` is independent of the target; the onset and the sequence
of successful octaves may depend on it. The section in PR173 has constant 70,
so (M) lies inside that exact section.

This is a positive population theorem. It does not establish a survivor upper
bound, return descent, absence of another cycle, or Collatz.

## 1. Exact affine-word conventions

Put

\[
 \alpha=\log_2 3,\qquad \rho=7/8.
\]

For a word `w = (a_1,...,a_s)` of positive integer exponents let

\[
 A_i=\sum_{j\le i}a_j,\quad A(w)=A_s,\quad
 \omega_w=3^s2^{-A(w)},\quad
 \beta_w=\sum_{i=1}^s3^{i-1}2^{-A_i}.
\]

The inverse equation from a positive odd target `b` is

\[
             b=\omega_w n+\beta_w.                    \tag{1.1}
\]

All rational denominators here are powers of two. The congruence
`beta_w = b (mod 3^s)` is equivalent to integrality of

\[
       n=\frac{2^{A(w)}b-2^{A(w)}\beta_w}{3^s}.         \tag{1.2}
\]

That congruence also makes every successive inverse step integral. For the
first step it implies `2^(a_1)b = 1 (mod 3)`. Its inverse parent
`b_1=(2^(a_1)b-1)/3` is a positive odd integer: the numerator is positive,
odd, and divisible by three. Dividing the remaining affine relation gives
the remaining word congruence at `b_1`. Induction proves legality of the
whole inverse word.

Because each intermediate target is odd, the prescribed exponent is exactly
the power of two removed by that odd Collatz step. Thus the ordinary shortcut
clock from `n` to `b` is exactly `A(w)`. At a fixed word length, different
admissible words give different sources: the accelerated forward orbit of
one source uniquely recovers the exponent word, in reverse order. In
particular this injectivity holds within any fixed-total class. No
nonperiodicity assumption is needed when only one depth is counted.

For a word family `W`, its normalized residue subdensity at level `s` is

\[
 F_W(r)=\sum_{\substack{w\in W\\\beta_w\equiv r\ (3^s)}}
                    3^s2^{-A(w)}.                    \tag{1.3}
\]

## 2. A controlled atom floor at every sufficiently large depth

The strengthened floor needed here is the following statement.

**Controlled-floor lemma.** There are constants `c > 0`, `B >= 1`, an integer
`E >= 1`, and `s_0`, such that for every `s >= s_0` and every ternary-unit
residue `r modulo 3^s`,

\[
 \sum_{\substack{w:\ |w|=s,\ \beta_w\equiv r\ (3^s)\\
  1.9s-E\le A(w)\le2.1s+E,\ \beta_w\le B}}
                   3^s2^{-A(w)}\ \ge c.              \tag{CF}
\]

The bounds on real `beta_w` and on the total `A(w)` are simultaneous.
The word family in (CF) is finite.

### 2.1 Inputs from the existing selected-density construction

Use exactly the original block schedule

\[
 b_j=10(j+1),\qquad d_N=5N(N+1),\qquad k_N=b_N.
\]

The selected prefix family `Gamma_N` has length `d_N`, with each block total
in `[1.9 b_j,2.1 b_j]`. The original note proves

\[
 \omega_w\le\rho^{d_N},\qquad \beta_w\le B_*,\qquad
 \#\{A(w):w\in\Gamma_N\}\le d_N+1,                   \tag{2.1}
\]

where one may take `B_* = 16*2^60`.

Let `T_(w,k)` be its positive transport operator. Its weighted counting bound
for an arbitrary function `h` on `Z/(3^k)` is

\[
 \left\|\sum_{w\in\Gamma_N}T_{w,k}h\right\|_\infty
 \le(d_N+1)(B_*+3^k\rho^{d_N})\,\|h\|_1.             \tag{2.2}
\]

The norm on the right uses normalized counting measure. In the original
notation the smoothed selected density

\[
       g_N=\sum_{w\in\Gamma_N}T_{w,b_N}D_{b_N}
\]

is defined at level `d_N+b_N`. Uniform convergence and positive retained mass
give a fixed unit cylinder `y modulo 3^q`, a number `kappa > 0`, and `N_0`
such that

\[
      g_N(r)\ge\kappa
\quad(N\ge N_0,\ r\equiv y\pmod{3^q}).                \tag{2.3}
\]

These are proved in Sections 2--4 of the existing note. Their only imported
analytic input is Tao's fine-scale estimate

\[
 \|D_k-\operatorname{lift}D_b\|_1\le C_4 b^{-4}
          \quad(1\le b\le k).                          \tag{2.4}
\]

### 2.2 Fill every intermediate depth

For any sufficiently large integer `h`, choose `N` by

\[
        d_{N+1}\le h<d_{N+2},\qquad k=h-d_N.
\]

Then

\[
       b_N\le k<b_N+b_{N+1}=10(2N+3).                 \tag{2.5}
\]

Define `g_(N,k)=sum_(w in Gamma_N) T_(w,k) D_k` at level `h`.
Transport commutes with lifting. Equations (2.2) and (2.4) give

\[
 \|g_{N,k}-\operatorname{lift}g_N\|_\infty
 \le(d_N+1)(B_*+3^k\rho^{d_N})C_4 b_N^{-4}=o(1),       \tag{2.6}
\]

uniformly for `k` in (2.5). Indeed `d_N` is quadratic, `k` is linear,
`3^k rho^(d_N)` is uniformly bounded, and the remaining power is
`O(N^2/N^4)`. Consequently `g_(N,k) >= 3 kappa/4` on the same cylinder
once `N` is large.

### 2.3 Restrict the terminal total without assuming conditional mixing

Let `D_k^good` be the nonnormalized Syracuse subdensity retaining only the
terminal words with total in `[1.9k,2.1k]`. The geometric Chernoff estimate
already used in the original construction gives

\[
 \|D_k-D_k^{\rm good}\|_1
   =\Pr(A_k\notin[1.9k,2.1k])\le2e^{-k/1200}.         \tag{2.7}
\]

Applying the **same positive prefix operator** and (2.2) bounds the pointwise
loss by

\[
 (d_N+1)(B_*+3^k\rho^{d_N})2e^{-k/1200}=o(1).          \tag{2.8}
\]

It follows that this fully retained subdensity is at least `kappa/2` on the
cylinder, at every sufficiently large level `h`.

Every retained full word has total in `[1.9h,2.1h]`. Its real offset satisfies

\[
 \beta_{w*v}=\beta_w+\omega_w\beta_v
 \le B_*+\rho^{d_N}2^k\le B_*+1                      \tag{2.9}
\]

for large `N`. The crude bound `beta_v < 2^k` holds for every positive
exponent word, since `A_i >= i` and the resulting geometric series is less
than `2^k`. The last inequality in (2.9) is uniform in (2.5).

Thus the cylinder lower bound now holds for **finite controlled families**
at every sufficiently large depth, not merely for unrestricted densities
or for the triangular subsequence.

### 2.4 Spread the controlled cylinder to all unit residues

The residue `1+3y` is a unit modulo `3^(q+1)`. Since 2 generates that unit
group, there is an integer

\[
           1\le e\le E:=2\,3^q
\]

such that `2^e r = 1+3y (mod 3^(q+1))`, for every supplied unit `r`.
Therefore `z=(2^e r-1)/3` lies in the positive cylinder. Prepending this
one exponent to a controlled word at level `h=s-1` multiplies normalized
density by `3*2^(-e)`. The density contribution is at least

\[
          c:=3\,2^{-E}\kappa/2>0.                    \tag{2.10}
\]

Its real offset is at most

\[
 2^{-e}+3\,2^{-e}(B_*+1)
 \le(1+3(B_*+1))/2.
\]

Take, for instance, `B=2B_*+3`; the total lies between `1.9s-E` and
`2.1s+E`. This proves (CF). There was no division by a rare total event and
no estimate of a conditional residue distribution.

## 3. Uniform controlled floors give near-linear ordinary populations

Before using a band, (CF) already yields the following useful consequence:
for every unit target `a` and every `sigma < 1`, its ordinary predecessor
count is at least `X^sigma` for all sufficiently large `X`.

For this consequence repeat the construction with block totals in
`[(2-epsilon)b,(2+epsilon)b]`, for an arbitrary fixed
`0 < epsilon <= 1/10`. The same offset bound works; the rejection estimate
becomes `2 exp(-epsilon^2 b/12)`. All convergence arguments remain valid.
Thus (CF) holds with `1.9,2.1` replaced by `2-epsilon,2+epsilon`, with
constants allowed to depend on `epsilon`.

Choose once and for all a positive odd unit predecessor `b` of `a` with
`b >= 2B`. Every controlled source satisfies

\[
 \frac b2\frac{2^{(2-\epsilon)s-E}}{3^s}
 \le n\le b\frac{2^{(2+\epsilon)s+E}}{3^s}.
\]

Its reciprocal is at least `omega_w/b`, so the family has reciprocal mass
at least `c/b`. Its cardinality is consequently at least

\[
             c\,2^{-E-1}
                   \left(\frac{2^{2-\epsilon}}3\right)^s.
\]

Because all sufficiently large depths are available, choosing the largest
`s` whose upper height bound is below `X` gives a power lower bound with
exponent

\[
 \theta_\epsilon=
 \frac{(2-\epsilon)\log2-\log3}
      {(2+\epsilon)\log2-\log3}\longrightarrow1.
\]

Choosing `epsilon` with `theta_epsilon > sigma` absorbs the fixed constants
and proves the stated `X^sigma` bound. Targets divisible by three are
excluded: the conclusion is false for their direct predecessor sets in
general. Every ordinary component nevertheless contains a unit target.

## 4. An elementary rotation choice with a positive buffer

Fix a positive unit target `a`. There are unbounded coprime rational
approximants `p/q` to `alpha` with

\[
                    |\alpha-p/q|\le q^{-2}.           \tag{4.1}
\]

Irrationality follows from the distinct prime factors of powers of 2 and 3.
Dirichlet approximation supplies the unbounded denominators. This is also
the rational-grid mechanism already used in PR173.

For each sufficiently large such `q`, put
`theta=log_2 a-(q+1)alpha`. The rational residues
`theta-jp/q`, `0 <= j < q`, form a translate of the `1/q` grid. Choose one
whose fractional part lies in `[3/q,4/q]`. Replacing `p/q` by `alpha`
moves it by less than `1/q`. Since these intervals are away from 0 and 1
for `q > 5`, no wrap occurs. Thus, for some

\[
          s=q+j\in[q,2q-1],
\]

the number

\[
       u_s=\{\log_2 a-(s+1)\alpha\}
\]

satisfies

\[
                     2/q\le u_s\le5/q.               \tag{4.2}
\]

In particular these selected depths are unbounded and eventually exceed
every fixed threshold from (CF).

## 5. A parent of height proportional to the chosen depth

Put `C=8(1+3B)`. Since `a` is a ternary unit, choose a fixed exponent class
`e_0 modulo 6` for which `2^(e_0)a = 4 (mod 9)`. Such a class exists because
2 generates the units modulo 9.

At the selected depth `s`, take the least positive exponent `e_s` in this
class for which

\[
                  a_s=(2^{e_s}a-1)/3\ge Cs.           \tag{5.1}
\]

The integer `a_s` is positive, odd, and a ternary unit. It reaches `a` in
exactly `e_s` ordinary shortcut steps. Consecutive permissible exponents
differ by six; their parents obey `a_(e+6)=64a_e+21`. Thus, for all
sufficiently large `s`,

\[
                    Cs\le a_s\le65Cs.                \tag{5.2}
\]

The threshold may depend on `a`; the constants in (5.2) do not.

Apply (CF) to the residue of this actual target `a_s`. For every contributing
word its positive odd source is

\[
 n=\frac{2^{A(w)}}{3^{s+1}}
                     (2^{e_s}a-1-3\beta_w).           \tag{5.3}
\]

Consequently

\[
 \log_2 n=A(w)+e_s+\log_2 a-(s+1)\alpha-\delta_w,
 \quad
 \delta_w=-\log_2\left(1-\frac{1+3\beta_w}{2^{e_s}a}\right).
                                                               \tag{5.4}
\]

All these errors have the same sign. Since `2^(e_s)a=3a_s+1`, (5.1) gives

\[
 0<\frac{1+3\beta_w}{2^{e_s}a}\le\frac1{24s}.
\]

For `0 <= v <= 1/2`, `-log_2(1-v) <= 4v`, using
`log 2 >= 1/2` and `-log(1-v) <= 2v`. Hence

\[
                  0<\delta_w\le\frac1{6s}\le\frac1{6q}.          \tag{5.5}
\]

Equations (4.2) and (5.5) put every contributing source's fractional binary
logarithm in `(0,5/q]`. No word-dependent carry is possible.

The total bound and (5.2) imply, for all sufficiently large `s`,

\[
              s/5\le d+1\le s,
       \qquad d=\lfloor\log_2 n\rfloor.               \tag{5.6}
\]

For completeness, `3/2 < alpha < 8/5`: these inequalities follow from
`2^3 < 3^2` and `3^5 < 2^8`. Thus the principal term
`A(w)-s alpha` is between `0.3s-E` and `0.6s+E`; the remaining
`log_2(a_s-beta_w)` is positive for large `s` and at most
`log_2(65Cs)=o(s)`. This proves (5.6).

Writing `v={log_2 n}`, convexity gives `2^v-1 <= v` for `0 <= v <= 1`.
Because `s <= 2q`,

\[
 (d+1)\frac{n-2^d}{2^d}
   =(d+1)(2^v-1)\le s\frac5q\le10.                  \tag{5.7}
\]

Every contributing source is therefore in the constant-10 section, and in
particular in the actual constant-70 forward section of PR173.

## 6. Fix one total, retain one octave, and count

For large `s`, at most `2s` integer totals lie in
`[1.9s-E,2.1s+E]`. Split the normalized mass in (CF) by those totals.
Some total `A` carries mass at least `c/(2s)`.

At this one total every word has weight `3^s 2^(-A)`. Exact word injectivity
therefore gives a set `P` of distinct sources with

\[
                         |P|\ge\frac{c}{2s}\frac{2^A}{3^s}.       \tag{6.1}
\]

The integer part in (5.4) is now fixed, so all members of `P` belong to one
and the same octave `[2^d,2^(d+1))`. They reach `a_s` at ordinary clock `A`
and then the original supplied target `a` at clock `A+e_s`, which is common
to the whole set.

Let `H=a_s2^A/3^s`. Every source is at most `H`, and the same phase
calculation with `beta=0` gives `2^d <= H < 2^(d+1)`. Using (5.2) in (6.1),

\[
 |P|\ge\frac{cH}{2sa_s}
      \ge\frac{c}{130C}\frac{2^d}{s^2}
      \ge\frac{c}{3250C}\frac{2^d}{(d+1)^2}.          \tag{6.2}
\]

Take `gamma=c/(3250C)`. Equation (5.6) shows that the successful octave
indices tend to infinity with the selected depths. This proves (M), with
all target, phase, word, count, and clock quantifiers in place.

The common clock also has an explicit linear bound in the octave index.
Since `2^(e_s)a=3a_s+1` and `a>=1`, (5.2) gives
`e_s <= log_2(195Cs+1)=O(log s)`. Therefore `A+e_s <= 3s` for all
sufficiently large selected depths. Combining this with (5.6) gives

\[
                     A+e_s\le15(d+1).                 \tag{6.3}
\]

Discarding the finitely many earlier choices preserves arbitrarily large
witness octaves and establishes the clock bound stated at the beginning.

### Unit sources, when required

The theorem above only needs odd sources, exactly as PR173's marked section
does. It does not assert that every counted source is a ternary unit.
An optional independent selection in `UNIT_SOURCE_APPENDIX.md` gives the
same population conclusion with unit sources and another absolute constant.
That selection uses the actual target modulo one additional power of three;
it is unnecessary for the conclusions below and is not silently imposed on
the simpler proof above.

## 7. Consequence for actual section survivors

Let `S_d` be the marked points of PR173 in `[2^d,2^(d+1))`, and let

\[
 V_d(t)=\#\{n\in S_d:T^j(n)\ne1\text{ for all }0\le j\le t\}.
\]

If a unit target `a` does not converge, every predecessor counted in (M)
also fails to converge. The common-clock property is stronger than needed
here: any predecessor which reached one would put `a` in the same ordinary
basin. Thus, for arbitrarily large `d`,

\[
                 \forall t,\qquad
       V_d(t)\ge\gamma\frac{2^d}{(d+1)^2}.            \tag{7.1}
\]

It follows that full Collatz is equivalent to the following concrete
condition without an unknown constant:

\[
 \boxed{\quad\exists d_0\ \forall d\ge d_0\ \exists t\ge0:
                    (d+1)^3 V_d(t)<2^d.\quad}        \tag{7.2}
\]

The forward implication follows by taking a common convergence time for the
finite band. For the reverse implication, a nonconvergent component contains
a positive unit target. Choose one of its arbitrarily high witness octaves
with `d >= d_0` and `gamma(d+1) >= 1`; then (7.1) contradicts (7.2).
The same argument permits any fixed power strictly larger than two.

The quantifier `for all sufficiently large d` in (7.2) is essential to this
derivation. An arbitrary unbounded subsequence of passing octaves need not
intersect the target-dependent witness subsequence. No such weaker
quantifier is claimed.

## 8. Exact remaining obligation

The forward visit theorem makes this section unavoidable. The new theorem
shows that each supplied ordinary unit component occupies a near-linear
number of actual points in this same section along unbounded octaves,
with only a squared logarithm lost and with equal ordinary clocks.

What remains is an unconditional **upper** estimate on the surviving points,
such as (7.2), or an independent argument forcing marked return descent.
Neither the global density-zero bound on the section nor the predecessor
lower bound gives that upper estimate. The initial universal-convergence
claim is therefore still open at this checkpoint.
