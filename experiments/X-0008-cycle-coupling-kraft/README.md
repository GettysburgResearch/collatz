# X-0008 — Negative-cycle coupling, padded returns, and Collatz–Kraft identities

Experiment ID: `X-0008`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of proposed exact claims `T-0014`, `T-0015`, `T-0016`, and `O-0008`

## Research questions

1. Does the exact two-dimensional difference/phase map reproduce every ordinary shortcut-Collatz step?
2. Does valuation acceleration give the stated one-mismatch formula?
3. Do the complementary phases of the negative eleven-cycle enter the negative eleven-cycle, negative three-cycle, or fixed phase according to one finite atlas?
4. Do complete circuits of the negative eleven-cycle generate exact geometric towers of padded return edges?
5. Do complete parity prefix codes satisfy the two exact Kraft identities, likelihood-ratio identity, and negative typical logarithmic drift?

## Method

`run.py` uses exact Python integers and fractions only. It:

- checks the synchronous coupling formula for all
  ```text
  1 <= v <= 300,
  1 <= q <= 1000;
  ```
- checks the accelerated valuation formula for all selected negative-cycle phases and
  ```text
  1 <= q < 5000;
  ```
- reconstructs the complete complement-basin table of the negative eleven-cycle;
- verifies every one-mismatch return tower for the first four padding levels;
- directly iterates the corresponding ordinary physical Collatz states;
- verifies the two grouped base transfer families from phase `-136`;
- checks the exact signed displacement formula;
- confirms that the two tower types first become supercritical at padding levels `45` and `21`;
- verifies the ordinary and tilted Kraft identities on several complete prefix codes;
- verifies the likelihood-ratio identity word by word;
- checks the exact expected odd count and logarithmic drift formula, including the nonuniform code
  ```text
  0, 10, 110, 111.
  ```

## Command

```bash
python3 -m py_compile experiments/X-0008-cycle-coupling-kraft/run.py
python3 experiments/X-0008-cycle-coupling-kraft/run.py
```

## Expected output

The checked-in output is

```text
results/summary.txt
```

and ends with

```text
all cycle-coupling and Kraft checks passed
```

## Digests

```text
b3afb57d63826d23b797b6d676f781b13aa0609be68ea8140042b4c815a4081e  run.py
442337a8811fe26c07a3816ad0fb623d2f88d0f7d18f32deaeb7292230097d23  results/summary.txt
```

## Interpretation

The experiment supports three structural conclusions.

1. Negative phases provide an exact synchronous reference system, not an analogy.
2. A mismatch from a negative cycle has finitely many phase types and an unbounded cycle-padding counter; each type generates an exact geometric tower of return edges.
3. Complete renewal coverage obeys an exact mean-one multiplier law but has negative typical logarithmic drift. A counterexample grammar must therefore be an exceptional pressure-positive sublanguage with one ordinary finite boundary.

## Limitations

- All checks are finite.
- The return towers do not form a closed invariant grammar.
- Haar-null exceptional sets may be nonempty, but the experiment does not locate an ordinary member.
- No positive-integer counterexample is proposed.
