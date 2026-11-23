# Target-aware band remainder: exact lifting and the unpaid continuation

**Status: the global closing step was not proved.** This attack combined the new unrestricted finite source optimizer with the mandatory dyadic band, then tried to transfer the smaller binary remainder's complete trajectory to the original target. It gives exact lifting through the full shared binary horizon and an all-parameter control against stopping at the common binary horizon. It does not give a new descent estimate beyond that horizon or a proof of Collatz.

The source optimizer is PR177 at `6de3e304bb49a93a6c5ef0e5563137e75c7defb4`, `HIGH_VARIANCE_WITNESS.md`; the unlimited cheap-prefix construction is PR180 at `04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`, `GLOBAL_SOURCE_SYNTHESIS.md`. The supplied source, original target, complete source grade, and actual ordinary clocks are retained. The exact pins are in [SOURCES.json](SOURCES.json); the original band and lifting pins are retained in [the source ledger](../../../../reports/2026-11-23-integer-boundary/band-source-pins.json).

## 1. Why the next attempt has to involve the target

For the original target `t=2B+1`, PR177's finite graph contains every complete capturing source that can be optimal: an even source `S` with `B<=S<2B`, whose entire positive-time trajectory lies below `B`. Thus a search over longer alternative words or more simultaneous edits cannot evade its complete minimum. PR180's whole low-gap clusters likewise already permit arbitrary replacement length.

The global construction attempted here therefore moves with the actual target orbit. Let `q=T^k(t)` be an actual mandatory-band visit, and write

\[
q=2^a+r,\qquad 0<r<2^a,\qquad
(a+1)r\le70\,2^a.                                      \tag{1}
\]

The idea was to use the smaller ordinary remainder `r`, not a free symbolic parity word. The old high-bit lifting identities already justify the arithmetic below; this note does not claim their discovery.

## 2. What the entire shared prefix really supplies

Write `r_j=T^j(r)` and `q_j=T^j(q)`. Let `o_j` count the odd inputs among `r_0,...,r_(j-1)`. For every `0<=j<=a`,

\[
\boxed{q_j=r_j+2^{a-j}3^{o_j}.}                          \tag{2}
\]

For `j<a`, the difference on the right is even, so the two actual states have the same parity. Taking that common branch proves (2) by induction. In particular,

\[
q_a=r_a+3^{o_a}.                                        \tag{3}
\]

The right side of (2) is an ordinary integer at every stated clock. The proof does not apply the remainder's word illegally after the matching horizon. At clock `a` the difference is odd, so the next two parities are opposite.

**Descent transfer within the horizon.** If `1<=j<=a` and `r_j<r`, then `q_j<q`. To see this, write the common affine prefix as

\[
T^j(x)=\lambda_j x+b_j,\qquad
\lambda_j=3^{o_j}/2^j>0,\quad b_j\ge0.
\]

The strict decrease at `r` forces `lambda_j<1`; hence

\[
q_j=r_j+\lambda_j2^a<r+2^a=q.                           \tag{4}
\]

Equivalently, failure of `q` to descend through the whole horizon forces failure of the actual smaller remainder to descend through that same horizon. The converse is not asserted: a larger source in the same parity cylinder can descend even when its smallest representative does not.

## 3. Three different resources must not be conflated

Suppose `t` is the least positive integer outside the basin of one. A later marked state `q=T^k(t)` need not equal `t`.

First, `r<q` in (1) does not establish `r<t`, and therefore does not license the least-target convergence hypothesis. The existing band-entrance theorem bounds `log q` by `O((log t)^4.117)`. It does not provide the sufficient value comparison

\[
q\le\frac{a+71}{70}\,t
\quad\Longrightarrow\quad
r\le\frac{70q}{a+71}\le t.                             \tag{5}
\]

The harmless endpoint equality in (5) can be made strict when needed. A polylogarithmic entrance **clock** is not this approximately logarithmic factor bound on the entrance **value**.

