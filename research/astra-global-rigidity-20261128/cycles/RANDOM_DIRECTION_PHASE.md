# The complete probability threshold for independent random directions

## Statement and scope

For each positive integer independently, include it in a random set \(S\) with
probability \(p\). Once the set has been chosen it stays fixed. Put
\[
 U(x)=\lceil3x/2\rceil,\qquad D(x)=\lceil x/2\rceil,\qquad
 T_S(x)=\begin{cases}U(x),&x\in S,\\D(x),&x\notin S.\end{cases}
\]
Let \(\alpha=\log_3 2\). Then:

1. If \(0\le p\le\alpha\), almost surely **every positive orbit is bounded**.
2. If \(\alpha<p\le1\), almost surely **the set of starts whose orbits tend to
   infinity has natural density one**. For \(\alpha<p<1\), there are constants
   \(c_p,C_p>0\) such that, for every positive integer \(x\),
   \[
      \Pr_S(\text{the orbit of }x\text{ is bounded})\le C_p x^{-c_p}.       \tag{1}
   \]
   In particular, for some \(\eta_p>0\), almost surely
   \[
      \#\{x\le N:\text{the orbit of }x\text{ is bounded}\}
            =O_S(N^{1-\eta_p}).                                         \tag{2}
   \]

This is an elementary written proof for the spatially independent random-set
model. It answers Question 7.8 of Oleg Vasilyev's *Up or down at every integer*
and supplies the critical boundary omitted from that question. Proposition
3.9(b) of that paper already treats \(p<\alpha\); that part is not claimed as
new. The proof uses neither a Collatz density theorem nor an unproved statement
about the ordinary parity-selected map. In particular the result for random
sets does not establish the original Collatz conjecture.

