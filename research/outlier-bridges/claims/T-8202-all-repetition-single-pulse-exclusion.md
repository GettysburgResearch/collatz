# T-8202 — All-repetition exclusion of single-pulse lifts of the two known negative cycles

**Claim ID:** `T-8202`  
**Status:** `PROPOSED / SOURCE-DEPENDENT`  
**Authoring agent:** `gpt56-outlier-01`  
**Reviewing agents:** none yet  
**Created:** 2026-07-23  
**Last updated:** 2026-07-23  
**Issue:** #52  
**Dependencies:** exact single-pulse affine reduction reconstructed below; E. M. Matveev's explicit real linear-form theorem in the form recorded in `SOURCE_LEDGER_ALL_REPETITION.md`; elementary continued-fraction facts  
**Scope:** one upward valuation pulse in an arbitrary repetition and rotation of either known ordinary negative accelerated Collatz cycle

## Statement

Consider either primitive accelerated negative cycle word

```text
P3  = (1,2),                 (A,k)=(3,2),
P11 = (1,1,1,2,1,1,4),      (A,k)=(11,7).
```

Repeat the chosen primitive word `r>=1` times, cyclically rotate it arbitrarily, and increase one valuation by an arbitrary integer `delta>=1`.

Subject to the exact Matveev theorem formulation recorded in the source ledger, the resulting accelerated word cannot encode a nontrivial positive integral Collatz cycle.

The only reduced divisibility hit in the entire two-family parameter space is

```text
P3, r=1, delta=1, rotated negative state z=-5,
(1,2) -> (2,2),
positive fixed point n=1.
```

Thus the unique hit is the trivial accelerated Collatz cycle. In particular, the finite repetition limit in branch-qualified PR #47 `X-9601` is removed for these two single-pulse families.

No divergent orbit, nontrivial positive cycle, or unconditional Collatz counterexample is constructed.

## Definitions

For one primitive cycle let

```text
U=2^A,
Q=3^k,
alpha=log_2(Q/U)=k log_2(3)-A > 0.
```

After `r` repetitions and one pulse of height `delta`, define

```text
D_(r,delta)=U^r 2^delta-Q^r.
```

A positive accelerated cycle requires `D_(r,delta)>0`.

For a rotated negative state `z`, put

```text
c_z = odd part of |3z+1|.
```

The relevant odd coefficients are

```text
P3:  z in {-5,-7},
     c_z in {7,5},
     c_max=7;

P11: z in {-17,-25,-37,-55,-41,-61,-91},
     c_z in {25,37,55,41,61,91,17},
     c_max=91.
```

Finally define the positive real linear form

```text
Lambda=(Ar+delta) log(2)-kr log(3)
      =(delta-r alpha) log(2).
```

Since `D_(r,delta)>0`, one has `Lambda>0`.

## Motivation

PR #47 reduced every single pulse to a divisibility condition and checked repetitions through `20000`. PR #53 `L-8201` showed that every fixed pulse cone is finite, but it did not control repetition length.

The unexpected bridge is to the standard Diophantine architecture

```text
exact divisibility
 -> exponentially close powers of 2 and 3
 -> real linear form in log(2), log(3)
 -> explicit Baker–Matveev cutoff
 -> certified continued-fraction reduction
 -> finite exact rejection.
```

The resulting proof is not another bounded scan. Matveev removes every repetition beyond an explicit cutoff, and continued fractions represent every smaller repetition symbolically by sixteen primitive rational approximants.

## Proof

### 1. Exact single-pulse reduction

Let `w=(a_0,...,a_(k-1))` be a cyclic rotation of one primitive negative cycle with negative odd fixed point `z`. Its accelerated affine numerator satisfies

```text
C_w=z(2^A-3^k).
```

Repeat `w` `r` times and increase the first valuation by `delta`. The perturbed numerator is

```text
C_(r,delta)
 = z D_(r,delta)
   -(2^delta-1)(3z+1)3^(kr-1).
```

This follows by separating the first numerator term: that term is unchanged by the pulse, while every later term is multiplied by `2^delta`.

If the perturbed fixed point is integral, then `D_(r,delta)` divides the correction term. The denominator is odd and coprime to `3`, so powers of `2` and `3` may be removed. Hence the necessary condition is

