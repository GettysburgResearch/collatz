# Backward failure resets and the finite witness horizon

**23 November 2026. Status: PROPOSED exact consequences of the candidate
recurrence; the universal closing inequality remains OPEN.** This note
records a final attempt to derive a decreasing backward failure position
or a candidate subsequence whose witness horizon is reached. The argument
below rules out monotonicity of this particular position under extension
of an actual prefix. It does not rule out other descent methods.

## Definitions and dependencies

Use the shortcut map T(x)=x/2 for even x and T(x)=(3x+1)/2 for odd x.
Fix one positive ordinary integer n, and use the notation and written
identities of [TRIADIC_CONSTRUCTION_ATTEMPT.md](TRIADIC_CONSTRUCTION_ATTEMPT.md),
Sections 1--3:

\[
x_K=T^K(n),\quad e_K=x_K\bmod2,\quad
b_K=\sum_{i<K}(1-e_i),\quad c_K=1+e_K,
\]

\[
A_K=2^Kc_K-D_K,\qquad
\eta_K=A_K/3^{b_K},\qquad
r_K=b_K-\min\bigl(b_K,v_3(A_K)\bigr).
\]

Here D_0=0 and D_(K+1)=3^(1-e_K)D_K+(1-e_K)2^K. The numerator A_K is
nonzero, as proved in the cited note. Its exact recurrence is

\[
A_{K+1}=3^{1-e_K}A_K+2^{K+1}\sigma_K,
\qquad \sigma_K=e_K+e_{K+1}-1.                 \tag{1}
\]

To locate the first backward integrality failure, start z_K=c_K and
pull backward using z_i=2z_(i+1) when e_i=1 and
z_i=(2z_(i+1)-1)/3 when e_i=0. If the first failure occurs at j, then
r_K=b_(j+1). This description concerns the complementary candidate;
the original trajectory x_i is positive and integral throughout.

## Four exact transition cases

1. **Alternating, 01 or 10.** Equation (1) has sigma_K=0. Since
   b_(K+1)=b_K+1-e_K, it follows that eta_(K+1)=eta_K and
   r_(K+1)=r_K.

2. **Even-even, 00.** Equation (1) becomes
   A_(K+1)=3A_K-2^(K+1), which is not divisible by 3. Consequently

   \[
                    r_{K+1}=b_{K+1}=b_K+1.                 \tag{2}
   \]

   The first backward failure is immediately at j=K: the new terminal
   value is c_(K+1)=1, and the first inverse step produces (2-1)/3=1/3.

3. **Odd-odd, 11, with r_K<b_K.** This hypothesis implies 3 divides
   A_K. Now A_(K+1)=A_K+2^(K+1) is not divisible by 3, while
   b_(K+1)=b_K. Hence r_(K+1)=b_K: all previously cancelled denominator
   factors are lost.

4. **Odd-odd, 11, with r_K=b_K.** In this case

   \[
   r_{K+1}=b_K-
      \min\bigl(b_K,v_3(A_K+2^{K+1})\bigr).                \tag{3}
   \]

   For any 1<=t<=b_K, cancellation of at least t factors is equivalent
   to the fresh congruence A_K+2^(K+1)=0 modulo 3^t. If b_K=0, both
   exponents are zero and the congruence range is empty. No lower bound
   on this valuation follows from the preceding cases.

These cases use actual parity transitions and exact arithmetic. In
particular, a 00 transition resets the failure position to the latest
available clock, rather than making it decrease.

## Two actual positive controls

For n=3, the shortcut orbit starts 3,5,8,4,2,1,2. Directly from the
definitions:

| K | x_K | b_K | D_K | A_K | eta_K | r_K | First backward failure j |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2 | 8 | 0 | 0 | 4 | 4 | 0 | None |
| 3 | 4 | 1 | 4 | 4 | 4/3 | 1 | 2 |
| 4 | 2 | 2 | 20 | -4 | -4/9 | 2 | 3 |

Thus even an ordinary source that converges has failure positions moving
right. This is a finite counterexample to monotone decrease of that
position, not a counterexample to eventual favorable behavior.

Complete denominator cancellation also does not by itself produce a
short witness. Write eta_K=a_K/3^(r_K) in reduced form. The finite
sufficient horizon from
[TRIADIC_RANK.md](../../global-closure-20261123/duality/TRIADIC_RANK.md),
Section 4, is

\[
N=\operatorname{bl}(n),\quad
L_K=\operatorname{bl}(\max(1,|a_K|,3^{r_K})),\quad
H_K=8N+(9r_K+8)L_K+2,                                    \tag{4}
\]

where bl(m) is the least positive L with m<2^L. For the actual source
n=27, N=5 and the recurrence gives:

| K | x_K | b_K | D_K | A_K | eta_K=a_K | r_K | L_K | H_K |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 71 | 1 | 4 | 60 | 20 | 0 | 5 | 82 |
| 7 | 161 | 1 | 4 | 252 | 84 | 0 | 7 | 98 |

Both candidates cancel the entire denominator, but both have H_K>K.
These finite examples refute sufficiency of denominator cancellation
alone; they do not exclude a later successful candidate.

## The quadratic denominator cost and its quantifier limit

For every candidate, 3^(r_K)<=max(1,|a_K|,3^(r_K))<2^(L_K), so

\[
L_K>r_K\log_2 3,
\qquad
H_K>9(\log_2 3)r_K^2.                                    \tag{5}
\]

Thus at a full-denominator reset, the horizon has a quadratic lower
bound in the number of original-even steps accumulated at that clock.
In particular, H_K<=K would require
r_K<sqrt(K/(9 log_2 3)), as well as the numerator constraint in (4).

This argument does not show that a fixed source has infinitely many
00 transitions, that b_K grows faster than sqrt(K), or that every later
candidate violates H_K<=K. Nor do the finite controls establish an
asymptotic obstruction. A favorable subsequence remains possible; the
missing step is a simultaneous saving in the reduced numerator and
denominator sufficient for (4). No such saving is proved here.

**Evidence scope.** The four cases and (5) have the written proofs above;
the two tables are exact finite evaluations of the displayed recurrences.
No new Lean theorem or claim of Collatz convergence is added by this note.
