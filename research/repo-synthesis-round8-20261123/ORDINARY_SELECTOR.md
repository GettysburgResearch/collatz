# Actual expanding returns near the residual denominator-eight phases

23 November 2026. Parent:
`3954c775ba74e1f40776ff38cb4282698d4a334a`.

**Status: PROPOSED elementary written theorem, with a finite Lean
arithmetic core and exact ordinary controls. Full Collatz remains OPEN.**

The single-scalar criterion in [GERM_BRIDGE.md](GERM_BRIDGE.md) shifts
the construction target to an actual discounted gap scalar. A natural
next attack is to amortize its low states against its high states. This
note tests that attack on ordinary positive sources, rather than on a
freely chosen scalar recurrence.

The result is an explicit obstruction: there are actual finite orbit
segments with arbitrarily large endpoint/source ratio, with exactly one
scalar value above one and every other scalar value below one. Their
initial actual scalar values tend to `7/8` from below. Each source has
only linearly many bits in the construction parameter. This supplies no
positive source whose actual scalar equals `7/8`, and no fixed source
with an infinite exceptional itinerary.

## 1. Actual map, scalar, and strategic boundary

Use the positive odd accelerated map

\[
U(q)=(3q+1)/2^{g(q)},\qquad g(q)=v_2(3q+1),
\]

and the actual real scalar

\[
h(q)=\sum_{i\ge0}\frac{g(U^iq)}{3^{i+1}}.
\]

We use precisely the unconditional statements R8-G1 in the sibling
note:

\[
\frac12<h(q)\le1+\frac{\log_2q}{3},\qquad
h(Uq)=3h(q)-g(q).
\tag{1}
\]

No rationality, convergence to one, or chosen symbolic extension of h
is assumed. The one-step estimate in section 8 for `q/h(q)` contracts by at
most `35/36` whenever `q>=3` and `h(q)>=1`; the present construction
shows why counting isolated high visits cannot by itself amortize all
preceding low visits.

The prior actual-template and witness-charge results obstruct several
fixed-program approaches. They do not imply the universal selector
needed by the original band route. The present attack instead isolates
the residual phase cycle `{5/8,7/8}` in the new arithmetic scalar route.
Its geometry is the known negative odd cycle `-5 -> -7 -> -5` with
gaps `(1,2)`, not a newly discovered positive cycle.

## 2. Two complete ordinary blocks

Let L denote the two actual gaps `(2,1)` and P the two actual gaps
`(1,4)`. Their complete maps and ordinary domains are

| Block | Required source class | Intermediate | Endpoint |
| --- | --- | --- | --- |
| L | `q=16z+9` | `12z+7` | `18z+11=(9q+7)/8` |
| P | `q=64z+3` | `96z+5` | `18z+1=(9q+5)/32` |

Every listed intermediate and endpoint is positive and odd for `z>=0`.
The complete numerator equalities therefore certify the exact
valuations, not merely divisibility by the proposed powers of two.
For example, L uses `3q+1=4(12z+7)` followed by
`3(12z+7)+1=2(18z+11)`.

Both blocks have the same scalar prefix contribution:

\[
h(q)=\frac79+\frac{h(\text{endpoint})}{9}
=\frac78+\frac{h(\text{endpoint})-7/8}{9}.
\tag{2}
\]

Indeed `2/3+1/9=1/3+4/9=7/9`. At the hypothetical exact starting
scalar `7/8`, L passes through `5/8`, whereas P passes through `13/8`.
The physical affine maps are quite different:

\[
L(q)+7=\frac98(q+7),\qquad P(q)=\frac{9q+5}{32}.
\tag{3}
\]

For `m` consecutive L blocks followed by P, write the final endpoint r.
The full identity is

\[
r=\frac{9^{m+1}(q+7)}{32\cdot8^m}-\frac{29}{16}
=A_mq+7A_m-\frac{29}{16},
\qquad A_m=\frac9{32}\left(\frac98\right)^m.
\tag{4}
\]

The additive constant is retained throughout.

## 3. An explicit ordinary realization for every m

**R8-O1 (finite source construction).** Fix any integer `m>=1`. Set

\[
a=m+5,\qquad D=9^{m+1}.
\]

Choose the unique odd integer t in `0<t<2D` satisfying

\[
2^{a+4}t\equiv-13\pmod D.
\tag{5}
\]

Since D is odd, the power of two is invertible modulo D. Its residue
class is nonzero because `D>=81>13`. Of its representatives c and c+D
in `(0,2D)`, exactly one is odd. This proves existence and uniqueness;
no primitive-root assertion or discrete-log search is needed.

Define

