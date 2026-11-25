# Primary literature and the frozen repository frontier

**Scope.** The sources below were opened during this pass. Published statements, new deductions from them, and unresolved repository proposals are kept distinct. A theorem from a recent manuscript is not treated as a completed proof of Collatz or of an unrelated conjecture.

## Literature actually used

| Primary source | Exact use here | Hypothesis retained |
|---|---|---|
| [K. Monks, K. G. Monks, K. M. Monks and M. Monks, *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*, Theorem 4.1 and preceding definitions](https://www.mathematicalgemstones.com/maria/papers/mmmm.pdf) | Places a prescribed finite return chain in any fixed positive component containing a 3-unit; motivates the explicit two-odd entrance | The bound is on inverse odd branches, not total clock count or height. A finer modulus enforces a one-sided progression. The selected triple's color is not supplied. |
| [K. Yu, *p-adic logarithmic forms and group varieties II*, Acta Arith. 89 (1999), 337–378, Theorem 1](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf) | Applies to `2^k * (517727*x/203816) - 1` at the prime 3; bounds its valuation by a fixed-input constant times `log max(3,k)` | The two rationals are 3-adic units; the expression is nonzero; the number-field condition holds over Q at 3. The constant depends on fixed x. |
| [M. Inselmann, *An Approximation of the Collatz Map and a Lower Bound for its Average Total Stopping Time*, arXiv:2402.03276v3, Theorems 3.1 and 3.3](https://arxiv.org/html/2402.03276v3) | Guides the scalar ordinary-interval height and parity estimates; the packet supplies a separate sliding-block first-passage proof | A typical successful time does not automatically bound additive error at first entrance. The new logarithmic error and original-parent fibre argument are derived in `source/README.md`. |
| [T. Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum Math. Pi 10 (2022), e12, Proposition 1.17](https://doi.org/10.1017/fmp.2022.8) | Identifies what the established Fourier mixing estimate controls | Its specified random valuation law cannot be conditioned without proof on two actual colors or a short source interval. It is not used as a missing gate-color estimate. |
| [D. Applegate and J. C. Lagarias, *Lower bounds for the total stopping time of 3X+1 iterates*, Math. Comp. 72 (2003), 1035–1049, Theorem 4.1](https://arxiv.org/abs/math/0103054) | Informs the inverse-tree search and separates a ones-ratio certificate from a minimum-basin competitor | The inverse-tree result does not give a point below the floor for an arbitrary chosen cycle endpoint. |

The source lane also compares the precisely stated scalar manuscript of [Shaik, Corollary 1.2](https://shaikidris.github.io/polylog/paper/); its statement is not substituted for or needed to justify the new first-passage proof. The primary papers and exact internal source pins are recorded in each lane.

## Two heavy tools already present at the current frontier

**Subspace Theorem.** PR210 applies the three-place theorem at infinity, 2 and 3 to a repetitive critical backwards script. The relevant published statement is [J.-H. Evertse, *The p-adic Subspace Theorem*, May 2011, Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf). For approximants with clock monomials `X,Y` and numerator `N`, the proposed product bound is `|N| * 3^-m`, with fixed forms. Under the stated repeat and height hypotheses this gives rationality of an algebraic limiting coordinate. It does not establish that a critical limit of a fixed ordinary orbit is algebraic, balanced, repetitive, or confined to finitely many rational phases. Ordinary integer finite approximants alone do not supply any of those assertions. We reviewed the arithmetic setup; the entire rational-classification program is not imported as a verified dependency of this packet.

**Idempotent Fourier measures.** PR193's global criterion uses the Cohen–Helson–Rudin theorem, as stated in [Green and Sanders, *A quantitative version of the idempotent theorem in harmonic analysis*, Ann. Math. 168 (2008), 1025–1054](https://annals.math.princeton.edu/2008/168-3/p09). A bounded subsequence of symmetric Fejer measures for the actual bad-color indicator would have an idempotent limit and eventually periodic support. The repository proves the remaining ordinary-color rigidity. The missing assertion is the bounded subsequence, equivalently summability of the exact dyadic norm increments. Small scalar exceptional sets and the present head regeneration estimate do not bound that total variation.

## Frozen intake

| PR | Full head inspected | Relevant new work |
|---|---|---|
| [192](https://github.com/GettysburgResearch/collatz/pull/192) | `1f1d3d690d7517e1b2a44b5f2f4930bd45b63302` | Previous diagonal transport, inverse optima and unrestricted-height grid obstruction; base of this pass |
| [195](https://github.com/GettysburgResearch/collatz/pull/195) | `99a4ab3f808c01acd115ef08eee42a8b886d5d4c` | Round 12 complete-denominator factor constraints, fixed-template obstructions and rational basin controls |
| [197](https://github.com/GettysburgResearch/collatz/pull/197) | `10d87fee615d1095990d6b7ea329126b4cf7aa5a` | Paired guarded returns, actual first-passage source architecture and source-qualified resampling |
| [201](https://github.com/GettysburgResearch/collatz/pull/201) | `02fb390a76fb2ffb00fee612649ca23a82d99d31` | Logarithmic-depth ordinary thin-band amplification; its own cofinal absence remains open |
| [193](https://github.com/GettysburgResearch/collatz/pull/193) | `aa0b01234735683b413098b81afdf764de503730` | All-lifts inverse merger and the global Fejer criterion |
| [210](https://github.com/GettysburgResearch/collatz/pull/210) | `592328fecf8ea2cf41736294856d95f890a1ba98` | Critical record rational classification and repetitive-script Subspace-Theorem proposal |
| [146](https://github.com/GettysburgResearch/collatz/pull/146) | `f431078244e868dc699fad011044f0d5e7f76437` | Source-qualified native pair fusion on every ordinary interval |
| [205](https://github.com/GettysburgResearch/collatz/pull/205) | `32d722c5d5597846da5dad842c8ea15742abc176` | Bounded least-disagreement height strip and the distinct first-crossing alternative |

These pins describe the reviewed state, not an assurance about later branch heads. No external branch was merged into the current packet.
