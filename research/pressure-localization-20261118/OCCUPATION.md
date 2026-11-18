# How much source weight can have a small multiplier?

**PROPOSED.** Use the positive odd ordinary map and symbols of
[the logarithmic pressure note](LOGARITHMIC.md). Here the event is an
integer comparison 3^j≤L 2^A_j, independent of any floating-point log.

## 1. An all-time bound before physical repetition

A source x contributes at j until the first repetition among t_0,…,t_j,
including its last distinct state. Write an asterisk on a sum restricted
this way. Suppose every simple odd path has at most K Y^β states at most Y
for Y≥1, where 0<β<1. The PR 144 input is K=16 and β=19/20.

For every real L>0 the following bound holds across *all clocks and sources*:

    ∑*_j,x a_j(x) 1_{J_j(x)≤L} ≤ C L^β,
    C = K/(1−β/2) ∑_(x odd) x^(β−2) < ∞.                    (1)

For fixed x and clock satisfying the indicator, the weight is bounded by
min(x⁻²,L²/t_j²). Represent this minimum as the integral from 0 to x⁻²
of 1_{t_j≤L/√u}; boundary values do not affect the integral. Before
repetition the path is simple, so its count under the integral is at most
K(L/√u)^β, including zero if the threshold is less than 1. Integrating
gives K L^β x^(β−2)/(1−β/2); sum in x by nonnegativity. Infinite simple
paths follow by increasing finite prefixes. In particular C≤640 with the
displayed parameters, since the sum over all positive integers is at most
1+1/(1−β)=21. The estimate retains arbitrarily late returns into the
coefficient range; it does not impose a stopping horizon.

Let E*_j=∑*_x a_j(x). For integer Q≥1 and h>0, define

    G_Q(h) = (1/Q) ∑*_(j<Q,x) a_j(x) 1_{J_j(x)>h}.

Then (1) gives a deterministic one-sided error:

    0 ≤ (1/Q) ∑_(j<Q) E*_j − G_Q(h) ≤ C h^β/Q.               (2)

As j increases E*_j decreases to the mass of nonperiodic sources, each
with its own limiting weight. The W3 reciprocal-height estimate makes that
weight positive for every nonperiodic source. Thus for any γ<1/β and
h=Q^γ, G_Q(h) converges to exactly this escaping mass. An upper subsequence
tending to zero would prove all orbits eventually periodic. This upper
estimate remains open.

For example choose h=Q, so that all membership tests are integer
comparisons and the error in (2) is at most 640 Q^(−1/20). Given odd X≥1,
retaining only x≤X incurs additional clock-average error below
1/[2(X+1)]. The latter error is independent of Q and h. Formula (2)
gives an occupation test with bounded summands in place of the potentially
large moment contribution d_j(x).

There is also a useful summable formulation. For s>β, dyadically grouping
J≤1 and 2^k<J≤2^(k+1) for k≥0 in (1) gives

    ∑*_j,x a_j(x) min(1,J_j(x)^(−s))
       ≤ C [1+2^β/(1−2^(β−s))].

This controls inverse powers at large multiplier, with saturation near zero.

## 2. Bounds retaining all cycle laps, without a packing assumption

Set b_j=√a_j=J_j/t_j. The exact ordinary +1 term gives

    b_j−b_(j+1) = b_j²/(3J_j+b_j).

Consequently, for each x and L>0,

    ∑_(j<Q, J_j≤L) a_j(x) ≤ min(Q/x², (3L+1)/x).            (3)

The second bound telescopes all the way to b_0=1/x, even when the orbit
repeats. Put M=3L+1 and N=⌈Q/M⌉. Sum the second bound through N using
the ordinary harmonic estimate, and the first bound beyond N using the
reciprocal-square tail. This gives

    ∑_(j<Q,x) a_j(x) 1_{J_j≤L} ≤ M[2+ln(1+Q/M)].             (4)

In particular the low-multiplier contribution divided by Q vanishes
whenever L=o(Q).

A linear-sized cutoff is also possible on late time windows. For fixed
c>0 and odd X, the exact telescope on the clocks Q,…,2Q−1 yields

    (1/Q)∑_(Q≤j<2Q,x) a_j(x) 1_{J_j≤cQ}
      ≤ (3c+1/Q)∑_(x≤X,odd)[b_Q(x)−b_(2Q)(x)] + 1/[2(X+1)].

For each fixed x the decreasing b_j converges, hence the finite sum tends
to zero. Letting X grow afterward proves that the left side tends to zero.
The complementary mass on this window tends to lim E_j. This argument
needs neither simple-path packing nor an a priori convergence statement.
Without the first-hit discount it identifies the limiting energy but does
not identify which orbit classes have positive limiting weight.
