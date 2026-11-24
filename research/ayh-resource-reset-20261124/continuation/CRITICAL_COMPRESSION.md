# Polynomial-size smaller partners on typical exact critical fibers

**Status.** The arithmetic transport theorem is checked in Lean. The uniform counting result below is a written, source-qualified consequence of PR 146's finite synchronizing-clock estimate. All partners and common endpoints are ordinary positive integers. No assertion of independence across repeated uses, of convergence of either partner, or of pointwise success is needed for the result.

Use the shortcut map $T(x)=x/2$ on even inputs and $T(x)=(3x+1)/2$ on odd inputs. At a critical input $n$, write $d=\lfloor\log_2 n\rfloor$, $3n+1=2^e u$ with $u$ odd, and $s=5e-d-1\in[0,7]$. Its mark is $(d+1)(n-2^d)\le70\cdot 2^d$. Hold both $d,e$ fixed, and give the resulting finite fiber $F_{d,e}$ the uniform counting measure.

**Theorem.** For an absolute $C$, for all sufficiently large $d$, every admissible $e$, and every multiple of eight $8\le H\le d/12$, all but a relative fraction at most
$$
 C\big(\sqrt{(H+1)/d}+e^{-cH}+2^{-cd}\big)
$$
of this fiber have a physical common future with a critical source $m$ satisfying
$$
 2^{5H/4}m<n,\quad d(m)=d-5H/4,\quad e(m)=e-H/4,\quad s(m)=s(n).
$$
The two paths have $O(d)$ shortcut clocks from their respective starting integers. Consequently for each $\delta>0$ there is $\eta(\delta)>0$ such that in **every** sufficiently high nonempty fiber at least a $1-\delta$ fraction has an actual critical partner $m\le n^{1-\eta(\delta)}$. Taking $H=8\lfloor d/(8\log d)\rfloor$ instead gives a fraction tending to one with a simultaneous gain by a factor $2^{(5/4+o(1))d/\log d}$. Here and below logarithm bases in big-O bounds only change absolute constants.

### 1. The moving interval consists of actual odd endpoints

For large $d$, the upper mark lies strictly below $2^{d+1}$. As $n$ runs through $F_{d,e}$, its endpoint $u$ runs without multiplicity through one residue class modulo six, in the interval
$$
 J=\left[3\cdot2^{d-e}+2^{-e},\;3\cdot2^{d-e}\!\left(1+\frac{70}{d+1}\right)+2^{-e}\right].
$$
Indeed an odd $u$ must satisfy $2^e u\equiv1\pmod3$, and $n=(2^e u-1)/3$ is odd for $e>0$. Thus $|F_{d,e}|\asymp 2^{d-e}/d$, uniformly in the at most two admissible $e$ for each $d$. In particular $e=d/5+O(1)$.

### 2. A compressed endpoint of the correct ternary class

Stop the path from $u$ at its $H$-th even input, of either parity at the final endpoint after that step. Write $h$ for the number of steps and $p=h-H$ for the number of odd inputs. Discard $h>3H$, including paths with no such stop by that clock. The parity-word bijection on binary residues gives an $O(e^{-cH})$ fraction on an unrestricted length-$2^{3H}$ block, by the binomial lower-tail bound. Conditioning on an odd first input costs a factor of two. On the fixed class modulo six the index moves by six, hence runs through those odd residues evenly. A leftover block contributes $O(2^{3H}/|F_{d,e}|)$. This is exponentially small in $d$ throughout the displayed range of $H$.

On each surviving binary cell $u=2^h t-a$ with $1\le a\le2^h$, the positive mirror map $S(x)=x/2$ or $(3x-1)/2$ gives
$$
 T^h(u)=3^p t-r,\qquad r=S^h(a),\qquad 1\le r\le3^p .
$$
The two signs have the same parity indicators along the word, which gives the formula by induction. The upper bound follows from $S(x)\le3^{x\bmod2}x/2$ and $a\le2^h$.

Choose the unique $g\in\{1,2,3\}$ for which $2^p g\equiv a-1\pmod3$. Set
$$
 v=2^p(t-g)-1 .
$$
Here $p\ge1$ because $u$ is odd. All these integers are positive for large $d$, since $t\gg 2^{d-e-3H}$. From $h-p=H\equiv0\pmod8$ it follows that $v\equiv u\pmod3$. Moreover
$$
 0<u-2^H v=g2^h+2^H-a\le4\cdot 2^{3H}.
