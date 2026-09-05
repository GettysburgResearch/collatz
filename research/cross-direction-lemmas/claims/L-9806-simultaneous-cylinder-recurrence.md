# L-9806 — Simultaneous `64`/`81` cylinder recurrence

Claim ID: `L-9806`  
Title: The diagonal itinerary/reciprocal cylinder has exact base-`5184` digits and a periodic late reciprocal tail  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-9801`; the chart recurrence and reciprocal terminal lift restated below  
Scope: diagonal synthesis of PR #16 and PR #20  
Related counterexample candidates: none

## Definitions

For an integer or modular expression `y`, `[y]_m` denotes its least
nonnegative residue modulo `m`; negative powers inside such brackets denote
modular inverses. The symbols `epsilon_K` are binary chart digits, while `h`
is the ordinary reciprocal-phase numerator. Canonical representatives always
lie in the half-open interval beginning at zero and ending at their displayed
modulus.

### Itinerary coordinate

Let `epsilon_0,epsilon_1,...` be binary chart digits. Let `alpha_K` be the
canonical residue modulo `64^K` realizing the first `K` digits, and define the
terminal state `tau_K` by

\[
H_{\varepsilon_{K-1}}\cdots H_{\varepsilon_0}
(\alpha_K+64^Kz)=\tau_K+81^Kz,
\tag{1}
\]

where `H_epsilon(x)=(81x-17 epsilon)/64`. Initialize
`alpha_0=tau_0=0`. On appending `epsilon_K`, put

\[
\boxed{
p_K=[(81^K)^{-1}(\varepsilon_K-\tau_K)]_{64},
}
\tag{2}
\]

\[
\boxed{\alpha_{K+1}=\alpha_K+p_K64^K,}
\tag{3}
\]

\[
\boxed{
\tau_{K+1}
=\frac{81(\tau_K+81^Kp_K)-17\varepsilon_K}{64}.
}
\tag{4}

\]

### Reciprocal coordinate

The depth-compatible reciprocal coordinate is the terminal vertical lift

\[
\zeta_K=[-17h64^{-1}]_{81^K},
\qquad \zeta_0=0.
\tag{5}
\]

It has canonical digits

\[
\boxed{
\zeta_{K+1}=\zeta_K+\eta_K81^K,
\qquad0\le\eta_K<81.
}
\tag{6}

\]

For `K>=1`, `eta_K` is exactly the new terminal lift digit
`d_(K-1)^(K+1)` of the depth-`K+1` reciprocal chain in `PR16/L-9309`.
The initial digit is instead `eta_0=q_0^(1)`. Unlike the full left-hand phase
tuple, `(zeta_K)` is compatible as the phase depth changes.

## Statement

Define the simultaneous cylinder

\[
\mathcal C_K=
\left\{
n\in\mathbb Z:
n\equiv\alpha_K\pmod{64^K},
\quad
17n+64\zeta_K\equiv0\pmod{81^K}
\right\}.
\tag{7}
\]

CRT gives one canonical representative

\[
0\le R_K<Q_K,
\qquad Q_K=64^K81^K=5184^K.
\tag{8}
\]

Put

\[
X_K=\frac{R_K-\alpha_K}{64^K},
\qquad
G_K=\frac{17R_K+64\zeta_K}{81^K}.
\tag{9}
\]

Then the nested representatives have one exact base-`5184` digit

\[
\boxed{
R_{K+1}=R_K+c_KQ_K,
\qquad0\le c_K<5184,
}
\tag{10}

\]

determined by the pair of congruences

\[
\boxed{
c_K\equiv(p_K-X_K)(81^K)^{-1}\pmod{64},
}
\tag{11}
\]

\[
\boxed{
c_K\equiv
-(G_K+64\eta_K)(17\cdot64^K)^{-1}
\pmod{81}.
}
\tag{12}
\]

The state updates are

\[
\boxed{
X_{K+1}=\frac{X_K+c_K81^K-p_K}{64},
}
\tag{13}
\]

\[
\boxed{
G_{K+1}=\frac{G_K+17c_K64^K+64\eta_K}{81}.
}
\tag{14}
\]

In particular,

\[
\boxed{
c_K=0
\iff
X_K\equiv p_K\pmod{64}
\text{ and }
G_K+64\eta_K\equiv0\pmod{81}.
}
\tag{15}
\]

The cylinders contain one fixed ordinary nonnegative integer `A` at every
depth if and only if

\[
\boxed{c_K=0\text{ for all sufficiently large }K.}
\tag{16}

\]

This is the combined digit that must vanish. The reciprocal digit `eta_K`
need not vanish.

## Late normal form for a stabilized positive integer

Assume stabilization at `A>0`. The reciprocal congruence and (5) give
\(A\equiv h\pmod{81^K}\) at every depth, hence `A=h` as ordinary integers. For
all sufficiently large `K`,

\[
R_K=\alpha_K=A,
\qquad X_K=p_K=c_K=0.
\tag{17}
\]

Once `81^K>17A`, one has

\[
\boxed{1\le G_K\le64,}
\tag{18}

\]

and reduction modulo `64` gives

\[
\boxed{
G_K=\langle17^{1-K}A\rangle_{64}^{+},
}
\tag{19}

\]

where the brackets select the representative in `{1,...,64}`. Since `17` has
order `4` modulo `64`, `(G_K)` is eventually 4-periodic. Equation (14) becomes

\[
\boxed{
\eta_K=
\frac{
81\langle17^{-K}A\rangle_{64}^{+}
-\langle17^{1-K}A\rangle_{64}^{+}
}{64}.
}
\tag{20}

\]

Thus `eta_K` lies in `{1,...,80}` and is eventually 4-periodic. For `64|A`,
one gets `G_K=64` and `eta_K=80`. For the check `A=1`, the late reciprocal
digits repeat

```text
62, 41, 21, 1, ...
```

rather than vanishing.

## Proof

After `K` steps, adding `p64^K` to the initial residue adds `p81^K` to the
terminal state in (1). Requiring the next state to be congruent to
`epsilon_K` modulo `64` proves (2)--(4).

For `K>=1`, equation (5) is the terminal residue `q_(K-1)` at phase depth `K`;
increasing the depth preserves the same expression modulo `81^K`. Together
with the initial convention `zeta_0=0`, this proves the nested lift (6).

The moduli in (7) are coprime, so (8) follows from CRT. Substitute (3), (6),
and (10) into the two depth-`K+1` congruences. After dividing by `64^K` and
`81^K` respectively, they become (11) and (12). CRT modulo `64*81=5184`
selects exactly one canonical `c_K`. Direct division gives (13)--(14), and
setting `c_K=0` gives (15).

The representatives satisfy the hypotheses of `L-9801`, so ordinary
nonnegative realization is equivalent to eventual stabilization, which is
equivalent to (16).

Under stabilization, (17) is immediate once `64^K>A`. From (9), canonicality
of `zeta_K`, and `81^K>17A`,

\[
0< G_K <65,
\]

proving (18). Also

\[
81^KG_K=17A+64\zeta_K\equiv17A\pmod{64}.
\]

Since `81` is congruent to `17` modulo `64`, this proves (19). Finally, set
`c_K=0` in (14) and substitute consecutive values from (19), obtaining (20).
Its numerator is positive and below `81*64`, so `1<=eta_K<=80`. ∎

## Real-coordinate consequence

If `xi` is the real survivor code in `[0,1]`, then after stabilization the
actual tail state satisfies

\[
A_K=\left(\frac{81}{64}\right)^K(A-\xi)
+\xi(\text{shift}^K\varepsilon).
\tag{21}
\]

For `A>=2`, this state is positive and grows exponentially. This is compatible
with `c_K=0`: the initial simultaneous cylinder stabilizes while its forward
orbit grows.

## Motivation

`R-9801` rules out a local carry-to-repetition implication. This lemma supplies
the correct global replacement: combine the axes by CRT, track one canonical
base-`5184` digit, and ask whether that digit eventually vanishes.

## Dependency audit

- The itinerary recurrence and reciprocal terminal lift are derived explicitly.
- CRT supplies the combined cylinder and digit.
- `L-9801` supplies only the final ordinary-stabilization equivalence.

## Gap audit

- No theorem here forces or forbids eventual `c_K=0`.
- Vanishing of `eta_K` is the wrong target; it is incompatible with every
  stabilized `A>0`.
- Exponential growth of the tail state is not a contradiction.
- An arbitrary pair of digit streams defines a point in `Z_2 x Z_3`, not
  automatically one ordinary diagonal integer.

## Adversarial tests

- For `A=1`, `c_K` vanishes after the initial digit while `eta_K` is nonzero
  periodic.
- For `64|A`, positive representatives in (19) must use `64`, not `0`; this
  gives `eta_K=80`.
- Appending the itinerary axis before the reciprocal axis gives the same
  diagonal digit as direct CRT, providing an independent algebraic check.

## Remaining uncertainty

Whether a nontrivial survivor stream can make the combined digits eventually
zero is exactly the unresolved ordinary-section problem.

## Suggested next attack

Combine the late periodic restriction (19)--(20) with a nonperiodicity or
complexity theorem for the itinerary digits. The reciprocal axis is rigid
after stabilization even though it is not zero.
