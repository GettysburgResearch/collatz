# L-9833 — No ordinary seed for an infinite nested `10/30` suffix schedule

Claim ID: `L-9833`  
Title: Eventual input stabilization would force an impossible infinite descent of positive H endpoints  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: exact H cylinder concatenation; `L-9801`, `L-9827`, `L-9831`  
Scope: nested exact H cylinders formed by any infinite suffix schedule in `{10,30}`  
Related counterexample candidates: none

## Definitions

Let `w_0` be a fixed exact H prefix with canonical input and endpoint

\[
0\le A_0<U_0,
\qquad
0\le Y_0<V_0.
\tag{1}
\]

Fix any infinite suffix schedule

\[
z_0,z_1,z_2,\ldots\in\{10,30\},
\tag{2}
\]

and define the nested words

\[
w_n=w_0z_0z_1\cdots z_{n-1}
\qquad(n\ge1).
\tag{3}
\]

Write their canonical data as

\[
(U_n,V_n,A_n,Y_n).
\tag{4}
\]

For the suffix `z_i`, put

\[
k_i=
\begin{cases}
7,&z_i=10,\\
13,&z_i=30,
\end{cases}
\qquad
K_i=\sum_{j=0}^{i-1}k_j,
\qquad K_0=0.
\tag{5}
\]

Let

\[
h_i\in[0,2^{k_i})
\tag{6}
\]

be the exact interface block used when appending `z_i` to `w_i`.

## Statement

### 1. Exact canonical-input expansion

Exact cylinder concatenation gives

\[
\boxed{
U_n=U_0\,2^{K_n}
}
\tag{7}
\]

and

\[
\boxed{
A_{i+1}=A_i+h_iU_i.
}
\tag{8}
\]

Consequently

\[
\boxed{
A_n
=A_0+U_0H_n,
\qquad
H_n=\sum_{i=0}^{n-1}2^{K_i}h_i.
}
\tag{9}
\]

The integers `H_n` are exactly the mixed-radix prefixes selected uniquely in
`L-9831`.

### 2. Nested 2-adic limit and stabilization criterion

Equation (8) implies

\[
A_{n+1}\equiv A_n\pmod{U_n},
\qquad
0\le A_n<U_n,
\tag{10}
\]

while `U_n` tends to infinity. Hence the canonical inputs converge to a unique

\[
\boxed{
A_\infty
=A_0+U_0\sum_{i\ge0}2^{K_i}h_i
\in\mathbb Z_2.
}
\tag{11}
\]

This limit is an ordinary nonnegative integer if and only if the extension
blocks are eventually zero:

\[
\boxed{
A_\infty\in\mathbb Z_{\ge0}
\iff
h_i=0\text{ for all sufficiently large }i.
}
\tag{12}
\]

### 3. A zero block strictly lowers the endpoint

The exact suffix cylinders are

\[
\begin{array}{c|ccccc}
z&U_z&V_z&A_z&Y_z&\text{cylinder map}\\ \hline
10&128&81&72&46&72+128j\mapsto46+81j\\
30&8192&6561&4608&3691&4608+8192j\mapsto3691+6561j.
\end{array}
\tag{13}
\]

If the interface block for stage `i` is zero, then for a unique ordinary
integer `j_i >= 0` one has

\[
\boxed{
\begin{aligned}
z_i=10:
&\quad
Y_i=72+128j_i,
&&Y_{i+1}=46+81j_i,\\
z_i=30:
&\quad
Y_i=4608+8192j_i,
&&Y_{i+1}=3691+6561j_i.
\end{aligned}
}
\tag{14}
\]

Therefore

\[
\boxed{
\begin{aligned}
z_i=10:
&\quad Y_i-Y_{i+1}=26+47j_i>0,\\
z_i=30:
&\quad Y_i-Y_{i+1}=917+1631j_i>0.
\end{aligned}
}
\tag{15}
\]

Every zero extension block strictly decreases the positive integral endpoint.

### 4. Infinitely many nonzero blocks

The sequence `(h_i)` is not eventually zero. Otherwise, after some index
every stage would satisfy (15), producing an infinite strictly descending
chain

\[
Y_N>Y_{N+1}>Y_{N+2}>\cdots
\tag{16}
\]

of positive integers. This is impossible. Hence

\[
\boxed{
h_i\ne0
\quad\text{for infinitely many }i.
}
\tag{17}
\]

### 5. Nonordinary nested seed

Combining (12) and (17) gives

\[
\boxed{
A_\infty\notin\mathbb Z_{\ge0}.
}
\tag{18}
\]

Equivalently, the canonical inputs `A_n` never stabilize and are unbounded as
ordinary nonnegative integers. Thus no one ordinary nonnegative seed belongs
to every cylinder in this infinite nested `10/30` construction.

This conclusion is intentionally about admissible ordinary Collatz seeds. The
argument does not exclude (A_\infty) from being a negative integer or an
odd-denominator rational 2-adic integer; either would still be nonordinary for the
required nonnegative initialization.

### 6. Endpoint-zero audit

