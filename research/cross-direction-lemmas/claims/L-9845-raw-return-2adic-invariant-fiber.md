# L-9845 — Unique 2-adic invariant fiber of the raw H return

Claim ID: `L-9845`  
Title: The `30/(60 or 70)` return has a unique compatible 2-adic fiber with exact contraction rate and valuation nine  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: exact H cylinder concatenation; `L-9801`, `L-9841`  
Scope: the 2-adic endpoint fiber of the raw `{30,60,70}` multiplier architecture  
Related counterexample candidates: none

## Definitions

Use the raw phase interval and return map of `L-9841`:

\[
\mathcal I=\left(1,\frac98\right],
\qquad
P(R)=
\begin{cases}
\dfrac98\xi R,&1<R\le\xi^{-1},\\[1mm]
\xi R,&\xi^{-1}<R\le9/8,
\end{cases}
\tag{1}
\]

where

\[
\xi=\frac{3^{22}}{2^{35}},
\qquad
\frac89<\xi<1.
\tag{2}
\]

At phase `R`, append the macro suffix

\[
Z_{r(R)}=30\,r(R)0,
\qquad
r(R)=
\begin{cases}
7,&1<R\le\xi^{-1},\\
6,&\xi^{-1}<R\le9/8.
\end{cases}
\tag{3}
\]

Write its normalized exact H data as

\[
F_r(x)=\frac{\mathcal V_rx+\mathcal B_r}{\mathcal U_r},
\qquad r\in\{6,7\}.
\tag{4}
\]

## Statement

### 1. Exact macro-suffix data

The two macro branches have

\[
\boxed{
\begin{aligned}
\mathcal U_r&=2^{k_r},
&k_r&=3r+17,\\
\mathcal V_r&=3^{2r+10},
&\mathcal B_r&=7\,2^9
\left(3^{2r+2}+2^{3r+4}\right).
\end{aligned}
}
\tag{5}
\]

Thus

\[
\boxed{k_6=35,
\qquad k_7=38,}
\tag{6}
\]

and

\[
\boxed{\nu_2(\mathcal B_6)=\nu_2(\mathcal B_7)=9.}
\tag{7}
\]

Let

\[
\mathcal A_r
=\left[-\mathcal B_r\mathcal V_r^{-1}\right]_{\mathcal U_r}
\in[0,\mathcal U_r)
\tag{8}
\]

be the canonical input of `Z_r`. The forward branch is a bijection

\[
\boxed{
F_r:
\mathcal A_r+\mathcal U_r\mathbb Z_2
\longrightarrow\mathbb Z_2,
}
\tag{9}
\]

with inverse

\[
\boxed{
G_r(y)
=\mathcal V_r^{-1}
(\mathcal U_ry-\mathcal B_r).
}
\tag{10}
\]

### 2. Exact inverse contraction and forward valuation loss

For all `y,tilde y in Z_2`,

\[
\boxed{
\nu_2\!\left(G_r(y)-G_r(\widetilde y)\right)
=k_r+\nu_2(y-\widetilde y).
}
\tag{11}
\]

Equivalently, if `x,tilde x` lie in the same forward cylinder in (9), then

\[
\boxed{
\nu_2\!\left(F_r(x)-F_r(\widetilde x)\right)
=\nu_2(x-\widetilde x)-k_r.
}
\tag{12}
\]

Every inverse return contracts the standard 2-adic metric by exactly
`2^(-35)` or `2^(-38)`. In particular, the inverse graph transform contracts
uniformly by at least `2^(-35)`.

### 3. Unique invariant 2-adic graph

There is a unique function

\[
\boxed{\alpha:\mathcal I\longrightarrow\mathbb Z_2}
\tag{13}
\]

such that

\[
\boxed{
\alpha(R)=G_{r(R)}(\alpha(P(R))),
}
\tag{14}
\]

or equivalently

\[
\boxed{
F_{r(R)}(\alpha(R))=\alpha(P(R)).
}
\tag{15}
\]

This graph is the unique 2-adic endpoint fiber compatible with the entire
future raw-return itinerary. Explicitly, if

\[
R_i=P^i(R),
\qquad
r_i=r(R_i),
\tag{16}
\]

then

\[
\boxed{
\alpha(R)
=-
\sum_{i=0}^{\infty}
\frac{\mathcal B_{r_i}}{\mathcal V_{r_i}}
\prod_{t=0}^{i-1}
\frac{\mathcal U_{r_t}}{\mathcal V_{r_t}}.
}
\tag{17}
\]

The series converges in `Z_2` uniformly in the phase.

### 4. Exact Sturmian contraction rate

Put

