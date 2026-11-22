# The sparse boundary still carries a whole escaping source

**Status: new written synthesis, conditional only on the pinned canonical
potential/harmonic-flow inputs stated below.** The new all-depth counting
kernel has a separately audited Lean core. The canonical analytic inputs
and the present infinite-orbit deduction are not claimed as Lean theorems.

This note connects the first-crossing count with the actual ordinary
reference measure. It shows exactly what a putative escaping source would
force on the sparse boundary. Consequently the missing weighted estimate
has a specific test set and retains one fixed original source.

## 1. A sublinear coefficient kernel at every depth

For a target `q>=9`, put

\[
m(q)=\lfloor\log_3q\rfloor,\qquad H(q)=2^{m(q)}.
\]

Let `E_H(q)` consist of the positive boundary sources `n<H` which first
hit `q` after a positive shortcut clock `A_q(n)`, with all intermediate
positive-time states at least `H`. Use the actual coefficient

\[
\omega_q(n)=3^{\#\text{odd inputs through }A_q(n)}/2^{A_q(n)}.
\]

Each boundary integer is counted once, at its unique first hitting clock.
This is not a count of all earlier original histories and does not sum
extra circuits around a periodic target. The companion
`ALL_DEPTH_FIRST_CROSSING.md` proves

\[
\sum_{n\in E_{H(q)}(q)}\omega_q(n)
 =O\!\left(q^{1-(\log_3 2)/20}\right)=o(q).       \tag{1}
\]

The exponent is about `0.968454`. The proof allows all actual clocks and
all valuations; it uses the pinned finite native no-descent count after
charging each physical boundary source once.

## 2. Keep the actual canonical weights

Use the nonperiodic odd ternary-unit domain `N`, killed on first entering
any periodic state. Inherited source-qualified inputs give

\[
PG=G,\qquad h(q)=G(q)/q,\qquad L\nu=\nu,
\qquad \delta\nu(q)\le h(q)\le\nu(q),
\qquad\delta=e^{-200/3}>0.                       \tag{2}
\]

Here `P` uses the actual odd inverse coefficients `3/2^a`; `L` is ordinary
inverse counting on `N`. The reciprocal-packing estimate also gives

\[
\prod_{x\text{ on any distinct odd segment}}
       \frac{3x}{3x+1}\ge\delta.                 \tag{3}
\]

Define the finite weighted boundary kernel at `q in N` by

\[
\mathcal K(q)=
\sum_{n\in E_{H(q)}(q)\cap N}\omega_q(n)G(n).    \tag{4}
\]

The reversed words in (4) are prefix-free: each stops at its first state
below `H(q)`. Harmonicity and nonnegativity, unfolded only to the maximum
of this finite set of actual clocks, imply

\[
0\le\mathcal K(q)\le G(q)\le q\nu(q).           \tag{5}
\]

Thus no infinite optional-stopping theorem, unproved exit probability, or
replacement of `G(n)` by one is used in (5).

## 3. An escape forces a linear contribution from one boundary atom

Suppose one fixed positive odd unit `p` escapes, and write `q_i=U^i(p)`.
The states are distinct and tend to infinity. For all sufficiently large
`i`, `p<H(q_i)<=q_i`. Choose `n_i` to be the **last odd state below
`H(q_i)`** on the segment from `p` to `q_i`.

The next odd state and every later odd state through `q_i` are at least
the floor. Each intervening even run is at least its terminal odd state.
Therefore `n_i` belongs to the first-hit boundary in (4). There are no
repeated visits to `q_i` on an escaping orbit. In particular,

\[
\frac{2H(q_i)-1}{3}\le n_i<H(q_i),\qquad
n_i\longrightarrow\infty.                      \tag{6}
\]

The ordinary harmonic equation includes the actual forward edge, so
`nu(Ux)>=nu(x)` on this escaping component. The same **original** source
`p` therefore gives `nu(n_i)>=nu(p)>0`, independently of `i`. From (2),

\[
\boxed{G(n_i)\ge\delta\nu(p)n_i
 \ge\delta\nu(p)\frac{2H(q_i)-1}{3}.}           \tag{7}
\]

Let `f_seg` be the product in (3) on the actual segment `n_i -> q_i`.
Multiplying its ordinary edge identities gives

\[
\omega_{q_i}(n_i)=\frac{q_i}{n_i}f_{\rm seg}.
\]

Combining this with (3) and (7) proves

\[
\boxed{
\mathcal K(q_i)\ge\omega_{q_i}(n_i)G(n_i)
             \ge\delta^2\nu(p)q_i.
}                                                \tag{8}
\]

This is a positive linear lower bound from one retained original source.
The boundary location changes, but its mass is not reset to the fresh
weight `1/n_i`. Equation (1) remains true at the same targets. The two
statements are compatible because the arriving potential in (7) grows
linearly with the boundary height.

## 4. An exact weighted-boundary criterion for absence of escape

Equations (6)--(8) already show that

\[
\mathcal K(q)/q\longrightarrow0\quad(q\in N,\ q\to\infty)
\quad\Longrightarrow\quad
\text{every positive orbit is eventually periodic}.              \tag{9}
\]

The reverse implication follows from one further, explicitly inherited
canonical-potential result. PR175 proves that every positive superlevel
of `V(q)/q` on `N` lies in finitely many actual forward orbits. If every
orbit is eventually periodic, each such orbit has only finitely many
nonperiodic states. Hence `V(q)/q->0` on `N`. Since
`nu(q)<=delta^(-1)G(q)/q<=delta^(-1)V(q)/q`, (5) proves the reverse
implication. Thus, under the stated canonical inputs,

\[
\boxed{
\mathcal K(q)/q\to0\text{ on }N
\quad\Longleftrightarrow\quad
\text{every positive ordinary orbit is eventually periodic}.
}                                                \tag{10}
\]

Additional positive cycles are permitted on the right of (10) and are
excluded from the state domain on the left. The censored moving-bin
criterion in `MOVING_TILT_WINDOW.md` separately retains those cycles.

## 5. The precise remaining estimate

The new all-depth coefficient saving in (1) does not prove the weighted
decay in (9). A valid next step must bound the **actual** values `G(n)`
on this first-hit boundary, or otherwise force the normalized weighted
sum in (4) to vanish. Under a hypothetical escape, (7)--(8) describe the
specific spikes it must eliminate. No new source distribution can replace
that fixed mass `nu(p)`.

This is a narrower target than controlling every inverse word at every
depth: only the canonical first-upcrossing boundary at
`H(q)=2^floor(log_3 q)` enters. The decay assertion remains **OPEN**.

## Exact inherited source pins

- PR185 `276be8154f4e867acc0230466b34d9cb224aacf5`,
  `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`:
  ordinary harmonic flow, `h<=nu<=delta^(-1)h`, reciprocal-packing
  comparison, and the ordinary edge factors. The same file persists at
  refreshed head `7889fc680f5ee22237732eccc172b1699ef565da`.
- PR175 `54b5a324f55d97925ecb8100aa15ce7b08a12093`,
  `research/lean-global-closure-20261121/CANONICAL_POTENTIAL_SUPERLEVELS.md`,
  Sections 1 and 3: `PG=G`, `G<=V`, and the finite forward-orbit cover
  for each nonperiodic superlevel. The global cover uses its pinned
  fixed-basin sublinearity input; it does not follow from cardinality alone.
- The new `ALL_DEPTH_FIRST_CROSSING.md` pins the native count and keeps
  its numerical substitution separate from its formal finite interface.

The last-exit extraction and the linear lower bound (8) were independently
reviewed by the arithmetic attack agent. The further reverse implication
in Section 4 uses exactly the finite-forward-orbit-cover statement above.
