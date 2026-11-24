# Central fixed-target fibers, short paired returns and the cost of retaining the target

**PROPOSED written theorems with the analytic inputs identified below.** For every supplied ordinary unit `q`, every sufficiently large central clock row contains a near-optimal family ending at one actual pair `(q,Y)`. A single short extension of their binary cylinders gives complete ratio-five marks, equal odd counts and bounded real offset at a common ordinary target `Q`. We locate its entire fine ternary cell. Its least positive lift can be exponentially large even though the extension takes sublinear time. An independent physical rigidity theorem excludes fixing a mismatch at a nonperiodic `q` by replacing an arbitrary short terminal segment, even separately for every source. The fixed-target paired estimate PT and universal Collatz remain **OPEN**.

Use the positive shortcut map $T(2n)=n$, $T(2n+1)=3n+2$, and write $P_e(x)$ for the number of odd inputs before clock $e$. A unit is a positive odd integer prime to three. For a chronological parity word of length $e$ with $p$ odd inputs, put $2^eT^e(x)=3^p x+C$, $G=2^e/3^p$, and $\beta=C/2^e$. Thus $x=G(q-\beta)$ when the endpoint is $q$. A completed mark has odd first-arm endpoint $z$, companion endpoint $5z$, and equal cumulative odd counts. Its parsing uses first positive returns followed by all common halvings before the next odd sentinel.

## 1. Concentration at an actual companion endpoint

**R7-R1.** Fix a unit $q$ and a positive integer $m$. Let $p$ be sufficiently large, $|e-2p|\le\sqrt p/2$, and $L=\sqrt{e\log(2e)}$. There are one integer $Y>0$, one signed integer $k$, and at least
$$
                 G\exp(-O_{q,m}(L))
$$
distinct units $x\equiv1\pmod 3$ with
$$
 T^e x=q,\quad P_e(x)=p,\quad 0\le\beta_x\le1/2,\qquad
 T^e(mx)=Y,\quad P_e(mx)=p+k.
$$
Here $|k|+\log(1+Y)=O_{q,m}(L)$. This is a pointwise assertion for each supplied $q$ and every indicated large row. The same $Y,k$ serve the entire selected row family. They can vary with the row, and in R7-R1 neither $Y=mq$ nor $k=0$ is ensured.

We use two separately source-qualified inputs.

* **F.** Weaver and Wren, paper 48 v2, Lemma 7, equation (76), and the bounded initial branch in the proof of Theorem 8. In PR203's extraction, each sufficiently large odd depth $b$, each total $|s-2b|\le\sqrt b$, each fixed unit target, and each unit source class modulo $3^K$ with $1\le K\le\delta_*(b-1)$ have at least $c 2^s/(3^{b+K}\sqrt b)$ distinct ordinary unit inverses with $\beta\le F_*$. Only $K=1$ is needed here. The individual gap cap and the much larger range of extra digits are available in F. The floor concerns independent geometric gaps before conditioning and one physical first arm. [Paper 48 v2, Lemma 7 and Theorem 8](https://rstation.ai/problems/collatz/papers/48/v2) · [PR203 at 3f2c89f12b057b8bb8655bd6fc794c772aa8b65d, section 3](https://github.com/GettysburgResearch/collatz/blob/3f2c89f12b057b8bb8655bd6fc794c772aa8b65d/research/mixed-adic-basin-density-20261124/README.md)
* **H.** Shaik, manuscript v4.0.2, Corollary 1.2 and the proof of Proposition 6.4, section 6, “Shortcut and unaccelerated time estimates.” For any fixed $w>0$ choose a fixed $A$ with $A/(2A_{\rm FP})-1/2\ge w$. With at most $O_A(N/(\log N)^w)$ exceptions through $N$, an ordinary $n$ has a witness $t$ satisfying $T^t(n)\le(\log n)^A$, $|t-c_*\log n|=O_A(\sqrt{\log n\log\log n})$, and $|P_t(n)-t/2|$ with the same bound, where $c_*=2/\log(4/3)$. The proof takes the actual full-map clock $t+P_t(n)$; equality of two visited values by itself would not identify that count on cycles. We use the written fixed-exponent estimate. We did not rebuild that manuscript's formalization. [Full primary manuscript, sections 1 and 6](https://shaikidris.github.io/polylog/paper/) · [Manuscript version](https://doi.org/10.5281/zenodo.23132901)