\[
K_n=\sum_{i=0}^{n-1}k_{r_i}
=35N_6(n)+38N_7(n),
\tag{18}
\]

and define the depth-`n` backward approximation with terminal fiber `t` by

\[
\alpha_n(R;t)
=G_{r_0}\circ G_{r_1}\circ\cdots\circ G_{r_{n-1}}(t).
\tag{19}
\]

For distinct terminal fibers,

\[
\boxed{
\nu_2\!\left(
\alpha_n(R;t)-\alpha_n(R;\widetilde t)
\right)
=K_n+\nu_2(t-\widetilde t).
}
\tag{20}
\]

Let

\[
\ell=\log(9/8),
\qquad
\delta=\log(1/\xi),
\qquad
\rho=\frac\delta\ell.
\tag{21}
\]

If `x_i=log(R_i)/ell in (0,1]`, the branch count telescopes as

\[
\boxed{
N_7(n)=n\rho+x_n-x_0.
}
\tag{22}
\]

Consequently

\[
\boxed{
K_n=\kappa n+3(x_n-x_0),
\qquad
\kappa=35+3\rho,
}
\tag{23}
\]

and

\[
\boxed{|K_n-\kappa n|<3.}
\tag{24}
\]

The invariant graph is therefore selected at the exact asymptotic rate
`kappa` bits per raw return, with a universal discrepancy smaller than three
bits.

### 5. Exact valuation of the invariant fiber

For every phase,

\[
\boxed{\nu_2(\alpha(R))=9.}
\tag{25}
\]

More precisely, the zero-terminal approximants satisfy

\[
\boxed{
\nu_2\!\left(\alpha_n(R;0)-\alpha(R)\right)
=K_n+9.
}
\tag{26}
\]

Thus every compatible endpoint has the phase-independent low-bit constraint

\[
\boxed{
\alpha(R)\equiv512\pmod{1024}.
}
\tag{27}
\]

This is a genuine ordinary-integer obstruction: an ordinary endpoint not
congruent to `512 modulo 1024` cannot begin an infinite integral macro-return tail
for the raw return architecture.

### 6. Ordinary-integer and stabilization criterion

For a fixed phase `R`, the following are equivalent:

1. `alpha(R)` is an ordinary nonnegative integer.
2. There is an ordinary nonnegative integer `N_0` such that the deterministic
   recurrence

   \[
   N_{i+1}=F_{r_i}(N_i)
   \tag{28}
   \]

   is integral for every `i>=0`.
3. The canonical input residues of the finite composite words

   \[
   Z_{r_0}Z_{r_1}\cdots Z_{r_{n-1}}
   \tag{29}
   \]

   eventually stabilize as ordinary nonnegative integers.

When these conditions hold, `N_0=alpha(R)` is unique, every `N_i` is positive
after the first step, and

\[
\nu_2(N_i)=9
\qquad(i\ge0).
\tag{30}
\]

For an already constructed exact prefix whose current endpoint is `Y` and
whose multiplier phase is `R`, all future macro maps remain integral --
equivalently, all future macro-cylinder conditions hold -- if and only if

\[
\boxed{Y=\alpha(R)\in\mathbb Z_{\ge0}.}
\tag{31}
\]

Hence the remaining ordinary-seed problem is exactly whether this unique
2-adic invariant graph meets the ordinary nonnegative section at a physical
prefix endpoint. The theorem supplies the unique graph and its necessary
valuation, but does not assert that this intersection is empty or nonempty.

### 7. Strong separation, recursive decoding, and dimension

Put

\[
d_r=-\frac{\mathcal B_r}{\mathcal V_r},
\qquad
\lambda_r=\frac{\mathcal U_r}{\mathcal V_r},
\qquad
G_r(y)=d_r+\lambda_r y.
\tag{32}
\]

The two inverse branches separate four bits before either contraction scale:

\[
\boxed{
d_6-d_7=-\frac{7\,2^{31}}{3^{24}},
\qquad
\nu_2(d_6-d_7)=31.
}
\tag{33}
\]

More explicitly, with `c=0x0B6EB200`,

\[
\boxed{
d_7\equiv c,
\qquad
d_6\equiv c+2^{31}=\mathtt{0x8B6EB200}
\pmod{2^{32}}.
}
\tag{34}
\]

Consequently, if `q=G_r(q')`, then its branch and successor are decoded
recursively by

\[
\boxed{
r=
\begin{cases}
7,&q\equiv\mathtt{0x0B6EB200}\pmod{2^{32}},\\
6,&q\equiv\mathtt{0x8B6EB200}\pmod{2^{32}},
\end{cases}
\qquad
q'=F_r(q).
}
\tag{35}
\]

