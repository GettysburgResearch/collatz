# Ordinary lifts with signed or repeated terminal words

**PROPOSED written theorem.** Fix one positive ordinary source \(n\) for the shortcut Collatz map \(T\), with even branch \(x/2\) and odd branch \((3x+1)/2\). Write \(x_k=T^kn\), and let \(p_k\) count the odd inputs in the first \(k\) steps. A positive lift \(m_k=n+2^kt_k\) follows the same \(k\) bits to \(x_k+3^{p_k}t_k\). Suppose an actual terminal word from this lifted endpoint ends at a positive integer \(r_k\).

Suppose \(r_k=1\) and the terminal word is a concatenation of a bounded number of powers of words whose root lengths sum to \(o(k)\). Fix any finite prime set \(S\supset\{2,3\}\). For every sequence of **distinct-from-\(n\)** lifts at \(k\to\infty\), the part \((t_k)_{S'}\) of the source displacement outside \(S\), retaining every multiplicity, satisfies
\[
                         \frac{\log (t_k)_{S'}}{k}\longrightarrow\infty.
\]
Here \(t_k>0\) eventually by positivity of \(m_k\). The number of odd inputs, the repetition exponents, the total duration of the suffix and the part of the displacement supported in \(S\) can all grow without any upper bound. A block root may change with \(k\). In particular any such witnesses of ordinary source size at most \(\exp(O(k))\) must eventually be \(n\) itself. The statement treats every fixed positive source, including a source on a putative nontrivial cycle or an escape.

The prior PR192 result proves superexponential growth of the full displacement for bounded odd count by a positive nondegenerate unit sum. Its companion note already handles moving targets with bounded odd count. PR192 also proves the exact triadic denominator formula and the superlinear cost of reaching a distinct power of two. The present conclusion forces the part outside any prescribed finite prime set to grow superexponentially and permits signed presentations with arbitrarily many odd inputs in an arbitrarily long suffix, also at moving targets. [PR192, bounded-odd theorem](https://github.com/GettysburgResearch/collatz/blob/b72cea3bcd5aa51aba8df6f5e63bc1c473e9523b/research/astra-global-budget-20261124/arithmetic/README.md) · [PR192, moving targets](https://github.com/GettysburgResearch/collatz/blob/b72cea3bcd5aa51aba8df6f5e63bc1c473e9523b/research/astra-global-budget-20261124/arithmetic/LATEST_CONNECTIONS.md).

## Fixed-source statement for the entire ordinary carry

In a sequence \(k\to\infty\), let the terminal word have length \(\ell\) and \(h\) odd inputs, at positions \(0\le i_1<\cdots<i_h<\ell\). Its positive affine carry is \(C=\sum_{j=1}^h 2^{i_j}3^{h-j}\), with zero permitted for an all-even word. Assume the following conditions.

1. The **same integer** \(C\) admits a presentation
   \[
      C=\sum_{j=1}^{s}d_j2^{u_j}3^{v_j},\qquad s=O(1),
      \quad u_j,v_j\in\mathbb Z_{\ge0},\quad v_j\le h+o(k).
   \]
   The rational coefficients may vary and have either sign, with \(\log\max(|\operatorname{num}d_j|,\operatorname{den}d_j)=o(k)\). There is no upper bound on \(u_j\), \(h\), or \(\ell\); the true terminal word must still be physically followed.
2. For a fixed \(\delta>0\), \(x_k r_k/3^{p_k}\le e^{-\delta k}\).

For every fixed finite \(S\supset\{2,3\}\), \(\log (t_k)_{S'}/k\to\infty\) along the distinct-from-\(n\) lifts. Equivalently, fixing any \(A<\infty\), all sufficiently late supplied lifts with \(t_k=0\) or \(0<(t_k)_{S'}\le e^{Ak}\) are \(n\).

Subtract the two affine rows of the common prefix, then apply the terminal affine row. This gives the ordinary integer identity
\[
     F=2^\ell r_k-3^h x_k-C=3^{p_k+h}t_k .                        \tag{1}
\]
The needed opposing size bound also comes from the same path. On an odd input \(z\ge1\) one has \(3z+1\le4z\). Multiplication over the actual prefix gives
\[
     2^k x_k\le 4^{p_k}n,\qquad
     x_k/3^{p_k}\le n\,2^{-k}(4/3)^{p_k}\le n(2/3)^k.             \tag{2}
\]
For example \(r_k\le \exp((\log(3/2)-\epsilon)k)\) suffices for condition 2, for any fixed \(\epsilon>0\). The sharper two-step bound \(x_k\le\sqrt3\,n\,3^{p_k-k/2}\) from PR192 allows \(r_k\le 3^{(1/2-\epsilon)k}\). The proof below only uses condition 2. Bounds \(x_k,r_k\le\exp(O_n(k))\) follow from (2), condition 2 and \(x_k\ge1,\ p_k\le k\).

## Pruning signed subsums and comparing the complete divisor

Work along distinct lifts at \(k\to\infty\). Since \(n\) is fixed and all lifts are positive, \(t_k\) is a positive integer for large \(k\). Delete zero atoms and retain a fixed number \(s\), passing to a subsequence as needed. Let \(D\ge1\) be the product of the reduced denominators of their coefficients, with \(D=1\) for an empty product. Both \(\log D\) and each \(\log|D d_j|\) are \(o(k)\). Take nonzero integer coordinates
\[
  Z_0=D3^{p_k+h}t_k,\quad Z_1=Dr_k2^\ell,\quad Z_2=Dx_k3^h,\quad
  Z_{j+2}=(D d_j)2^{u_j}3^{v_j}.
\]
Equation (1) gives \(Z_0=Z_1-Z_2-\sum_j Z_{j+2}\). On its right side delete any nonempty subsum with signed total zero, until none is left. At least one right-side coordinate remains since \(Z_0\ne0\). The zero sum with \(-Z_0\) adjoined has no proper nonempty zero subsum. A zero subsum containing \(-Z_0\) would have a complementary zero subsum on the right. Keep the resulting right indices \(I\). The finitely many possible dimensions are bounded in terms of the original atom count.

Let \(g\) be the content of the complete surviving tuple, including \(Z_0\). Put \(H=\max_{i\in\{0\}\cup I}|Z_i|/g\), and let \(P\) be the product of the outside-\(S\) parts of all its primitive coordinates \(|Z_i|/g\). Write \(a_{(q)}=q^{v_q(a)}\) for the full \(q\)-part of a positive integer. For **any** right pivot \(j\in I\), write each right coordinate as \(Z_i=b_i2^{u_i}3^{v_i}\), with \(u_1=\ell,v_1=0,\ u_2=0,v_2=h\) in the first two positions. The integer coefficients \(b_i\) include each relevant \(Dr_k,Dx_k,Dd_j\). Then
\[
\begin{aligned}
  \frac{P}{H}
  &\le \frac{(|Z_0|/g)_{S'}}{|Z_0|/g}\,
                        \prod_{i\in I}(|Z_i|/g)_{S'}\\
  &\le \frac{g_{(3)}}{|Z_0|_{(3)}}\prod_{i\in I}|b_i|_{S'}\\
  &\le 3^{v_j-p_k-h}\,|b_j|_{(3)}
                        \prod_{i\in I}|b_i|_{S'}\\
  &\le 3^{-p_k+o(k)}\prod_{i\in I}|b_i|
   \le x_k r_k\,3^{-p_k}\exp(o(k))\le e^{-\delta k/2}.            \tag{3}
\end{aligned}
\]
Indeed the first ratio on the first line is the reciprocal of the entire \(S\)-supported part, hence is at most the reciprocal of its 3-part. Dividing by \(g\) can only remove outside factors. Also \(g\mid Z_j\), so \(g_{(3)}\le3^{v_j}|b_j|_{(3)}\), while \(|Z_0|_{(3)}\ge3^{p_k+h}\). Since \(3\in S\), the product \(|b_j|_{(3)}|b_j|_{S'}\) divides \(|b_j|\). Discarded columns cost nothing because all their absolute integer multipliers are at least one. The last inequality uses the same fixed-source height from condition 2. This argument tolerates arbitrarily large valuations at every \(q\in S\), including those of the unknown lift and of its target.

There is also an exact divisibility version of (3). Put \(V=|Z_0|/g\) and \(R=\prod_{i\in I}|b_i|\). Every primitive outside part on the right divides its multiplier, so \(P\mid VR\). The inclusion \(3^{p_k+h}\mid gV\) and \(g\mid 2^{u_j}3^{v_j}|b_j|\) give \(3^{p_k+h}\mid V3^{v_j}|b_j|\) after canceling the coprime \(2^{u_j}\). As \(P\) is coprime to three, this gives the full integer divisibility
\[
                      3^{p_k+h}P\mid 3^{v_j}VR.
\]
Together with \(V\le H\) it is another proof of the strict gain. It retains each outside prime power even when several primitive coordinates have common factors.

For a two-term zero sum the primitive tuple has absolute coordinates \(1,1\), so \(P=H=1\), incompatible with (3) at large \(k\). In each of the finitely many larger dimensions, Evertse's Corollary 1 applied to the **primitive signed zero sum** gives, for each fixed \(0<\epsilon<1\),
\[
                             P\ge c_{S,s,\epsilon} H^{1-\epsilon}.  \tag{4}
\]
The primitive coordinates have collective gcd one and the required nonzero proper subsums. The corollary with its constant parameter equal to one has finitely many exceptional tuples, absorbed by decreasing \(c_{S,s,\epsilon}>0\). Take the least constant over the finitely many dimensions. No uniformity over changing \(S\), atom budget, or \(\epsilon\) enters. Combined with (3), (4) gives \(\liminf (\log H)/k\ge\delta/(2\epsilon)\). Letting the fixed \(\epsilon\) decrease proves \((\log H)/k\to\infty\). On the other hand, with \(\epsilon=1/2\), (4) and the original coordinates give
\[
 H^{1/2}\ll_{S,s} P
       \le (t_k)_{S'}\,x_k r_k\,\exp(o(k)).
\]
Here \(D\) has subexponential size; no powers of two or three survive in an outside part. Because \(\log(x_k r_k)=O(k)\), it follows that \(\log (t_k)_{S'}/k\to\infty\). The argument works on every subsequence with a fixed number of nonzero atoms, hence on the entire claimed family. The moving rational coefficients were put into ordinary integer multipliers before the external theorem was applied. Its only prime set is the prescribed fixed \(S\). [J.-H. Evertse, *On sums of S-units and linear recurrences*, Corollary 1, p. 227, equations (9)–(12)](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf).

## Repeated words and a global sufficient condition

For a nonempty root word of length \(b\), odd count \(a\), and ordinary carry \(c\), put \(A=2^b,\ Q=3^a\). Distinct prime powers give \(A\ne Q\). Its \(d\)-fold repetition has carry
\[
                         c\,\frac{A^d-Q^d}{A-Q}.                  \tag{5}
\]
The coefficient \(c/(A-Q)\) has logarithmic rational height \(O(b)\), since each of the at most \(b\) literal carry terms is at most \(6^b\). Concatenating repeated blocks multiplies each block's carry by powers of two from preceding blocks and powers of three from subsequent ones. Expanding (5) gives at most two atoms per block, with \(0\le u_j\le\ell,\ 0\le v_j\le h\), even when \(\ell\) is arbitrarily large. For a bounded number of blocks with sum of root lengths \(o(k)\) their coefficients therefore meet condition 1. This proves the opening theorem.

It follows that \(n\) reaches 1 if and only if arbitrarily deep prefix cylinders of \(n\) have a positive witness which reaches 1 through this kind of terminal word and whose displacement has outside part at most \(\exp(O(k))\) for some fixed finite \(S\supset\{2,3\}\), also allowing \(t_k=0\). No bound on the full witness size is required. When \(n\) converges, take \(m_k=n\); every sufficiently late \(x_k\) reaches 1 in at most one additional step. Conversely the theorem forces every such supplied witness to equal \(n\) eventually along the witnessing sequence. This covers escape and cycles without first specifying which sort of counterexample \(n\) might be. A construction that insisted on distinct lifts with this resource bound would fail even at \(n=1\).

There are explicit ordinary witnesses with a first-hit suffix of this shape in **every** positive prefix cylinder. Fix \(k\) and **any** integer \(d\ge1\), which may grow arbitrarily with \(k\). Choose large \(j\) with
\[
         2^j\equiv 3^d(x_k+1)2^{-d}-1\pmod{3^{p_k+d}} .
\]
The target is a unit since it is \(-1\bmod3\), and 2 generates the units. Indeed \(v_3(4^{3^a}-1)=a+1\) by induction with the binomial theorem and \(2\bmod3=-1\). The exponents \(j\) form a nonempty progression. Thus \(z=(2^j+1)/3^d\) is a positive odd integer, and \(y=2^d z-1\equiv x_k\bmod3^{p_k}\). Choose \(j\) large enough that \(t=(y-x_k)/3^{p_k}>0\) and \(y>1\). The lift \(m=n+2^k t\) follows the actual first \(k\) bits to \(y\); it cannot have hit 1 before then since \(m>2^k\) and no step shrinks faster than halving. Its next \(d\) inputs are odd with exact states \(2^{d-i}3^i z-1\) at \(0\le i\le d\). It reaches \(2^j\) at \(i=d\) and then halves to its first 1. The suffix is exactly \(1^d0^j\), with no laps after convergence. Taking \(d=k\) exercises unbounded odd counts and two roots of total length two. The theorem forces \(\log (t)_{S'}/k\to\infty\) for **every** choice of these witnesses. The resource gap is therefore isolated even where these sparse terminal words and the target 1 have both been realized explicitly.

At every sufficiently late \(k\), \(x_k\) is a ternary unit, and powers of two exhaust its residue class modulo \(3^{p_k}\). Taking any \(2^j>x_k\) in that class gives a distinct positive lift with an all-even suffix to 1. Such witnesses exist for **every** fixed source once the restriction on the outside part of the source displacement is dropped. The known PR192 power-of-two case forces \(j/k\to\infty\) along the least such exponents. This is evidence for the necessity of a resource restriction, and is already covered by the pinned bounded-odd result. [PR192, bounded lifts and power-of-two equality](https://github.com/GettysburgResearch/collatz/blob/b72cea3bcd5aa51aba8df6f5e63bc1c473e9523b/research/astra-global-budget-20261124/arithmetic/README.md).

PR193's fixed-coset Pell bound does not put a given terminal carry into the signed additive class. PR192's earlier signed forward-window argument measures a carry along **one** fixed escaping trajectory. Here the competitors are changing positive lifts of a common prefix, the target may move, the large forced divisor is exactly (1), and the bound concerns the part of the source displacement outside any fixed prime set even when the terminal duration is arbitrarily large. PR195's round-seven elementary rigidity uses the actual terminal duration via \(2^\ell r_k<x_k+3^{p_k}\); it does not give this source-size conclusion for long structured suffixes. [PR193, transition products](https://github.com/GettysburgResearch/collatz/blob/bdd4409062bc02416ff6941f8d5690b800068cb3/research/astra-deep-closure-20261124/arithmetic/README.md) · [PR192, signed sums on a forward orbit](https://github.com/GettysburgResearch/collatz/blob/d2081d1cd2410e6004eaee9f9b13c5553afaf3f4/research/astra-closure-attack-20261124/FIXED_SOURCE.md) · [PR195, elementary suffix cost](../../round7/renewal/README.md).

The remaining issue is **existence** at each supplied fixed ordinary source, such as \(3u\) when \(u\) reaches 1. The argument forces a ternary divisor in an ordinary affine equation. It gives no large divisor of the different prime-to-six integer \(\gcd(|2^{k+p_k}-3^k|,C_k^{\rm comp})\) from round seven. No family meeting the new sufficient condition at every \(3u\) is presently established.


This boundary can be checked on the actual suffix-57 heads used in the directed implication. For \(27b=2^d u+1\), \(y=8b-1\) follows three odd steps to \(2^d u\), then \(d\) even steps to \(u\). Its child \(81y+57=2^{d+3}(3u)\) follows only even steps to \(3u\). As \(d\) increases, the two varying starts approach \(-19/27\) and \(0\) dyadically, since \(y=-19/27+(8u/27)2^d\). The first limiting dyadic source takes those three odd steps to zero; the second is zero from the start. Thus the shared early prefixes have only three and zero odd inputs, respectively. They do not give the growing \(p_k\) of a **fixed positive** source \(3u\) required in (1)–(3). A stopping word for \(u\) on one arm supplies no compressed terminal word after arbitrarily many actual bits of \(3u\) on the other. [PR195, the exact directed-head construction](../../round7/head/README.md).


## Evidence

[SparseTerminal.lean](SparseTerminal.lean) proves the ordinary shared-prefix lift, the exact displaced terminal row, the elementary height bound, the two literal runs, the repeated-block identity, signed zero-subsum pruning, the stripping of clock prime factors, and the last full integer divisibility. The \(S\)-part extraction in the proof applies its outside-product hypotheses to the actual prime factors, as shown in the text. The invocation of Evertse and the limiting and uniformity conclusions are written mathematics. The independently published finite checks from PR192 have their own source boundary.

[check.py](check.py) checks 624 finite signed physical tuples and 6,364 exact pivot divisibilities at two prime sets. It removes 628 zero subsums, exercises nontrivial common content and moving rational coefficients, and constructs 48 two-run first-hit witnesses, including \(d=k\). The three longest tested halving tails are verified from their exact power-of-two endpoints; the other 45 are also stepped through. The computations make no asymptotic claim. [Exact control output](../../../../reports/astra-global-closure-20261124/round8/arithmetic/controls.json) · [Kernel output](../../../../reports/astra-global-closure-20261124/round8/arithmetic/SparseTerminal.log).
