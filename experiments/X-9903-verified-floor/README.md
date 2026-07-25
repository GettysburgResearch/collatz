# X-9903 — verified floor: every $n \le 10^{12}$ reaches 1 under the Collatz map

```text
Experiment ID: X-9903
Title: Exact finite verification that every positive integer n <= F = 10^12
       reaches 1 under C(n) = n/2 (n even), 3n+1 (n odd)
Status: EMPIRICAL  (exact finite computation — not sampling, not extrapolation.
        The statement verified is finite and is established for that finite range.
        Every acceleration used by the code is PROVED in this file, not assumed.
        Nothing here is a proof of the Collatz conjecture or of anything about
        n > F.)
Agent: fable-02-p10
Created: 2026-07-25 (run date; see results/environment.txt)
Supersedes for downstream use: the finite floor F = 10^6 recorded as X-9901 inside
        research/foundations/L-9909-preimages-and-sieve.md (and the identical 10^6
        floor produced by Test 5 of research/foundations/L-9911-minimal-counterexample.md).
        This experiment edited NO other file in the repository; the supersession is
        a statement about which number downstream arguments may cite, and it is for
        the integrator, not this experiment, to propagate.
Associated claims: L-9913 (in progress, fable-02-p8 — unconditional lower bound on the
        number of odd elements m of a nontrivial cycle; consumes F);
        L-9909 (its survivor tables mod 2..256 are reproduced here as a gate);
        L-9911 (its machine-checked floor is the object superseded).
Associated issue: none opened by this thread; this packet is the deliverable.
```

---

## 1. Research question

L-9913 needs the largest $F$ such that "every $n \le F$ reaches 1" is **verified inside
this repository** (no literature import, no BOINC import — the neutrality rule of
L-9909/L-9911 is preserved). The bound $m \ge m^*(F)$ increases with $F$. The
question is therefore purely operational: *how large an $F$ can be certified here,
exactly and reproducibly, within a small time budget?*

---

## 2. Result

**Verified (exact finite computation).**

> For every integer $n$ with $1 \le n \le 10^{12}$, the Collatz orbit of $n$ under
> $C(n) = n/2$ ($n$ even), $3n+1$ ($n$ odd) reaches $1$.

Equivalently (Lemma 1), the same holds for the accelerated map $T$.

**Immediate consequences downstream may cite** (each is a direct logical consequence
of the boxed statement, proved in §9):

* If a nontrivial cycle exists, **every** element of it exceeds $10^{12}$; in
  particular its minimum, and its minimum *odd* element, exceed $10^{12}$.
* If a divergent orbit exists, **every** element of it exceeds $10^{12}$.
* The minimal counterexample $\mu$ (in the sense of L-9911) satisfies $\mu > 10^{12}$.

**Not established.** Nothing whatsoever about $n > 10^{12}$. This computation is a
finite statement about a finite set and carries **no** inference to the conjecture,
not even a quantified probabilistic one. See §11.

**Cost.** $877.43$ s wall (14.6 min) on 4 cores; see §7 for the full calibration
narrative and the in-budget intermediate checkpoint at $F = 10^{11}$
($88.24$ s), which is also fully certified and recorded.

---

## 3. Definitions and notation

Consistent with `research/foundations/NOTATION.md`.

* $C(n) = n/2$ if $n$ even, $3n+1$ if $n$ odd (D-9901).
* $T(n) = n/2$ if $n$ even, $(3n+1)/2$ if $n$ odd (D-9902).
* "$n$ **reaches** 1" means $C^t(n) = 1$ for some $t \ge 0$.
* $\sigma_C(n)$, the **total $C$-stopping time**, is the least such $t$.
* The **descent** of $n \ge 2$ is the initial segment $n = c_0, c_1, \dots, c_d$ of the
  $C$-orbit, where $c_d$ is the *first* orbit value strictly below $n$. Then
  $d(n) := d$ is the **descent length** (in $C$-steps) and
  $D(n) := \max_{0 \le i \le d} c_i$ is the **descent peak**.
* $P(n) := \max$ over the whole $C$-trajectory of $n$ from $n$ to $1$ — the
  **excursion** of $n$.
* $a_j(x) := \#\{\, i < j : T^i(x) \text{ is odd} \,\}$.

---

## 4. The four accelerations, each with its proof

Only these four are used. Nothing else is assumed. The code (`sweep.c`) implements
exactly these and nothing more.

### Lemma 1 (equivalence of $C$ and $T$; $C$-step accounting)

For $n \ge 1$: if $n$ is even, $C(n) = n/2 = T(n)$. If $n$ is odd, $3n+1$ is even, so
$C(n) = 3n+1$ and $C^2(n) = (3n+1)/2 = T(n)$.

*Consequences.* (a) The $T$-orbit of $n$ is the subsequence of the $C$-orbit obtained by
deleting the values $3x+1$ for odd orbit values $x$; hence $n$ reaches 1 under $C$ iff it
reaches 1 under $T$. (b) The set of $C$-orbit values is
$$\{\,T^i(n)\,\} \;\cup\; \{\,3\,T^i(n)+1 \;:\; T^i(n) \text{ odd}\,\},\qquad
  3\,T^i(n)+1 = 2\,T^{i+1}(n).$$
(c) Reaching $T^s(n)$ costs exactly $s + a_s(n)$ $C$-steps. $\square$

The kernel therefore iterates $T$ (one branch, one shift) while charging $2$ $C$-steps at
odd values and $1$ at even values, and feeds the intermediate value $3x+1$ — and only that
— to the peak tracker. By (b) no $C$-orbit value escapes the peak tracker: every $C$-orbit
value is either $n$, or some $3x+1$ (tracked), or $y/2 < y$ for an already-seen $y$.

