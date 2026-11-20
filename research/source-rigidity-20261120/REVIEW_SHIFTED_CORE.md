# Independent review of shifted-core transitions and the finite horizon

**Verdict: VERIFIED, with the external and optional repository dependencies
retained exactly as stated.** This is an independent mathematical
reconstruction by the parent agent, not a human referee report, a reproof of
the external S-unit theorem, or formal verification. It does not extend to
unrestricted Collatz closure.

## Frozen objects

| Object | SHA-256 |
| --- | --- |
| `SHIFTED_CORE_TRANSITIONS.md` | `f53846e08e1522058797c6cab57111cf9c7ed4385f39b0e055ab05264f7acb71` |
| `CLOSURE_ATTEMPTS.md` | `a81b8a9c9edb41f1dd563d5015bfb0637da85a286cdaa89053f9596aa46bc56c` |
| `BOUNDED_CORE_HORIZON.md` | `48b87b072ebd2a8e31f6767efd300d42df3599c10efdd9c82543eae2d266dec8` |
| Author checker | `c182efabeaf6a0e61cf1337732add443bee98ca519b8492296103cd42800bfa5` |
| Author report | `557636dfb76748100aaaeb6972aafc93739aa40112dfa3521d479aa2d159263e` |
| Independent `check_shifted_core_review.py` | `28f59efb2217812b1696173e55338b1f58ca7632d7728d5e9894a2b259640ab9` |
| Independent report | `d036975e1735c86ca2ded180ddba54ed8d653dff28724bb29622f433d5ebe4c3` |

The review applies only to these bytes. The publication manifest maps them
to the eventual commit. No verdict is inherited by later edits.

## SC1: fixed coefficients, exact degeneracy, and injectivity

