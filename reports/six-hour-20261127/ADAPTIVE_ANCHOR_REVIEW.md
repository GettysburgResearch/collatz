# Independent review of the simultaneous ternary-anchor bound

Review boundary: the four SHA-256 files in the table, after the first PR 200 checkpoint at 07ae08382588992c1b7f7a60cd331a6647177495. These files were supplied outside that commit. Review applies to these bytes and the explicitly repaired theorem statement below.

| File | SHA-256 |
|---|---|
| ADAPTIVE_TERNARY_ANCHORS.md | 157c633d00ed128e5b870dfdaa0591ff5d81710062baeb20e387f7696204f5cc |
| RationalAnchorDiscrepancy.lean | 64458782e42648610c1ebc108e1a1cf7c105c86c71c630886dc5dadb7db2dbc7 |
| check_adaptive_anchors.py | e817d623124914762b628d571ea08fe043139719f87ac9475c989fdc7bf256cc |
| ADAPTIVE_ANCHOR_CONTROLS.json | 8c48a341864c46db37b330f20ffe699325d723733b8eaeac1b901a2de273c156 |

The corrected integrated ADAPTIVE_TERNARY_ANCHORS.md has SHA-256 5334bbacc71d3564b19f00490483edc6e588772ccc0f3008540112f5cdf5f086. A byte comparison confirms that its only change is the quantifier repair below. The original is preserved separately under reports/six-hour-20261127/source-originals.

## Claim verdicts

* **Theorem 1, VERIFIED WITH FIXES using Yu's published Theorem 1.** Replace “let A contain all positive rational anchors of height at most H” by “let A be the set of all positive rational anchors of height at most H.” Literal inclusion admits an unbounded extra anchor. Set n=H=1 and add 3^s−1 to the singleton ball. Every clock has state 1 and score at least s. Under the corrected definition every nonempty subset of the ball inherits the same upper bound. The signed extension requires a nonzero displacement at the start of the proposed all-exact interval; a start exceeding H suffices.
* **Finite functional-graph compiler, VERIFIED.** The original nested residues argument covers arbitrary stopping points and entrances. An independent size-of-subtree proof is given below.
* **Theorem 2, VERIFIED deduction from SOURCE-QUALIFIED external statements.** Weaver Paper 15/v2 (A1) and (C6) have the asserted adaptive uniformity and charge the sum of division exponents. No independent review of the Evertse–Ferretti proof chain is claimed here. The source only supplies a lower bound for a stopped word, and the frozen theorem correctly checks the stopping condition. The asserted clocks lie in a prefix or around one period.
* **Lean, finite interface only.** The file contains eleven local declarations, including the private count inequality. The signed discrepancy identity, its divisibility, matching-run integral transport, the two dyadic guards, closure equality, physical exponent, forced discrepancy and signed displacement transport are finite algebraic statements. I rebuilt the unmodified source in a separate directory at the repository Lean and Mathlib pins, with automatic implicits off and warnings treated as errors. Its eleven axiom reports contained only standard kernel axioms. Independent signed-score and alternate path-code controls also ran identically under normal and optimized Python. Yu, anchor maximization, the analytic clock applications, graph compilation and Paper 15 are written components.

## Independent reconstruction

Write x for the current positive odd ordinary integer, y for the next, and use q,v>0 in the two chosen reduced anchors t=p/q and u/v. The relation 2^e y=3x+1 gives

    2^e q u−v(3p−q) = 2^e q(vy+u)−3v(qx+p).

For denominators divisible by three, a reduced numerator is a ternary unit and the score is −v₃(q). All remaining denominators give nonnegative scores (including infinity in the signed extension). Thus the maximizer can use unit denominators. If every member of a separate finite subfamily has nonunit denominator, every score is negative and the upper bound is immediate. For unit denominators write a=v₃(qx+p), b=v₃(vy+u). At a nonzero residual at least one score is finite, and m=min(a+1,b) is a nonnegative integer with 3^m dividing the residual. In particular min(a,b)≤m, even if one score is infinite.

Let A=qu and B=v(3p−q). B is a ternary unit, including for signed p, because 3∤qv. If 3 divides A, including A=0, the residual is a ternary unit. Otherwise 2 and A/B are nonzero rational ternary units and 2^e A/B−1 is nonzero on this edge. Printed page 337 of Yu gives the consequence used here. In (1.8), the exponent parameter can be max(e,3); (1.9) is the unit hypothesis. Equation (1.2) holds for the rational field since 3≡3 (mod 4). There is no multiplicative-independence assumption in this inequality. The heights for the two logarithms are bounded by ln 3 and 2 ln(2H). Inserting n=2,d=f=e_𝔭=1 gives

    m ≤ 19·1200³·6·(5+ln 2)/(ln 3) · ln(2H) ln(max(e,3)).

