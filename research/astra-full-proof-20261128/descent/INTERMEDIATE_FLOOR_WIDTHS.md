# The remaining interval widths on a genuine future minimum

A fixed source word turns the entire rational prefix floor into a
single lower endpoint on the range of candidate ordinary integers.
Keeping this dependence gives a signed estimate on the *wide* side
of the [survival comparison](SURVIVAL_WINDOWS.md). The physical prefix
floor itself excludes all sufficiently small widths on the calibrated
scale. An exceptional trajectory would have to supply native signed
mass in the intervening range.

Use the same notation and the ordinary product \(W_R\). Mark a source
by requiring every state, rational or ordinary, to stay at least \(a\).
Fix \(0<\theta<0.0500\) and select
\[
 0<\delta<\theta/2,\quad k=\lceil a^\delta\rceil,\quad
 g=k^{3/5},\quad R=\lfloor r_*+vg\rfloor,\quad v>0.
\]
For every fixed \(0<\epsilon<\delta\), put \(Y_0=\exp(a^\epsilon)\).
The total **signed** contribution summed over \(r\le R\) and widths
\(Y\ge Y_0\) to (1) of the survival note is \(o(1/a)\). The argument
below even bounds the absolute value after summing the ordinary
endpoints within each individual word interval. The absolute values
of the endpoint summands are not small in general.

**Exact lower support at this horizon.** For any word at rung \(r\ge1\)
which contributes a marked source \(x\in(0,N]\), let \(y\) be its
ordinary post-odd endpoint. The very last odd input on the true prefix
is \((2y-1)/3\ge a\). Each of the \(r\) prefix tolls is at most
\(1/(3a)\) in natural logarithms. The exact identity \(W_r=A_rx/y\)
therefore forces
\[
      Y=NA_r\ \ge\ A_rx=yW_r\
      \ge \frac{3a+1}{2}\exp(-r/(3a))
      \ge L_a:=\frac{3a+1}{2}\exp(-R/(3a)).                      \tag{0}
\]
Thus the entire contribution below \(L_a\) is exactly zero. Since
\(R=O(a^\delta)=o(a)\), \(L_a=(3/2-o(1))a\). This is a deterministic
statement about the same source and its actual last odd input. It
requires neither stationary small-ball bounds nor a sparse-set count.
The uniform all-\(R,N\) small-width estimates in the survival note are
separate results, useful without the calibrated horizon.

First replace \(W_R\) by one on this portion of the comparison. On a
marked trajectory every departure costs at most \(\log(1+1/(3a))\)
in natural logarithms. Thus \(0\le1-W_R\le R/(3a)\), including the
entire rational prefix. In each word the number of marked candidates
is at most \(C_\theta a^{-\theta}(B_r+Y)\) by the external fixed-barrier
bound. This statement uses the *necessary* ordinary endpoint condition
\(y\in E_a\). Since \(\mathbb E a_i=1\) and \(B_{r+1}=a_{r+1}B_r+1/2\),
\(\mathbb E B_r=r/2\). The total error, measured before endpoint
cancellation, is at most
\[
 O_\theta\bigl(R^2a^{-1-\theta}(1+R/Y_0)\bigr)=o(1/a).           \tag{1}
\]

For each word all intermediate states are increasing affine functions
of its initial source. The endpoint \(y\) is also an increasing affine
function of this source. Thus the full prefix constraint is an
intersection of lower half-lines in \(y\), hence one lower half-line.
The surviving endpoint interval is precisely the intersection of that
half-line with \((B_r,B_r+Y]\), further marked by \(E_a(y)\). This uses
no trit estimate on a history-dependent label. The complete history
constraint before this ordinary endpoint has already been evaluated
within the fixed word.

