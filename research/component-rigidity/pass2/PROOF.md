# Residue-locked inverse geometry and arithmetic component compactification

**Pass 2 — 25 September 2026. CR2-001–007: PROPOSED pending independent mathematical review.**
No complete Collatz proof, no global separator-regularity theorem, and no external priority claim.
The finite experiments are checks of their stated inventories, not proof by extrapolation.

## 0. What this pass changes

Pass 1 proves that every ordinary merger component meets every sufficiently high interval of any fixed relative width. This pass couples that size control to exact ternary residues. It then transports a credited finite-pattern merger gate into **every** sufficiently high relative interval, rather than merely constructing blocks somewhere far out.

The main new statement is:

> For every fixed finite integer pattern F and every R>1, there is an effective C_(F,R) such that, for every original positive integer N and every real X>=C_(F,R) N, the component of N contains a translate x+F entirely inside [X,RX].

This does **not** provide blocks whose length is a positive fraction of X. F is fixed before N and X. That order of quantifiers is the remaining distinction from the macroscopic-block closing criterion of Pass 1.

We also identify a concrete compact inverse-limit space in which every component is dense. This is useful structure, but its density is explicitly **not** a proof that two components coincide. The same residue-locked construction works for a control system with two disjoint positive cycles.

### Scope and sources

Use the unabsorbed shortcut map T=T_3 on positive ordinary integers, with

    T_p(n)=n/2 when n is even; (p*n+1)/2 when n is odd.

The generalized statements below cover only p=3 and p=5. A merger component consists of sources whose actual forward trajectories meet, with separate finite clocks. In particular 1<->2 for p=3; no absorbing modification is used.

This child follows Pass 1 at commit `5b0438ddeaef991e2f152add8d8782f0d6a55f02`, in draft PR #137. Main was read at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; AGENTS, README, research map and scoped errata were read. No corrected mass, stopping, rank or realization result is a premise here.

The finite-pattern compiler used in Section 5 is **credited**, not newly claimed: PR #134 at `025f2683c19bfedc3eeff0303206b20c889c8005`, `research/paired-comparison/endpoint-transplant/PROOF.md`, credited synchronizer and EPT-001/002. That source in turn credits #132 ACS-002/003. We restate the proof interface and its finite construction below so that no acceptance label replaces a hypothesis.

External context: K. M. Monks, *The Sufficiency of Arithmetic Progressions for the 3x+1 Conjecture*, Proc. AMS 134 (2006), 2861–2872, Theorem 1.1, already proves that every nonconstant arithmetic progression meets every merger component. Author copy: https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf . It was read and its theorem page inspected. Merely obtaining an intersection with a residue class is not a new AP-sufficiency result. The present refinement is the simultaneous control of a prescribed residue and **every sufficiently high narrow relative window**, together with its finite-pattern transfer. This was not a comprehensive priority search.

## 1. Exact residue-locked inverse ladders

### 1.1 Orders and original-source anchors

Fix p in {3,5}, an integer q>=1, m=p^q and P=(p-1)p^(q-1). Two generates the units modulo m and has exact order P.

For a short elementary proof, the order is p-1 modulo p, and

    v_3(2^2-1)=1,     v_5(2^4-1)=1.

If u=1+c p^a with p not dividing c and a>=1, binomial expansion gives v_p(u^p-1)=a+1. Iterating shows v_p(2^((p-1)p^j)-1)=j+1. Thus the order at successive lifts multiplies by p. It reaches the number of units, proving the assertion and giving a digit-by-digit discrete-log algorithm.

Fix a canonical unit residue r, 1<=r<m, p not dividing r. Every original N>=1 can be connected explicitly to a unit Y. If p does not divide N, set Y=N with original clock zero. Otherwise, write N=2^v u with u odd, and take

    Y=(p*u+1)/2 = T_p^(v+1)(N).

Then Y is a unit modulo p and Y<=(p+1)N/2. Choose s0 in [0,P) such that 2^s0 Y=r mod m. Put s=s0, except that if 2^s0 Y=1 put s=s0+P. The seed

    y0=2^s Y

satisfies

    y0>=2,   y0=r mod m,   T_p^s(y0)=Y,
    y0<=((p+1)/2)*2^P*N.                                  (1)

Every later ladder point remains linked to this SAME original N. A multiple of p uses the supplied forward arm, not an invented pure ancestor of N.

