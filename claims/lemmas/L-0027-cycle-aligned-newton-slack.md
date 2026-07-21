# L-0027 — Cycle-aligned Newton doubling with one-cycle slack

Claim ID: `L-0027`  
Title: Exact finite-word generation of every connector inverse in one dyadic stage  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-0016`, `L-0024`, `L-0026`  
Scope: the four phase-`-34` self-return towers of the negative eleven-cycle  
Related counterexample candidates: none

## Universal tower exponents

For each of the four phase-`-34` self-return tower types, the finite core constants satisfy

\[
k_0+r+1=11,
\qquad
g_0+b=7.
\]

Consequently every tower instance at padding height \(t\ge0\) has

\[
\boxed{K_t=11(t+1),}
\tag{1}
\]

\[
\boxed{G_t=7(t+1).}
\tag{2}
\]

The four types differ only in their finite anchors and recovery cores. Their binary and ternary exponent schedules are identical.

## Dyadic-stage precision

Use the corrected 256-step stage of `L-0024`. Put

\[
B_m=2^m,
\qquad
d_m=2^{m-8},
\]

and let the first target height of stage \(m\) be

\[
s_m=B_m+d_m.
\tag{3}
\]

Define the first-target connector precision

\[
\boxed{Q_m=K_{s_m}=11(s_m+1).}
\tag{4}
\]

Then

\[
s_{m+1}=2s_m
\]

and therefore

\[
\boxed{Q_{m+1}=2Q_m-11.}
\tag{5}
\]

A Newton lift from \(Q_m\) to \(2Q_m\) bits therefore supplies the entire next-stage first-target precision with exactly eleven spare bits.

Moreover every target depth inside stage \(m\) is at most

\[
K_{2B_m}=11(2B_m+1),
\]

and

\[
\boxed{K_{2B_m}<2Q_m.}
\tag{6}
\]

Thus the same full Newton lift contains every connector inverse required anywhere in the current 256-transition stage.

## Moving inverse and full Newton workspace

Put

\[
E_m=7B_m,
\qquad
N_m=3^{E_m},
\]

so that

\[
\boxed{N_{m+1}=N_m^2.}
\tag{7}
\]

Let

\[
\boxed{x_m=[N_m^{-1}]_{Q_m}}
\tag{8}
\]

be the least nonnegative inverse of \(N_m\) modulo \(2^{Q_m}\).

First perform the ordinary Newton lift of the **same** inverse:

\[
\boxed{
\widetilde x_m
\equiv
x_m(2-N_mx_m)
\pmod{2^{2Q_m}}.
}
\tag{9}
\]

Then

\[
\boxed{
N_m\widetilde x_m
\equiv1
\pmod{2^{2Q_m}}.
}
\tag{10}
\]

The complete next-stage inverse prefix is obtained by squaring and truncating:

\[
\boxed{
x_{m+1}
=
[\widetilde x_m^2]_{Q_{m+1}}.}
\tag{11}
\]

Indeed,

\[
\boxed{
N_{m+1}x_{m+1}
\equiv1
\pmod{2^{Q_{m+1}}}.
}
\tag{12}
\]

The distinction between \(x_m\) and \(\widetilde x_m\) is essential. The shorter word \(x_m\) suffices for the first connector only; the full \(2Q_m\)-bit Newton workspace is what supplies the deeper connectors later in the stage.

## Exact compilation of every within-stage inverse

For

\[
t_{m,j}=B_m+jd_m,
\qquad0\le j\le256,
\]

put

\[
\boxed{
a_m=[3^{-7d_m}]_{2Q_m}.}
\tag{13}
\]

Then at every precision \(K\le2Q_m\),

\[
\boxed{
3^{-7t_{m,j}}
\equiv
\widetilde x_m a_m^j
\pmod{2^K}.
}
\tag{14}
\]

Since

\[
G_{t_{m,j}}=7(t_{m,j}+1),
\]

the inverse needed by a connector from this source is

\[
\boxed{
3^{-G_{t_{m,j}}}
\equiv
3^{-7}\widetilde x_m a_m^j
\pmod{2^K}.
}
\tag{15}
\]

Let tower type \(i\) be the source at height \(t_{m,j}\), and type \(k\) the target at height \(t_{m,j+1}\). Write their anchors as

\[
B_i(t_{m,j}),
\qquad
A_k(t_{m,j+1}),
\]

and put

\[
K=K_{t_{m,j+1}}.
\]

The canonical connector seed is therefore the finite residue

\[
\boxed{
\eta_{m,j}^{i\to k}
=
\left[
\bigl(A_k(t_{m,j+1})-B_i(t_{m,j})\bigr)
3^{-7}\widetilde x_m a_m^j
\right]_K.
}
\tag{16}
\]

Its cap is

\[
\boxed{
\theta_{m,j}^{i\to k}
=
\frac{
B_i(t_{m,j})
+3^{7(t_{m,j}+1)}\eta_{m,j}^{i\to k}
-A_k(t_{m,j+1})
}{2^K}.
}
\tag{17}
\]

Equations (9), (13), and (16)–(17) generate all sixteen source/target connector tiles at every one of the 256 stage positions by finite arithmetic.

## No completion oracle

Every quantity above is a finite ordinary integer. Starting with one finite pair

\[
(m_0,x_{m_0}),
\]

iteration of

\[
x_m
\longmapsto
\widetilde x_m
\longmapsto
x_{m+1}
\]

generates every later connector-control word exactly. No digit of an infinite 2-adic inverse is assumed as input.

## Proof

Equations (1)–(2) follow directly from the four tower cores:

\[
(k_0,r,g_0,b)
=
(5,5,5,2),
(6,4,4,3),
(7,3,5,2),
(8,2,6,1).
\]

Every row gives \(k_0+r+1=11\) and \(g_0+b=7\). Adding \(11t\) and \(7t\) proves (1)–(2).

Since

\[
s_{m+1}
=2^{m+1}+2^{m-7}
=2(2^m+2^{m-8})
=2s_m,
\]

we obtain

\[
Q_{m+1}
=11(2s_m+1)
=2\cdot11(s_m+1)-11
=2Q_m-11,
\]

proving (5).

Also

\[
2Q_m-K_{2B_m}
=22(B_m+d_m+1)-11(2B_m+1)
=22d_m+11>0,
\]

which proves (6).

Equation (9) is the Newton specialization of `L-0026`; it proves (10). Since \(\widetilde x_m^2\) is an inverse of \(N_m^2=N_{m+1}\) modulo \(2^{2Q_m}\), and

\[
Q_{m+1}<2Q_m,
\]

truncation proves (11)–(12).

Finally,

\[
3^{-7t_{m,j}}
=3^{-7B_m}(3^{-7d_m})^j,
\]

which proves (14). Multiplication by \(3^{-7}\) gives (15). Substitution in the connector congruence proves (16), and exact division gives (17). ∎

## General cycle-aligned principle

For a negative cycle of length \(\ell\), a doubling scale with precision

\[
Q_m=\ell(s_m+1),
\qquad
s_{m+1}=2s_m,
\]

satisfies

\[
Q_{m+1}=2Q_m-\ell.
\]

Newton lifting doubles binary precision, leaving exactly one cycle block of \(\ell\) spare bits. In the present chart, \(\ell=11\).

## Strategic consequence

The entire connector-prefix track is now a finite proof object generated forward from the current finite prefix. The corrected compiler has enough precision for:

1. every connector in the current 256-step stage;
2. the first connector of the next stage;
3. eleven additional certificate bits.

The unresolved problem is no longer how to know the next connector bits. It is how to make the **ordinary physical residual** land in those computed connector cylinders forever.

## Gap audit

- The compiler generates control prefixes and caps; it does not alter the marked Collatz integer.
- Exact knowledge of the required residue is not proof that the physical residual has that residue.
- The residual integrality and positivity recurrence remains the load-bearing arithmetic selector problem.

## Adversarial tests

`X-0013` verifies (5)–(17) for several dyadic stages and representative stage positions, including the deepest connectors. Direct modular inversion and direct connector construction agree exactly.