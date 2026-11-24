# A total paid-return construction for every rational tripling phase

23 November 2026. Published parent PR182 head:
`c369ae3c426ec6aaf9a280ec9578b9910c2147d5`.

**Status: PROPOSED written theorems, finite Lean arithmetic, and exact
ordinary controls. Full Collatz and repeated-return termination remain
OPEN.**

The denominator-eight return mechanism extends to any complete rational
tripling coset. A fixed ordinary source supplies an exact finite budget
for its zero-carry run, through its binary distance from the canonical
rational periodic orbit. The necessary scalar guard then makes the
normalized physical source at least one, so every high step contracts
it by at most 7/16. The result is a total procedure that either rejects
the supplied equality, produces an actual canonical cycle certificate,
or constructs a paid return to a low state with an equivalent equality.
For an expanding canonical word, its rational periodic orbit is negative
and the cycle branch is impossible.

## 1. Actual scalar, complete phase, and source pins

Use the ordinary odd map

\[
2^{g(q)}U(q)=3q+1,\qquad g(q)=v_2(3q+1),\qquad
h(q)=\sum_{i\ge0}\frac{g(U^i q)}{3^{i+1}}.
\]

The parent scalar theorem supplies

\[
\frac12<h(q)\le1+\frac{\log_2q}{3},\qquad
h(Uq)=3h(q)-g(q).                                     \tag{1}
\]

The exact parent sources are:

- `research/repo-synthesis-round8-20261123/GERM_BRIDGE.md`, R8-G1--G4,
  blob `540110f09cf68e3309fd83fea9c7ae497536ded4`;
- `research/scalar-rigidity-round9-20261123/CARRY_RETURN.md`, R9-C2--C3
  and Section 8, blob `0b0d2ff63339522689f9984aad1bae3ab63d9e08`;
- `research/scalar-rigidity-round9-20261123/PHASE_RIGIDITY.md`,
  R9-P1--P5, blob `0fe27307dd075284bc03ac93ce9c40925b45f2bc`;
- `research/scalar-rigidity-round9-20261123/ARITHMETIC_RIGIDITY.md`,
  R9-A1 and R9-A3, blob `2c872eb9818be062e9444fde91555ba4e1e7230f`.

All four paths are read at the published parent head above. No pressure
maximum is selected or moved in this note. The source is the literal
positive odd integer supplied to the procedure.

Fix one reduced rational phase denominator d coprime to three. Let
`p_0,...,p_(L-1)` be the tripling orbit, represented in `(1/2,3/2]`,
and set

\[
b_i=3p_i-p_{i+1}\in\{1,2,3\},\qquad
A_j=\sum_{i<j}b_i,\quad A=A_L.
\]

Indices on p and b are periodic. The starting supplied equality is
`h(q)=p_0`, so its extra integer carry is zero. Every candidate state
has `h_i=p_i+k_i`, and its complete equations are

\[
g_i=b_i+3k_i-k_{i+1},\qquad
2^{g_i}q_{i+1}=3q_i+1.                                \tag{2}
\]

The algorithm updates the candidate by the exact actual gap, never by
choosing a gap from this equation. If d>1, a true candidate avoids one.
The d=1 standard phase is also allowed, with its endpoint at one handled
explicitly.

## 2. The necessary guard supplies a rational lower rank

Put `B=bl(q)`, and retain the exact necessary guards

\[
h>1/2,\qquad 3h\le B+3.                               \tag{3}
\]

Their rational comparisons require no real oracle. Since the candidate
has the prescribed fractional phase, the lower guard makes k a
nonnegative integer.

**R10-P1 (normalized lower rank).** At every candidate state passing
(3),

\[
\boxed{Y=q/2^k\ge1.}                                 \tag{4}
\]

For k=0 this is ordinary positivity. If k>=1, `p>1/2` and the upper
guard give `3k<B+3/2`, hence `3k<=B+1` by integrality. Therefore
`k<=B-1`, and `q>=2^(B-1)>=2^k`. This proves (4) from finite
arithmetic. It does not require that the candidate is the actual
infinite scalar.

Combining both complete equations (2) gives

\[
\boxed{Y_{i+1}=
\frac{3Y_i}{2^{b_i+2k_i}}+
\frac1{2^{b_i+3k_i}}.}                                \tag{5}
\]

The destination carry has canceled. If the source carry is positive,
(4), `b_i>=1`, and `k_i>=1` imply

\[
\boxed{Y_{i+1}\le\frac{7}{16}Y_i<\frac12Y_i.}         \tag{6}
\]

Thus a high run cannot continue through an arbitrary number of states
passing the guards. Starting at a high source s of carry k, put
`J=bl(s)-k>=1`. Since `Y_0<2^J`, J consecutive high transitions whose
endpoints also pass their guards would give `Y_J<1`, contradicting
(4). A low endpoint or sound rejection is reached within J transitions.
For a true actual equality rejection is impossible. This proves a
finite high return directly from the necessary guards; it strengthens
the previous separate all-time W attachment.

## 3. Every paid excursion has a common affine upper bound

