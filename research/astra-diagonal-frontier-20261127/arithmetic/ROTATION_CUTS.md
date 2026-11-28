# Rotation locking across an interval of ordinary height cuts

Let an ordinary positive odd cycle have distinct phases \(x_i\), minimum \(s\), maximum \(X\), primitive odd period \(p\), and total native halving clock \(A\). The word has \(2^{e_i}x_{i+1}=3x_i+1\) and \(A=\sum e_i\). Assume \(X<8s\). There is no assumption on the individual \(e_i\).

**Simultaneous-cut theorem.** For every real \(S\) satisfying \(X/8<S\le s\), take the odd integers \(B_S=[S,8S)\cap(2\mathbb Z+1)\). On all their dyadic lifts \(u=2^k n\), \(n\in B_S\), \(k\in\mathbb Z\), project \(2^k(3n+1)\) to the immediately lower or equal lift, or to the immediately upper or equal lift. Write \(\rho_-(S),\rho_+(S)\) for the two rotations, measured in octaves per odd step. Then
\[
              \rho_-(S)=\rho_+(S)=A/p,\qquad \gcd(A,p)=1.
\]
One may replace \(B_S\) independently at every cut by **any** subset containing the cycle's phases. In particular finite native forward and backward tests that every phase passes may be used to thin the grid. All primitive cycles in the same grid have the same period and clock. On the binary physical branch \(X\le(16s+7)/3\), the required interval of cuts has length at least \(s/3-7/24\). This is a simultaneous global condition with one fixed reduced clock. Its satisfaction is necessary.

## Proof in the dyadic lift

For any finite nonempty set \(B\) of positive odd integers with \(\max B\le8\min B\), each of its dyadic lifts has a unique representation since its odd part is intrinsic. Sort all lifts as \((t_j)_{j\in\mathbb Z}\) with \(t_{j+N}=2t_j\) for \(N=|B|\). Define \(G(2^k n)=2^k(3n+1)\). It commutes with doubling. It is weakly increasing on the lifts: after canceling a common dyadic factor, a strict reversal would require integers \(n,m\in B\) and \(k\ge1\) with
\[
        2^k n<m,\qquad 2^k(3n+1)>3m+1 .
\]
The orientation with a nonpositive power difference is impossible by subtraction. An inversion thus gives \(0<3(m-2^kn)<2^k-1\), requiring \(k\ge3\) and \(m>8n\). This comparison also proves monotonicity across the seam of any chosen fundamental octave. Ties in the images can occur on the ambient grid.

Write \(f_-(j)=\max\{i:t_i\le G(t_j)\}\) and \(f_+(j)=\min\{i:t_i\ge G(t_j)\}\). Both are weakly increasing and \(f(j+N)=f(j)+N\). For any such map, its iterates modulo \(N\) eventually repeat. A repeat after \(d\) steps through \(m\) octaves gives the limit \(\lim_{k\to\infty}(f^k(j)-j)/(kN)=m/d\). To see independence of the start, translate one start by multiples of \(N\) to bracket another. Every iterate obeys the same brackets with constant difference \(N\). Thus one periodic component suffices to calculate the rotation exactly, including when the chosen start has a transient.

On actual phases \(G(2^k x_i)=2^{k+e_i}x_{i+1}\) belongs to the grid. Both projections are therefore exact and the orbit completes \(A\) octaves in \(p\) steps. For coprimality, restrict to the dyadic lifts of just the cycle. Their ordered index map is a weakly increasing bijection, since its restriction permutes the odd parts and each phase has a unique predecessor there. It is an integer translation, say by \(m\) positions. After \(p\) steps it has moved \(pA\) positions, so \(m=A\). Transitivity on all \(p\) residues gives \(\gcd(A,p)=1\). Other cycles contained in \(B\) have the same rotation, and the reduced fractions give the same clock and primitive period. Taking \(B_S\) and the indicated subgrids proves the assertions.

The strict inversion inequality and the single-cycle coprimality implication appear in the frozen dyadic cycle order theorem. The two rounded ambient maps and the **common rational on every cut** are the extension here. Weaver's earlier same-fiber ordering also underlies the full-band rank construction. [Dyadic cycle order at d21bac7](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/unconventional-20261126/adelic/DYADIC_CYCLE_ORDER.md) · [Full-band rank ordering at d21bac7](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/arithmetic/FULL_RANK_CURVATURE.md)

## Exact evaluation and the cut parameter

