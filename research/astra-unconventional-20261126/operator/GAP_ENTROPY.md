# An almost linear odd-grade lower bound for all-class paired steering

**SOURCE-QUALIFIED written proof.** Fix the positive shortcut map \(T(2n)=n,\ T(2n+1)=3n+2\). Call a pair word admissible if, from an ordinary pair \((Y,3Y-1)\), it ends at \((X,3X-1)\) after a common clock \(H\), with equal odd counts on the two arms. Let \(W(P)\) count distinct such words over **all** positive choices of \(X,Y\) and all \(H\), with grade at most \(P\). Two occurrences of one pair of binary words count once. The estimate includes nonprimitive returns and the empty word.

**O7.** With absolute constants,
\[
 \log W(P)\ \ll\ (P+1)[1+\log\log(P+3)]^2.
 \tag{1}
\]
For any one fixed ordinary target \(X\), each lower word determines at most one ordinary source \(Y\). Covering all units modulo \(3^L\) from this fixed target by equal-grade paired returns therefore requires
\[
 P\ \gg\ {L\over[1+\log\log(L+3)]^2}.
 \tag{2}
\]
For \(P\ge L\) this is immediate; otherwise substitute \(P<L\) on the right side of (1). The proof controls a family of finite words. It does not charge a particular residue class at this cost, or assert that a steering procedure exists. It also does not imply the stronger exponential word count \(W(P)\le K^P\), which remains OPEN.

## 1. Integer carry and total time at rank zero

Use the signed rank \(r\) and nonzero integer \(C\) of [PAIRED_CAPACITY.md](PAIRED_CAPACITY.md). Initially \(r=1,\ C=-1\). A simultaneous even clock is called idle; all other clocks are active. An idle clock sends \(C\) to \(C/2\) without changing the rank. At an active clock with new rank \(r'\),
\[
  |C'|\le\tfrac32 |C|+\tfrac12 3^{|r'|}.
\]
Throughout the word there are at most \(2P\) active clocks and \(|r|\le P+1\). Iterating the last inequality while dropping the contractions at idle clocks gives \(|C|\le (3/2)^{2P}(1+3^{P+1})\). In particular \(v_2(C)\ll P+1\) at every clock.

