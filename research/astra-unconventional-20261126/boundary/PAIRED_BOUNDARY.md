# Ordinary exclusion of periodic boundary words

Let \(T(n)=n/2\) at even \(n\) and \(T(n)=(3n+1)/2\) at odd \(n\). Fix a Boolean color \(f\) on positive integers with \(f(Tn)=f(n)\). A nonconstant color has an adjacent opposite-colored pair. Since \(f(2n)=f(n)\), exactly one of the two dyadic children of an opposite-colored interval has opposite endpoint colors. Following these unique children gives a nested sequence of unit-mesh cells after dyadic rescaling, with a common limiting real position \(t>0\). At every level of this path the left labels are one fixed color and the right labels are the other fixed color. We call this a persistent boundary. For nondyadic \(t\) the integer endpoints at dyadic level \(k\) are \(\lfloor2^kt\rfloor,\lfloor2^kt\rfloor+1\). One-sided dyadic endpoints use their actual nested cells. The original construction is in [the global branch](../global/DYADIC_BOUNDARY.md).

## Zero positions have one parity

Suppose the smaller integer \(n\) in an adjacent pair is even. Set \(h=v_2(n+2)\ge1\), \(z=(n+2)/2^h\), and \(w=3^{h-1}z\). At physical clock \(h\), the trajectories from \(n,n+1\) have respective values
\[
                          w-1,\qquad 3w-1
\]
and respective odd departure counts \(h-1,h\). The first path makes one halving before its \(h-1\) odd steps, and the second makes \(h\) odd steps. If \(w\equiv3\bmod4\), exactly two further steps take both to \((3w-1)/4\), with equal total odd counts. This holds for all positive integers in the specified class. The arbitrary-exponent endpoint-label identities are compiler-checked in [PairedBoundary.lean](PairedBoundary.lean).

Consequently no mismatched edge may end in a binary suffix \(10\,1^{2j}0\) for \(j\ge0\). Indeed \(h=2j+1\) and \(z\equiv3\bmod4\) on that suffix. The companion exclusion for even \(h\) is \(00\,1^{2j+1}0\). These are finite low-bit comparisons. Along an infinite persistent path a forbidden suffix at any later level would contradict the opposite endpoint colors at that very level. In particular \(100\) is forbidden. Once a 1 has appeared, consecutive zeros thereafter have an odd number of intervening ones, since the earlier zero has a preceding 1. Thus every later zero occurs at positions of one parity. An alignment with a forced 1 in each odd place gives a fractional tail
\[
                 u=\frac23+\sum_{i\ge1} b_i4^{-i},\qquad b_i\in\{0,1\}.
\]
One may discard a finite starting prefix. A path ending in a constant digit string is treated separately.

The free digits do not satisfy a second parity restriction visible to all counted local comparisons. For the binary necklace \(01010111\) the gaps between zero positions are \(2,2,4\) cyclically. At each rotation \(V\) let \(z=-\operatorname{int}_2(V)/255\) in the 2-adic integers, and run the signed rational trajectories of \(z,z+1\). Their pairs enter joint periods 100 after \(21,22,23,24,25,26,27,20\) physical steps respectively, in left-rotation order starting with the displayed word. In each joint period the difference of odd counts has increment zero. At no common clock before or in that period do the values and odd counts both agree. This is checked, with the positivity test below, in [the exact replay](check_paired_boundary.py). Any universally counted-fusing finite low-bit word inside the repeated necklace would also fuse these rational reference values with equal count. The enumeration therefore rules out that local inference. The next argument excludes the very same necklace from ordinary invariant colors.

## Two different binary levels can be compared

**Theorem.** Let a nondyadic rational \(t=A/q>0\) be in lowest terms, with \(q\) odd. A finite dyadic shift of the starting clock is allowed. Choose two recurring residue phases \(r_-=2^{k_-^0}A\bmod q\) and \(r_+=2^{k_+^0}A\bmod q\), allowing equality, and consider the signed rational shortcut trajectories from
\[
                           -r_-/q,\qquad 1-r_+/q .
\]
If both are eventually periodic and each eventual cycle has an odd departure, \(t\) cannot be a persistent boundary of an ordinary invariant color. The cycles and their odd frequencies may differ.