```text
D_(r,delta) | c_z(2^delta-1).                 (1)
```

Eliminating all nontrivial solutions of (1) is therefore enough to exclude all nontrivial positive-cycle certificates in this family.

### 2. Divisibility forces exponential logarithmic proximity

Write

```text
U^r 2^delta = Q^r exp(Lambda).
```

Then

```text
D_(r,delta)
 =U^r 2^delta(1-exp(-Lambda)).
```

Condition (1) gives

```text
0 < 1-exp(-Lambda)
  = D_(r,delta)/(U^r 2^delta)
  <= c_z(1-2^(-delta))/U^r
  < c_z/U^r.                                  (2)
```

For `P3` with `r>=2`, and for `P11` with `r>=1`, one has `c_z/U^r<1/2`. The sole omitted case `P3,r=1` is handled exactly in Section 7. For `0<x<1/2`,

```text
-log(1-x)<2x.
```

Applying this to (2) in those ranges yields

```text
0 < Lambda < 2c_z/U^r <= 2c_max/U^r.          (3)
```

Equivalently,

```text
0 < delta/r-alpha
  < 2c_max/(r log(2) U^r).                    (4)
```

This is the central scale separation: a divisor hit requires an exponentially accurate rational approximation to `alpha`.

### 3. Explicit Matveev cutoff

Use the real linear form

```text
Lambda=b_1 log(2)+b_2 log(3),
b_1=Ar+delta,
b_2=-kr.
```

The numbers `2` and `3` are multiplicatively independent, so `Lambda` is nonzero. In the quoted Matveev formulation, for `n=2` and field degree `D=1`, take

```text
A_1=log(2),
A_2=log(3),
K=2^32 log(2)log(3).
```

For the large-`r` regime used below, (3) gives `Lambda<log(3)`, and therefore

```text
B=max{1, |b_1|A_1/A_2, |b_2|}
 =kr+Lambda/log(3)
 <kr+1.
```

Matveev therefore gives

```text
log(Lambda) >= -K(1+log(kr+1)).                (5)
```

On the other hand, (3) gives

```text
log(Lambda) < log(2c_max)-r log(U).            (6)
```

A solution must consequently satisfy

```text
r log(U)
 < log(2c_max)+K(1+log(kr+1)).                 (7)
```

Define

```text
f(r)=r log(U)-log(2c_max)-K(1+log(kr+1)).
```

The exact rational interval checker certifies the following.

| Family | cutoff `M` | certified lower bound for `f(M)` | certified lower bound for `f'(M)` |
|---|---:|---:|---:|
| `P3` | `50,000,000,000` | `17,861,829,773.921177960152` | `2.014029188867441174` |
| `P11` | `12,000,000,000` | `5,955,423,784.974198434066` | `7.352067516108272742` |

Moreover

```text
f'(r)=log(U)-Kk/(kr+1)
```

is increasing. Hence `f(r)>0` for every `r>=M`, contradicting (7). Therefore every possible solution has

```text
P3:  r < 50,000,000,000,
P11: r < 12,000,000,000.                       (8)
```

The source theorem is the only non-elementary external dependency in this step. The numerical inequalities in the table are exact rational interval certificates, not floating-point tests.

### 4. Legendre reduction below the cutoff

For `P3`, the exact checker certifies at `r=3`

```text
log(2)U^r-4c_max r > 270.891356446691998421.
```

For `P11`, it certifies at `r=1`

```text
log(2)U^r-4c_max r > 1055.565425786767993686.
```

Since `U^r/r` increases thereafter, (4) implies

```text
|delta/r-alpha| < 1/(2r^2)                     (9)
```

for

```text
P3:  r>=3,
P11: r>=1.
```

Write the fraction `delta/r` in lowest terms as `p/q`, so

```text
r=mq,
delta=mp,
m>=1.
```

The classical Legendre criterion applied to (9) shows that `p/q` is a continued-fraction convergent of `alpha`. Since `delta/r>alpha`, only upper convergents can occur.

The checker does not evaluate `alpha` with a floating-point library. It evaluates

```text
log(x)=2 sum_(j>=0) z^(2j+1)/(2j+1),
z=(x-1)/(x+1),
```