A rank-zero hold is a clock starting and ending at rank zero. At such a clock \(e=f\) and \(2C'=3^e C\). Let \(H_0\) count *all* these clocks, including simultaneous odd ones. For any maximal complementary stretch with \(k\ge1\) active clocks, the starting rank is zero or, for the initial stretch, one. All of its ranks have magnitude at most \(k+1\). Ignoring any idle contractions gives
\[
 |C_{\rm end}|\le(3/2)^k |C_{\rm start}|
       +3^{k+1}\big((3/2)^k-1\big)
 \le18^k |C_{\rm start}|,
\]
using \(|C_{\rm start}|\ge1\). A stretch without active clocks only contracts. Multiply across stretches and rank-zero holds, using \(|C_{\rm end}|\ge1\), to obtain
\[
        2^{H_0}\le3^P18^{2P},\qquad H_0\ll P.
 \tag{3}
\]

## 2. Valuation of the additive part of a short middle word

A legal subword of \(h\) clocks, with local odd counts \(a,b\) and affine offsets \(c_x,c_y\), sends \(x,y\) to \((3^a x+c_x)/2^h,(3^b y+c_y)/2^h\). If the starting rank is \(r\) and the ending rank is \(r'=r+b-a\), substitution gives
\[
 2^h C_{\rm end}=3^j C_{\rm start}+D,\qquad
 D=3^{(-r')_+}c_y-3^{(r')_+}c_x .
 \tag{4}
\]
Here \(j=(-r')_++b-(-r)_+=(r')_++a-(r)_+\ge0\). Each offset is nonnegative and at most \(3^h-2^h\), by induction on the affine numerator. A zero offset means the arm had no odd departure. A positive offset is a unit modulo three, since its last odd departure contributes a power of two and all earlier odd contributions are multiples of three. Consequently, if the subword contains an active clock and \(D=0\), both offsets are positive and \(r'=0\).

There is an absolute \(K\ge1\) such that every *nonzero* additive term in (4) satisfies
\[
                 v_2(D)\le K(1+h)\log(P+3).
 \tag{5}
\]
For a zero individual offset, or unequal valuations of the two offsets, this is immediate from their height bound. Otherwise divide their common power of two from the two positive offsets to get positive odd \(A,B\). Up to a sign and this power of two the term equals \(3^t A-B,\ t=|r'|\le P+1\). Apply Kunrui Yu's Theorem 1 with two units \(3,A/B\), exponents \(t,1\), and \(B_{\rm exp}=\max(3,t)\), to \(\Xi=3^t A/B-1\ne0\). Take the fixed field \(\mathbb Q(\zeta_3)\) and its prime over two; this meets the root-of-unity hypothesis, and the rational 2-adic valuation is unchanged since two is unramified. Both rational heights are bounded by \(O(1+h)\) for \(A/B\) and an absolute constant for three. The fixed-field theorem gives (5) after restoring the common power of two. The theorem, as stated, permits multiplicative dependence. [Yu, *p-adic logarithmic forms and group varieties II*, Acta Arith. 89 (1999), §1, (1.2), (1.8), Theorem 1](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf).

## 3. Gaps with two large ends must be separated

Write the word as an ordered list of active symbols from \((1,0),(0,1),(1,1)\), each preceded by its idle gap \(g_i\ge0\), and a final idle run. Just before \(g_i\), let \(v_i=v_2(C)\). Legality gives \(0\le g_i\le v_i\). Put \(d_i=\min(g_i,v_i-g_i)\); knowing the previous decoded state, this integer and one bit recover the actual gap. For \(L\ge1\) let \(N_L\) count the indices with \(d_i\ge L\).

Fix consecutive such indices \(i<j\). Start the following analysis **after** gap \(g_i\) and just before its active symbol. The current carry \(C_*\) is divisible by \(2^L\). Count elapsed clocks from here. At an endpoint after \(h\ge1\) clocks immediately following an active symbol, the subword starts with an active symbol, so (4) applies with the rank-zero conclusion when \(D=0\).

Choose \(M=\max(8,4K\log(P+3)+8)\). As long as \(h+1<L/M\), (5) gives \(v_2(D)<L\) when \(D\ne0\). Then (4) forces \(v_2(C_{\rm end})=v_2(D)-h\le M(1+h)/4\). The entire next idle gap has at most this length. The next active endpoint, if used, therefore has \(1+h_{\rm next}\le M(1+h)\). In particular one cannot already start \(g_j\ge L\) at such an endpoint.

If instead \(D=0\) before \(h+1\) reaches \(L/M\), the end rank is zero and \(v_2(C_{\rm end})\ge L-h\ge L/2\). The following \(L-h\) clocks must be rank-zero holds: as long as the carry is even the two arms have equal parity, and either common choice removes precisely one factor of two. There are enough clocks unless the word ends at rank zero, impossible for a return of final rank one. Before or during \(g_j\), this gives at least \(L/2\) rank-zero holds: if \(g_j\) begins before this run has ended, \(g_j\) itself is an idle run at rank zero and has length at least \(L\).

In the other case \(1+h\) reaches \(L/M\). Since the first post-active endpoint has \(h=1\), and each earlier nonzero-offset step multiplies \(1+h\) by at most \(M\), the segment from \(g_i\)'s end through \(g_j\)'s end uses at least a constant times \(\log L/\log M\) active clocks whenever \(L\ge M^4\). The segments for consecutive large indices are disjoint in clock interiors, including the ending idle gap and excluding the starting idle gap. Each is charged either this many active clocks, or \(L/2\) rank-zero holds. Equations (3) and the total active budget imply
\[
 N_L \ll 1+{P\log M\over \log L}+{P\over L}
 \qquad(L\ge M^4).
 \tag{6}
\]
For smaller \(L\), \(N_L\le2P\) suffices.

## 4. Count the words

Encode the active list and its end with \(O(P+1)\) bits. For each symbol, encode the flag and \(d_i\), for instance by a prefix-free binary code for \(d_i+1\) of length \(O(1+\log(1+d_i))\). Sequential decoding uses the previous exact carry, so the code recovers each gap without look-ahead. At a return the final idle gap is uniquely determined by its preceding carry, since it must end at rank one and carry \(-1\); alternatively its explicit length costs \(O(\log(P+2))\) bits. All gap parameters are \(O(P+1)\) by §1.

Summing the bound for \(N_{2^k}\) over \(0\le k\le O(\log(P+2))\) bounds the total logarithmic code length. The small scales cost \(O(P\log M)\). At larger scales the harmonic sum in (6) costs \(O(P\log M\,[1+\log\log(P+3)])\). As \(\log M=O(1+\log\log(P+3))\), this proves (1). The argument uses distinct ordinary trajectories only to guarantee nonzero carry throughout; the 2-adic logarithm estimate concerns the two rational units in (5), never a substituted Collatz source.

**Verification scope.** The physical one-clock update and carry nonvanishing are verified in [PairedCapacity.lean](PairedCapacity.lean). This counting proof and its use of Yu's theorem are written mathematics.

## 5. One specified entrance class and many possible terminals

Fix **one** residue \(Y\equiv A\pmod{3^L}\) in advance. Suppose a return word of grade at most \(P\) must be available for every ordinary \(X\) in a ternary cylinder \(X\equiv B\pmod{3^b}\), where \(b<L\). A particular word of grade \(p\) gives at most one possible residue of \(X\) modulo \(3^{L+p}\), from \(2^H X=3^pY+c_x\). If \(W_p\) counts the words of exactly that grade, counting residues at the common modulus \(3^{L+P}\) gives
\[
                    3^{L-b}\le \sum_{p=0}^P W_p\,3^{-p}\le W(P).
\]
Therefore (2) applies with \(L-b\) in place of \(L\). This is a family of possible ordinary targets with one specified entrance class. It leaves open the cost of that class for one specified ordinary target.

[GapArithmetic.lean](GapArithmetic.lean) verifies unit offsets of actual Boolean words, the rank-zero consequence of exact cancellation, deep divisibility of the additive term, and the excursion telescope with the looser absolute base \(24\). Its telescope takes the stated finite list of rank-zero equalities and complementary magnitude inequalities as input. Yu's theorem, the segmentation of an actual trajectory, the gap-separation argument and (1)–(2) are written steps. [Compiler and axiom output](../../../reports/astra-unconventional-20261126/operator/gap_arithmetic_lean.txt).
