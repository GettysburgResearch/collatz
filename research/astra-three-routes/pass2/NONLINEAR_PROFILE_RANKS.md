# Route 3 continuation — arbitrary separate valuation profiles still fail

**Status: PROPOSED pending independent mathematical review.** This extends the
parent's linear affine-valuation obstruction. The profiles below may be
quadratic, exponential, oscillatory, discontinuous, or otherwise arbitrary.
The theorem does not assume bounded degree, monotonicity, or a growth rate for
the profiles. It still concerns a **separable sum**, not a joint function of
several valuations, and is not a no-go theorem for every termination proof.

## 1. Class and two distinct conclusions

Fix finitely many primes p and, for each p, finitely many rational p-adic
integer roots alpha. Give each root an arbitrary real-valued function
f_(p,alpha) on the nonnegative integers, finite at each finite argument. Set

    R(n)=s log n + sum_(p,alpha) f_(p,alpha)(v_p(n-alpha)) + h(n),
    s>0, h(n)=o(log n).                                  (1)

Enlarge a finite floor to exclude positive integral roots, where a valuation
would be infinite. Constants f(0) can be subtracted and absorbed into h, so
assume f(0)=0. Extend the profile by zero at absent roots. Multiples log(p)
and any nonlinear rescaling can already be included in f.

**T-A3-501.** For every fixed ell>=1 and every finite floor, (1) cannot satisfy
R(T^ell(n))<=R(n) for all sufficiently large ordinary positive n.

**T-A3-502.** On positive odd integers the same class cannot satisfy
R(F(n))<=R(n) for all sufficiently large n, where the exact whole-run macro is

    a=v_2(n+1), u=(n+1)/2^a,
    F(n)=(3^a u-1)/2^v_2(3^a u-1).                       (2)

The second statement needs its own proof: F has unbounded shortcut length and
is not covered by a fixed-block theorem.

## 2. The finite-precision transport principle

For a fixed rational affine branch g(x)=a x+b mapping an allowed finite
ordinary cylinder to another ordinary cylinder, approach a rational p-adic
root alpha at exact precision k by actual positive integers n_k. Fix the
branch's other congruences, and avoid small neighborhoods of the finitely many
other roots and their preimages at the other primes. CRT gives such n_k with

    log n_k=k log p+O(1).

One can choose representatives between p^k and a fixed multiple of p^k by
adding a fixed multiple of the CRT modulus. The branch endpoint is positive
and of comparable real height for sufficiently large k. At the selected root,

    v_p(g(n_k)-g(alpha))=k+v_p(a);

all other root valuations are eventually constant. Branch membership is
preserved once k is above its fixed precision. At primes other than the
selected one, the avoided root neighborhoods do not cover every residue at
sufficiently high fixed precision; choose one remaining residue. Thus h at
source and endpoint is o(k).

The assumed rank inequality consequently gives

    f_(p,g(alpha))(k+v_p(a)) <= f_(p,alpha)(k)+o(k).        (3)

The error can depend on the fixed branch and roots but not on growing k.
It need not have a sign. Fixed shifts preserve the o(k) property, and a finite
chain of these inequalities still has an o(k) error. No limit f(k)/k is
assumed. These are actual ordinary finite-precision tests, not an ordinary
realization inferred from an infinite p-adic word.

## 3. Proof of T-A3-501: fixed shortcut blocks

Put m=2^ell. The exact all-even block T^ell(mn)=n implies R(mn)>=R(n). The
transport argument gives, for each p-adic integral rational alpha,

    f_(p,alpha)(k) <= f_(p,m alpha)(k+v_p(m))+o(k).        (4)

### Odd primes

If p is odd and alpha!=0, the roots m^j alpha for j in Z are all p-adic
integers and pairwise distinct. Only finitely many have nonzero profiles.
Transport forward to an absent root and backward from an absent root using
(4). There is no precision shift because p does not divide m. Therefore

    f_(p,alpha)(k)=o(k) for p odd, alpha!=0.              (5)

This is asymptotic elimination of the whole nonlinear profile, rather than
only of a linear coefficient. The root zero is not constrained by this step.

### The prime 2

For nonzero alpha in Z_2, forward multiplication by m remains in Z_2 and
visits distinct roots. Transport to the first absent root in a finite number
of steps. Equation (4), with its fixed shifts, yields

    f_(2,alpha)(k) <= o(k), alpha!=0.                    (6)

This is only an upper bound. A profile with large negative excursions is not
silently discarded. Backward division by 2 is not legitimate on all Z_2.

### An ordinary all-odd path defeats the remaining profiles

Choose an even positive b divisible by every relevant odd prime, and with
b-1 different from each dyadic root. Choose M>=3 larger than all the finite
valuations v_2(b-1-alpha). Let L tend to infinity through multiples of ell
and 2^(M-1). Then 3^L=1 mod 2^M and the exact ordinary path is

    x_i=3^i 2^(L-i)b-1, 0<=i<=L, T(x_i)=x_(i+1).        (7)

All its states exceed any fixed floor for large L. At the endpoints every
root-zero valuation at an odd prime vanishes, since b is divisible by p.
Their dyadic root-zero valuations vanish because the endpoints are odd.
At x_0, only the dyadic root -1 can have a growing valuation, namely
L+v_2(b); all other dyadic values are constant. At x_L all dyadic values are
constant by the chosen congruence. Equations (5)-(6) imply

    R(x_L)-R(x_0) >= s L log(3/2)-o(L) > 0.              (8)

