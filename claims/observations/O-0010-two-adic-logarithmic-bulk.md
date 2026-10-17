# O-0010 — The quadratic stage bulk converges to a 2-adic logarithm

Claim ID: `O-0010`  
Title: Exact logarithmic limit and one-bit convergence rate of the Hensel bulk  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0023`, `L-0027`  
Scope: the moving bulk in the dyadic stage-boundary connector stream  
Related counterexample candidates: none

## Statement

For \(m\ge1\), put

\[
y_m=3^{-7\cdot2^m}
\]

in \(\mathbb Z_2\), and define

\[
\boxed{
u_m=\frac{y_m-1}{2^{m+2}}.}
\tag{1}
\]

`L-0023` proves that \(u_m\) is an odd 2-adic integer and satisfies

\[
\boxed{
u_{m+1}=u_m+2^{m+1}u_m^2.}
\tag{2}
\]

Define the normalized 2-adic logarithm of \(3\) by

\[
\log_2(3)
:=
\log(-3)
=
\frac12\log(9),
\]

where the logarithm is the usual convergent series on \(1+4\mathbb Z_2\).

Then:

### 1. Exact logarithmic limit

\[
\boxed{
u_m\longrightarrow
u_\infty
=-\frac74\log_2(3).}
\tag{3}
\]

Equivalently,

\[
\boxed{
u_\infty
=7\sum_{n=1}^{\infty}\frac{4^{n-1}}n.}
\tag{4}
\]

Every term in (4) is a 2-adic integer, and the series converges in \(\mathbb Z_2\).

### 2. Exact convergence rate

\[
\boxed{
\nu_2(u_\infty-u_m)=m+1.
}
\tag{5}
\]

Thus the dyadic scale change \(m\mapsto m+1\) certifies exactly one new low bit of the limiting logarithmic bulk.

### 3. First 64 low bits

The least residue of \(u_\infty\) modulo \(2^{64}\) is

```text
0x5522e8f2837ee855
```

in ordinary hexadecimal notation.

### 4. Connector interpretation

For a fixed phase-`-34` tower type, `L-0023` gives

\[
\omega_m
=
\omega_\infty
+2^{m-r+1}3^{-g_0}u_m.
\]

Hence the stage-boundary connector stack consists of:

1. the periodic rational frontier \(\omega_\infty\);
2. a shifting prefix of the fixed logarithmic unit \(-\frac74\log_2(3)\);
3. the finite Newton approximation \(u_m\), which `L-0027` generates without a completion oracle.

## Proof

Since

\[
-3\equiv1\pmod4,
\]

its 2-adic logarithm is defined. For every \(x\in1+4\mathbb Z_2\),

\[
\log x
=
\lim_{m\to\infty}
\frac{x^{2^m}-1}{2^m}.
\]

Take

\[
x=(-3)^{-7}.
\]

For \(m\ge1\), the exponent \(7\cdot2^m\) is even, so

\[
x^{2^m}
=(-3)^{-7\cdot2^m}
=3^{-7\cdot2^m}
=y_m.
\]

Therefore

\[
\begin{aligned}
\lim_{m\to\infty}u_m
&=
\frac14
\lim_{m\to\infty}
\frac{y_m-1}{2^m}\\
&=
\frac14\log((-3)^{-7})\\
&=-\frac74\log(-3),
\end{aligned}
\]

which proves (3).

The logarithm series

\[
\log(-3)
=
\log(1-4)
=-\sum_{n=1}^{\infty}\frac{4^n}{n}
\]

gives (4). The valuation of its \(n\)-th displayed term is

\[
\nu_2\left(\frac{4^{n-1}}n\right)
=2(n-1)-\nu_2(n)\ge0,
\]

and tends to infinity, proving convergence in \(\mathbb Z_2\).

For the exact rate, equation (2) gives

\[
u_{j+1}-u_j=2^{j+1}u_j^2.
\]

Since every \(u_j\) is odd,

\[
\nu_2(u_{j+1}-u_j)=j+1.
\]

The valuations of successive tail increments are strictly increasing. In the convergent sum

\[
u_\infty-u_m
=
\sum_{j=m}^{\infty}(u_{j+1}-u_j),
\]

the first summand therefore has strictly smallest valuation and cannot cancel. This proves (5). ∎

## Interpretation

The apparently irregular moving stack is not an arbitrary 2-adic address. It is a renormalized logarithm of the negative cycle multiplier.

This explains three earlier phenomena at once:

- repeated scale doubling produces a quadratic Hensel recurrence;
- exactly one new limit bit stabilizes per dyadic stage;
- Newton lifting is the natural finite-word compiler.

The logarithmic identification is conceptual, not a counterexample certificate. The limit \(u_\infty\) is a completion object. `L-0027` is what makes its required **finite prefixes** computable without assuming the limit as input.

## Gap audit

- The logarithmic bulk belongs to the connector-control layer, not the ordinary residual layer.
- A computable 2-adic logarithm does not imply that one finite positive integer realizes the associated infinite Collatz schedule.
- No rationality, irrationality, or transcendence claim about \(\log_2(3)\) is required here.

## Adversarial tests

`X-0013` computes (4) modulo powers of two, compares it with the finite values \(u_m\), verifies the exact valuation in (5), and records the 64-bit fingerprint.