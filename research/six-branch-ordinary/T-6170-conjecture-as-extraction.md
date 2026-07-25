```text
Claim ID:            T-6170
Title:               The Collatz conjecture IS a least-root extraction question, at the
                     maximal architecture
Status:              PROVED
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        none (self-contained); reframes L-6105(d), Q-7601, T-7601, T-7801
Scope:               the full Collatz conjecture
Experiment:          experiments/X-6170-uniform-floor/
```

## Statement

For `L >= 1` define the **stopping floor**

```text
s_L = min { n >= 2 : T^j(n) >= n for all 1 <= j <= L },
```

where `T` is the shortcut map. (`n = 1` is excluded: it is the trivial cycle and satisfies the
condition for every `L`.)

**(a) `s_L` is well defined and `s_L <= 2^(L+1) - 1`.**

**(b) `s_L` is nondecreasing.**

**(c)**

```text
   The Collatz conjecture   <=>   s_L -> infinity   <=>   (s_L) is unbounded.
```

**(d)** Equivalently, by (b) and the argument of L-6105(d): the conjecture is false **iff**
`(s_L)` is eventually constant, and then its eventual value is the minimal element of a
counterexample orbit.

## Why this matters

The project has treated "ordinary extraction" — `sup_N m_N < infinity` versus
`m_N -> infinity` — as a technical gap sitting between its architectures and a counterexample,
and PR #57 `T-7601`, PR #56 `T-7801` and L-6105(d) all normalise the quantifier the same way.

**(c) says the extraction question is not a gap between the architectures and the conjecture.
It is the conjecture.** Every architecture's extraction question is the same question asked of
a smaller set:

| architecture | its least-root sequence | "bounded" means |
|---|---|---|
| six-branch chart (issue #58) | `m_N`, X-6110 | a divergent orbit confined to 6 macro blocks |
| any sound architecture `S` | `m_N^S` | a counterexample of that shape |
| **the maximal one: `{n : T^j(n) >= n forall j}`** | **`s_L`** | **a counterexample, full stop** |

Consequences worth stating plainly:

1. **Deciding extraction for any architecture is a weakening of Collatz, never a technique for
   it.** Proving `m_N -> infinity` for an architecture is a partial result (it excludes
   counterexamples of that shape); proving `sup m_N < infinity` would refute the conjecture.
   There is no third outcome in which the extraction machinery becomes an *instrument*.
2. **The normalisation costs three lines at every scale.** L-6105(d) is elementary, and so is
   (c). That it is elementary at the maximal architecture is the cleanest demonstration that
   quantifier normalisation is not progress.
3. **Choosing a thinner architecture does not make the question easier, only smaller.** The
   six-branch instance is the thinnest in the repository (dimension `0.136` against the
   ceiling `0.94996`, T-6131), which is exactly why its `m_N` blows up after 16 levels while
   `s_L` is still `63728127` at `L = 375`.

## Proof

**(a)** Take `n = 2^k - 1`, odd. Then `T(n) = 3*2^(k-1) - 1`, and inductively
`T^j(n) = 3^j 2^(k-j) - 1` for `0 <= j <= k`, each odd until `j = k`. Since
`3^j 2^(k-j) >= 2^k` for `j >= 0`, we get `T^j(n) >= n` for all `j <= k`. Hence
`s_L <= 2^(L+1) - 1`, and in particular the defining set is nonempty. `QED`

**(b)** The condition for `L+1` implies the condition for `L`, so the minimum cannot
decrease. `QED`

**(c)** *(⇐)* Suppose `s_L -> infinity` and let `n >= 2`. Choose `L` with `s_L > n`. Then `n`
fails the condition at depth `L`, so `T^j(n) < n` for some `j <= L`: every `n >= 2` eventually
drops strictly below itself. By strong induction on `n`, every positive integer reaches 1.

*(⇒)* Suppose the conjecture holds and fix `X`. Every `n` in `[2, X]` drops below itself after
finitely many steps; let `S` be the maximum of those finite times over the finitely many `n`.
For `L >= S` no `n <= X` satisfies the condition, so `s_L > X`. Hence `s_L -> infinity`.

The second equivalence in (c) is (b) plus the fact that a nondecreasing integer sequence is
unbounded iff it tends to infinity. `QED`

**(d)** If `(s_L)` is eventually constant `= s`, then `s` satisfies `T^j(s) >= s` for every
`L` and hence for all `j`, so `s` never drops below itself and (being `>= 2`) never reaches 1:
`s` is a counterexample, and it is the minimal element of its own orbit. Conversely, the
minimal element `m` of any counterexample orbit satisfies `T^j(m) >= m` for all `j`, so
`s_L <= m` for every `L` and `(s_L)` is bounded, hence eventually constant by (b). `QED`

## Adversarial tests

* `s_L` computed exactly for `L <= 375` (X-6170) reproduces the classical stopping-time record
  integers `3, 7, 27, 703, 10087, 35655, 270271, 362343, 381727, 626331, 1027431, 1126015,
  8088063, 13421671, 20638335, 26716671, 56924955, 63728127` — an external check that the
  definition is the classical one and the computation is right.
* `s_L <= 2^(L+1)-1` from (a) is loose but confirmed: at `L = 375` the true value is
  `63728127 = 2^25.93`, vastly below `2^376`.
* The trivial-cycle exclusion matters: without it `s_L = 1` for every `L` and (c) collapses.
  The computation excludes `n = 1` explicitly, and the first run — which did not — returned
  `s_L = 1` identically, catching the error.

## Gap audit

* *Is (c) circular?* No. It is an equivalence, proved in both directions from the definition,
  and it is stated precisely so that the reader does not mistake the extraction framing for a
  method. It provides no route to deciding either side.
* *Does (c) make the conjecture easier?* **No, and that is the point.** The claim's value is
  diagnostic: it prices the extraction framing at zero.
* *Is `s_L` computable?* Each value is, by exhaustive scan, and the sequence is the classical
  record sequence. But no finite prefix can certify boundedness (same gap as L-6105).
* *Does (d) need the orbit minimum to exist?* Yes, and it does: for a cycle the orbit is
  finite; for a divergent orbit `n_j -> infinity` (T-6131a) so only finitely many terms lie
  below any bound.

## Suggested next attack

None on this claim. Its consumers are R-6171 (which uses the same object to price a classical
attack) and M-6120 (which should cite it when telling authors that an extraction result is a
weakening of the conjecture, not a tool).