For an address `omega=(omega_0,omega_1,...) in {6,7}^N`, define

\[
\pi(\omega)
=\lim_{n\to\infty}
G_{\omega_0}\circ\cdots\circ G_{\omega_{n-1}}(0),
\qquad
\mathscr K=\pi(\{6,7\}^{\mathbb N}).
\tag{36}
\]

If two addresses first differ at index `n`, then

\[
\boxed{
\nu_2\!\left(\pi(\omega)-\pi(\widetilde\omega)\right)
=31+\sum_{i=0}^{n-1}k_{\omega_i}.
}
\tag{37}
\]

Thus `pi` is injective, the inverse system is strongly separated, and its
full-shift attractor has Hausdorff dimension

\[
\boxed{
\dim_H\mathscr K=s,
\qquad
2^{-35s}+2^{-38s}=1,
\qquad
s\approx0.0274133130.
}
\tag{38}
\]

In contrast, the subset selected by the fixed-slope rotation has

\[
\boxed{
\mathscr K_{\rm St}
=\{\alpha(R):R\in\mathcal I\},
\qquad
\dim_H\mathscr K_{\rm St}=0.
}
\tag{39}
\]

### 8. Interpretation boundary

The contraction in this theorem belongs to the inverse 2-adic endpoint
fiber. It does not contradict the positive real affine drift of `L-9843`:
the two results use different metrics and opposite time orientations. The
existence of the 2-adic graph is automatic from inverse contraction, whereas
ordinary nonnegative realization remains the discrete intersection criterion
in (31). The decoder (35) acts on the successive renormalized endpoints
`q_i`, not on disjoint blocks of the original endpoint's binary expansion.
An eventually periodic address does give a rational 2-adic endpoint, but the
converse is not proved. In particular, aperiodicity of the Sturmian address
alone does not exclude a rational or ordinary endpoint.

## Proof

For a completed suffix `r0`, `L-9841` gives

\[
U_r=2^{3r+4},
\qquad
V_r=3^{2r+2},
\qquad
B_r=7\,2^{3r}.
\tag{40}
\]

Compose `30` first and `r0` second. Exact affine concatenation gives

\[
\begin{aligned}
\mathcal U_r&=U_3U_r,\\
\mathcal V_r&=V_3V_r,\\
\mathcal B_r&=V_rB_3+B_rU_3.
\end{aligned}
\tag{41}
\]

Substitution proves (5). The parenthesis in `mathcal B_r` is odd, proving (7).
Oddness of `mathcal V_r` gives the unique canonical cylinder (8)--(9), and
solving the affine equation proves (10).

Equations (5) and (32) give

\[
\begin{aligned}
d_6&=-7\,2^9\left(2^{22}3^{-22}+3^{-8}\right),\\
d_7&=-7\,2^9\left(2^{25}3^{-24}+3^{-8}\right).
\end{aligned}
\tag{42}
\]

Subtraction proves (33), and reduction modulo `2^32` proves (34). Since
`lambda_r Z_2` is contained in `2^(k_r) Z_2` and both `k_r` exceed 32, the
terminal fiber cannot alter these residues; this proves (35). If two
addresses first differ at index `n`, their two tails differ with exact
valuation 31 by (33), and their common inverse prefix adds exactly
`sum_(i<n) k_(omega_i)` to that valuation. This proves (37), including strong
separation.

The standard strong-separation similarity formula now gives (38). For (39),
the Sturmian coding has at most `n+1` words of length `n`. Their image
cylinders have diameter at most `2^(-31-35n)`. For every `t>0`, their total
`t`-content is at most
`(n+1)2^(-t(31+35n))`, which tends to zero. Hence the Hausdorff dimension is
zero. Finally, a periodic address tail is the fixed point of one rational
affine contraction `G_w(y)=a+lambda y`, hence equals `a/(1-lambda)` in
`Q`; a finite inverse prefix preserves rationality. This proves the forward
rationality implication stated in Section 8.

Subtract two inverse images in (10). Since `mathcal V_r` is odd, its inverse
is a 2-adic unit, while `mathcal U_r=2^(k_r)`. This proves (11), and inversion
proves (12).

Let `X` be the complete metric space of all functions from `I` to `Z_2` with
the uniform 2-adic metric. Define

\[
(\mathscr Gf)(R)
=G_{r(R)}(f(P(R))).
\tag{43}
\]

Equation (11) makes `mathscr G` a contraction with Lipschitz constant at most
`2^(-35)`. Banach's fixed-point theorem gives the unique graph (13)--(15).
Iterating (14) and letting the terminal term tend to zero gives (17).

Repeated use of (11) proves (20). In normalized logarithmic phase,
`L-9841/(26)` is