### 1.2 The locked inverse rule

Given y>=2 with y=r mod m, solve

    2^k y = p*r+1 mod p^(q+1).                            (2)

The right side and y are units. There is one exponent class modulo pP. Let k be its least representative at least k_min, where k_min=2 for p=3 and k_min=3 for p=5. Thus

    k_min <= k <= pP+k_min-1.                            (3)

Set z=(2^k y-1)/p. Equation (2) implies z is integral and z=r mod p^q. It is positive and odd, and

    T_p^k(z)=y, with physical word 1 followed by k-1 zeros. (4)

Indeed, the first odd step gives 2^(k-1)y, and the next k-1 halvings give y. No intermediate parity is selected by fiat.

Both multipliers satisfy the uniform growth lower bound

    z >= (5/4)y.                                         (5)

For p=3 the only tight case is k=2; integrality then makes y=1 mod3, so y>=4, and (4y-1)/3>=5y/4. For p=5, k>=3 and y>=2 give (8y-1)/5>=5y/4. Also z<2^k y.

Let kappa in [0,P) be the unique exponent satisfying

    2^kappa r = p*r+1 mod p^q.                           (6)

Reducing (2) modulo p^q gives the crucial extra conservation law

    k = kappa mod P                                     (7)

at **every** ladder step, even though its full clock varies.

**CR2-001.** Equations (1)–(7) construct, for every original N, every q and every unit residue r, an infinite growing ordinary backward ladder y_j within that original component, all y_j=r mod p^q, with uniformly bounded individual inverse clocks and one fixed clock class modulo P.

This is deterministic arithmetic construction, not a stochastic trajectory model or a completion argument.

## 2. Joint logarithmic and residue geometry

Write alpha=log_2 p and K_j=sum_(i<j) k_i. Iterating the exact inverse identity gives

    log_2 y_j = log_2 y0 + K_j - j*alpha + e_j,
    e_j=sum_(i<j) log_2(1-1/(2^k_i y_i)).                  (8)

Since y_i>=2(5/4)^i and k_i>=2, the errors converge absolutely. The elementary bound -log_2(1-u)<=2u for 0<=u<=1/8 gives

    |e_infinity-e_j| <= 5/(2 y_j) <= (5/4)(4/5)^j.        (9)

By (7), K_j=j*kappa modulo P. Thus the logarithmic phases modulo P are a rotation with step kappa-alpha plus an error tending to a constant. Its normalized step (kappa-alpha)/P is irrational: otherwise log_2 p would be rational, contradicting the distinct prime factorizations of p^a and 2^b.

**CR2-002.** The phases log_2 y_j modulo P are uniformly distributed on the circle R/(P Z), while every y_j retains the exact residue r modulo p^q.

Proof: for any nonzero integer h, the exponential average with frequency h/P is a geometric progression with ratio different from one, multiplied by a factor converging to a constant. Replacing that factor by its limit costs an average tending to zero. Every nonzero Fourier average vanishes; the elementary trigonometric approximation criterion proves uniform distribution.

This is stronger than separately knowing that a component meets every AP and has dense logarithmic phases. Those two separate statements would not give their simultaneous intersection. It is also a statement about a constructed BACKWARD ladder, not about equidistribution of any arbitrary forward Collatz trajectory.

### 2.1 Effective finite arithmetic certificates

Let B=2^P. Normalize positive rationals modulo multiplication by B into [1,B). For any finite nonempty set of phases define its largest circular multiplicative gap by sorting a_1<...<a_h and taking

    G=max(a_(i+1)/a_i, B*a_1/a_h).

For a chosen J, take the ideal points

    (2^kappa/p)^i modulo B, 0<=i<=J,                     (10)

and let G_J be their gap. All these quantities are exact rationals. Set

    c_M=(5/8)(4/5)^M.

For every R>1 one can effectively choose M,J satisfying

    G_J/(1-c_M)<R.                                      (11)

Existence follows from the irrational rotation and c_M->0; an exhaustive rational search is an algorithm. To verify the transfer to actual ladders, put E_j=2^e_j. For j>=M, the sum of the losses 1/(2^k_i y_i) from i=M onward is at most c_M. The product inequality product(1-u_i)>=1-sum(u_i), followed by a limit, gives

    1 <= E_j/E_infinity <= 1/(1-c_M).

