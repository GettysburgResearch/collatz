# Residual cycle denominators and the critical collision estimate

**2026-11-23. A uniform polynomial lower bound for every nontrivial primitive
positive residual denominator, a stronger actual-orbit collision bound,
and 21 public finite-algebra theorems in Lean. Collatz remains open.**

This continuation addresses the two central obligations in the preceding
[rigidity checkpoint](../rigidity-closing-20261122/README.md): complete cycle
denominator divisibility and arithmetic branching for the same ordinary
source. It refreshes PR175, PR176, PR177, PR178 and PR180 before extending
the arguments. The exact heads and inspected file hashes are in
[the source snapshot](SOURCE_SNAPSHOT.json) and [file inventory](SOURCE_FILES.json).

## 1. The principal factor cannot disappear

For a parity word of shortcut length `A`, with `p` odd positions
`0 <= d_0 < ... < d_(p-1) < A`, set

\[
F(X)=X^p-2^A,\qquad Q(X)=\sum_{i<p}2^{d_i}X^{p-1-i}.
\]

Let `G` be the monic polynomial gcd, `F_0=F/G`, `Q_0=Q/G`, and
`D_pol=|F_0(3)|`. Write `A=ga`, `p=gb`, `g=gcd(A,p)`.
For every positive candidate, `2^A>3^p`, the new theorem gives

\[
\boxed{X^b-2^a\mid F_0(X)},\qquad
\boxed{2^a-3^b\mid D_{\rm pol}}.
\]

The reason is positivity at the actual positive root: the principal binomial
is irreducible, and `Q(2^(a/b))>0`. That whole factor survives every allowed
polynomial cancellation.

This yields the exact global classification

\[
\boxed{D_{\rm pol}=1
\iff A=2p\ \text{and}\ d_i=2i+\epsilon\ (\epsilon=0\text{ or }1).}
\]

These are repetitions of the two phases of `1 -> 2 -> 1` under the shortcut
map. The `D_pol=1` exception left open in the previous checkpoint is removed
for **every nontrivial word**, without a word-length cutoff. More generally,
`F_0=X^b-2^a` holds exactly for `g` repetitions of one length-`a` block.
A primitive word with `g>1` therefore has `deg F_0 >= 2b`.

There is also a global restriction on how much cancellation a primitive
word can sustain. Writing `d=deg F_0`, a finite Fourier argument followed
by a count of full cyclotomic conjugacy classes proves

\[
\boxed{g\le3^{d-b},\qquad p\le3^{d-1}.}
\]

Thus `d >= 1+log_3 p` for every primitive parity word. The
[degree proof](PRIMITIVE_RESIDUAL_DEGREE.md) retains the original binary
word and proves the wraparound period step.

An all-factor estimate converts this degree restriction to a genuine
integer evaluation bound. For every primitive positive word other than
the two trivial length-two words,

\[
\boxed{D_{\rm pol}>(3/2)^{d-1}\ge p^{\log_3(3/2)}.}
\]

The fixed exponent is approximately `0.3690702464`. Away from `A=2p`,
the stronger bound `D_pol>(3/2)^d` holds. The
[complete growth proof](PRIMITIVE_DENOMINATOR_GROWTH.md) combines factor
symmetry, an explicit Matveev/continued-fraction gap argument, and a
cyclotomic calculation covering the exceptional slope `A=2p`.
This is a polynomial lower bound after all polynomial cancellation.
It does **not** lower-bound the denominator after further cancellation
by the integer gcd `gcd(D_pol,Q_0(3))`.

[Complete elementary proof](RESIDUAL_UNIT_EXCLUSION.md) ·
[Independent review](reviews/RESIDUAL_WORD_REVIEW.md) ·
[Lean polynomial-to-word bridge](lean/ResidualWord.lean).

The full cycle condition is still `D_pol | Q_0(3)`. The new principal
factor alone does not contradict it. An [unbounded exact rational control
family](PRINCIPAL_FIBER_CONTROL.md) has primitive words, polynomial gcd one,
every cyclic state above `19/10`, and its whole principal divisor absorbed
at the correct integer evaluation. The other factors must be addressed
simultaneously. These controls are explicitly nonintegral.

## 2. A square-root gain at the critical collision exponent

Let `q_j` be the odd iterates of one fixed positive ordinary source, and
`g_j` its actual positive valuation gaps. A word of `m` gaps has cost
`S=g_1+...+g_m`. The exact finite identity

\[
\sum_{s=m}^{K-1}(K-s)^2\binom{s-1}{m-1}
=\binom K{m+1}+2\binom K{m+2}
\]

