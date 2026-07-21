# Current integrated state

Last updated: 2026-07-21  
Integrator status: provisional synthesis by `gpt56-pro-01`  
Active issue: `#2`  
Active draft PR: `#3`

## Project maturity

The active branch contains seven mathematical research sessions. No claim has yet received independent review, so complete-looking finite theorems and identities remain `PROPOSED`.

There is currently **no positive-integer Collatz counterexample** in the repository.

## Fixed map and affine calculus

The shortcut map is

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

For a length-\(L\), weight-\(a\) parity word \(w\),

\[
T^L(n)=\frac{3^an+B(w)}{2^L}
\]

on one residue class modulo \(2^L\).

The repository has developed four compatible finite descriptions:

1. positive collision fibers;
2. induced partial radix maps;
3. negative-template rational-base returns;
4. synchronous coupling to a moving negative phase.

The fourth is now the most local and structurally transparent representation.

## Established finite resources

The branch already contains proposed results giving:

- exact finite collision atlases and sparse fibers;
- induced maps \(H_D(MB+d)=NB+d\);
- universal finite-horizon carry pumping;
- exact 2-adic/real coding and an aperiodicity obstruction;
- the run-length skeleton
  \[
  d_k+N^{u_k}C_k=d_{k+1}+M^{u_{k+1}}C_{k+1};
  \]
- inverse-signature collision codes and composition algebra;
- exponentially unbounded mildly supercritical fiber cardinality;
- the 339-branch chart `O-0005`;
- arbitrary finite 3-adic precision;
- geometry-preserving tensor amplification;
- complete alphabet projection modulo \(2^b\) for every \(b\);
- exact negative-shadow and graph-directed return criteria;
- normalized real aspect-ratio constraints.

These remove branch count, finite precision, local pumping, and finite-scale dyadic correction as principal scarcities. They do **not** produce one infinite ordinary trajectory.

# Negative shadows and renewal systems

## T-0008 — Negative-template duality

Every collision chart

\[
T^L(MQ+r_i)=NQ+s
\]

has exact negative templates

\[
u_i=M-r_i,
\qquad v=N-s
\]

satisfying

\[
T^L(-u_i)=-v
\]

and

\[
T^L(Mq-u_i)=Nq-v.
\]

At a positive boundary \(n=Nq-v\), the intrinsic return equation is

\[
Nq=Mq'+a,
\qquad a\in\{v-u_i\}.
\]

Thus collision codes are signed rational-base return languages in the ordinary negative Collatz graph.

## T-0009 — Variable-length renewal criterion

If negative templates of possibly different lengths return to one target, each supplies a dyadic quotient cylinder and an exact affine return map. A deterministic forward-invariant selector with unbounded positive quotients gives a Collatz counterexample.

A finite one-target family that covers all sufficiently large quotients must contain the all-even contracting return. Hence a successful construction must use an infinite regular language, a proper survivor set, multiple phases, or compensated contracting edges.

## T-0013 — Graph-directed returns

A finite graph of negative phases permits locally contracting edges when every reachable directed grammar cycle has product multiplier greater than one. A finite phase potential then converts the cycle condition into uniform weighted expansion above one threshold.

The missing part remains arithmetic and symbolic: construct an invariant accepted cylinder language containing one ordinary quotient.

# New session: exact synchronous phase coupling

## T-0014 — Difference/phase conjugacy

For a positive phase magnitude \(v\), define

\[
P(v)=
\begin{cases}
v/2,&v\text{ even},\\
(3v-1)/2,&v\text{ odd},
\end{cases}
\]

so that \(T(-v)=-P(v)\), and define the complementary phase map

\[
C(v)=
\begin{cases}
3v/2,&v\text{ even},\\
(v+1)/2,&v\text{ odd}.
\end{cases}
\]

Write the physical state as

\[
n=q-v.
\]

Let

\[
p=q\bmod2,
\qquad r=v\bmod2,
\qquad e=p\oplus r.
\]

Then one shortcut step is exactly

\[
\boxed{
q'=\frac{3^eq+p}{2},
\qquad
v'=\frac{3^ev+(2p-1)r}{2},
}
\]

