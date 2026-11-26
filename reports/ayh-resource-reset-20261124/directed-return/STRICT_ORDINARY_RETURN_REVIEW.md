# Independent reconstruction of the strict ordinary directed return

Reviewer: interior-interface worker, 2026-11-24. Scope: final “Strict sublinear return” in `BOUNDED_DIRECTED_ELEVEN.md`, SHA-256 `a9af55e7ec85e8f39184815f77109fb8be3bfd11a232a3f828467e6cc345b2e8`, supplemented below by a sharp-entropy fixed-factor estimate. Verdict: **VERIFIED as a written deduction conditional on the separately checked finite directed substitutions**. The full 116-motif enumeration is outside this review.

Let \(k=\lfloor\log_2X\rfloor\). For any parity word of length \(k\) with \(p\) odd steps, the ordinary shortcut gives \(T^k(n)=3^p2^{-k}n+E\), where \(0\le E\le\tfrac12\sum_{i=0}^{k-1}(3/2)^i=(3/2)^k-1\). The parity word map permutes the residues mod \(2^k\): from either lift of a length-\(j\) prefix one obtains opposite next bits because the native high slope is odd. The same holds for \(3x\) on the original \(x\) grid. A cover of the octave by at most a fixed number of periods and a union bound give both tails, independently of any dependence between these rays.

At the threshold \(p\le 3k/5\), the Chernoff tilt is \(3/2\). The exact inequalities \(3125^{10}<2^{49}108^{10}\), \(3^{15}<2^{24}\), and \(3^5<2^8\) give an original exception \(O(X^{49/50})\), both heights \(O(X^{24/25})\), and intercept \(O(X^{3/5})\). For \(p\le94k/149\), use tilt \(94/55\). Fresh integer comparisons verify
\[
 3^{94}<2^{149},\qquad
 149^{20\cdot149}<2^{19\cdot149}\,94^{20\cdot94}\,55^{20\cdot55}.
\]
The right-minus-left differences have bit lengths 143 and 21,502, respectively. The original exception is \(O(X^{19/20})\) with endpoint power \(\theta=(94/149)\log_2 3=0.9999092286\ldots<1\). Both are two-ray, fixed-clock estimates.

At a retained tripling defect, one of these endpoints has the color distinct from \(f(1)\); it exceeds 1. Inspected PR 146 at `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/REVERSE_BASIN.md`: positive ordinary edges in either direction and forward triplings only at odd multiples of three lead from every \(n>1\) to \(n'\le9n/10\) in at most 61 steps. Iteration reaches 1. At the first change to \(f(1)\) some forward additional edge starts at an odd multiple of three, of height at most a fixed multiple of the original endpoint: intermediate values grow by at most a universal factor per step, and every later batch begins smaller. PR 197 `NonunitExit.lean`, `physical_chain` and `directed_successor`, gives a \(1\pmod {16}\) edge with the same ordered labels and height at most a fixed multiple. Applying the finite substitution under review gives a literal \(11\pmod {32}\) edge and, by the prior exchange, a \(17\pmod {48}\) edge with this same orientation and the advertised height bounds.

**Fixed-factor refinement.** Write \(s=\log_3 2\), \(h_2(s)=-s\log_2s-(1-s)\log_2(1-s)=0.949955527188\ldots\). For every prescribed fixed \(0<q<1\), apart from
\[
          O_q\!\left(X^{h_2(s)}/\sqrt{\log X}\right)
\]
original starts in an octave, each true tripling defect has an actual prescribed reverse directed witness in each of the two residues at height at most \(qX\) for all large \(X\). Choose an integer \(C_q\) so a fixed multiple of \(6\cdot3^{-C_q}\) is smaller than \(q/2\), with the multiple covering the directed height transfers above for either residue. Require both odd counts \(p\le sk-C_q\). Both ordinary heights are at most \(6 X3^{-C_q}+O(X^{\log_2(3/2)})\), as \(3^{sk}=2^k\). At the first excluded integer \(p=sk+O_q(1)\), Stirling's formula gives \(O_q(2^{kh_2(s)}/\sqrt{k})\) words. Since \(s>1/2\), the successive binomial terms thereafter decrease geometrically, uniformly for large \(k\). This proves the claimed original exceptional count without a resampling step.

The resident one-ray no-descent theorem in `research/integrated/exceptional-mass/README.md` counts starts never dropping below themselves over any of the first native clocks, with an explicit \(19/20\) bound and the dyadic entropy rate. Here the conclusion concerns a pair at one clock followed by a directed comparison witness. Sharpness of the entropy count for the chosen parity threshold does not prove optimality for failure to find such an ordinary witness. Each exceptional exponent still exceeds the \(.84\) population exponent and different original sources can select the same small witness.
