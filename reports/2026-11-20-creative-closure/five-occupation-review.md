# Independent review of coalescence and saturated capacity

**Verdict: VERIFIED at the stated local claim boundaries, OCC-001–004.**
No material mathematical defect was found in the frozen manuscript. Its
all-time entropy budget, first-hit partition, saturated Dirichlet bound,
two weight-family obstructions, and finite positive repair have the stated
scope. None supplies the missing all-source time-occupation upper bound.

Reviewer lane: `merger_completion`. The reviewed occupation manuscript and
production checker were written by a different lane. The independent
reconstruction below imports no functions from that production checker.

## Frozen objects

All paths are relative to the repository root.

| Object | SHA256 |
|---|---|
| `research/creative-closure-20261120/occupation.md` | `56ea718f7541a5206f721d73f41397c269c75c016a4d652f123bf54069160077` |
| `experiments/creative_occupation.py` | `0bded380f847cf7bfd64ee72ffbdc062d2e7995aa3f2591ab567023ff90cf1b1` |
| `reports/2026-11-20-creative-closure/occupation-report.json` | `8a901abc2d045c1a8db48362bfb0e63b09717446b0519ade9d3891859b77ec84` |
| `reports/2026-11-20-creative-closure/five-occupation-independent.py` | `009f2b340bc381ce37cb360113138aa32ed37203e62193051195358460a6bf73` |
| `reports/2026-11-20-creative-closure/five-occupation-independent-report.json` | `d74ae8c4ace6fe382b8652e71883294fc0ca7c5ce57960d9848b093315936c09` |

The imported finite-simple-path result was inspected in the exact local
copy of PR153 head `eb04a5d79020cefa0ba46794095b5766c5ff66a4`, path
`research/fixed-integer-descent/drift.md`, manuscript SHA256
`d73a93d8a803996bde7b15f33e307d28385c8ffe2f9b99f449dfea35140c3338`.
The inspected PR157 occupation interface is at head
`64361ecca770092d6c8242dc6211e38818af2e50`, path
`research/global-closure-20261120/transport.md`, manuscript SHA256
`5b1559d09ae81107416b44e97fd8b93a7a60d0f334746e3b2c94ab314d6c9649`.
The moving rank and quarter-safe return retain the PR152 pin and
qualifications explicitly given in those packets; this review does not
extend its verdict to unrelated claims in any of those PRs.

## OCC-001: original-source entropy and its exact failure of payment

The initial entropy bound is correct. The comparison function
\(2(\log2+\log x)/x^2\) decreases for \(x\ge1\), and its integral
there is \(2+2\log2\). Each original atom remains contained in its
deterministic carrier, including after absorption into the cemetery.
The carrier mass cannot decrease along that atom's path. Consequently
the pointwise information is nonnegative and increasing. Its weighted sum
equals the entropy drop by regrouping original sources at their endpoints;
the initial finite entropy dominates the regrouping absolutely.

For fixed mass \(m_0\), entropy is at least \(-m_0\log m_0\), giving
the finite total information budget. This is an entropy statement about
actual deterministic coalescence and requires no distributional reset.

The whole-source tail treatment is also correct. Summation by parts gives

\[
\sum_{n>M}\frac{\log(n(n+1))}{n(n+1)}
\le\frac{2(\log(M+2)+1)}{M+1}=E_M.
\]

The verified bound \(m_0<1/3<e^{-1}\) makes \(-t\log t\) increasing
over every carrier mass under consideration. Entropy contraction of the
omitted input and subadditivity therefore put each full entropy between
its retained-source entropy and that value plus \(E_M\). The difference
of two such errors lies in \([-E_M,E_M]\), so an entropy **drop** needs
one \(E_M\) error on either side, not two. The reciprocal-psi charge has
the separate error \(1/((M+1)\psi_*)\). Both arguments retain omitted
original atoms that later merge into small retained endpoints.

The independent reconstruction uses all 23,517 unsafe originals through
65,536, pushes their masses through eight actual returns, and calculates
the ninth push for the entropy drop. It obtains the rational whole-source
gap lower bound

\[
\ell_8-J_8\ge
\frac{90231186155081932485427645197981887}
{340282366920938463463374607431768211456}
>0.000265165623.
\]

Thus the claimed unit-coefficient one-return payment really fails for the
specified full input. The conclusion does not refute a larger coefficient
or a source-specific amortized estimate. The separate full-support mixture
argument is valid as well: its entropy tends to zero, whereas the positive
first charge at the actual one-return source 3 persists. That refutes a
coefficient uniform over all positive full-support inputs, not a comparison
restricted to the fixed \(f_0\).

## OCC-002: nonperiodic first-hit partition

For a nonperiodic endpoint \(y\), each source reaching it, other than
\(y\) itself, has one predecessor at its first hit. Two predecessor
basins cannot overlap: a deterministic source path visiting both would
visit \(y\) twice and make \(y\) periodic. The source \(y\) itself
cannot lie in such a predecessor basin for the same reason. This proves
the stated disjoint original-source partition and its capacity identity.

