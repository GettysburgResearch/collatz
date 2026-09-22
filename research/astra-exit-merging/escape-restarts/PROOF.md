# Actual escape restarts with one common contracting parameter

**AER-001–004: PROPOSED pending independent mathematical review.**
Date: 2026-09-21. Parent: PR #132, `7687eec1ac364009d644cb8d015f1fe3b28730cc`.
This is an additive research continuation. It does not close Collatz, assert
external priority, or promote any earlier proposal.

## Meaning of the result

The preceding affine-family compiler can choose a new subprogression of
parameters; that is not a restart for the already fixed input. This packet
instead supplies actual guarded returns for the given integer parameter.
Three added returns, together with one credited old return, all decrease
**the same quantity D-2**. Their arbitrary interleaving therefore terminates
unconditionally in a merger or an explicit failed guard. One of the new
returns passes through an expanding return before making a net decrease.

This removes an infinite-iteration question for this specified partial
language. It does not supply the missing transitions when the language ends.
Every finite word of the returns can be followed by a specified merger on
one complete residue class. Words starting with a new return lift to infinite
families rejected immediately by the exact #129 selector. These families have
smaller ORIGINAL companions and can keep their entire displayed original
forward arms above their sources. Other, later project selectors may already
cover some of these sources; the numerical benchmark is against #129 only.

## Conventions and credited input

Use the unabsorbed shortcut map

\[
T(n)=\begin{cases}n/2,&n\equiv0\pmod2,\\(3n+1)/2,&n\equiv1\pmod2.\end{cases}
\]

A word records actual source parities in chronological order. Both arms of a
comparison stage advance equally; the original sources can have different
prefix clocks. Raw iteration continues through 1 -> 2 -> 1. No absorbed
comparison is mistaken for an equal-clock merger.

Write

\[
H(C)=(9C+2,C),\quad R(D)=(3D-4,D),\quad
Q(E)=(3E-1,E),\quad K(E)=(9E-10,E).
\]

H uses C>=1; R and K use integer parameters at least 2 so both coordinates
are positive. The R entrance and its complete two-step table are credited
to #129 / AR-002, at `9d362511343c97790d42808c363b090a3342b45f`,
`research/paired-comparison/anchored-returns/PROOF.md`:

\[
H(8v-1)\xrightarrow{101\,/\,111}R(27v-1),\qquad v\ge1.
\]

| Actual D | R endpoint after two steps | Upper / lower words |
|---|---|---|
| D=0 mod4 | Q(D/4) | 00 / 00 |
| D=2 mod4 | R((3D+2)/4) | 01 / 01 |
| D=3 mod4 | (Y-5,Y-1), Y=9(D+1)/4 | 10 / 11 |
| D=1 mod4 | K((3D+1)/4) | 11 / 10 |

D=2 is already R(2)=(2,2), so a merger procedure stops there rather than
iterating its fixed comparison. The older Q and even-adjacent completions,
VL bridges, compressed first companion, and #132 clock-liveness argument are
credited, not counted as new. Exact source pins are in SOURCES_AND_LIMITS.md.

## 1. AER-001: a complete K table and three added R restarts

### 1.1 The K table is exact for every E>=2

Two actual shortcut steps give the following exhaustive, disjoint table.

| E modulo4 | New lower parameter F | Endpoint | Upper / lower words |
|---|---|---|---|
| 0 | E/4 | (27F-7,F) | 01 / 00 |
| 2 | (3E+2)/4 | R(F) | 00 / 01 |
| 1 | (3E+1)/4 | (27F-28,F) | 11 / 10 |
| 3 | (9E+5)/4 | (3F-11,F) | 10 / 11 |

Proof: substitute E=4t+i in K(E) and apply T twice. For i=0 use t>=1;
for i=1 use t>=1 because E=1 is outside the positive K domain. For i=2,3
use t>=0. The stated parities and every positive endpoint then follow.
Only the second row returns to R. The other three rows are **not** declared
resolved by this table.

### 1.2 The actual return rules

Each row below maps R(D) to R(E), without exchanging original source labels.
All guards are read from the current D. They are mutually disjoint.

| Tag | Actual guard | E | Upper / lower words | Length |
|---|---|---|---|---:|
| A, credited | D>2, D=2 mod4 | (3D+2)/4 | 01 / 01 | 2 |
| B | D=13 mod16 | (9D+11)/16 | 1100 / 1001 | 4 |
| C | D=23 mod32 | (27D+19)/32 | 10101 / 11100 | 5 |
| D | D=191 mod32768 | (19683D+41635)/32768 | 101101010111100 / 111111010001001 | 15 |

