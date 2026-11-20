# Uniform cycle bounds from shifted multiplicative rank

**SOURCE-QUALIFIED proposed theorem.** This note gives an effective finite
decision for positive cycles whose shifted values lie in a bounded number
of cosets of a multiplicative group of bounded rank. Neither the group's
generators, their heights, their prime supports, nor the coset
representatives are bounded in advance. It does not exclude every cycle
or prove Collatz.

The addition to the inspected repository is the rank-only defect bound
and its composition with classical cycle finiteness. The shifted defect
equation is from PR161. Finiteness of cycles with a fixed number of local
minima is classical, including the quantitative work of Simons and de
Weger. We reconstruct a deliberately coarse version to make the whole
new interface explicit; no improvement to the classical cycle bounds is
claimed.

## Sources and notation

Use the actual positive odd map

\[
U(n)=\frac{3n+1}{2^{a(n)}},\qquad a(n)=v_2(3n+1),
\qquad m=n+1.
\]

A **defect** is an edge with `a>=2`. Multiplicative rank is the rank of
a subgroup of the positive rationals, equivalently the rational rank of
its prime-valuation vectors. A rank-one generator may involve arbitrarily
many different primes.

The following sources were read at these exact identities:

* PR161, `4a0536b587fc91ee0c7bb1b160c06dda16ddbf23`,
  `research/source-rigidity-20261120/SHIFTED_CORE_TRANSITIONS.md`,
  SC1--SC3 and equations (14)--(18). That note proves a uniform count for
  prescribed shifted core pairs using a **prime-pool** parameter. It
  explicitly does not obtain a rank-only bound for arbitrary rational
  generators. Its three-term equation and nondegeneracy argument are
  reused with a different external theorem below.
* PR163, `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`,
  `research/deep-reverse-closure-20261120/SHIFTED_SMOOTH_COMPLETE.md`,
  supplies the same precise Lagarias two-logarithm estimate used here.
  Its special `{2,3}` classification is not assumed in the proof.
* PR166, `5996b9f525ca50978bc34f423192c36a87765bf3`,
  `research/grh-certificate-closure-20261120/UNIFORM_J_COMPLETION_ATTEMPT.md`,
  section 5, already applies general-rank unit equations to bounded-depth
  inverse certificates. The variables and conclusion below concern
  shifted **forward** transitions and complete cycles instead.
