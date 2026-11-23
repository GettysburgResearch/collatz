# Exact source products for all-gap collision attacks

23 November 2026. **Status: written finite arithmetic theorems and explicit
application boundaries. Full Collatz and actual-source collision control
remain OPEN.**

This note tests two classical mechanisms on the complete ordinary endpoint
law: the difference-product argument behind the larger sieve, and a direct
three-coordinate S-adic Subspace-Theorem encoding. All ordinary states,
diagonals, valuations, and complete carries are retained.

The positive deductions are exact full-source identities. The closing
attempt stops for two concrete reasons. A single prime-power collision
tower spends only its summable residue energy against an unbounded ordinary
height budget. The natural Subspace product has only a subpower saving in
the long-lag regime forced by the actual entropy deficit; balanced positive
ordinary CRT segments attain that scale exactly.

## 1. Frozen input and original ordinary law

Start from the checkout
`bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17`. The direct arithmetic comparison
is PR176 at `81095581a1dccb8b5d89ee2ea3e9ba4a7b447e0a`,
`research/lean-global-resolvent-20261121/overview/global-closing/ACTUAL_ALL_GAP_COLLISIONS.md`,
Sections 4–5. Its source-qualified stationary input is PR180's actual gap
lift and finite Shannon-deficit theorem.

Let `q_j=U^j(q_0)` be one hypothetical escaping positive odd ternary-unit
orbit. For `N>=2`, put

\[
 \pi_N={1\over N}\sum_{j=0}^{N-1}\delta_{q_j},\qquad
 H_N=\max_{j<N}q_j-\min_{j<N}q_j\ge1.
\]

The diameter convention for `H_N` differs from the maximum-height convention
in some source files. The two can be replaced by one another only using the
explicit inequality `diameter <= maximum height`.

## 2. Full-source difference energy, including the diagonal correction

For a finite prime-power set `S`, write `Lambda(p^a)=log p`. Then

\[
 \boxed{\sum_{Q\in S}\Lambda(Q)
       \left(\operatorname{Col}_Q(\pi_N)-{1\over N}\right)
 \le {1\over N^2}\sum_{i\ne j}\log|q_i-q_j|
 \le(1-1/N)\log H_N.}
 \tag{S1}
\]

**Proof.** For `i!=j`, unique factorization gives

\[
 \sum_{p^a\in S}\log p\;\mathbf1_{p^a\mid q_i-q_j}
 \le\sum_p v_p(q_i-q_j)\log p
 =\log|q_i-q_j|.
\]

Sum over the ordered distinct pairs and divide by `N^2`. The omitted
diagonal has precisely mass `1/N`, at every modulus. The upper bound uses
the actual ordinary diameter. `QED`.

There is also a fully weighted version. If distinct ordinary states have
weights `t_i>=0` summing to one, replace `1/N` by `sum_i t_i^2`, and replace
the middle sum by `sum_{i!=j}t_it_j log|q_i-q_j|`. The proof is identical.
Thus the identity can be used on the literal retained inverse weights;
off-ray mass is not silently removed when comparing to a full inverse law.

For the complete ternary tower, monotone convergence in (S1) gives

\[
 \boxed{\log3\sum_{m\ge1}
 \left(\operatorname{Col}_{3^m}(\pi_N)-1/N\right)
 ={\log3\over N^2}\sum_{i\ne j}v_3(q_i-q_j)
 \le(1-1/N)\log H_N.}
 \tag{S2}
\]

The sum is finite at every `N`. Both the actual source and every pair lag
are present. Nested powers of three contribute one `log 3` for each
valuation level; they are not separate independent congruence restrictions.

### The exact sieve limitation

In Gallagher's usual support formulation, the denominator is
`sum_{p in S} log(p)/nu(p) - log H`, and must be positive. A collision
formulation replaces the reciprocal support count by the actual collision
probability and keeps the diagonal. Formula (S1) derives the precise
quantity needed here without importing any support approximation.

If the only supplied collision lower profile is `exp(-c m)` with `c>0`,
its total contribution to the left side of (S2) is bounded by a geometric
series, independent of the number of tested ternary levels. Meanwhile
`H_N>=N-1` because the ordinary states are distinct. Thus the established
strict collision lower exponent alone cannot make this sieve denominator
positive against the growing height. It would need additional information
about many other primes, much larger total ternary valuation energy, or a
separate upper bound on the actual height expression.

