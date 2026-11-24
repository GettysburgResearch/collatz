# Ordinary descent and arithmetic obstructions at the closing step

24 November 2026. **Collatz remains OPEN.** This packet attacks three precise closing obligations: a smaller ordinary source, a contradiction on one escaping source, and exclusion of the complete reduced denominator of an ordinary cycle. It continues [PR192](https://github.com/GettysburgResearch/collatz/pull/192) with three GPT-6.2 Astra workers, independent reconstruction, and actual Lean execution.

The strongest new formal results construct ordinary smaller sources. The strongest new written results apply S-unit equations and the Subspace Theorem to the actual source and the actual evaluated cycle denominator. None supplies universal coverage. The arguments, the positive constructions, and the first missing implication are recorded together.

## 1. New ordinary descent certificates

Use the shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}
\]

and the accelerated odd map \(U(q)=(3q+1)/2^{v_2(3q+1)}\). The two exact odd-gap blocks are

\[
L=(2,1),\quad L(q)=(9q+7)/8,\qquad
P=(1,4),\quad P(q)=(9q+5)/32.
\]

These are literal ordinary steps, including their odd intermediate states. A finite legal word does not imply the existence of an infinite ordinary orbit with that word language.

### A smaller ordinary shadow without the old residue guard

[DESCENT.md](DESCENT.md) and [descent_Separated.lean](descent_Separated.lean) prove the following: on any infinite positive ordinary L/P input with at least six L blocks between consecutive P blocks, every odd state, including the intermediate states, has a smaller positive odd ordinary source whose trajectory never reaches one. There is no congruence condition on the starting value.

The construction uses slope \(251349/262144\) and eight explicit phase corrections. The resulting shadow has uniformly bounded dyadic denominators. The literal affine edge laws force any nonintegral denominator to grow, so all shadow boundaries are integers. Exact target gap pairs, positivity, the comparison at both odd phases, and the unbounded actual shortcut clock are proved. The public raw-input theorem constructs its finite phases from the Boolean L/P script; they are not supplied as an extra hypothesis.

This excludes a globally least odd nonconverger from this schedule class. It does not say that every nonconverger follows this class, or that a smaller companion below a later large value is necessarily below the original minimum.

### Finite mergers with unrestricted continuation

Two other certificates need only a finite prefix.

* **Triple paid block.** If an actual prefix is \(L^rPPP\), for any \(r\ge0\), then \(m=(q_0-7)/2\) is a smaller positive integer below both the initial boundary and the initial odd intermediate, and
  \[
  T^{3r+14}(m)=T^{3r+15}(q_0).
  \]
  [descent_Triple.lean](descent_Triple.lean) proves the whole finite statement from raw boundary equations. The continuation after the meeting point is arbitrary.
* **Variable slope after a long growth run.** If an actual prefix is \(L^rPLLL\), with \(r\ge3\), write \(q_0+7=2^{3r+1}v\). The ordinary cofactor and its positivity are derived from the input. The explicitly smaller odd source
  \[
  m=2^{2r+3}v-1=2^{2-r}(q_0+7)-1
  \]
  lies below both initial odd phases and satisfies
  \[
  T^{2r+16}(m)=q_{r+4}=T^{3r+14}(q_0).
  \]
  [descent_Extension.lean](descent_Extension.lean) proves the physical target path and its endpoint. The target begins with an unbounded all-odd ramp and then a fixed thirteen-clock word.

[DESCENT_EXTENSION.md](DESCENT_EXTENSION.md) develops the further finite-language consequences. The fixed half partner handles the unbounded family \(L^rP(LPL)^jP(P\mid LP)\). The ramp handles additional close-pair cases. Combining the certificates gives an accepting prefix in thirteen of the sixteen length-five words starting with P, after handling the initial L-run. The unresolved words at this depth are **PPLLL, PLLPP, PLLPL**. This is an exact finite code comparison, not a probability or density estimate on ordinary orbits.

The same note tracks the actual partner after a paid pair, instead of discarding its arithmetic state. The complete L/P selector remains open. Arbitrary positive odd gap schedules require further coverage beyond this alphabet.

## 2. Arithmetic restrictions on the same escaping source

[FIXED_SOURCE.md](FIXED_SOURCE.md) keeps one positive ordinary orbit \(q_i\), its actual gaps \(a_i\), and its clock \(A_n=\sum_{i<n}a_i\). The exact normalized values

\[
z_n=\frac{2^{A_n}q_n}{3^n}
\]

have different limits at two completions on a nonperiodic orbit: \(z_n\to\Lambda>0\) in the reals, and \(z_n\to0\) in \(\mathbb Q_2\). The real convergence uses the pinned strict-power count for one injective ordinary orbit. No algebraicity of \(\Lambda\) is assumed.

The rational finite-place Subspace Theorem uses these two limits to remove possible relations one coordinate at a time. This yields the following source-qualified written results.

| Result | Actual-source conclusion | Missing implication |
|---|---|---|
| FS1, finite comparison sets | For each fixed finite rational comparison set, the least number of defective affine edges in \([N,\lfloor RN\rfloor)\) tends to infinity when \(R>\log_2 3\). Prefix error count grows faster than \(\log n\). | No reason is proved that every escape must have a bounded-error comparison. |
| FS2, prime cofactor | For each fixed finite prime set and \(\beta<1/2\), times when the outside-prime factor of \(q_i\) is at most \(q_i^\beta\) have upper Banach density zero. | Large outside-prime factors are compatible with escape. |
| FS3, finite multiplicative rank | Visits to any rank-\(r\) rational multiplicative coset have uniformly vanishing long-interval proportion, with bounds independent of its chosen primes. | An arbitrary ordinary trajectory need not remain in bounded multiplicative rank. |
| FS5, signed full carry | An escaping orbit has no arbitrarily late proportional windows whose full carry has a bounded-length signed rational S-unit representation with bounded cancellation ratio. | No opposite upper bound for arbitrary actual carries has been found. |

