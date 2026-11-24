# A density-one finite-state predictor would settle Collatz

**PROPOSED written theorem, with a separately checked ordinary arithmetic kernel.** Let T be the positive shortcut Collatz map. For every radix k = 2^a 3^b > 1, the following statements are equivalent.

1. Every positive integer reaches 1.
2. Some fixed base-k finite automaton predicts whether n ever reaches 1, with natural density zero of wrong answers.
3. Some fixed such automaton has **lower** natural error density zero; accuracy may approach one only along a subsequence of cutoffs.

This reduction concerns a fixed machine and ordinary integer inputs. No predictor with the accuracy in (2) or (3) has been constructed. A separate unconditional consequence is that **every** such machine predicting whether n ever reaches **5** makes errors on a set of strictly positive lower natural density. The lower bound can depend on the machine. Section 5 gives a numerical formula in terms of binary-kernel size.

The arithmetic starting point is the exact residual transfer already present in Fourier Wren's 2026 manuscript, §3, and its exact-automaticity conclusion. The extension here allows density-zero edge failures, uses Konieczny's asymptotic Cobham theorem, and turns local defects or predecessor densities into lower error density on ordinary sources. The distinction matters because infinite nonautomatic sets can differ from finite-state recognizable sets on a density-zero set. The density of the symmetric difference is measured against **all integers**, not against a thin automatic comparison set. [Wren, v3](https://rstation.ai/problems/collatz/papers/64/v3) · [related thin-set obstruction, §7.5](https://rstation.ai/problems/collatz/papers/75)

The final repository intake also found concurrent [PR200, Theorem C](https://github.com/GettysburgResearch/collatz/blob/c43fcbe6643c3d816975a4fb4328dc19dbdac6fb/research/regularity-rigidity-20261124/AUTOMATA.md), which already proves an arbitrary-base sparse-error obstruction by a macroscopic-block method under its stated predecessor bounds. This note gives a separate mixed-radix asymptotic-Cobham proof using fixed-target positive density; it claims no priority for the automatic-approximation criterion. [The all-radix testing lemma](AUTOMATIC_TESTS.md) and [weighted-clock synthesis](WEIGHTED_CLOCKS.md) obtain exact limiting proportions using the additional natural-density and equal-count-coalescence inputs.

## 1. Ordinary transport between kernels

Use n≥0 for digit sequences, extending any coloring arbitrarily at zero, with T(0)=0. Write F≈G when the set of unequal values has natural density zero. Each nonconstant affine progression of positive integer slope pulls density-zero sets back to density-zero sets. The same holds for the one-step T and for its fixed iterates: up to X the image lies below 2X, and each point has at most two preimages per clock. Finite unions of such pullbacks preserve density zero.

Let A be a coloring with finite output alphabet such that A≈A∘T. The k-kernel is the collection of sequences A(k^j n+r) for all j≥0 and 0≤r<k^j.

*Forward transfer.* Given p<2^j, let q=T^j(p) and let u count odd inputs on that prefix. Parity lifting gives T^j(2^j n+p)=3^u n+q for every n. Also q<3^u. Indeed induct on j; adding the last source bit before that clock adds zero or 3^v to an old endpoint below 3^v, where v is the previous odd count. The new input is below 2·3^v. Its even or odd step ends below 3^v or 3^(v+1), respectively. Consequently every binary-kernel row equals some ternary-kernel row modulo ≈.

*Reverse transfer.* For h≥1 and 0<r<3^h with 3∤r there exist p<2^J and J≤6h for which

    T^J(2^J n+p)=3^h n+r       for every n≥0.

To see this, lift the entire affine progression backwards. Given a current low coefficient u coprime to three, choose 1≤e≤6 such that 2^e u≡4 modulo 9; the six powers cover the units. Apply y↦(2^e y−1)/3, which is a physical inverse word of length e: e−1 doublings, then the inverse odd edge. Every high coefficient still has a factor of 3 at this step, so all lifts are legal. The new low coefficient is positive, odd and 1 modulo 3. After h such steps the leading coefficient is 2^J, and the low coefficient is below 2^J by the strict input bound r<3^h and the negative inverse carries. Thus every ternary-unit row equals a binary row modulo ≈. The clocks and ternary residue are chosen once, independently of n. The public Std-only theorem `Collatz.KernelTransfer.ternary_row` checks this exact all-n statement. The density statements and the rest of the present argument are written mathematics.

## 2. Applying asymptotic Cobham rigidity

Konieczny's Theorem B states that a finite-valued sequence that is k-automatic and asymptotically l-automatic for multiplicatively independent bases agrees almost everywhere with a periodic sequence. “Asymptotically automatic” means that the corresponding kernel is finite *modulo* ≈. His Theorem A, with both bases merely asymptotic, only yields shift-invariance modulo ≈. We require the stronger Theorem B, with one genuine deterministic automaton. [Konieczny, Theorem B](https://arxiv.org/abs/2209.09588)

**D1.** If A is k-automatic for k=2^a3^b>1, and A≈A∘T, then A is asymptotically constant.

If k is a power of two, A is binary automatic by base-power equivalence. Modify A on multiples of three to a new constant symbol, obtaining B, still binary automatic by the product construction with a periodic mask. Every positive-depth ternary row of B is either constant or, by reverse transfer, agrees almost everywhere with one of the finitely many actual binary rows of A. Thus B is asymptotically ternary automatic; apply Theorem B in bases 2 and 3. This proves A agrees with a periodic coloring on ternary units.

If k is a power of three, A is ternary automatic. Forward transfer makes its binary kernel finite modulo ≈. Now Theorem B gives periodicity modulo ≈ on the full integer domain.

If a,b>0, let Q=3^b. Approximate doubling invariance follows from A(2n)≈A(n). For any fixed h and r<Q^h, the Q-row A(Q^h n+r) therefore agrees almost everywhere with A(k^h n+2^(ah)r), a genuine k-row. Thus A is asymptotically Q-automatic. Since k and Q are multiplicatively independent, Theorem B again supplies a periodic coloring modulo ≈.

It remains to collapse the periodic coloring P on the units. The shortcut map carries ternary units to ternary units. Thus P(x)=P(Tx) on almost every such x; a single violation would recur on an entire progression modulo twice a common multiple of 3 and the period, so the equality is exact on the units. Fix any positive progression of units on which P has a constant color. Monks' backward sufficiency theorem gives, for **each** positive ternary unit x, a positive predecessor in the progression. An orbit from a ternary unit stays a unit, so P(x) has that same color. This uses a backward statement and does not assert that arbitrary forward orbits visit a specified class. It follows that A is constant almost everywhere on the units. Every odd x has a unit image and the odd step is injective, so A has that color for almost all odd x. On each fixed 2-adic valuation shell use doubling invariance; the union of shells of valuation at least H has density 2^(-H). This proves D1. [Monks et al., Theorem 4.1 and its proof](https://arxiv.org/abs/1204.3904)

## 3. From edge defects to a positive lower error

For a fixed machine A its defect set D={n:A(n)≠A(Tn)} is automatic in the same radix. Equality of digits under an affine integer relation is recognized with bounded carry; the graph of T is the union of the relations 2y=n and 2y=3n+1, with a parity test. Intersect the synchronized relation with the two output conditions and project to n. Leading zeros can be accommodated by finite padding.

Every automatic set has either density zero or strictly positive lower natural density. One direct proof reads digits least significant first on a complete automaton allowing high-end zero padding without altering acceptance. At cutoff k^j this is a finite Markov chain with one transition per digit. If no reachable closed communicating class contains an accepting state, the probability of acceptance tends to zero: from every transient state some closed class can be reached in at most S steps with probability ≥k^(-S), where S is the number of states. Intermediate cutoffs cost at most a factor k. Otherwise choose a fixed path into a closed class with an accepting state. Once there, from any class member one can reach acceptance in at most S−1 steps and then pad with zeros to exactly S steps. The uniform probability of this is ≥k^(-S). This gives a strictly positive lower bound at all large scales.

Let F be an eventually invariant exact target label, meaning F(n)=F(Tn) except at finitely many n. Put E={n:F(n)≠A(n)} and write E(X) for its count in [1,X]. Outside the exceptional sources, each n∈D belongs to E or its image belongs to E. Hence D(X)≤3E(2X)+O(1). If D has positive lower density, then the lower density of E is at least one sixth that of D. If D has density zero, D1 shows A is constant almost everywhere. In that case the lower density of E is positive whenever F takes at least two different values on sets each of positive lower density.

For the basin indicator of 1, one label has positive lower density by the target-one theorem of Mazur or Lau. If any nonconverger exists, its component contains an odd ternary unit s: take an odd step and strip powers of two; the resulting odd integer is a unit. All ordinary ancestors of s are nonconvergent. Lau's Theorem 1.3 and Remark 1.4 give a positive lower density of odd ancestors of each fixed s coprime to 6. The original unaccelerated clock can insert even intermediates after odd steps, but it visits the same odd targets as T, so this gives the other label. This proves statements (1)–(3) above. The same argument works for every nonconstant finite coloring constant on each component. No densities are assumed uniform over infinitely many distinct components. [Lau, v2](https://hexagonmath.org/2610.00249v2) · [Lau's formalization statement](https://github.com/AxiomMath/CollatzPositiveDensity) · [Mazur's fixed-target statement](https://proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

## 4. An unconditional ordinary decision problem

Let F(n)=1 if the T-orbit of n contains 5 and 0 otherwise. Its sole edge failure is n=5. The ancestor sets of 5 and 85 are disjoint: 5 reaches 8,4,2,1, while 85 reaches 128 and then the powers of two down to 1; neither target reaches the other. Both are positive odd units. Lau's fixed-target theorem gives positive lower densities for these two disjoint sets, proving the unconditional lower error claim. All statements concern correctness against arbitrary positive ordinary inputs, even if every such input reaches 1. In particular `ever reaches 5` and `ever reaches 1` are substantially different targets.

## 5. Effective binary state-budget bound

Suppose A has s distinct binary-kernel rows (the number of states of a minimal least-significant-digit-first machine). Put B=2^(2^(2^163)). For the target in §4, the lower natural density of errors is at least

    min{ 1/(85^(25/11) B), 2^(−6s²−2)/6 }.

For the first term, the explicit v2 predecessor theorem gives lower densities ≥1/(t^(25/11)B) at t=5 and 85. For the second, on n=2u test A(2u)≠A(u) with two residual-state registers. On n=2u+1 test A(2u+1)≠A(3u+2) with two registers and carry c initialized at 2. For a low bit d, feed (3d+c) modulo 2 to the second register and set c←floor((3d+c)/2), which always belongs to {0,1,2}. At the end evaluate the first row at zero and the second at its remaining carry. This gives at most 3s² states and padding invariance. At least one of the two tests has positive upper density if D does. The closed-class argument above gives ≥2^(−2S−1) lower density for a positive-upper-density padded binary test of S states (use a path of length at most S−1 into the class). Passing back to n costs at most a factor two, so D has lower density ≥2^(−6s²−2). The factor six is from §3. None of these estimates is a practical bound for deciding an input.

## The remaining inference

A finite automated controller on a restricted L/P itinerary reads an orbit and may use indefinitely many ordinary clocks. It need not compute the basin label from the finitely many base-k digits of its **initial input**. Likewise, a sequence of ever larger finite computations whose accuracies improve on tested ranges need not produce a **single** fixed automaton with zero limiting lower error. The positive-density ancestor input makes each actual component visible but permits two or more such components. No argument here supplies the predictor, forces a foliation of all ordinary sources by contracting L/P scripts, or proves Collatz.
