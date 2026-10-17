# Backward preimage trees versus forward collision fibers

## What the located tree literature studies

Applegate–Lagarias and Krasikov–Lagarias bound the number of integers in backward `3x+1` trees and convert those estimates into density lower bounds for integers reaching specified congruence classes or smaller values. Their methods include explicit tree search and systems of difference inequalities.

## What the repository studies

At fixed depth `L`, a collision fiber is a level set of finite forward affine data such as

```text
r -> (odd_count(r), T^L(r)).
```

Different residues in one fiber follow different parity words but land at a common endpoint with the same multiplier. This is not the same count as the number of backward preimages of one integer under unrestricted inverse branches.

## Potential bridge

A useful theorem would construct a bipartite incidence object:

- left vertices: weight-`a` parity words or residues modulo `2^L`;
- right vertices: admissible endpoints/signatures modulo `3^a`;
- edges: affine inversion compatibility.

`PR3/T-0005` already uses the average right-fiber size by pigeonhole. Tree methods may help with variance, concentration, or structured large fibers. Applegate–Lagarias congruence-sensitive leaf distributions suggest studying second moments over signatures rather than only maximal cardinality.

## Caution

Do not quote backward-tree growth exponents as collision-width exponents. A theorem connecting the two distributions is presently missing.
