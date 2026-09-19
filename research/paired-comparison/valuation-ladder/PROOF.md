# Forced entry, valuation bridges, and a ladder of smaller companions

**Status: PROPOSED pending independent mathematical review.**
Publication pass: 2026-09-20 (Asia/Jerusalem). This is the complete mathematical
packet from the preceding chat pass, reconstructed and checked before upload.
It does not prove Collatz and makes no external priority claim.

Use the unabsorbed shortcut map T(n)=n/2 for positive even n, and
T(n)=(3n+1)/2 for positive odd n; in particular 1 -> 2 -> 1.
A word records actual source parities chronologically. Clocks count shortcut
steps, independently on each arm. A merger with a positive original source
m<n excludes n from being the least nonconvergent positive integer. This
argument does not require either displayed arm to descend below n.

## Provenance and relation to live work

The chat pass inspected #122 at `65c91ecea97d9ebf931eb1d9284b7950182a298e`
and #123 at `bf0696f888442c82a4c6cdc1df36becf8550295a`.
The publication pass additionally read #124 at
`1d4dfc103055648def3db73860778a383a91ea3c`, especially
`research/astra-exit-merging/adaptive-companions/PROOF.md`.
Main was `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.

The source packets remain proposed. No rank, transport, density, or external
formalization theorem is a premise of the elementary identities below.
The good first odd exit has prior credit in #122's SOURCES_AND_LIMITS.md to
Sodelin/Collatz-Conjecture-Work, commit
`026aa4ad4be6453a005ab950b160a9f2204c5271`, file
`proof-search/lemmas/L6_Minimal_Counterexample_Exit_Constraint.md`.
It is rederived here, not claimed new. The synchronous restriction for affine
H-pairs is also in #124 (AAC-001); our independent chat observation is not
presented as priority over that packet.

#124 supplies a simpler adaptive companion on the entire OLD 110-entry
domain, generally below 3n/4 rather than n/3. That improvement does not make
the unrestricted first-odd-run entrance below redundant: every hypothetical
least counterexample enters it, without a 110-prefix assumption. The valuation
bridges apply to H-pairs reached by any of these different mechanisms. Old
narrower certificates retain their original stronger source factors.

## VL-001. Every hypothetical least counterexample enters H

Write H(C)=9C+2. A least positive nonconvergent n must have n=3 mod4:
even n descends at once, and n=1 mod4, n>1, has T^2(n)=(3n+1)/4<n.
Thus uniquely n=2^r u-1 with r=v2(n+1)>=2 and positive odd u.
Take m=(n-1)/2=2^(r-1)u-1, a positive source smaller than n.
The initial odd runs give

    T^r(n)=3^r u-1,     T^(r-1)(m)=3^(r-1)u-1.

If 3^r u=1 mod4, the tails 00 on n and 01 on m give the credited merger

    T^(r+2)(n)=T^(r+1)(m)=(3^r u-1)/4.

A least counterexample must therefore have 3^r u=3 mod4. Now the tails
are 01 and 00 respectively. Put C=(3^(r-1)u-1)/4. Then

    T^(r+2)(n)=H(C),       T^(r+1)(m)=C,       C=2 mod3.       (1)

C is a positive ordinary integer; r>=2 proves its last congruence.
This is an entrance theorem, NOT a claim that every ensuing H-comparison
merges. All subsequent stages retain these original sources and clocks.

## VL-002. The Q-pair repeat and its exactly determined exit

Put Q(D)=(3D-1,D). For positive odd D,

    D=1 mod4:  Q(D) --two steps--> Q((3D+1)/4),
    D=3 mod4:  Q(D) --two steps--> (E,3E+2), E=(3D-1)/4.    (2)

The respective word pairs are (01,10) and (00,11).
The first rule has

    (3D+1)/4 - 1 = (3/4)(D-1).                             (3)

Consequently if D-1=2^(2k+1)b with b positive odd, the first rule is used
exactly k times before the second. Every asserted parity follows from this
valuation, with no unprescribed infinite repetition. The completion D=1
would repeat forever, but is not used in either positive-integer bridge.

## VL-003. Two unbounded bridges, strictly including the old entrance

### A: even comparison parameters

Assume v2(3C-2)=2k+3, k>=0. Put

    b=(3C-2)/2^(2k+3),     D=(3^(k+1)b+1)/2.

Then

    (T^(2k+4)(H(C)),T^(2k+4)(C))=(D,3D+2).                (4)

Proof: C=2 mod4, and the first two steps (00,01) reach
Q((3C+2)/4). Its parameter minus 1 is 2^(2k+1)b. Apply (2)-(3).
The full bridge words are

    H arm: 00(01)^k00;       C arm: 01(10)^k11.

The first entrance cylinders are C=14 mod16, C=54 mod64,
C=214 mod256, and so on. The k=0 case is the old entrance; higher k add
new classes.

### B: odd comparison parameters

Assume v2(3C-1)=2k+4, k>=0. Put

    b=(3C-1)/2^(2k+4),     D=(3^(k+2)b+1)/2.

Then

    (T^(2k+5)(H(C)),T^(2k+5)(C))=(D,3D+2).                (5)

Proof: C=3 mod8. The initial words (100,110) reach Q((9C+5)/8).
Its parameter minus 1 is 3*2^(2k+1)b; use (2)-(3) again.
The words are

    H arm: 100(01)^k00;      C arm: 110(10)^k11.

The first cylinders are C=27 mod32, C=107 mod128, C=427 mod512, etc.
These are disjoint from the old even entrance and from bridge A.
All b,D in (4)-(5) are positive integers by the specified valuations.

## VL-004. A total exit after either bridge, and finite composition

At the endpoint (D,3D+2) of either bridge, write

    D+1=2^s q,   s=v2(D+1)>=0, q positive odd, z=3^s q.

For s steps both arms are odd and maintain the affine relation y=3x+2.
The pair becomes (z-1,3z-1). Two further physical steps give

    z=3 mod4: (E,E),            E=(3z-1)/4;
    z=1 mod4: (C',H(C')),       C'=(z-1)/4.                (6)

The final word pairs are (1^s01,1^s00) and (1^s00,1^s01), respectively.
In the return case z>=5, so C'>0. In the merge case E>0. The s=0 case
is included; no positive valuation is assumed when D is even.

A return exchanges the arms. Concatenation must exchange the corresponding
word labels at the next stage, while retaining the two ORIGINAL roots.
After any finite list of returns ending in a merge, (1) gives an actual
smaller-original-source merger. The two original clocks differ by one;
equal increments during comparisons do not reset or erase that difference.
An outside-language value or a budget limit is NOT a merger certificate.

For the old k=0 cylinder, write C=2^(r+1)b0-2, r=v2(C+2)-1>=3.
The bridge gives D=(9C+2)/16=9*2^(r-3)b0-1. Thus s=r-3 and
z=3^(r-1)b0. Substitution into (6) gives precisely #123's rule:

    length r+3;
    3^r b0=1 mod4: merge at (3^r b0-1)/4;
    3^r b0=3 mod4: return to (D0,H(D0)), D0=(3^(r-1)b0-1)/4.

So the old transition is algebraically included, with its actual clocks and
orientation, not merely its successful set. The executable replay additionally
checks equality of every old admitted transition through C=65536.

## VL-005. Exact measure of these certificate languages

Here measure means normalized Haar measure on the 2-adic parameter space,
not a probability assigned to a particular counterexample, a convergence
census, or an established natural density of the infinite union on integers.
Only finite ordinary realizations of the cylinders supply certificates.

Bridge A has disjoint cylinders of measures 2^(-(2k+4)), summing to 1/12;
bridge B has measures 2^(-(2k+5)), summing to 1/24. They are disjoint, so the
entrance measure is 1/8, twice the old 1/16.

On each such cylinder, write its odd b as b=b0+6t (the factor 3 enforces
ordinary C integrality, irrelevant to 2-adic measure). The endpoint D has
odd slope as an affine function of t. Thus D is uniform 2-adically.
For every s, the odd part q=(D+1)/2^s is uniform among odd residues; exactly
half of its classes give either branch of (6). Fixing s and the mod4 choice,
C' in the return branch is again an affine function of the unused integer
parameter with odd slope. It follows that the return branch transports
normalized Haar measure to normalized Haar measure. This is exact cylinder
arithmetic, not an independence assumption for ordinary trajectories.

The total merge branch measure is 1/16 and the total return branch measure
is 1/16. A finite success after j returns consequently has measure
(1/16)^(j+1). These sets are disjoint, giving

    measure(finite successful new language)=1/15.

For the old entrance the two branch measures are 1/32 each, giving 1/31.
The all-return set has Haar measure zero for this language. It is NOT proved
to contain no positive ordinary integer, and most parameters leave the
language at a finite stage. Neither assertion supplies universal success.

## VL-006. A new whole cylinder and arbitrarily long first odd runs

For every integer t>=0,

    T^7(9(128t+59)+2)=T^7(128t+59)=81t+38.                (7)

The two words are 1000001 and 1101100. This can be obtained from bridge B
or by composing its affine maps. Each parity holds uniformly on the entire
progression, not merely on finitely tested t.

Let r>=2 and positive odd u satisfy

    3^(r-1)u=512t+237, t>=0,     n=2^r u-1.               (8)

Then 3^r u=3 mod4 and C=128t+59 in (1). Hence

    T^(r+9)(n)=T^(r+8)((n-1)/2)=81t+38.                  (9)

For every fixed r, odd multiplication by 3^(r-1) is invertible modulo 512,
so there are infinitely many positive u satisfying (8). The run length r
is unbounded and is read from the source, not selected after changing it.

### No forward descent on the entire displayed arm for r>=9

The original odd run strictly increases. On the seven-step H tail in (7),
the minimum is 54t+25=(3^(r+2)u+1)/256. For r>=9,
3^(r+2)>2^(r+8), so that minimum exceeds n=2^r u-1. The two intervening
post-odd-run values are larger than this minimum. Thus every positive-time
state through time r+9 is above n.

Example: n=236031, m=118015,

    T^18(n)=T^17(m)=478505,
    min_{1<=j<=18} T^j(n)=319003>n.

If 3|n, all positive depth-b pure ancestors are 2^b n: an odd inverse of a
multiple of 3 would require (2n-1)/3 integral, and doubling preserves
3-divisibility. In particular there is no smaller pure ancestor at any depth.
CRT combines (8) with 2^r u=1 mod3, producing infinitely many such n for
every r>=9. The example above is divisible by 3. No-forward-descent and
no-smaller-pure-ancestor are compatible with the displayed two-sided merger.

## VL-007. The original-source companion ladder

For any hard odd exit as in (1), and each

    0<=j<=floor((r-2)/2),

put

    d_j=(4^(j+1)-1)/3,         m_j=(n-d_j)/2,
    C_j=(3^(r-2j-1)u-1)/4.                              (10)

Then m_j is a positive integer below n and

    T^(r+1)(m_j)=C_j,          T^(r+2)(n)=H^(j+1)(C_j).  (11)

The companion word is

    1 0^(2j) 1^(r-2j-2) 00.

Proof: the first step from m_j equals
4^j(3*2^(r-2j-2)u-1). The next 2j even steps remove that factor, the
following r-2j-2 odd steps reach 3^(r-2j-1)u-1, and the last two even steps
give C_j. The hard congruence guarantees divisibility by four, including
r-2j-2=0. The bound 4^(j+1)<=2^r shows d_j<n and m_j>0.
Finally H^l(C)=9^l C+(9^l-1)/4 proves the upper equality in (11).

The offsets are 1,5,21,85,341,... . Every rung is a smaller ORIGINAL source,
not a newly compared intermediate state. Under least-counterexample
minimality every rung converges. A merger with any rung is sufficient.
The length of the ladder is finite for a fixed source; no unprovided rung
beyond its stated j range may be assumed.

## VL-008. A two-rung bypass that survives a blocked first companion

For all t>=0,

    T^12(81C+20)=T^12(C)=243t+155,
    C=4096t+2604.                                        (12)

The upper word is 0^11 1; the lower word is 001101001100.
Since H^2(C)=81C+20, this compares nonadjacent rungs. For r>=4 and

    3^(r-3)u=16384t+10417, t>=0,   n=2^r u-1,             (13)

use j=1 in (11) to obtain

    T^(r+14)(n)=T^(r+13)((n-5)/2).                       (14)

When 3|n, x=n/3-2 is positive odd and T(x)=(n-5)/2, so

    T^(r+14)(n)=T^(r+14)(n/3-2), 0<n/3-2<n/3.           (15)

The congruence in (13) gives infinitely many odd u for every r>=4.
CRT can also impose 3|n, independently of the power-of-two congruence.

For n=230319, m0=(n-1)/2=115159 has first arrival at 1 at time 55;
n first arrives at 1 at time 53. Thus T^t(n)=T^(t-1)(m0) is impossible
for EVERY t>=1. A putative earlier equality would propagate into the
incompatible eventual phases of 1<->2. This is a verified phase obstruction
for these fixed sources and clocks, not a convergence obstruction.
But the next rung m1=115157 succeeds:

    T^18(230319)=T^17(115157)=T^18(76771)=641.

### No forward descent for every r>=20 in (13)

The smallest state on the upper twelve-step word of (12) is
162t+103=(3^(r+1)u-1)/8192. For r>=20,
3^(r+1)>2^(r+13), making this strictly larger than n. The preceding initial
odd run and its two exit states are also above n. Thus all positive-time
states through r+14 exceed n.

Example: n=20530069503, x=6843356499,

    T^34(n)=T^34(x)=37500596075,
    min_{1<=j<=34} T^j(n)=25000397383>n.

This n is divisible by three and has no smaller pure ancestor at any depth.

## VL-009. Clock rigidity and the first variable-power escape

If fixed words with odd counts p,q and lengths A,B merge H(C) and C on an
infinite arithmetic progression, equality of slopes gives

    9*3^p/2^A = 3^q/2^B.

Unique factorization forces A=B and q=p+2. Changing the clock offset alone
cannot supply a fixed-word identity for these same affine sources. This
necessary condition does not forbid individual unequal-clock meetings,
changing words, or other companions. See also #124 AAC-001.

A class outside both new bridges is C=0 mod4. Write C=4^s d with s>=1
and 4 not dividing d. Direct iteration gives

    (T^(2s)(9C+2),T^(2s)(C))=(3^(s+2)d+2,d).             (16)

At each pair of steps, (A*4x+2,4x) uses words (01,00) and becomes
(3A*x+2,x). Iterating from A=9 proves (16).
The variable-power type (3^a d+2,d), and skipped-rung types (H^j(C),C),
are the next targets. Entering them does not itself establish a merger.

## Evidence, reproducibility, and what remains open

Run from the repository root:

```sh
python -B experiments/paired-comparison/valuation-ladder/run.py --full /tmp/vl.jsonl --check experiments/paired-comparison/valuation-ladder/canonical.json
python -B experiments/paired-comparison/valuation-ladder/verify.py /tmp/vl.jsonl --summary experiments/paired-comparison/valuation-ladder/canonical.json --self-test
```

Use any writable path instead of /tmp on Windows. Both programs are
standard-library-only. The verifier imports no generator/repository module;
it discovers the bridge by actual Q-pair iteration rather than substituting
the generator's valuation formulas. It rejects typed/word/clock/endpoint
corruptions. One author's two implementations are not independent peer review.

The new durable corpus reproduces the chat's complete C=1..65536 comparison:
old admission 4096, old mergers 2114; new admission 8191, new mergers 4366.
All old transitions are preserved exactly. No stage-budget exhaustion occurs;
61170 new-language inputs are explicitly retained as OUTSIDE.
The fresh additional grids check 6400 first exits, 5280 companion-ladder
instances, and 992 bridge instances with k=0..30. Both whole seed cylinders
are verified symbolically. The earlier chat reported a different private
6400-ladder sample; its runtime files were not present in this publication
session, so that historical execution count is not represented as reproduced.
The full deterministic rows are regenerated rather than committed in bulk.

No complete-checkout root validator, external Lean build, remote CI, or
independent mathematical acceptance is claimed. The precise further gap is
all-source successful coverage: finite exits from this language and potential
infinite return itineraries remain uncontrolled. The stronger entrances,
explicit families, and multiple companions above do not resolve that gap.
