# T-0006 — Geometry-preserving collision-code amplification

Claim ID: `T-0006`  
Title: Every finite collision alphabet can be embedded in arbitrarily large mildly supercritical collision fibers without losing its local geometry  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-0005`, `L-0006`, `L-0007`, `L-0008`, `T-0005`  
Scope: finite parity collision codes, inverse-root alphabets, and finite supercritical tail promotion  
Related counterexample candidates: none

## Statement

Let \(U_0\) be a nonempty finite parity collision code of common length \(L_0\), common weight \(a_0\), and precision at least \(a_0\). Let \(D_0\) be one of its inverse-root offset alphabets, normalized relative to a chosen reference word.

Then for every integer \(n\ge0\) there exists a finite collision code \(U_n\) such that:

1. \(U_n\) has exactly
   \[
   \boxed{|U_n|=|U_0|2^n}
   \]
   words;
2. its common weight is \(a_0+n\);
3. its precision is at least \(a_0+n\);
4. its inverse-root alphabet \(D_n\) contains a translated copy of \(D_0\);
5. its difference set contains the original difference set:
   \[
   \boxed{D_0-D_0\subseteq D_n-D_n;}
   \]
6. every congruence projection, consecutive subblock, or difference interval already witnessed in \(D_0\) survives in \(D_n\).

Moreover, after appending a suitable finite all-odd tail as in `T-0005`, the code becomes a supercritical Collatz collision fiber with the same cardinality and exactly the same inverse-root offset geometry. The tail can be chosen minimally, giving expansion ratio in

\[
1<\frac NM\le\frac32.
\]

Thus every useful finite collision alphabet admits arbitrarily large supercritical extensions that preserve all of its established local geometry.

## Construction

Set \(U_0\) as given. Suppose \(U_{i-1}\) has weight \(a_0+i-1\), precision at least that weight, and length \(L_{i-1}\).

Choose the atomic suffix code

\[
V_i=V_{a_0+i}
\]

from `L-0008`. It has weight one and precision exactly \(a_0+i\). Define

\[
U_i=U_{i-1}V_i.
\]

By `L-0006`, the concatenated code has precision at least

\[
\minigl((a_0+i-1)+1,\ a_0+i\bigr)=a_0+i.
\]

Its weight is \(a_0+i\), so it is again an ordinary collision code and can be iterated.

## Exact alphabet formula

Let

\[
R_i=2\cdot3^{a_0+i-1},
\qquad
K_i=\frac{2^{R_i}-1}{3^{a_0+i}}.
\]

Let \(L_{i-1}\) denote the cumulative length before appending \(V_i\). Applying `L-0007` at each stage gives

\[
\boxed{
D_i=D_{i-1}+2^{L_{i-1}}\{0,\pm K_i\},
}
\tag{1}
\]

where the sign depends only on the reference convention. Iterating,

\[
D_n
=D_0+
\sum_{i=1}^{n}2^{L_{i-1}}\{0,\pm K_i\}.
\tag{2}
\]

The sum is an exact mixed-radix Minkowski sum, not a heuristic approximation.

## Proof of the claims

At every stage the two choices in \(V_i\) are distinct, and concatenated parity words are distinct. By uniqueness of the parity residue, all inverse roots are distinct. Therefore cardinality doubles at each step, proving \(|U_n|=|U_0|2^n\).

The precision and weight induction was established above.

Fixing the reference suffix choice at every stage leaves the original offsets unchanged. Therefore \(D_n\) contains a translated copy of \(D_0\). Taking differences of two roots with all suffix choices equal gives

\[
D_0-D_0\subseteq D_n-D_n.
\]

Any property witnessed by elements of the embedded copy—surjectivity modulo a fixed modulus, a consecutive run, or an interval in the difference set—therefore survives.

Finally apply the finite CRT odd-tail construction of `T-0005` to \(U_n\). The odd tail multiplies every affine-constant difference by the same power of three and increases the denominator by the same power. Consequently inverse-root differences, hence the entire offset alphabet, are unchanged exactly. Choosing the shortest tail that makes the block supercritical places the expansion ratio in \((1,3/2]\). ∎

## Strategic consequence

`T-0005` proved that large supercritical alphabets exist. `T-0006` proves something stronger and more directed:

> Any locally useful alphabet can be amplified to arbitrarily large supercritical alphabets without sacrificing the feature that made it useful.

For example, starting from `O-0005`, one obtains arbitrarily large exact supercritical fibers that still:

- cover every residue modulo \(16\);
- contain a seven-term consecutive run;
- have difference set containing \([-934,934]\).

Therefore neither alphabet size nor preservation of a fixed finite amount of local geometry is the central obstacle. The remaining issue is geometry that scales with the boundary or closes vertically under the induced map.

## Gap audit

- The theorem preserves fixed geometry; it does not prove that modular coverage or difference intervals grow with \(n\).
- The lengths of the atomic suffixes grow rapidly.
- The resulting alphabets are finite and do not themselves produce an infinite admissible induced orbit.
- Choosing different finite odd tails changes the chart radices and lifting modulus but does not create vertical closure.

## Adversarial tests

`X-0004` constructs a sixteen-word example from a two-word base code and three atomic suffixes, checks exact precision, the tensor formula, unique inverse roots, and invariance of the base difference set. It also verifies that appending an odd tail leaves all offsets unchanged.

## Suggested next attack

Replace the atomic suffixes by codes whose normalized offset sets themselves have controlled small-modulus coverage. The exact tensor law then offers a route to geometry growing with the code depth rather than merely preserving a fixed base feature.