# What GRH supplies to the current Collatz routes

**PROPOSED elementary interface results; SOURCE-QUALIFIED use of standard
GRH consequences. No full Collatz proof is obtained.** GRH is an authorized
hypothesis throughout this investigation. No assertion about a particular
announcement or proof of GRH is needed.

Use the shortcut map T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n.
All orbit statements concern positive ordinary integers. The accelerated
odd map is U(n)=(3n+1)/2^{v_2(3n+1)}.

## Sources inspected

- PR146, `e238c63a5d57f96bb063b7472498d1977df51951`:
  `DEEP_REVERSE_BASIN.md`, `SHORTER_ANCESTORS.md`, and
  `ONE_CELL_SIXTY_FOUR.md` in `research/upper-bit-mergers/`.
- PR159, `0e7d2841b1591073c6399f91f3b6944ebcdbdbd5`: the prime-support
  peak and exact boundary-circulation notes.
- PR162, `2279da37ac612dbe049777354cdedb3c0aa03282`:
  `research/creative-closure-20261120/five_closure.md` and `occupation.md`.

For analytic input, Bach and Sorenson's
[Explicit bounds for primes in residue classes](https://doi.org/10.1090/S0025-5718-96-00763-6)
gives, under ERH, a prime in every reduced class a modulo q below
2(q log q)^2. Its general statement concerns the least prime with prescribed
Frobenius in a number field. The authors' bibliographic record is available
[here](https://digitalcommons.butler.edu/facsch_papers/1121/).

The corrected v3 of Lamzouri--Li--Soundararajan is
[arXiv:1309.3595v3](https://arxiv.org/abs/1309.3595v3).
The later paper by Carneiro--Milinovich--Quesada-Herrera--Ramos,
[arXiv:2404.08380v2, section 1.2](https://arxiv.org/html/2404.08380v2),
states the sharper absolute GRH bound P(a,q)<=(phi(q) log q)^2 for q>3
and improves its asymptotic constant. We use only the coarser Bach--Sorenson
bound. Improving its constant does not change any comparison below.

These external number-theory theorems are cited, not reproved or formally
rebuilt. The new arguments below use their stated scope precisely. No
priority claim is made for the elementary periodic-label lemma or for
consequences of the parity-word bijection.

## G1. A genuine GRH consequence: small prime realizers of every parity cylinder

Let H>=2 and let b be any odd residue with 0<b<2^H. Under GRH there is a
prime p congruent to b modulo 2^H satisfying

    p < 2 (2^H H log 2)^2 < 2^(2H+1) H^2.               (1)

The first H shortcut parities of p equal those of b. Equivalently every
length-H parity word whose first input is odd has a prime ordinary realizer
with at most 2H+2 ceil(log_2 H)+1 bits.

**Proof.** The class b modulo 2^H is reduced, so the cited least-prime
bound gives (1). The standard affine prefix identity shows that the first
H parities depend only on the input modulo 2^H. The parity-word/residue
bijection supplies the converse formulation. The bit bound follows by
replacing H^2 with 2^{2 ceil(log_2 H)}. No future behavior is inferred.

For b=2^H-1, write p+1=2^H a. Its actual first H steps satisfy

    T^j(p)=3^j 2^(H-j) a-1,       0<=j<=H,             (2)

and strictly increase. Since p>=2^H-1 and the upper bound in (1) gives
log_2 p <= 2H+O(log H), these primes form an unbounded family with first
descent time greater than H and hence at least

    (1/2-o(1)) log_2 p.                                (3)

This is an actual conditional finite-orbit construction. It does not say
whether the prime subsequently converges. Selecting a prime within a binary
cylinder preserves its finite prefix; it does not preserve or prescribe
membership in a target's full predecessor basin.

## G2. Exact obstruction to a prescribed-level inverse-core repair

Fix e>=1. The multiplicative order of 2 modulo 3^e is

    ord_(3^e)(2)=2*3^(e-1),                            (4)

and 2^{3^(e-1)}=-1 modulo 3^e. These facts follow from
v_3(2^{2*3^r}-1)=r+1 and the fact that the unit group has that cardinality;
no GRH input is needed.

For an odd ternary unit n, a single inverse odd step is

    x=(2^a n-1)/3.

If the numerator is divisible by 3^e, the quotient at that prescribed
level is q=(2^a n-1)/3^e. A strict decrease q<n requires and is equivalent
to

    2^a < 3^e, or a < e log_2 3.                       (5)

Indeed q<n is (2^a-3^e)n<1. Its left coefficient is an integer, and
2^a=3^e is impossible for a,e>=1.

Now impose n=-1 modulo 3^e. By (4), divisibility is equivalent to

    a=3^(e-1) modulo 2*3^(e-1).                        (6)

For e>=3, its least positive exponent 3^(e-1) exceeds e log_2 3. At e=3
this is 9>log_2 27; multiplying the left side by three while increasing
the right side linearly proves the assertion for all larger e. Therefore
no exponent can satisfy both the prescribed divisibility and decrease (5).

This is an exact arithmetic obstruction, not the failure of a particular
estimate for the least prime. GRH cannot change the congruence (6).

**Critical scope.** A larger actual valuation e'>e can yield a smaller
fully stripped ternary core even when q at the prescribed level is large.
The result does not exclude that possibility, arbitrary levels, multiple
inverse steps, or a forward excursion followed by an inverse route.

### Exact number of residue classes admitting a short prescribed-level inverse

Put h_e=floor(log_2 3^e). There are exactly h_e unit classes n modulo 3^e
for which some a satisfies both 3^e | (2^a n-1) and (5). They are

    n=2^{-a} modulo 3^e,       1<=a<=h_e.              (7)

The classes are distinct since h_e<2*3^(e-1). Their fraction among all
unit classes is h_e/[2*3^(e-1)]. This quantifies the mismatch between a
uniform supplied residue and the desired O(e) exponent. It does not
establish a natural-density theorem for the union over unbounded levels.

## G3. The obstruction occurs on completely certified depth-one sources

For E>=3 define

    n_E=(2^(3^E+1)-1)/3.                               (8)

The exponent 3^E+1 is even, so n_E is a positive odd integer and

    3n_E+1=2^(3^E+1),       U(n_E)=1.                  (9)

Thus its complete first-hit odd certificate has depth one. Moreover

    n_E+1=2(2^(3^E)+1)/3,
    v_3(n_E+1)=E,                                     (10)

by v_3(2^m+1)=1+v_3(m) for odd m. For every prescribed level 3<=e<=E,
we have n_E=-1 modulo 3^e. Consequently the obstruction in G2 holds at
every such level, despite possession of the complete certificate (9).

The family and this strengthening were suggested by the root agent and
independently checked here. It does not make the supplied source
nonconvergent; its convergence is explicit. It rules out using short
prescribed-level inverses as a universal repair merely because the source
already has a short known certificate.

## G4. The discriminant calculation for a Chebotarev replacement

Consider the most direct field encoding of congruence information,
K=Q(zeta_(3^e)). Its degree and absolute discriminant are

    d=2*3^(e-1),
    |Delta_K|=3^[3^(e-1)(2e-1)].                       (11)

The discriminant follows from the cyclotomic formula
|Delta_(Q(zeta_q))|=q^{phi(q)}/product_{p|q}p^{phi(q)/(p-1)}.
It can also be obtained by the resultant of Phi_(3^e) with its derivative.

Thus log|Delta_K| is of order e*3^e. The standard GRH least-prime
Chebotarev scale (log|Delta_K|+d)^2 is of order

    e^2*9^e.                                          (12)

For prescribed rational residue classes the same scale follows from the
least-prime bound. If that prime is proposed as the inverse exponent a,
the guaranteed size is exponentially larger than the O(e) allowance in
(5). The unrestricted integer exponent already has a representative below
2*3^(e-1), so imposing primality does not improve that existing guarantee.
For the obstructing class (6), all its exponents are divisible by 3 when
e>=2; at e>=3 there is no prime exponent in the class at all.

If instead the prime is an auxiliary source or cofactor, Chebotarev only
certifies the specified Frobenius/congruence properties. An actual ordinary
path to the supplied target still needs its endpoint equality, every inverse
division, positivity, and the height inequality. Those conditions have not
been encoded by the displayed field. Replacing the input by a different
prime in the same finite binary class changes the source, as G1 makes
explicit; it does not prove the original input's convergence.

Allowing all relevant Dedekind or Artin GRH hypotheses does not by itself
produce such an encoding. A successful different field construction would
have to exhibit it, track its degree and discriminant, and prove that its
prime bound lands inside the actual height budget. No such closing
construction was obtained here. This is not a claim of logical independence
between GRH and Collatz.

## G5. A fixed-conductor character representation would already be rigid

**Elementary reconstructed lemma.** Let f on positive integers take values
in any set. If f(Tn)=f(n) for every n and f is eventually periodic, then f
is constant.

**Proof.** Suppose f has period q above a threshold. Doubling invariance
f(2n)=f(n) shows that the same period holds everywhere: multiply n and n+q
by a sufficiently large power of two, then use their large-input periodicity.
Write q=2^r m with m odd. The identities

    f(n+m)=f(2^r(n+m))=f(2^r n)=f(n)

reduce the period to m. Regard f as a function F on Z/mZ. Choosing positive
even and odd lifts of each residue gives

    F(2a)=F(a),       F(3a+1)=F(a).                    (13)

Write m=3^s d with gcd(d,6)=1. Iterating the second identity s times gives

    F(a)=F(3^s a+(3^s-1)/2).

Replacing a by a+d changes the argument on the right by m. Thus d is
also a period. Work now modulo d, where both 2 and 3 are invertible. By
(13),

    F(3a+2)=F(2(3(a/2)+1))=F(3(a/2)+1)=F(a/2)=F(a).

This equals F(3a+1). As 3a+1 runs over all residues, every two adjacent
values agree, so F and f are constant. The modulus-one cases are included.

In particular a finite linear combination of Dirichlet characters, or any
fixed-conductor periodic expansion, cannot be a nonconstant ordinary
separating label. An arbitrary component Dirichlet series has not thereby
become a classical L-function: no Euler product, functional equation or
GRH zero assertion for that series has been established.

An approximate character expansion with increasing conductors could still
be useful, but it needs a proved error bound and conductor cost tailored to
the actual invariant label. G5 does not exclude such a route. GRH estimates
cannot replace that missing approximation theorem.

## Closing attempts and the remaining interface

PR146 already supplies an unconditional construction of some ancestor of
any fixed positive ternary-unit target in every binary residue class, with
extra clock D(s) satisfying log D(s)=O(s/log(s+2)). Its proof samples freely
chosen exponents and proves all inverse divisions. This is a stronger
starting point than simply proving that each relevant congruence has a
solution. The unresolved transfer concerns the supplied ordinary source or
an accurately controlled block of failures. GRH's prime selection does not
identify that source with the newly selected ancestor.

PR159's prime-height bound would close an escaping-orbit route only after
an upper bound on the primes appearing along that actual orbit. A least
prime in an arithmetic progression supplies no such upper bound. Its
circulation route instead needs a finite oriented moment of the actual
component boundary. A character-sum estimate for primes is not an estimate
for that generally nonperiodic boundary coefficient; G5 identifies the
fixed-conductor obstruction precisely.

PR162's positive occupation criterion keeps a fixed full-support input.
Replacing it by a distribution on primes or on freely chosen inverse words
does not preserve that transported source. GRH does not justify the
replacement. Its infinite physical five blocks remain useful ordinary
identities, but selecting a prime satisfying their residue guard gives a
different antecedent and does not establish coverage of every supplied one.

The useful answer is therefore specific: GRH gives the quantitative prime
realization in G1 and stronger arithmetic sampling tools, but no closing
Collatz implication was derived from them. The missing work is a valid
source-preserving reduction to those tools, with its full height and
conductor costs. The elementary obstructions G2--G5 delimit several tempting
reductions without ruling out all possible GRH-based proofs.
