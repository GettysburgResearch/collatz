# Focused review: odd-count weighted rank obstruction

**Review date:** 2026-11-21 UTC

**Reviewer:** `global_forcing`, separate from the note's author

**Verdict:** PASS at paper level for the stated fixed-weight, unrestricted-rule obstruction.

## Frozen scope

The final authored note was read from disk at this exact hash:

| Artifact | SHA256 |
|---|---|
| `research/band-return-20261121/WEIGHTED_RANK_OBSTRUCTION.md` | `52b8a358586e12b3d6fc15b10e8d689d8241d16c99854dcd729f6e052ef31739` |
| `reports/2026-11-21-band-return/weighted-rank-compiler-row.json` | `b95294ecc8ceda9b6c844b74bdda9a4d72e15d41219c0829cba59c8a0fd3b881` |

The recorded compiler source is PR168
`e4599b32e4b1a955ac9315d46782d4ad6a5db96c`,
`research/closure-frontier-20261121/negative_template_compiler.py`, with
SHA256 `16aab6efe1294a33c88f8b2fadae9d8060e68cc242eee18425aab7cfdcdd1745`.
The parent independently replayed the specified row and recorded clock
difference 11 and odd-count difference 7. This review read that focused
record; it did not rerun the compiler or audit other rows.

The independent checks here used exact integer modular exponentiation,
ordinary finite shortcut iteration, and symbolic algebra. No large integer
was approximated by floating-point arithmetic. This is not an additional
Lean formalization or a broad audit of earlier work.

## 1. The strict forward conditions are correctly necessary

For positive fixed weights, let

\[
 R(n,d,p)=(n+1)\lambda^d\mu^p.
\]

An odd ordinary certificate step has exact ratio
\(3/(2\lambda\mu)\), so strict decrease requires
\(\lambda\mu>3/2\). A positive even step has ratio
\((n+2)/(2(n+1)\lambda)\), so any such strict comparison requires
\(\lambda>1/2\). Requiring the step \(2\to1\) gives the stronger
\(\lambda>2/3\), as the note explicitly acknowledges.

The argument uses these as necessary conditions, not as sufficient
conditions for every forward step. The strict boundaries are handled
correctly: equality in the odd condition preserves rank, and
\(\lambda=1/2\) makes every positive even comparison increase it.

## 2. Exact CRT and integrality checks

For

\[
 e_j=2534744+3188646j,\quad
 S_j=(2^{e_j}-85)/27,\quad M_j=(S_j-2)/81,
\]

the independently evaluated exact checks were:

| Check | Result |
|---|---:|
| \(3^{14}\) | 4,782,969 |
| \(2^{2534744}\bmod3^{14}\) | 1,703,812 |
| \(2^{3188646}\bmod3^{14}\) | 1 |
| \(27\cdot63101+85\) | 1,703,812 |
| \(81\cdot779+2\) | 63,101 |
| \(27\cdot1969+85\) | \(2048\cdot26\) |
| \((81\cdot2047+2)\bmod2048\) | 1,969 |

Periodicity gives the stated congruence for every natural \(j\), not only
the tested exponent. It proves integral positive \(S_j\) and
\(S_j\equiv63101\pmod{3^{11}}\). Since \(e_j\ge11\), reduction of
\(27S_j+85=2^{e_j}\) modulo 2048 gives
\(S_j\equiv1969\pmod{2048}\).

Equivalently,

\[
 M_j=\frac{2^{e_j}-139}{2187}.
\]

The ternary congruence therefore gives \(M_j\equiv779\pmod{2187}\).
Modulo 2048, the divisor 2187 is congruent to 139 and is invertible, so
\(2187M_j\equiv-139\) gives \(M_j\equiv-1\pmod{2048}\).
Both required row guards are obtained without division by a nonunit modulo
2048 or an unjustified division of the ternary modulus.

The CRT progression was also checked:

