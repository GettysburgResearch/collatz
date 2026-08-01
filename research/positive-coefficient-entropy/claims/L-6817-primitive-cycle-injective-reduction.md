# L-6817 — Every repeated-state FC obstruction reduces to an internally injective first crossing

**Claim ID:** `L-6817`  
**Status:** **PROPOSED / SOURCE-QUALIFIED ONLY IN THE FINAL MECHANICAL COROLLARY**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-08-01  
**Dependencies:** `L-6814`; deterministic shortcut dynamics; `T-6806` only for the mechanical corollary  
**Scope:** canonical first-crossing failures and positive cycles

## 1. A repeated proper state contains a positive cycle

Let

\[
x_t=T^t(r)
\qquad(0\le t\le j)
\]

be a canonical coefficient-first-crossing segment with

\[
x_j\ge r.
\]

If

\[
x_a=x_b
\qquad(0\le a<b<j),
\]

then determinism makes

\[
x_a,x_{a+1},\ldots,x_{b-1}
\]

a positive periodic orbit of period dividing `b-a`.

If `r>1`, this period is nontrivial unless it is the trivial `1 <-> 2` orbit.
The latter cannot occur inside a non-descending segment starting at `r>2`,
because every later occurrence of `1` or `2` lies below `r`.  The word `10`
and source `1` remain the declared trivial boundary.

Thus every nontrivial canonical FC obstruction with a repeated proper state
contains a nontrivial positive cycle.

## 2. Least-period cycles are injective before their endpoint return

Assume a nontrivial positive cycle exists.  Choose one with least positive
period `L`, and rotate it to its minimum state `n`.

The minimum is odd: if it were even, its next shortcut iterate would be
`n/2<n`.

Let the full period contain `q_L` odd steps.  Its exact return equation is

\[
2^L n=3^{q_L}n+A,
\qquad A>0.
\]

Hence

\[
3^{q_L}<2^L.
\]

The coefficient therefore has a first crossing at some time

\[
1\le j\le L.
\]

Minimality of `L` gives

\[
\boxed{
x_0,x_1,\ldots,x_{j-1}
\text{ are pairwise distinct}.}
\tag{1}
\]

Indeed, a repetition `x_a=x_b` with `0<=a<b<j<=L` would produce a positive
period `b-a<L`.

## 3. The first crossing is a canonical failure

`L-6814` applies to the minimum rotation.  If `(r_w,s_w)` is the canonical
pair of its first-crossing word and

\[
n=r_w+t2^j,
\qquad t\ge0,
\]

then minimum-orbit no descent gives

\[
0\le T^j(n)-n
=(s_w-r_w)-t(2^j-3^q).
\]

Therefore

\[
\boxed{s_w-r_w\ge0.}
\tag{2}
\]

The first-crossing word is thus a canonical FC obstruction, and `(1)` makes
it internally injective on all proper physical states.

## 4. Reduction theorem

If any nontrivial canonical FC obstruction exists, then there exists one whose
proper physical states are pairwise distinct.

- If the original segment has no repeated proper state, use it.
- If it has one, Section 1 supplies a nontrivial positive cycle; Sections
  2--3 replace it by the internally injective first crossing of a least-period
  minimum rotation.

Thus every global FC nonexistence proof may restrict without loss to
internally injective canonical first crossings, while retaining the cycle
level `d=0`.

## 5. Mechanical corollary

Suppose the internally injective obstruction from Section 4 is the
upper-mechanical word.  In the proof of `T-6806`, the only branch that prevents
the repeated-factor source floor is equality of the two physical source
states.  Internal injectivity rules out that branch.

Consequently, subject to the finite certificate and quoted logarithmic-form
input of `T-6806`, the upper-mechanical internally injective obstruction
descends.  Hence every surviving nontrivial FC obstruction may be chosen
both

```text
internally injective;
and
nonmechanical.
```

This is the precise reduction required by `T-6812` before applying the
support-corrected envelope.

## 6. Gap audit

- Sections 1--4 are elementary and do not exclude the resulting injective
  obstruction.
- The final exclusion of an injective mechanical word inherits `T-6806`'s
  source qualification.
- The trivial word `10` is deliberately retained.
- No positive cycle or FC obstruction is claimed to exist.
- No proof of FC*, SC*, or Collatz is claimed.
