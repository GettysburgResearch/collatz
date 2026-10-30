# Why small invariance defects do not supply the missing regularity

**Status: PROPOSED, with elementary proofs and exact bounded replay.**
This is a method obstruction, not a Collatz proof and not a claim of global
priority. It complements the softened stopping-time route in the companion
density note. Use the unabsorbed shortcut map
`T(n)=n/2` for even n and `(3n+1)/2` for odd n.

## NI-001. Exact balanced dyadic near-invariants

For odd `k=2m+1`, write `e_j(n)=T^j(n) mod 2` and set

    f_k(n) = 1{e_0(n)+...+e_(k-1)(n) >= m+1}.

Then `f_k` has period `2^k`, mean `1/2`, and the exact ordinary natural
mean defect is

    D_k = mean |f_k(T(n))-f_k(n)|
        = binom(2m,m) / 2^(2m+1).

The logarithmic mean gives the same value. In particular `D_k -> 0`, while
the distance from `f_k` to every constant in ordinary or logarithmic mean
L1 is at least `1/2`; the best squared L2 distance is `1/4`.

**Proof.** The map from a residue modulo `2^r` to its first r shortcut
parities is a bijection. Induct on r: write `n=2z+e_0`; the next value is
z if `e_0=0` and `3z+2` if `e_0=1`. These are both bijections on the
remaining residues modulo `2^(r-1)`. Thus a full period gives independent
fair parity bits. Complementing the k bits exchanges the two majorities,
so the mean is one half. The two successive windows differ only in their
first and last bits. Their majority changes exactly when their common
`2m` bits contain m ones and the two remaining bits differ. This gives the
displayed binomial probability. The elementary central-binomial estimate
`binom(2m,m)/4^m = O((m+1)^(-1/2))` proves convergence to zero.
For any constant c, the L1 distance is
`(|c|+|1-c|)/2 >= 1/2`; minimizing its squared counterpart gives `1/4`.
Every periodic sequence has the same natural and logarithmic mean, by
summing each residue progression. All statements follow. QED.

The exact mismatch count on a period of length `2^(k+1)` is
`2*binom(k-1,(k-1)/2)`. Some values of D are:

| k | D_k |
|---:|---:|
| 1 | 0.5 |
| 3 | 0.25 |
| 5 | 0.1875 |
| 17 | 0.0981903076171875 |
| 65 | approximately 0.049673376874 |
| 257 | approximately 0.0249095549681 |

The closed formula proves the infinite family. Exhaustive replay only
checks its implementation at the finite lengths listed in the evidence.

## NI-002. Arbitrary fixed finite anchor data do not repair the estimate

Let S be any finite set of positive integers and prescribe Boolean values
`a(s)` for all s in S. For all sufficiently large odd k, the points of S
are distinct modulo `2^k`. Modify `f_k` on those residue classes to agree
with the prescriptions, obtaining a periodic Boolean function `g_k`.
Writing `q=2^k` and `a=|S|`, we have

    mean |g_k-f_k| <= a/q,
    |mean g_k - 1/2| <= a/q,
    mean |g_k o T - g_k| <= D_k + 2a/q,
    inf_c mean |g_k-c| >= 1/2-a/q.

These hold in both mean conventions. If the prescribed data satisfy a
finite set of checked edges `a(T(s))=a(s)`, the patched functions satisfy
those same edges exactly. Thus a fixed finite list of correct source
values and transitions cannot turn small mean defect into global rigidity.

**Proof.** At most a of q residue classes change. For every q-periodic h,
the mean of `|h o T|` is the mean of `|h|`: among the `2q` source residues,
each target modulo q has precisely one even preimage and one odd preimage.
The even preimage has form `2y`; the odd one comes from the unique solution
of `3z+2=y mod q`. Triangle inequality therefore adds at most `2a/q` to
the defect. The best constant L1 approximation to a Boolean function of
mean p has error `min(p,1-p)`. This proves the last bound and the remaining
claims. QED.

The anchor assignments need not extend to a globally invariant Boolean
function. No such extension, exceptional ordinary input, or nontrivial
Collatz component is claimed by this construction.

## NI-003. No uniform one-step coercivity bound

There is no function `psi(t)->0` as `t->0` such that every dyadic-periodic
Boolean function h satisfies

    inf_c ||h-c||_mean,1 <= psi(||h o T-h||_mean,1).

This remains false after imposing any one fixed finite compatible set of
anchor conditions. NI-001 and NI-002 are the counterexamples. In particular
no constant C and exponent alpha>0 make the right side `C*defect^alpha`
work uniformly over all dyadic periods.

This does not conflict with exact ergodicity. The dyadic shift has constant
fixed functions in L1, but its finite-memory functions can have arbitrarily
small nonzero invariance defect while retaining nonzero variance. A sequence
of nearly invariant approximants is not automatically Cauchy in L1.

For the companion density route, the required property is approximation of
**one fixed ordinary function** by dyadic periodic functions in mean L1.
That is stronger than merely finding a sequence whose invariance defect
shrinks. The order of these quantifiers must be retained.

## NI-004. Computability and pointwise asymptotic invariance are also insufficient

Define the explicit bounded computable function, for positive n,

    h(n) = (1 + sin(log log(n+2)))/2.

Then `|h(T(n))-h(n)|=O(1/log n)`, but h is not in the closure of dyadic
periodic sequences for either ordinary or logarithmic mean L1.

**Proof of the defect.** For large n, `T(n)/n` lies between `1/2` and 2.
The difference between `log log(T(n)+2)` and `log log(n+2)` is therefore
`O(1/log n)`, by the mean-value theorem. Sine is Lipschitz, proving the
claim.

**Ordinary mean.** Its Cesaro mean through X is `h(X)+o(1)`. To see this,
discard `n<X/(log X)^2`, a vanishing fraction, and use
`log log(n+2)-log log(X+2)=O(log log X/log X)` on the remaining interval.
Taking X near `exp(exp(pi/2+2pi j))` or
`exp(exp(3pi/2+2pi j))` gives different subsequential means, approaching
one and zero respectively.

**Logarithmic mean.** Integral comparison, and then `u=log x`, gives

    (1/log X) sum_(n<=X) h(n)/n
      = 1/2 + [sin(log log X)-cos(log log X)]/4 + o(1).

Indeed an antiderivative of `sin(log u)` is
`u*(sin(log u)-cos(log u))/2`. Replacing n+2 by n affects a summable error;
the sum/integral discrepancy is also `O(1)` since the derivative of
`h(x)/x` is absolutely integrable after a fixed lower endpoint. This mean
again does not converge.

Every mean-L1 limit of periodic sequences has an actual mean: approximate
within epsilon, use convergence of the periodic mean, and compare upper
and lower limits. Since h has no mean in either convention, it is outside
both closures. QED.

This example does not have the stopping-time cocycle or the zero set of the
new soft observable. A proof for that observable must use those additional
properties. Generic computability and `O(1/log n)` invariance defects cannot
by themselves supply its missing regularity.

## Relation to the repository and remaining task

PR137's finite-boundary coloring obstruction concerns exact retained
equations on finite intervals. NI-001--003 instead use whole, periodic
functions and exact averaged errors under the actual Collatz map. Neither
is an invariant positive-integer counterexample. NI-004 also preserves a
pointwise asymptotic invariance rate while showing why generic regularity
cannot be inferred from it.

The useful next target is a **Cauchy/approximation estimate for the actual
softened stopping observable**, or a different arithmetic compactness
principle that distinguishes it from these explicit controls. No such
estimate is established in this packet.
