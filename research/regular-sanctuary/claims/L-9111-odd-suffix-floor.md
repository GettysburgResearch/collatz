# L-9111 - Conditional 71-state odd-suffix normal form

- **Claim ID:** L-9111
- **Title:** A fully accelerated odd sanctuary needs at least 71 suffix states, with a complete spine at equality
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101, L-9104, L-9106, L-9109, and the external verification below `2^71`
- **Scope:** complete DFAs reading the suffix after the forced low odd bit
- **Related counterexample candidates:** none

## Statement

Let a complete `p`-state DFA `A` read **odd suffixes**: an odd canonical
LSD-first word is written uniquely as `1x`, and `A` reads only `x`.  Define

$$
O_A=\{[1x]: 1x\text{ is canonical and }A\text{ accepts }x\}.
$$

Assume the external premise that every positive integer below `2^71` reaches
the shortcut cycle `{1,2}`.  If `O_A` is nonempty, excludes `1`, and satisfies

$$
U(O_A)\subseteq O_A,
$$

then `p>=71`.

If `p=71`, let `m` be the least member of `O_A`.  Its full word has length 72
and its suffix has the form

$$
x=c_0c_1\cdots c_{69}1
$$

of length 71.  Number the suffix-prefix states

$$
r_i=\delta_A(r_0,c_0\cdots c_{i-1}),
\qquad 0\leq i\leq70,
$$

where `r_0` is the start state.  Then:

1. `c_0=1`, `delta_A(r_0,1)=r_1`, and
   `delta_A(r_0,0)!=r_1`;
2. `r_0,...,r_70` are distinct and exhaust all 71 states;
3. `r_i` has graph distance exactly `i` from `r_0`, so every transition from
   `r_i` targets some `r_j` with `j<=i+1`, and the suffix-spine transition
   labeled `c_i` advances to `r_(i+1)` for `i<70`;
4. the final `1` reaches an accepting gate
   `a=delta_A(r_70,1)=r_h` with `2<=h<=70`;
5. after deleting accepting states with no odd-canonical preimage, `{a}` is a
   semantics-preserving accepting set, and
   `delta_A(r_i,1)!=a` for every `i<70`;
6. the spine label entering the gate is zero: `c_(h-1)=0`.

These conditions are necessary, not sufficient, for odd-core invariance.

## Definitions

The suffix domain is

$$
\mathcal C_{\mathrm{suf}}=\{\epsilon\}\cup\{0,1\}^*1.
$$

The empty suffix represents the odd integer `1`.  Thus odd-core safety is
exactly the requirement that the start state of `A` is not accepting.
A state has an **odd-canonical preimage** when it is reached from `r_0` by
some $x\in\mathcal C_{\mathrm{suf}}$.

From `A`, form its **shortcut lift** `D_A` by adjoining one state `s` and
setting

$$
\delta(s,0)=s,
\qquad
\delta(s,1)=r_0,
$$

while every transition inside the copy of `A` is unchanged.  Only states in
the copy of `A` may accept.  The lift reads an arbitrary low zero run, consumes
the first `1` as the oddness marker, and then gives the remaining suffix to
`A`.

## Motivation

The original exact-floor solver uses 72 raw shortcut states and partitions on
its accepting gate.  The suffix representation removes the forced dyadic-
saturation state before synthesis.  Within this structured lift, the viable
nonzero gate partitions shift from shortcut indices `3,...,71` to suffix
indices `2,...,70`.  The existing shortcut gate-0 partition remains a separate
search because its accepting gate is the added saturation state and cannot
occur in this 71-state suffix lift.

## Proof or construction

The lifted DFA `D_A` has `p+1` raw states and, under D-9101 canonical
semantics, its semantic language is exactly the canonical encoding of

$$
\operatorname{Sat}_2(O_A)=\{2^k n:k\geq0,\ n\in O_A\}.
$$

Indeed, every canonical input has the unique form `0^k 1x`; the new state
skips `0^k`, consumes the first `1`, and `A` accepts precisely when it accepts
`x`.  The canonical word language of `O_A` is
$1(L(A)\cap\mathcal C_{\mathrm{suf}})$, hence is regular.  By L-9106, the
hypotheses on `O_A` make this lift a shortcut sanctuary.

L-9104 together with the verified-range premise forces every raw shortcut
sanctuary DFA to have at least 72 states.  Therefore

