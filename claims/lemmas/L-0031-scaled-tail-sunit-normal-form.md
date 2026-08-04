# L-0031 — Scaled-tail telescoping and positive S-unit stage normal form

Claim ID: `L-0031`  
Title: The phase-34 connector chain linearizes to a positive two-prime toll recurrence  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0016`, `L-0017`, `T-0027`  
Scope: the stabilized four-type phase-34 tower system and the corrected 256-transition stage  
Related counterexample candidates: none

## Motivation

The canonical connector variables `eta`, `theta`, and the residual variables `z`
make one stage look like a large collection of unrelated mixed-radix carries.
There is a simpler ordinary coordinate in which all internal connector terms
telescope.

The resulting stage equation is a positive finite sum of `{2,3}`-units. This is
the exact native normal form needed before finite-rank multiplicative-equation
theorems can be applied responsibly.

## 1. Stabilized tower data

For a padding height divisible by `16`, order the four phase-34 self-return tower
types by their initial binary exponents

```text
k_0 = 5, 6, 7, 8.
```

Their stabilized data are

| type `i` | `p_i` | `b_i` | `alpha_i` | `beta_i` |
|---:|---:|---:|---:|---:|
| 0 | 5  | 9  | 0 | 2 |
| 1 | 30 | 54 | 1 | 3 |
| 2 | 20 | 36 | 2 | 2 |
| 3 | 56 | 24 | 3 | 1 |

where

\[
\boxed{b_i=2^{\alpha_i}3^{\beta_i}.}
\tag{1}
\]

At padding height `t`, put

\[
N_t=3^{7(t+1)},
\qquad
T_t=2^{11(t+1)}.
\tag{2}
\]

Then the binary and ternary tower anchors of type `i` are

\[
\boxed{
A_i(t)=\frac{T_t p_i}{64},
\qquad
B_i(t)=\frac{N_t p_i+b_i}{64}.}
\tag{3}
\]

These formulas are ordinary integer identities.

## 2. Scaled connector coordinates

Consider consecutive tower instances

\[
(i_j,t_j),
\qquad
(i_{j+1},t_{j+1}).
\]

Let `(eta_j,theta_j)` be their canonical connector from `L-0017`:

\[
B_{i_j}(t_j)+N_{t_j}\eta_j
=
A_{i_{j+1}}(t_{j+1})+T_{t_{j+1}}\theta_j.
\tag{4}
\]

Define the scaled connector integers

\[
\boxed{
X_j=p_{i_j}+64\eta_j,
\qquad
Y_j=p_{i_{j+1}}+64\theta_j.}
\tag{5}
\]

Multiplying (4) by `64` and using (3) gives the exact two-prime equation

\[
\boxed{
N_{t_j}X_j+b_{i_j}
=
T_{t_{j+1}}Y_j.}
\tag{6}
\]

No modular notation remains in (6).

## 3. The scaled ordinary high tail

Let `z_j` be the residual high-tail variable before connector `j`. Thus

\[
h_j=\eta_j+T_{t_{j+1}}z_j
\tag{7}
\]

is the ordinary high tail entering the tower at `(i_j,t_j)`. Define

\[
\boxed{
W_j=p_{i_j}+64h_j
=X_j+64T_{t_{j+1}}z_j.}
\tag{8}
\]

The tower output tail is

\[
\theta_j+N_{t_j}z_j
=
\eta_{j+1}+T_{t_{j+2}}z_{j+1}.
\tag{9}
\]

Consequently

\[
W_{j+1}
=Y_j+64N_{t_j}z_j
=X_{j+1}+64T_{t_{j+2}}z_{j+1}.
\tag{10}
\]

Combining (6), (8), and (10) proves the local scaled-tail recurrence

\[
\boxed{
T_{t_{j+1}}W_{j+1}
=
N_{t_j}W_j+b_{i_j}.}
\tag{11}
\]

Every quantity in (11) is a positive ordinary integer on an ordinary connector
trajectory. The connector seed, cap, and residual offset have telescoped into
one fixed positive toll `b_i`.

## 4. Finite-chain composition

For a finite chain of `L` transitions, define

\[
\mathcal N_L
=
\prod_{j=0}^{L-1}N_{t_j},
\qquad
\mathcal T_L
=
\prod_{j=0}^{L-1}T_{t_{j+1}}.
\tag{12}
\]

For `0 <= k < L`, put

\[
U_k
=
\sum_{r=0}^{k-1}11(t_{r+1}+1),
\tag{13}
\]

\[
V_k
=
\sum_{r=k+1}^{L-1}7(t_r+1),
\tag{14}
\]

with empty sums equal to zero. Iterating (11) gives

\[
\boxed{
\mathcal T_L W_L
=
\mathcal N_L W_0
+
\sum_{k=0}^{L-1}
2^{U_k+\alpha_{i_k}}
3^{V_k+\beta_{i_k}}.}
\tag{15}
\]

Thus every finite tower word produces one positive affine equation whose toll
terms are individual `{2,3}`-units with coefficient one.

## 5. Corrected 256-transition stage

At scale `m >= 12`, put

\[
B=2^m,
\qquad
\delta=2^{m-8}=B/256,
\tag{16}
\]

\[
t_{m,j}=B+j\delta
\qquad(0\le j\le256).
\tag{17}
\]

All these heights are divisible by `16`, so the stabilized table applies. For a
stage source word

\[
w=(i_0,\ldots,i_{255})\in\{0,1,2,3\}^{256},
\tag{18}
\]

write `W_m` and `W_(m+1)` for the scaled tails at its two boundaries. Define

\[
\boxed{
\mathcal A_m
=
7\sum_{j=0}^{255}(t_{m,j}+1)
=
\frac{5369}{2}B+1792,}
\tag{19}
\]

\[
\boxed{
\mathcal E_m
=
11\sum_{j=1}^{256}(t_{m,j}+1)
=
\frac{8459}{2}B+2816.}
\tag{20}
\]

Also put

\[
U_{m,k}
=
11\sum_{r=1}^{k}(t_{m,r}+1),
\tag{21}
\]

\[
V_{m,k}
=
7\sum_{r=k+1}^{255}(t_{m,r}+1).
\tag{22}
\]

Then one complete corrected stage obeys

\[
\boxed{
2^{\mathcal E_m}W_{m+1}
=
3^{\mathcal A_m}W_m
+
\sum_{k=0}^{255}
2^{U_{m,k}+\alpha_{i_k}}
3^{V_{m,k}+\beta_{i_k}}.}
\tag{23}
\]

The odd exponent `mathcal A_m` is exactly the stage odd count in `T-0027`.
The binary exponent differs from the residual-stage depth because `W` absorbs
one connector radix at each end; equation (23) is a conjugate physical-tail
coordinate, not a relabeling of the residual `z` equation.

## Proof

The four rows in the stabilized table follow by substituting the four core
parameters of `L-0016` into its formulas for `A_t` and `B_t`. In each row,

\[
K_t=11(t+1),
\qquad
G_t=7(t+1),
\]

and direct simplification gives (3). Equations (4)--(11) were derived above.
Induction on the number of local transitions proves (15): when one more local
map is appended, all earlier tolls acquire the new odd multiplier and the new
toll acquires all preceding binary radices.

For the stage sums,

\[
\sum_{j=0}^{255}t_{m,j}
=\frac{767}{2}B,
\]

which gives (19), while

\[
\sum_{j=1}^{256}t_{m,j}
=\frac{769}{2}B,
\]

which gives (20). Equation (23) is (15) with `L=256`. ∎

## Interpretation

The connector system has two exact coordinate descriptions:

```text
residual/Montgomery coordinate:
    exposes canonical cylinders and quotient extinction;

scaled ordinary-tail coordinate:
    exposes one positive finite S-unit equation per stage.
```

The second coordinate is the natural interface to the fixed-word S-unit advice
in literature wave 5. It also reveals the necessary caveat: the endpoint words
`W_m` and `W_(m+1)` are additional multiplicative variables. A direct
Evertse--Schlickewei--Schmidt application requires their prime support to be
controlled.

## Gap audit

- Equation (23) does not imply that the endpoint words lie in a fixed finite-rank multiplicative group.
- The scaled coordinate does not replace canonical cap-to-correction stitching; it is conjugate bookkeeping for an already valid ordinary path.
- A finite S-unit equation has not yet been obtained for unrestricted endpoint prime support.
- No positive starting integer or infinite tower grammar is constructed.

## Adversarial tests

`X-0016` reconstructs actual stabilized tower connectors, canonical residual
chains, and scaled tails; it verifies (6), (11), (15), and the stage exponent
formulas using exact integers only.