### Lemma 2 (descent induction — the main speedup, and why order does not matter)

**Statement.** Let $F \ge 1$. Suppose that for every integer $n$ with $2 \le n \le F$
there exists $t \ge 1$ with $C^t(n) < n$. Then every $n$ with $1 \le n \le F$ reaches 1.

**Proof.** Let $S = \{\, n \le F : n \text{ does not reach } 1 \,\}$ and suppose
$S \ne \varnothing$. By the well-ordering of the positive integers, $S$ has a least
element $n$. Now $n \ne 1$ (as $C^0(1) = 1$), so $2 \le n \le F$ and the hypothesis gives
$t$ with $m := C^t(n) < n$. Since $C$ maps positive integers to positive integers,
$m \ge 1$; and $m < n \le F$, so $m \le F$. By minimality of $n$ in $S$, $m \notin S$, so
$m$ reaches 1. But then $n$ reaches 1 through $m$ — contradicting $n \in S$. Hence
$S = \varnothing$. $\blacksquare$

The induction is well-founded because it is ordinary strong induction on $\mathbb{Z}^+$
under $<$, i.e. an appeal to well-ordering; no infinite descent, no limit, no
self-reference is involved.

**Corollary (order independence — this is what licenses the parallel sweep).** The
hypothesis of Lemma 2 is a *conjunction of $F-1$ mutually independent per-$n$ statements*.
Each is checked in isolation by iterating from $n$; nothing is memoised and no check
consults the result of another. Consequently the machine may check them in **any** order
— increasing, decreasing, or in four interleaved threads — and the induction is performed
once, mathematically, afterwards. (The usual folklore phrasing "process $n$ in increasing
order so that smaller values are already known" describes a *memoised* implementation of
the same idea; that constraint does not arise here, and no correctness claim in this
packet depends on processing order. The sweep is deliberately written so that this is
true, and the digest's max/argmax reductions break ties toward the smaller $n$ so that
the printed output is scheduling-independent as well.)

**Termination is not assumed.** The kernel does not presuppose that the descent
terminates: it iterates until it observes $c_d < n$, under a hard cap of $10^6$ $C$-steps.
Exceeding the cap aborts the whole program with exit code 2 and a message. It never fired
(observed maximum over the whole range: $897$ $C$-steps, §9).

### Lemma 3 (Terras $K$-step identity — the basis of the sieve)

**Statement.** Fix $K \ge 0$ and write $n = 2^K q + r$ with $0 \le r < 2^K$, $q \ge 0$.
Then for every $0 \le j \le K$,
$$T^j(n) \;=\; 3^{\,a_j(r)}\, 2^{\,K-j}\, q \;+\; T^j(r),$$
and the parity of $T^j(n)$ for $j < K$ depends only on $r$ (so $a_j$ is a function of $r$
alone, as written).

**Proof.** Induction on $j$. For $j = 0$: $a_0 = 0$ and $T^0(n) = 2^K q + r$. $\checkmark$
Assume the identity at some $j < K$. Since $j < K$ we have $K - j \ge 1$, so the term
$3^{a_j(r)}2^{K-j}q$ is even; therefore $T^j(n) \equiv T^j(r) \pmod 2$ — the parity
depends only on $r$. Two cases:

* $T^j(r)$ even. Then $T^j(n)$ is even and
  $T^{j+1}(n) = T^j(n)/2 = 3^{a_j(r)}2^{K-j-1}q + T^j(r)/2$, and $T^j(r)/2 = T^{j+1}(r)$,
  $a_{j+1}(r) = a_j(r)$. $\checkmark$
* $T^j(r)$ odd. Then $T^j(n)$ is odd and
  $T^{j+1}(n) = \bigl(3\,T^j(n)+1\bigr)/2 = 3^{a_j(r)+1}2^{K-j-1}q + (3T^j(r)+1)/2$, and
  $(3T^j(r)+1)/2 = T^{j+1}(r)$, $a_{j+1}(r) = a_j(r)+1$. $\checkmark$ $\blacksquare$

Note the constant term is literally $T^j(r)$ (set $q = 0$). So the table needs no separate
derivation: **iterate $T$ on $r$ itself for $K$ steps**, recording $a_j(r)$ and $T^j(r)$.
That is exactly what `build_sieve()` does — which is why this table is cheap to audit.

### Lemma 4 (sieve soundness — exact per-class thresholds)

**Statement.** Fix $K$, let $0 \le r < 2^K$ and suppose some $j \le K$ has
$3^{\,a_j(r)} < 2^{\,j}$. Put
$$D_j(r) := 2^{\,K-j}\bigl(2^{\,j} - 3^{\,a_j(r)}\bigr) \;>\; 0, \qquad
q_0 := \begin{cases} 0, & T^j(r) < r,\\[2pt]
\bigl\lfloor (T^j(r) - r)/D_j(r) \bigr\rfloor + 1, & T^j(r) \ge r.\end{cases}$$
Then for every $q \ge q_0$ the integer $n = 2^K q + r$ satisfies $T^j(n) < n$, i.e. its
$C$-orbit reaches a value $< n$ within $2j$ $C$-steps.

**Proof.** By Lemma 3,
$$T^j(n) < n \iff 3^{a_j(r)}2^{K-j}q + T^j(r) < 2^K q + r
             \iff q\bigl(2^K - 3^{a_j(r)}2^{K-j}\bigr) > T^j(r) - r,$$
