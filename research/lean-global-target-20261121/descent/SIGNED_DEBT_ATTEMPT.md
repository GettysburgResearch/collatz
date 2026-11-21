# Signed debt, carrying, and the source certificate resource

This is a new normalization attempt following the arbitrary-budget correction
kernel. It did not produce a total transformer. The failure occurs at an
explicit carry block and then, when trying to charge that block to the source
certificate, at a precise use of the unknown closure statement.

## Exact state and update

Track an actual odd target alongside a known source certificate by

\[
y=Kx-c,
\]

allowing dyadic rational coefficients and signed debt. Initially
\(y=5x,\ K=5,\ c=0\). If the source and target take their exact next odd
steps with exponents \(a\) and \(b\), then

\[
x'=(3x+1)/2^a,\qquad y'=(3y+1)/2^b,
\]

and the exact update is

\[
\boxed{K'=K2^{a-b},\qquad c'=(3c+K-1)/2^b.}
\]

Every original source step consumes one letter of its supplied certificate.
The issue is what to do when the source reaches one while the target has not.

## A positive carry mechanism does exist

At source endpoint one, pad the source by its exponent-two loop. Put
\(u=c/K\). For a state with \(y=K-c>1\) and \(0\le u<1/2\), the update gives

\[
u'=\frac34u+\frac14-\frac1{4K}.
\]

As the target is odd and greater than one, \(K\ge y\ge3\). Therefore,
until a carry or target termination occurs,

\[
u'\ge\frac34u+\frac16.
\]

Starting at \(u\ge0\), this lower bound exceeds \(1/2\) after five steps:
\(\frac23(1-(3/4)^5)=781/1536>1/2\).
Thus a carry occurs within five odd steps unless the target reaches one first.
At that carry, replace

\[
(K,c)\longmapsto(K/2,c-K/2).
\]

The target is preserved, and the normalized debt returns below one half.
This supplies a total local reset operation on the stated region. It does
not make those resets descend.

## The first completed blocks that defeat a monotone scale/debt claim

For source \(x=5\), the source word is \((4)\). After one paired step the
source has reached one and the target is \(19=20-1\). Padding until the first
carry gives

| Target | Coefficient \(K\) | Debt \(c\) | Event |
| --- | ---: | ---: | --- |
| 19 | 20 | 1 | Source certificate exhausted |
| 29 | 40 | 11 | Target exponent one |
| 11 | 20 | 9 | Target exponent three |
| 17 | 40 | 23 | Target exponent one; carry due |
| 17 | 20 | 3 | Completed carry |

The scale is unchanged and the debt has increased. Even a strict decrease
of the lexicographic pair \((K,c)\) fails at this completed reset.

For source \(x=11\), the source word \((1,2,3,4)\) ends at one while the
target word prefix \((1,1,3,1)\) ends at \(71=80-9\). The first carry is

| Target | Coefficient \(K\) | Debt \(c\) | Event |
| --- | ---: | ---: | --- |
| 71 | 80 | 9 | Source certificate exhausted |
| 107 | 160 | 53 | Target exponent one |
| 161 | 320 | 159 | Target exponent one |
| 121 | 320 | 199 | Target exponent two; carry due |
| 121 | 160 | 39 | Completed carry |

Both scale and debt grow over the entire block. Consequently every positive
linear combination of these two coordinates also grows on this control.
This rejects this proposed well-founded resource, not signed correction
methods in general.

The exact rational traces are reproducible with
`python3 descent/signed_debt_attempt.py` from the enclosing research directory.
That script checks these finite controls and the algebraic invariants; it is
not a convergence proof or a wide computational verification campaign.

## Why a basic valuation resource is insufficient

An exponent-one step consumes one unit of \(v_2(y+1)\), which does provide
a finite ordinary resource for a consecutive all-one run. It is not
monotone across resets. For every odd \(h\ge3\), set

\[
n_h=\frac{2^{h+2}-5}{3}.
\]

Then \(n_h\) is a positive odd integer and

\[
3n_h+1=4(2^h-1),\qquad
v_2(n_h+1)=1,\qquad v_2((2^h-1)+1)=h.
\]

Thus one exact exponent-two step regenerates arbitrarily much of the
valuation resource. The first control is \(9\to7\), where the resource
increases from one to three. Any fixed positive weighting of this valuation
against log-height eventually increases on this family; omitting or
negatively weighting the valuation leaves exponent-one expansions increasing.
A successful integer resource needs more state or a different reset law.

## Attempt to pay for a reset with the finite source certificate

Before the source endpoint, the same binary carry would change the source:

\[
Kq-c=(K/2)(2q-1)-(c-K/2).
\]

To call the right-hand state a known-source state from the supplied
certificate for \(q\), one must establish

\[
\operatorname{Basin}(q)\Longrightarrow\operatorname{Basin}(2q-1).
\]

This is exactly the unknown psi closure in the pinned closure kernel. It
cannot be used as a free carry rule. This is the first circular step in the
proposed source-rank proof.

There is a valid alternative when \(q\equiv1\pmod3\): use the inverse
exchange

\[
q^*=\frac{4q-1}{3},\qquad
Kq-c=(3K/4)q^*-(c-K/4).
\]

For positive odd \(q\), the state \(q^*\) is an ordinary odd predecessor
with exact exponent two. Its basin membership follows from the supplied
certificate for \(q\). However, its certificate is formed by **prepending**
that exponent-two letter; its rank increases by one.

If the next paired step consumes the newly inserted head, the source returns
to \(q\), and the resulting coefficient/debt update is

\[
(K,c)\longmapsto
\left(\frac{3K}{2^b},\frac{3c-1}{2^b}\right).
\]

No letter of the original source suffix has been consumed. Repeating such
inverse-exchange loops therefore cannot be charged to the finite source
rank merely because each forward move consumes a letter. One must prove a
separate bound on the inserted letters or a secondary resource that falls
across these loops. The direct coefficient/debt candidate is already
defeated by the completed-block controls above. No successful replacement
resource was obtained in this pass.