For a general real cut, the set \(B_S\) only changes when \(S=n\) or \(S=n/8\) for an odd integer \(n\). The dyadic grid and projections are intrinsic to this set. Changes of fundamental representative leave the rotation fixed. Consequently rational boundary values and one test in each open component of a bounded interval give its complete rotation profile. The half-open convention should be applied literally at an endpoint. For \(S\) a positive odd integer use the simpler fundamental octave \(L=4S\). Its labels are exactly \(L\le u<2L\) with \(u\not\equiv0\pmod8\), and \(G(u)=3u+\operatorname{lowbit}(u)\). Set \(b=1+\mathbf1_{G(u)\ge4L}\). Round \(G(u)/2^b\) in the designated direction to the nearest integer allowed modulo eight. An upper round reaching the upper octave boundary is represented at \(L\) with one extra octave. To justify this end convention, \(2L\) itself is an actual lift even though its residue modulo eight is zero, and is the first upper target there. A lower round never needs a value below \(L\), since \(G(u)/2^b\ge L\) and \(L\) is eligible. Iterating either map until a label recurs gives its exact rational rotation without using logarithms.

These parameter facts give a precise finite certificate: if one allowed cut has unequal rotations, or two allowed cuts have different common rotations, that candidate range cannot contain an ordinary cycle with those prescribed extrema. A positive cycle forces the full common plateau even when the minimum and maximum values are not supplied in advance. For example a proof that every interval of cuts with a fixed common rotation and upper endpoint \(T\) has length \(o(T)\) as \(T\to\infty\) would rule out unbounded ordinary cycles of physical ratio \(\le8-\eta\) for every fixed \(\eta>0\). No such uniform width bound is proved here.

## Exact persistence of an individual rounded periodic orbit

Suppose one of the two rounded maps at a cut has a periodic orbit. Record the odd representatives \(n_i\) in cyclic order and the signed relative octaves \(a_i\), so the designated edge out of \(n_i\) rounds the raw number \(3n_i+1\) to \(v_i=2^{a_i}n_{i+1}\). Set \(m=\min_i n_i\), \(M=\max_i n_i\). For a nonexact edge a **blocker** is an odd positive integer with some dyadic lift in the interval between the raw number and \(v_i\), with the raw endpoint included and \(v_i\) excluded. An exact edge contributes no blockers. Let \(K\) be the union of the blockers of all edges.

The exact set of cuts retaining this same oriented, lifted cycle is
\[
 (M/8,m]\ \setminus\!\bigcup_{z\in K}(z/8,z].
\]
Indeed all its vertices belong to the ordinary grid exactly on the first interval. On that interval the only way a recorded edge can cease being its designated lower or upper nearest lift is the presence of one of its blockers. The odd integer \(z\) is in the active grid exactly for \(z/8<S\le z\).

In particular a blocker in \([m,M]\) makes the witness impossible at every cut. Otherwise each blocker below \(m\) deletes an initial segment and each blocker above \(M\) a terminal segment, since \(S\in(M/8,m]\). Its persistence set is thus a **single half-open interval**
\[
  \left(\max\{M/8,\max_{z\in K,\,M/8<z<m}z\},
        \min\{m,\tfrac18\min_{z\in K,\,M<z<8m}z\}\right],
\]
omitting empty inner extrema. The finite search for blockers uses just \(M/8<z<8m\); for each fixed edge and bounded \(z\) range only finitely many dyadic powers can enter the specified interval. For an ordinary closed orbit every edge is exact. Its persistence interval is the full \((X/8,s]\). A bound on switches among **nonexact** rounded witnesses alone could leave this stationary witness untouched. A uniform width theorem needs either an incompatible comparator at some cut or a separate exclusion of the empty-blocker case. Equal rotation can also persist when one nonexact witness is replaced by another.

## Full denominator and finite controls

For a positive rational cycle \(x_i=N_i/q\) in lowest terms, the same native equations and total clock may hold, including in this very physical band. Its physical labels need not belong to the integer grid used above. Using integer numerators changes the raw map to \(G_q(2^k N)=2^k(3N+q)\); its strict inversion threshold is \(3(m-2^k n)<q(2^k-1)\). The ordinary monotonicity proof and rounding test use \(q=1\). For a positive word with carry \(K\) and determinant \(D=2^A-3^p\), that statement is precisely the full condition \(D\mid K\), since the denominator is \(D/\gcd(D,K)\).

The exact control compares the efficient odd-cut iteration to literal binary searches in the lifted ambient set. Its finite census of 50,000 odd cuts through 99,999 has exactly three equalities. At cut 1 it gives the actual fixed cycle's slope 2. At cuts 9 and 11 the shared rotation is \(8/5\), but the ordinary grid contains no cycle of that slope. Indeed a primitive 5-step positive odd word of clock 8 has native exponents a positive composition of 8 into 5 and determinant 13; direct exhaustive testing of these words gives no positive integer cycle. The control also computes actual rational mechanical cycles at \((p,A)=(5,8),(41,65),(306,485)\), retaining their complete reduced denominators. Each lies in the relevant real band but fails the ordinary plateau at a displayed cut. An independent opposite-sign test uses the genuine integer \(3x-1\) cycle \(5,7\). For this sign the width-four grid makes \(3u-\operatorname{lowbit}(u)\) monotone, including its seam, so its signed version is tested on every rational cell and endpoint of its own cut interval. This finite census does not bound the lengths of plateaus at arbitrary heights.