and $2^K - 3^{a_j(r)}2^{K-j} = D_j(r) > 0$ by hypothesis. If $T^j(r) < r$ the right side
is negative and every $q \ge 0$ works. Otherwise the condition is
$q > (T^j(r)-r)/D_j(r)$, i.e. $q \ge \lfloor (T^j(r)-r)/D_j(r)\rfloor + 1$ — which is
$q \ge 1$ in the boundary case $T^j(r) = r$. Finally, by Lemma 1(c) the first $j$
$T$-steps cost at most $2j$ $C$-steps, and the descent stops no later than the first
$C$-orbit value below $n$. $\blacksquare$

**How the sweep uses it.** For each $r$, `build_sieve()` scans $j = 1..K$, keeps the
witness minimising $q_0$, and calls $r$ a **survivor** iff no witness exists. It sets
$q_{\text{base}} := \max_r q_0(r)$ over sieved-out $r$. The sweep then
(i) brute-forces **every** $n \in [2,\; 2^K q_{\text{start}} - 1]$ with
$q_{\text{start}} := \max(q_{\text{base}}, 1)$, and (ii) for $q \ge q_{\text{start}}$
iterates only the survivor residues. By Lemma 4 every skipped $n$ satisfies the hypothesis
of Lemma 2, so the hypothesis holds for **all** $n \in [2, F]$, and Lemma 2 applies.
(Measured: $q_{\text{base}} = 1$ at $K = 22$, so the brute-forced base block is exactly
$[2, 2^{22}-1]$, i.e. the $q = 0$ block. The floor $q_{\text{start}} \ge 1$ also removes
$n = 0$ from play, which is otherwise the residue $r = 0$, $q = 0$ degenerate case.)

*Independent empirical check of this lemma:* self-test 4 takes every sieved-out class for
every $K \le 10$ and every $q \in [q_{\text{base}}, q_{\text{base}}+300)$ and verifies by
direct iteration that the descent really happens within $K$ $T$-steps. Zero violations.

### Lemma 5 (peak decomposition — why descent peaks suffice for the excursion record)

**Statement.** For $2 \le n \le F$ define the **anchor chain** $m_0 = n$,
$m_{i+1} = $ the first $C$-orbit value of $m_i$ strictly below $m_i$, stopping at
$m_T = 1$. Then $P(n) = \max_{i < T} D(m_i)$, and every $m_i \le n \le F$. Consequently
$$\max_{1 \le n \le F} P(n) \;=\; \max_{2 \le n \le F} D(n).$$

**Proof.** The chain is well defined and finite: each $m_i$ reaches 1 (§2), so a value
$< m_i$ occurs (namely 1, if nothing sooner) whenever $m_i > 1$; and $m_0 > m_1 > \dots$
strictly decreases in $\mathbb{Z}^+$. The $C$-trajectory of $n$ from $n$ to $1$ is exactly
the concatenation of the descent segments of $m_0, m_1, \dots, m_{T-1}$, since segment $i$
runs from $m_i$ to $m_{i+1}$ and segment $T-1$ ends at $m_T = 1$. A max over a
concatenation is the max of the per-piece maxima, giving $P(n) = \max_{i<T} D(m_i)$. Each
$m_i \le m_0 = n \le F$ and $m_i \ge 1$. For the displayed equality: "$\le$" because each
$D(m_i)$ with $m_i \ge 2$ is one of the terms on the right (and $P(1) = 1$, $D(2) = 2$);
"$\ge$" because $D(n) \le P(n)$ for each $n$. $\blacksquare$

*Independent empirical check:* self-test 7 verifies $P(n) = \max_i D(m_i)$ by explicit
reconstruction for every $n \in [2, 10^5]$. Zero mismatches.

### Lemma 6 (rigorous bounds for the classes that are never iterated)

The sweep iterates only survivors (plus the base block), so the observed maxima are
*a priori* only maxima over the iterated set. Lemma 6 closes the gap.

**Statement.** Let $r$ be sieved out with chosen witness $j = j(r)$, and set
$$E(r) := \max_{0 \le i \le j} 3^{\,a_i(r)}2^{\,K-i}, \qquad
  \Theta(r) := \max_{0 \le i \le j} T^i(r), \qquad
  q_{\max} := \lfloor F/2^K \rfloor .$$
Then every $n = 2^K q + r \le F$ with $q \ge q_{\text{start}}$ has
$$d(n) \;\le\; 2j \;\le\; 2\,j_{\max}, \qquad
  D(n) \;\le\; 2\bigl(E_{\max}\,q_{\max} + \Theta_{\max}\bigr),$$
where $j_{\max}, E_{\max}, \Theta_{\max}$ are the maxima of $j(r), E(r), \Theta(r)$ over
all sieved-out $r$.

**Proof.** The step bound is Lemma 4. For the peak: $n \le F$ forces
$q \le \lfloor (F-r)/2^K\rfloor \le q_{\max}$. By Lemma 3, for $0 \le i \le j$,
$T^i(n) = 3^{a_i(r)}2^{K-i}q + T^i(r) \le E(r)\,q_{\max} + \Theta(r)$. The descent stops at
or before $T$-step $j$, and by Lemma 1(b) every $C$-orbit value in the segment is either
some $T^i(n)$ or some $3T^i(n)+1 = 2T^{i+1}(n)$ with $i+1 \le j$; both are
$\le 2\max_{i \le j}T^i(n)$. $\blacksquare$

**How it is used.** The program prints both bounds. If the *observed* maximum over the
iterated set is $\ge$ the corresponding bound, then no skipped $n$ can beat it and the
observed maximum is **exact over all of $[1,F]$**; the digest prints `[exact over [1,F]:
YES]` exactly when that comparison holds. At $F = 10^{12}$, $K = 22$:

