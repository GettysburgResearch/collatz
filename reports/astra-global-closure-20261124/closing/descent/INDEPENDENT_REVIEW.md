# Independent reconstruction of the three ternary-class mergers

**Verdict.** The three claimed variable-clock mergers hold on the stated ordinary source cylinder. I reconstructed the input cofactors, three complete target scripts, and six inherited prefix certificates independently of the author's Lean implementation. The 16-case conclusion is conditional on an ordinary five-block L/P prefix beginning at its first P and, for the three new cases, on the residue of the *initial* source. The rest of the trajectory is free.

## Sustained LPP covers two of the three residuals

For the actual three-block past LPP from \(x\) to \(q_0\), direct composition gives \(2^{13}q_0=729x+2207\) and \(2^{13}\xi=729\xi_{\rm in}+27224\), so \(\xi=729h+229\) with \(h\ge0\). Set
\[
 m=768h+239=(128q_0+349)/243=(3x+101)/64.
\]
The forward eight-bit script 11110111 from 239 uses seven odd inputs, carry 2363 and ends at 2051. The lift by \(3\cdot2^8h\) therefore gives \(T^8m=2051+3\cdot3^7h=9\xi-10\). Also \(q_0=1458h+451\), and \((3q_0+1)/4-m=(217q_0-1153)/972>1\). The positive odd partner is below both prescribed initial floors. The repeated three-step transport at \(-10\) and the second and third rows of the final-target table below now apply, reaching the common endpoint in \(3r+28\) clocks on PLLPP and \(3r+26\) on PLLPL. Arbitrarily long finite L/P histories can precede this LPP word by ordinary dyadic-cylinder realization of the concatenation. At its endpoint and \(r\ge3\), this adds two of PR192's three residuals to its existing thirteen. PPLLL remains open on this sustained-past cylinder. All sixteen are handled on the two narrower entrance guards described below. The separate twelve-letter theorem gives a direct predecessor of its following \(f\) independently of all later blocks. [Twelve-letter result](../../../../research/astra-global-closure-20261124/closing/descent/LONG_PAST.md)

## What the light prefix supplies

Let \(T(x)=x/2\) at even \(x\) and \(T(x)=(3x+1)/2\) at odd \(x\). Let \(q=q_r\) after \(r\) genuine L blocks. Iterating \(8(L(x)+7)=9(x+7)\) gives \(8^r(q+7)=9^r(q_0+7)\). As \(q\) is odd, \(2\cdot8^r\mid9^r(q_0+7)\). Coprimality and positive integrality give
\[
 q_0+7=2\cdot8^rv,\quad q+7=2\cdot9^rv,\quad \xi=(q_0+7)/2=8^rv,\quad v\ge1 .
\]
The guard gives \(\xi=177147h+3418\), \(h\ge0\). Equivalently \(q_0\equiv6829\bmod 177147\). Each finite genuine L/P gap script fixes one dyadic residue class, which has a CRT lift in each ternary residue class. The guard is additional information. For \(r\ge6\), the paid entrance \(q\) is automatically \(-7\bmod 177147\), irrespective of the original guard.

## Legality, transport, and final clocks

For any \(k\)-bit shortcut word from \(b\) with \(u\) odd inputs, the same word from \(b+2^kz\) changes the endpoint by \(3^uz\). This follows by induction since the difference after \(j\le k\) steps equals \(2^{k-j}3^{u_j}z\). Here \(u_j\) counts odd visits through step \(j\). This verifies every inverse choice through a positive forward orbit.

| Five blocks | \(m\) | First bits from the constant term of \(m\) | Constant endpoint | Slope in \(h\) |
| --- | --- | --- | ---: | ---: |
| PPLLL | \(248832h+4799\) | 1111110101 | 30755 | \(243\cdot3^8=9\cdot177147\) |
| PLLPP, PLLPL | \(262144h+5055\) | 111111011011010011 | 30752 | \(3^{13}=9\cdot177147\) |

Indeed \(248832=243\cdot2^{10}\), \(262144=2^{18}\). The first stage reaches \(9\xi-b\), \(b=7\) or \(10\) respectively. Writing \(f=(3q_0+1)/4\) in the reals gives \(2(f-m)=33777h+646\) or \(7153h+134\). Both are at least \(134\), so \(m<\lfloor f\rfloor\), including \(r=0\) where the source starts with P. Also \(f<q_0\), and both proposed \(m\) are positive odd integers for every \(h\).

