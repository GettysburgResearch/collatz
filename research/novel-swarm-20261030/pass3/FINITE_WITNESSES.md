# A finite witness theorem for binary linear Collatz invariants

**PROPOSED; self-audited only.** This concerns source-indexed invariants, not
parity itineraries and not decreasing rank functions. It supplies an explicit
finite edge bound absent from pass 2's existential search.

Let F be any field and d>=1. A binary linear model is

    f(n)=u M_(b_l)...M_(b_0) v, n>0,

where b_l...b_0 are the canonical most-significant-first binary digits of n,
u is a row, v a column, and M_0,M_1 are d by d matrices over F. Set
T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n.

## W1. Any failure of invariance has a small source witness

If f(T(n))=f(n) fails anywhere, it fails at a positive ordinary source

    n < 2^(4d+1).                                    (1)

This finite identity-test bound does not rely on the Collatz conjecture or
on pass 2's rigidity theorem. It follows from explicit linear transducers.

Split invariance into the even and odd identities

    f(2k)=f(k), k>=1;
    f(2k+1)=f(3k+2), k>=0.                           (2)

The k=0 odd case is f(1)=f(2), already tested by the k=1 even case.
Read k's digits least-significant first, multiplying a column by the current
M_b on the left. This gives the stipulated most-significant-first scalar
product at completion; no leading zeros are added to an ordinary input.

**Even lane (dimension d).** Start at (M_0-I)v, use transition M_b, and
finish with row u. This evaluates f(2k)-f(k).

**Odd lane (dimension 4d).** One d-block starts at M_1 v to evaluate the
2k+1 arm. Three d-blocks for carries c=0,1,2 evaluate 3k+2; initialize v in
carry 2 and zero in the other two. On an input bit b, transform the first
block by M_b. On carry c, compute

    e=(3b+c) mod 2, c'=floor((3b+c)/2),

and send M_e times that block to carry c'. Add contributions when their
carries coincide. The carry set is closed for b in {0,1}. At completion,
subtract the three carry blocks using respectively the rows

    u, u M_1, u M_1 M_0,

which flush the remaining canonical digits of 0,1,2. This exactly computes
f(2k+1)-f(3k+2). For k>=1 the last processed input bit is 1. The output
3k+2 has no spurious leading zero: on the last bit c=0 gives output bit1
and carry1, c=1 gives bit0 and carry2, and c=2 gives bit1 and carry2.
The flushed positive carry is always retained.

Every canonical k is a freely chosen low-bit word w followed by the final
1. Fold that final transition into the terminal row of each lane. A scalar
linear system of dimension m, with initial column z, is identically zero
iff its row annihilates span{M_w z:|w|<=m-1}. Indeed these increasing reachable
spaces start at dimension at most one, and any equality at a stage makes
the space stable under both transitions forever. If z=0 the assertion is
immediate. Thus a nonzero system has some |w|<=m-1 with nonzero output.

For the even lane, k<2^d, hence n=2k<2^(d+1). For the odd lane k<2^(4d),
hence n=2k+1<2^(4d+1). This proves (1). No bound is claimed optimal.

## W2. Every nonconstant model has such a violated edge

Pass 2, R4, proves that every finite-dimensional binary linear Collatz
invariant over a field is constant. Its exact dependency is

    PR140, c8a5f1a391a10ef4927383e472bceebb2b04c5e7,
    research/novel-swarm-20261030/pass2/RIGIDITY.md, R1--R4.

That proof combines the credited finite-family merger compiler, positive
inverse-ladder cone access, and finite-dimensional observability. It remains
PROPOSED pending independent mathematical review; this pass does not upgrade
its status. Combining it with W1 gives

> Every nonconstant d-dimensional binary linear model over any field has
> a literal Collatz-edge violation at a source n<2^(4d+1).

Thus checking every edge below that explicit cap is a finite universal
invariance test for that model class. This is not a finite test for Collatz:
there is no finite-dimensional representation of its convergence indicator
supplied here. The bound concerns one supplied representation, not arbitrary
unknown sequences.

## W3. Exact span search avoids enumerating the exponential interval

Over an effectively computable field, breadth-first reachable-span search
retains at most m linearly independent columns, with words producing them.
Check the output on the initial column and on the two children of each
retained column. A nonzero output returns a concrete word and therefore a
literal integer witness n. If all outputs vanish and both children of every
basis column lie in its span, the entire lane vanishes. There are O(m) matrix
applications and O(m^3) elementary field operations using dense arithmetic;
this is NOT a bound on bit complexity for arbitrarily large rational
coefficients or expensive field operations. Witness words have O(d) bits.

A closed-span certificate must verify the initial column, all transition
closures, and annihilation, not just record a list of sampled states. The
implementation additionally certifies a constant outcome directly, using
d+1 dimensions for f(k)-c and final canonical bit1, rather than using R4 as
a black-box acceptance rule. The verifier reconstructs each basis vector
from its supplied word and checks linear closure with a different elimination
implementation. Edge witnesses are evaluated using direct MSB row products,
not the producer's carry system.

## Executed examples and exact limits

The test suite covers all labeled representations of dimensions 1 and 2 over
F_2, seeded higher-dimensional representations over F_2,F_3,F_5, nilpotent
models, and models with hidden unreachable dimensions: 4,300 in total.
It returns 1,509 edge witnesses and 2,791 invariant/constant outcomes.
There are 8,448 separate carry-closure comparisons with literal evaluation.

For the nilpotent control M_0=I, M_1 e_j=e_(j+1), v=e_1, u=e_d^T,
the d=48 run finds the actual violated edge at

    n=187649984473769

after retaining 179 basis columns in the violating lane. This is an exact
finite-field result, not a scan of all smaller sources or a claim that this
is the least violation. The selected exported corpus has 13 edge witnesses
and 20 closed-span constant certificates; every one is independently
reconstructed by the companion verifier. The full 4,300-model producer
census is not independently re-enumerated by that verifier.

Normal parallel, normal serial and optimized producer runs agree exactly.
Same-author implementation diversity is not independent mathematical review.
The dimension bound is a proved all-model claim; the enumerations are bounded
implementation checks. No automaticity, algebraicity, finite binary rank, or
universal convergence of the actual Collatz indicator is established.
