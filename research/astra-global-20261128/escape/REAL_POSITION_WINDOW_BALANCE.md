# A smooth real mantissa law that balances every digit position

Normalize $x$ to the ternary band $[1,3)$ and set $e(x)=\mathbf1_{x<2}$, $S(x)=3^{e(x)}x/2$. Under $u=\log_3 x$ modulo one this is the irrational rotation $R(u)=u-\alpha$, $\alpha=\log_3 2$. Its Haar probability in $u$ gives branch mass $\alpha$. Use the usual nonterminating ambiguity convention of taking the terminating ternary expansion at triadic rationals; our laws give these points zero mass. Center digit windows on the leading digit or on any subsequent fractional digit, padding above the leading digit by a separate symbol.

**Theorem.** For each finite radius $r$ there is a probability $\mu$ with a smooth, strictly positive density in circle coordinate such that

$$
 \mu(e=1)>\alpha,\qquad
 \operatorname{Law}_\mu(W_i(Sx))=\operatorname{Law}_\mu(W_i(x))
 \quad\text{for every individual digit position }i\ge0.
$$

The excess can be chosen arbitrarily small and positive. This holds for all windows simultaneously at the prescribed radius. A real finite-precision ranking can therefore fail even when every position carries a separate coefficient. The branch is determined by the leading mantissa digit in this theorem. A true ordinary fixed-length certificate must also synchronize it with the final division carry; the [integer construction](POSITION_WINDOW_PUMP.md) achieves this extra condition at radii one and two.

Choose two fractional positions $k,l$, $l-k>2r$, and a compact subinterval in the interior of a length-$l$ ternary cylinder contained in $(1,2)$ on which these two digits are both zero. Take a smooth nonnegative bump $b(x)$ supported there, of integral one. For $h=3^{-k},t=3^{-l}$ let $\tau_h$ translate a density by $h$ to the right and put

$$g=-(I-\tau_h)(I-\tau_t)b.$$

The four translations toggle the specified digits from zero to one without carry or any other digit change, apart from the immaterial double-expansion points. Each individual $W_i$ misses at least one of the two positions. Pairing the two choices of that missing digit shows that the signed measure $g(x)dx$ gives zero to **every** position/window event and to the whole band. Its logarithmic moment is strictly positive. Indeed

$$\log(x+h+t)-\log(x+h)-\log(x+t)+\log x=
 -\int_0^h\!\int_0^t(x+s+v)^{-2}\,dv\,ds<0,$$

and $g$ has the opposite sign to this mixed difference.

Push $g(x)dx$ to a smooth zero-mean circle density $G(u)du$. The support stays away from the band endpoints. There is a real smooth zero-mean $H$ solving $R_*(Hdu)-Hdu=Gdu$. In Fourier coordinates set $\widehat H(0)=0$ and divide $\widehat G(m)$ by $e^{2\pi i m\alpha}-1$ for $m\ne0$. A fixed-base linear form in $\log2,\log3$ gives $\|m\alpha\|\ge c|m|^{-A}$ for some finite $A,c>0$. The Fourier coefficients of $G$ decay faster than each power, so those of $H$ do also. Conjugate symmetry yields a real solution. Only finite irrationality measure is needed here. [Matveev, Theorem 2.1, fixed rational bases](https://doi.org/10.1070/IM2000v064n06ABEH000314)

For $0<\epsilon<1/(1+\|H\|_\infty)$ use density $1+\epsilon H(u)$ against Haar and call its band image $\mu$. Its one-step signed difference is $S_*\mu-\mu=\epsilon g(x)dx$. Hence all the required window laws agree. On the band, $\log S(x)-\log x=e(x)\log3-\log2$, giving

$$\mu(e=1)-\alpha=\frac{\epsilon}{\log3}\int_1^3 (\log x)g(x)\,dx>0.$$

The four separated trit changes create observable logarithmic drift while remaining invisible to each single local window. The proof supplies a smooth real marginal whose normalized division prefixes can be sampled at any finite depth. It leaves the construction of a global integer flow with matching terminal parity at general radius open.
