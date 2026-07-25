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

**(e) What "no overflow occurred" means here, precisely.** Every `3x+1` executed on the
**verification path** — `descent64`, `descent128`, `build_sieve`, `run_tst`, `run_naive`:
every routine whose output reaches a digest — is preceded by a test proving its result fits
in the type used. The 64-bit tests that failed did not compute anything; they redirected the
work to the 128-bit kernel. The 128-bit test never failed. Therefore **no wraparound
occurred at any point on the verification path**, and this is a statement about executed
instructions, not an estimate.

*Scope correction (fable-02-v19).* The sentence above originally read "every `3x+1`
executed **anywhere** in this run", which the code does not support: the reporting helpers
`naive_tst()` / `naive_peak()` — used by `./sweep check n` (run.sh stage 8) and by
self-tests 2–8 — perform `3*x+1` with **no** guard. Nothing reachable here can wrap them
(the largest value any of them ever forms is the excursion $4.0056\cdot10^{23}$, about $14$
orders of magnitude below $\mathrm{OVF128}\approx1.134\cdot10^{38}$; the `uint64` helpers in
self-tests 3, 4 and 7 stay below $5\cdot10^{9}$), so no wraparound occurred in them either —
but that is an argument about their inputs, not a guard, and the blanket phrasing overstated
what the code does.

*How "guard aborts = 0" is established.* The `0` in the digest is printed as a literal, not
read from a counter; and `run.sh` pipes every stage into `tee`, so under POSIX `sh` the
driver sees `tee`'s exit status and **cannot** observe a `die()` → `exit(2)` from `sweep`.
The claim holds anyway, by a stronger argument than an exit code: `die()` exits the process
immediately, and *every* digest `printf` in `verify` happens after `pthread_join`, so a
digest printed completely — through its closing `VERIFIED:` line, as `results/digest.txt` is
— is itself a proof that no guard tripped anywhere in the sweep. `run.sh` now asserts the
presence of that line (added by fable-02-v19) instead of relying on an exit status it cannot
see.

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
  **(Partly done — see §15: fable-02-v19 re-implemented §4 from the lemmas and re-verified
  $n \le 10^{10}$ independently. The band $(10^{10}, 10^{12}]$ still rests on one
  implementation, spot-checked but not re-swept.)**
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

---

## 15. Independent verification (fable-02-v19, 2026-07-25)

Adversarial review under README §13, applying README §10. I began from the definitions,
not from the author's confidence, and re-implemented the mathematics before reading the
author's numbers back.

### 15.0 Verdict, and the coverage of this review — READ THIS BEFORE CITING §15

**No defect was found that could make the headline result wrong.** The claim "every
$n \le 10^{12}$ reaches 1 under $C$" is, on the evidence below, correct, correctly scoped,
and correctly proved-modulo-computation. Three wording/instrumentation defects were found
and fixed; all are documented in §15.6 and none touches soundness.

**Coverage of this review — stated explicitly so that no reader overstates its depth:**

* **Structural / mathematical verification: COMPLETE.** All six lemmas of §4 were
  re-derived by hand from the definitions; every overflow guard in `sweep.c` was audited
  line by line on every path; the induction, the order-independence corollary, the sieve
  and the never-iterated-class bounds were checked as proofs, not as claims.
* **Computational re-verification with my own independent implementation covers
  $n \le 10^{10}$** — every integer, contiguously — plus the extra contiguous blocks
  $[1.2\cdot10^{10},\,1.3\cdot10^{10}]$ and $[999\cdot10^{9},\,10^{12}]$, and an
  exhaustive audit of the sieve's soundness over $n \le 10^{8}$. That is $\approx
  1.2\cdot10^{10}$ integers re-verified from scratch, i.e. **1.2 % of $[1,F]$**.
* **The band $(10^{10},\,10^{12}]$ was NOT independently re-swept.** It rests on the
  original run, supported here only by 22 million random spot-checks, by the contiguous
  top block, and by the structural verification of the accelerations. Re-sweeping it
  independently would have cost hours of CPU on a shared 4-core box and was out of budget.
