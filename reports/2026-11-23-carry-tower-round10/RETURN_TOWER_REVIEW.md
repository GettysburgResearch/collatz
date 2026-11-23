# Independent review of the actual return-tower construction

23 November 2026. Reviewer: the independent general-phase-return lane.

## Frozen scope and verdict

The reviewed parent is PR182, full head
`c369ae3c426ec6aaf9a280ec9578b9910c2147d5`. The three new sources are
identified by their exact Git blobs; this verdict does not extend to
subsequent edits.

| Source under `research/carry-tower-round10-20261123/` | Frozen Git blob | Reviewed scope |
| --- | --- | --- |
| `RETURN_TOWER.md` | `281c72145c2627d431f45e9930463219d0a67a4b` | R10-T1--T3, Sections 2--6 |
| `tower_controls.py` | `329e1a6a38c497bf0d34784f04b1f15e18022e17` | Exact finite ordinary replay and rational scalar enclosures |
| `ReturnTower.lean` | `0ad736f8fb72c15d46861d047009137ab5e01204` | Finite arithmetic declarations, with the written attachment boundary |

**Verdict: VERIFIED at the written claim level, with successful strict
compilation of the advertised finite Lean portion. No theorem correction
was required.** The complete infinite ordinary-source exclusion remains
OPEN, as the source says. Exact repeated R words have a decreasing
valuation rank; changing return words can reset that rank.

The parent inputs were kept at their stated scope:

- `research/repo-synthesis-round8-20261123/GERM_BRIDGE.md`, R8-G1,
  blob `540110f09cf68e3309fd83fea9c7ae497536ded4`, supplies the actual
  scalar, its strict lower bound, logarithmic upper bound and recurrence.
- `research/scalar-rigidity-round9-20261123/CARRY_RETURN.md`,
  R9-C1--R9-C4, blob `0b0d2ff63339522689f9984aad1bae3ab63d9e08`,
  supplies complete ordinary L/P maps and the arbitrary paid-excursion
  bound. Its least-source result is used only on the exact scalar level
  `h=7/8`.

## 1. Complete paid comparison and successive-run growth

I reconstructed the shifted affine identity rather than dropping its
constant. For `X=x+7`, the parent's paid upper bound gives

\[
P(x)+7=\frac9{32}X+\frac{83}{16}.
\]

At any positive ordinary paid entrance `x>=3`, this is at most `4X/5`.
The low word multiplies the shifted source by `lambda=9/8` exactly.
Multiplying the complete return inequalities proves the source-qualified
product bound in (3). The next unpaid run also requires
`2^(3m_j+1)<=X_j`; this is an ordinary divisibility constraint, not a
property of unrestricted symbolic schedules.

On the exact `7/8` level set, the parent's least-source theorem gives
`X>=2^34` at every return and unpaid entrance. Consequently the sharper
factor is exactly

\[
\rho=\frac9{32}+\frac{83}{2^{38}}
=\frac{77309411411}{274877906944}.
\]

For R10-T1, raising the weaker bound to the fifth power and using
`(9/8)^5<2` gives `15m_j<5(B-1)+M_j`. The accumulated variable
`T_j=M_j+5(B-1)` satisfies `15T_(j+1)<16T_j`. Its finite induction
therefore gives the displayed
`3*15^j*m_j<(B-1)*16^j`. All factors and the strict comparison survive
the cancellation. No paid-word length or carry bound has been inserted.

I also reconstructed the sharper real estimate. Taking logarithms of
the rho product yields both the lower mean condition on `M_j` and
`m_j<=C_0+(alpha-1)(M_j-theta*j)`. Solving the resulting affine
recurrence for the excess `M_j-theta*j` gives (8). The comparisons
`rho*lambda^10<1<rho*lambda^11` put theta strictly between ten and
eleven; the source lower bound gives `C_0>=11`. The exact formulas,
rather than the explanatory decimals, fund the inequalities.

These statements permit slowly changing schedules. They do not imply
that the physical source decreases at every return.

## 2. Exact fixed-word repetition rank

For `R=L^11 P`, I recomputed all four integer constants:

\[
a=282429536481,
\quad b=274877906944,
\quad d=7551629537,
\quad c=1478790549031.
\]

The ordinary terminal-odd cylinder is
`aq+c == b (mod 2b)`. Because q is odd, it is equivalent to
`dq+c == 0 (mod 2b)`, so an actual next R exists precisely when
`v_2(Z(q))>=39`. The complete-cylinder argument is essential here:
the endpoint congruence fixes the entire 24-gap word, not just an
arbitrary composite division.

