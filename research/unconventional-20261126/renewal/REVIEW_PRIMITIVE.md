# Independent review of primitive rational-cycle pressure

I reviewed [PRIMITIVE_PRESSURE.md](../adelic/PRIMITIVE_PRESSURE.md)
at SHA-256 c533c36aad9c50abdd0190d06f0010440d1bc908a38bf5bd597429fd4d7b2031.
The construction and the marked least-period pressure follow as stated,
using the [separately reviewed sieve estimate](CYCLE_SIEVE_REVIEW.md)
for the positive-rate lower half.

* The two disjoint $10$ pairs exist on the mechanical macro since
  zeros are cyclically isolated and the number of zeros tends to
  infinity. Each reversible pair has the same grade. Its flip
  contributes one fixed monomial $c_i$ to the carry independently of
  the other flag. Bounded grade discrepancy gives absolute constant
  bounds for all subword multipliers. Every complete macro has order
  $m$ normalized positive offset, uniformly in the two flags.
* For the lower convergent $q/m$ the macro-slope $A/B$ is below one.
  Its positive periodic solution receives independently additive
  forcing from a constant term and two periodic scalar terms.
  Summing the $k$ consecutive contributions of the first flag gives
  $A^{r-k}Q_k$ and the single contribution of the second flag gives
  $A^{t-1}$. These are the terms in (3). All physical phases have
  order $m/(1-A/B)$, hence exceed a constant times $m^2$.
* If a native period is shorter than $mrt$, its grade fraction is
  still $q/m$ in lowest terms. Hence it is a multiple of $m$.
  Looking at the two fixed pair positions in each aligned macro
  then recovers the two nonconstant periodic binary flags. Both of
  their distinct prime periods divide the number of macros in that
  native period. This forces least period exactly $mrt$.
* Since $r,t>D$ and $Q_h\equiv hA^{h-1}\bmod D$, $D$ is coprime
  to $Q_rQ_t$. Every prime dividing $Q_r$ sees order exactly $r$ for
  $B/A$, as it cannot divide $D$. It therefore divides neither
  $Q_k$ nor $Q_t$, and $c_1A^{r-k}$ is a unit at it. No power of
  such a prime can cancel the denominator of the $r$-term against
  either other term. The argument for $Q_t$ is identical. In the
  localization at primes dividing $D$, the three terms of $D x_0$
  have residues $C_0$, $c_1k/r$, and $c_2/t$, respectively.
  Solving for $1\le k\le D<r$ cancels all of $D$. If $D=1$ the
  same conclusion is immediate. The remaining reduced denominator
  is exactly $Q_rQ_t$, and remains unchanged on every native phase.
* The upper bound for $\log_2 d/(mrt)$ follows from $Q_h\le B^h$.
  For the optional cutoff $c\sqrt{mrt}$, choosing large primes
  $r<t\le2r$ in the **fixed** progression $1$ modulo
  $\operatorname{lcm}(2,\ldots,K+1)$ ensures every $jr+1$ and
  $jt+1$ with $1\le j\le K$ is a composite multiple of $j+1$.
  The prime-order property now excludes every divisor prime up
  to $Kr>c\sqrt{mrt}$. The progression may change when $m$
  changes; the proof correctly chooses $r,t$ after fixing each $m$.
  No estimate for primes in varying progressions is needed.
* At fixed minimum threshold, arbitrarily large genuine least
  periods have nonnegative limiting lower exponent from these
  points. Together with the other family's lower rate $\theta-s$
  and the uniform upper bound, this proves the asserted positive
  part at every $s$. The small-denominator family fails ordinary
  unit spacing at sufficiently large fixed-$m$ flag periods by
  pigeonhole. It gives no ordinary integral cycle.

The proof is mathematical. I checked neither native compilation of
a primitive-pressure formalization nor independent fresh numerical
control of the $r,t,k$ construction in this review.
