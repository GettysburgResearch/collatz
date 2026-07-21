# Current integrated state

Last updated: 2026-07-21  
Integrator status: provisional synthesis by `gpt56-pro-01`  
Active issue: `#2`  
Active draft PR: `#3`

## Project maturity

The active branch contains nine mathematical research sessions. No claim has yet received independent review, so complete-looking finite theorems and identities remain `PROPOSED`.

There is currently **no positive-integer Collatz counterexample** in the repository.

## Fixed map

The shortcut map is

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

For a length-\(L\), weight-\(a\) physical parity word \(w\),

\[
T^L(n)=\frac{3^an+B(w)}{2^L}
\]

on one residue class modulo \(2^L\).

## Research arc before the current session

The branch already contains proposed results giving:

- exact finite collision atlases and sparse collision fibers;
- induced partial radix maps;
- universal finite-horizon carry pumping;
- dual real/2-adic coding and an aperiodicity obstruction;
- the exact run-length/cofactor skeleton;
- inverse-signature collision codes and a composition algebra;
- exponentially unbounded mildly supercritical branch count;
- arbitrary finite 3-adic precision;
- geometry-preserving tensor amplification;
- complete collision-alphabet projection modulo \(2^b\) for every \(b\);
- negative-template rational-base returns;
- graph-directed expansion with compensated local contraction;
- exact synchronous coupling to moving negative phases;
- cycle-padded mismatch towers;
- the Collatz–Kraft pressure law;
- the rounded-phase martingale and phase-escape Doob transform.

These results remove finite branch count, finite precision, local carry pumping, and finite-scale modular correction as principal scarcities. They do **not** produce one infinite ordinary trajectory.

# Four exact representations of one physical state

The repository now uses four compatible views.

## 1. Physical integer

The ordinary state is \(n>0\).

## 2. Finite interval gauge

Choose any \(v\ge1\), put

\[
q=v+n,
\]

and represent \(n\) by the finite interval

\[
I=[v,q),
\qquad |I|=n.
\]

## 3. Negative phase coupling

The lower endpoint \(v\) is the magnitude of a moving negative reference phase. The physical state is

\[
n=q-v.
\]

## 4. Ordered particle population

Put

\[
x=v-1.
\]

The shifted phase \(x\) is the size of a finite ordered particle population.

The current session proves that these are not merely analogous descriptions. They fit into one exact finite rewrite system.

# L-0014 — Collatz as finite-interval renormalization

Let \(I=[v,q)\) have positive length \(n=q-v\).

If \(n\) is even, define

\[
\boxed{
\mathcal R_0(I)
=
[\lceil v/2\rceil,\lceil q/2\rceil).
}
\]

If \(n\) is odd, define

\[
\boxed{
\mathcal R_1(I)
=
[\lfloor3v/2\rfloor,\lceil3q/2\rceil).
}
\]

Then

\[
\boxed{|\mathcal R_{n\bmod2}(I)|=T(n).}
\]

Thus shortcut Collatz is exactly the cardinality evolution of one finite integer interval under parity-selected contraction or outward-rounded dilation.

## Gauge freedom

The initial lower endpoint is arbitrary.

### Fixed gauge

\[
v_0=1,
\qquad q_0=n_0+1
\]

implies

\[
v_t=1,
\qquad q_t=T^t(n_0)+1.
\]

### Diagonal gauge

\[
v_0=n_0+1,
\qquad q_0=2n_0+1
\]

implies

\[
v_t=T^t(n_0)+1,
\qquad q_t=2T^t(n_0)+1.
\]

In this gauge, phase height \(v_t-1\) is exactly the physical Collatz state.

This corrects an important strategic ambiguity:

> phase growth is not gauge invariant; interval length is the physical invariant.

A negative-cycle gauge is useful only when it makes the finite endpoint grammar more structured.

# T-0018 — Critical ordered-particle completion

Define

\[
R_0(x)=\lfloor x/2\rfloor,
\qquad
R_1(x)=\lceil3x/2\rceil.
\]

They satisfy

\[
R_0(x)+R_1(x)=2x.
\]

This harmonic identity has an exact local combinatorial realization.

For \(k\ge1\), give each particle two children:

\[
2k\longmapsto(0,k),(1,3k),
\]

\[
2k-1\longmapsto(1,3k-2),(1,3k-1).
\]

For the ordered root population

\[
[x]=\{1,\ldots,x\},
\]

the branch-zero children are exactly

\[
[\lfloor x/2\rfloor],
\]

and the branch-one children are exactly

\[
[\lceil3x/2\rceil].
\]

Every parent has exactly two children. Hence after \(L\) levels:

\[
\sum_{|w|=L}R_w(x)=2^Lx.
\]

## Escape transform as a uniform descendant

Choosing one depth-\(L\) descendant uniformly gives branch-word probability

\[
\boxed{
\mathbb P_x([w])=rac{R_w(x)}{2^Lx}.
}
\]

For phase \(v=x+1\), this equals the Doob escape measure from `T-0017`:

\[
\mathbb P_x([w])=\mathbb Q_{x+1}([w]).
\]

The phase martingale is therefore the size-biased branch projection of a completely finite, mass-conserving particle rewrite tree.

# Ordinary Collatz is a distinguished marked spine

Each particle \(j\) has one distinguished child:

\[
\chi(j)=
\begin{cases}
(0,j/2),&j\text{ even},\\[1mm]
(1,(3j+1)/2),&j\text{ odd}.
\end{cases}
\]

