# L-9611 — Two-sided boundary phases force an ordinary height floor

**Claim ID:** `L-9611`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-26  
**Dependencies:** the exact negative-three pulse letters from PR #45 `L-8405` / PR #51 `O-8001`; elementary affine composition and CRT  
**Scope:** positive ordinary boundaries between exact words in the negative-three pulse chart  
**Related claims:** `L-9609`, `L-9610`, `T-9609`, `T-9610`

## 1. Primitive ordinary chart

Use

\[
n=6z+1.
\tag{1}
\]

The two exact two-odd-step shortcut-Collatz blocks are

\[
A:\quad 8z'=9z+1,
\qquad z\equiv7\pmod8,
\tag{2}
\]

and

\[
B:\quad 16z'=9z,
\qquad z\equiv0\pmod{16}.
\tag{3}
\]

These are the `y=3z` form of the centered chart used in `T-9608`. Every nontrivial positive physical state in this section has `z>=1`; `z=0` is the trivial physical state `n=1`.

For a finite word

\[
w=w_0\cdots w_{d-1}\in\{A,B\}^d,
\]

write its exact affine data as

\[
\boxed{Q_w z_d=9^d z_0+e_w,}
\tag{4}
\]

where

\[
Q_w=8^{\#A(w)}16^{\#B(w)}.
\tag{5}
\]

The constant may be generated chronologically from

```text
(Q,e)=(1,0)
append A: (Q,e) -> (8Q,9e+Q)
append B: (Q,e) -> (16Q,9e).
```

## 2. Exact source and output phases

Because `9^d` is a unit modulo `Q_w`, every exact realization of `w` starts in the unique source class

\[
\boxed{
\rho(w)=\bigl[-9^{-d}e_w\bigr]_{Q_w}.}
\tag{6}
\]

Because `Q_w` is a unit modulo `9^d`, every exact realization ends in the unique output class

\[
\boxed{
\sigma(w)=\bigl[Q_w^{-1}e_w\bigr]_{9^d}.}
\tag{7}
\]

Only necessity is needed below: an actually replayed word automatically satisfies both congruences.

## 3. Two-sided boundary class

Let `z>0` be a boundary between two exact macro words. Assume the preceding macro has a suffix `u` of length `d`, and the following macro has a prefix `v` of length `d`.

The preceding suffix gives

\[
z\equiv\sigma(u)\pmod{9^d},
\tag{8}
\]

while the following prefix gives

\[
z\equiv\rho(v)\pmod{Q_v}.
\tag{9}
\]

The moduli are coprime. Let

\[
\eta(u,v)
\]

be the least **positive** representative of the unique CRT class in `(8)`--`(9)`. If the least nonnegative representative is zero, use the full modulus `9^dQ_v`.

Define the depth-`d` two-sided phase floor

\[
\boxed{
H_d=\min_{u,v\in\{A,B\}^d}\eta(u,v).}
\tag{10}
\]

Then every positive boundary having at least `d` physical letters on each side satisfies

\[
\boxed{z\ge H_d.}
\tag{11}
\]

This is a finite local certificate with an unbounded consequence: once `(10)` is frozen, `(11)` applies to every occurrence, every macro sequence, and every repetition length.

### Proof

Equations `(8)` and `(9)` follow directly from `(4)` by reducing the last `d` steps modulo `9^d` and the first `d` steps modulo `Q_v`. CRT gives one class. A positive integer in that class is at least its least positive representative, which is at least `H_d`. ∎

## 4. Warm-up at depth five

The minimizing depth-five pair is

```text
past suffix   BAAAA
future prefix AAAAB.
```

Its phases are

\[
\sigma(BAAAA)=6560=9^4-1\pmod{9^5},
\]

and

\[
\rho(AAAAB)=4095=2^{12}-1\pmod{2^{16}}.
\]

The compatible positive integer

\[
2^{12}9^4-1=26{,}873{,}855
\]

satisfies both congruences. The complete 32-by-32 phase table proves no smaller pair exists, so

\[
H_5=26{,}873{,}855.
\tag{12}
\]

This warm-up is not load-bearing for the strongest corollary below; it exposes the mechanism in a human-readable form.

## 5. Exact depth-eight and depth-ten floors

`X-9614` exhausts the complete phase-pair tables with exact integers and separately implemented reconstruction.

At depth eight:

\[
\boxed{H_8=195{,}221{,}131{,}263.}
\tag{13}
\]

The unique first minimizer in lexical enumeration is

```text
past suffix   AABBBBBB
future prefix AAAABBAB
```

with

\[
\begin{aligned}
\sigma(AABBBBBB)&=4{,}251{,}528
                 &&\pmod{43{,}046{,}721},\\
\rho(AAAABBAB)&=68{,}554{,}751
                 &&\pmod{134{,}217{,}728}.
\end{aligned}
\tag{14}
\]

At depth ten:

\[
\boxed{H_{10}=90{,}608{,}969{,}363{,}967.}
\tag{15}
\]

The minimizing pair is

```text
past suffix   ABBAAAAABB
future prefix AAABAAAAAA
```

with

\[
\begin{aligned}
\sigma(ABBAAAAABB)&=1{,}389{,}919{,}581
                   &&\pmod{3{,}486{,}784{,}401},\\
\rho(AAABAAAAAA)&=191{,}803{,}903
                   &&\pmod{2{,}147{,}483{,}648}.
\end{aligned}
\tag{16}
\]

The exact table sizes are

\[
4^8=65{,}536,
\qquad
4^{10}=1{,}048{,}576
\]

ordered suffix-prefix pairs. These are phase certificates, not an orbit or period census.

Frozen ordered-pair digests:

```text
d=5:
f3f9b63a193b89327197132feb2495170ec58af3a1bfda038b5206e82847d4fd

d=8:
ad0dbcdc9608e3c4e699577ca3bc64760749e1dcd5b55f79a1fa485a6ecaf8f1

d=10:
f8dcff96cee68f12563e0fe21876b693dfd20e97d571c9d3760427c99abfa5af
```

## 6. Cycle-minimum coupling

Consider any finite alphabet of fixed-weight macros in the `z` chart. Suppose all macros have common

\[
Qz'=Pz+e_w,
\qquad 0<P<Q,
\tag{17}
\]

and put

\[
D=Q-P,
\qquad e_{\max}=\max_w e_w.
\]

Rotate a positive macro-boundary cycle to a minimum `m`, and write the next boundary as `m+k`, `k>=0`. Then

\[
e_w=Dm+Qk=D(m+k)+Pk.
\tag{18}
\]

Consequently

\[
\boxed{m+k\le {e_{\max}\over D}.}
\tag{19}
\]

If every macro has length at least `d`, the next boundary also satisfies `(11)`. Therefore

\[
\boxed{e_{\max}<H_dD}
\tag{20}
\]

excludes **every** positive cycle over the macro alphabet, for arbitrary macro ordering and arbitrary repetition length.

This is the direct global implication supplied by the phase floor. No finite-prefix extrapolation occurs: a finite phase table proves a theorem about every possible cycle word in the declared macro class.

## 7. Relationship to `L-9610`

`L-9610` extracts the final-letter residue modulo `27` at a cycle minimum.
The present theorem is its full boundary-phase extension:

```text
one terminal letter
  -> one output phase modulo 9;

a length-d past suffix and length-d future prefix
  -> one complete CRT class modulo 9^d times a dyadic source modulus.
```

The terminal theorem supplies a symbolic residue ladder; `L-9611` supplies an
Archimedean lower bound for the actual ordinary boundary. The two statements
are complementary rather than duplicate.

## 8. Gap audit

- `H_d` is a lower bound for positive boundaries, not a claim that the minimizing CRT class extends to an infinite orbit.
- The past and future words must each contain at least `d` letters; shorter macros need a smaller-depth certificate or a separate theorem.
- The two-sided bound concerns exact physical letters, not a relaxed residue automaton.
- A phase-floor certificate excludes cycles through `(20)` but does not decide aperiodic ordinary extraction.
- The exact values `(13)` and `(15)` are computer-assisted finite lemmas with separately written generator and verifier; they are not inferred from numerical approximation.

## 9. Verification

```bash
python3 -B experiments/X-9614-two-sided-phase-floor/run.py \
  --check-results \
  experiments/X-9614-two-sided-phase-floor/results/canonical.json

python3 -B experiments/X-9614-two-sided-phase-floor/verify.py \
  experiments/X-9614-two-sided-phase-floor/results/canonical.json
```

Expected terminal lines:

```text
X-9614 canonical results match
all independent X-9614 two-sided phase checks passed
```

Semantic digest:

```text
296074c8e5f59c11bc1de1c7d0d89084ae79012381ff1d850fb611281fe0cf06
```

## 10. Suggested continuation

The reusable attack is now:

```text
increase d only when the resulting H_d crosses a declared full-class bound;
never report H_d as finite-prefix evidence by itself.
```

The first open fixed-weight layer after `T-9610` begins at `a=244`; closing it requires either a deeper phase certificate or a parameter-uniform lower bound for `H_d`.
