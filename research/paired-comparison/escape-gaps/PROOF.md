# A merger compiler for arbitrary gaps and successive affine comparison types

**EG-001--006: PROPOSED pending independent mathematical review.**
Date: 2026-09-20 (Asia/Jerusalem). This is a research continuation, not a
complete Collatz proof, independent acceptance, or an external priority claim.

Use the unabsorbed shortcut map T(n)=n/2 for even n and (3n+1)/2 for odd n.
All witnesses and all certificate arms are positive ordinary integers. Raw T
continues through 1 -> 2 -> 1. Negative integers appear only in a finite,
explicitly justified word compiler, never as positive witnesses. Words list
actual source parities chronologically; a pair of words has independent clocks.

## Provenance and the first publication

The preceding chat packet is already published as PR #125, head
`081dd4fb8af75b3b237a5eb4cef28b84bb5329be`, tree
`bde740504a4f936c2d780a22be5eee8eec40427e`. Its five files were not replaced.
The failed chat response did not mean that this publication was absent.
This continuation is stacked on that exact head.

The prior packet supplies the forced H-entry, valuation bridges, and the
original-source ladder (VL-001--009), with proofs in
`research/paired-comparison/valuation-ladder/PROOF.md`. It in turn pins #122
at `65c91ecea97d9ebf931eb1d9284b7950182a298e` and #123 at
`bf0696f888442c82a4c6cdc1df36becf8550295a`.

The live parallel work was also read: #124 at
`1d4dfc103055648def3db73860778a383a91ea3c` and #126 at
`7e996feb24cc5d8579d75b39e0b909ffc03b3bcb`, especially their PROOF.md files
under `research/astra-exit-merging/`. Adaptive companions and finite negative
word shadowing are not claimed first here. In particular #126 already uses
negative *periods* with power-of-two differences to obtain adjacent pairs.
The extension below does not require a negative period or a power-of-two gap:
it stops at an exactly specified even-step count, and compiles every resulting
positive integer gap. No source theorem from these proposals is silently
promoted to an accepted status.

No rank/transport theorem, density theorem, or external formalization is a
premise. Public literature search was not a comprehensive priority audit.
No claim of global novelty is made.

## The results in one paragraph

Every positive gap g has an explicitly computable dyadic progression of
synchronously merging pairs (x,x+g), with modulus at most 8*g^7. This yields a
uniform residue-class merger for every affine type (3^a*d+b,d) satisfying
3^a-b>2^a. Every H(C)=(9C+2,C) comparison has a finite normalization into an
eligible type. In particular every exponent in the 4-adic escape family and
every companion-ladder depth now has a constructive gate, rather than a
separately searched example. **A gate for every type is not coverage of every
parameter in that type.** The actual value still must satisfy its gate.

# EG-001. A strictly contracting equal-odd-count window

Let 0<x<y. Write i=v2(x), j=v2(y), and

    sx = i + v2(3*(x/2^i)+1),
    sy = j + v2(3*(y/2^j)+1).

The first two odd-source times on the x arm are i and sx, and on the y arm
are j and sy. Thus whenever

    max(i,j)+1 <= L <= min(sx,sy),     L>=2,                 (1)

each arm has exactly one odd step in the first L steps. The physical words
are 0^i 1 0^(L-i-1) and 0^j 1 0^(L-j-1), giving

    X=(3x+2^i)/2^L,       Y=(3y+2^j)/2^L.                 (2)

For g=y-x>=2,

    |Y-X| <= (3g+2^(L-1)-1)/2^L < g.                     (3)

Also max(X,Y) <= 3y/4+1/2 < y when y>2. If g=1 the new gap is zero or one;
the maximum still strictly decreases unless (x,y)=(1,2). That pair returns
to itself at L=2 and is an explicit excluded fixed comparison, not an
absorbed merger.