Let x be the last low state before a positive carry. Its canonical
charge b must be two or three. The actual entry gap is `b-k'`, with
`1<=k'<=b-1`, but (5) gives the same normalized entry in every case:

\[
E_b(x)=\frac{3x+1}{2^b}.
\]

Every later high step is bounded by the unit-carry map

\[
H(y)=\frac38y+\frac1{16},\qquad
H(y)-\frac1{10}=\frac38\left(y-\frac1{10}\right).       \tag{7}
\]

All these maps are increasing. Since `E_b(x)>=1/2>1/10` for x>=1,
their successive upper iterates decrease. If t>=1 is the number of
high transitions before the first low endpoint r, then

\[
\boxed{r\le\frac1{10}+
\left(\frac38\right)^t\left(E_b(x)-\frac1{10}\right)
\le P_b(x),}                                          \tag{8}
\]

where

\[
\boxed{P_2(x)=\frac{9x+5}{32},\qquad
P_3(x)=\frac{9x+7}{64}.}                               \tag{9}
\]

This is **R10-P2**, valid for arbitrary carries and arbitrary excursion
length. In particular `r<=P_2(x)<=x/3` for x>=3. It is a comparison
with the last low entry source x. It does not automatically compare r
with the earlier source before a long expanding zero-carry run.

The first low endpoint may have a different phase from the initial
one. No unproved low transition is appended to normalize that phase.

## 4. A fixed ordinary source pays for its complete zero-carry run

For the canonical word starting at the supplied phase define its full
affine constant and signed denominator

\[
C=\sum_{i=0}^{L-1}3^{L-1-i}2^{A_i}>0,\qquad
D=3^L-2^A\ne0,\qquad q_*=-C/D.                       \tag{10}
\]

Both C and D are odd. The cyclic shifts of q_* are odd rational
states with precisely the canonical valuations. This follows from
the same full affine identity for each cyclic shift; its numerator is
odd and its denominator is D.

If `Dq+C=0`, q is the canonical rational periodic point. Its ordinary
integrality and literal finite orbit can be checked directly, yielding
a cycle certificate and its exact scalar. If D>0, q_* is negative,
so this branch is impossible for positive q. The standard d=1 phase
at q=1 provides a benign example of the cycle branch.

Otherwise set

\[
\boxed{T=v_2(|Dq+C|).}                                \tag{11}
\]

The number T is finite and positive. Extend the canonical prefix
clocks periodically. There is one index n such that

\[
A_n<T\le A_{n+1};\qquad n\le T-1.                    \tag{12}
\]

Before that index, all actual gaps agree with the canonical word:
the difference from the rational periodic state after i transitions
is `3^i(q-q_*)/2^(A_i)` and has valuation `T-A_i`.

At index n there are two alternatives:

- If `T=A_(n+1)`, the two equal-valuation terms cancel and the actual
  gap is strictly larger than b_n. The propagated scalar is then at
  most one half. This soundly rejects the supplied equality.
- If `A_n<T<A_(n+1)`, the actual gap is `T-A_n<b_n`. The next carry
  is exactly `b_n-(T-A_n)`, either one or two. This is the first paid
  entry.

This is **R10-P3**, an exact ordinary first-departure construction.
In particular the necessary valuation gate is

\[
T\bmod A\ \in\
\bigcup_{0\le i<L}\{A_i+1,\ldots,A_{i+1}-1\}\bmod A. \tag{13}
\]

There is no cutoff or probability claim in this gate. Once it passes,
the zero-carry length and entry carry are calculated from T and the
complete canonical word.

### Explicit total budget and retained affine cost

Let `B_0=bl(q)`. The first high state s is reached after n+1
transitions, so `s<=2^(n+1)q` and `bl(s)<=B_0+n+1`. The high-stage
budget from Section 2 is at most `bl(s)-1`. Consequently the first
paid low endpoint, or a sound rejection, occurs within

\[
\boxed{K(q)=B_0+2T.}                                 \tag{14}
\]

A bound using source height alone is

\[
K(q)\le3\operatorname{bl}(q)+
2\max(\operatorname{bl}|D|,\operatorname{bl}C).        \tag{15}
\]

Indeed `|Dq+C|<=|D|q+C` bounds T by
`max(bl|D|+B_0,bl C)`. The exact valuation budget (14) is usually
smaller.

The zero-carry endpoint is the actual positive integer

\[
x=\frac{3^nq+C_n}{2^{A_n}}.
\]

The returned source therefore satisfies the complete comparison

\[
\boxed{r\le P_{b_n}\left(\frac{3^nq+C_n}{2^{A_n}}\right).} \tag{16}
\]

Both the source-dependent length n and the full affine numerator C_n
remain in this formula. An expanding zero-carry prefix is not treated
as a free change of source.

## 5. A total, equality-preserving one-return transformer

**R10-P4.** The following procedure is total for every supplied positive
odd q and rational canonical phase p_0 with denominator coprime to three.

1. Construct its complete phase cycle, canonical charges, C and D.
2. At one, test the known scalar value one. If `Dq+C=0`, verify the
   literal canonical period and return its cycle certificate.