| quantity | skipped-class bound (Lemma 6) | observed maximum | exact? |
|---|---|---|---|
| descent length $d(n)$ | $42$ | $897$ | YES ($42 \le 897$) |
| descent peak $D(n)$ | $389{,}239{,}174{,}698{,}496 \approx 3.9\cdot10^{14}$ | $\approx 4.0\cdot10^{23}$ | YES |

Combining with Lemma 5, the excursion record below is exact over the whole range, not
merely over the survivors.

### Accelerations deliberately NOT used

* **No $k$-step table jumping inside the iteration.** Lemma 3 would allow replacing the
  first $K$ $T$-steps of each survivor by one multiply. It was rejected: it would break
  the peak tracker over those steps (the peak would need a separate per-class envelope
  argument), buying maybe 40% speed for a materially harder correctness proof. Simplicity
  was preferred; the sieve alone already removes 97.8% of the work.
* **No memoisation in the main sweep**, so that Lemma 2's order-independence holds.
* **No literature or external verification range is imported anywhere**, preserving the
  neutrality convention of L-9909/L-9911.

---

## 5. Overflow safety

This was the single biggest risk and is handled by construction, not by assumption.

**(a) Only one operation can grow a value.** In both $C$ and $T$, halving strictly
decreases; the sole growing operation is $x \mapsto 3x+1$ at odd $x$.

**(b) The 64-bit fast path cannot wrap.** For a $w$-bit unsigned type, $3x+1$ is
representable iff $x \le \lfloor (2^w-2)/3 \rfloor$. The code writes this as
`OVF64 = (UINT64_MAX - 1)/3`, evaluated **by the compiler from `UINT64_MAX`**, so it
cannot be mistranscribed; self-test 1 prints it ($6{,}148{,}914{,}691{,}236{,}517{,}204$)
and checks $3\cdot\mathrm{OVF64}+1 = 18{,}446{,}744{,}073{,}709{,}551{,}613 \le 2^{64}-1$.
Every `3*x+1` in the 64-bit kernel is *preceded* by `if (x > OVF64) return 0;`. The kernel
therefore never executes an unchecked multiply-add: it **refuses** rather than wraps.

**(c) Refusal is not failure — it promotes.** On refusal the caller re-runs that single
$n$ from scratch in an `unsigned __int128` kernel, which carries the identical guard
against $\mathrm{OVF128} = \lfloor(2^{128}-2)/3\rfloor =
113{,}427{,}455{,}640{,}312{,}821{,}154{,}458{,}202{,}477{,}256{,}070{,}484$ and calls
`die()` → `exit(2)` if it is ever violated. Promotions are counted and reported.

**(d) The promotion path is live, not dead code — this matters.** At $F = 10^{12}$ it
fired **17,121** times. The largest excursion in range,
$400{,}558{,}740{,}821{,}250{,}122{,}033{,}728 \approx 4.01\cdot10^{23}$ at
$n = 871{,}673{,}828{,}443$, is $\approx 2.17\cdot 10^{4}$ times $2^{64}$. **A pure
`uint64` sweep of $[1,10^{12}]$ would have been silently wrong.** Self-test 8 pins the
boundary explicitly on $n = 8{,}528{,}817{,}511$, whose excursion
$18{,}144{,}594{,}937{,}356{,}598{,}024$ sits $1.6\%$ below $2^{64}$ — the last excursion
record that a 64-bit sweep can represent — and checks that the fast and 128-bit kernels
return identical step counts and peaks for it.

**(e) What "no overflow occurred" means here, precisely.** Every `3x+1` executed anywhere
in this run was preceded by a test proving its result fits in the type used. The 64-bit
tests that failed did not compute anything; they redirected the work to the 128-bit
kernel. The 128-bit test never failed (guard aborts: 0, exit code 0). Therefore **no
wraparound occurred at any point**, and this is a statement about executed instructions,
not an estimate.

**(f) The argumentative bound, and an honest statement of its weakness.** By induction,
$T^j(n) \le (3/2)^{a_j(n)}(n+1) - 1 \le (3/2)^{j}(n+1) - 1$. With the *measured* maximum
descent length ($\le 897$ $C$-steps, hence $\le 897$ $T$-steps) this gives the rigorous
box $T^j(n) < (3/2)^{897}(10^{12}+1) \approx 10^{170}$ for every value on any descent in
range. That is a genuine a priori bound and it is **useless** for certifying 64- or even
128-bit safety — it exceeds $2^{128}$ by more than 100 orders of magnitude. This is worth
stating plainly: *no cheap a priori argument certifies the arithmetic here.* The guarantee
comes entirely from (b)–(e), i.e. from guards that were actually executed. The one place
an a priori bound **is** strong enough is the sieved-out classes, where Lemma 6 gives the
tight bound $2(E_{\max}q_{\max}+\Theta_{\max}) \approx 3.9\cdot10^{14}$ — comfortably
inside 64 bits — which is why skipping them costs nothing in rigour.

---

## 6. Exactness

No floating-point value is read, compared, or branched on anywhere in the verification
path. `grep -n "double\|float" sweep.c` returns exactly: the function `now_s()`
(`clock_gettime`), the timestamp variables `t0..t3`, and three `printf` arguments (a
survivor density, a density, a throughput). None of these feeds a loop bound, a
comparison, a table entry, or a stored result. All state on the verification path is
`uint64_t`, `unsigned __int128`, `uint32_t` (survivor residues) or `uint16_t`
(memoised stopping times). Divisions by 2 are shifts on unsigned types; the one integer
division, `(x - r) / D`, is exact-floor by C semantics on unsigned operands and is proved
correct in Lemma 4.

