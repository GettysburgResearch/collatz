# X-8304 — Exact ordered-valuation decision of the full 80-site run grammar

Experiment ID: `X-8304`  
Agent: `gpt56-cycle-02`  
Issue: #9  
Associated claims: `L-8306`, `T-8303`  
Classification: exact compressed computation; no counterexample

## Question

The earlier critical-scale experiments selected one subset of 80 disjoint run-transposition sites and forced the numerator through a proper denominator component.  Does **any** of the

```text
2^80 = 1,208,925,819,614,629,174,706,176
```

valid subsets give an ordinary integral fixed point for the complete denominator?

## Method

For the lower critical run word, the first three canonical disjoint unequal sites begin at run positions

```text
0, 7, 15.
```

Their exact numerator-delta valuations are strictly increasing.  In particular, after choosing the first two repair bits, every remaining delta is divisible by

```text
2^295.
```

The experiment performs two independent exact computations:

1. a directed real affine-monoid enclosure for the union of all `2^80` repaired fixed points;
2. the four possible quotient residues modulo `2^295` determined by the first two repair bits.

The real interval lies strictly below the modulus.  None of the four quotient residues lies in the integer window of that interval.  Therefore no completion of any prefix can be integral.

This is a complete grammar result, not sampling and not a proper-factor sieve.

## Replay

```bash
python3 -B run.py --check-results results/canonical.json
python3 -B verify.py results/canonical.json
```

`verify.py` imports no author module and reconstructs the mechanical bits, disjoint sites, directed interval, complete numerator residue, and four prefix cylinders independently.

## Boundary

The result excludes exactly the frozen 80-site disjoint run-transposition grammar.  It does not exclude:

- later sites;
- overlapping replacements;
- hierarchical Farey block transpositions outside this site list;
- other words with the same `(A,k)`;
- positive cycles in general;
- an infinite negative-cycle chart path.
