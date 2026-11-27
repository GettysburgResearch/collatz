# The critical width of the unweighted binary four-segment count

**PROPOSED, with an exact rational certificate.** Let \(2^{e_i}x_{i+1}=3x_i+1\) describe a primitive positive rational odd cycle of odd period \(P\), common reduced denominator \(d\), and exponents \(e_i\in\{1,2\}\). Write \(\theta=P^{-1}\sum e_i\), \(E_i=\sum_{j<i}e_j\), and \(W=\max(E_i-i\theta)-\min(E_i-i\theta)\). There is a constant
\[
             1.98534327 < W_* < 1.98534329
\]
such that, for each **fixed** \(W_0<W_*\), cycles of \(W\le W_0\) satisfy \(d\ge P^{c(W_0)}\) for all sufficiently large primitive periods. In particular each fixed denominator supports finitely many cycles in this class. This uses PR200's four-segment source estimate, its fixed-place Subspace Theorem input, and the source-qualified irrationality exponent at most three of \(\log_2 3\). The onset is ineffective. The rational arithmetic below is new; the analytic transfer and external theorems are retained inputs. The previous sufficient cap was \(99/50\). [PR200 at 2346db2d, four-segment proof](https://github.com/GettysburgResearch/collatz/blob/2346db2d49030ef385b73e1ee3e27dcbff86d2d9/research/six-hour-20261127/cycles/FOUR_BRIDGE_BINARY_CYCLE_BOUND.md) · [Weaver, Paper 145/v1, Lemma 4](https://rstation.ai/problems/collatz/papers/145/v1) · [Chudnovsky, ratio theorem](https://arxiv.org/abs/2610.28079)

## Return frequencies and the exact fourth moment

In the two-layer representation a local date is \(\lfloor i\theta+t\rfloor+z_0-z_i\), with \(z_i\in\{0,1\}\). The bit must be zero when \(f_i=\{i\theta+t\}>w=W_0-1\). A mechanical letter one allows only a weakly decreasing bit, and a letter two allows only a weakly increasing bit. When four copies of a conditioned segment have equal pair-sums of their ordinary affine numerators, their two bit-pair sums agree at every date. Indeed expressing the powers of two as \(2^{v_i}(2-z_i)\) after one uniform doubling and peeling the last available ternary digit gives a bit-sum difference divisible by three and in \([-2,2]\). Induction gives the assertion; the converse is immediate. These are the ordinary numerator and the exact local transition of the pinned four-segment proof.

At a forced site all four bits are zero. Between consecutive forced sites the number \(F_n\) of returning quadruples is the zero-to-zero entry of the prescribed transfer product. For \(0.9853\le w\le0.9854\) and \(\alpha=\log_2 3-1\), put
\[
        L=1-w,\qquad u=53\alpha-31,\qquad v=55-94\alpha .
\]
The following are Lebesgue frequencies **per original date** of starts of each return word. A return of length \(n\) contributes once, with no extra factor \(n\). The table omits the finitely many isolated partition endpoints, which have zero limiting frequency.

| Return length | Frequency | \(F_n\) |
|---|---|---:|
| 53 | \(L-u\) | 17778623164916750424132973 |
| 94 | \(L-v\) | 814142973180663320799016177501290226148687690 |
| 147 | \(u+v-L\) | 21492223200414094275800099834565366836969886189515023336083934482791192 |

Here \(53(L-u)+94(L-v)+147(u+v-L)=1\). The test cuts the return interval at all preimages up to date 147 of the seam and the forced-site boundary. It checks the unwrapped integer labels and the order of all relevant affine cuts at the four corners of a rational slope and width rectangle enclosing the table. Extremality of affine functions on rectangles preserves these comparisons throughout. At the midpoints of the resulting cells it follows the actual schedule to the first strict return and multiplies its nonnegative integer matrices. The return frequencies are affine in both parameters there and agree with the table at each corner. Logarithm enclosures use the convergent positive atanh series with a geometric remainder bound. [Exact certificate and constants](check_bridge_pressure.py)

For the complete local language with this forced-zero cap, the asymptotic base-three log fourth-energy per date is exactly
\[
 \Gamma(w)=(L-u)\log_3 F_{53}+(L-v)\log_3 F_{94}
                      +(u+v-L)\log_3 F_{147}.                       \tag{1}
\]
This remains valid for arbitrarily chosen starting angles, for lengths tending to infinity and slopes tending to \(\log_2 3\), including rational slopes. To see uniformity, every subsequential limit of the empirical phase measures is invariant under rotation by the irrational \(\alpha\). Testing a continuous function proves invariance by telescoping and uniform continuity as the slope tends to its limit. The only such probability is Lebesgue. Moving interval endpoints converge, and the proportion of visits near any of the finitely many endpoints is consequently arbitrarily small. There is a uniform finite return bound even at an exceptional point. Finitely many translates of a fixed open subinterval of the forced interval cover the compact circle under the irrational rotation, and the cover persists for sufficiently nearby slopes. Thus exceptional visits and the two incomplete end pieces cost \(o(n)\) in the log energy of an \(n\)-date segment. The other complete forced-to-forced factors multiply exactly. Prescribed feasible initial and final bits cost at most a bounded number of dates at the first and last forced cut. This also proves the upper estimate when a prescribed segment is infeasible.