The coefficient is less than 1.2·10¹². It applies to the local discrepancy and the explicit window bound in terms of the maximum exponent; rescaling the simpler asymptotic logarithms may change the constant. [Yu, pp. 337–339, DOI 10.4064/aa-89-4-337-378](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf)

Across k exact transitions put E=Σe. The displacement equation is simply 2^E(x_end+t_end)=3^k(x_start+t_start). Clear the two endpoint denominators and use (2,3)=1 to obtain 2^E | q_end(q_start x_start+p_start). The factor q_end cannot be dropped for a general even final denominator. For example at the fixed physical state 1 the signed magnitudes 3,2,5/4,11/16 follow three exact e=2 edges, so 64 divides 16(1+3) and does not divide 1+3. If the initial displacement is nonzero, 2^k≤2^E≤H²(x_start+1) for signed or unsigned p. Equality with a smaller actual state permitted later cannot repair an initially impossible all-exact run. If a lap closes with the same chosen anchor, a nonzero displacement yields 2^E=3^P. Signed cycle comparison starts at a state above H to ensure this nonvanishing.

Because x_i+1≤(3/2)^i(n+1), the interval from J to 2J cannot contain J exact transitions when (4/3)^J>(n+1)H². Starting at clock zero, the number 1+floor(log₂[H²(n+1)]) of transitions likewise forces a residual. The selected shallow endpoint belongs to the prescribed closed interval in both arguments. The physical exponent satisfies e_i≤log₂(3x_i+1)≤2+i log₂(3/2)+log₂(n+1). On a positive period, the product gives Σe≤2P. These bounds give the three claimed logarithmic precisions and the polynomial-height dyadic form.

## A separate reconstruction of the deterministic compiler

Orient each transient in-tree toward its terminal cycle or sink. Remove the cycles and treat each immediate predecessor of a removed cycle as a tree root, charging its edge to the cycle once when used. Sinks themselves can be tree roots. Let s(v) count the vertices in v's rooted subtree, and let L=max(2,ceil M^ε). Give v grade floor(log_L s(v)). Grades are nondecreasing toward the root. Every connected component of one grade g is a finite directed tree. Its leaves have pairwise disjoint original subtrees, each of size at least L^g, contained in the original subtree of its top vertex, of size less than L^(g+1). Hence there are fewer than L such leaves. Store all leaf-to-top label words in that component. Each internal path is a contiguous factor of one stored word, and their total stored lengths over all components are at most LM. The edges crossing grades are singletons (or free ones) and there are at most 1+log_L M per path. Add one periodic word per cycle and charge the entering edge. Each physical label costs at most log₂(3H²) in the frozen positive graph, so the required budget and piece bounds follow with arbitrary entrance and end cuts. Discard all-one and empty words and add the word (2) if the dictionary would otherwise be empty.

In the original compiler a residue class in the depth-to-terminal coordinate can have gaps only by reaching a terminal, because that depth decreases in unit increments. The least occupied refinement contains at most M/L^(l+1) vertices. Its emptiness at the final level creates no uncovered suffix. A path ending at a vertex or inside a last stored piece is admissible under phase-flexible factors in both proofs.

## External stopping conditions

A fixed non-eventually-periodic positive ordinary orbit enters neither 1 nor any positive rational template cycle, because any such entrance is periodic thereafter. In the cyclic assertion the primitive exponent period equals the least ordinary state period: if a shorter word of length s repeats the exponent sequence, its affine map fixes the phase after several laps; its multiplier 3^s/2^E differs from 1, so a fixed point of its positive power is its fixed point. Thus any representing template has length at least P, while budget B<P forbids one. The cycle through 1 is outside the sufficiently large period range. Each residual yields at least one shallow endpoint, and a clock is charged by at most its two neighbors. An eventually periodic positive ordinary trajectory has a finite height maximum; for positive anchors its height estimate is automatic at every clock. Signed exact coincidences need separate handling. [Paper 15/v2, (C2)–(C6) and Theorem 9 including (A1)](https://rstation.ai/problems/collatz/papers/15)

The first missing implication toward Collatz is a theorem forcing one ordinary nonconvergent orbit to violate these upper bounds, or forcing a smaller ordinary coalescing source from a shallow clock. Neither the sparse lower count nor the deterministic compiler makes that assertion.
