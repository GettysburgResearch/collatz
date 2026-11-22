# Three precise questions for another proof attempt

These tasks can be sent independently with their definition files. They
state the missing mathematical assertions directly. Their consequences
are recorded here so that a successful proof cannot be confused with an
already supplied hypothesis. They are all **OPEN**.

## A. A shrinking-exponent bound for an explicit positive series

Define `x_0=p`, and, for positive integers,
`x_(L+1)=x_L/2` when `x_L` is even and `(3x_L+1)/2` otherwise.
Let `a_L` count odd inputs through time `L`,
`j(x)=min{j>=0:x<=3^j}`, and `tau(p)=inf{L:x_L=1}`.
For positive integers `t`, study the completely defined nonnegative sum

\[
\mathscr B_t=
\sum_{p>0\text{ odd}}\frac1{p^2}
\sum_{\substack{L<\tau(p)\\a_L-j(x_L)=t}}
\left(\frac{x_L}{3^{j(x_L)}}\right)^2x_L^{-1/t}.
\]

**Question:** prove `mathscr B_t->0`, or prove a quantitative bound that
implies this limit. A fixed positive endpoint exponent cannot replace
`1/t`.

Useful facts already supplied: each source has at most two visits in a
positive bin; `x_L+1<=3^(t+1)(p+1)^2` there; omitted odd sources `p>P`
contribute at most `1/P`; each finite-bin sum admits exact rational
enclosures by the provided integer-root algorithm. The source `p` must
not be resampled when the bin changes.

This is self-contained apart from elementary convergence of the reciprocal
square series. A proof of the requested limit would settle full Collatz
by the retained-source argument in `MOVING_TILT_WINDOW.md`. None of the
available fixed-exponent estimates proves it.

## B. Canonical weight on a sparse first-hit boundary

Use `P`, `G`, and the ordinary canonical inputs exactly as specified in
`SPARSE_BOUNDARY_MASS.md`. For `q` in its nonperiodic odd-unit domain,
put `H(q)=2^floor(log_3 q)`. A boundary integer `n<H(q)` must move
above that floor immediately, stay there, and first hit `q`; let
`omega_q(n)=3^s/2^A` be its actual coefficient. Set

\[
\mathcal K(q)=\sum_{n\in E_{H(q)}(q)}\omega_q(n)G(n).
\]

**Question:** prove `mathcal K(q)=o(q)` on that ordinary domain, using
the actual canonical `G`. It is enough to control this particular sparse
boundary rather than every inverse word.

Already available: the entire unweighted kernel is
`O(q^(1-(log_3 2)/20))`, with no clock or valuation cutoff;
`K(q)<=G(q)`; and finite positive superlevels of `V(q)/q` have the
pinned global finite-forward-orbit cover. The first unsupported step is
control of the arriving `G(n)` values. An escaping fixed source would
force one boundary atom to contribute at least `delta^2 nu(p) q`.

Under the pinned analytic inputs this question excludes every escaping
orbit; additional cycles remain a separate obligation. Replacing `G(n)`
by one or by a newly normalized source weight is not the requested theorem.

## C. Complete the exact failed half while retaining its source

Retain one supplied complete positive odd source word beginning with gap
three:

\[
3q+1=8u,\quad u\text{ odd},\quad n=8q-1,\quad
9u-1=2^h r,\quad h\ge1,\quad r\text{ odd}.
\]

The only unresolved half of the new dichotomy has

\[
3^{h+1}r=4z+1,\qquad
T^{h+8}n=9z+2,\qquad
T^{h+3}(18u-3)=z,
\]

with `0<18u-3<n`. The smaller-target hypothesis proves `Basin z`.
The original source constraints also give

\[
27q+1=8\cdot2^h r,\qquad
27n+35=64\cdot2^h r.
\]

**Question:** find a universal actual merger or a lower-grade literal-tail
handoff for `9z+2` under precisely this supplied-source configuration.
An arbitrary new certificate extracted from `Basin z` has no proved grade
bound. For `h>=3`, `z>n`, so numerical target induction at `z` cannot
be invoked directly either.

The successful half and the entire `[3,3]` source-prefix family are already
proved; do not spend the attempt reproving them. A solution of this task
would finish this psi head, not automatically every target in the larger
active interval. The universal `MixedCover` obligation remains the exact
interface for completing that broader induction.