Hence y_M,...,y_(M+J) are a common rotation of (10), with each circular phase moved in the positive direction by a multiplicative factor between 1 and 1/(1-c_M). Such a one-sided perturbation multiplies the maximum gap by at most 1/(1-c_M): an empty perturbed arc (a,b) would give an empty unperturbed arc (a,b(1-c_M)). Equation (11) certifies the finite actual net.

Only dilations by B^t=2^(Pt), t>=0, are now used. These preserve BOTH the component and the residue r modulo p^q. For X at least the largest net node, a net of gap less than R supplies a point in [X,RX] by such a dilation. When R>=B the assertion is immediate from one phase; for 1<R<B the empty-arc argument gives it. The required exponent is nonnegative because X is above all retained nodes.

Combining (1), (3) and z<2^k y, an admissible all-source height constant is

    C_(p,q,r,R)=((p+1)/2)*2^[P+(pP+k_min-1)(M+J)].        (12)

**CR2-003 (joint residue-window theorem).**

    For every p in {3,5}, q>=1, unit r mod p^q and R>1,
    there is an effective C_(p,q,r,R) such that
    for every N>=1 and real X>=C_(p,q,r,R)*N,
    there is an ordinary n in [N]_p intersect [X,RX]
    satisfying n=r mod p^q.

A maximum over the finitely many unit residues makes the constant uniform in r as well. The original source is universally quantified and remains fixed throughout the physical construction.

### 2.2 Finite examples, not practical height claims

The retained recipe certificates use M=32 and R=21/20. Examples are:

| p | q | r | P | kappa | J | Uniform C |
|---|---:|---:|---:|---:|---:|---|
| 3 | 1 | 1 | 2 | 0 | 64 | 2 * 2^674 |
| 3 | 1 | 2 | 2 | 1 | 64 | 2 * 2^674 |
| 3 | 2 | 1 | 6 | 2 | 256 | 2 * 2^5478 |
| 3 | 2 | 8 | 6 | 1 | 256 | 2 * 2^5478 |
| 3 | 3 | 1 | 18 | 2 | 512 | 2 * 2^29938 |
| 3 | 3 | 26 | 18 | 1 | 512 | 2 * 2^29938 |
| 3 | 5 | 47 | 162 | 153 | 4096 | 2 * 2^2010498 |
| 5 | 1 | 1 | 4 | 0 | 256 | 3 * 2^6340 |

These uniform constants are intentionally very loose. For a fixed source, its actual finite net supplies a substantially smaller explicit threshold. The q=5 example was used to instantiate the four-way gate in Section 5; its largest retained node has 1,312,421 binary digits. This is an exact symbolic/path certificate, not an assertion that it would be sensible to enumerate all sources below that height.

## 3. A concrete compact arithmetic space

For a ternary unit n let ell_q(n) be its discrete logarithm base two modulo 3^q, viewed in Z/(P_q Z), where P_q=2*3^(q-1). Define

    theta_q(n)=log_2 n - ell_q(n) in R/(P_q Z).           (13)

These coordinates are compatible under reduction from q+1 to q, since the discrete logarithms reduce compatibly. They are invariant under doubling, because both terms in (13) increase by one, modulo P_q.

This gives a map from dyadic classes of ordinary ternary units into the explicitly defined compact space

    Sigma_3 = inverse limit_q R/(P_q Z),                 (14)

where the maps are reduction modulo P_q. After rescaling the circles this is the familiar inverse-limit construction using threefold circle covers, a 3-adic solenoid. No external theorem about solenoids is needed here; (14) is the definition used in this packet. Compactness follows from closedness in the product of compact circles.

The ordinary embedding is injective on dyadic classes. Equality at the first coordinate already says log_2(n/m) differs from an integer by a multiple of two, hence is an integer; therefore n/m is an integral power of two. Conversely such multiplication leaves every coordinate unchanged.

**CR2-004 (all-component density in the compactification).** The image of the unit members of every original ordinary merger component is dense in Sigma_3.

Proof: for each fixed q choose any unit r and use CR2-002. Along that ladder ell_q(y_j)=ell_q(r), a constant, while log_2 y_j is dense modulo P_q. Thus the projection of the component to the q-th circle is dense. Every basic open set in the inverse limit is the pullback of an open condition at some finite level (combine finitely many conditions at their largest level), proving density. This uses actual ordinary ladder points, not an assertion that an arbitrary limiting point is ordinary.

