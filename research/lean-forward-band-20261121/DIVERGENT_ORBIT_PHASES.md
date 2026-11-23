# Disjoint incoming branches force finite phase error on a divergent orbit

## Precise dependency and conclusion

Assume the uniform predecessor-density conclusion of PR180: there is an
absolute `c_0 > 0` such that every positive ternary-unit integer `b` satisfies

\[
 \liminf_{X\to\infty}\frac1{\log X}
       \sum_{\substack{n\le X\\n\to b}}\frac1n
                   \ge\frac{c_0}{b}.                 \tag{P}
\]

Here `n -> b` means an actual finite ordinary shortcut path. The constants
in the existing note permit `c_0=c/(44 log(64/3))`; its precise numerical
value is unnecessary below.

Let `q_0,q_1,...` be a positive odd ternary-unit orbit of the accelerated
map `U`, and suppose its entries are **all distinct**. This is the hypothesis
of a divergent orbit, not merely that its initial point is not periodic.
Then

\[
                     \sum_{i\ge0}\frac1{q_i}
                              \le\frac{22}{c_0}.      \tag{R}
\]

Consequently the cumulative binary-logarithmic perturbation is finite, and
the odd orbit's binary logarithms approach one irrational rotation on the
circle. Its odd terms obey the base-2 Benford law. Together with PR173's
universal visit theorem, this also says that its visits to the marked
section would be infinite but have zero asymptotic frequency in odd time.
These conclusions do not exclude such an orbit.

## 1. Two small unit parents and one off-orbit choice

For any positive odd unit `q`, exactly three exponents in `{1,...,6}` make

\[
                          b=(2^e q-1)/3
\]

integral. They have one parity. The corresponding values `2^e q` modulo nine
run through `1,4,7`; exactly one gives `3 | b`. Thus exactly two of the six
choices give a positive odd ternary-unit parent. Each satisfies

\[
                            b<(64/3)q<22q.            \tag{1.1}
\]

For the distinct forward orbit `q_i`, at most one of those parents can be
any member of that entire orbit. Indeed, if `b=q_j` and `U(b)=q_i`, then
`q_(j+1)=q_i`; distinctness forces `j+1=i`. For `i=0` there is no such
nonnegative `j`.

Choose a unit parent `b_i` which does not belong to the forward orbit.
It is not periodic: its forward orbit immediately enters the nonrepeating
orbit at `q_i`. Its ordinary trajectory consists of `b_i`, some even
halvings, and then the odd terms `q_i,q_(i+1),...`.

## 2. The full predecessor sets are pairwise disjoint

Write `P_i={n>0:n -> b_i}`. If an integer lay in both `P_i` and `P_j`, its
deterministic trajectory would contain both odd numbers `b_i,b_j`.
At equal clocks they would be equal, which would force `q_i=q_j` and
`i=j`. At unequal clocks, the later one would be an odd point on the earlier
one's forward orbit, hence one of the `q_k`. That contradicts its off-orbit
choice. Therefore the `P_i` are pairwise disjoint.

For each finite `m`, disjointness gives

\[
 \sum_{i<m}\sum_{\substack{n\le X\\n\in P_i}}\frac1n
                      \le\sum_{n\le X}\frac1n.
\]

Divide by `log X`. The right side tends to one, while a finite sum of lower
limits is at most the lower limit of the sum. Equation (P) therefore gives

\[
                         c_0\sum_{i<m}\frac1{b_i}\le1.
\]

Since `b_i<22q_i`,

\[
                         \sum_{i<m}\frac1{q_i}
                         \le22\sum_{i<m}\frac1{b_i}
                         \le22/c_0.
\]

Taking increasing finite partial sums proves (R). No exchange of an infinite
sum with a density limit is used.

## 3. A convergent real phase correction

Write `3q_i+1=2^(a_i)q_(i+1)` with `a_i>=1`, and set

\[
 \alpha=\log_2 3,\qquad
 \epsilon_i=\log_2\left(1+\frac1{3q_i}\right).
\]

Then

\[
 \log_2 q_{i+1}=\log_2 q_i+\alpha-a_i+\epsilon_i,
 \qquad
 0<\epsilon_i\le\frac1{3\log2}\frac1{q_i}.
\]

Thus

\[
 \sum_i\epsilon_i\le\frac{22}{3c_0\log2}<\infty.
\]

Put