For real \(p\ge1\), the inequality
\(\sum a_i^p\le(\sum a_i)^p\) extends from finite subsets by monotone
convergence. Subtracting the strictly positive source atom gives the
strict pointwise inequality in the manuscript. Periodic points are
correctly excluded from this inverse identity, and summability of the
unweighted power \(C^p\) is correctly left unproved.

## OCC-003: saturated spatial mass, including cycles

The passage from a finite simple shortcut path to the distinct values of
one full orbit is valid. If an orbit repeats, all of its distinct values
occur in its preperiod and one cycle traversal, which is a finite simple
listed path before the first repeated endpoint. If it never repeats,
every finite subset of its values lies in a finite simple prefix. The
distinct unsafe return endpoints are a subset of these actual shortcut
values.

Apply the pinned translated-interval occupancy bound to each source's
distinct value set and use nonnegative summation over the original
weights. This gives the claimed interval capacity bound without deleting
periodic states and without asserting a whole-basin density estimate.

For the Dirichlet moment, layer-cake gives

\[
\sum_{y\ge L}\frac{C(y)}{y^s}
=s\int_L^\infty t^{-s-1}\sum_{L\le y\le t}C(y)\,dt
\le\frac{10s m_0}{s-29/30}L^{29/30-s}.
\]

At \(s=1\), the constant is \(300m_0\le150\), exactly as stated.
The recursive imported exponent likewise permits every \(s>h_*\) by
choosing a strict intermediate exponent. The bitlength compactification
is summable because \(C\le1/2\) and \(2^{-c b(y)}\le y^{-c}\).

These bounds count an original atom once per distinct endpoint. They
provide no bound for the number of returns to that endpoint. In
particular, the cycle-inclusive spatial bound does not itself exclude a
cycle. The manuscript preserves this essential distinction.

## OCC-004: whole-parameter failures and the finite repair

The independent checker reconstructs acceleration by maximal repetitions
of the literal word \(1^a0\), using direct shortcut operations. It does
not use the production checker's affine endpoint formula. It computes the
rank over extra modes as an additional bounded check of the compact mode
menu and then enforces the quarter-safe guard on each internal return.

For all unsafe originals through 8192, exact rational source weights are
accumulated once at every encountered endpoint. All 2941 originals reach
1 within 37 returns. The two capacity intervals at 31 and 121 match the
production report **exactly as rational numbers**, including the full
uncomputed-source error \(1/8193\). The reconstructed return path is

\[
31,121,91,103,175,445,334,167,319,1822,911,244,46,23,1.
\]

Using the lower capacity bound at 31 and upper bound at 121 independently
verifies

\[
C(31)^2\,121>C(121)^2\,31,
\qquad C(31)^5/C(121)^7>5000.
\]

Since \(121/31>1\), the first inequality proves failure for every real
\(s\ge1/2\); this includes the entire summable exponent range supplied
by OCC-003. The bitlengths 5 and 7 turn the second inequality into the
claimed failure for every real \(c>1\). A single incoming edge suffices
to violate each supersolution inequality.

The proposed repair is an actual positive finite resolvent on the
certified 121 path. There are thirteen nonabsorbed states, each receiving
mass 150. Direct pushforward gives
\((I-H)V=150\delta_{121}\), and \(\|V\|_1=1950\). The bound
\(\|w_1\|_1\le150\) dominates the original defect at 121, so this
patch removes that defect and leaves every other defect unchanged.
The missing finite total budget for all remaining repairs is explicitly
retained; neither termination of an unproved orbit nor summability of
infinitely many patches is assumed.

## Actual execution and evidence boundary

This review executed:

```bash
python -X utf8 -B experiments/creative_occupation.py --compare reports/2026-11-20-creative-closure/occupation-report.json
python -X utf8 -B reports/2026-11-20-creative-closure/five-occupation-independent.py --output reports/2026-11-20-creative-closure/five-occupation-independent-report.json
```

The production comparison returned exit 0 and `PASS`, with 27,771 actual
return edges, 3475 flow identities and 10,425 convex-power checks. The
independent command produced the pinned `PASS` report reproduced above;
its terminal completion receipt was not retained after session
interruption. The report is written only after all independent assertions
have succeeded. It can be regenerated using its `--compare` interface.

Optimized-Python execution was not performed by this reviewer. The author
reported normal and optimized comparisons; those reports are not counted
as this reviewer's independent execution. The publication runner includes
normal and `-O` comparisons of the frozen production and independent
reports and records those separate receipts.

The independent logarithm calculation uses twenty terms of the exact
rational atanh series after dyadic range reduction. For
\(0\le z\le1/3\), its positive remainder is bounded by
\(2z^{41}/(41(1-z^2))\); only the final rational bounds are rounded to
the binary scale \(2^{128}\). It therefore differs from the production
integer-series implementation while preserving rigorous outward bounds.

The finite reconstruction verifies the reported numerical obstruction and
physical witness paths. The all-parameter entropy, partition, Dirichlet,
and parameter-range conclusions are justified by the written arguments
reviewed above. The verdict supplies no global upper estimate for
\(\mathcal G_N(f_0)\), no universal supersolution, and no resolution of
Collatz.
