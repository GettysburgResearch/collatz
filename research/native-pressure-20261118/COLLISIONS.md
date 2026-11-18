# A quadratic finite-depth bound on the ternary collision density

**PROPOSED.** With μ_n as in the [native transfer proof](README.md), for
every n≥1,

    3^n ∑_(r mod 3^n) μ_n(r)² ≤ 16(n+1)².                         (1)

This auxiliary result concerns a finite marginal of the Syracuse random
law. It is distinct from the D_q of PR 144 and from a claim about the
infinite distribution having a square-integrable density. The proof of
ordinary descent in the main note uses the direct ordinary bound there.

For a positive exponent word let A=∑a_i and let F be its exact nonnegative
real offset F_(a_n)∘⋯∘F_(a_1)(0), where F_a(z)=(3z+1)/2^a.
Then u=2^A F is a positive odd integer. At fixed A, distinct words give
distinct u: its expansion as ∑_(i=1)^n 3^(n−i)2^(a₁+⋯+a_(i−1))
recovers each partial sum by subtracting the previous terms and taking
the 2-adic valuation. The final exponent follows from A. The statement
also holds at n=1. This is the elementary offset injectivity used in
Tao's Lemma 6.2.

Let P_a(r) be the mass of words with total A=a and residue F≡r modulo
3^n. Each word in this group has probability 2^(−a). If a single residue
contains m such words, their m distinct integers u are in one arithmetic
progression modulo 3^n, so their sum is at least 3^n m(m−1)/2. After
summing residues this proves

    3^n ∑_r P_a(r)² ≤ (3^n/2^a) P(A=a) + 2 E[F·1_{A=a}].           (2)

The iid geometric law gives E[2^(−a_i)]=1/3, hence E[3^n/2^A]=1.
The recursion for the offset yields E[F]=n/3. Sum (2) over a≤8n.
Cauchy across at most 8n+1 classes bounds the square root of the
normalized collision moment of their mixture by
√((8n+1)(1+2n/3)). For the remaining mass, E[(3/2)^a_i]=3 gives
P(A>8n)≤[3(2/3)^8]^n. Its normalized ℓ² norm is at most 3^(n/2)
times this probability, which is below 1. The triangle inequality and
√((8n+1)(1+2n/3))+1≤4(n+1) prove (1).

It follows immediately that μ_n(B)≤4(n+1)√(|B|/3^n) for every subset.
In particular, the collision entropy divided by n log 3 tends to one.
The earlier fine-scale mixing theorem of Tao concerns total variation
from uniform finer digits after fixing a coarse scale. The collision
entropy assertion here follows from the distinct real offsets and does
not use that external mixing theorem.

[Tao, *Almost all orbits of the Collatz map attain almost bounded values*, §6, Lemma 6.2](https://arxiv.org/html/1909.03562v7#S6).

## Finite checks

The arithmetic producer measures all 131,071 ordinary sources less than
2^17 across shells k=0,…,16. It checks the exact offset mean and native
fiber energy. The ordinary energy at each k is stored with denominator 4^k.
It also encloses the ternary second moments at n=0,…,11 using 120-bit
outward intervals and a geometric tail.

The second implementation computes ternary moments at 168-bit precision
by a full-cycle resolvent instead of geometric truncation. For ordinary
sources it recomputes the collision multiplicities by endpoint alone and
recovers p from the ternary magnitude. A separate integer identity compares
the actual pushforward, truncated to k≤16 and p≤5, against the explicit
valuation-vector law summed over all permitted initial zero runs. These
are author-side implementations and finite checks of the written statements.

```sh
python -B experiments/native-pressure-20261118/verify.py > /tmp/native-collisions.json
python -B experiments/native-pressure-20261118/crosscheck.py /tmp/native-collisions.json
```

[Exact finite intervals and collision numerators](../../reports/native-pressure-20261118/collisions.json).

El Jaouhari previously proved the sharp L^p range and quantitative
quadratic energy bounds for the ternary laws, with alternative moment
arguments and upper-tail asymptotics developed subsequently.

[El Jaouhari, October 2026](https://doi.org/10.5281/zenodo.23377671).
[Ternary Syracuse laws, Theorems on moment growth](https://rstation.ai/problems/collatz/papers/9/v1).
