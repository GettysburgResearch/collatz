# X-0011 — Regular marked-grammar collapse bridge

Experiment ID: `X-0011`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of proposed exact claims `L-0015` and `T-0020`

## Research questions

1. Can a regular language of finite endpoint pairs be compiled exactly to the
   regular language of physical interval lengths?
2. Can high zero padding on a projected length track be removed without a
   bounded-length assumption?
3. Does the resulting DFA interoperate with the exact shortcut transducer and
   maximal safety-kernel construction used by the regular-sanctuary program?
4. Do fixed finite macro-block checkpoints normalize to one-step closure as
   stated in `T-0020`?

## Method

`run.py` is standard-library only. It implements:

- canonical LSD-first integers;
- synchronous endpoint-pair encodings over `00,01,10,11`;
- complete pair DFAs;
- an exact NFA projection enforcing
  \[
  v+n=q
  \]
  with one carry bit;
- canonical high-zero removal as the right quotient by \(0^*\);
- subset determinization with canonical-positive monitoring;
- the exact shortcut subsequential transducer;
- exact DFA closure witnesses;
- the greatest raw-state safety kernel avoiding canonical `1` and `2`.

The implementation is a small independent bridge. It does not replace the much
larger exact verifier in PR #12.

## Checks

The script:

1. generates 64 deterministic random finite endpoint languages and proves that
   the compiled DFA accepts exactly their finite difference sets;
2. verifies deduplication when several gauges represent the same physical
   length;
3. compiles the infinite regular fixed-gauge language
   \[
   \{\operatorname{conv}(1,q):q\ge2\}
   \]
   to all canonical positive integers;
4. proves exact shortcut closure of that compiled DFA;
5. computes its maximal raw-state safe kernel and proves that no canonical
   positive word reaches the kernel—so it is semantically empty;
6. verifies fixed-block normalization on the terminal two-cycle control.

## Command

```bash
python3 -m py_compile experiments/X-0011-regular-marked-collapse/run.py
python3 experiments/X-0011-regular-marked-collapse/run.py
```

## Expected output

```text
verified exact regular interval-length projection
compiled fixed-gauge all-positive intervals: pair_states=5 length_states=8
verified exact shortcut closure and empty safe kernel
verified finite-block normalization on 2-value control
all regular-marked-collapse checks passed
```

Here “empty safe kernel” means **no canonical positive word reaches the raw
safe-state set**; the raw set itself need not be literally empty.

The checked-in copy is `results/summary.txt`.

## Interpretation

The experiment confirms an effective bridge:

\[
\text{regular finite interval configurations}
\longrightarrow
\text{regular ordinary marker language}.
\]

Together with `T-0020`, this means a finite-phase regular marked-particle
certificate belongs to the same existential class as a regular sanctuary and
can be checked by PR #12.

The new construction frontier is therefore not another finite-state phase
cover. It is an explicitly unbounded counter/stack or a genuinely nonregular
ordinary survivor language.

## Limitations

- The random tests validate the implementation, not the general proof.
- No regular sanctuary is constructed.
- The compiler may incur exponential subset-construction blowup.
- Pushdown and counter languages are outside the experiment.
- No positive-integer counterexample is proposed.
