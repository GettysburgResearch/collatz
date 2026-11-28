# A computable odd-branch change with the full clock and all fixed affine phase tests

The map in [Shadowing with independent phases](SHADOWING_WITH_INDEPENDENT_PHASES.md) can be made computable for every uniformly computable family of bounded real tests \(f_i(n)\). The *same* choice preserves the fixed affine phase law
\[
       F(an+r)=F(n)+b\,v_2(a)\pmod {2b}
       \quad\hbox{on a set of natural density one}                       \tag{1}
\]
for every fixed positive integer \(a\) and fixed integer \(r\). It preserves exact halving, the pointwise first-discrepancy deadline \(Z\le\tau\), all prescribed ordinary two-cycles with odd vertices \(q_i\ge3\), density-one agreement up to \(\tau-o_P(\sqrt{\log n})\) in the sense of the companion, and its exact critical collision formula. In particular there is an algorithm for a positive integer map with these properties, requiring no decision about any infinite true trajectory. Its finite searches are extremely large.

## A finite branch test that intercepts every trajectory

Use the genuine shortcut to compute the next \(B(r)=\lceil\log_2(r+1)\rceil\) states of an odd \(r\), and redirect it whenever all these states are at least \(r\). All true global minima pass this test. At an odd input selected by it, use the companion's genuinely changed edge to the appropriate designated vertex or four times that vertex; keep the same rules for the other inputs. The proof that \(Z(n)\le\tau(n)\) and of finite capture is unchanged.

Here the local test cannot cause an early change at protected dates. Put \(L=\log n\). Fix \(\varepsilon>0\). With probability tending to one, (7) of [the initial shadowing theorem](SHADOWING_TO_THE_MINIMUM.md) gives \(\min_{k\le\tau-\varepsilon\sqrt L}\log T^k n\ge\varepsilon\sqrt L/(3\mu)\). Choose a fixed constant \(0<c<\min(1/2,1/(6\mu\log2))\). For \(v=\lfloor c\varepsilon\sqrt L\rfloor\) the next \(v\) steps are within the local test horizon at every one of these dates, and \(k+v\le\tau\). The genuine height modulus (6) of that note gives, uniformly there,
\[
           \log T^{k+v}n-\log T^kn=-v/\mu+o_P(\sqrt L)<0
\]
with probability tending to one. Thus none of the odd inputs in this entire window meets the finite redirect test. The genuine/modified first-discrepancy comparison, actual cycle-entry clock and height-process comparison follow as before.

## Resonating with all odd primes

Write \(p_1=3,p_2=5,\ldots\) for the odd primes. At stage \(j\) put \(Q=Q_{j-1}\), \(N=Q^{\lceil\sqrt j\rceil}\), \(P=2bQN\), and choose \(q=Q(1+2bk)\) with \(N\le k<2N\). We can start, for example, with \(Q_1=1+2b\). Every such choice satisfies the companion's growth (4) at all sufficiently large stages. Use integer scale boundaries
\[
             B_j'=2^{\lfloor\sqrt{\lfloor\log_2 Q_{j-1}\rfloor}\rfloor},
       \qquad \delta=2^{-w},\qquad
             w=\left\lceil(1+\lfloor\log_2 N\rfloor)^{3/4}\right\rceil.
\]
The symbol \(B_j'\) specifies phase scales and is separate from the finite branch horizon \(B(r)\). We select so that for some \(s_j\to\infty\),
\[
                        \max_{i\le s_j}\|q\log_2(p_i)/2\|\le\delta .     \tag{2}
\]

Here is a count valid for each **fixed** \(s\) at every sufficiently late stage, uniformly in the previous choice \(Q\). For \(0<\|h\|_\infty\le H\), the geometric-sum frequency \(\alpha_h=bQ\sum_{i\le s}h_i\log_2 p_i\) satisfies
\[
                       \|\alpha_h\|\ \gg_{s,b}\ (QH)^{-C_{s,b}} .       \tag{3}
\]
Indeed, subtract the nearest integer, multiply by \(\log2\), and apply Matveev's rational linear-form theorem to the fixed positive rationals \(2,p_1,\ldots,p_s\). The coefficients, including the nearest integer, are \(O_{s,b}(QH)\), and unique prime factorization gives nonvanishing. Corollary 2.3 of the original work bounds \(\log|\Lambda|\) below by \(-C_{s,b}\log(2QH)\) for these fixed rational heights and degree one. [Matveev, *Izvestiya: Mathematics* 64 (2000), pp. 1217–1269, Corollary 2.3](https://doi.org/10.1070/IM2000v064n06ABEH000314)

For \(0<\eta<1/4\) the periodic triangular function \(\phi_\eta(u)=(1-\|u\|/\eta)_+\) has mean \(\eta\), nonnegative Fourier coefficients summing to one, and tail \(O(1/(\eta H))\) beyond \(|h|>H\). This follows by convolving two equal interval indicators, or from its coefficients \(\eta(\sin(\pi h\eta)/(\pi h\eta))^2\). The product of \(s\) such bumps has mean \(\eta^s\), absolute coefficient sum one and tail outside the frequency cube \(O_s(1/(\eta H))\). Translate each coordinate by \(Q\log_2p_i/2\) and evaluate on \(k(bQ\log_2p_i)_{i\le s}\). The translations preserve coefficient magnitudes. By (3) and the finite geometric sum, the mean over our consecutive \(N\) dates differs from \(\eta^s\) by at most
\[
                  O_s(1/(\eta H))+O_{s,b}((QH)^{C_{s,b}}/N).
\]
With \(\eta=\delta/4,\ H=\lceil\eta^{-(s+2)}\rceil\), the first error is \(o(\eta^s)\). The second is \(N^{-1+o_s(1)}\), because \(\log Q/\log N\to0\) and \(\log H/\log N\to0\) for fixed \(s\). At least \(\tfrac12N\eta^s=N^{1-o_s(1)}\) candidates therefore meet all \(s\) requirements even with margin \(\delta/4\).

Use the companion's finite Fourier-energy exclusion, now with integer degree \(D=(3P)^{6\lceil\sqrt{j+1}\rceil}\). All relevant shells \(J\le B_{j+1}'+1\) lie in its former \(J\le(3P)^{1/1000}+1\) budget for large \(j\). The same divisor estimate removes at most \(P^{1/1000+o(1)}\) candidates even with strict energy requirement \(E_W(q)<(2j^2)^{-1}\). Thus for every fixed \(s\), eventually more than \(\lceil\sqrt P\rceil\) candidates pass both tests with the stated margins.

