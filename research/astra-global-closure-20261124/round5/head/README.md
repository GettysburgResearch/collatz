# A summable opposite-phase test on whole growing intervals

**PROPOSED written bounds on the original ordinary sources, using the stated synchronization inputs. Universal convergence remains OPEN.** Use the positive shortcut \(T(2n)=n\), \(T(2n+1)=3n+2\). Let \(L(z)=B\) if \(z\) never reaches one, and let \(L(z)=+\) or \(-\) if its first shortcut time to one is even or odd, respectively. Write \(\iota\) for the permutation exchanging the signs and fixing \(B\). The cycle \(1,2\) gives \(L(T^s z)=\iota^s L(z)\) at every clock.

In row \(j\) put \(R_j=81^j\), \(7R_j\le x<8R_j\), \(y=\lfloor x/81\rfloor\). Fix a nonempty open interval \(J\subset(7,8)\). Count only edges \(x/R_j\in J\) with \((L(x),L(y))=(B,+)\), giving each original child weight \(1/R_j\). For every \(0<\beta<1/12\) the total weight, summed over all rows, of edges for which **some** positive integer within distance \(\lfloor\exp(j^\beta)\rfloor\) of either endpoint has label \(-\) is finite. The tested neighbor can depend on the entire ordinary source and its future. More generally the result holds for either directed orientation and either prescribed terminating phase, testing for the other phase.

There is a further estimate after forward steps. For any fixed \(K>0,\ 0<\alpha<1/4\), one can discard at finite total weight all these edges for which, at **any** common shortcut clock \(0\le s\le j^\alpha\), either actual iterate \(T^s x,T^s y\) has within distance \(j^K\) a positive integer carrying the third label \(\iota^s(-)\). At the single deterministic clock \(s=\lfloor j^\alpha\rfloor\), every \(0<\alpha<1/2\) is admissible. At large rows all the displayed windows are positive by \(T^s n\ge n/2^s\).

Thus the earlier directed head reduction can retain just edges with both entire stretched-exponential intervals free of the third phase, together with the stated exclusions along their two orbits. Under the fixed-target density input M, a finite total weight for this remaining population implies universal convergence. The earlier mesoscopic `GOODPROFILE` restriction may be intersected at its own fixed clock. None of these estimates establishes how often an actual bad/terminating pair persists inside the two allowed labels.

## Compressing a whole interval at an early prefix

The counting device uses Lyapunov Weaver's *Synchronization of growing Collatz blocks and selected references*, rStation paper 124, v1, (7)–(12). We need the stopped **positive sibling** estimate inside that proof, rather than the \(h^{-1/2}\) tail of its whole-block fusion theorem. The scalar chain and synchronization estimates used by the source are credited to Said Duran and David Leen. [Primary manuscript](https://rstation.ai/problems/collatz/papers/124)

Start a consecutive interval of \(D\ge2\) forms \(z,z+1,\ldots,z+D-1\) at equal initial grade on the one parameter, with \(z=3^a n+c\). At each depth the equivalence relation is equality of the full affine profiles in the *same* remaining quotient. Use \(m=\lceil256\log(\max(D,4096))\rceil\) original bits. Keep the rightmost index of each class at \(m\), obtaining a prefix-measurable set \(\mathcal R_m\). Then

\[
                      \mathbb E\#\mathcal R_m\ll(1+\log D)^3.       \tag{W1}
\]

To see the source of the saving, take a position with \(k\) positions left including itself. Its future prefix is Haar because its parameter slope is odd. For \(k\ge4096\), take \(m_k=\lceil256\log k\rceil\le m\). Outside a prefix event of probability \(\le k^{-8}+m_k^2/(k-1)\), this position has a strictly later sibling in the block with identical odd count and iterate at a common clock \(\le m_k\). The source proves this by stopping a parity word when \(2^s/3^{p_s}\) first exceeds \((k-1)/m_k\). For a given stopped length and odd count, two word numerators in one residue modulo \(3^{p_s}\) give the integral displacement of a counted sibling. Selecting the least numerator leaves total exceptional mass \(O(m_k^2/k)\), in addition to the binomial stopping tail. The equal slopes and equal values on its cylinder make this profile identity valid for every positive lift, so the position cannot be its class's rightmost representative at \(m\). For \(k<4096\) use probability one. Summing over \(k\) proves (W1). The positions need not have independent histories. The same estimate holds conditionally if the entire block is specified by an earlier common prefix and its current center still has odd slope in the remaining quotient.