Second, even if `r<t` and its complete convergence certificate is available, the certificate's descent or completion clock need not fit inside `a`. A complete certificate alone does not extend (2) past the point where the actual parities split.

Third, at a later visit, descent of `q` is not yet descent below the unchanged original floor `t`. The exact saving needed for a smaller original-target partner is

\[
\boxed{r_j+2^{a-j}3^{o_j}<t.}                           \tag{6}
\]

Equation (4) supplies only a bound by `q`. Resetting the induction reference to `q` would discard the original least-target resource. If the least bad integer itself were marked, then `q=t` and the first and third distinctions disappear, but mandatory visitation does not establish that stronger starting condition.

## 4. An all-parameter band family outlasting the whole binary horizon

The matching horizon cannot be paid for by the band width alone, even if the band is narrowed to an exponentially small relative width.

For every integer `k>=2`, put

\[
a=3k,\qquad h=2k+1,\qquad
r=2^h-1,\qquad q=2^a+2^h-1.                            \tag{7}
\]

Then `q` is an odd integer of binary height `a`, and

\[
(a+1)(q-2^a)\le4\,2^a<70\,2^a.                        \tag{8}
\]

Indeed `(3k+1)<=2^(k+1)` for `k>=1`, by elementary induction, so
`(3k+1)2^(2k+1)<=4*2^(3k)`. The relative excess is less than `2^(1-k)`.

Nevertheless,

\[
\boxed{T^j(q)>q\quad\text{for every }1\le j\le a.}     \tag{9}
\]

For the first `h` clocks, divisibility of `q+1` by `2^h` gives the exact odd-run formula

\[
T^j(q)=(3/2)^j(q+1)-1>q\quad(1\le j\le h),
\]

and

\[
T^h(q)=3^h(2^{k-1}+1)-1.                               \tag{10}
\]

Every positive shortcut step satisfies `T(x)>=x/2`. Therefore for `h<=j<=a`,

\[
T^j(q)\ge\frac{T^h(q)}{2^{a-h}}
 =3^h+\frac{3^h-1}{2^{k-1}}>3^h.                        \tag{11}
\]

Finally `3^(2k+1)>2^(3k)+2^(2k+1)>q` for `k>=2`. It holds at `k=2`; the left side grows by factor nine at the next step, while the sum on the right grows by less than factor eight. Equations (10)--(11) prove (9), with no assumption on the intervening parities after the initial odd run.

This family has only a leading binary one and a lower block of ones. Its remainder is of order `q^(2/3)`, substantially smaller than the upper bound of order `q/log q` in (1). The control does not assert that the family diverges, that all its remainders converge, or that its inputs satisfy a joint bad query. It refutes only the proposed inference from mandatory-band geometry to descent by the entire common-bit horizon. A few convergent examples are checked separately, without extrapolating their convergence to the family.

The older `INVERSE_ODD_BUDGET.md` already gives marked inputs with any prescribed fixed initial-ascent and odd-surplus budgets. The specific point of (7)--(11) is that the failed deadline is the input's **entire binary matching horizon**, growing as its binary height, while its relative distance to a power of two tends exponentially to zero. No novelty claim is made for the general phenomenon of long initial ascents.

## 5. The missing global construction

The finite boundary optimizer remains useful for verifying a proposed cheaper complete source. It supplies no certificate grade for an unconstructed continuation of (3). The complete remainder trajectory supplies genuine arithmetic data, but after clock `a` the two parity histories diverge. To finish this route one must construct a later ordinary merger or a lower-grade complete source, retaining both the original target comparison (6) and the entire source grade. Neither a copied remainder tail nor a normalized affine shadow provides that construction.

This continuation obtained no such target-aware surgery. The positive content of the current repository remains the exact finite optimizer and the already proved mandatory-band entrance. The new material here is a directly checked diagnosis of the proposed combination, not an advance on the missing universal return estimate. No new Lean declaration is claimed.

Reproduction: `python -X utf8 -B check_band_remainder.py`; the checker uses exact integers and explicitly raises on failure. The parameterized proof above is separate from its finite executable controls.
