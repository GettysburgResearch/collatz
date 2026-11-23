# A strict collision-exponent gap for every ordinary stationary limit

Date: 2026-11-23.

**Status: new written original-source deductions, with a separately checked
Lean sequence core. Escape exclusion remains open.** The main result is a
strict, process-dependent improvement of the critical collision exponent for
every fixed weak limit of the actual ordinary time laws. It uses stationarity,
which the finite critical-budget count does not use. It does not assume that a
Rényi entropy rate exists. It also identifies the moving inverse laws with
the ordinary time laws in total variation, uniformly over the inverse clock.

This changes one possible closing target: for an actual fixed time-limit law,
an upper bound with the critical exponent and **any subexponential loss** would
contradict the new lower bound. No such upper bound is proved here. Section 8
tests whether the latest arithmetic pressure estimate supplies it, without
interchanging time and resolution limits.

## 1. Frozen inputs and the actual source

The new argument uses the following exact checkpoints.

| Input | Head and file |
|---|---|
| Critical collision budget | PR185, `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`, `research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md` |
| Ordinary inverse law | Same PR185 head, `research/rigidity-closing-20261122/SAME_SOURCE_INVERSE_ENTROPY.md` |
| Ordinary pressure atoms and their exact weights | PR177, `6de3e304bb49a93a6c5ef0e5563137e75c7defb4`, `research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md` |
| Fresh arithmetic off-diagonal upper bound | PR178, `4e204f54136c79cf8c9393b34e3330594f99ae0a`, `research/global-closure-20261123/escape/PRESSURE_COLLISION_ATTACK.md` |
| One ordinary pressure maximum in both directions | PR182, `b78819e95ee7d39f02022de991b42217821e7590`, `research/closure-round2-20261123/SOURCE_CLOSURE.md` |
| Full ordinary loss-measure summation | Same PR182 head, `research/closure-round2-20261123/ESCAPE_CLOSURE.md` |
| Latest actual real-boundary regularity and its precise collision boundary | PR180, `fcdcdbadc6172e414f7282442a8a6b85587d7e70`, `research/source-clock-20261123/{EXTENSIONS,COLLISION_TRANSFER}.md` |

Let one positive ordinary odd unit have an escaping accelerated orbit

\[
q_j=U^j(q_0),\qquad U(n)=\frac{3n+1}{2^{v_2(3n+1)}},\qquad
g_j=v_2(3q_{j-1}+1)\quad(j\ge1).
\]

All the states are distinct. Put

\[
\ell=\log_2 3,\quad
A_M=\sum_{j=1}^M g_j,\quad
\Phi(b)=b\log b-(b-1)\log(b-1),\quad
\theta=\Phi(\ell)/\log3.
\tag{1}
\]

All logarithms other than `log_2` are natural. The actual physical telescope
and distinctness imply

\[
A_M=M\ell+\log_2(q_0/q_M)
 +\sum_{j<M}\log_2(1+1/(3q_j))
\le M\ell+O_{q_0}(\log(M+1)).
\tag{2}
\]

The stronger reciprocal estimate in PR177 is not needed for (2).

The ordinary time law is

\[
\pi_M=\frac1{M+1}\sum_{j=0}^M\delta_{q_j}.
\tag{3}
\]

We first regard it as a measure on the actual positive integers and then
push it to `Z_3^times`. No Haar, geometric, or stationary law is substituted
for its finite source distribution.

## 2. Every inverse clock has the same time limits

Retain the source-qualified bounded positive harmonic flow from PR185:

\[
\nu(q)=\sum_{Un=q}\nu(n),\quad
v_j=\nu(q_j)\uparrow C\in(0,\infty),\quad
K(q,n)=\mathbf1_{Un=q}\frac{\nu(n)}{\nu(q)}.
\]

For every finite `r>=0`, its moving-root endpoint law is

\[
\zeta_{M,r}=\frac1{M+1}\sum_{j=0}^M K^r(q_{r+j},\cdot).
\tag{4}
\]

Ordinary endpoint uniqueness gives the exact retained atoms

\[
\zeta_{M,r}(\{q_j\})=\frac{v_j}{(M+1)v_{r+j}}\le\frac1{M+1}.
\tag{5}
\]

