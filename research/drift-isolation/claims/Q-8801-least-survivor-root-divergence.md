# Q-8801 — Least-survivor-root divergence

Claim ID: Q-8801  
Title: Does the least positive depth-`n` root tend to infinity?  
Status: IDEA / OPEN  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: T-8806, L-8804, T-8808, O-8802  
Scope: the exact base-`5/4` bottom map  
Related counterexample candidates: issue #26; no `K-####` candidate

## Question

For

```text
tau(x)=ceil(5x/4)
```

let `S_n` be the positive integers whose first `n` bottom digits lie in
`{0,1}`, and let

```text
m_n=min S_n.
```

Is

```text
m_n -> infinity?
```

## Exact significance

The sets `S_(n+1)` are nested inside `S_n`, so `(m_n)` is nondecreasing.
Moreover, `O-8802` proves the equivalence

```text
there is a positive infinite chart survivor
iff (m_n) is bounded
iff (m_n) eventually stabilizes.
```

Therefore:

- proving `m_n -> infinity` closes the exact `4 -> 5` chart negatively;
- proving eventual stabilization constructs one explicit divergent positive
  `5x+1` chart orbit.

## Known exact inputs

- `L-8804` gives a complete meet-in-the-middle composition formula for every
  finite frontier.
- `T-8808` proves

  ```text
  m_50=4538335001132531.
  ```

- `L-8811` shows every finite binary word remains locally realizable, so a proof
  cannot consist of a finite forbidden-word list.
- `R-8802` shows autonomous finite-state schedules cannot give stabilization.

## Strongest useful next theorem

A recursive inequality of the form

```text
m_(h+m) >= F(m_h,m_m)
```

with `F` forcing unbounded growth on an infinite sequence of splits would solve
the negative side. On the positive side, a nested pair sequence in `L-8804` whose
least representatives become constant would give the required root.

## Failure conditions

- Computing one more finite value does not prove divergence.
- Haar measure zero or Hausdorff dimension `1/2` does not imply `m_n -> infinity`.
- A compatible `2`-adic directive does not imply bounded ordinary
  representatives.
