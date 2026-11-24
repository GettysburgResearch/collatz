# Diffusive transverse spread of genuine smaller heads beyond the native clock

**Status.** PROPOSED written theorem, on the actual ordinary head rows, using the SOURCE-QUALIFIED finite binary-grid pair bound and the PR 197 rounded-head witnesses. Three finite arithmetic and counting declarations are isolated in `LateWitnessTracks.lean`. Collatz and summability of the entire head disagreement series remain OPEN.

Put $T(n)=n/2$ for even $n$, $T(n)=(3n+1)/2$ for odd $n$. Fix an orbit-invariant binary color. On $R=81^j, d=\log_2 R$ the original child is $x=81n+r$, $7R\le x<8R$, $0\le r<81$. A regenerated head at time $t$ means a genuine discordant four-trit edge from the construction of `HEAD_INCIDENCE.md` with the bounded-intercept mark. If its child is $z=\lfloor U_t/3^u\rfloor$, the effective exponent in the *common parent* coordinate is
\[
 k=p_U(t)-u+4\mathbf 1_{U\text{ is the original child arm}} .
\]
The transverse coordinate is the integer $k-\lfloor t/2\rfloor$. All probabilities below count original children with weight $1/R$.

**Theorem.** Fix $A>1$. Outside $O_A(Rd^{-A})$ original children, the following assertions hold throughout the late physical slab $3d\le t\le 3.1d$.

* On a genuinely discordant source, every contiguous slab interval of $D\ge (\log d)^6$ integer clocks has at least $cD$ marked times supplying genuine smaller discordant heads. For **any** choice of one such head per marked time, their transverse coordinates take at least $c_A\sqrt{D/\log d}$ distinct values on that interval. In particular an interval of length comparable with $d$ needs $\gg_A\sqrt{d/\log d}$ distinct centered exponents. The same statement holds for the fixed interior mantissa arc allowed by the incidence theorem, with constants depending on the arc.
* More generally prescribe at most $d^P$ tracks, each specifying at most $W\ge1$ integer candidates $k$ at each clock. Count a clock whenever **any** of its genuine regenerated heads belongs to the track. Simultaneously on all contiguous $D$-clock intervals, each such track accounts for at most
\[
       C_{A,P} W\sqrt{D\log d}
\tag{1}
\]
clocks. The track list may depend on the first $s=\lfloor d/2\rfloor$ native bits of the original parent and on its suffix $r$. Within a track its list at time $t$ may in addition depend on the low $t-t_0$ bits of a coarse coordinate $m$ specified below. One makes the prescriptions before seeing its next unused binary block. An oracle for the true endpoints is not among these inputs.

In particular, even allowing the strip's offset to be selected after the full trajectory is known, the discordant mass whose witnesses stay in a band of width $W=d^\beta$ around one of polynomially many specified drift curves through a positive fraction of a polynomial-length interval $D\asymp d^\gamma$ is summable if $2\beta<\gamma$. Here one may allow any integer offset in the actual $O(d)$ range as part of the polynomial track list. This includes large incoming grade. Older distinctness in `HEAD_INCIDENCE.md` separates the heights at distinct times but permits all their centered exponents to coincide.

## A common ordinary source coordinate

Write $a=1-\tfrac12\log_2 3=0.20751\ldots$. The bounded-intercept estimate gives, at every marked time on the good source sample,
\[
 z=\lfloor 3^k 2^{-t}n\rfloor+b',\qquad 0\le b'\le C_A,
 \qquad |k-t/2|\le C_A\sqrt{d\log d}.
\tag{2}
\]
Indeed divide the actual upper affine formula by $3^u$; on the child arm substitute $81n+r$. Its nonnegative suffix contribution is $r3^{k-4}2^{-t}=o(1)$ here; the upper intercept is bounded by the fixed $E$. The odd-count and grade envelopes in `HEAD_INCIDENCE.md` supply the last inequality. Enlarge the fixed integer rounding allowance when necessary.

