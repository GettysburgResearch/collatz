# Independent review of the signed-prefix transport

**VERIFIED at the narrow claims below.** I reconstructed the lower/upper source projections of *common_phase*, *upper_certificate* and *replace_without_query*, the height comparison for the listed negative-center competitors, and the hypothesis needed to use a smaller ordinary bad member. This review does not establish total coverage by such competitors.

## Frozen inputs

| File or declaration | Identity |
|---|---|
| SignedPrefix.lean | SHA-256 8538fd9b00b33c1f73dada4a2830c2edf9741f4cf4a7ccc86608fabe95f58e0c |
| check_transport.py | SHA-256 ffa3831ebc6a4e70b01cc43497b78b9b25430fa103cf12fb5a22cd71807afdab |
| competitors.json | SHA-256 9e74efd63542d437c574a06399fee79e03c7a4cb0f432c86b8f6558b34fcc420 |
| Base SourceDeletion.lean, MinimumFailure.lean | Parent 570476be82f706122cdd23ebd7a00f3d4ff90cd8, SHA-256 21227f38df7f95b29613ec322a1e48f3fc0e423155fb12867c9dfcf546699af0 and 988435d6a6e986d20293593037765775e951a73f1f74e712690ba6ddfc4334c4 |
| bounded_return | PR197, 156652e03fe7a78f9cd4442039779cc622fdf3de, research/ayh-resource-reset-20261124/closing-proposal/QuantitativeReturn.lean |

## The two actual ordinary lower inputs

Use $T(z)=z/2$ for even $z$ and $(3z+1)/2$ for odd $z$. The denominator-$d$ reference updates the signed numerator $a$ by $a/2$ at even $a$ and $(3a+d)/2$ at odd $a$. Its parity is the Euclidean residue in $\{0,1\}$, including negative $a$. If $d$ is odd and $dz=a+2v$, then $z$ and $a$ have equal parity, and the new numerator displacement is $v$ or $3v$ respectively. Applying this argument $j$ times to $dz=a+2^{j+r}t$ gives
$$
 dT^jz=S_d^j(a)+2^r3^ot ,
$$
where $o$ is exactly the number of odd **inputs** on either length-$j$ path. For $d=3^q,\ S_d^j(a)=3^q b,\ o=q+m$, cancellation gives $T^jz=b+2^r3^mt$. A possibly negative $b$ is allowed, while $T^jz$ remains an ordinary natural number. The signed reference need not be an ordinary source.

In *common_phase* invoke this equation at two different ordinary lower inputs, $z$ and $w$, with their own signed seed, clock and denominator. The common quantities are $b,r,m,t=1$. Thus $T^jz=T^kw$. Since true basin membership is invariant under all finite forward clocks, $\operatorname{Good}(z)\leftrightarrow\operatorname{Good}(w)$. Neither signed phase has been declared good, and no new basin test is used.

## The rival upper arm and its exact cost

The rival seed contains $3^{R+1}w$. On its **lower** path that makes $q=R+1$. On its **upper** path it is $3^R(3w)$, giving the ordinary source $3w$ and reference denominator $3^R$. The same numerator $c$ appears with these two distinct denominators. The clock identity $k+r=l+t$ ensures a common binary power in both seed equations. If $S_{3^R}^{l}(c)=0$ with exactly $R$ odd inputs, then $T^l(3w)=2^t$, followed by $t$ literal halvings to one. The resulting certificate has exactly $l+t$ shortcut clocks and $R$ odd inputs. In *replace_without_query*, badness of the original lower $z$ passes to $w$ at the ordinary meeting above. The supplied hypotheses construct a witness for the rival upper arm without a fresh basin query.

This result does not assert that $w<z$, that $w$ is odd, that the displayed witness is a first hit, or that its odd count is at most the original upper count. These are separate conditions when any is needed. In the finite competitor application the height comparison and seed parity give a **smaller positive odd** reverse disagreement. Upper rank may increase from two (up to five in the supplied tables). This is valid for least **height** over all positive odd reverse disagreements and cannot be used as a decreasing rank argument. A mere smaller bad vertex does not qualify on that basis alone. The other route first finds a positive bad vertex $x$ with $2^{40}x<z$. PR197 *bounded_return* accepts precisely that source and returns a reverse defect $w\equiv17\bmod48$ with $w\le2^{40}x<z$. Its upper membership carries no quantitative rank guarantee.