The full affine equation gives `b Z(R(q))=a Z(q)`. Since a is odd,
one literal R lowers the valuation by exactly 38. Conversely, the
same source-cylinder equivalence supplies another literal R whenever
the remaining valuation is at least 39. Positivity makes Z nonzero.
This proves the exact maximum

\[
N(q)=\left\lfloor\frac{v_2(Z(q))-1}{38}\right\rfloor,
\]

including the boundary cases where the valuation is 38, 39, 76 or
77. The ordinary bit-length estimate then proves (12). This is a
rank for one complete return type; the note correctly leaves its
behavior across other types open.

## 3. Actual finite towers and unconditional scalar bounds

For each prescribed T, I reconstructed the complete numerator
`C_T=c(a^T-b^T)/(a-b)`, then the terminal CRT choice and the source
in (15)--(16). The odd representative t exists uniquely because the
modulus is odd. The congruence makes q integral, and the odd complete
numerator makes it odd. The elementary bound on the normalized
affine constant proves positivity and the stated linear source-bit
bound `q<2^(62T+7)`.

The full composite equality with an odd endpoint fixes each actual
prefix valuation. It therefore constructs a literal finite ordinary
orbit, rather than only a rational affine trajectory. The appended
`s-1` gaps equal to one are likewise literal, ending at
`v=2*3^(s-1)t-1`.

Applying the parent's unconditional actual scalar upper bound at v
and substituting it through this finite prefix gives exactly

\[
\frac12<h(r)<\frac12+
\frac{8K+27}{6\cdot3^{K+5}}<\frac58.
\]

The final comparison reduces to `32K+108<3^(K+6)`, an elementary
induction also present in Lean. No completion to one or infinite
candidate equality is used to bound the true scalar.

Each L or P contributes `7/9` to its two-step scalar prefix. Thus the
complete R tower has exactly the propagated scalar formula (19).
The actual scalar is strictly below `7/8` and decreases as the
physical source grows. Reserving one unused R ensures valuation 34
at both ends of every advertised comparison. This reserve is what
allows the conclusion for every prescribed finite number of returns.

The terminal r has shifted valuation one, and its center also has
valuation one. Backward center transport gives initial valuation
`38T+1`, so the construction has exactly T consecutive R words,
consistent with R10-T2. The potential counterexamples therefore
concern actual finite towers arbitrarily near the scalar level; they
do not realize exact `h=7/8` or one fixed infinite positive source.

## 4. Execution evidence

Both supplied control commands were executed from the complete
checkout:

```text
python3 research/carry-tower-round10-20261123/tower_controls.py
python3 -O research/carry-tower-round10-20261123/tower_controls.py
```

They returned identical PASS output with **35,714 exact checks**,
15 repetition-rank boundary cases, three mixed arbitrary-paid towers,
and nine controlled-tail towers through T=256. The latter contain
25,711 checked literal ordinary gaps across the whole control suite.
All require checks remain active under optimized Python. The final
stdout SHA256 is
`0f3e7540a2fe827fe41ad970485689233a7be2235ab1024ef711a31236efea7e`.
The final ten checks explicitly certify positivity and first-low-return
normalization for the five arbitrary paid-word fixtures.

A separate reviewer calculation did not import the author's program.
It composed complete affine constants directly, computed binary
valuations by repeated exact division, and replayed the constructions
at T=2,5,7,11. It passed **1,336 additional exact checks**, including
the entire ordinary prefix, actual gap-one tail, complete center
transport, shifted valuations, unconditional rational scalar
enclosures, and strict separation of adjacent scalar intervals.

Lean 4.34.1 with Mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612` compiled the frozen
`ReturnTower.lean` successfully using:

```text
lake env lean -DwarningAsError=true -DautoImplicit=false -j1 <absolute-path>/ReturnTower.lean
```

An earlier, unfrozen version used `omega` in the large-integer
`constant_return_expands` proof and needed a one-million-heartbeat
limit. The author changed that proof tactic to `linarith`; I inspected
the exact change and independently recompiled the final frozen file
successfully at the default heartbeat limit. There was no theorem or
hypothesis change. The mathematical scope of the Lean declarations is
the finite algebra and budget
induction stated in the note. The actual real scalar, its ordinary
attachment, and the infinite family of finite cylinders remain the
written proof checked above.

## 5. Remaining boundary

The strongest new fixed-source conclusion is an exact finite rank
for repeated R, supplemented by necessary growth bounds across
arbitrary return types. The missing theorem is control of rank resets
when those types change at one unchanged positive ordinary source.
The finite expanding cylinders preserve that distinction and do not
contradict the source's narrow claims. No full Collatz verdict is
implied by this review.