Its child rank is exactly

\[
T(j).
\]

Iterating distinguished children from one finite root \(j\) gives the ordinary shortcut-Collatz trajectory of \(j\).

For the rightmost root population \([j]\), if \(w_L(j)\) is its physical parity prefix, then

\[
\boxed{
R_{w_L(j)}(j)=T^L(j).
}
\]

This identifies the ordinary-versus-adic obstruction precisely:

- an **unmarked escape path** is a branch through a growing population;
- an **ordinary spine** is one permanently marked finite-root lineage;
- the first does not imply the second.

A valid string-rewrite counterexample certificate must preserve the marker through the distinguished child indefinitely.

# T-0019 — Exact ordinary-spine likelihoods

Let

\[
n_{t+1}=T(n_t),
\qquad e_t=n_t\bmod2,
\qquad A_L=\sum_{t<L}e_t.
\]

For the ordinary parity prefix

\[
w_L=e_0\cdots e_{L-1},
\]

the diagonal phase-escape weight is

\[
\boxed{
\mathbb Q_{n_0+1}([w_L])
=
\frac{n_L}{2^Ln_0}.
}
\]

Relative to fair parity, the likelihood ratio is exactly the physical growth factor:

\[
\frac{\mathbb Q([w_L])}{2^{-L}}=rac{n_L}{n_0}.
\]

Relative to the \(3/4\)-odd Collatz growth tilt,

\[
\boxed{
\frac{\mathbb Q([w_L])}{3^{A_L}/4^L}
=
\frac{2^Ln_L}{3^{A_L}n_0}
=
\prod_{\substack{t<L\\n_t\text{ odd}}}
\left(1+\frac1{3n_t}\right).
}
\]

Equivalently,

\[
\log\frac{n_L}{n_0}
=
A_L\log3-L\log2
+
\sum_{\substack{t<L\\n_t\text{ odd}}}
\log\left(1+\frac1{3n_t}\right).
\]

If the odd-state reciprocal sum converges, phase escape and the \(3/4\)-growth tilt are asymptotically comparable along that ordinary spine.

## Marked-spine rarity

The root population \([n_0]\) has \(2^Ln_0\) depth-\(L\) descendants.

The one distinguished descendant of the specified root \(n_0\) has mass

\[
\boxed{\frac1{2^Ln_0}.}
\]

There is one distinguished ordinary descendant per root particle, so the mass of **all** distinguished ordinary lineages is exactly

\[
\boxed{2^{-L}.}
\]

This does not depend on how rapidly their endpoints grow.

Therefore the phase-escape transform solves an unmarked population-bias problem, not the marked ordinary-boundary problem.

# Strategic correction

The preceding sessions sought an entropy-thin, pressure-positive escape language. That remains useful, but it is only one layer.

The sharper target is now a **two-layer marked rewrite grammar**.

## Population layer

Prove regeneration, positive graph pressure, or a phase potential for an unmarked finite population or interval.

## Marker layer

Carry one finite marked particle and force it through the distinguished child at every step.

Only the marker layer certifies that the construction begins from one ordinary positive integer rather than from an unmarked or adic escape path.

# Computational state

- `X-0001`: consecutive collision bundles.
- `X-0002`: complete finite fibers through depth 22.
- `X-0003`: inverse-signature construction and the 339-branch chart.
- `X-0004`: offset tensors and arbitrary-precision atomic codes.
- `X-0005`: complete dyadic projection through \(b=5\).
- `X-0006`: negative-template identities, renewal equations, and aspect ratios.
- `X-0007`: exact aspect-ratio census and the negative-136 chart.
- `X-0008`: synchronous coupling, padding towers, and Collatz–Kraft identities.
- `X-0009`: rounded phase martingale and escape transform.
- `X-0010`: finite interval gauges, particle partitions, mass conservation, distinguished ordinary spines, and exact likelihood identities.

All programs use exact Python integers and the standard library only.

# Central unresolved step

The project still lacks a **finite-boundary regeneration theorem**.

The strongest current construction target is:

> Build a finite or pushdown two-layer rewrite grammar whose unmarked interval/population layer regenerates with positive growth, whose marked finite-root particle is always sent through the distinguished child, and whose marked ranks are proved unbounded.

This formulation directly contains one ordinary finite starting integer and no longer leaves the boundary condition to a later adic audit.

# Immediate priorities

1. **Marked boundary substitution.** Search for parameterized particle blocks in which the unmarked population reproduces and the distinguished marker moves to a larger copy of the same boundary type.
2. **Endpoint-string grammar.** Rewrite finite binary lower and upper endpoints from `L-0014`; use a negative-cycle lower gauge while retaining an explicit upper-boundary marker.
3. **Population/marker potentials.** Combine phase pressure for the unmarked layer with a separate monotone potential for the marked rank.
4. **Cycle-padding with a marker.** Revisit `T-0015`: determine how the ordinary distinguished child moves through a padded negative-cycle population, not only how the unmarked phase transfers.
5. **Measure-guided search.** Use `T-0019` to rank ordinary prefixes, but reject every proposal that lacks a deterministic marker rule.
6. **Independent audit.** Reconstruct `L-0014`, `T-0018`, `T-0019`, and `X-0010`, especially endpoint roundings, the odd-parent right child, and the distinction between branch mass and marked-spine mass.
