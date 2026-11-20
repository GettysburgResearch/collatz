# Ordinary basin closure: certificate transfer and adaptive descent

**PROPOSED. Collatz remains unresolved.** This pass attacks an actual global
closure implication. Its main additional result is an exact two-macro ordinary
return subsystem: every finite schedule is realizable, each fixed periodic
schedule has a finite arithmetic budget, and the two individual budgets can
replenish each other under switching. It also supplies a checked partial
certificate compiler and an equivalent finite-endpoint formulation of a separate
analytic target. None supplies the remaining universal closure.

Use the positive shortcut map

$$
T(n)=\begin{cases}n/2&2\mid n,\$3n+1)/2&2\nmid n,\end{cases}
$$

and its odd acceleration
$$
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
$$
Write $x\sim y$ for an actual ordinary forward merger at finite,
possibly different clocks, and $\mathcal C$ for the basin of 1.

## The global target

At the frozen PR146 head, the following implication is equivalent to full
Collatz:

$$
\boxed{16k+1\in\mathcal C\ \Longrightarrow\ 32k+1\in\mathcal C
\quad\text{for every }k\ge0.}
$$

That equivalence is a source result, not a proof of the implication. Its exact
source and the related pair-process and analytic interfaces are pinned in
[SOURCES.md](SOURCES.md).

The first attempt uses the **whole finite ordinary convergence certificate** of
the left source, including every division exponent. A second independent attempt
tries to turn repeated ordinary pair sections into a well-founded descent. A
third attempts an arithmetic upper bound on the particular-vector moment used
by PR144/PR156. The precise successful statements and the missing inferences
are kept together below.

## 1. A positive certificate transformer

[CERTIFICATE_CARRY.md](CERTIFICATE_CARRY.md) proves exact rules for companions
$R_j(x)=2^j x-1$. In states $R_1,R_2$, any source-certificate prefix over
division exponents $\{2,3\}$ can be consumed without enlarging the state set.
Further two-letter rules either consume more source letters or merge directly
into an already certified suffix. Every accepted certificate supplies actual
merger clocks. The number of unused source letters is a genuine termination
rank **for this partial grammar**.

The distinction between termination and acceptance is essential. The compiler
reports an unhandled carry rather than assuming that every residual companion
of the terminal source 1 converges. An exact exhaustive boundary already occurs
at known odd hitting depth two:

$$
x_r=\frac{2^{6r+4}-7}{9},\qquad
U^2(x_r)=1,\qquad
U^2(2x_r-1)=2^{6r+1}-1\quad(r\ge1).
$$

These are all nontrivial $x\equiv1\pmod{16}$ of that hitting depth. Thus even
this depth-two restriction of the target requires convergence of every indicated
Mersenne number. The companion has a proved growing excursion and cannot inherit
a nonincreasing odd-step count or total division budget from its short source
certificate. No claim that the Mersenne restriction alone is equivalent to full
Collatz is made.

## 2. Ordinary returns need not descend

For a hypothetical least nonconverger $m=2a-1$, $a$ is even, the arm
$a$ converges, and the arm $3a-1$ would not. The physical floor $m$
and the designation of those arms must be retained when the canonical pair
coordinates reset.

[EXPANDING_RETURNS.md](EXPANDING_RETURNS.md) gives a complete infinite positive
integer cylinder with a first canonical return after 38 shortcut clocks:

$$
a=210578993150+549755813888u,\qquad
b=216364159964+564859072962u,\qquad u\ge0.
$$

The returned pair is $(b,3b-1)$, with $b>a$. All physical odd-part floor
guards, all cross-arm meetings through those clocks, and all intervening
numerical sections are checked by exact affine arithmetic. This refutes the
universal claim that every surviving first return must provide a descent.
It is not a nonconvergent Collatz example.

There is a useful positive distinction: any **one repeated expanding return
word** consumes a finite 2-adic valuation of an explicit positive affine form,
so it cannot repeat forever from one fixed positive source. A proof allowing
different return words must control the resource across switches. That control
has not been established; neither finite repetition nor a changing-source
family substitutes for it.

