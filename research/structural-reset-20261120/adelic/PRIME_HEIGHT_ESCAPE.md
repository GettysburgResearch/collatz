# Elementary prime-height dispersion for arbitrary ordinary schedules

**Status: PROPOSED, complete elementary written proof, pending narrow
independent review.** No external analytic theorem is required. The
results constrain hypothetical escapes and arbitrary positive cycles;
they do not prove Collatz.

Frozen input: `55d8968d2ecbc23a91c9c4733929f34be9bf0d28`.

## 1. Map, ordinary domain, and quantities

Use the positive odd accelerated map

\[
 U(n)=\frac{3n+1}{2^{v_2(3n+1)}},\qquad n\in2\mathbb N+1.
 \tag{1}
\]

This is a section of the repository's shortcut map. Write

\[
 n_{j+1}=U(n_j),\quad a_j=v_2(3n_j+1)\ge1,\quad
 x_j=\log_2 n_j.
 \tag{2}
\]

All states are actual positive ordinary integers. A repeated state makes
the deterministic orbit eventually periodic. Hence a non-eventually-
periodic orbit has distinct states, \(n_j\to\infty\), and \(x_j\to\infty\).
A primitive odd cycle of period \(m\) has \(m\) distinct positive odd
states. These ordinary facts are not inferred from p-adic admissibility.

For a finite prime set \(S\), put

\[
 [n]_S=\prod_{p\in S}p^{v_p(n)},\qquad
 y_j(S)=\log_2[n_j]_S,\qquad
 W_N=\sum_{j<N}x_j,\quad Y_N(S)=\sum_{j<N}y_j(S).
 \tag{3}
\]

Always \(0\le y_j(S)\le x_j\). Fix an integer \(s\ge1\), and allow
any \(S\) with \(|S|\le s\). Every bound below is uniform over the
actual primes in \(S\). Within a prefix, \(S\) is one set shared by
all its states; it may be chosen after the prefix is observed and may
change between prefixes. The theorem does not allow a separate set of
\(s\) primes for each individual state.

## 2. Ordinary gcd control from the affine correction

### ADEL-001: a pairwise estimate with no valuation cutoff

For any two times \(i<j\), put \(d=j-i\). Then

\[
 \boxed{\log_2\gcd(n_i,n_j)<x_i-x_j+3d.}
 \tag{4}
\]

The right side is positive whenever it bounds a nontrivial gcd; the
strict inequality is also valid when the gcd is 1.

**Proof.** Let \(B_t=\sum_{u=i}^{i+t-1}a_u\), so \(B_0=0\), and
write \(B=B_d\). Iterating the exact affine relation gives

\[
 2^B n_j=3^d n_i+C,
 \qquad
 C=\sum_{t=0}^{d-1}3^{d-1-t}2^{B_t}>0.
 \tag{5}
\]

The gcd divides \(C\). Since every remaining exponent is at least one,
\(B-B_t\ge d-t\), and therefore

\[
 \frac C{2^B}
 \le\sum_{u=1}^d\frac{3^{u-1}}{2^u}
 =\left(\frac32\right)^d-1
 <\left(\frac32\right)^d.
 \tag{6}
\]

On the other hand, logarithms of (1) give exactly

\[
 x_{u+1}-x_u=b_u-a_u,
 \qquad b_u=\log_2(3+1/n_u)\le2.
 \tag{7}
\]

Thus \(B=x_i-x_j+\sum_{u=i}^{j-1}b_u\le x_i-x_j+2d\). Combining
this with (6) and \(\log_2(3/2)<1\) proves (4). \(\square\)

No upper bound on any \(a_u\) was used. Large divisions appear as
downward changes in \(x\), and will be paid for by variation.

## 3. A block can concentrate only limited prime height

Take any consecutive block \(B\) of \(r\ge2\) states. Define

\[
 H_B=\sum_{j\in B}x_j,\quad M_B=\max_{j\in B}x_j,\quad
 R_B=\max_{j\in B}x_j-\min_{j\in B}x_j.
\]

### ADEL-002: the local prime-height budget

For every \(|S|\le s\),