Here and below total variation means `sup_A |mu(A)-nu(A)|`, equivalently
half the `l1` distance for probabilities. Because `pi_M` is supported on
the distinct `q_j` and every one of its atom masses dominates (5), its
common mass with `zeta_(M,r)` is exactly the sum of (5). Consequently

\[
\boxed{
\|\zeta_{M,r}-\pi_M\|_{\rm TV}
=1-\frac1{M+1}\sum_{j=0}^M\frac{v_j}{v_{r+j}}
\le\frac1{M+1}\sum_{j=0}^M(1-v_j/C)=:\varepsilon_M\longrightarrow0.}
\tag{6}
\]

This is uniform over every finite inverse clock. In fact the supremum over
`r` equals the displayed upper bound, by first holding `M` fixed and letting
`r` tend to infinity. Pushforward to ternary residues only decreases total
variation. Thus **arbitrary choices `r=r_M` have exactly the same ternary
subsequential weak limits as the unchanged ordinary time law**.

This conclusion retains the harmonic-flow qualifications in its pinned
construction. The conclusions below for `pi_M` itself require no such flow.

## 3. Extracting a stationary backward-gap law from that source

For `1<=m<=M`, let `P_(M,m)` be the empirical law of the actual reversed
past windows

\[
(g_j,g_{j-1},\ldots,g_{j-m+1}),\qquad m\le j\le M,
\]

with uniform endpoint `j`. Its length is `L=M-m+1`. Each actual gap occurs
at most `m` times, so

\[
\mathbb E_{P_{M,m}}\sum_{i=1}^m G_i\le \frac{mA_M}{M-m+1}.
\tag{7}
\]

Fix any ternary weak-limit subsequence of `pi_M`. For each fixed `m`,
(2) and (7) make the word laws tight on the countable discrete set of
positive `m`-tuples: the set with total gap at most `R` is finite, and
its omitted mass is at most a constant times `m/R`. Extract a further
diagonal subsequence on which every `P_(M,m)` converges in total variation
to a probability `P_m`. Tightness is needed here; pointwise convergence
alone would not preserve total mass.

Deleting either the first or the last coordinate of an empirical
`(m+1)`-word changes the sampling interval by only its boundary endpoints.
The total-variation error tends to zero. Hence the `P_m` are consistent
under both deletions. Kolmogorov extension gives a stationary process

\[
\eta\quad\text{on}\quad\{1,2,3,\ldots\}^{\mathbb N},\qquad
\mathbb E_\eta G_1\le\ell.
\tag{8}
\]

The expectation bound follows by passing first the bounded truncated
cost to the limit and then increasing the truncation. It is an inequality;
uniform integrability of the original gap costs is not asserted.

Iterating the actual odd recurrence gives, for every retained window,

\[
q_j\equiv\Pi_m(g_j,\ldots,g_{j-m+1})\pmod{3^m},\qquad
\Pi_m(w)=\sum_{i=1}^m3^{i-1}2^{-(w_1+\cdots+w_i)}\pmod{3^m}.
\tag{9}
\]

The omitted initial endpoints carry at most `m/(M+1)` of (3). Therefore
the already chosen weak limit `mu` satisfies

\[
\mu\bmod3^m=(\Pi_m)_*P_m\quad\text{for every }m.
\tag{10}
\]

Equivalently it is the ternary series factor of the stationary backward
gap process. The series converges ternarily for every gap sequence. No real
convergence of that series is used or claimed. Every weak limit of (3),
and by (6) every weak limit of (4), has such a lift.

## 4. Stationarity forces a strict collision-exponent gap

Write

\[
H_m=-\sum_wP_m(w)\log P_m(w),\quad
C_m=\sum_wP_m(w)^2,\quad R_m=-\log C_m.
\]

At mean `b>1`, the positive-integer geometric distribution

\[
\gamma_b(k)=b^{-1}(1-b^{-1})^{k-1}\quad(k\ge1)
\tag{11}
\]

has entropy `Phi(b)`. Gibbs' inequality against `gamma_ell` gives

