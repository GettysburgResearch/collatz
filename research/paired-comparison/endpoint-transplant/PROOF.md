# Endpoint transplantation, thick predecessor basins, and root-capped block inverses

**EPT-001--005: PROPOSED pending independent mathematical review.**
Date: 2026-09-21. No complete Collatz proof or external priority claim.
This is an additive continuation of #131, not a correction of its proved-scope
warnings. The new universal assertion keeps the ORIGINAL component fixed;
it does not claim to make a prescribed input satisfy a freely chosen gate.
The remaining source-height obstruction is stated explicitly below.

Use the unabsorbed shortcut map T(n)=n/2 for even n, (3n+1)/2 for odd n,
on positive ordinary integers. Thus 1 <-> 2. Words list source parities in
chronological order. Every original arm retains its own clock.

## Provenance and precise dependencies

The preceding chat was already published in #129 at
`9d362511343c97790d42808c363b090a3342b45f`,
`research/paired-comparison/anchored-returns/PROOF.md`. Its AR-001--006 proof
was read back; no duplicate publication or main merge is needed.
This child is based on #131 `e092da549c8c50e8a9430f88fb721ea51fe34d91`,
`research/paired-comparison/delayed-shadow-compiler/PROOF.md`.
DS-004 provides nearby uniform subcells, while DS-005 explains why a fixed
ordinary center can permanently lie outside that language even when it merges.
Neither statement is promoted to a pointwise selector here.

Parallel #132 was read at `7687eec1ac364009d644cb8d015f1fe3b28730cc`,
`research/astra-exit-merging/affine-completeness/PROOF.md`, ACS-001--004.
Its controlled all-intercept chart compiler and simultaneous affine-family
construction are CREDITED, not claimed new here. Parallel #130 at
`53cf9b53bd568b1ab67601b00e789b464198e42b` advertises the same general
classification; its live PR description was read, not its full proof or code.
The older all-gap and original-source interfaces remain credited to
#124--128 and their exact source pins in the parent proofs.
The finite-offset primitive needed below is restated with a proof, so the
logical route does not depend on treating an unreviewed label as acceptance.

Main was read at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
AGENTS, README, the research map and integrated scoped errata were read.
No mass/transport estimate, coefficient stopping hypothesis, density result,
or assertion about convergence of an arbitrary orbit is a premise.

For external context, K. M. Monks, *The Sufficiency of Arithmetic Progressions
for the 3x+1 Conjecture* (Proc. AMS 134, 2006), Theorem 1.1, already proves
that every nonconstant arithmetic progression meets every merger component.
Author copy: https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf .
This context must not be presented as a new AP-sufficiency result. The present
construction assembles simultaneous finite patterns in a fixed inverse basin
and adds an explicit endpoint/source-height formula. The external search
was not a comprehensive priority audit. Monks's theorem is not used as a
premise of the proofs below.

## Credited finite-offset synchronizer, restated

For every finite set F of at least two distinct nonnegative integer offsets,
there are effectively computable B,L,Q,e, words w_d (d in F) of common length
L, and a positive-tail threshold t0, such that M=2^L, A=3^Q, Q>=1, 3 does
not divide e, and

    T^L(B+Mt+d)=At+e, all d in F and all integers t>=t0.       (1)

Here 0<=B<M. Our nonnegative-offset compiler has e>0.
This is the equal-slope special case of ACS-002/003, not a new claim of
finite-family synchronizability.

For completeness, every current family is an affine function of ONE common
remaining parameter with slope a power of three. To join two families, order
their slopes and write their comparison as (3^a y+b,y). With a>0:

* b nonzero even: impose y even, apply 0/0; b becomes b/2.
* b odd: impose y odd, apply 0/1; a becomes a-1 and
  b becomes (b-3^(a-1))/2, using the old a in this expression.
* b=0: impose y odd, apply 1/1; b becomes (1-3^a)/2, nonzero.

Thus finitely many halvings and at most one zero-intercept preparation
reduce a, and eventually reach a constant signed gap. For the positive gap g,
order the coordinates by value. For even g impose lower even, obtaining g/2.
For g=1 mod4, g>1, impose lower=1 mod4 and use words 10/01 to obtain
(3g+1)/4. For g=3 mod4 impose lower=2 mod4 and use 01/10 to obtain
(3g-1)/4. Each new gap is smaller. Gap one closes on lower=4 mod8 by 001/100.

