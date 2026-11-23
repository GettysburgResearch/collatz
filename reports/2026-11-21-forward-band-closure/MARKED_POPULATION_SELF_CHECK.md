# Independent self-check of the marked predecessor population argument

This checks the sensitive inferences in `MARKED_PREDECESSOR_POPULATIONS.md`.
It is a second pass over the mathematics, not an independent formal proof.
The analytic input and the population conclusion remain written mathematics;
the ordinary finite criterion is being formalized separately with its
population premise explicit.

| Sensitive inference | Exact identity or estimate used | Failure excluded |
|---|---|---|
| Smooth selected densities have one positive cylinder | The PR180 telescoping estimate is summable and `mean(g_N)=P_N>=P_infinity>0`; hence one cylinder has `g_N>=kappa` for every later `N`. | An almost-everywhere lower bound would not suffice at the supplied integer target. The premise is pointwise on every lift of one finite cylinder. |
| Interpolation covers every sufficiently large depth | For `d_(N+1)<=h<d_(N+2)`, `k=h-d_N` satisfies `b_N<=k<b_N+b_(N+1)`. | A triangular subsequence of depths cannot be assumed to intersect the rotation-selected depths. This step removes that mismatch. |
| Interpolation loses vanishing pointwise mass | `||(sum T_w)(D_k-lift D_bN)||_infty <= (d_N+1)(B_*+3^k rho^dN) C_4 b_N^(-4) = O(N^(-2))`. | The norm conversion includes both the number of possible totals and the ternary resolution. Neither factor is dropped. |
| Terminal-total truncation is permissible | Its normalized `L1` loss is at most `2 exp(-k/1200)`; the same prefix operator turns this into `O(N^2 exp(-cN))`. | No conditional mixing given the total is assumed. The large factor `3^k` is inside a controlled operator norm, not multiplied onto the raw rejection probability by itself. |
| Real offsets stay bounded after interpolation | `beta_(w*v)=beta_w+omega_w beta_v <= B_*+rho^dN 2^k <= B_*+1`. | A ternary residue bound alone gives no bound on the real offset. Here `k=O(N)` and `d_N` is quadratic. |
| Spreading retains simultaneous controls | Prepend one exponent `e<=E`: density multiplier `3*2^(-e)`; offset `2^(-e)+3*2^(-e) beta`; total increases by at most `E`. | The unrestricted atom floor is not substituted for the controlled subdensity. The extra exponent has a fixed uniform ceiling. |
| Parent chosen for the original target is legal | Choose `2^e a=4 (mod 9)`, so `a_s=(2^e a-1)/3` is positive, odd, and a ternary unit. | The atom floor is only for unit residues, and inverse odd steps at multiples of three cannot be freely appended. |
| The parent is only linear in depth | Consecutive eligible parents satisfy `a_(e+6)=64a_e+21`; the least one above `Cs` is at most `65Cs` for large `s`. | A huge fixed target or an uncontrolled parent height would spoil the squared-logarithm population bound. The onset may depend on the target. |
| Rotation has a buffer of the correct sign | A rational grid puts `frac(log2 a-(s+1)alpha)` in `[2/q,5/q]` with `q<=s<2q`. | Bare closeness to an integer allows approaches from below; positive buffered phase prevents crossing into the previous octave. |
| The full real correction has one sign and is small | `delta_w=-log2(1-(1+3 beta_w)/(2^e a))`, with `0<delta_w<=1/(6s)<=1/(6q)`. | The parent error and the word-offset error are combined before estimating. Their signs are not discarded. |
| All fixed-total words share one octave | `log2 n=A+e+log2 a-(s+1)alpha-delta_w`; `A,e` are fixed and the residual phase stays strictly between 0 and 1. | Same leading approximation does not by itself imply a common octave when errors can cross its boundary. |
| The exact section constant is sufficient | `s/5<=d+1<=s`, `s<=2q`, and `2^v-1<=v` yield `(d+1)(n-2^d)<=10*2^d`. | The comparison uses the source's own binary exponent, not the depth or the target exponent in its place. |
| Congruence gives a positive ordinary inverse path | Every first numerator `2^a b-1` is positive, odd, and divisible by 3; divide the remaining affine congruence and induct. | A rational affine solution or a residue solution is not silently treated as a positive integer orbit. |
| Different words give different source integers | At fixed length the actual odd forward itinerary uniquely recovers all exact removed powers of two; fixed-total injectivity also follows from the existing numerator lemma. | Word counts are not mistaken for source counts. No assumption that the target is nonperiodic is needed at one fixed depth. |
| The chosen total carries actual population | At most `2s` totals carry mass at least `c`; one has mass at least `c/(2s)`, and each word there has the same weight `3^s 2^(-A)`. | The selected total is found by pigeonholing, not by a claimed fixed-total mixing theorem. |
| Squared-logarithm loss is fully accounted for | `|P| >= c 2^A/(2s3^s)`, while `H=a_s2^A/3^s` and `a_s<=65Cs`; hence `|P|>=cH/(130Cs^2)`. | One factor of `s` comes from the total pigeonhole, and the other from the parent. Neither is suppressed. |
| The sources have a common ordinary clock | The inverse word takes `A` shortcut steps to `a_s`; the parent takes `e_s` more to `a`. | Equal accelerated depth alone would not give equal ordinary clocks. Fixing the total is essential. |
| The common clock is quantitatively bounded | `e_s<=log2(195Cs+1)` and `A<=2.1s+E` imply `A+e_s<=3s<=15(d+1)` eventually. | Common time is not confused with a bounded time; the additional bound follows from the actual chosen parent and source heights. |
| Witness scales are unbounded | The rational denominators `q` are unbounded, `s>=q`, and `d+1>=s/5`. | An infinite choice procedure could otherwise revisit a bounded set of bands. |
| The criterion uses the right quantifiers | A failed unit target supplies arbitrarily high witness bands where `V_d(t)>=gamma 2^d/(d+1)^2` **for every** `t`. | An arbitrary unbounded subsequence of passing bands may avoid this target-dependent witness subsequence. The criterion asks every sufficiently large band to pass. |
| The nonunit-target issue is handled only where valid | The population theorem assumes `3` does not divide the supplied target. Every ordinary component contains such a target. | The theorem is not falsely stated for direct predecessors of a multiple of three. |
| The global conclusion remains conditional on an upper estimate | The new result is a lower bound on marked predecessors. The displayed survivor bound is a separate, unproved assertion. | Density zero, bounded first-hit time, or the new lower bound is not relabeled as a proof of convergence. |

