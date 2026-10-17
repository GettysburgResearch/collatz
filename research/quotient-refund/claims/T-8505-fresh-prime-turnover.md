# T-8505 — Every infinite refund path has unbounded odd-prime support

**Claim ID:** `T-8505`  
**Status:** `PROPOSED / SOURCE-QUALIFIED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Dependencies:** `L-8504`; Evertse 1984 Corollary 1, in the normalization audited by PR #33 `L-9706` and PR #34 `T-9828`  
**Scope:** every hypothetical forever-defined ordinary orbit of `T-8504`

## Theorem

Let

\[
(t_n,i_n,k_n),\qquad t_n=t_0+16n,
\]

be an infinite ordinary orbit of the deterministic refund map, and let

\[
W_n=b_{i_n}(M_n-r_n)+M_nk_n
\]

be its intrinsic scaled physical boundary words. Then:

1. every `W_n` has a prime divisor at least `5`;
2. no prime at least `5` divides two adjacent words;
3. after removing their exact powers of `2` and `3`, adjacent primitive cores are coprime integers greater than one;
4. the union
   \[
   \bigcup_{n\ge0}\operatorname{supp}_{\rm prime}(W_n)
   \]
   is infinite;
5. more strongly, every fixed finite prime set is escaped at infinitely many stages;
6. infinitely many globally new odd primes divide the physical shifted values `n_n+34`.

In particular, no finite-prime multiplicative library, fixed `S`-unit ansatz, or bounded collection of prime-supported complement counters can produce the missing counterexample state.

## Local prime turnover

The four boundary residues are

```text
W_n mod 64 in {5,30,20,56}.
```

A `{2,3}`-smooth integer cannot occupy any of them:

- residue `5 mod 64` would require `3^a == 5 mod 64`;
- residue `30 mod 64` would require `3^a == 15 mod 32`;
- residue `20 mod 64` would require `3^a == 5 mod 16`;
- residue `56 mod 64` would require `3^a == 7 mod 8`.

The cyclic power sets of `3` modulo `64,32,16,8` omit those four targets. Therefore every `W_n` has a prime divisor `p>=5`.

The exact local stage equation is

\[
\boxed{M_nW_{n+1}=N_nW_n+b_{i_n}.}
\tag{1}
\]

If a prime divides both `W_n` and `W_(n+1)`, equation `(1)` makes it divide `b_(i_n)`. Since every `b_i` is supported only on `{2,3}`,

\[
\boxed{
\gcd(W_n,W_{n+1})\mid b_{i_n},}
\tag{2}
\]

so no prime at least `5` survives across one boundary.

## Exact primitive cores

Write

```text
b_i=2^i 3^(beta_i),
beta=(2,3,2,1).
```

`L-8504` gives

\[
\nu_2(W_n)=i_n.
\tag{3}
\]

For `n>=1`, reduce the preceding stage equation modulo powers of three. The term `N_(n-1)W_(n-1)` is divisible by a power of three strictly larger than `3`, whereas `b_(i_(n-1))` has exact ternary valuation `beta_(i_(n-1))`. Since `M_(n-1)` is a ternary unit,

\[
\boxed{
\nu_3(W_n)=\beta_{i_{n-1}}.}
\tag{4}
\]

Define

\[
\boxed{
C_n=
\frac{W_n}{2^{i_n}3^{\beta_{i_{n-1}}}}
\qquad(n\ge1).}
\tag{5}
\]

Then `C_n` is coprime to six and exceeds one. Equation `(2)` now gives the exact core turnover

\[
\boxed{
\gcd(C_n,C_{n+1})=1
\qquad(n\ge1).}
\tag{6}
\]

Thus every local connector replaces the complete prime-to-six core rather than merely changing one factor.

## Finite-support contradiction

Assume that all sufficiently late `W_n` are supported on one fixed finite prime set `S` containing `{2,3}`. At stage `n`, form the integer zero sum

\[
\boxed{
M_nW_{n+1}-N_nW_n-b_{i_n}=0.}
\tag{7}
\]

Divide its three coordinates by their common gcd to obtain one primitive projective triple `x_n`. Every coordinate is an integer `S`-unit. The triple is nondegenerate: it has one positive coordinate and two negative coordinates, and none of the three coordinates is zero, so no nonempty proper subsum vanishes.

Evertse's 1984 Corollary 1 applies with dimension `2` and outside-`S` exponent `d=0`. It permits only finitely many primitive nondegenerate projective triples of this form.

The triples here are pairwise projectively distinct. Compare the coordinate containing `M_nW_(n+1)` with the fixed toll coordinate `b_(i_n)`. Their projective ratio has binary valuation

\[
\nu_2(M_n)+\nu_2(W_{n+1})-\nu_2(b_{i_n})
=11(t_n+17)+i_{n+1}-i_n.
\tag{8}
\]

It lies in

\[
[11(t_n+17)-3,\ 11(t_n+17)+3].
\tag{9}
\]

Successive intervals are separated by `176-6>0`. Hence all projective points are distinct, contradicting Evertse finiteness.

Therefore no finite prime set supports an eventual tail. Applying the same argument after any starting index proves that every fixed finite prime set is escaped infinitely often.

## Globally new primes

Let

\[
P_n^{\rm new}
=
\prod_{\substack{p\mid W_n\\p\nmid W_0W_1\cdots W_{n-1}}}
p^{\nu_p(W_n)}.
\]

The preceding theorem implies `P_n^(new)>1` for infinitely many `n`. Consequently

\[
\boxed{
\sum_{n\ge0}\log P_n^{\rm new}=+\infty.}
\tag{10}
\]

By `L-8504`,

\[
n_n+34=2^{11t_n+5}W_n,
\]

so the odd-prime supports of `W_n` and `n_n+34` agree. Infinitely many distinct odd primes therefore divide the physical boundary shifts.

## Proof boundary

The theorem is a necessary condition, not an existence theorem. It does not supply the fresh primes, the forever-defined seed, or a finite rule generating their exact locations. It rules out a broad but tempting class of proposed invariants and shows that a successful one-counter certificate must manufacture a new coprime prime-to-six core at every step and globally new primes infinitely often.
