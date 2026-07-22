# T-9420 — Rational binary survivor codes are exactly eventually periodic

Claim ID: `T-9420`  
Title: A binary `64/81` code has rational value if and only if its digit word is eventually periodic  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `D-9401`, `L-9402`, `L-9417`  
Scope: the entire binary survivor attractor  
Related counterexample candidates: issue #4 M1; no `K-####` candidate

## Theorem

For every

```text
epsilon in {0,1}^N,
```

the following are equivalent:

1. `Phi(epsilon)` is rational;
2. the unscaled value
   ```text
   S_0=sum_(n>=0)epsilon_n(64/81)^n
   ```
   is rational;
3. `epsilon` is eventually periodic.

Thus

```text
boxed:
Phi({0,1}^N) intersect Q
 = {Phi(epsilon): epsilon eventually periodic}.       (1)
```

## Proof that eventual periodicity implies rationality

Suppose `epsilon` has preperiod `r` and period `s>=1`. Put `T=64/81`. Then

```text
S_0
 =sum_(n=0)^(r-1) epsilon_n T^n
  +T^r
    [sum_(j=0)^(s-1)epsilon_(r+j)T^j]/(1-T^s).        (2)
```

This is rational, and multiplication by `17/81` makes `Phi(epsilon)` rational.

## Proof that rationality implies eventual periodicity

Assume `S_0` is rational. For every `n`, define

```text
S_n=sum_(k>=0)epsilon_(n+k)T^k.                       (3)
```

By `L-9417`, every `S_n` is rational and its reduced denominator divides one
fixed positive odd integer `B`, the initial denominator.

In the real embedding,

```text
0<=S_n<=sum_(k>=0)T^k=1/(1-T)=81/17.                 (4)
```

There are only finitely many rational numbers in the interval `[0,81/17]`
whose reduced denominator divides `B`: for each divisor `b|B`, the numerator is
an integer in the finite interval

```text
0<=a<=81b/17.                                         (5)
```

Hence the infinite tail-state sequence `(S_n)` repeats. Choose `r<s` with

```text
S_r=S_s.                                              (6)
```

The scaled values satisfy

```text
Phi(sigma^r epsilon)=Phi(sigma^s epsilon).             (7)
```

`L-9402` proves that `Phi` is injective on binary sequences. Therefore

```text
sigma^r epsilon=sigma^s epsilon,                       (8)
```

which is exactly eventual periodicity with period `s-r`. **QED**

## Finite-state interpretation

If `S_0=A/B` is rational, all digit tails lie in the explicit finite set

```text
R_B
 ={a/b in [0,81/17]: b|B, gcd(a,b)=1}.                (9)
```

The deterministic update

```text
S_(n+1)=81(S_n-epsilon_n)/64                           (10)
```

therefore evolves in a finite rational state space. Injectivity converts state
recurrence into exact digit-tail recurrence.

This gives an effective, though not optimized, preperiod-plus-period bound:

```text
r+s<=|R_B|
 <=sum_(b|B)(floor(81b/17)+1).                         (11)
```

## Relationship to standard p-adic periodicity

The conclusion resembles the classical theorem that rational `p`-adic numbers
have eventually periodic base-`p` digit expansions. Here the digit radix is the
rational contraction `64/81`, not an ordinary integral base. The proof is
native: the odd unit `81` creates no new denominator, `64` is paid by exact
`2`-adic numerator divisibility, and the simultaneous real contraction bounds
the tail states.

No external periodic-expansion theorem is needed.

## Consequences

1. `T-9418` follows immediately: a rational infinite-support code has eventually periodic, hence bounded, gaps.
2. Every sparse positive stack directive of `T-9419` is irrational because its increasing gaps prevent eventual periodicity.
3. Every rational point of the binary survivor attractor has a finite replay certificate: preperiod, period, and the rational formula (2).
4. Any ordinary M1 witness would have to be eventually periodic. `T-9421` shows that only the two trivial integer values survive this classification.

## Dependency audit

- `L-9417` supplies the fixed finite denominator set.
- The real geometric bound (4) supplies finite height.
- `L-9402` supplies exact injectivity.
- The converse direction is the elementary geometric formula (2).

No Padé theorem, linear-independence result, density estimate, or finite
experiment is used.

## Gap audit

- The theorem is specific to the rational digit alphabet and to a contraction
  whose numerator is a positive power of the `2`-adic uniformizer while the
  denominator is a `2`-adic unit.
- A signed or unbounded digit alphabet can destroy the finite real-state bound.
- Rationality is classified; algebraicity of higher degree is not.
- Eventual periodicity does not imply that the value is an ordinary integer.

## Adversarial tests

`X-9413` exhausts short preperiod/period pairs, verifies formula (2), checks the
digit-tail denominator divisor chain, and confirms that repeated rational tail
states reproduce the exact digit suffix.

## Suggested next attack

Apply the real range of an eventually periodic code to classify the ordinary
integer section. Since the rational formula is completion-independent and the
real code value lies in `[0,1]`, only `0` and `1` can occur. This is `T-9421`.
