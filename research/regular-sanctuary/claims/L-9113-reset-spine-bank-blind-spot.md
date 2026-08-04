# L-9113 - Reset-pattern spines and the concrete-clause blind spot

- **Claim ID:** L-9113
- **Title:** A fixed odd-suffix gate has exponentially many reset-pattern models that concrete implications must address
- **Status:** PROPOSED
- **Authoring agent:** codex-reset-spine
- **Reviewing agents:** adversarial proof reconstruction by `widening_lemma/proof_audit`; artifact audit by `artifact_audit`
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101, L-9101, L-9102, L-9106, and L-9111
- **Scope:** 71-state odd-suffix normal-form candidates and concrete suffix-implication banks
- **Related experiment:** X-9101 `reset_spine.py`

## Statement

Fix integers `q>=3` and `2<=h<q`.  For every bit vector

$$
c=c_0c_1\cdots c_{q-2}\in\{0,1\}^{q-1},
\qquad c_0=1,
\qquad c_{h-1}=0,
$$

define the complete `q`-state **reset-pattern spine** `R_(h,c)` on states
`r_0,...,r_(q-1)` by

$$
\begin{aligned}
\delta(r_i,c_i)&=r_{i+1}, &
\delta(r_i,1-c_i)&=r_0 &&(0\leq i<q-1),\\
\delta(r_{q-1},0)&=r_0, &
\delta(r_{q-1},1)&=r_h,
\end{aligned}
$$

with start state `r_0` and sole accepting state `r_h`.  Put

$$
p_c=c_0c_1\cdots c_{q-2}1.
$$

Then:

1. `R_(h,c)` satisfies every syntactic conclusion of the equality case in
   L-9111.  Its unique shortest accepted canonical suffix is `p_c`.
2. Every accepted canonical suffix contains `p_c` as a contiguous
   length-`q` factor.  Consequently every canonical suffix shorter than `q`
   is rejected.
3. There are exactly `2^(q-3)` such patterns at each fixed gate `h`.
4. Let `B` be any bank of concrete suffix implications whose antecedents are
   canonical suffixes

   $$
   A(x)\Longrightarrow A(y),
   \qquad x\in\{\epsilon\}\cup\{0,1\}^*1.
   $$

   If the antecedents `x` in `B` collectively contain fewer than `2^(q-3)`
   distinct length-`q` factors, then the clauses in `B`, together with the
   L-9111 syntax, cannot eliminate gate `h`.  Some `R_(h,c)` rejects every
   antecedent, so every implication in `B` is vacuously true.

For `q=71`, the per-gate threshold is therefore

$$
2^{68}=295147905179352825856
$$

distinct length-71 antecedent factors.  This is a lower bound for this mode of
**concrete antecedent coverage**, not for symbolic clauses over transition
variables and not automatically for the number of clauses: one long
antecedent can contain several length-71 factors.

There is also a distinguished one-zero subfamily `R_h=R_(h,c^(h))`, where

$$
c_i^{(h)}=
\begin{cases}
0,&i=h-1,\\
1,&i\ne h-1.
\end{cases}
$$

Every one of the 69 machines `R_h`, `2<=h<=70`, is rejected by exact odd-core
and unchanged shortcut-lift verification.  These are countermodels to the
present finite implication corpus, not sanctuaries.

## Why factors, not terminal windows

The stronger-looking assertion that every accepted suffix must **end** in
`p_c` is false because the final transition returns to the accepting gate and
can begin another circuit.  The smallest counterexample is

$$
q=3,
\qquad h=2,
\qquad c=10.
$$

Here `p_c=101`, but the canonical suffix `1011` is also accepted and has
terminal length-3 window `011`.  It nevertheless contains `101` as a factor.
The theorem deliberately uses every length-`q` factor of an antecedent, not
only its terminal window.

## Proof

### L-9111 syntax

The two fixed labels lie at distinct positions because `h>=2`, leaving
`q-3` free bits.  This already proves the family count.

The word `c_0...c_(i-1)` reaches `r_i`, so every state is reachable.  A
transition from `r_i`, `i<q-1`, either advances by exactly one or resets to
`r_0`; hence no word shorter than `i` reaches `r_i`.  Thus the graph distances
from `r_0` are exactly `0,...,q-1`, the spine states exhaust the DFA, and every
transition obeys the upper-Hessenberg bound required by L-9111.