Choose $t_0=\lfloor 2.9d\rfloor, k_0=\lfloor t_0/2\rfloor, c=3^{k_0}2^{-t_0}$ and $m=\lfloor cn\rfloor$. The cell $m$ alone suffices: writing $\Delta=t-t_0$ and $g=k-k_0$, throughout (2) we have $g\ge4$ and
\[
  3^g2^{-\Delta}=2^{-a\Delta+O_A(\sqrt{d\log d})}<1
\]
for all sufficiently large $d$, since $\Delta\ge .1d-O(1)$. Dropping the fractional part of $cn$ therefore changes its subsequent floor by at most one. Every child in (2) belongs to the **finite list**
\[
  z_{t,k,b}(m)=\left\lfloor3^g m/2^\Delta\right\rfloor+b,
  \qquad 0\le b\le C'_A .
\tag{3}
\]
Everything in the ensuing upper bounds is uniform in these bounded corrections. Candidate exponents outside (2) can first be discarded; every actual marked child is retained on the good sample.

For fixed $r$ the parent interval has $N=R/81$ integers. The number $M$ of intersecting consecutive $m$-cells is $cN+O(1)=2^{(1-2.9a)d+O(1)}$, greater than $2^{.39d}$ eventually. Their preimages are intervals of length at most $1+c^{-1}$. Even after prescribing $n\bmod 2^s=v$, the number of parents per cell is at most $1+(1+c^{-1})/2^s\ll c^{-1}2^{-s}$, since $c^{-1}=2^{2.9ad+O(1)}$ and $2.9a>1/2$. Consequently for a test on $m$ periodic modulo $2^H$, with $H\le .31d$ and uniform-grid probability $p_v$ possibly depending on $v$, the normalized count over any set $V$ of initial residues satisfies
\[
  \frac1N\#\{n:n\bmod 2^s\in V,\ m\text{ passes its test}\}
    \ll 2^{-s}\sum_{v\in V}p_v .
\tag{4}
\]
Indeed at most $M/2^H+2$ complete periods cover the entire cell interval. This incurs one absolute constant for the *whole test*, including a conjunction at many clocks. The same upper bound holds for a nonnegative periodic weight by summing its level sets. For the native survivors $V$ at time $s$, the source-qualified merger tail supplies $|V|/2^s=O(d^{-1/2})$. The original and later tests use different resources in this counting argument.

## Fresh blocks for several late head tests

Fix $v,r$. On a complete base grid modulo $2^H$, expose $l=m\bmod 2^\Delta$; write $m=l+2^\Delta q$. From (3) the child and parent are exactly
\[
 z=3^g q+c_l,\qquad
 \lfloor z/81\rfloor=3^{g-4}q+\lfloor c_l/81\rfloor,\qquad
 z\bmod 81=c_l\bmod81,
 \quad c_l=\lfloor3^g l/2^\Delta\rfloor+b .
\tag{5}
\]
For every next block of $h\le H-\Delta$ bits, its parent runs bijectively modulo $2^h$ conditional on $l$, because the new slope is odd. Thus the pair theorem for the *fixed suffix* $c_l\bmod81$ bounds the fraction of block values lacking the finite physical merger by $C/\sqrt h$. If $z$ is truly discordant this finite failure is necessary. This argument can check a list of $W$ exponents chosen from the known prefix and all the finitely many roundings in (3), at cost $C_AW/\sqrt h$. The finite failure mark, unlike eventual discordance, is measurable after those $h$ bits. One can apply the test on a completed grid by its residue description even outside the source interval; all asserted physical witnesses are positive on the original row.

For ordered test times $t_1<\cdots<t_p$ in an interval of $D$ slab clocks, give $t_i$ the window $h_i=t_{i+1}-t_i$, and take $h_p=D$. The total deadline is at most $.2d+.1d+O(1)<.31d$. Conditional iteration of (5) on that **one base grid**, followed by (4), bounds their joint incidence by
\[
 C_0\frac{|V|}{2^s}(C_A W)^p D^{-1/2}
     \prod_{i<p}(t_{i+1}-t_i)^{-1/2}.
\tag{6}
\]
This is an upper bound on true events via horizon-specific finite failures. Their actual witnessing exponents and arms may vary. No fair bits are asserted for the two physical endpoints conditional on the true paths. Equation (6) uses an exact triangular dependence on the lower binary blocks of the projected integer $m$.

