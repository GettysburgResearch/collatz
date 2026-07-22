# Linear-height quotient-refund packet

**Agent:** `gpt56-cylinder-01`  
**Issue:** `#43`  
**Namespace:** `85xx`  
**Status:** theorem-level claims are `PROPOSED`; `X-8501`--`X-8503` are exact finite interface audits

## Headline

The frozen doubling-scale architecture in PR #33 loses its ordinary quotient to the next complete radix. This packet changes the padding schedule to

\[
t_n=t_0+16n.
\]

The resulting architecture is outside that negative theorem. Refund does not require a 256-transition stage. For one connector,

\[
N_t=3^{7(t+1)},
\qquad
Q_t=2^{11(t+33)}.
\]

At every multiple of `16` with `t>=3744`,

\[
\boxed{N_t>2Q_t.}
\]

A legal ordinary residual transition therefore doubles its residual counter.

## Causal connector arithmetic

The connector inverse is generated from one ordinary Bezout carry

\[
Nr=1+Mc
\]

and one six-bit cell. The carry advances from `t` to `t+16` by appending one exact base-`3^112` digit while the binary modulus gains `176` bits. No completed logarithm or inverse tape is initialized.

`L-8502` gives the full connector from `(r,c)` by finite formulas for

```text
omega_i,
delta_(ij) mod64,
one wrap bit,
eta_(ij),
theta_(ij).
```

## The one-counter normal form

`L-8503` removes target-type and residual bookkeeping. Put

\[
d=M-r,
\qquad
e=N-c.
\]

For source type `i`, define

\[
W_{t,i}(k)=b_i d+Mk,
\]

\[
W^+_{t,i}(k)=b_i e+Nk.
\]

Then

\[
M W^+_{t,i}(k)=N W_{t,i}(k)+b_i,
\qquad
W_{t,i}(k)\equiv p_i\pmod{64}.
\]

The output residue modulo `64` uniquely selects the next type. The next complement quotient exists exactly when the output lies in one explicit next-scale residue class. Thus the complete exact state is only

```text
(height t, current type i, ordinary complement counter k).
```

There is no externally supplied infinite directive.

## Complete conditional counterexample theorem

`T-8504` proves that, for `t>=3744` and `k>=256`, every legal update satisfies

\[
\boxed{k_{n+1}\ge2k_n.}
\]

Therefore one finite state `(t_0,i_0,k_0)` whose deterministic partial map is defined forever initializes the explicit positive integer

\[
\boxed{
n_0=2^{11(t_0+1)}\frac{b_{i_0}(M_0-r_0)+M_0k_0}{64}-34
}
\]

and proves every future shortcut-Collatz block, positivity, and unboundedness.

Growth and future type selection are no longer separate open obligations. The sole positive gap is infinite definedness from one finite ordinary counter. `T-8501` gives the equivalent formulation in PR #3's canonical residual coordinate and is retained as a cross-check.

## Intrinsic unimodular physical marker

`L-8504` proves that the complement basis is unimodular:

\[
\boxed{
\begin{pmatrix}M&M-r\\N&N-c\end{pmatrix}
\in\operatorname{SL}_2(\mathbb Z).
}
\]

For consecutive boundary words `(W,U)`,

\[
\boxed{k=(N-c)W-(M-r)U,}
\]

\[
\boxed{b_i=MU-NW.}
\]

The two cone edges are neighboring Farey fractions,

\[
\frac{N-c}{M-r}-\frac NM=\frac1{M(M-r)},
\]

and every positive refunded connector lies strictly between them.

More importantly, the physical boundary integer itself contains the stage marker. For

\[
n=2^{11(t+1)}W/64-34,
\]

one has

\[
\boxed{\nu_2(n+34)=11t+5+i.}
\]

Since `16|t`, the residue of this valuation modulo `176` recovers `i`, then recovers `t`; the odd boundary word recovers `k`. A verifier may therefore begin with the single written integer `n_0`. It need not trust separately supplied stage or type metadata.

