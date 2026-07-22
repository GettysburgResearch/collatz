# L-9862 — The first exact state refinement settles remainder thirty-two

Claim ID: `L-9862`  
Title: A general twisted-pair realization, the minimal thirty-two-channel boundary, and the exact order at `s=32`  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-p`  
Reviewing agents: `gpt56-synthesis-01`, `gpt56-synthesis-01-h`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9816`, `L-9839`, `L-9848`, `L-9856`, `L-9859`, `L-9861`  
Scope: characteristic-two period-four dyadic Padé residuals, with the exact first state-refinement layer `s=32`

## Definitions

For a truncation height `H`, put `Q=1+X` and work in

\[
\mathscr R_H
=\mathcal B_H[X]/(X^{H+1}),
\qquad
\mathcal B_H
=\mathbf F_2[c_0,\ldots,c_m]/(c_i^2-c_i),
\quad m=\lfloor\log_2H\rfloor.
\tag{1}
\]

The universal 2-adic phase unit and normalized summands are

\[
C_H=Q^c
=\prod_{i=0}^{m}(1+c_iX^{2^i}),
\qquad
\mathscr S_{n,v}^{(H)}
=C_H^vQ^{-3\binom v2}{n\brack v}_Q.
\tag{2}
\]

Thus

\[
F_{n,c}(1+X)=\sum_{v=0}^{n}\mathscr S_{n,v}^{(H)}
\pmod {X^{H+1}}.
\tag{3}
\]

The exact q-Pascal transition of `L-9856` is

\[
\boxed{
\mathscr S_{n+1,v}^{(H)}
=\mathscr S_{n,v}^{(H)}
+C_HQ^{n+4-4v}\mathscr S_{n,v-1}^{(H)}.
}
\tag{4}
\]

For a residue modulus `M`, define

\[
Z_{n,r}^{(M,H)}
=\sum_{v\equiv r\ (M)}\mathscr S_{n,v}^{(H)},
\qquad r\in\mathbf Z/M\mathbf Z.
\tag{5}
\]

## Statement

### 1. General twisted-pair realization of every closed residue height

Let `M` be even and suppose

\[
Q^{-4M}=1\pmod {X^{H+1}}.
\tag{6}
\]

For `j in Z/MZ`, define

\[
\mathbf E_{n,j}
=\sum_{v\text{ even}}Q^{-4jv}\mathscr S_{n,v}^{(H)},
\qquad
\mathbf O_{n,j}
=\sum_{v\text{ odd}}Q^{-4jv}\mathscr S_{n,v}^{(H)}.
\tag{7}
\]

They are exact weighted readouts of the residue state (5):

\[
\mathbf E_{n,j}
=\sum_{r\text{ even}}Q^{-4jr}Z_{n,r}^{(M,H)},
\qquad
\mathbf O_{n,j}
=\sum_{r\text{ odd}}Q^{-4jr}Z_{n,r}^{(M,H)}.
\tag{7a}
\]

These twisted parity sums obey the exact closed transition

\[
\boxed{
\begin{aligned}
\mathbf E_{n+1,j}
&=\mathbf E_{n,j}+C_HQ^{n-4j}\mathbf O_{n,j+1},\\
\mathbf O_{n+1,j}
&=\mathbf O_{n,j}+C_HQ^{n-4j}\mathbf E_{n,j+1},
\end{aligned}
\qquad j\in\mathbf Z/M\mathbf Z.
}
\tag{8}
\]

Moreover,

\[
\boxed{
\mathbf E_{n,j+M/2}=\mathbf E_{n,j},
\qquad
\mathbf O_{n,j+M/2}=Q^{-2M}\mathbf O_{n,j}.
}
\tag{9}
\]

Hence `M/2` twisted pairs form a closed `M`-component realization.  On the
reduced index set `0<=j<M/2`, the boundary from `j=M/2-1` to `j=0` carries
the factor `Q^(-2M)` only in the even-output equation.  The residual itself
is the untwisted readout

\[
F_{n,c}(1+X)=\mathbf E_{n,0}+\mathbf O_{n,0}.
\tag{10}
\]

### 2. Height seventy-two forces the first channel refinement

