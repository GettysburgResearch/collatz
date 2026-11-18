# Multiplicative rank on ordinary odd trajectories

**PROPOSED.** This packet gives two different return bounds for values lying in a low-rank multiplicative coset. Both concern actual positive odd iterates, and allow the group and coset to be selected after observing a finite segment. Neither prevents an orbit from continually acquiring multiplicatively independent values.

Use the shortcut map T and odd map U(x)=(3x+1)/2^v₂(3x+1). Write x_i=U^i(x_0), and count only distinct states when specified. A multiplicative coset is uG with u>0 rational and G a subgroup of the positive rationals of finite rank r. A set of integers supported on s specified primes lies in a group of rank s. Rank bounds also apply to sets built from arbitrary composite generators.

**External input.** We use the uniform bound A(k,t)=exp((6k)^(3k)(t+1)) for nondegenerate solutions to a linear equation with k terms in a multiplicative group of rank t. For two terms use the bound 2^(9(t+1)) recorded in the same source. Coefficients may be any specified nonzero rationals. See Evertse, Schlickewei and Schmidt, *Annals of Mathematics* 155 (2002), Theorem 1.1 and equation (1.5). The bounds below are applications of these external theorems. [Paper](https://arxiv.org/abs/math/0409604)

## 1. Globally finite close pairs in the odd clock

Fix k≥1, u and G. At most A(k+1,2r+k) distinct positive odd sources in uG return to uG after exactly k odd steps. The intervening valuations are unbounded in this assertion.

Indeed, put a_i=v₂(3x_i+1) and s_i=a_0+...+a_(i−1), with s_0=0. Telescoping gives

    2^(s_k) x_k = 3^k x_0 + Σ_{i=0}^{k−1} 3^(k−1−i) 2^(s_i).

Divide by 3^(k−1) and isolate the constant term i=0. With x_0=u g and x_k=u h, the equation becomes

    (u/3^(k−1)) 2^(s_k) h − 3u g − Σ_{i=1}^{k−1} 2^(s_i)/3^i = 1.

The variable vector consists of 2^(s_k)h, g, and 2^(s_i) for 1≤i<k. The endpoint group coordinates cost at most 2r generators in rank, and the k binary exponents cost at most k more. The single positive term exceeds the sum of the absolute values of *all* negative terms. Thus no nonempty subsum vanishes. Distinct sources give distinct g. This proves the bound, including k=1 with the empty internal sum.

In particular the gaps in odd time between successive visits to any fixed coset tend to infinity on an infinite distinct orbit, if there are infinitely many visits. For N distinct consecutive odd states, if M of them lie in uG, partition the M−1 gaps into lengths at most K and lengths greater than K. Uniformly in the segment, coset, and choice of generators,

    M ≤ 1 + N/(K+1) + Σ_{k=1}^K A(k+1,2r+k).

For every fixed positive occupation fraction, take K larger than twice its reciprocal. This inequality forces r ≥ c log N − O(1), with constants depending only on the fraction. In particular a coset of rank o(log N) occupies a vanishing fraction uniformly, even when the starting value is arbitrarily large.

## 2. A shorter bound using the elapsed shortcut clock

Suppose a distinct odd segment has M selected values in uG. Put m=M−1≥1 and let L be the total number of shortcut steps between its first and last selected values. Then

    L ≥ log₂(m!) − m(18r+10).

Each consecutive selected pair admits a binary parity word w of positive length t, beginning with an odd step. Composition gives y=(3^q x+c_w)/2^t with c_w>0. For x=u g and y=u h the two-term equation

    (2^t u/c_w)h − (3^q u/c_w)g = 1

has at most B=2^(9(2r+1)) solutions because (h,g) belongs to G². Therefore at most B pairs use any one word. Fewer than 2^(t+1) binary words have positive length at most t. In increasing order of elapsed lengths, the jth length is at least log₂ j − log₂ B − 1. Summation gives the displayed bound. A source repeated around a cycle may be counted only once per period.

For a segment of N distinct odd states starting at x_0, the whole elapsed clock is at most 2(N−1)+log₂ x_0, by multiplying 2^a x'=3x+1≤4x. After an entire odd period of a cycle the log x_0 term cancels. On a fixed infinite distinct odd orbit the sharper initial-prefix estimate is

    L ≤ (N−1) log₂ 3 + log₂ x_0 + O(log N),

since Σ_{i<N} log₂(1+1/(3x_i))=O(log N) by distinctness. It follows that for any fixed-rank coset the count among the first N odd states of such an orbit satisfies

    limsup M log₂(N)/N ≤ log₂ 3.

Indeed on any subsequence where the left side stays positive, log₂ m / log₂ N tends to one, and log₂(m!)≥m log₂ m−O(m). This also works if r=o(log N) and the coset varies with N. The bound is for prefixes from a fixed x_0. The first theorem supplies the weaker density conclusion on arbitrary translated time windows without an initial height term.

Neither estimate applies to arbitrary even-only strings: 2^j,2^(j−1),...,1 all lie in a rank-one group. The strict positive affine remainder for an odd input is essential. A bounded-rank model for a positive proportion of a divergent odd orbit is excluded. The actual prime support of arbitrary Collatz iterates is unconstrained by such a model.

Baseline `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The repository also uses a different S-unit theorem in the [corrected-stage exclusion](../RESULTS_CATALOG.md#corrected-256-stage-ordinary-completion-exclusion). No stage hypothesis is used here.

### Prior comparison

Earlier work gives quantitative sublinear bounds for visits to unions of finitely many **untranslated** cosets, with the group and representatives allowed to depend on the observed prefix. A further paper gives effective multiplicative-rank restrictions for actual cycles and trajectory heights. The finite S-unit close-pair formulation here supplies a different proof interface. The extension to a union of **additively translated** cosets, with possible affine resonance at the distinct centers, is addressed separately. [Prior moving-coset estimate, rStation 138](https://rstation.ai/problems/collatz/papers/138/v1) · [Prior rank and height estimates, rStation 137](https://rstation.ai/problems/collatz/papers/137/v1) · [Affine returns in this branch](AFFINE_RETURNS.md)
