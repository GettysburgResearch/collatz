# Earlier witness transfers through J

**Main 512-residue implication: OPEN.** This note broadens three already proved
conditional reductions. It does not claim a complete recursive cover or
unconditional convergence on the larger classes.

For positive odd n, write

    C(n) = (3n+1)/2^v2(3n+1),       J(n) = 4n+1.

Use the bridge notation

    P(m): E(27m)    implies E(54m+1),
    Q(m): E(54m+1) implies E(9m),

for positive odd m. Also put X(m)=128m+1, Y(m)=64m+1, and let CLOSURE(m)
denote E(X(m)) implies E(Y(m)).

The witness definition of E, its equivalence to exact odd trajectories, and
the finite prefix concatenation rule are established in [the proof
packet](README.md). The four CA-003 seed certificates are reproduced in full
in [the preceding continuation note](continuation-algebra.md). The earlier
fixed-prefix certificates remain valid; the present argument transfers
witnesses one step before a formerly fixed final valuation is needed.

| Local claim | Status | Exact scope |
|---|---|---|
| W512-080 | PROVED-IN-NOTE | Q(m), m=95 mod256, reduces to P(p) or Q(p), with 0<p<m. |
| W512-081 | PROVED-IN-NOTE | P(m), m=1215 mod16384, reduces to P(p) or Q(p), with 0<p<m. |
| W512-082 | PROVED-IN-NOTE | For m>3 and m=3 mod2^119, CLOSURE(m) is equivalent to CLOSURE((m+4011)/2), with a smaller parameter. |

These statuses concern the conditional reductions themselves. They do not
assert that every smaller bridge needed by a reduction has been proved.

## 1. Why J permits an earlier transfer

For positive odd n,

    3J(n)+1 = 4(3n+1).

Thus C(J(n))=C(n), with exact first exponent increments differing by two.
From a witness for n, adding two to its first increment gives a witness for
J(n). Conversely, subtracting two from the first increment of a witness for
J(n) gives one for n. The number of odd steps is unchanged. When n=1, a
zero-length witness can first be padded with the exact exponent-two loop.

Every J preimage used below is a positive odd integer greater than1, so the
nonempty-witness case always applies. No arbitrary choice of the next exact
valuation is made. The identity works for every possible value of
v2(3n+1).

## 2. Shared normalization of (54h+1,36h+1)

Let h be a positive integer and write

    h = 2^b u,       u odd,       s=floor(b/2),       p=3^s u.

Then p is positive and odd, and p<=h. Suppose a witness for 54h+1 is known
and a witness for 36h+1 is sought.

If b=2s, after s exact exponent-two steps the pair is

    (54p+1,36p+1) = (54p+1,J(9p)).

A Q(p) call therefore supplies a witness for 9p; a J transfer and reversal
of the target prefix reconstruct the desired target.

If b=2s+1, after s exact exponent-two steps the source is J(27p). The target
is then 72p+1 and takes one further exact exponent-two step to 54p+1.
Removing J from the source produces a P(p) call. Its output reconstructs
the target by reversing those s+1 steps.

Every quarter step is exact: its displayed quotient has an even coefficient
of the positive odd parameter and constant term1. The same normalization
was already used in Q19. The implementation now exposes it once as
`normalize_q_pair`, and reuses it for all three relevant adapters.

For a source witness with length R and final cumulative exponent A, and a
returned recursive target witness with data (L,B), the normalization has
the following bookkeeping:

| Parity | Recursive bridge | Recursive source data | Reconstructed target data |
|---|---|---|---|
| b=2s | Q(p) | (R-s, A-2s) | (L+s, B+2s+2) |
| b=2s+1 | P(p) | (R-s, A-2s-2) | (L+s+1, B+2s+2) |

The source endpoint after its quarter steps is greater than1. Therefore an
alleged source witness ending at or before that prefix is invalid; the
adapter rejects it rather than padding an incomplete prefix.

## 3. W512-080: Q95 extends to modulus256

Let

    m=256t+95,       h=(27m-5)/256=27t+10,       t>=0.

The source 54m+1 follows the exact exponent word (1,2,3) to

    5832t+2165 = 216h+5 = J(54h+1).

The target 9m follows the exact word (1,1,4) to

    972t+361 = 36h+1 = J(9h).

Every intermediate state is a positive odd integer. These are affine
identities on all t>=0, not a claim inferred from sample trajectories.

Remove J from the known source endpoint and apply the shared normalization
of (54h+1,36h+1). Its parameter satisfies

    0<p<=h<m.

Positivity follows from h>=10, and h<m follows directly from
(27m-5)/256<m. Thus this is a valid descending conditional call.

Write epsilon=b mod2, where b=v2(h). If the original source witness has
data (R,A), the recursive source has data

    (R-3-s, A-8-2s-2epsilon).

If the recursive target has data (L,B), the reconstructed witness for 9m
has data

    (L+3+s+epsilon, B+8+2s).

For epsilon=0 the recursive bridge is Q(p); for epsilon=1 it is P(p).

The original m=95 mod512 class is the even-t subset. On that subset, the
new h is twice the old normalization parameter. The old J-pair
normalization and the present shared normalization give exactly the same
recursive source witness and final reconstructed target witness. Both
certificates remain checked independently.

As one finite illustration of the newly added half, m=23391 gives h=p=2467
and the smaller call Q(2467). The latter parameter is35 mod128, so the
existing fixed merger certificate completes this particular call. This
example is not used to justify the universal affine identities.

## 4. W512-081: P1215 extends to modulus16384

Let

    m=16384t+1215,       h=(243m-333)/16384=243t+18,       t>=0.

The source 27m follows the exact exponent word (4,1,1,2,3) to

    52488t+3893 = 216h+5 = J(54h+1).

