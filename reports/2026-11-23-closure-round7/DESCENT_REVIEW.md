# Independent review of the delayed-prime and ordinary-shadow construction

23 November 2026. Reviewer: the independent germ-construction lane.
Parent checkpoint: `e4367dd2c4406c1041e66d82dfba822908747fa3`.

**Result: PASS for the stated written theorems OD7.1--OD7.3 and the
bounded exact controls. No mathematical correction was required.**
This is a written mathematical review and an independent deterministic
replay. It is not a Lean formalization of the analytic or Hensel arguments.
It does not certify a universal ordinary descent or germ-construction
theorem.

## Exact reviewed artifacts

| Path | Git blob | SHA256 |
| --- | --- | --- |
| `research/closure-round7-20261123/ORDINARY_DESCENT.md` | `7bd74242edac13f4f1a6aa28e95cd25c06616cd8` | `613188d23cf7bdaa15eb5f64563e5d6af1de8bf239d1ddbd9c7d59cfe0d946a6` |
| `research/closure-round7-20261123/descent_controls.py` | `89ae71328850ffb48f655219c40472353665e8ed` | `3cbf78515a1324c63141eb1f66f5c01b811dfa54e35a1cbfa8130388ffc7223d` |

The note and the complete control implementation were read. The proofs
below were reconstructed independently before accepting the replay.

## 1. Complete rational family and real floor

The concatenation formula gives the complete polynomial numerator of
`W_m=u^(m-1)v`. At two it gives

\[
C_{W_m}=C(S_m+Q^{m-1}),\qquad
D_{W_m}=(Q-P)S_m,
\]

with the complete denominator retained. Since `gcd(S_m,Q)=1`, also
`gcd(S_m,S_m+Q^(m-1))=1`. An ordinary source would therefore require
`S_m|C`, contradicted by `S_m>=Q^(m-1)>=Q>P>C>0`. This excludes this
specific family; it is not an exclusion of all ordinary cycles.

The inverse even and odd branches preserve odd denominators and force
their prescribed parities. The full affine fixed-point equation makes
their composition return to the proposed source. Starting at the
positive fixed point, forward literal iteration then stays positive.
The unique longest cyclic zero run proves primitivity and hence the
full state period, not merely the length of a displayed repeated word.

The block maps have fixed points `q` and `2q`. Repeated `u` boundaries
stay strictly above `q`; the `v` block first halves such a state and
then has increasing odd steps and decreasing even steps ending above
`q`. Thus every state is strictly above `q/2`. This argument works for
**every** `m>=2`, so choosing a larger Hensel lift to obtain a desired
delay cannot spoil the floor.

The arithmetic-progression approximation choosing
`A=20s+3`, `p=20r+1`, and `A-p log_2(3)` positive and tending to zero
is valid. Irrational-rotation density persists after removal of any
finite prefix, so the chosen `r` can tend to infinity. Then `A-p>=2`
eventually and

\[
q=\frac{1-(2/3)^p}{2^{A-p\log_2 3}-1}\longrightarrow\infty.
\]

Choose this clock first, with `q>2M`, and choose the Hensel parameter
`m` afterwards. This proves the simultaneous arbitrary-floor claim.

## 2. Exact five-adic delay

The residue conditions imply `v_5(2^A-3^p)=1` and `5` divides neither
`A` nor `m`. The root `alpha=2 mod 5` of `z^A-3^p` is therefore simple
and satisfies `v_5(alpha-2)=1`. Both prefactors of

\[
N_{W_m}(\alpha)=P^{m-1}N_u(\alpha)(m-1+\alpha)
\]

are units. Factoring `(1-m)^A-alpha^A` gives a unit second factor, so
the numerator valuation at the root is exactly
`K=v_5((1-m)^A-3^p)`.

Removing the actual factor `t-(alpha-2)` from the **full** translated
denominator leaves a polynomial `U` with unit constant coefficient:
the original constant coefficient and `alpha-2` both have valuation
one. Consequently `U^(-1)` has integral coefficients and unit constant
coefficient. The polar term at Taylor order `j` has valuation exactly
`K-j-1`; the remaining term is integral. When that valuation is
negative, cancellation by the integral term is impossible. For lower
orders both terms are integral. This proves precisely

\[
v_5(\operatorname{den}(c_j))=\max(0,j+1-K).
\]

The digit-lifting step has one root lift and four nonroot lifts at each
depth because the derivative is a unit. Choosing a nonroot lift gives
the requested exact valuation. The expression cannot be zero as an
ordinary integer because `A` is odd and `m>=2`.

This delays **only prime five**. The full source is nonintegral, while
the formula shows five is absent from its constant denominator. Its
odd complete denominator is also coprime to three. Thus another
forbidden prime is already present at Taylor order zero. The note
correctly disclaims an arbitrarily long initial jet in `Z[1/3]` and
does not claim an ordinary-cycle counterexample.

## 3. Genuinely convergent ordinary shadows

For any prescribed finite word containing an odd step, the last odd
term of its complete carry is a unit modulo three; all earlier odd
terms contain a factor of three. Hence the carry is a unit modulo
`3^s`.

Two has order `2*3^(s-1)` modulo `3^s`. The induction underlying this
claim is exact: if `v_3(a-1)>=1`, cubing raises `v_3(a-1)` by exactly
one, because the linear term has strictly smaller valuation than the
remaining binomial terms. Starting with `2^2-1=3` supplies the stated
order at every level. Therefore one can solve
`2^(h+b)=C_w mod 3^s` and then increase `b` by any multiple of that
order.

The resulting ordinary integer

\[
n=(2^{h+b}-C_w)/3^s
\]

can be made larger than any requested real bound. Reverse-branch
legality supplies the prescribed parity word, and its integral start
makes each literal forward state integral. The endpoint is exactly
`2^b`; the following `b` even steps reach one. These witnesses are
proved convergent, rather than merely finite parity realizers.

The shared-prefix identity for the **actual** germs supplies the
coefficient bound `v_2(c_j(n)-c_j(r))>=h-j`. The proof retains the
entire tail difference and uses its binary integrality. The explicit
standard tail gives a common denominator `3^s` for every coefficient
of each constructed ordinary germ. Both arguments are valid.

As the requested prefix grows, the ordinary source is allowed to
change and need not stay bounded. There is no fixed ordinary source
with the complete nonintegral rational itinerary. The nonclosure of
`Z[1/3]` under these binary limits is correctly used only to block
that finite-approximation inference.

## 4. Independent replay

The reviewer executed:

```sh
python -X utf8 -B research/closure-round7-20261123/descent_controls.py
```

The result was `PASS`. The rational fixtures have literal periods
`12, 42, 117, 1242, 24732` and exact five-adic delay orders
`1, 2, 3, 4, 1`, respectively. The final fixture certifies every
literal rational cycle state strictly above eleven. The ordinary
shadows have power-of-two endpoint exponents `36` and `2520` and
both were replayed through one. Eight actual Taylor coefficients per
ordinary shadow were checked.

The full deterministic output has SHA256
`7da303d48193b0b646cf74a2498defaff4a9d16251fff3be99d4b4ebfa5696d9`.
The controls use explicit runtime checks and exact arithmetic. Their
bounded success is separate from the all-order and arbitrary-floor
written proofs reviewed above.
