# A forward-clock test and a finite test for cycles

**The Collatz conjecture remains open.** The theorem `final_proposal` proves an equivalence for the ordinary positive-integer conjecture. Its two arithmetic conditions are open. Neither is assumed as an axiom. The cycle test has a certified finite search range at each depth. The forward test uses only the valuations along the supplied ordinary orbit. [Final Lean statement](FinalProposal.lean)

## The two conditions

Write $U(x)=(3x+1)/2^{v_2(3x+1)}$ for odd $x$. Starting at an odd unit $a$ (an odd positive integer prime to three), let $S_k(a)$ be the sum of the first $k$ valuations. It counts actual shortcut steps. The following two statements together are equivalent to convergence of every positive integer.

1. **Forward clocks.** For every odd unit $a$, there exists $k$ with
   $$
     2^{6S_k(a)}>(k+1)3^{6k}.
   $$
2. **Finite cycle tests.** For arbitrarily large $b$, the following Boolean test returns false. Search positive odd units $x<10\cdot2^b$. Follow the first $b$ odd steps and retain a path only when its shortcut clock is $2b$ and its endpoint $q$ exceeds two. The test returns true if any retained path satisfies
   $$
     (4^bq)^6>(b+1)(3^b x)^6.
   $$

A single positive Boolean test proves that a nontrivial cycle exists. Conversely, a nontrivial cycle makes the test positive at **every sufficiently large depth**, with one fixed endpoint. This statement uses no renewal or density assumption. These quantifiers concern existence of a path at a given depth. [Cycle amplification and certified executable search](CycleAmplification.lean)

## Why the forward test detects a descent or a cycle

For a path with odd inputs $x_0,\ldots,x_{b-1}$, terminal $q$ and clock $s$, the multiplicative distortion is

$$
 D=\frac{2^s q}{3^b x_0}=\prod_{i<b}\left(1+\frac1{3x_i}\right).
$$

If $q>2$, every odd input exceeds one. Write $x_i=2u_i+1$ with $u_i\ge1$. For each input the integer inequality
$$
 u_i(3x_i+1)^6\le (u_i+1)(3x_i)^6
$$
follows by expansion. If the inputs are distinct, sort the distinct positive $u_i$. The $j$-th one is at least $j$ for $1\le j\le b$. Then
$$
 D^6 \le \prod_{i<b}\frac{u_i+1}{u_i}
      \le \prod_{j=1}^b\frac{j+1}{j}=b+1.
$$
The Lean proof performs all comparisons with integers. If this bound fails, two recorded odd inputs agree. The intervening nonempty portion of the original route is a lap, and the earlier portion reaches that lap from the supplied source. [Cycle detection on the actual route](CycleDetection.lean)

Suppose $a>2$ crosses the forward-clock threshold. If the endpoint is at least $a$, the actual distortion exceeds the bound, producing a nontrivial cycle reached from $a$. Otherwise the forward orbit has reached a smaller odd unit. In the absence of nontrivial cycles, strong induction proves that every odd unit reaches one, and removal of initial powers of two and one odd step covers all positive integers. In the converse direction, after a hit at one all odd gaps have length two. The clock threshold is eventually crossed. [Kernel-checked induction](ClosureProposal.lean)

For one fixed ordinary unit $a$, Lean also proves that its odd orbit eventually repeats if and only if the clock crosses at more than $\lfloor a/2\rfloor$ distinct depths. A list of depths can be checked directly. On an orbit without repetition, each crossing would have to end at a different, smaller odd value. On an orbit that repeats, the positive distortion gained on each lap eventually beats the polynomial threshold. The set of crossings is then unbounded. This criterion includes nontrivial periodic orbits. [Pointwise theorem and executable certificate](ClockRecurrence.md)

## How we tried to close the remaining cases

- For an ordinary fixed gate, the earlier missing-word test reduces at an explicit depth to checking the deterministic odd iterate for equality with one. A converging gate can realize every prefix word in any finite collection of eligible tests. In the published 512-source example, the common gate $2^{63}-1$ reaches one after 553 shortcut steps. [Fixed-gate theorem](FixedGate.md) and [simultaneous converging examples](SynchronousShadow.md)
- Any failure of convergence has a least positive bad multiple of three. For every initial odd-run length the formal proof exhibits infinitely many candidate multiples that merge into smaller ones, with an all-exit exclusion after sufficiently many neutral pairs. The ordinary multiple $1{,}153{,}278{,}255$ and the smaller multiple $554{,}824{,}413$ provide one explicit merger. The other residue classes still require descent. [Least-multiple proof](MinimumDescent.md)
- Ternary lifting proves that positive roots congruent to one modulo $3^b$ admit no smaller positive same-depth inverse ancestor through depth $b$. A separate counting argument estimates the fraction of obstructed roots. The obstruction also occurs on verified converging orbits. [Downward lifting and counting](DescentClocks.md)
- For every finite horizon $H$ and every lower size bound, there is a **single converging positive integer** with no forward clock crossing during its first $H$ odd steps and no smaller inverse ancestor within $H$ odd steps, at any shortcut clock. Its next odd gap reaches one. This rules out a uniform finite-horizon proof that one of those two mechanisms must succeed. [Mixed forward and inverse example](MixedBarrier.md)
- For a hypothetical nontrivial cycle, the smallest and largest odd values cannot both lie in $[N,2.08N]$ when $N$ is the cycle minimum. Lean proves the finite word count, the ordinary cycle reduction, and the numerical contradiction from two inequalities. Their application to all positive cycles uses the cited published linear-form and period bounds and the published finite convergence verification. A wider cycle survives this restriction. [Cycle width proof and primary sources](OrbitAttack.md)

The main obstruction on an escaping trajectory is pointwise. Its distinct odd states have a tail minimum. A clock crossing at that minimum would force a smaller value or an actual repeat. Finite experiments, estimates for typical initial values, and lower bounds on the number of inverse paths do not supply that crossing for the particular integer. The weighted, central-row problem in PR #207 has a stronger population requirement and an external renewal input. Our cycle test decides only whether any qualifying path exists at the given depth. [PR #207 at b56c4dc](https://github.com/GettysburgResearch/collatz/blob/b56c4dc2c28a184cf55638bb80c49a9d4662fc81/research/diffusive-central-row-closure-20261124/README.md)

At one common physical observation time, the escape calculation gives an unconditional lower count of distinct ordinary sources that have visited a small gate and are subsequently above $\sqrt b$. A stronger normalized positive-density conclusion uses the external fixed-total renewal estimate stated in PR #207. Both versions leave the opposing upper bound open. [Common-clock proof and dependencies](OrbitTrace.md)

Two PRs updated during the pass address different surviving cases. PR #193 gives a written occupation bound above twice the minimum of a sufficiently long cycle. PR #200 improves a bounded-excursion estimate and checks inverse obstructions through depth 192. Their stated conclusions allow a wider cycle and leave the later excursion of a single escaping source unresolved. [PR #193 at 24cdd0e](https://github.com/GettysburgResearch/collatz/blob/24cdd0e5471d4421716cfce6bd88916f858f994c/research/astra-universal-proof-20261124/critical/CYCLE_OCCUPATION.md) and [PR #200 at 81ea4c1](https://github.com/GettysburgResearch/collatz/blob/81ea4c1754d73c98d1451447527e6b2ba56977cc/research/regularity-rigidity-20261124/minimum-closure/README.md)