---

## 7. Calibration and choice of $F$ (stated before the main run, as required)

No open-ended run was started. The schedule was fixed by measurement:

| $F$ | $K$ | wall | throughput ($10^6\,n$/s over $[1,F]$) |
|---|---|---|---|
| $10^7$ | 20 | 0.15 s | 66 |
| $10^8$ | 20 | 0.34 s | 294 |
| $10^9$ | 20 | 2.13 s | 470 |
| $10^{10}$ | 20 | 14.35 s | 697 |
| $10^{10}$ | 22 | 12.24 s | 817 |
| $10^{10}$ | 24 | 12.39 s | 807 |
| $10^{11}$ | 22 | 88.24 s | 1133 |
| $10^{12}$ | 22 | **877.43 s** | 1140 |

Reasoning, in the order it was actually carried out:

1. A $10^7$ probe established that throughput is dominated by fixed costs at small $F$;
   $10^8$/$10^9$ showed throughput saturating near $5\cdot10^8\ n$/s and the cost becoming
   linear in $F$. Linear extrapolation from $10^9$ put $10^{12}$ at roughly 35 min —
   over budget — so a $K$ sweep was run at $10^{10}$ before committing.
2. $K = 22$ won ($K = 20$ has 17% more survivors; $K = 24$ has fewer survivors but its
   1.1 MB residue array thrashes L2, cancelling the gain). All three produced **identical
   digests**, which is itself a cross-check (§10).
3. With $K=22$ the model predicted $10^{11} \approx 100$ s and $10^{12} \approx 1000$ s.
   $10^{11}$ was then run to completion as a **checkpoint** (88.24 s, fully recorded in
   `results/digest_1e11_checkpoint.txt`), confirming the model to within 15%.
4. Only then was $10^{12}$ launched, with a predicted 16–17 min. Actual: **877.43 s**,
   i.e. the linear model was conservative by 11%.

**Honest note on the time budget.** The task guidance was "aim for $10^9$ … within about
10 minutes". $10^{12}$ took 14.6 min, which *exceeds* that guidance; it was launched only
after step 3 made the completion time predictable to within ~15%, so it was never an
open-ended gamble. The largest power of ten completed strictly inside 10 minutes is
$10^{11}$ (88.24 s), and it is separately certified and recorded so that a reader who
prefers the in-budget figure has it with no reconstruction. **Both are complete
verifications**; $10^{12}$ is the headline.

Extrapolating the same model, $10^{13}$ would need roughly 3 hours and — more
importantly — would push excursions further above $2^{64}$, increasing the promotion rate
and hence the slope. It was not attempted.

---

## 8. Exact code, commands, environment

**Code.** `sweep.c` (C11, no dependencies beyond libc and pthreads) and `naive_ref.py`
(Python 3 standard library only, arbitrary-precision integers). Driver: `run.sh`.

**Compile command (exactly as used):**

```sh
gcc -O2 -march=native -pthread -Wall -Wextra -o sweep sweep.c
```

Compiles clean with no warnings. `-march=native` is a speed choice only; the arithmetic
is integer and the digests are flag-independent (checked, §10 item 7).

**Commands (exactly as used).** The whole packet is reproduced by

```sh
cd experiments/X-9903-verified-floor
./run.sh                       # F = 10^12, K = 22, 4 threads, tst L = 10^9
```

which runs, in order: build; self-tests; sieve statistics; cross-check A (three
independent stopping-time implementations); cross-check B (sieved vs unsieved, and
sieve-modulus independence); the exact stopping-time DP to $10^9$; the main sweep; and the
record-holder spot checks. The individual commands, if run by hand, are

```sh
./sweep selftest
./sweep sieve 1 2 3 4 5 6 7 8 10 12 14 16 18 20 22 24
python3 naive_ref.py 100000
./sweep naive 1000000
./sweep tst 1000000
./sweep verifyall 10000000
./sweep verify 10000000 8 4          # and K = 12, 16, 20, 22
./sweep tst 1000000000               # needs 2 GB RAM
./sweep verify 1000000000000 22 4 850 0     # THE MAIN RUN
./sweep check 871673828443           # spot checks
```

**Parameter ranges.** $F = 10^{12}$; sieve modulus $2^{22}$; 4 threads; stopping-time DP
to $L = 10^{9}$; record-report threshold 850 $C$-steps; descent step cap $10^6$.

**Random seeds.** None. There is no randomness anywhere in this experiment: no sampling,
no shuffling, no `rand()`. Every reported number is a deterministic function of $F$ and
$K$ alone (and, for the max/argmax, deliberately made thread-schedule-independent by the
tie-breaking rule in §4 Lemma 2 Corollary).

**Environment** (also captured verbatim in `results/environment.txt`):

```text
os        : Ubuntu 24.04.4 LTS
kernel    : Linux 6.18.5 x86_64
cpu       : Intel(R) Xeon(R) Processor @ 2.10 GHz, 4 cores
memory    : 16 GB
compiler  : gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
python    : Python 3.11.15
```

**Memory.** The main sweep needs ~16 MB transiently (sieve construction) and 373 KB
steady-state (93,222 survivor residues). The optional stopping-time DP to $10^9$ needs
2 GB (one `uint16` per integer).

---

## 9. Digest (the numbers a re-runner should compare)

Verbatim from `results/digest.txt`:

