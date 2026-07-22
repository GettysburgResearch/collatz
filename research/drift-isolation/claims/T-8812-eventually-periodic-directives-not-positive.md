# T-8812 — Eventually periodic directives have no positive ordinary completion

Claim ID: T-8812  
Title: An eventually periodic `4 -> 5` chart directive completes only to a nonpositive rational seed  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-8801, T-8802  
Scope: every eventually periodic binary phase directive  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

Let `eps=(eps_j)_(j>=0)` be an eventually periodic sequence with
`eps_j in {0,1}`. Define its chart completion in `Q_2` by

```text
Phi(eps)=(1/5)*sum_(j>=0) eps_j*(4/5)^j,
A=Phi(eps)-2.
```

Then `Phi(eps)` is rational and

```text
-2 <= A <= -1
```

in the real embedding. In particular, `A` is not a positive ordinary integer.
Therefore no positive infinite orbit of the exact `4 -> 5` chart can have an
eventually periodic phase directive or bottom word.

## Motivation

Finite-state and periodic symbolic constructions are natural first attempts at
closing an expanding chart. This theorem proves that the ordinary-completion
obstruction defeats the entire eventually periodic class, including arbitrary
finite steering prefixes.

## Proof

Choose a preperiod length `r>=0` and period length `s>=1` such that the tail is
periodic. Splitting the series at `r` and summing the periodic tail as a geometric
series shows that `Phi(eps)` belongs to `Q`. Explicitly, if

```text
U=sum_(j=0)^(r-1) eps_j*4^j*5^(r-1-j)
```

and

```text
V=sum_(j=0)^(s-1) eps_(r+j)*4^j*5^(s-1-j),
```

then

```text
Phi(eps)
 = U/5^r + 4^r*V/[5^r*(5^s-4^s)],
```

with the first term interpreted as zero when `r=0`. Thus the `2`-adic series
and the ordinary real geometric series evaluate to the same rational number.

In the real absolute value all summands are nonnegative, and `eps_j<=1`, so

```text
0 <= Phi(eps)
   <= (1/5)*sum_(j>=0)(4/5)^j
   = 1.
```

Subtracting two gives

```text
-2 <= A <= -1.
```

If the `2`-adic completion were a positive ordinary integer, it would be that
same rational number in `Q`, contradicting the displayed real inequality.

Finally, `T-8802` identifies positive ordinary chart orbits with these
completions. The bottom word is the coordinatewise complement of the phase
word, so eventual periodicity is preserved under the change of symbols. **QED**

## Dependency audit

- `D-8801` supplies `Phi_(4,5)`.
- `T-8802` supplies the physical interpretation `A=Phi(eps)-2` and the
  phase/bottom-word translation.
- Only finite and geometric sums are used.

## Gap audit

- The proof applies because the directive is eventually periodic, making the
  completion one rational number evaluated in two completions.
- It does not identify the real and `2`-adic sums of a general aperiodic
  directive.
- It does not exclude non-eventually-periodic finite-state systems driven by an
  external input.
- The endpoint values occur: all-zero gives `A=-2`; all-one gives `A=-1`.

## Adversarial tests

Constant, purely periodic, and finite-prefix-plus-periodic directives all fall
under the same formula. Direct substitutions reproduce the two negative fixed
phase completions from `T-8802`.

## Remaining uncertainty

None known in the rational/geometric argument. Independent reconstruction is
still required before status promotion.

## Suggested next attack

Use `D-8802` to convert this theorem into an exact no-go result for autonomous
bounded-state certificates, then focus constructive work on genuinely
aperiodic unbounded-state mechanisms.
