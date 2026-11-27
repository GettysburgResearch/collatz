# Simultaneous smaller physical representatives on every translated interval

**PROPOSED written theorem.** Use the positive shortcut map \(T(n)=n/2\) at even inputs and \(T(n)=(3n+1)/2\) at odd inputs. Let \(P_j(n)\) count odd departures before clock \(j\). Write \(\lambda=\log_2 3\), \(\alpha=1/\lambda\), and \(\theta=H_2(\alpha)=0.94995\ldots\), where \(H_2\) is binary entropy.

For each \(\varepsilon>0\) there are constants \(C,L\) with this property. Take any interval \(I\) of \(N\ge2\) consecutive positive integers and any subset \(S\) of its \(17\bmod48\) integers. Except for at most \(CN^{\theta+\varepsilon}\) members \(z\) of \(S\), there is an actual \(y\in S,\ y<z\), with
\[
 T^H z=T^H y,\quad P_H(z)=P_H(y),\qquad
 T^H(3z)=T^H(3y),\quad P_H(3z)=P_H(3y)
\]
at the **same prescribed shortcut clock** \(H=\lceil L\log_2(2N)\rceil\). The two coordinates may first merge at different times. A hit at one on the supplied upper arm transfers to the triple of this smaller canonical parent at any upper rank. Sort the four-integer signatures at \(H\) and choose an earlier member of the same fiber to implement the selection. More generally at most \(dCN^{\theta+\varepsilon}\) sources have fewer than \(d\) earlier partners. The exception is an absolute count on \(I\), including on a preselected rare \(S\).

## A native-clock bound with nearby partners

Put \(a_j=3^{P_j(n)}/2^j\). Substitution of the shortcut updates gives
\[
       T^h(n)=a_h n+\frac12\sum_{i<h,\ T^i(n)\ {\rm odd}}a_h/a_{i+1}.
\]
At a record \(a_h\le a_i\) for every \(i\le h\), the affine remainder lies in \([0,h/2]\). The first coefficient at most \(b<1\) lies in \((b/2,b]\), because its predecessor exceeds \(b\) and every factor is at least \(1/2\). The kernel checks the physical coefficient, record remainder, partner separation, and a two-coordinate strip inequality. [FirstPassage.lean](FirstPassage.lean)

Stop \(z\) and \(3z\) independently at their first coefficients at most \(N^{-\delta}\). At fixed clocks and grades write their coefficients \(l,m\) and endpoints \(u,v\). Then \(u=lz+e,\ v=3mz+f\), with \(e,f\in[0,H/2]\) through a deadline \(H\). Thus \(u\) ranges over an interval of length at most \(N^{1-\delta}+H/2\). Since \(m/l<2\), \(v-(3m/l)u\) ranges over an interval of length at most \(7H/2\). These lengths hold uniformly in the position of \(I\). Two sources with the same stopped lower endpoint, clock and grade have distance at most \(H/(2l)<H N^\delta\).

Take \(H=\lfloor\log_2 N\rfloor\). Missing a cut entails at least \((1-\delta)H/\lambda-O(1)\) odd steps on that arm. The parity-word bijection, Stirling's bound and a geometric tail give \(O_\delta(N^{H_2((1-\delta)/\lambda)})\) exceptions on each arm, when \(0<\delta<1-\lambda/2\). The triples are an odd-stride progression over all original sources, before selecting \(S\). There are \(O((1+H)^4)\) possible pairs of clocks and grades. Hence all but
\[
       O_\delta\!\left(N^{H_2((1-\delta)/\lambda)}
           +N^{1-\delta}(1+\log N)^5\right)
\]
sources in \(S\) have a smaller partner in \(S\) at distance \(<H N^\delta\), already by the native deadline. Equal stopped endpoints and grades can be padded on each coordinate to the prescribed \(H\). The balanced exponent is below \(0.966\). Multiplying the signature term by \(d\) gives at least \(d\) earlier partners outside the enlarged exception.

## A class of pairs that survives recursion

Use pairs \((x,y)\) of positive integers with \(x\) in any interval of \(N\) consecutive integers and \(|y-ax-b|\le1,\ 1/2\le a\le3\). The real intercept \(b\) is unrestricted. Each \(x\) is paired with at most three integers \(y\). Each \(y\) is paired with at most five \(x\)'s since the admissible real interval has length at most four. The range of \(y\) fits in at most \(3N+4\) consecutive integers. The initial canonical pairs \((z,3z)\) meet these conditions. Arbitrary subsets are allowed throughout.