This identifies the failure of this particular larger-sieve application;
it does not rule out all arithmetic sieves. In particular, large collision
is not an upper support bound, and no such bound is inferred here.

## 3. A fixed ordinary source gives an exact S-adic product

Take one actual segment from `p=q_i` to `q=q_{i+d}`, `d>=1`. Let its
chronological gap word have total `A` and complete carry

\[
 C=\sum_{j=0}^{d-1}3^{d-1-j}2^{a_j},\qquad a_0=0.
\]

Then `C` is a positive integer coprime to six, and

\[
 2^Aq=3^d p+C.
 \tag{S3}
\]

On the integer vector

\[
                   x=(X,Y,Z)=(2^A,3^d,C),
\]

use coordinate forms at the real place, and at each of the places 2 and 3
use

\[
          X,\quad Y,\quad L_p(X,Y,Z)=p(X-Y)-Z.
\]

Each triple is linearly independent, with determinant `-1`; for one fixed
starting source `p`, the forms are fixed. Let `P(x)` be the product of the
absolute values of these nine form values, with normalized ordinary
`p`-adic absolute values. Equation (S3) gives

\[
                         L_p(x)=2^A(p-q).
\]

**Theorem 1 (literal source product).** If `p!=q`, then

\[
 \boxed{P(x)=C\,2^{-A}|p-q|_2|p-q|_3.}
 \tag{S4}
\]

**Proof.** The real product is `2^A 3^d C`. The binary product is
`2^{-2A}|p-q|_2`. The ternary product is `3^{-d}|p-q|_3`. Multiply them.
No complete denominator or carry is factored away. `QED`.

If the endpoints collide modulo `3^m`, oddness and (S4) give

\[
                       P(x)\le {C\over2^{A+1}3^m}.\tag{S5}
\]

The ordinary anchor identity in PR176 is another expression of the same
divisibility. The present calculation states the entire local product that
a Subspace-Theorem application would actually have to make small.

Two independent hypotheses remain. A standard fixed-form application needs
a bound `P(x)<=H(x)^{-epsilon}` for one fixed positive epsilon, where
`H(x)=max(2^A,3^d,C)` (this primitive integer vector has no finite-place
height factor). It also needs one fixed `p` in its linear forms. Summing
collisions over every original index `i` does not supply fixed forms;
allowing moving forms requires a separate theorem and control of their
coefficient heights.

## 4. Balanced ordinary collisions attain only the m/d saving

The next construction is an exact test of the proposed **uniform finite**
implication from balanced clocks and residue collision to fixed-power
Subspace smallness. It does not use or assert an infinite ordinary source.

For every `d>=1`, define

\[
 a_j=\lfloor j\log_2 3\rfloor,\qquad
 g_j=a_j-a_{j-1}\in\{1,2\},\quad 1\le j\le d.
 \tag{S6}
\]

Its total is `A=floor(d ell)`, and its complete carry satisfies

\[
 3^{d-1}\le C\le(d/3)3^d,
 \qquad 2^A\le3^d<2^{A+1}.
 \tag{S7}
\]

The carry upper bound follows term by term from `2^{a_j}<=3^j`.
Put `D=2^A-3^d`, which is odd and prime to three.

**Theorem 2 (exact positive ordinary realization).** For each `m>=1`,
there is a positive odd ternary-unit source `p` which realizes precisely
the gaps (S6), and whose endpoint `q` satisfies

\[
                 v_2(p-q)=1,\qquad v_3(p-q)=m.\tag{S8}
\]

Consequently its exact product obeys

\[
 \boxed{{1\over6}3^{-m}\le P(x)\le {d\over3}3^{-m},
 \qquad \log H(x)=d\log3+O(\log(d+1)).}\tag{S9}
\]

**Proof.** Specify the following two coprime congruences:

\[
 Dp-C\equiv2^{A+1}\pmod{2^{A+2}},\qquad
 Dp-C\equiv3^m\pmod{3^{m+1}}.\tag{S10}
\]

Since `D` is invertible in both moduli, CRT supplies one residue class
modulo `2^{A+2}3^{m+1}` and arbitrarily large positive representatives.
The source is odd because `C` is odd, and it is a ternary unit because
`m>=1`, while `C` and `D` are ternary units.

The first congruence implies

