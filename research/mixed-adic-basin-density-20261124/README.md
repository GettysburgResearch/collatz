# Polynomial mixed-adic cylinders and positive-density critical-length basin blocks

**Status: PROPOSED written deductions from SOURCE-QUALIFIED inputs. Collatz remains OPEN.** No independent rebuild of the external analytic proofs and no Lean compilation in this session. The finite checker and proposed Lean transport core are separate evidence. The point is to keep the entire multiplicity in the inverse-word floor, not just use its existence consequence (the linear-budget router).

Use the positive shortcut map T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n, with T(0)=0 only for finite canonical-prefix calculations. For odd n>0, let U(n)=(3n+1)/2^v_2(3n+1). A **unit** is a positive odd integer prime to three. A(a) denotes the ordinary predecessors of a fixed unit a, i.e. integers whose actual T orbit visits a. All logarithms below are natural unless indicated.

## Stronger continuation: fixed-target depth bank

The subsequent [fixed_target_depth_bank.md](fixed_target_depth_bank.md) removes input M from both principal conclusions: A follows from the source-qualified floor F alone, and B from F,S. It fixes one large nonperiodic predecessor of the desired target, then sums over distinct inverse odd depths rather than totals at a fixed depth. The populations cannot overlap. It also prescribes both first-hit clock and odd-count residues modulo any fixed modulus, with an optional growing-modulus refinement using the Rhin phase-gap bound. Its stronger conclusions are the preferred handoff. The alternative fixed-depth proof below is preserved because it uses a different counting cancellation and allows a moving pool of targets.

## 1. The new conclusions

**Theorem A (mixed-adic lower density, conditional on F and M below).** There exists an absolute eta>0 with the following property. Fix a unit a and a fixed real interval shape 0<A<B. There exists c=c(a,A,B)>0 such that, for all sufficiently large X, simultaneously for all integers h,k>=0 with h+k<=eta log X and ALL residues r mod 2^h and l mod 3^k,

    #{n in [AX,BX] intersect A(a): n=r mod 2^h, n=l mod 3^k}
        >= c X/(2^h 3^k).                                      (A)

The depth budget can be reduced further by any fixed factor. The constant and threshold do not depend on h,k,r,l. In particular this handles a polynomial-size growing modulus, and an arbitrary prescribed binary parity prefix of length h (the low binary bits and T parity prefix are bijective).

**Theorem B (positive density of critical-length synchronized blocks, conditional on F,M,S).** There exist absolute eta_1,c_0>0. Set

    M_X = floor(exp(c_0 sqrt(log X))).

For each fixed a,A,B as above there exists c>0 such that, uniformly over all k<=eta_1 log X and every l mod 3^k, at least

    c X/3^k

different starting integers n in [AX,BX] with n=l mod 3^k have their **whole block** n,...,n+M_X-1 inside [AX,BX] and in A(a). All members reach the same intermediate unit at a common physical T clock, bounded by C log X with an absolute C. The clock need not be the same across different starting blocks. For k=0, greedy disjoint selection yields >=c X/(2 M_X) disjoint blocks, whose union therefore occupies a positive fraction of the interval. More generally the same selection yields >=c X/(3^k(2 M_X-1)) disjoint blocks (round down if needed).

Both eta and c_0 can be chosen independently of the fixed target, unlike choosing a synchronization-error bound smaller than that target's unknown density. Theorem B improves PR202's scale to an absolute small constant times sqrt(log X) in the exponent and, more importantly, replaces subpower density loss by a constant fraction. It concerns **single-target blocks**; no simultaneous ratio-five or distinct-target pair routing is asserted.

## 2. Exact imported inputs