For the bounded offset at *every* $q$, select a fixed $u\ge6$ with $q_0=(2^u q-7)/9$ a positive odd unit, $q_0>F_*+1$, and $(9F_*+7)/2^u\le1/2$. Such $u$ occur in unbounded arithmetic progressions since two generates the units modulo 27. The ordinary A branch has $T^u(q_0)=q$ and two odd inputs. Apply F to the target $q_0$, first-arm class one modulo three, $b=p-2$, $s=e-u$. This is in F's central window eventually, since $u$ is fixed. Append the actual $u$ steps on the first arm. This gives at least $c_qG/\sqrt e$ distinct starts in $[(q-1/2)G,qG]$ at exactly $(e,p)$. We have imposed no companion condition in this operation. [A branch with ordinary legality, round six](../../round6/renewal/README.md)

For $n=mx$ the map $x\mapsto n$ is injective and $n\asymp_{q,m}G$. Also
$$
 \log G=e/c_*-(p-e/2)\log 3,\qquad c_*\log n=e+O_{q,m}(\sqrt e).
$$
Apply H with $w=2$ through $N=\lceil mqG\rceil$. Its *original-source* exceptional count is $O_{q,m}(G/e^2)$, strictly smaller than the fixed-row population even if all these exceptions occur in the row. No conditional distribution of companion paths is used. Every remaining $n$ has $|t-e|=O_{q,m}(L)$ and $T^t(n)\le O_{q,m}(e^A)$. If $t\ge e$, then $T^e(n)\le2^{t-e}T^t(n)$. If $t<e$, apply $T(z)+1\le(3/2)(z+1)$ forward. Thus $\log(1+T^e(n))=O(L)$. Since each physical step uses at most one odd input, $|P_e(n)-p|=O(L)$ as well. There are at most $\exp(O(L))$ possible integer pairs $(Y,k)$. Pigeonhole gives the claimed multiplicity.

There is a slower version of R7-R1 under F and Inselmann in place of H, with $o(e)$ in place of $O(L)$. For fixed $\epsilon>0$, Inselmann's Theorem 2.18 gives power-saving exceptional counts for the full trajectory bounds up to $c_*\log n$ (the paper calls this *-dense). At the integer part of that clock the upper bound is $O(n^\epsilon)$; moving $O(\sqrt e)$ clocks to $e$ costs $\exp(O(\sqrt e))$ as above. For odd counts, let $0<\epsilon<1/4$. The trajectory lower bound ensures $T^i(n)\ge n^\epsilon$ up to $i\le(1-2\epsilon)c_*\log n$. The logarithm of the product of the corrections $1+1/(3T^i(n))$ there is $O(e n^{-\epsilon})$. The remaining $O(\epsilon e+\sqrt e)$ corrections through $e$ have logarithms bounded by $\log(4/3)$. The exact identity $T^e(n)=n3^{P_e(n)}2^{-e}\prod(1+1/(3T^i(n)))$ and $1\le T^e(n)\le\exp(O(\epsilon e+\sqrt e))$ give $|P_e(n)-p|=O(\epsilon e+\sqrt e)$. For fixed $\epsilon$, an exception bound $O_\epsilon(N^{1-D_\epsilon})$ is $o(G/\sqrt e)$ at the supplied $q,m$. Take the sufficiently-large-row threshold for each fixed $\epsilon$ first, then use $\epsilon=1/j$ along increasing thresholds. The argument requires no uniform estimate for $D_\epsilon$ as $\epsilon$ decreases. [Inselmann, arXiv:2402.03276v3, definition of *-density and Theorem 2.18](https://arxiv.org/html/2402.03276v3)

## 2. Actual complete marks after one short binary extension

**R7-R2.** Take $m=5$ in R7-R1. One can select $h=O_q(L)$, $0\le a\le h$, $0<M<2^h$, and an ordinary unit $Q$ such that, with $P=p+a$, $E=e+h$ and $G'=2^E/3^P$,
$$
 2^h Q\equiv M\pmod{3^{P+1}},\qquad
              (M+3^{P+1})2^{-h}\le Q<1+6\cdot3^P.                 \tag{1}
$$
At every ordinary unit in this single fine cell there are at least $G'\exp(-O_q(L))$ distinct chronological words with complete ratio-five marks at $(E,P)$, first-arm offset at most $1/2$, both physical endpoint labels and equal odd counts. In particular caller $Q$ is an actual positive integer. The two sources at $Q$ have the form $(x+2^e t,5(x+2^e t))$ for one $t$ shared by all the selected $x$. Since $P/E\to1/2$ and $h=o(p)$, these are near-optimal central *paired* rows. Their supplied first-arm target in R7-R1 was $q$. Formula (1) gives $\log Q=P\log3+O_q(L)$.