The letter D in the first column is a rule name; D in formulas is the
integer parameter. In the code these are separate string and integer values.

**B proof.** The R row D=1 mod4 first reaches K(E1), E1=(3D+1)/4.
The additional condition E1=2 mod4 is exactly D=13 mod16. Apply the second
K row to get E=(3E1+2)/4=(9D+11)/16. The concatenated words are 1100/1001.
Equivalently D=16t+13 gives E=9t+8, t>=0.

**C proof.** Substitute D=32t+23. The complete physical paths are

```
3D-4: 96t+65, 144t+98, 72t+49, 108t+74, 54t+37, 81t+56;
D:    32t+23, 48t+35, 72t+53, 108t+80, 54t+40, 27t+20.
```

The final pair is R(27t+20). Every displayed parity holds for all t>=0.

**D proof, with its expanding component kept explicit.** On the broader
class D=2048t+191, the eleven-step words

```
G_upper = 10110101011; G_lower = 11111101000
```

give R(D1), D1=2187t+205. One finite proof is to replay the base pair (569,191):

```
569,854,427,641,962,481,722,361,542,271,407,611;
191,287,431,647,971,1457,2186,1093,1640,820,410,205.
```

For a source progression of modulus 2048, the slope at every prefix time
j<11 is an even integer (an odd power of 3 times 2^(11-j)). Thus these base
parities prove the words on the entire progression, and the endpoint slopes
are 3*2187 and 2187. Importantly,

\[
D_1-D=139t+14>0.
\]

G is an expanding return and is not an accepted contracting rule by itself.
Restrict instead to D=32768t+191. Its G output is D1=34992t+205, which is
13 mod16 for every t. Apply B. The final lower parameter is

\[
E=19683t+116=\frac{19683D+41635}{32768}.
\]

Concatenating G with B proves row D. The fixed example is the actual
comparison-parameter path 191 -> 205 -> 116, with clocks 11 then 4 on each
arm. It is not a claim that the original-source integer is 191.

### 1.3 Exact single-rule countdowns are not used as a switching rank

For B,

\[
7E-11=\frac9{16}(7D-11).
\]

The guard is exactly v2(7D-11)>=4. Hence consecutive B steps subtract four
from that valuation. For C,

\[
5E-19=\frac{27}{32}(5D-19),
\]

and consecutive C steps subtract five from v2(5D-19). The arguments are
nonzero on the positive integer domain of the corresponding rule. For A,
the credited identity is E-2=3(D-2)/4. These three centres differ. The next
section uses one common ordinary quantity instead of assuming that separate
countdowns may be reset or combined freely.

## 2. AER-002: arbitrary actual switching terminates under D-2

For every admitted row in Section 1, E>=2 and

\[
\boxed{0\le E-2\le\frac67(D-2),\qquad E<D.}
\]

For A the ratio is 3/4. For B,

\[
E-2=\frac{9(D-2)-3}{16}\le\frac9{16}(D-2).
\]

For C, write D=32t+23, E=27t+20. Then

\[
7(E-2)=189t+126\le192t+126=6(D-2).
\]

For D, D=32768t+191 and E=19683t+116 give

\[
7(E-2)=137781t+798<196608t+1134=6(D-2).
\]

All parameters at t=0 and all positive slopes in these expressions are in
the stated positive domains. This proves the inequality for every integer
admitted by any rule, not only bounded test values.

**Normalizer.** At D=2 return MERGE. Otherwise apply the unique admitted
A/B/C/D rule, append its actual words, and repeat. If no guard applies,
return the unchanged terminal D with label OUTSIDE. For EVERY D>=2 this
procedure terminates. For D>2, let K be the least nonnegative integer with

\[
6^K(D-2)<7^K.
\]

There are at most K accepted stages and at most 15K shortcut steps per arm.
If K stages occurred without termination, the positive integer terminal
D_K-2 would be less than one, a contradiction. This is an O(log D) bound
on stage/physical-word length, not an assertion of O(log D) bit complexity.

No Collatz-convergence assumption, least-counterexample hypothesis, stopping
time oracle, or controlled choice of a parameter digit is used. D is the
actual input, and the guard selects its actual next words. In particular,
changing among the return types cannot recharge this rank. An infinite
positive ordinary itinerary wholly in this specified return language is
impossible. After j nonterminal returns,

\[
D_0-2\ge(7/6)^j.
\]

Arbitrarily long finite words can have different, increasingly large sources;
that fact is consistent with this bound.