It suffices to take \(\eta=\theta+\varepsilon<1\). Choose a sufficiently small fixed \(\delta>0\) and an \(\eta'\) with \(H_2((1-\delta)/\lambda)<\eta'<\eta\). At \(h=\lfloor\log_2 N\rfloor\) the parity words are in bijection with residues modulo \(2^h\): lifting an \(i\)-bit source by \(2^i\) changes its physical endpoint by \(3^{P_i}\), so the two next parities differ. Each coordinate lies in a bounded number of periods. Using the coordinate multiplicities, all but \(O(N^{\eta'})\) input pairs have made **both** coefficient passages
\[
        l\le N^{-\delta},\qquad m\le N^{-\delta}/a
\]
by their respective clocks at most \(h\). Failing an entire passage entails failing its final-clock test, and \(a\) and rounding alter the binomial threshold by only an absolute constant. For large \(N\) both cuts are below one.

Partition hits by their two first clocks and two grades. For one group write \(u=lx+e,\ v=my+f\), with \(e,f\in[0,h/2]\). Its image satisfies
\[
 \operatorname{diam}\{u\}\le N^{1-\delta}+h/2,\qquad
 v-(am/l)u-mb=m(y-ax-b)+f-(am/l)e .
\]
Both \(l\) and \(am\) belong to \((N^{-\delta}/2,N^{-\delta}]\). The new slope is therefore in \((1/2,2)\). The intercept error has magnitude at most \(2+3h/2\). Partitioning by the floor of that error gives \(O(1+h)\) pieces of thickness at most one with unrestricted real intercepts. The first coordinate fits in at most \(M=\lceil N^{1-\delta}+h+2\rceil\) consecutive positive integers. All stopped pairs are therefore covered by \(O((1+h)^5)\) translated strips of the **same type** at smaller size. This step uses no distribution hypothesis inside a stopped image.

Test both ordered coordinates and their odd counts at a common horizon. Padding equal signatures preserves equality. Within each original clock-and-grade group, equality at horizon \(H(M)\) in a smaller strip gives equality in *both original coordinates* by \(h+H(M)\). Each coordinate's prefix clock and grade agree between the compared sources. Pad each coordinate separately to the new common horizon.

For large \(N\), \(M\le N^{1-\delta/2}\). Take \(L\) large enough that \(h+H(M)\le H(N)=\lceil L\log_2(2N)\rceil\) over this range. If the smaller strips give at most \(CM^\eta\) signatures apiece, the preceding partition bounds the width-\(N\) count by
\[
       C_0 N^{\eta'}+C C_1(1+h)^5 M^\eta.
\]
The terms are respectively \(o(N^\eta)\) and \(o(CN^\eta)\). Enlarge \(C\) over the finite initial range to close strong induction uniformly in the strip location and in the subset. Only the first \(d\) members of a signature fiber can have fewer than \(d\) earlier representatives, proving the result.

## Provenance and the pointwise boundary

García and Tal proved zero upper Banach density for representatives of the one-coordinate synchronous equivalence relation. Leen and the scalar interval-compression work obtained entropy exponents and bounded clocks retaining the odd count; Weaver's stronger power result concerns scalar labelled images. Multiplication of the two scalar image bounds does not give the present pair bound. Our recursive input is a joint thin strip of actual pairs, with its slope normalized after every pair of independently chosen first passages. The proof above is elementary. [García–Tal, Lemma 3 and Theorem 1](https://matwbn.icm.edu.pl/ksiazki/aa/aa90/aa9033.pdf) · [Weaver, Paper 28/v3, §1 and §8](https://rstation.ai/problems/collatz/papers/28/v3)

The affine sum and small remainders at multiplier records appear in Weaver's translated first-passage proof. PR197's post-descent argument controlled affine profiles and source multiplicity on a prescribed absolute-size octave. Its directed-return theorem transports Boolean labels to a smaller witness that need not meet the original lower orbit. Here the smaller parent shares actual counted mergers with both original arms. [Weaver, Paper 191/v1, equations (3)–(4)](https://rstation.ai/problems/collatz/papers/191/v1) · [PR197, post-descent transfer](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/literature-step/POST_DESCENT_TRANSFER.md) · [PR197, directed return](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/directed-return/STRICT_RETURN_REFINEMENT.md)

A hypothetical least canonical \(z\) with its lower outside the basin and its triple inside must be exceptional in every interval containing it. Many larger sources may occupy its same pair of components and have smaller representatives there. The missing implication is that the *original* least defect has an earlier physical representative, or independently belongs to the basin of one.
