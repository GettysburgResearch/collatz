# L-7610 — Sharp bilateral height for complete-factor quotient jets

**Claim ID:** `L-7610`  
**Title:** The exact fixed-point height, not the coarser endpoint-plus-displacement envelope, controls complete-factor jet lifting  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-global-01` (`GPT-5.6 Pro`)  
**Reviewing agents:** none  
**Created:** 2026-08-01  
**Last updated:** 2026-08-01  
**Dependencies:** branch-qualified PR #83 corrected `L-6909` and `L-6912`; for the support corollary, branch-qualified PR #81 `L-6816` / PR #83 `T-6914`  
**Scope:** complete-factor quotient jets for coefficient-first-crossing non-descents  
**Related counterexample candidates:** none

This is a new strengthening discovered during the frozen review of PRs #80, #81, and #83. It remains `PROPOSED` and is not used to verify those source PRs.

## Statement

Let a shortcut-parity word of length `j` and weight `q` have affine map

```text
T_w(x)=(Q*x+A)/P,
P=2^j,
Q=3^q,
D=P-Q>0.
```

Suppose its canonical source and endpoint satisfy

```text
T_w(r)=s=r+d,
r,s positive ordinary integers,
d>=0.
```

Put

```text
C=Q/P,
E=A/P,
H_w=A/D=E/(1-C).
```

Then the following hold.

### A. Exact bilateral height formulas

```text
r=(E-d)/(1-C),
s=(E-C*d)/(1-C).
```

Consequently,

```text
0<r<=s<=H_w.
```

Equality `r=H_w` or `s=H_w` holds if and only if `d=0`. For an acyclic near-return `d>0`,

```text
0<r<s<H_w.
```

### B. Exact candidate-dependent jet threshold

Let `U` be a unitary divisor of `D`, with complementary factor

```text
D=U*K,
gcd(U,K)=1.
```

Assume PR #83 `L-6912` supplies residues

```text
delta_U == d mod U,
rho_U   == r mod U,
sigma_U == s mod U,
```

where `rho_U` and `sigma_U` are its source and endpoint quotient jets.

If

```text
U>H_w,
```

then all three residues lift uniquely to the exact ordinary values:

```text
delta_U=d,
rho_U=r,
sigma_U=s.
```

Equivalently, it is enough that

```text
U>=floor(A/D)+1.
```

### C. Sharper uniform first-crossing threshold

For every coefficient-first-crossing non-descent, the reviewed bilateral bound gives

```text
0<=d<E<q/3.
```

Therefore

```text
H_w=E/(1-C)<q/[3(1-C)].
```

Define

```text
B_j^sharp=ceil(q/[3(1-3^q/2^j)]).
```

Then every unitary factor satisfying

```text
U>=B_j^sharp
```

recovers `d,r,s` exactly.

This removes the additional `q/3` term from the coarser universal endpoint bound in PR #83 `L-6912`.

### D. Support-sensitive threshold

Let `u` be the upper-mechanical word at the same `(j,q)`, and suppose `w` has `R` displaced odd positions. PR #81 `L-6816` / PR #83 `T-6914` give

```text
E_w<E_u-C*R/12.
```

Hence

```text
H_w<[E_u-C*R/12]/(1-C).
```

Thus the same rough support that narrows the allowed displacement interval also lowers the exact modulus needed to recover both ordinary quotient jets.

### E. Sharpened balanced-or-dominant reduction

The elementary factor-partition argument of PR #83 `L-6912` may be repeated with `B_j^sharp` in place of its coarser bound.

In particular, if

```text
D>(B_j^sharp)^3,
```

then either:

```text
balanced:
  D=U*V for unitary U,V both larger than B_j^sharp,
  so both blocks recover the same exact d,r,s;

or

dominant:
  D=W*c for one complete prime power W with
  c<=B_j^sharp and W>D/B_j^sharp,
  so W recovers d,r,s and c must complete the divisibility.