* Therefore: **the floor $F = 10^{10}$ is now independently double-implemented; the floor
  $F = 10^{12}$ is single-implementation with its mathematics independently proved.**
  L-9913 may consume $F = 10^{12}$, but a reader who wants a twice-computed floor should
  cite $10^{10}$.

### 15.1 What I re-ran of the author's own code

| command | result | matches packet? |
|---|---|---|
| `gcc -O2 -pthread -Wall -Wextra` (no `-march=native`) | compiles clean, **zero warnings** | yes |
| `./sweep selftest` | all 8 PASS, 0 failures | yes (`results/selftest.txt`) |
| `./sweep naive 100000` / `naive 1000000` / `tst 1000000` / `tst 10000000` | checksums $10{,}753{,}840$ / $131{,}434{,}424$ / $131{,}434{,}424$ / $1{,}552{,}724{,}831$ | yes (stage 4) |
| `./sweep verifyall 1000000` vs `verify 1000000 K` for $K=8,12,16,22$ | all five digests identical (287 @ 626331; 56991483520 @ 704511) | yes (stage 5) |
| `./sweep verify 1000000000 22 4` | 644 @ 217740015; 1414236446719942480 @ 319804831; 26,326,897 iterated | yes (`crosscheck_flags.txt`) |
| `./sweep verify 10000000000 22 4` | 729 @ 2788008987; 18144594937356598024 @ 8528817511 | yes |

I did **not** re-run the $10^{12}$ sweep (CPU budget; a shared box).

### 15.2 What I re-derived by hand

* **Lemma 3 (Terras).** Re-proved by induction on $j$. The step that matters is that
  $K-j \ge 1$ makes $3^{a_j}2^{K-j}q$ even, so $T^j(n) \equiv T^j(r) \pmod 2$ and $a_j$ is
  a function of $r$ alone. The identity is correctly stated **only for $j \le K$**: at
  $j = K$ the leading term is $3^{a_K}q$, whose parity is not forced by $r$, so the
  induction must stop there — and it does, in both the statement and `build_sieve()`.
* **Lemma 4 (thresholds).** $T^j(n) < n \iff q\,D_j(r) > T^j(r) - r$ with
  $D_j(r) = 2^{K-j}(2^j - 3^{a_j}) > 0$. Both branches check out, and **the equality case
  is handled correctly**: at $T^j(r) = r$ the formula gives $q_0 = \lfloor 0/D\rfloor + 1
  = 1$, which is sharp, since $q = 0$ means $n = r$ and $T^j(r) = r \not< r$. `sweep.c`
  line 219 reads `q0 = (x < r) ? 0 : ((x - r) / D + 1)` — this matches the lemma exactly,
  so the correction recorded in §12 is genuinely in the shipped source. I also confirmed
  the author's claim that the correction changed no result: I measured $q_0 \in \{0,1\}$
  for **every** sieved-out $r$ at **every** $K \le 22$, so $\max_r q_0 \in \{0,1\}$ and
  $q_{\text{start}} = \max(q_{\text{base}},1) = 1$ either way.
* **Lemma 2 + Corollary.** Re-proved. Well-ordering on $\mathbb{Z}^+$; the landing value
  $m = C^t(n)$ satisfies $m \ge 1$ because $C$ maps $\mathbb{Z}^+$ to $\mathbb{Z}^+$, and
  $m < n \le F$, so the induction hypothesis is never applied outside $[1,F]$. No
  circularity: the descent test never consults whether anything reaches 1.
* **Lemma 6.** Re-derived; see §15.4.
* **§9 consequences.** The cycle argument is correct (if $z \in Z$ reached 1 then $1 \in Z$,
  forcing $Z=\{1,2,4\}$), as is "a cycle cannot be all-even" (halving strictly decreases).

### 15.3 My own implementation, side by side