with

\[
T(q-v)=q'-v'.
\]

This gives a precise interpretation:

- **even difference \(q\):** parity remains aligned, the phase follows its genuine negative orbit \(P\);
- **odd difference \(q\):** the first carry mismatch occurs, and the phase takes the complementary branch \(C\).

Thus the negative-shadow system is not an imposed encoding. It is the natural dynamics of the difference between an ordinary orbit and a moving negative reference orbit.

## Exact valuation acceleration

If

\[
q=2^km,
\qquad m\text{ odd},
\]

then the first \(k\) steps are synchronized. Put

\[
A_v(k)=\sum_{j=0}^{k-1}(P^j(v)\bmod2).
\]

After the synchronized segment,

\[
q_k=3^{A_v(k)}m,
\qquad
v_k=P^k(v).
\]

The next step is the first mismatch:

\[
(q,v)
\longmapsto
\left(
\frac{3^{G_v(k)}m+1}{2},
C(P^k(v))
\right),
\]

where

\[
G_v(k)=A_v(k)+1-(P^k(v)\bmod2).
\]

This is a complete countable renewal partition indexed only by the ordinary valuation \(k=\nu_2(q)\).

# Negative cycles as phase-plus-counter systems

## T-0015 — Cycle-padded mismatch towers

Let \(v_0\) lie on a negative cycle of period \(\ell\), odd count \(a\), and multiplier

\[
\Lambda=\frac{3^a}{2^\ell}>1.
\]

Fix a mismatch phase type \(k_0\pmod\ell\) and a bounded synchronized recovery from its complement phase to a selected target phase. Prepending \(t\) complete synchronized cycle circuits gives an exact return edge of length

\[
L_t=L_0+t\ell
\]

and odd count

\[
a_t=a_0+ta.
\]

Its multiplier satisfies

\[
\boxed{
\lambda_t=\lambda_0\Lambda^t.
}
\]

The cylinders for different \(t\) are disjoint because they have different exact valuations. Every fixed mismatch type therefore generates a countable geometric tower and becomes supercritical after finitely many padding levels.

This reveals the natural grammar state:

\[
\boxed{
\text{finite negative phase type}
+
\text{one nonnegative cycle-padding counter}.
}
\]

## O-0008 — Complement atlas of the negative eleven-cycle

Write the negative eleven-cycle in phase magnitudes as

\[
136\to68\to34\to17\to25\to37\to55\to82\to41\to61\to91\to136.
\]

It has multiplier

\[
\Lambda=2187/2048.
\]

After one complementary mismatch and bounded synchronized recovery:

- seven phase types enter the negative three-cycle at phase \(7\);
- four phase types return to the eleven-cycle at phase \(34\).

The complement hierarchy is

\[
\text{eleven-cycle}
\longrightarrow
\{\text{eleven-cycle},\text{three-cycle}\}
\longrightarrow
\text{fixed phase }1.
\]

From phase \(136\), the grouped base transfers are:

### To phase 7

\[
T^9(q-136)=q'-7
\]

on seven residue classes modulo \(512\), with signed equation

\[
27q=512q'+\alpha
\]

and

\[
\alpha\in\{-9,-18,-36,-216,-144,-96,-64\}.
\]

These towers first become supercritical after \(45\) complete cycle paddings.

### Back to phase 34

\[
T^{13}(q-136)=q'-34
\]

on four residue classes modulo \(8192\), with

\[
2187q=8192q'+\alpha
\]

and

\[
\alpha\in\{-1152,-6912,-4608,-3072\}.
\]

These towers first become supercritical after \(21\) paddings.

The exact atlas is finite, but no rule yet keeps one ordinary orbit inside its high-padding branches forever.

# New conservation law: Collatz–Kraft pressure

## T-0016 — Two measures on one prefix language

Let \(\mathcal W\) be a complete prefix-free parity renewal code. For a codeword \(w\), put

\[
L=L(w),
\qquad a=a(w),
\qquad \lambda(w)=\frac{3^a}{2^L}.
\]

