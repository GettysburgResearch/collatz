# Attacking the marked section through its small offset

This pass starts from PR173 at commit
`fa0c9e2a2851e6324391e39c17afcb5913185aec`. Its bounded forward-visit
theorem puts every positive ordinary orbit at an odd integer

\[
n=2^d+a,\qquad (d+1)a\le70\,2^d,
\]

where `d=floor(log2 n)`. The induced return map is total; the missing
assertion is eventual strict descent from every marked start above one.
The source's construction already proves that a single first return can
increase height by an arbitrarily large factor.
See the pinned [source README](sources/PR173_README.md),
[`ForwardSection.lean`](lean/vendor/ForwardSection.lean),
[`SectionDynamics.lean`](lean/vendor/SectionDynamics.lean), and
[`RisingReturns.lean`](lean/vendor/RisingReturns.lean).

The offset route now supplies an **unbounded explicit family of marked
inputs whose first positive marked return is strictly smaller**, with no
basin or ordinary-floor premise. A quantitative bridge makes this an
actual return-map result, not just ordinary prefix descent. The separate
rising family below defeats a proposed universal supply of the offset
rule. Its exact post-prefix state exposes a multiplication obligation
that has not been closed. Full coverage of marked inputs remains open.

## A proved first-return descent family

The general bridge uses

\[
H(m)=4\lfloor\sqrt m\rfloor+\lfloor\log_2m\rfloor.
\]

Every positive `m` has a marked visit before `H(m)`, and the elementary
ordinary bound is `T^j(m)<=2^j*m`. Therefore an actual endpoint
`T^t(n)=m>0` with

\[
2^{H(m)}m<n
\]

gives a smaller marked endpoint on the orbit of `n`. PR173's `captures`
theorem places this endpoint among its complete returns, so some
positive return iterate is smaller. This uses no convergence hypothesis
for `m`. A convenient entirely integral sufficient condition is

\[
2^d\le n,\qquad 6m<d.
\]

Indeed `H(m)<=5m`, `m<=2^m`, and hence
`2^H(m)*m<=2^(6m)<2^d<=n`. If every positive clock before `t` is even,
there cannot be a marked return before `t`. The same finite bound then
shows that the **first** positive return itself is smaller.

Here is an unconditional symbolic family satisfying all these conditions.
For every `r>=0`, put

\[
\begin{aligned}
d_r&=256\,4^r,\\
L_r&=128\,4^r-(r+1),\\
s_r&=2L_r=d_r-2r-2,\\
a_r&=\frac{4^{L_r}-1}{3},\\
N_r&=2^{d_r}+a_r,\\
m_r&=12\,4^r+1.
\end{aligned}
\]

The quotient defining `a_r` is an odd positive integer, since
`3a_r+1=4^L_r` and `L_r>0`. The exact identities are

\[
3N_r+1=2^{s_r}m_r,
\qquad T^{s_r}(N_r)=m_r,
\qquad 6m_r<d_r.
\]

At every clock `1<=j<s_r`, the actual value is
`2^(s_r-j)*m_r`, hence even and unmarked. Also

\[
\lfloor\log_2N_r\rfloor=d_r,\qquad
(d_r+1)a_r\le70\,2^{d_r}.
\]

Thus every `N_r` is a genuine PR173 mark. Its first positive return obeys

\[
\boxed{R(N_r)<N_r\qquad\text{for every }r\ge0.}
\]

The inputs are unbounded. All these statements, including the first-return
identification and the absence of an ordinary-floor premise, are in
[`BandBridge.lean`](lean/BandBridge.lean). The main results are
`return_descent_of_endpoint_guard`, `return_descent_of_small_endpoint`,
`first_return_descent_of_even_prefix_small`,
`family_first_return_descent`, and
`unbounded_descending_first_returns`.

This repairs the return-map interface for certified deep endpoints. It
does not assert that every marked input reaches such an endpoint. The
following analysis records why the simpler offset-window supply does
not cover the whole marked set.

## 1. A genuine ordinary descent rule

Suppose the smaller offset has a strict stopping prefix

