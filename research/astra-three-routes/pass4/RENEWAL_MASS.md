# Route 1: sum the long corridors exactly, then eliminate certified safe states

**Status: PROPOSED pending independent review.** The complete fixed-floor
survivor estimate remains OPEN. The theorems here bound arbitrarily long
residence in specified corridors and in an explicitly rank-contracting region.
They do not confuse those killed populations with all nonconvergent sources.
Every sum is over ordinary positive integers. No predecessor theorem is used.

This pass changes the role of the old periodic-shadow obstruction: maximal
residence in each such shadow can be summed analytically instead of bounded by
an arbitrary fixed lookahead. The unresolved mass is transferred to the
changing-mode or unsafe return process, not discarded.

Use the definitions of MOVING_GHOST_RANK.md. For a>=2 the quantity z_a(n) is
positive. Let k_a(n)=floor(v2(z_a(n))/(a+1)), allowing zero. A positive count
means that n has exactly the corresponding active mode. Put P=2^(a+1), Q=3^a.

## 1. T-A3-801: a complete-source, all-residence Mellin sum

For any integer K>=1 and s>1, the sources with k_a(n)>=K satisfy
z_a(n)=P^K*l with l>=1. They are a subset of these positive multiples, with
the ordinary integrality and positivity restrictions retained. Therefore

    sum_(n>=1, k_a(n)>=K) z_a(n)^(-s)
       <= zeta(s) P^(-sK).                             (1)

No ordinary source cutoff appears. The notation zeta(s) is just the convergent
positive series sum_(l>=1) l^(-s); its value need not be imported externally.
By Tonelli, for lambda>=0 and theta>=0 with
lambda*(Q/P)^theta<P^s,

    sum_n z_a(n)^(-s)
      * sum_(i=0)^(k_a(n)-1) lambda^i
            [z_a(g_a^i(n))/z_a(n)]^theta
    <= zeta(s) / [P^s-lambda*(Q/P)^theta].              (2)

This is an integrated bound for the entire unbounded INITIAL corridor,
including real height amplification when theta>0. It is not an estimate for
arbitrarily many later reentries with a transported distribution.

### An exact identity, not just an upper bound

For a=2, z_2(n)=n+5, P=8, Q=9. Every source with k_2(n)>=K is exactly

    n=8^K*l-5, l>=1.

Hence equality holds in (1), and at s=2, theta=0,

    sum_(n>=1) (n+5)^(-2) sum_(i<k_2(n)) lambda^i
       = zeta(2)/(64-lambda), 0<=lambda<64.             (3)

At lambda>=64 the expression diverges: the positive layers themselves are
zeta(2)*lambda^i/64^(i+1). Thus the threshold is sharp for this corridor.
The source n changes with K; no infinite ordinary periodic orbit is asserted.

For all a>=2 together at s=2, lambda=1, theta=0, the entire infinite dictionary
has the bound

    sum_(a>=2) sum_n k_a(n)/z_a(n)^2
       <= zeta(2) sum_(a>=2) 1/(4^(a+1)-1)
       <= 4*zeta(2)/189 < 8/189.                       (4)

The comparison uses 1/(1-4^(-a-1))<=64/63 and
sum_(a>=2)4^(-a-1)=1/48. Also zeta(2)<2 by integral comparison.
This is an actual infinite-dictionary bound, not the mass of a finite sample.
It does not say that the adapted seed 1/z_(a(n))(n)^2 is invariant after exit.

### Exact finite numerical enclosures

At cutoff J, the partial sum sum_(l=1)^J l^(-2), plus 1/(J+1) and 1/J,
brackets the remaining complete sum. The checker uses J=4096 and outward
rounding to multiples of 10^(-12). For lambda=1, (3) gives

    0.026110064080 <= complete occupation <= 0.026110065027.

The other certified lambda values are 2,16,32. All times K are included by
the proof of (3); the finite calculation only encloses its constant. The
576 ordinary progression checks validate the coding separately.

## 2. T-A3-802: a safe-state resolvent with an explicit whole-source tail

Define the computed safe region

    G={n>1:4R_*(A(n))<=R_*(n)}.

An aligned state from the rank theorem belongs to G, but G may be larger.
Each step that remains in G and avoids 1 quarters the SAME positive integer
rank. A source n can therefore remain for fewer than

    b(n)=floor(log_4 R_*(n))+1

such steps without reaching 1 or leaving G. Properness and R_*(n)<=n^2 make
this an explicit O(log n) module bound, not a premise about total stopping.
The shortcut time spent before that exit is at most

    3*b(n)*ceil(log_2(R_*(n)+6)).                        (5)

Indeed every intermediate source has n_i<=R_*(n_i)+1<=R_*(n)+1, and the
module clock in the rank note is at most 3 log_2(n_i+5). Formula (5) is
O((log n)^2), although it may terminate at an UNSAFE source rather than at 1.

Now let K_G push nonnegative source mass along A and kill it on first arrival
at 1 or outside G. If 0<=f(n)<=C n^(-s), s>1, every source remaining after r
steps has

    R_*(n)>=4^r, hence n>=2^r.

Therefore, for every r>=1,

    ||K_G^r f||_1
      <= C sum_(n>=2^r) n^(-s)
      <= C * 2^(s-1)/(s-1) * 2^(-r(s-1)).              (6)

The proof includes all positive sources, with no assumption about what they
do after exiting G. For any L>=1 the entire omitted resolvent tail obeys

    sum_(r>=L) ||K_G^r f||_1
    <= [C*2^(s-1)/((s-1)(1-2^(-(s-1))))]
       *2^(-L(s-1)).                                   (7)

For s=2 the right side is C*2^(2-L). Thus arbitrarily many safe modules can
be eliminated with an integrated, certified truncation remainder. Applying
an ordinary deterministic exit pushforward cannot increase this mass norm.

The source-envelope hypothesis on f is mandatory. It is not automatically
preserved by an unsafe return, and (7) must not be iterated on a new unknown
input density without proving a new bound. The unsafe-return operator is the
remaining obstruction, much as PR #91 retained its resonance-return operator.
Here the safe region uses a new moving-index common rank rather than that
packet's fixed section rank; no cross-branch theorem is imported.

## 3. Exact pilot and where the attempted full proof stops

Among 2<=n<=16384, 5231 inputs are aligned and 10505 satisfy the larger
quarter-drop guard. Iterating only that guard sends 128 starting inputs to
1 and 16255 to an explicitly unsafe input. The largest shortcut duration in
this finite pilot is 26. Theorems (5)-(7), not these counts, give the universal
exit and tail bounds. They are not a convergence proof for the unsafe values.

The old fixed-floor signed boundary condition has not been established.
Equations (1)-(7) supply a new exact way of paying for long local growth and
removing a provably transient safe region. To complete the original route one
still needs a quantitative estimate on the actual mass returning between
unsafe states, with no unjustified fresh-density or independent-parity step.

A possible complete endpoint is a summable positive supersolution for the
induced unsafe inverse operator, with its safe excursions controlled by (7).
Another is the full lower-rank merging cover in RESONANT_SOURCE_FAN.md.
Neither is claimed here. In particular (4) is finite initial-corridor occupation,
not a bound on all successive corridors of the Collatz process.
