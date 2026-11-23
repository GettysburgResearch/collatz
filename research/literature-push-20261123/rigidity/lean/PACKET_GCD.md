# Complete numerical gcd for arbitrary finite packet families

`PacketGCD.lean` extends the separately frozen homogeneous-repunit core
to the complete numerator used by the adjacent arithmetic construction.
All products and gcds are ordinary natural numbers.

Fix coprime `X,Y`, a positive `r`, and a finite index set `I` of any
size. The positive indices `n_i` are pairwise coprime. Put

\[
R_i=U_{n_i}(X^r,Y^r),\qquad P=\prod_{i\in I}R_i,
\qquad c_i=X^{s_i}Y^{r n_i-1-s_i},
\]
\[
B=U_r(X,Y)P+
  \sum_{i\in I}c_i\prod_{j\in I\setminus\{i\}}R_j.
\]

The module proves from these actual base and index hypotheses that

\[
\boxed{\gcd(B,P)=1.}
\]

It then proves, for arbitrary natural `D,V`,

\[
\boxed{\gcd(DP,VB)\mid DV.}
\]

The final declaration specializes the complete numbers to

\[
\boxed{
\gcd\bigl((X^r-Y^r)P,(Y-2^b)B\bigr)
\mid (X^r-Y^r)(Y-2^b).}
\]

There is no assumed repunit-coprimality premise in these specialized
theorems, and no passage to radicals or selected prime factors.

## Why the cancellation is valid

The imported and freshly compiled full repunit gcd identity makes the
`R_i` pairwise coprime. Its base-coprimality theorem also gives
`gcd(R_i,X*Y)=1`, so every literal monomial `c_i` is coprime to `R_i`.

For a fixed index `i`, every term of `B` except
`c_i product_(j!=i) R_j` is divisible by `R_i`. The surviving term is
coprime to `R_i`, including all of its complete factors. Hence `B` is
coprime to each `R_i`, and therefore to their product.

For the full gcd step,

\[
\gcd(DP,VB)\mid\gcd(D,VB)\gcd(P,VB).
\]

Coprimality of `B,P` cancels `B` from the second gcd. The first remaining
factor divides `D`, and the second divides `V`. This proves divisibility
by the full numerical product `DV`, with multiplicities retained.

## Domain and scope

The algebra works for every finite index set, including the empty set.
It needs positive `r,n_i`, but not the stronger `n_i>=2`, distinct legal
shift positions, or a prescribed packet count. In the arithmetic
application those stronger conditions ensure actual finite-word
realization and ensure that the written exponents are nonnegative;
they remain part of that separate construction.

The Lean statements use natural subtraction. The intended application
has `X>Y>2^b` and legal shifts, so these are exactly its positive
ordinary differences and literal exponents. This module does not prove
the finite Collatz realization, the numerator lower bound, or the final
separation inequality. It proves their complete gcd cancellation core.

## Verification

There are five new theorem declarations and five definitions.
`PacketGCDAudit.lean` audits all ten declarations. The final receipt
records a fresh strict build of the unchanged repunit dependency,
the packet module, and its audit, all with source hashes before and
after. All commands exited zero and every axiom set is a subset of
`propext`, `Classical.choice`, and `Quot.sound`.

See `reports/2026-11-23-literature-push/rigidity-packet-*` for exact
commands, compiler and mathlib pins, output logs, and the freeze manifest.
