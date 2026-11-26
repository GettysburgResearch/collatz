# A lower bound for Béhani’s Bergman spectral-radius question

**Theorem O9.** For Béhani’s shortcut Collatz transfer operator $\mathcal T$ on the classical Bergman quotient $X_{\omega_0}$,
$$
      \frac{\sqrt{20}}3\ \le\ r(\mathcal T)\
      \le\sqrt{\frac{5516102802}{2482245023}}.
$$
In particular $1.49071198<r(\mathcal T)<1.49071236$. The lower inequality excludes the value $\sqrt2$ proposed in Question 4.1 of Béhani’s *Linear dynamics of an operator associated to the Collatz map*. The argument leaves the exact value open. The analytic lower bound requires no numerical certificate.

## The published operator and the lower bound

The coefficient norm is $\|f\|^2=\sum_{j\ge3}\pi|c_j|^2/(j+1)$, with the degrees $0,1,2$ quotiented out. The transfer sends $z^j$ to $z^{Tj}$, with zero output in the quotient when $Tj<3$. The shortcut sends an odd $j$ to $(3j+1)/2$. For an endpoint $a\ge3$, every $j$ with $T^k j=a$ has stayed outside $\{0,1,2\}$ throughout, because that set is forward invariant. Proposition 2.1 gives
$$
       \|\mathcal T^k\|^2=\sup_{a\ge3}
            \sum_{T^k j=a}\frac{j+1}{a+1}.
$$
This is a transfer formula. Swapping the numerator and denominator gives a different operator.

Let a chronological forward parity word of length $k$ have $q$ odd letters and carry $F$, so that $2^k a=3^q j+F$. The full word occurs for an endpoint residue class $r\bmod 3^k$ exactly when $2^k r\equiv F\bmod3^q$, once the endpoint in that class is taken sufficiently large. One proof splits off the last letter of the forward word. If that letter is even, the preceding endpoint is $2a$ and the carry is unchanged. If it is odd, the carry is $3F'+2^{k-1}$. The congruence first gives $a\equiv2\bmod3$, then gives the preceding congruence at $(2a-1)/3$. At each backward step positivity holds for sufficiently large endpoints because all slopes are positive. The successive inverse choices construct the prescribed ordinary parities. At one endpoint distinct words give distinct sources, by forward determinism.

There are exactly $3^{k-q}$ allowed residues modulo $3^k$ for a given word because $2$ is a ternary unit. At each such residue, letting $a\to\infty$ gives the contribution $(j+1)/(a+1)\to 2^k/3^q$. Define $S_k(r)$ as the sum of these limiting slopes for all allowed words. Proposition 4.2 of Béhani states $\|\mathcal T^k\|^2=\max_{r\bmod3^k} S_k(r)$. The lower argument needs only $\ge$, which follows directly by taking the indicated ordinary endpoints to infinity. Averaging the slope sum over residues gives
$$
  3^{-k}\sum_{r\bmod3^k} S_k(r)
    =\sum_{q=0}^k {k\choose q}\,3^{-q}\,2^k3^{-q}
    =2^k(1+1/9)^k=(20/9)^k.
$$
The spectral radius formula gives the lower bound after taking $2k$-th roots.

## An integer certificate for the upper bound

For a function $v$ on the ternary integers, the positive operator
$$
  (Lv)(r)=2v(2r)+\tfrac23{\bf1}_{r\equiv2\bmod3}v((2r-1)/3)
$$
satisfies $S_k=L^k{\bf1}$ by the first backward step. If a positive bounded table $v$ of period $m=3^h$ has $Lv\le\beta v$ at every lifted residue, then $S_k\le(\max v/\min v)\beta^k$. Proposition 4.2 therefore gives $r(\mathcal T)^2\le\beta$.

For each residue $r\bmod m$, the even term is uniquely determined. When $r\equiv2\bmod3$ the three possible odd input residues modulo $m$ are
$$
     ((2r-1)/3)+j(m/3)\pmod m,\qquad j=0,1,2 .
$$
Thus three times the exact maximum of $Lv$ on the residue is
$$
  Y_r=6v_{2r\bmod m}
   +2{\bf1}_{r\equiv2\bmod3}
      \max_{j=0,1,2} v_{(((2r-1)/3)+j(m/3))\bmod m}.
$$
The accompanying checker constructs a positive integer table with $h=10$, computes every $Y_r$ using arbitrary-precision integers, and verifies $Y_r\le3\beta v_r$ for all 59,049 residues. It uses $\beta=5516102802/2482245023$. The positive-integer supersolution can be regenerated using the standard Python library. Its canonical decimal-lines SHA-256 is 91170eb02223527b842d0e06d8370ba6e8278f71f5a108f33075660de54dae88. The search iteration need not converge. The final inequalities certify the global upper bound independently of how the table was found. Run `python check_bergman.py --depth 10` to reproduce the certificate. The smaller depths in the stored controls supply fast regression cases.

The algebraic lower bound and the certified upper bound apply to the same $X_{\omega_0}$ and the same direction of the operator. They do not concern the positive-exponent composition operator of O8. The high-precision bracket does not prove equality with its lower endpoint.

## Sources

- V. Béhani, *Linear dynamics of an operator associated to the Collatz map*, Proc. Amer. Math. Soc. 152 (2024), 1191–1206, Proposition 2.1, Question 4.1 and Proposition 4.2. <https://doi.org/10.1090/proc/16627> <https://arxiv.org/pdf/2303.03203>
- The use of maxima over ternary lifts has an unweighted comparison in rStation paper 47, Theorem 5. The present table tracks the slope weights in Béhani’s Bergman quotient. <https://rstation.ai/problems/collatz/papers/47>
