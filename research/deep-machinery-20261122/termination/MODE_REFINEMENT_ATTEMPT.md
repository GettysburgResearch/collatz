# A direct termination attempt through arbitrary mode switches

**22 November 2026. Status: a failed global closing attempt, with an exact
all-parameter obstruction to bounded repayment by the existing rank.**

No Collatz proof or Lean termination certificate is claimed. This note tests
whether the repository's existing unbounded periodic-corridor acceleration can
be completed by size-change termination or by finite-depth mode refinement.
It does not present a new favorable residue family as universal coverage.

The main calculation concerns **every** pair of parameters `b >= 3`, `K >= 1`.
It constructs a positive ordinary history with `K` alternating maximal mode
pairs `(2,1),(b,1)`. Starting at the first unsafe mode, the existing common
rank has no strict decrease below its starting value for `2K-1` maximal
modules. A new pair counter repairs each pair, but the globally well-founded
organization of arbitrary such repairs is not obtained.

## 1. The exact literature bridges being attempted

The primary papers supply precise interfaces, not the missing Collatz
invariant:

* Yolcu, Aaronson and Heule, [*An Automated Approach to the Collatz
  Conjecture*](https://emreyolcu.com/research/rewriting-collatz.pdf),
  Section 3.2 and Theorem 3.17, give an eleven-rule mixed binary/ternary
  string system whose termination is equivalent to Collatz. Its value-
  preserving carry subsystem terminates separately; the complete dynamic
  boundary system is the unresolved part. The unary matrix-interpretation
  obstruction in Theorem 3.10 is not an obstruction to every mixed-base
  interpretation.
* Ben-Amram, [*Size-Change Termination, Monotonicity Constraints and Ranking
  Functions*](https://lmcs.episciences.org/1001/pdf), Theorem 4.12 and
  Algorithm 4.13, require every cyclic constraint in the finite composition
  closure to pass the local termination test: a strict descending cycle
  which is forward or balanced in the circular graph. The variables range
  over a well-founded domain. Merely obtaining finitely many control states
  does not establish that condition.
* Finkel and Schnoebelen, [*Well-Structured Transition Systems
  Everywhere!*](https://www.cmi.ac.in/~madhavan/courses/concurrency2017/literature/finkel-schnoebelen-wsts.pdf),
  Definition 4.4 and Proposition 4.5, require **transitive compatibility**
  for the self-covering-path termination argument. Theorem 4.6 also requires
  decidable order and effective successors. Higman's word ordering alone
  supplies none of the transition compatibility.

For the last point, even normalized binary strings give a concrete failure.
With the leading `1` and final boundary retained, the binary suffix for 3 is
`1`, and that for 5 is `01`; the former embeds as a subsequence of the latter.
The shortcut step sends 3 to 5. But the strictly positive future of 5,
`8,4,2,1`, has suffixes `000,00,0,empty`, none containing `01`. Thus the
nonempty simulation required by transitive compatibility fails already on
these valid positive states. Allowing a zero-step simulation does not repair
the termination theorem's hypothesis.

## 2. Existing definitions, kept unchanged

Use the existing
[moving-corridor definitions](../../astra-three-routes/pass4/MOVING_GHOST_RANK.md):

\[
 w_a=1^a0,\qquad
 g_a(n)=\frac{3^a n+3^a-2^a}{2^{a+1}},\qquad
 z_a(n)=(3^a-2^{a+1})n+3^a-2^a.
\]

For a positive odd `n`, its active mode is `a=v_2(n+1)`; even inputs have
mode zero. The acceleration `A` executes the maximal number `k` of copies
of the physical word `w_a`. The existing proper integer envelope is

\[
 R_*(n)=\min_{a\ge0}\frac{z_a(n)^2}{3^{v_3(z_a(n))}},
\]

with the zero convention at a zero numerator. We use the existing finite
envelope formula: its candidates are `a=0,1,2`, together with
`a=h=v_3(2n+1)` when `h>=3`. These parent statements retain their stated
paper-level status; this note does not change their proof receipt.
For the new family, Section 3 also compares every index directly, so its
asserted rank values do not depend solely on that general envelope formula.

The old one-mode corridors `w_a^k` and their counters are **not new here**.
The following calculation begins at the subsequent mode-switch obligation.

## 3. A universal family of adverse mode switches

Fix `b>=3`, and abbreviate

\[
 X=3^b,\quad Y=2^b,\quad
 D=9X-16Y>0,\quad B=13X-8Y>0.
\]

The two-mode return is

\[
 H_b=g_b\circ g_2,\qquad
 H_b(n)=\frac{9Xn+B}{16Y}.
 \tag{1}
\]

Its rational fixed point and its intermediate point are

\[
 r=-\frac B D,\qquad s=g_2(r)=-\frac{9X+Y}{D}.
 \tag{2}
\]

These rational points are used only to specify finite congruences. In
particular, they are not positive ordinary infinite orbits.

Their exact dyadic modes are

\[
 r+1=-\frac{4(X+2Y)}D,\qquad
 s+1=-\frac{17Y}D,
\]

so `v_2(r+1)=2` and `v_2(s+1)=b`. The word at `r` is therefore
`w_2 w_b`, and each of its two maximal constant-mode corridors has exactly
one copy. The relevant ternary valuations are

| quantity | at `r` | at `s` |
|---|---:|---:|
| `v_3(n)` | 0 | 0 |
| `v_3(n-1)` | 1 | 1 |
| `v_3(2n+1)` | b | 2 |
| `v_3(n+5)` | 2 | 4 |

In addition, `v_3(z_b(r))=b+2`. The identities proving the nontrivial
entries are

\[
\begin{aligned}
 2r+1&=-17X/D,&2s+1&=-9(X+2Y)/D,\\
 r+5&=8(4X-9Y)/D,&s+5&=9(4X-9Y)/D,\\
 z_b(r)&=X(9Y-4X)/D.
\end{aligned}
\tag{3}
\]

Since `b>=3`, `v_3(4X-9Y)=2`.

### Positive ordinary realization, with all quantifiers retained

For **every** `K>=1`, choose any integer `n_0>=10` such that

\[
 Dn_0+B\equiv0
 \pmod{2^{(b+4)K+4}\,3^{b+3}}.
 \tag{4}
\]

The coefficient `D` is coprime to 6, so (4) has infinitely many positive
ordinary solutions. Set `n_j=H_b^j(n_0)` and `y_j=g_2(n_j)`.
For `0<=j<K`, all these are positive ordinary integers and

\[
 A(n_j)=y_j,\qquad A(y_j)=n_{j+1},
\]

with exact maximal mode/count pairs `(2,1)` and `(b,1)`.

To prove the finite-word claim directly, `n_0-r` has dyadic valuation at
least `(b+4)K+4`. One application of `H_b` lowers that valuation by
`b+4`; the intermediate `g_2` lowers it by three. Thus the actual finite
states stay sufficiently close to `r` and `s` to retain respectively
the exact active modes 2 and b, including the final next mode 2.
The two distinct successive modes certify maximal repetition count one.
Every branch of each finite word is therefore the ordinary shortcut branch,
not just an integral value of a rational affine formula.

The initial ternary precision is at least `b+3`. Under `H_b` it increases
by `b+2`, and under the intermediate `g_2` it increases by two. Hence all
valuations in (3) persist along the entire finite history.

Every block increases ordinary size: `g_2(x)>x` and `g_b(x)>x` for positive
`x`. Its odd steps increase, and its final even step ends above the block's
starting value. Consequently the full shortcut history also has no descent
below its initial ordinary value through these blocks.

### Exact values of the existing common rank

At every pair boundary, the finite-envelope candidates are

\[
 n^2,\quad (n-1)^2/3,\quad (n+5)^2/9,
 \quad z_b(n)^2/3^{b+2}.
\]

For `n>=10` the third is strictly smallest. Its comparison with the first
two is elementary. For the last candidate, `z_3(n)>6(n+5)` for `n>=3`,
and `z_{a+1}(n)>3z_a(n)` for `a>=3`. Therefore
`z_b(n)^2 > 3^b(n+5)^2` for every `b>=3`, which is the needed comparison.
At `y_j`, the candidates are only
`y_j^2`, `(y_j-1)^2/3`, `(y_j+5)^2/81`, with the last strictly smallest.

The infinite dictionary can also be compared directly here. At `n_j`,
`v_3(n_j+1)=0` and `v_3(2n_j+1)=b`, so for `a!=b` the identity
`z_a(n)=3^a(n+1)-2^a(2n+1)` gives `v_3(z_a(n))=min(a,b)`.
For `a>2`, the recurrence gives `z_a(n)>3^(a-2)z_2(n)`.
Consequently `R_a/R_2>3^(a-2)>1` when `2<a<b`, and
`R_a/R_2>3^(2a-b-2)>1` when `a>b`. The exceptional index `a=b`
was compared above. At `y_j`, `v_3(y_j+1)=0` and `h=2`; every `a>2`
has `v_3(z_a(y_j))=2`, while `v_3(z_2(y_j))=4` and its numerator
is smaller. Thus these indices also exceed `R_2`. The comparisons
with indices zero and one were already made. This proves directly that

\[
 \boxed{R_*(n_j)=(n_j+5)^2/9,\qquad
        R_*(y_j)=(y_j+5)^2/81.}
 \tag{5}
\]

The first module contracts this same rank by exactly `9/64`, since
`g_2(n)+5=(9/8)(n+5)`. Nevertheless,

\[
 R_*(n_{j+1})>R_*(n_j),\qquad
 R_*(y_{j+1})>R_*(y_j).
 \tag{6}
\]

In particular, start at the unsafe state `y_0`, not at the preceding
aligned state `n_0`. For all `1<=ell<=2K-1`,

\[
 \boxed{R_*(A^\ell(y_0))>R_*(y_0).}
 \tag{7}
\]

For even `ell`, use the second inequality in (6); for odd `ell`, use
`R_*(n_{j+1})>R_*(n_j)=(64/9)R_*(y_j)`. Thus **no fixed number of maximal
mode switches guarantees repayment for this rank**. This statement does
not exclude a nonuniform, correctly proved repayment theorem.

For `b=3,K=2`, one concrete source in (4) is `n_0=94720603`.
Its four maximal modules end at `n_2=341379211`, with pair-boundary ranks
`996888175543296` and `12948863235197184`. Starting at `y_0` gives the
three-module failure of repayment asserted by (7). The accompanying
fixture records the intermediate ordinary values and checks the literal
shortcut words independently of (1).

## 4. The constructive repair, and where refinement still stops

For this pair, define

\[
 Z_b(n)=Dn+B.
\]

Then the **exact** transport equation is

\[
 Z_b(H_b(n))=\frac{3^{b+2}}{2^{b+4}}Z_b(n).
 \tag{8}
\]

Accordingly `v_2(Z_b(n))` decreases by `b+4` on each legal pair return.
The integer component `Z_b(n)^2/3^{v_3(Z_b(n))}` also contracts by
`3^(b+2)/2^(2b+8) < 1`. These are real repairs of the periodic pair;
the example is not an impossibility theorem for all refinements.

The roots in (2) are distinct as `b` varies: writing `t=(2/3)^b`, they
are `-(13-8t)/(9-16t)`, a strictly varying function on this parameter
range. None is a one-mode root. Each has active mode 2, while the
one-mode root of mode 2 is -5, outside their range. A fixed list of
one-mode counters therefore does not already contain this repair.

A moving index can encode the whole new pair family too. The unresolved
step is **not** merely to add these counters. For a general finite
physical word `w` of length `L`, odd count `o`, and correction `C_w`,
the analogous counter has numerator

\[
 Z_w(n)=(3^o-2^L)n+C_w
       =2^L(T^L(n)-n).
 \tag{9}
\]

Changing the selected word can replenish its dyadic precision:
`v_2(Z_w(n))=L+v_2(T^L(n)-n)` whenever the difference is nonzero.
The exact decrement for repeating one selected word supplies no decrement
when a new word is selected. I did not establish a source-history invariant
or a well-founded order paying for those changes. Applying size-change
termination before proving that condition would assume the desired result.

## 5. Scope relative to the current joint source/target program

These are all-positive, physically legal **target** histories, with complete
finite parity proofs. They are stronger than rational shadows considered
without ordinary realization. They are not asserted to form one infinite
ordinary orbit: the initial integer in (4) depends on `K`.

They also do not prove that the same pattern occurs in the restricted
terminal residual histories selected by a least-grade/maximal complete
bounded-four source. The repository's source-floor theorem supplies a
complete source for each large target, but that existential coverage does
not fix its certificate length, grade, or terminal alignment in this family.
Those extra variables could carry information absent from the target rank.
No no-go theorem for the full joint-source program is inferred here.

The direct global termination attempt remains incomplete. The substantive
outcome is the quantified test (7), its exact repair (8), and the unproved
refinement accounting identified by (9), rather than a claim that a named
termination theorem automatically completes Collatz.

## Reproduction

Run `python check_mode_refinement.py` in this directory. The checker writes
`mode-refinement-fixture.json`, checks multiple parameter pairs and every
literal shortcut step, and uses explicit exceptions on failures. The
all-parameter conclusion is the algebra above; the finite fixture is a
reproducibility aid, not its proof. The fixture evaluates the parent
finite-envelope formula and does not independently reprove that general
formula; the proof above separately compares all indices on this family.