\[
T^t(a)<a,\qquad t\le d.
\]

If `p` is the number of odd steps in that prefix, exact binary lifting gives

\[
T^t(2^d+a)=T^t(a)+3^p2^{d-t}.
\]

The affine lower bound `3^p*a <= 2^t*T^t(a)` forces `3^p<2^t`. Thus

\[
T^t(2^d+a)<2^d+a.
\]

This works on the entire cylinder `a+2^t q`, for every ordinary `q`.
A complete certificate `T^t(a)=1`, with `a>1`, is sufficient but is more
than the rule needs. The actual stopping prefix is proved in
[`BandCertificates.lean`](lean/BandCertificates.lean), including the
source-definition bridge to the earlier exact high-bit lifting theorem.

At a globally least ordinary counterexample, every positive offset below
the candidate already converges. That fact supplies a finite stopping
clock for the offset. It supplies **no upper bound by the binary depth**.
The next section proves that a universal bound of this particular form
would be false, even on a narrow subfamily of the marked band.

There are also two induction distinctions. The endpoint of this ordinary
stopping prefix need not itself be marked, so the certificate is not by
itself a descent after complete marked returns. A least failure among
marked inputs supplies convergence only for smaller marked inputs; it
does not supply convergence of an arbitrary smaller offset. Conversely,
the bounded-visit theorem does not assert that a globally least ordinary
failure is marked. Any use of an ordinary floor below a marked candidate
therefore retains that floor as an explicit additional hypothesis.
Neither induction bridge is assumed here.

## 2. An infinite family that consumes the whole offset window

For each `k>=0`, set

\[
b=2^{k+1},\qquad d=b+k+1,\qquad
a_k=2^b-1,\qquad
n_k=2^d+a_k=2^b(b+1)-1.
\]

These are actual positive odd integers, not completed binary inputs.
They satisfy

\[
\lfloor\log_2 n_k\rfloor=d,\qquad
(d+1)a_k\le 70\,2^d,
\]

so every `n_k` is marked. In fact the proof only needs
`d+1<=2b`, which gives `(d+1)a_k<=2*2^d`.

Both `a_k` and `n_k` start with `b` rising odd steps. More generally, for
any `u>0` and `r>=0`,

\[
T^{2r}(2^{2r}u-1)=3^{2r}u-1.
\]

Since `3^(2r)>=2^(3r)`, even `r` subsequent maximal halvings cannot put
the value below its initial value. Therefore

\[
2^{2r}u-1\le T^j(2^{2r}u-1)
\quad\text{for every }0\le j\le3r.
\]

Apply this with `r=2^k`, first `u=1`, then `u=b+1`. The elementary bound
`k+1<=2^k` gives `d<=3*2^k`, hence

\[
\boxed{a_k\le T^t(a_k)\quad\text{and}\quad
n_k\le T^t(n_k)\quad\text{for every }t\le d.}
\]

Thus the marked-band inequality does not provide the offset stopping
prefix needed in section 1. The obstruction is stronger than an
unavailable estimate: this entire family has **no such prefix**. No
assertion about the eventual convergence or divergence of the Mersenne
offsets is used in proving the finite horizon.

This low-bit mechanism is credited to the rising-block mechanism already
used by PR173. The new application identifies the exact failure of the
offset-certificate window and follows the resulting ordinary state past
that window. The corresponding statements are in
[`BandDescent.lean`](lean/BandDescent.lean):
`odd_run_survives_three_halves`, `input_marked`,
`offset_survives_depth`, and `input_survives_depth`.

## 3. The state after the window: an exact multiplier obligation

Define the odd integer `v_k` by

\[
v_0=1,\qquad
v_{k+1}=v_k(2b v_k+1),\quad b=2^{k+1}.
\]

Induction by squaring gives

\[
3^b=4b v_k+1,
\qquad
v_k=\frac{3^{2^{k+1}}-1}{2^{k+3}}.
\]

The recurrence proves oddness directly. It also gives the exact
ordinary transports

\[
\begin{aligned}
T^{b+k+3}(a_k)&=v_k,\\
T^d(n_k)&=4(b+1)v_k+1.
\end{aligned}
\]