I reconstructed the ordinary transition using literal shortcut steps, with
\(m=n+1\), \(m'=U(n)+1\), and \(a=v_2(3n+1)\). The relation

\[
2^a m'=3m+2^a-2
\]

is exact. If the fixed prime pool contains 2 and 3 and the two cores are
\(q,q'\), write \(m=qu\), \(m'=q'v\). The vector
\((2^{a-1},u,2^{a-1}v)\) consists of units for that one fixed set of
places, with rational coefficients \((1,3q/2,-q')\).

The potentially delicate point is coefficient uniformity. I independently
opened Evertse's author-hosted primary paper
<https://pub.math.leidenuniv.nl/~evertsejh/95-decforms.pdf> and inspected
Theorem 3 on printed page 7, including a page image. It allows arbitrary
nonzero coefficients in the number field. Thus the primes in \(q,q'\)
do not enlarge the place set. For three variables and \(s\) finite primes,
the stated constant \(B_s=(9\cdot2^{35})^{27(s+1)}\) has the correct
normalization. The theorem bounds the number of solutions, not their
heights.

For \(a\ge2\), the two signed differences are
\(2^{a-1}(1-m')<0\) and \(1-2^{a-1}<0\); the positive pair is
strictly positive. Single terms and the full sum are nonzero. Hence all
seven nonempty subsums meet the source hypothesis. At \(a=1\), precisely
the latter signed pair vanishes; the exclusion is essential.

The encoding is injective because its second coordinate and fixed coefficient
\(q\) recover \(n\), and its first coordinate recovers \(a\). There is
no hidden count of residue classes, denominator factors, or repeated visits.
SC1 is valid for distinct ordinary transitions with arbitrarily large \(a\).

## SC2--SC3: what finite transition count actually excludes

Assigning distinct defect edges to their ordered core pairs gives
\(D_N\le B_sK_N^2\). The endpoint at time \(N\) must be included in
\(K_N\), as the author does. A simple prefix supplies distinct source
states, which is the exact reason occurrences can be counted here. Repeated
laps of a positive cycle would not satisfy that distinctness premise.

There are only finitely many distinct defect edges with both endpoint cores
at most any fixed \(H\). Along a nonperiodic ordinary orbit this proves
that the maximum of the two endpoint cores tends to infinity along defect
times. It does not imply that every single core tends to infinity.

For any ordinary even shifted value \(m\), valuation one is equivalent to
\(v_2(m)\ge2\). Each such step replaces \(m\) by \(3m/2\), reducing
its finite binary valuation by one. Consequently an infinite ordinary tail
cannot avoid defects forever. Combining this fact with the finite edge count
proves SC3's eventual-periodicity conclusion for a fixed finite core family.
It does not exclude a nontrivial finite cycle.

## Elementary clock and SC4

The estimate \(m'\le3m/2\) holds for every positive even \(m\) and every
actual exponent. If \(R_k\) is the time immediately after defect \(k\),
then

\[
R_{k+1}=R_k+v_2(m_{R_k})
\le(\log_2 3)R_k+\log_2m_0.
\]

The initial interval is handled by the same formula with \(R_0=0\).
The next defect has not completed among the first \(N\) transitions, so
\(N<R_{D_N+1}\), with a strict inequality. This proves the author's
floor in equation (16), as well as the integer conservative estimate
\(N<\ell(2^{D_N+1}-1)\).

SC4 substitutes \(D_N\le B_sK^2\) at the specified integer horizon.
If neither repetition nor a new core occurred, its strict clock inequality
would say \(H<H\). The endpoint conventions, initial exit at zero, and
\(K\ge1\) restrictions are correct. The sharper symbolic ceiling is
also valid, including when its argument is an integer. The comparison with
the fully integer horizon follows from the geometric sum for
\(1<\log_2 3<2\).

Thus this is a genuine finite alternative for one fixed ordinary source.
The bound is far too large to represent an executed computation. Exiting
the finite core family is not numeric descent, and a repeated state could
belong to a hypothetical nontrivial cycle.

## Optional PR145 implication: verified application, retained source status

I reopened the full `research/pointwise-run-defects/COMPRESSED_DESCENT.md`
at PR145 commit `dd245a712f985909f541590e3f6c179b7ba011e4`, including its
final section on a growing number of powered pieces. Its displayed bound
is exactly the one quoted in the new proof. Its p-adic Subspace-Theorem
dependency and PROPOSED, ineffective status remain visible.

A defect contributes an odd letter followed by a nonempty zero block;
joining adjacent odd letters yields at most \(2D_N+1\) constant-letter
blocks, each with a one-letter base word. Thus the base/gap budget is
\(B=k\), not the sum of the repeated lengths. The expanded shortcut path
is simple on a nonperiodic orbit, and its physical length is at least
\(N\). Selecting \(\eta\) after a proposed bounded ratio
\(D_N/\log N\) gives the claimed contradiction. The derived
super-square-root core count is a valid conditional application of that
frozen source, not a new unconditional proof of the source theorem.

## Closing ledger and new-core example

The gcd relation bounds retained factors only. In the explicit family
\(n=2\cdot3^{2k}-1\), the odd valuation is exactly two, and the outgoing
shifted core is \((3^{2k+1}+1)/4\). Restricting \(k\) to multiples of
the orders of 3 at the extra primes makes this core congruent to one at
every such prime. It therefore avoids the prescribed pool without needing
its factorization. This refutes precisely the proposed one-step bound by
incoming core and division cost; the original source changes with \(k\).

The shifted approximation identity in the closing ledger retains the full
outside-prime core and the common-time relative error. It does not remove
the unknown algebraicity or power saving. The growing-prime argument
legitimately chooses one pool after seeing an entire finite prefix, while
charging its increasing cardinality in \(B_s\). None of these calculations
produces a conflicting upper bound on accessible cores of one infinite
ordinary orbit.

## Independent finite evidence

The reviewer program imports no author code. It constructs each odd step
through literal shortcut operations and separately factors shifted values
over two named pools. Normal and `-OO` runs produced byte-identical reports.
It completed:

- 1,014 pool/transition checks on 507 positive odd sources;
- 506 nondegenerate defect checks and 508 exact exponent-one degeneracies;
- 1,854 literal valuation-one run edges, with division exponents reaching
  1,026 in the independent controls;
- eight complete simple-prefix controls, checking the integer clock and
  injectivity of the unit-equation encoding;
- six local new-core examples, with separate pool-avoidance, cycle-occurrence,
  terminal-core, and integer-constant controls.

These checks support the algebra and domains. They do not computationally
verify the astronomical S-unit bound, the external theorem, the limiting
claims, or the unrestricted Collatz conjecture.