Consequently, a sequence using only these guarded windows and common even
halvings must stop after finitely many accepted steps, at a merger, a failed
guard, or the fixed pair (1,2). This is a genuine local decreasing integer
quantity. It is NOT a rank for the old expanding H returns, for negative
shadow prefixes, or for arbitrary mode changes. Failure of (1) is not
convergence or divergence information. For example (3,4) fails (1).

# EG-002. Every positive gap has a whole arithmetic progression of mergers

For every integer g>=1 we construct positive B and M=2^ell, with 0<B<M,
and equal-length words p,q having the same odd count, such that

    T^ell(M*t+B)=T^ell(M*t+B+g),       every integer t>=0.  (4)

Moreover the first construction satisfies

    M <= 8*g^7.                                           (5)

Thus one explicitly supplied success progression has ordinary natural density
1/M >= 1/(8*g^7) in its lower-source coordinate. This describes that single
progression, not a density for all pairs or the whole Collatz problem.

## Base gap and common doubling

For g=1, take M=8, B=4 and words 001/100:

    T^3(8t+4)=T^3(8t+5)=3t+2.

For even g=2h, double both sources of an h-certificate and prefix 0 to both
words. The new residue is 2B and new modulus is 2M.

## Odd gap, 1 modulo 4

For g>1 with g=1 mod4 put h=(3g+1)/4<g; then h=1 mod3.
Suppose a certificate for (z,z+h) has z=M*t+B. Restrict t to one residue
modulo 3 so that z=1 mod3. This is always possible because M is a power of 2.
Set

    x=(4z-1)/3,       y=(4(z+h)-2)/3.

Both are positive integers, y-x=(4h-1)/3=g, and the physical words 10/01
send (x,y) to (z,z+h). Appending the h-certificate proves (4). The new source
modulus is 4M, since t=t0+3v cancels the denominator 3. If 0<B<M and t0 is
chosen in {0,1,2}, the new residue (4(B+Mt0)-1)/3 lies strictly between 0
and 4M. Every v>=0 is retained.

## Odd gap, 3 modulo 4

Now put h=(3g-1)/4<g; h=2 mod3. Restrict z to 2 mod3 and set

    x=(4z-2)/3,       y=(4(z+h)-1)/3.

The words 01/10 send the pair to (z,z+h), and y-x=(4h+1)/3=g. The same
modulus and positivity arguments apply.

These reductions are a terminating integer recursion, not an assumed Collatz
trajectory of g. For g>1 every reduced gap is at most 4g/5. Both odd cases
cost a modulus factor 4. Since 4*(4/5)^7<1, induction gives M<=8*g^7;
the even step satisfies 2*8*(g/2)^7<=8*g^7. This also gives an explicit
logarithmic word-length bound ell<=3+7*log_2(g). No floating-point estimate
is needed by the implementation or by the inductive inequality.

## Two additional compiler choices retained in the experiment

Variant 1 uses the same recursion from the base

    T^5(32t+5)=T^5(32t+6)=9t+2,
    words 10001/01100.

It satisfies M<=32*g^7. This gives genuinely different cylinders, although
some can overlap or be contained in other gates.

Variant 2 always supplies a cylinder whose larger member is even. For odd
g>1 read j=v2(3g-1), set h=((3g-1)/2^j+1)/2<g, and invert the pair of words
1 0^j / 0^j 1. Restrict the old lower member z so that 2^(j+1)z=1 mod3;
then the new sources are

    x=(2^(j+1)z-1)/3,
    y=(2^(j+1)(z+h)-2^j)/3.

Their difference is g. Their parities and all indicated halvings are
physical; y has exactly j initial factors of 2. Use the odd-lower base
(5,6), and common doubling for even gaps. This variant also terminates by
strictly decreasing g. Bound (5) is asserted for variant 0, not silently
transferred to this alternate compiler.

The tests verify all three resulting cylinders symbolically. None of these
constructions asserts that the pair (x,x+g) merges for every x. In particular,
the gap-one example (1,2) never merges synchronously.

# EG-003. Balanced finite negative shadows compile successive affine types

Fix integers a>=1 and b, and suppose

    c=3^a-b > 2^a.                                        (6)

