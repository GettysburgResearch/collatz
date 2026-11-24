# Either odd residue modulo six carries each directed Collatz cut

**PROPOSED written theorem with two complete affine certificates. Positive Collatz is OPEN.** Let $T(2v)=v$, $T(2v+1)=3v+2$, and let $C$ be the positive ordinary basin of 1. Fix **one** $r\in\{1,5\}$. For every positive odd $n$, there is a directed path from $n$ to $3n$ whose moves are ordinary $T$-edges in either direction or forward triplings $u\to3u$ at $u\equiv r\pmod6$. All extra moves use the same chosen residue. The path is bounded in length independently of $n$. The queries are drawn from an explicit finite list of injective positive-slope affine functions and have heights comparable to $n$.

Consequently **each of four individual implications is equivalent to Collatz**. Choose either residue $r$, then choose either direction $u\in C\Rightarrow 3u\in C$ or $3u\in C\Rightarrow u\in C$, and test only positive $u\equiv r\pmod6$. A counterexample forces at least the classical exponent $0.84$ in **each** of these four actual sets of violations along unbounded scales. Under the separate fixed-target density and pair estimates below, one sign on one scheduled head suffix, with even **or** odd binary valuation selected in advance, still carries divergent mesoscopic discordance.

## The finite certificates

Start the [residue one](cover1.txt) or [residue five](cover5.txt) tree at the affine progression $2t+1$, $t\ge0$. An internal binary or ternary node of arity $p$ partitions the row $mt+b$ into $(pm)t+(b+jm)$ for $0\le j<p$. Each leaf indexes a word in the file's dictionary. Here are all legal transitions, including the whole input domain of each.

| Letter | Input | Output | Reason |
|---|---|---|---|
| h | $2s$ | $s$ | Ordinary even step |
| D | $s$ | $2s$ | Reverse ordinary even step |
| t | $2s+1$ | $3s+2$ | Ordinary odd step |
| i | $3s+2$ | $2s+1$ | Reverse ordinary odd step |
| A | $6s+r$ | $18s+3r$ | Forward tripling in the chosen residue |

For a rule $is+j\mapsto ks+l$ and a current affine form $at+b$, check $i\mid a$, $b\bmod i=j$. Its entire image is then $k(a/i)t+k\lfloor b/i\rfloor+l$. Check positivity of slope and base after every letter. At every leaf with initial form $mt+d$, the final pair of coefficients must equal $(3m,3d)$. The branching proves coverage by successively dividing the original parameter with remainder. No individual representative or finite trajectory extrapolation is used.

| Allowed $r$ | Disjoint leaves | Words | Longest word | All letters | All A positions $Q_r$ | Smallest query/input $l_r$ | Largest query/input $h_r$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 948 | 261 | 63 | 35,627 | 2,325 | 27145/732923 | 26406895/30563 |
| 5 | 1,263 | 312 | 62 | 49,015 | 2,701 | 65/4167 | 4614215/6759 |

The ratios are the endpoint and limiting-slope bounds across all query positions. Indeed $(at+b)/(mt+d)$ stays between $a/m$ and $b/d$ for $t\ge0$. As a small illustration, the row $n=144t+63$ in the residue-five tree uses `tAthhiDDi`. Its sole extra query is $216t+95$, and its final state is $432t+189=3n$. The residue-one tree includes $n=1728t+219$ with word `tthAthhiDDiDi` and sole query $1944t+247$.

[check.py](check.py) reads the data afresh and replays this argument directly from the five rules. Both `python -X utf8 -B check.py` and `python -O -X utf8 -B check.py` reproduced [CONTROLS.json](CONTROLS.json) byte for byte. Its checks use explicit exceptions in both modes. This is exact finite arithmetic covering all positive odd integers. The analytic transfers below remain written deductions.

## Four separate ordinary cut bounds

For any $T$-invariant binary label $f$, let $E_i$ be the odd $n$ with $f(n)=i$, $f(3n)=1-i$, and $E_{i,r}$ the subset $n\equiv r\pmod6$. Along the chosen path ordinary edges preserve $f$. If the endpoint labels are $i,1-i$, at least one **forward** query changes labels with that same order, even if several others change them back. Each affine query position is injective on its source leaf. For every interval $0<A\le B$,

$$
 |E_i\cap[A,B]|\le Q_r\,|E_{i,r}\cap[l_rA,h_rB]|.                 \tag{1}
$$

The reverse inclusion is immediate, so the two counts have the same upper power exponent and the same convergence behavior for each moment $\sum n^{-s}$, $s>0$. PR195's compiled 40-leaf forward and 172-leaf reverse descent tables establish either global odd-unit implication sufficient for $f=1_C$. The new table promotes either individual-residue implication to the corresponding law on **all** odd $n$, by (1). This proves the stated four global equivalences. For one least counterexample $N$, PR195 even supplies an $E_1$ witness below $(167/27)N$ and an $E_0$ witness below $(2351/123)N$. Applying (1) locates witnesses in both restricted residues, with $N/3\le u\le h_r(167/27)N$ for $E_{1,r}$, and $N\le u\le h_r(2351/123)N$ for $E_{0,r}$. The lower bounds use respectively $3u\notin C$ and $u\notin C$. These four necessary witnesses do not give a smaller nonconvergent integer.

