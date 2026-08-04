# T-8802 — Exact `5x+1` `4 -> 5` chart and completion formula

Claim ID: T-8802  
Title: Two-phase expanding control chart for the shortcut `5x+1` map  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-8801, L-8801  
Scope: the partial map `H=T_5^2` on residues `2,3 mod 4`  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

For every integer `q>=1`, the shortcut `5x+1` map satisfies

```text
T_5^2(4q-1) = 5q-1,   parity word 10,
T_5^2(4q-2) = 5q-2,   parity word 01.
```

Thus the partial two-step map `H=T_5^2` has two exact same-phase expanding
branches with source radix `4`, target radix `5`, and phases `-1,-2`.

For every `m>=1`, `q>=1`, and `c in {1,2}`, these branches stack to the finite
tower identity

```text
H^m(4^m*q-c) = 5^m*q-c.
```

Now suppose a positive ordinary integer `A=A_0` remains in these two branches
for every `H`-iterate. For each `j`, write its phase as

```text
A_j = 4q_j+d_j,   d_j in {-2,-1},
eps_j = d_j+2 in {0,1}.
```

Then in `Z_2`,

```text
A+2 = Phi_(4,5)(eps)
    = (1/5)*sum_(j>=0) eps_j*(4/5)^j.
```

Conversely, every binary directive has a unique `2`-adic completion given by
this formula; its successive `H`-states have the prescribed phases. This does
not imply that the completion is a positive ordinary integer.

In particular, the two constant directives complete to

```text
eps=111...  -> A=-1,
eps=000...  -> A=-2.
```

Therefore a tower that uses only one phase forever cannot be a positive
ordinary `5x+1` counterexample.

## Definitions

- `H` is only applied when its current input is congruent to `-1` or `-2`
  modulo `4`.
- A directive completion is taken in `Z_2`; ordinary positivity is an additional
  global requirement.
- `Phi_(4,5)` is defined in D-8801.

## Motivation

This is a rigorous positive-drift control object. It is simpler than the
repository’s `64 -> 81` charts but exhibits the same central difficulty:
finite expanding towers are easy, while an infinite symbolic directive must
complete to one positive ordinary integer. Any proposed certificate mechanism
that cannot handle this control chart is failing at the level of representation
or completion, not because `5x+1` lacks expansion.

## Proof or construction

For the phase `-1`,

```text
4q-1 -> (5(4q-1)+1)/2 = 10q-2 -> 5q-1.
```

The parities are `1,0`. For the phase `-2`,

```text
4q-2 -> 2q-1 -> (5(2q-1)+1)/2 = 5q-2,
```

with parities `0,1`.

For the finite tower, induct on `m`. More explicitly, after `k` applications,

```text
H^k(4^m*q-c)=5^k*4^(m-k)*q-c
```

for `0<=k<=m`. Before the last application the coefficient of `q` remains
divisible by `4`, so the same phase identity applies. Setting `k=m` gives the
tower formula.

For an infinite chart orbit,

```text
A_j=4q_j+d_j,
A_(j+1)=5q_j+d_j.
```

Eliminating `q_j` gives

```text
A_j = (4/5)A_(j+1) + d_j/5.
```

Iteration through depth `N` yields

```text
A_0
 = (4/5)^N A_N
   + (1/5)*sum_(j=0)^(N-1) d_j*(4/5)^j.
```

Because every `A_N` is an integer,

```text
v_2((4/5)^N A_N) >= 2N -> infinity.
```

The tail term vanishes in `Q_2`, and hence

```text
A
 = (1/5)*sum_(j>=0) d_j*(4/5)^j
 = (1/5)*sum_(j>=0) eps_j*(4/5)^j
   - (2/5)*sum_(j>=0)(4/5)^j
 = Phi_(4,5)(eps)-2,
```

because the geometric sum is `5` in `Q_2`.

For the converse, let the displayed series define `A_0`, and define `A_j` by
shifting the directive. Modulo `4`, the tail after `d_j` vanishes and `5` is a
unit congruent to `1`, so `A_j congruent d_j (mod 4)`. The branch formula then
maps `A_j` to `A_(j+1)`. Uniqueness follows because two completions agreeing on
the first `N` phases are congruent modulo `4^N` for all `N`.

Finally, the all-one normalization gives `Phi_(4,5)(111...)=1`, hence `A=-1`;
the all-zero series gives `A=-2`. **QED**

## Dependency audit

- D-8801 supplies `T_5`, same-phase terminology, and `Phi_(4,5)`.
- L-8801 provides an independent affine check, though the two branch identities
  are also derived directly here.
- No probabilistic claim about `5x+1` is used.

## Gap audit

- The theorem is a partial chart, not a statement that every `5x+1` orbit enters
  it or remains there.
- Every infinite directive has a `2`-adic completion, but most completions need
  not be ordinary integers, positive, or dynamically relevant outside `Z_2`.
- Each finite tower has a positive starting integer; compatibility of all
  finite towers instead selects the negative completions for constant phases.
- Expansion of the quotient `q -> (5/4)q` does not overcome completion failure.
- No divergent positive seed is claimed.

## Adversarial tests

X-8801 checks both identities for every `1<=q<=100,000`, totaling 200,000
physical replays. It also derives the same two phases by an exhaustive
same-phase word census at length `2`, weight `1`.

The same census finds no literal length-`6`, weight-`4` fixed phase at `a=5`:
`5^4-2^6=561` divides none of the fifteen affine corrections. This is an
arithmetic chart-realization failure, not a convergence result.

## Remaining uncertainty

The exact identities and completion formula appear complete. The unresolved
problem is whether a nonconstant directive, together with finite connectors,
can replenish enough dyadic precision to select a positive ordinary integer.

## Suggested next attack

Search for a finite connector automaton between phases `-1` and `-2` with
positive net fuel balance. The control chart is small enough that a complete
PDR/SAT or residue-cylinder analysis may be possible.
