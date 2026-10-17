# Iteration 06: renewal bridges, full boundary audit, and subcritical future demand

All theorem-level claims remain `PROPOSED` pending independent review. This
iteration follows the completion-height advice in the literature wave-5 audit:
move a centered ordinary room to its first nonzero section, write the smallest
simultaneous `2`-/`3`-adic bridge, and search for an integral height before
adding any further analytic machinery.

The exact block coordinates are those of `D-9501`:

\[
p_n=2^{3r_n+2}u_n,
\qquad u_n\equiv1\pmod4,
\qquad p_n\equiv1\pmod3,
\]

\[
2^{3r_{n+1}+2}u_{n+1}-3^{2r_n+1}u_n=1.
\tag{1}
\]

---

## L-9517: Complete finite-code boundary classification

**Claim ID:** `L-9517`  
**Title:** Every nongenuine point of the H ghost closure is a nonpositive finite-code boundary  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-22  
**Dependencies:** `L-9514`  
**Scope:** the complete H ghost closure

### Statement

For

\[
\phi_r(x)=2^{3r+2}3^{-(2r+1)}(x-1),
\qquad r\ge0,
\]

let `G_*` be the set of ghosts of genuine infinite itineraries and let
`G=closure(G_*)` in `Z_2`. For a finite word `w`, let `Phi_w` be the
corresponding composition of inverse branches, and let `Phi_empty` be the
identity. Then

\[
\boxed{
G=G_*\sqcup\{\Phi_w(0):w\text{ finite, including the empty word}\}.
}
\tag{2}
\]

Every finite-code boundary is rational in the real embedding, with

\[
\Phi_\varnothing(0)=0,
\qquad
\boxed{\Phi_w(0)<0\quad(w\ne\varnothing).}
\tag{3}
\]

In particular, no positive ordinary integer in `G` is a boundary point: every
positive ordinary point of `G` is the ghost of a genuine infinite itinerary.

### Proof

The exact ghost recursion is

\[
G=\{0\}\cup\bigcup_{r\ge0}\phi_r(G).
\tag{4}
\]

Every nonzero point in the `r`-th image has exact valuation `3r+2`. Hence the
first inverse branch is unique. Repeatedly invert it. Either the process reaches
`0` after finitely many branches, yielding `Phi_w(0)`, or it continues
forever. In the latter case the accumulated contraction valuation tends to
infinity, so the nested finite compositions converge to the unique ghost of
the resulting infinite code. This proves exhaustion. Exact branch valuations
also prove disjointness.

Each branch has positive rational coefficient in the real embedding, and

\[
x\le0\Longrightarrow\phi_r(x)<0.
\]

Induction on the finite word length proves (3). QED.

### Repair to T-9510

The proof of `T-9510` must use this complete boundary classification, not only
the outer sequence `phi_0^q(0)`. If the monotone minimum `nu_K` stabilizes at
an integer `P>=16`, compactness puts `P` in `G`; (2)--(3) then force `P` to be
a genuine infinite-code ghost.

---

## L-9518: Dual centered-renewal bridge and integral sign law

**Claim ID:** `L-9518`  
**Title:** Consecutive nonzero letters share one dual-valuation bridge and one integral renewal height  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-22  
**Dependencies:** `D-9501`, `L-9516`  
**Scope:** every exact positive H orbit

### Setup

Let

\[
t_0<t_1<t_2<\cdots
\]

be the indices at which `r_(t_k)>0`. Put

\[
R_k=r_{t_k},
\qquad
L_k=t_{k+1}-t_k,
\qquad
U_k=u_{t_k}.
\tag{5}
\]

Thus all letters strictly between `t_k` and `t_(k+1)` are zero.

### Statement

There is a positive integer `W_k=5 mod 6` such that

\[
\boxed{
9^{R_k}U_k-1=4^{L_k}W_k,
\qquad
2^{3R_{k+1}}U_{k+1}-1=3^{L_k}W_k.
}
\tag{6}
\]

Therefore