To prove this, retain R7-R1's common $Y,k$. On all translations by $2^et$ the two endpoints at $e$ are exactly
$$
             q+3^pt,\qquad Y+5\,3^{p+k}t.
$$
Both old parity words persist under such translations, including the possibly different companion words of the different starts. All endpoint pairs therefore have the same signed state $k,D$ with $D=3^{k_-}Y-5\cdot3^{k_+}q$, $k_\pm=\max(\pm k,0)$. The state and the future first-arm bit determine the future companion bit. PR146's integer steering reaches state $(0,0)$ in
$$
 g=O(1+|k|+\log(2+|D|))
$$
more first-arm bits. The bound follows from its proof: remove the nonzero levels in at most $3|k|$ steps. Throughout, the magnitude of the offset at the next step is bounded by $(3|D_i|+6\cdot3^{|k|})/2$, as the algorithm never increases the magnitude of a nonzero level before its removal. At level zero the amortized logarithmic bound in section 1 of that proof gives the rest. Thus $g=O_q(L)$. An odd first-arm parameter slope makes all chosen bits legal on a binary subclass. [PR146 at f431078244e868dc699fad011044f0d5e7f76437, section 1](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/FIVE_RETURN_IN_EVERY_CLASS.md)

After that root prescribe $b=g+\lceil\log_2(q+2)\rceil+2$ common even steps and then an odd sentinel. Put $h=g+b$. The whole suffix has $a$ first-arm odd inputs and carry $C_\sigma$, and set $M=3^a q+C_\sigma$. Formally evaluating its real affine map at $q$ gives $0<M/2^h\le2^{-b}(3/2)^g(q+1)<1$. The old first-arm offset was at most $1/2$. The new offset is at most $2^{-b}(3/2)^g(1+1/2)<1/2$. Both estimates follow by one-step iteration on nonnegative real arguments, independent of physical parity of the argument used in the estimate.

A common lift may now be taken with $0\le t<3\cdot2^{h+1}$ and $t\equiv0\pmod3$. Its binary condition is
$$
              3^{p+a}t+M\equiv2^h\pmod{2^{h+1}}.
$$
Indeed the parity word of length $h$ together with its next odd sentinel is one binary cylinder, and $3^{p+a}$ is odd. This solution supplies all suffix parities by the ordinary affine row decoding. It preserves the unit class of all old sources. The common terminal value is $Q=(3^{p+a}t+M)/2^h$, an odd unit since every start was a unit and $T$ preserves units modulo three. The lifted starts are still distinct. At this clock the companion endpoint is $5Q$, and its odd count is $p+k+(a-k)=P$. Scanning consecutive first returns from the original odd source and consuming each even padding up to its odd sentinel parses the entire word, since the final endpoint is itself an odd root. All these words have positive first arm, bounded real offset, and full unit legality on the entire fine cell modulo $3^{P+1}$. Distinct first-arm prefix words remain distinct. The change from $G$ to $G'$ costs at most $\exp(O_q(L))$.

Since $0<M<2^h$, every positive member $y$ of that cell satisfies $2^hy-M>0$. This difference is a multiple of $3^{P+1}$. This proves the lower bound in (1), while the displayed upper range for $t$ gives the upper bound. The extension therefore gives an explicit family of good fine cells with *no* small ordinary representative, although the dyadic centers $M/2^h$ have subexponential numerator and denominator. These fast symbolic corrections cannot be counted as fixed-target predecessors of $q$.

## 3. An exact barrier to repairs confined to the end

**R7-R3, unconditional.** Suppose an ordinary word of length $e$ and weight $p$ takes $x$ to a fixed positive $q<3^p$. Suppose $z>0$ follows those same $e$ first-arm parities and reaches $r>0$ after a further $h$ physical steps, with any suffix chosen after seeing $z$. If
$$
                         2^h r<q+3^p,                                \tag{2}
$$
then $z=x$ and $r=T^h q$. Indeed the common carry and coprimality of $2^e,3^p$ give $T^e z\equiv q\pmod{3^p}$. Positivity gives $T^e z=q+3^p t$ for an integer $t\ge0$. The physical bound $T^e z\le2^h r$ and (2) force $t=0$. The same first-arm affine row then forces $z=x$. At nonperiodic $q$, any positive suffix from such a lift back to $q$ requires $h\ge\log_2(1+3^p/q)$. This assertion does not require equal suffixes, a pair law or a Fourier estimate.

