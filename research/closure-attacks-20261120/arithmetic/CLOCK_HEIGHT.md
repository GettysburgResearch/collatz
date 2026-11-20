# Ordered prime-height accounting and the maximum of an arbitrary cycle

**Status: PROPOSED; complete elementary written proofs, pending independent
review at frozen bytes. Collatz remains unresolved.** The headline is a
restriction on every positive ordinary cycle, with no prime alphabet or
valuation-word restriction:

\[
 L=\log_2\max_i n_i,\qquad
 s=\#\{p:p\mid n_i\text{ for some }i\}
 \quad\Longrightarrow\quad
 \boxed{L\le s\{8+12\ln(1+L)\}.}                 \tag{A}
\]

Thus a nontrivial cycle requires at least
\(L/(8+12\ln(1+L))\) distinct primes. Equivalently,
\(L=O(s\log(s+1))\), uniformly in the prime magnitudes and the period.
The proof also gives a localized finite-history inequality and quantitative
dispersion of height across prime pools whose cardinalities can grow.

The return-numerator method has direct prior art. In particular, rStation
Paper 138 already proves prime-power return tails, and (A) can also be
obtained as a peak-window corollary of that method. The localized bound
in terms of \(\sum\ln^+\log_2 n_i\) below is an independently derived
refinement; no broad novelty claim is made. See Section 8.

## 1. Map, quantities, and dependencies

Use actual positive ordinary odd iterates

\[
 n_{i+1}=U(n_i)=\frac{3n_i+1}{2^{a_i}},\qquad
 a_i=v_2(3n_i+1)\ge1,\qquad x_i=\log_2 n_i\ge0.
 \tag{1}
\]

Throughout, \(\ln\) is the natural logarithm. Put
\(\ln^+x=\ln\max\{1,x\}\), including \(\ln^+0=0\).
For a prefix of \(N\ge1\) states and a finite prime set \(S\), define

\[
 W_N=\sum_{i<N}x_i,\qquad \bar x_N=W_N/N,
 \quad z_i(p)=v_p(n_i)\log_2p,
 \quad Y_N(S)=\sum_{i<N}\sum_{p\in S}z_i(p).
 \tag{2}
\]

Repeated states are allowed in all finite estimates. A prime pool is one
set shared across the prefix; it may be chosen after the entire prefix
is observed. The estimates do not allow an independently selected pool
at each time. The cycle statements use the actual periodic lift, including
windows longer than the primitive period.

The only arithmetic input is the following elementary estimate, reconstructed
here from ADEL-001 at PR154 head
`fe40bb6f88e8094290ef01207d9bf7c4798d35d0`,
`research/structural-reset-20261120/adelic/PRIME_HEIGHT_ESCAPE.md`:

\[
 x_{i+1}-x_i\le1,\qquad
 \log_2\gcd(n_i,n_j)<x_i-x_j+3(j-i)\quad(i<j).
 \tag{3}
\]

For completeness, if \(d=j-i\), \(A_t=\sum_{u=i}^{i+t-1}a_u\),
and \(A=A_d\), then

\[
 2^A n_j=3^d n_i+C,
 \quad C=\sum_{t=0}^{d-1}3^{d-1-t}2^{A_t},
 \quad 0<C<2^A(3/2)^d.
\]

The common divisor divides \(C\). Also
\(A=x_i-x_j+\sum_{u=i}^{j-1}\log_2(3+1/n_u)
\le x_i-x_j+2d\). These facts prove the gcd estimate.
The upward bound follows from
\(x_{i+1}-x_i=\log_2(3+1/n_i)-a_i\le1\).

No external analytic theorem, distinctness, upper bound on individual
\(a_i\), or fixed-source extraction is needed for (3).

## 2. The ordered clock and a height-localized tail estimate

Define

\[
 t_i=3i-x_i.
 \tag{4}
\]

Then \(t_{i+1}-t_i\ge2\). For a fixed prime, (3) gives

\[
 \min\{z_i(p),z_j(p)\}<t_j-t_i\qquad(i<j).
 \tag{5}
\]

In particular, indices carrying \(p\)-height at least \(h>0\) are
separated by more than \(h\) in this increasing clock. The point of
the next lemma is to charge those separations only where ordinary height
is sufficiently large.

### AR-CLOCK-001: localized level count

For every prime \(p\), every \(h>0\), and every actual prefix,