By the rational enclosures in the certificate, \(\Gamma(0.98534327)<1<\Gamma(0.98534329)\). On this bracket equation (1) is affine with positive slope. Define \(W_*=1+w_*\), where \(\Gamma(w_*)=1\). For \(W_0-1<w_*\), enlarge the cap to at least \(0.9853\) if necessary. The full segment energy is bounded above by \(3^{\gamma n}\) for all sufficiently long segments on any sequence of slopes approaching \(\log_2 3\), for some fixed \(\gamma<1\). PR200's source estimate gives \(\liminf\log(dX)/\log P\ge3/\gamma>3\) along any sequence with \(P\to\infty,\ \log d=o(\log P)\), where \(X=\max x_i\). Its elementary bound \(X\le2^{W_0}/(2^\theta-3)\) and the supplied irrationality exponent give the contradictory upper exponent three. If no denominator power held, one could choose precisely such a sequence. The cutoff \(W_*\) is an energy threshold for the specified complete two-layer path population. A cycle may impose further restrictions. No claim of a cycle at or above this width follows.

## Every fixed even moment in the unforced two-layer population

Removing forced zeroes restores the full allowed binary transition at every date. For \(k\) positive and \(k\) negative copies, any tuple with coordinatewise equal \(k\)-bit sums contributes to an exact ordinary numerator equality. This gives a lower bound at every \(k\). It is an equality at \(k=2\) by ternary peeling. If \(v_j\) counts matched tuples of common grade \(j=0,\ldots,k\), the next grade \(\ell\) has count
\[
 \sum_{j\le\ell}{k-j\choose\ell-j}^{\!2}v_j
 \quad\hbox{at a rising letter},\qquad
 \sum_{j\ge\ell}{j\choose\ell}^{\!2}v_j
 \quad\hbox{at a falling letter}.
\]
Use the same three return words merely as cuts, keeping all grades at each cut. On each open-cell return product of length \(n\), the certificate checks the following componentwise bounds for the action on one positive test vector \(v\).

| Copies per side | Test vector \(v\) | Multiplicative lower bound | Multiplicative upper bound |
|---:|---|---|---|
| 1 | (1000000, 620204) | \(3^{0.42n}\) | — |
| 2 | (1000000, 1866354, 321361) | \(3^{1.005n}\) | \(3^{1.0054n}\) |
| 3 | (1000000, 3862925, 1912064, 150141) | \(3^{1.6751n}\) | — |

Each transfer fixes a positive diagonal. A bounded fragment containing both directions connects any fixed diagonal bit endpoint to every grade in the appropriate forward or backward orientation. Consequently the test-vector comparisons propagate to the energy with fixed initial and terminal bit. Endpoint and exceptional-return contributions are subexponential by the preceding frequency argument. For any such growing family of unforced \(a\)-date segments, write \(E_{2k}\) for the ordinary ordered \(k\)-sum equality count. Then \(\liminf a^{-1}\log_3 E_2\ge0.42\), the fourth exponent lies between \(1.005\) and \(1.0054\) in the liminf/limsup sense, and the sixth lower exponent is \(1.6751\).

These three transfers already obstruct **every fixed even moment** in this particular equal-length, unweighted bridge argument. With \(F(t)=\sum_{\text{paths}}e(tB)\), the ordinary raw moment is \(E_{2k}=\int_0^1|F(t)|^{2k}\,dt\), counting all multiplicities of the integer numerator \(B\). Hölder gives log convexity. For \(k\ge3\),
\[
 \liminf_{a\to\infty} a^{-1}\log_3 E_{2k}
 \ \ge\ 1.6751+(k-3)(1.6751-1.0054)\ >\ (2k-1)/3.               \tag{2}
\]
The cases \(k=1,2\) also strictly exceed \((2k-1)/3\). A layout of \(2k\) equal segments of nearly \(h\) binary clocks followed by testing an interval of relative length \(2^{-h}\) has source log size approximately \((2k-1)h\). A uniform single-segment moment bound below the exponent on the right of (2) would be needed to cross the cubic height barrier by that use of Hölder.

Even quantization leaves this lower bound intact up to a factor depending on \(k\). Write the single-segment prime-power reciprocity identity \(2^mR_W-3^nR_Z=dB\) as in the pinned proof. A raw \(k\)-sum collision makes its signed \(R_Z\) sum a multiple of \(2^m\). After quantizing the fractions \(R_Z/2^m\bmod1\) to a grid by flooring, the two \(k\)-fold grid sums differ by one of at most \(2k+1\) residues. If \(b(x)\) is the multiplicity profile of the grid \(k\)-fold sum, each shifted-pair count \(\sum_xb(x)b(x+j)\le\sum_xb(x)^2\). Thus \(E_{2k}^{\rm raw}\le(2k+1)E_{2k}^{\rm grid}\). This argument neither bounds the correlation between different segments nor analyzes fractional Fourier moments. The constrained threshold from (1) and the unforced obstruction (2) concern different populations.
