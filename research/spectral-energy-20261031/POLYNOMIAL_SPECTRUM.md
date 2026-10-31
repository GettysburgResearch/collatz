# Polynomial-weight phase diagram, witnessed entirely inside the basin of 1

**PROPOSED; self-audited, not independently or formally certified.**
The map is the unabsorbed odd Collatz map

    U(n)=(3n+1)/2^a(n),   a(n)=v_2(3n+1),   b(n)=3/2^a(n).

On positive odd integers outside an arbitrary finite set K, define

    (L_K f)(t)=sum_{x not in K, U(x)=t} b(x) f(x),   t not in K.

For real s use H_s=l^1(n^-s), with norm sum |f(n)| n^-s.
The operator is initially defined on finitely supported vectors. The weights
are part of the definition: this is not the Koopman operator or unweighted
inverse counting.

## P1. Complete polynomial-weight phase diagram

For EVERY finite K:

* If s<=1, L_K extends boundedly to H_s and

      spectrum(L_K)=Fredholm-essential-spectrum(L_K)
                   ={z: |z| <= R_s},   R_s=(3/2)^(1-s).

  Every point of that disk admits a norm-one, disjoint-support approximate
  eigenvector sequence. All states supporting those vectors are explicitly
  known to reach 1. No hypothetical escaping orbit is used.
* If s>1, L_K has no bounded extension to H_s.
* For 0<=s<=1, ||L_K^m||=R_s^m for every m>=1. For s<0,

      R_s^m <= ||L_K^m|| <= 2^(-s) R_s^m.

Thus NO polynomial weight gives spectral radius below one, even after
removing an arbitrarily large finite verified core. For s<1 the radius is
strictly greater than one. For s>1 the operator is not bounded at all.

This is a statement about a proposed proof architecture, not a disproof of
Collatz. The explicit witnesses demonstrate why long finite excursions can
produce the entire bad spectrum even inside a basin known to converge.

### Attribution and delta

PR142's `HARMONIC_SPECTRUM_AND_COMPUTABILITY.md`, pinned at
`3c0ce26d6021fbd700df61652d596293b661612c`, already treats the s=1 harmonic
space, finite killing, equivalent norms and compact perturbations. The
extensions here are the full real polynomial scale, its sharp radius and
unbounded side, and a single explicit convergent family furnishing the
approximate spectrum. No literature-wide priority is claimed.

## P2. Explicit disjoint expanding corridors that terminate at 1

For q>=1 put

    A_q=3^q+1,
    t_q=(2^A_q-1)/3,
    h_q=(t_q+1)/3^q,
    n_(q,j)=3^j 2^(q-j) h_q-1,   0<=j<=q.

All these are positive odd integers. Indeed the elementary lifting identity
v_3(2^(3^q)+1)=q+1 gives v_3(t_q+1)=q, while v_2(t_q+1)=1.
For completeness, the lifting identity follows by induction: for any
integer u=-1+3v, one has u^3+1=(u+1)(u^2-u+1) and
u^2-u+1=3(1-3v+3v^2), so the second factor has 3-adic valuation
exactly one. Start with u=2 and cube successively.

The exact valuation word is

    a(n_(q,0)),...,a(n_(q,q)) = 1,...,1,A_q.

The first q transitions therefore multiply n+1 by 3/2, and the final one
lands at 1. These are literal positive ordinary trajectories, not just
compatible residue cylinders. Each has q+1 odd steps before first hitting 1.

The corridors for distinct q are disjoint before 1. If two interior states
coincided, their future valuation words would agree. The number of remaining
ones would first have to agree, then the first valuation greater than one
would have to be both A_q and A_r, forcing q=r. Within one corridor the states
strictly increase. Their minima n_(q,0) tend to infinity, so any finite K is
avoided for all sufficiently large q until the terminal 1.

The construction uses very large numbers: the bit length is approximately
3^q. It is an explicit proof witness, not an efficient verification strategy.

## P3. Bounds on powers and unboundedness

The normalized coordinate vector is e_n=n^s delta_n. Its surviving image has
coefficient

    w_s(n)=b(n) (n/U(n))^s
          =b(n)^(1-s) [3n/(3n+1)]^s.

For 0<=s<=1 this is at most R_s. A long corridor makes every fixed finite
product arbitrarily close to R_s^m, proving equality of the power norms.
Killing can only reduce positive column sums and does not remove these
corridors far from K.

For s<0, write D_m=product_{j<m} b(U^j n), t=U^m n. A surviving column has
norm D_m(n/t)^s. We have D_m<=(3/2)^m and

    t <= (3/2)^m(n+1)-1,

