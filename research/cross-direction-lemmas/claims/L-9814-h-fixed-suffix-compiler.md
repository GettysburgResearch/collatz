# L-9814 — A fixed-suffix compiler for H first crossings

Claim ID: `L-9814`  
Title: Two fixed H suffixes optimally compile every multiplier phase into a strict first crossing  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9813` for the exact offset and first-letter residue identities  
Scope: parametric families of genuine expanding-to-contracting H crossings  
Related counterexample candidates: none

## Definitions

For an H letter `r>=0`, write

\[
m_r=\frac{3^{2r+1}}{2^{3r+2}}
=\frac34(9/8)^r.
\tag{1}
\]

Let `z=(r_1,...,r_ell)` be a fixed nonempty suffix. Define

\[
P_0=1,
\qquad Q_0=0,
\tag{2}
\]

and recursively

\[
P_j=m_{r_j}P_{j-1},
\qquad
Q_j=m_{r_j}Q_{j-1}+\frac14.
\tag{3}
\]

Thus

\[
P_j=\prod_{i=1}^jm_{r_i},
\qquad
Q_j=\frac14\sum_{i=1}^j\prod_{k=i+1}^jm_{r_k}.
\tag{4}
\]

As in `L-9813`, put

\[
\alpha=\frac{\log(9/8)}{\log(4/3)},
\qquad
a=\lfloor\alpha s\rfloor,
\qquad
v_s=(s,0^{a-1}),
\tag{5}
\]

and

\[
R_s=M(v_s)=(4/3)^{\{\alpha s\}},
\qquad
t_s=(3/4)^a,
\qquad
q(v_s)=1-t_s.
\tag{6}
\]

## Statement

### 1. Exact suffix compiler

For every prefix `z_j=(r_1,...,r_j)`,

\[
\boxed{M(v_sz_j)=R_sP_j,}
\tag{7}
\]

and

\[
\boxed{
q(v_sz_j)
=P_jq(v_s)+Q_j
=(P_j+Q_j)-P_jt_s.
}
\tag{8}
\]

Define the exact multiplier window

\[
L_z=\max(1,P_1^{-1},\ldots,P_{\ell-1}^{-1}),
\qquad
U_z=\min(4/3,P_\ell^{-1}).
\tag{9}
\]

Then

\[
\boxed{I_z=(L_z,U_z)}
\tag{10}
\]

is precisely the set of phases `R` for which every proper appended prefix
expands and the full suffix contracts.

The window is nonempty exactly when

\[
\boxed{
P_\ell<1,
\qquad
P_j>\max(P_\ell,3/4)
\quad(1\le j<\ell).
}
\tag{11}
\]

Equivalently, every proper prefix product of `z` exceeds `3/4` and every
nonempty terminal-block product is below `1`.

### 2. Positive-density strict families

Assume `I_z` is nonempty and choose rational numbers

\[
L_z<\lambda<\rho<U_z.
\tag{12}
\]

Then the set of `s` for which

\[
R_s\in(\lambda,\rho)
\tag{13}
\]

has natural density

\[
\boxed{
\frac{\log(\rho/\lambda)}{\log(4/3)}.
}
\tag{14}
\]

For every sufficiently large selected `s`, the final suffix letter is the
first contracting prefix and

\[
\boxed{0<\Delta_{v_sz}<D_{v_sz}.}
\tag{15}
\]

If `H_j=P_j+Q_j`, then a chosen appended prefix is outside the scalar offset
test exactly under the eventual criterion

\[
\boxed{
q(v_sz_j)>1\text{ eventually}
\iff H_j>1.
}
\tag{16}
\]

The compact subwindow in (12) is essential for a single arbitrary suffix:
hits can otherwise approach `U_z` along the shrinking-target boundary.

### 3. Exact short-suffix classification

Restrict the suffix alphabet to `{0,1,2,3,4}`. A block of length `d` and digit
sum `T` has multiplier

\[
p(d,T)=\frac{3^{d+2T}}{2^{2d+3T}},
\tag{17}
\]

which is strictly increasing in `T`. For `1<=d<=4`, exact integer comparison
gives

| `d` | `p(d,T)<1` exactly when | `p(d,T)>3/4` exactly when |
|---:|---:|---:|
| 1 | `T<=2` | `T>=1` |
| 2 | `T<=4` | `T>=3` |
| 3 | `T<=7` | `T>=5` |
| 4 | `T<=9` | `T>=8` |

Consequently a word of length at most four is admissible exactly when every
proper prefix sum meets the right-hand threshold and every terminal-block sum
meets the left-hand threshold. The exact counts are

| suffix length | admissible suffixes | prefixes with 3/2/1 final choices |
|---:|---:|---:|
| 1 | 3 | `1 / 0 / 0` |
| 2 | 9 | `2 / 1 / 1` |
| 3 | 36 | `8 / 4 / 4` |
| 4 | 141 | `30 / 17 / 17` |

Every admissible suffix of length at least two eventually has

\[
q(v_sz_{\ell-1})>1.
\tag{18}
\]

Thus all `9+36+141` such compilers lie beyond the old penultimate-prefix
`q<1` criterion.

### 4. Uniform optimal two-suffix cover

The two length-two suffixes

\[
\boxed{z_-=30,\qquad z_+=10}
\tag{19}
\]

cover the entire phase interval `1<R_s<4/3`. Use

\[
z_-quad\text{when }R_s\le32/27,
\qquad
z_+\quad\text{when }R_s>32/27.
\tag{20}
\]

For `z_-=30`,

\[
P_1=m_3>1,
\qquad
P_2=\frac{6561}{8192},
\qquad
M(v_s30)\le\frac{243}{256}.
\tag{21}
\]

For `z_+=10`,

\[
P_1=\frac{27}{32},
\qquad
P_2=\frac{81}{128},
\qquad
M(v_s10)<\frac{27}{32}.
\tag{22}
\]

Thus in both cases the final zero is the first contracting prefix, with the
uniform margin

\[
\boxed{1-M\ge13/256.}
\tag{23}
\]

Once `a>=8`, both penultimate prefixes have `q>1`, yet both completed words
satisfy strict displacement:

\[
\boxed{
0<\Delta_{v_sz_\pm}<D_{v_sz_\pm}.
}
\tag{24}
\]

No single fixed suffix can cover all of `(1,4/3)` while also placing a proper
prefix beyond `q<1`. Hence the pair in (19) is cardinality-minimal, and length
two is minimal under that outside-`q` requirement.

## Proof

The H offset recurrence `q_(ur)=m_rq_u+1/4` and multiplier multiplication give
(7)--(8) by induction. The inequalities `RP_j>1` for `j<ell` and
`RP_ell<1` are exactly `L_z<R<U_z`, proving (9)--(10).

For `I_z` to be nonempty, `U_z>1` forces `P_ell<1`. For every proper `j`,
the inequality `P_j^(-1)<U_z` is equivalent to both `P_j>3/4` and
`P_j>P_ell`. This proves (11), including its terminal-block form.

On the compact window (12), put

\[
\eta_z=1-\rho P_\ell>0.
\]

Then `1-M(v_sz)>eta_z`, while (8) gives `q(v_sz)<H_ell`. The exact
first-letter residue in `L-9813` gives `A_(v_sz)>=8^s`. Hence

\[
8^s\eta_z>H_\ell
\]

for all sufficiently large selected `s`, and the displacement identity gives
`Delta_(v_sz)>0`. Moreover,

\[
D_{v_sz}-\Delta_{v_sz}
=(U_{v_sz}-A_{v_sz})(1-M(v_sz))+q(v_sz)>0,
\]

proving (15). Since `t_s` tends to zero through positive values, (8) proves
(16).

The irrationality proof for `alpha` in `L-9813` and Weyl equidistribution send
(13) to the interval

\[
\left(
\frac{\log\lambda}{\log(4/3)},
\frac{\log\rho}{\log(4/3)}
\right),
\]

whose length is (14).

Formula (17) follows by collecting the powers of `2` and `3`. Checking the
adjacent integer powers at each threshold gives the short table. Applying the
prefix and terminal-block tests in (11) gives the displayed finite counts.
Every admissible word of length at least two begins with `r_1>=1`, so

\[
H_1=m_{r_1}+1/4>1.
\]

Because every `m_r>=3/4`, the implication

\[
H>1\Longrightarrow m_rH+1/4>1
\]

propagates through the penultimate prefix and proves (18).

For the uniform cover, direct multiplication gives (21)--(22). The first
prefix of `30` always expands; the first prefix of `10` expands exactly when
`R_s>32/27`. The chosen rule therefore gives a first crossing and (23).
The completed offset bounds are

\[
q(v_s30)<\frac{10145}{8192},
\qquad
q(v_s10)<\frac{137}{128}.
\tag{25}
\]

Since

\[
8^s\frac{13}{256}
\ge\frac{13}{4}
>\frac{10145}{8192}
\qquad(s\ge2),
\]

the first-letter barrier proves (24) for every selected `s` once the words are
defined; `a>=8` additionally ensures both penultimate offsets exceed one.

Finally, a length-one suffix has no appended proper prefix beyond `q<1`. If a
single longer suffix covered all phases, `L_z=1` would make every nonempty
proper-prefix product greater than one: equality is impossible for a nonempty
product of powers of `2` and `3`. In particular `P_(ell-1)>1`. Since the last
letter multiplier is at least `3/4`, one gets `P_ell>3/4` and hence
`U_z=P_ell^(-1)<4/3`, a contradiction. This proves optimality. ∎

## Motivation

`L-9813` proved strict displacement for two isolated infinite families. This
lemma converts that observation into a reusable finite compiler. The optimal
pair `(30,10)` removes the shrinking-target issue entirely by adapting the
suffix to the current multiplier phase and still operates beyond the previous
scalar offset test.

## Dependency audit

- Multiplier multiplication and the exact offset recurrence are rederived in
  (7)--(8).
- `L-9813` supplies only the canonical first-letter floor and displacement
  identity used for strictness.
- Irrational equidistribution supplies the density claim for arbitrary compact
  subwindows; the uniform pair itself needs no density estimate.
- The short-suffix counts use exact integer inequalities, not floating point.

## Gap audit

- The suffix choice in (20) is adaptive; one fixed H word is not being extended
  indefinitely.
- Strict displacement of these finite words does not prove the empirical sign
  claim for every H word.
- The compiler does not create an infinite H or Collatz trajectory.
- Turning the two-suffix cover into an induction requires showing that the
  post-crossing state returns to the same normalized family.

## Adversarial tests

- Uniform strictness would fail for one arbitrary suffix near `U_z`; the pair
  avoids this by retaining the global margin (23).
- The recurrence coefficient `Q_j` is the additive intercept. The limiting
  offset is `H_j=P_j+Q_j`, not `Q_j` alone.
- Suffix `0` covers the phase interval at length one but cannot satisfy the
  outside-`q` requirement because its penultimate prefix is `v_s`.
- The words `30` and `10` are not claimed to be dynamically interchangeable;
  they are two distinct finite compilers.

## Remaining uncertainty

Whether the post-crossing affine data admit a return map closed under the same
two compiler suffixes is open. Such closure would be substantially stronger
than the finite sign theorem proved here.

## Suggested next attack

Compute the exact post-crossing normalized state for `30` and `10` and test
whether a finite collection of charts is closed under the adaptive rule. A
finite invariant chart cover would turn this one-stage compiler into a genuine
inductive mechanism.
