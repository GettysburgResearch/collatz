# Erdős--Kahane methodology and the carry-rigidity EQ proof

## Classical pattern

The Erdős--Kahane method for Bernoulli convolutions and self-similar measures typically argues:

```text
large Fourier coefficient
 -> many phases lie unusually close to integers
 -> the near-integer choices have low combinatorial entropy
 -> exceptional parameters/frequencies form a sparse set.
```

Kaufman, Tsujii, Solomyak, Mosquera--Shmerkin, and related work develop quantitative versions for real self-similar measures, often outside a small parameter or frequency set.

## Repository pattern

The PR #16 chain replaces generic real-parameter transversality by an exact arithmetic lift system:

```text
large coefficient
 -> small quadratic phase energy
 -> few nonzero integer carries
 -> long exact zero-carry runs
 -> excessive divisibility of one nonzero ordinary integer
 -> completion-height contradiction.
```

The split is:

- `L-9309`: every lift prefix is one residue class modulo `81^L`;
- `T-9307`: low-energy prefixes occupy a power-small fraction of every interval;
- `T-9308`: dyadic shelling converts sparse exceptions into a uniform harmonic tail;
- `L-9310`: an individual low frequency cannot maintain too many zero carries because of archimedean height;
- `T-9311`: uniform pointwise decay on every subexponential window;
- `T-9312`: low/high assembly gives all-depth weighted EQ.

## Literature verdict

The classical literature is **methodological overlap**, not a direct proof:

- the ambient group is different;
- the parameter is fixed;
- the characters move with depth;
- the frequency window grows triangularly;
- the exact integer carries are native arithmetic data absent from generic real IFS theorems.

If the chain survives review, its strongest novelty claim is not “another application of Solomyak.” It is a deterministic, nonarchimedean Erdős--Kahane theorem where exact carry quantization replaces parameter exclusion.

## Review checklist

1. Verify the sign and level convention of every reciprocal phase.
2. Verify that the lift tuple is a bijection over **every translated** complete block.
3. Check the `41/40` grid split and the direction of the exponential-moment Markov bound.
4. Check the final incomplete dyadic shell and `L<K` uniformly.
5. In the zero-carry theorem, verify:
   - the modulus `81^(ell+r+1)`;
   - the ordinary numerator is nonzero for primitive frequency;
   - terminal-distance indexing;
   - removal of powers of `64`.
6. Reconstruct the survivor/mirror comparison without relying on plots or word order inferred from code.
7. Only then import the issue-#4 Erdős--Turán consequences.

## Next literature-facing questions

- Can the crude carry-energy constant be optimized through a lattice shortest-vector calculation?
- Can `p`-adic logarithmic-form lower bounds improve the zero-run height squeeze?
- Is there a general theorem for coprime charts `M<N` giving a power Fourier envelope from integer carry quantization?
- Can the proof be recast as a transfer operator with a spectral gap on a countable carry state space?

The all-depth EQ result, even if correct, does not settle one exceptional ordinary point in the infinite attractor.