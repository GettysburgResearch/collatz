# T-8506 — Every legal refund connector adds more than 170 core bits

**Claim ID:** `T-8506`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Dependencies:** `L-8505`; the exact inequality `3^53>2^84`  
**Scope:** every legal path with `t_n>=3744`, after the first primitive core is defined

## Theorem

For every legal connector at height `t_n>=3744`, the primitive cores of `L-8505` satisfy

\[
\boxed{C_{n+1}>2^{170}C_n.}
\tag{1}
\]

Consequently

\[
\boxed{C_{n+r}>2^{170r}C_n}
\qquad(r\ge1),
\tag{2}
\]

and the prime-to-six part of the physical boundary shift is strictly increasing and unbounded at every connector, not merely along a subsequence.

Combined with `T-8505`, every step replaces the preceding coprime core by a core more than 170 bits larger, and infinitely many steps introduce a globally new odd prime.

## Proof

At height `t`, put

\[
N=3^{7(t+1)},
\qquad
M=2^{11(t+17)}.
\]

The exact inequality `3^53>2^84` gives

\[
\log_2\frac NM
>
\frac{84\cdot7(t+1)-53\cdot11(t+17)}{53}
=
\frac{5t-9323}{53}.
\tag{3}
\]

At `t=3744`,

\[
5t-9323=9397>53\cdot177,
\]

and the left side of the comparison increases with `t`. Hence

\[
\boxed{\frac NM>2^{177}.}
\tag{4}
\]

From `L-8505`,

\[
\frac{C_{n+1}}{C_n}
>
\frac{3^{G_n}}{2^{L_n}}
=
\frac NM
2^{i_n-i_{n+1}}
3^{\beta_{i_{n-1}}-\beta_{i_n}}.
\tag{5}
\]

The four binary signatures lie in `{0,1,2,3}` and the ternary signatures lie in `{1,2,3}`. Therefore

\[
2^{i_n-i_{n+1}}
3^{\beta_{i_{n-1}}-\beta_{i_n}}
\ge
2^{-3}3^{-2}
=
\frac1{72}
>
2^{-7}.
\tag{6}
\]

Combining `(4)--(6)` proves

\[
C_{n+1}>2^{177-7}C_n=2^{170}C_n.
\]

Iteration proves `(2)`. ∎

## Full-objective consequence

A positive certificate need not separately prove drift for the physical values, the complement counters, or the primitive cores. All three growth obligations are automatic once the exact top-boundary divisibility remains defined.

The remaining invariant is nevertheless stronger than a growth invariant: it must make the exact high binary valuation in `L-8505/(5)` recur forever while replacing a rapidly growing coprime prime-to-six core at each step.