Words with \(B_r>Y\) contribute \(o(1/a)\) in absolute value after
summing \(r\). Indeed there are at most \(Y+1\) integers in an
interval of length \(Y\), the weight here is \(1/Y\), and
\(\Pr(B_r>Y,\ Y\ge Y_0)\le r/(2Y_0)\). For the others the upper
endpoint is at most \(2Y\). Discarding \(y<\sqrt Y\) costs
\(O(Y^{-1/2})\) per word. Split the remainder into native positive
octaves \([Z,2Z)\). Their lower limits are at least \(\sqrt Y/2\).
At the integer date \(t=\lfloor\frac14\log_2 Z\rfloor\) every starting
integer in such an octave has all its preceding states and its date
\(t\) state at least \(Z2^{-t}>a\), for all sufficiently large \(a\).
The floor label therefore satisfies \(E_a(y)=E_a(T^t y)\) there.
This is an ordinary endpoint test at a fixed clock. Apply the signed
starting-trit bound to each intervening source subinterval to get
\[
 \left|\sum_{y\in I\cap[Z,2Z)}
 (3\mathbf1_{y\equiv2\ (3)}-1)\mathbf1_{E_a}(y)\right|
       \ll_A Z(1+\log Z)^{-A}.                                    \tag{2}
\]
The subinterval form follows directly from the source proof on odd
octaves. It also follows by subtraction of the two ordinary prefixes
in its displayed inequality (3): both nonempty endpoints are in
\([Z-1,2Z]\), and \(t\asymp\log Z\). The endpoint test \(E_a\) may depend
on \(a\) since (3) is in total variation. [PR215, signed native count and endpoint at a residual time, equation (3)](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/escape/phase2/NATIVE_BINOMIAL_TRANSFER.md)

The octave lengths sum to \(O(Y)\), and all logarithms are comparable
to \(\log Y\). Divide (2) by \(Y\) and sum over \(r\le R=O(a^\delta)\).
Taking \(A>(1+\delta)/\epsilon\) makes the resulting
\(O_A(a^{\delta-\epsilon A})=o(1/a)\). Together with (1) and the
discarded terms this proves the wide-width claim.

At this same source scale the rational final marked mass is
\(o(1/a)\). A source satisfying the full floor survives the recorded post-odd
floor at every date. Equation (1) in the [absorbing rational floor
estimate](../mass/ABSORBING_RATIONAL_FLOOR.md) bounds this larger event
by \(O(u^{-1}e^{-c k^{1/5}})\), \(u\asymp k^{-2/5}\), uniformly at every
floor \(a\ge32\). This is \(o(1/a)\) for the chosen power scale. If \(a\) is the minimum of its own positive orbit and a
ternary unit, the actual native first-landing estimate at threshold
\(a\) gives mass \(\gg1/a\) above this entire floor. The corresponding
finite survival factor is at least \(\exp(-R/(3a))=1-o(1)\).
The exact lower support (0) and the signed upper tail then give
\[
 \sum_{r\le R}\bigl[\text{signed full-floor contribution at }
          L_a\le Y<\exp(a^\epsilon)\bigr]\gg 1/a                      \tag{3}
\]
for any such sequence of \(a\to\infty\). In particular (3) is
necessary on arbitrarily large supplied minima of an escaping
positive orbit. A single cycle supplies one minimum. The unproved
step is a uniform \(o(1/a)\) upper over the intermediate widths. A
bound by inverse powers of \(\log Y\) alone costs far more than
\(1/a\) near \(Y\asymp a\), and the fixed-word floor does not justify
a common interval across different words.

## The boundary left by pairing identical reduced sources

There is an exact source-preserving pairing of the signed terms.
It leaves a current across the width cutoff. Even a completed
downward and upward excursion on the same ordinary trajectory has
unequal weights in this comparison.

