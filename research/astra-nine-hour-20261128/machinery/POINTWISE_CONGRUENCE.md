# Pointwise congruence steering at a prescribed odd depth

**PROPOSED, elementary written proof.** Let \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on the positive odd integers. Put
\[
 \eta_n^a(E)=\sum_{\substack{U^nx=a\\x\in E}}3^n2^{-S_n(x)},
 \qquad \rho_n(a)=\eta_n^a(\mathbb N),\qquad
 S_n(x)=\sum_{j<n}v_2(3U^jx+1).
\]
For every odd \(q\ge5\) coprime to six with \(3\nmid d=\operatorname{ord}_q(2)\), set \(R=2q-1\) and \(B=(4+4d)R\). For every positive odd \(a\) coprime to three, every residue \(u\bmod q\), and **every individual** \(n\ge R\),
\[
 \frac{\eta_n^a(u\bmod q)}{\rho_n(a)}
       \ \ge\ (3/2)^R 2^{-B}.                                      \tag{1}
\]
The constant is uniform in \(a,n,u\). It applies to normalized raw depth measures at zero overshoot along a single ordinary escaping ray, conditional on that ray existing. Every \(q=5^j\) is available, since \(\operatorname{ord}_{5^j}(2)\mid4\cdot5^{j-1}\). More generally every allowed \(q\le(n+1)/2\) is available with a lower bound \(\exp(-Cq^2)\), with absolute \(C\).

For **every** \(q\ge5\) coprime to six and every \(b,r\ge0\), an explicit common odd depth \(R=2q\operatorname{ord}_q(8/9)+2(q-1)+b\) and raw clock bound \(B=B(q,b,r)\) have the same property for all nonempty cells modulo \(2^{b+1}3^r q\) meeting the odd integers. The expressions in the final section are large. The two constructions apply to the actual inverse map with its positive valuations.

## A finite path implies the full normalized floor

Write \(I_e(z)=(2^ez-1)/3\) for an inverse step with \(e\ge1\) and \(2^ez\equiv1\bmod3\). For positive odd \(z\) it has positive odd value with true outgoing valuation \(e\). In one step the sum of all weights \(3\,2^{-e}\) is either zero, one, or two, with zero precisely at \(3\mid z\). Let \(T\) be this positive transfer on bounded test functions and \(V\) the set of positive odd ternary units. If from each \(z\in V\) there exists one path of exactly \(R\ge1\) letters of total \(e\)-sum at most \(B\) into a cell \(E\), then
\[
 T^R1_E\ge 3^R2^{-B}1_V,\qquad T^R1\le 2^R1_V .
\]
Apply \(T^{n-R}\) to obtain (1), whenever \(\rho_n(a)>0\). Each unit has a unit inverse successor, so that denominator is positive for every \(a\in V\). The same inequality holds after every positive mixture of source rows, whenever its total mass is finite and nonzero.

## Small raw clock when \(3\nmid\operatorname{ord}_q(2)\)

Put \(H=2d\). Then \(2^H=4^d\equiv1+3d\bmod9\) so \(v_3(2^H-1)=1\). For any \(z\in V\) and a nominal legal \(e\), the three choices \(e,e+H,e+2H\) have the same image modulo \(q\) and give all three residues of \(I_{e+kH}(z)\bmod3\). This follows by expanding \(2^{kH}\bmod9\). Choose the one giving residue one. In a first step take nominal \(e=1\) or \(2\) according to the parity required by \(z\bmod3\). Every remaining nominal \(e\) may now be chosen freely from \(\{2,4\}\), with the same three-way adjustment.

On \(\mathbb Z/q\) the two maps \(A=I_2\) and \(D=I_4\) are permutations. The compositions \(AD,DA\) have the same slope and intercepts \(-7/9,-19/9\). Thus \((AD)(DA)^{-1}\) is translation by \(4/3\), a generator of the additive cyclic group. In a finite permutation group the two maps and their positive powers contain their inverses. The directed graph on the \(q\) residues is strongly connected, and shortest paths have length at most \(q-1\). Since \(A(1)=1\), one can travel from any residue through \(1\) to any target using exactly \(2(q-1)\) letters by inserting idle \(A\) steps at \(1\). Perform this after the first adjusted step. Each actual letter is at most \(4+4d\). This proves the announced \(R,B\).

## All coprime moduli and simultaneous binary and ternary precision

Use the permutations \(C=I_1,D=I_2\) on \(\mathbb Z/q\). Composition is right to left:
\[
 CD(u)=(8u-5)/9,\qquad DC(u)=(8u-7)/9 .
\]
The second affine map fixes \(-7\), so its order is \(l=\operatorname{ord}_q(8/9)\). The positive word \(W=(CD)(DC)^{l-1}\) translates by \(2/9\) in exactly \(2l\) letters. The \(q\) successive boundary states of \(W^q\) visit every residue. The positive \(C,D\) graph is strongly connected, shortest paths have length at most \(q-1\), and \(D(1)=1\).