For clarity, an odd-prime nonzero-root valuation at either endpoint is at
most O(L), because its fixed rational denominator is a p-adic unit and the
ordinary numerator has exponential-in-L size. If f(k)=o(k), then f(k_L)=o(L)
whenever 0<=k_L<=C L; bounded k_L also causes no difficulty. A very negative
value in (6) increases the difference in (8), so it is not a loophole.

But applying the supposed ell-step nonincrease successively along (7) gives
R(x_L)<=R(x_0). Contradiction. This proves T-A3-501.

## 4. Proof of T-A3-502: the adaptive whole-run map

Every fixed pair a,b>=1 defines a nonempty exact dyadic branch of (2),

    g_(a,b)(n)=(3^a n+3^a-2^a)/2^(a+b).                 (9)

For any odd dyadic rational endpoint beta its inverse root is

    alpha_(a,b)=(2^(a+b) beta-3^a+2^a)/3^a.

The identity alpha+1=2^a(2^b beta+1)/3^a shows its exact source odd-run length
is a and its exact following even-run length is b. Finite neighborhoods of
this root therefore specify the actual branch. Odd primes can be controlled
independently by CRT.

### Odd primes other than 3: every profile becomes sublinear

For p!=2,3, both g_(1,1)(x)=(3x+1)/4 and g_(1,2)(x)=(3x+1)/8 are invertible
on Z_p. Their rational fixed points are respectively 1 and 1/5. Off a fixed
point, the bi-infinite rational orbit is distinct. Equation (3) has no
precision shift here. Finite forward and backward transport implies f=o(k)
on that orbit. The second map handles the first map's fixed point and vice
versa; when 1/5 is not p-integral it simply supplies no exceptional fixed
point. Thus

    f_(p,alpha)(k)=o(k) for every root, p!=2,3.           (10)

### The prime 3: unit-root profiles become sublinear

Transport along a nonfixed forward orbit of g_(1,1) eventually reaches an
absent profile. Each edge shifts precision by +1. The finite chain gives

    f_(3,alpha)(k) >= -o(k).

Use g_(1,2) to cover alpha=1. Hence this lower bound holds for every ternary
root. For a ternary unit beta there are infinitely many b>=1 for which

    alpha_b=(2^(b+1)beta-1)/3 is in Z_3.

These roots are distinct; choose one absent from the finite feature set.
Since g_(1,b)(alpha_b)=beta, (3) gives
f_(3,beta)(k+1)<=o(k). Combining the two directions,

    f_(3,beta)(k)=o(k) for every ternary unit beta.        (11)

Profiles at roots in 3Z_3 need not be controlled beyond the lower bound.
The final witness below sees only argument zero at these roots.

### The prime 2: all observable profiles are sublinear from above

Even dyadic roots have argument zero on odd inputs. For an odd dyadic root
beta, the infinitely many distinct roots

    alpha_b=(2^(b+1)beta-1)/3, b>=1

are odd and belong to the exact a=1,b branch. Choose an absent alpha_b and
approach it at precision k>b+1. The endpoint precision is k-b-1. Equation (3)
therefore gives

    f_(2,beta)(t) <= o(t), t=k-b-1.                      (12)

Again this is only an upper bound; arbitrary negative behavior is allowed.

### A single arbitrarily long ordinary macro gives the contradiction

Take a=1 mod 4 and n_a=3*2^a-1. Its exact macro is

    F(n_a)=m_a=(3^(a+1)-1)/8,                            (13)

because a+1 is twice an odd integer and v_2(3^(a+1)-1)=3. Choose a_0=1 mod 4
whose m_(a_0) is not any of the finitely many dyadic roots. Choose M larger
than all v_2(m_(a_0)-alpha), and restrict

    a=a_0 mod 2^(M+2).

Euler's congruence modulo 2^(M+3) makes m_a=m_(a_0) mod 2^M, so every dyadic
endpoint profile is fixed. At n_a only the root -1 has growing dyadic
precision a; (12) bounds its contribution from above by o(a). Both n_a and
m_a are ternary units, so all roots in 3Z_3 have argument zero. Equations
(10)-(11) control the other odd-prime terms by o(a), since their precisions
are O(a). It follows that

    R(m_a)-R(n_a) >= s a log(3/2)-o(a)>0.                (14)

This contradicts macro nonincrease and proves T-A3-502 independently of the
fixed-block argument.

## 5. Consequences, tests, and the remaining constructive route

The conclusion holds above every finite floor. For a positive weight
w=exp(-R), any pointwise killed inverse supersolution inequality that includes
each of these surviving path edges would imply the forbidden rank
nonincrease. Thus the same obstruction applies to the corresponding finite
separable nonlinear-profile weights. It says nothing about a contraction
only after summing over an actual survivor ensemble.

The new checker exhibits exact rank increases for nonlinear quadratic, cubic,
and oscillatory profiles, separately for ell=1,2,4 and for the adaptive macro.
It compares exp(R) by integer powers and rational arithmetic, not floating
logarithms. These examples test the arithmetic interfaces; the all-profile
conclusion is the proof above, not extrapolation of the examples.

The next constructive classes must genuinely change at least one hypothesis:
interactions between features, a controlled infinite dictionary, a common
vector/tree-valued well-founded order, a different proved total adaptive
block grouping, or a different leading growth law. None is ruled out here.
In particular PR #91's common-rank multi-return repayment families are not
contradicted: their grouping is not required to be one application of F, and
their supplied finite/parametric cover is not claimed complete. This pass
keeps route 3 active while eliminating arbitrary *separate* nonlinearity as
an attempted repair of the specific old templates.