$$
The first $p$ ordinary steps of $v$ are odd, and they give $T^p(v)=3^p(t-g)-1$. Subtracting $X=T^h(u)$ leaves the fixed signed gap $D=r-3^p g-1$, with $|D|\le 3^{p+1}+1$. Matching the odd counts is what reduces the relevant log-gap cost to $O(H)$.

### 3. Uniform transfer after conditioning

PR 146's written growing-gap bound gives, on a full binary grid of depth $b$, an exceptional fraction
$$
  \ll (1+\sqrt{\log(2+|D|)})/\sqrt b
$$
for the failure of $X,X+D$ to merge synchronously by clock $b$. Use its counted-fusion event, invariant over a fixed initial residue modulo $2^b$. This is the finite-grid statement in the proof, before the two-block interval covering. The ordinary pair values here are positive. The bound and its scope are identified at the end.

After the binary condition and the fixed ternary residue in part 1, $t$ ranges over a single arithmetic progression of step three. Its number of terms $L$ is comparable to $2^{d-e-h}/d$ on each cell, with an absolute rounding error. The corresponding $X=3^p t-r$ has **odd** step $3^{p+1}$. Every full block of $2^b$ terms of this progression therefore gives each binary residue once. Take $b=\lfloor\log_2 L\rfloor\gg d$, using $h\le3H\le d/4$. At most two blocks cover all $L$ terms, including an incomplete end block, so the exceptional relative fraction on each such cell is $O(\sqrt{(H+1)/d})$. Summing over the disjoint stopping cells proves the same bound there. This argument does not assume an independent parity sample after selecting a successful pair.

On success both $u,v$ physically reach the same $z$ in respectively $h+b,p+b$ steps, padding a prior meeting to $b$ if needed. The large valuation of $n$ did not prescribe any of these later parities.

### 4. Rebuilding the strictly smaller critical source

Write $H=8k$, $f=e-2k>0$, $D_0=d-10k$ and $m=(2^f v-1)/3$. The congruence and parity above make $m$ a positive odd integer of exact exponent $f$. The upper size inequality follows from
$$
 2^{10k}(3m+1)=2^{f+2k}2^{8k}v\le 3n+1,
$$
with $2^{10k}>1$. Discard the lower edge $u<3\cdot2^{d-e}+4\cdot2^{3H}+2^H$, comprising a relative $O(d\,2^{3H-(d-e)})$ of the original fiber. Else $v\ge 3\cdot2^{d-e-H}+1$, and hence $m\ge2^{D_0}$. The upper size bound gives $m<2^{D_0+1}$. Since $2^{10k}(m-2^{D_0})\le n-2^d$ and $D_0+1\le d+1$, the mark holds for $m$. The two inequalities defining the critical surplus are preserved exactly. The initial $e,f$ steps take $n,m$ to $u,v$, respectively. This proves the theorem. For the fractional-power consequence take $H$ to be the largest multiple of eight below $\varepsilon d$ with sufficiently small fixed $\varepsilon=O(\delta^2)$, and use $n<2^{d+1}$.

[CriticalCompression.lean](CriticalCompression.lean) proves the arithmetic and physical transport `critical_compression` for arbitrary positive $k,f$ from the stated exact factorizations, octave edge, critical inequalities, and an actual merger. The probabilistic counting estimate and construction of the stopping cells are written arguments.

### Why iteration is a new obligation

The constructed $v$ satisfies $v\equiv-1\pmod{2^p}$, although the original $u$ ranged over a full odd residue class in a long interval. Thus the operation concentrates its output on a prescribed long binary prefix. The fresh fiber estimate gives no conditional success law there. A fixed bad component could also have a single failed least critical root and many large members admitting smaller partners. Counting sources without a smaller certificate does not count sources failing to converge, even when a power saving for the former is available. A proof for every root, a transport theorem maintained until a fixed floor, or a proof that the uncertified roots themselves converge remains missing.

### Pinned dependencies

- [PR 197, CriticalSection.lean](https://github.com/GettysburgResearch/collatz/blob/2fb1f11c959e35eba875338833d84969222dc089/research/ayh-resource-reset-20261124/positive-section/CriticalSection.lean) defines the exact critical set and proves global equivalence.
- [PR 146, PREFIX_COMPRESSION.md](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/PREFIX_COMPRESSION.md) gives the matching-count compression construction. Here the extra shift $g$, the selected count of even inputs, and the critical lift preserve the original exact excess.
- [PR 146, GROWING_ADDITIVE_GAPS.md](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md), equation (1), gives the uniform input-gap estimate used above. Its finite parity transport and the input estimate for arbitrary oriented states are in [THREE_RAY_UPPER.md](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md). They are written source results, not new Lean declarations or an independent re-verification of that probabilistic argument here.