**Scope.** OUTSIDE remains possible. The procedure is total as a finite
normalizer, not total as a successful merger selector. The common rank is
not asserted for G alone, for all H returns, for the other three K rows,
or for arbitrary Collatz steps.

## 3. AER-003: every finite return word has an exact successful cylinder

A terminal R merger is available on D=64t+12:

\[
T^6(3D-4)=T^6(D)=9t+2,
\]

with words 000001/001100. Substitution proves the six parities; this is
also an instance of the credited Q/adjacent completion. It is not a new
assertion that every R parameter merges.

Take ANY finite nonempty word s over A,B,C,D. For a row i write its lower
map as F_i(D)=(P_i D+a_i)/2^(ell_i), using the constants in Section 1.
Start with the terminal class r=12, M=64. Working backwards through s,
replace

\[
r\longmapsto (2^{\ell_i}r-a_i)P_i^{-1}\pmod{2^{\ell_i}M},
\qquad M\longmapsto2^{\ell_i}M.
\]

Each P_i is odd, so the inverse exists. The congruence modulo 2^(ell_i)
is exactly that rule's guard; its quotient lies in the next required class.
Induction therefore proves one exact residue class of inputs realizing the
specified sequence and ending in the terminal class. Conversely those guards
and terminal class imply this congruence, so it is exact for this word.
The modulus is

\[
M_R=2^{6+\sum_i\ell_i}.
\]

The least residue is positive: none of the possible first guards contains
zero. Every positive representative stays positive by the actual words.
D=2 cannot occur in the middle of this prescribed successful word: A fixes
it, the other guards exclude it, and the terminal class excludes it.

### Lift into the existing H comparison without changing its original arms

Impose D=27v-1, C=8v-1. Since 27 is invertible modulo M_R, this gives one
class C=B mod M_H, where M_H=8M_R. Prefix the upper/lower words by 101/111.
The resulting H cylinder has length

\[
L=3+\sum_i\ell_i+6.
\]

Every positive source C in the class satisfies an actual equal-clock merger
of H(C) and C. The endpoint is an affine function of the progression index.
This is still a prescribed finite-word family, not an infinite ordinary
trajectory or a statement that every fixed C enters the family.

### Whole old-failure classes, not just isolated additional examples

If the first return letter is B, the H parameter satisfies C=79 mod128.
If it is C, then C=63 mod256. If it is D, then C=255 mod256.

All three classes have C=15 mod16, hence v2(3C-1)=2, failing the old VL
odd guard; the even guard does not apply. They also have v=(C+1)/8 even,
so v2(9v-1)=0, failing #129's AR-A guard. For the first class C is not
31 mod32. For the other two classes the AR-B value Y=243(C+1)/32 is
respectively 2 or 0 mod4, not its required residue 1. Therefore the exact
#129 selector is OUTSIDE at clock zero on EVERY such source.

This is a strict comparison with #129's specified algorithm only. The
later #130/#131/#132 gate compilers are not refuted, and no disjointness
from their successful regions is asserted.

For the single word B, the complete cylinder is

\[
C=7759+8192t,\qquad
T^{13}(9C+2)=T^{13}(C)=2187t+2072,
\]

with upper/lower words 1011100000001 / 1111001001100. The arbitrary words
B^j and mixed words, such as (BCAD)^j, supply unbounded finite families.
Their current parameters, not newly chosen intermediate source labels,
are what the contracting normalizer uses.

## 4. AER-004: smaller ORIGINAL sources, with the entire original arm above its root

Fix any H cylinder C=B+Mt from Section 3, with words W,Z of length L.
Let q_j count the odd bits of the first j letters of W and set

\[
\gamma=\min_{0\le j\le L}\frac{9\,3^{q_j}}{2^j}>0.
\]

The original upper prefix at every j is an affine function of C with
slope at least gamma and a positive constant. Choose ANY r>=2 such that

\[
\gamma 3^{r-1}>8\,2^r.
\]

Such r exist and all sufficiently large r work. Choose positive u by CRT:

\[
3^{r-1}u\equiv4B+1\pmod{4M},\qquad
2^r u\equiv1\pmod3.
\]

There is exactly one class modulo 12M. It consists of odd u, since the
first modulus is divisible by four and its right side is odd. Define

\[
N=2^r u-1,\qquad m=(N-3)/4,\qquad
C=(3^{r-1}u-1)/4.
\]

These are positive integers. C is in the required H class and the first
congruence makes 3^r u=3 mod4. The credited compressed first-odd-run entry
therefore has words

