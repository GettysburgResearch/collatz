# From a blocked rewrite to a smaller ordinary source

**Collatz remains open.** Every positive integer reaches a fixed family of blocked mixed-base configurations or a verified finite base within ten ordinary shortcut steps. On reaching a configuration, deleting four ternary digits gives a positive partner strictly below the **original** source, even if the intervening orbit grew. A proof that every such configuration meets its partner would settle the conjecture. This continuation verifies entire infinite families of these mergers and estimates how many inputs admit them.

Throughout, $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. Two positive integers meet if their forward orbits contain a common value at finite, possibly different clocks.

## A fixed head and an actual forward visit

Let $J$ consist of the integers with ternary leading digits $21$ and at least four further trits. Every $x\in J$ has an AYH representation with fixed mixed prefix **c a f** followed by a purely ternary suffix. Its only blocked transition in PR 183's ten-rule subsystem is **a f**. The kernel-checked theorem gives, for every positive $n$, a clock $j\le10$ at which $x=T^j(n)$ is below 600 or belongs to $J$. Every positive state below 600 reaches one within 160 steps. For $n\ge600$, the four-trit truncation $m=\lfloor x/81\rfloor$ satisfies $7m<5n$. Therefore universal convergence is equivalent to $x$ meeting $\lfloor x/81\rfloor$ for every $x\in J$. [Proof and integer covering certificate](FIXED_HEAD.md) · [Lean theorem](TernaryHeadDescent.lean).

One kernel-checked certificate covers **all 81 children of each parent** in an explicit arithmetic progression. If $m$ is in this progression, $T^{172}(81m+r)=T^{172}(m)$ for every $0\le r<81$. The proof checks endpoints and odd counts at one representative and transports both over every positive lift. [Whole-fiber proof](WholeTernaryFiber.lean).

The growing version still follows the same ordinary source. Put $D=\lfloor\log_2 n\rfloor$ and $H=\lfloor\sqrt D/\log(D+2)\rfloor$. For large $D$, within $H$ clocks the orbit reaches a configuration with the prescribed head and an increasing number of leading zero trits after it. Deleting $H$ terminal trits gives $0<m<(n+1)2^{-H}$. The selected hit values form a set of natural density zero. Using PR 146's written finite-grid estimate, all but $O(2^D/\log(D+2))$ original sources in the octave actually meet their prescribed partner through that hit. The physical hitting argument is independent of the statistical estimate. [Growing schedule, conditional grids, and proof scope](GROWING_HEAD.md).

## Smaller partners with exactly the same critical surplus

For a marked odd $n$, write $d=\lfloor\log_2 n\rfloor$, $3n+1=2^e u$ with $u$ odd, and $s=5e-d-1$. The critical section $B$ requires $0\le s\le7$ and the high-bit mark $(d+1)(n-2^d)\le70\cdot2^d$. For every $\delta>0$, some $\eta(\delta)>0$ works in **each sufficiently high nonempty fiber of fixed $d,e$**. At least a fraction $1-\delta$ have a common ordinary future with a critical $m\le n^{1-\eta(\delta)}$ having exactly the same surplus. The counting argument depends on PR 146's written estimate. The Lean transport theorem proves the size, critical membership, and ordinary common future from the specified arithmetic data and a supplied merger of the odd endpoints. [Uniform counting argument](CRITICAL_COMPRESSION.md) · [Arithmetic transport](CriticalCompression.lean).

Two results constrain a proposed iteration. Arbitrarily large critical inputs have a first positive physical return larger than $n^{27/25}$. For a separate family, every merger with a smaller critical partner or the base takes more than $\lfloor d/4\rfloor$ further odd transitions on at least one arm after the first odd endpoints. A checked stopping criterion permits later common endpoints. [First returns](FIRST_RETURN.md) · [Merger-clock lower bound](BOUNDED_CRITICAL_MERGERS.md) · [Ternary stopping criterion](TernaryStopping.lean).

## How many ancestors reach one fixed target?

Let $A(b)$ consist of the positive integers whose orbits contain the same fixed $b$, with $3\nmid b$. A twelve-cell inverse policy supplies legal ordinary words from every such target, including even targets. Lean checks the word choice on arbitrary unit inputs, the cost of every within-block prefix, and the physical clock of each inverse link. The infinite concatenation and its phase and height estimates are written proofs. [Inverse policy](INVERSE_WORD_COVER.md) · [Formal scope](InverseWordCover.lean).

The resulting lower bound for the upper counting exponent of $B\cap A(b)$ is $\theta=0.654197799645\ldots$. Hence one may delete any set of upper counting exponent **strictly below** $\theta$ when testing convergence on $B$. The calculation uses Krasikov–Lagarias's published predecessor exponent $0.84$, whose computer-assisted proof was not replayed here. Substituting the repository's separately source-qualified $0.901$ gives $\theta=0.701705020810\ldots$. For the density-zero image of the growing-head schedule, the number of actual $b$-ancestors below $X$ is at least $X^{0.84-o(1)}$ for **all sufficiently large $X$**. This last statement uses the deterministic hitting and clock bounds. [Proof, external inputs, and limiting quantifiers](BASIN_COUNTING.md) · [Finite multiplicity and deletion lemmas](BasinCounting.lean).

## A sharper closing criterion for failed local comparisons

A fourth attack adds the missing symmetry to one particular comparison family. On the single sequence of bands
\[
H_j=[7\cdot81^j,8\cdot81^j)\cap\mathbb N,
\]
let \(D_j\) count the sources that never meet their four-trit truncation. The new written theorem proves
\[
D_j=o(81^{0.84j})\quad\Longrightarrow\quad
\text{every positive integer reaches one}.
\]
A bound of that size on the failures of a finite certificate also suffices. Only one of the four exponent classes of the fixed-head section is needed. The bound must hold as the level tends to infinity; one favorable subsequence is insufficient.

The proof combines a summable sequence of color changes under truncation with the exact identity \(f(2n)=f(n)\) for convergence status. Fine subcells recover an irrational rotation on the head interval. The limiting color must be constant, while the published inverse-basin bound prevents either color from having so few ordinary starts if a counterexample exists. This is a written argument, independently reconstructed; its full conclusion is not a Lean declaration. Three supporting Lean theorems check the floor identity, actual halving clocks on the subcells, and the return-rigidity implication for an ergodic transformation on a proper subset. [Full proof and scope](HEAD_EDGE_RIGIDITY.md) · [Formal ingredients](HeadEdgeTransport.lean).

This addresses a specific way to overcome the earlier transport warning. The ancestor counts alone do not turn a local failure count into a survivor bound. The new criterion additionally uses exact doubling symmetry, all sufficiently high levels and a power bound on failures. The present estimates of order \(X/\sqrt{\log X}\) for fixed-depth certificates are above \(X^{0.84}\). Proving the stronger bound, or proving merger at each exceptional source directly, remains open.

## Replay

The [Lean driver](check_lean.sh) built six supporting modules and seven new modules into fresh output storage and printed the axiom dependencies of all 20 new public theorems. The run passed with Lean 4.34.1, the pinned Mathlib revision, implicit variable creation disabled and warnings treated as errors. Every audited dependency is a subset of the standard axioms propext, Classical.choice and Quot.sound. The four exact Python replays cover [critical compression](check_critical_compression.py), [the inverse words and physical paths](check_inverse_word_cover.py), [the inverse clock budget](verify_inverse_cost.py), and [the first-return examples](verify_rising.py). All passed normally and with optimization, with identical output. [Evidence and independent reviews](../../../reports/ayh-resource-reset-20261124/continuation/README.md).
