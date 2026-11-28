# Exact finite bounds for affine word transporters

This note records the coordinator's separate rational-arithmetic kernel for
the [measure classification](../machinery/phase7/CRITICAL_AFFINE_OVERLAPS.md).
Write a positive-gap word in composition order as
\[
A_w(z)=\alpha_wz+\beta_w,\qquad
\alpha_w=3^{|w|}/2^{S_w},\quad S_w=\sum_{e\in w}e,\quad
A_e(z)=(1+3z)/2^e.
\]
Every nonempty word has positive offset and exact reduced dyadic denominator:
\[
                         v_2(\beta_w)=-S_w.                 \tag{1}
\]
Induction proves this directly. A nonempty tail has negative valuation, so
the two summands in \(1+3\beta_{\rm tail}\) have different valuations and
cannot cancel. The one-letter case starts the induction.

Let \(L=2^a3^b\), for integers \(a,b\). If the full slopes of \(u[e]\) and
\(L A_{v[f]}\) agree, their last-letter offsets cancel:
\[
 \beta_{u[e]}-L\beta_{v[f]}=\beta_u-L\beta_v.                 \tag{2}
\]
Suppose this difference is a nonzero rational \(c\), with \(e\ne f\).
Comparing full slopes gives \(f-e=a+S_u-S_v\ne0\). Thus the two nonempty
prefix contributions in (2) have different valuations. Equation (1),
including either empty-prefix case, gives
\[
 S_u\le\max(0,-v_2(c)),\qquad
 S_v\le\max(0,-v_2(c)+a).                                  \tag{3}
\]
There are finitely many positive-gap prefixes in this box. The remaining
last-gap relation is summed geometrically in the measure-classification
note. This arithmetic step is independent of regularity or orbit hypotheses.

These identities also prove that the rational maps form a free monoid.
Equal offsets give equal total gap budgets by (1), with positivity handling
the empty word. For two nonempty words having equal slopes and offsets,
(2) makes their shorter prefix offsets equal. Their prefix budgets agree,
so equality of the full slope valuations forces their last letters to
agree. Cancel the last letter and induct. Equal affine maps therefore have
exactly the same positive-gap word. This supplies the cancellation used
to prove prefix-freeness of reduced matching target cylinders.

[AffineTransporter.lean](AffineTransporter.lean) formalizes (1), (2), (3),
empty prefixes, freeness, and the passage from a full match with unequal
last letters to the finite box. It does not formalize the entropy formula,
almost-sure gap recovery, or the measure classification. The separately
audited [counted-fusion kernel](../machinery/phase7/FusionSteering.lean)
handles the actual positive-integer part of that written proof.