Every imposed residue lifts consistently to the original parameter: the
current coefficient is odd, hence invertible modulo the required power of
two. Refine the SAME parameter for all families and advance all arms by the
same number of steps. Previously merged families stay merged. Induction on
the finite number of offsets proves (1). Choose a sufficiently positive tail
so all original sources are positive. This uses controlled parameter digits,
not a choice of parity for an already fixed source.

All slopes in the final common parameter are powers of three, and at least
one odd step must occur because distinct forms cannot merge using only
halvings. The common odd count Q is therefore positive. After any odd step,
the state is a unit modulo three, and subsequent shortcut steps preserve
that property. Hence the common endpoint is a unit modulo three for every
positive parameter; since A=3^Q, its intercept e is also a unit.

Example supplied by this credited compiler:

    x=388+2048t,
    T^11(x)=T^11(x+1)=T^11(x+2)=T^11(x+3)=243t+47,
    words 00101011100 / 10001011100 / 01100011100 / 11101000001.   (2)

This is the same four-way gate as #132, after shifting its parameter by one.
It is reused below, not counted as a new four-way cylinder.

## EPT-001. Endpoint transplantation for EVERY fixed positive original input

Fix any gate (1), any positive original N, and any required lower bound Z
for the new sources. One can construct, without a convergence assumption,
a time a, a target Y=T^a(N), a nonnegative integer k and an ordinary t>=t0
such that EVERY gate source is at least Z and

    T^(L+k)(B+Mt+d) = Y = T^a(N), all d in F.               (3)

If 3 does not divide N, take a=0 and Y=N, so all new sources are pure
predecessors of N itself. If 3 divides N, write N=2^v u with u odd; then
v halvings and one odd step give a=v+1 and Y=(3u+1)/2=2 mod3.
This is a finite prescribed prefix, and in all cases Y<=2N.

### Ternary lifting and the exact source-height bill

The order of two modulo 3^Q is

    P=2*3^(Q-1).                                          (4)

An elementary proof starts with order two modulo three and uses
v3(4^(3^j)-1)=j+1, obtained inductively by expanding (1+3c)^3.
The order at each lift multiplies by three, reaching the number of units.
Thus two generates ALL units modulo 3^Q. There is a unique 0<=k0<P with

    2^k0 Y=e mod3^Q.                                      (5)

It can be computed one ternary digit at a time: a solution k at precision q
has the three candidates k+d*(2*3^(q-1)), d=0,1,2, at precision q+1;
exactly one works. This is a finite modular calculation, not an orbit search.

Let t_min>=t0 ensure B+Mt+d>=Z for all d. Let k_min be the least nonnegative
integer for which 2^k_min Y>=A*t_min+e. Choose the least k>=k_min congruent
to k0 modulo P. Then

    k_min <= k < k_min+P,
    t=(2^k Y-e)/A >= t_min.                               (6)

Equation (1) now ends at 2^k Y. Appending exactly k zero bits on every new
source arm gives (3). The same actual original N is retained throughout.
Increasing k by arbitrary multiples of P gives arbitrarily far translations.

This is different from replacing N by a nearby parameter and claiming that
its certificate applies to N. It keeps the orbit component by an explicit
common endpoint. It is also different from claiming all new roots are below
N: they may be much larger, and no minimality argument is licensed by (3).

Example: for N=27, the one-step target is Y=41. Gate (2) has Q=5,e=47.
Here k=8 gives 2^8*41=243*43+47, so

    T(27)=T^19(88452)=T^19(88453)=T^19(88454)=T^19(88455)=41. (7)

All four new sources are pure predecessors of 41. They are NOT smaller
original companions of 27. The five paths in (7) are literal positive paths.

## EPT-002. Thick inverse basins; a quantitative all-positive-component theorem

For every positive Y coprime to three, every finite integer offset pattern F,
and every Z, the pure predecessor set of Y contains a translate x+F lying
above Z, with all its points reaching Y at ONE common finite time.
Normalize F by subtracting its minimum and apply EPT-001 with a=0.
Singleton patterns follow by taking a larger finite pattern first.