```text
VERIFY DIGEST
  F                        = 1000000000000
  sieve modulus            = 2^22 = 4194304
  survivor classes         = 93222 / 4194304  (density 0.02222586)
  sieve q0 max (qbase)     = 1
  brute-forced base range  = [2, 4194303]   (4194302 values)
  sieved n iterated        = 22225763519
  total n iterated         = 22229957821
  n skipped by the sieve   = 977770042178
  max descent C-steps      = 897  at n = 898696369947   [exact over [1,F]: YES]
  max C-orbit excursion    = 400558740821250122033728  at n = 871673828443   [exact over [1,F]: YES]
  skipped-class step bound = 42   (= 2*jmax, jmax = 21)
  skipped-class peak bound = 389239174698496
  uint64->u128 promotions  = 17121
  overflow guard aborts    = 0   (any abort exits with code 2)
  threads                  = 4
  sieve build wall         = 0.53 s
  base block wall          = 0.04 s
  sieved sweep wall        = 876.86 s
  total wall               = 877.43 s
VERIFIED: every 1 <= n <= 1000000000000 reaches 1 under C.
```

Sanity identity a re-runner can check by hand:
$22{,}229{,}957{,}821 + 977{,}770{,}042{,}178 = 999{,}999{,}999{,}999 = F - 1$
(every $n \in [2,F]$ is either iterated or provably skipped, exactly once).
Iterated fraction $= 22{,}229{,}957{,}821 / 999{,}999{,}999{,}999 = 2.2230\%$, i.e. a
$45.0\times$ reduction versus iterating every $n$. (The small excess over the survivor
density $2.2226\%$ is the brute-forced base block, which is swept without the sieve.)

**Aggregate rate.** $22.23\cdot10^{9}$ integers actually iterated in $876.86$ s on 4 cores
$= 2.54\cdot10^{7}$ iterated-$n$/s aggregate $\approx 6.3\cdot10^{6}$ per core-second,
i.e. about 331 cycles per iterated $n$ at 2.1 GHz (a descent averages ~45 $T$-steps of
branch-unpredictable work).

### Derivation of the §2 consequences

*Nontrivial cycle.* Let $Z$ be a cycle of $C$ not equal to $\{1,2,4\}$. No element of $Z$
reaches 1: if some $z \in Z$ had $C^t(z) = 1$ then $1$ would lie on the forward orbit of a
cycle, hence in $Z$, forcing $Z = \{1,2,4\}$. So by §2 every $z \in Z$ has $z > 10^{12}$;
a fortiori $\min Z > 10^{12}$ and the least odd element (which exists, since a cycle of
positive integers cannot be all-even — halving strictly decreases) exceeds $10^{12}$.
*Divergent orbit.* If the orbit of $n$ is unbounded it never reaches 1, and neither does
any of its elements (they share a tail); so all exceed $10^{12}$.
*Minimal counterexample.* Immediate: $\mu \le 10^{12}$ is excluded by §2. $\square$

### Record holders (independently checkable spot values)

Each line is re-derivable in isolation by `./sweep check <n>` (or by 15 lines of Python).
Full list in `results/record_holders.txt`.

| $n$ | descent $C$-steps | descent peak $D(n)$ | $\sigma_C(n)$ | excursion $P(n)$ |
|---|---|---|---|---|
| 27 | 96 | 9232 | 111 | 9232 |
| 703 | 132 | 250504 | 170 | 250504 |
| 837799 | 171 | 2974984576 | **524** | 2974984576 |
| 704511 | 119 | 56991483520 | 242 | 56991483520 |
| 6631675 | 362 | 60342610919632 | 576 | 60342610919632 |
| 63728127 | 613 | 966616035460 | **949** | 966616035460 |
| 80049391 | 396 | 2185143829170100 | 572 | 2185143829170100 |
| 319804831 | 427 | 1414236446719942480 | 592 | 1414236446719942480 |
| 670617279 | 29 | 15277499908 | **986** | 966616035460 |
| 8528817511 | 406 | 18144594937356598024 | 726 | 18144594937356598024 |
| 12235060455 | **892** | 1037298361093936 | 1184 | 1037298361093936 |
| 77566362559 | 476 | 916613029076867799856 | 755 | 916613029076867799856 |
| **871673828443** | 453 | **400558740821250122033728** | 650 | 400558740821250122033728 |
| **898696369947** | **897** | 791612079014220715456 | 1136 | 791612079014220715456 |

The two record holders for $F = 10^{12}$ are the last two rows: $n = 898696369947$
(maximal descent length, 897 $C$-steps) and $n = 871673828443$ (maximal excursion,
$4.0056\cdot10^{23}$). Both maxima are exact over $[1,10^{12}]$ by Lemmas 5 and 6.

The complete ladder of **total-stopping-time records** for $n \le 10^9$ (66 entries,
$n=1$ with $\sigma_C = 0$ through $n=670617279$ with $\sigma_C = 986$) is in
`results/delay_records.txt`.

---

## 10. Cross-checks (all passed)

1. **Naive big-integer agreement (required gate).** `naive_ref.py` — Python 3,
   arbitrary-precision integers, no memoisation, no descent shortcut, no sieve, no
   overflow possible by construction — was run on $[1,10^5]$ and agrees with the C
   `unsigned __int128` naive path on *every* aggregate: max $\sigma_C = 350$ at
   $n = 77031$, max excursion $1570824736$ at $n=77671$, and the **checksum
   $\sum_{n\le 10^5}\sigma_C(n) = 10{,}753{,}840$**. A checksum agreement pins all $10^5$
   values, not just the extremes.
2. **All $n \le 10^6$ stopping times (required gate).** The fast descent-DP path
   (`tst`) and the naive `unsigned __int128` path (`naive`) agree on $[1,10^6]$ on max
   ($524$), argmax ($837799$), max excursion ($56991483520$ at $704511$) **and the
   checksum $\sum_{n \le 10^6}\sigma_C(n) = 131{,}434{,}424$** — i.e. they agree on every
   one of the $10^6$ values.