\[
 A_n=\sum_{i<n}a_i,\qquad
 \theta=\log_2 q_0+\sum_{i\ge0}\epsilon_i,\qquad
 r_n=\sum_{i\ge n}\epsilon_i.
\]

The exact identity is

\[
                 \log_2 q_n=n\alpha-A_n+\theta-r_n,
                    \qquad r_n\downarrow0.           \tag{3.1}
\]

Modulo one, the orbit is therefore at circular distance at most `r_n` from
`n alpha+theta`. The number `alpha` is irrational, since otherwise a
positive power of three would equal a positive power of two.

For any continuous one-periodic function, uniform continuity and `r_n -> 0`
show that its averages along the two phase sequences differ by `o(1)`.
Irrational-rotation equidistribution then proves equidistribution of
`{log_2 q_n}`. In particular, for `1 <= u < v <= 2`,

\[
 \lim_{N\to\infty}\frac1N\#\left\{n<N:
 u\le\frac{q_n}{2^{\lfloor\log_2q_n\rfloor}}<v\right\}
                           =\log_2(v/u).             \tag{3.2}
\]

This is the base-2 Benford assertion for **odd accelerated time**.
No assertion about equidistribution under every ordinary halving clock is
made; that would require analyzing its variable time weights.

## 4. What follows for the shrinking section

Distinct positive integers `q_n` eventually leave every finite set, so
`d_n=floor(log_2 q_n)` tends to infinity. The marked section requires

\[
 \{\log_2 q_n\}\le
                \log_2\left(1+\frac{70}{d_n+1}\right),
\]

whose right side tends to zero. For any fixed `eta>0`, all sufficiently late
marked phases lie in `[0,eta]`. Equidistribution bounds their upper frequency
by `eta`. Letting `eta` tend to zero shows that marked visits have odd-time
frequency zero.

On the other hand, PR173 gives a future marked visit from every positive
tail state. A nonrepeating orbit therefore has infinitely many marked
visits. If `i_j` is the odd-time index of the j-th marked visit, then
`i_j/j -> infinity`. Thus the mean of the first j odd return gaps tends to
infinity; individual gaps need not do so. Ordinary shortcut clocks are at
least as large, so their corresponding mean return gap also tends to infinity.

No rate for `r_n -> 0` follows from (R). In particular, one cannot replace
the actual perturbed phase by the limiting rotation inside windows of width
`1/log q_n` without an additional relative error estimate. Even an exact
irrational rotation can have infinitely many visits to shrinking targets
with zero asymptotic frequency.

## 5. Last sweep-out check using the new marked fans

The marked population theorem gives another exact consequence. Let `F_a`
be the marked predecessors of a fixed unit target `a` which reach it within
`15(floor(log_2 n)+1)` ordinary clocks. Then

\[
          \sum_{n\in F_a}
                  \frac{(\lfloor\log_2 n\rfloor+1)^2}{n}
                                      =+\infty.       \tag{5.1}
\]

Indeed, each successful octave contributes at least `gamma/2`: there are
at least `gamma*2^d/(d+1)^2` sources, and each is below `2^(d+1)`.
Infinitely many disjoint successful octaves give (5.1). The unit-source
version also holds using the optional appendix.

This shows precisely why a bounded-clock sweep-out does not itself give a
bounded incoming column at the squared-logarithmic harmonic weight: a
single supplied target already receives infinite mass. At the ordinary
harmonic weight `1/n`, the guaranteed contribution from one octave is only
`gamma/(2(d+1)^2)`. Even summing that guarantee over every octave would
converge. It therefore does not force a contradictory infinite harmonic
trace on the shrinking section.

For equal-clock predecessors of a nonperiodic target, their full predecessor
subtrees are disjoint. When applying (P), retain unit equal-clock sources,
as supplied by the optional unit-source appendix. Summing their available lower density coefficients
still incurs the factor `1/source`; that normalization does not disappear
under renewal. No upper bound on the actual surviving marked population has
been obtained from these sums.

## Closure status

The disjoint-branch argument proves the reciprocal summability and the
asymptotic rotation law conditional on (P). It rules out a divergent odd
orbit with divergent reciprocal sum, including one bounded above by a
constant multiple of its time index. It does not rule out divergent orbits
with summable reciprocal values, additional cycles, or a positive survivor
population. The all-large-band survivor upper estimate remains unproved.
