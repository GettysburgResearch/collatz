# A cylinder criterion for the exact Bergman radius

**Proposed theorem O13.** Let independent positive integers D_i have probabilities p(1−p)^(d−1) at d≥1. Compose the 3-adic affine contractions G_d(b)=(3b+1)/2^d. The first h outer maps determine one residue modulo 3^h independently of the remaining tail and hence define consistent cylinder probabilities mu_(p,h)(a). Define
```
delta(p) = lim_{h→∞} -log(max_a mu_(p,h)(a)) / (h log 3).
```
This limit exists. For the classical Bergman transfer and the biased law p=1/10, its radius R equals sqrt(20)/3 precisely when delta(1/10)=1. The O9 certificate implies delta(1/10)>0.9999936. The criterion isolates an all-depth maximum-cylinder obligation. Tao's 3-adic Syracuse law uses p=1/2, and its published fine-scale mixing statement is formulated in a different norm.

## Induction on odd letters

Work on continuous functions on Z_3 with the supremum norm. Put Uf(x)=f(2x) and Jf(x)=1_(x=2 mod3) f((2x−1)/3). The O9 operator is L=2U+(2/3)J and its spectral radius is R squared. For t>2 put z=2/t. The norm-convergent resolvent series defines the positive operator
```
K_t=(tI−2U)^(-1)(2/3)J,
K_t f(x)=(1/3) sum_{d≥1} z^d 1_(2^d x=1 mod3) f((2^d x−1)/3).
```
Each term follows d−1 even inverses with an odd inverse. If p=1−z and B_p denotes the transfer of G_D on densities relative to additive Haar, the image under G_d is the residue 2^d x=1 mod3 and the Jacobian density there is 3. Hence
```
K_t = [2/(9(t−2))] B_p.
```
After h contractions the image of Z_3 is one full h-cylinder, and Haar pushes to the uniform probability on that cylinder. Consequently B_p^h 1(a)=3^h mu_(p,h)(a), exactly. By positivity, the supremum of this function equals the operator norm. Submultiplicativity gives existence of the displayed limit for delta and r(B_p)=3^(1−delta(p)). These cylinder laws are the projections of the unique stationary law: the random composition contracts by 3^(-h) in the ternary metric, independently of its letters.

## The threshold test

For every t>2,
```
r(L)<t     iff r(K_t)<1,
r(L)≤t     iff r(K_t)≤1.
```
For the strict forward implication take v=(tI−L)^(-1)1, a strictly positive continuous function by the Neumann series. It satisfies (I−K_t)v=(tI−2U)^(-1)1=1/(t−2). Both its positive minimum and finite maximum bound the powers of K_t by a constant times a geometric factor strictly less than one. Conversely if r(K_t)<1, take v=(I−K_t)^(-1)1≥1. Then (tI−L)v=(tI−2U)1=t−2>0. The same comparison gives r(L)<t.

For completeness, r(K_t) is continuous for t>2. Write K(z) for the displayed positive series with parameter z. The supremum norm of K(z)^h is its maximum on the constant one. At each x it is a nonnegative series of monomials in z, with coefficients given by legal h-letter words. Hölder's inequality makes its logarithm convex in log z, and taking a supremum preserves convexity. Therefore h^(-1) log norm K(z)^h is convex in log z. Its pointwise limit log r(K(z)) is finite on 0<z<1. The upper bound is norm K(z)≤z/[3(1−z)]; the lower bound is r(K(z))≥z/3 since x=−1 admits the all-d=1 word of every length. A finite convex function on an open interval is continuous. Finally K_s≤(t/s)K_t for s>t by its positive series, since every d≥1. These observations and the strict threshold test establish both directions at equality.

At t=20/9 the scalar 2/[9(t−2)] is one and p=1/10. By O9 the radius squared is at least t, and max cylinder mass is at least 3^(-h). Applying the test proves the equivalence. Equivalently the stationary law has a uniform Frostman bound mu(B)≤C_s(radius B)^s for every s<1. Such dimension control permits subexponential growth of the density maxima and need not give a bounded density. The same reasoning gives an implicit identity for arbitrary R:
```
R²−2=(2/9)3^(1−delta(1−2/R²)).
```
At t=r(L)>2 equality r(K_t)=1 follows from continuity and the strict threshold test on both sides.

## Effective Frostman exponent at the specified bias

Let v be the O9 integer table, indexed from residue 0, with Lv≤beta v, beta=5516102802/2482245023. Among ternary units its minimum m is 71736705115 and maximum M is 99999999999. For t=20/9,
```
K_t v ≤ v+(beta−t)(tI−2U)^(-1)v.
```
On the units the last resolvent is at most M/(t−2) and v≥m. At a nonunit K_t v is zero. Thus everywhere K_t v≤(1+e)v, where
```
e=(beta−20/9)M/[m(20/9−2)]=1237899999987621/178068079238127392645.
```
The table is strictly positive even on nonunits. Therefore r(B_(1/10))≤1+e and delta(1/10)≥1−log(1+e)/log 3. In particular this exceeds 0.9999936: log(1+e)≤e, log 3>1.09, and e/(1.09)<0.0000064. For example log 3>1.09 follows by retaining four terms in the positive power series 2 atanh(1/2). The checker reproduces the arithmetic comparison and the table hash. This all-depth estimate does not imply delta(1/10)=1.

Related tilted-law work concerns Shannon entropy dimension and absolute continuity. The required delta is a worst-cylinder exponent. In particular full Shannon entropy dimension does not supply the assertion above; a small exceptional cylinder may still carry exponentially more than the uniform mass. See D. Leen, *Tilted 3-adic Syracuse laws: absolute continuity, dimension and the limits of L²*, <https://doi.org/10.5281/zenodo.23268832>, as identified in the discussion of the tilted family and its Shannon-dimension formula in <https://rstation.ai/problems/collatz/papers/135/v1>, Section 1. Neither manuscript is an input to O13.

Sources: V. Béhani, <https://arxiv.org/pdf/2303.03203>, Question 4.1 and Proposition 4.2. T. Tao, *Almost all orbits of the Collatz map attain almost bounded values*, <https://doi.org/10.1017/fmp.2022.8>, Lemma 1.12 and Propositions 1.14 and 1.17 (comparison with the unbiased shortcut process).