\[
 \boxed{\sum_{j\in B}y_j(S)
 \le\frac{s}{r}H_B+srR_B+3sr^2.}
 \tag{8}
\]

**Proof.** For each prime \(p\in S\), select a state in the block where
\(v_p(n_j)\) is maximal. At that one state its \(p\)-height is at most
\(M_B\). At every other state the entire power of \(p\) divides the
gcd with the selected state. Order the two indices and apply (4):
its \(p\)-height is less than \(R_B+3r\). Hence

\[
 \sum_{j\in B}y_j(S)
 \le sM_B+s(r-1)(R_B+3r).
\]

Since \(M_B\le H_B/r+R_B\), this is at most
\(sH_B/r+srR_B+3sr(r-1)\), which proves the conservative bound (8).
\(\square\)

A companion observation will be useful for counting: outside the union
of the at most \(s\) selected states, every state satisfies

\[
 y_j(S)\le s(R_B+3r).
 \tag{9}
\]

Neither the constants nor the choice of block depends on which primes
were selected. Ties in maximal valuation can be resolved arbitrarily.

## 4. Total height variation is an ordinary finite resource

From (7) and \(a_u\ge1\), every upward increment of \(x\) is at most 1.
For a finite prefix let \(P\) be the sum of positive increments and \(D\)
the sum of the magnitudes of negative increments. Over \(N\) transitions,
\(P\le N\), and telescoping gives \(D=P+x_0-x_N\). Consequently,

\[
 \sum_{j<N}|x_{j+1}-x_j|
 =P+D\le2N+x_0.
 \tag{10}
\]

For any disjoint collection of state blocks contained in the prefix,
the sum of their ranges is at most this total variation:

\[
 \sum_B R_B\le2N+x_0.
 \tag{11}
\]

The estimate includes arbitrarily large downward steps. There is no
discarded set of unsafe or high-valuation transitions.

### ADEL-003: an explicit finite-history inequality

For \(N\ge1\) and integer \(r\ge2\), put
\(M=r\lfloor N/r\rfloor\) and

\[
 B_{N,r}=\sum_{M\le j<N}x_j.
\]

Then every actual positive odd orbit prefix satisfies, simultaneously
for all \(|S|\le s\),

\[
 \boxed{Y_N(S)\le\frac{s}{r}W_N+sr x_0+5srN+B_{N,r}.}
 \tag{12}
\]

**Proof.** Partition the first \(M\) states into disjoint blocks of
length \(r\), and sum (8). The first terms sum to at most \(sW_N/r\).
The range terms are at most \(sr(2N+x_0)\) by (11). The constant terms
sum to at most \((N/r)3sr^2=3srN\). Bound \(y_j\le x_j\) on the
remaining fewer than \(r\) states. \(\square\)

This inequality is effective and purely algebraic. No exceptional
subspaces, ineffective cutoffs, infinite legal completions, or bounded
valuation alphabet enter its statement.

## 5. Uniform dispersion on any hypothetical ordinary escape

### ADEL-004: height-weighted theorem

For every non-eventually-periodic positive odd orbit and every fixed
integer \(s\ge1\),

\[
 \boxed{\sup_{|S|\le s}\frac{Y_N(S)}{W_N}\longrightarrow0.}
 \tag{13}
\]

**Proof.** Since \(x_j\to\infty\), \(N/W_N\to0\). For each fixed
\(r\), also \(B_{N,r}/W_N\to0\). Here is the needed boundary argument,
which must not silently replace downward increments by upward ones.

For any fixed \(R\ge1\), upward increments at most 1 imply

\[
 W_N\ge\sum_{k=1}^R(x_N-k)
 =R x_N-R(R+1)/2\qquad(N\ge R).
\]

First let \(N\to\infty\), then \(R\to\infty\), to obtain
\(x_N/W_N\to0\). At each fixed \(k\),

\[
 \frac{x_{N-k}}{W_N}\le\frac{x_{N-k}}{W_{N-k}}\longrightarrow0.
\]

There are fewer than \(r\) terms in \(B_{N,r}\), proving its
negligibility. Divide the uniform inequality (12) by \(W_N\) to get

