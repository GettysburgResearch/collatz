# Leading digits and finite automata in the stationary six-branch chart

**Status: PROPOSED.** The following statements concern positive ordinary values. They are conditional on the existence of a survivor where a survivor is explicitly assumed. The existence question remains open.

Use the chart of [L-0041](../../claims/lemmas/L-0041-six-branch-root-cap-recurrence.md) and the [resident rigidity packet](../integrated/six-branch-rigidity/README.md), based on PR #64 at `88884c3e590b08aeb2018872987e71e14de1fe7b`. The baseline here is `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Put Q=2^19, P=3^12 and λ=P/Q. A legal step has Qx'=Px+a with a in the six-element digit alphabet of L-0041. A legal future of length m forces one of at most 6^m residues modulo Q^m. A legal past of length m forces one of at most 6^m residues modulo P^m: composing a word gives Q^m x'=P^m x+A and Q is invertible modulo P^m.

## Theorem 1. No recognizable sanctuary in any integer base

For every integer b≥2, there is no base-b recognizable set of positive integers contained in the all-time survivor set and containing the complete forward orbit of even one positive integer. In particular there is no nonempty recognizable forward-invariant subset of the survivor set. Recognizability here means acceptance of the canonical most-significant-digit-first representations by a finite automaton.

**Proof.** An all-time orbit satisfies

    x_n = λ^n C + O(1),    C = x_0 + Σ_{j≥0} a_j/(Q λ^{j+1}) > 0.

The error bound is at most max(a)/(P−Q), by summing the discarded geometric tail after multiplication by λ^n. The number log_b λ is irrational: otherwise a positive power of P/Q would equal an integer power of b, impossible in lowest terms. Thus the fractional parts of log_b x_n are dense, by irrational rotation and an error tending to zero. Every finite canonical base-b prefix occurs on arbitrarily late orbit values, since its significands contain a nonempty open interval.

In a deterministic automaton of s states, every extendible prefix can reach acceptance in at most s−1 further symbols, by taking a shortest path. For each of the (b−1)b^(k−1) canonical prefixes of length k select such a completion. The selected integers are distinct and below b^(k+s). The recognized set therefore has positive upper asymptotic density. In contrast the upper density of the legal all-time set is at most (6/Q)^m for each m, by its future residues. Letting m increase gives zero. ∎

## Theorem 2. No single survivor orbit contains an infinite recognizable subset in any base

An infinite language of canonical base-b representations recognized by a finite automaton contains a family uv^t w, with v nonempty and all t≥0, by pumping a cycle on an accepting path. The corresponding positive integers satisfy z_t = α B^t + β with B=b^|v| and rational α>0, β, by summing the geometric series. They strictly increase and z_(t+1)/z_t tends to B.

If they lay on a single survivor orbit, write z_t=x_(n_t). The times strictly increase since the legal map strictly increases. The asymptotic x_n=C λ^n+O(1) from Theorem 1 implies λ^(n_(t+1)−n_t) tends to B. A convergent sequence in the discrete positive powers of λ is eventually constant, so B would be a positive power of P/Q. Such a power has nontrivial denominator and B is an integer. This proves the assertion for every b. More generally any increasing subsequence of an orbit whose consecutive ratios have finite limit greater than one has limit in the positive powers of λ.

## Theorem 3. Pumped languages in unions of orbits

For odd b even the union of all survivor orbits contains no infinite base-b recognizable subset. For b coprime to 3 the same conclusion holds for any set of values in which, for every m, all but finitely many values have a legal past of length m. The pasts may come from different ordinary roots.

**Proof.** An infinite regular language of canonical representations contains all words uv^t w for t≥0, with v nonempty, by pumping a cycle on an accepting path. Their integer values have the form

    z_t = (A B^t + D)/E,    B=b^|v|,  E=B−1,

with fixed integers A,D and A>0. This follows by summing the geometric series for the repeated block. Positivity of A also follows from unbounded canonical lengths. Choose p=2 for odd b, or p=3 if 3 does not divide b. Take h=2, so B^h≡1 modulo 4 for p=2 and modulo 3 for p=3. For every positive j,

    v_p(B^(hj)−1) = v_p(B^h−1)+v_p(j).

Indeed raising 1+y to a prime-to-p power preserves v_p(y), and raising to the pth power increases it by exactly one by the binomial expansion under the stated divisibilities. It follows that v_p(z_(ht)−z_(hu))=c+v_p(t−u) for t>u, with fixed nonnegative c=v_p(A)+v_p(B^h−1)−v_p(E). Hence arbitrarily late terms of this progression occupy at least p^(d−c) distinct residues modulo p^d when d≥c.

For p=2 take d=19m and use future residues. For p=3 take d=12m and use past residues. In the latter case discard the finitely many exceptions to the legal past condition. In both cases the lower bound exceeds 6^m for large m. ∎

The past argument needs arbitrarily long legal histories for the tested values. An arbitrary union of forward orbits need not supply them. For bases divisible by six the pumped-progression argument above has neither unit available. Theorems 1 and 2 still hold in those bases.

## Missing inference

These obstructions apply to recognizable sets of ordinary values. An individual orbit need not contain any infinite recognizable subset or admit a recognizable envelope inside the survivors. Neither theorem decides whether the least positive legal roots escape.