For fixed \(R>\log_2 3\), the existence of some fixed prime set, length bound, and cancellation bound on infinitely many such carry windows is equivalent to **eventual periodicity of that source**. This includes hypothetical nontrivial cycles. Positive summand length by itself does not distinguish the cases: it diverges even for the carry \(4^l-3^l\) on the fixed point one. The signed refinement retains this distinction explicitly. On proportional windows near exponential height excursions, arbitrary signed length also tends to infinity without an imposed cancellation bound.

### A new stationary argument for the complexity of individual states

[SOURCE_EXTENSION.md](SOURCE_EXTENSION.md) proves a different statement. Fix a finite prime set \(P\supseteq\{2,3\}\), and let \(h_P(q)\) be the least number of positive **integer** P-units whose sum is \(q\). Along any nonperiodic positive ordinary orbit, the empirical distributions of \(h_P(q_i)\) have no tight subsequence. In particular, for every fixed K,

\[
\liminf_{N\to\infty}\frac{\#\{i<N:h_P(q_i)>K\}}{N}>0.
\]

If \(\log q_N/N\to\gamma>0\) along a subsequence, the corresponding lower density is at least \(\gamma/\log(3/2)\), independently of K and P.

The proof uses the Evertse–Schlickewei–Schmidt theorem between two rows with finitely many summands, even across an arbitrary intervening word. Finite summands give positive integral ordinary states with the same literal gaps. In a stationary limit, recurrence forces these states onto positive cycles, whose mean gaps exceed \(\log_2 3\). The actual source clock gives the opposite upper bound for the mean. This is a written compactness argument, not a Lean theorem.

PR194's canonical carry-birth estimate does not give a tight distribution of these positive integer presentations. The two quantities count different objects. The required bound in the opposite direction remains open.

## 3. Complete evaluated cycle denominators

For a primitive chronological shortcut word of length A with p odd steps and full carry C, write

\[
D=2^A-3^p>0,\qquad d=\frac{D}{\gcd(D,C)}.
\]

Here d is the **entire reduced rational denominator**, after integer evaluation and cancellation. An ordinary cycle requires d=1.

[CYCLE_CLOSURE.md](CYCLE_CLOSURE.md) constructs a certificate from any two proper cuts. If their reduced affine centers are \(c/a,e/b\), set \(K=ae-bc\) and

\[
G=\gcd(|2^{L_1}-3^{p_1}|,|2^{L_2}-3^{p_2}|).
\]

Then \(K\ne0\) and \(D/\gcd(D,|K|G)\) divides d, with the full prime-power multiplicities. When G=1 this is exactly d. For independent clock vectors, Corvaja–Zannier gives \(\log G=o(A)\). Sublinear total center height therefore implies \(d=2^{A-o(A)}\). Dependent clocks still give \(d\ge2^{A/2-o(A)}\), and an explicit primitive family attains that half-rate. A fixed-dimensional moving-target argument gives a further clock-relation alternative with its subsequence quantifiers preserved.

### Growing partitions

[CYCLE_EXTENSION.md](CYCLE_EXTENSION.md) removes the fixed-number-of-windows limitation in a different way. For k nonempty windows with maximum center height H, every fixed \(m\ge1\) and \(\epsilon>0\) have a uniform constant such that

\[
A\le C_{m,\epsilon}
\big[1+(1+\epsilon)\log_2(3/2)\big]^{\lceil k/m\rceil}
(1+H+\log d+\log A).
\]

Evertse's prime set stays exactly \(\{2,3\}\); the varying center coefficients and denominators are paid for in the outside-prime product. Grouping arbitrarily many but fixed m windows makes the estimate stronger than inserting a growing k into the previous finite-dimensional bound.

Thus \(k=O(\log A)\) and \(H\le A^{1-\eta}\), for any fixed \(\eta>0\), force \(\log d=A^{1-o(1)}\). For a hypothetical growing family of ordinary cycles, even the number of monochromatic runs must grow faster than \(\log A\).

There is no proved upper bound on the number of cheap windows in an arbitrary ordinary cycle. Near-critical primitive positive rational cycles can have arbitrarily large minimum, bounded gaps, and require many such windows. The omitted upper bound must therefore use ordinary integrality in an additional way. An asymptotic exclusion would also need an effective cutoff or a separate argument for remaining finite periods.

## 4. Verification and source boundary

[SOURCES.json](SOURCES.json) pins the consumed repository interfaces, including the new PR193, PR194, and PR188 heads. The earlier [PR192 source snapshot](../astra-phase-and-cycle-20261124/SOURCE_SNAPSHOT.json) remains unchanged. A source pin or metadata inventory is not a whole-PR mathematical review.

The descent worker executed the complete separated-input, triple-paid, and ramp statements in Lean 4.34.1 with `-j1 -DwarningAsError=true`. The other Lean modules prove arbitrary finite telescopes and two-center cancellation identities. The Subspace, S-unit, compactness, linear-form, and moving-gcd deductions remain source-qualified written mathematics. [ROOT_REVIEW.md](ROOT_REVIEW.md) records independent reconstruction and corrections at exact source hashes. The [execution report](../../reports/astra-closure-attack-20261124/README.md) records the integrating replay and repository validation separately.

Exact Python controls retain their checks under `-O` and use integers or rational arithmetic. Their bounded coverage checks examples, algebra, and failed strengthenings; it is not an unbounded convergence proof. The actual closing obligations are universal smaller-source coverage, an opposite bound for the same source complexity, or complete ordinary-cycle exclusion with the finite remainder handled.