## The native clock for the original head pair

Write \(x=81y+r\), \(0\le r<81\). First fix \(r\). For each of the two endpoint windows take its consecutive block of \(D\) forms, of radius \((D-1)/2\) if \(D\) is odd. Use \(h=\lfloor\log_2(R_j/81)\rfloor\asymp j\). For \(h\ge2m\), the relative original-source count of the directed event with the third label somewhere in this block is

\[
             \ll_p \frac{(1+\log D)^{3+2p}}{(1+h)^p},
             \qquad 1<p<3/2 .                                      \tag{W2}
\]

Condition on the full \(m\)-bit prefix of \(y\). If the two head profiles have fused already, the directed event is empty. Otherwise any third eventual label is carried by a member of \(\mathcal R_m\), by persistence of prefix equality and the common phase flip after the same number of clocks. For each such representative compare the *given two head profiles* and that representative. Their maximum grade gap is \(\le4+m\). At clock zero the normalized offsets \(|D_{ik}|/3^{s_{ik}}\) for all three pairs are \(O(D+1)\). The scalar transition table bounds a one-step normalized magnitude by \((3/2)\) times its old value plus one, also if the orientation changes at zero grade. After \(m\) clocks, the log of two plus the largest magnitude is therefore \(O(1+\log D+m)\). Consequently \(Q\ll(1+\log D)^2\) in the [uniform triple-moment bound (U1)](UNIFORM_TRIPLES.md). Its conditional probability of surviving as three profiles through clock \(h\) is at most \(C_p((1+\log D)^2/(1+h))^p\). The chosen representative and its coefficients are fixed by that prefix. Sum this all-state upper bound over \(\mathcal R_m\) on the prefix and then use (W1). This bounds the Haar probability of the witnessing *finite profile event*, which contains the actual three-label event. It never takes conditional probabilities given an eventual basin.

The full head parent interval has exactly \(R_j/81\) consecutive integer parameters for each \(r\). It is covered by at most two algebraic residue grids of length \(2^h\), each of which assigns exactly the Haar count to every \(h\)-bit event. This gives (W2) after multiplication by an absolute constant, with the original children still counted once. Summing the 81 residues, dividing by \(R_j\), taking the union of the two windows and restricting to \(J\) preserves the bound. Finitely many rows before \(h\ge2m\) contribute a finite constant to either stated application. For \(D=2\lfloor e^{j^\beta}\rfloor+1\) the right side of (W2) is \(O_p(j^{-p+\beta(3+2p)})\). For example, \(p=5/4+3\beta\) gives

\[
 p-\beta(3+2p)-1=(1-12\beta)(1/4+\beta/2)>0.
\]

This proves the first summability claim. Merely summing the fixed-triple estimate over \(D\) neighbors would lose the conclusion for every positive \(\beta\).

## Neighborhoods at later physical clocks

For \(1\le s\) with \(s+m\le h/2\), let \(e_{j,s}(D)\) be the normalized original count among the fixed directed \((B,+)\) edges with a third label in either of the two length-\(D\) centered blocks at the actual clock \(s\), with labels read at that clock. For each fixed \(A_0>1\),

\[
 e_{j,s}(D)\ll_{p,A_0} (1+j)^{-A_0}+
 \frac{(1+\log D)^3}{\sqrt{1+s}}
 \left(\frac{(1+\log D)^2+(1+s)\log(2+j)}{1+j}\right)^p.          \tag{W3}
\]

Expose the \(s\) original bits first. The head pair's signed grade difference is a bounded-increment martingale starting at four. Its normalized offset has uniformly bounded square-root moment by the one-step contraction and bounded initial state. Azuma and Markov therefore discard \(O_{A_0}((1+j)^{-A_0})\) at this particular clock so that

\[
   |4+p_x(s)-p_y(s)|\ll_{A_0} 1+\sqrt{s\log(2+j)},\qquad
   |Z_s|\le C_{A_0}(2+j)^{2A_0}.
\]

