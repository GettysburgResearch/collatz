# A shrinking real annulus for every ternary unit and an empty descent region

**Status.** The annulus count is a proposed deduction from the source-qualified floor F. The descent exclusion is an elementary statement about every literal ordinary word. No claim of Collatz convergence or of an independent verification of the analytic proof of F is made.

Use the shortcut map T(n)=n/2 for even n and (3n+1)/2 otherwise, and its accelerated odd map U. An outward word is read from its target, with positive exponents e_i, length b, total s, partial totals S_i and real offset

    β(w) = Σ_{i=1}^b 3^(i−1) 2^(−S_i),       G = 2^s / 3^b.

At target q the candidate integer source is G(q−β). Reduction of the dyadic rational β modulo 3^j uses its odd-modulus inverse of 2.

## What the primary source actually supplies

Weaver and Wren, *Hierarchical Syracuse renewal and linear valuation budgets for modular routing*, paper 48 v2, 28 October 2026, Lemma 7, equation (76), gives absolute h₀, δ, F, A, c and N and one **fixed unit cylinder** y mod 3^h₀. At length n≥N, integer 0≤K≤δn, integer |t−2n|≤2√n, and every z above y mod 3^h₀ at depth n+K, it asserts

    3^(n+K) P(β=z mod 3^(n+K), S_n=t, β≤F,
                   max e_i≤ceil((3/2)log₂(n+1)+A)) ≥ c π_n(t),

where the letters are independent with P(e_i=j)=2^(−j), j≥1, and π_n(t)=2^(−t) binom(t−1,n−1). The offset on the inequality side is the ordinary real dyadic number; the residue is the reduction of that very number. The constant F has no numerical value in the paper. For this central range Stirling gives π_n(t)≥c'/√n uniformly as n→∞.

Theorem 6 equation (66) controls fine-scale ternary oscillation *summed* over exact total slices. Lemma 7 additionally uses the selected-prefix transfer (70)–(75), a positive base cylinder and a last free tail of length at least n/1616; its proof chooses δ≤min(δ₂/1616,1/1000). The height bound comes from the paragraph after (79) bounding the selected prefix offset plus its contracted free-tail offset. It does not provide a density over intervals in the real variable. Theorem 8's proof (80)–(83) uses a bounded first letter to spread one fixed cylinder over the unit residues for total 2b, and verifies ordinary legality by prefix peeling. These are the primary hypotheses being used. The full Fourier, stopped renewal, collision and selected-block arguments are external inputs here. [Primary v2, §§8–9](https://rstation.ai/problems/collatz/papers/48/v2)

Declaring each fixed-total word to have its exact mass 2^(−s) converts the stated joint probability to a word count. Prepending v sends β_tail to (1+3β_tail)2^(−v). With v bounded, this gives the all-unit central version of F used in PR203 for |s−2b|≤√b, because |s−v−2(b−1)|≤2√(b−1) eventually. Weaver's paper 202 v1, §2 input 2, independently states precisely this fixed-total counting interface and credits paper 48. [PR203 at 3f2c89f12b057b8bb8655bd6fc794c772aa8b65d](https://github.com/GettysburgResearch/collatz/blob/3f2c89f12b057b8bb8655bd6fc794c772aa8b65d/research/mixed-adic-basin-density-20261124/README.md) · [Weaver 202 v1](https://rstation.ai/problems/collatz/papers/202/v1)

## An annulus at every small real scale

Assuming F, there are absolute c₀,c₁,C,b₀>0 such that for b≥b₀, |s−2b|≤√b, 0≤K≤δ(b−1), every unit r mod 3^(b+K), and

    2^(−√b/2) ≤ ρ ≤ 1,

at least

    c₁ ρ 2^s / (3^(b+K) √b)                                    (1)

distinct words of length b and total s have β=r mod 3^(b+K) and c₀ρ≤β≤ρ. All satisfy

    max_i e_i ≤ max(ceil((3/2)log₂ b+A), log₂(1/ρ)+C).

