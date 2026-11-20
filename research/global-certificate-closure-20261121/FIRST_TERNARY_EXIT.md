# Final closing attempt: the first ternary exit does not repay the source height

**Status: exact failed inequality and a proved scoped dead-end lemma. No
complete adaptive construction or Collatz proof.**

This is the requested attempt to turn the newly certified small five
comparisons into an actual smaller reverse failure. It retains the given
ordinary source, its full certificate, and the same upper-height bound.
It also checks the late PR169 bypasses rather than treating two new cells
as a complete adaptive rule.

Dependencies and comparison sources:

- PR163 `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`,
  `MERSENNE_WITNESS_DEPTH.md`, already observes that repeated \(I_2\)
  steps spend finite ternary precision while expanding height, and that
  one subsequent \(I_1\) step does not repay it when the expansion run is
  long. That fact is credited here. The additional details below are the
  exact reverse-guard failure, infinite actual exponent classes where
  the first exit has no further odd predecessor, and the source-specific
  c=3 comparison.
- The present packet's `SMALLER_FIVE_FAILURES.md` supplies the actual
  certified values \(r=5U(q)\) against shifted targets \(2r-1\) and
  \(4r-1\), under one least reverse failure.
- PR169 `6cb9bfdc828f91576066b0e4a099d47d8144e915`,
  `research/certificate-renewal-20261121/C5_CERTIFIED_BYPASSES.md`,
  gives two genuine smaller paired reverse instances on specified
  residue classes. Section 4 below checks their exact relation to this
  attempted adaptive extension.

## 1. Keep the actual certified pair throughout the precision run

Let

\[
e=119+162j,\quad P=2^e,\quad
\eta=\nu_3(4P-11),\quad h=\eta-5,\quad
D=\frac{4P-11}{3^\eta}.
\]

Then \(\eta\ge5\), and \(D\) is a positive odd ternary unit. The
hard rank-five pair is exactly

\[
X=1+256\,3^hD,\qquad Y=1+128\,3^hD. \tag{1}
\]

The upper has its actual first-hit word

\[
(2,2,2,5,e-1),
\]

and the lower has ordinary word \((2,2,2,1,2)\) to \(M=P-1\).

Applying \(I_2(v)=(4v-1)/3\) simultaneously \(i\) times, for
\(0\le i\le h\), gives

\[
A_i=1+256\,4^i3^{h-i}D,\qquad
B_i=1+128\,4^i3^{h-i}D. \tag{2}
\]

Every value is an actual positive odd integer. The ordinary forward word
\(2^i\) returns \(A_i\) to \(X\) and \(B_i\) to \(Y\). In
particular \(A_h\) is certified by

\[
(2^h,2,2,2,5,e-1), \tag{3}
\]

where \(2^h\) means repeated exponent-two letters. If the original
lower were bad, \(B_h\) would be bad as well. No free tripling or
changed source certificate has been used.

## 2. The exact failed repayment and the binary guard

At the first differing ternary digit, an exponent-one inverse from
\(B_h\) is available exactly when \(D\equiv2\pmod3\). It is

\[
Z=I_1(B_h)=\frac{1+256\,4^hD}{3}=\frac{A_h}{3}. \tag{4}
\]

The ordinary relation is \(U(Z)=B_h\). The putative companion upper
would have to be \(2Z-1\), and its exact height difference is

\[
\boxed{
(2Z-1)-X
=\frac{256D\bigl(2\cdot4^h-3^{h+1}\bigr)-4}{3}.
} \tag{5}
\]

For \(h\ge2\), this is strictly positive. Indeed
\(2\cdot4^2-3^3=5\), and the expression
\(F_h=2\cdot4^h-3^{h+1}\) satisfies
\(F_{h+1}=3F_h+2\cdot4^h>0\). Even \(D=1\) gives a positive
numerator in (5). Thus the first differing digit does **not** repay the
preceding expansion for arbitrarily deep actual sources.

There is also a separate domain failure, including at \(h=0,1\), where
the numerical comparison goes the other way. Formula (4) gives

\[
\boxed{Z\equiv3^{-1}\equiv171\pmod{256}.} \tag{6}
\]

An eligible reverse lower must be one of \(65,129,193\pmod{256}\).
Thus the first exit never itself constitutes an eligible reverse call.
Its source provenance in (3) certifies \(3Z\), not \(2Z-1\).
Substituting the latter as a certified antecedent would be an additional
unsupported step even if the other two guards had passed.

## 3. Infinite actual classes where that exit has no odd predecessor

For every fixed \(h\ge0\), impose the stronger digit condition

\[
\boxed{D\equiv2\,4^{-h}\pmod9.} \tag{7}
\]