Two certified macros, F and G, make the switching issue exact. Along an ordinary
finite realization of `F,G,F,G`, the pair of individual valuation resources
returns to its original value after two increasing returns:
$$
(47,9)\longmapsto(9,47)\longmapsto(47,9).
$$
No function of this pair alone can strictly decrease at every such return.
Additional arithmetic information is required.

A further direct attack in [TWO_MACRO_NORMALIZATION.md](TWO_MACRO_NORMALIZATION.md)
reduces this particular two-macro subsystem to the integer ceiling map
`b ↦ ceil(3^24 b / 2^38)`, restricted to two consecutive remainders. No
all-source exclusion of that restriction was obtained. In the intended
least-counterexample setup the known arm already has a finite hitting clock;
the broader missing step is successful merger or descent when useful
sections cease.

## 3. The analytic tail is controlled; the arithmetic head is not

[PRIMITIVE_TRACE.md](PRIMITIVE_TRACE.md) starts from PR156's exact all-word
trace for

$$
D_q=\sum_{n\ge1\text{ odd}}\frac{J_q(n)^4}{U^q(n)^2},\qquad
J_q(n)=\frac{3^q}{2^{\sum_{j<q}v_2(3U^j(n)+1)}}.
$$

It proves an exact reduction to finitely many actual positive odd endpoints:

$$
P_q=\sum_{\substack{1\le t<2\cdot3^q\\t\text{ odd}}}
       \frac{H_q(t)}{t^2},\qquad
H_q(t)=\sum_{U^q(n)=t}J_q(n)^4,
$$

$$
\frac{\zeta(2)-1}{4}\left(\frac35\right)^q
\le D_q-P_q\le
\frac{\zeta(2)}4\left(\frac35\right)^q.
$$

Consequently $D_q=O((q+1)^2)$ is equivalent to the same bound on $P_q$.
The latter remains unproved. The endpoint recurrence sums all inverse gaps
exactly, with no finite gap cutoff and no independent-uniform ternary lift.
The note also shows that two explicit independence replacements grow
exponentially; generic mixing does not even predict the required bound.

The moment route concerns exclusion of nonperiodic trajectories. It would
still require a separate exclusion of nontrivial positive cycles. The basin
closure target at the top of this page would settle both failure types.

## The next proof obligation

For the chosen basin target, extend the actual certificate transformation to
its unbounded carries and prove that it always reaches a certified suffix.
This must resolve the displayed terminal Mersenne family and the retained
$(1,2)$ denominator carry. A returning pair may grow, so numerical size
cannot be substituted for a missing rank. A fixed expanding macro cannot
repeat indefinitely, but this does not settle switched macros or permanent
section avoidance.

For the independent analytic route, prove the ordinary weighted head estimate
in PRIMITIVE_TRACE, equation (10). The exponentially small tail has already
been removed. None of the results here licenses a statement that full Collatz
or either remaining target is proved.

## Reproduction

The companion scripts use exact integers and rational numbers and have no
third-party runtime dependency. Run `python -B run_checks.py` from this
directory. The written proofs establish the unbounded statements; finite
replays check implementations and reject corrupted certificates. Repository
validation is reported separately and is not a proof of the mathematics.

Publication receipts and the independent review are kept in
`reports/2026-11-20-ordinary-basin-closure/` rather than in the scientific
statements.

## Concurrent source update

Before publication, PR146 advanced to
`0410811710af2f7da71522ec67233528048adb9a`. Its new `BASIN_PHASE.md`
includes the same depth-two Mersenne family reconstructed
here, and `RANK_THREE_MERSENNE.md` gives a stronger three-step encoding of all
large Mersenne exponents. Its `BOUNDED_RANK_TRANSFER.md` supplies a general
bounded-time test for lifted merger when the antecedent's odd depth is known.
On the one-sided target this is stronger than our two-state partial grammar.
Accordingly, neither that family's discovery nor superiority of the partial
compiler over the current source is claimed. The compiler remains an explicit
independently checked implementation of its stated rules. The later source
still leaves the nonlifted ordinary closure open.

Concurrent PR157 at `64361ecca770092d6c8242dc6211e38818af2e50` develops a
forward-five basin criterion and an actual occupation-bound target, also
without a closing upper bound. Its direct closing-attempt note was read for
comparison. Those alternative premises are not inserted into any proof here.
See [SOURCES.md](SOURCES.md) for the exact publication boundary.