## Exact finite exercise

`verify_marked_cloud.py` constructs three deliberately selected legal clouds
with supplied targets 1, 5, and 7. It uses the approximant `485/306` and
certifies its error with the exact integer inequalities

\[
 2^{485\cdot306-1}\le3^{306^2}\le2^{485\cdot306+1}.
\]

Decimal logarithms only locate a candidate depth. The reported phase interval
is subsequently certified by raising the positive integer ratio
`a/3^(s+1)` to the denominator power and comparing it with integer powers of
two. Every inverse step, bounded offset, fixed total, positive odd source,
source distinctness, source-specific section inequality, common ordinary
clock, and normalized mass/count/height identity is checked exactly.

The sample additionally keeps all sources ternary units; the analytic theorem
does not require that extra restriction. The output is in
`MARKED_CLOUD_EXAMPLES.json`. These examples exercise the finite arithmetic
interface and do not validate the uniform analytic floor or its asymptotic
population lower bound.

## Remaining verification boundary

The new all-depth controlled subdensity and its passage into the section have
not been implemented in Lean. Their declared analytic dependency is the
PR180 selected-density construction and Tao's stated fine-scale mixing
estimate. The separate Lean finite criterion must keep its population input
as an explicit proposition argument; it must not introduce that input as an
axiom or claim it was kernel checked.
