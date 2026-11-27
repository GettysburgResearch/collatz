# Squareclasses of adjacent products on unrestricted ordinary trajectories

**PROPOSED.** In a primitive positive integer cycle with \(P\) odd states, a single squareclass of adjacent products occurs at most \(2(2+2\sqrt P)\) times. The class may be chosen after seeing the cycle. An affine squareclass space of dimension \(r\) occurs on at most \(2^{r+1}(2+2\sqrt P)\) edges. These bounds allow arbitrary valuations, maximum height and unmarked edges. The complete product list has affine squareclass rank at least \(\log_2 P-O(\log\log(P+2))\). There are corresponding bounds on every injective prefix from one fixed positive source.

The [finite rank certificate](RANK_CERTIFICATE.md) gives rank at least 32 on every nontrivial positive integer cycle, with published computational inputs. It yields 3,321 in the earlier prescribed narrow physical band. A high-rank cycle or escaping source remains possible.

Use actual odd Syracuse edges \(2^a y=3x+1\), \(a=v_2(3x+1)\). One edge takes \(a\) steps of the shortcut map. A bracket denotes a positive rational modulo squares. The affine rank of a nonempty set of classes is the dimension of the span of their differences in this \(\mathbb F_2\)-space. Arbitrary unrelated square multipliers disappear in this quotient. The earlier [multiplicative-rank theorem](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-deep-closure-20261124/arithmetic/README.md) bounds a group before taking this quotient. Its Pell discriminant is our starting point.

## 1. A sharp height gap

Put \(D(x)=\operatorname{sf}((3x)(3x+1))\), the positive squarefree kernel. Consecutive positive integers are coprime and cannot both be squares, so \(D>1\). Then \(X=6x+1\) and \(V=2\sqrt{3x(3x+1)/D}\) are positive integers with \(X^2-DV^2=1\). An odd source has \(X\equiv7\bmod12\).

For distinct positive odd \(x<x'\) with \(D(x)=D(x')=D\),
\[
 \frac{x'}x>\max\{\rho,4D\},\qquad \rho=(2+\sqrt3)^4=97+56\sqrt3>128.       \tag{1}
\]

First consider the two solutions directly. Put \(t=X+V\sqrt D,\ t'=X'+V'\sqrt D\) and \(q=t'/t>1\). Then \(q=U+W\sqrt D\), with \(U=XX'-DVV'\), \(W=XV'-X'V\) integers and \(U=(q+q^{-1})/2>1\). Four divides \(DVV'\). Three also divides it because its square \((X^2-1)(X'^2-1)\) is divisible by nine. Hence \(U\equiv1\bmod12\) and \(q\ge13+\sqrt{168}\). Moreover
\[
 \frac{x'}x=\frac{X'-1}{X-1}
   =q\left(\frac{1-(qt)^{-1}}{1-t^{-1}}\right)^2>q.                        \tag{2}
\]