\[
x_{i+1}=x_i-\rho+\mathbf1_{\{r_i=7\}}.
\tag{44}
\]

Summation proves (22), and substitution in (18) proves (23)--(24).

Every summand of (17) has valuation

\[
9+K_i.
\tag{45}
\]

The first has valuation exactly nine and every later summand has strictly
larger valuation. The ultrametric inequality therefore proves (25). Apply
the exact `n`-branch contraction to the terminal difference
`0-alpha(R_n)`, which has valuation nine by (25), to obtain (26). Equation
(27) is equivalent to exact valuation nine.

It remains to prove the ordinary criterion. If `alpha(R)=N_0>=0`, equation
(15) shows inductively that (28) equals `alpha(R_i)` in `Z_2`. Divisibility in
`Z_2` of an ordinary integer numerator by the ordinary power
`mathcal U_(r_i)` is ordinary divisibility, so every `N_i` is an integer;
positivity follows from the positive affine coefficients. Conversely, any
fully integral forward orbit lies in the cylinder (9) at every stage. Pulling
it backward `n` steps and comparing it with the invariant graph gives a
difference divisible by `2^(K_n)` for every `n`, hence the initial point is
`alpha(R)`.

The canonical input of the length-`n` composite word is the canonical
representative of `alpha(R) modulo 2^(K_n)`. The stabilization criterion of
`L-9801` proves the equivalence with part 3. Equation (25), applied along the
base orbit, gives (30). Finally, integrality of every future macro map is
equivalent to satisfying the corresponding canonical input cylinder at every
stage. The already proved equivalence of parts 1 and 2 therefore gives (31)
and completes the proof. ∎

## Motivation

`L-9841` closes the raw multiplier phase and `L-9843` shows that its real
affine offset cannot close on a bounded graph. The exact dyadic endpoint
fiber behaves in the opposite way under backward time: each macro return
adds at least 35 forced low bits, producing one and only one compatible
2-adic endpoint over every phase.

The valuation-nine law is the first phase-independent arithmetic restriction
on a hypothetical ordinary endpoint for this architecture. It does not settle
ordinary realization, but it reduces that question to one explicit invariant
graph rather than an abstract branching tail tree.

## Dependency audit

- `L-9841` supplies the raw phase rotation and exact data of each completed
  suffix `r0`.
- Exact affine concatenation is recomputed in (41).
- The strong-separation Hausdorff-dimension formula for two 2-adic affine
  similarities is used in (38); the zero-dimensional Sturmian subcover is
  proved directly.
- `L-9801` is used only for the final ordinary stabilization equivalence; its
  needed canonical-residue statement is also explicit in the proof.
- No real-fiber boundedness, probabilistic independence, or empirical carry
  data are used.

## Gap audit

- Exact valuation nine is necessary, not sufficient, for ordinary
  realization.
- The invariant graph is 2-adic; it need not be continuous as a real-valued
  function across the phase cut.
- The theorem does not prove that any physical prefix endpoint lies on the
  graph.
- A unique compatible 2-adic endpoint is not automatically an ordinary
  Collatz seed.
- Aperiodicity of the recursively decoded address does not by itself prove
  2-adic irrationality or nonordinariness.

## Adversarial tests

- The macro words are `3060` and `3070`; using only the return words `60` and
  `70` gives the wrong shift lengths and offset valuation.
- Forward branches expand 2-adic distances after their low cylinder is fixed;
  contraction occurs only for the inverse maps `G_r`.
- The exact offset valuation is nine because
  `3^(2r+2)+2^(3r+4)` is odd. Later series terms begin at least 35 valuations
  higher, so cancellation cannot change (25).
- The branch-`7` count has sign `N_7(n)=n rho+x_n-x_0`; reversing that sign
  gives the wrong information rate.
- The hexadecimal decoder is applied again only after the forward
  renormalization `q_(i+1)=F_(r_i)(q_i)`; it does not identify disjoint
  32-bit blocks of the original endpoint.
- The graph criterion concerns endpoint integrality at macro checkpoints. It
  does not itself impose the remaining Collatz orbit or first-crossing
  requirements between those checkpoints.

## Remaining uncertainty

It is unknown whether `alpha(R)` is an ordinary integer for any phase on a
physical raw-return orbit. No rationality, irrationality, or transcendence
classification of the graph values is proved here.

## Suggested next attack

Prove or refute the missing converse to the easy rationality implication:
does a rational point of the strongly separated set `K` necessarily have an
eventually periodic recursively decoded address? A positive answer, combined
with the aperiodic Sturmian phase word, would turn the zero-dimensional fiber
result into a genuine ordinary-seed obstruction.
