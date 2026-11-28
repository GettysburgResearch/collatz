# Broad track, checkpoint 5

## Finite power trees on simple integer paths

`FINITE_POWER_GRAMMAR.md` proves that minimum repetition-tree size divided by $\log(1+T/B)$ tends to infinity uniformly on simple positive shortcut input segments, where $B=\log_2(x_0+1)$ and $T/B\to\infty$. The syntax permits arbitrary nesting and charges one node per power regardless of exponent. A uniform logarithmic-time Evertse estimate for overlapping short-period windows handles templates whose expanded lengths depend on the path. A finite-depth extraction and disjoint-subtree count handle unbounded nesting. In particular the number of constant odd-gap plateaus on a fixed nonperiodic positive ray is superlogarithmic in the final physical event time. The result includes one full primitive cycle cut at its least state. Source-specific prior results for factor complexity and charged adaptive dictionaries are compared in the manuscript.

`PowerTreeArithmetic.lean` strictly compiled with the shared Lean 4.34.1 environment. The checked endpoints are finite parity-prefix congruence, $2^{qp}\le3^p(x+1)$ when a literal $q$th power has distinct states one period apart, and $2^{qp}\le(x+1)^5$. The Evertse and combinatorial extraction proofs are written arguments.

## Actual previous-factor addresses, including shared grammar nodes

`PREVIOUS_FACTOR_ADDRESSES.md` gives a separate lower bound for exact matches against arbitrary earlier states. Let $a_i,b_i$ be the destination and earlier source starts of copies in a longest-previous-factor parse. The proof also permits a chosen dictionary of addresses, provided a used match ends on its first discrepancy, with final truncation allowed. For $D=\log(1+T/B)\to\infty$, any parses with $O(D)$ packets have
$$
 \liminf D^{-1}\sum_i b_i/(B+a_i)\ge (1-c)/(2c)=0.3547556\ldots,\quad c=\log_2(3/2).
$$
Macroscopic copies can supply the full bound as their threshold decreases to zero. Macroscopic exact copies with uniformly vanishing relative addresses occupy at most $c$ of limiting logarithmic time. The carry is integral and odd, and the shifted-block address charges become active only at their physical destination times. This permits addresses comparable to the current time without an uncontrolled reference-denominator cost.

With arbitrary shared grammar nodes, a finite traversal gives $\int_0^Tdt/H(t)\le2g+1$, where $g$ counts rules and $H$ is the maximum prior shifted bit length. This proves superlogarithmic shared grammar size on every fixed subexponentially growing aperiodic positive ray. The manuscript also proves a dyadic local factor-count bound in terms of the grammar's earliest expanded internal boundaries. For unrestricted growth and unrestricted previous addresses a logarithmic-size shared grammar remains possible under these arguments.

## Exact obstruction from a single perturbed clock

`GAUSSIAN_CLOCK_REPAIR.md` tests a proposed Gaussian interpolation and iterative inverse for cumulatively perturbed quadratic clocks. In the normalized consecutive-column system a single $+1$ change in the cumulative odd count perturbs only one matrix entry. Lagrange interpolation gives the exact new reduced denominator outside 2 and 3 of the penultimate normalized coefficient, $\prod_{d=1}^{n-1}(3^{hd}-2^{hd})$, for every even $h\ge2$. Its logarithm has quadratic order already for one bounded defect, and the formal iterative inverse has infinite support. Directly carrying the unperturbed coefficient-height estimate through this repair loses its quadratic margin. This calculation supplies no general exclusion of irregular clocks and no obstruction to every other choice of auxiliary form.

## Exact finite controls

Normal and optimized Python produced identical output with active explicit guards.

- `check_power_grammar.py` independently enumerated all 254 nonempty binary words of length at most seven to check optimal tree sizes. It audited 100 simple positive source prefixes, 3,102 literal powers, 1,136 shared copies, 4,588 finite grammar boundary inequalities, and 105,283 signed integer transports including every nonempty subsum.
- `check_gaussian_repair.py` solved 32 systems by exact rational elimination, checking 176 repaired rows and the reduced extra-prime denominator in every case. The largest tested denominator outside six occupied 571 bits.
