# Smaller unit representatives for both ordered arms

**PROPOSED. Universal transfer is OPEN.** On positive integers let \(T(2s)=s,\ T(2s+1)=3s+2\). Write \(u\sim v\) for an ordinary common forward iterate, allowing different clocks. Three constructions below replace a unit pair \((q,3q)\) by an actually smaller unit pair with both ordered components preserved. They apply to either direction of a putative basin disagreement. They are independent of any analytic density input. PR195's directed tables give the role of the unit criterion and its earlier six-prefix construction. [PR195, round seven, exact head](https://github.com/GettysburgResearch/collatz/tree/0e8a7f9f965416189b30b57b8aa818fbcb7757c7/research/astra-global-closure-20261124/round7/head)

## An adaptive exclusion at the least odd tripling disagreement

Use the least-odd-disagreement reduction in the companion arithmetic note: if one exists, its lower member \(q\) is good, every positive integer at most \(q\) is good, and \(n=3q\) is bad. For this paragraph it suffices to assume these three statements. Factor the actual integer in both ways,
\[
 n=3^h w=2^m a-1,\qquad 3\nmid w,\quad a\text{ odd},\quad m=v_2(n+1).
\]
If \(h\ge3\), the positive integer \(z=2^h w-1\) is strictly below \(q=3^{h-1}w\), since \(2^h<3^{h-1}\) for every \(h\ge3\). The ordinary all-odd prefix gives \(T^h z=n-1\), so \(n-1\) is good. Also \(n+1\) is good for every \(m\ge1\), since \(Tq=(n+1)/2=T(n+1)\).

Put \(H_i=3^i a-1\). Now \(n\sim H_m\) and \(n-1=2(2^{m-1}a-1)\sim H_{m-1}\). (At \(m=1\), the latter argument has zero initial odd steps.) For any \(Y=4s+3\), \(T^2(Y-1)=T^2(3Y-1)=(3Y-1)/4\). If \(3^m a=1\bmod4\), use \(Y=3^{m-1}a\) to link \(H_{m-1}\) and \(H_m\). Consequently in this whole case \(z\) is an actual representative of the bad component below \(q\), a contradiction. The clocks depend on **both** valuations and may be arbitrarily long across the input family.

Thus a least failure with \(h\ge3\) requires \(3^m a=3\bmod4\). On this surviving side, use \(Y=3^m a\) to obtain \(H_m\sim H_{m+1}\), equivalently \(n\sim2n+1\). The positive neighbors \(n-1,n+1\) are still good. For \(m\ge3\) the surviving upper is itself the canonical failed source representative. Set \(U=(3^{m-1}a-1)/4\), an integer by the surviving residue, with \(U=2\bmod9\). Its parent component is good since \(4U=H_{m-1}\sim n-1\). Moreover \((4U+1)/9=3^{m-3}a\), where \(3\nmid a\), so the earlier canonical formula gives \(B(U)=2^m a-1=n\), and \(B(U)\sim9U+2\) by the ordinary all-odd path. If \(N\) denotes the least bad positive integer, then \(N\le B(U)=3q<3N\) under the least-odd-disagreement hypothesis. This sharpens the earlier factor 171 on this surviving branch alone. [Canonical source and ordinary edge proof](../../astra-closing-step-20261124/descent/README.md)

The argument does not give a smaller bad representative on this second side. The two-adic test is applied to the unit after the *entire* initial string of ones, at its actual ordinary stopping clock.

## A common contraction at different clocks

Let \(a\) be an odd ternary unit with \(T^t a=T^s(3a)=1\). For every \(q=a+D\) with positive \(D\) divisible by \(2^M\), where \(M=\max(3,t+2,s+2)\), put \(x=a+3D/4\). Then \(x<q\) is an odd ternary unit and
\[
 T^t x=T^{t+2}q,\qquad T^s(3x)=T^{s+2}(3q).
\]
In fact if \(T^h b=1\), the affine lift of the parity prefix gives \(T^h(b+2^h k)=1+3^{p_h(b)} k\). For the perturbations \(4k,3k\) the two endpoints coalesce because \(T^2(1+4v)=1+3v\). Apply this at \(b=a,3a\), using their own clocks and perturbations. The unit claim follows from \(x\equiv a\bmod 3\). If \(v_2(D)=m\ge M\), take exactly \(1+\lfloor (m-M)/2\rfloor\) successive such reductions before the size of the binary difference falls below this certificate's threshold. The exponent decreases by exactly two at each move. For example \(a=1,t=0,s=5\) covers **every** \(q=1\bmod128\) above one, without a ternary restriction. Its smaller unit is \(T^2q\). The individual-horizon lemma is kernel-checked as `cycle_scale`.

