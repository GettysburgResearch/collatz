# Forced divergence without any complete upward chain tail

Let `U(x)=ceil(3x/2)` and `D(x)=ceil(x/2)` on the positive integers. For a set `S`, let `T_S` choose `U` on `S` and `D` elsewhere. Call `A` force-divergent when every `S` containing `A` gives an unbounded map. Vasilyev's Question 7.7 asks whether every such `A` contains a tail of an orbit of `U`. **The trureturing project had already published a negative answer by November 20, 2026, using separated holes chosen on upward chains, with a reported Lean formalization.** The construction below independently reconstructs the same mechanism and records arbitrary-thinness and maximal-growth refinements. It is not a new solution of Question 7.7. Vasilyev's own §6.5 already uses two forced upward successors after a downward step in a periodic example. [Vasilyev, *Up or down at every integer*, v2, sections 6.5 and 7](https://borowiecki.dev/pdf/2611.20344) · [Prior trureturing construction and formalization](https://www.trureturing.org/research/vasilyev-2026-force-divergence-question-7-7/)

## The spacing lemma

Let `H` be a set of integers at least 8 satisfying
\[
           h,h'\in H,\quad h<h'\quad\Longrightarrow\quad 2h<h'.       \tag{1}
\]
Put `A=N\H`. For any `h in H`,
\[
       h/2\le D(h)\le U(D(h))<h .                                    \tag{2}
\]
The strict last inequality follows directly from the two parity cases, or from `U(D(h))≤3(h+1)/4+1/2<h` when `h≥8`. No integer of `H` lies in `[h/2,h)`, by (1). Thus neither `D(h)` nor `U(D(h))` is a hole.

For every `S` containing `A`, a down step can occur only at a hole. It is followed by two forced up steps. Every consecutive block of three steps therefore has at least two up steps. Since `U(x)≥3x/2` and `D(x)≥x/2`,
\[
                   T_S^3(x)\ge\frac98x\qquad(x\ge1).                  \tag{3}
\]
Iterating gives `T_S^(3m)(x)≥(9/8)^m x`. The one- and two-step lower bounds are respectively one half and one quarter of their input, so every orbit tends to infinity, uniformly over all choices of `S` containing `A`. In particular, no permitted map has a finite cycle. The construction below only has to place holes on all upward chain tails while preserving (1).

## A computable schedule hitting every upward chain infinitely often

For `j≥1` let `b_j=1+v_2(j)`. Every positive integer occurs infinitely often in this sequence. Put `h_0=0`. Choose `h_j` to be the first element of the actual upward orbit
\[
                       b_j,U(b_j),U^2(b_j),\ldots
\]
strictly exceeding
\[
                       \max(8,2h_{j-1},2^{j^2}).                       \tag{4}
\]
The search terminates because `U(x)>x`, and in fact `U^r(b_j)≥(3/2)^r b_j`. This is an explicit integer algorithm. The holes are strictly increasing, satisfy (1), and have `h_j>2^(j^2)`. To decide whether a supplied positive integer lies in `H`, generate holes until the first one at least as large as it and compare. Hence both `H` and `A` are computable.

Fix any positive `b` and any tail of its upward orbit. Infinitely many stages have `b_j=b`. At those stages the selected `h_j` are unbounded elements of that same upward orbit, so infinitely many lie in the prescribed tail. Thus `A` contains no upward chain tail. This proof does not require a classification of the chain roots.

The counting function obeys
\[
                    \#(H\cap[1,X])\le\sqrt{\log_2 X}\qquad(X\ge2).
                                                                         \tag{5}
\]
Consequently `A` has density one. In fact the complement can be made arbitrarily thin: for any supplied computable nondecreasing unbounded function `g:N→N`, replace `2^(j^2)` in (4) by an integer `M_j` with `g(M_j)≥j`. The search for `M_j` terminates, and then `#(H∩[1,X])≤g(X)` at every positive `X`. The spacing and chain-tail conclusions are unchanged.

## Maximal growth rate, with infinitely many downward interruptions

For the concrete schedule (4), every permitted map has the same asymptotic logarithmic growth rate as the all-up map:
\[
               \lim_{n\to\infty}\frac1n\log T_S^n(x)=\log(3/2)
                       \qquad(x\ge1,\ S\supseteq A).                 \tag{6}
\]
First, (3) excludes repeated vertices. Every downward departure therefore uses a different hole. The elementary upper bound `T_S(z)+1≤(3/2)(z+1)` shows that the first `n` vertices are at most `(3/2)^n(x+1)`. By (5) the number `d_n` of downward departures is `O_x(sqrt n)`. The product of the elementary lower multipliers gives
\[
      x\,(3/2)^n3^{-d_n}\le T_S^n(x)\le(x+1)(3/2)^n,
\]
which proves (6). For the map `T_A` itself every orbit nevertheless has infinitely many down steps: an eventual all-up orbit would be an upward chain tail wholly contained in `A`, already excluded.

These statements answer a structural question about the unrestricted up-down family. They neither change the ordinary Collatz branch rule nor settle its convergence.

## Verification scope

The written construction and its arbitrary-thinness extension are unbounded arguments. The [finite checker](check_guarded_holes.py) independently implements the scheduler, verifies spacing and the actual upward-orbit membership of each generated hole, and checks the three-step inequality for supplied finite controls. The generic finite arithmetic implication is proved in [GuardedHoles.lean](GuardedHoles.lean). The infinite schedule, frequency and limiting growth statements are written proofs, not local Lean theorems. The prior project's reported formalization was read through its release and blueprint but was not rebuilt here. No numerical search is used as evidence that the infinite schedule meets every chain.

The separate [binary-automatic construction](AUTOMATIC_FORCED_DIVERGENCE.md) has positive lower-density holes, an equal positive visit frequency on every upward chain, and an explicit actual growth rate for its own map.
