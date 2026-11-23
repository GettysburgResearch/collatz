# Independent review of the actual all-gap collision argument

23 November 2026. Reviewer: checkpoint18 cycle lane.

**Disposition: the new finite arguments and the stated asymptotic
consequences are valid, conditional where indicated on the supplied
fixed-block entropy limits.** This review does not certify the upstream
stationary extraction, prove the missing collision upper bound, or claim
Lean verification.

## Frozen scope

| Artifact | SHA256 |
|---|---|
| `ACTUAL_ALL_GAP_COLLISIONS.md` | `82b0bf20b7a315e0102692eddae3058f84d8ec74a983be057669c0b55f795caa` |
| `check_all_gap_collisions.py` | `fc1957cc6c71dc541447d80596f250d7d15a517dd52189b1ae55003cf2bd671d` |
| `all-gap-collision-controls.json` | `8c9bee680b369e9d726dd25a9e157e65a9282f589009cecc37383333a084bce4` |
| `SOURCES.json` | `a84f063ac601ad523f3e76ff71bd25243adcdd641c43d8d8de620bed21076e4d` |
| `collision-execution.json` | `877fbb38d9be54afd00aee1591eafb9a890d1cb9cde6de40c4dd148649c11df7` |

The full note, final checker source, result, source ledger and execution
manifest were read. The manifest records normal and optimized executions
with identical output, 37,627 finite checks and four negative controls.
This reviewer did not add another execution or perform a historical audit
of the frozen upstream papers.

## Finite entropy and occupation

The sliding-block estimate (6) retains the correct sampling factor.
Every offset k-block marginal is sampled at N-m consecutive positions
within the N-k positions of the full k-word law. Concavity therefore
bounds its entropy by (N-k)/(N-m) times the latter entropy. Covering all
m coordinates with ceil(m/k) such blocks and using subadditivity proves
the displayed finite bound; overlapping final blocks cause no problem.

For a fixed m-word, the endpoint residue modulo 3^m is fixed by the full
carry identity. Injectivity of the ordinary orbit makes the K endpoints
below X<3^m distinct, hence their m-words distinct. Conditional on this
low-endpoint event the word law is uniform on K words. Concavity gives
K log K <= (N-m)H_(N,m), including K=0 with the stated convention.

Theorem 1 now requires only the stated convergence H_(N_i,k)->H_k at
one fixed k. At m_i=floor(B log_3 N_i)+1, the right side of (14) tends
to alpha B. On a subsequence where K_i/N_i tends to a positive limit,
log K_i/log N_i tends to one; a zero limit is immediate. Omitting the
first m_i=O(log N_i) times changes density by o(1). This proves both
occupation conclusions, including alpha=0. Applying the positive
occupation bound for each B<1/alpha also proves the maximum-height
consequence (16). No convergence of growing-block entropies is assumed.

## Complete arithmetic constraints

The reduced anchor identity (18) is exact. The full determinant D and
its common divisor g with the carry are both odd and prime to three.
Thus g divides the actual endpoint difference, and dividing by g loses
neither its 2-adic nor its 3-adic valuation. The endpoints are odd, so a
collision modulo 3^m supplies the extra factor two in (20). The height
bound follows from the nonzero integer b*q_i-c, with absolute values
retained when the anchor is negative.

The exact-valuation source cylinder needs the full modulus 2^(A+1),
as in (23). To check intermediate valuations, split the complete carry
at any proper prefix. The nonempty suffix carry is odd; reduction of
the final congruence modulo the prefix's 2^(partial_gap+1) makes that
intermediate quotient odd. The final quotient is odd by (23) itself.
The return congruence modulo 3^m is then equivalent to D*q=C, with D
invertible there. CRT gives exactly one class modulo 2^(A+1)*3^m.
The note correctly does not turn its interval density into an orbit
sampling law.

## Location of the forced collision mass

For (27), merging word atoms into endpoint-residue atoms increases
collision probability, and the order-two entropy is at most Shannon
entropy. Passing from the retained tail law to the complete endpoint
law contributes the square of its mass, (1-m/N)^2; the remaining cross
terms are nonnegative.

For the strict-deficit case, (6), m_i=O(log N_i), and the fixed-k limit
give H_(N_i,m_i)/m_i <= h_bar eventually. Consequently the full ordered
pair count is at least c*N_i^(2-h_bar/Phi)=c*N_i^(1+beta). At most
N_i*(2L_i+1) ordered pairs have separation at most L_i. If
L_i=o(N_i^beta), this contribution is o(N_i^(1+beta)); subtracting it
proves Theorem 2. This includes the diagonal and uses the complete
pair-gap sum. It does not assume that colliding endpoints have identical
words, and it does not replace a changing anchor by a fixed one.

## Evidence and the remaining opening

The checker implements the finite entropy comparisons by exact rational
exponentials of entropy, avoiding floating-point estimates. It retains
all actual gaps in its finite prefixes, reduces the rational anchors,
checks the full CRT cylinder, and checks the all-gap decomposition.
Explicit `require` calls raise exceptions rather than using Python
assert statements, so their conditions remain active under optimization.
Its fixtures are finite distinct prefixes, not asserted escaping orbits.

The fixed-source stationary extraction, convergence of fixed-block
entropies and harmonic-flow comparison are source-qualified inputs in
the note. They were not independently reproved here. The finite bounds
(6), (8), (18)--(27) are separately reconstructed above; Theorems 1 and
2 follow from them with the precisely stated entropy hypotheses.

The necessary all-gap collision upper estimate remains open. Neither
the growing ordinary source heights nor the heights of the changing
anchors receive a total budget from the new inequalities. Theorem 2
shows why a short-gap estimate alone does not control the required sum.
The critical diagonal limit and the fixed-resolution-then-limit target
remain distinct. No step in this review supplies either missing upper
bound or excludes the critical iid branch.