```

The same replacement may be made with the smaller candidate-specific threshold from part D whenever the support data are already known.

## Proof

The corrected bilateral equations are

```text
A=D*r+P*d=D*s+Q*d.
```

Divide the source equation by `P`:

```text
E=(1-C)r+d,
```

which gives the formula for `r`.

Divide the endpoint equation by `P`:

```text
E=(1-C)s+C*d,
```

which gives the formula for `s`.

Because `r>0`, the source formula gives `d<E`. Since `d>=0` and `0<C<1`,

```text
r=H_w-d/(1-C)<=H_w,
s=H_w-C*d/(1-C)<=H_w.
```

Also `s-r=d>=0`. Equality in either upper bound forces `d=0`; conversely `d=0` gives `r=s=H_w`. This proves part A.

The congruences defining `delta_U,rho_U,sigma_U` are those of PR #83 `L-6912`. For a genuine near-return, all three canonical residues are congruent to `d,r,s` modulo `U`. The displacement already satisfies `0<=d<E<H_w`. Under `U>H_w`, part A places all three ordinary values in `[0,U)`, so their canonical residues modulo `U` equal the values themselves. This proves part B.

Part C follows from `E<q/3`. The ceiling is safe even when `q/[3(1-C)]` is an integer because the preceding height inequality is strict. Part D follows by dividing the support-loss inequality by the positive number `1-C`.

Finally, the balanced-or-dominant proof in `L-6912` uses only:

1. a positive integer threshold above every admissible ordinary source and endpoint;
2. the complete prime-power components of `D`;
3. multiplication of components until a unitary product crosses that threshold.

Parts C and D supply smaller thresholds with exactly the same properties, so the factor-partition proof carries over. This proves part E.

## Why the strengthening matters

PR #83 treated the displacement bound and endpoint/source height as two successive additions. The bilateral identities show that the displacement is already subtracted inside both ordinary quotient formulas.

The actual common height is the rational fixed point

```text
A/D,
```

not

```text
q/[3(1-C)]+q/3.
```

The gain is polynomial rather than exponential, so it does not by itself close FC*. It does, however:

- enlarge the set of factors whose quotient jets lift exactly;
- strengthen the balanced/dominant factor dichotomy;
- couple PR #81's square-root support loss directly to PR #83's complete-factor obstruction;
- remove avoidable slack from any future cross-prime contradiction.

## Dependency audit

- The proof uses only the corrected source/endpoint equations and the definitions of the unitary quotient jets.
- The support-sensitive clause imports the strict support loss and preserves its source status.
- No result from this file is used retroactively in the frozen verification verdicts.

## Gap audit

- Exact jet recovery is not jet incompatibility.
- Balanced blocks may still return identical `d,r,s`.
- A dominant giant factor may still be completed by its small cofactor.
- The cycle level `d=0` remains included.
- The general `gcd(j,q)>1` resultant components remain open.
- No FC*, SC*, or Collatz proof follows.

## Adversarial tests

1. At `d=0`, the bilateral formulas give `r=s=A/D`, as required for a cycle.
2. For `d>0`, the endpoint is closer to `A/D` than the source because `0<C<1`:
   ```text
   H_w-s=C*d/(1-C)<d/(1-C)=H_w-r.
   ```
3. Replacing `U>H_w` by only `U>d` is insufficient to recover the quotient jets.
4. The ceiling in part C is safe at an integral upper threshold because the height inequality is strict.
5. The theorem never infers full-denominator divisibility from one large factor.

## Remaining uncertainty

None in the elementary algebra. The usefulness of the sharper threshold for proving a uniform cross-factor contradiction is open.

## Suggested next attack

In the balanced case, compare the exact triples `(d,r,s)` recovered from the two complementary unitary blocks after applying the support-sensitive threshold. In the dominant case, exploit the now smaller cofactor bound to classify or contradict the completing cofactor. Any theorem obtained there must be submitted separately as `PROPOSED`.