The target 54m+1 follows the exact word (1,2,8,2) to

    8748t+649 = 36h+1 = J(9h).

Again, every intermediate affine state is a positive odd integer for all
t>=0. Removing the source J gives exactly the same shared normalization.
Its parameter satisfies 0<p<=h<m, with h>=18 and
(243m-333)/16384<m.

With epsilon=b mod2 and the same notation for source and recursive target
data, the recursive source has

    (R-5-s, A-13-2s-2epsilon),

and the reconstructed target has

    (L+4+s+epsilon, B+15+2s).

The original m=1215 mod32768 class is the even-t subset. Its old certificate
and normalization are retained independently and produce the same witnesses.

A finite illustration from the added half is m=1754303. It gives h=p=26019,
which is35 mod128, so Q(26019) is completed by the existing fixed merger
certificate.

## 5. W512-082: CA-003 extends from K>=121 to K>=119

Use the four finite seed witnesses from the preceding continuation note.
Their relevant prefixes are:

| Role | Seed | Prefix length | Prefix exponent sum | Seed endpoint |
|---|---:|---:|---:|---:|
| Original source | 385, padded at1 | 33 | 71 | 1 |
| New source | 256897 | 33 | 68 | 5 |
| Original target | 193, padded at1 | 67 | 124 | 1 |
| New target | 128449 | 67 | 121 | 5 |

Only the two original seed witnesses are padded; this is exact terminal
padding at1. No supplied lifted witness is artificially padded in this
construction.

For K>=119 and positive integer u, put

    m=3+2^K u,
    m'=2007+2^(K-1)u=(m+4011)/2.

The lifted source prefixes have states

    S  = 1 + 3^33 2^(K-64)u,
    S' = 5 + 3^33 2^(K-62)u = J(S).

The lifted target prefixes have states

    T  = 1 + 3^67 2^(K-118)u,
    T' = 5 + 3^67 2^(K-116)u = J(T).

All prefixes remain exact. For each seed prefix, the perturbation term at
every intermediate state is even, since the final exponent sum is the
largest prefix exponent sum. The strongest condition is K-118>=1 in T,
which is precisely K>=119. Every displayed lifted state is positive, odd,
and greater than1.

The source transfer is now:

1. Remove the forced33-step prefix of the supplied X(m) witness, obtaining
   a witness for S.
2. Apply J to obtain a witness for S'.
3. Prepend the33-step 256897 seed prefix, obtaining a witness for X(m').

The length is unchanged, and its final exponent changes by

    -71 + 2 + 68 = -1.

Given a witness for Y(m'), reconstruct Y(m) by:

1. Removing its forced67-step prefix, obtaining a witness for T'.
2. Removing J to obtain a witness for T.
3. Prepending the padded67-step 193 prefix.

Again the length is unchanged, and the final exponent changes by

    -121 - 2 + 124 = +1.

These operations are valid for arbitrary supplied witnesses of the stated
starts. A valid X(m) witness must have length greater than33, and a valid
Y(m') witness must have length greater than67, because the forced endpoints
exceed1. Alleged shorter inputs are rejected. A missing recursive target
never counts as a successful reconstruction.

Both J transfers are reversible. Therefore

    CLOSURE(m) if and only if CLOSURE(m').

Moreover, m>=3+2^119>4011 gives 0<m'<m. Both parameters are positive odd
integers congruent to3 mod4. Choosing K=119 and
u=(m-3)/2^119 covers the full advertised class; u need not be odd.

The original K>=121 fixed-word certificate remains an independent subset
check. Its34-step source and68-step target mergers agree exactly with the
present J transfers wherever both apply. At K=118 with u odd, the proposed
state T would be even, so this argument does not justify lowering the
threshold further.

## 6. Verification and evidence limits

The production adapters in `verify.py` now use Q95 modulo256, P1215
modulo16384, and CA-003 at precision119. The former fixed-prefix identities
remain separate checks. Q19 and the broadened Q95/P1215 rules share one
normalization implementation rather than separate copies of the parity
argument.

The replay uses exact integer arithmetic and Fraction polynomials. It
checks all intermediate affine states, not only final identities. Bounded
trajectory searches occur only while constructing finite test fixtures;
the production transformation algorithm does not search for missing target
witnesses. Unsupported recursive leaves and resource limits return
UNRESOLVED.

Both commands complete successfully with identical reports:

```sh
python3 research/witness-closure-512-2026-11-20/verify.py
python3 -O research/witness-closure-512-2026-11-20/verify.py
```

The main replay reports41 transformed fixture witnesses,5 Q19
reconstructions,13 broadened Q95/P1215 reconstructions,4 CA-003
reconstructions, and4 negative-template reconstructions. It separately
checks9 original Q95/P1215 subset reconstructions and2 original CA-003
subset reconstructions. It rejects11 malformed witnesses,25 invalid
certificates or reconstructions, and16 truncated forced-prefix witnesses.
These are precisely scoped test counts, not an exhaustive coverage bound.

Using those same fixtures without further trajectory searches, the replay
also checks five nonminimal supplied source witnesses and five nonminimal
supplied recursive target witnesses. Adding terminal loops must preserve
the exact corresponding padding after reconstruction. The CA-003 and
negative-template equivalences additionally pass two source and two target
round trips, reproducing the original cumulative-exponent tuples exactly.

The second negative-template family checked by the separate
`verify_negative.py` is not automatically dispatched by the main
`verify.py` transformer. This note does not add that dispatch or claim a
global cover from either verifier.

The three new domains are respectively twice, twice, and four times the
sizes of their former individual congruence classes. Their possible overlap
with other proved rules is not counted here. The full assertion remains
open until every required recursive call can be discharged by a complete
well-founded family of rules or terminal certificates.