Proof. Let P=2·3^h₀, the order of 2 modulo 3^(h₀+1), and L=ceil(log₂((1+3F)/ρ)). Among v=L,...,L+P−1, choose the unique residue satisfying

    2^v r = 1+3y mod 3^(h₀+1).

The class z=(2^v r−1)/3 mod 3^(b−1+K) is well-defined and lies above the fixed base cylinder. Also v≤√b/2+C, so |(s−v)−2(b−1)|≤(3/2)√b+C+2≤2√(b−1) uniformly for large b. Apply F at length b−1, total s−v, deficit K and residue z. Prepending v gives the claimed full length, total and residue. The image obeys

    2^(−v) ≤ β = 2^(−v)(1+3β_tail) ≤ ρ,
    2^(−v) ≥ ρ / (2^P (1+3F)).

Each tail word has probability exactly 2^(−s+v). Consequently the source's lower bound gives at least c 2^(s−v)/(3^(b−1+K)√b) distinct words. The lower bound on 2^(−v) proves (1). The appended cap in the conclusion is the actual cost of moving the first letter. Keeping the source's logarithmic cap would prohibit all scales below 2^(−cap), since β≥2^(−e₁). No word law has been reweighted or restarted on an actual forward trajectory.

The ordinary application is exact. At a positive odd unit q and a unit terminal class a mod 3^K, K≥1, take r=q−3^b2^(−s)a mod 3^(b+K). Each word in (1) yields a distinct positive odd unit I_w(q)=G(q−β) in

    [G(q−ρ), G(q−c₀ρ)],        I_w(q)=a mod 3^K.                  (2)

Prefix integrality follows by successive reduction modulo 3, positive oddness by the inverse formula, and the final unit residue prevents a terminal multiple of three. The complete forward itinerary of the endpoint determines the gaps in reverse order. Formula (2) is a genuine short *chosen* real window adjacent to Gq; its centre and its allowed residues are prescribed in the displayed way.

## Conditioning the finite and stationary laws

At fixed b, s, ρ as above let E be the event c₀ρ≤β_b≤ρ. The negative-binomial atom bound sup_t π_(b−1)(t)≤C/√b follows by Stirling at its mode (the adjacent mass ratio is t/[2(t−b+2)]). Since β_b≥2^(−e₁), independence of the remaining letters gives

    P(S_b=s, E) ≤ Σ_{v≥log₂(1/ρ)} 2^(−v) sup_t π_(b−1)(t) ≤ Cρ/√b.

The corresponding lower bound cρ/√b follows by summing (1), after multiplying by 2^(−s), over the 2·3^(b+K−1) disjoint unit residues. Thus the probability is positive and the conditional ternary law satisfies, for every unit r,

    P(β_b=r mod 3^(b+K) | S_b=s, c₀ρ≤β_b≤ρ) ≥ c 3^(−b−K).          (4)

The conditioning here genuinely includes a real annulus and the exact total. Its distribution still comes from sampling independent inverse gap words.

Let R and Z be the same infinite offset series at the real and ternary places, respectively. The strong law gives S_n/n→2, so R converges almost surely because 3/4<1. Ternary convergence is immediate from the factor 3^(i−1). Write m₃ for full Haar probability on the 3-adic integers. For every fixed 0<ρ≤1 and Borel A contained in the units,

    P(c₀ρ≤R≤ρ, Z∈A) ≥ cρ m₃(A).                                  (5)

Indeed for a unit cylinder A of depth j, sum the **unconditioned** word-mass version of (1) over its 3^(b−j) depth-b lifts with K=0 and over all integer |s−2b|≤√b. Their number is comparable to √b and each contributes ≥cρ3^(−b)/√b per lift. For b≥j the β_b residue already equals Z mod 3^j. The allowed range for ρ holds eventually. Since the real annulus is closed, its indicator at the limit dominates the limsup of its indicators along the sequence. Reverse Fatou proves (5) on cylinders. Finite disjoint unions and the monotone class theorem extend the inequality to all Borel subsets of the units. Taking A to be all units and using P(R≤ρ)≤2ρ shows that the conditional law of Z given this real annulus dominates an absolute multiple of unit Haar probability.

