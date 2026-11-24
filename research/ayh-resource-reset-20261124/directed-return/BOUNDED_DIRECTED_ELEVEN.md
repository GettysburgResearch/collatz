# A bounded directed substitution at 11 modulo 32

**PROPOSED.** Use the positive ordinary shortcut \(T(2n)=n,\ T(2n+1)=3n+2\). Fix a binary label \(f\) invariant under \(T\). For distinct labels \(a,b\), let \(D_{r,m}^{a,b}(X)\) count the positive \(x\le X\) with \(x\equiv r\bmod m\) and \((f(x),f(3x))=(a,b)\). We prove

\[
 D_{1,16}^{a,b}(X)\le 1007D_{11,32}^{a,b}(H X),
 \qquad H=574854143371/219537<2618500.
\]

Every query is an ordinary positive integer and carries the original ordered labels. Its parameter is one of a fixed finite list of positive-slope affine functions on the original source progressions. Consequently the harmonic sums transfer at constant cost. The earlier ordered-label bijection \(11+32t\leftrightarrow17+48t\) transfers this result to \(17\bmod48\), with at most a further factor two in the height bound.

## Source path and certificate

Start at an actual defect \(x\equiv1\bmod16\). If \(x\equiv2\bmod3\), the ordinary exchange with \((2x-1)/3\) gives the desired query. Otherwise follow one of the three maps \(F_e(x)=(2^e x+c_e)/3\), where \(c_2=-1\), \(c_4=c_5=3\). For \(x\equiv1\bmod3\), use \(e=2\). For \(3\mid x\), use the unique actual choice \(e=4\) or \(5\) carrying the same ordered labels. Each new source remains \(1\bmod16\). The ordinary exchanges are proved in PR197 at baseline b0538639df0ab7edd239281bd897e705160f732c, in NonunitExit.lean and UnitResidueExchange.lean.

Each certificate entry specifies a word \(w\) on \(\{2,4,5\}\), an index \(0\le i\le |w|\), a positive row \(ms+b\), and a comparison path. Whenever \(w\) occurs in the source path, its state \(x_i\) at this index belongs to the stated row. From \(x_i\) to \(3x_i\) the comparison path uses ordinary edges in either direction and extra edges only in the forward orientation \(32s+11\to96s+33\). Since \(x_i\) retains the ordered labels \((a,b)\), the first change away from \(a\) gives a query with labels \((a,b)\). A path containing no query rules out that word on a genuine defect path. The search used mixed-base affine rewriting, following the proof-producing approach of Yolcu–Aaronson–Heule and the whole-progression certificates in PR195, round7/head at 0e8a7f9f965416189b30b57b8aa818fbcb7757c7.