by induction from U(n)<=(3n+1)/2. Therefore its norm is at most
2^(-s) R_s^m. The same corridors prove the lower bound. The spectral radius
is consequently R_s for every s<=1.

For s>1 choose any odd unit t outside K. Its legal parents
x_a=(2^a t-1)/3, with a in the appropriate parity class, are positive odd,
outside K for large a, and satisfy

    ||L_K e_(x_a)|| = (3/2^a)(x_a/t)^s
                    ~ 3^(1-s) 2^(a(s-1)) -> infinity.

This establishes unboundedness even when 1 is killed.

## P4. The entire disk is essential, not merely its outer radius

Set c(n)=3n/(3n+1). On the q-corridor, for j<q,

    w_j=R_s c(n_(q,j))^s.

Uniformly over 0<=j<=q, products of these c-factors tend to 1: all n_(q,j)
are at least n_(q,0), and q/n_(q,0)->0. The terminal edge has coefficient

    w_q=c(t_q)t_q^(s-1).

### The case s<1

For 0<|lambda|<=R_s define a_0=1 and a_(j+1)=w_j a_j/lambda. Put
f_q=sum_{j=0}^q a_j e_(n_(q,j)). Interior coordinates cancel exactly:

    (L_K-lambda)f_q = -lambda e_(n_(q,0))
                     + a_q w_q e_1,

with the second term omitted when 1 belongs to K. If |lambda|<R_s, the norm
of f_q grows at least like (R_s/|lambda|)^q up to a factor tending to one.
If |lambda|=R_s, its norm is asymptotic to q+1. In either case

    ||(L_K-lambda)f_q||/||f_q||
        <= |lambda|/||f_q|| + w_q ->0.

For lambda=0 use e_(t_q), whose image norm is w_q->0.

### The critical case s=1

Here R_s=1 and w_q->1, so one MUST NOT reuse the preceding terminal-edge
argument in the interior of the disk.

For 0<|lambda|<1 scale each corridor vector above to make its outgoing
coefficient at 1 equal to one. Subtract two such scaled vectors from distinct
corridors. The outgoing terms cancel exactly. The only residuals are at the
two initial states, with sizes tending to zero like |lambda|^q; the vector
norms remain bounded above and bounded away from zero, because the backwards
coordinate sizes form a geometric progression up to c-products tending to
one. Choose pairs (2q,2q+1), so their supports are disjoint as q varies.
This works whether the terminal state 1 is retained or killed.

For |lambda|=1, the single-corridor vector has norm asymptotic to q+1, and
both endpoint residuals are bounded; it suffices without pairing. For
lambda=0 use

    e_(t_(2q))/c(t_(2q)) - e_(t_(2q+1))/c(t_(2q+1)).

Its image is exactly zero, also when 1 is killed.

After normalization the constructed vectors have norm one and disjoint
supports, hence pairwise distance two. If L_K-lambda were Fredholm, a
parametrix would give I minus a compact operator. Applying it to these
vectors would force a convergent subsequence, a contradiction. Thus every
point in the disk belongs to the Fredholm essential spectrum. The power
bounds put the full spectrum inside that disk and complete P1.

## P5. Slowly varying modifications do not restore a gap

Let w(n)=n^-s ell(n), where ell is positive and slowly varying at ordinary
infinity, in the usual measurable locally bounded sense. Use the norm
sum |f(n)|w(n). If its L_K is bounded, then for every fixed m the corridors
with q tending to infinity give

    ||L_K^m|| >= (3/2)^(m(1-s)).

Indeed the endpoint/source ratio tends to (3/2)^m and the slowly varying
factor ratio tends to one. Hence its spectral radius is at least R_s.
For s>1 the same fixed-target parents as in P3 give an unbounded column norm,
since x^(s-1)/ell(x)->infinity. Therefore no regularly varying weight can
provide a bounded operator with spectral radius below one.

At s=1, ell(n)->0 also makes the operator unbounded by those parents. No
claim is made that every other slowly varying factor yields a bounded
operator, or that its full spectrum is determined here. In particular this
corollary does not silently assume equivalence to the harmonic norm.

## What remains open

These results eliminate polynomial/regularly varying global spectral-gap
repairs of the current Jacobian transfer operator. They do NOT exclude
arithmetic, non-regular, state-dependent weights; an induced operator with a
changed clock; or direct fixed-source descent arguments. None of those
alternatives is proved to terminate here. A useful positive replacement must
separate the explicit long-but-convergent corridors from a genuinely
persistent survivor; merely enlarging a verified core cannot do that.