A useful, limited Liouville statement follows. If F:Sigma_3->R is continuous and n->F(theta(n)) is constant on actual components, then F is constant: one component already has dense image. Values on multiples of three are fixed by their short forward arm to a unit.

Conversely, suppose a nonconstant invariant Boolean coloring b exists. Choose two components with different colors. Each has dense ordinary image in Sigma_3. Therefore b restricted to the ordinary embedded points is discontinuous at EVERY one of those points, and there is no extension to Sigma_3 continuous even at a single point. Every neighborhood contains ordinary points of both colors.

**Important boundary.** None of this proves that an arbitrary invariant b admits a continuous, measurable-with-useful-regularity, or bounded-variation extension. An almost-everywhere representative could erase a countable exceptional set. Density in a compact space does not identify distinct dense subsets. This compactification organizes the arithmetic coordinates; it does not supply the missing regularity.

## 4. Credited finite-pattern synchronization interface

For every finite set F of nonnegative integer offsets with at least two elements, the credited compiler supplies effective integers L,Q,B,e and t0, with M=2^L, A=3^Q, Q>=1, 0<=B<M, e a unit modulo three, and words w_d of common length L satisfying

    T^L(B+Mt+d)=At+e, for every d in F and t>=t0.         (15)

All original roots and intermediate states are positive for that tail. A singleton can be included in a two-offset pattern, and arbitrary finite integer offsets can be translated to nonnegative offsets.

Here is the construction being credited, restated to expose its exact scope. Families are affine functions of one common remaining parameter, with slopes powers of three. For a comparison (3^a y+b,y), a>0:

* For nonzero even b, impose y even and use 0/0; b halves.
* For odd b, impose y odd and use 0/1; a decreases by one and b becomes (b-3^(a-1))/2, with the old a in that expression.
* For b=0, impose y odd and use 1/1; the new intercept (1-3^a)/2 is nonzero.

Finitely many halvings and at most one zero-intercept preparation reduce a. Eventually one has a constant signed gap; order the arms to make it g>0. An even gap halves with lower arm even. A gap g=1 mod4, g>1, reduces to (3g+1)/4 by lower=1 mod4 and words 10/01 on the appropriate arms; a gap g=3 mod4 reduces to (3g-1)/4 by lower=2 mod4 and 01/10. All these new gaps are smaller. Gap one closes with lower=4 mod8 and words 001/100.

The current coefficient of the common parameter is odd, so every imposed power-of-two residue lifts consistently. Advance all arms by the same number of steps after each refinement; already merged arms stay merged. Induction merges the finite family. Choosing a sufficiently positive tail makes all physical states positive. At least one odd step is needed to merge distinct affine sources. Thereafter the endpoint is a unit modulo three, so Q>=1 and e is a unit.

This is a compiler on a freely selected common parameter cylinder. It is NOT permission to change the bits of a fixed original N. Section 5 connects the compiler to N by an actual endpoint in its component, without claiming the constructed roots are smaller than N.

Two credited gates checked here as all-parameter affine identities are

    T^3(4+8t)=T^3(5+8t)=3t+2,
    words 001 / 100;

and

    T^11(388+2048t+d)=243t+47, d=0,1,2,3,
    words 00101011100 / 10001011100 /
          01100011100 / 11101000001.                     (16)

The second is the same gate already stated in #134 and credited there to #132. Neither finite gate is counted as new in this pass.

## 5. Finite patterns in EVERY high relative interval

Fix a gate (15) and write D=max F. For y=e mod A define

    phi(y)=B+(M/A)(y-e).

Then phi(y) is an integer, and phi(y)+F is a monochromatic pattern in the component of y once (y-e)/A>=t0. To place it in [X,RX], it suffices to choose its endpoint in

    u(X)=e+(A/M)(X-B),
    v(X)=e+(A/M)(RX-B-D).                                (17)

Choose 1<S<R. For sufficiently large X, u(X)>0, S*u(X)<=v(X), and X>=B+M*t0. Apply CR2-003 with q=Q, residue e mod A, and relative width S. If u(X)>=C_(3,Q,e mod A,S) N, it supplies an endpoint y of the SAME original component inside [u(X),S*u(X)], in the required residue. Equation (17) then gives the desired entire pattern.