Written from §3/§4 alone, deliberately structurally unlike `sweep.c`: it iterates the
**raw $C$ map** one step at a time (no $T$ acceleration, no 2-step charging), uses
`unsigned __int128` **unconditionally** (no 64-bit fast path, hence no promotion logic to
get wrong), uses **no sieve** and **no memoisation** in the descent modes, and asserts on
every $n$ that the landing value lies in $[1,n)$. Plus an independent Python
arbitrary-precision re-derivation of the sieve, and a pure-Python bigint orbit checker.

| range / quantity | `sweep.c` (author) | independent (fable-02-v19) | agree |
|---|---|---|---|
| $[2,10^7]$ max $d$ | 401 @ 8088063 | 401 @ 8088063 | ✅ |
| $[2,10^7]$ max $D$ | 60342610919632 @ 6631675 | 60342610919632 @ 6631675 | ✅ |
| $[2,10^{10}]$ max $d$ | 729 @ 2788008987 | 729 @ 2788008987 | ✅ |
| $[2,10^{10}]$ max $D$ | 18144594937356598024 @ 8528817511 | 18144594937356598024 @ 8528817511 | ✅ |
| $[2,10^{10}]$ every $n$ descends into $[1,n)$ | asserted via sieve+kernel | **directly iterated, all $10^{10}$, zero failures** | ✅ |
| $\sum_{n\le10^6}\sigma_C$ | 131434424 | 131434424 | ✅ |
| $\sum_{n\le10^7}\sigma_C$ | 1552724831 (685 @ 8400511) | 1552724831 (685 @ 8400511) | ✅ |
| Lemma 5: $\max_{n\le10^6}P(n)$ | 56991483520 @ 704511 (as $\max D$) | 56991483520 @ 704511 (as $\max P$, full orbits) | ✅ |
| $K{=}22$ survivors | 93222 (density 0.02222586) | 93222 (density 0.02222586) | ✅ |
| $K{=}22$ $q_{\text{base}},j_{\max},E_{\max},\Theta_{\max}$ | $1,\,21,\,816293376,\,553230080$ | $1,\,21,\,816293376,\,553230080$ | ✅ |
| L-9909 survivor lists mod $2\ldots256$ | hard-coded in self-test 5 | re-derived from Lemma 3/4 in Python bigint | ✅ |

Additional invariants my implementation emits, for any future re-runner to reproduce
(`sweep.c` does not compute these, so they are new independent digests, not comparisons):

```text
[2, 10^10]      sum of descent C-steps = 52389759307
                sum of descent peaks mod (2^61-1) = 551883662441138380
                sum of landing values mod (2^61-1) = 1021512246452381066
[999e9, 10^12]  max d = 587 @ 999867219711 ; max D = 518372589701178367000 @ 999325521135
                sum of descent C-steps = 5239007077
```

**Record holders.** All 14 rows of the §9 table were recomputed in **pure Python
arbitrary-precision integers** (no fixed-width type anywhere) and every one of the four
columns matches, including the two the review was asked to target:

```text
n = 871673828443 : d = 453, D = P = 400558740821250122033728, sigma_C = 650
                   400558740821250122033728 / 2^64 = 21714.3329  (confirms the 2.17e4 claim)
n = 837799       : sigma_C = 524, P = 2974984576               (confirms the max-TST claim)
n = 898696369947 : d = 897, D = P = 791612079014220715456, sigma_C = 1136
n = 8528817511   : d = 406, D = P = 18144594937356598024, sigma_C = 726
```

**High-range sampling.** 22,000,000 pseudorandom $n$ in $[10^{11},10^{12}]$ (two seeds)
were iterated to $1$ in full, in guarded `unsigned __int128`. All reached 1; no guard
fired; no step cap approached (mean $\sigma_C \approx 278$, max observed 1097).

### 15.4 The three things the review was asked to break

**(a) Overflow safety — SOUND, and the guard predicate is exactly the right one.**

