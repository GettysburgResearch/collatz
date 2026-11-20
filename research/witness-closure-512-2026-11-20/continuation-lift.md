# A continuation lift from the parameter m = 1

## Status and scope

This note proves a conditional induction rule. It does **not** prove the full
witness-closure assertion, and it does not assert unconditional convergence of
all inputs in the cylinder below. The rule reconstructs the requested target
witness using fifteen instances of the original bridge assertions at strictly
smaller positive odd parameters.

The calculation is independent of empirical coverage claims. The two finite
seed witnesses, their exact continuation formulas, the normalization identities,
and the parameter bounds are given explicitly.

Let E be the set defined by the finite witness identity in the question. For a
positive odd integer z, write

    C(z) = (3z+1) / 2^v2(3z+1),       J(z) = 4z+1.

The recurrence definition and the finite witness identity are equivalent.
Membership in E is preserved in both directions along a finite exact C prefix.
Also, for positive odd z, J(z) and z have the same next odd iterate. A witness
for z transfers to J(z) by adding two to its first exponent increment; the
reverse transfer subtracts two. At z=1, first append the exponent-two loop if a
nonempty witness is needed.

For each positive odd a, use the notation

    P(a):  E(27a)    implies E(54a+1),
    Q(a):  E(54a+1) implies E(9a).

These assertions denote witness-producing implications, not assumptions that
all their sources or targets converge. Together, P(a) followed by Q(a) gives

    E(27a) implies E(9a).

Thus, when the relevant P and Q assertions are available, a factor of three can
be removed from a known member of E that is divisible by 27.

## The conditional theorem

Let

    m = 1 + 2^K u,       K >= 71,       u positive and odd.

Assume P(a) and Q(a) are available for every positive odd a < m. Then a supplied
witness for

    x = 128m+1

can be transformed into a witness for

    y = 64m+1.

More precisely, only fifteen smaller-parameter bridge calls are needed. Their
parameters and order are specified below. This proves the desired closure
implication at m under a strong induction hypothesis on the parameter m.

The seed m=1 itself is already a finite certified case: 129 and 65 have the
witnesses displayed next. It is not included in the expression with u positive.

## 1. Exact seed witnesses

For 129, the following 44 exponent increments end at 1 and have sum 77:

    2,2,2,1,1,3,1,1,1,2,2,1,2,1,1,2,1,1,1,2,3,1,
    1,2,1,2,1,1,1,1,1,3,1,1,1,4,2,2,4,3,1,1,5,4.

For 65, the following eight exponent increments end at 1 and have sum 19:

    2,2,4,1,1,2,3,4.

Both lists are finite exact certificates: at each step the stated power of two
is the exact valuation of 3z+1, and the final state is 1. No stopping-time
estimate is being assumed.

Let A_j and B_j be their cumulative exponent sums. Applying the same affine
prefix formulas to the perturbed inputs gives the states

    x_j = C^j(129) + 3^j 2^(K+7-A_j) u       (0 <= j <= 44),
    y_j = C^j(65)  + 3^j 2^(K+6-B_j) u       (0 <= j <= 8).

Every displayed state is a positive odd integer. Indeed,

    A_j <= 77,       K+7-A_j >= 1,
    B_j <= 19,       K+6-B_j >= 58.

The seed state is odd and the added term is even. The affine recurrences
therefore supply integer odd quotients at every step, which proves that every
prefix exponent remains exact. In particular, the perturbed endpoints are

    X = 1 + 3^44 2^(K-70) u,
    Y = 1 + 3^8  2^(K-13) u.

The given x witness has the stated 44-step prefix, so it supplies a witness for
X. To construct the y witness, it suffices to construct a witness for Y and
prepend the fixed eight-step target prefix.

Notice that K=70 would fail the oddness test at the source endpoint: the
perturbation of the final seed value 1 would be odd. Thus the threshold K>=71
is material.

## 2. Normalizing an expression centered at 1

Let a>=0, v>=1 and u be positive and odd. For

    Z = 1 + 3^a 2^v u,

the following reductions are exact.