At `H=72`, the exact residue-quotient criterion `L-9859/(12)` reads

\[
4\,2^{\nu_2(M)}>72.
\tag{11}
\]

Therefore

\[
\boxed{
M=32\text{ is the smallest residue-sum modulus that closes modulo }X^{73}.
}
\tag{12}
\]

The old sixteen-channel state fails at the exact start of the present
coefficient window:

\[
\boxed{
\operatorname{ord}_X(1+Q^{-64})=64,
\qquad
Q^{-128}=1\pmod {X^{73}}.
}
\tag{13}
\]

Indeed, the kernel state `e_0+e_16` has zero sixteen-channel projection, but
one q-Pascal step produces the nonzero projected defect

\[
C_{72}Q^n(1+Q^{-64}).
\tag{14}
\]

Thus the move from sixteen to thirty-two channels is forced for the generic
residue-sum quotient, not chosen merely for computational convenience.

### 3. Exact thirty-two-channel certificate at `s=32`

At this height,

\[
C_{72}
=\prod_{i=0}^{6}(1+c_iX^{2^i})
\pmod {X^{73}}.
\tag{15}
\]

Put

\[
Z_{n,r}=Z_{n,r}^{(32,72)}.
\tag{16}
\]

Starting with `Z_(0,0)=1` and all other channels zero, the exact transition is

\[
\boxed{
Z_{n+1,r}
=Z_{n,r}+C_{72}Q^{n+4-4r}Z_{n,r-1}
\pmod {X^{73}},
\qquad r\in\mathbf Z/32\mathbf Z.
}
\tag{17}
\]

Define the final parity readouts

\[
E_{32,h}=[X^h]\sum_{\substack{0\le r<32\\r\text{ even}}}Z_{32,r},
\qquad
O_{32,h}=[X^h]\sum_{\substack{0\le r<32\\r\text{ odd}}}Z_{32,r}.
\tag{18}
\]

For the complete undecided window, recurrence (17) gives

\[
\boxed{
\begin{array}{c|ccccccccc}
 &64&65&66&67&68&69&70&71&72\\ \hline
E_{32,h}&0&0&0&0&0&0&0&0&1\\
O_{32,h}&0&0&0&0&0&0&0&0&0
\end{array}
}
\tag{19}
\]

as an identity in the full Boolean ring `B_72`.  Consequently, uniformly
for every `c in Z_2`,

\[
\boxed{
\bigl([X^{64}]F_{32,c},\ldots,[X^{72}]F_{32,c}\bigr)
=(0,0,0,0,0,0,0,0,1).
}
\tag{20}
\]

### 4. Exact order, slack, and target exclusion

The forced-factor baseline is

\[
B_{32}=\frac{32}{2}+A(32)=16+48=64.
\tag{21}
\]

Therefore

\[
\boxed{
\lambda_{32}(c)=\operatorname{ord}_{q-1}F_{32,c}(q)=72
\quad(c\in\mathbf Z_2),
}
\tag{22}
\]

and

\[
\boxed{\delta_{32}=72-64=8.}
\tag{23}
\]

For every odd reduced `a`, every integer `zeta`, and every dyadic target
above the actual remainder,

\[
\boxed{
L=2^k>32
\quad\Longrightarrow\quad
\Phi_L(U)\nmid R_{a,\zeta,32}(U).
}
\tag{24}
\]

Together with `L-9848`, `L-9856`, `L-9859`, and `L-9861`, this makes the
simple-target hypothesis in `L-9839/(14e)` vacuous for the first eight
nonzero actual layers

\[
\boxed{s=4,8,12,16,20,24,28,32.}
\tag{25}
\]

## Proof

### General twisted-pair transition

Multiply (4) by `Q^(-4jv)` and sum over even output sizes.  In the shifted
term put `u=v-1`, which is odd.  The shifted sum becomes

\[
\begin{aligned}
C_HQ^{n+4}
\sum_{v\text{ even}}Q^{-4(j+1)v}\mathscr S_{n,v-1}^{(H)}
&=C_HQ^{n+4-4(j+1)}
\sum_{u\text{ odd}}Q^{-4(j+1)u}\mathscr S_{n,u}^{(H)}\\
&=C_HQ^{n-4j}\mathbf O_{n,j+1}.
\end{aligned}
\tag{26}
\]