\[
u=\frac{2^{a+4}t+13}{D},\qquad
q=2^{3m+1}u-7,\qquad r=2^at-1.
\tag{6}
\]

The integer u is positive and odd, so q and r are positive and odd.
For `0<=j<=m`, put

\[
q_j=9^j2^{3(m-j)+1}u-7.
\tag{7}
\]

For `j<m`, the exponent `3(m-j)+1` is at least four, hence
`q_j=9 mod 16`. Formula (3) gives `L(q_j)=q_(j+1)`.
At the last boundary `x=q_m`, equations (5)--(6) give

\[
9x+5=2Du-58=32r.
\]

As r is odd, `9x+5=32 mod 64`, so `x=3 mod 64`. Thus P is literal
there and ends at r. The whole gap word `(2,1)^m,(1,4)` is an actual
ordinary prefix starting at the single integer q constructed in (6).

The source sizes are modest as a function of m. From `t<2D` and
`13/D<1`, the integral u satisfies `u<=2^(a+5)`. Consequently

\[
q<2^{4m+11},\qquad r<2^{5m+10}.
\tag{8}
\]

These are size bounds, not stopping-time bounds.

## 4. The endpoint has a genuinely low actual scalar

**R8-O2 (unconditional actual tail bound).** The endpoint r has
`a-1` literal initial gaps equal to one:

\[
U^k(r)=3^k2^{a-k}t-1\quad(0\le k\le a-1).
\]

For `k<a-1`, the displayed number plus one is divisible by four,
so its next numerator has exact binary valuation one. At the end of
this prefix let `v=2*3^(a-1)t-1`. The scalar tail identity gives

\[
h(r)=\frac12+\frac{h(v)-1/2}{3^{a-1}}.
\tag{9}
\]

Since `t<2D` and `3<4`,

\[
v<4\cdot3^{a-1}D<2^{2a+4m+4}.
\]

Applying (1) at the actual endpoint v yields

\[
\boxed{\frac12<h(r)
<\frac12+\frac{12m+31}{6\cdot3^{m+4}}<\frac58.}
\tag{10}
\]

The last inequality is equivalent to
`48m+124<3^(m+5)`. It holds at m=0 (`124<243`), and induction follows
by tripling: `3(48m+124) > 48(m+1)+124`.

This bound concerns the actual infinite scalar. Only an actual finite
gap prefix and the unconditional upper bound (1) were used; no part of
the argument requires that r eventually reach one.

## 5. Exactly one high visit and unbounded expanding returns

Write `b=h(r)`, so `1/2<b<5/8`. At every two-step block boundary,
repeated use of (2) gives

\[
h(q_j)=\frac78+\frac{b-7/8}{9^{m+1-j}},
\qquad \frac56<h(q_j)<\frac78.
\tag{11}
\]

At the intermediate state of any L block,

\[
\frac12<3h(q_j)-2<\frac58.
\tag{12}
\]

At the intermediate state of the final P block,

\[
h(Uq_m)=\frac{4+b}{3},\qquad
\frac32<h(Uq_m)<\frac{37}{24}.
\tag{13}
\]

**R8-O3 (actual return obstruction).** Among the `2m+3` actual states
from q through r, exactly one has scalar above one and all the others
have scalar below one. Nevertheless the endpoint/source ratio is
unbounded across this explicit family.

For any prescribed real `C>0`, choose m with
`A_m>max(C,1)`. Such an m exists because `9/8>1`. Formula (4) gives
`r>Cq`, since `q>0` and `7A_m-29/16>0`. In particular the actual
potential also has unbounded low-to-low returns:

\[
\frac{r/h(r)}{q/h(q)}
=\frac rq\frac{h(q)}{h(r)}
>\frac43\frac rq.
\tag{14}
\]

Thus a proof cannot merely assign a fixed reward to each visit with
`h>=1` and expect that reward to cover arbitrarily long preceding low
runs. A source-sensitive return theorem, or a different globally
controlled quantity, would need additional information.

**R8-O4 (actual approach to the exceptional phase).** The initial
actual scalar obeys the explicit separation bounds

\[
\boxed{\frac1{4\cdot9^{m+1}}
<\frac78-h(q)
<\frac3{8\cdot9^{m+1}}.}
\tag{15}
\]

Therefore positive ordinary actual scalar values approach `7/8` from
below. The earlier L intermediates similarly approach `5/8` from
below. In particular there is no positive source-independent real
neighborhood excluding ordinary scalar values around either phase.

## 6. The remaining fixed-source obligation