\[
\boxed{
v_2(9^{R_k}U_k-1)=2L_k,
\qquad
v_3(2^{3R_{k+1}}U_{k+1}-1)=L_k.
}
\tag{7}

Define the positive integral renewal height

\[
\boxed{Z_k=(p_{t_k}-4)/4=2^{3R_k}U_k-1.}
\tag{8}

Let

\[
\kappa={\log(4/3)\over\log(9/8)},
\qquad
C_k=R_k-\kappa L_k,
\]

\[
A_k=(9/8)^{C_k},
\qquad
c_k=(3/4)^{L_k}.
\]

Then

\[
\boxed{Z_{k+1}=A_kZ_k+(A_k-c_k).}
\tag{9}

On a nonperiodic orbit,

\[
\boxed{
\operatorname{sgn}(Z_{k+1}-Z_k)=\operatorname{sgn}(C_k).
}
\tag{10}

Moreover,

\[
\boxed{
\log Z_{k+1}-\log Z_k
=C_k\log(9/8)+\varepsilon_k,
}
\tag{11}

where

\[
0<\varepsilon_k
=
\log\left(1+{1-(8/9)^{R_k}\over Z_k}\right)
<{1\over Z_k}.
\tag{12}

Along a hypothetical nonperiodic survivor, `sum epsilon_k` converges and

\[
\boxed{
{Z_k\over(9/8)^{K_{t_k}}}\longrightarrow {Q_\infty\over4}>0.
}
\tag{13}

### Proof

The nonzero departure gives

\[
p_{t_k+1}-4=3(9^{R_k}U_k-1).
\]

Each following zero letter multiplies `p-4` by `3/4`. At arrival,

\[
p_{t_{k+1}}-4=4(2^{3R_{k+1}}U_{k+1}-1).
\]

Clearing `4^(L_k-1)` yields

\[
4^{L_k}(2^{3R_{k+1}}U_{k+1}-1)
=3^{L_k}(9^{R_k}U_k-1).
\]

Coprimality gives the common integer `W_k`; the two residual units show
`W_k=5 mod 6`, proving (6)--(7).

Eliminate `W_k` from (6), substitute
`U_k=(Z_k+1)/8^{R_k}`, and use the definition of `kappa`; this gives (9).
If `C_k>0`, both terms in

\[
Z_{k+1}-Z_k=(A_k-1)Z_k+(A_k-c_k)
\]

are positive. If `C_k<0`, then

\[
Z_{k+1}=A_k(Z_k+1)-c_k<Z_k+1.
\]

The endpoints are integers, so `Z_(k+1)<=Z_k`; equality repeats the exact
state and is impossible on a nonperiodic orbit. This proves (10). Factoring
(9) proves (11)--(12).

Finally,

\[
{Z_k\over M_{t_k}}
={p_{t_k}/4-1\over M_{t_k}}
={Q_{t_k}\over4}-{1\over M_{t_k}}.
\]

`T-9502` gives `Q_i->Q_infinity` and `M_i->infinity`, proving (13). Telescope
(11) against the capital increments to obtain convergence of the positive
error sum. QED.

### Centered-room star

If a positive ordinary ghost begins in centered room

\[
P=4+4^{q+1}z,
\qquad z>0\text{ odd},
\qquad 3\mid z,
\]

write `z=3X` and let `R` be the first nonzero letter. Then, with `a=q+1`,

\[
\boxed{3^aX+1=8^RU.}
\tag{14}

If the following zero room has length `b` and bridge core `Y`, then

\[
\boxed{4^bY+1=9^RU.}
\tag{15}

Eliminating the central core gives the exact two-place equation

\[
\boxed{
8^R4^bY-9^R3^aX=9^R-8^R.
}
\tag{16}

This is the smallest simultaneous exponential equation governing one centered
room, as requested by the wave-5 literature audit.

---

## T-9511: Subcritical future-core demand identity

**Claim ID:** `T-9511`  
**Title:** In the sole subcritical escape regime, current valuation is exactly a future geometric-mean core demand  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-22  
**Dependencies:** `T-9505`; the subcritical conclusion of `T-9509`  
**Scope:** a hypothetical nonperiodic survivor satisfying `r_n/c_*^n->0`

### Definitions

Put

\[
c=c_*={\log9\over\log8},
\qquad a=1/c,
\qquad h_n=\log_8u_n.
\]

Let

\[
X_n=3^{2r_n+1}u_n,
\]

\[
\delta_n=
\log_8{4X_n\over3(X_n+1)},
\qquad
\delta_0=\log_8(4/3),
\]

\[
\beta_n=\delta_0-\delta_n
=\log_8(1+1/X_n)>0.
\tag{17}

The exact core recurrence gives

\[
\boxed{h_{n+1}-h_n=cr_n-r_{n+1}-\delta_n.}
\tag{18}

Define the exponentially weighted future mean and toll

\[
\overline h_n=(1-a)\sum_{j=1}^\infty a^{j-1}h_{n+j},
\]

\[
B_n=\sum_{j=0}^\infty a^{j+1}\beta_{n+j}.
\tag{19}

The sums converge by the discounted core budget in `T-9505`.

### Statement

In the subcritical regime

\[
r_n/c^n\longrightarrow0,
\]

one has the exact identity

\[
\boxed{
\overline h_n-h_n
=c\bigl(r_n-\kappa+B_n\bigr).
}
\tag{20}

Equivalently, the future weighted geometric mean of the odd cores is

\[
\boxed{
\prod_{j=1}^\infty
u_{n+j}^{(1-a)a^{j-1}}
=
u_n\,8^{c(r_n-\kappa+B_n)}.
}
\tag{21}

In particular,

\[
\boxed{
\sup_{j\ge1}\log_8u_{n+j}
\ge h_n+c(r_n-\kappa).
}
\tag{22}

Thus every large current valuation forces a later odd-core spike exponential
in `r_n`.

The same identity gives an exact remaining-budget formula:

\[
\boxed{
\sum_{j=1}^\infty c^{-(n+j)}h_{n+j}
={c^{-n}\over c-1}
\left[h_n+c(r_n-\kappa+B_n)\right].
}
\tag{23}

### Proof

For finite `m`, variation of constants in (18) gives

\[
r_n=c^{-m}r_{n+m}
+
\sum_{j=0}^{m-1}c^{-(j+1)}
(h_{n+j+1}-h_{n+j}+\delta_{n+j}).
\]

The first term tends to zero by subcriticality. The discounted core budget
permits passage to the convergent infinite sums. The logarithmic differences
telescope with geometric weights:

\[
\sum_{j\ge0}a^{j+1}(h_{n+j+1}-h_{n+j})
=a(\overline h_n-h_n).
\]

Also

\[
\sum_{j\ge0}a^{j+1}\delta_0
={\delta_0\over c-1}=\kappa.
\]

Subtracting the positive toll `B_n` proves (20). Exponentiation proves (21),
and a weighted average cannot exceed the supremum, proving (22). Equation
(23) is the same identity after rewriting the weighted sum. QED.

### Rounded-deficit corollary

Let

\[
s_n=\lceil cr_n\rceil-r_{n+1},
\qquad
\theta_n=\lceil cr_n\rceil-cr_n,
\qquad
 d_n=(s_n)^+.
\]

Subcritical variation of constants also gives

\[
\boxed{
r_n
=\sum_{j=0}^\infty c^{-(j+1)}(s_{n+j}-\theta_{n+j}).}
\tag{24}

Consequently

\[
\boxed{
\sup_{m\ge n}d_m\ge(c-1)r_n.
}
\tag{25}

Hence bounded rounded deficits on a tail force bounded letters on that tail:

\[
\sup_{m\ge n}d_m\le D
\Longrightarrow
r_n\le D/(c-1).
\tag{26}

At a positive-deficit step, (18) gives

\[
\log_8(u_{m+1}/u_m)>d_m-1-\delta_0.
\]

Combining with (25), every current `r_n` forces some later core jump satisfying

\[
\boxed{
\sup_{m\ge n}
\log_8{u_{m+1}\over u_m}
>
(c-1)r_n-1-\delta_0.
}
\tag{27}

This is a completion-height dichotomy: the only remaining subcritical ray must
contain unbounded deficit blocks and correspondingly unbounded multiplicative
core resets.

---

## T-9512: Minimal nonperiodic survivor has a small relative toll

**Claim ID:** `T-9512`  
**Title:** Plastic sparsity makes the real toll of a least nonperiodic survivor sublinear  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-22  
**Dependencies:** `T-9506`, `L-9504`  
**Scope:** conditional on existence of a nonperiodic infinite exact orbit

### Statement

Suppose nonperiodic infinite exact orbits exist, and let `P` be the least
starting state among them. Every state on its forward orbit is again a
nonperiodic survivor and hence is at least `P`. Let

\[
s=\log_2\rho<1,
\]

where `rho^3=rho+1`. Then

\[
\boxed{
\sum_{n\in\mathcal I,\ n\ge P}{1\over n}
=O(P^{s-1}).
}
\tag{28}

For the orbit multiplier and toll variables,

\[
Q_\infty
=P+\sum_{k\ge1}{1\over M_k},
\]

one has

\[
\boxed{
0<\log(Q_\infty/P)=O(P^{s-1}),
}
\tag{29}

and therefore

\[
\boxed{Q_\infty-P=O(P^s).}
\tag{30}

### Proof

Partial summation applied to the plastic count

\[
A_\infty(X)=O(X^s)
\]

proves the harmonic-tail estimate (28). The states of a nonperiodic orbit are
distinct. By minimality they all lie in the indicated tail of `I`. The
Toll--Euler product gives

\[
{Q_\infty\over P}
=
\prod_{j\ge1}(1-1/p_j)^{-1}.
\]

Since `p_j>=P>=16`,

\[
-\log(1-1/p_j)\le {16\over15p_j}.
\]

Summing and using (28) proves (29). Exponentiation proves (30). QED.

---

## Q-9507: Subcritical renewal finite trap

**Claim ID:** `Q-9507`  
**Title:** Convert the future-core demand into an integral finite-trap height  
**Status:** `IDEA`  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-22  
**Dependencies:** `L-9518`, `T-9511`

### Target

The real-valued future mean in (20) is an exact transformed height, but it is
not integral. Find an integer or finite-state refinement `H_k` of the renewal
variables

\[
(Z_k,R_k,L_k,U_k,W_k)
\]

such that an eventual zero-carry subcritical ray satisfies

\[
|H_{k+1}|\le c_0|H_k|+d,
\qquad c_0<1,
\]

outside a finite set, and audit the finite trap for legal transitions. This
would instantiate the completion-height theorem used successfully in the
residue-cylinder work elsewhere in the repository.

A viable height must account for the unbounded deficit blocks in (25)--(27):
raw `u`, raw `Z`, and raw capital cannot contract uniformly. The simultaneous
star (14)--(16) is the smallest exact arithmetic system on which to search.
