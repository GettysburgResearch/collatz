# The critical source budget at the minimum of the original component

**Proposed application with a source-qualified stronger form.** Let
\(m\ge2\) be the least positive ordinary member of a nongood component,
either cyclic or escaping. Thus every forward state of every ordinary
\(Y\) in that component is at least \(m\). Let \(X\ge2\) be in this
component and suppose \(3X-1\) reaches 1. Consider physical equal-clock,
equal-grade returns \((Y,3Y-1)\to(X,3X-1)\), of multiplier
\(M=3^p/2^H\), with no grade, rank or clock cutoff. For \(N\ge m\) put
\[
 F_1(X;N)=\sum_{\substack{Y\ {\rm thus\ reaching}\ X\\Y\le N}}
                 \frac{M}{X}.
\]
Every contributing \(Y\) belongs to the same **original** lower
component, so \(Y\ge m\). The upper target \(3X-1\ge5\) is transient
and can occur only once in the upper forward trajectory of a fixed
\(Y\). Each \(Y\) therefore contributes at most once, even when the
lower arm undergoes repeated laps. Its summand is at most \(1/Y\)
by \(X=M Y D,\ D\ge1\).

Write \(\alpha=\log_3 2,\ \theta=H_2(\alpha)\). The published-input
form is
\[
 F_1(X;N)\ll
   e^{C\sqrt{\log(2m)}}m^{-g}\,[1+\log(N/m)],
 \qquad g=1-\theta+1/351 .                                      \tag{1}
\]
In particular the sum is \(o(1)\), uniformly as \(m\to\infty\), at
every \(N\le\exp(m^{g-\epsilon})\), for fixed \(0<\epsilon<g\).
The elementary, finite-clock proof below gives for every
\(0<\sigma<1-\theta\) the independent version
\[
 F_1(X;N)\ll_\sigma (1+\log N)^3 m^{-\sigma},
 \qquad \log(2N)\le m .                                          \tag{2}
\]
Neither assertion supplies many actual paired ancestors of a
specified \(X\) near the original floor. The term from the empty
word, when included, is \(1/X\).

## Published first-landing input

Use the exact window form of [Paper 102/v1, Theorem 1](https://rstation.ai/problems/collatz/papers/102/v1),
as recorded in the [pinned whole-ray packet](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-multiple-attacks-20261125/synthesis/README.md).
For odd starts uniformly sampled in \((W/4,W]\), \(W\ge4L\), the
fraction never making an odd landing \(\le L\) is at most
\(C\exp(C\sqrt{\log L})L^{-g}\). Its imported analytic dependencies
are retained; the exponent and window estimate are prior work.

In each octave \(Z\le Y<2Z\), \(Z\ge m\), group the original sources
by \(v=v_2(Y)\), so the odd part \(w=Y/2^v\ge m\). It too never
lands below \(m\). Its group lies in a window \((W/4,W]\) with
\(W=\lceil2Z/2^v\rceil\ge m\) whenever nonempty. For \(m\) large,
take \(L=\lfloor m/8\rfloor\). This gives
\(O((Z/2^v)e^{C\sqrt{\log m}}m^{-g})\) surviving odds in the
group. Sum the geometric factors in \(v\), and weight the octave
by \(1/Z\). There are \(O(1+\log(N/m))\) octaves. Adjusting the
constant for small \(m\) proves (1). This is an all-height
consequence of the first-landing input, with no change of order of
limits. The related [PR193 first-hit trace bound](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/boundary/TRACE_PROFILE.md)
controls each first-hit odd-depth layer at a target missing all
small forward paths, including sources of unbounded height, using
further predecessor-density inputs. Here critical paired mass is
summed over all depths and truncated by ordinary source height.

## Standalone finite-clock calculation

Fix \(0<\sigma<1-\theta\). Choose \(\beta\in(1/2,\alpha)\)
sufficiently close to \(\alpha\) that
\(\sigma'=1-H_2(\beta)>\sigma\), and fix
\(\beta\log_2 3<\lambda<1\). For large \(Z\ge m\) let
\(U_0=2Z\), \(U_{j+1}=U_j^\lambda\). Test stages with \(U_j\ge m\).
The sum of their budgets \(h_j=\lfloor\log_2 U_j\rfloor\) is at
most \(D_\lambda\log(2Z)=:H\). A survivor here need only stay
at or above \(m\) for these first \(\lceil H\rceil\) shortcut
clocks.

At stage zero use the original \(Y\in[Z,2Z)\). For later stages
use its first entrance \(\le U_j\), with starting value \(v\) in
\((U_j/2,U_j]\), since one step reduces height by at most two.
The first descent threshold \(U_1<Z\) for large \(Z\), so
these later entrances start below the original octave.
Let \(q_j\) be the number of odd steps of the next \(h_j\)-clock
block at this \(v\). If \(q_j\le\beta h_j\) then the exact affine
formula yields
\[
  T^{h_j}v\le 3^{q_j}(2^{-h_j}v+1/3)
        \le (7/3)U_j^{\beta\log_2 3}<U_{j+1}.
\]
For the first inequality, write the additive part divided by \(3^{q_j}\)
as a sum over odd step indices \(i\), each term
\(2^{i-h_j}3^{-q_{i+1}}\le 2^{i-h_j}/3\). Inductively timely stage
success gives a first entrance to every next threshold within the
cumulative budgets, eventually reaching below \(m\). At the first
failure for a surviving source, all prior thresholds have been
reached on time and the native \(h_j\)-word at \(v\le U_j\) has more
than \(\beta h_j\) odds. Parity-word coding on a complete binary
period then bounds the number of such \(v\)'s by
\(O_\beta(U_j^{1-\sigma'})\): the range has a bounded number of
periods of length \(2^{h_j}\).

Consider a later stage and fix its clock \(t\le H\) and exact \(v\).
If \(p\) is the odd grade up to this first entrance, each prior
departing state exceeds \(U_j\). Consequently
\[
  v=3^p 2^{-t}Y D,\qquad 1\le D\le\exp(t/(3U_j)).
\]
In the indicated range \(\log(2Z)\le m+O(1)\),
\(t/U_j=O_\lambda(1)\). For fixed \(t,v\) and the octave of \(Y\)
there are \(O_\lambda(1)\) possible integers \(p\), from separation
by a factor of three. For each, the possible \(Y\)'s form a subset
of one real interval of length
\(O_\lambda(Zt/U_j)\); adding its endpoint costs
\(O_\lambda(Z(1+t)/U_j)\) since \(U_j\le2Z\). Summing over \(t\le H\)
and bad \(v\) bounds the original-source count at this stage by
\(O_\lambda(Z(1+\log Z)^2U_j^{-\sigma'})\). Direct grid counting gives
the same bound at the initial stage. The tested thresholds have
\(\sum_{j:U_j\ge m}U_j^{-\sigma'}\ll_{\lambda,\sigma'}m^{-\sigma'}\),
by geometric growth of their logarithms when read backwards.
Thus the whole surviving octave has size
\(O_\sigma(Z(1+\log Z)^2m^{-\sigma})\). Sum its reciprocal weights
over the octaves to obtain (2). Bounded \(m\) is harmless after
increasing constants.

This uses the stopped-source reconstruction already employed in
[the scalar first-passage proof](../../astra-literature-closure-20261125/source/README.md).
The calculation isolates its elementary critical-frequency exponent
and fixed minimum dependence. It asserts neither a power saving in
unbounded \(N\) at fixed \(m\) nor positivity of the needed paired
mass near a hypothetical least bad source.
