# The required pure powers lose smoothness at their first descent

**PROPOSED, elementary exact family.** This is a scoped obstruction to
inferring future smoothness from a smooth starting integer. It is not a
counterexample to Collatz and not an obstruction to every fixed-source
upper bound.

Use the positive odd map
\(U(n)=(3n+1)/2^{v_2(3n+1)}\). For a finite prime set
\(P\supseteq\{2,3\}\), define
\(R_P(m)=m/\prod_{p\in P}p^{v_p(m)}\).

## PP1. Exact first descent in PR146's pure-power progression

PR146 at `e238c63a5d57f96bb063b7472498d1977df51951`,
`research/upper-bit-mergers/DEEP_REVERSE_BASIN.md`, identifies the
minimum-rank reverse implication with convergence of
\(3^{27j-1}\), \(j\ge1\). Take its infinite subprogression
\(j=4r+3\), \(r\ge0\), and set

\[
n=3^{108r+80}.
\]

Then the very first accelerated step is a strict numerical descent:

\[
v_2(3n+1)=2,\qquad
u=U(n)=\frac{3^{108r+81}+1}{4}<n.
\tag{1}
\]

Nevertheless its shifted core is exactly

\[
\boxed{R_{\{2,3\}}(u+1)
       =\frac{3^{108r+81}+5}{8}
       =\frac{3n+5}{8}.}
\tag{2}
\]

**Proof.** The exponent \(108r+81\) is one modulo four.
Thus \(3^{108r+81}\equiv3\pmod{16}\). Its sum with one has
2-adic valuation exactly two, proving the valuation in (1).
Because \(n>1\), \((3n+1)/4<n\). Its sum with five has
2-adic valuation exactly three and is prime to three. Therefore
\(u+1=(3^{108r+81}+5)/4\) has 2-adic valuation one and
3-adic valuation zero, proving (2). All sources and endpoints are
positive ordinary integers. \(\square\)

The right side of (2) is unbounded and is asymptotic to \(3n/8\).
So even within the exact pure-power family required by PR146, a
successful first descent does not leave a bounded shifted core.
The upper antecedent has fixed first-hit odd rank four in that
reduction, while these cores have no uniform bound.

This does not show that any of these powers fails to converge.
Nor does it refute an upper bound depending on the entire numerical
source, or an accumulated bound along one fixed future. The parameter
\(r\) changes the source.

## PP2. Arbitrarily large outside-pool height at one descending step

The preceding mechanism is not tied to the pool \(\{2,3\}\) if
the pure-power exponent is unrestricted. Fix any finite prime pool
\(P\supseteq\{2,3\}\). Let \(L\) be a common multiple of
\(\operatorname{ord}_p(3)\) for every \(p\in P\setminus\{2,3\}\),
taking \(L=1\) when the list is empty. For every positive multiple
\(k\) of \(L\), put

\[
n=3^{4k},\qquad u=U(n)=\frac{3^{4k+1}+1}{4}.
\]

Then

\[
\boxed{u<n,\quad R_P(u)=u,\quad
       R_P(u+1)=\frac{3^{4k+1}+5}{8}.}
\tag{3}
\]

**Proof.** The same modulo-16 calculation gives the exact divisions
and \(u<n\). For every extra prime \(p\in P\), the choice of
\(k\) gives \(3^{4k+1}\equiv3\pmod p\). Consequently
\(u\equiv1\pmod p\) and
\((3^{4k+1}+5)/8\equiv1\pmod p\). The two displayed values are
odd and prime to three, so every prime in \(P\) is absent. This
proves (3). \(\square\)

The starting integer has prime support exactly \(\{3\}\), whereas
both the entire next ordinary value and almost half its shifted value
have all their prime factors outside the prescribed pool. Both outside
quantities grow without bound while the first-step valuation stays two.

Thus no finite local upper bound depending only on the initial prime
support, the division exponent, and \(P\) can control the newly
created outside-pool height. The source value or another unbounded
resource must enter such a bound. This is a direct pure-power version
of the new-core obstruction, not a claim that the shifted core of the
initial pure power was itself one.

## Remaining global task

The ordered return estimates in PR159
`0e7d2841b1591073c6399f91f3b6944ebcdbdbd5`,
`PRIME_SUPPORT_PEAKS.md`, and PR160
`6d877e718f5ef9d57fe1830912c444359718747a`,
`arithmetic/CLOCK_HEIGHT.md`, constrain a common prime pool across an
actual history. Neither permits replacement of that common pool by the
support of the initial value alone. Equations (1)--(3) make the missing
inference concrete for the pure powers now arising in PR146.

A full proof still needs to control the subsequent ordinary orbit of
\(u\). The inequality \(u<n\) does not close induction on pure-power
exponents because \(u\) is generally not another pure power. It also
does not give a certificate for every smaller ordinary integer. No
source-persistent bound on future core creation is proved here.
