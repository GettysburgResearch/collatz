# Current integrated state

Last updated: 2026-07-21  
Integrator status: provisional synthesis by `gpt56-pro-01`  
Active issue: `#2`  
Active draft PR: `#3`

## Project maturity

The active branch now contains eight mathematical research sessions. No claim has yet received independent review, so complete-looking finite theorems and identities remain `PROPOSED`.

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

A length-\(L\), weight-\(a\) parity word \(w\) acts affinely:

\[
T^L(n)=\frac{3^an+B(w)}{2^L}
\]

on one residue class modulo \(2^L\).

## Research arc before the current session

The repository already contains proposed exact results on:

- finite collision fibers and induced partial radix maps;
- mixed-radix string rewrites and finite-horizon carry pumps;
- complete collision-fiber recursion;
- inverse-signature collision codes;
- exponentially unbounded mildly supercritical branch count;
- arbitrary finite 3-adic precision;
- preservation of finite alphabet geometry under code tensors;
- complete collision-alphabet projection modulo \(2^b\) for every \(b\);
- negative-template return systems
  \[
  Nq=Mq'+a;
  \]
- variable-length renewal criteria and finite-code obstructions;
- normalized real aspect ratio;
- multi-target graph potentials;
- exact coupling to moving negative phases;
- negative-cycle padding towers;
- Collatz–Kraft pressure and negative typical drift of complete renewal coverage.

These results remove branch count, finite precision, local pumping, and finite-scale modular correction as principal scarcities. They do **not** provide one ordinary starting value with an infinite expanding trajectory.

# Principal local representation

## T-0014 — Synchronous difference/phase coupling

Write a physical state as

\[
n=q-v,
\qquad v\ge1.
\]

With

\[
p=q\bmod2,
\qquad
r=v\bmod2,
\qquad
e=p\oplus r=n\bmod2,
\]

one shortcut step is exactly

\[
q'=\frac{3^eq+p}{2},
\qquad
v'=\frac{3^ev+(2p-1)r}{2},
\]

and

\[
T(q-v)=q'-v'.
\]

Even \(q\) means synchronization with the ordinary negative orbit; odd \(q\) is a complementary mismatch.

If \(q=2^km\) with \(m\) odd, the first \(k\) steps synchronize and the next step is the first mismatch. This gives a complete renewal partition indexed by \(\nu_2(q)\).

## T-0015 — Negative-cycle padding towers

A negative cycle of length \(\ell\), odd count \(a\), and multiplier

\[
\Lambda=\frac{3^a}{2^\ell}>1
\]

turns every fixed mismatch/recovery type into a countable tower:

\[
L_t=L_0+t\ell,
\qquad
a_t=a_0+ta,
\qquad
\lambda_t=\lambda_0\Lambda^t.
\]

The natural grammar state is therefore:

\[
\boxed{
\text{finite negative phase type}
+
\text{one nonnegative padding counter}.
}
\]

`O-0008` records the complete one-mismatch complement atlas of the negative eleven-cycle.

## T-0016 — Collatz–Kraft pressure

For every complete parity prefix code,

\[
\sum_w2^{-|w|}=1
\]

and

\[
\sum_w\frac{3^{a(w)}}{4^{|w|}}=1.
\]

Thus, under fair cylinder probabilities,

\[
\mathbb E\left[\frac{3^{a(w)}}{2^{|w|}}\right]=1,
\]

while, for finite mean length,

\[
\mathbb E[\log\lambda]
=
\frac12\log(3/4)\,\mathbb E[|w|]
<0.
\]

The multiplier is exactly the likelihood ratio between Bernoulli odd probability \(3/4\) and fair parity.

Complete broad coverage is therefore the wrong target: every positive-growth survivor language is Haar-null and exceptional.

# New session: rounded phase martingale

## L-0013 — Physical parity removes the XOR

Let

\[
e=T^t(n)\bmod2
\]

be the physical parity. The moving negative phase has the exact rounded update

\[
\boxed{
S_0(v)=\left\lceil\frac v2\right\rceil,
\qquad
S_1(v)=\left\lfloor\frac{3v}{2}\right\rfloor.
}
\]

Thus

\[
v_{t+1}=S_{e_t}(v_t).
\]

The quotient update is

\[
q'=
\begin{cases}
(q+(v\bmod2))/2,&e=0,\\[1mm]
(3q+1-(v\bmod2))/2,&e=1.
\end{cases}
\]

Most importantly,

\[
\boxed{
S_0(v)+S_1(v)=2v.
}
\]

Every physical parity word drives an exact integer-valued rounded phase shadow independent of the magnitude of the accompanying quotient.

## T-0017 — Fair phase absorption

Under independent fair physical parity bits,

\[
V_{t+1}=S_{E_t}(V_t)
\]

is a nonnegative martingale:

\[
\mathbb E[V_{t+1}\mid V_t]=V_t.
\]

It is absorbed at phase \(1\) almost surely.

This supplies a second exact conservation law beside `T-0016`.

## Exact phase–Kraft identity

For every finite complete physical-parity prefix code \(\mathcal W\),

\[
\boxed{
\sum_{w\in\mathcal W}
2^{-|w|}\bigl(S_w(v)-1\bigr)
=
v-1.
}
\]