It includes \(D\equiv2\pmod3\), so (4) is legal. But now

\[
A_h=1+256\,4^hD\equiv1+4\cdot2\equiv0\pmod9,
\]

and consequently \(3\mid Z\). For every \(a\ge1\),
\(2^aZ-1\equiv-1\pmod3\), so \(Z\) has no integral odd inverse
\(I_a(Z)\). This is a dead end for the proposed inverse continuation;
it does not rule out an earlier different branch or a forward excursion.

These conditions occur on infinitely many actual exponents in the given
rank-five progression, for every prescribed \(h\). To prove this, work
modulo \(3^{\eta+2}\), where \(\eta=h+5\), and prescribe

\[
P\equiv\frac{11+3^\eta d}{4}\pmod{3^{\eta+2}},
\qquad d\equiv2\,4^{-h}\pmod9.
\]

This lies above the required class \(P\equiv11/4\pmod{243}\).
The elementary order formula
\(\nu_3((2^{162})^{3^s}-1)=5+s\) shows that
\(2^{119+162j}\) runs through all such lifts. The resulting exponent
class has period \(2\cdot3^{\eta+1}\); its unit digit ensures that
the ternary valuation is exactly \(\eta\).

For example, all

\[
e\equiv767\pmod{13122}
\]

have \(\eta=7\), \(h=2\), and \(D\equiv8\pmod9\). Their first
exit has all three problems: \(2Z-1>X\), the residue in (6), and
\(3\mid Z\). Every such upper still has the explicit rank-five
ordinary certificate above. The statement is not about unverified
antecedents or limiting 3-adic sources.

## 4. The late PR169 bypasses do not supply the missing adaptive step

The two new certified contractions require, respectively,

\[
59049\mid16384k-6049,
\qquad
59049\mid32768k-9911.
\]

Reducing either condition modulo three gives \(k\equiv1\pmod3\).
But on (1),

\[
k=2\cdot3^hD.
\]

Therefore either new rule, when applied directly to the hard Mersenne
family, requires \(h=0\), equivalently \(\eta=5\). The rules are
genuine strictly smaller calls on their stated cells; they do not directly
cover the arbitrarily large \(\eta\) classes in section 3.

After spending \(h\ge1\) exponent-two inverses, the new standard-pair
parameter is \(2\cdot4^hD\). It is divisible by eight, whereas the
PR169 rules require \(k\equiv14\pmod{32}\). Applying the existing
bypass words at that expanded parameter would violate their binary
domain. A new variable-length paired word with checked guards is needed;
no such extension follows from the two cells.

## 5. The source-specific c=3 attempt produces a different target

The certified value

\[
r_0=\frac{2P-1}{9}
\]

appears as \(5U(q)\) in the valuation-four phase and as an ordinary
iterate of \(5U(q)\) in the other phase. Its ordinary path goes to
\(2^{e-1}+1\), then below the same least-failure floor.

For \(\eta\ge6\), one has \(r_0\equiv41\pmod{81}\). Hence it
does give the smaller eligible c=3 source

\[
\widehat X=\frac{512r_0-175}{81}
=\frac{1024P-2087}{729}<X,
\]

whose parameter is \(k/3\). Its upper prefix reaches the actual known
\(r_0\). However, its lower prefix reaches \(2r_0+1\), while the
prescribed bad Mersenne predecessor is \(4r_0-1\).

The c=3 internal parameters of this smaller source are exactly
\((a,e_{\rm block})=(3,1)\), because

\[
r_0+1=8\frac{2^{e-2}+1}{9},\qquad
3^3\frac{2^{e-2}+1}{9}-1
=2(3\cdot2^{e-3}+1).
\]

Thus this smaller comparison is already handled by the direct
\(e_{\rm block}=1\) transfer. It does not produce a smaller *failing*
comparison, and it does not meet the large-gap guard
\(e_{\rm block}\ge3a+80\). Connecting its target to the required
negative-shift target is still the missing physical step.

## Result of the closing attempt

The first-exit proposal fails at the exact inequality (5) and the domain
condition (6), with the infinite ordinary dead-end classes in (7).
The natural source-specific c=3 embedding gives a valid smaller query
whose target is already certified, but supplies no proved connection to
the bad Mersenne target. I have not obtained a complete smaller reverse
call from the new five phases.

`check_first_ternary_exit.py` checks the actual source certificates,
paired inverse paths, exit identities, and c=3 embedding for seven exact
exponent classes. The all-depth statements are proved above by the
explicit formulas and ternary order argument. Neither the checker nor
this lemma excludes longer adaptive constructions, branching before the
first exit, or ordinary forward excursions.