Then an explicit whole dyadic progression of positive d supplies an
equal-clock merger for

    (3^a*d+b, d).                                         (7)

The construction is uniform in a and b, not a separate numerical search.

## A finite word exists without assuming convergence of negative Collatz

Start at -c and follow actual signed shortcut T until precisely a even steps
have occurred. This stopping time L is finite. To prove it, on magnitudes
z>1 an odd step sends z to (3z-1)/2 >= z; an even step halves it. Before and
including the a-th even step, every magnitude is at least c/2^a>1. Thus the
path cannot reach the all-odd fixed point -1.

Furthermore, any odd block starting at magnitude z>1 has finite length,
because (3z-1)/2-1=3(z-1)/2 consumes one unit of v2(z-1) per odd step.
Therefore the next even step always occurs, until all a have occurred.
This proof uses neither periodicity nor a conjecture about negative orbits.

Let w be the resulting physical word. It has L-a odd steps, and write its
last state as -h, where h>1.

## The slope discrepancy disappears at exactly that depth

For any positive integer u sufficiently large for positive starting values,
put d=2^L*u-1. The two actual prefixes are

    3^a*d+b = 3^a*2^L*u-c  --w-->  3^L*u-h,
    d                         --1^L--> 3^L*u-1.           (8)

For the first identity, the difference from the signed path at prefix time
j is 3^(a+q_j)*2^(L-j)*u. It is even before the final time, proving every
required parity by induction. At time L its exponent is a+(L-a)=L. The
second identity is the usual finite odd spine. u need NOT be odd; its
valuation can make the actual odd run longer than the displayed prefix.

The original slope ratio 3^a has therefore become the constant positive gap
h-1. Apply any EG-002 certificate for that gap, with lower residue B modulo
M. The exact guard is

    3^L*u-h = B mod M.                                    (9)

Because 3 is invertible modulo M, this is one residue for u. It gives one
residue for d modulo 2^L*M. Choose its positive ordinary representative far
enough along the progression that 3^a*d+b>0. Then every positive-time state
is positive. The endpoint in (8) is positive and congruent to B with 0<B<M,
so it belongs to the nonnegative-index tail of the supplied gap certificate.

Appending the two gap words proves the entire affine merger cylinder. The
modulus from variant 0 is at most 8*2^L*(h-1)^7. The combined words have the
same length; their odd counts differ by exactly a, as coefficient comparison
requires. The original source names and any earlier clock offset are retained.

The signed path is only a finite parity template. It does not furnish one
infinite positive realization, a convergence proof for a negative orbit, or
permission to prescribe an arbitrary given positive source's future.

# EG-004. Every H comparison has a finite normalization into an eligible type

Let H(C)=9C+2 and C>0. Read s=floor(v2(C)/2), write C=4^s*d and put a=s+2.
Then 4 does not divide d, and the physical words (01)^s / 0^(2s) give

    (H(C),C) --> (3^a*d+2,d).                             (10)

The two-step identity is immediate from a lower parameter divisible by four:
(3^a*d+2,d) --> (3^(a+1)*(d/4)+2,d/4).

If d is odd, the pair in (10) already satisfies (6), since a>=2 and
3^a-2>2^a.

If d=2 mod4, two further steps, 00/01, give

    (3^(a-1)*D+(1-3^(a-1))/2, D),  D=(3d+2)/4.           (11)

The new exponent A=a-1 is at least one and its negative magnitude is
(3^(A+1)-1)/2>2^A. Thus EG-003 applies to this type too.

This is complete *type normalization* for all positive C. It does not say
the actual final parameter lies in a selected success cylinder. The new
selector tests those exact cylinders and returns OUTSIDE when they all
fail. The generator retains those outcomes.

## Concrete cylinders and a real old-language escape

For every t>=0,

    T^10(9(1024t+735)+2)=T^10(1024t+735)=729t+524,
    words 1011000001 / 1111100100.                        (12)

Another gate uses C=4096t+2143 and length 12. Both are outside the parent's
first valuation-bridge entrance at their displayed residues. The all-type
compiler, not a separate brute-force seed search, produces them.