There is a complementary uniform upper bound using an additional source-qualified input. Weaver, paper 9 v2, Appendix B, Theorem 16 (B1)–(B2), gives for each 1≤p<∞ the stationary real cutoff density g_B dm₃=P(R≤B,Z∈dz) and ||g_B||_p≤C_p(1+B)^(1−1/p). Appendix C, Theorem 18, also studies central-clock stability for Lipschitz real tests at natural depth. It does not itself state the pointwise deeper finite lower bound (4). The use of a large first gap to compress a bounded real offset is already present in Appendix C after (C2). [Paper 9, Appendices B–C](https://rstation.ai/problems/collatz/papers/9)

For 0<ρ≤1 condition on the first letter v. The remaining stationary variables are independent copies R′, Z′, and (R,Z)=2^(−v)(1+3(R′,Z′)) coordinatewise. Only v≥log₂(1/ρ) contributes. The real cutoff for R′ is B_v=(2^vρ−1)/3. The ternary affine map pushes an L^p density onto one coset with norm factor 3^(1−1/p). A zero B_v contributes zero since R′>0. Minkowski and Theorem 16 therefore give

    ||g_ρ||_p ≤ C_p Σ_{v≥log₂(1/ρ)} 2^(−v)(2^vρ)^(1−1/p)
              ≤ C′_p ρ.

The annulus density is dominated by g_ρ, and its mass is at least cρ. The normalized conditional ternary densities have uniformly bounded L^p norms for **every fixed finite p**. Together with (5) this yields the two-sided comparison

    c m₃(A) ≤ P(Z∈A | c₀ρ≤R≤ρ) ≤ C_p m₃(A)^(1−1/p)              (6)

for all unit Borel sets A and p>1. The constants do not depend on ρ or A. This proves a uniform lower minorization and transfer of small Haar sets for this particular stationary law. It asserts neither bounded L∞ density nor a uniform conditional law at a fixed ordinary integer.

**Exact dyadic scale change (independent arithmetic review).** Write ν for the joint stationary law. For every integer d≥0, Borel I⊂(0,1] and ternary Borel set A,

    ν(2^(−d)I × A) = 2^(−d) ν(I × 2^d A).                          (S)

Indeed R=2^(−e₁)(1+3R′)>2^(−e₁). On R≤2^(−d), the first gap has e₁≥d+1. Subtract d from this gap and keep every later gap. Both boundary coordinates are multiplied by 2^d, and the probability of the original first gap was exactly 2^(−d) times the probability of the new one. This proves the identity by conditioning on the first gap. In particular the normalized conditional law at radius 2^(−d)ρ₀ is exactly multiplication by 2^(−d) of that at ρ₀, for 1/2<ρ₀≤1. The L^p bound just proved can equivalently be obtained by transporting only this compact band, on which paper 9 (B2) and the positive annulus mass give the uniform normalized bound.

For any finite b≥2 the same operation is a bijection on literal words. With offset residue r at any prescribed ternary depth, the number at total s+d in real set 2^(−d)I equals the number at total s in I and residue 2^d r. Thus if the clock is shifted together with the radius, a compact-band version of (1) supplies a positive count at **every** dyadic scale d, with original total 2b+d+O(√b), and only the first letter's cap is increased by d. If the original total is required to stay central, the allowable d is limited by the remaining tail's central window as in the proof of (1). This exact bijection is on symbolic gap words; for the corresponding ordinary application use the terminal residue formula at the actual total.

## A canonical law on the inverse tree of one ordinary unit

This stationary conclusion can be transported to one specified ordinary root, provided one retains the canonical *inverse* path law. Weaver, paper 19 v2, §9.2 (F1)–(F3), uses Valbuena's trace h(a)>0 and previous inverse-law inputs. For each fixed odd positive unit a, let μ_a be the law of the limiting real offset under the Markov kernel on its actual odd-unit inverse tree,

    P_h(a,x) = (3/2^e) h(x)/h(a),       U(x)=a,   e=v₂(3x+1).

Its canonical fibre theorem gives weak convergence of the finite measures

    (1/N) Σ_{j=1}^N 3^j P(R∈dt, Z≡a mod 3^j)  ⇒  h(a) μ_a(dt).

For the closed annulus I_ρ=[c₀ρ,ρ], (5) gives 3^j P(R∈I_ρ,Z≡a mod 3^j)≥cρ at **every** j. Averaging and using the closed-set direction of Portmanteau yields

    μ_a(I_ρ) ≥ cρ/h(a)      (every positive odd unit a; 0<ρ≤1).     (7)

This preserves the specified ordinary root in the inverse Markov experiment. The trace factor depends on that root. These Cesàro measures use averaging before normalization; no rate, individual-depth fibre limit, or law of the one forward path starting at a is inferred. In particular if local real mass is used to discard a class of original forward survivors, the implication from those survivors to events of this inverse law is still required. [Weaver, paper 19 v2, §9.2, equations (F1)–(F3)](https://rstation.ai/problems/collatz/papers/19/v2)

There is an almost-sure consequence on one infinite path sampled from the canonical inverse law at any fixed ordinary unit a. Let X_j be its state, let R^(j) be the limiting real offset of its remaining inverse path as measured from X_j, and fix ρ. Equation (7) and the Markov property give

    P_a(R^(j)∈I_ρ | past through j) ≥ cρ/h(X_j) ≥ (cρ/2) g(X_j),

where g(x)=ρ₁(x)/h(x), 1≤ρ₁(x)≤2, and g is bounded by paper 19 (F1)–(F5). That source's bounded-selection identity (F8) gives for any full-path event A the convergence of the Cesàro averages of E_a[1_A g(X_j)] to P_a(A). To apply it to the displayed conditional bound, approximate 1_A by its conditional expectations on the path through j. They converge in L¹, and both the annulus indicator and g are bounded. Thus, with V_N the average of 1_{R^(j)∈I_ρ} over 0≤j<N,

    liminf_N E_a[1_A V_N] ≥ (cρ/2) P_a(A).

On A={limsup_N V_N≤cρ/2−ε} reverse Fatou bounds the limsup of the same averages by (cρ/2−ε)P_a(A). Hence P_a(A)=0 for every ε>0. Almost surely the upper frequency is at least cρ/2 for each fixed ρ, with an absolute constant. Countably many dyadic scales can be imposed simultaneously, so liminf_j R^(j)=0 almost surely. The denominator h(X_j) was removed by the cited Cesàro selection identity; no independent successive annulus trials are assumed. This conclusion still concerns paths chosen in the ordinary inverse tree.

## The central descent region is empty

Let q>1 be any positive odd integer and x₀=q,x₁,...,x_b=y a literal sequence of positive odd predecessors. At every step,

    2^(e_i) x_(i−1) = 3x_i+1.

All x_i≥3, since U(1)=1 and q>1. Hence 3(3x_i+1)≤10 x_i. Multiplying the b one-step inequalities and cancelling the positive interior factors gives

    3^b 2^s q ≤ 10^b y.                                            (3)

Suppose b>0 and 4s≥7b. Then (3^b2^s)^4 ≥ (3^4·2^7)^b = 10368^b > 10000^b = (10^b)^4. Thus (3) forces y>q. In particular *every* b≥16, s≥2b−√b falls in this impossible descent region, since √b≤b/4. It makes no difference how large the real β is allowed to be, how deeply a ternary class is resolved, or how many such words exist. At a putative non-descending source n with a visited q≥n>1, a central word reaching q cannot yield a rival ordinary start ≤n. The restriction q>1 matters: (e₁,...,e_b)=(2,...,2) gives q=y=1 at every b.

More generally, exact telescoping yields

    log₂(y/q) = s−b log₂3 − Σ_i log₂(1+1/(3x_i)).

A proposal for inverse descent must use terminal words in a different slope range, or obtain a different, later common endpoint and an independent descent mechanism. This obstruction applies to the *total* used in the proposed comparison; a later word with different total, a prefix that already descends, or a forward iterate q<n is outside the claim. One-point annulus mass does not give the conditional distribution of a selected pair of ordinary sources.

There is also a plain support check for unrestricted product-measure lower bounds. For a class equal to 1 modulo 3^b, every word with that offset residue is integral at target 1 and gives G(1−β)>0, hence β<1. No uniform floor over the product of all ternary units with a fixed real interval contained in [1,∞) can hold. As another finite-scale check, 2^sβ is an odd integer, and on one β residue mod 3^(b+K) all these odd integers lie in one class mod 2·3^(b+K). This is an exact lower bound on the spacing of distinct offsets at fixed b,s and residue. The finite-coordinate support restriction uses ternary observation depth growing with the word length. The stationary limit has full topological support by paper 19 v2 §9.1 (B7)–(B13); its polynomial lower bound on product-metric balls on compact real ranges is a different statement.

Paper 19 v2 also supplies decisive prior results about the proposed stronger inference. Its main theorem (3) proves pure singularity of the stationary joint law relative to real Lebesgue times ternary Haar, using counted coalescence. Thus no bound ν(I×A)≥c |I|m₃(A) with c>0 can hold for all real subintervals I of a fixed positive-length interval and every unit ternary cylinder A. Such bounds extend by finite partitions and a monotone class to domination of product measure on that interval, contradicting singularity. The annuli in (5) have a fixed aspect ratio and accumulate at zero; this family lacks the interior subintervals needed for that argument. Full support and full product dimension do not give such domination.

For a nonperiodic root q, paper 19 §9 (B1)–(B6) obtains the stronger all-total finite bound q−β≥c q, with c>0 absolute but uncomputed. The distinct odd states of any one finite inverse path belong to one forward orbit set. The supplied sparsity estimate makes Σ log(1+1/(3x_i))≤B uniformly, and the exact product gives c=exp(−B). Hence y≤q is possible only when s−b log₂3≤B/log 2. This sharper slope conclusion needs the distinct-state and sparsity inputs. Inequality (3) above also covers periodic q>1, with the explicit central onset b=16 and no external analytic estimate. Paper 19 (F9) independently locates the support of the canonical μ_q below (1−c)q when q is nonperiodic. [Weaver, paper 19 v2, (3), §§9–9.2](https://rstation.ai/problems/collatz/papers/19/v2)

## Open inference

The joint annulus theorem controls literal ordinary inverse sources and reaches very small relative widths about its selected centres. The central descent inequality explains why it cannot turn them into smaller ancestors of a fixed n through a q≥n. PR193's prescribed ratio-five patterns occur in translates whose height is unconstrained by the pattern width. PR195's selected discordant head pairs have windows about their original endpoints. No estimate above links those specified centres to the selected centres Gq, conditions the inverse law on both arms, or bounds the surviving two-class mass. [PR193 paired result at fbe870ec44239e6b6c753bab9d1c7537acfff701](https://github.com/GettysburgResearch/collatz/blob/fbe870ec44239e6b6c753bab9d1c7537acfff701/research/astra-prescribed-closure-20261124/paired/README.md) · [PR195 source-window test at ef3496b577ed7525d5e0c82a9b782819457403d5](https://github.com/GettysburgResearch/collatz/blob/ef3496b577ed7525d5e0c82a9b782819457403d5/research/astra-global-closure-20261124/round5/head/README.md)
