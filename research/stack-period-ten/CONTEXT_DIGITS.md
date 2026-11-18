# Leading digits at periodic and Sturmian stack checkpoints

**PROPOSED necessary condition.** In the native $64\to81$ stack, suppose a fixed *ordinary positive* initial room $A_0>1$ realizes an entire specified increment directive. For every periodic positive increment directive, the ordinary contexts on each period phase are jointly Benford in any finite list of pairwise multiplicatively independent integer bases made only of 2 and 3. For the aperiodic Sturmian directives below, the same joint law holds conditional on every controller phase interval of positive length. This excludes constructions imposing a missing joint leading-digit box at the indicated checkpoints, even if the permitted context magnitudes are unbounded.

Use PR #20, `82ca2f932438a9fe0897704ba62959ca23ec830f`, `research/padic-repetition/claims/L-9407-stack-partial-theta-normal-form.md`, for the underlying formal stage interface. Only its ordinary branch equations are used here. In particular no 2-adic infinite sum is identified with an Archimedean sum.

## Real asymptotics conditional on one physical source

Set $\lambda=81/64$, $\ell_t=9m_t+1$, $h_t=\sum_{i<t}\ell_i$, and $\epsilon_j=1$ at the stage beginnings $j=h_t$ and zero elsewhere. The ordinary recurrences are
$$
 64A_{j+1}=81A_j-17\epsilon_j,\qquad
 A_{h_t}=64^{\ell_t}x_t+(64^{\ell_t}+17)/81 .
$$
Writing $c_j=(17/81)\sum_{i\ge0}\epsilon_{j+i}\lambda^{-i}$ gives $0\le c_j\le1$, and $A_j=C\lambda^j+c_j$ with $C=A_0-c_0>0$. This real correction follows by iterating the ordinary recurrence. Both schedules considered below have $h_t\gg t^2$ and $\ell_t=O(t)$, so their contexts obey
$$
 \log x_t=\log C+h_t\log\lambda-\ell_t\log64+o(1).
$$
In particular they are eventually positive.

Let $b_i=2^{u_i}3^{v_i}$ with $u_i,v_i\ge0$, not both zero, and the pairs $(u_i,v_i)$ pairwise nonproportional. Put $z=\log_2 3$. This number is transcendental: unique factorization rules out rational z, and the Gelfond–Schneider theorem rules out algebraic irrational z because $2^z=3$. For integers $k_i$ not all zero the real number
$$
 L=\sum_i k_i\log_{b_i}\lambda
   =\sum_i k_i\frac{4z-6}{u_i+v_i z}
$$
is transcendental. As a rational function of an indeterminate, each nonzero term with $v_i>0$ has a distinct simple pole at $-u_i/v_i$, and its numerator is nonzero there. A pure-base-two term has a nonzero linear coefficient. The sum is therefore nonconstant, and a nonconstant rational function over the rationals maps a transcendental argument to a transcendental number.

## Periodic positive increments

Let the increments repeat with period r and period sum $D>0$. On a fixed phase $t=rj+s$, $\ell_t$ is affine in j, and $h_t$ is quadratic with leading coefficient $9rD/2$. This follows by summing $\ell_{rj+i}=\ell_i+9jD$ over full blocks and the final prefix. For a nonzero integer vector k, the angle $\sum_i k_i\log_{b_i} x_{rj+s}$ equals a quadratic polynomial with irrational leading coefficient $9rD L/2$, plus $o(1)$. Weyl's polynomial equidistribution theorem and its vector criterion give Haar equidistribution of the full tuple of fractional logarithms on every phase. A finite steering prefix only changes the starting height, origin and real constant.

## Algebraic-slope Sturmian increments

Fix an algebraic irrational $0<\gamma<1$, a real intercept $\eta$, and an integer $d\ge1$. Set
$$
 m_t=m_0+dt+\lfloor t\gamma+\eta\rfloor-\lfloor\eta\rfloor .
$$
The two increments $d,d+1$ form the Sturmian coding. Write $s_t=\{t\gamma+\eta\}$. For each fixed $H\ge1$,
$$
 h_{t+H}-h_t=9H(d+\gamma)t+G_H(s_t),\qquad
 \ell_{t+H}-\ell_t=J_H(s_t),
$$
where $G_H,J_H$ are bounded piecewise continuous functions (depending on the fixed parameters). Indeed write $h_{t+H}-h_t=\sum_{i=0}^{H-1}(9m_{t+i}+1)$ and replace $\lfloor(t+i)\gamma+\eta\rfloor$ by $(t+i)\gamma+\eta-\{s_t+i\gamma\}$.

In Weyl's vector criterion include $s_t$ itself beside the context logarithms. If the context frequencies k are not all zero, the H-lag correlation of the Weyl exponential equals the mean of
$$
 e^{2\pi i\,9H(d+\gamma)Lt}\,g_H(s_t)+o(1)
$$
for a bounded Riemann-integrable function $g_H$. The additional controller frequency contributes just a constant at this lag. The numbers $1,\gamma,9H(d+\gamma)L$ are rationally independent: the last is transcendental and the first two are algebraic and rationally independent. Kronecker–Weyl on the two-dimensional torus makes the displayed mean zero. The van der Corput difference theorem then makes the original Weyl mean zero. If all context frequencies vanish but the controller frequency is nonzero, elementary irrational rotation gives the same conclusion. This proves joint Haar distribution including the controller phase.

For either theorem an individual leading-digit box in base b corresponds to a logarithmic interval $[\log_b(a/b^{k-1}),\log_b((a+1)/b^{k-1}))$ for a k-digit integer a. The limiting joint frequency on a periodic phase is the product of the interval lengths. In the Sturmian case intersecting with a controller arc multiplies the frequency by that arc's length. Finite directive cylinders are determined up to endpoints by finite unions of such arcs. Thus contexts constrained, for example, to powers of two times one of finitely many odd numbers at all checkpoints of any such positive-frequency cylinder cannot realize that directive. These results permit contexts whose leading digits meet the joint law. The independent [period-ten exclusion](PROOF.md) uses a different 2-adic argument.
