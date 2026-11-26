# Exact balanced source blocks at a macroscopic gate

## Physical law and coalescence input

Write $T(2x)=x$, $T(x)=(3x+1)/2$ for odd $x$, and $o_k(x)$ for the number of odd inputs before step $k$. For $1\le x<X$, let $k_X(x)$ be its first native time at or above $X$, omitting starts that never exit. At a chosen gate $z=z(X)$, give an exiting source the mass
$$
 F_X(x)=\frac{w_z(x)}x
       =\frac{3^{o_{k_X(x)}(x)}}{2^{k_X(x)}z}
$$
and every other source mass zero. Here $w_z(x)$ is the first-passage product of $3a/(3a+1)$ at odd departing inputs. The equality follows by multiplying the one-step identities. Suppose that along an unbounded sequence of integer $X$,
$$
 B_X:=\sum_{x<X}F_X(x)\ge\delta H_{X-1},\qquad \delta>0.
$$
All source probabilities below divide by $B_X$. A positive charged escaping component on the fixed ray of PR200 supplies this hypothesis. The theorem also applies to any gate satisfying the displayed inequality.

We use one external theorem. Write
$$
 E_H=\{q\ge0:T^H(q)=T^H(q+1),\quad o_H(q)=o_H(q+1)\}.
$$
This set is periodic modulo $2^H$ and its density $p_H$ tends to one. Said Duran's Gao formalization gives convergence of pair fusion. Valbuena's shortcut bridge establishes equality with both displayed conditions at the **same native clock** and gives the finite cardinality and period. I inspected the statements and proofs in the pinned files. The external development was not rebuilt in this run.

- `GaoShortcutBridge.lean`, `good_iff`, `good_mod`, `good_card`, `goodProbability_eventually`, lines 51–99, Git blob `a2aa84bb6f1e9ad92080bbb28ecc5c9920d4787e`. [Shortcut bridge](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/formal-periodic-census/source/GaoShortcutBridge.lean)
- `Martas.lean`, `MartasGao.martas`, line 288, Git blob `b8d834332ef59f3583d94360c91555dca08f2d0f`. [Pinned Lean source](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/formal-periodic-census/source/Martas.lean) · [Said Duran's software archive](https://doi.org/10.5281/zenodo.23003500)
- Valbuena, `paper/tao-basin-densities.tex`, lines 1697–1789, Git blob `63ca82653986b0dfa4c54bac17ed80199b806448`. This source also derives periodic means for each fixed basin from the adjacent-variation bound. [Paper source](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex)

## A uniform mixture of complete source blocks

Fix an integer $M\ge1$. Partition the integers into aligned blocks $[b,b+M)$, $M\mid b$. For $H\ge1$ call such a block usable if $b\ge1$, $b+M<X(2/3)^H$, and all adjacent pairs inside it belong to $E_H$. A usable block containing a source of positive mass consists entirely of sources of this same gate with **exactly equal** mass. If $\mathcal G_{M,H,X}$ is the union of these blocks, then
$$
 \limsup_{X\to\infty}\mathbb P_X(x\notin\mathcal G_{M,H,X})
 \le \frac{(2M-1)(1-p_H)}{\delta}.
$$
In particular, for fixed $M$ the lost conditional mass tends to zero in the iterated limits $X\to\infty$, then $H\to\infty$.

Indeed, $T^i(x)+1\le(3/2)^i(x+1)$. So every state in the first $H$ clocks of a usable block is below $X$. All its sources encounter one common state $y$ at clock $H$ and have the same number $q$ of odd inputs before $H$, by the consecutive-pair equalities. Their subsequent orbit, gate time, and full odd count therefore agree. The formula for $F_X$ gives exact equality.

The finitely many bottom sources and the fixed-factor top strip omitted by the cutoff have total unconditioned harmonic mass $O_{M,H}(1)$. For each remaining source in a bad block some $x+d\notin E_H$, with $|d|<M$. Each fixed translate of the periodic complement has harmonic mass $(1-p_H)\log X+O_H(1)$, by summing over full periods or partial summation. Use $F_X(x)\le1/x$, sum over the $2M-1$ translates, then divide by $B_X$. This proof is uniform over the choice of gate meeting the mass lower bound. It assumes no rate for $1-p_H$.

## What happens to the source entropy

Inside a charged usable block, write $x=b+r$. Conditional on the block, $r$ is uniform on $\{0,\ldots,M-1\}$. If $M=2^s$, the first $s$ parity letters run over all binary words exactly once. This uses the elementary length-$s$ bijection between shortcut parity words and source residues modulo $2^s$, by complementary final parity of the two lifts of each shorter word. Consequently, at *every fixed* length $s$, the initial parity law of a macroscopic ordinary gate tends in total variation to fair bits. Taking $X\to\infty$ first at fixed $s,H$, then $H\to\infty$, gives that conclusion even if the gates move.

Consider the ordinary integer affine translation $A_H(b+r)$ defined by
$$
 2^Hy=3^q(b+r)+A_H(b+r).
$$
For the actual letters it is nonnegative, as follows by the even and odd recursions. Conditional on this same block,
$$
 A_H(b+r)=A_H(b)-3^qr.
$$
Thus the source digit and translation have mutual information exactly $\log M$. Their joint law is at total-variation distance $1-1/M$ from the product of the two uniform marginals. The shared later physical trajectory supplies no extra variation. All translations have the same residue modulo $3^q$, as required by the common terminal congruence. Every source choice creates an equal and opposite change in the translation which cancels it **before** the later gate. This is an explicit obstruction to replacing these natural marginals by independent affine choices in the disjoint-window argument. Different candidate source laws would need their own comparison.

The two identities for $A_H$, including the natural-arithmetic sign, are checked in `GateMergeCarry.lean`. External coalescence and the harmonic limit above remain source and paper dependencies.

## Growing initial clocks without any coalescence input

There is also an elementary entropy estimate on initial words. Suppose $t=t(X)\to\infty$ with $t=o(\log X)$, and $Q=2^t$. The conditional source weight below $Q$ is at most $H_Q/B_X=O_\delta((1+t)/\log X)$. For $x>Q$, in any one class modulo $Q$ its harmonic mass is at most $Q^{-1}(1+\log X)$, by grouping integer points in consecutive $Q$-blocks. Therefore the conditional distribution on the surviving first $t$ parity letters after removal of the bottom sources is bounded pointwise by $C_\delta2^{-t}$. Its entropy is at least $t\log2-\log C_\delta$. Concavity of entropy then gives for the full macroscopic-gate law
$$
 H(\text{first }t\text{ letters})\ge
 t\log2-O_\delta(1+t^2/\log X).
$$
For complete-word semantics the letters here are always read along the physical orbit. If only pre-exit letters are desired, the starts with any exit before $t$ lie above $X(2/3)^t-1$. Deleting them costs $O_\delta((1+t)/\log X)$, and the same entropy estimate follows for the remaining starts.

For a fixed reference state $a_m$ on an escaping ray, a source $x$ hitting $a_m$ before $t$ must satisfy $x\le2^t a_m$. Its conditional probability is $O_\delta((1+t+\log a_m)/\log X)$. Thus a high-entropy early block and the nearly deterministic late suffix on the charged gate can occupy disjoint clocks on almost every such source. The earlier anticorrelation determines explicitly how fixed fair source digits can disappear before the common late segment. A uniform mechanism forcing extra **retained** mass to split between different late gates remains open.
