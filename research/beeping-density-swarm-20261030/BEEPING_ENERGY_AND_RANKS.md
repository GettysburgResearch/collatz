# The 17-state machine: an exact orbit-energy clock and a rank barrier

**Status: PROPOSED ordinary mathematical results, with independent bounded
replay. Collatz remains unresolved.** The external equivalence was checked
against the literal transition table and its complete-configuration invariant.
The new consequences below have ordinary proofs; they are not proof-assistant
formalizations. No global-priority claim is made.

## 1. What the source actually supplies

The public source is
[Mira-Cult/math, `turing-machines/collatz-beeping17/README.md`](https://github.com/Mira-Cult/math/blob/c465130c54f992c5cf0e5c93c752a79c2e0a7398/turing-machines/collatz-beeping17/README.md),
frozen at `c465130c54f992c5cf0e5c93c752a79c2e0a7398`.
Its literal table is exactly the one in the user-supplied post:

```text
1RL0RB_1LC1RB_0LK0LD_1RE1LD_0RF0RB_0LG0LG_1LH1LG_0RA0RI_1RJ1RI_1RF1RF_0RA1LK_0LM0LM_0LN1LM_1RO1LN_0RA0RP_0RQ1RP_1RL1RQ
```

There are 17 working states, A through Q, with the read-0 transition first in
each row. A transition exits O precisely when a beep is counted. The head
starts at cell zero in A on an all-zero two-sided tape. All 34 transitions are
defined and none halts.

The source now includes an ordinary invariant proof, not only bot notes or
finite simulations. Its central theorem is that the blank run beeps
infinitely often exactly when all positive Collatz inputs converge. A least
counterexample b would cause exactly b(b−1)/2 beeps before permanent silence.
That conclusion includes both a nontrivial cycle and a trajectory with
infinitely many distinct values.

Its global theorem is valid provided its three macro rules are valid. The
independent reconstruction in Section 2 checks those rules, including finite
duration, untouched counter cells, expansion beyond old capacity, and first
return to A. The source's own Lean developments for other machines do not
certify this 17-state table. We did not run or import its simulator.

The relevant OpenAI manuscript is
[Single-fold Diophantine representations](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae/preprints/Single-fold-Diophantine-representations-September-24-2026).
Its first theorem asserts a polynomial representation of any recursively
enumerable set with exactly one complete auxiliary witness for each member.
The manuscript explicitly leaves several fixed arithmetic constants
numerically unspecified. This packet uses neither that theorem nor its
formalization as a premise for any machine or rank claim.

## 2. Complete configurations and independent macro audit

Use the shortcut map

\[
T(v)=\begin{cases}v/2,&v\text{ even},\\(3v+1)/2,&v\text{ odd}.\end{cases}
\]

Let C(n,v,K), for n≥1 and 1≤v≤K, mean:

- state A, head at zero;
- 1s at counter cells −n through −2;
- a zero separator at −1;
- 1s at active cells 0 through K−1 except the zero at v−1;
- all other cells zero.

K records retained capacity. It need not equal the logical value v. The
blank tape is C(1,1,1). The following arrows stop at the **first** subsequent
A, at head zero, and describe the whole resulting tape:

| Source | Target | Exact transitions | Beeps |
|---|---|---:|---:|
| C(n,2k,K), k≥1 | C(n,k,K) | 2k(k+1) | 0 |
| C(n,2k+1,K), k≥1 | C(n,3k+2,max(K,3k+2)) | 5k²+9k+4 | 0 |
| C(n,1,K) | C(n+1,n+1,max(K,n+1)) | 2n(n+2) | n |

### Even arithmetic

After A erases cell zero, maintain a marker at m=i and a value hole at
h=2k−1−i, with B at m+1. Every cell strictly between the two is a 1.
When h−m≥3, B fills the right hole; C moves it one cell left; D fills the
marker; E moves it one cell right. The new holes are m+1 and h−1.
The traversal takes 2(h−m)+1 transitions.

At i=k−1 the two holes are adjacent. B fills the value hole and C reads
the marker zero. C enters K to the marker's left. That region consists of
1s down to the separator, so K returns to A at zero. The remaining hole is
at k−1. Nothing touches the counter or the cells strictly beyond the original
value hole. There is no O, no earlier A, and all scans are finite. Summing
the shuttle lengths gives 2k(k+1).

### Odd arithmetic

Start instead with marker i and hole 2k−i. Nonfinal shuttles work as above.
At distance two, C moves the value hole immediately to the marker's right,
D fills the marker, and E now sees a zero. F, G and H establish a marker at
k−1 and a value hole at k+1, with I immediately right of the marker.

In an expansion round with marker m and hole h, I fills the hole, J fills
h+1, F puts a zero at h+2, G fills m, and H inspects m−1. If m>0, H places
the new marker there; if m=0 it sees the separator and returns to A. Thus
each round moves the hole two places right and the marker one left. There
are exactly k rounds. The final hole is 3k+1 and the value is 3k+2.

At the start of expansion round r, h−m=2+3r. That round costs
2(h−m)+5=9+6r. The k halving shuttles cost 2k²+3k, establishing the
expansion marker costs three, and the initial A costs one. Adding the
expansion cost 3k²+6k gives 5k²+9k+4.

J and F act identically on either read bit. Therefore crossing the old right
boundary does not truncate a trajectory. Newly crossed cells have the stated
1s and final hole, while any farther retained tail is preserved. This is
the point that distinguishes unbounded arithmetic from a bounded cycle
search. Again the counter and separator are intact, all scans are finite,
and O is absent.

### Reset and copy

At v=1, A fills cell zero. L puts a hole at one, M returns to the separator,
and N scans the counter leftward and extends it by one 1. The machine reaches
O at −n after n+4 transitions.

For r=0,…,n−2, the next temporary counter marker is j=−n+r and the active
hole is h=1+r. O erases j and beeps. P crosses the counter to the separator;
Q fills the active hole; L puts the next hole one place to its right; M
returns to the separator; N restores j. O is reached at j+1. The loop
length, obtained by counting the two scans on each side, is

\[
2h-2j+3=2n+5.
\]

After n−1 loops O reaches the separator, beeps once more and returns to A.
The updated counter has n cells and the hole is n. Thus the value becomes
n+1, the tape remains canonical, and retained capacity is max(K,n+1).
The reset takes (n+4)+(n−1)(2n+5)+1=2n(n+2) transitions. The n=1 case
contains no copy loops and initializes the blank tape in six transitions.

These three proofs are uniform in K. The only visited cells are within
[-1,v−1] in an even arithmetic macro, [-1,T(v)−1] in an odd arithmetic
macro, and [-n−1,n] in a reset. Large retained tails are never assumed absent.

### Global equivalence

The machine tests n=1,2,… sequentially and increments n only after the
current trajectory reaches one. Every individual macro finishes in positive
finite time. Consequently all convergent rounds finish, whereas a first
nonconvergent round continues through arithmetic macros without ever
entering O. This proves the source's equivalence and triangular beep count.
Shortcut iteration has the same reaches-one predicate as ordinary Collatz
iteration because its compressed intermediate odd-step value 3v+1 is never
one.

## 3. An exact quadratic energy identity

The following consequence is useful for deciding whether a timing argument
has gained anything over an arithmetic trajectory argument.

Define the arithmetic cost, excluding a reset, by

\[
c(v)=\begin{cases}
v^2/2+v,&v\text{ even},\\
(5v^2+8v+3)/4,&v>1\text{ odd}.
\end{cases}
\]

Put

\[
\Phi(v)=\frac23v^2+2v,\qquad
w(v)=\frac{(v+1)(25v+23)}{12}\quad(v>1\text{ odd}).
\]

**BE-ENERGY.** Suppose the shortcut orbit of n first reaches one at time τ,
and let A(n) be the literal machine transitions spent in arithmetic macros
during that round. Then

\[
\boxed{
A(n)=\Phi(n)-\Phi(1)+
\sum_{\substack{0\le j<\tau\\T^j(n)\text{ odd}}}w(T^j(n)).
}
\]

More generally the same identity holds on any finite arithmetic initial
segment, not crossing the first visit to 1, with the terminal term
−Φ(T^ℓ(n)) instead of −Φ(1). It does not assume that the trajectory eventually
converges. At 1 the actual machine resets, so that reset is a separate macro.

**Proof.** Direct substitution gives

\[
c(v)=\Phi(v)-\Phi(T(v))
\]

when v is even, and

\[
c(v)=\Phi(v)-\Phi(T(v))+w(v)
\]

when v>1 is odd. Summation telescopes. These are rational-polynomial
identities, so there is no probabilistic or asymptotic step. Although Φ
and individual tolls need not be integers, their displayed sum is the
integer transition count. ∎

For example n=3 has shortcut preterminal values 3,5,8,4,2. The arithmetic
costs are 18,42,40,12,4, totaling 116. The energy formula gives the same
116. Its reset costs 30 more transitions.

The result also groups exactly over the usual odd-only accelerated map
A_odd(v)=(3v+1)/2^{ν₂(3v+1)}: the entire odd step and following even run
cost Φ(v)−Φ(A_odd(v))+w(v). Thus changing to an accelerated arithmetic clock
does not discard machine time; it changes it by one explicit potential
difference and one positive quadratic toll.

This is an exact compression theorem for this particular machine, not a
termination theorem. An upper bound on its elapsed time must ultimately
control a positive quadratic sum along the actual odd orbit.

## 4. Exact beep gaps and excursion-time comparison

Let R(n)=2n(n+2). If inputs up through N converge, define

\[
S_N=\sum_{n=1}^{N}\big(A(n)+R(n)\big),\qquad S_0=0.
\]

**BE-SCHEDULE.** After input n finishes, its final beep occurs at literal
transition S_n. Its full burst of n beep times is

\[
S_{n-1}+A(n)+n+5+j(2n+5),\qquad j=0,\ldots,n-1.
\]

In particular the gap from the final beep of input n−1 to the first beep
of input n is exactly

\[
A(n)+n+5.
\]

**Proof.** The first O is entered n+4 transitions into a reset; its exit
beeps one step later. Successive copy loops cost 2n+5, and the last exit
lands exactly at R(n). Add the start time of the reset. ∎

This makes the scheduler's missing obligation explicit. To rule out permanent
silence one needs finite A(n) for every tested input, or another theorem that
forces every round to finish. A positive density of finished arithmetic
inputs does not imply that this sequential scheduler reaches them.

**BE-PEAK.** For a convergent input n≥2 let H(n) be the largest shortcut
value before its first visit to one. Then

\[
\frac12H(n)^2\le A(n)\le
\sum_{v=2}^{H(n)}c(v).
\]

The last sum is explicit. With m=⌊H/2⌋ and r=⌊(H−1)/2⌋, it equals

\[
\frac{m(m+1)(2m+1)}3+m(m+1)
+\frac{5r(r+1)(2r+1)}6+
\frac{9r(r+1)}2+4r.
\]

It is (7/24)H³+O(H²). Hence for this unary machine, finite excursion
height and finite arithmetic runtime differ by at most a cubic bound on a
convergent trajectory.

**Proof.** Every c(v)≥v²/2, and the peak is one of the preterminal values.
A deterministic convergent trajectory cannot repeat a preterminal value:
a repeat would trap it in a cycle without one. Therefore its preterminal
values are distinct members of {2,…,H}, proving the upper bound. Summing
the even and odd quadratic formulas gives the displayed expression. ∎

The convergence hypothesis in the upper bound matters. A nontrivial bounded
cycle repeatedly revisits values; one cannot use a bound on peak height
alone to conclude that a nonconvergent round finishes.

## 5. A finite algebraic rank obstruction that includes retained capacity

The repository already has more specialized but strong finite-feature
obstructions in
[`research/astra-three-routes/pass3/JOINT_ARITHMETIC_RANKS.md`](../astra-three-routes/pass3/JOINT_ARITHMETIC_RANKS.md).
Those concern a positive logarithmic leading term corrected by arbitrary
finite polynomial valuations and residues. The theorem here concerns a
different class: a finite lexicographic tuple of nonnegative quasi-polynomial
functions on the machine's full canonical state space. Its extra coordinate
K does not rescue that template.

Fix M≥1. Call a function of (n,v,K) a quasi-polynomial of period M if, on
each residue class modulo M of those three coordinates, it agrees with a
fixed real polynomial in the coordinates. Only its values on n≥1 and
1≤v≤K matter.

**BE-RANK-BARRIER.** There is no finite tuple

\[
\mathcal R(n,v,K)=(R_1(n,v,K),\ldots,R_d(n,v,K))\in\mathbb N^d
\]

of such quasi-polynomials that strictly decreases in lexicographic order
on every arithmetic macro C(n,v,K)→C(n,T(v),max(K,T(v))) with v>1.
The conclusion still holds if all finitely many small v are exempted.

**Proof.** Take one common period M and fix any n=n₀. For each coordinate
look on the diagonal K=v and the residue class v≡−1 (mod M). Its values
there agree with the polynomial

\[
p_i(x)=R_i(n_0,x,x).
\]

Each p_i is nonnegative at all sufficiently large x≡−1 (mod M). Thus
any nonconstant p_i has positive leading coefficient and is eventually
strictly increasing.

Now take v=2Mt−1 for large t. It is odd and exceeds one; moreover

\[
T(v)=3Mt-1>v,
\qquad v\equiv T(v)\equiv-1\pmod M.
\]

Because K=v, the odd macro ends at K′=T(v); both endpoints lie on the
same diagonal residue class. If every p_i is constant, the tuple is unchanged.
Otherwise choose the first nonconstant p_i. All preceding coordinates are
equal and that coordinate strictly increases for sufficiently large t. Both
possibilities contradict strict lexicographic descent. ∎

The statement extends immediately to a finite piecewise-polynomial template
whose branch is eventually fixed along each diagonal residue class. For
example adding finitely many threshold tests does not change the proof.

### Exact scope, including escape routes

The theorem applies to all canonical inputs, not merely configurations
actually reached from blank tape. The latter restriction may encode much
more arithmetic information, and is not ruled out. It also does not rule
out unbounded adaptive blocks, unbounded valuation/digit information,
nonpolynomial ranks, arbitrary ordinal constructions, or polynomial bounds
on stopping times obtained by other methods. A polynomial describing a
Diophantine relation is not a polynomial rank and is unaffected.

This is a concrete search-space exclusion. It prevents investing in a
state-dependent finite-degree polynomial/finite-residue rank for the whole
canonical machine unless the proposed invariant or macro grouping escapes
the stated domain. It is not evidence that no well-founded proof exists.

## 6. The Diophantine quantifier check

Let Good={n≥1: n reaches one}. This set is infinite unconditionally, since
it contains every power of two. Applying a single-fold theorem directly
to Good would produce an equation with infinitely many complete solutions
whether or not Collatz is true.

The appropriate set is instead

\[
Prefix=\{N\ge1:\text{every }1\le n\le N\text{ reaches one}\}.
\]

This is recursively enumerable: simulate the finitely many inputs, or run
the sequential scheduler. If Collatz is true Prefix is all positive integers;
if its least counterexample is b, Prefix={1,…,b−1}. Therefore **conditional
on a single-fold representation theorem**, a polynomial with parameter N
for Prefix has exactly b−1 complete natural solutions in the false case
and infinitely many in the true case. Use parameter N−1 if the theorem's
parameter domain is all of ℕ including zero.

An equally valid choice is the set of positive beep ordinals for which the
machine emits that beep. It has exactly b(b−1)/2 members in the false case.
Single-foldness controls all witnesses and is essential for this complete
solution count. Ordinary existential Diophantine representation alone can
give infinitely many auxiliary witnesses for even one successful parameter.

Neither encoding bounds the height of witnesses, gives a practical displayed
polynomial, or removes the all-input obligation. The new equation is an
exact logical reformulation; a successful algebraic proof would have to
establish a structural property of that specific representation.

## 7. Reproduction and evidence boundary

Run from the repository root; these commands write only temporary receipts:

```sh
python -B experiments/beeping-density-swarm-20261030/verify_beeping.py --output /tmp/beeping.json
python -O -B experiments/beeping-density-swarm-20261030/verify_beeping.py --output /tmp/beeping-optimized.json
```

The checker uses an independently written set-of-ones tape interpreter that
parses the literal machine. It tests first return to A, head position, whole
tape, exact visited interval, exact time, every reset beep time, and the
triangular cumulative count. It does not import any upstream checker.
Timeout is failure, and explicit checks remain enabled under `python -O`.

Observed normal-mode results:

| Check | Result |
|---|---:|
| Canonical macro cases | 1,068 |
| Literal transitions in those cases | 5,944,690 |
| Largest retained capacity in a case | 10,379 |
| Blank-run completed inputs | 26 |
| Blank-run literal transitions | 62,274 |
| Blank-run completed macros | 231 |
| Blank-run beeps | 351 |
| Arithmetic starts checked for energy/peak identities | 10,000 |
| Largest shortcut height in that arithmetic test | 13,557,212 |
| Largest arithmetic cost in that arithmetic test | 530,752,023,167,038 |

The energy test evaluates shortcut arithmetic, not 530 trillion literal
machine transitions. The literal macro tests and the much faster arithmetic
tests are different evidence tiers. Polynomial coefficient checks establish
the displayed local identities by exact rational arithmetic. They do not
formalize the tape invariant or prove universal termination.

Literal SHA-256 without a trailing newline:
`a63448cf13cfd4180dc4bfbc7f40c127d431440a83ee7743d7b5b8d15e2bc0b1`.
The complete bounded receipt is
[beeping_evidence.json](../../experiments/beeping-density-swarm-20261030/beeping_evidence.json).

## 8. What remains promising and what remains missing

The machine is a good exact interface for proof tools: its unbounded behavior
reduces to three short invariant schemas, and the sequential-prefix rule
already handles both ways Collatz could fail. The strongest practical use
is to formalize the schema once and transport arithmetic certificates to
machine recurrence, rather than expand unary literal traces unnecessarily.

A constructive next target is a **source-restricted or adaptively grouped
energy budget**: a proved total rule that finishes a block with enough
decrease in a well-founded quantity to repay the explicit positive odd toll.
The rule must establish its own termination; “continue until repayment” is
not such a rule. The theorem above rules out the simplest all-canonical
finite polynomial implementation. The existing finite-valuation obstructions
also warn that merely adding finitely many arithmetic features is unlikely
to be sufficient.

The first unsupported step toward a full proof remains a uniform successful
return/repayment statement for every positive ordinary source. Neither the
machine equivalence, its exact energy clock, positive-density convergence,
nor the conditional finite-versus-infinite polynomial reformulation supplies
that statement.
