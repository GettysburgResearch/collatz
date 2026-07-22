# T-8807 — Exact `2`-adic Cantor geometry of chart completions

Claim ID: T-8807  
Title: The `4 -> 5` completion set has Haar measure zero and Hausdorff dimension `1/2`  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-8801, T-8802  
Scope: the full binary completion set in `Z_2` and its ordinary integer section  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

Let

```text
C = { Phi_(4,5)(eps) : eps in {0,1}^N }
  = { (1/5) * sum_(j>=0) eps_j*(4/5)^j : eps_j in {0,1} }
  subset Z_2.
```

If two directives `eps,eta` first differ at index `j`, then

```text
v_2(Phi_(4,5)(eps)-Phi_(4,5)(eta)) = 2j.              (1)
```

Consequently:

1. The coding map is injective and isometric when `{0,1}^N` is given the
   prefix metric `4^(-j)`.
2. At level `k`, the set `C` occupies exactly `2^k` residue classes modulo
   `4^k`.
3. `C` has normalized Haar measure zero in `Z_2`.
4. `C` has `2`-adic Hausdorff dimension exactly `1/2`.
5. The set

   ```text
   S = { A in Z_(>0) : A remains forever in the exact 4 -> 5 chart }
   ```

   has upper natural density zero.

This is a quantitative thinness theorem, not an emptiness theorem.

## Definitions

- The `2`-adic metric is `|x-y|_2=2^(-v_2(x-y))`.
- A level-`k` cylinder fixes the first `k` directive bits.
- Haar measure is normalized so every residue class modulo `2^m` has measure
  `2^(-m)`.

## Motivation

The ordinary-section problem asks whether a very thin `2`-adic completion set
contains a shifted positive integer. Exact dimension separates two issues:

- symbolic abundance: there are continuum many `2`-adic chart completions;
- arithmetic rarity: they lie in a measure-zero set of dimension `1/2`, and
  ordinary positive survivors have density zero.

This provides a geometric target for Diophantine, automata, and rational-base
methods without mistaking thinness for nonexistence.

## Proof or construction

Suppose `eps_i=eta_i` for `i<j` and `eps_j-eta_j=±1`. Factor the difference:

```text
Phi(eps)-Phi(eta)
 = [4^j / 5^(j+1)]
   * [ (eps_j-eta_j)
       + sum_(r>=1) (eps_(j+r)-eta_(j+r)) * 4^r/5^r ].
```

The bracket is congruent to `±1 modulo 4`, hence is a `2`-adic unit. Since the
power of `5` is also a unit, the valuation is exactly `2j`. This proves (1),
injectivity, and the isometry.

A fixed length-`k` prefix determines one residue class modulo `4^k`, because
the remaining tail is divisible by `4^k`. Distinct prefixes differ first before
index `k`, so equation (1) shows that they occupy distinct classes. There are
therefore exactly `2^k` classes.

Their total Haar measure is

```text
2^k / 4^k = 2^(-k).
```

As `C` lies in this union for every `k`, its Haar measure is zero.

For Hausdorff dimension, the same `2^k` cylinders have diameter `4^(-k)`, giving
upper dimension at most

```text
log(2)/log(4)=1/2.
```

Push the fair Bernoulli measure on directives forward to `C`. Every level-`k`
cylinder has mass `2^(-k)` and diameter `4^(-k)`, so the mass is the square root
of the diameter. The standard mass-distribution estimate, with at most a fixed
factor adjustment for radii between consecutive powers of four, gives lower
Hausdorff dimension at least `1/2`. Thus the dimension is exactly `1/2`.

Finally, T-8802 identifies positive chart survivors with the shifted ordinary
section `A+2 in C`. For every fixed `k`, this shifted set occupies at most `2^k`
residue classes modulo `4^k`. Hence its upper natural density is at most
`2^(-k)` for every `k`; letting `k` tend to infinity gives zero. **QED**

## Dependency audit

- D-8801 supplies the completion map.
- T-8802 supplies the exact relationship between ordinary completions and
  physical chart survivors.
- The geometry uses only elementary `2`-adic valuation and cylinder counting.

## Gap audit

- Haar measure zero and density zero do not imply emptiness.
- Hausdorff dimension is computed in `Z_2`, not in the real line.
- The lower-dimension argument uses the pushforward Bernoulli measure and must
  account for arbitrary ball radii; the consecutive-scale constant does not
  change the exponent.
- The ordinary survivor set is a countable section of an uncountable Cantor set;
  dimension alone cannot decide whether that section is empty.

## Adversarial tests

The prefix/residue count is directly checkable: every length-`k` directive
prefix yields one distinct residue modulo `4^k`. X-8802 separately profiles
finite ordinary roots and confirms the expected initial halving pattern before
arithmetic correlations appear.

## Remaining uncertainty

The decisive arithmetic question is whether `C` contains any ordinary integer
strictly larger than `2` after the shift required by T-8802.

## Suggested next attack

Prove a quantitative intersection theorem between `C` and ordinary integers.
Possible routes include rational-base bottom-word transducers, `S`-unit or
Subspace-Theorem estimates for unusually long low-digit prefixes, or a finite
residue invariant that improves the trivial `2^k` cylinder count.