Consequently, the fair mass of codewords ending at phase at least \(H\) satisfies

\[
\sum_{S_w(v)\ge H}2^{-|w|}
\le
\frac{v-1}{H-1}.
\]

High negative phases are necessarily supported by a thin set of parity cylinders.

## Finite complete graph rigidity

Suppose a finite graph of exact phase-return words has a complete outgoing prefix code at every vertex. Let

\[
P(i,j)
=
\sum_{e:i\to j}2^{-|w_e|}.
\]

Then

\[
P(v_i-1)=(v_i-1).
\]

Every recurrent communicating class of such a complete finite graph is phase \(1\). A nontrivial recurrent multi-phase construction must therefore be incomplete and exceptional, infinite-state, or equipped with an unbounded stack/counter.

This strengthens the one-target obstruction of `T-0009`.

## Exact phase escape transform

Put

\[
h(v)=v-1.
\]

For \(v>1\), define

\[
\boxed{
\mathbb Q_v(e)
=
\frac{h(S_e(v))}{2h(v)}.
}
\]

For a finite parity word \(w\),

\[
\boxed{
\mathbb Q_v([w])
=
2^{-|w|}
\frac{S_w(v)-1}{v-1}.
}
\]

This is the exact Doob transform that conditions the fair rounded phase away from absorption.

Its physically odd probability is

\[
\boxed{
\mathbb Q_v(e=1)
=
\begin{cases}
3/4,&v\text{ odd},\\[1mm]
3/4+\dfrac1{4(v-1)},&v\text{ even}.
\end{cases}
}
\]

Therefore phase survival automatically biases physical parity at or above the Collatz growth tilt.

Let

\[
\gamma=\frac34\log3-\log2>0.
\]

Under the escape transform,

\[
\mathbb E_{\mathbb Q}
\left[
\log\left(\frac{3^e}{2}\right)
\middle|v
\right]
\ge\gamma.
\]

The phase itself also has uniformly positive logarithmic drift. Almost every escape-transform path has:

- exponentially growing phase magnitude;
- exponentially growing formal Collatz multiplier.

This does **not** yet imply an ordinary positive Collatz orbit. It identifies the correct exceptional symbolic measure.

# Three measures on one parity language

A finite physical parity word \(w\) now carries three exact weights.

### Fair cylinder mass

\[
\mu_{\mathrm{fair}}(w)=2^{-|w|}.
\]

### Collatz growth tilt

\[
\mu_{\mathrm{growth}}(w)
=
2^{-|w|}
\frac{3^{a(w)}}{2^{|w|}}.
\]

### Phase escape tilt

\[
\mu_{\mathrm{escape}}(w)
=
2^{-|w|}
\frac{S_w(v)-1}{v-1}.
\]

The first likelihood ratio is the Collatz multiplier. The second is the phase endpoint ratio.

At odd phases, the growth and escape one-step tilts coincide exactly. At even phase \(v\), their physically odd probabilities differ by only

\[
\frac1{4(v-1)}.
\]

Thus the negative-phase survival problem and the positive-growth pressure problem are two views of nearly the same exceptional language.

# Computational state

- `X-0001`: consecutive collision bundles.
- `X-0002`: complete finite fibers through depth 22.
- `X-0003`: inverse-signature construction and the 339-branch chart.
- `X-0004`: offset tensors and arbitrary-precision atomic codes.
- `X-0005`: complete dyadic projection through \(b=5\).
- `X-0006`: negative-template identities, renewal equations, and aspect ratios.
- `X-0007`: exact aspect-ratio census and the negative-136 chart.
- `X-0008`: synchronous coupling, cycle-padding towers, complement atlas, and Collatz–Kraft checks.
- `X-0009`: rounded phase coupling, phase–Kraft identities, escape-transform path weights, drift bounds, and exact fair absorption distributions.

All programs use exact Python integers and the standard library only.

# Central unresolved step

The project still lacks a **finite-boundary regeneration theorem**.

The sharp current target is:

> Construct a finitely generated exact return grammar that approximates the phase escape transform, has positive graph-cycle growth, and contains one explicitly certified ordinary finite quotient.

This requires all of:

1. exact phase and cylinder closure;
2. an incomplete entropy-thin survivor language;
3. padding counters or another unbounded finite-memory mechanism;
4. positive pressure and graph-cycle products;
5. one ordinary finite accepted boundary, not merely a 2-adic path.

# Immediate priorities

1. **Escape-transform approximation.** Build finite or pushdown return graphs whose edge frequencies approximate
   \[
   \mathbb Q_v(e)=\frac{S_e(v)-1}{2(v-1)}.
   \]
2. **Phase-136 pushdown model.** Combine the eleven-cycle padding towers with the escape likelihood and search for a closed high-padding component.
3. **Ordinary-boundary theorem.** Develop a finite certificate that an exceptional accepted parity language contains one ordinary quotient.
4. **Three-pressure audit.** Rank candidate grammars by fair mass, Collatz growth tilt, phase escape tilt, and deterministic cycle multipliers.
5. **Multi-mismatch compression.** Use the rounded phase maps rather than the larger quotient-parity semigroup.
6. **Independent audit.** Reconstruct `L-0013`, `T-0017`, and `X-0009`, especially martingale absorption, graph rigidity, and the Doob drift bounds.