For odd `w`, the usual sibling identity is
`T^3(4w+1)=T(w)`. Consequently

\[
\operatorname{Basin}(a_k)\iff\operatorname{Basin}(v_k),
\qquad
\boxed{\operatorname{Basin}(n_k)
\iff\operatorname{Basin}((b+1)v_k).}
\]

These are actual path equalities and Basin equivalences. The source and
target are specified separately: convergence of `v_k` is not silently
substituted for convergence of `(b+1)v_k`.

For a least ordinary counterexample `n_k`, its smaller offset `a_k`
converges, and therefore `v_k` has an actual finite certificate. The
remaining obligation is multiplication by

\[
b+1=2^{k+1}+1.
\]

This is conditional on the ordinary-floor hypothesis at that member.
It is not an assertion that a least failure in the marked section has the
same hypothesis, or that an arbitrary failure must have this family form.

The first few algebraic pairs are

| `k` | `b` | `v_k` | `(b+1)v_k` |
|---:|---:|---:|---:|
| 0 | 2 | 1 | 3 |
| 1 | 4 | 5 | 25 |
| 2 | 8 | 205 | 1845 |
| 3 | 16 | 672605 | 11434285 |

The table illustrates the exact formulas; it is not evidence that the
universal multiplication implication has been established. The all-index
identities are the substantive result. See `quotient_identity`,
`offset_hits_quotient`, `input_hits_sibling`,
`input_basin_iff_multiplier`, and `offset_basin_iff_quotient` in the Lean
module.

## 4. Trying to close the multiplier by induction and witness energy

Put `a=b/2` and `v=v_(k-1)` at a positive index. Then

\[
v_k=v(2av+1),\qquad
(b+1)v_k=(2a+1)v(2av+1).
\]

The preceding smaller member supplies the target `(a+1)v` if an induction
on this family is available. Ordinary minimality also supplies `v` via
its smaller Mersenne ancestor. This gives two concrete known sources,
`v` and `(a+1)v`. Neither of their ordinary certificates has yet been
transported to the new product `(2a+1)v(2av+1)`.

There is exact growing binary agreement:

\[
v_{k+1}-v_k=2^{k+2}v_k^2,
\]

and, writing `w_k=(2^{k+1}+1)v_k`,

\[
w_{k+1}-w_k
=2^{k+1}v_k\bigl(1+2(2^{k+2}+1)v_k\bigr).
\]

Both sequences therefore approach the same binary limit. This agreement
supplies longer finite parity prefixes. It does not supply a complete
ordinary certificate: the shared prefix at index `k` has length only on
the scale of `k`, while the ordinary bit lengths are on the scale of
`2^k`. Requiring a supplied source certificate to end within that common
prefix would reintroduce the missing window condition.

Following a known source and a target multiplier through a common prefix
also changes the affine offset. For an odd multiplier `p`, if both arms
are odd then

\[
T(pv)=pT(v)-\frac{p-1}{2}.
\]

Once their parities differ, the multiplier itself changes. Consuming the
known source's certificate clock is a valid finite process, but reaching
source `1` leaves a transformed target. No bound puts that terminal
target below the original marked integer in this family. A clock energy
alone therefore does not discharge the target certificate.

An ordinary-height induction fails for a separate, explicit reason:
`v_k` grows like `3^b/(4b)`, whereas `n_k` grows like `b*2^b`. The known
source can already be much larger than the marked candidate. Likewise,
the earlier common rank with clock weight `201/200` does not pay for a
growth rate approaching `(3/2)^b` across `b` clocks. A successful mixed
rank must be attached to a proved transport of the whole obligation,
including its multiplier and offset; a rank on the known source alone
cannot supply that transport.

The unsupported multiplier step is now concrete: derive an actual certificate
for `(2^{k+1}+1)v_k` from the supplied smaller-source certificates by a
uniform terminating rule, and then extend that rule to the other marked
offsets. A global use also needs the ordinary-floor/marked-return bridges
identified in section 1. Neither the finite-band theorem nor the quotient
recurrence establishes those implications.