Allow a more general edit. Delete the last $j$ bits of the original central word and replace them with $h$ arbitrary new steps, again requiring the endpoint $q$. The retained prefix has at least $p-j$ odd inputs and endpoint $y\le2^j q$. If
$$
                    q\,2^{\max(j,h)}<3^{p-j},\qquad j\le p,          \tag{3}
$$
the same argument forces the *same physical source* and the new suffix follows the actual future of $y$. When $q$ is nonperiodic, it can be visited only once, hence $h=j$. All companion parities and the terminal $Y,k$ are then unchanged as mathematical consequences of determinism. In particular replacing a terminal $o(p)$ segment of an already fixed-target family by another $o(p)$ segment cannot repair an incorrect companion. A construction that changes earlier parities, or selects the companion condition in the original inverse law, is outside this barrier.

## 4. Ordinary harmonic components and the tripling test

**R7-R4, unconditional.** The ordinary graph of all complete ratio-five inverse blocks admits an explicit nonconstant bounded function constant on *every* edge. Consequently any stochastic kernel supported on finite outward concatenations, including a finite-mean reweighting of the actual complete marks, has a nonconstant bounded harmonic function on all ordinary units.

Each ordinary source has at most one forward first-positive-return-plus-padding parent. Terminal means that this parent does not exist. The units $1$ and $5$ are distinct terminals. For $1$ the arms coalesce at clock 3, and for $5$ they coalesce at 15. No earlier positive clock is an equal-odd-count ratio-five return; the numerical ratios at clocks 11 and 12 for $5$ have counts 5 and 6. After coalescence, positivity precludes ratio five forever. Define $H(x)=1$ when iterating the partial parent reaches $1$, including zero iterations, and $0$ otherwise. A parent edge equates the two $H$ values, including at a child of $1$ because $1$ has no parent. Thus $H(1)=1,H(5)=0$ persist under every supported kernel and every finite induced jump. True Collatz convergence has value one at both terminals. This invariant disproves ordinary full-space Liouville for the stated kernels; it does not distinguish genuine basin labels. The two-child A law alone is a finite-mean example (two admissible exponents in $[6,23]$ at each parent, uniform choice).

R7-R1 also applies at $m=3$. Suppose $q$ is an actual failed unit with $q$ reaching one and $3q$ not reaching one. F and the nonperiodic depth construction in PR203 give at least $c_q X$ distinct odd units $x$ in $[X,2X]$ reaching $q$, with central clocks up to fixed prefix/suffix shifts. Impose the two congruences mod 2 and mod 3 in that construction. PR146's direct *ordinary nonmeeting* bound for $x,3x$ discards at most $O(X/\sqrt{\log X})$ odd starts in that interval. Thus on a $1-O_q(1/\sqrt{\log X})$ fraction of this bank, $3x$ meets the trajectory of $x$ and reaches one. All of those companions have the opposite convergence label to the desired $3q$. This gives a quantitative obstruction to extracting a smaller failed directed source from typical one-arm pullbacks. The upper bound still permits a fixed-row fraction as small as $\exp(-o(e))$, and in particular a total count $X\exp(-C\sqrt{\log X})$. It supplies neither the lower bound on the exceptional part nor a contradiction. [PR203, fixed-target depth bank §§2–4](https://github.com/GettysburgResearch/collatz/blob/3f2c89f12b057b8bb8655bd6fc794c772aa8b65d/research/mixed-adic-basin-density-20261124/fixed_target_depth_bank.md) · [PR146, ordinary tripling upper bound](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md)

**First unsupported step toward PT.** R7-R1 leaves a definite row multiplicity at a specific moving state, while PR200's fixed-menu suffix requires the row to occupy its *preassigned* state menu at its selected ordinary target. R7-R2 pays for returning that state in the clock but fails the ordinary height requirement (1). R7-R3 excludes a short physical tail replacement at any nonperiodic supplied target. An input proving adequate fixed-target mass for the required relative state during the original central block is still missing. Even PT for the five comparison would need a genuinely opposing estimate on its own failure set or another closing argument. [PR200, finite-menu reduction at abf36c63b4d0181541d7e029d390d6f636940750](https://github.com/GettysburgResearch/collatz/blob/abf36c63b4d0181541d7e029d390d6f636940750/research/regularity-rigidity-20261124/pointwise-fibers/COMMON_SUFFIX.md)

[Lean kernel](ShortSuffix.lean) · [Finite controls](check.py) · [Execution receipt](../../../../reports/astra-global-closure-20261124/round7/renewal/EXECUTION.md)
