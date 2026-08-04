# L-9109 - Conditional exact-floor normal form

- **Claim ID:** L-9109
- **Title:** A 72-state sanctuary at the verified-range floor has a full spine, accepting gate, and start-state zero loop
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101, L-9104, L-9106, and the external verification below `2^71`
- **Scope:** complete raw DFAs with exactly 72 states under the conditional verified-range premise
- **Related counterexample candidates:** none

## Statement

Assume the external premise

> every positive integer below `2^71` reaches the shortcut cycle `{1,2}`.

Let a complete raw DFA `D` have exactly 72 states, and suppose its semantic
language `L_D` is a nonempty shortcut sanctuary.  Let `m` be the least integer
in `L_D`, with canonical LSD-first word

$$
w=b_0b_1\cdots b_{70}1.
$$

Then all of the following are necessary:

1. `w` has length exactly 72 and begins in `11`, so `b_0=b_1=1`;
2. the 72 prefix states
   `q_i=delta(q_0,b_0...b_(i-1))`, for `0 <= i <= 71`, are distinct and
   exhaust the DFA state set;
3. `q_i` has graph distance exactly `i` from `q_0`; consequently every edge
   from `q_i` goes to some `q_j` with `j<=i+1`, and for `i<=70` the spine edge
   labeled `b_i` advances to `q_(i+1)`;
4. the final `1` is an accepting gate
   `a=delta(q_71,1)=q_g in F` for some `0 <= g <= 71`; every accepting state
   having a canonical preimage equals `a`, so replacing the raw accepting set
   by `{a}` preserves the semantic language, and `delta(q_i,1)!=a` for every
   `i<71`;
5. the start state has a forced zero loop, `delta(q_0,0)=q_0`, while
   `delta(q_0,1)=q_1`, `delta(q_1,1)=q_2`, and `delta(q_1,0)!=q_2`;
6. consequently `L_D=0* O`, where `O` is its regular odd core.

Moreover, if a spine state `q_i` is accepting and `i>=1`, then its incoming
spine label `b_(i-1)` must be zero.  In particular, if `g>=1`, then
`b_(g-1)=0`.

## Definitions

The 71 transitions labeled `b_0,...,b_70` form the **spine**.  The final
transition labeled `1` returns to one of the already exhausted states and is
the **gate**.  The zero loop is on the raw start state and acts before any
least-significant nonzero digit is read.

## Motivation

L-9104 gives only a numerical state floor.  At equality, the proof has no
slack: a shortest accepted prefix must visit every state.  Closure then forces
additional syntax that can be built directly into any exact-floor SAT or CEGIS
search.

## Proof or construction

By L-9104, `D` accepts a canonical word of length at most 72.  The verified-
range premise and sanctuary closure forbid every accepted word of length at
most 71.  Hence the least member `m` has bit length exactly 72.

The least member is odd.  Otherwise `T(m)=m/2` would be a smaller member of
`L_D`.  Put `alpha=nu_2(3m+1)`.  Since `m` is odd, `alpha>=1`, and L-9106's
odd iterate

$$
U(m)=\frac{3m+1}{2^{\alpha}}=T^{\alpha}(m)
$$

also lies in `L_D`.  If `alpha>=2`, then, because `m>1`,

$$
U(m)\leq\frac{3m+1}{4}<m,
$$

contradicting minimality.  Thus `alpha=1`, equivalently `m=3 modulo 4`.  Its two
least significant bits are therefore `11`.

Now consider the prefix states `q_0,...,q_71`.  If `q_i=q_j` for some
`0<=i<j<=71`, deleting the intervening input block and retaining the final
`1` gives a shorter canonical word with the same accepting endpoint.  This is
impossible.  The 72 prefix states are distinct and, because `D` has exactly 72
states, exhaust its state set.  The final symbol is `1`, and its target must be
an accepting state; exhaustion names it `a=q_g` for some `g`.

The graph distance from `q_0` to `q_i` is at most `i` along the spine.  If a
word `u` of length less than `i` reached `q_i`, then

$$
ub_ib_{i+1}\cdots b_{70}1
$$