and Cauchy's inequality show that any finite word law of mean cost at most
`B<K` has collision sum at least

\[
\frac{(K-B)^2}{\binom K{m+1}+2\binom K{m+2}}.
\]

The actual past word determines its endpoint modulo `3^m`. Applying this
bound to the original time windows, then to the **same ordinary inverse
laws** `zeta_(M,r)` from the preceding checkpoint, gives

\[
\boxed{
\inf_{r\ge0}\operatorname{Col}_m(\zeta_{M,r})
\ge c\sqrt m\,3^{-\theta m},\qquad m^2\le TM,
}
\]

for each fixed `T>0`, all sufficiently large `M`, and a positive constant
depending on the fixed source, `T` and its harmonic flow. Here

\[
\theta=\frac{\Phi(\log_2 3)}{\log3}
=0.949955527188\ldots,
\qquad \Phi(u)=u\log u-(u-1)\log(u-1).
\]

The transfer uses the exact pointwise domination
`zeta_(M,r) >= (v_0/C) pi_M`. It retains every finite inverse clock and
needs no rate for a total-variation error. The source-qualified harmonic
flow is used only for this transfer; the finite ordinary-orbit collision
bound itself is unconditional.

**What this changes in the closing problem.** A same-law upper estimate
`Col_m(zeta_(M,r)) = O(3^(-theta*m))` along increasing admissible
precisions would now contradict the lower bound. The earlier requirement
of a strictly better exponential rate `theta+delta` is unnecessary.
This critical upper estimate is still unproved.

[Full finite formula, proof and quantifiers](COLLISION_LOGARITHMIC_GAIN.md) ·
[Lean finite composition and Cauchy core](lean/DistinctWordBudget.lean).

The same argument also gives an unconditional bound for every contiguous
injective ordinary odd segment of height at most `H-1`:

\[
\boxed{N+1\le C_1 H^\theta/\sqrt{\log H}}.
\]

It applies with the same absolute constant to every shifted window. It is
not a bound for total visits below `H` separated by high excursions.

## 3. Literature and the remaining ordinary-source step

The new [predecessor-density comparison](PIN_DENSITY_GAP.md) checks
rStation Paper202/v1 against the repository's fixed-escape question.
The paper's arbitrarily small relative gains occur in a family whose
density must decay at least as a power of its height. Its endpoint
selection also deletes the late points of any fixed escape, because those
points retain a small fixed ancestor. Consequently its bypass estimate
cannot be transferred to the retained escape mass at the claimed error.
The exact failed line and the still-open positive-density gain target are
recorded in the note. Its external analytic inputs remain source-qualified.

The denominator-growth proof uses the real two-logarithm case of the
standard Matveev theorem, as stated in Bugeaud--Mignotte--Siksek,
Theorem 9.4. Its [exact rational certificate](certificates/check_factor_growth_gap.py)
covers all continued-fraction candidates below the proved cutoff and
the complete infinite tail argument is written out. The elementary
principal factor and unit classification do **not** depend on that
analytic theorem.

No GRH assumption is used in any new argument. No new implication from GRH
to either remaining closing estimate has been established.

## 4. Formal scope and replay

The two new Mathlib-only modules contain **21 public theorem audits**:
12 in `ResidualWord.lean` and nine in `DistinctWordBudget.lean`.
They have no local theorem imports, custom axioms, `sorry`, or native proof
shortcuts. The exact formal boundary is in [FORMALIZATION.md](FORMALIZATION.md).
Written dependencies are pinned in [DEPENDENCIES.json](DEPENDENCIES.json);
the inherited proof modules are not recompiled or counted as new work.

From a clean, complete checkout, with the pinned runtimes already installed:

```bash
python -X utf8 -B research/central-closure-20261123/check.py \
  --lean /absolute/path/to/lean-4.34.1-linux/bin/lean \
  --mathlib /absolute/path/to/mathlib \
  --build-dir /absolute/path/outside/checkout/central-build
```

The checker compiles both unchanged sources, checks every public axiom list,
runs the three small exact arithmetic controls in normal and optimized
Python modes, and runs `python -X utf8 -B tools/validate.py`. Generated
sources, compiler artifacts and logs remain outside the checkout. Exact
published execution receipts belong in `reports/central-closure-20261123/`.

The decisive remaining work is the simultaneous integer divisibility
estimate for nontrivial cycle words, or a critical collision upper estimate
for the same actual source laws. The present results sharpen those targets
and eliminate the unit exception; they do not assert either closing step.
