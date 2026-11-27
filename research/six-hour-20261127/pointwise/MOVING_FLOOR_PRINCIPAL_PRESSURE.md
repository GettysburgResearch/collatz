# The principal moment rate at moving physical floors

Use the notation and imported odd-clock envelope of HIGH_FLOOR_PRINCIPAL_PRESSURE.md (SHA-256 5aa2ded620dc9dc513caad4a804c42efa625baef102154de76196276fdf49eb1). Let the floor satisfy \(H_n\to\infty\), \(n^{-1}\log_2 H_n\to\alpha\), with \(0\le\alpha<\lambda=\log_2 3\). For every fixed \(z\ge0\) and every real moment power \(p\), the entire dependence on the moving floor is
\[
 \lim_{n\to\infty}n^{-1}\ln\mathbb E[
    \mathbf1_{\{\min_{0\le i\le n}x_i>H_n\}} Z_n(z)^p]
 =\max(0,p-1)(\lambda-\alpha)\ln 2.                               \tag{1}
\]
In particular cycles cannot affect the centered exponent on such diverging floors. For \(\alpha>\lambda\) the event is eventually empty because the principal terminal is less than \(2\cdot3^n\). At the boundary \(\alpha=\lambda\), even feasibility depends on the finer floor, so (1) makes no assertion there.

For \(p>1\), the upper estimate on the event follows from \(Z_n(z)\le Z_n(0)\le 3^n H_n^{-1}\exp(n/(3H_n))\), and the unfiltered first moment is at most \(n+1\). For the lower estimate put \(b=2-\lambda\) and take any \(b+\alpha<t<2\). Select the actual odd starts in \([2^{\lfloor tn\rfloor},2^{\lfloor tn\rfloor+1})\) throughout the original proof. The conditional physical envelope there has \(\log_2 x_i\ge(t-b-O(\epsilon t))n-O(1)>\log_2 H_n\) uniformly after choosing a sufficiently small fixed \(\epsilon\). Their payoff is at least \(2^{(2-t-O(\epsilon t))n-O(1)}\); the sum of their reciprocal tilted starting denominators stays bounded away from zero. Sending \(n\to\infty\), \(\epsilon\downarrow0\), then \(t\downarrow b+\alpha\) yields (1)'s lower rate.

To cover the remaining powers, the native moving-floor event actually has probability \(1-O_\alpha(e^{-c_\alpha n})\) at each fixed \(\alpha<\lambda\), for all sufficiently large \(n\) depending on the floor sequence. Under the *original* geometric word law let \(S_j=A_n-A_{n-j}\) count the last \(j\) exponents. Every \(j\) has the ordinary geometric sum law. For any fixed \(\eta>0\), choose \(s>0\) small enough that \(r=\mathbb E\,2^{s(\lambda-e)}<1\), possible since \(\mathbb E e=2>\lambda\). Then
\[
 \Pr(\exists j\le n:S_j<\lambda j-\eta n)
    \le 2^{-s\eta n}\sum_{j\ge1}r^j.
\]
Also \(\Pr(Z_n(0)>2^{\eta n})\le(n+1)2^{-\eta n}\). Outside these events every actual physical state obeys
\[
 x_i\ge 3^i m/2^{A_i}
   =3^i 2^{A_n-A_i}/Z_n(0)\ge 2^{(\lambda-2\eta)n}.
\]
Take \(2\eta<\lambda-\alpha\). With the strictly positive universal payoff floor \([2\max(1,z)]^{-1}\), the same concavity and conditional Jensen estimates as for the fixed floor give zero rate for \(p\le1\). This establishes a quantile statement for the true integer paths attached to unfiltered words. The restriction to the joint accepted-word trace requires a different law.

Prepared by the binary-energy reviewer, 27 November 2026 UTC.
