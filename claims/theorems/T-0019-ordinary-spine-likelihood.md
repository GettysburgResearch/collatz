# T-0019 — Ordinary-spine likelihood identities

Claim ID: `T-0019`  
Title: Exact escape, growth-tilt, and marked-descendant weights along one ordinary Collatz trajectory  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-0001`, `T-0016`, `T-0017`, `T-0018`  
Scope: one ordinary positive-integer Collatz spine inside the phase-escape particle tree  
Related counterexample candidates: none

## Statement

Let

\[
n_{t+1}=T(n_t),
\qquad n_0\ge1,
\]

be one ordinary shortcut-Collatz trajectory. Put

\[
e_t=n_t\bmod2,
\qquad
A_L=\sum_{t=0}^{L-1}e_t,
\]

and let

\[
w_L=e_0e_1\cdots e_{L-1}
\]

be its first \(L\) physical parity bits.

Use the diagonal phase gauge

\[
v_0=n_0+1.
\]

Then:

### 1. Exact escape-cylinder weight

The phase-escape measure of the ordinary parity prefix is

\[
\boxed{
\mathbb Q_{n_0+1}([w_L])
=
\frac{n_L}{2^Ln_0}.
}
\tag{1}
\]

Equivalently, relative to fair parity,

\[
\boxed{
\frac{\mathbb Q_{n_0+1}([w_L])}{2^{-L}}
=
\frac{n_L}{n_0}.
}
\tag{2}
\]

Thus the escape transform weights an ordinary parity prefix by its exact physical growth factor.

### 2. Exact comparison with the Collatz growth tilt

Let

\[
\mu_{3/4}([w_L])
=
\frac{3^{A_L}}{4^L}
\]

be the \(3/4\)-odd Bernoulli weight from `T-0016`. Then

\[
\boxed{
\frac{
\mathbb Q_{n_0+1}([w_L])
}{
\mu_{3/4}([w_L])
}
=
\frac{2^Ln_L}{3^{A_L}n_0}.
}
\tag{3}
\]

This ratio has the exact product expansion

\[
\boxed{
\frac{2^Ln_L}{3^{A_L}n_0}
=
\prod_{\substack{0\le t<L\\n_t\text{ odd}}}
\left(1+\frac{1}{3n_t}\right).
}
\tag{4}
\]

### 3. Exact logarithmic decomposition

The ordinary physical growth satisfies

\[
\boxed{
\log\frac{n_L}{n_0}
=
A_L\log3-L\log2
+
\sum_{\substack{0\le t<L\\n_t\text{ odd}}}
\log\left(1+\frac{1}{3n_t}\right).
}
\tag{5}
\]

The first two terms are the formal multiplicative pressure; the final sum is the exact finite-\(+1\) correction.

### 4. Asymptotic equivalence criterion

If

\[
\sum_{\substack{t\ge0\\n_t\text{ odd}}}
\frac{1}{n_t}<\infty,
\tag{6}
\]

then the ratio in (3) converges to one finite positive limit. Along that ordinary spine, the phase-escape and \(3/4\)-growth cylinder weights are asymptotically equivalent up to a constant factor.

In particular, condition (6) holds whenever the trajectory eventually grows at least exponentially.

### 5. Marked-descendant rarity

In the ordered-particle completion of `T-0018`, the root population \([n_0]\) has exactly

\[
2^Ln_0
\]

depth-\(L\) descendants.

The distinguished ordinary lineage of the single root particle \(n_0\) contributes exactly one of those descendants. Hence its full marked-spine probability under uniform descendant selection is

\[
\boxed{
\frac{1}{2^Ln_0}.
}
\tag{7}
\]

There is one distinguished ordinary descendant for each of the \(n_0\) root particles, so the probability of selecting **some** ordinary distinguished lineage is exactly

\[
\boxed{2^{-L}.}
\tag{8}
\]

This remains true regardless of how rapidly the corresponding ordinary trajectories grow.

## Proof

In the diagonal gauge, `L-0014` gives

\[
v_t=n_t+1.
\]

The phase endpoint after the word \(w_L\) is therefore

\[
S_{w_L}(n_0+1)=n_L+1.
\]

Using the path-density formula of `T-0017`,

\[
\mathbb Q_{n_0+1}([w_L])
=
2^{-L}
\frac{(n_L+1)-1}{(n_0+1)-1}
=
\frac{n_L}{2^Ln_0},
\]

which proves (1)--(2). Dividing by \(3^{A_L}/4^L\) gives (3).

At an even state,

\[
\frac{n_{t+1}}{n_t}=\frac{1}{2}.
\]

At an odd state,

\[
\frac{n_{t+1}}{n_t}
=
\frac{3n_t+1}{2n_t}
=
\frac{3}{2}
\left(1+\frac{1}{3n_t}\right).
\]

Multiplying these one-step identities proves (4), and taking logarithms proves (5).

If (6) holds, then

\[
\sum_{n_t\text{ odd}}
\log\left(1+\frac{1}{3n_t}\right)
\]

converges absolutely because

\[
0<\log(1+x)\le x.
\]

Hence the product in (4) converges to a finite positive value. Eventual exponential growth implies summability of the reciprocals.

Part 5 follows from `T-0018`: every root particle has exactly \(2^L\) descendants and exactly one distinguished ordinary descendant at depth \(L\). ∎

## Interpretation

The theorem separates two different notions of an exceptional path.

### Unmarked phase escape

The branch cylinder \(w_L\) receives mass

\[
\frac{n_L}{2^Ln_0}.
\]

Growing endpoint populations are favored.

### Marked ordinary boundary

The one distinguished descendant that certifies the finite ordinary root receives mass

\[
\frac{1}{2^Ln_0}.
\]

The factor \(n_L\) disappears when the endpoint particle itself must be the distinguished boundary marker.

Therefore the phase-escape Doob transform solves the **unmarked population-growth bias**, but it does not by itself solve the ordinary-boundary problem.

## Strategic consequence

A candidate grammar must carry two certificates simultaneously:

1. an unmarked population or phase potential proving expansion;
2. a marked boundary-spine rule proving that one finite ordinary root follows the accepted language.

Pressure-positive unmarked languages can be useful search guides, but they cannot replace the marker.

## Gap audit

- The identities are exact but do not imply existence of a divergent ordinary spine.
- Asymptotic equivalence of two symbolic measures along a hypothetical growing trajectory is not an ordinary-boundary proof.
- The marked-spine probabilities tend to zero for every fixed root; this is a rarity statement, not a nonexistence result.

## Adversarial tests

`X-0010` verifies (1)--(8) on many ordinary trajectories and checks the product identity exactly with rational arithmetic.

## Suggested next attack

Construct a **two-layer rewrite certificate**: an unmarked population layer governed by phase/Kraft pressure, and a marked particle layer forced through the distinguished child. Search for a finite substitution in which the population layer regenerates while the marker stays on a self-similar right boundary.