\[
N:\ 1^r01,\qquad m:\ 1^{r-2}01,
\]

and endpoints H(C),C. Thus

\[
\boxed{T^{r+2+L}(N)=T^{r+L}(m),\qquad0<4m<N.}
\]

The parameter r and the finite return word can both be unbounded. No
smaller *local* intermediate point is used instead of this original m.

### Whole-arm no-descent proof

The first r odd steps increase N. The intervening value
(3^r u-1)/2 exceeds N for r>=2 because 3^r>2^(r+1). Also
C=(3^(r-1)u-1)/4 >=3^(r-1)u/8. Every upper H-prefix is at least gamma*C,
which exceeds 2^r u>N by the chosen inequality. Consequently

\[
\boxed{T^j(N)>N\quad(1\le j\le r+2+L).}
\]

The second CRT condition gives 3|N. Every positive one-step predecessor
of such an N is 2N: the odd inverse (2N-1)/3 is not integral. Inductively,
its only positive predecessor at depth b is 2^b N. It has no smaller pure
ancestor at any depth, despite the smaller-source two-sided certificate.

### A numerical instance, literally replayed

For the word B, gamma=729/4096; r=13 and u=60941 give

```
N=499228671,  m=124807167,  C=8096636495;
T^28(N)=T^26(m)=2161541018;
min_{1<=j<=28} T^j(N)=748843007>N;
3|N, 0<4m<N.
```

Its H parameter is in the strict old-failure class. A mixed BCAB example is

```
N=4094923276287, m=1023730819071;
T^41(N)=T^39(m)=14200048388774;
min_{1<=j<=41} T^j(N)=6142384914431>N.
```

The large numbers illustrate the proved arithmetic properties, not evidence
that the global coverage question has become small.

## 5. Least-counterexample interpretation and boundaries

A least positive nonconvergent N cannot have any of the Section 4
certificates, because m<N converges. The same two original trajectories
may pass through these mixed R returns and the older H returns; no root,
clock, or orientation is reset. The R part has the unconditional finite
rank bound of Section 2. The earlier #132 persistent-companion argument
handles an infinite sequence of admitted noncore H checkpoints in a
least-counterexample comparison. Neither statement forces a restart at
EVERY finite failed guard.

The implemented extension tries the three exact old #129 transitions first,
then the new finite R normalization and a credited Q/gap completion on an
old failure. This preserves all old successful certificates byte-for-byte.
When a trial does not produce a complete H transition, the reported OUTSIDE
state remains the last accepted H checkpoint; clocks of a failed trial are
not counted as accepted progress. Its local R path is reconstructible via
kernel.r_normalize. A merger-or-failed-guard normalizer is not a convergence
algorithm.

Concrete residual controls remain C=17 and C=71. The selected language is
OUTSIDE there even though their H pairs have the separately known isolated
synchronous meetings at times 54 and 64. C=2 has no synchronous meeting at
all: 20 and 2 first reach 1 at clocks 6 and 1, and their raw core phases
remain opposite. These controls prevent either an OUTSIDE-to-divergence
inference or an assertion that all fixed H companions must synchronize.

**Still missing:** pointwise control of all other R/K exits and the other
first-entry classes, or a different root-compatible companion rule that
forces success. No complete Collatz proof was obtained. The new contribution
is that a particular escaping K branch can be restarted on its actual input,
and three added returns compose under a single proven rank, rather than
under separately reset valuations or chosen new parameter digits.

## 6. Evidence is separate from the proofs

The experiment independently replays 65,535 full R normalizations, all
4,095 tested K rows, 386 complete finite-word cylinders, 24 original-source
lifts, the same complete 65,536 H inputs as #129, and four controls. Its
135,584 deterministic rows include every unsuccessful H outcome.

The benchmark is 5,082 old versus 5,255 extended merger certificates, an
addition of 173 (54 at C=2 mod3), with all old words/endpoints retained.
There are 60,281 remaining OUTSIDE outcomes and no budget exhaustion in
this corpus. These are procedure outcomes, not convergence percentages,
not an exhaustive comparison against every later repository mechanism.

A separately written verifier imports no generator/kernel/repository module.
It computes stage endpoints from raw states, reconstructs whole-word affine
identities and finite classes in the forward direction, checks all actual
old/new selector outcomes and their independent clocks, and verifies whole
original-source progressions and all-state lower bounds. Computational
agreement does not independently accept the all-parameter proofs. See the
experiment guide and validation receipt for exact commands and limits.