## Counting many hits and applying regeneration

Let $N_I$ count the actual marked clocks of a track on $I$, on the source-envelope complement (set it to zero on the discarded original exceptions). Expand $\binom{N_I}{p}$ as a sum over ordered positions. For each term overcount the true event by its own finite tests in (6). For $1\le p\le D$, the first position has at most $D$ choices. For the gaps $j_i\ge1$ with $\sum j_i\le D$, insert $e^p\exp(-p\sum_i j_i/D)\ge1$. Since $x^{-1/2}e^{-px/D}$ is decreasing, its integral on $(0,\infty)$ gives
\[
 \sum_{j\ge1}j^{-1/2}e^{-pj/D}\le\sqrt{\pi D/p}.
\]
It follows that
\[
 \mathbb E\left[\mathbf1_{n\bmod2^s\in V}\binom{N_I}{p}\right]
   \le C_0\frac{|V|}{2^s}\sqrt p
         \left(C_1 W\sqrt{D/p}\right)^p .
\tag{7}
\]
For $L\ge p$, $\binom{L}{p}\ge(L/p)^p$. Choose $p=\lceil c\log d\rceil$ and $L=\lceil C_{A,P}W\sqrt{D\log d}\rceil$. The event is empty if $L>D$; otherwise the constants allow $p\le L\le D$, and (7) makes its probability $O(d^{-A-P-3}|V|/2^s)$. Sum over $O(d^2)$ intervals and at most $d^P$ tracks for each $v,r$, with (4) if the menu depends on the initial residue. This proves (1). Equivalently, (7) yields a Gaussian tail in $L/(W\sqrt D)$ in its nonvacuous range, up to absolute factors and constants depending on the original envelope.

The earlier true entrance to the common polylogarithmic floor occurs at $d/a+o(d)>3.1d$ on the good original sample. The scalar sliding windows, original low-grade occupation bound and positive-frequency bounded-intercept regeneration of `HEAD_INCIDENCE.md` now apply to blocks throughout the slab. Tile each tested interval by length $b=O_A(\log d)$ blocks, discarding a terminal remainder. Every block starting below grade $4b$ consists of clocks at grade at most $5b$, and their total length on a discordant source is $O_A((\log d)^5)$. Every other block gives a fixed positive fraction of marked clocks. For $D\ge(\log d)^6$, this proves the uniform $cD$ lower bound without a union over the sources of separate exceptional probabilities. Apply (1) simultaneously to the singleton tracks $k=\lfloor t/2\rfloor+v'$ in the $O_A(\sqrt{d\log d})$ relevant range. Dividing $cD$ by their individual clock cap proves the claimed transverse spread. Taking a fixed interior arc uses the same positive-frequency construction with its prescribed interior margin.

## Boundary

A diffusive interface spanning order $\sqrt D$ centered exponents in $D$ clocks remains compatible with (1). The argument neither bounds the mass of that spread-out branch by a summable sequence nor supplies a conditional second native survival factor for the original physical pair. What it proves is a simultaneous product estimate for **specified sparse tracks of smaller genuine head tests** at clocks strictly beyond $d$, with the initial native survivor test optionally retained, and an unconditional geometric restriction on every remaining discordant source.

**Inputs.** PR 197 at `6eb986b0ce0b1836a356474d25d709ed4e948b67`, `research/ayh-resource-reset-20261124/two-class-descent/HEAD_INCIDENCE.md`, `ROUNDED_HEAD_DESCENT.md`, `ACTUAL_FRONTIER_OCCUPATION.md`, and the concentration and first-passage references pinned there. PR 146 at `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md`, supplies the complete-grid canonical-pair tail for the 81 bounded suffixes. No input about fixed-target predecessor density is needed.
