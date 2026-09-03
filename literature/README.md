# Literature

External results imported for reference. An imported result is **never** a resident theorem of this repository: it keeps its own map normalization, its own evidence state (published proof, formal proof at a frozen commit, replayed here or not), and its own boundaries. Consequences drawn from it inside this repository are separate claims with their own `PROPOSED`/reviewed status and live under `research/`.

| Packet | Result | Native map | Evidence state here |
|---|---|---|---|
| [`mazur-2026-natural-density-log-time/`](mazur-2026-natural-density-log-time/README.md) | for every `f→∞`, a natural-density-one set of `N` has `Col^m(N)<f(N)` with `m ≤ 436 log N`; quantitative fixed-target bound `≪ (log N_0)^{-d}`, `d<5/143` | raw `Col` and Syracuse `Syr` | external Lean formalization at a frozen commit; **not replayed**; paper-exposed numerics replayed exactly |
| [`mazur-2026-predecessor-x090/`](mazur-2026-predecessor-x090/README.md) | `π_a(x) ≥ x^{9/10}` eventually for every positive `a` with `3∤a` | repository shortcut `T` | external Lean formalization with two `native_decide` trust points; 344,373,768-row certificates **not replayed**; paper-exposed numerics replayed exactly |

Replay of the paper-exposed numerics: [`mazur-2026-checks/replay_paper_numerics.py`](mazur-2026-checks/replay_paper_numerics.py), output in [`replay_paper_numerics.out`](mazur-2026-checks/replay_paper_numerics.out). Run with

```bash
python3 literature/mazur-2026-checks/replay_paper_numerics.py
```

Interfaces of these results with the repository programs, and the improvement map, are in [`../research/density-interfaces/`](../research/density-interfaces/README.md).

## Import discipline

1. State the result in the source's own normalization first, then translate to the shortcut map `T` explicitly.
2. Record what was replayed (exact numerics, small identities) and what was not (formal proofs, large certificates).
3. Separate what the source proves from what the repository infers from it; the inference is a new claim.
4. A density-one, almost-all, or lower-bound statement never crosses the repository's central firewall into a statement about one fixed positive integer.
