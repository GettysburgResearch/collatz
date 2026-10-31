# Concurrent PR140 pass and exact integration boundary

**PROPOSED; comparison and conditional arithmetic deduction, not independent
acceptance.** The initial PR143 content commit is
`c431a0d46d311872d8afd5388215abf56b3d392e`, based on the frozen pass-3 head
`6bee3183ff7f29f2e20ca88ab94bc7745c1af602`.

While this work was being prepared, PR140 advanced to
`fe2247fcd7730c15430941a7b6e011d006d41d84`, tree
`431a91c25bbd3a5bcbbaa35fd43afde70edeb557`, adding ten pass-4 files.
The remote comparison confirmed ten additions and no modifications/deletions.
Those paths are disjoint from this packet. The continuation merges that exact
upstream commit into its OWN branch without modifying the upstream branch,
rewriting history, or changing any of the initial eight packet files.
This note is the ninth packet file. No mathematical registry is promoted.

## What was read, and what was not replayed

At the exact new upstream commit, this session read:

- `research/novel-swarm-20261030/pass4/README.md`, blob
  `6a0aefd3ace44d6137685747e1607c4d2b5d9919`;
- `research/novel-swarm-20261030/pass4/WINDOWS.md`, blob
  `b6ac911e613c0ecaaa4032b2831790e09c3a5f54`;
- `research/novel-swarm-20261030/pass4/PRESSURE.md`, blob
  `1d2125a91b2b2c24a63894ece0113c89d8045eb5`.

Its all-width induction and pressure proof were inspected; its experiments,
full validation corpus, and record proof were not independently replayed in
this session. Its self-audited PROPOSED status remains unchanged. The separate
normal/optimized tests in our receipt apply to our unchanged scripts, not
retroactively to that concurrent ten-file packet or to a complete checkout.

## Overlap and distinct contributions

Upstream P4-1 proves the stronger TRANSLATED estimate

    sup_(a>=1) sum_(a<=t<a+K) F(t) <= 20 K^(19/20).

Thus its positive superlevels have zero upper Banach density. Our explicit
anchored PF-001 is not advertised as the project's strongest averaged bound.
Our PF-001b retains a nonexplicit optimized anchored exponent; neither result
establishes pointwise decay. Both use the same credited orbit-packing/Tonelli
mechanism. There is no novelty or priority claim for duplicating that step.

Upstream also supplies certified drops of FULL F and a summable-variation
bound on nonperiodic orbits. Our monotone E_q is a DIFFERENT quantity, indexed
by a common finite odd clock and summed over all starting sources. Its
monotonicity is compatible with those F drops. The moment S_q in PF-008 is
also distinct from the upstream coefficient-record count and the original
occupation-collision target E5. Those exponents must not be interchanged.

The distinct focus of this packet is the computable finite-clock energy,
unfinished-prefix all-target certificates, the squared-derivative moment
criterion, the exact ordinary fixed space, and the specified power-envelope
obstruction. The actual vanishing claim remains open in BOTH packets.

## PF-009. Optional strengthened explicit moment threshold

Assume the proposed upstream W2 bound for the distinct values of any simple
shortcut path in an interval of length K:

    count <= 16 K^(19/20).

For one hypothetical nonperiodic odd source n, sort the first Q odd values
as z_1<...<z_Q. Since odd values are a subset of the corresponding simple
shortcut path, W2 gives z_i >= (i/16)^(20/19). Combining this with PF-008 (10)
and summing the lower integral yields

    sum_(q<Q) S_q
      >= [2^-400/n^4] [19/(59 * 16^(40/19))] Q^(59/19).

Therefore S_q=O(q^p) for ANY p<40/19 would exclude an escaping source.
This upgrades the explicit p<80/39 range obtained from the older coarse
packing constant. The nonexplicit optimized PF-008b range remains slightly
larger. In particular the already sufficient quadratic target (M) is
unchanged, and still unproved. This deduction does not supply a moment upper
bound; its upstream premise retains its review qualification.

No external Haar quadratic-energy estimate is substituted for (M). Neither
the new translated averages nor the finite-clock energy by themselves give
that missing all-source bound.