Source: [Vasilyev, arXiv:2611.20344v1, Proposition 3.9(b), Question 7.8](https://arxiv.org/abs/2611.20344v1).
The model and question were checked in the primary text. The finite loop
estimate is formalized in [RandomDirectionLoops.lean](RandomDirectionLoops.lean);
the probability argument below is not formalized.

## 1. Reveal directions only at new states

First take independent **time** bits \(B_0,B_1,\ldots\), with
\(\Pr(B_j=1)=p\), and let
\[
        X_0=x,\qquad X_{j+1}=\lceil 3^{B_j}X_j/2\rceil .                 \tag{3}
\]
This is an auxiliary process, not the fixed-set dynamics. Up to its first
repeated state its law is exactly the law obtained by revealing membership
in \(S\) as the fixed-set orbit visits new integers. Indeed, every direction
revealed before that first repeat belongs to a different integer and has the
prescribed independent Bernoulli law. For each finite deadline the two
first-repeat events therefore have identical probabilities. Increasing the
deadline gives
\[
 \Pr_S(\text{the orbit from }x\text{ is bounded})
      =\Pr(\text{the process (3) ever repeats a state}).                 \tag{4}
\]
A repeated state in a deterministic map starts an eventual cycle. A sequence
of distinct positive integers tends to infinity, since it can visit any fixed
finite interval only finitely many times. These observations justify both
sides of (4). They do not replace the spatial bits by fresh time bits after
a repeat.

## 2. A loop from height \(v\) must be long and down-heavy

Consider any word of \(t\ge1\) up/down choices, containing \(u\) up choices,
that returns the positive integer \(v\) to itself. At every step
\[
          2X_{j+1}=3^{B_j}X_j+\varepsilon_j,
            \qquad \varepsilon_j\in\{0,1\}.
\]
After the word,
\[
       2^t v=3^u v+C,\qquad 0\le C\le3^t-2^t.                        \tag{5}
\]
For the upper bound, append one letter of multiplier \(a\in\{1,3\}\).
The error changes from \(C_t\) to
\(C_{t+1}=aC_t+2^t\varepsilon_t\), so
\(C_t+2^t\le3^t\) implies
\(C_{t+1}+2^{t+1}\le3(C_t+2^t)\le3^{t+1}\).

The positive integers \(2^t\) and \(3^u\) are unequal. Positivity in (5)
forces \(2^t>3^u\), and their positive integral difference is at least one.
Consequently
\[
                    u<\alpha t,\qquad v\le C<3^t.                    \tag{6}
\]
This estimate is intentionally coarse in height. Its usefulness is that it
applies to every repeated segment, including one at an arbitrarily late time.

## 3. Supercritical directions: a polynomial bound on every trap probability

Assume \(\alpha<p<1\), and set
\[
 q=(p+\alpha)/2,\quad \kappa=q\log3-\log2>0,\quad
 I(a\Vert p)=a\log(a/p)+(1-a)\log((1-a)/(1-p)).
\]
Write \(W_j=\sum_{r<j}B_r\), \(I_q=I(q\Vert p)>0\), and
\(I_\alpha=I(\alpha\Vert p)>0\). For a binomial sum of length \(j\),
exponential Markov with a negative parameter, optimized at
\(e^\theta=a(1-p)/(p(1-a))\), gives
\[
                 \Pr(W_j\le aj)\le e^{-jI(a\Vert p)}\quad(a<p).       \tag{7}
\]
The same inequality with a strict event covers nonintegral thresholds.

Let \(\mathcal G_x\) be the event
\[
        W_j\ge qj-\frac{\log x}{2\log3}\quad\text{for every }j\ge0.
\]
Its failure is impossible for
\(j\le(\log x)/(2q\log3)\). A union bound using (7) thus gives
\[
 \Pr(\mathcal G_x^c)
    \le\frac{x^{-I_q/(2q\log3)}}{1-e^{-I_q}}.                          \tag{8}
\]
Rounding is upward, so on \(\mathcal G_x\), for all \(i\ge0\),
\[
             X_i\ge x3^{W_i}/2^i\ge\sqrt{x}\,e^{\kappa i}.            \tag{9}
\]

If a repeated segment starts at time \(i\) and has length \(t\), (6) and
(9) require
\[
  t>\frac{\log x}{2\log3}+\frac{\kappa i}{\log3},\qquad
  \sum_{r=i}^{i+t-1}B_r<\alpha t.                                     \tag{10}
\]
For every fixed \((i,t)\) the last sum is binomial, regardless of overlaps
with other candidate segments. No independence between candidate loops is
asserted or needed. In particular, we do **not** condition its binomial law
on \(\mathcal G_x\). An unconditional union bound over the deterministic
region (10) yields
\[
 \begin{split}
 \Pr(\mathcal G_x\text{ and a repeat})
  &\le\sum_{i\ge0}\sum_{t>\frac{\log x}{2\log3}+\frac{\kappa i}{\log3}}
                       e^{-I_\alpha t}\\
  &\le\frac{x^{-I_\alpha/(2\log3)}}
       {(1-e^{-I_\alpha})(1-e^{-I_\alpha\kappa/\log3})}.                \tag{11}
 \end{split}
\]
Equations (4), (8), and (11) prove (1), for example with
\[
 c_p=\min\left\{\frac{I_q}{2q\log3},
                       \frac{I_\alpha}{2\log3}\right\}>0.
\]
The sum of the two displayed prefactors is an admissible \(C_p\).

For completeness, put \(\gamma=\min(c_p,1/2)\). Summing (1) gives an
expected bounded-start count \(O(N^{1-\gamma})\). Markov's inequality at
\(N=2^k\), with threshold \(N^{1-\gamma/2}\), gives probabilities whose
sum over \(k\) is finite. Borel--Cantelli and monotonicity between successive
dyadic endpoints prove (2) with \(\eta_p=\gamma/2\). This argument needs
no independence between the orbits from different starts. At \(p=1\),
every step is strictly increasing and the conclusion is immediate.

## 4. The critical boundary: recurrence of the time-bit process

Now take \(p=\alpha\). For a current state \(x\), write
\(s=\log x\) and \(Z=\log(X_{j+1}/x)\). The two possible values of \(Z\)
are bounded in absolute value by one for large \(x\). Because rounding adds
between zero and one half before division has been accounted for,
\[
   0\le\mathbb E Z
       \le x^{-1},\qquad
   \mathbb E Z^2\ge\alpha\bigl(\log(3/2)\bigr)^2=:v_0>0.             \tag{12}
\]
Here the unrounded mean is exactly
\(\alpha\log(3/2)+(1-\alpha)\log(1/2)=0\). The second bound follows
from the up outcome alone.

For \(|z|\le1\) and \(s>1\), the second derivative of the logarithm on
the segment from \(s\) to \(s+z\) is at most \(-1/(s+1)^2\). Hence
\[
       \log(s+z)\le\log s+z/s-z^2/(2(s+1)^2).
\]
With \(F(x)=\log\log(\max(x,3))\ge0\), (12) implies, for all
sufficiently large \(x\),
\[
 \mathbb E[F(X_{j+1})-F(x)\mid X_j=x]
     \le\frac1{x\log x}-\frac{v_0}{2(\log x+1)^2}<0.                 \tag{13}
\]
Choose an integer \(M\ge6\) beyond that threshold. All one-step values from
\(x>M\) exceed 3, so the extension used to define \(F\) introduces no
error into (13).

Fix \(x>M\) and \(H>x\), and stop at the first visit to \([1,M]\) or
\([H,\infty)\). This stopping time is finite almost surely: while the process
stays in \((M,H)\), a fixed number of consecutive down choices forces it into
\([1,M]\), and disjoint blocks have independent positive probabilities of
being all down. The stopped process \(F(X)\) is a nonnegative supermartingale;
it is bounded before and at exit, since an upper exit has height at most
\(3H/2+1\). Optional stopping (or its bounded-time version followed by
bounded convergence) gives
\[
           \Pr_x(\text{hit }[H,\infty)\text{ before }[1,M])
                         \le F(x)/F(H).                               \tag{14}
\]
On never hitting \([1,M]\), the finite-interval exit just proved requires an
upper exit for each \(H\). Letting \(H\to\infty\) in (14) shows that
\([1,M]\) is hit almost surely from every state. By the Markov property it is
visited infinitely often almost surely (apply the same conclusion after each
deterministic time). A finite set cannot be visited infinitely often without
a repeated state. Thus the right side of (4) equals one.

For \(p<\alpha\), use common independent uniform random variables to couple
the time bits with those at \(\alpha\). Both maps are increasing in the
state and \(D\le U\), so the lower-\(p\) path stays below the critical path.
Its infinitely many visits to \([1,M]\) again force a repeat. Finally apply
(4) separately to each positive start and take a countable intersection over
starts. This proves the first assertion, including \(p=0\).

## Verification and remaining scope

The loop lemma is a statement about every finite up/down word, not sampled
experiments. Its Lean module proves the affine identity, the integral error
bound, and the strict contraction and height bounds for an actual closed
word. The independent finite checker exhausts small words and checks the
coefficient recurrence against literal integer trajectories; it also retains
the distinction between spatial and time randomness. Neither that finite
check nor the Lean core is described as a formalization of the infinite
probability argument.

The proof was reconstructed by the root agent and independently checked by
the global-cycle agent. Searches for the exact recent question did not locate
a prior answer; this is a limited priority search, not a claim to have surveyed
all random dynamical systems literature. The phase statement concerns random
membership of the **integers** in \(S\), and does not apply it to the
deterministic odd set.