$$
p+1\geq72,
$$

which proves `p>=71`.

Now take `p=71`.  Since `2^k n >= n`, the least member of
`Sat_2(O_A)` is the least member `m` of `O_A`.  The lift has exactly 72 states,
so L-9109 applies with no slack.  Its least accepted word has length 72 and
begins `11`.  The first `1` moves from the added state `s` to the suffix start
`r_0`; the remaining 71-symbol suffix is therefore `x=c_0...c_69 1`, with
`c_0=1`.

L-9109's 72 distinct prefix states consist of `s` followed by the 71 states
`r_0,...,r_70`.  They exhaust the lift, hence the suffix states are distinct
and exhaust `A`.  If a word shorter than `i` reached `r_i` from `r_0`, prefixing
the consumed oddness marker `1` would reach the corresponding lifted state in
fewer than `i+1` steps, contradicting L-9109's exact distance.  Thus suffix
distances are exactly `0,...,70`, which gives the upper-Hessenberg transition
bound and spine advances.

The initial `11` in the full word makes `delta_A(r_0,1)=r_1`.  L-9109's
competing-edge restriction at the second full-word state gives
`delta_A(r_0,0)!=r_1`.

The accepting gate of the lift cannot be `s`, because the lift's accepting set
contains only suffix states.  In L-9109's indexing, `q_0=s` and
`q_(i+1)=r_i`.  Write the gate as `a=r_h`, so its lifted index is `g=h+1`.
L-9109 forbids the first lifted `1` transition `s -> r_0` and the next
transition `r_0 -> r_1` from landing at the accepting gate.  Hence `h` is
neither zero nor one, so `2<=h<=70`.  Translating the remaining singleton-gate
conclusion gives `delta_A(r_i,1)!=a` for `i<70` and permits deletion of every
other accepting state with no odd-canonical preimage.  Finally, L-9109 says
the spine label entering an accepting spine state is zero.  Here
`b_(g-1)=b_h=c_(h-1)`, proving the last assertion.

## Dependency audit

- D-9101 fixes LSD-first canonical semantics.
- L-9104 supplies the conditional 72-state raw-DFA floor.
- L-9106 proves that the dyadic saturation of a safe `U`-invariant odd
  language is a shortcut sanctuary.
- L-9109 supplies the exact 72-state lifted normal form.
- The numeric floors 71 and 72 are conditional on the external verification
  below `2^71`; citation admission remains pending issue #7.

## Gap audit

- This result concerns the suffix representation, not every possible DFA for
  the same odd language.  A nonminimal representation may use more states.
- A 71-state suffix lift can realize only shortcut gates `3,...,71` after the
  index shift.  It does not represent every raw 72-state machine in those
  partitions: a generic shortcut normal form may send work-state transitions
  back to the saturation state, whereas the suffix lift keeps every such
  transition inside its copy of `A`.
- Shortcut gate 0 can return from the odd machine to the saturation state and
  is not representable by a 71-state suffix lift.
- Above 71 suffix states, exhaustion, exact distances, and the full normal form
  need not hold.
- The theorem gives only necessary syntax.  Exact `U` closure and final lifted
  shortcut verification are still mandatory.

## Adversarial tests

- Allowing suffix gate `h=0` would accept the empty suffix, hence the forbidden
  odd integer `1`.
- Allowing `h=1` conflicts with the forced first suffix transition
  `delta_A(r_0,1)=r_1` and would accept the two-bit full word `11`.
- Consuming the first odd bit inside `A` instead of in the added saturation
  state changes the state accounting; the theorem deliberately uses suffix
  semantics to make the `71+1` lift exact.
- The gate-0 shortcut partition is explicitly retained rather than silently
  claimed to be covered.

## Remaining uncertainty

The reduction appears complete, conditional on L-9109 and the verified range.
No 71-state suffix candidate is known.

## Suggested next attack

L-9113 shows that antecedent-by-antecedent concrete-bank coverage is
exponentially mismatched to reset-pattern spines, while L-9114 eliminates gate
2 by a direct carry argument.  Continue gates `3,...,70` with symbolic
transition-cube nogoods or iterated minimum-word image constraints.  Lift every
proposal to the unchanged shortcut verifier, and revalidate every reusable
arithmetic implication against the exact fully accelerated odd map.
