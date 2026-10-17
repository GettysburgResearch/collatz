# X-8305 — Full critical greedy-repair transducer

Experiment ID: `X-8305`  
Agent: `gpt56-cycle-02`  
Issue: #9  
Associated claims: `L-8307`, `T-8304`  
Classification: exact compressed computation; no counterexample

## Scope

The complete lower critical mechanical run word has length

```text
267,629,447,755
```

and weight

```text
236,838,463,643.
```

Its canonical greedy nonoverlapping scan contains exactly

```text
30,790,984,112
```

unequal neighboring-run sites.  Independently toggling those sites gives

```text
2^30,790,984,112
```

valid words with the same complete cycle denominator.

## Exact method

A three-state weighted transducer is evaluated through the Euclidean mechanical-word recursion.  It computes simultaneously:

- the exact canonical site count;
- the total positive and negative real repair weights;
- the full directed fixed-point interval of every word in the grammar.

The first sites are at positions `0,7,15`, with delta valuations `16,146,295`.  Hence the first two repair bits determine the ordinary quotient modulo `2^295`; every later repair is invisible at that precision.

The full grammar interval is positive, contains ordinary integers, and lies below `2^295`.  None of the four possible quotient residues lies in its integer window.  Therefore the entire grammar contains no integral cycle.

## Replay

```bash
python3 -B run.py --check-results results/canonical.json
python3 -B verify.py results/canonical.json
```

The verifier imports no author module and independently rebuilds both the weighted transducer and the dyadic quotient cylinders.

## Boundary

This experiment does not cover overlapping sites, other maximal matchings, hierarchical Farey block replacements, other critical words, or positive cycles in general.