To prove the assertion, use \(h\) with \(2^h\equiv1\bmod q\). On the left admissible levels \(k\equiv k_-^0\bmod h\) the actual lower endpoint is \((2^kA-r_-)/q\). On the right admissible levels \(k\equiv k_+^0\bmod h\) the upper endpoint is \((2^kA+q-r_+)/q\). For each arm \(\sigma\in\{-,+\}\) and a large integer \(Q\), let \(i_\sigma(Q)\) be the clock immediately after its \(Q\)-th odd departure on the signed rational trajectory. Let \(k_\sigma(Q)\) be the least admissible dyadic level at least \(i_\sigma(Q)\). Put \(c_\sigma=k_\sigma-i_\sigma\). Thus \(0\le c_\sigma<h\). We compare the left endpoint at level \(k_-(Q)\) with the right endpoint at level \(k_+(Q)\). Their colors are opposite even when these levels differ.

There is an arithmetic progression \(Q=Q_0+m\Delta\), \(m\ge0\), on which both paddings \(c_\sigma\) and the two rational states \(u_\sigma/q\) reached at clocks \(i_\sigma(Q)\) are constant. Indeed, if a signed cycle has length \(d\) and \(b>0\) odd departures, increasing \(Q\) by \(hb\) advances its physical clock by \(hd\), preserving its state and its clock modulo \(h\). Use a common multiple of the two increments once both cycles have started.

Lifting a signed reference by \(2^k A/q\) preserves its first \(i\le k\) parity bits. The real signed difference at clock \(i\) is exactly \(2^{k-i}3^Q A/q\). Thus our two actual positive integers at the chosen clocks are
\[
                         (2^{c_\sigma}3^{Q}A+u_\sigma)/q.
\]
Multiply each by \(2^{C-c_\sigma}\), \(C=\max(c_-,c_+)\). This leaves its color unchanged. We have produced an opposite-colored positive pair \(X_m,X_m+D\) for every \(m\ge0\), where
\[
 X_m=B+E(3^\Delta)^m,\qquad
 B=2^{C-c_-}u_-/q,\qquad E=2^C3^{Q_0}A/q\ne0 .
\]
The separation \(D=(2^{C-c_+}u_+-2^{C-c_-}u_-)/q\) is an ordinary integer since both original terms are. If \(D=0\) we already have a contradiction.

For \(D\ne0\) let \(\mathcal U_D\) be the set of dyadic starts whose two arms at signed offset \(D\) counted-fuse at a finite common shortcut clock. Each finite-clock event is clopen, by the equal-count affine lifting identity. Their union is open and has additive Haar measure one. For precision, Paper 124's equation (18) at fixed block width \(|D|+1\) gives failure probability \(O_D((1+s)^{-1/2})+2^s/X\) on intervals of length \(X\) at clock \(s\). Let \(X\to\infty\) at each fixed \(s\); finite clock success or failure depends on the source residue mod \(2^s\). Then let \(s\to\infty\). A negative \(D\) follows by translation. [Weaver, Paper 124/v1, equation (18)](https://rstation.ai/problems/collatz/papers/124/v1)

The set of even-indexed \(X_m\)'s is dense in a nonempty dyadic ball. More explicitly \(g=3^{2\Delta}=1+2^b v\), with \(b\ge3\) and \(v\) odd. Successive squaring gives \(v_2(g^{2^j}-1)=b+j\), so powers of \(g\) cover \(1+2^b\mathbb Z_2\) at every finite precision. The ball \(B+E+2^{b+v_2(E)}\mathbb Z_2\) meets the open full-measure \(\mathcal U_D\). Some actual \(X_m\) belongs to a finite fusion cylinder in the intersection. This contradicts its opposite ordinary colors. The contradiction uses an ordinary source, the preservation of colors between distinct dyadic levels, and the two otherwise independent clocks.

## Uniform exclusion of long repetitions

Fix a nonconstant binary periodic word \(w\) of length \(h\), with purely periodic fraction \(r/q=0.\overline{w}\) in lowest terms. Assume the two signed references in some phase of this rational tail have the nonzero eventual-cycle property in the theorem. There is a finite bound depending on \(w\) on the length of a repetition of \(w\) **immediately after a bit breaking its left periodic continuation** on any persistent path. Consequently \(0.\overline{w}\) is absent from the shift omega-limit of every such path. This includes \(01010111\).

In fact a prefix integer \(N\) immediately followed by repetitions \(w\) agrees, for as many binary levels as those repetitions last, with the path having hypothetical real starting value \(N+r/q=A/q\). Here \(A=qN+r\). The last bit of \(w\) has the parity of \(r\), since the reduction of \(\operatorname{int}_2(w)/(2^h-1)\) divides by an odd integer. A preceding bit different from that last bit makes \(A\) odd. The exact signed references, the progression of \(Q\)'s, the paddings and thus \(B,D,C,Q_0,\Delta\) in the proof above are independent of \(N\).