PR146's bounded directed return from $3n$ to $n$ uses only *forward* triplings at odd sources from a fixed injective-affine menu of comparable heights. Hence an $E_{1-i}$ edge charges some $E_i$ edge at comparable height, with bounded multiplicity. Combining this with (1), for each single choice $i,r$ there are constants $c,H,Q>0$ such that for every interval

$$
 |(E_0\cup E_1)\cap[A,B]|\le Q\, |E_{i,r}\cap[cA,HB]|.           \tag{2}
$$

Constants in (2) are larger than those displayed for (1). In particular there is no logarithmic weight or loss of a count exponent in (2).

With $f=1_C$, the published Krasikov–Lagarias fixed-target predecessor bound and the PR146 actual-label variation argument show that a counterexample gives $\gg X^{0.84}$ full-cut crossings on an unbounded sequence of dyadic octaves. The variation argument uses two components' predecessor populations and irrationality of $\log_2 3$. The argument is independent of the positive-density hypothesis. Equation (2) gives, for *each* $i,r$, $\gg S^{0.84}$ violations on an unbounded sequence of dyadic octaves $[S,2S)$, by dividing a fixed-ratio transfer interval into boundedly many octaves. An $o(S^{0.84})$ estimate for any one selected ordinary class on every large octave would settle Collatz. PR197's literal escape process additionally tracks the actual successor and can preserve the pair of labels even in a multi-step nonunit continuation. Its separate $0.600085\ldots$ threshold for each sign counted both odd unit residues together. Our sign-preserving paths localize a directed crossing, and may pass through intermediate ordinary components.

## One restricted head obstruction at the old common clock

Fix an open subarc $J\subset(7,8)$, a row schedule $j\equiv c\pmod L$, an integer $Q_0\ge0$, and **one** ordered sign $i$. Write $R_j=81^j$. Count the positive children $x\in R_jJ$ of the form $x=81y+57$, $y\equiv7\pmod8$, with $2^{Q_0}\mid x$, whose parent–child color order is $(f(y),f(x))=(i,1-i)$. Keep only children whose $v_2(x)$ has one prescribed parity. Write $b_j$ for the resulting count divided by $R_j$, zero on skipped rows.

To place a query $u\equiv r\pmod6$, choose $k\ge0$ with $2^k u\equiv-1\pmod{27}$. Set
$$
 b=(2^ku+1)/27,\qquad y=8b-1,\qquad x=81y+57=2^{k+3}(3u).
$$
Then $T^3 y=2^k u$, so parent and child have the labels of $u$ and $3u$ in this order. The actual valuation $v_2(x)=k+3$ is even for $r=1$ and odd for $r=5$, by reducing the congruence modulo 3. The possible $k$'s form a progression of step 18. Its logarithmic rotation by $18\log_{81}2$ modulo $L$ meets the required open arc and row class from every phase within a fixed number of steps, by compactness and irrationality. Hence one can choose $k$ from a fixed finite menu, also ensuring $k+3\ge Q_0$. In particular $u\le x\le Ku$ uniformly, and $x$ recovers $u$ as its odd part divided by 3. Finitely many bottom rows can be absorbed separately. This is PR195's existing placement, with its exact binary valuation retained.

Under the separately stated fixed-target density premise M, a counterexample forces $\sum_{n\in E_0\cup E_1}1/n=\infty$ by PR146's dyadic variation/rotation limit. Equation (2) gives divergence of $\sum_{u\in E_{i,r}}1/u$ (sum over geometric octaves, using bounded overlap). The finite-menu injection then gives $\sum_j b_j=\infty$. Finally keep only children satisfying the exact common-clock GOODPROFILE test of the [original PR201 packet, §4](../README.md). Write $b_j^{\rm good}$ for their normalized count. The pinned pair estimates P give $0\le b_j-b_j^{\rm good}\ll j^{-5/4}$ on the original sources, since the discarded children are a subset of PR201's whole-row discard. Thus for **each** one of the four choices,
$$
  \text{all positive integers reach 1}\quad\Longleftrightarrow\quad
       \sum_j b_j^{\rm good}<\infty\qquad\text{under M and P}.          \tag{3}
$$
The schedule, arc, valuation parity and orientation are fixed before looking at any source. The exceptional $O(R_j j^{-5/4})$ count is too large to transfer the $0.84$ power threshold to GOODPROFILE. That threshold applies to the restricted classes *before* the common-clock discard.

### Moving windows

Under PR193's additional published/manuscript inputs to its head-sampling argument, the implication from failure in (3) is stronger. There are $D,\eta>0$ such that every sufficiently late $s$ satisfies
$$
 \sum_{s\le j\le\lceil e^{Ds}\rceil} b_j^{\rm good}\ge\eta.         \tag{4}