\[
H_1\le\Phi(\ell),\qquad
H_m\le m\Phi(\ell),\qquad
H_{a+b}\le H_a+H_b.
\tag{12}
\]

All these entropies are finite. The last inequality is the block entropy
chain rule plus stationarity. Jensen's inequality also gives `R_m<=H_m`.

There are two exhaustive cases.

### A. A finite block has a Shannon deficit

Suppose for some fixed `k>=1`,

\[
D_k=k\Phi(\ell)-H_k>0.
\]

Partition a length-`m` word into blocks of length `k` and one remainder.
The exact subadditive bound is

\[
H_m\le\lfloor m/k\rfloor H_k+(m\bmod k)\Phi(\ell)
     =m\Phi(\ell)-\lfloor m/k\rfloor D_k.
\]

Consequently

\[
\boxed{C_m\ge
 \exp[-m\Phi(\ell)+\lfloor m/k\rfloor D_k].}
\tag{13}
\]

For `m>=2k`, one can take the fixed exponent improvement
`D_k/(2k)>0`. This uses a single finite block deficit, not an assumed
limit of `R_m/m`.

### B. There is no finite-block Shannon deficit

Then `H_m=m Phi(ell)` for every `m`. For a block law with total mean at
most `m ell`, its relative entropy against `gamma_ell^tensor m` is

\[
D(P_m\Vert\gamma_\ell^{\otimes m})
=m\log\ell+(\mathbb E\textstyle\sum_iG_i-m)
   \log\frac\ell{\ell-1}-H_m\le0.
\]

Relative entropy is nonnegative, and equality occurs only for identical
probability laws. Thus every block is exactly the geometric iid law.
Its collision sum is explicitly

\[
\boxed{C_m=\left(\sum_{k\ge1}\gamma_\ell(k)^2\right)^m
=(2\ell-1)^{-m}.}
\tag{14}
\]

The geometric distribution is nonuniform, so strict Jensen gives

\[
\log(2\ell-1)<\Phi(\ell).
\tag{15}
\]

This completes the equality case rather than incorrectly assuming that
maximum Shannon entropy also gives maximum Rényi-2 rate.

### Actual ternary consequence

Grouping word masses by the arithmetic map (9) only increases the sum
of squares. From (10), (13), and (14), **every fixed actual weak limit**
has constants `epsilon_mu>0` and `m_mu` such that

\[
\boxed{\operatorname{Col}_{3^m}(\mu)
\ge\exp[-(\Phi(\ell)-\epsilon_\mu)m]
\quad(m\ge m_\mu).}
\tag{16}
\]

In particular its upper Rényi-2 dimension satisfies the strict inequality

\[
\boxed{
\limsup_{m\to\infty}
 \frac{-\log\operatorname{Col}_{3^m}(\mu)}{m\log3}
<\theta.}
\tag{17}
\]

This is a statement about the original source's ternary time-limit laws.
The auxiliary geometric law appears only in the rigorously forced equality
case of an entropy inequality. It never replaces the actual finite law.

## 5. A finite-window strengthening in the deficit case

There is a useful quantitative continuation of case A. For `1<=k<=m<=M`,
every `k`-coordinate consecutive subblock of the sampled `m`-word has an
endpoint interval of length `M-m+1` contained in the full `k`-word interval
of length `M-k+1`. If `Q` is its law and `P=P_(M,k)`, then

`P=rho Q+(1-rho)Q'`, where `rho=(M-m+1)/(M-k+1)`.

Entropy concavity and nonnegativity give `H(Q)<=H(P)/rho`. Partition
the `m`-word into `k`-blocks and a remainder; the latter is a projection
of a consecutive `k`-block within the same word. The entropy chain rule
therefore gives the exact finite inequality

\[
\boxed{H(P_{M,m})\le
\lceil m/k\rceil\frac{M-k+1}{M-m+1}\,H(P_{M,k}).}
\tag{18}
\]

For each fixed `k`, the entropy `H(P_(M,k))` converges to `H_k` along
the chosen subsequence. Here is the needed tail argument, rather than an
unsupported entropy-continuity assertion on a countable alphabet. Put
`c(w)=sum_i w_i`; its mean is uniformly bounded by (7). For the tail
`c(w)>R` of mass `delta`, compare its conditional probability with
`exp(-t c(w))/Z_k(t)`, where `t>0` and `Z_k(t)<infinity`. Gibbs' inequality
gives the upper bound