The even-valuation escape C=2528 supplies

    (22754,2528) --4 steps--> (12800,158)
                  --2 steps--> (3200,119).

The last type is (27D-13,D). Its signed template is -40 -> -20 -> -10 -> -5,
so its three-step balanced endpoint is (400,404). The gap-four certificate
then merges. The complete H clocks are 14/14 and the endpoint is 38.

This lifts to the smaller-original-source certificate

    T^18(13483)=T^17(6741)=38.                            (13)

The old #125 selected return language is OUTSIDE at its H parameter 2528.
This example does have forward descent; no no-descent property is attached
to it. The next section gives infinite families where that stronger property
also holds.

# EG-005. All escape exponents and all ladder depths lift to original sources

## Every escape exponent

Fix s>=1. EG-003 applied to (a,b)=(s+2,2) supplies a progression of odd d
(the word has L>=a>=1) that merges (3^(s+2)d+2,d). Set C=4^s*d and prepend
(10). Therefore every s, however large, has an explicit progression of H
parameters with v2(C)=2s, i.e. previously discarded 4-adic escape inputs.
It is the exponent that is arbitrary; not every d at that exponent is covered.

For any chosen original first-odd-run length r>=2, impose by CRT

    4C+1 = 0 mod 3^(r-1),
    u=(4C+1)/3^(r-1), n=2^r*u-1, m=(n-1)/2.

The dyadic gate and this odd-modulus condition are compatible. u is positive
odd and the initial exit is hard. The parent entry is

    T^(r+2)(n)=H(C),      T^(r+1)(m)=C.

Appending the new words gives a genuine merger with 0<m<n/2. Every fixed
s and r yields infinitely many ordinary sources by adding the CRT modulus.
They are not one common source for all s or all r.

## Every successive companion-ladder depth

For j>=1,

    H^j(C)=9^j*C+(9^j-1)/4.

Take a=2j and b=(9^j-1)/4. Here c=(3*9^j+1)/4>4^j=2^a, so EG-003 gives
an explicit merger cylinder for (H^j(C),C) at EVERY j.

For any r>=2j impose

    4C+1=3^(r-2j+1)*u,  u positive odd,
    n=2^r*u-1,  D_j=(4^j-1)/3,  m=(n-D_j)/2.             (14)

CRT realizes the dyadic C gate with this divisibility. The original words
are 1^r 01 and 1 0^(2j-2) 1^(r-2j) 00, giving

    T^(r+2)(n)=H^j(C),    T^(r+1)(m)=C,    0<m<n/2.       (15)

Thus the parent ad hoc H-squared bypass is extended to a uniform gate
construction at every existing rung. For a fixed original n the allowed
ladder is still finite: j<=floor(r/2). No nonexistent rung is introduced.

## Uniform absence of forward descent on the entire displayed original arm

Let K be the number of appended original-arm steps after its first r odd
steps; it includes the two-step initial hard exit. It is finite and depends
on the chosen gate, not on its progression parameter. Require

    3^r >= 2^(r+K).                                      (16)

The first r odd steps strictly increase. Their last state is 3^r*u-1. Every
subsequent shortcut step retains at least half the preceding positive value.
Hence every remaining displayed state is at least (3^r*u-1)/2^K, and

    (3^r*u-1)/2^K - n
      = [(3^r-2^(r+K))*u+2^K-1]/2^K > 0.

Since 3/2>1, condition (16) is met by sufficiently large r for EVERY chosen
escape exponent or ladder depth. It is deliberately conservative, not an
optimal threshold.

Additionally impose u=2^(-r) mod3, through the stronger CRT condition

    4C+1 = 3^e*2^(-r) mod 3^(e+1),
    e=r-1 for an escape, e=r-2j+1 for a rung.              (17)

Then 3 divides n. Such n has only the depth-b pure ancestor 2^b*n: the odd
inverse (2n-1)/3 is not integral, and doubling preserves 3-divisibility.
There is consequently no smaller pure ancestor at any depth, in addition
to no forward descent anywhere on the displayed original arm.