would be canonical, accepted, and shorter than 72 bits.  Thus the distance is
exactly `i`.  If either labeled edge from `q_i` targets `q_j`, the path through
`q_i` gives `j<=i+1`.  For `i<=70`, the edge labeled `b_i` is the displayed
spine edge to `q_(i+1)`.

Next let `f in F` have any canonical preimage `v1`.  The state reached after
`v` is some `q_i`.  Replacing `v` by the length-`i` spine path to `q_i` gives
the accepted canonical word

$$
b_0b_1\cdots b_{i-1}1
$$

of length `i+1<=72`.  No accepted canonical word is shorter than 72, so
`i=71` and `f=delta(q_71,1)=a`.  Every semantically relevant accepting state
is therefore `a`; raw accepting states with no canonical preimage can be
deleted, making `{a}` a semantics-preserving singleton acceptor.  The same
argument directly gives `delta(q_i,1)!=a` for every `i<71`.

It remains to determine the start-state zero transition.  Exhaustion gives
`delta(q_0,0)=q_j` for some `j`.  If `j>=1`, the canonical word

$$
z=0b_jb_{j+1}\cdots b_{70}1
$$

follows the suffix of the spine and the accepting gate, so `z in L_D`.
Because its low bit is zero, shortcut closure also accepts

$$
b_jb_{j+1}\cdots b_{70}1,
$$

a canonical word of length `72-j <= 71`.  This contradicts the verified-range
premise.  Hence `j=0` and `delta(q_0,0)=q_0`.

Because `b_0=b_1=1`, the first two spine edges explicitly give
`delta(q_0,1)=q_1` and `delta(q_1,1)=q_2`.  If
`delta(q_1,0)=q_2`, replacing the second low bit of `w` by zero would make

$$
10b_2b_3\cdots b_{70}1
$$

another accepted 72-bit canonical word.  Its value is `m-2`, contradicting
the choice of `m` as the least accepted integer.  Thus
`delta(q_1,0)!=q_2`.

The zero loop means that adding or deleting any initial run of LSD-first zeros
does not change acceptance.  Every canonical word is a zero run followed by
an odd canonical word, proving `L_D=0* O`.

Finally, if `q_i in F`, `i>=1`, and `b_(i-1)=1`, then the length-`i` prefix of
`w` is itself canonical and accepted, again too short.  This proves the stated
accepting-state restriction.

## Dependency audit

- D-9101 fixes the raw-state count and semantic canonicalization.
- L-9104 supplies an accepted word of length at most the state count.
- L-9106 identifies the odd iterate `U(m)` inside a shortcut sanctuary.
- The number 72 and every contradiction involving length at most 71 are
  conditional on the strict `n<2^71` premise audited in L-9104 from Barina's
  contribution statement and Section 6:
  https://doi.org/10.1007/s11227-025-07337-0.
- Citation admission remains pending issue #7.

## Gap audit

- The theorem is conditional and applies only at the exact 72-state floor.
  With 73 or more states, the spine need not exhaust the machine and the zero
  loop is not forced by this argument.
- `11` is proved for the least integer in the language, not for every accepted
  word.
- The normal form is necessary, not sufficient: it does not by itself prove
  nonemptiness, safety, or closure.
- Raw accepting states with no canonical preimage may exist, but removing them
  preserves the semantic language.  The singleton acceptor is this
  semantics-preserving normalization, not a claim that the input file's raw
  accepting mask was already singleton.

## Adversarial tests

- Allowing the start-state zero edge to enter `q_1` would accept a shifted
  spine word whose shortcut image has length 71; this catches the boundary
  case where the newly constructed even word still has length 72.
- The inequality `(3m+1)/4<m` needs `m>1`, supplied by sanctuary safety.
- The final gate target need not be the start state; only state exhaustion and
  acceptance are forced.
- A shortcut-length argument alone does not exclude `delta(q_1,0)=q_2`; the
  strict numerical comparison with the least member is needed.

## Remaining uncertainty

The structural proof appears complete, conditional on the verified range.
No 72-state candidate satisfying even these necessary conditions is known.

## Suggested next attack

Resume the implemented exact-floor CEGIS search across gate partitions
`0,3,...,71`, preserving every exact learned implication and returning every
proposed table to the existing closure relation without weakening its
certificate obligations.  Gates 1 and 2 are inconsistent with the forced
initial `11` transitions.