\[
 \boxed{
 \#\{i<N:z_i(p)\ge h\}
 \le\frac5h\#\{i<N:x_i\ge h/2\}
       +\left(1+\frac{x_0}{h}\right)
        \mathbf1_{\{h\le2x_0\}}.}
 \tag{6}
\]

**Proof.** Split \(\{i<N:x_i\ge h/2\}\) into maximal consecutive
components. Consider a component \([a,b]\) not beginning at zero, with
\(\ell=b-a+1\), and suppose it contains a marked index with
\(z_i(p)\ge h\). Since \(x_{a-1}<h/2\) and upward increments are
at most one, \(x_a<h/2+1\). Reaching a marked state, whose height is
at least \(h\), gives

\[
 h\le x_i\le x_a+(i-a)<h/2+\ell,
 \quad\text{so}\quad \ell>h/2.
\]

At the other end, \(x_b\ge h/2\). Consequently

\[
 t_b-t_a=3(\ell-1)+x_a-x_b<3\ell.
\]

If there are \(k\ge1\) marked indices in this component, their consecutive
clock gaps exceed \(h\). Thus
\(k\le1+3\ell/h<5\ell/h\), using \(1<2\ell/h\).
Components with no marked indices need no charge.

An initial component \([0,b]\), if present, has clock span at most
\(3\ell+x_0\). Its marked count is at most
\(1+(3\ell+x_0)/h\), hence at most
\(5\ell/h+1+x_0/h\). Such a component exists only when
\(x_0\ge h/2\). Sum over all components. This proves (6), including
single-state components and prefixes ending in a high component. \(\square\)

The proof is a general clock-packing lemma: it uses only nonnegative
heights, upward increments at most one, \(0\le z_i\le x_i\), and (5).
The numerical replay therefore includes exact rational synthetic inputs
to check its boundary cases independently of Collatz factorization.

## 3. Integrating all prime-power scales

Set

\[
 E(x)=2(x-1)_++x\ln^+x,
 \qquad (x-1)_+=\max\{x-1,0\}.
 \tag{7}
\]

### AR-CLOCK-002: finite-history prime-height budget

For every prime \(p\),

\[
 \boxed{
 Y_N(\{p\})\le2N+5\sum_{i<N}\ln^+x_i+E(x_0)
 \le N\{2+5\ln(1+\bar x_N)\}+E(x_0).}
 \tag{8}
\]

Consequently, simultaneously for every prime set \(S\) of size at most
\(s\),

\[
 \boxed{Y_N(S)
 \le sN\{2+5\ln(1+\bar x_N)\}+sE(x_0).}
 \tag{9}
\]