The same calculation with odd output sizes gives the second line of (8).
Condition (6) makes the twist index cyclic modulo `M`.
Grouping the size index in (7) by its residue modulo `M` proves (7a):
parity is preserved because `M` is even, and changing `v` by `M` does not
change the weight because `Q^(-4M)=1`.

Changing `j` to `j+M/2` multiplies a size-`v` summand by `Q^(-2Mv)`.  If
`v=2k`, this is `(Q^(-4M))^k=1`; if `v=2k+1`, it is `Q^(-2M)`.  This proves
(9), including the stated boundary rule.  Setting `j=0` and adding the two
parities proves (10).

### Minimality and exact Boolean-ring reproduction

For `H=72`, condition (11) says that `2^(nu_2(M))` must be at least `32`.
This proves (12).  Since `64` and `128` are powers of two,

\[
Q^{64}=1+X^{64},
\qquad
Q^{128}=1+X^{128}.
\tag{27}
\]

Multiplication by a unit does not change augmentation order, so (13)
follows.  The general kernel witness `L-9859/(30)--(31)` with `M=16` is
exactly (14).

For a coefficient-level reproduction of (19), write

\[
z_{n,r,h}=[X^h]Z_{n,r},
\quad
u_i=[X^i]C_{72},
\quad
q_{n,r,j}=[X^j]Q^{n+4-4r}.
\tag{28}
\]

Then (17) is the finite recurrence

\[
\boxed{
z_{n+1,r,h}
=z_{n,r,h}
+\sum_{i+j+k=h}u_iq_{n,r,j}z_{n,r-1,k},
\qquad 0\le h\le72.
}
\tag{29}
\]

Start with `z_(0,0,0)=1`, all other coefficients zero; use the seven
factors in (15); reduce after every multiplication with `c_i^2=c_i`; and
iterate (29) for `n=0,...,31`.  Summing the sixteen even and sixteen odd
channels gives exactly (19).  Every nonconstant Boolean monomial cancels
before the displayed output, leaving the single even-size unit in degree
`72`.

### Independent finite group-ring checksum

There is a second exact reproduction which does not use the Boolean ANF
transition.  Work in

\[
\mathscr G=\mathbf F_2[q,q^{-1}]/(q^{128}-1).
\tag{30}
\]

For an ordinary representative `c in {0,...,127}`, let
`P_(i,v)^(c)` be the parity enumerator of the size-`v` subset exponents from
`L-9848/(6)` after the first `i` coordinates.  Adding coordinate `i` gives

\[
\boxed{
P_{0,0}^{(c)}=1,
\qquad
P_{i+1,v}^{(c)}
=P_{i,v}^{(c)}
+q^{c+i-4(v-1)}P_{i,v-1}^{(c)}.
}
\tag{31}
\]

All exponents in (31) are reduced cyclically modulo `128`.  At `i=32`,
form

\[
P_{\mathrm{even}}^{(c)}=\sum_{v\text{ even}}P_{32,v}^{(c)},
\qquad
P_{\mathrm{odd}}^{(c)}=\sum_{v\text{ odd}}P_{32,v}^{(c)}.
\tag{32}
\]

Substituting `q=1+X` and extracting degrees `64,...,72` gives, for every one
of the `128` representatives,

\[
\boxed{
\begin{array}{c|c|c}
\text{readout}&\text{nine-bit mask, degrees }64\text{ through }72
&\text{coefficient vector}\\ \hline
P_{\mathrm{even}}^{(c)}&\mathtt{0x100}&(0,0,0,0,0,0,0,0,1)\\
P_{\mathrm{odd}}^{(c)}&\mathtt{0x000}&(0,0,0,0,0,0,0,0,0)
\end{array}
}
\tag{33}
\]

This finite audit covers every 2-adic `c`: in characteristic two,

\[
q^{128}-1=(q-1)^{128},
\tag{34}
\]

and replacing `c` by `c+128 beta`, with `beta in Z_2`, does not change the
series modulo `X^128`.  Thus (31)--(34) independently reproduce (19)--(20),
without assuming their phase independence.

