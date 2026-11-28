# The remaining interval widths on a genuine future minimum

A fixed source word turns the entire rational prefix floor into a
single lower endpoint on the range of candidate ordinary integers.
Keeping this dependence gives a signed estimate on the *wide* side
of the [survival comparison](SURVIVAL_WINDOWS.md). Together with its
small-width bound, an exceptional trajectory would have to supply
native signed mass at intermediate widths on a single calibrated
source scale.

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
The small-width bound (7) then gives
\[
 \sum_{r\le R}\bigl[\text{signed full-floor contribution at }
          a/2<Y<\exp(a^\epsilon)\bigr]\gg 1/a                      \tag{3}
\]
for any such sequence of \(a\to\infty\). In particular (3) is
necessary on arbitrarily large supplied minima of an escaping
positive orbit. A single cycle supplies one minimum. The unproved
step is a uniform \(o(1/a)\) upper over the intermediate widths. A
bound by inverse powers of \(\log Y\) alone costs far more than
\(1/a\) near \(Y\asymp a\), and the fixed-word floor does not justify
a common interval across different words.
