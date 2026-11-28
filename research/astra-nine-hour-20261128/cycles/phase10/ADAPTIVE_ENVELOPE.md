# Integer mechanical envelopes at every native cut

Consider an ordinary positive odd cycle of period \(p\):
\[
          2^{e_t}x_{t+1}=3x_t+1,\qquad e_t\ge1,\qquad \rho=A/p>\log_2 3.
\]
There is no restriction on its width or on \(\gcd(A,p)\). A constant native word can only give the fixed odd state one. The nontrivial case has \(\rho<2\) by the positive product identity. For any initial phase \(\theta\), set
\[
 b_t=\lfloor(t+1)\rho+\theta\rfloor-\lfloor t\rho+\theta\rfloor,\quad B_t=2^{b_t},
 \qquad h_t=\sum_{s<t}(e_s-b_s),\quad h_-=\min h_t,\quad h_+=\max h_t .
\]
Let \(Z_t^*\) denote the greatest periodic integer vector on the mechanical calendar, satisfying \(Z_{t+1}^*=\lceil3Z_t^*/B_t\rceil\). Its period divides the denominator of the reduced \(\rho\). Indeed the one-lap scalar map on that shorter calendar is monotone, hence has no nontrivial finite cycle: a point fixed by its iterate is already fixed by the original map. Its values are given by the [integer threshold inversion](../phase9/STAIRCASE_INVERSION.md) in the corresponding spatial ranks. Then at every date
\[
   1+\big\lfloor 2^{1+h_t-h_+}x_t\big\rfloor
   \ \le Z_t^*\le\
   1+2^{1+h_t-h_-}x_t.                                                \tag{1}
\]
In particular at a maximum native surplus the envelope dominates \(2x_t+1\) itself. At a minimum surplus it is at most \(2x_t+1\). This gives an integer comparison at all cuts even when the native states occupy arbitrarily many dyadic octaves.

For the upper comparison put \(C_t=2^{h_t-h_-}\ge1\). The positive integers \(C_tx_t\) have mechanical edges
\[
                         B_t C_{t+1}x_{t+1}=3C_tx_t+C_t.
\]
Consequently \(v_t=1+2C_t x_t\) satisfies
\[
                B_t v_{t+1}-3v_t=B_t-1+2(C_t-1)\ge B_t-1.
\]
Every fixed ceiling vector has corresponding residual at most \(B_t-1\). The inverse of the cyclic operator \((Mw)_{t+1}=B_tw_{t+1}-3w_t\) is nonnegative: iteration over a lap writes each coordinate as a sum of residuals with strictly positive weights divided by \(2^A-3^p>0\). Therefore \(v\ge Z^*\) at every date, with strict inequality throughout if \(h\) is nonconstant.

For the lower comparison put \(c_t=2^{h_t-h_+}\le1\), \(r_t=2c_t x_t\) and \(u_t=1+\lfloor r_t\rfloor\). Again \(B_t r_{t+1}=3r_t+2c_t\). If \(c_t=1\), then \(r_t\) is an integer. Otherwise \(2c_t\) is the reciprocal of an integer and \(\{r_t\}\le1-2c_t\). In both cases
\[
                                3\{r_t\}+2c_t<3.
\]
The integer \(B_t\lfloor r_{t+1}\rfloor-3\lfloor r_t\rfloor\) is therefore at most two. Equivalently \(u_{t+1}\le\lceil3u_t/B_t\rceil\) at every date. Iterating this componentwise subsolution upwards under the monotone vector map, bounded above by a large integer supersolution, gives a periodic fixed vector dominating \(u\). Greatestness proves the other half of (1).

There is a one-coordinate form using the same scalar threshold \(U\) at every origin. Put \(D_t=p\sum_{s<t}e_s-tA\), and let \(d_{\min},d_{\max}\) be its extreme values. Restart the phase at date \(t\) with phase zero. Then \(h_s-h_t=\lceil(D_s-D_t)/p\rceil\) in that restarted calendar. Hence
\[
   (U-1)2^{-1+\lceil(d_{\min}-D_t)/p\rceil}\le x_t
     < U2^{-1+\lceil(d_{\max}-D_t)/p\rceil}.
\]
Here \(U=U(A/g,p/g)\) with \(g=\gcd(A,p)\). In particular the source height has not been replaced by the maximum or minimum of an unrelated rotation.

### Exact unrestricted-word endpoint

For an arbitrary positive exponent word with positive denominator, drop the mechanical order and take the same cyclic matrix \(M\) with native radices. Denote by \(V^*\) its greatest integer upward-ceiling vector, and by \(v=M^{-1}{\bf1}\) its positive rational ordinary return. Since \(M{\bf1}=B-3\), one has
\[
                  M(2v+{\bf1})=B-1.
\]
Thus a genuine integer ordinary return implies \(V^*=2v+{\bf1}\) in every coordinate: it attains every maximal digit simultaneously and no stable vector can be larger. Conversely if the maximal digit vector lies in the image of \(M\) over the integers, then \(2v\) is integral. The determinant \(2^A-3^p\) is odd, so \(v\) itself is integral. Its native equations force oddness and positive exact exponents at every date. The only candidate cyclic denominators here are ordinary positive words with \(2^A>3^p\). For the exact Apéry sets of [the digit-semigroup theorem](../phase9/DUAL_APERY_CLOCK.md), full ordinary cancellation is equivalently saturation of the last zero-class point at the absolute top of the binary digit box. The equality is a characterization; the positive word need not be mechanical.
