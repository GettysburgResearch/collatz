# T-8302 — The negative-three two-branch chart is a paired accelerated cycle compiler

Claim ID: `T-8302`  
Title: Every periodic word in the exact negative-three pulse chart is a paired accelerated valuation word with the same full Collatz cycle denominator  
Status: `PROPOSED / EXACT CONSTRUCTIVE REDUCTION`  
Authoring agent: `gpt56-cycle-02`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: only the definition of the accelerated odd Collatz map; branch-qualified `PR51/O-8001` supplied the motivating chart  
Scope: finite words in the two exact branches centered at the negative three-cycle  
Related counterexample candidates: none; `O-8301` is a rigorously rejected frozen near-candidate

## Statement

Let

\[
 S(n)=\frac{3n+1}{2^{\nu _2(3n+1)}}
\]

be the accelerated map on positive odd integers. Put

\[
 x=\frac{n-1}{2}.
\]

For a chart symbol `e in {0,1}`, define the partial integer branch

\[
 \boxed{2^{4-e}x'=9x+3e.}                                    \tag{1}
\]

Its exact domains are

\[
 e=1:\quad x\equiv5\pmod8,
 \qquad
 e=0:\quad x\equiv0\pmod {16}.                              \tag{2}
\]

Then the corresponding physical odd state `n=2x+1` follows exactly two accelerated Collatz steps with valuation block

\[
 \boxed{(2-e,2)}                                              \tag{3}
\]

and reaches `n'=2x'+1`.

Now fix a finite binary chart word

\[
 e=(e_0,\ldots,e_{m-1}),
 \qquad e_j\in\{0,1\}.
\]

Put

\[
 E_0=0,\qquad E_{j+1}=E_j+4-e_j,                              \tag{4}
\]

\[
 C_0=0,\qquad
 C_{j+1}=9C_j+3e_j2^{E_j}.                                    \tag{5}
\]

Let

\[
 s=\sum_{j=0}^{m-1}e_j,
 \qquad
 k=2m,
 \qquad
 A=4m-s.                                                       \tag{6}
\]

Then:

1. the chart composition is
   \[
   \boxed{2^A x_m=9^m x_0+C_e,\qquad C_e=C_m;}                \tag{7}
   \]
2. the expanded accelerated word is
   \[
   \boxed{w(e)=(2-e_0,2,2-e_1,2,\ldots,2-e_{m-1},2);}         \tag{8}
   \]
3. its ordinary affine numerator satisfies
   \[
   \boxed{C_{w(e)}=D+2C_e,\qquad D=2^A-3^k=2^A-9^m;}         \tag{9}
   \]
4. because `D` is odd,
   \[
   \boxed{D\mid C_{w(e)}\quad\Longleftrightarrow\quad D\mid C_e;} \tag{10}
   \]
5. consequently, a finite word `e` is a nontrivial positive periodic orbit of the partial chart exactly when
   \[
   D>0,\qquad D\mid C_e,\qquad x_0=C_e/D>0,                  \tag{11}
   \]
   with the branch domains in (2) replaying exactly. In that case
   \[
   \boxed{n_0=2C_e/D+1}                                      \tag{12}
   \]
   is a finite unconditional positive Collatz counterexample.

### Critical-scale specialization

For the frozen PR #45 parameters

```text
k = 3,149,971,404,836,
A = 4,992,586,555,009,
```

put

```text
m = k/2 = 1,574,985,702,418,
s = 2k-A = 1,307,356,254,663.
```

Thus any chart word of length `m` and weight `s` has **exactly the same full denominator**

\[
 2^A-3^k                                                     \tag{13}
\]

as the PR #45 critical mechanical program. The lower mechanical chart word `L(s,m)` and all same-length, same-weight block replacements can therefore reuse every certified denominator factor and every full-denominator test from that program.

### Exact adjacent chart repair

Suppose positions `u,u+1` contain `01`, and let

\[
 E_u=\sum_{j<u}(4-e_j).
\]

Replacing `01` by `10` changes the chart numerator by

\[
 \boxed{
 C_{\cdots10\cdots}-C_{\cdots01\cdots}
 =-21\,9^{m-u-2}2^{E_u}.}                                   \tag{14}
\]

The reverse replacement changes the sign. Hence the chart itself carries a proof-producing monomial repair basis.

## Definitions

Symbol `1` is the unpulsed negative-three block `(1,2)` and symbol `0` is the one-pulse block `(2,2)`. In the `x` coordinate these are respectively

\[
 x\mapsto\frac{9x+3}{8},
 \qquad
 x\mapsto\frac{9x}{16}.                                     \tag{15}
\]

The trivial physical state `n=1` is `x=0`.

## Motivation

`PR51/O-8001` left an exact two-branch ordinary chart whose all-time closure would be a complete counterexample. PR #45 left a trillion-letter critical denominator and a mechanical compiler, but its word was not constrained to the chart. Equations (8)--(13) identify the missing connection: the chart has its own critical mechanical submonoid at exactly the same denominator.

This permits the two constructive lanes to share:

- continued-fraction scale;
- certified factors of `D`;
- Euclidean mechanical compilation;
- local monomial repairs;
- factorwise quotient cylinders; and
- independent exact cycle replay.

## Proof

Assume first `e=1` and `x=5 mod 8`. For `n=2x+1`,

\[
 3n+1=2(3x+2),
\]

and `3x+2` is odd. The first accelerated valuation is therefore `1`. The next odd state is `3x+2`, and

\[
 3(3x+2)+1=9x+7
\]

has exact valuation `2` when `x=5 mod 8`. The resulting odd state is `(9x+7)/4`, so its shifted coordinate is `(9x+3)/8`. This proves (1)--(3) for `e=1`.

If `e=0` and `x=0 mod 16`, then `3n+1=2(3x+2)` has exact valuation `2`, and the second accelerated numerator has exact valuation `2` as well. Direct simplification gives `x'=9x/16`. This proves the second branch.

Induction on the chart symbols gives (7) from (4)--(5). Applying the physical change of variables `n_j=2x_j+1` to (7) gives

\[
 2^A n_m
 =9^m n_0+(2^A-9^m)+2C_e,
\]

which proves (8)--(9). The denominator `D` is odd, proving (10). The standard affine cycle criterion then gives (11)--(12), and the already-proved local branch calculation supplies every advertised valuation.

For (14), the two local chart constants are

\[
 C_{01}=9\cdot0+16\cdot3=48,
 \qquad
 C_{10}=9\cdot3+8\cdot0=27.
\]

The common prefix contributes `2^{E_u}`, and the common suffix contributes `9^{m-u-2}`. Their difference is `-21` times those factors. **QED**

## Dependency audit

The proof is self-contained. `PR51/O-8001` is used only for provenance and notation. No result about an infinite completion, a negative cycle, or a proposed cycle theorem is assumed.

## Gap audit

- Finite words and a complete repair basis do not produce a full-denominator hit.
- `D|C_e` must involve the entire denominator, not a proper certified factor.
- A compatible infinite branch word may define only a `2`-adic point rather than a positive ordinary integer.
- The first attempted monotonicity shortcut was false: chart branch `1` can follow itself and expand, for example `x=61 -> 69`. No extinction conclusion is imported from that failed idea.
- `O-8301` satisfies only a 61-bit proper divisor and is explicitly rejected.

## Adversarial tests

`X-8302`:

- checks (9) for all binary words through length nine;
- verifies all local repair signs and exponents;
- compiles the trillion-scale lower mechanical chart word;
- reconstructs a 41-swap proper-factor solution; and
- rejects that frozen word independently in both the real and factorwise quotient coordinates.

## Remaining uncertainty

The exact full-denominator identity at the critical scale remains open.

## Suggested next attack

Use `L-8303` quotient-target lifting, rather than numerator divisibility alone, at each certified prime power. Add hierarchical Farey-neighbor block transpositions from `L-8302` until the local replacement entropy exceeds the desired Hensel quotient precision, while preserving the paired chart grammar.
