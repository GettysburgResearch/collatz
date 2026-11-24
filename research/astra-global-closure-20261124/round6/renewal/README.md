# Ordinary residue routing at completed ratio-five marks

**PROPOSED, conditional only on the stated classical exponential-sum theorem for the growing-precision estimate.** From every positive odd ternary unit \(q\), a family of actual paired predecessors is pointwise equidistributed in *every* unit class modulo \(3^k\), at one common physical clock and one odd count. The clock is at most \(\exp(Ck^{2/3})\), uniformly in \(q\). Each route carries \((x,5x)\) to \((q,5q)\) at complete marks. A separate count locates central rows with many symbolic completed words. The physical clock cost of imposing the full prescribed residue remains too large to obtain critical pressure. Universal convergence is OPEN.

## The pointwise result

Use the shortcut \(T(2n)=n,\ T(2n+1)=3n+2\). A mark is an odd first-arm endpoint with second arm five times the first and with equal cumulative counts of odd inputs. Each block stops at the first positive equal-count ratio-five return, then consumes all common halvings before the next odd sentinel. At time zero the first arm is odd. Haar on \(U=\mathbb Z_3^\times\) is normalized to mass one. A unit below means positive and coprime to six for ordinary endpoints.

There is an absolute \(A\) such that, for all sufficiently large \(k\), take \(N\) to be the least multiple of 162 at least \(\exp(Ak^{2/3})\). Set \(E=N+11,\ d=N/81,\ e=kE,\ p=4k\). For every ordinary unit \(q\) and every unit \(a\bmod3^k\), the family constructed below contains
\[
 \frac{d^k}{2\cdot3^{k-1}}\bigl(1+O(3^{-k})\bigr)                    \tag{1}
\]
different sources \(x\equiv a\bmod3^k\) reaching \((q,5q)\) in exactly \(2k\) completed blocks, \(e\) shortcuts and \(p\) odd inputs on each arm. The implied constant is absolute. Its \(d^k\) paths, including all residue classes, are equiprobable under the *constructed inverse rule*. Their individual weights in the true iid marked-word law are \(2^{-e}\). Multiplying (1) by \(2^{-e}\) gives a genuine fixed-target lower bound for completed-word mass in the stated row. For the finitely many smaller \(k\), a choice of \(N\) with exact class counts is given below. In particular the physical-clock bound \(\exp(Ck^{2/3})\) holds for every \(k\ge1\).

The ordinary heights admit a uniform relative bound. Each inverse has real multiplier \(2^u/9\ge64/9\) and subtracts \(7/9\). Its forward offset is at most \(7/64\) and forward multiplier at most \(9/64\). Summing the actual composed offsets gives \(R\le(7/64)/(1-9/64)=7/55\). Thus
\[
        (2^E/81)^k(q-7/55)\ \le x <(2^E/81)^k q.                    \tag{2}
\]
In particular all paths are finite actual sources of comparable real height, even at \(q=1\).

## A fixed-clock regular family

