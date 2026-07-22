# L-9841 — Completed-zero H return family and raw phase rotation

Claim ID: `L-9841`  
Title: The suffixes `30`, `60`, and `70` form a finite raw multiplier return system with non-descending return cylinders  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: exact H affine-word algebra; `L-9840` for the zero-descent design criterion  
Scope: exact completed two-letter H suffixes `r0` and a finite alternating multiplier architecture  
Related counterexample candidates: none

## Definitions

For an H letter `r>=0`, put

\[
m_r=\frac{3^{2r+1}}{2^{3r+2}}
=\frac34\left(\frac98\right)^r.
\tag{1}
\]

Let `e_r=r0` be the completed two-letter suffix consisting of `r` followed by
`0`. Write its normalized affine map as

\[
f_{e_r}(x)
=\mu_rx+\frac7{16}
=\frac{V_rx+B_r}{U_r}.
\tag{2}
\]

For this claim, subscripts `r` on `(U_r,V_r,B_r,A_r,Y_r)` refer to the word
`e_r`, not to the one-letter word `r`.

## Statement

### 1. Exact canonical data for every completed suffix `r0`

For every `r>=0`,

\[
\boxed{
U_r=2^{3r+4},
\qquad
V_r=3^{2r+2},
\qquad
B_r=7\,2^{3r},
\qquad
\mu_r=\frac{V_r}{U_r}
=\frac9{16}\left(\frac98\right)^r.
}
\tag{3}
\]

Define the parity coefficient

\[
\boxed{
\varepsilon_r=
\begin{cases}
1,&r\text{ even},\\
9,&r\text{ odd}.
\end{cases}
}
\tag{4}
\]

Then the canonical input and endpoint are

\[
\boxed{
A_r=\frac{\varepsilon_rU_r}{16},
\qquad
Y_r=\frac{\varepsilon_rV_r+7}{16}.
}
\tag{5}
\]

Consequently, with `D_r=U_r-V_r`, the zero-interface displacement is

\[
\boxed{
\delta_r(j)
=A_r-Y_r+j(U_r-V_r)
=\frac{\varepsilon_rD_r-7}{16}+jD_r.
}
\tag{6}
\]

### 2. Complete zero-descent classification of `r0`

The multiplier ratios satisfy

\[
\mu_{r+1}=\frac98\mu_r,
\qquad
\mu_4=\frac{59049}{65536}<1,
\qquad
\mu_5=\frac{531441}{524288}>1.
\tag{7}
\]

The formal non-descent quotient set

\[
\mathcal N_r
=\{j\in\mathbb Z_{\ge0}:\delta_r(j)\le0\}
\tag{8}
\]

is exactly

\[
\boxed{
\mathcal N_r=
\begin{cases}
\{0\},&r=0,\\
\varnothing,&1\le r\le4,\\
\mathbb Z_{\ge0},&r\ge5.
\end{cases}
}
\tag{9}
\]

Thus `10`, `20`, `30`, and `40` pass the robust-descent test of `L-9840`,
while every member of the infinite family

\[
\boxed{r0\qquad(r\ge5)}
\tag{10}
\]

violates both halves of that test:

\[
U_r<V_r,
\qquad
A_r<Y_r.
\tag{11}
\]

At a zero interface, every `r0` with `r>=5` strictly increases the positive
integral endpoint for every quotient `j>=0`.

### 3. A universal contraction-to-expansion return compiler

For any contracting multiplier phase

\[
0<R<1,
\tag{12}
\]

let

\[
\boxed{
r(R)=\min\{r\ge5:R\mu_r>1\}.
}
\tag{13}
\]

Then `r(R)` exists and the completed suffix `r(R)0` returns the phase to the
uniform window

\[
\boxed{
1<R\mu_{r(R)}\le\frac98.
}
\tag{14}
\]

The first letter `r(R)` is already a strict contracting-to-expanding
crossing, and the terminal zero leaves the completed word expanding. Hence
the infinite family (10) is an exact multiplier-return compiler, not merely a
formal source of non-descending endpoint maps.

### 4. A finite raw return architecture

Put

\[
\boxed{
\xi=\mu_3\mu_6=\frac{3^{22}}{2^{35}}.
}
\tag{15}
\]

The exact integer comparisons

\[
3^{22}<2^{35},
\qquad
3^{24}>2^{38}
\tag{16}
\]

give

\[
\boxed{
\frac89<\xi<1.
}
\tag{17}
\]

Define the expanding and contracting phase intervals

\[
\boxed{
\mathcal I_+=\left(1,\frac98\right],
\qquad
\mathcal I_-=(\mu_3,\mu_4].
}
\tag{18}
\]

Appending `30` maps `I_+` bijectively onto `I_-` by

\[
\boxed{D(R)=\mu_3R.}
\tag{19}
\]