To replay the congruences, start on \(16h+1\). After a prefix, store all states as \(a_jh+b_j\) on the remaining free ordinary parameter. The latest slope is a power of two. To append \(e\), precisely one \(d\in\{0,1,2\}\) makes \(2^e(a_id+b_i)+c_e\) divisible by three. Substitute \(h=3h'+d\) in every previous row, then append the new affine state. Induction gives exactly the ordinary realizations of each entire word on its one source progression. At the indicated index the slope is divisible by \(m\) and the intercept is \(b\bmod m\). Applying this argument to a later substring imposes its past and future congruences on the same intermediate ordinary integer.

At each physical letter check the slope and intercept of the actual row against the domain of one of the five rules \(2s\to s,\ s\to2s,\ 2s+1\to3s+2,\ 3s+2\to2s+1,\ 32s+11\to96s+33\). Check positivity, and at the end require exactly three times the initial affine row. The 116 motifs use 88 distinct paths, 7,115 letters and 193 forward query positions. The maximum path length is 94.

The numbers of strings avoiding every listed motif, from length zero to ten, are
\[
 1,\ 3,\ 9,\ 25,\ 54,\ 65,\ 58,\ 27,\ 8,\ 1,\ 0.
\]
A true source reaches \(17\bmod48\) within nine letters or encounters a certified substring by its tenth. This bounded localization uses intermediate finite comparisons in addition to the three original continuation maps.

## Original-source weights

Keep one possible literal exit at each still-allowed prefix. Its terminal residue imposes one more ternary trit on the original source. At a first blocked prefix use the shortest matching suffix, retaining every forward query position in its comparison path. There are 251 literal exit positions and 503 first blocked prefixes. Of those prefixes, 74 use an entirely ordinary path. The 251 exits together with the retained query positions yield 1,007 possible outputs. At each position the source row \(uh+v\) and output row \(ch+d\) have positive slopes and intercepts. The query is injective on that position's original row and its ratio to the source is bounded by \(\max(c/u,d/v)\). Exact maximization yields \(H\) above. Counting the positions separately handles collisions at different stopping times. The same argument replaces \(1/(uh+v)\) by \(H/(ch+d)\) for reciprocal sums.

PR146's two-sided, bounded-size substitution of all odd defects into \(1\bmod16\), in THREE_RAY_ONE_RESIDUE.md at f431078244e868dc699fad011044f0d5e7f76437, now transfers the full two-sided exponent \(0.84\) from the original variation argument and Krasikov–Lagarias to \(11\bmod32\) and \(17\bmod48\). It does not specify which orientation attains this population. The same source maps transfer the unweighted harmonic criterion under its original fixed-target positive-density premise M. Separately, the forward and reverse basin criteria on \(1\bmod16\) in PR146's THREE_RAY_ONE_SIDED.md and REVERSE_BASIN.md each transfer by the directed theorem here. The implication in either one fixed direction at every positive \(11\bmod32\) source, or at every positive \(17\bmod48\) source, suffices on its own for Collatz.

## Strict sublinear return on an original octave

For all but \(O(X^{49/50})\) positive \(x\in[X,2X)\), both ordinary values \(T^k(x),T^k(3x)\) are \(O(X^{24/25})\) at \(k=\lfloor\log_2 X\rfloor\). The \(k\)-bit parity words permute the complete binary grid, by lifting a parity prefix one bit at a time. Multiplication by three permutes the same grid. An original octave occupies at most a bounded number of complete periods as an upper cover. Each individual upper tail therefore counts at most a constant times
\[
 \sum_{p>3k/5}\binom{k}{p}\le\big((5/2)(3/2)^{-3/5}\big)^k
 \le 2^{49k/50}.
\]
The comparison follows from \((3125/108)^{10}<2^{49}\). For \(p\le3k/5\) the affine coefficient is at most \((3^{3/5}/2)^k\le 2^{-k/25}\), since \(3^{15}<2^{24}\). The additive term is bounded by \((3/2)^k=O(X^{3/5})\), uniformly in the word. Taking the union of the two exceptional sets proves the assertion on original source weight.

One of the two smaller endpoints of a retained true tripling defect has label different from \(f(1)\). The 26-leaf directed theorem of PR146, REVERSE_BASIN.md and ReverseBasin.lean, takes each \(n>1\) to at most \(9n/10\) through at most 61 edges, using forward triplings only at odd multiples of three. All its query sources are bounded by a fixed multiple of \(n\), either from its finite affine rows or from the constant per-move height bound. Following these descents from that smaller endpoint to 1 yields a forward nonunit query \(v\ll X^{24/25}\) with labels opposite-to-\(f(1)\), then \(f(1)\). The nonunit two-successor exchange gives a \(1\bmod16\) source with the same order and height \(O(v)\). Our finite substitution supplies an actual
\[
 y\equiv11\bmod32,\qquad y\ll X^{24/25},\qquad
 (f(y),f(3y))=(1-f(1),f(1)),
\]
where the binary colors are encoded as 0 and 1. The corresponding \(17\bmod48\) witness has the same height order. This step gives strict descent beyond a fixed threshold, and it can be applied again at any subsequent good source. The exceptional-set estimate counts original inputs. Different inputs can share a witness, and the estimate does not show that each witness avoids the next exceptional set. The exception exponent \(0.98\) exceeds \(0.84\). Universal convergence remains open.

The standard parity estimate gives a tradeoff in the two powers. On the same ordinary grid, take \(p\le (94/149)k\). The endpoint exponent becomes \(\theta=(94/149)\log_2 3<1\), since \(3^{94}<2^{149}\); the additive exponent remains smaller. Chernoff tilt \(94/55\) gives an exceptional count \(O(X^{19/20})\). The exact upper-tail comparison is \(149^{20\cdot149}<2^{19\cdot149}94^{20\cdot94}55^{20\cdot55}\). Thus the same directed comparison witness has sublinear height \(O(X^\theta)\) at the resident \(19/20\) exceptional power, with less height saving than the \(24/25\) choice above. The new conclusion of these forward estimates is the actual ordered \(11\bmod32\) or \(17\bmod48\) witness at the resulting height.

Directed11Motifs.json has SHA-256 d2acc996d6f97b171891d542255eadb936533a4bfcdb8415aa05a19c3c361665. The independent integer replay in check_directed11.py evaluates the whole-source progressions and their query menus. The sublinear-return and counting deductions above are written arguments.