\[
           3^d p+C\equiv2^A\pmod{2^{A+1}}.
\]

This is the standard exact ordinary source cylinder for the supplied
positive gap word: the final quotient is odd, and backwards splitting of
the complete carry makes every intermediate quotient odd with its
prescribed valuation. Positive `p` makes all intermediate values positive.
From (S3), `Dp-C=2^A(p-q)`, so (S10) gives exactly (S8).

If distinctness of every intermediate state is desired, choose a larger
CRT representative avoiding finitely many values. The affine slopes at
different clocks are unequal, since equality would make a nonzero power
of two equal a nonzero power of three. Thus each pair of different clocks
can coincide for at most one real source.

Now (S4) gives `P(x)=C/(2^{A+1}3^m)`. Bounds (S7) yield (S9), including
the height estimate. `QED`.

In particular, along any choice `m=m(d)=o(d)`,

\[
                         {-\log P(x)\over\log H(x)}\longrightarrow0.
 \tag{S11}
\]

This conclusion allows the product itself to exceed one on some scales;
its logarithm still has the stated normalized limit. There is no fixed
positive Subspace saving in these hypotheses.

The sources in Theorem 2 vary with `d,m`. The construction refutes a
uniform finite inference, not an additional theorem that genuinely uses
one fixed all-time source. That distinction is the reason for retaining
`p` explicitly in (S4) rather than calling these a counterexample to
ordinary escape exclusion.

## 5. Why all consecutive lags do not yet change the calculation

PR176's actual finite Shannon-deficit theorem shows that, at precision
`m=floor(log N/Phi(ell))`, a positive power surplus of actual collisions
must occur at lags beyond `N^delta` for some positive delta. Thus the
forced part of the collision sum includes precisely the regime `m/d->0`.
Its theorem does not say the intervening words are balanced, nor that
their carries are small; granting those extra favorable properties would
still leave the scale (S11) in the uniform finite test.

For a **fixed** source `p=q_0`, the prefixes at every consecutive lag have

\[
 2^{A_n}q_n=3^np+C_n,\qquad
 C_{n+1}=3C_n+2^{A_n}.\tag{S12}
\]

These exact relations do keep one source in all the forms. However,
eliminating the carries between consecutive relations returns the original
physical equation `2^{g_{n+1}}q_{n+1}=3q_n+1`. It does not create an
additional small fixed linear form. Treating `C_n` as a bounded-height
coefficient would be false: even the balanced words have
`C_n>=3^{n-1}`. Treating `q_n` as a fixed coefficient would also change
the problem.

The exact sequence (S12), rather than separate finite words, remains the
plausible arithmetic place for further work. A useful advance would be a
simultaneous-lag constraint that exploits its fixed positive `p` and the
actual carries, with a gain beyond the `3^{-m}` supplied by a residue
collision. None is proved by the Subspace product or the sieve identity
above.

## 6. Primary literature and evidence boundary

- P. X. Gallagher, *A larger sieve*, Acta Arithmetica 18 (1971), 77–81,
  DOI `10.4064/aa-18-1-77-81`. The
  [publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/18/0/97714/a-larger-sieve)
  was read. Both public PDF endpoints returned HTTP 403 during this pass;
  full-paper inspection is not claimed.
- Christian Elsholtz, *The distribution of sequences in residue classes*,
  Proceedings of the AMS (2002), DOI `10.1090/S0002-9939-02-06395-5`,
  [author PDF](https://www.math.tugraz.at/~elsholtz/WWW/papers/papers05procamsdistribution.pdf),
  page 3: the precise larger-sieve lemma and the positivity of its
  denominator were read. Formula (S1) is proved directly here.
- Adamczewski–Bugeaud, *On the complexity of algebraic numbers I*,
  [publisher PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v165-n2-p04.pdf),
  Section 4, Theorem E and its normalized local-form product, were read.
  Formula (S4) is the direct arithmetic test for that smallness mechanism;
  the Subspace Theorem is not asserted to apply without its quantitative
  and fixed-coefficient hypotheses.

The exact checker `check_endpoint_machinery.py` executed successfully on
172 positive ordinary CRT collisions (periods through 200), six distinct
ordinary finite orbit controls for the difference-product identity, and
20 rational weighted repeat-moment identities. These finite controls test
the arithmetic identities; the all-parameter proofs are written above.
No new Lean formalization or full Collatz conclusion is asserted.
