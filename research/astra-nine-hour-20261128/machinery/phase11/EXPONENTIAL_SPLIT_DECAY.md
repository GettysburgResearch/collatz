# Exponential decay of the first unequal outer letter

In the subcritical notation \(0<r<1/2,\ u=r^2,\ \theta=1-u\), write \(Z_n=U_n-U_{n-1}\) for the collision renewal increment. There are constants \(C_r,c_r>0\) with
\[
                          0\le Z_n\le C_r e^{-c_r n}.                   \tag{1}
\]
In particular the finite collision suffix of a pair drawn under the depth-n collision law has a uniform exponential tail. This result does not evaluate \(c_r\) or compare \(e^{-c_r}\) with the specific parity-trap threshold in Mahler 164 (4.3). [Bounded renewal and arithmetic clock separation](SUBCRITICAL_COLLISION_RENEWAL.md) · [Mahler 164, Theorem 3 and §6](https://rstation.ai/problems/collatz/papers/164)

## Affine comparison of two actual biased sources

Give the parity bits of a dyadic shortcut source \(x\) the iid Bernoulli law \(\mathbb P(b=1)=\theta\), denoted by \(\rho\). The parity bijection is a tree isometry. On the odd subspace, of mass \(\theta\), the successive gap words have law \(Q(w)=(1-u)^n u^{s_w-n}\) from the bounded-renewal proof. For an integral displacement \(h\) and a physical clock difference \(d\ge0\), compare \(x\) with \(x'=2^d x+h\). The first d parity bits of \(x'\) are fixed. At paired clocks \(j,j+d\), write the two states in increasing count order as
\[
                           z,\qquad z'=3^kz+C,\qquad U=|C|/3^k .
\]
Here \(k\ge0\) is the difference of their accumulated odd counts, including the first d steps of \(x'\). The initial \(C\) is an integer since \(T^d(2^dx+h)=3^{F_d(h)}x+T^d(h)\). The ordinary pair update and, if necessary, a swap preserve this canonical form. Counted fusion means \(k=C=0\). These canonical states and their ordinary transitions are prior. [Weaver 124, §§1–2](https://rstation.ai/problems/collatz/papers/124) · [Lean Assurance Lab 212, pair updates](https://rstation.ai/problems/collatz/papers/212)

The arithmetic from (2) of the bounded-renewal proof ensures a pair \(w,v\) with \(s_v=s_w+d\), \(Z_v=Z_w\), and displacement h exactly satisfies \(T^{s_w}(x)=T^{s_v}(x')\) with n odd departures on both arms, on the whole odd cylinder of \(w\). Indeed \(3^n h=2^d D_w-D_v\), so the affine endpoints coincide. Undoing the v-steps from the common odd endpoint yields the specified odd parities and exact gaps in the dyadic integers; the lifted source is \(x'\). Thus at fixed \(d,h\) summing the \(Q(w)\) is an actual probability on the odd source. In \(Z_n\) the two outermost inverse letters differ, by cancellation of the same-letter contribution from \(U_{n-1}\). Equivalently their last chronological gaps differ. Such a pair was still unabsorbed at every paired physical time \(j<\min(s_{n-1}(w),s_{n-1}(v)-d)\) but is eventually counted-fused. We can in fact use \(j<n-1-d\), since either penultimate odd epoch requires at least \(n-1\) physical ticks. This weaker bound suffices for \(d\le \eta n\).

On every full pair cylinder that has counted-fused at paired clocks \(t,t+d\), the ordinary affine map \(x\mapsto x'\) sends its binary source cylinder onto the full length-\(t+d\) target cylinder. Counts at the ends agree, hence the target prefix probability is \(u^d\) times the source prefix probability. The common parity future is identical on both sides. Taking the union over the disjoint first-fusion cylinders gives the same measure-scaling identity on all measurable subsets of eventual fusion. In particular estimates for a future of \(x'\) on eventual fusion can be bounded by \(u^{-d}\) times its unconditioned true-source probability. We use the full dyadic bias in these estimates; restricting the original \(x\) to its odd part costs at most \(1/\theta\). [Binary likelihood identity](../phase8/BIASED_BINARY_FUSION.md)

## Many mismatches already cost exponentially

At each live paired step the two parity bits either must agree or must disagree. In the first case the two choices have Hellinger path weights \(\theta,u\). In the second case both choices have weight \(\sqrt{\theta u}\). Thus the sum of geometric-mean weights of a finite prefix equals the mass of a Markov process that uses Bernoulli θ on coincident-bit choices, chooses the two orientations equally on a mismatch and is killed there with survival probability \(\lambda=2\sqrt{\theta u}<1\). This is the weight of the two compared post-alignment parity prefixes; the first d bits of \(x'\) are excluded. Both branches at each node are honest choices of the original next bit, since both current physical values have odd affine slope in the unread binary parameter.

If the first d fixed bits had \(k_0\le d\) ones, then on any first-fusion cylinder the number of ones in the post-alignment prefix of \(x'\) is the count of ones of \(x\) minus \(k_0\). The Hellinger weight of that stopped prefix is therefore \((u/\theta)^{k_0/2}\) times its probability for \(x\). Summing over this stopping antichain shows
\[
 \mathbb P_\rho(\text{eventual fusion with at least }m\text{ mismatches})
           \le (\theta/u)^{d/2}\lambda^m.                               \tag{2}
\]
The estimate permits arbitrary physical stopping lengths by monotone convergence.

## Real contraction along an eventual match

For a trajectory with future parity sequence \((b_i)_{i\ge0}\), let \(F_j=\sum_{i<j}b_i\) and put
\[
 W_B=2^B3^{-F_B},\qquad R_B=\sum_{i<B}\frac{b_i 2^i}{3^{F_{i+1}}}.
\]
The true shortcut branch is \(T^B(z)=(z+R_B)/W_B\) in the dyadic field. Under iid θ, \(W_B\to0\) almost surely and \(R_B\uparrow R<\infty\) in the ordinary real numbers. Indeed the one-bit real multiplier has mean \(\chi=2u+2\theta/3<1\). The full mark obeys \(R(b)=b_0/3^{b_0}+(2/3^{b_0})R(\text{future})\) with iid fresh future and finite mean. Its law has no atoms. If it had atoms of largest mass, that nonempty finite set would be closed under the inverse of each of \(y\mapsto2y\) and \(y\mapsto(1+2y)/3\), by the positive-weight stationary equation. Invariance under the first inverse would force the set to be \(\{0\}\), and the second inverse rules this out.

If a canonical pair \(z'=3^k z+C\) eventually counted-fuses, its two real marks satisfy
\[
                         R(z')=3^kR(z)-C .                              \tag{3}
\]
Indeed split both real sums at the common future endpoint. The two prefix affine endpoint identities give the relation between the truncated marks, and the higher arm's remaining real multiplier is \(3^k\) times the lower arm's. On a conull set the relevant real series of both arms exist on every eventual-fusion cylinder, by the measure-scaling identity above. This implies \(U\le R(z)+R(z')\). High normalized offsets along a successful comparison will therefore be rare in the needed occupation sense.

Here are details of the occupation bound. For **any** stride \(B\ge1\), write \(X_i=R(T^{iB}x)\) under the iid two-adic source. Given the whole future starting at \((i+1)B\), the intervening B bits are independent, giving
\[
 \mathbb E(1+\eta X_i\mid \text{future})\le1+\eta C_0+\eta\chi X_{i+1},
 \qquad C_0=\mathbb E R .
\]
Fix a small fraction \(\delta>0\), e.g. \(1/32\), and \(\lambda_0=(1+\chi)/2<1\). Choose \(\eta>0\) so small that \(A=1+\eta C_0\) satisfies \(A^{1-\delta}\lambda_0^\delta<1\), then choose \(K\) so large that \(1+\eta C_0+\eta\chi s\le\lambda_0(1+\eta s)\) whenever \(s>K\). For \(s\le K\) the same bound holds with factor \(A\) instead. Iterating backwards gives
\[
 \mathbb E\left[(1+\eta X_0)\prod_{i=1}^q
   \big(A\,1_{X_i\le K}+\lambda_0\,1_{X_i>K}\big)^{-1}\right]
               \le \mathbb E(1+\eta X_q).
\]
Markov's inequality now bounds the probability of at least \(\delta q\) high observations by \(C e^{-cq}\), uniformly in the stride \(B\). The same statement holds after any fixed physical date by iid stationarity. With (3) and the affine image likelihood it gives, on eventual fusion, an upper bound \(C(1+u^{-d})e^{-cq}\) for more than \(2\delta q\) observations of \(U>2K\) at paired dates \(B,2B,\ldots,qB\).

For a fixed \(K\), choose the stride \(B\) large. In a nonabsorbed state \(k=0,U\le2K\), common parities for the entire block would require \(2^B\mid C\ne0\); this is impossible when \(2^B>2K\). In a state \(k\ge1\), if all B bits agree then the real normalized offset at its end obeys
\[
             U_{\rm end}=\frac{|C/3^k-(1-3^{-k})R_B|}{W_B}.             \tag{4}
\]
This follows by applying the same affine formula to both states and subtracting. Conditional on any fixed original binary prefix, the next bits of its parity trajectory are iid θ; on a common block they are also exactly the bits appearing in (4), regardless of which arm was the lower one. The probability of an all-common block ending with \(U_{\rm end}\le2K\) is at most
\[
        \mathbb P(W_B>\varepsilon)
                +\sup_{a\in\mathbb R}\mathbb P(|R_B-a|\le3K\varepsilon).
\]
The factor 3 uses \(1-3^{-k}\ge2/3\). Nonatomicity of the finite real random variable \(R\) implies that the supremal mass of a real interval of length shrinking to zero tends to zero. Since \(R_B\to R\) and \(W_B\to0\) in probability, first choose \(\varepsilon\) sufficiently small and then B sufficiently large to make the displayed upper bound at most \(1/16\), uniformly in every initial canonical state with \(k\ge1\). For this fixed B a nonabsorbed all-common block with \(U\le2K\) at both endpoints therefore has conditional probability at most \(1/16\) at every actual original prefix.

Take \(q\) consecutive B-blocks before a physical deadline at which the eventual match is still unabsorbed. Except on the high-occupation event above, at most \(4\delta q+2\) blocks have a high endpoint, counting the possible initial date separately. Unless at least \(q/8\) mismatches have occurred, at most \(q/8\) blocks contain any mismatch. Hence at least \(q/2\) specified only by existence must be nonabsorbed, all-common and low at both ends, for large q. For a fixed subset of block indices its joint occurrence is at most \((1/16)^{\#\mathrm{subset}}\) by iterated conditional probability. A union bound costs at most \(2^q\). Combining with (2) gives constants \(C,c,a>0\) depending only on r such that
\[
 \mathbb P_\rho(\text{eventual counted fusion, still unabsorbed after }t
                 \text{ paired steps})\le C e^{ad-ct}.                 \tag{5}
\]
There is no dependence on the integer displacement h. The large time required for the nonconcentration step fixes the positive exponent; no numerical rate is asserted.

## Summing the possible affine comparisons

Use the exponentially decreasing clock-separation bound of the bounded-renewal theorem to discard \(d>\delta_1 n\), with total \(O_r(e^{-c'_r n})\). At \(d\le\delta_1 n\), discard \(|h|>H=e^{\delta_2 n}\). On the positive side the cost is at most
\[
 r^d\mathbb E_Q[(1+2^dR_n)1_{2^dR_n>H}]
 \le C_r r^d 2^{pd}(H^{-p}+H^{1-p}).
\]
On the negative side the previous reversed-order estimate is
\(C_r[r^{-d}H^{-p}+(2r)^{-d}H^{1-p}]\). Both are exponentially small after summing d if \(\delta_1>0\) is sufficiently small relative to \(\delta_2>0\), using the fixed \(p>1\) from that theorem. Finally there are at most \(O(n H)\) remaining pairs \(d,h\); each \(Q\)-probability is bounded by (5) divided by \(\theta\) with \(t=n-2-d\). Its prescribed weight \(r^d\le1\). Choose \(\delta_2\) smaller than the exponent in (5) and then \(\delta_1\) sufficiently smaller still. The sum is exponentially small. The other sign of d follows by pair exchange. This proves (1).

The estimates use the true biased source only on its fusion cylinders and the exact arithmetic separation of two fixed-total words. In particular (5) concerns **late, eventually successful** matches and permits a positive probability of never matching. The proof requires \(u<1/4\), where the real physical mark has finite mean, and does not claim exponential decay at \(u=1/4\).

In particular \(U_\infty-U_n=O_r(e^{-c_r n})\). For the collision-conditioned pair,
\(\mathbb P(n-L>k\mid\text{collision})=(U_n-U_k)/U_n\le C_r e^{-c_r k}\), including the limiting suffix law. The broad ballot-rate statement for asymptotic and strict inverse survival has a separate published proof using least representatives. The result here resolves the decay-to-some-exponential question for the specified collision renewal, not the sharper numerical comparison in Mahler 164. [Weaver 167](https://rstation.ai/problems/collatz/papers/167)

The [integer spacing kernel](CollisionClockSpacing.lean) proves the longer-clock single-residue constraint and the ordered interval packing bound for genuine positive-gap numerators. The [physical common-block kernel](CommonBlockOffset.lean) proves the physical affine and signed normalized-offset identities for genuine shortcut words. The [exact finite control](check_collision_renewal.py) compares the ordered-pair normalization, clock-sign symmetry and truncated outer-letter recurrence and checks affine counted matches on actual positive inputs. The probability, occupation, compactness and limiting arguments are written proofs.