For example the first odd H gate, lifted at r=21, gives

    n=18884853759,  m=9442426879,
    T^33(n)=T^32(m)=5588257271510,
    min_(1<=i<=33) T^i(n)=28327280639 > n.

This is not itself a 4-adic escape; it illustrates the same all-types lift
at ladder depth j=1. A genuine s=2 escape example is

    n=29884485524783103, m=14942242762391551,
    T^55(n)=T^54(m)=90758794836139935455,
    min_(1<=i<=55) T^i(n)=44826728287174655 > n.

Both sources are divisible by three. The full corpus supplies 64 such
original-root examples across s=1..16 and j=1..16, with two r choices each.

## A one-third companion on infinitely many ladder depths

When j=2 mod3, D_j is also 2 modulo 3, since D_j=1+4+...+4^(j-1). For the 3-divisible sources in (17),

    x=(n-D_j-1)/3

is positive odd, T(x)=m, and 0<x<n/3. Thus (15) plus the gate gives an
EQUAL-clock merger of n and x. This holds for arbitrarily large j in that
congruence class, with the same no-forward-descent bound. It generalizes
the j=2, x=n/3-2 special case. Ten such lifts are replayed in the corpus.

# EG-006. Composition, finite evidence, and the remaining quantifier

The implemented extension first runs the exact parent valuation-return
language. It preserves every parent success and its words. At an OUTSIDE
parameter it applies (10)-(11) and tests the three compiled affine cylinders
in declared order. A hit appends an equal-length pair of words to the
correct original arms; an earlier return may have exchanged their roles.
No new smaller-source inequality is asserted for an intermediate state.
Every prior original source and its independent arrival clock is retained.

On precisely C=1..65536:

| Outcome | Parent #125 language | Extended language |
|---|---:|---:|
| MERGE | 4366 | 4465 |
| OUTSIDE | 61170 | 61071 |
| BUDGET | 0 | 0 |

There are 99 additional certificates. This is a modest finite numerical
increment, not a large-density breakthrough. It is the automatic coverage
of arbitrarily many comparison TYPES that is the main new result. The
sample contains all positive C, including ones not congruent to 2 mod3;
that congruence is forced only at the FIRST least-counterexample entry,
not at every later return. These are procedure outcomes, not a convergence
census or a percentage of hypothetical counterexamples eliminated.

The supplied deterministic corpus also contains 12,300 gap cylinders
(three variants on 1..4096 and four large-integer gaps), 378 affine cylinders,
64 no-forward-descent original certificates, ten one-third lifts, and 8,998
eligible bounded controls for EG-001. Whole cylinders are checked by exact
integer affine identities and parity legality, not extrapolated from their
first few values. The separate verifier reconstructs actual signed/positive
paths and affine numerators and reconstructs the parent transition using
actual forward steps rather than its generator's closed formulas.

All outside/budget inputs are retained in the full-row artifact. Native
implementation diversity from one author is not independent mathematical
review. See the exact execution receipt for modes and corruption tests.
No complete-checkout root validator, remote CI, Lean build, or external
mathematical review is claimed.

## What this has NOT proved, and the next research target

The type normalization is total, but the success selector is not. For each
gap and each eligible affine type, we have supplied particular ordinary
progressions, not shown that every given parameter enters one. Increasing
the number of compiled gates cannot by itself prove that the exceptional
ordinary set is empty. Nor may the local rank in EG-001 be reset and applied
to the expanding old returns without a separate argument.

The next useful target is an entry theorem or companion-switch rule for the
FAILED congruences of the actual fixed original source. It should use the
finite-window contraction (1) and the exact transition between comparison
types to obtain either a successful gate or a common decreasing quantity.
A theorem about the transported exceptional parameters, rather than merely
another nonempty success cylinder, is what would promote this compiler into
a global argument. The current work supplies the gate construction and
physical interfaces for that task, not the missing universal entry theorem.
