# Transcendental inverse parity for every nonperiodic exponential morphic word

**Proposed.** Let $(e_n)$ be a binary morphic sequence with a presentation of exponential emitted length, including automatic sequences and primitive-substitution codings. Put $s_n=\sum_{j<n}e_j$. In $\mathbb Z_2$ the inverse-parity value
$$
 x=-\frac13\sum_{n\ge0}e_n\,2^n3^{-s_n}
$$
is rational if the word is eventually periodic, and transcendental over $\mathbb Q$ otherwise. No hypothesis on the frequency of ones or convergence of the series at infinity is needed. In particular the proposed result is a transcendence statement for individual sources, not just a test on positive ordinary trajectories.

We give the descent argument because the monomial parametrization of the [exponential proof](EXPONENTIAL_MORPHIC.md) uses algebraic constant factors. Assume $x$ algebraic and fix an algebraic closure of $\mathbb Q$ in $\mathbb C_2$. At the original rational weights $z_b=2^{|\tau(b)|}/3^{|\tau(b)|_1}$ for the nonempty emitted blocks, the inverse-parity formula is a row relation in $1,G_b(z)$ with first coefficient $x$ and all remaining coefficients rational. The [productive reduction](MORPHIC_NORMALIZATION.md) permits erasing presentations. Construct the reduced point $y_j$, parametrization $Z$, series $H=G\circ Z$ (including $1$), and rational-function reduction $H=R F$ to an independent basis at a late sample, as in the exponential proof. The coefficients of the row may be algebraic: the finite-place independence is over $\overline{\mathbb Q}$ and its proof fixes their number field before forming auxiliary polynomials. Transport through the original polynomial matrices and then $R(y_j)$. The transported row is zero as an algebraic vector.

Now let $\gamma$ be any automorphism of $\overline{\mathbb Q}$ over $\mathbb Q$. Apply it to the algebraic vector identity, the chosen coefficients of $R$, and the sampled algebraic coordinates. Conjugation is only applied to algebraic data and to coefficients of formal series. The conjugated parametrization satisfies
$$
 Z^\gamma(y_j^\gamma)=(Z(y_j))^\gamma=Z(y_j),
$$
because the right-hand coordinates are precisely the original rational iterated weights. Also $y_j^\gamma$ has the same coordinate 2-adic moduli as $y_j$: its coordinates are products of rational powers of ordinary primes, and the conjugates differ by roots of unity. Thus the conjugated series and cleared basis identities can be evaluated there. Term by term $H^\gamma(y_j^\gamma)$ equals the same original 2-adic vector at the iterated point; every combined prefix weight is rational. The original finite substitution matrices are rational at the original rational samples. Evaluating the conjugated zero row therefore gives the original inverse-parity relation with $\gamma(x)$ in place of $x$. It follows in the same completion that $\gamma(x)=x$ for every $\gamma$, so $x\in\mathbb Q$.

A rational 2-adic integer realizing an exponential morphic parity word has an eventually periodic orbit by the [signed rational theorem](SIGNED_PARITY.md). Conversely, for eventually periodic parity the inverse affine map of one period has rational coefficients and slope $2^L/3^u\ne1$; its unique fixed point, and every finite inverse prefix thereof, are rational. The stated dichotomy follows.