`OVF64 = (UINT64_MAX-1)/3 = 6148914691236517204 = \lfloor(2^{64}-2)/3\rfloor$; then
$3\cdot\mathrm{OVF64}+1 = 2^{64}-3$ fits. In `descent64` the only growing operation sits
inside `if (x & 1u)` and is immediately preceded by `if (x > OVF64) return 0;`. There is
no second odd branch, no `goto`, no early `continue`: the guard is **unconditional and
unbypassable**. On refusal the function returns *without writing* `*steps`/`*peak`, and
`descent()` discards the partial state and recomputes the whole descent from scratch in
`descent128` — so no wrapped or partial value can leak into the statistics.

The load-bearing point is that **the refusal predicate is exactly the predicate that is
needed**, neither weaker nor stronger. The descent peak is $\max(n, \max\{3x+1 : x$ odd on
the orbit$\})$. If every odd $x$ satisfies $x \le \mathrm{OVF64}$ then every $3x+1 \le
2^{64}-3 < 2^{64}$, so the 64-bit path can never *under-report* a peak that ought to exceed
$2^{64}$; conversely a refusal occurs iff some $3x+1 \ge 2^{64}$, i.e. iff $D(n) \ge
2^{64}$. **I confirmed this empirically rather than taking it on trust:** the author's
promotion counter goes $0 \to 2$ between $F = 1.2\cdot10^{10}$ and $F = 1.3\cdot10^{10}$,
and my independent count of $\#\{n \in [1.2\cdot10^{10}, 1.3\cdot10^{10}] : D(n) \ge
2^{64}\}$ is **exactly 2**. So the counter is genuinely instrumented (an
`__atomic_fetch_add` in `descent()`, sweep.c:154), it has the right semantics, and the
promotion path is live. The 17,121 figure at $10^{12}$ was not independently recomputed
(it needs the full sweep) and is in any case labelled incidental in §11 — correctly.

The 128-bit guard is adequate with enormous margin: $\mathrm{OVF128} \approx
1.134\cdot10^{38}$ against a claimed peak of $4.0056\cdot10^{23}$, a factor of $2.8\cdot
10^{14}$. Guards are also present in `build_sieve` (line 203), `run_tst` (line 376) and
`run_naive` (line 426). Zero guard-aborts is established as described in the corrected
§5(e), and `run.sh` now asserts it.

**(b) Descent induction and order independence — SOUND. This is the subtlest step and it
is stated correctly.**

The hypothesis of Lemma 2 is a conjunction of $F-1$ statements, each of which is a property
of $n$ *alone* ("$\exists t\ge1: C^t(n) < n$") and is decided by iterating from $n$ with no
reference to any other $n$'s result. I audited the sweep for shared mutable state that a
worker could *read*: `S.surv`/`S.nsurv` are read-only after `build_sieve()` (built before
`pthread_create`, which establishes happens-before); `cursor` is an atomic work-distribution
counter whose value never enters the arithmetic; `w[i].st` is per-thread and merged only
after `pthread_join`; `g_promotions` is an atomic counter never read by the computation.
Hence no thread's *result* can depend on another's, and processing order is irrelevant.
The contrast the author draws with the folklore "increasing order" rule is exactly right:
that rule exists because a **memoised** implementation makes `check(n)` *consume*
`check(m)` for $m<n$; nothing is consumed here, so the constraint does not arise. The
induction is performed once, mathematically, afterwards.

One caveat worth recording, because it is easy to conflate with ordering: order-independence
does **not** by itself give *coverage*. The induction needs every $n \in [2,F]$ to be either
iterated or provably skipped. That is a separate obligation, discharged in (c).

**(c) The sieve — SOUND, and it cannot skip an unverified $n$.** Verified three ways.

1. *Structurally.* $q_{\text{base}} = \max_r q_0(r)$ over **all** sieved-out $r$, and the
   sweep skips residues only for $q \ge q_{\text{start}} = \max(q_{\text{base}},1) \ge
   q_0(r)$ for every sieved-out $r$. Using the global max rather than the per-class
   threshold is conservative. Every $n > 2^K q_{\text{start}} - 1$ has
   $q = \lfloor n/2^K\rfloor \ge q_{\text{start}}$.
2. *By accounting.* Brute force covers $[2, 2^Kq_{\text{start}}-1]$; the sieved phase covers
   $q \in [q_{\text{start}}, \lfloor F/2^K\rfloor]$ and, within each $q$, all survivor
   residues with $n \le F$ (`if (n > F) break;` is sound because `surv[]` is ascending).
   The digest identity $22{,}229{,}957{,}821 + 977{,}770{,}042{,}178 = F-1$ confirms exact,
   non-overlapping coverage. Skipped fraction $= 97.777\%$, as claimed.
3. *Exhaustively, by direct iteration.* My `cover` audit walked **every** $n \in [2,10^8]$
   at $K = 22$, classified it independently, and for each of the **93,676,341** skipped $n$
   directly iterated the $C$ map to confirm it descends within $2j(r)$ $C$-steps:

   ```text
   base block 4,194,302 + survivors 2,129,356 + skipped 93,676,341 = 99,999,999 = F-1
   zero sieve violations; worst descent among skipped n = 34 C-steps (bound 42)
   ```

**(d) Lemma 6 — SOUND; the reported maxima really are exact over all of $[1,F]$.**

Re-derived: for sieved-out $r$ with witness $j$ and $n = 2^Kq+r \le F$ (so $q \le q_{\max}$),
Lemma 3 gives $T^i(n) = 3^{a_i}2^{K-i}q + T^i(r) \le E(r)q_{\max} + \Theta(r)$ for
$i \le j$; the descent stops at or before $T$-step $j$; and by Lemma 1(b) every $C$-orbit
value in that segment is either some $T^i(n)$ or $3T^i(n)+1 = 2T^{i+1}(n)$ with $i+1\le j$,
both $\le 2\max_{i\le j}T^i(n)$. Hence the factor 2. In the code, `curE` is correctly
initialised to $2^K$ (the $i=0$ term $3^0 2^{K-0}$) and `curT` to $r$ ($=T^0(r)$), and
`bestE`/`bestT` are captured **at** the chosen $j$, so they are maxima over $i \le j(r)$
exactly as the lemma requires; the bound is evaluated in `u128`.

I recomputed the constants from scratch in Python bigint and got the digest's numbers
byte for byte: $E_{\max} = 816{,}293{,}376 = 3^{13}\cdot2^{9}$, $\Theta_{\max} =
553{,}230{,}080$, $j_{\max} = 21$, $q_{\max} = 238{,}418$, step bound $42$, peak bound
$389{,}239{,}174{,}698{,}496$. Since $42 \le 897$ and $3.892\cdot10^{14} \le
4.006\cdot10^{23}$, both `[exact over [1,F]: YES]` flags are justified, and the comparison
direction in the code (`bound <= observed`) is the conservative one.

**(f) L-9909 reproduction — CONFIRMED, and confirmed independently of the self-test.**
Self-test 5 only compares against lists *hard-coded in `sweep.c`*, so on its own it is worth
no more than the transcription. I read `research/foundations/L-9909-preimages-and-sieve.md`
directly and re-derived all eight lists from Lemma 3/4 in my own Python: mod 2 $\{1\}$,
mod 4 $\{3\}$, mod 8 $\{3,7\}$, mod 16 $\{7,11,15\}$, mod 32 $\{7,15,27,31\}$, mod 64
(8 classes), mod 128 (13 classes), mod 256 (19 classes) — exact match, in both the counts
$1,1,2,3,4,8,13,19$ and the class lists.

### 15.5 Scoping (README §10 / §13 item 8) — clean

The boxed claim is confined to $n \le 10^{12}$; §2 and §11 disclaim everything about
$n > 10^{12}$ and explicitly refuse even a probabilistic reading ("the counterexample, if
any, is not here", not "the conjecture is more likely true"). §11's three-way split —
verified finite output / exact-but-incidental / not established — is precisely what §10
asks for, and the placement of each item in it is correct; in particular
$\max_{n\le10^{12}}\sigma_C$ is correctly listed as **not** computed, and the promotion
count is correctly listed as incidental. Finite consistency is not substituted for infinite
existence anywhere. §10's record-keeping requirements (ID, question, code, commands,
parameter ranges, environment, seeds, digest, interpretation, limitations, claim IDs) are
all met. I found no overstatement in the mathematical claims.

### 15.6 Defects found (none affects the headline result)

1. **§5(e) overstated the guard discipline** — "every `3x+1` executed **anywhere** in this
   run was preceded by a test". False as written: `naive_tst()`/`naive_peak()`
   (sweep.c:455–466), reached by `./sweep check n` — which is run.sh stage 8 and which §9
   recommends to readers — and self-tests 2–8 execute `3*x+1` unguarded. No wrap can occur
   for anything reachable here (max value formed $4.0056\cdot10^{23}$ vs
   $\mathrm{OVF128}\approx1.134\cdot10^{38}$; the `uint64` helpers stay under
   $5\cdot10^{9}$), so the *results* are unaffected. **Fixed**: §5(e) rewritten to scope
   the sentence to the verification path and to state the input-range argument for the
   helpers separately.
2. **"guard aborts = 0" was not observable by the driver.** The `0` is a printed literal,
   and `run.sh` (POSIX `sh`, no `pipefail`) pipes every stage into `tee`, so `set -e` sees
   `tee`'s status and a `die()` → `exit(2)` from `sweep` would neither stop the script nor
   be recorded. The claim is nevertheless true by a stronger argument — `die()` exits before
   any digest output, so a digest complete through its `VERIFIED:` line proves no guard
   tripped, and `results/digest.txt` is complete. **Fixed**: §5(e) now states this argument
   explicitly, and `run.sh` asserts the `VERIFIED:` line after the main sweep (verified to
   pass on the recorded `digest.txt`, and `sh -n` clean).
3. **Silent per-thread truncation of the record *lists*.** `stats_add`/`stats_merge` cap
   `hs[]`/`hp[]` at `MAXHITS = 4096` **per worker**, but the `LIST TRUNCATED` warning fires
   only on the *merged* count, so a thread that overflowed its own buffer could be silently
   dropped while the merged total stayed below 4096. Affects the optional record *listing*
   only — `max_steps`/`max_peak`/argmax are separate scalars and are never truncated — and
   at the recorded threshold (850 steps) only 15 hits exist. **Not fixed** (reporting-only;
   fixing it would change `sweep.c`'s output format). Flagged for any future run that
   lowers the threshold.
4. Cosmetic, unfixed: `verify`'s `minpeak` argument is parsed with `strtoull` before the
   `u128` cast, so peak thresholds $\ge 2^{64}$ cannot be requested (the main run used 0);
   and `(qstart << K) - 1` is unguarded against overflow for pathological
   $q_{\text{base}}$ (measured $q_{\text{base}} = 1$ for every $K \le 24$, so unreachable).

**Changes I made to this packet:** the §5(e) rewrite (defect 1 and 2), the §12 bullet
pointing at this section, the `run.sh` `VERIFIED:`-line assertion (defect 2), and this §15.
No result, digest, or `results/` file was altered; `sweep.c` was not modified.

### 15.7 Confidence

* That every $n \le 10^{10}$ reaches 1: **very high** — two independent implementations
  sharing no code, one of them sieve-free and 128-bit throughout, agreeing on extremes,
  argmaxes and checksums.
* That every $n \le 10^{12}$ reaches 1: **high** — the accelerations are proved and I
  re-derived every proof; the sieve is exhaustively audited to $10^{8}$ and structurally
  sound for all $F$; the overflow discipline is correct and its live path is confirmed by an
  exact independent count. The residual risk is not mathematical but the ordinary risk of a
  single un-re-run 877-second computation (silent hardware error, or a bug that is invisible
  below $10^{10}$ and at all five sieve moduli and all three optimisation levels). I judge
  that risk low but not zero, which is why §15.0 distinguishes the two floors.
* That the reported maxima ($d_{\max} = 897$, $P_{\max} = 400558740821250122033728$) are
  exact over $[1,10^{12}]$ **given** the run: **very high** — Lemmas 5 and 6 are correct and
  their constants independently reproduced.

Signed: **fable-02-v19**, 2026-07-25.