**Proof.** The layer-cake identity gives
\(Y_N(\{p\})=\int_0^\infty\#\{i:z_i(p)\ge h\}\,dh\);
choices at finitely many equality thresholds have no effect. The part
\(0<h<2\) is at most \(2N\). Integrate (6) over \(h\ge2\).
Each state contributes

\[
 5\int_2^{2x_i}\frac{dh}{h}=5\ln^+x_i,
\]

where the integral is zero if \(x_i\le1\). The initial-component term
integrates to zero if \(x_0\le1\), and otherwise to
\(2x_0-2+x_0\ln x_0\), exactly \(E(x_0)\).
Finally, \(\ln^+x\le\ln(1+x)\) and Jensen's inequality give
\(\sum\ln^+x_i\le N\ln(1+\bar x_N)\). Summing the bound for the
individual primes proves (9). No prime magnitudes occur in its constant.
\(\square\)

The source term is essential for a short segment beginning with a large
prime power. It is retained rather than treating a first occurrence as
an already paid return.

### AR-CLOCK-003: growing prime pools on one fixed escaping orbit

On a non-eventually-periodic positive ordinary orbit, \(\bar x_N\to\infty\).
For \(W_N>0\), (9) gives the explicit uniform estimate

\[
 \sup_{|S|\le s}\frac{Y_N(S)}{W_N}
 \le\frac{s\{2+5\ln(1+\bar x_N)\}}{\bar x_N}
       +\frac{sE(x_0)}{N\bar x_N}.
 \tag{10}
\]

Thus the supremum tends to zero even for cardinalities \(s=s_N\) satisfying

\[
 s_N=o\!\left(\frac{\bar x_N}{\ln(1+\bar x_N)}\right).
 \tag{11}
\]

This statement keeps the original ordinary source fixed. Distinctness
implies escape from every finite set, hence \(x_i\to\infty\) and the
mean-height assertion. Alternatively distinct positive integer states
alone give a factorial lower bound for \(W_N\). In (11), the source term
in (10) also tends to zero. A prime set may depend on the entire observed
prefix; the assertion still uses one set within each prefix.

## 4. Mean height and prime concentration on arbitrary cycles

Let a positive odd cycle have period \(m\) and mean height
\(\bar x=m^{-1}\sum_{i<m}x_i\). If \(\bar x=0\), all states are one.
Otherwise define its prime-height fraction

\[
 P_S=\frac{\sum_{i<m}\sum_{p\in S}z_i(p)}{m\bar x}.
\]

### AR-CLOCK-004: unrestricted cycle budget

For every finite prime set \(S\) of size at most \(s\),

\[
 \boxed{P_S\le\frac{s\{2+5\ln(1+\bar x)\}}{\bar x}.}
 \tag{12}
\]

**Proof.** Apply (9) to repeated complete laps and divide by the total
height. The source term tends to zero; every other ratio is unchanged.
There is no distinctness hypothesis to obstruct this repetition. \(\square\)

If \(S\) is the union of all prime factors of the cycle, then

\[
 \bar x\le s\{2+5\ln(1+\bar x)\}.
 \tag{13}
\]

This is a statement about the number of prime divisors, not the
multiplicative rank. Prime support can be much larger than rank.

## 5. Maximum height: an ordered peak window

### AR-CLOCK-005: every cycle's maximum requires many primes

For any positive odd cycle, let \(L=\log_2\max n_i\). If \(s\ge1\)
is the number of distinct primes appearing in its states, then

\[
 \boxed{L\le s\{8+12\ln(1+L)\}<\infty,
 \qquad L<128s\ln(4s).}
 \tag{14}
\]

Equivalently, the first inequality gives the unconditional support bound
\(s\ge L/(8+12\ln(1+L))\) on every nontrivial candidate cycle.
The all-one cycle has \(s=L=0\) and is treated separately.

**Proof.** On the periodic lift take
\(N=\lfloor L\rfloor+1\) consecutive states ending at a maximum.
At distance \(d\) before the maximum, the upward bound in (3) gives
\(x_{N-1-d}\ge L-d\). Therefore

\[
 \frac{W_N}{N}\ge L-\frac{N-1}{2}\ge L/2.
 \tag{15}
\]

Every height in this window is at most \(L\), and \(x_0\le L<N\).
The first bound in (8), with
\(E(x_0)\le2L+L\ln(1+L)\), gives

\[
 Y_N(\{p\})
 \le N\{4+6\ln(1+L)\}.
 \tag{16}
\]

Sum over the \(s\) primes. Their entire height equals \(W_N\), so (15)
and (16) prove the first inequality in (14). The window may repeat cycle
positions: all return and height estimates are valid with those time
multiplicities.

For the explicit upper bound put \(L_*=128s\ln(4s)\).
For \(s\ge1\), \(\ln(4s)\le2s\), so
\(1+L_*\le257s^2\). Using \(\ln257<6\) and \(\ln4>1\),

\[
 8+12\ln(1+L_*)<80+24\ln s
 <128\ln(4s)=L_*/s.
\]

The function \(u-s\{8+12\ln(1+u)\}\) is strictly increasing for
\(u\ge L_*\), because its derivative is \(1-12s/(1+u)>0\).
Thus the first inequality in (14) cannot hold for \(L\ge L_*\).
\(\square\)

The constant 128 is deliberately loose. The result is an all-cycle
asymptotic restriction, not an optimized exclusion for a selected number
of primes or a finite-period census.

## 6. A finite-prefix maximum theorem

### AR-CLOCK-006: arbitrary prime support on an actual prefix

Suppose every state in one actual finite prefix is supported on a common
set of at most \(s\ge1\) primes. Let its source height be \(x_*\) and
its maximum height be \(L\). Then either \(L<2x_*\), or

\[
 L\le s\{12+14\ln(1+L)\}.
 \tag{17}
\]

In particular,

\[
 \boxed{L\le\max\{2x_*,128s\ln(4s)\}.}
 \tag{18}
\]

**Proof.** Let the maximum occur at index \(i\), and put
\(k=\lfloor L/2\rfloor\). If \(i<k\), then
\(L\le x_*+i<x_*+L/2\), proving the first alternative.
Otherwise use the \(N=k+1>L/2\) states ending at that maximum.
All their heights lie between \(L/2\) and \(L\). Their first height
is at most \(L<2N\). Formula (8) consequently gives
\(Y_N(\{p\})/N\le6+7\ln(1+L)\).
Summing over all support primes proves (17).
The same comparison with \(L_*=128s\ln(4s)\) works: at that value
\(12+14\ln(1+L_*)<96+28\ln s<L_*/s\), and the relevant difference
is increasing thereafter. This proves (18). \(\square\)

The support set may have been selected after the original prefix was
observed. Applying (18) to an entire infinite orbit with one fixed finite
support would bound that orbit and force eventual periodicity; it would
not by itself identify the eventual cycle as the fixed point one.

## 7. The first unsupported closing implication

These estimates do not exclude every cycle. They require a large cycle
to distribute its height over an increasing number of primes; they do
not place a conflicting upper bound on that number. Nor do they force a
bounded prime pool to retain height on an escaping fixed-source orbit.

The whole-denominator identity for a period with total division \(A\) is
still
\(n_0=C/(2^A-3^m)\), with ordinary realization requiring division by the
complete denominator. None of (6)--(18) proves that this divisibility
fails for every nontrivial positive word. The new inequalities remain
necessary conditions for any such word that does realize an ordinary
cycle.

An attempt to turn (10) into a contradiction first needs a theorem
forcing a positive height fraction into a pool of size
\(o(\bar x_N/\ln(1+\bar x_N))\), or a different conflicting cost for
the primes outside that pool. An attempt to close cycles first needs an
upper restriction incompatible with (14), or a separate full-denominator
exclusion. Those are unproved. Exact prime-flow balance alone does not
supply them; the companion finite circulations demonstrate its loss of
ordering.

## 8. Source comparison and evidence level

1. The repository's ADEL-001--007 at the head pinned in Section 1 give
   the elementary pairwise gcd estimate and earlier prime-height budgets.
   Their optimized block inequality yields a concentration scale
   \(O(s/\sqrt{\bar x})\). The localization in (6) gives instead
   \(O(s\ln(1+\bar x)/\bar x)\), with the explicit source term in (9).

2. [*Multiplicative rank, height, and energy of odd Collatz trajectories*,
   rStation Paper 137, v1](https://rstation.ai/problems/collatz/papers/137/v1)
   proves a rank-dependent maximum-height bound \(\log M=O(r^2)\),
   as well as rank and energy restrictions. Restricting its rank to prime
   support size gives an \(O(s^2)\) maximum-height bound. Formula (14)
   has the stronger \(O(s\log(s+1))\) dependence for **prime support**;
   it does not improve every rank-dependent result or the certified
   numerical rank exclusion in that paper.

3. [*Prime-power returns and multiplicative complexity of Collatz orbits*,
   rStation Paper 138, v1](https://rstation.ai/problems/collatz/papers/138/v1)
   gives prime-power return tails and joint-return entropy estimates. Its
   Sections 2 and 6 already permit a prime pool chosen after the prefix,
   and its relative-height result concerns time-density counts. Its
   maximum-free return-tail calculation can also yield (14) with different
   constants on a peak window. The localization to actual high-height
   components in (6), the sum \(\sum\ln^+x_i\), and the resulting
   height-weighted bound are the specific refinement presented here.

4. Paper 138 explicitly credits Yueer Yang,
   [*Multiplicative Rank and Quantitative Return Bounds for Collatz Orbits*](https://doi.org/10.5281/zenodo.22554650),
   6 September 2026, as a direct predecessor. That preprint has not been
   independently reconstructed in this packet; its historical relationship
   is reported through Paper 138, not silently claimed as a fresh discovery.

The cited external papers are comparison sources, not dependencies of
the elementary proofs above. Their full proof stacks and external
computational inputs are not globally endorsed by this note. No
literature-priority theorem is claimed after this limited comparison.

`check_arithmetic_closure.py` performs exact rational checks of the clock
lemma on synthetic inputs and exact arithmetic checks of the companion
circulations. It separately uses floating-point logs as sanity checks
on actual finite trajectories; those diagnostics are not exact proofs
of logarithmic inequalities. The all-size statements rest on the written
arguments, not the finite samples.