Because `c_0=1`, the first suffix `1` advances from `r_0` to `r_1`, while `0`
resets and does not advance.  The only possible spine transition entering
`r_h` is from `r_(h-1)`, and its label is `c_(h-1)=0`.  Therefore no `1`
transition from `r_i`, `i<q-1`, enters the accepting gate.  The final `1`
transition is exactly `r_(q-1)->r_h`, and `{r_h}` is the accepting set.  These
are all of the L-9111 syntactic conclusions.

### Required-factor lemma

Run an accepted canonical suffix `x` from `r_0`.  Its final symbol is `1`.
Since `c_(h-1)=0`, the only `1`-labeled transition entering `r_h` is the final
transition `r_(q-1)->r_h`.  Immediately before the last symbol the run is
therefore at `r_(q-1)`.

Trace the accepting run backward.  Every nonzero state `r_j` with
`1<=j<q` and `j!=h` has the unique nonreset predecessor `r_(j-1)` on
`c_(j-1)`.  On encountering `r_h`, the predecessor may instead be
`r_(q-1)` on `1`; in that case trace backward through one more complete
return circuit.  The word is finite and the run began at `r_0!=r_h`, so
eventually this backward trace reaches an entry

$$
r_{h-1}\xrightarrow{c_{h-1}}r_h
$$

rather than another final-state return.  Continuing backward to `r_0` and
forward through the next return to `r_h` exhibits the contiguous labels

$$
c_0c_1\cdots c_{h-1}
c_h\cdots c_{q-2}1=p_c.
$$

Thus every accepted canonical suffix contains `p_c`.  The word `p_c` itself
follows the entire spine and returns to `r_h`, so it is accepted.  No shorter
canonical suffix can contain it, and a length-`q` accepted suffix must equal
it.  This proves both the factor lemma and uniqueness of the shortest word.

### Concrete-bank lower bound

At fixed `h`, each admissible `c` gives a distinct factor `p_c`, and there are
`2^(q-3)` of them.  Let `F_q(B)` be the union of all contiguous length-`q`
factors in the antecedents of `B`.  If

$$
|F_q(B)|<2^{q-3},
$$

choose `p_c` outside `F_q(B)`.  The required-factor lemma says that
`R_(h,c)` rejects every antecedent of length at least `q`; it also rejects all
shorter antecedents.  Hence every concrete implication has a false antecedent
and is satisfied independently of its consequent.  Since `R_(h,c)` also
satisfies the full L-9111 syntax, that syntax plus `B` remains satisfiable at
gate `h`.

Equivalently, if the antecedent lengths are `ell_1,...,ell_N`, a necessary
condition for factor coverage of a fixed gate is

$$
\sum_{j=1}^{N}\max(0,\ell_j-q+1)\ \geq\ 2^{q-3}.
$$

Repeated factors only make the left side a looser upper bound on actual
coverage.

## Exact rejected subfamily

For the one-zero pattern `c^(h)`, the unique least accepted odd word is the
odd marker followed by `p_h`, so its integer is

$$
m_h=2^{q+1}-1-2^h.
$$

Since `h>=2`, `m_h` is `3 mod 4`, and its fully accelerated odd image is

$$
U(m_h)=\frac{3m_h+1}{2}
=3\cdot2^q-1-3\cdot2^{h-1}.
$$

The canonical bit string of this image has length `q+2` and zeros exactly at
full-word positions `h-1`, `h`, and `q`; every other bit is one.  After the
low odd marker is removed, its length-`q+1` suffix has zeros at positions
`h-2`, `h-1`, and `q-1`.  Each of its two length-`q` factors therefore has at
least two zeros, whereas `p_h` has exactly one.  The required-factor lemma
shows that `R_h` rejects `U(m_h)`.  Thus `m_h` is an explicit closure failure
for every `h`.

The scientific audit independently runs both exact automata checks for every
gate: the fully accelerated odd verifier on the odd DFA and the unchanged
shortcut verifier on its dyadically saturated lift.  Both report `m_h` and
the displayed image as the closure counterexample in all 69 cases.

## Frozen `q=71` audit

The audit strictly loads:

- 213 normalized implications translated from
  `results/spine-q72-gate0-bank.json`; and
- 11 locally learned implications from
  `results/odd-suffix-q71-gate2-seeded-scout.json`.