The threshold

\[
\tau=\mu_6^{-1}
\tag{20}
\]

lies strictly inside `I_-`. On `I_-`, choose the return suffix by

\[
\boxed{
S(R)=
\begin{cases}
\mu_7R,&\mu_3<R\le\tau
\quad\text{(append `70`)},\\[1mm]
\mu_6R,&\tau<R\le\mu_4
\quad\text{(append `60`)}.
\end{cases}
}
\tag{21}
\]

Then

\[
\boxed{S:\mathcal I_-\longrightarrow\mathcal I_+}
\tag{22}
\]

is a bijection. Hence the three completed suffixes

\[
\boxed{\{30,60,70\}}
\tag{23}
\]

form a closed **raw**, non-renormalized multiplier architecture which
alternates expansion and contraction forever.

### 5. The two-step phase map is an irrational rotation

The return map `P=S composed with D` on `I_+` is

\[
\boxed{
P(R)=
\begin{cases}
\dfrac98\xi R,&1<R\le\xi^{-1},\\[2mm]
\xi R,&\xi^{-1}<R\le9/8.
\end{cases}
}
\tag{24}
\]

Let

\[
\ell=\log(9/8),
\qquad
\delta=\log(1/\xi).
\tag{25}
\]

By (17), `0<delta<ell`. In the logarithmic coordinate `x=log R in (0,ell]`,
equation (24) becomes

\[
\boxed{
x\longmapsto
\begin{cases}
x+\ell-\delta,&0<x\le\delta,\\
x-\delta,&\delta<x\le\ell.
\end{cases}
}
\tag{26}
\]

After identifying the two endpoints, this is rotation by `-delta` modulo
`ell`. The ratio

\[
\boxed{\delta/\ell\notin\mathbb Q}
\tag{27}
\]

is irrational. Therefore every raw multiplier orbit in `I_+` is dense and
aperiodic. Among return stages, the exact branch frequencies are

\[
\boxed{
\operatorname{freq}(70)=\frac\delta\ell,
\qquad
\operatorname{freq}(60)=1-\frac\delta\ell.
}
\tag{28}
\]

### 6. Exact crossing and endpoint roles

For `R in I_+`, appending `30` gives a final multiplier in `I_-`, while the
proper one-letter prefix before its terminal zero still has multiplier above
one. Thus `30` makes a strict expanding-to-contracting crossing at its final
zero.

For `R in I_-`, the selected suffix `60` or `70` has completed multiplier in
`I_+`; its first letter already crosses strictly from contraction to
expansion, and its final zero preserves expansion.

At zero interfaces the endpoint roles are complementary:

\[
\boxed{
\begin{aligned}
30:&\quad Y_{\rm in}-Y_{\rm out}>0
&&\text{for every }j\ge0,\\
60,70:&\quad Y_{\rm in}-Y_{\rm out}<0
&&\text{for every }j\ge0.
\end{aligned}
}
\tag{29}
\]

Thus the architecture evades the finite-family no-go condition of `L-9840`
at every return stage, and does so with a positive-frequency raw multiplier
schedule rather than an externally imposed rare exception.

### 7. Full-state boundary

Every completed suffix `r0` acts on the affine offset by

\[
\boxed{
q\longmapsto\mu_rq+\frac7{16}.
}
\tag{30}
\]

Consequently a down-return pair `30,(r0)` with `r in {6,7}` acts by

\[
\boxed{
q\longmapsto
(\mu_3\mu_r)q
+\frac7{16}(1+\mu_r).
}
\tag{31}
\]

The phase rotation does not erase this fiber coordinate, nor does it prove
that the canonical interface blocks eventually vanish. Therefore the finite
architecture is a genuine multiplier return and a genuine escape from
uniform endpoint descent, but not yet an ordinary nested H seed or a Collatz
orbit.

## Proof

Appending the terminal letter `0` to the one-letter map

\[
x\longmapsto m_rx+\frac14
\]

gives

\[
x\longmapsto
m_0\left(m_rx+\frac14\right)+\frac14
=\mu_rx+\frac7{16}.
\]

Multiplying the one-letter numerator and denominator data by those of `0`
proves (3).

Now

\[
V_r=9^{r+1}
\equiv
\begin{cases}
9\pmod{16},&r\text{ even},\\
1\pmod{16},&r\text{ odd}.
\end{cases}
\tag{32}
\]

Thus `epsilon_r V_r+7` is divisible by sixteen. The value in (5) lies in
`[0,U_r)`, and oddness of `V_r` makes the canonical solution unique modulo
`U_r`. Substitution in the affine map gives `Y_r`, proving (5), and
subtraction proves (6).