There is also a cylinder whose signed references do not converge to one. For \(q=8192t-21\), \(t\ge1\), put \(x=6912t-17\). Then
\[
 T^5q=x<q,\qquad T^8(3x)=T^{13}(3q)=2187t-5 .
\]
The signed reference \(-21\) reaches \(-17\) in five steps with three odd inputs. From \(-51\) the next eight steps reach \(-5\) with three odd inputs, and \(-63\) reaches \(-5\) in thirteen with six odd inputs. Affine parity lifting proves the identities on every positive member. Alternatively, use the positive base \(t=1\), as in the kernel-checked theorem `negative_twenty_one`. This is a full dyadic cylinder with no condition on the ternary digits. The two members of a pair can have different hitting clocks.

## A contraction with a stable ternary iteration

Set \(Q=9767881+258280326t\), \(X=2537983+67108864t\), \(t\ge0\). These are positive odd numbers and \(Q\) is a ternary unit. The two base prefixes at \(2537983\) and \(3\cdot2537983\) have length 26, each with 18 odd inputs. Their endpoints are 14651822 and 43955465. Consequently
\[
 T^{26}X=TQ,\qquad T^{26}(3X)=T(3Q),\qquad
 X<\rho Q,\quad \rho=2^{25}/3^{17}<0.260 .
\]
For the inequality, the exact affine relation is \(3^{17}X=2^{25}Q-160487363\). In all cases \(X=7\bmod8\), and \(X\) is a unit when \(t\ne2\bmod3\). Restricting to \(3^k\mid X+1\), \(k\ge1\), ensures it is a unit.

For every \(y=8s+7\) with \(3\mid y+1\) define \(R(y)=2(y+1)/3-1\). This is positive for the stated inputs. It satisfies
\[
 T(R(y))=y,\quad T^4(3R(y))=T^3(3y)=9s+8,\quad
 R(y)\equiv7\pmod8 .
\]
Furthermore \(v_3(R(y)+1)=v_3(y+1)-1\). For \(3^{k+1}\mid X+1\) these equations give \(k\) further strict decreases to the odd ternary unit
\[
 Z_k=2^k(X+1)/3^k-1,\qquad
 Z_k<\rho(2/3)^k Q,\qquad Z_k\sim Q,\quad 3Z_k\sim3Q .
\]
Increase the divisibility once to ensure that the last member is a unit. Each \(k\) is achieved on a whole arithmetic progression of \(t\), since the coefficient \(2^{26}\) in \(X+1\) is a ternary unit. Thus the gain can exceed any prescribed fixed factor while retaining **both** ordered components by explicit ordinary paths. This iteration is well founded on its stated domain. At the first unsatisfied ternary digit it gives no further move.

For a concrete lacunary consequence, set \(Q=(2^m-1)/3\). The conditions just used specify one class \(Q\bmod 3^{18+k}\) within the odd positives. Indeed \(Q=9767881+2\cdot3^{17}t\), and \(t\) is specified modulo \(3^{k+1}\). There is one even class of \(m\bmod 2\cdot3^{18+k}\) satisfying \(2^m\equiv3Q+1\bmod3^{19+k}\), since 2 generates the units by \(v_3(4^{3^j}-1)=j+1\). Oddness of \(Q\) then supplies the factor two in the displayed progression. Choose one exponent between one and two full periods. It has \(m\asymp3^k\); along these choices there is an actual upper representative
\[
  3Z_k\ \ll\ (2^m-1)m^{-\log_3(3/2)} .
\]
For even \(m\ge2\), \(2^m-1\sim2^{m-1}-1\): advance their all-odd prefixes to \(3^m-1\) and \(3^{m-1}-1\), respectively. With \(y=3^{m-1}=3\bmod4\), \(T^2(y-1)=T^2(3y-1)=(3y-1)/4\). Thus this gain also holds for the neighboring odd Mersenne index. It excludes these chosen exponents as minimum failures once a fixed contraction factor is exceeded. Exponents outside the congruences remain untreated by this construction.

[CarryDescent.lean](CarryDescent.lean) proves the adaptive downward merger and its size comparison, the affine lift, cycle contraction, the complete 26-step row, the stable carry and the complete signed-reference cylinder on positive inputs. [check.py](check.py) independently replays the paths and the selected exponent congruences. The arithmetic progression and asymptotic consequences are written proofs. No uniform selector on all odd inputs is obtained.