### Forced baseline and target exclusion

For `s=4t`, `L-9848/(9)` gives

\[
A(4t)=t+2W(t),
\qquad
W(t)=\sum_{m=1}^{t}2^{\nu_2(m)}.
\tag{35}
\]

At `t=8`,

\[
W(8)=1+2+1+4+1+2+1+8=20,
\qquad
A(32)=8+2\cdot20=48.
\tag{36}
\]

The exact diagonal factor adds `s/2=16`, proving the baseline (21).  All
coefficients below degree `64` vanish, while (20) identifies degree `72` as
the first surviving unit.  This proves (22)--(23).

For a reduced residual, the odd local substitution `q=U^a` preserves
augmentation order and has `c=zeta/a+4s-4 in Z_2`.  Every dyadic target
above `32` has `L>=64`, so its augmentation cost is `L/2>=32>8`.  The slack
criterion `L-9848/(11)--(12)` proves (24).  This completes the claim. ∎

## Motivation

The first seven proved layers require augmentation information only below
degree `64`, where sixteen residue channels close.  The forced baseline at
`s=32` is exactly degree `64`.  The old quotient therefore loses information
at the first coefficient that can matter, and its kernel defect (14) makes
that loss explicit.

The thirty-two-channel refinement succeeds, while the general twisted-pair
identity repackages it as sixteen coupled parity pairs.  This is a structural
state transition rather than a larger unexplained table.

## Dependency audit

- `L-9816` supplies the exact diagonal factor.
- `L-9839` supplies the forced lower dyadic cyclotomic factors.
- `L-9848` supplies the normalized subset residual, `A(4t)`, and the
  augmentation-slack target criterion.
- `L-9856` supplies the universal Boolean-ring q-Pascal transition.
- `L-9859` supplies the exact residue-quotient closure and minimality
  criterion.
- `L-9861` supplies the first specialized twisted-pair transition; the
  general `M/2`-pair theorem is proved here.
- The height-`72` refinement, two independent certificates, exact order
  `lambda_32=72`, and target exclusion are proved here.
- No numerical root approximation, phase sampling, or transverse genericity
  assumption is used.

## Gap audit

- Minimality in (12) is among residue-class sum quotients.  It does not rule
  out a different nonlinear or jet-enriched compression with fewer scalar
  coordinates.
- Equation (19) proves only the single layer `s=32`.  It does not turn the
  paired state (8)--(9) into an all-layer unit induction.
- The all-layer identity
  `lambda_(4t)=4t+2*sum_(j<=t)2^(nu_2(j))` remains conjectural.
- No order at `s>=36` is inferred from the present certificate.
- Odd-macro numerator and phase jets remain outside the claim.

## Adversarial tests

- Sixteen channels fail at order exactly `64`, not merely somewhere above
  the computed window.  Reusing `L-9861/(10)` at height `72` would alias the
  decisive coefficients.
- The witness `e_0+e_16` is an arbitrary coefficient state. It proves
  failure of the universal sixteen-channel residue-sum quotient, not that the
  witness itself occurs on the actual residual orbit.
- The raw even/odd pair is not closed.  The general recurrence needs all
  `M/2=16` twists and the boundary factor `Q^(-64)`.
- All seven phase bits `c_0,...,c_6` are retained before cancellation.
- In the group-ring checksum, all `128` phase residues must be covered;
  checking only the lower `64` would drop the bit that first appears at
  degree `64`.
- The coefficient window begins only after the independently proved forced
  baseline.  The nine displayed entries alone do not prove lower vanishing.

## Remaining uncertainty

Can the sixteen twisted pairs be triangularized after division by the forced
augmentation power so that their untwisted leading unit is propagated by a
small block invariant?  The exact state now survives the refinement
boundary, but its unit line remains hidden inside the coupled twists.

## Suggested next attack

Apply four q-Pascal steps at once to the general paired system (8), normalize
by the increment in `B_(4t)`, and track the boundary twist separately.  A
triangular four-step block could explain why the finite certificates through
`s=32` always leave one constant unit and could connect directly to the
binary doubling recurrence in `L-9848/(16)`.