In particular, the pure predecessor set of every such Y contains arbitrarily
long blocks of consecutive integers: it is THICK. For every positive N,
including multiples of three, its merger component is thick. Indeed EPT-001
reaches a unit Y on N's actual orbit after at most v2(N)+1 steps.

The coprimality qualification for PURE predecessors is necessary. If 3|N,
the only direct predecessor is 2N: the odd inverse (2N-1)/3 is not integral.
The same applies recursively to every 2^jN. Thus its entire pure predecessor
set is exactly {2^jN:j>=0}, which has no long consecutive blocks.
The component statement survives because it permits the short forward prefix.

### Blocks within a computable multiplicative height window

For every K>=1 there is an effective constant C_K such that for EVERY N>=1,
its component contains K consecutive integers, each strictly larger than N
and at most C_K*N. They reach a common actual iterate T^a(N), with
0<=a<=v2(N)+1 (and a=0 whenever 3 does not divide N).

To see the quantitative claim, choose once a gate for F={0,...,K-1}, using
a two-offset gate when K=1. Write D=max F, M=2^L, A=3^Q and P as in (4).
For Z=N+1 choose t_min=max(0,ceil((N+1-B)/M)); positivity is automatic.
Then t_min<=N/M+1 and

    A*t_min+e <= (A/M+A+e)N,    Y<=2N.

Put H=max(2,A/M+A+e). The least choice (6) satisfies 2^kY<2^P*H*N:
if k_min=0 this is immediate, and otherwise the minimality of k_min gives
2^(k_min-1)Y<A*t_min+e. Therefore

    B+Mt+D < [(M/A)*2^P*H+B+D]N.                          (8)

The ceiling of the bracket is a possible C_K. It can be extremely large;
this is an effective existence bound, not a practically small compression.
Its significance is that N is fixed and universally quantified, rather than
chosen later to satisfy newly prescribed dyadic digits.

### Consequences and exact remaining boundary

An eventually syndetic set S is one meeting every sufficiently late block
of some fixed length K. Every such S meets every merger component: place a
K-block of that component beyond the threshold. Consequently it suffices
for Collatz to prove that the convergent set has bounded gaps eventually.
Equivalently, existence of even one nonconvergent positive integer forces
arbitrarily long entirely nonconvergent blocks, arbitrarily far out.

No bounded-gap theorem for convergent numbers is proved here. Thickness of
two different components does not force them to intersect; disjoint thick
sets exist. Thickness alone does not give positive natural density, much
less contradict a density-one theorem. No density or global convergence
claim is inferred from these consequences.

## EPT-003. Complete one-block inverses under the ORIGINAL source cap

Fix integers N>=2 and X>=1. Consider a physical inverse witness from an ODD
source m<N to X with word 1^r0^j, where r>=1 and j>=0. Put R=floor(log2 N).
Every such witness, and only such a witness, is obtained from

    1<=r<=R,   3^r divides 2^j X+1,
    m=2^r*(2^j X+1)/3^r-1,    1<=m<N.                    (9)

Moreover all possible j lie in the finite range

    2^j X+1 <= 3^R,
    0<=j<=floor(log2((3^R-1)/X)),                         (10)

with no candidates when X>3^R-1. This is a source-cap bound, not an arbitrary
clock cutoff. Testing all j and all r up to v3(2^jX+1), retaining (9), is
complete at unbounded clock for THIS block language.

Proof. Write m+1=2^r b. The first r steps are physically odd and reach
3^r b-1; the j following halvings reach X exactly when
3^r b=2^jX+1. Conversely the integrality and positivity in (9) guarantee
all those parities. Since m+1<=N, r<=R and b<=floor(N/2^r). Finally

    max_(1<=r<=R) 3^r floor(N/2^r) = 3^R.                (11)

Indeed, for r<R set q=floor(N/2^r)>=2. Then
3*floor(q/2)>=q, so these terms do not decrease as r increases; the final
term is 3^R. Equations (10) follow. The endpoint bound is sharp: the source
m=2^R-1<N with word 1^R reaches 3^R-1.