In the displayed dyadic balls the valuation of \(E\) is now the fixed value \(C\). Thus only finitely many possible balls occur as the odd \(A\) varies. In each choose one finite fusion cylinder, at a common upper precision \(H\). For every corresponding \(A\), powers of \(3^{2\Delta}\) attain that cylinder with an exponent index \(m\le 2^{H+1}\), by their period in the finite dyadic unit group. Both required dyadic levels are therefore bounded in terms of \(w\) alone. A sufficiently long finite repetition supplies exactly the same ordinary endpoints and gives the same contradiction. For a different starting phase rotate \(w\); if one phase has the required references it remains accessible within \(h\) further bits. For arbitrarily long repeated segments on a single path, extend backwards until the first disagreeing bit (rotating when necessary). The alternative is an arbitrarily long matching initial prefix, which forces a periodic tail already excluded by the theorem. This proves the omega-limit assertion without asserting a uniform bound on a possibly long initial, unanchored prefix across all colors.

For the necklace \(w=01010111\) there is a small finite certificate for an explicit bound, independent of Paper 124. Use the unreduced \(q=255\), \(A=255N+87\) with \(A\) odd following the breaking bit, and \(Q=57+112m\). At the left phase \(k\equiv7\bmod8\), the signed reference is at numerator \(1527\) after \(100+200m\) steps with padding three. At the right phase \(k\equiv5\bmod8\), the corresponding numerator is \(159\) after \(101+200m\) steps with padding zero. These progression statements follow by replaying one period with the exact counts. Multiplying the right endpoint by eight gives the opposite-colored neighbors
\[
               Y_m=\frac{8\cdot3^{57+112m}A+1272}{255},\qquad Y_m+1 .
\]
Here \(v_2(3^{112}-1)=6\), so \(0\le m<2^{15}\) covers all residues of \(Y_m\) modulo \(2^{24}\) with its specified low nine bits. As \(A\) varies through its odd values the possible low-nine-bit classes are the 32 multiples of 16 modulo 512. The [exact verifier](check_paired_boundary.py) finds a finite counted-fusing cylinder of depth at most 24 in every one, by testing ordinary representative neighbors and retaining both their physical clock and odd counts. Therefore \(103+200(2^{15}-1)=6{,}553{,}503\) source bits suffice. An actual path cannot have \(819{,}188\) copies of this displayed phase immediately after a breaking bit. No optimization of this explicit bound is assumed. In contrast, the comparison restricted to each individual edge at a common clock survives every finite local word of the periodic necklace.

## Ternary multiplication and the remaining cases

The free-digit representation gives \(3u\bmod1=\sum 3b_i4^{-i}\) except for the identified circle endpoint. Its binary digits are pairs \(b_i b_i\). The exact scalar lift \(H(a)=(3a+2^{v_2(a)})/2\) preserves color. At an aligned source zero preceded by at least three ones the lower source endpoint \(n\) is \(14\bmod16\), hence \(2\bmod4\). Apply color invariance separately to \(n\) and \(n+1\): their respective image labels are those at \(j=3n/2+1\) and \(j+1\). The source fractional tail begins in 1 and has no consecutive zeros, so it is at least \(2/3\) and \(j\) is the lower cell endpoint at the real point \(3t/2\) on this mesh. Here \(j\equiv2\bmod4\); the repeated-digit formula puts \(3t/2\) in the left child at the next binary level. That child has lower edge \(2j\equiv4\bmod8\), a fused pair. The new opposite-colored target edge therefore has its persistent continuation in the right child. Infinitely many such source digits give distinct persistent boundary points approaching \(3t/2\) from the right, with identical orientation. They occur on every tail having infinitely many zeros which is not eventually alternating and not a dyadic endpoint. The persistent edges intermittently next to \(3t/2\) do not supply a persistent path through \(3t/2\).