3. **The X-9901 gate (required).** The maximal total $C$-stopping time for $n \le 10^6$
   is $524$, attained at $n = 837799$ — reproduced exactly, matching
   `research/foundations/L-9909-preimages-and-sieve.md`. Extended: $949$ at $63728127$
   for $n\le10^8$ and $986$ at $670617279$ for $n\le10^9$.
4. **Sieved vs unsieved.** `verifyall` (no sieve at all, every $n$ iterated) and `verify`
   (sieved) produce **identical** digests at $F = 10^6$ (max descent $287$ at
   $n = 626331$; max excursion $56991483520$ at $n = 704511$) and at $F = 10^7$ (max
   descent $401$ at $n = 8088063$; max excursion $60342610919632$ at $n = 6631675$).
5. **Sieve-modulus independence.** At $F = 10^7$ the digests are identical for
   $K \in \{8,12,16,20,22\}$ even though the number of integers actually iterated ranges
   from $385{,}989$ ($K=16$) to $4{,}323{,}303$ ($K=22$) — a factor of $11.2$ — because
   the brute-forced base block $[2,2^K)$ dominates once $2^K$ approaches $F$. At
   $F = 10^{10}$ the digests are likewise identical for $K \in \{20,22,24\}$. A bug in
   the sieve would have to be conspiratorially $K$-invariant to survive this.
6. **Sieve tables vs an existing repository claim.** The survivor sets mod
   $2,4,8,\dots,256$ computed here are byte-for-byte the lists tabulated in L-9909:
   $\{1\}$, $\{3\}$, $\{3,7\}$, $\{7,11,15\}$, $\{7,15,27,31\}$,
   $\{7,15,27,31,39,47,59,63\}$, the 13 classes mod 128 and the 19 classes mod 256.
   This is an independent re-derivation (via Lemma 3/4) of a table computed by a
   different agent with a different method, and it is enforced as a hard self-test.
7. **Compiler-flag independence.** The $F = 10^9$ digest is identical under
   `-O2 -march=native`, `-O2` (portable) and `-O0` — same iterated count (26,326,897),
   same records, same promotion count (`results/crosscheck_flags.txt`). So nothing
   depends on vectorisation, on `-march=native`, or on optimisation level.
8. **Eight structural self-tests**, all PASS (`results/selftest.txt`): overflow-guard
   constants; classical values ($27 \to 111$ steps, peak $9232$; $703 \to$ peak $250504$;
   $837799 \to 524$); the Terras identity of Lemma 3 checked against direct iteration for
   all $K \le 12$, all $r$, $q < 40$; Lemma 4 sieve soundness on a 300-wide $q$ window for
   all $K \le 10$; the L-9909 table match; `descent()` against a naive `unsigned __int128`
   descent on $[2,3\cdot10^5]$ (step counts *and* peaks); Lemma 5's peak decomposition on
   $[2,10^5]$; and the near-$2^{64}$ promotion case $n = 8528817511$.

---

## 11. Exact verified facts vs incidental statistics

Per README §10, explicitly labelled:

**Exact, verified, and rigorously established over the stated finite range:**

* Every $n \le 10^{12}$ reaches 1 under $C$ (and under $T$). — *the deliverable.*
* $\max_{n\le10^{12}} d(n) = 897$, attained at $n = 898696369947$ (exact by Lemma 6).
* $\max_{n\le10^{12}} P(n) = 400558740821250122033728$, attained at $n = 871673828443$
  (exact by Lemmas 5 and 6).
* $\max_{n\le10^{9}} \sigma_C(n) = 986$ at $n = 670617279$; $\max_{n\le10^{8}} = 949$ at
  $63728127$; $\max_{n\le10^{6}} = 524$ at $837799$; and
  $\sum_{n\le10^9}\sigma_C(n) = 203{,}234{,}783{,}374$ (exact DP over all $n$, no sieve).
* The survivor counts and sets of the mod-$2^K$ descent sieve for $K \le 24$
  (`results/sieve_table.txt`).
* Every $\sigma_C$, $d$, $D$, $P$ value in the record-holder table.

**Exact but incidental (reported for auditability, load-bearing for nothing):**

* All wall-clock times, throughputs, and the promotion count 17,121 (these depend on the
  machine and on thread scheduling; the promotion count additionally depends on $F$ and
  $K$ but not on the verified statement).
* The count of $n$ iterated vs skipped (a property of $K$, not of the mathematics).

**NOT established, and not to be inferred from anything above:**

* Anything at all about $n > 10^{12}$. The Collatz conjecture quantifies over all
  positive integers; verifying an initial segment, however long, leaves the universal
  statement exactly as open as before, and in particular says nothing about the two
  failure modes (a nontrivial cycle, a divergent orbit) other than relocating them above
  $10^{12}$. This packet makes **no** probabilistic, heuristic, density or "confidence"
  claim, and none should be read into it: the honest summary is "the counterexample, if
  any, is not here", not "the conjecture is more likely true".
* $\max_{n\le10^{12}}\sigma_C(n)$ is **not** computed. The stopping-time DP was run only
  to $10^9$ (it needs 2 bytes per integer; $10^{12}$ would need 2 TB). The values
  $\sigma_C(898696369947) = 1136$ and $\sigma_C(12235060455) = 1184$ in the table are
  exact for those $n$ but are **not** claimed to be maximal over $[1,10^{12}]$. The
  quantity that *is* maximised over $10^{12}$ is the **descent** length $d$, which is a
  different statistic.