$$
To check localization, let $a_j$ be the full normalized head-cut count. PR195's full-row variation inequality bounds it by $C R_j^{-1}$ times the number of all positive tripling defects through $C R_j$, including even sources. Strip powers of two. Their odd parts $n$ charge a selected $u\in E_{i,r}$ by the affine paths in (2), then an injectively placed head of height $x\asymp n$ on a scheduled row $k$. Each fixed $n$ has at most $O(1+\log(CR_j/n))$ possible even lifts. Each charged $x$ has boundedly many such odd antecedents. Therefore for a fixed shift $K$,
$$
 a_j\ll (j+1)81^{-j}+
   \sum_{1\le k\le j+K}(1+|j-k|)81^{k-j} b_k .
$$
The first term covers fixed bounded heights. PR193's full-row window lower bound gives a fixed positive mass on $[s+K+L,\lceil e^{D_0(s+K+L)}\rceil]$ for any fixed large $L$. When this convolution is summed over that window, the contribution from $k<s$ is $O(\sum_{d\ge L}(d+1)^2 81^{-d})$, since $b_k\le1$. Choose $L$ to absorb it. Each remaining $k$ has bounded total convolution weight, and all indices lie below $\lceil e^{Ds}\rceil$ for any fixed $D>D_0$ and large $s$. Finally $\sum_{j\ge s}(b_j-b_j^{\rm good})=O(s^{-1/4})$ under P. This proves (4). None of (1)–(4) supplies the opposing ordinary cut estimate.

## Provenance and first unsupported step

* **PR195, `0e8a7f9f965416189b30b57b8aa818fbcb7757c7`**, round 7, [head paths, explicit least-source constants and placement](https://github.com/GettysburgResearch/collatz/blob/0e8a7f9f965416189b30b57b8aa818fbcb7757c7/research/astra-global-closure-20261124/round7/head/README.md). Its 33-row quantitative substitution permits both directions and both unit residues. Its two directed descent formulas are the global closing input used after (1).
* **PR146, `f431078244e868dc699fad011044f0d5e7f76437`**, [directed return and cut (3)](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/DIRECTED_TRIPLING.md) and [dyadic limit and threshold](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_DENSITY.md). The $0.84$ count transfer uses those pinned written PR146 results, which were read at this head. Their published predecessor input is [Krasikov and Lagarias, Theorem 6.1](https://arxiv.org/pdf/math/0205002), for this ordinary shortcut map and each fixed target prime to 3.
* **PR197, `b0538639df0ab7edd239281bd897e705160f732c`**, [ordered unit escape](https://github.com/GettysburgResearch/collatz/blob/b0538639df0ab7edd239281bd897e705160f732c/research/ayh-resource-reset-20261124/unit-exit/ORIENTED_UNIT_SUFFIX.md). Its separate $17\bmod48$ result and the exact strictly smaller ordered representative there have finer binary information than (1).
* **PR193, `bdd4409062bc02416ff6941f8d5690b800068cb3`**, [head sampling, especially the full-row proof of (4)](https://github.com/GettysburgResearch/collatz/blob/bdd4409062bc02416ff6941f8d5690b800068cb3/research/astra-deep-closure-20261124/descent/README.md). The proof invokes the fixed-target density bound, complete-grid fusion and a two-logarithm estimate to separate earlier and later rows. Its almost-everywhere statement concerns real mantissas sampled at distinct head integers.
* **PR201, `73a145ca99448a78219bd149e273f33b6e3fda4b`**, original head note, [P, M, and KG8–KG11](https://github.com/GettysburgResearch/collatz/blob/73a145ca99448a78219bd149e273f33b6e3fda4b/research/killed-green-head-closure-20261124/README.md). P is the PR146 physical pair-chain input. M is the [reported positive lower ordinary predecessor-density theorem](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/). The latter is used only for (3)–(4). No independent rebuild of M or derivation of P is claimed.
* **Scope of adjacent programs.** [PR192's least-source descent](https://github.com/GettysburgResearch/collatz/blob/b72cea3bcd5aa51aba8df6f5e63bc1c473e9523b/research/astra-closing-step-20261124/descent/README.md) seeks a smaller representative in a prescribed child component. [PR200's common suffix](https://github.com/GettysburgResearch/collatz/blob/abf36c63b4d0181541d7e029d390d6f636940750/research/regularity-rigidity-20261124/pointwise-fibers/COMMON_SUFFIX.md) seeks a bounded compatible companion. The new path can use several intermediate components. It preserves the *ordered crossing of a binary cut*, without producing a representative in two specified components or a prescribed pair endpoint. No almost-everywhere ternary law or inverse atom floor enters the finite certificates.

The first unsupported step is to exclude the directed failures on even one of these classes, or to prove a quantitative upper bound contradicting the relevant lower bound. Each extra A move is a potential change of component. An affine path containing A's certifies the directed comparison structure, while an ordinary merger would require eliminating its changes of component.