The chronological word \(101000\) on \(x=64s+49\) gives \(T^6x=9s+7,\ T^6(5x)=45s+35\), with two odd inputs on each arm. At clocks one and two their equal-count ratio errors are \(-2\) and \(-1\). At clocks three through five their odd counts differ. Hence the first return is at six. Its backward branch with all mandatory even padding is
\[
       A_u(q)=(2^u q-7)/9,\qquad u\ge6 .
\]
If this is integral at an odd \(q\), it is odd, positive and congruent to 49 modulo 64. The first six steps end at \(2^{u-6}q\) and its fivefold multiple. Exactly \(u-6\) common halves lead to the odd sentinel \(q\). We retain units at the earliest source. Each intermediate marked value on any admissible concatenation is automatically a ternary unit, since the forward affine numerator is 7 modulo 3. [PR200, frozen 39918be724038ac550d77c7fc95d17e05251dfc6, first-return convention and elementary branch](https://github.com/GettysburgResearch/collatz/blob/39918be724038ac550d77c7fc95d17e05251dfc6/research/regularity-rigidity-20261124/RATIO_PRESSURE.md)

In one pair, read the exponents **outwards from** \(q\) as \(E-t,t\) for \(6\le t\le N+5\). Both are at least six. With \(B=2^E,\ P=81\),
\[
       A_t A_{E-t}(q)=(Bq-C_t)/P,\qquad C_t=7\cdot2^t+63.          \tag{3}
\]
Integrality of this last expression implies the legality of both steps. Indeed its equation can be written as \(2^t(2^{E-t}q-7)=9(9x+7)\). Coprimality with 9 gives an integer middle value, then \(2^t y=9x+7\). The six-step calculation proves full physical realization. More generally, on a list of pairs, divisibility of the whole numerator by \(P^k\) forces all intervening divisibilities. Reduce the whole numerator modulo \(P\) to get the first inverse numerator times a power of the unit \(B\), replace that step by its integral value, divide by \(P\), and repeat.

Two generates the units modulo \(3^s\) for all \(s\ge1\): its order mod three is two and \(v_3(4^{3^j}-1)=j+1\) by repeated cubing. On a length-162 period, \(C_t\bmod243\) therefore runs once over all units. For any \(q\in U\), (3) is integral with unit output precisely when \(C_t\equiv Bq-P\) or \(Bq-2P\bmod243\). Hence every \(q\) has exactly \(d=2N/162\) legal pair labels. Under uniform choice from those \(d\) labels, Haar is invariant. For a bounded test \(g\), substitute \(q=(Px+C_t)/B\) on each branch image. Its Haar scaling factor is \(1/P\), and the integral over \(q\) of the inverse average is \(N/(dP)\int_Ug=\int_Ug\). Constancy of row degree alone would not imply this change of variables.

For ordinary \(q\), distinct labels after any fixed number of pairs give distinct sources. A source determines its own marked forward parsing, including the first positive return, padding and next odd sentinel at each step. Reading \(2k\) such blocks recovers all labels. This does not assume that different stopping *clocks* are disjoint. All paths used in (1) have the same prescribed clock.

## Uniformity at every supplied ordinary point

Take the \(t_j\) for the moment as independent uniform elements of the whole length-\(N\) interval, with \(j=0,\ldots,k-1\) in outward order. Define the unrestricted integer carry
\[
 D=\sum_{j=0}^{k-1}P^j B^{k-1-j}C_{t_j},\quad
 L=5k,\quad r=B^kq-P^ka .
\]
The relation \(D\equiv r\bmod3^L\) is exactly the ordinary unit-output and final residue condition by (3). The residue \(r\) is a unit. The number of admissible words counted is \(N^k\Pr(D\equiv r)\). The proportion of all trial words that give *some* legal unit output is exactly \((d/N)^k=P^{-k}\). The unconditional carry calculation precedes this normalization.

For an additive frequency of exact conductor \(3^\ell\), independence factors the characteristic function of \(D\). Its \(j\)-th factor, if \(\ell>4j\), is a unit complex phase times a normalized sum of \(e^{2\pi i b2^t/3^{\ell-4j}}\), for a unit \(b\) depending on the frequency and the fixed multipliers. Every conductor \(2\le\ell\le4k+1\) has a \(j\in[0,k-1]\) with \(2\le\ell-4j\le5\). This factor vanishes exactly: \(N\) is a multiple of the full period and the sum of a primitive additive character over the units modulo \(3^s\) is zero when \(s\ge2\). Modulo three, \(D\) is uniform on the two units. Thus its two conductor-three coefficients are \(-1/2\), as for normalized Haar on the units.

For \(4k+2\le\ell\le5k\), use \(0\le j<\lceil k/2\rceil\). Each remaining conductor exponent \(s=\ell-4j\) lies between \(2k\) and \(5k\). Korobov's Theorem 4, with fixed prime 3 and base 2, gives
\[
 \frac1N\left|\sum_{t=6}^{N+5}\exp(2\pi i b2^t/3^s)\right|
       \le 3\exp\{-c(\log N)^3/(s\log3)^2\}
\]
when \(s\) is sufficiently large and \(2< s\log3/\log N<s/(8\beta)\), where \(\beta\) depends only on 3 and 2. The shifted start multiplies \(b\) by the unit 64. Here \(s\asymp k\) and \(\log N\asymp k^{2/3}\), so the parameter tends to infinity but is \(o(s)\), uniformly on the asserted range. Choose the fixed \(A\) large enough that the estimate is at most \(3^{-12}\). Hence every high coefficient has magnitude at most \(3^{-6k}\). Finite Fourier inversion has at most \(3^{5k}\) coefficients. It yields
\[
        3^{5k}\Pr(D\equiv r\bmod3^{5k})=\tfrac32+O(3^{-k})
                 \quad(3\nmid r).
\]
The constant \(3/2\) is the density of unit Haar relative to Haar on the whole ring. Multiplication by \(N^k\) gives (1). For exceptional bounded \(k\), choose \(N\) divisible also by \(2\cdot3^{5k-1}\), so already the \(j=0\) factor kills every conductor \(2\le\ell\le5k\). Increasing the absolute constant in the clock bound covers this finite prefix. [N. M. Korobov, *On the distribution of digits in periodic fractions*, Theorem 4, English journal pp. 671–674](https://doi.org/10.1070/SM1972v018n04ABEH001870) · [J. Vandehey, *Differencing methods for Korobov-type exponential sums*, Theorem 2.4, parameters stated on p. 5](https://arxiv.org/pdf/1606.07911)

## Symbolic central mass and the physical price of a correction

Let \(u_e\) be the probability that physical clock \(e\) is a mark under conditional binary Haar on odd starts, including \(u_0=1\). Let \(\mathcal W_{p,e}\) be all its complete words with \(p\) odd inputs. Their disjoint sentinel cylinders have mass \(2^{-e}\), so \(u_e=\sum_p 2^{-e}|\mathcal W_{p,e}|\). With the PR146 independent marked gap law \(\Pr(L>t)\asymp(1+t)^{-1/2}\), one obtains
\[
 \sum_{e\le H}u_e\asymp\sqrt H.                                      \tag{4}
\]
For the upper bound, a sum of \(j\) gaps can be at most \(H\) only if each individual gap is at most \(H\). Sum \((1-c/\sqrt H)^j\). For the lower bound, truncation gives \(\Pr(L_1+\cdots+L_j>H)\le Cj/\sqrt H\). Sum over \(j\le c'\sqrt H\). These are renewal counts in a finite interval. No pointwise strong renewal theorem at index one half is required. [PR146, f431078244e868dc699fad011044f0d5e7f76437, first return and marked renewal](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/FIVE_RETURN_CLOCK_AND_TERMINALS.md) · [F. Caravenna and R. Doney, *Local large deviations and the strong renewal theorem*, Theorems 1.4–1.5](https://arxiv.org/abs/1612.07635)

Choose a fixed large \(D_0>1\) using the two constants in (4). The marks in \([H,D_0H]\) have combined mass \(\gg\sqrt H\). For each such clock, its noncentral mass at \(|2p-e|>K\sqrt{H\log(2H)}\) is at most the same binomial tail without the mark restriction, conditional on the first bit odd. Taking \(K\) large makes the sum of these tails \(O(H^{-2})\). The remaining strip has \(O(H^{3/2}\sqrt{\log(2H)})\) integer rows. For each large \(H\) there is therefore an actual completed symbolic row in that strip with
\[
          2^{-e}|\mathcal W_{p,e}|\gg 1/(H\sqrt{\log(2H)}).          \tag{5}
\]
For a random terminal Haar unit \(y\), each fixed word of this row admits unit inverse with probability \(3^{-p}\), by its affine map. Thus (5) is also an averaged lower bound for the round-five mass \(M_{p,e}(y)\) after multiplication by \(3^{-p}\). The chosen clock, odd count and endpoint average in (5) are stated separately from the pointwise conclusion (1).

For the exact attempted concatenation, let \(\mathcal V\) be any collection of completed words of fixed odd count \(b\) and clock \(h\), and put \(m=b+1\). The count \(g(y)\) of legal inverses from this collection depends only on \(y\bmod3^m\), and \(\int_Ug=3^{-b}|\mathcal V|\). Apply (1) with precision \(m\) and append a \(\mathcal V\)-inverse to each of its legal ordinary outputs. All concatenations have a common clock and parse uniquely. For each \(q\), their true mass, multiplied by the natural ternary factor \(3^{4m+b}\), is exactly
\[
     (1+O(3^{-m}))\,
         \underbrace{(N2^{-E})^m}_{\text{mass of the selected router words}}\,
         \underbrace{2^{-h}|\mathcal V|}_{\text{symbolic mass of the desired row}} .       \tag{6}
\]
The error is relative for nonempty \(\mathcal V\), because (1) holds in every unit cell and \(g\ge0\). In particular (5) can be turned into a pointwise ordinary lower estimate, with the explicit loss in (6). The selected pair dictionary has unconditioned symbolic mass \(N2^{-E}\). At a fixed ordinary parent its legal pair weight is \(d2^{-E}\), whose ternary normalization \(81d2^{-E}\) gives the same \(N2^{-E}\) in (6). For \(h\sim2b\) and \(m=b+1\), the negative logarithm of the complete correction factor is \(m(E\log2-\log N)\), much greater than \(b\). A single full-precision use already exceeds a logarithmic loss. Sparse use only helps if the next test depends on much less precision than its full row legality, or an estimate controls the unresolved higher digits. For a proposed schedule of such corrections at precisions \(m_i\), the normalized mass product costs the sum \(\sum_i m_i(E_i\log2-\log N_i)\) when the relative factors in (6) apply. Even a bounded-precision correction costs a fixed positive amount per insertion.

PR200's finite pressure bound already yields \(\gg_q X^{1/9}\) ordinary marked predecessors in certain height intervals. Formula (1) establishes uniform residue distribution at **one exact paired row** with explicit height window (2). Counting those words alone gives no improvement of that fixed-height exponent. The order \(e\) here is far above \(2p\), even though the odd count is fixed and both labels are preserved. PR192's singularity concerns the full stationary law on real and ternary coordinates. The Haar-preserving kernel here selects and renormalizes a finite set of completed words on the ternary coordinate, so its Haar identity has a different measure and domain. [PR192, 301b84491ffafe283bd63d104c1b60ddf0e97f06, marked joint law](https://github.com/GettysburgResearch/collatz/blob/301b84491ffafe283bd63d104c1b60ddf0e97f06/research/astra-two-centre-20261124/basin.md) · [PR200, 39918be724038ac550d77c7fc95d17e05251dfc6, harmonic finite-dictionary obstruction and pressure \(1/9\)](https://github.com/GettysburgResearch/collatz/blob/39918be724038ac550d77c7fc95d17e05251dfc6/research/regularity-rigidity-20261124/RATIO_PRESSURE.md)

There is a fixed-height consequence in a growing family of progressions. For some absolute \(c>0\), for all sufficiently large \(X\) depending on a fixed ordinary unit \(q\), every unit class \(a\bmod3^k\) with
\[
              1\le k\le c(\log\log X)^{3/2}
\]
contains at least \(\gg_q X^{1/9}\exp(-O(\sqrt{\log X}))\) actual marked ancestors of \((q,5q)\) in \([48\cdot2^{-400}X/55,X]\). To see this, set \(G=(2^E/81)^k\) and \(Y=X/G\). By choosing \(c\) small one has \(kE\le\sqrt{\log X}\) uniformly in this range for all large \(X\), since \(\log(kE)\le Ak^{2/3}+O(\log(2k))\) and the finitely many modified small-\(k\) clocks are fixed. The increasing tree constructed in PR200 §§2–3 supplies \(\gg_q Y^{1/9}\) distinct eligible roots \(y\in[2^{-400}Y,Y]\) already reaching the given pair. Its construction works for either labels at any root: first use a sufficiently large elementary \(A_u(q)\) if its height lies below the certificate threshold. For every such \(y\), (1) supplies at least one \(x\) in the requested class, and (2) puts it in the displayed shell. Roots \(y\ne y'\) have disjoint outputs because \(T^{kE}x=y\) at one common clock. Finally \(G\le\exp(O(\sqrt{\log X}))\). The comparison with a single primitive-root padding is in the growing precision: that one-step budget \(O(3^k)\) gives \(k=O(\log\log X)\) under the same square-root-log clock allowance.

Weaver's paper 37, Theorem D, gets an almost linear sum of valuations and a central row for **arbitrary single-arm Syracuse words**. Paper 127, Theorems 2 and 5, gives pointwise empirical convergence for capped single-arm inverse kernels. Their branch is \((2^e q-1)/3\). Neither theorem asserts occurrence of the simultaneous second-arm mark at the end of the chosen word. Brofferio's rational affine Poisson-boundary theorem assumes finite first moment; the PR200 true marked law already has infinite mean positive log height multiplier. A boundary identification would still require an ordinary-point count and complete legality. Here the external cancellation theorem acts directly on the actual independent padding labels of (3), where its phase can be checked explicitly. [Weaver, paper 37 v4, Theorem D](https://rstation.ai/problems/collatz/papers/37/v4) · [Weaver, paper 127 v1, §§1, 9–12](https://rstation.ai/problems/collatz/papers/127/v1) · [S. Brofferio, *The Poisson boundary of random rational affinities*](https://doi.org/10.5802/aif.2191)

**First unsupported step toward closure.** A fixed ordinary \(q\) still needs enough legal *completed* words when \(2^e/3^p\) is comparable to \(X/q\), with a quantitative lower bound after summing across the physical-height strip. Row (5) supplies neither a particular ordinary endpoint nor a bound on every central row. Row (1) supplies every ordinary endpoint at excessive clock cost. The possibility of unequal convergence labels at \(q,5q\), the unrestricted failure upper bound and any universal merger remain open. The single-arm canonical trace \(h(v)/v\to0\) along large ancestors of a *fixed* ordinary root does not give a bound along its forward escaping orbit. [Weaver, paper 12 v1, equations (24)–(27)](https://rstation.ai/problems/collatz/papers/12/v1) · [Round-five ordinary target and unresolved central atom](../../round5/renewal/README.md)

[Lean arithmetic kernel](MarkedRouter.lean) · [Exact finite controls](check.py) · [Execution record](../../../../reports/astra-global-closure-20261124/round6/renewal/EXECUTION.md)
