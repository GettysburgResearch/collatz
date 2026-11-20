# Prime-height dispersion and restricted merger rigidity

**Collatz remains unresolved.** This packet changes the proof objects: it
studies how prime factors carry an orbit's logarithmic height, and which
algebraic identities force every ordinary merger component to coincide.
It contains complete written proofs of those structural statements,
independent narrow reviews, and exact arithmetic checks. The two closing
hypotheses are still open.

The packet is a new branch from main
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Earlier exploratory work is
cited at immutable source commits; it is not merged into this branch.
Author-stage PROPOSED labels in the frozen proofs are preserved. The
separately pinned reviews specify which exact statements were reconstructed.
No proof-assistant verification or human acceptance is implied.

## 1. Every hypothetical escape must disperse prime height

Use the actual positive odd map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

For one ordinary orbit \(n_0,n_1,\ldots\), put
\(x_j=\log_2n_j\), \(W_N=\sum_{j<N}x_j\), and
\([n]_S=\prod_{p\in S}p^{v_p(n)}\). For every fixed integer \(s\ge1\),
the main theorem proves that every non-eventually-periodic orbit satisfies

\[
\boxed{
\sup_{|S|\le s}
\frac{\sum_{j<N}\log_2[n_j]_S}{W_N}\longrightarrow0.
}
\]

The prime set may be chosen after seeing the entire prefix, and may change
with the horizon. Thus even the heaviest bounded collection of primes
eventually carries a vanishing fraction of the accumulated height. One
cannot choose a new prime set separately at each individual state.

The proof is elementary and contains no cutoff on division exponents.
For two visited states, the exact affine correction gives

\[
\log_2\gcd(n_i,n_j)<x_i-x_j+3(j-i).
\]

In an \(r\)-state block, each selected prime can have only one unrestricted
maximal power. Every other occurrence is paid for by that gcd bound.
All block ranges together are at most the total variation of height.
Since upward increments of \(x_j\) are at most one, that variation is at
most \(x_0+2N\), including arbitrarily large downward jumps. Consequently,
for every actual finite history,

\[
\sum_{j<N}\log_2[n_j]_S
\le\frac{s}{r}W_N+sr x_0+5srN+B_{N,r},
\]

where \(B_{N,r}\) is the height of its final fewer than \(r\) states.
On an ordinary escape, \(W_N/N\to\infty\), so the limit follows.

There is also a count version: for every fixed \(\varepsilon>0\), the
fraction of visited states with \([n_j]_S\ge n_j^\varepsilon\) tends to
zero, uniformly over \(|S|\le s\). Repeating a primitive positive cycle
gives the same concentration restriction in terms of its mean height.
An elementary bounded-prime-support finiteness corollary follows. The
classical S-unit bound, with a better asymptotic dependence on support
size, is explicitly acknowledged.

**First missing step.** Dispersion is not a contradiction. A closing
argument would need a competing arithmetic property of one fixed surviving
ordinary history, or another way to exclude the diffuse case. Prime-flux
conservation only telescopes to endpoint identities; fixed-modulus
recurrence supplies height on the wrong scale. A fixed-source comparison
sequence \(2j+5\) demonstrates why finite ordinary representation, a short
rule, slow growth, and small pairwise gcds alone do not force retention.
For cycles, no universal bound on the number of participating primes is
established.

[Full proof, ADEL-001--007](adelic/PRIME_HEIGHT_ESCAPE.md) ·
[Independent review](capacity/ADELIC_REVIEW.md) ·
[Closing attempts and exact failures](adelic/CLOSING_ATTEMPT.md) ·
[Primary-source comparison](adelic/SOURCES.md).

## 2. A restricted five-ray merger already implies all of Collatz

Here \(T\) is the shortcut map: \(T(n)=n/2\) for even \(n\), and
\(T(n)=(3n+1)/2\) for odd \(n\). Write \(x\sim y\) if their actual
ordinary orbits meet at two finite, independently chosen clocks. Let

\[
\mathcal E=\{4^a x:a\ge1,\ x\text{ odd},\ 3\nmid x\}.
\]

The second main theorem is the exact equivalence

\[
\boxed{
\text{Collatz}
\quad\Longleftrightarrow\quad
\forall t\in\mathcal E,\quad t\sim5t+1.
}
\]