The three-step identities \(T^3(8z-7)=9z-7\) and \(T^3(8z-10)=9z-10\) use parity words 101 and 011 whenever the starting argument is positive. With \(9\xi=9\cdot8^rv\), all \(r\) repetitions are legal; each transport point is a forward iterate of a positive starting value. They reach \(Y=9^{r+1}v-b\), equivalently \(2(Y+b)=9(q+7)\). No inverse map is applied to a nonintegral state.

A source suffix with total clock \(A\), ten odd inputs, and carry \(C\) has \(2^Aw=3^{10}q+C\). The carry updates by \(C\mapsto9C+c2^A\) on each new block, with \((a,c)=(3,7)\) or \((5,5)\). Substituting \(q=2(Y+b)/9-7\) gives \(2^{A-1}w=6561Y+K\), \(K=(C-7\cdot3^{10})/2+6561b\). The following entire-residue checks derive from that identity.

| Suffix | \(A,C\) | \(K\) | \(Y\bmod2^{A-1}\) | Final target bits | Base endpoint | Target and source clocks including the prefix |
| --- | --- | ---: | ---: | --- | ---: | --- |
| PPLLL | \(19,1704901\) | 691706 | 28742 | 011000010001101101 | 722 | \(3r+28,\ 3r+19\) |
| PLLPP | \(21,761093\) | 239485 | 305059 | 11000011001100011000 | 1909 | \(3r+38,\ 3r+21\) |
| PLLPL | \(19,892165\) | 305021 | 239523 | 110000110011000101 | 5996 | \(3r+36,\ 3r+19\) |

The odd coefficient 6561 gives the listed unique residues. Each literal script uses eight odd inputs and has the listed \(K\). The residue-lift identity above proves that all admissible lifts end at exactly \(w\). A subsequent arbitrary source suffix can be appended at identical clocks to both paths.

## Which previous cases complete the count

I independently obtained these values by deriving the residues from the affine relation and applying literal shortcut steps at the least representatives. In the column \(B,u,K\), the target identity is \(2^Bw=3^uy+K\).

| Earlier prefix | Partner construction | \(B,u,K\) | Residue of \(y\) | Endpoint at that residue | Five-letter words covered |
| --- | --- | --- | ---: | ---: | ---: |
| PPP | fixed half | \(14,6,6034\) | 2846 | 127 | 4 |
| PPLP | fixed half | \(17,8,84002\) | 22302 | 1117 | 2 |
| PLPP | ramp, \(\ell=1\) | \(17,7,16358\) | 27022 | 451 | 2 |
| PLPL | ramp, \(\ell=1\) | \(15,7,24550\) | 2446 | 164 | 2 |
| PLLL | ramp, \(\ell=3\) | \(13,5,3406\) | 7942 | 236 | 2 |
| PPLLP | ramp, \(\ell=1\) | \(20,9,599926\) | 206190 | 3871 | 1 |

