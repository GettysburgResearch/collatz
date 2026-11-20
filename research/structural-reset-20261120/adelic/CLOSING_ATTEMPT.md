# Attempt to close the prime-height bridge

**Status: exploratory; the closing implication remains OPEN.** The main
dispersion proof is frozen separately in `PRIME_HEIGHT_ESCAPE.md`.
The calculations here test whether ordinary integrality, exact prime
flux, or finite representation complexity force the opposite behavior.
They do not produce a Collatz counterexample or an escape exclusion.

## 1. What a successful contradiction would have to establish

For a positive odd trajectory, write

\[
 x_j=\log_2n_j,\qquad W_N=\sum_{j<N}x_j,
 \qquad
 \nu_N(p)=\frac{\sum_{j<N}v_p(n_j)\log_2p}{W_N}.
\]

On every hypothetical nonperiodic ordinary orbit, the main theorem gives

\[
 \max_p\nu_N(p)\longrightarrow0.
 \tag{1}
\]

Thus it would suffice to derive a positive limsup for the mass of a
uniformly bounded number of primes from one fixed surviving source.
The primes could change with the horizon. This is weaker than asking
one fixed prime set to retain mass, but substantially stronger than
saying that every individual integer has finitely many prime factors.

The following attempts examine mechanisms that might have forced that
retention. None presently does.

## 2. Exact prime flux gives an endpoint identity, not retention

The recurrence is
\(3n_j+1=2^{a_j}n_{j+1}\). For every odd prime \(p\),

\[
 v_p(3n_j+1)=v_p(n_{j+1}),
\]

so summing gives the exact flux balance

\[
 \sum_{j<N}\bigl(v_p(3n_j+1)-v_p(n_j)\bigr)
 =v_p(n_N)-v_p(n_0).
 \tag{2}
\]

For any finite odd-prime set \(S\), weighting (2) by \(\log_2p\) gives

\[
 \sum_{j<N}\log_2[3n_j+1]_S-
 \sum_{j<N}\log_2[n_j]_S
 =\log_2[n_N]_S-\log_2[n_0]_S.
 \tag{3}
\]

This looked promising because it exactly preserves the accumulated
prime accounting. It does not preserve any fixed prime-height share:
both sums in (3) can be small relative to \(W_N\), uniformly over all
bounded-size \(S\), while the total mass sits among increasingly many
primes. The equation telescopes through the actual next state and
supplies no lower bound for either sum.

The real identity is equally exact:

\[
 \sum_{j<N}a_j
 =N\log_2 3+\sum_{j<N}\log_2(1+1/(3n_j))
 +x_0-x_N.
 \tag{4}
\]

It controls total division and height growth. It contains no term
forcing retention at particular finite primes. Combining (3) and (4)
therefore reproduces the product formula rather than adding a new
independent sign or saving.

**First unsupported step in this attempt:** replacing the exact endpoint
balance (3) by a positive retained fraction of \(W_N\). There is no
inequality in that direction in the calculation.

## 3. Fixed p-adic recurrence is below the required scale

Even a theorem giving positive-frequency visits to a prescribed residue
class modulo \(p^k\), with \(p,k\) fixed, would only force a constant
amount of \(p\)-height per counted visit. That produces a lower bound
of order \(N\). On a nonperiodic ordinary orbit, however,

\[
 \frac{W_N}{N}\longrightarrow\infty.
\]

An order-\(N\) lower bound is compatible with (1). The required bridge
would need valuations growing with the ordinary height--for example,
enough visits with \(v_p(n_j)\log p\) comparable to \(\log n_j\)--or
another estimate of comparable cumulative strength. A finite congruence
automaton or fixed modulus does not supply that conclusion.

There is also no inherited-prime conservation: adjacent odd states are
coprime, since every common divisor divides \(3n_j+1-3n_j=1\).
Reappearance of the same prime occurs only at longer gaps, precisely
where the main gcd bound charges it to height variation.

**First unsupported step in this attempt:** moving from recurrence in
fixed residues to recurrence in a modulus whose logarithm is a positive
fraction of the visited state's height.

## 4. A fixed-source ordinary control defeats generic complexity arguments

Consider the explicit comparison recurrence

\[
 u_0=5,\qquad u_{j+1}=u_j+2,
 \quad\text{so}\quad u_j=2j+5.
 \tag{5}
\]

This is **not** a Collatz trajectory. It is a control for proposed
arguments using only a fixed ordinary seed, finite binary and ternary
expansions at every time, a short deterministic rule, bounded upward
logarithmic growth, and small pairwise gcds.

It has all those properties. In particular
\(u_{j+1}/u_j\le7/5<3/2\), and
\(\gcd(u_i,u_j)\mid2(j-i)\). Nonetheless its accumulated prime-height
mass disperses uniformly over every bounded number of primes.

To prove this last statement directly, set \(M=2N+3\), the largest of
the first \(N\) values. All these values are odd. For every odd prime
\(p\), the congruence \(2j+5\equiv0\pmod{p^k}\) has exactly one
residue class in \(j\). Hence

\[
 \sum_{j<N}v_p(2j+5)
 \le \sum_{k\le\log_pM}(N/p^k+1)
 \le\frac{N}{p-1}+\log_pM.
\]

Multiplying by \(\log_2p\), and using
\(\log_2p\le p-1\), gives, uniformly in \(p\),

\[
 \sum_{j<N}v_p(u_j)\log_2p\le N+\log_2M.
 \tag{6}
\]

At least \(\lfloor N/2\rfloor\) of the first \(N\) values are at
least \(N\), so their total logarithmic height is at least
\(\lfloor N/2\rfloor\log_2N\). Equations (5)--(6) therefore imply

\[
 \sup_{|S|\le s}
 \frac{\sum_{j<N}\log_2[u_j]_S}{\sum_{j<N}\log_2u_j}
 \longrightarrow0
 \tag{7}
\]

for every fixed \(s\). The same fixed seed and short program generate
the entire history; no moving-source compactness loophole is involved.

Thus ordinary finite representation, low algorithmic description length,
small growth per step, and gcd separation do not themselves force the
desired retention. This does not refute a retention theorem that uses
the exact \(3n+1\) recurrence. It identifies the additional arithmetic
that such a theorem would need to exploit.

## 5. What remains after this attempt

The prime-height route now has an elementary necessary condition on
every hypothetical escape, an explicit finite-history inequality, and
an unrestricted cycle concentration bound. The attempted converse
mechanisms above yield either an exact identity or a bound on the wrong
scale. The comparison (5) prevents promoting their generic ingredients
to a universal concentration principle.

A successful continuation must force repeated large prime-power content,
control a growing collection of relevant primes in a way incompatible
with (1), or discover a different arithmetic obstruction to the diffuse
case. None of those statements is established here. The first unsupported
implication is therefore still the source-persistent retention or an
equivalent conflicting arithmetic theorem, with arbitrary cycle
exclusion remaining a separate problem.