For a word \(w\) of \(L\ge1\) letters and total clock \(s\), its rational output is \((2^s z-c_w)/3^L\). The integer \(c_w\) is positive and prime to three. For a desired terminal residue \(v\bmod3^h\), all steps are integral with that endpoint exactly when
\[
 2^s z\equiv c_w+3^L v \pmod {3^{L+h}}.                            \tag{2}
\]
To see sufficiency, at each stage the final integrality implies the integrality of all previous stages by successively reducing the remaining congruence. This equivalence holds with \(h=0\). A prefix having a following integral inverse step ends at a ternary unit. The right side in (2) is a unit. The powers of two run through all units modulo \(3^t\): \(2\) has order \(2\) modulo three and \(v_3(4^{3^k}-1)=k+1\) by induction. Consequently an arbitrary unit \(z\) can be replaced by \(2^\delta z\) to satisfy (2), for \(0\le\delta<2\cdot3^{L+h-1}\). In the positive odd inverse path this replacement means adding \(\delta\) to the *first* chronological letter. All subsequent inputs are positive odd integers.

Choose such a prefactor for \(W^q\) with final residue one modulo three. If the initial residue modulo \(q\) was already zero, skip this whole stage. Otherwise \(2^\delta z\) is nonzero modulo \(q\) and some boundary after \(W^j,\ 1\le j\le q-1\), reaches zero. Stop there. The remaining legal continuation ensures that the current ordinary integer is a ternary unit. This stage has at most \(2lq\) odd steps, raw clock at most \(4lq+2\cdot 3^{2lq}\), and ends at residue zero modulo \(q\).

For a desired odd residue modulo \(2^{b+1}\), take its positive odd representative \(y\le2^{b+1}-1\). Record the first \(b\) true valuations along \(y\), then arrange them in reverse as an inverse suffix \(v\). When \(b=0\) take the empty suffix. If \(x\) is the output of \(v\) from any odd input for which it is integral, then \(x\equiv y\bmod2^{b+1}\): the affine response to the change from \(U^b(y)\) has valuation at least \(1+S_b(y)\ge b+1\). Also \(U(t)\le(3t+1)/2\le2t\) on positive odd inputs and
\[
 2^{S_b(y)}U^b(y)=\prod_{i<b}(3+1/U^i(y))\,y\le4^b y ,
\]
so \(S_b(y)\le3b+1\).

Write \(s_0\le2lq\) for the number of steps used in the first stage. Put \(R=2lq+2(q-1)+b\). Take a word in \(C,D\) with exactly \(L=R-s_0-b\ge2(q-1)\) letters reaching from zero modulo \(q\) to the unique \(q\)-preimage of the required final residue under \(v\). This uses the route through the loop at one. Append \(v\). Equation (2) for this entire \(L+b\)-letter block lets us prescribe the required final ternary residue modulo \(3^r\) by another initial prefactor \(2^{\delta'}\), with \(\delta'<2\cdot3^{R+r-1}\). This second prefactor acts at a zero residue modulo \(q\), so the terminal \(q\)-residue is preserved. It changes the first of the \(C,D\) letters, leaving the binary suffix intact. The total raw clock is bounded by, for example,
\[
 B=4lq+2\cdot3^{2lq}+2R+3b+1+2\cdot3^{R+r}.
\]
The path is an ordinary positive odd inverse trajectory, has exactly \(R\) steps, and ends in the prescribed joint cell.

## Scope and relation to earlier congruence results

The back-tracing construction of Monks, Monks, Monks and Monks, Theorem 4.1, reaches any fixed full congruence class from any unit target with a uniform upper bound on odd steps. Their statement permits varying odd depth and omits a total valuation budget. The normalization in (1), common exact odd depth, and uniform polynomial valuation budget for the indicated infinite family of moduli are the features used here. [Primary theorem and proof](https://arxiv.org/html/1204.3904v2)

For \(q=5^j\), (1) excludes concentration outside any one specified \(5\)-adic residue at every sufficiently large individual depth, quantitatively and without smoothing or overshoot. The lower bound deteriorates rapidly with \(j\). It supplies no comparison between the total ordinary densities of a target and a prescribed *first* inverse sibling. The controlled portion of the path is at its **source end** after the common initial \(n-R\) inverse steps. A fixed zero-overshoot posterior may retain a large atom, consistently with (1). The joint fixed-modulus Haar theorem under diverging overshoot has a different conclusion.