For each fixed j, taking the largest admissible valuation r minimizes m
among its one-block candidates. The multi-block algorithm retains all r;
it does not assert that its first found complete witness is the least root.
Pure-halving-only witnesses introduce no extra existence case: such a
witness with root below N implies X<N already, where the empty witness
with original source X is available.

## EPT-004. Complete finite inverses at EVERY fixed odd-block budget

An odd block is a maximal consecutive run of ones in a physical word;
even prefixes and tails are allowed. For every finite block budget B>=0,
fixed original cap N>=2 and endpoint X, there is a terminating exact decision
procedure for whether ANY m<N reaches X using at most B odd blocks.
No bound on the lengths of individual runs is supplied as an extra input.

Define a finite height envelope

    U_0=N,  U_(b+1)=3^floor(log2 U_b).                    (12)

Every state reached from a source below N within b odd blocks is below U_b.
This follows by induction from (11): an odd block starting below U_b peaks
at most at U_(b+1)-1, and even steps decrease. U_(b+1)>=U_b for U_b>=2.
Thus (12) also covers shorter paths and arbitrary even stretches.

Algorithm. If X<N return the original root X and the empty word. If B=0,
or X>=U_B, return NO_IN_THIS_GRAMMAR. Otherwise enumerate every last-block
predecessor z<U_(B-1) from (9)--(10), now with cap U_(B-1). For EACH z,
recursively test whether some ORIGINAL root m<N reaches z with at most B-1
blocks. On success concatenate its actual word and the last-block word.
If all candidates fail, return NO_IN_THIS_GRAMMAR. The base cap in every
recursive call is still N; U_b is only an intermediate-state envelope.

Termination follows from finite branching (10) and decreasing B.
Soundness follows from concatenating actual positive paths with the same
original root m<N. For completeness, strip initial even steps from a
nonempty candidate path; this only decreases its original source. If no
odd step remains, X<N was handled. Otherwise split off its last odd block
and even tail. Their start z is below U_(B-1) by (12), so its exact r,j
appear in the enumerated menu, and the prefix is covered inductively.
A split with zero separating even steps can only merge two odd blocks,
so the returned word never exceeds the advertised block budget.

This is NOT an all-source successful selector. For example N=3, X=T(3)=5
has no root m<3 reaching X at ANY block budget: roots 1 and 2 remain in
{1,2}. An actual-input procedure must sometimes advance the original N-arm.
Every arbitrary finite lower-root merger belongs to some finite block budget
at some finite actual endpoint; the theorem does not bound or force those
resources for every N. It reorganizes a complete search, not its global success.

## EPT-005. Ternary valuation switches at the first original step

For EVERY odd positive N and integer s>=6 satisfying

    3^s divides 8N+3,   b=(8N+3)/3^s,

there is the explicit smaller ORIGINAL source

    m=2^s b-1,    0<m<8*(2/3)^s*N<N,
    T^(s+4)(m)=T(N).                                    (13)

The m-word is 1^s0100; the N-word is just 1. This is a two-block witness.
It uses the actual ternary valuation of N, not freely assigned future parities.
Proof: the odd block reaches 3^s b-1=8N+2. The suffix 0100 follows

    8N+2 -> 4N+1 -> 6N+2 -> 3N+1 -> (3N+1)/2.

All parities follow from N odd. Also
m=8*(2/3)^s*N+3*(2/3)^s-1; for s>=6 the constant is negative and
8*(2/3)^s<1. This proves every bound in (13). Taking the exact valuation
s gives arbitrarily strong compression on the corresponding unbounded
families. All these N are divisible by three, so none has a smaller pure
ancestor at any depth; yet one forward step creates the lower-root merger.
N>1 and T(N)>N, so the entire displayed original arm stays above N. This
arm is only one step long; it is not marketed as a long forward excursion.

For each fixed s, infinitely many b satisfy
3^s b=27 mod32. They give N=3 mod4 as required of a hypothetical least
counterexample. Taking b in those progressions proves genuinely infinite
ordinary families, not just independent abstract comparison parameters.
Examples of whole cylinders, all t>=0, are

    T(1731+2916t)=T^10(1215+2048t)=2597+4374t,
    T(4647+8748t)=T^11(2175+4096t)=6971+13122t.            (14)

