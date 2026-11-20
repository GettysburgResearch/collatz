# Continuation: transferring complete witnesses by matching two seed pairs

**Main 512-residue implication: OPEN.** This continuation proves a new
descending conditional reduction. It does not prove convergence for every
parameter and does not supply a complete recursive cover.

The dependencies are the supplied definition of `E`, direct integer algebra,
and the witness/trajectory and concatenation lemmas W512-010 and W512-011 in
[the proof packet](README.md). The four finite seed certificates used below
are included in full. No convergence bound or earlier research history is
assumed.

For positive odd `M`, put

\[
X(M)=128M+1,\qquad Y(M)=64M+1,
\]

and write

\[
\mathcal C(M):\quad X(M)\in E\Longrightarrow Y(M)\in E.
\]

These odd parameters are among the allowed cases of the original question.
In the notation of the proof packet, \(\mathcal C(M)\) is equivalent to
\(Q(M)\).

| Local claim | Status | Exact scope |
|---|---|---|
| CA-001 | PROVED-IN-NOTE | Lifting a fixed finite witness to nearby positive ordinary integers while preserving its exact exponent prefix. |
| CA-002 | PROVED-IN-NOTE | Transfer between two parameter families when both seed heights change by the same integer. |
| CA-003 | PROVED-IN-NOTE | For \(M>3\), \(M\equiv3\pmod{2^{121}}\), the exact reduction \(\mathcal C(M)\Longleftrightarrow\mathcal C((M+4011)/2)\). The new parameter is smaller. |

## 1. CA-001: a finite witness lifting lemma

Let a positive odd seed `z` have a witness of length `r`, with cumulative
exponents

\[
0=A_0<A_1<\cdots<A_r,
\]

and odd states \(z_i=T^i(z)\), so \(z_r=1\). The witness may include terminal
exponent-2 loops at 1. Let \(N\geq A_r+1\) and let `u` be a positive integer.
Then the first `r` odd steps from \(z+2^N u\) have exactly the same exponent
increments as the seed, and their states are

\[
\boxed{
z_i+3^i2^{N-A_i}u\qquad(0\leq i\leq r).
}
\tag{CA.1}
\]

In particular, their endpoint is

\[
\boxed{1+3^r2^{N-A_r}u.}
\tag{CA.2}
\]

**Proof.** Substitution in the recurrence gives

\[
3\bigl(z_i+3^i2^{N-A_i}u\bigr)+1
=2^{A_{i+1}-A_i}
 \bigl(z_{i+1}+3^{i+1}2^{N-A_{i+1}}u\bigr).
\]

Every state in parentheses is a positive odd integer: its first summand is
odd, and its second summand is positive and even because
\(N-A_{i+1}\geq1\). Hence the displayed division is exact and removes all
powers of 2. Induction proves the formula. This argument concerns a fixed
positive ordinary integer throughout; no completion or limiting orbit is
used.

The endpoint in (CA.2) exceeds 1. Thus a supplied witness for the lifted
input cannot end before this prefix has been traversed. Its remaining suffix
is a witness for the endpoint.

## 2. CA-002: equal changes of two seed heights

For a finite witness with length `r` and final exponent `A`, define its
height to be

\[
h=A-2r.
\]

Padding by the loop at 1 changes `(r,A)` to `(r+1,A+2)` and leaves `h`
unchanged. This height is used here only to compare finite certificates; no
general stopping or monotonicity assertion about it is assumed.

Suppose positive odd parameters `b,c` have finite witnesses for all four
seeds \(X(b),Y(b),X(c),Y(c)\). Denote their data by

\[
(r_b,A_b),\quad(s_b,B_b),\quad(r_c,A_c),\quad(s_c,B_c).
\]

Assume that the source heights and the target heights both change by the
same integer `d`:

\[
\begin{aligned}
A_c-2r_c&=A_b-2r_b+d,\\
B_c-2s_c&=B_b-2s_b+d.
\end{aligned}
\tag{CA.3}
\]

Equivalently, the two seed pairs have the same difference between their
source and target heights.

Pad the source witnesses to a common length
\(R=\max(r_b,r_c)\), and the target witnesses to a common length
\(S=\max(s_b,s_c)\). Write their padded final exponents as

\[
\alpha_b=A_b+2(R-r_b),\quad
\alpha_c=A_c+2(R-r_c),
\]

\[
\beta_b=B_b+2(S-s_b),\quad
\beta_c=B_c+2(S-s_c).
\]

Then (CA.3) is precisely

\[
\alpha_c=\alpha_b+d,\qquad
\beta_c=\beta_b+d.
\tag{CA.4}
\]

