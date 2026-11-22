# No nonzero finite-period excessive profile at any real exponent

## The strengthened theorem

**Status: written theorem, with explicit published arithmetic-progression
input. The real asymptotic conclusion is not a Lean theorem.**

The fixed-resolution obstruction extends from sublinear powers to **every
real power**, including the critical exponent one. The critical case uses
two distinct actual ordinary inverse histories at the same odd depth.
It does not use a limiting parent law or an interchange with an infinite
series.

Let U be the accelerated map on positive odd integers, and let

\[
(PF)(q)=\sum_{\substack{e\ge1\\2^eq\equiv1\pmod3}}
 \frac3{2^e}F\!\left(\frac{2^eq-1}{3}\right).
\tag{1}
\]

Let M≥1 be a fixed integer and p any real number. Suppose:

1. F is finite and nonnegative on positive odd integers and PF≤F there.
2. L is finite and positive for sufficiently large positive arguments, and
   \(L(cx+d)/L(x)\to1\) for every fixed c>0 and real d, along positive
   arguments for which the ratio is defined.
3. There is a finite nonnegative residue profile a modulo M such that

\[
\frac{F(n)}{n^pL(n)}-a(n\bmod M)\longrightarrow0
\quad(n\to\infty,\ n\text{ positive odd}).
\tag{2}
\]

**Theorem.** Every coefficient of a on a residue class containing odd
integers is zero.

This excludes a nonzero fixed finite-period leading profile. It does not
exclude an upper bound by n^pL(n), a zero profile at that normalization,
or an excessive function whose asymptotic behavior keeps changing with
the residue resolution. In particular, it is not a contradiction to the
existence of the repository's canonical envelope.

## Exact dependencies

For p<1, the theorem is Corollary B of
`FIXED_RESOLUTION_ENVELOPE_OBSTRUCTION.md`, frozen at SHA-256
`898337c461d9a9c23ac38e99a98800a02a500d51d3660bbdbac8b73fb90509e3`.
Its ternary and mixed-modulus constructions are elementary; its arbitrary
modulus statement imports the author's stated negative extension of the
arithmetic-progression sufficiency theorem.

For p≥1, this addendum uses only the **positive** arithmetic-progression
theorem of Kenneth M. Monks, *The Sufficiency of Arithmetic Progressions
for the 3x+1 Conjecture*, Proceedings of the AMS134 (2006),2861–2872,
Theorem1.1:

<https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf>.

The precise consequence needed is that the positive basin of one meets
every positive arithmetic progression. Apply sufficiency to the orbit of
one; any common future lies in its ordinary cycle{1,2}, and hence supplies
a finite actual hit of one. No convergence theorem for arbitrary positive
integers is assumed.

The remaining inputs are exact finite-word arithmetic and the elementary
positivity implication P^ell F≤F. The ordinary binary lift used below is
also proved in this packet's published `EndpointSteering.lean`, in
`orbit_shift` and `odds_shift`, at PR175 head
`2bc2ad37b490a5aea63658eaf657bc048da4532e`. The proof below reconstructs its
application. No PR180 population, density, or canonical-potential theorem
is used by the new p≥1 cases.

## 1. A zero at the unit-cycle residue spreads to every residue

Let z be any positive odd integer with a finite odd gap word W leading
to one. Let ell be the number of gaps and B their sum, so

\[
U^\ell(z)=1,\qquad T^B(z)=1,
\]

and the first B shortcut inputs contain exactly ell odd inputs. For the
fixed modulus M, define

\[
q_t=1+2M3^\ell t,
\qquad x_t=z+2^{B+1}Mt,
\qquad t=1,2,\ldots.
\tag{3}
\]

The source shift is a multiple of2^B, so it preserves the entire actual
binary prefix, including its gap word W. Its endpoint shift is
3^ell times the quotient of that source shift by2^B. Consequently

\[
U^\ell(x_t)=q_t,
\quad x_t\equiv z\pmod M,
\quad q_t\equiv1\pmod M.
\tag{4}
\]

Every source, endpoint, and intermediate trajectory value is positive.
The initial and terminal values are odd, and the preserved gap word has
exact valuations. This is ordinary binary lifting of a supplied complete
word, not an inference from a terminal congruence alone.

Keeping this one actual word in P^ell F(q_t)≤F(q_t) gives

