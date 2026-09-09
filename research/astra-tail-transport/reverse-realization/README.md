# Low word rank is a backward certificate

**PROPOSED pending independent mathematical review. No complete Collatz proof.**
This is an addition-only continuation of PR105 at
`912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe`. Start with [PROOF.md](PROOF.md).

## The connection

The previous expanding-word rank can attain its minimum at a word that is
physically illegal FROM the source. The new theorem changes direction, without
changing the rank or assuming the illegal path:

> For every word w with multiplier at least 5/4, a component value at most n^2
> supplies a positive ordinary ancestor x<(4/5)n that physically reaches n.

Writing T_w(x)=(P x+A)/D and Z_w(n)=(P-D)n+A, the witness is

    x=(Dn-A)/P = n-Z_w(n)/P.

The low rank forces enough ternary divisibility for x to be integral; the
positive affine remainder bound forces x>0. This works for ALL such words,
not only the six phases previously studied, and does not require the component
to be a minimum. It certifies ordinary-value descent, NOT rho descent.

The rank also has the exact positive-orbit representation

    rho(n)=min(base components,
      3^(q_L(x))*g(n-x) over positive x<n with T^L(x)=n,
      2^L<4n and 4*3^(q_L(x))>=5*2^L).

Consequently every rho value through ordinary source N can be reconstructed
using O(N log N) physical shortcut states, instead of separately scanning the
whole word dictionary at each source. Bit complexity and valuation costs are
stated separately in the proof.

## Two quantitative gains for the SAME infinite-word rank

Keeping the exact progression modulus and counting long-word small sources
only once proves

    floor(sqrt(X))-1 <= #{n>=2:rho(n)<=X} <350sqrt(X),
    sum rho(n)^(-s) < infinity iff s>1/2,
    sum 1/rho(n)<14.

This improves the parent's 39/40 upper counting exponent to the sharp exponent
1/2. A separate positive summation gives the sharp ordinary-height tail

    1/(9N^2) <= sum_(n>N) 1/rho(n)^2 <77/N^2, N>=2.

These initial tails do not regenerate after arbitrary transport. The previous
12/2^48 residual belongs to another rank/operator/input and is not reassigned.

## A concrete odd family beyond the elementary rules

For every e=9 mod16, e>=25,

    n=(4*3^e-73)/17, x=(256*3^(e-4)-73)/17,
    T^6(x)=n with word 111010, x<(64/81)n.

Here n=19 mod36, its actual first three bits are 110, and its UNIQUE minimizing
word is 111010. The source has no elementary even, 10, inverse-1 or inverse-110
reduction from the specified normalizer. The backward word nevertheless works.
Its witness has rho(x)=(4096/81)rho(n), a LARGER rank, so one must use ordinary
value for the induction. The global-rank equalities use the parent's exact
minimum lemma; the inverse path and ordinary decrease are proved here directly.

A much smaller nonminimal-component example is 1351 --111010--> 1711.

## What was attempted for full closure

The backward rule, elementary forward reductions, and inverse-110 rule compose
into a total finite normalizer with strict ordinary-value decrease on every
successful move. It returns 1 or a precise residual; its physical two-source
certificate has O((log n)^2) total clock. It does NOT always return 1.

Residuals lie in 3,7,15,19,27 mod36; in particular EVERY n=3 mod12 is residual.
For every finite K there are ordinary n=0 mod3, n=-1 mod2^(K+2), for which
normalizing T^j(n) simply returns n for all 1<=j<=K. These are zero-clock
administrative echoes, not positive cycles. A successful final argument must
force genuine progress beyond them. No such all-source theorem is supplied.

| ID | Proven in the manuscript / boundary |
|---|---|
| ATT-301 | Universal reverse realization and exact positive-ancestor formula; batch rank algorithm. |
| ATT-302 | Sharp square-root rank counting, critical summability threshold, explicit tails. |
| ATT-303 | Two-sided initial ordinary-height tail for the enlarged dictionary. |
| ATT-304 | Total finite component normalizer and physical composition; residual may remain. |
| ATT-305 | Infinite odd illegal-minimizer family with a smaller ordinary ancestor. |
| ATT-306 | Arbitrarily long zero-progress echoes for the proposed iteration. |
| Q-ATT-301 | Every residual eventually has a strictly smaller normalized forward endpoint: OPEN. |

## Evidence and review

[Experiment](../../../experiments/X-ATT-004-reverse-realization/README.md): formal
word enumeration and a separately written positive-orbit reconstruction agree
on 4095 ranks and all 1688 qualifying source/word pairs in [2,4096]. Both verify
finite merging diagrams, four complete rank balls and adversarial controls.
The normalizer sends 184 tested inputs to 1; 569 inputs are already residual,
and the remaining inputs terminate at one of the residuals. These are labels
of this partial algorithm, not assertions of nonconvergence.

Both implementations have one author. Normal/optimized replays and twelve
resealed corruption tests are computational cross-checks, not independent
mathematical review. [Source and status record](SOURCES_AND_STATUS.md) distinguishes
new proofs, inherited estimates, and the remaining full-proof obligation.
