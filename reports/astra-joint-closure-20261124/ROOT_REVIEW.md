# Coordinator reconstruction

**Verdict: VERIFIED at the scoped elementary claims and finite checks below; global Collatz closure remains OPEN.** This report applies to the scientific source hashes in SOURCE_MANIFEST.json, together with the exact upstream pins in SOURCE_INTAKE.json. It does not approve every statement on a source branch.

## Weighted ordinary paired rows

I reconstructed the cylinder recurrence directly: after writing the free binary lift as v+2t, each endpoint has an odd free slope, so the next branch parity is fixed on that child cylinder and its new slope is the stated power of three. At equal grades, equality of intercepts in ratio five implies equality on the whole cylinder. The first-return stopping rule therefore identifies the exact record at a supplied source; the later zero padding is recovered uniquely by taking the odd part of that first endpoint.

For a record with p odd inputs, the condition on the child's class modulo 81 is exactly the parent's one class modulo 81 times 3^p. Checking all units modulo 3^12 covers every record since p≤8. The floor fifth root is conservative: taking the floor before the integer fifth root yields precisely the same admissible integer lower weights. All lower sums have strictly positive certified margin. No numerical approximation is used to certify positivity. I read the checker and independently executed the full payload; the final replay runs both normal and optimized Python.

The height condition y≥2C_*+3 makes each actual inverse child exceed 3y/2, while no child exceeds 2^400 y. Positivity and unit legality persist at every node. The unique parent decoder excludes collisions both at equal and unequal tree depths: an unequal-depth collision would force a strictly increasing reverse path from the root back to itself. The weighted transition probability telescopes to at most G_path^(-1/5)V(child)/V(root), and x≤q0 G_path gives the asserted upper bound on each stopped leaf's probability. A finite stopping tree has total probability one. This proves the aggregate lower count without an independent random law for actual Collatz steps.

The fixed terminal A branch is available in an unbounded exponent progression modulo 18. It makes q0 sufficiently large and makes its affine map carry the uniform prefix offset bound 2C_* into [0,1/2]. The source heights remain those of the stopped tree. For each clock, the resulting bounded multiplicative scale interval contains only a bounded number of grades. Thus the loss in selecting one row is O_q(log X), rather than its square. The theorem applies to q=1 and q=5 as well as other units. Its displayed height interval refers to the exhibited subset of a row, not every source counted in that row.

**Boundary.** The clock/grade ratio is uncontrolled. The finite pressure method remains subject to PR200's harmonic obstruction at exponent one; increasing a finite dictionary is not itself a mechanism for universal convergence. The 1/5 bound is a concrete improvement in a narrower paired count, not an unrestricted predecessor record or a resolution of PT.

## First-hit packing

The product over odd phases of a hypothetical loop at q is its inverse dilation D. A one-odd-step loop at q>1 is arithmetically impossible. The first two odd inputs give D≥1+5/(9q); its affine offset is therefore at least 5q/(9q+5)>1/2 for q>5. Composing it after a path of nonnegative offset cannot reduce that lower bound. The explicit trajectory from 5 excludes the remaining unit case q=5 and a second paired visit at q=1. Thus the cross-row disjointness does not assume that all cycles are trivial. Counting the actual integer interval of length (q+1/2)H proves the octave sum bound. This bound is compatible with a central 1/sqrt(log H) floor and with PT's subexponential losses.

## Long odd runs and ordinary counterfamilies to the selector

I reconstructed the exact odd-run identity, the reduction to distinct incoming edges, and the finite signed shadow. The shadow's remaining divisibility drops by one factor of three at each backward odd step. Starting after the first backward even step, its magnitude cannot fall below two, and each subsequent legal odd inverse costs a factor at most 3/4. This gives the stated general path budget without replacing a positive source by a negative one.

For the one-block selector, u<n forces more odd inputs than the original segment. The exact valuation v3(2^e−1)=i then bounds e below exponentially in i. Writing D as a positive multiple of n plus a strictly positive remainder proves the sharper necessary condition involving v3(n). The family with large powers of three and fixed binary suffix violates that condition at every first-run position. I checked the exponent inequality using log_2(3/2)<2/3 and the allowed size of the cofactor.

The positive CRT family is also valid: after division by 3^i the coefficient of n is a ternary unit, the new congruence refines the old one, and the exact binary valuation is independent. Each constructed progression has a positive affine competing source with slope below 1/3 for all sufficiently large representatives. A finite nesting over i=1,…,m retains the same eventual ordinary sources and every previous certificate. It does not retain an integer supplied before the refinement. The exact example and five exhaustive finite obstruction instances pass the separate control.

## Finite local rational cycle tests

The two branch orders have equal slope and intercept difference 1/4 modulo every modulus coprime to six. Since their finite semigroup is a group, all translations are available. Fixing the return slope and intercept at lifted prime powers gives the requested local value after cancellation. The lifted precision is strictly above the valuation of the slope defect; division therefore preserves the claimed residue. Prescribing intercept one and slope one at an outside prime power forces that entire power into the reduced denominator. The designated cancelled factor J really divides both numerator and full denominator, and it persists under rotation by local integrality.

The terminal ones-and-zeros suffix imposes the requested ternary unit independently of the middle word. Corrections take values in a finite group, so their lengths are uniformly bounded. Neutral zero/one runs change the real logarithmic defect densely; a finite cover of the compact range of previous defects gives a bound independent of the middle-word length. This is an existence proof, with no claimed practical bound on that padding.

All rotated fixed points are positive with denominator coprime to six. That forces the indicated branch parity at every step; the word is an actual rational orbit. The product identity bounds its entire real minimum. The middle words are injected at a fixed offset, proper powers have a strictly smaller exponential count, and division by the number of rotations preserves the critical entropy exponent. The result is a statement about deliberately nonordinary cycles, and cannot be applied to infer a missing denominator prime for an arbitrary supplied word. The fixed-source denominator estimate is credited to PR195 rather than presented as new.

## Formal verification and dependencies

The final replay made six successful compiler executions covering 25 distinct theorem declarations. Eleven finite declarations are new, and fourteen are import-adjusted replays of frozen PR202/203 proof bodies. The three standard Lean axioms are the entire printed union. The original PR202 unused-binder diagnostic is recorded; delivered working modules pass warnings-as-errors. Supporting compiled dependencies were reused, not rebuilt from scratch.

The new infinite theorems above are written mathematics with exact finite certificates where stated. The quantitative external renewal floor, predecessor density theorem, and whole-interval synchronization estimates have not become formal theorems through these finite checks. The new weighted-tree theorem and local rational construction do not depend on those external analytic results.

The first unsupported global inference is still an ordinary-source closure statement: neither the inverse-tree count, the refined successful cylinders, nor the rational approximants force the supplied surviving integer to enter the basin of 1.