The half starts at \((q_0-7)/2=\xi-7\); genuine L transfers this comparison to \((q-7)/2\). Indeed on L one has \(x=16t+9\), the comparison follows bits 101, and \(T^3((x-7)/2)=(L(x)-7)/2\). The ramp starts at \(2^{2r+\ell}v-1\) and takes \(2r+\ell\) all-odd steps to \(3^\ell(q+7)/2-1\). For \(r\ge3\) both constructions start odd, positive and below both initial floors. The six disjoint prefixes cover 13 of the 16 words. For each shorter accepted prefix the two paths can continue together through the remaining letters. The three uncovered words are precisely the rows in the preceding table. For \(r\le2\), a genuine input itself falls below the original floor by its first paid boundary, as shown in the pinned earlier theorem. This finite certification gives no finite bound for first reaching P in an arbitrary infinite Collatz orbit and covers no arbitrary gap alphabet. [PR192, pinned six-prefix proof](https://github.com/GettysburgResearch/collatz/blob/d2081d1cd2410e6004eaee9f9b13c5553afaf3f4/research/astra-closure-attack-20261124/DESCENT_EXTENSION.md)


## Which guards can recur inside the alphabet

The \(\xi\equiv3418\bmod3^{11}\) cylinder has \(\xi\equiv7\bmod9\). Under a genuine L, \(\xi'=(9/8)\xi\equiv0\bmod9\); under P, \(\xi'=(9\xi+83)/32\equiv4\bmod9\). Thus the first guard **cannot occur after even one preceding L or P**. Positive finite inputs in the guarded section exist by CRT, and the theorem applies there at entry. This distinguishes entry coverage from any argument along a sustained L/P run.

The second guard \(\xi=3^{13}h+9148\) remedies that incompatibility. It has \(\xi\equiv4\bmod9\), hence \(q_0\equiv1\bmod9\). Its actual positive P predecessor \(p=(32q_0-5)/9\) is odd; the first gap leads to the odd integer \((16q_0-1)/3\), whose triple plus one equals \(16q_0\), proving exact gaps \(1,4\). This establishes the possibility of a preceding P at each such positive source. It gives no guarantee that an arbitrary orbit visits this particular full ternary class.

| Suffix | \(m\) on the second guard | First forward bits | Odd steps | Value at \(h=0\) after this word | \(2(f-m)\) |
| --- | --- | --- | ---: | ---: | --- |
| PPLLL | \(2^{21}h+12031\) | 111111110111010110001 | 15 | 82325 | \(588665h+3372\) |
| PLLPP, PLLPL | \(2^{13}3^5h+11419\) | 1101111010111 | 10 | 82322 | \(801657h+4596\) |

All numbers in the last column are positive with room for the integer floor. The endpoint slopes are \(3^{15}=9\cdot3^{13}\) in both rows, so the first stages again reach \(9\xi-b\); all downstream proofs above persist. The target clocks are \(3r+39,3r+33,3r+31\) respectively. For \(r\ge1\), the starting light intermediate \(f=(3\xi-10)/2\) is \(1\bmod27\) and \(3\bmod4\), since \(\xi\equiv22\bmod27\) and \(8\mid\xi\). It is this **intermediate** that belongs to the odd PR174 section; \(q_0\equiv10\bmod27\).

## Positive predecessor at every ternary height

For \(n=1+3^Hv\), suppose \(d\ge1\), \(v>0\), \(3^d\mid2+4^Hv\) and \(2^d4^H\le3^d3^H\). Put \(u=(2+4^Hv)/3^d\), \(m=2^d u-1\). The first \(d\) inputs of \(m\) are odd and \(T^d(m)=3^d u-1=1+4^H v\). Since \(T^2(1+4x)=1+3x\) with bits 10, iterating \(H\) tours gives \(T^{d+2H}(m)=n\). The start \(m\) is positive and odd, and the exact size margin is
\[
3^d(n-m)=2(3^d-2^d)+v(3^{H+d}-2^d4^H)>0 .
\]
For \(H\ge1\), choose \(d_H=\lceil H\log(4/3)/\log(3/2)\rceil\). A smaller \(d\) gives a negative coefficient of \(v\) in the last display, so cannot work uniformly as admissible \(v\) tends to infinity. The divisibility test with \(d\ge1\) forces \(v\equiv1\bmod3\); in particular \(H=v_3(n-1)\) and one cannot adjust it at will on a preassigned ordinary source.

For \(H\ge3\), imposing \(v\equiv2\bmod4\) gives \(n=1+27j,\ j\equiv2\bmod4\). At fixed \(H\), CRT supplies one \(v\) class modulo \(4\cdot3^{d_H}\), equivalently one \(n\) class modulo \(4\cdot3^{H+d_H}\). Distinct \(H\) give disjoint classes. Relative to the odd PR174 section \(n\equiv55\bmod108\), the union therefore has natural density
\[
       \sum_{H\ge3}\frac{27}{3^{H+d_H}}=0.0509640\ldots .
\]
The tail beyond \(H=K\) is supported on \(n\equiv1\bmod3^{K+1}\), so the stated limit of finite density sums is legitimate. The first three terms \(1/27+1/81+1/729\) already exceed \(0.05\). For \(H=d=3\), the progression is \(n\equiv1891\bmod2916\), with first partner \(1327\) arriving in nine steps. This density counts the scope of this particular predecessor construction. Its overlap with prior descent or merger certificates is included.

**Actual convergent member arms at every height.** Take \(M=H+1+d_H\). Since 2 is primitive modulo \(3^M\), arbitrarily large exponents solve
\[
                 2^e\equiv 2-2\cdot3^{H+1}4^{-H}\pmod{3^M}.
\]
The right side is a unit and forces \(e\) odd. Choose \(e\ge3\), set \(v=(2^e-2)/3^{H+1}\), and take \(e\) large enough for \(v>0\). Dividing the congruence gives \(v\equiv-2\cdot4^{-H}\bmod3^{d_H}\). Modulo four it also gives \(v\equiv2\bmod4\) directly from \(3^{H+1}v=2^e-2\). Thus \(n=(2^e+1)/3\) has the smaller predecessor just proved and \(3n-1=2^e\) reaches one. The primitive-root fact follows from \(v_3(4^{3^j}-1)=j+1\), by binomial expansion and induction. This constructs new witnesses when \(H\) or \(e\) varies; it is not a witness-preserving selector for every input. The density calculation concerns the larger unconditional predecessor family, and no density is claimed for the power-of-two specialization.

The positive predecessor excludes these \(n\) as the globally least positive nonconverger. Alone it supplies no proof that \(m\) converges and does not establish the reverse-closure implication on the whole PR174 section. [PR174 at the pinned head](https://github.com/GettysburgResearch/collatz/tree/c92cd473de3b85ceb945702a726d2eb7350a6af8)


## Exact limits on recurrence and overlap with PR192

For the guard \(\xi\equiv9148\bmod3^{13}\), the two immediately preceding blocks, if present, are uniquely L then P in forward order. In reverse order the residue at 9148 forces a P and has predecessor representative \((32\cdot9148-83)/9=32517\equiv0\bmod9\). That forces an L, whose predecessor representative is \(8\cdot32517/9=28904\equiv5\bmod9\). The remaining precision is still at least \(3^9\), so this last obstruction applies at every lift and neither L nor P can precede it. The second guard admits actual two-block LP pasts, but no three-block past contained in that alphabet. For its central \(f\), \(v_3(f-1)=1+v_3(\xi-4)=3\) and \((f-1)/27\equiv22\bmod27\), different from the \(16\bmod27\) in the base height-three tour class.

A distinct seven-block script permits arbitrarily long L/P histories to be prepended to the script, using the dyadic cylinder of any finite concatenation. Let \(x\) be the original boundary of LLLLPLP, let \(q\) be its final boundary, and suppose the next two shortcut clocks give the integral \(f=(3q+1)/4\). Direct composition gives
\[
 2^{25}q=3^{14}x+27738191,\qquad
 2^{25}\xi_{\rm final}=3^{14}\xi_{\rm initial}+114569216,
\]
so \(\xi_{\rm final}\equiv4244071\bmod3^{14}\) and \(f\equiv3974617\bmod3^{14}\). The target word 1111111101110101001000 has 22 clocks, 14 odd inputs, and carry 5293177. Thus \(m=(2^{22}f-5293177)/3^{14}\) is integral; substituting the endpoint equations simplifies it to \(m=(3x-11)/32\). The actual four leading L's give \(x+7\equiv0\bmod 2^{13}\), so \(x\equiv57\bmod64\) and \(m\) is positive odd. Conversely \(2^{22}f=3^{14}m+5293177\) fixes \(m\bmod2^{22}\) uniquely. The certified target word has exactly that residue, by its invertible odd numerator slope. Its actual endpoint is \(f\). Since \(2^{22}<3^{14}\), \(0<m<f\). The formula in \(x\) also puts \(m\) below \(x\) and its first light intermediate, regardless of earlier unspecified history.

**The seven-block script already has a smaller predecessor under the PR192 construction.** For four starting L's the older PLPL ramp at \(\ell=1\) starts at \(m_{\rm old}=(x-9)/16\) and reaches \(y=3(q_{\rm P}+7)/2-1\) after nine odd clocks, where \(q_{\rm P}\) is the entrance to the first P. In the older PLPL row, dropping the last odd bit of 011101010010001 leaves fourteen bits, six odd visits and carry \((24550-2^{14})/3=2722\). Substitution into the raw partial-source equation gives \(2^{14}f=3^6y+2722\). This equation forces the correct least residue of \(y\bmod2^{14}\) independently of the parity of \(f\) or the next source step. Therefore \(T^{23}m_{\rm old}=f\) even on the partial terminal L. Moreover \(m-m_{\rm old}=(x+7)/32>0\). The 22-clock script is one clock shorter and uses a larger predecessor. Its same-source existence conclusion on this cylinder already follows from PR192. An unrestricted prehistory need not have a minimum above either partner.

There is also a finite counterexample to requiring a directed smaller predecessor for *every* odd PR174 input. Each \(1\le m<55\) reaches one within 71 shortcut steps and none visits 55 before doing so (846 literal steps total when all 54 paths are followed separately). The subsequent 1–2 cycle omits 55. Thus 55 itself has no smaller predecessor, although it converges. A general least-nonconverger or eventual-merger argument has a different conclusion.


## Frozen inputs and scope

| Source | SHA-256 |
| --- | --- |
| SustainedResidual.lean | 951817b99d9ab64b21520ccc4cc1c336c3822d02f96a536c157dc75188dc2920 |
| ResidualDescent.lean | b5f149855866419b771e49127bdaabd1cb5749ec7d6f3b6091f3fb54bf1ccc98 |
| HeightPartner.lean | e908f6c8738f06754ebc3b76b7deac0335e700a2e0ffbddee7314f1cd0a1ec6f |
| PastCylinder.lean | 2f3904caf3ea257820b1328673a1c4745202b7f89a9723639eb055618b569fe3 |
| CycleShadows.lean, imported finite lifting | 05ef6b77b2ce9d571c598e5a0e4a526be3412b844349476ec72408b0bf145e99 |
| PR192 DESCENT_EXTENSION.md at d2081d1cd2410e6004eaee9f9b13c5553afaf3f4 | e902faffe7ee584ad354119d7809e0a4b663a12373fe7d2244dac5c84cb370d1 |

I independently recomputed the displayed affine coefficients and literal bits, reconstructed the infinite families and density, and checked these source hashes. CycleShadows and ResidualDescent were also rebuilt from these source bytes as inputs to the later clean replay of LongPast. The other three author modules have their own recorded strict-build receipts. The 16-case synthesis uses the pinned prior certificates, and the asymptotic density and power-of-two member constructions are written arguments. My separately authored LongPast certificate is outside this independent review.
## Independent check of the three-clock order bound

I checked HEIGHT_CLOCKS.md at SHA-256 280349f0b49d6ca4be3421ec0ca4bcb56c740e08eff7d613710172fb9e423165. At true height \(H=v_3(n-1)\), take \(s\) initial inverse positive-cycle tours, then \(j\) doublings, then \(d\) inverse odd moves, and write \(t=H-s\). The word is integral exactly at the indicated ternary divisibility after the tours. If \(1\le d\le t\), divisibility forces \(2^j\ge3^d-1\), giving a coefficient greater than one and a constant at least one in the resulting \(m\). Hence success requires \(d>t\). With \(a=\log(4/3)/\log(3/2)\) and \(b=\log2/\log(3/2)=a+1\), the necessary output-size constraint yields \(d-t>aH+b(j-t)-b\). For \(t>0\), the initial guard modulo \(3^t\) gives \(3^t\mid2^j+1\), forcing \(j\) odd and \(j\ge3^{t-1}\) by \(v_3(2^j+1)=1+v_3(j)\).

A fixed triple occupies at most one class modulo \(3^{d-t}\) for the unit \(v\), with relative density at most \((3/2)3^{-(d-t)}\), also upon requiring \(v\equiv2\bmod4\). Positivity and the strict output-size condition cut that class by linear inequalities, so finite unions have natural density. Summing over the necessary \(d,j,t\) gives an absolute constant times \(3^{-aH}\), since the exponential lower bound on \(j\) dominates the exponential cost in \(t\). For inputs \(v\le X\), every successful word satisfies \(2^d\le m+1<n+1\) and \(j=O(d+1)\). There are only \(O_H(\log^2(X+2))\) relevant triples, giving negligible total integer-rounding error. Thus the convergent density majorant controls the infinite union's tails, and the natural density exists. The original \(s=H,j=0,d=\lceil aH\rceil\) family supplies a matching lower bound with an absolute constant. The \(\Theta(3^{-aH})\) result is valid for this *ordered* inverse-word class.

As a separate arithmetic check on the basic positive-tour density, selecting \(d_H\) by the exact integer inequality \(2^{d_H+2H}\le3^{d_H+H}\) and summing through \(H=150\) gives \(0.0509640473681569571980540\ldots\). The remaining tail is at most \(27/(2\cdot3^{150})<3.65\cdot10^{-71}\).

