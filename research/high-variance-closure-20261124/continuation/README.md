# A fixed measure, a proper multiscale score and the remaining ordinary estimate

**Collatz remains OPEN.** This continuation follows the checked checkpoint
`273e5433a4b16a17998ad98d92549ee06896abff`. It pursues the remaining reset
step and an explicit measure chosen independently of convergence. The
ordinary series criterion is now formalized in Lean. Its universal
finiteness has not been proved.

## 1. One explicit measure and a complete fixed-source criterion

Let the positive shortcut map be \(T(n)=n/2\) at even inputs and
\((3n+1)/2\) at odd inputs. Let \(P_k(n)\) count its odd inputs before
clock \(k\), and define

\[
A_k(n)=\frac{2^{k+P_k(n)}}{3^k}.
\]

For **every positive ordinary integer** \(n\), Lean proves

\[
\{A_k(n):k\ge0\}\text{ is bounded}
\quad\Longleftrightarrow\quad
\sum_{k\ge0} A_k(n)<\infty
\quad\Longleftrightarrow\quad
\exists j,\ T^j(n)=1.
\]

The forward arithmetic is explicit. If \(n\) never reaches 1, every
state is at least 20, by the previously checked finite base. On every
prefix the formalized estimate gives

\[
2^{3k}(T^k n)^3\le n^3 2^{5P_k(n)},\qquad
A_k(n)^5\ge\frac{(256/243)^k}{n^3}.
\]

The individual terms then grow exponentially. If \(n\) reaches 1,
their eventual multiplier is \(8/9\) every two clocks, proving
summability. Both cases are in the Lean proof, including the existential
physical hitting statement. This is a formal equivalence, **not a proof
that the series is finite for all positive integers**.

There is a measure fixed in advance behind the series. Assign independent
shortcut parity bits with odd probability \(2/3\). The unique dyadic
probability measure \(\mu\) thereby specified has cylinder masses
\(2^{P_k(n)}/3^k\), so a written layer-sum argument gives

\[
V(n):=\int_{\mathbf Z_2}2^{v_2(n-r)}\,d\mu(r)
=1+\frac12\sum_{k\ge1}A_k(n).
\]

Thus finite potential for this specific measure is exactly ordinary
convergence. The measure is atomless and singular to dyadic Haar; its
choice uses no unknown stopping times. The measure construction and
integral identity remain written mathematics.

Writing \(S(n)=\sum_{k\ge0}A_k(n)\), its exact recurrences are

\[
S(2n)=1+\tfrac23S(n),\qquad
S(2n+1)=1+\tfrac43S(3n+2).
\]

A finite nonnegative supersolution of these two inequalities on all
positive integers would bound all partial sums and complete Collatz.
No such ordinary supersolution was found. The attempted real/adic
separation has a precise limitation: for every finite set of primes,
every positive floor and every prescribed finite parity prefix, there
is a nonintegral positive rational passing those local integrality tests,
following that prefix, staying above the floor forever and having infinite
potential. Denominator-one arithmetic is still required.

[Measure, arithmetic obstruction and missing supersolution](BIASED_PARITY_MEASURE.md)
· [Full fixed-source Lean theorem](lean/BiasedParity.lean).

## 2. Repairing simultaneous resets while retaining a proper score

The earlier [sparse section](../SPARSE_RESET_MEASURE.md) supplies a total
computable rank with a debit outside its marked valleys. A finite bank of
phase-shifted versions can all reset simultaneously on arbitrarily long
ordinary expanding blocks. The present construction changes the marking
architecture instead.

Take increasingly high tails \(A_j\) of the sparse image and wrap their
first \(j-l\) actual forward steps into a level \(M_l\). Then
\(T(M_l)\subset M_{l-1}\). A source can refill only its highest active
level. The cutoffs also separate the physical starts of marked blocks,
including blocks whose membership is witnessed by a different ordinary
ancestor. The physical upper density of their union is at most \(1/4\)
along **every** positive orbit.

This permits the proper, computable integer toll

