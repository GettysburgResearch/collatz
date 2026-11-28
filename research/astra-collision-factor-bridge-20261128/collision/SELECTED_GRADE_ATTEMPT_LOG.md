# Attempt log for the actual stationary selected-grade lower bound

**Status: no closing estimate obtained.** This records the final native proof attempts after the independently reviewed [critical negative-grade theorem](../arithmetic/CRITICAL_GRADE_TAIL.md). It is not another equivalence theorem. The remaining estimate is the existing one-copy event in that theorem, with its ordinary selector retained.

The [stationary collision consumer](../factoring/STATIONARY_COLLISION_CONSUMER.md) is used with fair future words of length \(h\), a nonnegative real seed \(R_0\), and its jointly driven ternary seed. Write \(A_h\) for the grade, \(q=3^{A_h}\), \(r\) for the final ternary residue represented in \([0,q)\), and
\[
 \rho=X/2^h\le1,\qquad
 K=\left\lfloor\frac{R_h+q\rho-r}{q}\right\rfloor-
   \left\lfloor\frac{R_h-r}{q}\right\rfloor.
\]
The seed is independent of the future word. A stationary seed is required only when applying the stationary results; the finite identities below allow any such seed.

## 1. The selector phase is exactly uniform on a shifted finite grid

Put
\[
 U_h=\operatorname{frac}\bigl((R_h-r)/q\bigr).
\]
Then \(K=1\) exactly when \(U_h\in[1-\rho,1)\), with the full interval understood when \(\rho=1\). The half-open convention follows directly from the displayed floor difference.

For a word \(w\) of grade \(a\), write its affine map as
\[
 f_w(x)=(3^a x+B_w)/2^h.
\]
The full ternary congruence gives
\[
 n_w=(2^h r-B_w)/3^a\in\mathbb Z,
 \qquad
 U_h=\operatorname{frac}\bigl((R_0-n_w)/2^h\bigr).
\]
Modulo \(2^h\), the integer \(n_w\) is the unique source parity class of \(w\). These classes permute all \(2^h\) residues. Thus for every fixed initial seed the phases are a shifted uniform grid of mesh \(2^{-h}\). Every interval of length \(X/2^h\) with the relevant half-open convention contains exactly \(X\) of those phases. In particular
\[
 \Pr(K=1\mid R_0,Z_0)=\rho
\]
exactly: the selector is independent of the initial joint seed.

This does not make it independent of the grade or of the final joint state. In the simplest exact native calibration, take the zero seed and \(h=X=1\). The even word selects no positive endpoint, while the odd word selects the actual endpoint \(T(1)=2\). Hence \(K=A_1\), and
\[
 \Pr(K=1,A_1=0)=0,
 \quad\Pr(K=1)\Pr(A_1=0)=1/4.
\]
The zero seed is not stationary, and this finite example does not disprove the desired critical stationary asymptotic. It identifies the invalid inference: uniform selector phase and a binomial grade marginal alone cannot justify their independence.

At the critical date the selected phase interval has length about \(X^{-3.8188}\), while its grid contains \(X\) points. Controlling the grade distribution in this particular shrinking interval is the missing arithmetic estimate. Rewriting it as a phase interval does not supply that estimate.

## 2. An identical-word coupling gives only the diagonal scale

For two independent initial seeds, put \(k=\lfloor R_0\rfloor\) and \(k'=\lfloor R'_0\rfloor\). Consider the contribution to the two-copy event \(J=1\) in which the two complete future words are identical. For a fixed common word, equality of the selected endpoints corresponds to the same ordinary source in both shifted source windows. Summing over the common word counts exactly their intersection:
\[
 \sum_{|w|=h}J(w,w)
   =\bigl(X-|k-k'|\bigr)_+.
\]
Each identical ordered word pair has probability \(4^{-h}\). Consequently its exact contribution is
\[
 \Pr(J=1,\ w=w')
   =4^{-h}\,\mathbb E\bigl(X-|k-k'|\bigr)_+.
\]
After the collision normalization \(4^h/X^2\), this contributes at most \(1/X\). For every fixed proper seed law it is asymptotic to \(1/X\), by bounded convergence applied to \(\min(|k-k'|,X)/X\). No finite first moment is needed for that assertion. The fair-seed truncated-moment bound further gives an error of order \(\log X/X^2\).

Thus forcing both copies to use the same random future does not produce a positive limiting collision coefficient. It supplies the familiar diagonal scale. A common-tail argument would still have to control the arithmetic relation between the two different prefixes; that relation was not evaluated here.

## 3. Why the stationary marginal and entropy inputs did not close the estimate

The actual stationary real/ternary law is singular with respect to product Haar measure. Its full product-metric dimension and its weak dyadic equidistribution on a compact quotient do not give a relative estimate on shrinking ordinary integer fibres. The quotient identifies the different integer diagonals. These are explicit scope limitations of [Weaver's original joint-law manuscript](https://rstation.ai/r/collatz/posts/33), especially Sections 1, 7, 10.6 and 11; they are not additional assumptions introduced in this pass.

The same source's bounded grade/endpoint mutual information concerns a finite-depth law from a product-Haar seed. It is not an independence theorem at a selected integer fibre. Even a bounded global information cost permits an order-one bias after conditioning on an event whose probability tends to zero. Applying that bound directly to the critical selector would therefore leave the essential relative error uncontrolled.

A related attempt was to extend ordinary component labels to the ergodic stationary affine process, then use its ergodicity. No valid extension with the needed ordinary trace and label transport was constructed. Integer diagonals have ambient measure zero. Moreover, the genuine visit-to-five label already has a nontrivial natural density while its failure of invariance occurs at only one ordinary edge. Any argument using only ambient almost-everywhere invariance would lose precisely the finite ordinary information that this calibration detects. A successful trace theorem would have to state and prove that interface; stationarity by itself does not supply it.

## 4. What the final attempt actually leaves

The critical negative-grade theorem remains the strongest new consumer: one path, one explicit grade threshold, and the full ordinary selector. Its limiting negative tail is the reviewed cycle mixture, with a strict contraction-scale gap between the known cycle and every other positive cycle. The one-eighth question would be settled by the stated relative lower bound for this selected event.

None of the attempts above proves that bound. The independent binomial law of the unselected driving bits, exact one-copy normalization, identical-word coupling, and weak stationary quotient information were all checked; each falls short at the explicit interface described here. No numerical extrapolation or freshly independent post-minimum parity process is used to bridge that gap.