Every nonempty H affine word has positive additive numerator, so its canonical
output on a nonnegative input is positive. In particular,

\[
Y_n>0
\qquad(n\ge1).
\tag{19}
\]

Even if the chosen initial prefix allowed `Y_0=0`, the first appended suffix
makes the endpoint positive. Moreover, `h_i=0` cannot occur with `Y_i=0`:
equation (14) would require `0=A_z+jU_z` with `A_z > 0` and `j >= 0`.

Thus the descent contradiction uses positive integers and has no hidden zero
endpoint exception.

### 7. Interpretation boundary

The theorem holds for every infinite symbolic schedule in `{10,30}`, including
the forced Sturmian schedule of `L-9822`. It does **not** say that every H
construction has a nonordinary limit; it concerns this particular nested
suffix architecture.

For the forced schedule, terminal-zero renormalization chooses later symbols.
After the first actual completed suffix the raw multiplier is already
contracting, so the later appended suffixes are not proved to be repeated
physical first crossings. The theorem excludes an ordinary point from the
nested exact cylinders, not an ordinary orbit realizing infinitely many
first-crossing resets.

## Proof

For exact cylinder concatenation, appending a suffix of denominator `2^k`
gives

\[
U_{i+1}=2^{k_i}U_i,
\qquad
A_{i+1}=A_i+h_iU_i.
\tag{20}
\]

Induction proves (7)--(9). In particular the residues are compatible modulo
the increasing powers `U_n`, so they define (11).

If the blocks are eventually zero, (8) makes `A_n` eventually constant, and
its value is an ordinary nonnegative integer. Conversely, suppose
the limit equals (A_\infty=N) with (N\ge0). Once (U_n>N), its canonical residue modulo
`U_n` is `N`.
But `A_n` is precisely that canonical residue, so `A_n=N` thereafter and (8)
forces every later `h_i=0`. This reproves (12), the relevant specialization of
`L-9801`.

The interface congruence for a suffix `z` is

\[
Y_i+h_iV_i=A_z+j_iU_z.
\tag{21}
\]

If `h_i=0`, nonnegativity of `Y_i`, together with `0<A_z<U_z`, forces
`j_i >= 0`. Applying the suffix cylinder gives

\[
Y_{i+1}=Y_z+j_iV_z.
\tag{22}
\]

Substitution of the exact suffix data yields (14)--(15). After the first
suffix every endpoint is a positive integer, so eventual zero blocks would
contradict well-foundedness of the positive integers. This proves (17), and
(12) then proves
(18). ∎

## Motivation

`L-9831` shows that the exponentially branching abstract tail tree contains
one nested physical carry path. The remaining question is whether its nested
input cylinders converge to one ordinary seed. Formula (9) turns that into a
simple extension-block question, and the endpoint dynamics rules out the only
way an ordinary nonnegative seed could occur.

The obstruction is elementary but global: an ordinary seed would eventually
stop adding high input bits, while each such zero-bit stage strictly lowers a
positive endpoint. Infinitely many stages cannot do both.

## Dependency audit

- Exact H concatenation supplies (20)--(22), all restated here.
- `L-9801` provides the general nested-cylinder stabilization principle; its
  needed special case is reproved.
- `L-9827` supplies the exact suffix cylinder data.
- `L-9831` identifies the blocks with the unique physical mixed-radix path;
  the descent proof itself needs only exact concatenation.
- No empirical H sign claim, phase density theorem, or infinite ordinary
  Collatz orbit is assumed.

## Gap audit

- A nonordinary 2-adic limit is not an admissible marked nonnegative seed.
- The argument does not classify the limit as irrational or transcendental,
  and does not exclude a negative integer or rational 2-adic value.
- It applies to infinite schedules composed solely of `10` and `30`; another
  return architecture may behave differently.
- The Sturmian schedule remains a symbolic renormalized schedule rather than
  a sequence of proved physical first crossings.

## Adversarial tests

- Nonstabilization alone does not exclude negative 2-adic integers; the
  conclusion is stated for ordinary nonnegative initialization.
- The zero-block condition is `h_i=0`, not that a suffix letter equals zero.
  Both suffixes already contain a terminal zero.
- When `h_i=0`, allowing `j_i=-1` would make the input negative because
  `0<A_z<U_z`; canonical endpoint nonnegativity therefore forces `j_i >= 0`.
- A strictly decreasing sequence of real numbers could be infinite. The
  contradiction uses integrality and positivity of every `Y_i`.
- Later Sturmian symbols are externally scheduled after raw contraction; the
  theorem must not be advertised as an infinite first-crossing orbit.

## Remaining uncertainty

None for exclusion of an ordinary nonnegative seed in this nested suffix
construction. The arithmetic type of the limiting 2-adic seed and the design
of a different return architecture that could stabilize at an ordinary point
remain open.

## Suggested next attack

Determine whether the nonzero-block set has positive lower density along the
Sturmian schedule. Any such bound, combined with (9), would quantify ordinary
input growth; stronger residue information might also exclude rational or
negative-integer 2-adic limits.