\[
F(q_t)\ge \frac{3^\ell}{2^B}F(x_t).
\tag{5}
\]

Because x_t/q_t→2^B/3^ell, assumptions on L and the profile imply

\[
a(1\bmod M)\ge
\left(\frac{3^\ell}{2^B}\right)^{1-p}a(z\bmod M).
\tag{6}
\]

The coefficient is positive for every real p. Thus a zero at residue one
forces a zero at the residue of every such z.

For each residue modulo M containing odd integers, take a positive odd
representative z_0 and the arithmetic progression z_0+2M N. Monks's
positive theorem supplies a member z in the basin of one. Applying (6)
therefore spreads a(1)=0 to all relevant residue classes. The progression,
its selected finite word, and both clocks are fixed before t tends to
infinity. No bound on the word length or uniform-in-depth limit is needed.

## 2. Powers above one: the positive unit cycle

Assume p>1. Use the actual targets and their exact gap-two parents

\[
q_t=1+6Mt,
\qquad x_t=1+8Mt,
\qquad 3x_t+1=4q_t.
\tag{7}
\]

Both are positive odd integers in residue one modulo M. Their single
inverse contribution gives F(q_t)≥(3/4)F(x_t). Taking its normalized
finite limit yields

\[
a(1)\ge(3/4)^{1-p}a(1).
\]

Here (3/4)^(1−p)>1, so a(1)=0 by nonnegativity. Section1 then gives
the theorem for p>1.

The sign of the exponent is essential: the negative fixed point supplies
the expanding normalized self term for p<1 in the earlier packet, while
the positive unit cycle supplies it for p>1 here.

## 3. The critical exponent: two distinct histories at equal odd depth

Assume p=1. A single normalized history has limiting weight one, so the
strict self-term argument alone gives no contradiction. We instead keep
two distinct histories in the same finite iterate P^ell.

Apply Monks to the positive arithmetic progression

\[
1+2M+2M\mathbb N.
\]

It supplies a positive odd z>1, congruent to one modulo M, with a finite
odd gap word W to one. Write ell≥1 for its number of gaps and B for
their sum. The word W is different from the length-ell word

\[
E=(2,2,\ldots,2).
\]

Indeed the unique source of the complete word E is one: its inverse
gap-two map sends one to one at every letter. Thus E cannot be the
complete word of z>1.

Lift both histories to the **same positive target**

\[
q_t=1+2M3^\ell t.
\]

Their sources are

\[
x_t=z+2^{B+1}Mt,
\qquad
y_t=1+2^{2\ell+1}Mt.
\tag{8}
\]

The first has exact gap word W and shortcut clock B; the second has
exact gap word E and shortcut clock2ell. Both have the same **odd
depth ell**, so they are separate terms of the same P^ell parent sum.
Every source is positive odd and in residue one modulo M.

The two sources cannot coincide. If they did, determinism of the actual
accelerated map would give the same first ell exact gaps from that
ordinary source, forcing W=E. The distinctness argument is what permits
adding the two contributions; they are not two descriptions of one
ancestor.

Keeping both actual terms gives

\[
F(q_t)\ge
\frac{3^\ell}{2^B}F(x_t)
+\frac{3^\ell}{2^{2\ell}}F(y_t).
\tag{9}
\]

At p=1 each coefficient times its source-to-target growth factor is
exactly one. Dividing (9) by q_t L(q_t) and taking the limit therefore
gives

\[
a(1)\ge a(1)+a(1)=2a(1).
\]

Nonnegativity forces a(1)=0. Section1 propagates that zero to every
odd-bearing residue class. This proves the critical case and completes
the all-real-exponent theorem.

## Scope of the strengthening

The new argument closes the exponent-one exception within the excluded
profile architecture and handles every superlinear exponent as well.
The arbitrary modulus statement imports the specific published
arithmetic-progression theorem; all transport thereafter concerns
explicit finite ordinary histories with nonnegative kernel weights.
There is no tail interchange, no random-source independence premise,
and no substitution of a negative ordinary orbit for a positive one in
the p≥1 cases.

The theorem still leaves the intended global Collatz step open. It does
not construct or bound the irregular canonical excessive envelope at
moving ordinary targets. Nor does it supply convergence of an arbitrary
source: the only basin points selected in this proof are the finite
witnesses supplied by the arithmetic-progression theorem.
