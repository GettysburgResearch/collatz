# Uniform rotation-distance floors for nontrivial cycles

**PROPOSED / SOURCE-QUALIFIED.** Every nonidentity shift of the primitive
parity word of a nontrivial positive ordinary shortcut cycle has Hamming
distance at least **12** using the locally replayed convergence range below
4,000,000. Using Barina's reported convergence range below 2^68 instead
raises this floor to **44**. Both conclusions use the logarithmic-form
bound and the distance inequality proved or sourced in the
[main note](README.md). Neither conclusion asserts existence of such a cycle.

## Bounds to replay

Use L,q,m,d,Z,c,gamma as in the main note. Suppose d<=k. Since
7/12 < gamma and c < 317/200, if

    2^j > (12/7) (2+16(j+1)+k) (317/200)^(k+1),

then the distance inequality is impossible for 2^j<=L<2^(j+1).
The left side doubles per unit increase in j and the linear factor at the
right grows by less than a factor of two. Thus L<2^j. This step gives
(L<2^17) for k=10 and (L<2^39) for k=42.

For a cap N on L, bracket alpha=ln(2)/ln(3) by a/b < alpha < c'/d'
with b c'-a d'=1 and b+d'>N. Every rational between the bracket endpoints
in lowest terms has denominator at least b+d' (write its numerator and
denominator as a positive integer linear combination of the endpoint
columns). Since q/L<alpha, this gives q/L<=a/b. The minimum bound is then

    m <= q/[3 (L ln 2 - q ln 3)] <= a/[3 (b ln 2 - a ln 3)].

The second inequality uses monotonicity in q/L. The [checker](floor_check.py)
encloses the two logarithms by 100 terms of the positive atanh series and
a rational geometric tail. It verifies each Farey determinant, denominator
threshold, sign and strict bound by rational comparisons.

| Distance hypothesis | L cap | Lower Farey endpoint | Upper Farey endpoint | Strict bound on m |
|---|---:|---:|---:|---:|
| d<=10 | 131072 | 79335/125743 | 31867/50508 | 2^33 |
| d<=10, refined | 12000 | 6956/11025 | 665/1054 | 4,000,000 |
| d<=42 | 2^39 | 137528045312/217976794617 | 340526703945/539722056247 | 2^76 |
| d<=42, refined | 90,000,000,000 | 6586818670/10439860591 | 65470613321/103768467013 | 2^68 |

To obtain each refined L cap, suppose the cycle minimum is at least the
chosen convergence cutoff. In either case lambda<=L/(3m)<1/2, hence
exp(lambda)<2. Retaining exp(lambda) in the phase-ratio estimate of the main
note gives Z<=log_2(1+2m 3^(d/2)). The first row for each distance
hypothesis now gives Z<=42 or Z<=111 respectively. Substitute these into
(1) of the main note using the displayed rational bounds on c and gamma.
The resulting L bounds are strictly below 12000 and 90,000,000,000.
The corresponding second Farey rows put the minimum below the convergence
cutoff, a contradiction. Distances are even, giving the two stated floors.

## Convergence inputs

For the smaller floor the checker iterates the exact shortcut map for each
2<=n<4,000,000 until the value falls strictly below n. Induction gives
convergence for this entire range. The largest observed time to first
descent was 224 shortcut steps. The full run is independent of both Farey
brackets.

For the stronger floor we use the project report dated 7 May 2020
that every positive integer below 2^68 converges. We inspected the project
page and its link to the corresponding Barina paper. We did not replay that
external computation. The raw and shortcut maps give the same convergence
assertion, since the shortcut odd branch contracts the forced following even
step. [Barina project and dated record](https://pcbarina.fit.vutbr.cz/) ·
[Barina, *Convergence verification of the Collatz problem*](https://doi.org/10.1007/s11227-020-03368-x).
