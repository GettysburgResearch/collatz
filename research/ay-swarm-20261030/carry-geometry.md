# Carry chambers, exact digit flux, and a guarded natural-number order

**Status:** PROPOSED mathematical lemmas with proofs and exact executable checks;
independent review pending. This is an exploratory packet, not a Collatz proof.
The formulas concern one finite positive ordinary integer at a time. There is no
passage from compatible finite strings to an ordinary infinite trajectory.

The starting point is the mixed binary/ternary SRS of Emre Yolcu, Scott Aaronson,
and Marijn J. H. Heule, *An Automated Approach to the Collatz Conjecture*,
[arXiv:2105.14697v3](https://arxiv.org/html/2105.14697v3), and its
[rule file at 8a4dfda60f97a6d33ff0a24fdfa7a172d4bec340](https://github.com/emreyolcu/rewriting-collatz/blob/8a4dfda60f97a6d33ff0a24fdfa7a172d4bec340/rules/collatz-T.srs).
The base-conversion cells and Collatz equivalence are theirs. We derive the
run-level flux, exact source guard, critical-event accounting and compressed
implementation below. No claim of external mathematical priority is made.

## 1. What this changes

The six binary/ternary exchange rules implement a three-state carry transducer.
Its carry may travel through an arbitrarily long alternating binary corridor.
The **order** of the long and singleton runs determines which corridors create
or remove binary 1s. Keeping only the number of critical `ag -> fa` applications
loses this information: one such application can increase the accelerated
output's popcount by an arbitrarily large amount.

There is nevertheless an exact, inexpensive positive result. Write `s(n)` for
binary popcount and `r(n)=v2(n+1)` for the trailing-1 run length of an odd integer.
The natural-number rank

\[
K(n)=\binom{s(n)}2+r(n)
\]

strictly decreases on an explicit source language recognized by a two-state
run scanner with one signed counter. The guard is **maximal for this rank**:
the scanner decides exactly whether `K(U(n))<K(n)`, without constructing
`3n+1` or following a future orbit. It strictly extends the easy no-`00` source
language. It does not cover every integer and is not forward invariant.

The supplied run transducer also evaluates the exact ordinary Collatz macro on
run lengths too large to expand into a binary string. This preserves the full
ordered run lengths for the next order-search pass instead of truncating them
to finite residue or digit-count summaries.

## 2. Maps and boundary conventions

The shortcut map is

\[
T(n)=n/2\quad(n\text{ even}),\qquad T(n)=(3n+1)/2\quad(n\text{ odd}).
\]

For positive odd `n`, use the accelerated odd map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

The arithmetic convention has `U(1)=1`; termination arguments kill state `1`.
The SRS word for binary `1 b_(L-2)...b_0` is `c` followed by the remaining
binary symbols (`a=0,b=1`) and `d`. Thus `cd` is terminal. A normalized odd
macro starts with `bd -> gd`, moves this ternary digit left using the six
exchange rules, applies one `ce/cf/cg` rule at the `c` boundary, and then uses
`ad -> d` to remove all even factors. For `n>1` this realizes `U(n)` exactly.

All binary words below are canonical and finite. Runs are read from least to
most significant bit; a positive odd input starts and ends with a 1-run.

## 3. Exact carry law

Let `n=sum_i b_i 2^i`, where `b_0=1`, `b_(L-1)=1`, and bits outside
`0,...,L-1` are zero. Put `b_(-1)=0` and `c_0=1`. Schoolbook addition of
`n+2n+1` gives

\[
d_i=b_i+b_{i-1}+c_i-2c_{i+1},\qquad
c_{i+1}=\left\lfloor\frac{b_i+b_{i-1}+c_i}{2}\right\rfloor.
\]

Here `d_i` are the bits of `3n+1` and every `c_i` is 0 or 1. In particular,

\[
c_{i+1}=\begin{cases}
b_i,&b_i=b_{i-1},\\
c_i,&b_i\ne b_{i-1}.
\end{cases}
\tag{CG1}
\]

An equal pair resets the carry to that bit; an alternating pair transports it.
This explains why a low-boundary change can affect an arbitrarily long upper
alternating corridor.

Define

\[
C(n)=\sum_{i\ge1}c_i.
\]

The sum is finite. Summing the displayed digit equation, including its leading
zero boundary, gives

\[
s(3n+1)=2s(n)+1-C(n).
\]

Removing trailing zero bits does not change popcount, so

\[
\boxed{s(U(n))-s(n)=s(n)+1-C(n).}\tag{CG2}
\]

For example, if the binary word has no `00`, the carry never clears before
the high boundary, so `c_1=...=c_(L+1)=1`, `C=L+1`, and
`s(U(n))=2s(n)-L`. The terminal carry `c_(L+1)` is necessary: dropping it
creates an off-by-one error even at `n=1`.

## 4. Run-level flux theorem

There is an exact version of (CG2) that needs only run lengths truncated at 2.
Initialize a scanner state `h=1` and three counters `P=M=O=0`. For each run
`(bit,length)`, in least-significant-first order:

| Run and incoming state | Counter update | Outgoing state |
|---|---|---|
| Singleton 1, `h=0` | `P += 1` | 0 |
| Singleton 0, `h=1` | `M += 1` | 1 |
| Zero run of length at least 2, `h=1` | `O += 1` | 0 |
| Any other run of length at least 2 | none | its bit |
| Any other singleton run | none | unchanged |

The counters mean:

- `P`: isolated 1s traversed while the carry is zero;
- `M`: isolated 0s traversed while the carry is one;
- `O`: long zero runs that open a new interval of zero carry.

**Theorem CG3.** For every positive odd ordinary integer,

\[
\boxed{s(U(n))-s(n)=P(n)-M(n).}\tag{CG3}
\]

### Proof, including the high boundary

After the first bit of a constant run, (CG1) retains the incoming carry. A
second equal bit resets it to the run's bit. Thus runs of length at least 2
reset the state, while singleton runs retain it, exactly as in the scanner.

Let `Z=L-s(n)` be the number of zero bits and let
`z=L+1-C(n)` be the number of zero carries among `c_1,...,c_(L+1)`. Equation
(CG2) becomes

\[
s(U(n))-s(n)=z-Z.
\]

Partition the word into intervals where the carry is zero. Such an interval
starts at the second zero in a zero run of length at least 2. If it closes, it
closes at the second 1 in a subsequent 1-run of length at least 2. Its initial
zero run contributes one fewer zero carry than zero bits. Its final 1-run
contributes one zero carry before resetting to 1, cancelling that deficit.
Each intervening singleton 1 contributes one additional zero carry; intervening
zero bits contribute one each and cancel their contribution to `Z`. The net
contribution of this interval is therefore the number of its intervening
singleton 1-runs, counted by `P`.

If the zero-carry interval remains open at the most significant end, its final
1-run is a singleton. The extra high-boundary zero carry `c_(L+1)=0` cancels
the initial zero-run deficit, and all its singleton 1-runs contribute to `P`.

Outside these intervals, a singleton zero run contributes a zero bit with no
zero carry, giving `-1`; these are exactly the runs counted by `M`. A longer
zero run starts one of the intervals already accounted for. Thus `z-Z=P-M`.
This proves the formula for both possible high-boundary states. ∎

This theorem is an identity, not an average drift claim. In particular, an
arbitrary rearrangement of the same short/long runs can change the flux because
the incoming carry changes.

There is a useful parametric consequence: replacing any run of length at least
2 by any other length at least 2 preserves `P,M,O` and the popcount defect.
Thus an arbitrary short/long run skeleton determines the defect for an entire
infinite family of ordinary integers. The exact guard below is preserved too:
its only additional question is whether the initial 1-run is a singleton.

## 5. Exact relation to the critical SRS event

In the normalized odd macro, let `t_i in {0,1,2}` be the ternary digit moving
left immediately before crossing input bit `b_i`. Interior exchanges have
`1<=i<=L-2`; `t_(L-1)` is handled by the `c` boundary rule. Initially
`t_1=2`. The exchange table is simply

\[
(b_i,t_i)\longmapsto
\left(t_{i+1},e_{i-1}\right),\qquad
3b_i+t_i=2t_{i+1}+e_{i-1}.
\]

The carry relation is

\[
\boxed{t_i=b_{i-1}+c_i.}\tag{CG4}
\]

It holds at `i=1`; the recursion above and the schoolbook carry recursion prove
it inductively. The rule `ag -> fa` is exactly `b_i=0,t_i=2`, so it occurs at
the first zero of a zero run entered with carry 1. Zero runs are internal to
a canonical odd word, so none is lost at the `c` boundary. Consequently,

\[
\boxed{A(n):=\#(ag\to fa)=M(n)+O(n),}\tag{CG5}
\]

and therefore

\[
\boxed{s(U(n))-s(n)=P(n)+O(n)-A(n).}\tag{CG6}
\]

This is the arithmetic connection to the companion [all-context ten-rule
rank](orders.md). That rank proves termination while `ag -> fa` is absent;
the remaining event-return problem must control what happens when the event
is restored. Equation (CG6) identifies an exact digit budget: event count
alone omits both newly opened zero-carry intervals and isolated-1 debt inside
them. The formula applies to the stated normalized macro, not to arbitrary
interleavings of the eleven SRS rules.

## 6. A natural-number rank and its maximal exact source guard

For odd `n`, set `s=s(n)`, `r=r(n)=v2(n+1)`. Since `1<=r<=s`, the intervals

\[
\left[\binom s2+1,\binom{s+1}2\right]
\]

are disjoint and ordered by `s`. Thus

\[
K(n)=\binom{s(n)}2+r(n)
\]

orders the feature pair `(s,r)` exactly in lexicographic order, with a single
natural number. It is well founded. It is not a proper height rank: infinitely
many integers can have the same value, which does not obstruct a strictly
decreasing-rank termination proof.

If `r>=2`, writing `n=2^r q-1` with `q` odd gives

\[
3n+1=2(3\cdot2^{r-1}q-1),\qquad
U(n)+1=3\cdot2^{r-1}q,
\]

so `v2(3n+1)=1` and `r(U(n))=r-1`. If `r=1`, the positive odd image always
has `r(U(n))>=1`, so this component cannot strictly decrease on a popcount tie.

**Theorem CG7 (maximal source guard).** For every positive odd integer,

\[
K(U(n))<K(n)
\quad\Longleftrightarrow\quad
\left[P<M\right]\ \text{or}\ \left[P=M\text{ and }r\ge2\right].
\tag{CG7}
\]

This follows directly from (CG3) and the preceding tie analysis. It includes
the terminal exception automatically: `n=1` has `P=M=0,r=1` and is not in the
strict guard.

### Positive infinite source families

Every `n>1` with no `00` in its binary word satisfies the guard. If there is
any zero, all zero runs are singleton, the carry stays 1, and `P=0<M`. If there
is no zero, `n=2^r-1` with `r>=2` and the tie component decreases.

Every `n>1` whose 1-runs all have length at least 2 also satisfies the guard.
No singleton 1 can contribute to `P`, while `r>=2`. This includes arbitrarily
long zero runs; for example `51=(110011)_2` maps to `77=(1001101)_2` with
unchanged popcount and `r:2->1`.

More generally, the regular sublanguage

\[
P=0\quad\text{and}\quad(M>0\text{ or }r\ge2)
\]

is recognized with finite state (forbid the positive-charge transition and
remember whether a negative-charge transition occurred). The full exact guard
uses the unbounded counter `M-P`; it need not be replaced by a fixed finite
residue label.

Every consecutive segment of nonterminal `U`-steps satisfying the guard has
length at most `K(n_start)-1`. Hence every positive odd ordinary source either
reaches 1 or leaves this guard within that many steps. Even sources are first
divided by their power of two. This is an exit bound, not a bound
for the subsequent unrestricted orbit.

### Explicit failures of closure and tie shortcuts

- `11=(1011)_2 -> 17=(10001)_2` exits the no-`00` language. Both integers are
  ordinary and the step is exact.
- `25 -> 19` has equal popcount 3 but `r:1->2`; `K:4->5`. A blanket
  nonincreasing-popcount rule with the same tie component is false.
- `37 -> 7` has `P=M=1`, equal popcount 3, and `r:1->3`; `K:4->6`. A matched
  signed carry budget is insufficient on its own.

## 7. One critical event can create unbounded debt

For every integer `m>=1`, define the positive odd ordinary sources

\[
N_m=1+8\frac{4^m-1}{3},\qquad \widetilde N_m=N_m+6.
\]

They have the same long upper alternating corridor; only their three lowest
bits differ. Direct arithmetic gives

\[
T(N_m)=2^{2m+2}-2,\qquad
T(\widetilde N_m)=2^{2m+2}+7,
\]

and therefore

\[
U(N_m)=2^{2m+1}-1,\qquad
U(\widetilde N_m)=2^{2m+2}+7.
\tag{CG8}
\]

The run scanner on `N_m` has

\[
P=m,\quad M=0,\quad O=1,\quad A=1.
\]

Its popcount increases from `m+1` to `2m+1`, by `m`, despite exactly one
critical `ag` event. Its neighbor's output has popcount 4 for every `m>=1`.
Thus the same upper alternating corridor becomes dense or sparse according
to the carry entering from below. There is no constant bound on popcount
damage per critical event.

The identities do not assert termination of the Mersenne targets. Their role
is to retain an infinite exact obstruction to a fixed event-credit budget.
The position and length of the newly opened carry interval are essential data.

## 8. A small obstruction to replacing ordered carry geometry by one counter

Put `z(n)=L(n)+1-C(n)`. Consider any real affine candidate

\[
F(n)=a\,s(n)+b\,z(n)+c\,r(n)+d
\]

that is bounded below on all positive odd integers. It cannot strictly
decrease on every nonterminal `U`-step.

First, `n=2^k+1` for `k>=3` has `(s,z,r)=(2,k,1)`. Lower boundedness therefore
forces `b>=0`. The step `3->5` has features `(2,0,2)->(2,0,1)`, forcing
`c>0`. The steps

\[
9\to7:\ (2,3,1)\to(3,0,3),\qquad
11\to17:\ (3,0,2)\to(2,4,1)
\]

would require

\[
-a+3b-2c>0,\qquad a-4b+c>0.
\]

Adding them gives `-b-c>0`, contradicting `b>=0,c>0`. This excludes precisely
this affine feature family, including arbitrary real coefficients and a
constant offset. It excludes neither an ordered run interpretation, a
nonlinear rank, nor a rank with more independent positional information.
Lower boundedness alone is not sufficient for a real-valued ranking proof;
the obstruction holds already under this weaker necessary condition.

## 9. Compressed implementation and exact next obligation

The [checker and transducer](../../experiments/ay-swarm-20261030/carry_geometry.py)
implements the original six exchange cells. On a constant input bit, the
ternary state reaches its fixed state in at most two transitions, so an
arbitrary run length can be processed by two literal transitions and one
bulk count. The output remains an exact run word, and the high `c` boundary
and subsequent `ad` steps are explicit. Its work is linear in the number
of runs with arbitrary-precision arithmetic on their lengths; it does not
claim constant bit complexity in the encoded lengths.
An input with `R` runs produces at most `3R+3` output runs under this direct
bound: each internal run emits at most three constant pieces and the high
boundary emits at most three. Adjacent equal pieces are merged. The exact
lengths survive in the output, so this compression can be iterated without
replacing ordinary input by a completion or a finite-state abstraction.

The next unresolved step is concrete:

> Construct a well-founded order on the full ordered run words that handles
> a carry interval opened by `ag`, including all intervening singleton runs,
> and proves strict decrease on complete critical-event returns. Its proof
> must allow the unbounded family (CG8), all finite positive source words,
> and the exact high boundary of the transducer.

The signed flux word and its ordered run lengths are a candidate state space;
no decreasing order on that state space is supplied here. A claim that each
event receives a fixed credit is explicitly refuted by (CG8). A claim that the
guarded natural rank alone is global is explicitly refuted by the examples
above. The new identities supply exact transition data and a useful partial
order, not the missing universal argument.

### Executable evidence

From the repository root:

```sh
python -X utf8 -B experiments/ay-swarm-20261030/carry_geometry.py --output experiments/ay-swarm-20261030/carry-results.json
python -O -X utf8 -B experiments/ay-swarm-20261030/carry_geometry.py
```

The artifact records the executed bound, actual source counts, all short/long
run skeletons through eleven runs, 256 ordinary paired-family parameters, four
compressed checks with run lengths around `10^80`, and the exact affine-rank
obstruction. Finite checks support the implementation; the all-integer claims
above rest on the displayed proofs. Parent-level validation and independent
review are recorded separately in the swarm report.

The executed default run checked **32,768 odd sources through 65,535**. The
rank decreased at 18,510 sources; the no-`00` family contributed 2,582 sources
above 1, while the regular `P=0` guard contributed 11,906. All **2,730**
short/long run skeletons through eleven runs passed. Normal and optimized
Python produced byte-identical JSON. These are bounded counts, not asymptotic
densities or a coverage theorem.