\[
 \limsup_{N\to\infty}\sup_{|S|\le s}\frac{Y_N(S)}{W_N}\le s/r.
\]

The integer \(r\) is arbitrary. Let \(r\to\infty\). \(\square\)

### ADEL-005: count-weighted theorem

On the same orbit, for every fixed \(s\ge1\),

\[
 \sup_{|S|\le s}\frac1N\sum_{j<N}\frac{y_j(S)}{x_j}\longrightarrow0.
 \tag{14}
\]

Consequently, for every \(\varepsilon>0\),

\[
 \boxed{\sup_{|S|\le s}\frac1N
 \#\{j<N:[n_j]_S\ge n_j^\varepsilon\}\longrightarrow0.}
 \tag{15}
\]

**Proof.** Fix a floor \(h>0\). All sufficiently late states have
\(x_j\ge h\). Start after that finite initial segment and partition
the remaining prefix into length-\(r\) blocks.

In each block the at most \(s\) selected states from Section 3 contribute
at most \(s\) to \(\sum y_j/x_j\). At every other state, (9) and the
floor give a contribution at most \(s(R_B+3r)/h\). Thus, summing over
complete blocks and using (11), the upper density of this normalized sum
is at most

\[
 \frac{s}{r}+\frac{5sr}{h}.
 \tag{16}
\]

The finite initial segment and the fewer than \(r\) terminal terms have
zero density. All bounds are uniform in \(S\). For fixed \(r\), let
\(h\to\infty\), then let \(r\to\infty\). This proves (14).
Every index counted in (15) contributes at least \(\varepsilon\) to
the normalized sum, proving (15). \(\square\)

### Meaning and exact converse for a fixed source

For \(W_N>0\), define a probability measure on primes by

\[
 \nu_N(p)=\frac{\sum_{j<N}v_p(n_j)\log_2p}{W_N}.
 \tag{17}
\]

Its total mass is 1. The theorem says \(\max_p\nu_N(p)\to0\) on any
escape, and therefore every bounded number of primes has vanishing total
mass. This is stronger than mass merely leaving each one fixed finite
prime set: the heaviest primes may be selected anew at every horizon.

A positive odd orbit is eventually periodic if and only if, for some
fixed finite prime set \(S\) and \(0<\varepsilon\le1\), the set in
(15) has positive upper density. For an eventual cycle take all its
prime factors; for the fixed point 1, \([1]_S=1=1^\varepsilon\).
The reverse direction is (15). This is a characterization, not a proof
that every source satisfies its right-hand condition.

## 6. Consequences for arbitrary primitive positive cycles

Let a primitive positive odd cycle have period \(m\), and put

\[
 H=\frac1m\sum_{j<m}x_j,\qquad
 P_S=\frac{\sum_{j<m}y_j(S)}{\sum_{j<m}x_j}.
\]

The fixed point 1 has \(H=0\) and is omitted from ratios with that
denominator. Every other candidate cycle has \(H>0\).

### ADEL-006: unrestricted cycle concentration bound

For every integer \(r\ge2\) and \(|S|\le s\),

\[
 \boxed{P_S\le\frac{s}{r}+\frac{5sr}{H}.}
 \tag{18}
\]

**Proof.** Repeat the actual cycle indefinitely, and apply (12) at
\(N\) tending to infinity through multiples of both \(m\) and \(r\).
Then \(B_{N,r}=0\), \(W_N=NH\), and \(Y_N/W_N=P_S\). The source
term \(sr x_0/(NH)\) tends to zero. \(\square\)

Primitivity gives \(\prod_{j<m}n_j\ge m!\), hence
\(H\ge\log_2(m!)/m\to\infty\) as \(m\to\infty\). It follows
from (18) that along every family of primitive cycles with periods
tending to infinity,

\[
 \sup_{|S|\le s}P_S\longrightarrow0
 \tag{19}
\]

for each fixed \(s\). This covers all valuation words, not only words
admitting a fixed powered-factor cover.

There is a matching count statement. For every \(s,\varepsilon,\eta>0\)
there is an explicit finite constant \(C\), independent of which primes
constitute \(S\), such that every primitive cycle satisfies

\[
 \sup_{|S|\le s}\#\{j<m:[n_j]_S\ge n_j^\varepsilon\}
 \le\eta m+C.
 \tag{20}
\]

To verify this, choose a floor \(h>0\). At most
\(\lfloor2^h\rfloor\) of the distinct cycle states have \(x_j<h\).
In a repeated-cycle length-\(r\) block, remove these low states, allow
the at most \(s\) selected positions, and bound all other normalized
contributions using (9) divided by \(h\). The same variation calculation
as in (16), averaged over sufficiently many repetitions, gives

\[
 \frac1m\#\{j<m:[n_j]_S\ge n_j^\varepsilon\}
 \le\frac{2^h}{m}+
 \frac1\varepsilon\left(\frac{s}{r}+\frac{5sr}{h}\right).
 \tag{21}
\]

Choose integer \(r\ge2\) with \(s/(\varepsilon r)\le\eta/2\), then
choose \(h\) with \(5sr/(\varepsilon h)\le\eta/2\), and take
\(C=\lceil2^h\rceil\). This is an explicit but deliberately unoptimized
bound.

### ADEL-007: an elementary bounded-prime-support finiteness corollary

If the union of the prime divisors of all the odd states of a nontrivial
primitive cycle has size at most \(s\), then

\[
 H\le20s^2,\qquad m<3\cdot2^{20s^2}.
 \tag{22}
\]

**Proof.** Take \(S\) to be that union, so \(P_S=1\). Use \(r=2s\)
in (18), obtaining \(1\le1/2+10s^2/H\), which gives the first bound.
The elementary integral bound
\(\log(m!)\ge m\log m-m+1\) gives

\[
 H\ge\log_2m-\log_2e,
\]

so \(m\le e2^{20s^2}<3\cdot2^{20s^2}\).

For each fixed period \(m\), cyclic summation of (7) gives
\(\sum_{j<m}a_j=\sum_{j<m}b_j\le2m\). There are finitely many
positive integer exponent words of that length and total sum. Each word
has at most one rational fixed point, because its homogeneous slope
\(3^m/2^{\sum a_j}\) is not 1. Thus (22) yields a finite, in-principle
effectively enumerable collection of cycles, uniformly over which
\(s\) primes occur. No such enumeration is performed here. \(\square\)

The raw bounded-prime-support finiteness conclusion is also a consequence
of classical quantitative S-unit bounds, which give better numerical
period estimates. The present corollary is an elementary derivation
from the stronger prime-height concentration inequality; it is not
claimed as a newly discovered finiteness principle. See [SOURCES.md](SOURCES.md).

## 7. Boundaries and the first unsupported implication

The finite inequality (12) and the limit theorems have no bounded-alphabet,
low-complexity or finite-prime hypothesis on an escape. They say that any
ordinary escape must spread its accumulated logarithmic height over
an increasing number of primes. They do not say this is impossible.

The first missing implication toward escape exclusion is a conflicting
property of one ordinary surviving history--for example, a positive
limsup of (17) on some uniformly bounded number of primes. No such
persistent concentration estimate follows from the present proof.
Each individual integer's factorization is finite, but the union and
the occupation measure along an infinite history need not be tight.

Pointwise concentration is refuted even for actual converging integers:
for every fixed finite \(S\), there are arbitrarily large ordinary
one-step predecessors of 1 with \([n]_S=1\). The exact construction
appears in [ADELIC_LEDGER.md](ADELIC_LEDGER.md). It does not refute a
source-persistent all-time hypothesis; it rules out replacing that
hypothesis by a local or all-ancestor assertion.

For cycles, an arbitrary hypothetical cycle may use arbitrarily many
primes. Neither (18) nor (22) bounds their number universally, excludes
an isolated nontrivial cycle, or proves all prime-support classes empty.
The full cycle problem remains OPEN, separately from the escape bridge.

The elementary method uses a positive affine correction and bounded
upward logarithmic increments. Comparison systems can share these
features. Any completion must therefore provide additional arithmetic
specific enough to settle standard \(3n+1\), not merely these general
properties.