\[
-\sum_{c(w)>R}P(w)\log P(w)
\le tC+\delta\log Z_k(t)-\delta\log\delta,
\qquad \delta\le C/R.
\]

Choose `t` small first and then `R` large. This makes the entropy tails
uniformly small; convergence on the finite complement proves the assertion.

If case A holds, (18) consequently gives, along that same source subsequence,
an exponent improvement at every growing resolution `m=o(M)`, including
`m=O(log M)`. The factor `(M-m+1)/(M+1)` from omitted endpoints is still
retained when passing to collisions of `pi_M`; (5) gives the corresponding
lower bound for every inverse clock. Case B alone does **not** give this
finite-window conclusion at arbitrary moving resolutions. Long correlations
can disappear in fixed-block limits, so the two orders of limits remain
distinct.

## 6. The improvement is process-dependent

No uniform positive gap over all stationary mean-constrained gap processes
is claimed. This limitation is substantive. Choose a large block length
`N` and a finite constant-composition type class `W_N` whose single-letter
frequencies approximate the mean-`ell` geometric distribution from below.
Concatenate independent uniform words from `W_N` and choose the phase
uniformly among the `N` positions. This is a stationary positive-gap process
with mean at most `ell`.

Its Rényi-2 rate is `log|W_N|/N`: conditioning on the phases leaves all
complete independent blocks with probability at most `|W_N|^-1`, while
equal phases and matching blocks give the reverse exponential bound.
The at most two boundary blocks and the factor `1/N` do not affect the rate.
Type counting permits `log|W_N|/N` to approach `Phi(ell)`. Every fixed
process has a strict deficit, consistently with (17), but the deficits can
approach zero. This is a stationary-process model, not a Collatz orbit.
It establishes sharpness of the entropy comparison over stationary gap
processes; it does not establish the same sharpness for their ternary factors,
where grouping can further increase collisions.

## 7. The exact new closing target and limit order

For a subsequence `M_i` producing `mu`, and arbitrary finite `r_i`, (6)
implies for every fixed `m`

\[
\operatorname{Col}_{3^m}(\zeta_{M_i,r_i})
\longrightarrow\operatorname{Col}_{3^m}(\mu).
\tag{19}
\]

An upper bound on this **same limit** of the form

\[
\operatorname{Col}_{3^m}(\mu)
\le\exp[o(m)]\,3^{-\theta m}
\tag{20}
\]

would contradict (16). Equivalently, it would suffice to show that one
actual time-limit law has lower Rényi-2 dimension at least `theta`.
This is weaker in its allowed loss than the previous finite critical
comparison with `sqrt(m) 3^(-theta*m)`.

There is no supplied modulus in (19). Thus the existence of a good fixed
time limit does not permit choosing `m` comparable to `log M_i`, or any
other specific growing resolution, except where the additional finite-block
deficit argument in Section 5 applies. The proof takes the time limit first,
then the resolution limit in (16)--(20).

## 8. Testing the latest pressure upper bound against this target

The fresh PR178 estimate for the actual canonical component pressure
measure `mu_s=sum_(n in E) r_E(n)^s delta_n`, `s>1`, is

\[
\mathcal O_Q(\mu_s)\le2\zeta(s)^2Q^{-s}.
\]

Its sharper one-density transfer to the actual moving law reads

\[
\mathcal O_Q(\zeta_{M,r})
\le\frac{2\zeta(s)}{S_s}D_{M,r}Q^{-s},\qquad
D_{M,r}=\left\|\frac{d\zeta_{M,r}}{d(\mu_s/S_s)}\right\|_\infty.
\tag{21}
\]

The retained ordinary atoms force

\[
D_{M,r}\ge\frac{c_0 S_s}{M+1}H_M^s,
\qquad H_M=\max_{j\le M}q_j.
\tag{22}
\]

