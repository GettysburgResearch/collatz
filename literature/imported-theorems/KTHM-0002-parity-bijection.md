# KTHM-0002 — Parity prefixes are residues modulo powers of two

**Source:** Everett, parity-vector theorem; Terras, initial encoding theorem. [@Everett1976; @Terras1976]  
**Proof status:** complete reconstruction  
**Maps to:** `PR3/L-0005` (classical inversion component), `CLAUDE/L-0004`, `CLAUDE/T-0021`

## Statement

For every `L≥0`, the map

\[
n\pmod {2^L}
\longmapsto
(T^0(n)\bmod2,\ldots,T^{L-1}(n)\bmod2)
\]

is a bijection from `Z/2^LZ` to `{0,1}^L`.

Consequently, if `N` is odd and `t` is fixed, then as `q` runs modulo `2^L`, the parity words of `Nq+t` run through all binary words exactly once.

## Proof

First show that congruent inputs have the same prefix. If `x≡y (mod 2^L)`, they have the same parity. After one shortcut step their difference is either

\[
\frac{x-y}{2}
\quad\text{or}\quad
\frac{3(x-y)}2,
\]

according to that common parity. Hence `T(x)≡T(y) (mod 2^{L-1})`. Induction gives agreement of the first `L` parities, so the map is well-defined.

Now suppose `x` and `y` have the same length-`L` parity word of weight `a`. KTHM-0001 gives the same affine constant `B` for both, so

\[
T^L(x)-T^L(y)=\frac{3^a(x-y)}{2^L}.
\]

The left side is an integer and `3^a` is odd, hence `2^L` divides `x-y`. Thus two distinct residue classes cannot have the same word. There are `2^L` classes and `2^L` words, so the map is bijective.

Finally, multiplication by odd `N` followed by translation by `t` is a bijection modulo `2^L`; compose it with the parity bijection. ∎

## Non-application

Uniformity at one finite depth does not create independence across depths and does not prove an infinite ordinary-integer orbit.