* **F (SOURCE-QUALIFIED, recent external paper):** lyapunov_weaver, *Hierarchical Syracuse renewal and linear valuation budgets for modular routing*, rStation [paper 48](https://rstation.ai/problems/collatz/papers/48), Lemma 7, equation (76), and the proof of Theorem 8, equations (80)-(83). The retrieved primary text gives a uniform floor for the original independent Geom(1/2) positive gaps on a fixed unit cylinder at depth h_0, when the total is within 2 sqrt(b) of 2b and the additional ternary precision is at most delta_* b. It includes an absolute real-offset bound F_0 and a logarithmic cap on each gap. The prepended bounded exponent in Theorem 8 spreads this floor to every unit residue. We use that proof at all central totals, not just the particular total 2b in the theorem's stated existence conclusion. No independent proof or kernel replay of this analytic floor is claimed here.
* **M (SOURCE-QUALIFIED, external):** Lech Mazur, *Positive Lower Density of Collatz Predecessors*, manuscript v1.0, Sept. 6, 2026, [ProofAtlas release](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/). For each fixed positive target prime to three, the ordinary predecessor set has positive lower natural density. The public release reports a Lean compilation, not independently rebuilt here. We use it only through the elementary fixed-shape local unit-pool construction in PR202, section 3, pinned below. No density estimate uniform in a, effective threshold, or convergence of all predecessors to 1 is assumed.
* **S (SOURCE-QUALIFIED, repository):** PR146, frozen commit f431078244e868dc699fad011044f0d5e7f76437, [WHOLE_INTERVAL_SYNCHRONIZATION.md](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md), equation (4). For M consecutive forms there are >=2^{H-1} residue classes modulo 2^H on which their exact affine profiles coincide at a common H=ceil(C_S log^2(2M)). Indeed (4) bounds the failure probability by C ceil(log_2(2M))/sqrt(H) under uniform low bits; once the first group coalesces its equality persists. We need only the first group, not five times the group or its later ratio-five return. We do not certify this probability estimate in the present PR.

The local pool input extracted from M is

    # {q unit in A(a): AY<=q<=BY} >= c(a,A,B) Y                   (P)

for each fixed 0<A<B and all sufficiently large Y. For completeness its argument is in PR202 commit 3b10b24d12d4b349cb20f4cbc83086c8a09f807e, [README section 3](https://github.com/GettysburgResearch/collatz/blob/3b10b24d12d4b349cb20f4cbc83086c8a09f807e/research/synchronized-long-basin-blocks-20261124/README.md#3-actual-unit-populations-in-real-intervals). Strip at most a fixed number of powers of 2 from a positive fraction of the ancestor pool; when the resulting odd ancestor is divisible by 3, take its next shortcut step and one of two short odd inverse lifts to obtain a unit. This conversion has bounded height factor and multiplicity. A finite inverse phase bank, with successive odd inverse lifts into 1 mod 9 and an exponent in a fixed progression as final padding, localizes a constant fraction to any fixed multiplicative interval. Its phases are an irrational rotation modulo 6 and a finite net suffices, so no Diophantine rate is needed here.

Only the stated inputs and elementary finite counting are used. Their assumptions cannot be replaced by typical-point convergence or by a single existence route.

## 3. Deriving the uniform count of inverse words

For inverse gaps e_1,...,e_b>=1, listed starting from the target q, put s=sum e_i and

    beta_w = sum_{i=1}^b 3^{i-1} 2^{-(e_1+...+e_i)}.

Then the full inverse composition is

    y = I_{e_b} ... I_{e_1}(q) = (2^s/3^b)(q-beta_w),
    I_e(u)=(2^e u-1)/3.                                        (1)

Fix constants delta_*, F_0, c, n_0, h_0 and the unit cylinder y_0 mod 3^{h_0} in Lemma 7 of F. Let b be sufficiently large, 0<=K<=delta_*(b-1), |s-2b|<=sqrt(b), and r_beta any unit residue modulo 3^{b+K}.

Since 2 generates the units modulo 3^{h_0+1}, choose v in the fixed finite range [1,2*3^{h_0}] with 2^v r_beta=1+3y_0 modulo 3^{h_0+1}. The tail residue

    (2^v r_beta-1)/3 mod 3^{b+K-1}

lies above the fixed cylinder and is well defined. Lemma 7 applies at n=b-1, extra depth K and total s-v, because

    |(s-v)-2(b-1)| <= sqrt(b)+|2-v| <= 2 sqrt(b-1)

for all sufficiently large b, uniformly over the bounded v. Under the original iid gap law, every word of length n and total t has probability 2^{-t}. The exact slice probability pi_n(t)=binom(t-1,n-1)2^{-t} is >=c_1/sqrt(b) on this central range, by Stirling's inequalities. Converting the floor (76) into a count, then prepending v, gives

    # {w: length b, total s, beta_w=r_beta mod 3^{b+K},
               beta_w<=F_*}
         >= c_* 2^s/(3^{b+K} sqrt(b)),                           (F')

with absolute positive constants c_*, F_* (take F_*=1+3F_0), a common onset, and no dependence on r_beta or s in the range. In fact the logarithmic individual cap survives after a constant adjustment, but we do not need it.

This deduction is the quantitative part not present in the existence-only interface used in PR202. It retains the multiplicity of words on each total slice. Importantly, it does not multiply marginal probabilities of the total and the residue; the joint floor (76) is essential.

Now fix any unit q and any unit class zeta modulo 3^K (K>=1). Take

    r_beta = q - 3^b 2^{-s} zeta mod 3^{b+K}.

This is a unit because b>=1. For all counted words, (1) is integral and y=zeta mod 3^K. Full composite integrality forces each prefix integral: reduce the numerator first modulo 3 to get integrality of I_{e_1}(q), cancel that factor and repeat. Starting from an odd positive q, every integral I_e with e>=1 is positive odd. Each intermediate value has to be prime to three since it admits the next inverse odd step; the terminal is a unit by zeta. Thus every counted word is a literal ordinary inverse itinerary. In particular U^b(y)=q and T^s(y)=q. Different words at the same q,b,s give different y, because U reads the exact positive gaps backwards from y. We can use any K up to delta_*(b-1), not a different b for each residue.

## 4. A uniform affine transfer estimate

Let H>=1, 1<=p<=H, r in [0,2^H), z>=0 with 3 not dividing z and z+1<=3^H. Suppose M consecutive forms have a single affine profile on this binary class:

    T^H(r+2^H t+i)=z+3^p t,    0<=i<M,                          (2)

whenever all starts are positive. This includes M=1 with any prefix after making its final odd count positive.

Impose a further starting congruence n=l mod 3^k. For n=r+2^H t this is equivalent to t=t_0 mod 3^k with t_0=(l-r)2^{-H} mod 3^k. Thus the endpoint y of (2) must belong to the class

    zeta=z+3^p t_0 mod 3^{p+k}.

It is a unit class, because p>=1 and 3 does not divide z. Choose one b=max(b_*,1+ceil((H+k)/delta_*)) (increasing b_* by a fixed amount if needed), for all p<=H, all residues, all target q and all central totals s. Then p+k<=delta_*(b-1). Apply (F') at K=p+k. Write

    L_{p,s}=2^H 2^s / 3^{p+b}.
    n = r+2^H (y-z)/3^p
      = L_{p,s}(q-beta_w)+r-2^H z/3^p.                         (3)

Both congruences hold. Uniformly for all allowed parameters,

    |log L_{p,s}| <= C_2(H+k+1),
    |n-L_{p,s} q| <= L_{p,s}F_*+2^H+2^H 3^H
                   <= C_3 exp(C_3(H+k+1)).                     (4)

Choose absolute eta'>0 small enough that if H+k<=eta' log X then L_{p,s} and its reciprocal are <= X^{1/4} and the absolute error is <= X^{1/2} for all sufficiently large X. The thresholds in these bounds are absolute; this choice does not depend on the target a.

Take a fixed interior subinterval [A'X,B'X] of [AX,BX], for example A'=A+(B-A)/3, B'=B-(B-A)/3. For each central total s use the pool of units q in A(a) in

    [A'X/L_{p,s}, B'X/L_{p,s}].

By (P), since X/L_{p,s}>=X^{3/4}, this pool contains >=c(a,A',B') X/L_{p,s} choices, uniformly over s and p, at all sufficiently large X. Each q is kept fixed during the inverse construction. Equations (3)-(4) place n in [AX,BX] with a margin of order X; whenever M=o(X), the entire block is in that interval. Also t=(n-r)/2^H>=0 for large X. The exact legality argument above and (2) give T^{H+s}(n+i)=q for all i<M. Hence n+i are actual predecessors of a.

At a particular s, the number of constructed starting integers is at least

    c(a,A,B) (X/L_{p,s}) * (2^s/(3^{b+p+k} sqrt(b)))
      = c(a,A,B) X/(2^H 3^k sqrt(b)).                          (5)

There is **no collision in this count**: a given n determines its endpoint y=T^H(n), its next b odd steps, their total physical clock s and the resulting target q. The exact gap word w is the reverse of that forward gap list. Even if q lies in a cycle, b fixes which visit is being used. The same uniqueness proves that sets counted at *different central totals* are disjoint. There are at least sqrt(b) integer totals in [2b-sqrt(b),2b+sqrt(b)], for every b>=1. Summing (5) therefore yields

    #{n satisfying both congruences and whole-block reachability}
        >= c(a,A,B) X/(2^H 3^k).                              (6)

This is the central cancellation: the 2^s/3^b inverse multiplicity pays the forward scale factor, and the central total range pays sqrt(b). Fixing the odd depth, rather than the physical clock, is what makes this sum exact. The count would not be justified by summing separate depths b; a source could be counted repeatedly that way.

## 5. Deductions A and B

For A, given any original residue r mod 2^h, extend the finite prefix by **one** extra odd shortcut step: write T^h(r+2^h t)=z_0+3^{p_0}t and choose v in {0,1} making z_0+3^{p_0}v odd. Then the refined class r'=r+2^h v mod 2^{h+1} has H=h+1, p=p_0+1 and canonical endpoint z=T(z_0+3^{p_0}v), so 3 does not divide z. The elementary inequality T(m)+1 <= (3/2)(m+1) gives z+1<=3^H since r'<2^H. This works also for h=0 and r=0. Choose eta<eta'/2. Apply (6) with M=1; the extra factor 2 is absorbed by the constant. This proves A in the original class, with no restriction on l even when l=0 mod 3.

For B, take M=M_X, H_0=ceil(C_S log^2(2M)), H=H_0+1 and select >=2^{H_0-1} synchronized binary classes from S. Refine **each** by the same one-bit odd-step rule just used; their new residues are distinct modulo 2^H. Their p,z may vary, but (4)-(6) were uniform in them. Choose absolute c_0>0 small enough that H_0<= (eta'/3) log X for large X, and eta_1<=eta'/3. Then H+k<=eta' log X and M=o(X). On every refined class (6) gives >=c X/(2^H 3^k) starts. Add the counts on at least 2^{H-2} disjoint binary classes. This gives the claimed positive fraction of starting indices, all in the specified ternary class. The physical clock H+s is O(H+k+1)=O(log X). Greedy packing proves the disjoint-block consequence.

The synchronization input already implies large blocks for almost all starts in a *subcritical* range log M=o(sqrt(log X)), and in a target-dependent small critical range one can simply make synchronization failure rarer than that target's density. The new B fixes the critical-range constant before the target is chosen, works even for a growing ternary congruence, and gives the constant-density count directly by the multiplicity transport. This is not a claim of historical priority over all external literature.

## 6. A global obstruction and its precise limitation

Suppose there exists any nonconvergent positive integer. Its orbit reaches some fixed odd unit a (remove twos, take one odd step, then remove twos). This a cannot reach 1; its ancestor set A(a) is disjoint from A(1). Apply A separately to the two fixed targets, with the same absolute eta. In **every** allowed mixed-adic cylinder in a fixed-shape interval, both basin colors have a uniformly positive fraction. In particular:

* Any classifier of the convergence indicator based only on the lowest h binary bits and k ternary digits, h+k<=eta log X, has error >=c X on [X,2X] if Collatz is false. The classifier may be an arbitrary lookup table, depend on X, and have exponentially many entries in the digit budget. No finite automaton restriction.
* The same holds for arbitrary adaptive binary/ternary prefix queries with a common depth budget: refine all terminal query cylinders to a common pair of full depths within a (possibly halved) budget. Equivalently count the disjoint terminal cylinders and sum their uniform errors.
* Thus under F,M, a sequence of such classifiers with o(X) mistakes would settle Collatz (including cycles). In particular the local lower bound must be on the **true** convergence colors, not the finite stopping-to-a-moving-floor colors.

Proof of the first statement: for each of the 2^h3^k disjoint classes in the interval the classifier gives one fixed bit. At least min(c(1),c(a)) X/(2^h3^k) actual members of the opposite color occur there by (A). Sum over the classes. For the adaptive variant, each leaf is a class with some h',k' and the leaf classes partition the full residue space; their reciprocal moduli sum to one. No assertion that the classifier itself is available is being made.

By B, both colors also have positive-density sets of starting positions of blocks of the SAME critical length exp(c_0 sqrt(log X)). This continues to hold inside every macroscopic interval with any ternary starting class in the depth budget. A hypothetical counterexample is therefore not a sparse exceptional low-digit pattern. But the two collections may be spatially segregated; a positive-density lower bound for each does not imply the existence of either color inside *every* small neighborhood of a specified discordant pair. In particular this does not remove the remaining two-class obstruction of PR195 and PR197, or establish the directed implication from PR193. The exact missing bridge is short-interval conditional mixing at the **selected** original discordant sources, or construction of a predictor with the stated error guarantee. Neither follows just from the floor used here.

## 7. Relation to current work and next target

- PR202 (3b10b24d12d4b349cb20f4cbc83086c8a09f807e): common-clock routing and macroscopic phase-bank localization. The present proof replaces its existence route and fixed single total by joint multiplicities summed at fixed odd depth.
- PR193 (67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e): exact one-way binary-child closure and collision-energy target. A reduction to one directed pair does not imply conditional lower color mixing.
- PR197 (6eb986b0ce0b1836a356474d25d709ed4e948b67), HEAD_INCIDENCE.md: distinct regenerated smaller heads counted with original-source multiplicity; its recurrence still admits a nonsummable two-class remainder.
- PR195 (1c6e750e2f6970e6d5456cba5a93c2f3de8c2a97), round5/head/README.md: summable third-phase neighborhoods of actual discordance. The present block theorem cannot be substituted for a short-interval bound conditioned on that selected remainder.
- PR200 (39918be724038ac550d77c7fc95d17e05251dfc6), FOURIER_UNIFORMITY.md: Fourier/automaticity restrictions on true color; A instead gives a direct uniform lower bound on growing mixed-adic cylinders. No higher-order Fourier conclusion is claimed.
- PR199 (d868f8e8405c08b8c501236853bea495ca593824): target-specific sparse sections using Mazur and first-passage rigidity. PR201 (084b983fbec6f3d2120ef101946754431f82874e): low-grade summability and odd-grade spreading. PR182 (234fd2ece3a17c8950dce452291198705b4e6e60): the dyadic companion remains a separate arithmetic route; see companion_obstruction.md for the conjugate-height calculation.
- The external literature input F is stronger than the theorem D in paper 37 used previously. It is the *fractional extra precision* and the **joint fixed-total floor** that enable the new estimate.

These are source reads and narrow interfaces, not a fresh independent audit of all files or all recent proofs. The stronger continuation above removes the separate positive-density assumption and adds exact first-hit phases, but does not solve the two-class remainder. The next high-value target is to exploit the original-word conditional floor under a **second** output constraint while retaining enough multiplicity to insert a third phase at a selected head pair. A second unconstrained marginal, or summing words at varying odd depth without accounting for duplicates, would not suffice.

## 8. Evidence

Finite transport and counting identities are exercised by controls.js (see CONTROLS.json for executed counts). MixedTransport.lean is a proposed finite core for composition, inverse-word uniqueness and injectivity across totals. No Lean toolchain or independent subagent runtime was available. **No new kernel verification, whole-repo validator run, or independent analytic proof review is claimed.** The full theorem is conditional on the exact named source inputs. Collatz remains open.