## Arithmetic of the competitor classes

For the old and new inputs write $z=(2^H-c_0)/27$ and $w=(2^{H+\Delta}-c')/3^{R+1}$. Once the signed reference reaches the same negative integer $-s$, choose its entry clocks and accumulated odd counts $(i,q)$ and $(i',q')$. A shared signed cycle of length $P$ has $O$ odd inputs. Set
$$
 O\,\Delta k=q-3-q'+R+1,\qquad \Delta=i'-i+P\Delta k .
$$
Taking $k=\lfloor(H-i)/P\rfloor$ laps on the old side and $k+\Delta k$ on the rival leaves precisely the same binary exponent and the same ternary exponent after division by the respective denominators. The routine checks divisibility by $O$ before taking $\Delta k$, nonnegativity at the initial admissible cutoff, the complete seed congruence modulo $3^{R+1}$, and positivity. The upper odd clocks are the prescribed gap prefix reaching signed zero and the subsequent halvings. The strict height inequality after clearing the powers of two is linear in $2^H$. A strictly favorable leading coefficient and a strict inequality at $H=1600$ imply it at all later admissible $H$.

I reconstructed the charts independently from the gap list, then directly iterated the two positive lower sources and both upper triples. On every compatible clock $1600\le H\le2571$ for the 173 listed competitors, all 2,086 comparisons had $0<w<z$, equal physical lower endpoints, an old upper hit with two odds, and a new upper hit with $R$ odds. This covered exactly 1,043 distinct pairs $(e,H\bmod486)$, consistent with 91 of 1,134 pairs remaining after this comparison. Each surviving pair represents an infinite clock progression. This finite replay corroborates the phases and cost convention. Uniformity in $H$ follows from the arithmetic just described. [Independent direct replay](review_chart_paths.py)

I also built SourceDeletion, MinimumFailure and SignedPrefix into a fresh temporary object directory with Lean 4.34.1, compiler 5045d0056413266e57c625dcd7c365b10e377c52, and warnings as errors. All nine SignedPrefix axiom queries passed, listing only propext, Classical.choice and Quot.sound. The source-level projection check of PR197 is distinct from a rebuild of that external file. [Transport source](../../../research/astra-full-proof-20261125/transport/SignedPrefix.lean)

## Final wording and additional hypothesis checks

I read the corrected transport README at Git blob 7b027a082e3dfeef661a2aef1687c7d392191381, SHA-256 edcd3312e48fa027c79718f441e799020a95640e77275753a254c4bb65c88d4f. Its two routes to a smaller unrestricted disagreement have the distinct charges verified above. I also reran the author's entire checker with optimized Python and obtained the stored JSON exactly, including 16,733 short sources, 158 direct drop rows, one ancestor row, 42 comparison rows, and 91 residual pairs. For the large first gap, $e=2+2k+v$ with $k\ge100$, the two lower odd steps from $z\equiv3\bmod4$ reach $(9z+5)/4=1+2^{e-2}u$. The identity $T^2(1+4v')=1+3v'$ gives the stated lower endpoint. The strict inequality at $k=100$ absorbs the constant terms for $2^v u\ge1$ and persists at larger $k$. This covers exactly the large-gap implication in the prose.

For the separate canonical suffix, if the upper endpoint at clock $L$ is $u>2$, a previous hit of one is impossible because all subsequent states would be one or two. Hence an arbitrary supplied upper hit contains the complete prefix and the remaining suffix loses exactly two odd inputs. For odd $u$, the states $1+3^{k+1}u$ and $3^ku$ really do have the same successor, by the even and odd branch formulas. The latter statement transfers badness. It does not by itself turn the good base $u$ into a reverse disagreement with good triple; the orientation change and the separate height criterion in the prose are necessary. I inspected these assertions in CanonicalSuffix.lean, SHA-256 ea9b3eeb4ea69004d5aac7a7cba18eb17f6943f581c515f8369ef7d87edf9962. My independent compiler run covered SignedPrefix and its two base dependencies. [Transport proof and coverage](../../../research/astra-full-proof-20261125/transport/README.md)