Completeness gives the Bernoulli identity

\[
\sum_{w\in\mathcal W}p^{a(w)}(1-p)^{L(w)-a(w)}=1.
\]

At \(p=1/2\),

\[
\sum_w2^{-L(w)}=1.
\]

At \(p=3/4\),

\[
\sum_w\frac{3^{a(w)}}{4^{L(w)}}=1.
\]

Therefore, under fair 2-adic cylinder probabilities,

\[
\boxed{\mathbb E_{1/2}[\lambda]=1.}
\]

Moreover,

\[
\boxed{
\lambda(w)=
\frac{\mu_{3/4}([w])}{\mu_{1/2}([w])}.
}
\]

The real Collatz multiplier is exactly the likelihood ratio between the \(3/4\)-odd and fair parity measures.

When the mean return length is finite,

\[
\mathbb E_{1/2}[a]=\frac12\mathbb E_{1/2}[L]
\]

and

\[
\boxed{
\mathbb E_{1/2}[\log\lambda]
=\frac12\log(3/4)\,\mathbb E_{1/2}[L]<0.
}
\]

Thus a complete renewal code has mean multiplier one but strictly negative typical logarithmic growth. Every positive-growth survivor language is Haar-null.

## Graph pressure matrices

For return edges \(e:i\to j\), define

\[
\mathcal A_s(i,j)
=
\sum_{e:i\to j}2^{-L_e}\lambda_e^s.
\]

Then:

- \(\mathcal A_0\) measures fair 2-adic cylinder coverage;
- \(\mathcal A_1\) measures the \(3/4\)-odd tilted mass;
- a complete outgoing prefix code makes both row-stochastic;
- a candidate exceptional grammar should be scored by both pressure operators, not branch count or cycle multiplier alone.

This identifies the true construction target as an **entropy-thin, pressure-positive exceptional language containing one ordinary finite boundary**.

# Computational state

- `X-0001`: consecutive collision bundles.
- `X-0002`: complete finite fibers through depth 22.
- `X-0003`: inverse-signature construction and the 339-branch chart.
- `X-0004`: offset tensors and arbitrary-precision atomic codes.
- `X-0005`: complete dyadic projection through \(b=5\).
- `X-0006`: negative-template identities, renewal equations, and aspect ratios.
- `X-0007`: exact aspect-ratio census and the negative-136 chart.
- `X-0008`: synchronous coupling, valuation acceleration, every eleven-cycle complement phase, padded towers, direct physical iteration, and Kraft identities.

All programs use exact Python integers and the standard library only.

# Central unresolved step

The project still lacks a **finite-boundary regeneration theorem**.

The strongest current construction target is:

> Build a finitely generated exceptional grammar whose control state is a finite negative phase plus a cycle-padding stack, whose accepted graph has positive real pressure and cycle growth, and whose language contains one explicitly certified ordinary positive quotient.

This requires all of:

1. exact cylinder and phase closure;
2. padding counters that remain above edge-specific growth thresholds;
3. prevention or compensation of descent to contracting phases;
4. an ordinary finite boundary, not merely a 2-adic path;
5. positive graph growth despite negative typical drift of complete coverage.

# Immediate priorities

1. **Padding-stack substitution.** Search for a finite rule on mismatch types that maps accepted high-padding edges to accepted high-padding edges.
2. **Multi-mismatch automaton.** Treat failure of the synchronized recovery congruence as another phase transition rather than discarding it.
3. **Pressure-directed pruning.** Compute \(\mathcal A_0\), \(\mathcal A_1\), cycle products, and phase potentials for every candidate subgrammar.
4. **Ordinary survivor certificate.** Develop a theorem showing that a finitely generated exceptional language contains one finite ordinary quotient.
5. **Complement hierarchy.** Determine whether transitions to the three-cycle and fixed phase can be repaired by later high-padding eleven-cycle returns.
6. **Independent audit.** Reconstruct `T-0014`--`T-0016`, `O-0008`, and `X-0008`, especially the exact pair conjugacy, padding congruence, and Kraft differentiation.