For a positive source \(x\in\mathbb Z[1/3]\), define its actual width
\(Y_t(x)=N3^t2^{-\sigma_t(x)}\) for every number of odd departures
\(t\ge0\), with \(Y_0=N\). Write \(\mu_r\) for the uniform source law
on \(u/3^r\) through \(N\). Let \(0\le V(x)\le1\) be any intrinsic mark
used unchanged in every denominator, such as \(W_R\) with the entire
floor. Put \(I_t=\mathbf1_{Y_t\le C}\) with \(0<C<N\); write \(\Delta_r^-\)
for the contribution to the signed rung from \(Y_r\le C\). Pulling
back \(3\mid u\) exactly gives
\[
 \Delta_r^-=\mathbb E_{\mu_{r-1}}[V I_r]-\mathbb E_{\mu_r}[V I_r].
\]
In the first term the additional run is taken on the same source.
At level \(r-1\) its post-odd endpoint \(n=T^{\sigma_{r-1}}x\) is an
ordinary integer, so the next actual width factor is
\(Y_r/Y_{r-1}=3/2^{1+v_2(n)}\). Therefore
\[
 J_C:=\sum_{j=0}^{R-1}\mathbb E_{\mu_j}[V(I_{j+1}-I_j)]
      =\sum_{r=1}^R\Delta_r^-+\mathbb E_{\mu_R}[V I_R]
                         -\mathbb E_{\mu_0}[V I_0].                 \tag{4}
\]
The positive part of each difference is a downward crossing through
\(C\), and the negative part is an upward crossing. Equation (4) is
finite and uses the actual native next even-run and odd step.

Regroup \(J_C\) by *reduced* origin. A particular positive \(x\le N\)
with reduced denominator \(3^j\) occurs in every \(\mu_{j+s}\) with
weight \(1/(N3^{j+s})\). For \(d=R-j\ge1\), its joint contribution is
\(V(x)/(N3^j)\) times
\[
 \begin{aligned}
 \sum_{s=0}^{d-1}3^{-s}(I_{j+s+1}-I_{j+s})
 &=-I_j+\sum_{l=1}^{d-1}2\,3^{-l}I_{j+l}
                                  +3^{-(d-1)}I_R .                 \tag{5}
 \end{aligned}
\]
The positive coefficients on the right sum to one. An origin whose
width is above \(C\) at first integrality has nonnegative net; the net
is positive if its mark is positive and it later enters the lower
side within the horizon. An origin entering the ordinary grid below
or at \(C\) has nonpositive net. In particular every native origin
starts on the first side. A completed downward and upward excursion
at relative indices \(s<t\) contributes \(3^{-s}-3^{-t}>0\). If a
native origin escapes, its distinct-segment bound gives \(W_\infty>0\),
so \(Y_t=(N/x)W_t T^{\sigma_t}x\to\infty\). Its eventual return above a
fixed cutoff does not cancel an earlier downward crossing in (5).
Any successful use of (4) must therefore compare different primitive
origins or exploit additional arithmetic about whether they cross.

The unchanged positive map supplies a calibration. Take
\(V=\mathbf1_{\{T^i x\ge1\;\forall i\ge0\}}\), with no correction
product. Every ordinary positive integer has this mark. On a fixed
word its rational prefix floor cuts out a single endpoint interval;
the positive ordinary suffix automatically meets the floor. The
signed trit sums to at most two in absolute value on any interval of
consecutive integers. Hence the total signed contribution to the
rungs from \(Y_r>C\) has absolute value at most \(2R/C\), by applying
this bound inside each word and dividing by \(Y_r\). Meanwhile
\(\mathbb E_{\mu_0}V=1\) and
\(\mathbb E_{\mu_R}V\ll e^{-ch^2/k}\) at \(R=r_*+h\),
\(\sqrt k\ll h=o(k)\), by the [recorded floor-one upper](../mass/ABSORBING_RATIONAL_FLOOR.md).
Using (4) and the two complementary width ranges gives
\[
                J_C=1+O(R/C+e^{-ch^2/k})\qquad(0<C<N).             \tag{6}
\]
Thus even in this actual positive system with an interval cutoff on
*every* word and exact cancellation on every complete ternary period,
the same-origin boundary current tends to one for \(R\ll C<N\).
This is a floor-one control. It supplies no high-floor exceptional
trajectory and does not evaluate the unresolved intermediate sign in (3).