If v=2t with t>=1, then t-1 successive exponent-two steps give

    J(3^(a+t-1) u).

Consequently, a witness for Z is equivalent, by those steps and a J transfer,
to a witness for 3^(a+t-1)u.

If v=2t+1 with t>=0, then t successive exponent-two steps give

    2 * 3^(a+t) u + 1.

To verify exactness, at every step that is taken the coefficient of u in Z-1
has at least three factors of two. Dividing 3Z+1 by four therefore gives an odd
integer. In the even case the final state has coefficient four and is treated
by J; no extra quarter step is assumed there.

## 3. Even K-70: seven strips, then P

Write

    K-70 = 2s,       s>=1,       n = 3^(s+36) u.

The preceding normalization shows

    E(X) is equivalent to E(3^7 n),
    E(Y) is equivalent to E(2n+1).

For the source, use s-1 exponent-two steps from X, then remove J. For the
target, Y reaches 2n+1 after s+28 exponent-two steps.

Starting with the resulting witness for 3^7n, perform the following calls for
j=7,6,...,1:

    a_j = 3^(j-3) n = 3^(s+33+j) u,
    3^j n = 27a_j
        -- P(a_j) --> 54a_j+1
        -- Q(a_j) --> 9a_j = 3^(j-1)n.

After these fourteen calls there is a witness for n. The fifteenth call is

    P(a_0),       a_0 = n/27 = 3^(s+33) u,

which supplies a witness for 2n+1. Prepending s+28 exponent-two steps constructs
a witness for Y; prepending the seed target prefix constructs the required
witness for y.

All parameters are positive and odd. The largest is a_7=3^(s+40)u, and

    a_7 / (2^K u) = (3/4)^s * 3^40 / 2^70 < 1.

For example, the elementary integer inequality 3^10=59049<65536=2^16 implies
3^40<2^64<2^70. Therefore every parameter in the chain is strictly below
2^K u<m.

## 4. Odd K-70: Q, then seven strips

Write

    K-70 = 2s+1,       s>=0,       n = 3^(s+36) u.

Normalization now gives

    E(X) is equivalent to E(2 * 3^8 n + 1),
    E(Y) is equivalent to E(n).

For the source, X reaches 2*3^8n+1 after s exponent-two steps. For the target,
Y reaches J(n) after s+28 exponent-two steps.

First apply

    Q(a_*),       a_* = 3^8 n / 27 = 3^(s+41)u.

Its known source is 54a_*+1=2*3^8n+1, and it supplies the target
9a_*=3^7n. Then perform the seven P(a_j),Q(a_j) strip pairs from the preceding
section, for j=7,...,1. This again uses fifteen calls in total and supplies a
witness for n.

Apply J to that witness to obtain one for J(n). Prepend s+28 exponent-two steps
to obtain one for Y, then prepend the fixed target prefix to obtain one for y.

The largest recursive parameter is a_*=3^(s+41)u. It satisfies

    a_* / (2^K u) = (3/4)^s * 3^41 / 2^71 < 1.

Indeed, 3^41<3*2^64<2^66<2^71. Thus every call again has a positive odd
parameter strictly smaller than m. The boundary K=71 corresponds to s=0;
all formulas and both reconstruction prefixes remain valid.

## 5. Interpretation and limitation

The two seed trajectories reach 1 after different numbers of odd steps. Their
affine continuations therefore do not merge uniformly near m=1. This rule uses
their two continuation values as sources for a sequence of smaller bridge
problems instead. It addresses that particular obstruction to direct merger.

The rule does not establish its fifteen smaller bridge assertions. A proof
procedure may apply the rule only when it can supply those assertions, or
within a strong-induction argument whose remaining parameter classes have
also been discharged. An implementation must stop with UNRESOLVED if any of
the required smaller calls is unresolved. In particular, this note is a new
conditional reduction, not a proof of the full conjectured closure.

The remaining coverage problem is unchanged in kind: a complete argument
would need a family of valid reductions and terminal certificates covering
every positive odd parameter of both P and Q. No such coverage is claimed
here.