The new boundaries have \(\log\log B_{j+1}'-\log\log B_j'\to\infty\). For a stage \(i\) meeting \(a\sqrt J\le l\le AJ\), one has \(J\ll_a (B_{i+1}')^2\) and \(B_i'\le AJ\). Consequently \(J\le \exp(O_a(\sqrt{\log Q_i}))\) and \(\log Q_{i+1}=o(\sqrt J)\). Both frequencies \(Q_i,Q_{i+1}\) have \(\gamma=\log_2 3\) errors \(\ll\exp[-c(\log Q_i)^{3/4}]\) for large \(i\), since \(\log N\sim\log Q_i\) at its stage of selection. These are the two estimates in (4) of the initial shadowing theorem, even over a transition seam. All shell and path arguments survive unchanged.

For (1), in a shell compare the scales of \(n\) and \(an+r\) to \(J\), first discarding the \(O_a(2^{-V})+o(1)\) fractions with 2-adic valuations above \(V\) for fixed, sufficiently large \(V\). The remaining scales differ from \(J\) by \(O_{a,r}(V+1)\). The floor and selector tests at either participating frequency \(Q_i\) shift under \(\log_2 a\) by the exact doubled-parity phase \(b\,v_2(a)\), up to errors tending to zero by (2) and the fixed prime factorization of the odd part of \(a\). The perturbation of \(\log_2(an)\) by \(r\) costs \(O_{a,r}(Q_i 2^{-J})=o(1)\) in the angular tests. The simultaneous strips of the initial proof give \(o(1)\) shell cost, then send \(V\to\infty\). Ray overrides have only \(O_{a,r}(\log X)\) preimages. This proves (1) at every cutoff.

## Explicit finite decisions

The following details make total computability independent of any effective onset in the limiting theorems.

* For every candidate \(q\) approximate its finitely many energies to absolute error \(1/(8j^2)\), and keep those whose approximants are below \(3/(4j^2)\). The true energies of retained candidates are below \(j^{-2}\); every candidate with the above strict margin is retained. The weights are bounded, uniformly computable values on finite integer cells times the known smooth exponential weight. Fourier integrals split into finitely many explicitly located intervals, including the rational cutoff \(c\), so they can be computed to any specified precision. One may integrate the elementary exponential exactly in computable-real arithmetic or use rational approximations with certified endpoint errors.
* Approximate \(\|q\log_2(p_i)/2\|\) to absolute error \(\delta/8\), for \(i\le j\). Select the largest \(0\le s\le j\) for which at least \(\lceil\sqrt P\rceil\) retained candidates have every one of the first \(s\) approximants below \(\delta/2\). Choose the least such candidate \(q\) from that set. If no such \(s\) exists choose the first candidate in the original interval. This procedure performs only prescribed finite computations. Every fixed \(s\) eventually works at every stage by the lower count, so the default is used only finitely often and \(s_j\to\infty\).
* Interpolate the selectors with rational parameters by using \(\nu(l)=\lfloor\log_2\log_2\max(2,l)\rfloor\) in place of the continuous \(\log\log l\), and the normalized difference between \(\nu(l)\) and the two endpoint values. This is computable by twice taking the floor binary logarithm. If an early denominator vanishes use the first pattern on that interval. All late denominators tend to infinity. Across the entire protected scale range the numerator changes by \(O_a(1)\); the one-stage and two-stage seam estimates still hold. At an indicator threshold use the exact construction's strict inequality: \(\lfloor bQ\log_2 n\rfloor=\lfloor\log_2(n^{bQ})\rfloor\), and comparison of its fractional part to a rational \(d/e\) reduces to comparing \(n^{ebQ}\) and \(2^{e\lfloor bQ\log_2 n\rfloor+d}\). All endpoints and tie conventions are decidable by integer arithmetic.
* To obtain the terminal clock, minimum and height-path independence used in the critical law, simulate the true path only through \(100\lceil\log_2(n+1)\rceil\), retain its finite minimum and its first date there, and form the corresponding centered, interpolated path. By the true \(\tau/\log n\to\mu\), these finite objects are identical to the complete true objects on density one. Use a computable convergence-determining collection of bounded continuous tests, for example finite products of rational tent functions of rational-time path evaluations and the terminal standardized clock, together with integer minimum indicators. Rational-time marginals determine continuous-path laws and the genuine path laws are tight, so these tests suffice also after phase conditioning by the balancing result. The formula for every real critical parameter follows from continuity of the Gaussian distribution.

Thus the modified local odd rule, including its auxiliary phase at every individual integer, is determined by finite computations. The scale at which any experimental sample reflects the limiting law is a separate matter. The [finite controls](check_shadowing_phases.py) check physical capture, synchronous phases, rational selector seams and the local redirect guard on explicit finite schedules.
