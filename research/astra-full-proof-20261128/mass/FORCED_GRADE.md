# A conserved grade in affine comparisons of a high coupled pair

An actual pair with an odd-count gap \(k\ge0\) has the form \(v,3^k v+c\) on a fixed positive residue cylinder. Let \(f\) be any shortcut-invariant component label. Peeling ternary digits of \(Z=3^kv+c\) gives a direct finite comparison. Indeed
\[
 f(3n+r)\quad\longrightarrow\quad f(3n+2)=f(2n+1)
       \quad\longrightarrow\quad f(2n)=f(n),\qquad r=0,1,2,
\]
uses at most three numerical adjacency edges at each digit. After \(k\) digits the lower integer is \(v+\lfloor c/3^k\rfloor\). Thus a disagreement implies at least one of these genuine adjacent disagreements or one of the remaining \(|\lfloor c/3^k\rfloor|\) adjacent disagreements at the lower end. Positivity is required at each displayed node; for fixed \(k,c\) this holds for all sufficiently large \(v\).

The following written obstruction explains why merely shortening a finite comparison path does not remove its total forced odd-count level. Freeze an arbitrary finite partition by binary residue classes of \(v\), and refine it to a common precision \(S\). On \(v=2^S u+r\), write a nonconstant comparison node as
\[
 A(u)=a u+b,\qquad a=2^s a_o>0,\quad a_o\ \text{odd}.
\]
Signed integer intercepts can also be used when the physical values are positive for sufficiently large \(u\). The first \(s\) shortcut parities of this affine row are fixed by \(b\bmod2^s\). Write \(Q_s(b)\) for their number of odd departures and put
\[
             \Phi(A)=v_3(a)+Q_s(b).
\]
It is the ternary valuation of the slope remaining after the entire forced binary prefix.

A physical shortcut step affine on this entire row preserves \(\Phi\). If the intercept is even, its slope becomes \(a/2\); if the intercept is odd, its slope becomes \(3a/2\). Exactly the corresponding zero or one odd departure is removed from the pending \(s\) steps. A nonconstant row with \(s=0\) cannot take a single affine shortcut step without further partition. Inverse edges and paths of fixed physical steps preserve the same grade on any precision that makes those steps affine. For a unit adjacency edge \(A(u)\leftrightarrow A(u)+1\), the absolute change in grade is
\[
                   |Q_s(b+1)-Q_s(b)|.
\]
This is literally the odd-count gap of the two forced prefixes. It can be large on a row with a large dyadic slope.

Consider any finite scheme that connects \(v\) to \(3^k v+c\) on each cell by physical edges (in either direction) and unit adjacencies of nonconstant integer-affine rows. The scheme may choose its path from the residue \(r\), with a common finite refinement for all choices. Then
\[
  2^{-S}\sum_{r\bmod 2^S}
     \sum_{\text{adjacency on the path for }r}
          |Q_s(b+1)-Q_s(b)|\ \ge\ k .
\]
On each cell, telescope \(\Phi\) along the path and use the triangle inequality. The signed net change at the two given endpoints is
\(k+Q_S(3^k r+c)-Q_S(r)\). Since \(3^k\) permutes the residues modulo \(2^S\), the two latter terms cancel in the average. The statement makes no independence assumption about the selected path.

For example \(f(3^k v-1)=f(2^k v-1)\), since \(T^k(2^k v-1)=3^k v-1\). Thus \(f(v)\) and \(f(3^k v)\) can be compared by only two adjacency tests if only the number of tests is counted. The test at \(2^k v-1,2^k v\) already exposes \(k\) forced odds versus \(k\) forced evens. The conservation law includes exactly this cost. It applies to comparisons carried by nonconstant arithmetic rows. It does not bound cancellation between multiple correlated tests or the exceptional event that an individual positive source is exactly the terminal integer 1.

The canonical high-pair coordinates and the role of forced parities are recorded in [Weaver 13, the pair-chain section](https://rstation.ai/problems/collatz/papers/13/v1), following Duran. The grade conservation argument above is elementary and does not invoke a stochastic coalescence estimate.

[The bounded checker](check_forced_grade.py) tests 4,514 affine shortcut edges, including negative intercepts, 1,080 exact averaged rows, and the terminal-phase transport on actual convergent trajectories. Both this statement and the terminal-phase divergence theorem are written results.
