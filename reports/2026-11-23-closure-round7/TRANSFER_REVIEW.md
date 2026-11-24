# Independent review of the actual forward/inverse-law comparison

23 November 2026. Reviewer lane: `ordinary_descent7`.

## Frozen source and verdict

Reviewed source:
`research/closure-round7-20261123/SOURCE_TRANSFER.md`, Git blob
`338e5b93906ea66570b7827f300361b4e5a77b6d`, based on parent PR182 head
`e4367dd2c4406c1041e66d82dfba822908747fa3`.

The local same-orbit count dependency was also read in full:
`research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`, blob
`6881dc864f3b586958bd46d5c38b1c2524008565`. Its stated domain is a
forward-invariant set on which the actual odd map is injective, and its
bound applies at every real height `X>=1`. The whole injective forward
ray has exactly this domain. The bound does not count the branching
predecessor basin.

The entrance-law and compiler inputs remain source-qualified at the
PR177 head and exact paths/blobs pinned in the reviewed note. This
review reconstructs the deductions from their displayed actual weights,
normalization, and canonical exponent table; it does not claim a new
independent audit of every upstream entrance-law theorem.

**VERIFIED at the stated conditional written-mathematics scope.** No
correction was identified in R7-ST-1, its sharpened overlap rate,
R7-ST-2, the retained-atom collision-dimension claim, R7-ST-3, or the
all-depth periodic compiler control. The verdict assumes the displayed
source-qualified entrance law on one hypothetical escaping component
and retains that same component and same actual forward source. It
does not construct an escaping orbit, establish the missing forward-law
convergence or collision estimate, or prove Collatz.

No new Lean proof or execution of the transfer control script is claimed
by this review. The source's finite execution receipts retain their
separate stated status. This verdict binds the exact blob above and does
not automatically extend to later revisions.

## 1. Exact ordinary laws and the coarse cutoff comparison

The forward law is uniform on `N` distinct actual states `q_i`, while
the inverse terminal-source law is

`nu_j(n)=r(n)^s 1_(D_j)(n)/A_j`.

The original ordinary source is retained in each increasing predecessor
set, which gives the fixed positive normalizer lower bound `A_j>=a`.
Together with `r(n)<=1/n`, this gives

`nu_j(n)<=1/(a*n^s)`

on the full ordinary source space, including zero mass off `D_j`.
For integer `X>=1`, its tail beyond `X` is bounded by the decreasing
ordinary series and the integral from `X` to infinity. The forward mass
at most `X` is at most the count of the entire same forward orbit
divided by `N`. Testing total variation on this one ordinary initial
interval proves (4), uniformly in the inverse root. This does not require
the inverse law to contain the complete forward prefix, and it does
not drop sources that project to the same residue.

The whole-orbit count is used within its exact domain: arbitrarily
separated visits are included. The earlier proof charges high binary
clocks by the same fixed number of odd transitions and hence an
injective map on the same invariant set; it does not require a
consecutive low-height window. No predecessor-population interpretation
of that estimate is needed here.

## 2. The sharper layer-cake exponent

On a countable ordinary space,

`1-TV(pi_N,nu_j)=sum_(i<N) min(1/N,nu_j(q_i))`

because the actual forward states are distinct. Enlarging the index set
to the full same injective ray and replacing the inverse weight by its
pointwise upper bound both have the correct inequality direction.

For `R=(N/a)^(1/s)>=1`, the exact identity

`min(1/N,1/(a*q^s))=(s/a)*integral_R^infinity 1_(q<=t)*t^(-s-1) dt`

holds in both cases `q<=R` and `q>R`. Summation is justified by
nonnegativity. The resulting counting function is exactly
`F(t)=#{i>=0:q_i<=t}` for the one forward ray; it is not the size of
an inverse set or a component.

Applying the whole-ray count and replacing the logarithmic denominator
by its value at `R` gives

`Cs/(a*(s-theta))*R^(theta-s)/sqrt(1+log R)`.

The integral converges since `s>1>theta`. Substitution of `R` yields
precisely the normalizer exponent `a^(-theta/s)` and the decay power
`N^(theta/s-1)`. The claimed square-root logarithmic gain is retained.
The condition `N>=max(1,a)` is sufficient for the count bound's domain;
the subsequent big-O statement is asymptotic with the fixed source and
fixed `s`. The same argument applies to `mu_s` because its normalizer
is at least `a` and it satisfies the same pointwise upper bound.

This proves separation of the specified forward and inverse laws. It
does not estimate the forward empirical law against its own stationary
residue limit.

## 3. Full-quotient residue projection

The residue test set `{1,...,X}` consists of distinct classes when
`1<=X<Q`. It contains the projection of every ordinary inverse source
at most `X`; inverse sources above `X` that enter the same residue set
only increase its mass. Each residue class contains at most
`floor(H_N/Q)+1` of the distinct actual forward states, so the projected
forward probability on that test set is at most

`X*(floor(H_N/Q)+1)/N`.

