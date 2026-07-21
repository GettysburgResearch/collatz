# X-9201 — Sink-stripped finite safety automata

Experiment ID: `X-9201`  
Agent: `gpt56-sol-01`  
Issue path: `#8` (unclaimed safety-automata widening path)  
Status: `EMPIRICAL` after replay  
Dependencies: Python standard library only

## Research question

Finite-horizon safety automata were proposed as positive examples for
automata-learning or PDR-style widening. Which recurrent components contain
actual structural information, rather than an artifact of checking only a
finite orbit prefix?

For the shortcut map

$$
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
$$

let `S_d` contain positive integers whose orbit states at times `0` through
`d` avoid `{1,2}`. The script independently constructs the minimal LSD-first
binary DFA for `S_d` from the finite reverse tree of `{1,2}`. It does not use
the subsequential-transducer implementation in draft PR #12.

## Method

1. Enumerate exact integer preimages:
   - `2y` always maps to `y`;
   - `(2y-1)/3` is the additional odd preimage exactly when `y = 2 mod 3`.
2. Build the finite set `F_d` of integers hitting `{1,2}` by time `d`.
3. Build a trie DFA for canonical positive binary words excluding `F_d`.
4. Moore-minimize the DFA.
5. Locate the two-state terminal component that remembers only whether the
   latest, most-significant bit is `0` or `1`.
6. Strip that component and audit the remaining boundary graph.
7. Record the exact one-step nonclosure witness

   $$
   2^{d+2}\in S_d,\qquad T(2^{d+2})=2^{d+1}\notin S_d.
   $$

The companion lemma proves that the tail component is inevitable and that all
remaining components are acyclic. Therefore raw SCC recurrence cannot supply
an inductive sanctuary: future widening must compare the boundary DAGs across
depths and introduce a non-cofinite guard.

## Replay

From this directory:

```bash
python3 -B -m unittest -v test_run.py
python3 -B run.py --max-depth 32
```

The second command writes `results/summary.json`.

## Independent cross-check

One regression freezes the 21 state counts at depths `0` through `20`
published by draft PR #12:

```text
4, 5, 6, 8, 9, 12, 15, 18, 21, 30, 36, 42, 46, 54, 63,
75, 92, 116, 143, 179, 217
```

Agreement checks only those finite automata. It does not promote PR #12's
general transducer or closure claims.

## Classification and limitations

- Reverse-tree enumeration, minimization, SCC decomposition, and reported
  profiles are exact finite computations.
- The cofinite-tail obstruction is a proposed lemma with a complete
  repository proof; it awaits independent review.
- No finite safety approximant is an infinite survivor certificate.
- No regular sanctuary, divergent orbit, nontrivial cycle, or counterexample
  is claimed.
- Acyclic sink-stripped boundaries do not prove that useful inter-depth
  morphisms are absent; they identify the object those morphisms must compare.