* Simons and de Weger, *Theoretical and computational bounds for m-cycles
  of the 3n+1-problem*, author-hosted version 1.44 (31 August 2010),
  sections 1.1 and 6.1, especially Lemma 14 and the following finiteness
  conclusion. [Primary PDF](https://math.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.44%5B2010%5D.pdf).
  Their quantitative bounds are much sharper than the coarse block bound
  reconstructed here. Our defect count equals the number of alternating
  odd-increase/even-decrease blocks in their shortcut normalization.
* The unshifted multiplicative-rank bounds in [rStation Paper 138, v1,
  13 November 2026](https://rstation.ai/problems/collatz/papers/138),
  Theorems 1--3, are prior work. They apply to the odd states `n_i`.
  The rank below is that of `n_i+1`, or of their ratios inside assigned
  cosets. Neither is silently identified with unshifted rank. No broad
  literature-priority claim is made.

### External theorem ESS

Evertse, Schlickewei and Schmidt, *Linear equations in variables which lie
in a multiplicative group*, Annals of Mathematics 155 (2002), 807--836,
Theorem 1.1, equation (1.2), printed page 808, states that

\[
c_1u_1+\cdots+c_tu_t=1,\qquad (u_1,\ldots,u_t)\in\Gamma
\]

has at most `exp((6t)^(3t)(R+1))` nondegenerate solutions when `Gamma` has
rank `R` and the nonzero coefficients are fixed, in characteristic zero.
Nondegenerate means that no nonempty subsum vanishes. The bound is uniform
in the coefficients and the group. We use it inside the algebraic closure
of the rationals. The theorem and formula were checked in the primary
text and page image; no proof-assistant rebuild is claimed.

[Journal record](https://annals.math.princeton.edu/2002/155-3/p04) ·
[Primary paper](https://arxiv.org/pdf/math/0409604).

For integer `r>=0` use the convenient **integer** bound

\[
B(r)=2^{4\cdot18^9(r+1)}.
\tag{1}
\]

It exceeds `exp(18^9(2r+2))`, since `e<4`. Its enormous size is
intentional; the purpose is a completely computable rank-only ceiling.

## SRC-001. A rank-only bound for shifted defect transitions

Let `G` be any multiplicative subgroup of the positive rationals of rank
at most `r`, and let `c_1,...,c_k` be any fixed positive rationals, `k>=1`.
There are at most

\[
D(r,k)=k^2 B(r)
\tag{2}
\]

distinct positive ordinary defect edges `n -> U(n)` for which both
`n+1` and `U(n)+1` belong to the union of these `k` cosets of `G`.

**Proof.** Fix the two coset indices and write

\[
m=c_i u,\qquad m'=c_j v,\qquad u,v\in G,
\qquad b=a(n)-1\ge1.
\]

The actual shifted recurrence is

\[
2^b+\frac32 m-2^b m'=1.
\tag{3}
\]

The tuple `(2^b,u,2^b v)` lies in

\[
\Gamma=\{(2^z,g,2^z h):z\in\mathbb Z,\ g,h\in G\}.
\]

This group has rank at most `2r+1`: it is the image of the product of
one infinite cyclic group and two copies of `G`. If `G` is finitely
generated, explicit generators are `(2,1,2)`, `(1,g_l,1)` and
`(1,1,g_l)`. The rank statement also holds under the finite-rank
definition in ESS. The coefficients in (3) become `(1,3c_i/2,-c_j)`;
their heights and prime factors do not enter the ESS bound.

Write the three signed terms as `X,Y,Z`. Each is nonzero, and

\[
X+Y>0,\quad X+Z=2^b(1-m')<0,\quad Y+Z=1-2^b<0.
\]

Here `m'>=2` and `b>=1`. The full sum is one. Thus the solution is
nondegenerate. ESS with `t=3` gives at most
`exp(18^9(2r+2)) < B(r)` solutions for this ordered pair of cosets.
The encoding is injective: the first coordinate determines `b`, and
`c_i` times the second determines `n+1`. A source has only one actual
successor. Assign overlapping cosets deterministically, and sum over
the at most `k^2` ordered pairs. This proves (2). ∎

This is a count of **distinct ordinary edges**, not occurrences on an
indefinitely repeated cycle. It permits selecting one common group and
its cosets after an entire finite history is observed. It does not permit
a fresh unrelated group at every edge.

The defect restriction is essential. For all `h>=2`, the actual
exponent-one edges from `n=2^h-1` have shifted values
`m=2^h` and `m'=3*2^(h-1)`, both in the fixed rank-two group generated
by 2 and 3. There are infinitely many such edges. In (3), `b=0` makes
`Y+Z=0`, exactly violating the ESS hypothesis.

## SRC-002. Fixed-source deadlines and shifted rank growth

Fix an ordinary source `n_0`. If a simple prefix
`n_0,...,n_N` has all shifted values in a union as in SRC-001, then

\[
N<\ell\bigl(2^{D(r,k)+1}-1\bigr),
\qquad \ell=\lceil\log_2(n_0+1)\rceil.
\tag{4}
\]

This is the PR161 integer-clock argument with its defect count replaced
by SRC-001. For clarity, at any odd state there are exactly
`v_2(n+1)-1` consecutive exponent-one edges before the next defect.
The shifted value grows by at most a factor of two per odd step.
If `R_i` is the time just after the `i`th defect, `R_0=0`, then

\[
R_{i+1}\le2R_i+\ell,\qquad R_i\le\ell(2^i-1).
\]

If the prefix has `d` defects, its next one ends after time `N`, so
`N<R_(d+1)<=ell(2^(d+1)-1)`. Its edge sources are distinct and hence
`d<=D(r,k)`, proving (4). All endpoints through time `N` are included
in the multiplicative-cover hypothesis.

Consequently one fixed positive orbit eventually confined to one such
union must be eventually periodic. For a nonperiodic orbit let `r_N`
be the rank of the group generated by the shifted values in the whole
prefix and put `d_N=#{j<N:a(n_j)>=2}`. The sharper ESS bound gives

\[
\log\max(1,d_N)\le18^9(2r_N+2).
\tag{5}
\]

In particular the shifted rank tends to infinity. The elementary
fixed-source defect clock from PR161 makes `d_N` at least logarithmic
in `N`; (5) therefore gives a logarithm-of-logarithm lower bound for
`r_N`. No rate comparison with the stronger **unshifted** results in
Paper 138 is asserted.

## SRC-003. A coarse reconstruction of classical cycle finiteness

Let a positive odd cycle have least period `N`, minimum `mu`, and `d`
defects in one least period. Then `d>=1` and

\[
N<256d2^d,\qquad
\log_2\max_i(n_i+1)<256d2^d.
\tag{6}
\]

This is a coarse classical `m`-cycle bound, reconstructed here only to
give a convenient explicit interface. Its external input is Lagarias,
*Ternary Expansions of Powers of 2*, Lemma 2.2(1), equation (2.4),
printed page 10 in [arXiv version 4](https://arxiv.org/pdf/math/0512006):

\[
\left|\log_3 2-\frac pq\right|\ge\frac1{1200q^{14.3}}
\quad(q\ge1,\ p\in\mathbb Z).
\tag{7}
\]

That exact statement, also used in PR163, was checked in the primary
text and page image. It is derived there from classical logarithmic-form
bounds; it is not proved by the finite checker.

**Proof.** Start the cycle at its minimum, and write
`h=log_2(mu+1)`. Decompose one cycle into `d` blocks, each consisting
of consecutive exponent-one steps followed by one defect. If a block
starts at shifted value `m`, its length is exactly `sigma=v_2(m)`.
During its first `sigma-1` steps the shifted value is multiplied by
`3/2`. The final defect does not increase it. Hence every value during
that block is at most

\[
m(3/2)^{\sigma-1}\le m^{\log_2 3}<m^2.
\]

Applying this successively, the logarithm of the start of block `j`
is at most `2^j h`. Therefore

\[
N\le(2^d-1)h<2^d h,\qquad
\log_2\max_i(n_i+1)\le2^d h.
\tag{8}
\]

Put `A=sum_i a(n_i)`. Multiplying the actual odd-step equations around
the cycle gives

\[
0<\Lambda=A\log2-N\log3
=\sum_i\log\left(1+\frac1{3n_i}\right)
<\frac N{3\mu}.
\tag{9}
\]

Also `2^A=product_i(3+1/n_i)<=4^N`, so `A<=2N`.
Equation (7), with `(p,q)=(N,A)`, yields

\[
\Lambda\ge\frac{\log3}{1200A^{13.3}}
>\frac1{1200A^{14}}.
\]

Together with (9), this gives
`mu < 400 N A^14 <= 400*2^14 N^15`. Since
`400*2^14+1 < 2^23`, it follows that

\[
h<23+15\log_2N<23+15d+15\log_2h.
\tag{10}
\]

We claim `h<256d`. On `h>=256d`, the function
`h-15 log_2 h` is increasing: its derivative is
`1-15/(h log2)>0`, using `log2>1/2`. At `h=256d` use
`log_2 d<=d-1` for integer `d>=1` to get

\[
256d-15\log_2(256d)\ge241d-105>23+15d.
\]

This contradicts (10). Substitution in (8) proves (6). ∎

No cycle lower bound from numerical verification is used. The trivial
odd cycle `{1}` is included. For the shortcut map the complete period
has `A<=2N` steps and every even intermediate is below three times the
largest odd state plus one, so an equally explicit full-cycle bound
follows if needed.

## SRC-004. Effective compactness for shifted rank and cosets

For integers `r>=0,k>=1` define

\[
D=k^2 B(r),\qquad Q=256D2^D.
\tag{11}
\]

Every positive odd cycle whose shifted values lie in a union of `k`
cosets of some rank-at-most-`r` group satisfies

\[
\boxed{N<Q,\qquad n_i<2^Q\ \text{for every state}.}
\tag{12}
\]

The bound is uniform over **all** choices of that group and its
representatives. In particular it is uniform over all generators with
arbitrary sizes and arbitrarily many prime divisors.

**Proof.** Its least period has distinct edge sources. SRC-001 bounds
`d` by `D`; SRC-003 and monotonicity of `256d2^d` imply (12). ∎

Thus for fixed `r,k` there are finitely many such cycles in total,
including when neither the group nor the representatives are supplied.
One finite exhaustive decision procedure enumerates every odd start
below `2^Q`, follows its first `Q` odd steps, retains exact cycles, and
tests whether the shifted state set has such a rank/coset cover. This
last finite test is also effective: factor the finitely many shifted
integers, enumerate their partitions into at most `k` nonempty classes,
and compute the rational rank of the joint set of within-class
valuation differences. A partition qualifies precisely when that rank
is at most `r`; choose one representative per class and generate the
group by these ratios. Empty classes may be added if desired.

This procedure is fantastically impractical and has **not** been run.
The point is that a numerical ceiling exists before the primes or
generators are known. The number-of-solutions theorem is not being
misquoted as a height theorem: the cycle dynamics and (7) are the
additional bridge from a count of defects to a bound on height.

### An elementary exact rank-one boundary

A positive cycle whose shifted values have **absolute** multiplicative
rank one is necessarily the trivial cycle `{1}`. This small exclusion
uses neither external theorem.

Indeed a finite rank-one family of integers larger than one consists
of powers of one integer `b>=2`: take the primitive nonnegative integer
vector spanning their prime valuations. If the cycle had an
exponent-one edge, its shifted endpoints would have ratio `3/2`, hence
`3/2=b^z` for some integer `z`. Positive `z` gives an integer at least
two, negative `z` a reciprocal integer at most one half, and zero gives
one. All are impossible. Thus every edge is a defect. For every `n>1`,
such an edge has `U(n)<n`, excluding a cycle unless it contains 1.

The word **absolute** is essential: rank of all shifted values and rank
of their ratios can differ. In particular the shifted ratios along any
long exponent-one block have rank one, although those values need not
have absolute rank one. No assertion about all rank-one cosets follows
from this short argument.

## SRC-005. Why this does not supply a global rank ceiling

Even explicitly certified convergent sources have unbounded shifted
rank as a family. Here is a proof avoiding a census or conjectural
convergence.

Start with `q_0=1`. Given an odd ternary unit `q`, choose an inverse odd
step `x=(2^a q-1)/3` with `a>=2`, `x>q`, and `3` not dividing `x`.
Such a choice always exists among `a in {2,4,6}` when `q=1 mod3`, and
`a in {3,5,7}` when `q=2 mod3`: powers of four cycle through the three
classes `1,4,7 mod9`, so exactly one of the three integral quotients
is divisible by three. The sole possible equality `x=q` is `(q,a)=(1,2)`;
choose `(q,a)=(1,4)` there, obtaining 5. Every other admissible choice
is strictly larger. Define `q_(j+1)` by the least such choice.

Then `q_0<q_1<...`, every `U(q_(j+1))=q_j` is exact with valuation
`a>=2`, and `q_R` has a first-hit certificate of exactly `R` odd steps
to 1, all of them defects. Apply SRC-001 with `k=1` to the shifted
values on this finite certified path. If their multiplicative ranks
were bounded by one constant `r`, it would give `R<=B(r)` for every
`R`, a contradiction. The ranks therefore tend to infinity.

This uses changing certified sources `q_R`. It constructs no divergent
orbit and does not refute a rank bound depending on one fixed source.
It does refute a universal source-independent rank ceiling even on the
basin of 1. Thus neither the rank-only compactness theorem nor the
known unshifted support bounds can close Collatz by asserting a global
finite rank budget. A source-specific control of continued new rank,
or a different unrestricted descent, is still missing. Arbitrarily
high-rank positive cycles have not been excluded.

## Executable evidence

`check_shifted_rank.py` uses exact integer and rational arithmetic. It
reconstructs the shifted equation and every nondegeneracy sign, rejects
exponent-one and malformed inputs, checks the exact length and quadratic
height envelope of actual run/defect blocks, exercises finite
valuation-rank and coset-cover calculations, and builds the certified
inverse tower in SRC-005. It also checks the integer constants and
endpoint inequalities used in SRC-003.

Those executions verify the finite algebra and the implementation's
domain. They do not prove ESS, the logarithmic-form estimate, the
calculus argument for all real `h`, or universal Collatz convergence.
No all-cycle census or computation through the bound (12) is claimed.
