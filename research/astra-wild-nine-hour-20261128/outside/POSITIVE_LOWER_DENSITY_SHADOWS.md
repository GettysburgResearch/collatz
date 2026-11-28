# One wrong script with exponential integer accuracy at positive lower density

**Proposed written construction.** Given any positive ordinary \(x\) and any \(N\ge0\), there is a single prescribed infinite script at real start \(r_0=x\) satisfying all of the following:

* The first \(N\) shortcut choices are true and the next is wrong. Every subsequent real state is nonintegral. The associated binary initial coordinate executes the script physically, and every odd-prime coordinate always equals the image of the very same dyadic real state.
* \(\liminf_t(\log r_t)/t>0\). At a set of dates of **positive lower natural density**, the nearest integer \(z_t>0\) satisfies \(|r_t-z_t|\le2^{-t/25}\). These dates belong to genuine ordinary all-odd segments of lengths tending to infinity. On a subset still of positive lower density, \(z_t\) and the simulated profinite state both approach \(-1\) in \(\widehat{\mathbb Z}\). Thus for each fixed modulus their residues eventually agree there.
* By the [integer recovery theorem](EXPONENTIAL_INTEGER_SHADOWS.md), the set of *all* dates of this exponential accuracy has no subset of positive natural density. The construction does not give a limiting overall parity law or real speed.

The construction uses the overlapping real intervals of two explicit affine words. Their common slope also allows simultaneous finite-prime congruences without materially reducing the real precision.

## A real interval and congruences from the same choices

Use \(t\) pairs, each either the chronological word \(10\) or \(01\). Their maps are respectively
\[
                 y\mapsto Ay+1/4,\qquad y\mapsto Ay+1/2,\qquad A=3/4 .
\]
From a prescribed \(y\) the final value ranges over
\[
       A^t y+1-A^t+\sum_{j=0}^{t-1}\frac{d_j}4 A^j,\qquad d_j\in\{0,1\},       \tag{1}
\]
where the chronological last pair carries digit \(d_0\). For any \(v\in[0,1]\), choose \(d_0,\ldots,d_{t-k-1}\) so the sum, after *any* choices of the remaining \(k\) digits, differs from \(v\) by at most \(A^{t-k}\). Indeed \([0,A]\cup[1/4,1]=[0,1]\). At each step select a digit taking the residual target to \([0,1]\) after rescaling by \(A^{-1}\). The remaining target and every possible remaining digit sum then lie in \([0,A^{t-k}]\).

Let \(M\) be coprime to six. With \(k=M-1\le t\), the remaining digits can prescribe the output residue of (1) modulo \(M\), if \(y\) has odd-place residues (as a dyadic rational does). Each of the \(k\) remaining coefficients \(A^j/4\) is an additive generator in \(\mathbb Z/M\mathbb Z\). The subset sums start from \(\{0\}\); adjoining a generator \(c\) replaces the current set \(S\) by \(S\cup(S+c)\), strictly enlarging it unless it is already the entire group. Thus all residues occur after \(M-1\) digits, independently of all fixed digits and of the starting residue. For \(M=1\) there is no restriction.

## Geometric stages and genuine rounded segments

Take the requested true prefix and wrong letter, then enough odd letters to reach a large stage-start time \(t\). Initial finite choices affect no density. Write \(J=\lfloor t/10\rfloor\). The letters in a stage are
\[
                   1^t,\quad t\text{ pairs as above},\quad 1^{2J},\quad 1^J .
\]
The end time is \(t'=4t+3J\). Choose \(m\to\infty\) so slowly that
\[
     U=3^m M\le\sqrt t,\qquad M=\prod_{5\le p\le m,\ p\;\mathrm{prime}}p^m .
\]
For example take the largest such \(m\), once \(t\) is large. Put \(k=M-1\).

Let \(y\) be the state after the first \(t\) reserve letters. On applying the \(2J\) following odd letters, a pair-block endpoint \(q\) goes to \(B(q+1)-1\), \(B=(3/2)^{2J}\). Varying the target digit parameter \(v\in[0,1]\) in (1) therefore gives a *target interval* of length \(B\) for the next state. For large \(t\), \(B/2^J=(9/8)^J\ge U\), so the closed interval contains an integer \(z\equiv-1\pmod{2^J U}\). It is positive because its lower end grows. Choose the late pair digits for this real target parameter \(v\), then choose the reserved early pair digits so \(q\equiv-1\pmod M\). The resulting real state differs from \(z\) by at most \(BA^{t-k}\). Its odd coordinates agree with \(z\bmod U\): the residue \(-1\) persists modulo \(M\) under odd steps and the \(2J\) odd steps force it modulo \(3^m\).

The final \(J\) odd letters are *genuine* for \(z\), since \(2^J\mid z+1\). After \(0\le j\le J\) of them the integer is
\[
              z_j=(3/2)^j(z+1)-1 ,
\]
and the difference of real states is at most \((3/2)^{3J}A^{t-k}\). As \(k\le\sqrt t\), for every sufficiently large stage this is \(<2^{-t'/25}\). The strict asymptotic margin is equivalent to \(3^{325}<2^{532}\) on replacing \(J/t\) by \(1/10\). These are therefore the unique nearest integers. Each pair of odd-place residues remains congruent modulo \(U\), with \(z_j\equiv-1\pmod U\). At the binary place each of the first \(J-j\) future letters is one. The binary state and \(z_j\) consequently agree with \(-1\) modulo \(2^{J-j}\). Keeping just \(0\le j\le J/2\) makes all these profinite precisions tend to infinity.

Every stage contributes at least \(t/22\) selected half-window dates for sufficiently large \(t\). For a time in the following stage, the preceding completed window therefore has size at least a fixed positive fraction of that time, since consecutive stage starts differ by a factor at most \(4.3\). This proves positive lower density on the full clock.

## Real escape with the prescribed fixed source

During the first \(t\) letters the real state grows by at least \((3/2)^t\). Every complete pair retains at least \(A\) times its input, and its intermediate state is at least half its input. Thus throughout the pair section the state is at least \((9/8)^t r_t/2\), and the stage's final state is at least \((9/8)^t r_t\). The odd suffixes only increase positive states. At every stage the minimum is eventually at least its entry height. Since \(t'\le4.3t\), one preceding completed stage already gives a positive uniform lower bound on \(\log r_s/s\) for all sufficiently large \(s\). The first wrong choice at \(N\) created the irreducible denominator two; that denominator doubles at every following tick. No genuine positive ordinary orbit follows the constructed infinite script from the specified start.

The binary source is the unique \(2\)-adic input for the constructed parity word, by the usual shortcut parity-cylinder bijection. Its difference from the named ordinary source is essential. Each nearest integer agrees with that binary coordinate for the *remaining length* of its genuine window, while its real difference after the original wrong tick never vanishes. The construction does not use asymptotic digit distribution for powers of \(3/2\), and does not identify the nearest integer from one stage with a predecessor of the next one. A limit-law theorem for all stages, such as the [unmarked forward-law classification](ALL_PROFINITE_FORWARD_LAWS.md), concerns a different observable and does not fill these breaks.
