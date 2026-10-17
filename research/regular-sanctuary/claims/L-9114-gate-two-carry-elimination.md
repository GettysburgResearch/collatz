# L-9114 - Gate-two carry elimination

- **Claim ID:** L-9114
- **Title:** The accepting gate cannot be the second suffix-spine state
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** independent carry reconstruction by `structured_templates`; artifact audit by `artifact_audit`
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101 and the syntactic normal form stated in L-9111
- **Scope:** complete odd-suffix DFAs with the exact-distance spine constraints
- **Related counterexample candidates:** none

## Statement

Let `q>=3`, and let a complete `q`-state suffix DFA have states
`r_0,...,r_(q-1)`, start state `r_0`, and singleton accepting gate `r_h`.
Assume the following normal-form conditions:

1. every transition from `r_i`, for `i<q-1`, targets some `r_j` with
   `j<=i+1`, and at least one input bit advances to `r_(i+1)`;
2. `delta(r_i,1)!=r_h` for every `i<q-1`;
3. `delta(r_0,1)=r_1` and `delta(r_0,0)!=r_1`;
4. `delta(r_(q-1),1)=r_h`;
5. the represented odd language is invariant under the fully accelerated map
   `U`.

Then `h!=2`.

Consequently, conditional on L-9111 and its external verified-range premise,
the 71-state suffix search needs only gates `3,...,70`.  Under the unchanged
one-state dyadic lift, this excludes structured shortcut gate 3.  It does not
exclude generic raw 72-state shortcut gate 3, whose work transitions may
return to the added saturation state.

## The 1-preferred shortest spine word

For every `0<=i<q-1`, choose

$$
c_i=
\begin{cases}
1,&\delta(r_i,1)=r_{i+1},\\
0,&\text{otherwise}.
\end{cases}
$$

At least one input advances, so the chosen bit always advances.  Therefore

$$
x=c_0c_1\cdots c_{q-2}1
$$

is an accepted canonical suffix of length `q`.  This word is
**minimum-length**, but it need not represent the numerically least accepted
integer when both bits advance at some state.  Closure applies to it anyway.

Write the full odd input as `1x` and its integer value as `m`.  In full-word
bit positions,

$$
m_0=1,\qquad m_{i+1}=c_i,\qquad m_q=1.
$$

Suppose for contradiction that `h=2`.  The forced initial edge gives `c_0=1`.
At `r_1`, the one-edge cannot enter the gate, while some edge must advance to
`r_2`; hence `c_1=0`.

Thus `m` is 3 modulo 8.  In particular `v_2(3m+1)=1` and

$$
U(m)=\frac{3m+1}{2}=m+\frac{m+1}{2}.
$$

## Length and distance dichotomy

The input has full length `q+1`, and `m<U(m)<2^(q+2)`.  Hence the full output
has length `q+1` or `q+2`.  Its low bits are

$$
U(m)_0U(m)_1=10
$$

in LSD-first order.

If the output has full length `q+1`, its suffix has length `q`.  Before its
final canonical one, all `q-1` transitions must advance in order to cover
distance `q-1`.  Its first suffix bit is zero, but
`delta(r_0,0)!=r_1`; contradiction.

Suppose instead that the output has full length `q+2`.  Its suffix has length
`q+1`, so its `q` preterminal transitions must cover distance `q-1`.  Since
each transition advances by at most one, exactly one transition stalls and
all others advance; no backward transition is possible.  The first suffix bit
is zero and sends `r_0` to `r_0`, so this is the unique stall.  Consequently
the output bits `U(m)_2,...,U(m)_q` must advance successively from
`r_0,...,r_(q-2)`.

## Carry induction

Put `t=(m+1)/2`.  From `c_0=1,c_1=0`, the bits of `t` begin

$$
t_0=0,\qquad t_1=1,
$$

and, before the fixed high bit,

$$
t_j=c_j\quad(2\le j\le q-2),\qquad t_{q-1}=1.
$$

Now add `U(m)=m+t` column by column.

At column 1, `1+1` produces output bit zero and a carry into column 2.  At
column 2 the summands are `c_1=0`, `c_2`, and that carry.  The output bit
`U(m)_2` must be one to advance from `r_0`; therefore `c_2=0` and the next
carry is zero.  (When `q=3`, the fixed high bit occurs here and instead makes
`U(m)_2=0`, an immediate contradiction.)

When `q=4`, column 3 is already the fixed high-bit column: it gives output bit
one, which would have to advance from `r_1` even though `c_1=0`; this is an
immediate contradiction.

For `q>=5`, column 3 instead gives

$$
U(m)_3=c_3.
$$

This bit must advance from `r_1`; only zero can enter the gate `r_2`, so
`c_3=0`.  Inductively, with zero carry and all preceding `c` bits zero, column
`j` gives

$$
U(m)_j=c_j.
$$

It must advance from `r_(j-2)`, while `c_(j-2)=0` means that the one-edge at
that state does not advance.  Hence `U(m)_j=0` and `c_j=0`.  This forces every
`c_i=0` for `2<=i<=q-2`.

At column `q-1`, however, the fixed high bit of `t` gives

$$
U(m)_{q-1}=1
$$

with zero carry.  This bit must advance from `r_(q-3)`, but
`c_(q-3)=0` says precisely that its one-edge does not advance.  This final
contradiction proves `h!=2`.

## Independent computational reconstruction

The companion experiment `symbolic_minimum.py` encodes the same argument as a
Boolean ripple-carry circuit and a local distance-budget path constraint.  It
does not use a monolithic bit-vector multiplication or a symbolic dynamic
array walk.

- full transition-table enumeration for `q=3,...,8` found zero gate-2 models
  accepting the chosen image;
- a weaker bit-pattern enumeration through `q=21` also found zero;
- at `q=71`, the local symbolic constraint is solver-UNSAT for gate 2 and SAT
  for every gate `3,...,70`;
- every SAT model is reconstructed and its chosen input/image acceptance is
  rechecked with ordinary exact arithmetic.

The solver observation is corroboration only.  The proof above is the claimed
reason gate 2 is impossible.

The committed q=71 artifact
`results/symbolic-minimum-q71-gates2-70.json` records the one gate-2
solver-UNSAT constraint and 68 satisfiable countermodels for gates 3 through
70.  Every satisfiable model is exactly rejected by both odd-core and shortcut-
lift verification; no candidate is reported.  Its payload SHA-256 is
`8273c8a3b3879c242323c8467d431f4f2713b46a596d47f9d2a753362c74a3b3`;
its formatted-file SHA-256 is
`5f6ed1ec31d890082819026c28634786072673060cc0275fc6a31bb9537eab57`.
Solver UNSAT remains corroboration only; the carry induction is the proof.

## Gap and dependency audit

- The result assumes the exact-distance suffix-spine syntax.  It is not a
  theorem about arbitrary 71-state DFAs, larger suffix DFAs, or generic raw
  shortcut machines.
- Its use at `q=71` inherits L-9111's dependence on the external verification
  below `2^71`.  The carry lemma itself is valid for every `q>=3` once the
  stated syntax is assumed.
- The selected word is 1-preferred and minimum-length, not necessarily the
  least accepted integer.  No numerical minimality is used.
- SAT for gates `3,...,70` proves only that this one necessary constraint is
  consistent.  The exact verifier rejects the frozen SAT models; none is a
  sanctuary candidate.

## Suggested next attack

Apply the same distance-budget method to the first two or three `U` images of
the chosen spine word.  The first image has only an all-advance/one-stall
dichotomy; iterating this symbolic orbit may eliminate additional low gates
without the exponential blind spot of concrete word clauses.