The threshold can be made explicitly linear in N. Put c=e-(A/M)B, a=A/M and C=C_(3,Q,e mod A,S). Then

    u(X)=aX+c,
    v(X)-S*u(X)=a(R-S)X+(1-S)c-aD.

It is enough to require

    X >= B+M*t0,
    X >= [D+(S-1)|c|/a]/(R-S),
    X >= (C*N+|c|)/a.                                  (18)

Together with X>=1 these imply all the needed inequalities. Since N>=1, replacing the fixed lower bounds by the same constants times N yields one effective C_(F,R). This explicitly handles the affine offsets rather than treating a limiting ratio as a proof at finite height.

**CR2-005 (relative-window pattern theorem).** For every fixed nonempty finite integer pattern F and R>1, there exists an effective C_(F,R) such that

    for every original N>=1 and every real X>=C_(F,R)*N,
    there is an integer x with x+F subset [X,RX] intersect [N].

All roots x+d reach the same endpoint y after the gate clock L, and y is connected by an explicit composed physical arm to an actual iterate of N. The final arm therefore retains a single common clock for all pattern members, while N retains its separate actual clock.

For F={0,...,K-1}, every component contains a K-block in EVERY sufficiently high relative interval. This combines the earlier thickness and relative-gap statements with an additional arithmetic coupling; neither old statement alone implies this joint placement.

### Why it still does not discharge the closing criterion

K is fixed before X. The proof gives no control adequate to choose K comparable to X, since the compiler's Q,L and the residue-net threshold depend on K. There is no proof of convergent blocks [X,(1+epsilon)X] at unbounded heights. Existing certificates for arbitrary fixed K, even placed in every relative interval, do not justify exchanging these quantifiers.

Also, disjoint abstract color classes can have this strong fixed-pattern property. For example, color n by the parity of floor(sqrt(n)). Each color has runs of length tending to infinity with gaps of size O(sqrt(X)) near X, so every fixed K fits inside each color in every sufficiently high [X,RX]. This coloring is not Collatz-invariant: it has different values at 2 and 4. The example only refutes the geometric inference from fixed-pattern placement to equality of components.

## 6. Explicit obstruction to a boundary-free finite regularity proof

Pass 1 sets d_n=b(n+1)-b(n) and derives the exact equations

    d_n=d_(2n)+d_(2n+1),
    d_(2n+1)+d_(2n+2)=d_(3n+2)+d_(3n+3)+d_(3n+4),

with d_1=0 and Boolean primitive. Its dyadic variation V_k has the birth identity V_(k+1)=V_k+2B_k. A proposed global closing target remains V_k=o(k).

On a finite interval 1..H, keep only physical edges whose endpoints both lie in that interval. Do not assign any exterior port the color of the component of 1. For an even H, define

    S_H={n: 2H/3<n<H and n=1 or 3 mod6},
    b_H(n)=1 for n in S_H, and 0 otherwise.              (19)

Each point of S_H is an isolated vertex of the truncated Collatz graph. It is odd and its outgoing endpoint (3n+1)/2 exceeds H. Its even predecessor 2n exceeds H. It has no odd predecessor, since the latter exists only for endpoints n=2 mod3, whereas (19) uses residues 0 and 1 modulo three.

Consequently b_H is an exact finite invariant coloring with b_H(1)=0. It satisfies every current equation whose full support is retained. For H=2^h its last-shell variation is

    V_(h-1)(b_H)=2|S_H|=(2/9)H+O(1),                    (20)

because each selected odd point has two unselected even neighbors, both boundary edges lie in the last shell, and the selected residues have asymptotic density 1/3 in an interval of length H/3.

**CR2-006 (finite-boundary obstruction).** No bound V_(h-1)=o(H), and in particular no sublinear-in-h bound, holds uniformly over all Boolean colorings satisfying only the fully retained equations on 1..2^h. Explicitly legal finite boundary assignments already force the linear-in-H lower example (20).

This does NOT refute the global regularity target. These colorings are not claimed to extend compatibly as H grows, and their first nonzero source moves outward with H. It refutes a boundary-free local estimate, not an estimate using anchored source conditions, compatibility through arbitrarily large exterior regions, or a boundary term that is actually controlled.

