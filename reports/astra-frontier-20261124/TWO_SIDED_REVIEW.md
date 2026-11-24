# Independent reconstruction of PR191

Frozen source: PR191, `37b3916633cd32a0c173b20bb18ec3a7ec290a63`,
`research/two-sided-cycle-packing-20261124/README.md`, Git blob
`5380e3b5f0f0366556a2591e910f039bac0abfa7`.
[Source](https://github.com/GettysburgResearch/collatz/blob/37b3916633cd32a0c173b20bb18ec3a7ec290a63/research/two-sided-cycle-packing-20261124/README.md).

These are written-mathematics verdicts at the named head. The Lean replay of
its finite algebra is separate. No verdict asserts universal cycle exclusion.

## TCP-1 and TCP-2: VERIFIED

A positive rational cycle has one reduced denominator coprime to six.
Its literal parity words, applied to two states over that denominator, force
divisibility of their numerator difference by the entire power of two for a
common future. A common past containing s odd steps supplies an independent
factor 3^s. Neither assertion changes the underlying source or uses a
random law.

For equal-clock blocks, let N=2^A, M=3^p and D=N-M. Multiplying their actual
positive identities proves D>0. The predecessor of a minimal boundary and
the predecessor of a maximal boundary give D n_min >= d C_min and
D n_max <= d C_max. A common prefix of length l and a common suffix with
s ones factor the carry range exactly as 2^l 3^s Delta. The same factor
divides every boundary difference. Sorting the distinct boundary numerators
therefore yields d Delta >= D(r-1). Repeated h future blocks and k past
blocks yield d Delta >= D 2^(hA)3^(kp). The complete denominator is retained.

For the adjacent swap, Delta=1. If A>=3, D=1 is impossible modulo eight:
2^A-1 would be 7 modulo eight whereas 3^p is 1 or 3. For A=2 the two legal
centers are 1 and 2, both fixed by their two-step words; an actual mixed
cycle cannot move between them. The result excludes mixed schedules, not
each single atom's own possible cycle.

## TCP-3: VERIFIED CONDITIONAL ON THE EXACT TS5 INPUT

Every contracting affine block takes its input strictly toward its own
center. A cyclic maximum is at most the largest center, even when odd
counts vary. The cited bound center < (2/3)2^Lmax then makes repeated
maximal-length atoms impossible for an integer cycle, by divisibility of
the difference by 2^Lmax. Sorting multiple occurrences gives the stated
variable-length cap and rational-denominator version.

The full source for the center bound was inspected:
PR177 `25bf9b95a9404998e8e55aa401773488cd3dd4b8`,
`research/lean-exact-witness-global-20261121/construction-attacks-20261123/descent/TEMPLATE_SELECTION.md`,
TS5, Git blob `1a5181163de2d5ac751954ddedac96e1c0ca37dc`.
[Exact dependency](https://github.com/GettysburgResearch/collatz/blob/25bf9b95a9404998e8e55aa401773488cd3dd4b8/research/lean-exact-witness-global-20261121/construction-attacks-20261123/descent/TEMPLATE_SELECTION.md).
It uses Matveev's published logarithmic-form theorem and a continued-fraction
certificate. This review does not independently certify that imported
analytic theorem or claim to have replayed its separate certificate. Our
new elementary two-block result has no TS5 dependency.

## TCP-4: VERIFIED

Write A=ga, p=gb with gcd(a,b)=1. Choosing bu-av=1 gives, modulo each
m=gcd(C,D_ell), units w=2^a/3^b and t=2^u/3^v. The exact identities
t^b=2w^v and t^a=3w^u respect both monic defining relations of R_ell.
The image of F is 3^(1-p)C, including all cyclic positions and all Bezout
exponents. Rotation to minimal b d_i-a i makes the T exponents nonnegative;
negative W exponents are legitimate units.

The evaluation row annihilates the multiplication matrix of (T-1)F modulo
m. Multiplication by the adjugate and the coordinate corresponding to 1
give m dividing the determinant, without assuming m prime or the ring a
domain. Prime by prime,
min(v(C),sum v(D_ell)) <= sum min(v(C),v(D_ell)). Thus the product of the
component gcd bounds includes every prime power of gcd(C,D); overlap of
cyclotomic factors is not discarded.

Over the complex numbers the quotient ring decomposes into its simple
(zeta,tau) evaluations. The map z=tau^a zeta^(-u) gives
z^b=2^a zeta^(-1), and is bijective on each b-element fiber because a,b
are coprime. The value of F is z^(1-p)Q(z), while tau-1 is nonzero.
This proves the exact zero-determinant characterization. In the principal
component the reduced F has positive coefficients and degree below b;
Eisenstein for T^b-2 makes its value nonzero. No bound forces a strict
saving in at least one component of an arbitrary word.

## TCP-5: VERIFIED WITH ITS ORIGINAL MINIMUM SCOPE

The identity 8*4^s(q'+7)=9(q+7)+166s preserves divisibility of q+7 by
83 in both directions. If that divisibility holds, q+7 is a positive even
multiple of 83, and y=60(q+7)/83-5 is a positive odd integer. Direct
substitution gives the literal shadow gaps (1,2) and (1,4). Their odd
endpoints force the exact two valuations; they are not merely formal
affine maps. Since every block begins with gap one, an infinite shadow
cannot reach the odd fixed state one.

If q_* is the least original block boundary, every original odd state,
including the middle of each block, is at least (3q_*+1)/4. The shadow
value (60q_*+5)/83 is strictly smaller. Thus the argument really applies
to a globally minimal nonconverger occurring on the entire tail, or a
globally minimal nonstandard cycle. It does not apply to a minimum taken
only inside a fixed scalar level set, because the shadow need not preserve
that scalar.

Closing a cycle gives (2^(3r+2S)-9^r)(q+7)=166 times an integer. If the
first factor is a unit modulo 83, the smaller shadow exists. The remaining
congruence 2S=59r modulo 82 follows from ord_83(2)=82 and 9=2^62;
in particular r must be even for the globally least cycle in this alphabet.
It does not exclude every cycle with odd block period independently of
the global-minimum hypothesis.

## First remaining cycle obligation

Packing tests a supplied partition, and the norm detects divisibility
failure of a supplied complete word. A universal proof still must force
a restrictive partition, bound the relevant word lengths, or obtain a
strict numerical denominator saving for every remaining primitive word.
The new elementary cycle packet attacks the partition and word-length
interface, without importing the desired universal bound as a hypothesis
that is subsequently treated as proved.