This parameter domain has natural density \(1/9\). The forward implication
is immediate; the reverse implication is a complete algebraic descent.
It closes the domain-extension question left open in FR-008 of the
[previous research packet](https://github.com/GettysburgResearch/collatz/blob/55d8968d2ecbc23a91c9c4733929f34be9bf0d28/research/focused-forward-20261120/five-ray/PAIRED_RETURNS.md).

For an arbitrary component label \(f\), assume the restricted mergers and
define \(F(n)=f(5n)\). Ordinary paths and that hypothesis give four laws:

| Law | Exact domain |
|---|---|
| \(F(2n)=F(3n)=F(5n)=F(n)\) | Every positive \(n\). |
| \(F(3n+1)=F(n)\) | Odd \(n\) prime to three. |
| \(F(9n+1)=F(n)\) | \(n\equiv3\pmod4\). |
| \(F(15n+1)=F(n)\) | Every positive odd \(n\). |

These laws force \(F\) to be constant. If \(n>1\) were its least different
label, the first cases reduce it to \(n\equiv67\pmod{120}\). Two legal
uses of the second law give \(v=(9n+5)/8\equiv1\pmod{15}\).
According to the parity of \(v\), a final legal law gives one of

\[
q=\frac{9n+5}{16},\qquad
q=\frac{27n+23}{32},\qquad
q=\frac{81n+53}{160},
\]

each a positive integer strictly smaller than \(n\) with the same label.
Every other input class already has an explicit smaller representative.
All \(n>1\) are covered. Constancy transfers back to \(f\) through actual
ordinary paths, proving the equivalence.

The companion checker represents inputs as \(480k+r\) and verifies every
law application, domain, exact division, and descent as an affine identity
for all admissible integer \(k\). This checks the conditional selector's
arithmetic. It does not establish the assumed physical mergers or their
clocks. The resulting logarithmic number of abstract reductions is not a
Collatz stopping-time bound.

**First missing step.** Prove the restricted mergers themselves. At
\(t=4^a x\), the exact ordinary paths identify that question with
\(x\sim5\cdot3^{a-1}x\). Reusing the four conditional laws to prove this
would be circular unless every call to the missing hypothesis were
replaced by a physical certificate or justified by a decreasing induction
parameter. Such an induction has not been supplied.

[Full equivalence and descent, CR-001--002](component/PROOF.md) ·
[Smaller sufficient system of identities](component/REDUCED_LAWS.md) ·
[Independent review](adelic/COMPONENT_REVIEW.md) ·
[Exact symbolic checker](component/check_component_rigidity.py) ·
[Author execution receipt](component/CHECK_RECEIPT.md).

## 3. A physical coupling attempt and its precise failure

The auxiliary pair route uses only legal paths in the full ordinary
merger graph. On odd positive inputs,

\[
A(n)=
\begin{cases}
(16n+3)/3,&n\equiv0\pmod3,\\
(4n-1)/3,&n\equiv1\pmod3,\\
(2n-1)/3,&n\equiv2\pmod3.
\end{cases}
\]

Each move preserves the input's actual component. Applied to two unequal
inputs in the same ternary class, it consumes one unit of
\(v_3(x-y)\). The proper cost
\(\log(1+\max(x,y))+\kappa v_3(x-y)\), with
\(\kappa>\log(16/3)\), strictly decreases during this mode.

At different ternary classes, the simplest independent-branch carry fails:
\((18u+3,18u+5)\) maps to \((96u+17,12u+3)\), with increased height
and no ternary credit. This infinite family rules out that proposed
one-block closure beyond every finite exception region. The packet gives
the actual-state drift condition a replacement would need, without
asserting that such a replacement exists.

It also proves why moving to larger ancestors cannot provide prime-height
retention on a fixed escaping forward history: every fixed source in a
component shares the same eventual tail. Relative closeness or favorable
finite preperiods are insufficient for ordinary coalescence.

[Physical moves, cost, obstruction, and scope, CP-001--005](capacity/PAIR_COUPLING.md).

## Evidence and continuation

The primary deliverables are the written structural proofs. Their narrow
reviews reconstruct the arguments; the scripts are complementary checks.
The new prime-height regression includes long growing prefixes, large
downward jumps with actual division exponent 2048, incomplete blocks, and
prime sets chosen after observing a prefix. It uses exact integers and no
floating logarithms. These are small adversarial checks, not an expanded
finite convergence census.

The [publication report](../../reports/2026-11-20-structural-reset/README.md)
records exact source pins, reviews, commands, and execution receipts.
No old scientific packet, frozen review boundary, workflow, or accepted
claim registry is changed by this exploration. The next mathematical task
is one of the two displayed closing implications, rather than increasing
a finite search ceiling or polishing a numerical constant.