This retains the full ordinary quotient and every forward occurrence.
It does not assume equidistribution or transfer an ordinary total
variation bound through a projection. The direct event comparison
therefore proves (7).

Since `H_N>=N`,

`floor(H_N/Q)+1 > H_N/Q >= N/Q`,

so `L_(N,Q)=N/(floor(H_N/Q)+1)<Q` strictly. Under
`L_(N,Q)>=2^s`, the chosen integer
`X=floor(L_(N,Q)^(1/s))` is positive, smaller than `Q`, and at least
half the unrounded power. Because `1-s<0`, the inverse tail contributes
at most

`2^(s-1)/((s-1)*a)*L_(N,Q)^(-(s-1)/s)`;

the forward test-set contribution is at most the same power with
coefficient one. This proves the exact constant in (8).

If `H_N/Q_N=o(N)` along growing prefixes, the quotient denominator
is `o(N)`, so `L_(N,Q_N)` tends to infinity. The maximal projected
separation then holds for every choice of inverse root. The note
correctly distinguishes this growing-resolution assertion from any
fixed-modulus limit. The same quotient bound also gives maximum forward
residue mass at most `1/L_(N,Q)`, and hence a collision upper at most
that quantity; this validates the comparison of scales without
identifying the two laws.

## 4. The retained atom and collision dimension

The fixed ordinary identity `q_0` belongs to every inverse predecessor
set. Its mass is at least

`b=r(q_0)^s/M_s>0`

uniformly in the inverse root. Projection preserves at least this much
mass in one residue class. The collision sum is therefore bounded below
by `b^2` and above by one, independently of the modulus and root.
Dividing its negative logarithm by `m*log 3` at modulus `3^m` yields
zero in the limit. The same reasoning applies to `mu_s`, where the
ordinary atom has mass exactly `b`.

This is an inverse-law collision-dimension statement. It supplies no
collision dimension for the forward stationary law and does not count
one repeated path-depth state as multiple ordinary atoms.

## 5. The relative-entropy coefficient and constant

For `j>=N-1`, every forward state in the prefix is in `D_j`, so there
are no zero reference probabilities. Expanding relative entropy gives
exactly

`log A_j-log N-(s/N)*sum_(i<N) log r(q_i)`.

Sorting the distinct same-source forward values changes no probability.
For the ordered values `n_k`, one has both `n_k>=k` and
`k<=F(n_k)`. Taking logarithms of the full orbit-count upper and using
`n_k>=k` yields the displayed inequality (11), including its positive
one-half logarithmic correction.

The factorial integral gives the average `log k` at least `log N-1`.
The derivative bound

`d/dx log(1+log x)=1/(x*(1+log x))<=1/x`

for `x>=1` gives the average `log(1+log k)` at least
`log(1+log N)-1`. Consequently the average `log n_k` is at least

`(log N + (1/2)*log(1+log N) - log C - 3/2)/theta`.

Using `r(q_i)<=1/q_i` and `A_j>=a` now produces precisely

`(s/theta-1)*log N + (s/(2*theta))*log(1+log N) - K`,

with

`K=(s/theta)*(log C+3/2)-log a`.

Thus both the sharpened log-log coefficient and the stated constant
are correct, including the `N=1` range. Replacing the normalizer by
`M_s` gives the same valid lower bound for relative entropy against
`mu_s`. The note correctly keeps the signed arithmetic transport term
outside this conclusion; an unbounded entropy penalty alone does not
bound a free-energy trial or the variational optimum.

## 6. Literal periodic compiler control

The proposed starting transported root is the actual compiler value
`S(1)=64*1+21=85`. For a root congruent to one modulo three, the
listed exponents `2,6,4` for residue classes `1,4,7` modulo nine
give positive odd integer parents congruent to one modulo three.
They are the first positive admissible exponents for the indicated
parent colour. Moreover

`3*y_(k+1)+1=2^(e_1(y_k))*y_k`

with `y_k` odd, so the exact forward two-adic valuation equals the
selected exponent. These are literal ordinary inverse steps at every
depth.

All selected exponents are at least two, which proves

`3*(y_(k+1)-1)>=4*(y_k-1)`

and hence the stated bound `y_k>=1+84*(4/3)^k`. The unprimed source
one remains one under its repeated exponent-two inverse branch, so a
repeated finite address can coexist with unbounded transported roots.

The note expressly identifies this as a periodic ordinary control.
It neither provides an escaping component nor contradicts a theorem
restricted to injective escaping rays. Repeated source one at distinct
path depths cannot be inserted as distinct ordinary atoms into the
earlier inverse law. That distinction is correct and essential.

## Remaining hypothesis

The reviewed comparisons quantify why the displayed inverse terminal
law cannot be used directly as the missing forward collision limit.
They do not supply a new transport controlling that change of law or
the absolute transported ordinary mass required by the pressure route.
The conditional escaping-component premise and these actual-source
closing obligations remain open.