At a fixed `Q`, the critical height theorem in PR185 makes the right
side of (21) necessarily grow like at least
`(M+1)^(s/theta-1)` times a positive logarithmic factor, for every fixed
`s>1`. It therefore does not pass to the time limit (19) as a finite
upper bound. Adapting `s` does not repair this: the exact cancellation of
`S_s` leaves at least `2*c_0*H_M/((M+1)*Q)` once `H_M>=Q`, uniformly
for all `s>1`, and this still grows by the same height theorem.

Choosing `Q` to grow with `M` can reduce that estimate, but does not prove
(20): (19) supplies no compatible upper bound on the time needed for
convergence at resolution `Q`. The original source mass is asymptotically
one by (6), so increasing the inverse clock cannot remove this issue.
The new process-dependent exponent gap can absorb subexponential losses
**after a valid same-limit upper estimate is obtained**. It does not turn
an unbounded fixed-resolution density comparison into such an estimate.

This was the first direct attempted consumer of the new gap. A nonuniform
bilinear arithmetic estimate for the actual endpoint pairs, or a direct
same-limit regularity theorem, remains the first unproved closing step.
The positive real-boundary entropy and upper local dimension in PR180
are on a different marginal; its explicit collision model prevents their
automatic substitution for (20).

## 9. A second closing target: a finite real realization of the same series

There is a direct alternative to the Rényi upper bound. Suppose the **same**
stationary gap process in (8) had a finite positive real series

\[
R=\sum_{i\ge1}3^{i-1}2^{-(G_1+\cdots+G_i)}<\infty
\quad\text{almost surely}.
\tag{23}
\]

This condition would already contradict its actual mean bound. Here is an
elementary proof with the integrability issue retained. Let `S` denote the
left shift. The positive series obeys

\[
R=2^{-G_1}(1+3R\circ S),\qquad R\ge2^{-G_1},
\]

and hence

\[
G_1\log2-\log3
=\log(R\circ S)-\log R
 +\log\!\left(1+\frac1{3R\circ S}\right).
\tag{24}
\]

The positive correction is integrable: the second inequality gives

`log(1+1/(3R)) <= G_1 log2 + log(4/3)`.

Thus the logarithmic coboundary in (24) is integrable, even though
`log R` itself need not be integrable. Let `clip_N` clip a real number to
`[-N,N]`. Stationarity gives zero mean to
`clip_N(log(R o S))-clip_N(log R)`. These differences converge pointwise
to the coboundary and are bounded in absolute value by its absolute value,
because clipping is 1-Lipschitz. Dominated convergence therefore proves
that the coboundary has mean zero. Integrating (24) now yields the strict
identity

\[
\boxed{
\mathbb E G_1\log2-\log3
=\mathbb E\log\!\left(1+\frac1{3R}\right)>0,}
\tag{25}
\]

contradicting (8). No independence, ergodicity, or finite expectation of
`log R` was assumed.

One concrete sufficient condition for (23) would be tightness, uniformly in
`m`, of the **actual limiting real partial sums** `Pi_m` in (9), evaluated
as positive real rational numbers before reduction modulo `3^m`. The sums
increase with `m`; uniform tightness would make their increasing limit
finite almost surely. The ternary convergence in (10) alone supplies no
such real tightness. Likewise, the fixed whole-component real boundary in
PR180 includes root-dependent affine routing; identifying its marginal with
(23) requires precisely that missing control. A different real probability
law cannot be inserted into (24).

This gives another explicit first unproved step, and tests it against the
actual mean constraint. It is not asserted that the real tightness condition
holds for an escaping source.

## 10. Formalization boundary

`lean/StationaryCollisionGap.lean` proves four reusable statements:

1. subadditive blocking at an arbitrary block size;
2. the exact all-length deficit with the quotient floor retained;
3. a positive eventual exponent improvement from one strict block deficit;
4. the exhaustive deficit-or-rigidity argument yielding an eventual strict
   rate bound without assuming convergence of the Rényi rate.

The entropy comparisons, equality characterization, extraction of a
stationary original-source law, arithmetic coding, and total-variation
identity are the written proofs above. They are not hidden global hypotheses
or asserted to be formalized by the generic sequence core. This note proves
no Collatz convergence or escape-exclusion theorem.
