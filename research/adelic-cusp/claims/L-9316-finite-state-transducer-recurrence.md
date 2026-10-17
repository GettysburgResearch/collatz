# L-9316 — Finite-state transducer recurrence transfer

**Claim ID:** L-9316  
**Title:** Small non-erasing sequential transducers cannot hide the efficient Thue--Morse recurrences  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `T-9316`  
**Scope:** stateful source-to-native transfer for Thue--Morse-related extremal sign encodings  
**Related counterexample candidates:** none

## 1. Transducer model

Let

\[
\mathcal T=(S,s_0,\Delta,\Lambda)
\]

be a deterministic sequential transducer with:

- finite state set `S`, of size
  \[
  Q=|S|\ge1;
  \]
- binary input alphabet;
- binary output alphabet;
- transition map
  \[
  \Delta:S\times\{0,1\}\to S;
  \]
- nonempty transition output
  \[
  \Lambda:S\times\{0,1\}\to\{0,1\}^+.
  \]

Assume constants

\[
1\le a\le b
\tag{1}
\]

satisfy

\[
a\le|\Lambda(s,c)|\le b
\qquad(s\in S,\ c\in\{0,1\}).
\tag{2}
\]

A fixed finite initial output word is allowed; it contributes only an additive constant to output positions.

Let `T(v)` be the infinite output generated from an infinite input word `v`.

## 2. Thue--Morse block supply

Let `tau` be the Thue--Morse word, fixed by

```text
mu(0)=01,
mu(1)=10.
```

For every `m>=0`, put

\[
L=2^m.
\tag{3}
\]

Because

\[
\tau=\mu^m(\tau),
\tag{4}
\]

every index `j` with `tau_j=1` supplies the same input block

\[
\mu^m(1)
\tag{5}
\]

of length `L`, beginning at input position `jL`.

Among the indices

\[
0,1,\ldots,2Q+1
\tag{6}
\]

there are exactly `Q+1` values with `tau_j=1`. Indeed, every pair

\[
(\tau_{2k},\tau_{2k+1})
\]

contains one zero and one one.

The same statement holds for the complemented Thue--Morse word after replacing the common block in `(5)` by its bitwise complement.

## 3. State synchronization

Fix a finite shift `sigma^s tau` or `sigma^s overline(tau)`. For every sufficiently large `m` with `L>s`, the `Q+1` common blocks above begin in the shifted input at positions

\[
jL-s,
\tag{7}
\]

where `tau_j=1` and `0<=j<=2Q+1`.

Record the transducer state immediately before each such block. There are `Q+1` block starts but only `Q` states. Hence two block starts

\[
r_m<t_m
\tag{8}
\]

enter the same transducer state.

Because the input blocks are identical and the transducer is deterministic, the emitted output factors are identical.

Let their common output length be `ell_m`, and let the second output start be `T_m`. Bounds `(2)` give

\[
\boxed{
\ell_m\ge aL,
\qquad
T_m\le c_0+b(2Q+1)L,
}
\tag{9}
\]

where `c_0` is the fixed initial-output length.

## 4. Ordinary recurrence obstruction

Put

\[
\delta=\log_{64}(81/64).
\tag{10}
\]

Equation `(9)` gives

\[
\ell_m-\delta T_m
\ge
\left(a-\delta b(2Q+1)\right)L-\delta c_0.
\tag{11}
\]

Therefore, if

\[
\boxed{
a>\delta b(2Q+1),}
\tag{12}
\]

then

\[
\ell_m-\delta T_m\longrightarrow+\infty.
\tag{13}
\]

By `T-9316`, the output itinerary cannot be a nontrivial ordinary `64 -> 81` survivor and its appended nearest-integer cylinder blocks cannot be eventually zero.

Equivalently, the sufficient distortion condition is

\[
\boxed{
\frac ba
<
\frac1{(2Q+1)\log_{64}(81/64)}.
}
\tag{14}
\]

## 5. Letter-to-letter corollary

For a letter-to-letter transducer,

\[
a=b=1.
\]

Condition `(12)` becomes

\[
(2Q+1)\delta<1.
\tag{15}
\]

Since

\[
\frac1\delta
=17.6548475770\ldots,
\tag{16}
\]

condition `(15)` holds for every

\[
\boxed{Q\le8.}
\tag{17}
\]

Thus:

\[
\boxed{
\text{No output of an at-most-eight-state deterministic letter-to-letter}
\text{ transducer on a shifted/complemented Thue--Morse input}
\text{ can stabilize as an ordinary survivor itinerary.}
}
\tag{18}
\]

This includes stateful sign conventions that are not one-letter morphisms.

## 6. Comparison with the morphic bound

For a one-state transducer, `(14)` gives

\[
\frac ba<\frac1{3\delta}.
\]

`L-9315` is stronger for a true morphism, giving

\[
\frac ba<\frac1{2\delta},
\]

because a morphism does not need the state-pigeonhole step and can use the earliest adjacent equal blocks directly.

The two lemmas therefore cover different source descriptions:

- `L-9315`: arbitrary-state-free non-erasing morphisms, with the sharper distortion margin;
- `L-9316`: genuinely stateful sequential encodings, with an explicit state/distortion tradeoff.

## 7. General synchronized-block form

The proof uses only the following abstract data:

1. at scale `L_j`, at least `Q+1` identical input factors of length `L_j` occur before position `C L_j+O(1)`;
2. a `Q`-state deterministic non-erasing transducer emits between `a` and `b` symbols per input symbol.

Then two factors enter the same state, and the output is excluded whenever

\[
\boxed{
\delta C\frac ba<1.
}
\tag{19}
\]

This is the natural finite-state extension of the bounded-distortion morphic criterion.

## 8. Literature interface

The wave-5 literature audit requires the exact Dubickas extremal sign convention to be translated into native digits and appended blocks.

If the full source presents the extremal language as a sequential image of Thue--Morse, the audit is now finite:

1. count the transducer states `Q`;
2. bound every transition output length between `a` and `b`;
3. check `(14)`;
4. if it holds, apply `L-9316` and conclude infinitely many nonzero appended blocks.

For letter-to-letter encodings, at most eight states are permitted by the current recurrence witness. A larger machine may still be excluded by locating more densely packed identical source blocks or by a sharper state-synchronization argument.

## 9. Dependency audit

- Thue--Morse block supply uses only the uniform morphism and pair complementation.
- State synchronization is the pigeonhole principle.
- Output-length bounds are exact deterministic transducer accounting.
- `T-9316` supplies the ordinary recurrence cone.
- No source theorem, automaticity theorem, or experiment is used.

## 10. Gap audit

- Erasing transitions are not covered.
- A nondeterministic or two-way transducer is not covered.
- A subsequential final-output function is irrelevant for infinite words, but any unbounded delayed-output convention must be exposed separately.
- Machines violating `(14)` may still produce efficiently recurrent outputs; the theorem supplies a sufficient condition only.
- No exact Dubickas transducer is asserted before full-source acquisition.
- Excluding a finite-state extremal family is not an all-itinerary theorem.

## 11. Suggested next attack

After acquiring the source equality language, identify the weakest exact presentation among:

```text
coding -> morphism -> sequential transducer -> more general finite relation.
```

Apply `L-9315` at the first two levels and `L-9316` at the third. Only if all these presentations fail should a new source-specific recurrence proof be necessary.