On every remaining prefix the head must still be live. This event has unconditioned probability \(O((1+s)^{-1/2})\), by the scalar tail on the original fixed head state. Centering a block of shifts at either of the two present profiles adds at most \(D\) to the maximum normalized pair offset. This is immediate in either orientation from the formula \(z_{\rm high}=3^g(z_{\rm low}+Z_s)\). The new arms inherit their center's exponent in the remaining original quotient. Apply (W1) to their next \(m\) bits. Independently of the outcome of those bits, their grade spread then increases by at most \(m\), and their log-offset bound increases by \(O(1+m)\). Thus (U1) after the full \(s+m\) prefix has \(Q\ll_{A_0}(1+\log D)^2+(1+s)\log(2+j)\). Average the representative count conditionally on the given \(s\)-prefix *before* summing over live \(s\)-prefixes. This gives the product in (W3) without independence of survival, the grade and the endpoint labels. The same two-grid argument converts the \(h\)-bit bound into the original count. The discarded prefix must be paid only once per tested clock.

For \(D=2\lfloor j^K\rfloor+1\), the second term is \(O_{p,K}(j^{-p}(1+s)^{p-1/2}(1+\log j)^{3+2p})\) for large \(j\). A union over \(1\le s\le j^\alpha\) gives exponent \(-p+\alpha(p+1/2)\). Use \(A_0>2+\alpha\) for the first term. Since \((p-1)/(p+1/2)\uparrow1/4\) as \(p\uparrow3/2\), the result is summable for all claimed \(\alpha<1/4\). At a single prescribed \(s=\lfloor j^\alpha\rfloor\), the exponent is \(-p+\alpha(p-1/2)\), yielding the bound up to \(\alpha<1/2\). Clock zero is covered by (W2). The presence of an opposite-phase integer can be tested from its unbounded future. Only the containing finite profile event is required to be measurable at \(h\).

## The remaining ordinary estimate

Let \(D_N^{\rm rem}(J)\) count the original directed edges through row \(N\) satisfying both absence conditions above for any *fixed* admissible parameters. By (W2)–(W3) its difference from the original directed mass is bounded uniformly in \(N\). At PR195 `b69ec87d28f539233a32b7c07964f5605320eb71`, `research/astra-global-closure-20261124/round4/head/README.md`, Theorem 1, the full unphased log-weighted vertical variation is \(\le C_J(1+D_N^{\rm rem}(J))\), after changing the constant. With Mazur's fixed-target predecessor-density input M this gives

\[
     \text{every positive integer reaches one}
     \quad\Longleftrightarrow\quad \sup_N D_N^{\rm rem}(J)<\infty.
\]

M is used only for this closure implication. Its reported formal release counts ordinary predecessors under every sufficiently large full cutoff. It supplies no bound on a phase-free short interval centered at a selected discordant source. [Author's theorem and scope](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

PR201 `084b983fbec6f3d2120ef101946754431f82874e`, `research/killed-green-head-closure-20261124/README.md`, (KG8)–(KG11), allows its own `GOODPROFILE` conditions on the *same children*. Its continuation `continuation/README.md`, (G1), disperses one absolute grade while retaining the actual roots and signed gaps. PR193 `5f160a843750f209ea1251dfb01ea0b23e532fd6`, `research/astra-ordinary-boundary-20261124/transfer/ALL_EVENTUAL_MEETINGS.md`, (1), provides only an absolute \(o(1)\) upper-deadline error for this paired sample. PR200 `39918be724038ac550d77c7fc95d17e05251dfc6`, `research/regularity-rigidity-20261124/continuation/FOURIER_UNIFORMITY.md`, (FOU), estimates a single invariant label. None supplies a summable upper bound for \(D_N^{\rm rem}\). The odds and clocks in the labels and windows above belong to the two original physical trajectories throughout.

`WindowRepresentatives.lean` checks existence and separation of rightmost representatives, persistence of an arbitrary third label, the prefix-dependent finite covering count, and a concrete exponent allocation. The probability estimates, ordinary transfer and density implication are written mathematics. `check_windows.py` tests the symbolic compression on ordinary lifts at bounded clocks. It makes no eventual-color assignments.
