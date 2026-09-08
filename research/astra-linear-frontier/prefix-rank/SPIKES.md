# APR-009: compulsory excursions survive the enlarged rank dictionary

**Status: PROPOSED pending independent mathematical review.** This is an exact
limit on the new Gamma rank, not a refutation of Collatz or of all switching
methods. It accompanies the positive all-period theorem rather than hiding
where its proposed global extension fails.

## 1. Every positive power of three starts at its properness lower bound

For every H>=1, let n=3^H. Then

    Gamma(n)=n, uniquely at the baseline candidate.           (1)

If 4^k>n, the prefix candidate cannot improve n. Otherwise k<H. The actual
prefix starts odd, so q>=1 and its affine A is a 3-unit. Therefore
v3((3^q-2^k)n+A)=0. Also A<=3^k-2^k<n/3, so its absolute raw numerator is
at least n-A>2n/3. Its squared rank exceeds n for n>=3. This proves (1)
for EVERY prefix, not just the finite sample or one fixed dictionary.

## 2. The next state's rank is uniformly superlinear

Put y=T(n)=(3n+1)/2 and

    kappa=2 log(4)/log(12)>11/10.

Then

    Gamma(y) > n^kappa > n^(11/10).                         (2)

The final comparison is certified by 4^9>3^11, without decimal logs.

For a nonzero length-k displacement at y, write

    Z=(3^q-2^k)y+A = ((3^q-2^k)3^(H+1)+C)/2,
    C=3^q-2^k+2A.

C is an odd nonzero integer with |C|<3^(k+1). If k<H its ternary valuation
is at most k, while the other summand has valuation at least H+1. Thus
v3(Z)<=k. Moreover |Z|>=y-A>n, using A<n/3. The candidate consequently
exceeds n^2/3^k and is at least 4^k. The weighted geometric mean of these
bounds is n^kappa. If k>=H the bound 4^k alone exceeds n^kappa. The baseline
y^2 is larger too, since y is a 3-unit. Zero displacements are omitted by
definition and do not create rank zero. This proves (2).

## 3. Every lower-rank merger must pay this first excursion

Every predecessor of a positive multiple of three is on its even ray:
an odd shortcut step cannot enter residue zero modulo three. Thus every
positive ancestor of n=3^H is 2^a n, a>=0. Properness gives

    Gamma(2^a n)>=2^a n>=Gamma(n).

In ANY physical lower-Gamma merging diagram T^r(n)=T^s(x), r must be at
least one. Its forward side therefore visits y and incurs a peak rank
strictly greater than Gamma(n)^kappa. Both clocks, every ordinary witness,
and arbitrary diagram lengths are covered. This is a necessary peak cost;
it does not assert that a rank-lowering diagram exists for every power 3^H.

## 4. Pure Gamma weights and rank moments do not close the mass argument

Let K be the shortcut mass pushforward on {2,3,...}, killed at first reaching
1. For w(n)=Gamma(n)^(-s), s>0,

    (Kw)(y)/w(y) >= (Gamma(y)/Gamma(n))^s -> infinity

along the distinct endpoints y=(3^(H+1)+1)/2. In particular every summable
pure power (s>1/2) fails a pointwise inverse supersolution inequality, even
beyond any finite floor. This statement concerns K, NOT an induced U-return
operator whose endpoint might follow additional safe steps.

For every p>0 the following full-support input has finite p-th rank moment:

    f(x)=Gamma(x)^(-(p+1))
         + sum_{H>=1} 1_{x=3^H} 3^(-Hp)/H^2.                (3)

Indeed sum Gamma^p f <=60+2 by APR-003 and sum H^(-2)<=2.
But Kf has infinite p-th rank moment, since the source atoms in (3) alone
give contributions greater than 3^((kappa-1)pH)/H^2 at distinct endpoints.
Its UNWEIGHTED mass remains finite and is not increased by the killed
pushforward. Moment explosion is not orbit divergence or a positive cycle.

## 5. Consequence for the proposed proof

The new rank defeats arbitrary finite-pattern limitations by selecting from
all actual finite prefixes with a proved evaluation bound. It still does
not supply a globally contracting step or an automatically invariant mass
space. The all-period construction in PERIODIC_SWITCHING.md resolves a
large, explicitly quantified switching class without claiming coverage of
(1)--(3) or of every aperiodic source.

A complete proof needs the remaining physically guarded, lower-Gamma merging
cover, or actual retained-operator control beyond these failed weight/moment
classes. Safe excursion estimates and a positive rank at every source do not
supply that final assertion. All new claims remain pending review.