Choose an integer `K` satisfying

\[
K\geq1,\quad K+d\geq1,\quad
K+7\geq\alpha_b+1,\quad
K+6\geq\beta_b+1.
\tag{CA.5}
\]

For every positive integer `u`, put

\[
M=b+2^K u,\qquad M'=c+2^{K+d}u.
\tag{CA.6}
\]

Both parameters are positive odd integers. Applying CA-001 to the padded
source witnesses shows that `X(M)` and `X(M')` reach the same odd value
after exactly `R` steps:

\[
\boxed{
T^R(X(M))=T^R(X(M'))
=1+3^R2^{K+7-\alpha_b}u.
}
\tag{CA.7}
\]

The second equality follows from
\(K+d+7-\alpha_c=K+7-\alpha_b\). The target witnesses likewise give

\[
\boxed{
T^S(Y(M))=T^S(Y(M'))
=1+3^S2^{K+6-\beta_b}u.
}
\tag{CA.8}
\]

Consequently, without assuming any unproved bridge,

\[
X(M)\in E\Longleftrightarrow X(M')\in E,
\qquad
Y(M)\in E\Longleftrightarrow Y(M')\in E,
\]

and hence

\[
\boxed{\mathcal C(M)\Longleftrightarrow\mathcal C(M').}
\tag{CA.9}
\]

### Explicit certificate bookkeeping

Given any witness for `X(M)`, replace its initial `R` increments by the
padded `X(c)` seed increments and retain its entire remaining suffix. This
is a witness for `X(M')`. Its number of odd steps is unchanged; every
cumulative exponent at or after the splice changes by `d`, including the
terminal exponent.

If a witness for `Y(M')` is then supplied, replace its initial `S`
increments by the padded `Y(b)` seed increments. The result is a witness for
`Y(M)`. Its number of odd steps is unchanged, and the terminal exponent
changes by `-d`.

These are ordinary finite concatenations at the common values (CA.7) and
(CA.8). The prefix exponents are forced by CA-001, so no arbitrary choices
of a parity path are being made.

If `d<0`, the parameter transformation is an affine contraction:

\[
M'=c+2^d(M-b).
\]

It strictly decreases `M` whenever

\[
M>\frac{c-2^d b}{1-2^d}.
\tag{CA.10}
\]

The source terminal exponent also decreases by the positive integer `-d`.
Either decrease can justify this particular recursive call. Neither fact
establishes that every parameter admits such a call.

## 3. Four explicit seed certificates

The required seeds for `b=3` and `c=2007` have the following data.

| Parameter | Seed | Length | Final exponent | Height |
|---:|---:|---:|---:|---:|
| 3 | \(X(3)=385\) | 9 | 23 | 5 |
| 3 | \(Y(3)=193\) | 43 | 76 | -10 |
| 2007 | \(X(2007)=256897\) | 34 | 72 | 4 |
| 2007 | \(Y(2007)=128449\) | 68 | 125 | -11 |

Thus both heights change by `d=-1`, and both height differences equal 15.
The full cumulative-exponent tuples are below. For each row, the number of
entries is `r+1`, the first entry is 0, the entries strictly increase, and
direct integer substitution gives

\[
3^r z+\sum_{j=0}^{r-1}3^{r-1-j}2^{A_j}=2^{A_r}.
\]

```text
z = 385
r = 9
A = [0, 2, 4, 6, 7, 12, 13, 14, 19, 23]

z = 193
r = 43
A = [0, 2, 4, 7, 9, 10, 11, 12, 13, 15, 17, 18, 20, 21,
     22, 24, 25, 26, 27, 29, 32, 33, 34, 36, 37, 39, 40, 41,
     42, 43, 44, 47, 48, 49, 50, 54, 56, 58, 62, 65, 66, 67,
     72, 76]

z = 256897
r = 34
A = [0, 2, 4, 6, 7, 9, 10, 11, 13, 15, 16, 18, 22, 23,
     24, 26, 27, 30, 31, 34, 38, 39, 41, 42, 45, 46, 47, 48,
     53, 56, 61, 62, 63, 68, 72]

z = 128449
r = 68
A = [0, 2, 4, 7, 8, 9, 13, 14, 15, 17, 18, 20, 21, 22,
     24, 26, 29, 32, 33, 34, 39, 40, 41, 42, 44, 46, 49, 53,
     56, 58, 59, 60, 61, 62, 64, 66, 67, 69, 70, 71, 73, 74,
     75, 76, 78, 81, 82, 83, 85, 86, 88, 89, 90, 91, 92, 93,
     96, 97, 98, 99, 103, 105, 107, 111, 114, 115, 116, 121, 125]
```

These finite certificates prove only the four seed memberships. Their role
in an infinite family is justified separately by CA-001 and CA-002.

## 4. CA-003: the descending rule near parameter 3

Pad the 385 witness by 25 exponent-2 loops, from length 9 to length 34.
Its final exponent becomes

\[
23+2\cdot25=73.
\]

The 256897 witness already has length 34 and final exponent 72.
Likewise, pad the 193 witness by 25 exponent-2 loops, from length 43 to
length 68. Its final exponent becomes

\[
76+2\cdot25=126,
\]

while the 128449 witness has length 68 and final exponent 125.

For any integer \(K\geq121\) and positive integer `u`, put

\[
M=3+2^K u,\qquad
M'=2007+2^{K-1}u=\frac{M+4011}{2}.
\tag{CA.11}
\]

The source perturbations are \(2^{K+7}u\) and \(2^{K+6}u\), respectively.
The padded source certificates therefore give

\[
\boxed{
T^{34}(X(M))=T^{34}(X(M'))
=1+3^{34}2^{K-66}u.
}
\tag{CA.12}
\]

Their cumulative prefix exponents are 73 and 72.

The target perturbations are \(2^{K+6}u\) and \(2^{K+5}u\). The padded
target certificates give

\[
\boxed{
T^{68}(Y(M))=T^{68}(Y(M'))
=1+3^{68}2^{K-120}u.
}
\tag{CA.13}
\]

Their cumulative prefix exponents are 126 and 125. The strongest lifting
requirement is \(K+6\geq126+1\), namely `K>=121`. All the displayed
endpoints are positive odd integers greater than 1.

It follows that

\[
\boxed{
M>3,\quad M\equiv3\pmod{2^{121}}
\quad\Longrightarrow\quad
\mathcal C(M)\Longleftrightarrow
\mathcal C\!\left(\frac{M+4011}{2}\right).
}
\tag{CA.14}
\]

To cover the entire displayed congruence class, simply use `K=121` and
\(u=(M-3)/2^{121}\); `u` need not be odd. The new parameter satisfies

\[
M'\equiv3\pmod4,\qquad 0<M'<M,
\]

because \(M\geq3+2^{121}>4011\). Both parameters therefore remain in the
allowed odd-parameter case. The isolated value `M=3` is already covered by
the displayed seed certificates.

### Reconstructing the requested witness

Given a supplied witness for `X(M)`, its first 34 steps are the 385 seed
increments followed by 25 increments of 2. Replace these by the 256897
seed increments and retain the suffix. This gives a witness for `X(M')`
with the same length and terminal exponent smaller by 1.

If the smaller bridge \(\mathcal C(M')\) provides a witness for `Y(M')`,
replace its first 68 increments by the 193 seed increments followed by
25 increments of 2. Retain the suffix. This gives the required witness for
`Y(M)`, with the same length as that recursive target witness and terminal
exponent larger by 1.

This is a conditional recursive construction: the call at `M'` must still
be discharged by another proved rule or a finite certificate. CA-003 does
not assert that repeated calls using the current packet cover every input.

## 5. An equivalent normalization check

For comparison with the elementary bridge algebra, take `u` odd and
write `K` by parity. The four lifted seed endpoints can also be normalized
using W512-012 and W512-013. In each column the two parameters give exactly
the same membership condition:

| Parity | \(X(M)\in E\) and \(X(M')\in E\) are each equivalent to | \(Y(M)\in E\) and \(Y(M')\in E\) are each equivalent to |
|---|---|---|
| \(K=2q\) | \(3^q u\in E\) | \(3^{q+7}u\in E\) |
| \(K=2q+1\) | \(2\cdot3^{q+1}u+1\in E\) | \(2\cdot3^{q+8}u+1\in E\) |

These equivalences do not assume upward closure under multiplication by 3.
Indeed, the even row displays an upward factor of \(3^7\), which cannot
be justified merely by the one-way factor-removal consequence of the
original bridges. The proof instead transfers both sides to another
parameter having a smaller supplied source certificate exponent.

## 6. What remains open

The new result supplies one rigorous descending call, with a complete
witness reconstruction, for a previously problematic family. Its proof
uses full seed witnesses and terminal padding; it does not require a
uniform forward merger between `X(M)` and `Y(M)` themselves.

A proof of the full claim still needs a complete well-founded rule covering
every allowed input. In particular, this note does not establish that each
uncovered parameter has a second seed pair satisfying (CA.3) with a
negative height change, nor that finitely many such rules and the earlier
rules cover all cases. Inferring either assertion from the finite seed
search would be the first unsupported step.