An eventual proof must therefore specify the exterior information it uses. Applying a finite calculation to the actual global coloring is legitimate only if that calculation's boundary hypotheses have been established; setting unresolved ports to zero is not such an establishment.

## 7. A control that survives the joint arithmetic compactification

The p=5 map has the disjoint positive cycles

    1 -> 3 -> 8 -> 4 -> 2 -> 1,
    13 -> 33 -> 83 -> 208 -> 104 -> 52 -> 26 -> 13.

Their basins supply two genuinely different components. CR2-001–003 nevertheless apply to each. Replacing P_q by 4*5^(q-1) and ell_q by the base-two logarithm modulo 5^q gives an analogous compact inverse limit in which both components are dense. Thus even the new **joint** arithmetic-logarithmic density does not by itself imply rigidity.

**CR2-007 (scope control).** A closing argument using only primitive-root lifting, the locked inverse identity, summable logarithmic errors and density in this compactification would also apply to these two disjoint p=5 components, so cannot be valid. It needs an additional property specific to the actual 3x+1 arithmetic and its compatible ordinary separators.

We do NOT assert the finite-pattern theorem for p=5. Its credited gap compiler exploits contraction by approximately 3/4, which is absent from the corresponding 5/4 expressions. Only the residue-window and compactification construction is generalized to the control map.

## 8. Exact evidence and remaining obligation

`experiment.py` and `verify_certificates.py` use only the Python standard library and explicit error checks, not removable assertions. The checker imports neither the generator nor any project module. This is same-author implementation diversity, not independent mathematical review.

Executed generator inventory:

* All 9,678 unit-residue input types from the stated grids: p=3, q=1..7, all units r and all three lifts modulo 3^(q+1); p=5, q=1..4, all units and all five lifts. The y=1 representative is raised within its unchanged residue type to meet y>=2.
* 42,240 fixed-source inverse edges physically replayed one shortcut step at a time, totaling 1,008,890 literal shortcut steps. For p=3 the grids use q=1,2,3, all units and original N=1..64; for p=5 q=1,2, all units and original N in {1,5,13,17}. Every ladder has 24 edges.
* Eight retained source nets with 6,272 inverse edges, 64 joint residue-window witnesses and eight four-block transplants. These large edges are checked as exact compressed physical words, not counted as another million literal steps. The largest retained node has 1,312,421 bits.
* Two all-parameter affine gates, two disjoint 5x+1 cycles, five explicit open-boundary coloring examples, and eight direct input/gate negative controls.

The standalone checker independently reconstructs all eight exact ideal nets using direct rational powers, verifies their universal inequalities and height exponents, all original-source anchors, all 6,272 compressed physical inverse edges and 64 windows. It replays each of the 32 four-block roots for 11 literal steps (352 steps), checks the all-parameter four-way gate, and rejects ten direct certificate mutations. It does not rerun or authenticate the generator's entire small-grid census; the validation receipt distinguishes the two inventories.

Normal and optimized generator outputs agree byte-for-byte. Normal and optimized checker outputs also agree byte-for-byte. The generator semantic digest is `d17742dbac2469f9ec0eab2b7deb53cea765ce8098a1842cc2379c476cd12872`. Full source/output hashes and commands are in the separate validation receipt. The compact JSON recipes regenerate their huge integers without float approximations or decimal-size-limit changes.

### First unsupported step

No sublinear global variation/birth bound has been derived. No macroscopic convergent-block family has been constructed. No arbitrary component separator has been shown to possess enough regularity to use the compactification's Liouville statement. The added geometry strengthens necessary structure but does not remove these obligations.

The sharp next theoretical task is a **boundary-aware, anchored arithmetic estimate**: control the influence of genuinely compatible exterior component data on interior separator variation, using the three-term current law and one fixed original source. CR2-006 says exactly why a uniform estimate on arbitrary finite boundary assignments will fail. CR2-007 says why joint density alone will fail. Any proposed estimate should retain both tests, rather than making the hypotheses silently strong enough to assume convergence.

No main or canonical scientific status was changed. No full-repository validator, remote CI, formal proof assistant, independent mathematical reviewer, or comprehensive priority audit was run in this pass. Container Git networking failed DNS; publication uses the authorized GitHub connector, with its commit and remote read-back recorded separately.