\[
 M=761855+4478976h,\quad
 M'=713433+4194304h,\quad
 2187M'+1069=2048M.
\]

The family lies above this positive base and is unbounded, since its
exponents increase by the positive integer 3,188,646. Thus it supplies
arbitrarily large positive ordinary inputs satisfying the row's two
arithmetic guards.

## 3. Both certificates have the stated actual clocks and odd counts

The ordinary 11-clock prefix from 1969 was independently iterated:

```text
1969, 2954, 1477, 2216, 1108, 554,
277, 416, 208, 104, 52, 26.
```

Its odd input clocks are exactly \(0,2,6\). Its affine intercept is 85,
so the congruence cylinder gives

\[
 T^{11}(S_j)=\frac{27S_j+85}{2^{11}}=2^{e_j-11}.
\]

The remaining steps are \(e_j-11\) halvings. Hence the source certificate
has total clock \(e_j\) and exactly three odd inputs. The full odd word
\((2,4,e_j-6)\) has that same count and total clock.

The transformed certificate was independently checked through an ordinary
positive residue, rather than inferred solely from a negative-reference
word. The source-shift identity implies

\[
 3^{10}S'_j=2^{e_j+11}-2504477.
\]

The canonical residue is
\(S'_j\equiv3262123\pmod{2^{22}}\). Its actual 22-clock prefix has
odd input clocks

```text
0, 1, 3, 5, 7, 9, 10, 12, 16, 21
```

and endpoint 45,926. Exact iteration gives affine intercept 2,504,477 and

\[
 3^{10}\cdot3262123+2504477=2^{22}\cdot45926.
\]

Thus, on the entire proposed family,

\[
 T^{22}(S'_j)=2^{e_j-11}.
\]

The transformed source consequently has total clock \(e_j+11\) and
exactly ten odd inputs. Its listed full odd word
\((1,2,2,2,2,1,2,4,5,e_j-10)\) matches the independently checked odd
clock gaps and has total clock \(e_j+11\).

These are genuine first-hit witnesses, not gratuitously padded ones: the
displayed power-of-two endpoints are greater than two, so the preceding
prefixes cannot already have visited the closed \(1,2\) cycle. The final
power-of-two tails first reach one at the claimed clocks. This directly
corroborates the retained \((d,p)\mapsto(d+11,p+7)\) comparison on the
unbounded family, independently of the generic compiler implementation.

## 4. The exact rank comparison gives an eventual strict increase

Substitution of \(S=81M+2\), \(S'=81M'+2\) into the row gives

\[
 2187(S'+1)=2048(S+1)-86172.
\]

The constant was checked directly:
\(81\cdot1069-3\cdot2187+3\cdot2048=86172\).
With

\[
 Q=\frac{2048}{2187}\lambda^{11}\mu^7
   =(2\lambda)^4(2\lambda\mu/3)^7,
\]

the necessary strict forward conditions imply \(Q>1\). The exact
ratio on the actual certificates is

\[
 \frac{R(S',d+11,p+7)}{R(S,d,p)}
 =Q\left(1-\frac{86172}{2048(S+1)}\right).
\]

It is greater than one when

\[
 S+1>\frac{86172Q}{2048(Q-1)}.
\]

The unbounded certified family exceeds this threshold for every fixed
admissible pair of weights. The conclusion is therefore not based on a
finite search or on dropping the finite affine correction.

## 5. Scope of the verified obstruction

The result rules out this fixed multiplicative rank when it is required
to decrease on all the stated ordinary forward-source comparisons and
all guarded instances of the specified reverse row. It does not rule out
selecting only some moves, retaining a forward growth guard, using a
different rank, or adding state information. In particular it does not
contradict the earlier checked common rank whose forward returns retain
an explicit guard.

The reviewed note preserves these limitations and labels the argument as
paper-level. No arithmetic or certificate-clock gap was found in the
specified family or in the rank incompatibility. No full Collatz proof is
claimed by this review.
