# R-9601 — Ordinary extraction is not a compactness or growth consequence

Claim ID: `R-9601`  
Title: Finite compatibility extracts an ordinary seed exactly through bounded least roots, and supercriticality does not supply that bound  
Status: `PROPOSED / INDEPENDENT RECONSTRUCTION`  
Authoring agent: `gpt56-pro-04`  
Created: 2026-07-25  
Dependencies: elementary well-ordering and congruence algebra; independently reconstructs the core of draft PRs #56 and #57; uses PR #48 only for the branch-specific transported-cylinder crosswalk  
Scope: all prefix-correct ordinary-seed architectures in the repository; the positive-cycle lane is treated separately  
Related counterexample candidates: none

## 1. The exact quantifier gap

Every finite-prefix construction proves a statement of the form

\[
\forall N\ \exists x_N\in\mathbf Z_{>0}
\quad
x_N\text{ satisfies the first }N\text{ gates}.
\tag{1}
\]

The counterexample objective requires

\[
\exists x\in\mathbf Z_{>0}\ \forall N
\quad
x\text{ satisfies the first }N\text{ gates}.
\tag{2}
\]

The implication `(1) -> (2)` is false.  Finite branching or nested congruences may produce one compatible point of `Z_2`; they do not put that point in `Z_(>0)`.

The valid replacement is the following bounded-minimum theorem.

## 2. Bounded-minimum extraction theorem

Let

\[
S_0\supseteq S_1\supseteq S_2\supseteq\cdots
\tag{3}
\]

be nonempty subsets of `Z_(>0)`, where `S_N` consists of the same initial ordinary seeds satisfying the complete first `N` gates.  Put

\[
m_N=\min S_N.
\tag{4}
\]

Then the following are equivalent:

1. one positive integer survives every depth;
2. `(m_N)` is bounded;
3. `(m_N)` is eventually constant;
4. one finite set of positive integers meets every `S_N`.

If these conditions fail, then

\[
m_N\longrightarrow\infty
\tag{5}
\]

and the complete architecture has no positive ordinary survivor.

### Proof

Nesting makes `(m_N)` nondecreasing.  If `x` belongs to every `S_N`, then `m_N<=x` for all `N`.  Conversely, a bounded nondecreasing integer sequence is eventually constant, say `m_N=m` for `N>=N_0`.  By definition, `m` belongs to every late `S_N`; nesting then places it in every earlier set as well.  The finite-set formulation is equivalent to boundedness.  If a nondecreasing positive-integer sequence is unbounded, it tends to infinity. ∎

## 3. One compatible cylinder

Let

\[
1=M_0\mid M_1\mid M_2\mid\cdots,
\qquad M_N\to\infty,
\tag{6}
\]

and choose canonical compatible residues

\[
0\le R_N<M_N,
\qquad R_{N+1}\equiv R_N\pmod {M_N}.
\tag{7}
\]

Write

\[
R_{N+1}=R_N+a_NM_N,
\qquad a_N\ge0.
\tag{8}
\]

The selected inverse-limit point is a nonnegative ordinary integer if and only if any, hence all, of the following hold:

```text
R_N is bounded;
R_N is eventually constant;
a_N is eventually zero.
```

For signed extraction, it is a negative ordinary integer exactly when

\[
M_N-R_N
\tag{9}
\]

is eventually a fixed positive integer.

Indeed, if `x>=0` realizes every class, then once `M_N>x`, its canonical residue is `x`.  Conversely, eventual constancy realizes the same integer at every earlier depth by compatibility.  The negative case is identical with the upper representative `M_N-c`.

This is the exact ordinary-support inference.  Existence of the `2`-adic limit is automatic and strictly weaker.

## 4. Collatz-native supercritical ghost

The failure is already visible in the raw shortcut-Collatz parity coordinates.

Every finite parity word of length `N` occupies exactly one residue class modulo `2^N`, so every finite prefix has infinitely many positive ordinary representatives.  Consider the computable periodic word

```text
(1110)^infinity.
```

One four-step block is

\[
T^4(x)={27x+19\over16}.
\tag{10}
\]

Its unique infinite parity realization therefore satisfies

\[
x={27x+19\over16},
\qquad
x=-{19\over11}.
\tag{11}
\]

Since the denominator is odd, this point lies in `Z_2`; it is not an ordinary integer.  Its exact orbit is

\[
-{19\over11}
\longmapsto
-{23\over11}
\longmapsto
-{29\over11}
\longmapsto
-{38\over11}
\longmapsto
-{19\over11},
\tag{12}
\]

with parities `1,1,1,0`.

The block multiplier is

\[
{27\over16}>1.
\tag{13}
\]

Thus this single native example has all of the following:

```text
every finite prefix has infinitely many positive ordinary roots;
one exact computable infinite compatible path exists;
every advertised transition is a genuine shortcut-Collatz transition;
the path is supercritical;
any positive ordinary realization would be unbounded;
no ordinary integer realizes the infinite path.
```

Consequently finite compatibility plus exact physical replay plus arbitrarily persuasive conditional growth does not approach ordinary extraction unless an archimedean bound on the pulled-back initial representatives is added.

## 5. Directionality corollary

Forward growth and backward extraction are logically different coordinates.

A theorem of the form

\[
x\in\bigcap_NS_N
\quad\Longrightarrow\quad
\text{the physical orbit of }x\text{ grows}
\tag{14}
\]