A signed reference hitting zero forces \(q\mid3^b\) for some \(b\): multiply its positive affine numerator formula at the zero hit by \(q\), obtaining \(q\mid3^b r\), and use \((r,q)=1\). For \(q=3^d\) the powers of 2 generate all units modulo \(3^d\), by the elementary order formula for \(2\bmod3^d\). If \(d\ge2\), some shifted fractional tail of \(A/q\) equals \(1/q<1/3\), incompatible with an eventual binary tail avoiding \(00\) (whose minimum is \(0.\overline{01}=1/3\)). Such phases recur indefinitely. Thus a rational persistent point with a zero reference has, after a dyadic shift, denominator \(3\) or is dyadic. For every other rational persistent point, at least one entire sign side of its recurring reference phases must have unbounded trajectories. Indeed a bounded trajectory with a fixed odd denominator is eventually periodic, and the two phases may be chosen independently. Rational 2-adic periodicity is an independent open issue in the classical conjugacy literature. [Bernstein and Lagarias, *The \(3x+1\) conjugacy map* (1996)](https://websites.umich.edu/~lagarias/doc/bernstein.pdf) The results above do not imply that an aperiodic persistent boundary has a periodic word in its shift omega-limit.


## A zero reference forces reversal on a geometric sequence

For fixed positive \(D\) and fixed shift \(c\in\mathbb Z\) we have
\[
     \lim_{J\to\infty}\frac1J\#\{1\le j\le J:f(3^jD+c)\ne f(3^jD)\}=0 ,
\]
omitting finitely many nonpositive arguments. On each parity of \(j\), the sequence \(3^jD\) is Haar-equidistributed on a dyadic ball: the finite-level order calculation above applies with \(\Delta=1\). The complement of \(\mathcal U_c\) is null there. Given any \(\varepsilon>0\), a finite union of successful cylinders covers relative mass at least \(1-\varepsilon\) there; the geometric progression visits these with their exact limiting frequencies. This holds for every invariant Boolean color without assuming a rational boundary.

If \(t=A/3\), take the phase \(2^kA\equiv1\bmod3\). For large \(k\) the left endpoint \((2^kA-1)/3\) has color \(f(A)\). The right endpoint \((2^kA+2)/3\) has color \(f(2^{k-2}A+1)\) by two shortcut steps. Write \(k-2=2j+s\) with \(s\in\{0,1\}\) fixed on the phase, and \(D=2^s A\). The identity \(f(4x+1)=f(3x+1)\) gives \(f(4^jD+1)=f(3^jD+1)\) by successive substitutions in \(4^jD\). All sufficiently late right labels are opposite \(f(A)\). The geometric lemma at shift \(+1\) and \(f(3^jD)=f(3^jA)\) give
\[
        \lim_{J\to\infty}J^{-1}\#\{1\le j\le J:f(3^jA)\ne f(A)\}=1.             \tag{1}
\]
When \(D\) is odd, \(f(3^jD+1)=f(3^{j-1}D)\) for \(j\ge1\), so the reversal is eventual. For an eventual dyadic upper endpoint of numerator \(A\), the opposite labels are those of \(2^kA-1\) and \(2^kA\); a length-\(k\) odd rise gives \(f(2^kA-1)=f(3^kA-1)\). For a lower endpoint use \(f(4^j A+1)=f(3^j A+1)\) and \(f(4^jA)=f(A)\). The geometric lemma yields (1) also for both dyadic orientations. Density here is in the ordinary exponent \(j\) for a single specified \(A\).

The calculation also gives the exact rule on the free digits of an arbitrary path. At aligned level \(n\) put \(p=n+1\), with \(f(p-1)=L\) and \(f(p)=R\ne L\). The mandatory next 1 forces \(f(2n+1)=f(3p-1)=L\). At the next level, the chosen pair is determined by the color of \(4n+3\), which equals \(f(9p-1)\) after two odd shortcuts. If the free bit equals 1, the new right endpoint is \(4p\) and \(f(9p-1)=L\). If it is 0, the new right endpoint is \(4p-1\) and \(f(9p-1)=R\). During a maximal run of \(\ell\) free ones terminated by a free zero this gives \(f(3^j p-1)=L\) for \(0\le j\le2\ell+1\) and \(f(3^{2\ell+2}p-1)=R\). Indeed the intermediate coefficients are \(4^d p\), and \(f(3^a4^d p-1)=f(3^{a+2d}p-1)\) for \(a\ge0\) by the \(2d\)-step rise.

Equation (1) cannot be reversed by ordinary equidistribution of \(3^j A\) in its dyadic balls. This gives exact probabilities for fixed finite-clopen tests, while membership in the component of a fixed positive anchor is an infinite-time event. The lower bound for the ordinary natural density of that component gives no lower bound for its frequency on the geometric sequence.