Both original N-families are 3 mod12. The second companion is below N/2.
The one-block alternative 1^(s+1)0000 would use 2^(s+1)b-1 and require
s>=7 for a uniform smaller-root bound. Equation (13) improves its factor
by nearly two and reduces the admission threshold to six; the alternative
is not counted as a separate new success class.

A distinct three-block example is

    T(111)=T^12(103)=167, word 111011110100.

The complete cap-111 query proves that the endpoint 167 has no smaller-root
witness with at most two odd blocks. It does not prohibit other later-endpoint
certificates. Its affine lift supplies another whole family:

    T(111+8748t)=T^12(103+8192t)=167+13122t, t>=0.         (15)

These N are again 3 mod12. Here v3(8N+3)=4 for every t, so (15) genuinely
leaves the guard of (13). To verify the whole cylinder, the companion shift
8192 is a multiple of 2^12, preserving all twelve physical parities; its
word has eight odd steps, giving endpoint shift 2*3^8=13122. The original
one-step shift gives the same slope. All smaller-root bounds hold throughout.

## Exact executed evidence, limitations, and next target

Run from repository root:

    python -S -B experiments/paired-comparison/endpoint-transplant/run.py --full /tmp/ept.jsonl --summary /tmp/ept.json
    python -S -B experiments/paired-comparison/endpoint-transplant/verify.py /tmp/ept.jsonl --summary /tmp/ept.json --self-test

The deterministic corpus contains 148489 rows: 74 whole affine gates, 254
modular-log lifts through Q=64, 1541 explicit target transplants, 130048
complete small inverse queries, 16380 original-source selector outcomes,
183 ternary-family members (including s=96 and 128), and nine sharp-cap checks.
The large-Q modular rows do not allocate astronomically large powers 2^k:
they verify modular lifting. Explicit transplanted integers use the two-,
three-, and four-offset gates for all N=1..512, plus five high-threshold cases.
Gate coverage also includes offsets through 2^64+3 and consecutive patterns
of lengths 2..12. The proof, not these finite bounds, supplies the universal
quantifiers of EPT-001/002.

The inverse query grid is exactly cap=2..128, X=1..256, B=0..3. The selector
grid is exactly N=2..4096 and B=0..3, trying actual original times a=1..8.
Every failed outcome is retained. Independent FORWARD enumeration of every
root m<N through three odd blocks checks both positive and NEGATIVE outcomes,
and the first successful original time; it imports no generator or repository
module. This is not merely a merger-witness checker.

| Allowed companion odd blocks | Merger by original time 8 | Outside this bounded search |
| --- | ---: | ---: |
| 0 (forward descent baseline) | 3791 | 304 |
| 1 | 3908 | 187 |
| 2 | 3959 | 136 |
| 3 | 3964 | 131 |

At B=3, 1019 displayed certificates have no forward descent on their original
arm, including 53 whose original source is divisible by three. There are
173 successes beyond forward descent within the same eight-step horizon.
Many other cases get an earlier merger despite having a later descent by
that horizon. Counts are NOT convergence percentages, optimal companion
counts, or a comparison against the different C-grid in #129/#131.

Generator runs normally and under -O produce identical full bytes and
summaries. The standalone verifier runs normally and under -OO with -S,
and rejects 20 direct semantic row mutations plus three duplicate-key/type
JSON controls. These are direct controls, not separately resealed full-corpus
mutations. Same-author implementation diversity is not independent review.
A combined prepublication command reached its execution time limit; the
final commands were rerun separately. See the receipt for final-byte checks.
No complete-checkout root validator, remote CI, Lean build or independent
mathematical review was run. Direct Git transport failed DNS; API publication
and source-blob readback are not full-checkout validation.

**What is actually still missing.** The all-component theorem closes the
existence/access quantifier for prescribed finite offset patterns, but its
new roots can be above N. The root-capped block compiler preserves m<N and
is complete at every fixed budget, but has no proved universally successful
budget or actual-endpoint rule. A full resolution needs a theorem that
bridges these two sides: a smaller-root certificate for the ACTUAL N, or a
separately established eventually-syndetic convergent set. Neither is claimed.
Review the ternary-unit endpoint, source-height bill, necessary pure-basin
qualification, all-r inverse menu, recursive ORIGINAL cap, and negative
forward cross-check before enlarging the certificate language further.