\[
b_*(n)=\min_{T^k(m)=n}
\left(m+\#\{i<k:T^i(m)\notin M_1\}\right).
\]

All finite searches defining it terminate because every orbit has
infinitely many unmarked dates. Its sublevel sets are finite. It obeys

\[
b_*(Tn)\le b_*(n)+\mathbf1_{n\notin M_1},
\]

so this proper toll never increases on a marked edge. It repairs the
earlier log-height toll's failure on the growing family \(7\cdot3^m\).

Let \(t_l(n)\) be the actual time to level \(M_l\), 1, or an explicitly
enumerated sufficiently small cycle, and choose the stated rapidly
decaying weights. The resulting proper finite score

\[
R_*(n)=4\sum_l w_l t_l(n)+W_1 b_*(n),
\qquad W_j=\sum_{l\ge j}w_l,
\]

has debit at least \(3W_1\) off \(M_1\) at each nonperiodic source.
At a nonperiodic marked source with highest level \(J\), its exact debit
is

\[
4\bigl(W_{J+1}-w_Jt_J(Tn)\bigr)
+W_1\bigl(b_*(n)-b_*(Tn)\bigr).
\]

The last term is nonnegative. **The remaining return-time term has not
been paid for.** At periodic sources the displayed expression is only an
upper bound, because the additional finite-cycle killing conditions may
intervene. Their presence does not exclude a nonstandard cycle.

The construction makes that boundary test a finite rational calculation
at each supplied source. It does not prove that every required boundary
passes it. [Complete wrapped construction and exact deficit](MULTISCALE_CLOSURE.md).

## 3. Reset frequency can pay growing relative costs, if a potential supplies them

For the actual original sparse physical set \(S\), fixed two-logarithm
bounds and a rational-grid argument give some effective \(p>0\) such
that every sufficiently high true block of length
\(\lfloor\sqrt{\log(n+2)}\rfloor\) has at most

\[
O\!\left(\sqrt{\log n}\,(\log n)^{-p}\right)
\]

visits to \(S\). The estimate holds uniformly over ordinary starting
points. It does not assume independent future gaps.

On any one escaping orbit \(X_i\), for each \(0<\delta<p\),

\[
\sum_{\substack{i<N\\X_i\in S}}
\frac{(\log(X_i+2))^\delta}{\log(X_i+2)}
=o\!\left(\sum_{i<N}\frac1{\log(X_i+2)}\right),
\]

and the sum on the right diverges. A nonnegative finite potential paying
the corresponding physical debit would force every positive orbit into
one fixed finite interval, including any cycle lying entirely above it.
Identifying cycles that meet the interval would still need a finite check.
The required potential inequality remains open.

The candidate tests were continued past the first failure. Exact reset
accounting shows that an ordinary first-hit clock refunds its accumulated
credits at a reset. A centered high-frequency sawtooth sum has a genuine
integer-exact positive correction, but its proposed global debit fails
on expanding ordinary valleys with endpoint phases approaching the same
one-sided limit. The proofs distinguish finite witnesses from a single
escaping source throughout.

[Quantitative frequency theorem](QUANTITATIVE_RESETS.md)
· [Physical costs and fixed-basin oscillation](RESET_COSTS.md)
· [Simultaneous resets and compression](SIMULTANEOUS_RESETS.md)
· [Exact phase correction and its failed global estimate](SAWTOOTH_RESETS.md).

## Verification

The continuation replay compiles the exact pinned `QuarterShift.lean`
dependency and the new `BiasedParity.lean` from copied sources in an empty
directory, with warnings treated as errors. It audits all five public
declarations in each, separating the five new declarations from the five
previously checked dependency declarations. Two exact finite controls run
in normal and optimized Python.

```sh
python -X utf8 -B research/high-variance-closure-20261124/continuation/checks/replay.py \
  --lean /path/to/lean-4.34.1/bin/lean \
  --mathlib /path/to/mathlib \
  --receipt /tmp/ordinary-series-replay.json
```

**The measure, multiscale score, physical-density theorem and analytic
candidate tests are not Lean formalized.** The new Lean theorem proves the
series/hitting equivalence and its arithmetic estimates. It does not
establish universal summability. Exact receipts and the independent review
are under `reports/2026-11-24-high-variance-closure/continuation/`.