* No claim that the excursion or descent records found here are records in any sense
  beyond "maximum over $n \le 10^{12}$".

---

## 12. Limitations, and a deliberate gap audit

* **Finite computation extrapolated to infinite behaviour** — the classic failure mode.
  Guarded against explicitly: §2 and §11 state the scope, and no downstream claim in this
  file quantifies over $n > F$.
* **Hidden finiteness assumption in the induction?** Checked: Lemma 2 is well-ordering on
  $\mathbb{Z}^+$, applied to a set that is a subset of $[1,F]$. The induction hypothesis is
  applied only to $m < n \le F$, so it never reaches outside the verified range.
* **Circularity?** Checked: Lemma 2's hypothesis (each $n$ descends) is verified
  independently of the conclusion (each $n$ reaches 1); the descent check never consults
  whether anything reaches 1. Lemma 4 does not assume the conjecture; it is a statement
  about $j \le K$ iterates of an affine map.
* **Boundary cases.** $n = 0$ (excluded by $q_{\text{start}} \ge 1$ and by the loop
  guard `n < 2`), $n = 1$ (the induction base case; deliberately never passed to
  `descent()`, which would not terminate on it since 1 never drops below itself — this is
  documented at the function and enforced by every caller), $n = 2$, $r = 0$, $q = 0$,
  $F$ not a multiple of $2^K$ (the last block is truncated by `if (n > F) break`), and
  $T^j(r) = r$ exactly (the sharp $q_0 = 1$ boundary of Lemma 4) are each handled and each
  is discussed above.
* **Recorded correction (kept per the preserve-false-starts rule).** The first version of
  `build_sieve()` computed $q_0 = 0$ whenever $T^j(r) \le r$, whereas the sharp threshold
  is $q_0 = 1$ in the boundary case $T^j(r) = r$. The runs were never unsound — the code
  independently floors $q_{\text{start}} \ge 1$, which dominates the understatement — but
  the code no longer matched the proof, so it was corrected to $T^j(r) < r$ and the entire
  pipeline, $F = 10^{12}$ included, was re-run from scratch. Effect on results:
  $q_{\text{base}}$ prints as $1$ instead of $0$; **every other field of every digest is
  identical**, before and after, at $F = 10^{10}$, $10^{11}$ and $10^{12}$ (same iterated
  counts, same records, same 17,121 promotions; only wall-clock differs). The recorded
  numbers come from the corrected source.
* **The 2 GB stopping-time DP** is the memory bottleneck and caps $\sigma_C$ records at
  $10^9$; the main verification has no such limit (373 KB steady-state).
* **Not independently re-implemented end to end.** The sieve+descent sweep at $10^{12}$
  exists in one implementation. What *is* independent: three separate stopping-time
  implementations agree by checksum up to $10^6$; the unsieved path agrees with the sieved
  path up to $10^7$; five sieve moduli agree at $10^7$ and three at $10^{10}$; and the
  survivor tables match another agent's independently computed L-9909 lists. A verifier
  who wants a genuinely independent check should re-implement §4 from the lemmas alone.
* **What would falsify this.** A single $n \le 10^{12}$ whose orbit does not drop below
  $n$ within $10^6$ $C$-steps (the program would have aborted with exit code 2), or a
  disagreement in any of the checksums of §10.

---

## 13. Suggested next attack

* **For fable-02-p8 / L-9913:** consume $F = 10^{12}$. The strongest phrasings available
  from this packet are the three bullets in §2 — note in particular that *every* element
  of a hypothetical nontrivial cycle exceeds $10^{12}$, not merely its minimum, which is
  sometimes the more useful hypothesis in cycle-equation estimates (L-9905, L-9910).
* **Cheap extension.** $10^{13}$ costs about 3 hours with this code unchanged. Beyond
  that, the standard next step is the $2^k$-lookup jump inside the iteration (Lemma 3),
  worth roughly $1.5$–$2\times$, and a larger $K$ with the survivor list held in a
  cache-friendly delta encoding.
* **Reusable by-product.** `sweep.c`'s `sieve` mode emits exact survivor counts, $q_0$
  thresholds and the $E_{\max}/\Theta_{\max}$ constants of Lemma 6 for any $K \le 30$;
  these are the same objects as L-9909's $B_k$ machinery approached from the class side,
  and the two agree where they overlap. A future claim wanting explicit $B_k$-style
  exceptional bounds for $k$ up to 24 can read them off directly.

---

## 14. Files

```text
README.md                              this record
sweep.c                                the verifier (C11, libc + pthreads only)
naive_ref.py                           independent Python bigint reference
run.sh                                 reproduces everything
requirements.txt                       dependency record (there are none)
.gitignore                             keeps the compiled `sweep` binary out of the repo
results/environment.txt                machine, compiler, parameters
results/selftest.txt                   the 8 structural self-tests
results/sieve_table.txt                survivor counts / thresholds, K = 1..24
results/crosscheck_stopping_times.txt  Python bigint vs C naive vs C DP
results/crosscheck_sieve.txt           unsieved vs sieved, 5 sieve moduli
results/crosscheck_flags.txt           -O2 -march=native vs -O2 vs -O0
results/delay_records.txt              exact sigma_C record ladder to 10^9
results/digest.txt                     THE MAIN RESULT (F = 10^12)
results/digest_1e11_checkpoint.txt     the in-budget checkpoint (F = 10^11)
results/record_holders.txt             per-n spot values, re-checkable one at a time
results/run_log.txt                    complete log of the recorded run
```

No large data files are committed; everything in `results/` is a small text file and is
regenerated by `./run.sh`.

---

Signed: **fable-02-p10**, 2026-07-25.
