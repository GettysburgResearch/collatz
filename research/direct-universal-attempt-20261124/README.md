# Direct attempts at the universal step

**No universal proof was obtained.** This follow-up to
[`4f226f3b278ffe4559110a6ca952ff4a7c56ceba`](https://github.com/GettysburgResearch/collatz/commit/4f226f3b278ffe4559110a6ca952ff4a7c56ceba)
responds to the request to work through the central difficulty. Three
GPT-6.2 Astra streams were directed at the missing universal conclusions,
while the coordinator tried to restore the rational poles in the
negative-center construction. The outcomes below are recorded as
unsuccessful closing attempts. They are not additional claims of a
Collatz solution or a count of newly formalized theorems.

The preceding [checked packet](../high-variance-closure-20261124/ordinary-arithmetic/README.md)
and its 11 new Lean declaration audits are unchanged. This follow-up adds
no Lean source and claims no new Lean verification.

## 1. Producing an actual arithmetic companion

The target was the missing existential statement: for each fixed positive
ordinary `n`, construct integers `A` and `h>=0` such that
`D(n)=A/3^h`. The previous finite comparison theorem can reject or confirm
a supplied candidate; it cannot create a successful one.

The arithmetic stream tried two constructions. The substitution of parity
words `0 -> 1, 1 -> 01` identifies the transformed binary Collatz source
with `-1-D(n)`. To use it, however, one must prove that this transformation
takes the ordinary positive source to a rational with denominator a
power of three. Binary convergence of the transformed source supplies no
such arithmetic inheritance.

The second construction used record-high physical endpoints. The actual
prefix estimates give bounded real terminal compensation at those
clocks. To make the auxiliary coordinate an ordinary integral lift also
requires a particular congruence modulo `3^k`. The original physical
endpoint equation involves `3^(P_k)` and a different carry. No argument
was found that puts the required ternary lift in the bounded real window,
or gives a substitute with bounded denominator. Approximating `n` by
already convergent sources produces compatible dyadic approximations,
but their rational heights need not remain bounded.

**Unproved step:** an actual successful candidate for every fixed `n`,
or a finite bound on the height of such a candidate. Universal arithmetic
membership has not been established.

## 2. Paying the complete accumulated descent bill

The descent stream kept the same fixed hypothetical escaping orbit
`X_i=T^i(x)` and the signed ancestor price `P_i=R†(X_i)`. Put

\[
 v_i=v(X_i),\quad Y_N=\sum_{i<N}v_i,\quad
 c_i=v_i(1-3\mathbf1_{M_1}(X_i)),\quad
 S_N=\sum_{i<N}c_i,\quad d_i=P_i+c_i-P_{i+1}\ge0.
\]

The preceding written weighted separation and origin-count arguments give
`S_N >= Y_N/10-C_0`, `Y_N -> infinity`, and only
`O_x((1+Y_N)^(1-epsilon))` strict discount dates. Consequently the actual
gross increases of the price on unmarked edges are at least

\[
 \sum_{\substack{i<N\\X_i\notin M_1}}(P_{i+1}-P_i)_+
 \ \ge\ \frac7{10}Y_N-O_x((1+Y_N)^{1-\epsilon})-C_0/3.
\]

Indeed, away from a strict discount the unmarked increase is exactly
`v_i`. At a discount date its shortfall from `v_i` is at most `sup v`.
The marked mass is at most `3Y_N/10+C_0/3`. Thus the full unmarked bill
diverges on such an orbit; its small individual allowances do not become
summable. This calculation uses the actual minimizing price, not just
an upper allowance on its increases.

For the net bill, take each ordinary origin `m` whose path first enters
this fixed forward orbit at `X_(t_m)`. Let `C_m` be its signed path cost
before that entry and `A(m)=m+4G(m)`. Exact splitting at the first entry
gives

\[
 P_N=S_N+\min_{t_m\le N}\{A(m)+C_m-S_{t_m}\},
 \qquad
 \sum_{i<N}d_i=P_0+\max_{t_m\le N}\{S_{t_m}-A(m)-C_m\}.
\]

The size of the cumulative discount is therefore the size of this record
over actual incoming paths. Counting record dates does not give a lower
bound on the record. Clearing both full affine path equations retains
their different positive carries and yields no saving in the required
direction. Likewise, a merger obtainable after changing the lower
source does not supply a merger from this prescribed `x`.

**Unproved step:** at arbitrarily late endpoints of this same orbit,
find incoming origins whose record comes within a fixed additive
constant of `S_N`, or produce another all-source mechanism that pays the
entire loss. Nonstandard positive cycles also remain to be excluded.

These displayed calculations are written consequences of
[RESET_EXIT](../high-variance-closure-20261124/ordinary-arithmetic/RESET_EXIT.md)
and [ORIGIN_BIAS](../high-variance-closure-20261124/ordinary-arithmetic/ORIGIN_BIAS.md),
not additional Lean-checked statements.

## 3. Keeping the original center in the component merger

The boundary stream tried to connect a positive center `b` to the
punctured sides in the terminal recurrence. Merging three perturbed
sources does not include `b` itself. Density of the ancestor set in
every binary cylinder allows the ancestor to vary and does not force
one of the prescribed terminal sources into that set.

A compactness attempt transported dyadic component boundaries by
tripling. The grid error tends to zero, but the newly produced boundaries
can start at successively deeper levels. This gives no fixed compact
set of persistent rays with the invariance needed for a global argument.
The `+1` sign and positive-source information cannot be replaced by
unsigned limiting geometry.

The latest long-block construction was then inspected in
[PR202 at `3b10b24d12d4b349cb20f4cbc83086c8a09f807e`](https://github.com/GettysburgResearch/collatz/blob/3b10b24d12d4b349cb20f4cbc83086c8a09f807e/research/synchronized-long-basin-blocks-20261124/README.md).
That written construction is explicitly conditional on its synchronization,
modular-routing and predecessor-density inputs; its Lean candidate was
reported uncompiled. Those inputs were not promoted to newly verified
theorems in this follow-up.

The attempted overlap with the literal dyadic center has an exact clock
problem. In PR202's equation (1), after its stated refinement, every member
of a synchronized block has the same **positive** odd count `p>=1`
through a common native clock `h`. A center `2^L b` with `L>=h` has
zero odd inputs through that clock. It cannot be a member of that block,
regardless of how closely the main real-scale terms align. Using a
different preimage of `b` avoids this elementary exclusion only by
requiring the routing to preserve the common future with `b`; the stated
modular router does not provide that additional target constraint.

**Unproved step:** a meeting with the original center's actual component,
or an argument excluding every remaining boundary. The long blocks do
not supply the missing fixed-floor certificate in each such block.

## 4. Restoring the missing rational poles

The coordinator extended the inverse-center trial from negative integers
to negative rationals, retaining both inverse maps `z -> 2z` and
`z -> (2z-1)/3` with weights `1/3` and `2/3`. This restores the poles
that the integer restriction had removed. It also removes the killing
that made the earlier Green measure finite: the unrestricted operator
preserves total mass at every generation, so its full Green occupation
has infinite total mass. Its nonnegative valuation kernel is at least
one and the corresponding unmodified Green potential diverges.

A different finite measure or a compensating normalization remains
possible. The real-negative support and the integrality of the positive
source do not, by themselves, bound the dyadic potential at that source:
the rational approximation denominators grow. No finite supersolution
valid for every ordinary source was constructed in this attempt.

## Outcome

The checked checkpoint is available, and the renewed direct attacks were
carried out. None supplies universal arithmetic membership, global
component merger, or a fully paid descent score. The mathematical status
is unchanged: **Collatz is not proved here.**