Equations (5)--(7) choose a new ordinary source for each m. Passing to
an infinite compatible 2-adic source would not supply a positive
ordinary integer. Likewise, approximating `7/8` arbitrarily well does
not produce an actual equality `h(q)=7/8` for any fixed q.

If an actual orbit had the residual denominator-eight phase cycle,
write `h_i=p_i+k_i`, where the p_i alternate between `5/8` and `7/8`
and the integers `k_i` are nonnegative. Then its complete constraints
would be

\[
g_i=b_i+3k_i-k_{i+1}\ge1,\qquad
2^{g_i}q_{i+1}=3q_i+1,
\tag{16}
\]

with `b_i=1,2` when the p_i start at `5/8`. The two-block subsystem
above illustrates specific low and carry excursions. It does not
exhaust arbitrary carry paths in (16). A proposed finite-state or
amortized exclusion must control these unbounded integer carries and
the unchanged positive ordinary source together. That is the first
unsupported step here.

## 7. Source pins and evidence boundary

The following inputs were inspected at their frozen heads. Claims
listed as context are not new blanket reviews of those PRs.

| Source | Exact head and path | Use here |
| --- | --- | --- |
| PR177 | `25bf9b95a9404998e8e55aa401773488cd3dd4b8`; `research/lean-exact-witness-global-20261121/construction-attacks-20261123/descent/TEMPLATE_SELECTION.md`, TS-A and contracting-prefix result | Actual template distance and source-size payment barriers; context |
| PR177 | Same head; `construction-attacks-20261123/witness/WITNESS_CHARGE_AND_POWER_INDUCTION.md` under the same research packet | Homogeneous witness-charge closure barrier; context |
| PR146 | `f431078244e868dc699fad011044f0d5e7f76437`; `research/upper-bit-mergers/NEGATIVE_FIVE_CHECKPOINT.md` | Prior negative-cycle shadowing and actual finite-source geometry |
| PR173 | `fa0c9e2a2851e6324391e39c17afcb5913185aec`; PR summary | Band-return context; first returns can expand, eventual descent remains open |
| PR184 | `366dab89ee9548084ab9b5e4e90ff82abf287a20`; PR summary | Reserved-splice context; marked source-bounded partner remains open |

The new construction (5) uses modular inversion and an odd
representative to obtain linearly sized ordinary sources. The actual
scalar pattern (10)--(15), rather than the already known negative
cycle itself, is the contribution of this note.

`OrdinarySelector.lean` formalizes finite complete gap equalities,
the repeated affine identity, scalar block identities and interval
consequences, and the exponential inequality used in (10). It does
not formalize the real series, the full modular existence argument,
or the unbounded family theorem. Compilation and the axiom audit are
reported separately by the executing parent.

`selector_controls.py` constructs selected members with exact integer
arithmetic, replays every claimed ordinary gap, propagates rational
scalar enclosures without a convergence assumption, and separately
checks completed trajectories to one for those finite examples.
Completed examples permit exact values of h as an additional control;
they are not the proof of (10)--(15). Checks remain active under
`python -O`. There is no bounded enumeration promoted to an all-source
claim, and no proposed universal paid selector is supplied by this
obstruction.

## 8. Appendix: the high-state one-step estimate

**R8-O5.** Let `q>=3`, let g be a positive integer, and let h be a real
number with `h>=1`. Suppose

\[
q'=(3q+1)/2^g,\qquad h'=3h-g>\frac12.
\]

Then

\[
\frac{q'/h'}{q/h}\le\frac{35}{36}.
\tag{17}
\]

Indeed

\[
\frac{q'/h'}{q/h}
=\frac{(3+1/q)h}{2^g(3h-g)}
\le\frac{10h}{3\cdot2^g(3h-g)}.
\]

For g equal to one or two, the function `h/(3h-g)` decreases on the
allowed positive-denominator interval. Its maximum for `h>=1` is
`1/(3-g)`. In both cases the displayed ratio is at most `5/6`.

For `g>=3`, use `h=(h'+g)/3` and `h'>1/2` to obtain

\[
\frac{h}{h'}=\frac13+\frac{g}{3h'}
<\frac{2g+1}{3},\qquad
\frac{q'/h'}{q/h}<\frac{20g+10}{9\cdot2^g}.
\]

The last expression decreases with integral g, because
`20g+30<2(20g+10)` for `g>=1`. At g=3 it equals `35/36`, proving
(17). For actual q and h(q), the recurrence and strict lower bound in
(1) supply h' and its hypotheses. This is a one-step estimate on high
states. Equations (10)--(14) show that it cannot be extended to
arbitrary low-state returns merely by counting the high visits.

This auxiliary real-variable argument is written mathematics; it is
not included among the Lean declarations in this note.