with an exact rational tail bound, producing intervals narrower than `2^-574`. Every continued-fraction digit below the cutoffs is therefore certified.

### 5. Certified primitive candidates

For `P3`, the certified continued fraction begins

```text
alpha=[0;5,1,7,1,2,4,11,1,2,2,3,27,1,9,1,1,3,7,1,19,...].
```

The upper convergents with primitive denominator below the Matveev cutoff are

```text
1/5,
8/47,
26/153,
1269/7468,
4033/23734,
32377/190537,
916004/5390637,
10043667/59106470,
67557657/397573379,
559632586/3293409335.
```

For `P11`, the certified continued fraction begins

```text
alpha=[0;10,1,1,4,166,1,11,7,1,35,1,114,3,...].
```

The upper convergents below the cutoff are

```text
1/10,
2/21,
1496/15791,
18051/190537,
145913/1540182,
5380730/56796197.
```

These sixteen primitive fractions represent every remaining possible pair `(r,delta)`: a putative pair must be a positive integral multiple `(mq,mp)` of one row.

### 6. Every positive multiple is impossible

Let `p/q` be one of the certified upper convergents and let `q_+` be the next convergent denominator. The exact continued-fraction identity gives

```text
p-q alpha > 1/(q+q_+).                         (10)
```

For a putative multiple `(r,delta)=(mq,mp)`,

```text
Lambda=m(p-q alpha)log(2)
       > log(2)/(q+q_+).                        (11)
```

But (3) gives

```text
Lambda < 2c_max/U^(mq) <= 2c_max/U^q.          (12)
```

Since `log(2)>1/2`, equations (11)--(12) are incompatible whenever

```text
U^q > 4c_max(q+q_+).                           (13)
```

The following exact table verifies (13) for all sixteen rows. `Aq` is the exponent in `U^q=2^(Aq)`.

| Family | `p/q` | `q_+` | `Aq` | `4c_max(q+q_+)` |
|---|---:|---:|---:|---:|
| `P3` | `1/5` | `6` | `15` | `308` |
| `P3` | `8/47` | `53` | `141` | `2,800` |
| `P3` | `26/153` | `665` | `459` | `22,904` |
| `P3` | `1269/7468` | `8133` | `22,404` | `436,828` |
| `P3` | `4033/23734` | `55601` | `71,202` | `2,221,380` |
| `P3` | `32377/190537` | `5200100` | `571,611` | `150,937,836` |
| `P3` | `916004/5390637` | `53715833` | `16,171,911` | `1,654,981,160` |
| `P3` | `10043667/59106470` | `112822303` | `177,319,410` | `4,814,005,644` |
| `P3` | `67557657/397573379` | `2895835956` | `1,192,720,137` | `92,215,461,380` |
| `P3` | `559632586/3293409335` | `65470613321` | `9,880,228,005` | `1,925,392,634,368` |
| `P11` | `1/10` | `11` | `110` | `7,644` |
| `P11` | `2/21` | `95` | `231` | `42,224` |
| `P11` | `1496/15791` | `15886` | `173,701` | `11,530,428` |
| `P11` | `18051/190537` | `1349645` | `2,095,907` | `560,626,248` |
| `P11` | `145913/1540182` | `55256015` | `16,942,002` | `20,673,815,708` |
| `P11` | `5380730/56796197` | `6530022473` | `624,758,167` | `2,397,601,995,880` |

The checker compares powers by exact bit length, so it never constructs the largest displayed power of two.

Thus every `P3` case with `r>=3` and every `P11` case with `r>=1` is impossible.

### 7. Exact small cases and the unique trivial hit

Only `P3` repetitions `r=1,2` remain outside the Legendre range.

For `r=1`, positivity begins at `delta=1` and

```text
D=8*2-9=7.
```

The two odd coefficients are `5` and `7`. Hence exactly one reduced divisor hit occurs:

```text
7 | 7(2^1-1).
```

It corresponds to `z=-5`. Direct substitution in the exact fixed-point formula gives

```text
n=-5-((2^1-1)(3(-5)+1)3)/7
  =-5+6
  =1.
```

The valuation word is `(2,2)`, the trivial accelerated cycle.

For `r=2`, the least positive denominator is

```text
D=8^2*2-9^2=47,
```

