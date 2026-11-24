# Stronger fixed-target depth bank: remove the predecessor-density input

**PROPOSED written deduction, conditional on the external joint floor F (paper 48, Lemma 7 and the bounded prepending argument of Theorem 8).** This supersedes the need for input M in the principal conclusions of README. It is also a different disjointness argument: varying the odd depth is now safe because the target is **fixed and nonperiodic**. No convergence theorem or positive-density input is used to build the bank. This note was developed after the fixed-depth/summed-total proof in README; that alternative remains available.

Use the same T, U, unit convention and floor (F') as in README, section 3. In particular for each sufficiently large b, 1<=K<=delta_*(b-1), each |s-2b|<=sqrt(b), any supplied unit q and unit class zeta modulo 3^K, at least

    c_* 2^s/(3^{b+K} sqrt(b))

distinct literal inverse words have b odd steps, total s, positive endpoint y=zeta mod 3^K, and

    y=(2^s/3^b)(q-beta_w), 0<beta_w<=F_*.

All constants are absolute. As in README, this is a written extraction of the multiplicity from the source-qualified joint probability floor, not an independent verification of that floor.

## 1. Main conclusions

A and B in README hold with **F alone** for A and **F,S** for B (M unnecessary), with possibly smaller absolute depth and critical-length constants.

More strongly, fix any modulus m>=1 and desired residues u,v modulo m. In each of those conclusions we may require every counted start to reach the fixed target a for the first time with

    tau_a(n) = u mod m,        P_a(n) = v mod m,

where tau is the physical shortcut clock and P counts odd inputs strictly before that first hit. In B this condition holds simultaneously for the entire consecutive block. The lower-bound constant and onset may depend on a,A,B,m, but the allowable mixed-adic depth and critical length constants can be chosen independently of all these fixed parameters (including m). The two phase residues are arbitrary, not selected after counting.

There is a direct uniform form: fix 0<A<B and 0<lambda<1. For every sufficiently large X, every **nonperiodic** unit q with

    Q_0(A,B) <= q <= X^lambda,

and every affine profile in the depth budget H+k<=eta_lambda log X, the phase-unrestricted lower bound on the number of constructed sources reaching q is

    c(A,B,lambda) X/(q 2^H 3^k).                              (U)

The threshold and constant in (U) are uniform in q. No claim is made for a periodic q using this varying-depth count, or for q comparable to X.

## 2. One fixed nonperiodic target

For an arbitrary fixed unit a choose a large unit q in A(a) which is not periodic. This needs no convergence assumption for a.

There are arbitrarily large unit odd immediate U-predecessors of a. Indeed 2 generates the units modulo 9, and exponents e>=1 in a suitable class modulo 6 make 2^e a equal to 4 or 7 modulo 9. Then q=(2^e a-1)/3 is a positive odd unit with U(q)=a, and q grows without bound on that progression. If a is nonperiodic, all its predecessors are nonperiodic. If a is periodic, only the finitely many vertices of its own cycle can be periodic predecessors, so choose a sufficiently large q outside that cycle. We only need existence; no computable test distinguishing these two cases is assumed.

For later use choose q so large that q>F_*+1 and B F_*/q <(B-A)/12. This choice is independent of X and the source residue. Fix the actual physical and odd-count clocks (tau_a(q),P_a(q)) for the path to a.

If an integer y reaches a nonperiodic q at odd depth b, it cannot reach q at any different odd depth: otherwise U^j(q)=q for some j>0. This proves exactly the disjointness of the inverse-word populations when b varies. Similarly an arbitrary source that eventually reaches this q cannot have visited a earlier, because then a reaches q and q reaches a, making q periodic. Consequently the passage through q is before (or at) the first hit of a, and its exact clock and odd count may be used to control the first-hit residues.

## 3. Fix the affine profile, vary the depth

Let T^H(n+i)=z+3^p t on n=r+2^H t for 0<=i<M, as in README section 4. Here H>=1, 1<=p<=H, 3 does not divide z, 0<=r<2^H, and z+1<=3^H. M=1 is allowed. Impose n=l mod 3^k by requiring

    y=zeta=z+3^p (l-r)2^{-H} mod 3^{p+k}.

All inverses in this congruence are taken modulo 3^k for the inner factor. Thus zeta is a well-defined unit class. As before each counted word supplies

    n=L_{p,b,s}(q-beta_w)+r-2^H z/3^p,
    L_{p,b,s}=2^H 2^s/3^{p+b}.                              (1)

The difference from L_{p,b,s}q consists of a nonpositive word correction bounded by L_{p,b,s}F_* and the canonical offset bounded by 2^H+2^H3^H.

Put alpha=log_2 3, d=2-alpha>0, and

    Y = X 3^p/(q 2^H),
    b_0 = log_2(Y)/d.

For q fixed, or Q_0<=q<=X^lambda, and H+k<=eta_lambda log X for sufficiently small eta_lambda>0, we have

    c_lambda log X <= b_0 <= C log X

for all large X, uniformly over the affine profile and q in the uniform range. This follows by expanding log_2 Y=log_2 X-log_2 q+p alpha-H. Choose eta_lambda so small that H+k<=delta_*(b-1) for all integers b in the window below; also 2^H+2^H3^H=o(X) uniformly. These requirements are compatible: b_0 is bounded below by a positive multiple of (1-lambda) log X. In the fixed-target case use lambda=1/2 once X is large enough. Thus the constants for fixed targets are absolute.

Use the consecutive integer window

    floor(b_0) <= b <= floor(b_0)+floor(c_w sqrt(b_0)),

where c_w>0 is absolute and d c_w<1/4. For all sufficiently large X these b exceed the common floor onset. Let A'=A+(B-A)/3, B'=B-(B-A)/3. Seek an integer total s such that

    log_2 A' <= s-b alpha-log_2 Y <= log_2 B'.                (2)

This is exactly A'X<=L_{p,b,s}q<=B'X. If such an s exists it is automatically central:

    |s-2b| <= d |b-b_0| + max(|log_2 A'|,|log_2 B'|)
             <= sqrt(b)

for all sufficiently large X, uniformly in the window. It is then at least b and is admissible for F'. The constants in the last large-X threshold can depend on the fixed interval shape.

### The finite phase bank, including both first-hit residues

For unmarked counts take m=1. To prescribe the two first-hit residues, require

    b = v-p-P_a(q) mod m,
    s = u-H-tau_a(q) mod m.

The first congruence selects a progression of b in the window. For this progression, b alpha+log_2 Y modulo m evolves by m alpha modulo m. Since alpha is irrational, the normalized phase rotation on the circle of length m is irrational. Condition (2), with the fixed s residue, is membership in an arc of fixed positive length (one may shorten the interval in (2) to length <1 and use its interior). A finite orbit segment of this rotation forms a net, so for some L_m depending only on the interval shape and m, **every** L_m consecutive allowed b's contains a hit, regardless of the starting phase log_2 Y or the two prescribed residues. Thus >=c(A,B,m) sqrt(b_0) distinct b in the window admit a corresponding s. This uses compactness of the circle and density of an irrational rotation, not an unproved rate or fresh independence. Choose one qualifying s per b.

For all these pairs (b,s), F' applies at K=p+k. Each produces at least

    c_* 2^s/(3^{b+p+k} sqrt(b))
      = c_* L_{p,b,s}/(2^H 3^k sqrt(b))
      >= c_* A' X/(q 2^H 3^k sqrt(b))                       (3)

literal sources, by (1). The offset term in (1) is o(X), while the word correction is at most B' X F_*/q < (B-A)X/12. Hence every resulting n lies strictly inside [AX,BX] with a fixed margin times X. If M=o(X), its entire consecutive block lies in the same interval. The lift t is nonnegative for large X. The common physical clock H+s from each n+i reaches q; the exact odd count to that visit is p+b, because the b-gap inverse word is literal and y is odd. No earlier visit to a is possible by nonperiodicity of q, as proved in section 2. Therefore the first-hit phase congruences hold for all i.

Within a fixed b, the full gap list is uniquely read by U from y, so different counted words give different y and n. Across different b's, any duplicate n would give the identical y=T^H(n) reaching the fixed q at two distinct odd depths, which is impossible. This is crucial: if q were periodic, or if we selected a moving q for every b, this argument would fail. Sum (3) over >=c sqrt(b_0) depths with b asymptotic to b_0. We obtain

    # starts >= c(A,B,m) X/(q 2^H 3^k).                     (4)

In particular there is no square-root loss and no assumption about a predecessor-density pool. In the fixed-target setting q is fixed once and for all, so absorb 1/q into the lower-bound constant. In the unmarked uniform form q may vary with X up to X^lambda: every use of F', the phase-bank size and all bounds above are uniform, as long as q>=Q_0 so the real word correction is small. No phase marking is needed for this uniform statement.

## 4. Consequences on native binary cylinders and synchronized blocks

Extend any binary prefix by one odd step as in README section 5 and apply (4) with M=1. This gives A and its simultaneous phase strengthening under F alone, for every mixed-adic residue (including multiples of three) and h+k<=eta log X, for an absolute eta>0. In the case of B, use S to obtain >=2^{H-2} refined synchronizing residues of the common length H=ceil(C_S log^2(2M))+1; take c_0,eta_1 small enough as in README. Apply (4) separately on each residue with its own p,z but the same fixed q and the same depth/phase admissibility constants, and add disjoint binary classes. This gives the claimed positive density of block starts for M=floor(exp(c_0 sqrt(log X))) with each prescribed phase. The actual prefix clocks H+s are O(log X), with uniform constants; the final path q to a adds its fixed finite clock.

As a special case M=1,h=k=0,a fixed, this recovers positive lower ordinary predecessor density using F, with the proof based on fixed nonperiodic q and disjoint odd-depth slices. It is conditional on F; it is not an independent unconditional verification of Mazur's theorem. The uniform form (U) is a mixed-cylinder version of reciprocal-density lower bounds. It does not imply that the sum of reciprocals over a disjoint antichain of ancestors diverges.

If Collatz is false, choose a nonconvergent unit a, and use the disjoint predecessor pools of 1 and a. In each allowed mixed-adic cylinder the true colors B,+,- (not reaching 1, reaching 1 at even first shortcut clock, reaching 1 at odd first shortcut clock) now each have positive lower relative density, with absolute uniform depth budget and target-dependent constants. For the convergent colors take m=2 and either u, allowing either v. This rules out an arbitrary low-digit classifier for **any** of these three labels with o(X) total mistakes under F. It also rules out an exceptional nonconvergent set supported on an o(1) fraction of these growing mixed cylinders.

## 5. Optional growing phase modulus (source-qualified Diophantine input)

Use the fixed two-logarithm separation bound D from PR202 (Rhin, as quoted in Simons-de Weger Lemma 12):

    ||j alpha|| >= c_D j^{-kappa},    kappa=13.3, j>=1.

For any fixed 0<nu<1/(2(kappa+1))=5/143, the proof gives

    # starts >= c(a,A,B,nu) X/(q 2^H 3^k m^2)

uniformly for 1<=m<=(log X)^nu and all two first-hit residues, with q fixed as above. In this statement c may absorb 1/q or not; it is independent of m and the residues. Indeed along the allowed b progression, normalize the circle of length m to circumference one, and use the rotation by alpha. The target arc has length >=c(A,B)/m. Pick the first convergent denominator Q>=C(A,B)m, where C is large enough. D and the preceding convergent estimate imply Q<=C' m^kappa. A consecutive Q-term rotation segment is within 1/Q of a translated Q-point grid, and therefore contains >=c Q/m hits to the target arc. The b window has >=c sqrt(b_0)/m allowed values, which is >>m^kappa since m^{kappa+1}=o(sqrt(log X)). Partition into complete Q-blocks and discard the last incomplete block. This gives >=c sqrt(b_0)/m^2 distinct qualifying b. The proof of (3) then supplies the bound. B follows by the same disjoint binary summation. This optional refinement uses D; the fixed-modulus result and F-only positive-density result do not.

## 6. The actual closure gap

The stronger result is directly relevant to PR195's third-phase obstruction: all three actual phases are present at positive relative density in every growing mixed-adic class on macroscopic intervals. But the selected discordant pair in PR195 can be extremely localized in real space, and the phase-absence window there is much shorter than a macroscopic interval. This theorem gives no lower mass for third-phase points in such a selected window.

Likewise the count (U) for nonperiodic targets gives a uniform lower inverse mass at a reciprocal scale; turning it into a contradiction by summing along an escaping ray still requires a disjoint side-cut mass whose sum diverges. PR192's current basin.md identifies exactly that missing bound. Ancestor sets of distinct forward values on a single ray are nested, not disjoint. No summation of their masses is justified.

Thus the new bridge removes the separate predecessor-density assumption from the main density theorem, and controls genuine phase-marked cylinders, but does not prove Collatz. The next target is a short-real-window lower floor **conditional on the original two-class survivor**, not a further unmarked marginal estimate.