[Exact replay](check_rotation_cuts.py) · [Recorded controls](rotation_cut_controls.json)

## Angular clock bounds and an upper comparator for the lower map

Write \(\lambda=\log 2\) and \(\gamma=\log_2 3\). For *any* sequence of genuine positive cycles with minima \(s\to\infty\), including cycles with odd rational denominator, all dyadic angles \(t_i=\log_2(x_i/B)\bmod1\) approach uniform distribution for any choice of positive normalization \(B\) for each cycle. In fact
\[
 t_{i+1}=t_i+\gamma+\epsilon_i\pmod1,\qquad
 \epsilon_i=\log_2(1+1/(3x_i))=O(1/s).
\]
For every fixed nonzero Fourier index \(k\), telescoping the exponentials around the cycle gives \(|1-e^{2\pi i k\gamma}|\cdot|p^{-1}\sum_i e^{2\pi i k t_i}|=O_k(1/s)\). The factor on the left is nonzero by unique prime factorization. Trigonometric polynomial approximation gives the uniform limiting law, also for bounded functions with finitely many discontinuities. This argument is uniform in \(B\).

Consequently the ordinary native clock satisfies the asymptotic bounds
\[
  \liminf_{s\to\infty} X(A/p-\gamma)\ \ge\ \frac1{3\lambda^2},
  \qquad
  \limsup_{s\to\infty} s(A/p-\gamma)\ \le\ \frac1{6\lambda^2}.
\]
For the first inequality, \(X/x_i\ge2^{\{\log_2(X/x_i)\}}\), whose angular mean tends to \(1/\lambda\). For the second, \(s/x_i\le2^{-\{\log_2(x_i/s)\}}\), whose angular mean tends to \(1/(2\lambda)\). Average the uniform estimate \(\epsilon_i=(1+O(1/s))/(3\lambda x_i)\) to finish. In particular if \(X/s\le R+o(1)\) for fixed \(R\), then \(\liminf s(A/p-\gamma)\ge 1/(3R\lambda^2)\). These angular bounds do not distinguish the full denominator.

Here is an explicit sufficient comparison that would distinguish the ordinary bounded branch. Set \(L=4s\) and choose any integer subgrid known to contain every candidate phase. In its dyadic lift let \(E_-(V)\) be the largest grid point at most a positive real \(V\), and write \(F_-\) for the lower projected raw map in physical units. Suppose an infinite sequence of **probes**, which need not be grid points, has \(V_j\in[L,2L)\) and integer shifts \(b_j\) such that
\[
 F_-(E_-(V_j))\le 2^{b_j}V_{j+1}
       =3V_j+d_j,\qquad |d_j|\le C .
\]
The stronger left inequality with \(G(E_-(V_j))\) in place of its lower projection also suffices. From a dyadic lift of an actual phase below \(V_0\), induction and monotonicity bound its raw iterates by consecutive lifted probes. Dividing the logarithm by the elapsed number of steps gives \(A/p\le\liminf_{n\to\infty} n^{-1}\sum_{j<n} b_j\), since fundamental representatives lie in one octave. Applying the Fourier proof to long probe prefixes costs an additional \(O_k(1/n)\) from the two ends and gives Haar angular limits as \(s,n\to\infty\). This compares to the **lower** map forced by the cycle; it imposes no requirement that a probe follow the upper map or possess an ordinary native successor.

If one can arrange \(d_j\le1\) on a sequence of growing candidate scales with a common absolute \(C\), the telescoping probe clock and the Taylor expansion give
\[
 \limsup s(A/p-\gamma)
 \le \frac{1}{12\lambda}\int_0^1 2^{-t}\,dt
 =\frac1{24\lambda^2}.
\]
This contradicts the preceding lower bound for every fixed \(R<8\). More generally it suffices that the long-probe weighted means \(\sum d_j2^{-t_j}/\sum2^{-t_j}\) have upper limit strictly below \(8/R\), where \(t_j=\log_2(V_j/L)\). On the physical branch \(R=16/3\) this threshold is \(3/2\). A strictly positive margin in this average matters. Neither the sparse alphabet from a finite admissible past and future nor the finite rounding census constructs this infinite comparator for arbitrary scales.