already larger than either target `c(2^1-1)`. For later `delta`,

```text
D-c(2^delta-1)
 =2^delta(8^2-c)-9^2+c
```

strictly increases because `8^2>c`. Therefore there are no hits.

This completes the exclusion. ∎

## Dependency audit

1. The single-pulse affine identity is reconstructed in Section 1; branch-qualified PR #47 `L-9601` is a consistency source rather than an inaccessible black box.
2. The exact negative-cycle words and their ordinary negative states are replayed by `X-8202`.
3. Matveev's explicit theorem is used exactly once, in Section 3, with `n=2`, degree `1`, `A_1=log(2)`, and `A_2=log(3)`.
4. The continued-fraction interval construction, cutoff inequalities, candidate table, and small cases are recomputed independently by two standard-library programs.
5. The classical Legendre criterion and the lower bound (10) are elementary continued-fraction facts. The latter follows directly from the complete-quotient formula
   ```text
   |alpha-p_n/q_n|
    =1/[q_n(q_n alpha_(n+1)+q_(n-1))]
    >1/[q_n(q_n+q_(n+1))].
   ```

## Gap audit

- **External theorem inspection.** The exact Matveev statement was located in a zbMATH review mirrored by the MaRDI portal and tied to the primary DOI. An independent reviewer must reconstruct the theorem from the primary paper and verify that no omitted convention changes `A_j`, `B`, the logarithm branch, or the constant `2^(6n+20)`.
- **Status inheritance.** Until that source reconstruction is complete, this claim remains `PROPOSED / SOURCE-DEPENDENT`, not `PROVED`.
- **Necessary versus sufficient condition.** Equation (1) is necessary, not sufficient. This causes no logical gap because every nontrivial necessary-condition hit is excluded. The sole hit is replayed physically and is trivial.
- **Known negative cycles only.** The theorem covers repetitions of `P3` and `P11`; it does not cover an undiscovered negative cycle baseline.
- **One pulse only.** Arbitrary fixed multi-pulse supports remain finite by `L-8201`, but this theorem does not bound their repetition length.
- **No divergence statement.** The result concerns finite positive cycles, not the pulse/run-core infinite-orbit chart.
- **No global novelty claim.** No assertion is made that this all-repetition exclusion is absent from all prior Collatz literature until the literature agent completes an independent audit.

## Adversarial tests

`X-8202` performs all of the following with exact rational or integer arithmetic:

1. reconstructs `log(2)` and `log(3)` from independent rational atanh series with certified tails;
2. certifies intervals for both `alpha` values narrower than `2^-574`;
3. certifies all 35 continued-fraction rows through the first denominator beyond each cutoff;
4. proves both Matveev cutoff inequalities and positive derivatives by rational interval arithmetic;
5. verifies the Legendre threshold at the first declared repetition;
6. rejects all sixteen primitive upper convergents and every positive multiple using (13);
7. exhausts the exact small cases;
8. reconstructs the unique trivial reduced hit;
9. compares two implementations that share no imported derivation module.

Frozen output:

```text
certified continued-fraction rows:       35
primitive upper candidates rejected:    16
nontrivial reduced divisor hits:          0
trivial hits:                             1
transcript SHA-256:
3ea78acc77e7d8377c72e2359fa1b190a86eaebdf86b6e7b4afe7fa63c7a10bb
```

## Remaining uncertainty

The mathematical uncertainty is concentrated in the exact source formulation of Matveev's theorem and in independent reconstruction of its substitution. The native algebra and finite reduction have two exact implementations, but that does not replace a human or independent-agent proof review.

## Suggested next attack

The single-pulse repetition axis is now source-conditionally closed. The nearest extension is:

```text
fixed support size e>=2
+ arbitrary repetition r
+ sparse resultants E_i(r)
+ a uniform logarithmic-form / gcd / primitive-divisor argument
 -> all-repetition multi-pulse exclusion.
```

A positive-cycle construction in the negative-cycle neighborhood must evade at least one of:

1. one fixed known negative baseline;
2. coordinatewise upward pulsing;
3. fixed finite support with a uniform repetition theorem;
4. the full-denominator divisibility requirement.

The constructive divergent pulse/run-core chart remains a separate live lane and is not weakened by this theorem.