## Necessary fresh-prime turnover

`T-8505` proves that every hypothetical infinite refund path must manufacture genuinely new arithmetic content forever.

Each boundary word lies in one of

```text
5, 30, 20, 56 modulo 64,
```

and none of these classes contains a `{2,3}`-smooth positive integer. Hence every boundary word has a prime divisor at least `5`.

The local equation gives

\[
\gcd(W_n,W_{n+1})\mid b_{i_n},
\]

so no prime at least `5` divides two consecutive boundary words. Finally, a fixed finite eventual prime support would turn every local equation into infinitely many distinct primitive nondegenerate `S`-unit triples, contradicting Evertse's 1984 finiteness theorem. Therefore:

\[
\boxed{
\bigcup_n\operatorname{supp}_{\rm prime}(W_n)
\text{ is infinite},
}
\]

and infinitely many globally new odd primes divide the physical values `n_n+34`.

A successful invariant cannot be a fixed-prime multiplicative library or bounded collection of prime-supported counter templates.

## Other structural filters

`T-8502` proves that the set of all compatible initial completions has Haar measure zero and `2`-adic Hausdorff dimension zero. At depth `N`, the directive exposes at most `2N` symbolic bits while exact continuation demands

\[
88N^2+(11t_0+275)N
\]

residue bits.

`T-8503` applies the fully inspected Väänänen–Wallisser theorem to the exact linear-grid completion series. Every eventually periodic local type tail of minimal period at most `58` is irrational and nonordinary; the source condition first fails at `59`.

A witness must therefore be an exceptional ordinary point generated by genuinely unbounded arithmetic state. Entropy, a short autonomous controller, and a fixed prime library do not supply it.

## Verification

```bash
python3 -B experiments/X-8501-linear-refund/derive.py \
  --output experiments/X-8501-linear-refund/results/canonical.json \
  --summary experiments/X-8501-linear-refund/results/summary.txt
python3 -B experiments/X-8501-linear-refund/verify.py \
  --check-results experiments/X-8501-linear-refund/results/canonical.json

python3 -B experiments/X-8502-complement-quotient/derive.py \
  --output experiments/X-8502-complement-quotient/results/canonical.json \
  --summary experiments/X-8502-complement-quotient/results/summary.txt
python3 -B experiments/X-8502-complement-quotient/verify.py \
  --check-results experiments/X-8502-complement-quotient/results/canonical.json

python3 -B experiments/X-8503-unimodular-physical-marker/derive.py \
  --output experiments/X-8503-unimodular-physical-marker/results/canonical.json \
  --summary experiments/X-8503-unimodular-physical-marker/results/summary.txt
python3 -B experiments/X-8503-unimodular-physical-marker/verify.py \
  experiments/X-8503-unimodular-physical-marker/results/canonical.json
```

Each checker is separately written and imports no derivation module.

## Review order

1. `D-8501-linear-connector-refund-class.md`
2. `L-8502-inverse-carry-connector-normal-form.md`
3. `L-8503-complement-quotient-normal-form.md`
4. `T-8504-single-counter-refund-map.md`
5. `L-8504-unimodular-physical-marker.md`
6. `T-8505-fresh-prime-turnover.md`
7. `T-8501-deterministic-refund-decoder.md`
8. `L-8501-fixed-width-linear-refund.md`
9. `T-8502-quadratic-cylinder-pressure.md`
10. `T-8503-period-58-irrationality.md`
11. `Q-8501-infinite-defined-residual.md`
12. `experiments/X-8501-*`, `X-8502-*`, and `X-8503-*`

## Scope boundary

This packet is not a Collatz counterexample. It is an integer-first reduction that leaves one exact safety property open. A long valid prefix, zero-dimensional completion set, modular lasso, causal inverse carry, or qualitative fresh-prime condition does not prove that one finite ordinary counter survives forever.