3. Otherwise compute T. Reject if (13) fails.
4. Replay only actual odd steps, transporting the rational candidate
   by `h'=3h-g`. Reject at a failed guard (3), a nonintegral or negative
   phase carry, or an incompatible endpoint at one.
5. After the first positive carry, stop at the first subsequent zero
   carry. Return its ordinary endpoint and its new canonical phase.
6. If no earlier outcome occurs by (14), reject the original equality.

For a true actual equality, Sections 2 and 4 ensure the procedure
cannot reject. For a returned prefix of length N, whether the supplied
candidate was true or false, exact backward substitution gives

\[
\boxed{h(q)-p_0=3^{-N}(h(r)-p_{N\bmod L}).}            \tag{17}
\]

Thus the equality is equivalent at the returned source. This is a
concrete total transformer, not an assumption that a return exists.
It recognizes a verified canonical cycle separately and never labels
a general paid return as acceptance of the infinite equality.

Repeated use is not proved to terminate. Equation (16) can increase
the original source after sufficiently long zero-carry runs.

## 6. The sharp denominator-1456 phase

Start at `p_0=729/1456`. Its canonical word is

`W = (1,1,1,1,1,1,2,2,2,2,2,3)`.

Direct complete affine calculation gives

\[
L=12,\quad A=19,\quad
C=700273,\quad D=7153,\quad
W(q)=\frac{531441q+700273}{524288}.                    \tag{18}
\]

The necessary gate (13) is exactly

\[
\boxed{v_2(7153q+700273)\bmod19
\in\{7,9,11,13,15,17,18\}.}                          \tag{19}
\]

A true candidate has the initial six actual gaps equal to one, so
`q+1` is divisible by `2^7` and `bl(q)>=7`. Since D has bit length
13 and C has bit length 20, (14) gives the concrete bound

\[
\boxed{K(q)\le3\operatorname{bl}(q)+26.}              \tag{20}
\]

This supplies a finite paid return or rejection for the previously
surviving complete phase. It does not exclude all its repeated returns.

### An explicit same-phase family with a sharp 101/102 threshold

Let

`V = (1,1,1,1,1,1,1,5,2,2,2,3)`.

Its candidate carries are zero except for one unit carry between the
seventh and eighth transitions. It returns to the same scalar phase,
and its exact ordinary map is

\[
V(q)=\frac{531441q+1227505}{2097152}.                   \tag{21}
\]

Set

\[
R=531441/524288,\quad c=700273/7153,\quad
\kappa=-2838855001/117194752,\quad
\alpha_m=\frac{R^{m+1}}4.
\]

Every literal positive ordinary source of the complete word `W^m V`
has endpoint

\[
\boxed{r=\alpha_m(q+c)+\kappa.}                       \tag{22}
\]

**R10-P5.** Every such source descends for `0<=m<=101`, and every
such source expands for `m>=102`.

Here is a proof for the full source class. Its first departure from
the periodic W itinerary is the reduced charge at position `12m+6`,
so `v_2(7153q+700273)=19m+7`. For m>=2 this gives

\[
q\ge(2^{45}-700273)/7153>17958.
\]

The exact rational comparisons

`alpha_101<1<alpha_102`,
`alpha_101*(17958+c)+kappa<17958`, and
`alpha_1*(3+c)+kappa<3`

are checked by integer arithmetic. Monotonicity in alpha, and the
negative coefficient of q when alpha<1, prove descent for m=2 through
101; the last comparison proves m=0 and 1 because q>=3. For m>=102,
`r-q=(alpha_m-1)(q+c)+c+kappa>0`, since `c+kappa>0`.

Every finite word has a complete positive ordinary cylinder by the
parent R9-A3, so both sides of this threshold have literal ordinary
realizations. The claim concerns exactly this W/V family. It is not
a 101-cycle descent theorem for every arbitrary paid return, and it
does not assert that these finite candidates equal the actual infinite
scalar.

## 7. Evidence and remaining fixed-source problem

`general_phase_controls.py` implements the actual-gap transformer,
keeps complete rational candidates and phase carries, and returns its
source budget and affine comparison. Its exact controls cover both
signs of D, the standard cycle branch, composite low phases, arbitrary
finite high paths, the 1456 valuation gate, and the full W/V threshold.
All checks remain active under optimized Python.

`GeneralPhaseReturn.lean` records finite arithmetic for the new
guard-to-rank implication, high-step contraction, and arbitrary-length
affine upper iteration. The actual real scalar input is (1); the
ordinary phase attachment, valuation departure construction, and full
transformer correctness remain the written proof above. The executing
parent records compilation and declaration-dependency auditing.

No new literature theorem is required: the mechanism uses the parent's
actual scalar, exact parity-cylinder arithmetic, and finite affine
inequalities. The absolute mass construction and all-time scalar
rigidity questions are unchanged by merely computing a return.

**First unsupported step:** prove that the sequence of paid returns
from one unchanged positive ordinary source has enough contraction to
terminate, while paying for every intervening canonical expansion and
phase change. The total one-return construction and its linear source
budget make that remaining dynamical question explicit; they do not
settle it.
