# The rational cycle obstruction survives any finite set of places

**PROPOSED, elementary extension of AR1.** This note concerns changing
noninteger rational witnesses. It provides no fixed ordinary divergent
orbit. It isolates where a proposed product-formula closure must use
global integrality, rather than finitely many congruences.

## FP1. Additional finite prime-power observations

In [AR1](ADIC_REAL_DENSITY.md), additionally fix a positive integer Q
coprime to six and any residue z_Q modulo Q. The noninteger cycle roots
may be chosen to satisfy
\[
 r\equiv z_Q\pmod Q,\qquad \gcd(\operatorname{den}(r),Q)=1,
\]
while preserving the prescribed real neighborhood, binary cylinder,
ternary-unit cylinder, and positive lap score 8q-5N. There are infinitely
many such roots, with unbounded reduced denominators.

Here a congruence of a rational is interpreted only when its reduced
denominator is a unit modulo the modulus. A single Q can encode any
finite collection of observations at primes other than two and three.

### A finite modular control word

Work first modulo Q>1. Both E(x)=x/2 and O(x)=(3x+1)/2 are affine
permutations, so the semigroup they generate is a finite group: the
inverse of each generator is a positive power of that generator. This
group contains all translations. To see this, put
\[
 A=E^{-1}\circ O=3x+1,\qquad
 B=O\circ E^{-1}=3x+1/2.
\]
Then A composed with B^{-1} is the translation x->x+1/2. Since one-half
is a unit modulo Q, its integer iterates give every translation modulo Q.
The group also contains the scaling x->2x=E^{-1}(x).

Let w be the original binary prefix from AR1. Choose a_0 as in AR1 so
that -2^{-a_0} is the required residue modulo 3^M, taking a_0=0 when
M=0. Let S(x)=2x-z_Q. The preceding group calculation produces a finite
positive word v in E and O whose affine action modulo Q is
\[
 F_v=E^{-a_0}\circ S\circ F_w^{-1}.
\]
Therefore the longer prefix u=w v satisfies
\[
 F_u=E^{-a_0}\circ S\pmod Q.                            \tag{1}
\]
It retains the first K prescribed binary letters. The new word v is
fixed once the local observations have been fixed. It is not claimed to
be the ordinary continuation of the supplied binary representative.

Let e be the order of two modulo Q, and let f be the order of 3/2
modulo Q. The identity O^b(x)+1=(3/2)^b(x+1) shows O^b is the identity
modulo Q when b is a multiple of f. Take
\[
 a\equiv a_0\pmod{\operatorname{lcm}(P,e)},\qquad
 b\equiv0\pmod f,                                     \tag{2}
\]
where P=2*3^{M-1} for M>0 and P=1 for M=0.

For the full cyclic word u 1^b 0^a, its return map modulo Q is
E^{a_0} composed with F_u, hence exactly S(x)=2x-z_Q.
Write its full affine formula as (3^q x+C)/2^N. It follows that
\[
 2^N-3^q\equiv-2^N\pmod Q,
 \qquad C\equiv-z_Q2^N\pmod Q.                         \tag{3}
\]
The fixed-point denominator is thus a unit modulo Q, and its fixed
point is z_Q modulo Q. These statements remain true after reducing the
fraction.

### Real tuning still works

Use the real coefficients F_u(x)=Ax+B in the AR1 fixed-point formula.
To approach the real target x_*, seek
\[
 b\log_2(3/2)-a\longrightarrow
 \log_2\frac{x_*}{Ax_*+B+1}
\]
under (2). The multiples of f log_2(3/2) are still an irrational
rotation modulo lcm(P,e), so the same density argument applies.
Both a and b tend to infinity and a/b tends to log_2(3/2).
All AR1 proofs of positivity, exact parity legality, ternary congruence,
positive lap score, and denominator growth apply with u as the fixed
prefix. Binary agreement holds at least through the original prefix w.
For Q=1 no control word or extra restriction is needed.

This proves FP1. No claim that the entire affine permutation group is
generated is needed; translations and scaling by two suffice.

## Why this is not an all-place counterexample

Every nontrivial reduced denominator supplied by FP1 is coprime to 6Q.
Its prime divisors lie outside the controlled finite set. The construction
therefore does not give a noninteger rational integral at every prime.
Indeed a reduced rational integral at every prime has denominator one.

At a particular ordinary integer n, if the binary, ternary, and extra
congruences all agree with n, the denominator cost is
\[
 \operatorname{den}(r)\,|r-n|\ge2^K3^M Q.               \tag{4}
\]
This is the same nonzero-integer divisibility argument as AR2. Thus
congruences at more places force a larger denominator; they do not remove
the changing-witness issue.

The fixed-source pins in [FS1](FIXED_SOURCE_CLOSURE.md) have their own exact
height identity. To force a return using (4), a proof still needs a
quantitative estimate that exceeds that identity's integer threshold.
Merely declaring a finite set of good places cannot provide it.

## Source and evidence scope

This is an extension of the self-contained AR1 proof, using only finite
affine-group arithmetic and irrational rotation. The same comparisons
with PR149 at `92c0129e794dde3ec55ceec470a12d51ba3f7e2f` and classical
real rational-cycle density apply. No broad literature-priority claim is
made for FP1.

`check_finite_places.py` constructs the modular control word by a bounded
finite group search and checks the resulting rational cycles exactly.
Its finite success checks the interface, not the arbitrary-modulus
theorem. It does not reinterpret the modular control word as an actual
continuation of the original ordinary source.

Four finite witnesses passed for the extra moduli 5, 91, 35, and 25,
including nonunit residues at controlled primes. The replay checked
5,954 shortcut edges and 3,748 accelerated edges, exact denominator
coprimality and congruences, real neighborhoods, and positive lap scores.
Normal and `-OO` reports were byte-identical in
`finite-places-report.json`.