places no bound on `(m_N)` and therefore proves nothing about whether the intersection is nonempty.

This applies without qualification to conclusions such as:

```text
quotient doubling after entry;
permanent refund conditional on an infinite path;
primitive-core growth;
fresh-prime turnover;
positive cycle mean;
large finite stack capacity;
positive-density noncanonical lifts.
```

Those results may be correct and useful after extraction.  They cannot substitute for it.

A successful positive proof must establish at least one equivalent item:

```text
sup_N m_N < infinity;
eventual constancy of the canonical pulled-back residue;
eventual zero transported digits;
one explicit finite seed with an all-time inductive invariant.
```

A successful negative proof for a fixed architecture must establish

```text
m_N -> infinity
```

or an equivalent uniform exit/ranking theorem.

## 6. Current architecture disposition

### Corrected doubling-scale phase-34 class

PR #33, with the independent reconstruction in PR #44, crosses the boundary negatively for its frozen corrected 256-transition architecture.  It proves that every compatible infinite directive selects a nonordinary completion.  This is genuine global progress for an exhaustive strict class.

### Fixed six-branch pulse chart

PRs #45 and #50 expose one deterministic rational-base machine.  Let `S_N` be the positive roots whose first `N` canonical digits lie in its six physical digits, and let `m_N=min S_N`.  Then:

```text
m_N bounded/eventually constant
    -> one explicit all-time root
    -> exact replay
    -> a branch-qualified K-candidate;

m_N -> infinity or one empty level
    -> the complete six-branch architecture is eliminated.
```

No current theorem decides this sequence.  Its complexity and non-C-finite barriers constrain a hypothetical root but do not decide extraction.

### Linear-height intrinsic refund

PR #49 proves strong conditional growth and currently describes the finite quotient as manufacturing a future stack.  The plain Euclidean-stack interpretation is not valid: PR #48 `R-8203` exhibits an internal transition with

```text
plain next digit mod 64 = 45,
actual next legality residue mod 64 = 16.
```

The valid repaired object is PR #48 `L-8210`'s transported residue

\[
\Theta_s=[-P_s^{-1}B_s]_{K_s}.
\tag{15}
\]

Ordinary extraction is exactly eventual constancy of `Theta_s`, equivalently eventual zero of its transported digits.  Radix capacity and refund do not prove that criterion.

### Negative-three run core and H renewal

Both programs possess exact ordinary finite-depth cylinders and strong consequences conditional on infinite legality.  Neither supplies a bounded least-root theorem, eventual transported-digit stabilization, or one forever-defined seed.  Reset families and SCCs produce changing finite witnesses, not a fixed ordinary root.

## 7. Cycle-side blocker

The positive-cycle route is finite and does not use the compactness theorem above.  For a valuation word put

\[
D=2^A-3^k,
\qquad
R=C-nD.
\tag{16}
\]

A counterexample certificate requires

\[
D>0,
\qquad R=0,
\tag{17}
\]

followed by exact valuation replay.

Proper-factor divisibility, a compressed word, or a real near-integer is not enough.  PR #50's mixed-place height theorem is a legitimate closure mechanism: sufficiently deep physical dyadic replay, odd-prime divisibility, and a directed real interval can force `R=0`.  Its own audit shows the current near-candidates are many orders of magnitude below the required height budget or fail the first physical branch.

Thus the meaningful cycle target is not another proper factor.  It is one full residual equality, or a height contradiction excluding an exhaustive family of nonzero residuals.

## 8. What is genuinely weaker than Collatz

The logical distinction must be stated accurately.

- Proving `m_N->infinity` for one strict subsystem is genuinely weaker than the Collatz conjecture and eliminates that entire subsystem.
- Proving a full-denominator nonzero-residual theorem for one exhaustive word family is genuinely weaker than Collatz and eliminates that family.
- Proving `(m_N)` bounded is **not** a weaker positive theorem than “Collatz is false.”  It is a restricted sufficient condition that immediately supplies a counterexample once the physical conjugacy is replayed.
- Rewriting “one forever-defined seed exists” as “the minima are bounded” is an exact decision criterion, not by itself a reduction in difficulty.

## 9. Blunt conclusion

The repository is not wholly circular.  It has closed complete strict architectures, independently verified substantial theorem chains, found and repaired false bridges, and developed real full-denominator closure tools.

However, the leading positive divergent-orbit lanes have not reduced their existence problem.  They have isolated it accurately.  Relative to an unconditional counterexample, further finite-prefix depth, branch supply, encoding capacity, or conditional growth is treading water unless it changes the bounded-minimum/eventual-stabilization decision.

The universal extraction inference cannot be supplied because it is false.  The only legitimate next offense is architecture-specific:

```text
choose one exact machine;
prove its least roots are uniformly bounded,
or prove they tend to infinity.
```

For the cycle lane:

```text
cross a complete mixed-place height gate,
or prove a full-denominator obstruction for an exhaustive family.
```

No additional bounded experiment is needed for this conclusion.

## Gap audit

- This result does not decide the least-root sequence of any still-open architecture.
- It does not claim that architecture-specific arithmetic cannot force extraction.
- The supercritical ghost refutes a proof schema, not every seed-first construction.
- The physical six-branch and mixed-place implications retain their branch-qualified source statuses.
- No `K-9600` candidate is produced.