For the sharper (1), take the least unit \(\eta=u+v\sqrt D>1\) in the integer-coordinate norm-one group. It exists because \(t\) is one such unit and its positive integer trace coordinate increases with the real unit. Every positive real unit greater than one is a positive integral power of \(\eta\). Dividing by a suitable power leaves an integer-coordinate norm-one unit in \([1,\eta)\). Such a unit strictly above one has positive coordinates by conjugation, contrary to minimality. Thus \(t=\eta^j,\ t'=\eta^{j'}\), \(j'>j\). Write \(X_j=(\eta^j+\eta^{-j})/2\). Then \(X_0=1,\ X_1=u,\ X_{j+2}=2uX_{j+1}-X_j,\ X_{2j}=2X_j^2-1\).

* If \(u\) is even, \(X_j\) is even precisely for odd \(j\). For an accepted index \(j=2k\), the requirement \(X_j\equiv3\bmod4\) and the doubling formula force odd \(k\). Thus \(j,j'\equiv2\bmod4\) and \(q\ge\eta^4\ge(2+\sqrt3)^4\).
* If \(u\) is odd, \(X_{2k}\equiv1\bmod4\) and \(X_{2k+1}\equiv u\bmod4\), by the recurrence. An accepted index is odd and \(u\equiv3\bmod4\). For odd \(j\), \(X_j\equiv u\bmod3\), by the same recurrence in the cases \(u=0,1,-1\bmod3\). Acceptance gives \(u\equiv1\bmod3\), hence \(u\ge7\). The indices differ by at least two and \(q\ge(7+\sqrt{48})^2=\rho\).

Both cases give \(j'-j\ge2\), so \(q\ge\eta^2>4v^2D\ge4D\). This proves (1). The absolute constant is sharp across ordinary sources: take \(D=3,\ \eta=2+\sqrt3,\ j=4k+2\). The resulting positive odd sources have successive ratios tending to \(\rho\); this example does not put the sources on one orbit.

## 2. A quadratic norm charges each return to its shortcut clock

The same-field return mechanism is prior work: [PR192, P2](https://github.com/GettysburgResearch/collatz/blob/ae48a04cca29abe5fc8273bcda45e7eee0874896/research/astra-unconventional-20261126/adelic/PELL.md) proves the all-word bound \(x\le4\cdot36^h\). The direct integer norm below sharpens it to \(x<3\cdot12^h\), keeps the actual carry, and is then combined with the source spacing to pack an arbitrary marked set of visits. The underlying no-return mechanism is not claimed as new.

Let odd \(y\) follow odd \(x\) after \(h\ge1\) actual shortcut steps, \(b\ge1\) of them odd. Write \(A=3^b,\ B=2^h\). Then \(By=Ax+C\), with \(0<C\le3^h-2^h\). The upper bound follows by induction on the letters: an even step keeps \(C\) unchanged, and an odd step replaces it by \(3C+2^h\) at current length \(h\).

Suppose \(D(x)=D(y)=D\). Write \(X=6x+1,\ Y=6y+1\), with positive Pell coordinates \(V,W\), respectively. Then \(K=BY-AX=6C+B-A\) is an integer. In \(\mathbb Q(\sqrt D)\) set
\[
  \epsilon=K-(BW-AV)\sqrt D
          =\frac B{Y+W\sqrt D}-\frac A{X+V\sqrt D}.
\]
Its norm is a nonzero integer. If it vanished, the nonsquare \(D\) would force \(K=BW-AV=0\). Together with \(BY=AX\), the two Pell identities would then give \(B^2=A^2\), impossible by unique factorization. If \(|\epsilon|\le1\), its conjugate \(2K-\epsilon\) has absolute value at most \(2|K|+1\). The case \(|\epsilon|>1\) is immediate, so always \(|\epsilon|\ge(2|K|+1)^{-1}\).

The displayed reciprocals are positive and \(Y>6Ax/B,\ X>6x\), whence \(|\epsilon|<\max(A,B^2/A)/(6x)\). Thus
\[
    6x<(2|K|+1)\max(A,B^2/A),\qquad x<3\cdot12^h<2^{4h+2}.               \tag{3}
\]
Here \(|K|\le6\cdot3^h\) and \(\max(A,B^2/A)\le4^h\). The exact first inequality keeps the actual affine carry. This argument uses arbitrary complete intervening words.

## 3. Packing a sparse set of visits

Let \(m\ge1\) count all visits to one \(D\) on a primitive odd cycle. In chronological order sum (3) over the shortcut distances to the next visit, including the cyclic seam. These clocks total at most \(2P\): multiplying \(2^{a_i}=(3+1/x_i)x_i/x_{i+1}\) over a lap gives \(2^{\sum a_i}\le4^P\). Thus \(\sum_{\rm visits}\log_2 x<8P+2m\). The \(m\) physical sources are distinct. Sorting them by height and applying (1) gives
\[
             m\log_2 s+\tfrac72 m(m-1)<8P+2m,                              \tag{4}
\]
where \(s\) is the cycle minimum. In particular \(m\le2+2\sqrt P\): the opposite inequality would give \(m(7m-11)>16P\).

For \(N\ge1\) odd edges from one fixed positive odd \(n\) with distinct departures, the total shortcut clock is at most \(2N+\log_2 n\) by the same product and positivity of the terminal value. Discard the last occurrence of \(D\) in chronological order. Each of the other \(k=\max(m-1,0)\) visits has its next return inside the prefix. Sorting these \(k\) locations and summing their clocks yields
\[
               \tfrac72 k(k-1)\le8N+4\log_2 n+2k.                          \tag{5}
\]
In particular each class has \(O(\sqrt{N+\log(2n)})\) occurrences. Repeated laps do not supply fresh sources in this prefix statement.

Because \([D(x)]=[3]+(a\bmod2)[2]+[xy]\), an affine \(r\)-space of adjacent-product squareclasses supplies at most \(2^{r+1}\) discriminants. Multiplication gives the bounds stated at the beginning, with no choice of the coset prescribed in advance. A subset capturing a fixed positive fraction of an \(N\)-edge injective prefix requires dimension at least \(\tfrac12\log_2 N-O_n(1)\).

## 4. Near-logarithmic rank for a complete list

If the whole list of adjacent products has affine rank \(r\), all product vectors lie in a linear space of dimension at most \(r+1\). Since \([x_{i+1}]=[x_i]+[x_i x_{i+1}]\), the states lie in a single affine space of dimension at most \(r+1\) and have linear span of dimension at most \(r+2\). This uses all the intermediate edges. The [short-circuit record argument](RANK_CERTIFICATE.md) gives \(\log_2 M=O((r+1)^2)\) for a cycle maximum and \(O((r+1)^2+\log(2n))\) for a fixed-source prefix. The same qualitative estimate follows independently from [PR192, A3](https://github.com/GettysburgResearch/collatz/blob/ae48a04cca29abe5fc8273bcda45e7eee0874896/research/astra-unconventional-20261126/adelic/README.md).

By (1) each \(D\) occurs at most \(1+\log_\rho(M/s)\) times on a primitive lap, or \(1+\log_\rho M\) times among distinct positive sources. Therefore
\[
  P=O(2^r(r+1)^2),\qquad
  N=O(2^r((r+1)^2+\log(2n))).
\]
If \(r\ge\log_2P\) the claimed lower bound already holds. Otherwise use \(r<\log_2P\) in the polynomial factor and take logarithms. This proves \(r\ge\log_2P-O(\log\log(P+2))\) and \(r\ge\log_2 N-O_n(\log\log(N+2))\). On a non-eventually-periodic fixed orbit the quadratic field extension generated by square roots of the adjacent-product ratios therefore has degree at least \(N/(\log N)^{O(1)}\).

In the earlier narrow band \(M/s\le(16s+7)/(3s)\le23/3<\rho\), all \(D\)'s on one primitive lap are distinct, so \(P\le2^{r+1}\). The prior [period exclusion](../../six-hour-20261127/arithmetic/CRT_PERIOD_EXCLUSION.md) gives \(P>10^{1000}\) under its stated primitive, binary-valuation and height hypotheses. This yields \(r\ge3321\) in that band.

A positive ordinary realization satisfies the complete closing divisibility and every edge used above. The restrictions combine the integer Pell coordinates with one actual orbit, including the seam for the cycle counts. A conflicting upper bound on the allowed mod-square rank or a forced low-rank set of sufficiently many visits for every proposed counterexample remains open.