Their 224 antecedents have 2,170 length-71 factor occurrences and 1,692
distinct factors: 1,662 occur in the imported bank and 30 in the local bank.
For comparison only, their terminal length-71 windows have 195 distinct
values (187 imported and 8 local).  Terminal counts are not used in the
proof.

Direct evaluation finds zero active frozen antecedents on every distinguished
`R_h`.  The audit then generates the 69 exact implications

$$
A(p_h)\Longrightarrow A(U(m_h)\text{ with its low marker removed}).
$$

All implication pairs are distinct and absent from the frozen implication
ledger.  One targeted antecedent already occurs as an interior factor of a
longer frozen antecedent, so adjoining all 69 raises the distinct factor count
from 1,692 to 1,760 rather than 1,761.

Finally, for every gate the constructive pigeonhole search selects a pattern
absent from all 1,760 factors.  Direct DFA evaluation confirms that its
`R_(h,c)` activates none of the 224 frozen antecedents and none of the 69 new
antecedents.  All 69 selected machines satisfy every normal-form check.  They
are classified only as finite-clause evasion witnesses; their exact closure
is not asserted.

`reset_spine.py` performs the audit without Z3, emits deterministic strict
JSON with a canonical semantic SHA-256 digest, and supports strict
recomputation through `--validate`.  The committed artifact
`results/reset-spine-q71-bank-blind-spot.json` freezes this audit.  Its semantic
SHA-256 is
`7851e9d0888e20e631206e66e2b373f69df3fb31f7bf45aeb92a04847d293e16`;
its formatted-file SHA-256 is
`3c32409080649bd02cf7ce1dd090e3e16dd1ac1ce958d8accc5d777354590dcd`.

## Dependency audit

- D-9101 supplies canonical LSD-first word semantics.
- L-9101 supplies the exact shortcut transducer used by unchanged lift
  verification.
- L-9102 supplies exact regular-language closure checking.
- L-9106 supplies the odd-core map and the suffix-to-shortcut lift.
- L-9111 supplies the equality-case syntax checked item by item.
- The exponential factor lemma itself is elementary and does not depend on
  the external verified Collatz range used to derive L-9111.

## Gap audit

- Factor occurrence is necessary, not sufficient, for an antecedent to be
  accepted.  The factor count deliberately overestimates concrete-bank
  coverage, so the lower bound remains valid but is not tight.
- The theorem concerns clauses whose guards are concrete accepted suffixes.
  A symbolic transition-cube clause can exclude many or all reset patterns at
  once and is not subject to the factor-count bound.
- A direct arithmetic contradiction can likewise eliminate a gate without
  covering this family antecedent by antecedent; this is not a lower bound on
  proof complexity.
- The theorem says the finite clauses do not eliminate a gate under the
  L-9111 syntax.  It does not say that an arbitrary reset-pattern witness is a
  sanctuary.
- The 69 distinguished reset spines are known **not** to be sanctuaries; their
  value is that they expose a bank blind spot and supply exact missing clauses.
- Counts and hashes in the scientific audit are tied to the two named frozen
  artifacts.  The validator rejects silent artifact drift.

## Adversarial tests

- Exhaustive enumeration for every pattern at `q=3,...,7` checks the complete
  L-9111 syntax, rejects every canonical word shorter than `q`, and verifies
  the required-factor conclusion on every accepted canonical word through
  length `q+3`.
- The accepted `q=3` word `1011` prevents regression to the false
  terminal-window statement.
- Gates `h=2` and `h=q-1`, malformed patterns, booleans masquerading as
  integers, and the exact `m_h`/`U(m_h)` formulas are tested explicitly.
- The scientific test freezes factor and terminal-window counts, checks all
  69 exact verifier records and all 69 augmented-bank evasions, and patches
  both optional Z3 entry points to fail if called.
- Strict-JSON tests reject NaN, extra root fields, digest tampering, and
  semantic tampering even when an attacker recomputes the displayed digest.

## Suggested next attack

Concrete counterexample accumulation is structurally mismatched to this
family.  The next useful clauses should be symbolic **transition-cube
nogoods**: extract a small partial assignment of DFA transitions sufficient
for an exact closure failure, minimize that cube, and block every completion
of it at once.  The reset-pattern family is a controlled benchmark for that
learner: a successful symbolic clause should cover exponentially many `c`
patterns while remaining independently checkable against an exact transducer
witness.