The ratio identity in (7) follows from (3). The displayed exact values at
`r=4,5` prove that `D_r>0` through `r=4` and `D_r<0` from `r=5` onward. At
`r=0`, equation (6) is `delta_0(j)=7j`. For `1<=r<=4`, direct substitution
gives

\[
A_r-Y_r=26,18,917,405
\qquad\text{respectively},
\tag{33}
\]

and `D_r>0`. For `r>=5`, both `D_r` and
`(epsilon_rD_r-7)/16` are negative. This proves (9)--(11).

Since `mu_r` tends to infinity geometrically, (13) exists. If its minimum is
larger than five, minimality gives

\[
R\mu_{r(R)-1}\le1
<R\mu_{r(R)},
\]

and the ratio `mu_r/mu_(r-1)=9/8` proves (14). If the minimum is five, then
`R<=1` and `mu_5<9/8` give the same bound. Since
`m_r=(4/3)mu_r`, the first letter crosses above `4/3`, proving part 3.

For the finite architecture, (16) is exactly the pair of inequalities
`xi<1` and `(9/8)xi>1`, proving (17). The identities

\[
\mu_4=\frac98\mu_3,
\qquad
\mu_7=\frac98\mu_6
\tag{34}
\]

show that `D` maps `I_+` onto `I_-`. They also give

\[
\mu_3<\mu_6^{-1}<\mu_4.
\]

The lower branch of `S` maps

\[
(\mu_3,\mu_6^{-1}]
\longrightarrow
\left(\frac98\xi,\frac98\right],
\]

while its upper branch maps

\[
(\mu_6^{-1},\mu_4]
\longrightarrow
\left(1,\frac98\xi\right].
\]

These half-open images partition `I_+`, proving (21)--(23). Composing the two
steps gives (24), and taking logarithms gives (26).

If `delta/ell=p/q` were rational with positive integers `p,q`, exponentiation
would give

\[
\left(\frac{2^{35}}{3^{22}}\right)^q
=\left(\frac98\right)^p,
\]

or

\[
2^{35q+3p}=3^{22q+2p},
\]

which is impossible by unique factorization. Irrational-rotation minimality
and unique ergodicity now prove density, aperiodicity, and the interval-length
frequencies (28).

The crossing assertions follow from

\[
m_r=\frac43\mu_r.
\]

The endpoint assertions are the cases `r=3,6,7` of (9). Finally, composing
the affine offset updates proves (30)--(31). ∎

## Motivation

`L-9840` says a reusable suffix architecture cannot retain an ordinary seed
if every zero interface decreases the endpoint. The family `r0`, `r>=5`, is
the strongest possible formal escape: every quotient increases the endpoint.

More importantly, two members of that family close the raw multiplier defect
left by the earlier `10/30` compiler. The three-word system `{30,60,70}`
alternates exact crossings on a compact invariant phase interval and produces
an irrational rotation without dividing out a terminal multiplier.

## Dependency audit

- All canonical data are derived directly from the H affine recurrence and
  odd modular uniqueness.
- `L-9840` is used only to interpret the endpoint classification as a design
  rule; its theorem is not needed for the calculations.
- Irrational-rotation minimality and unique ergodicity are the only standard
  dynamical facts invoked.
- No computation, empirical carry sign, or unproved first-crossing conjecture
  is used.

## Gap audit

- The multiplier architecture is closed in the raw phase, but the affine
  offset and 2-adic endpoint tail remain live fiber coordinates.
- The result does not prove that the nested canonical input converges to an
  ordinary nonnegative integer.
- Formal non-descent at `h=0` does not prove that the actual interface blocks
  become zero.
- Alternating multiplier crossings are not yet one marked Collatz orbit.

## Adversarial tests

- The canonical coefficient in (5) depends on the parity of `r`; using `9`
  for every `r` gives a nonintegral endpoint for even `r`.
- At the cut `R=mu_6^(-1)`, suffix `60` would land exactly at multiplier one.
  The half-open convention assigns that point to `70`, which lands at `9/8`.
- The inequalities `8/9<xi<1` are both needed: one puts the cut inside
  `I_-`, and the other keeps both return images inside `I_+`.
- The rotation is for the two-step raw multiplier map. It does not identify
  or quotient away the affine fiber.

## Remaining uncertainty

Whether the skew product consisting of the phase rotation, affine offset, and
canonical 2-adic interface carries has an ordinary nonnegative nested point is
open. The theorem removes uniform multiplier decay and uniform zero-interface
descent as obstructions, but not the full-state return obstruction.

## Suggested next attack

Analyze the two-step fiber maps in (31) over the irrational rotation and then
apply the reset-cylinder sieve of `L-9837` to the alternating
`30/(60 or 70)` carry stream. The decisive question is whether its unique
physical low-block path can stabilize even though the formal endpoint maps
alternate descent and ascent.
