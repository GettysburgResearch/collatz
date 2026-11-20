# What the inverse-potential closing bounds assert

**PROPOSED, unconditional equivalences using the local forward-defect proofs.**
None of the closing bounds is proved here. This note separates the exact
logical boundary from the useful estimates that led to it.

Use the shortcut map, the odd map, and the full inverse supremum from
`PROOF.md`:

\[
W(z)=\sup\bigl(\{0\}\cup\{8k-5A:
\text{a legal }k\text{-edge inverse word of cost }A\text{ from }z\}\bigr).
\]

Every intermediate state and the terminal state is a ternary unit. The
ordinary domain below is exactly the positive odd integers prime to three.
Put

\[
\ell=\log_2 3,\qquad c_*=3/\log_2(3/2)>5,\qquad
K=\frac{c_*-5}{\ln\ell}>\frac14,
\]

and let \(\mathcal B\) be the actual basin of 1. Natural logarithms are
used in \(K\) and in the log-log term below. Finiteness of \(W(1)\) is an
all-word supremum statement, not a claim about a single inverse policy.

## 1. Finiteness at one controls its whole basin

**Proposition.** If \(W(1)<\infty\), then

\[
\boxed{W(n)\le5\log_2 n+W(1)+1
\quad(n\in\mathcal B,\ n\text{ odd},\ 3\nmid n).}   \tag{1}
\]

This conclusion is restricted to the basin. No estimate on a hypothetical
different component is included.

**Proof.** For a unit \(t\in\mathcal B\), let \(d(t)\) be its first-hit
shortcut time and \(a(t)\) its number of odd inputs before that hit.
The reversed ordinary path is a legal inverse word from 1. Appending any
inverse word from \(t\), and then taking the supremum, gives

\[
W(t)\le W(1)+5d(t)-8a(t).                           \tag{2}
\]

This proves actual finiteness throughout the stated basin domain.

For each positive odd ternary unit \(t<33\), exact finite arithmetic gives

\[
5d(t)-8a(t)-5\log_2t\le1.                          \tag{3}
\]

The complete finite data are listed below. There is no numerical logarithm
in their verification: putting \(q=5d(t)-8a(t)\), the check is
\(2^{q-1}\le t^5\) when \(q>1\), and is immediate when \(q\le1\).

For any other \(n\) in the basin, take its first odd-orbit value \(t<33\).
Before that visit, the proved forward inequality in `PROOF.md`, Section3,
makes \(R=W-5\log_2 n\) strictly increase. In particular
\(R(n)\le R(t)\). Equations (2) and (3) imply (1). QED.

| \(t\) | \(d(t)\) | \(a(t)\) | \(q=5d-8a\) |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 5 | 4 | 1 | 12 |
| 7 | 11 | 5 | 15 |
| 11 | 10 | 4 | 18 |
| 13 | 7 | 2 | 19 |
| 17 | 9 | 3 | 21 |
| 19 | 14 | 6 | 22 |
| 23 | 11 | 4 | 23 |
| 25 | 16 | 7 | 24 |
| 29 | 13 | 5 | 25 |
| 31 | 67 | 39 | 23 |

## 2. Equivalent closing statements

Fix any real \(\alpha<K\). The following statements are equivalent:

- **H5:** There is a real constant \(C\) such that
  \(W(n)\le5\log_2n+C\) at every positive odd ordinary ternary unit.
- **Hcritical:** There is a real constant \(C\) such that
  \(W(n)\le c_*\log_2(n+1)+C\) on that domain.
- **Hloglog(\(\alpha\)):** There is a real constant \(C\) such that

  \[
  W(n)\le c_*\log_2(n+1)
       +\alpha\ln\!\bigl(1+\log_2(n+1)\bigr)+C       \tag{4}
  \]

  on that domain. Its right side is finite at every point, including 1.
- **C+F:** Collatz holds and \(W(1)<\infty\).

**Proof.** H5 implies Hcritical immediately. Hcritical implies Collatz by
the finite-cycle and escaping-orbit arguments in `PROOF.md`, Sections4–5.
It also gives \(W(1)<\infty\) upon evaluation at 1. Conversely, under C+F
the basin domain in (1) is the whole required ordinary domain; (1) proves
H5 with \(C=W(1)+1\).

H5 also implies Hloglog(\(\alpha\)) for any fixed real \(\alpha\), after
enlarging the additive constant if necessary. Indeed

\[
c_*\log_2(n+1)-5\log_2n
 +\alpha\ln\!\bigl(1+\log_2(n+1)\bigr)
\longrightarrow+\infty,
\]

since \(c_*>5\), so this expression has a finite lower bound on the
positive ordinary domain. Conversely, the escaping-orbit lower bound in
`LOGLOG_GROWTH.md` is

\[
\liminf_{j\to\infty}
\frac{W(n_j)-c_*\log_2(n_j+1)}{\ln\ln n_j}\ge K.
\]

The ratio of the logarithm in (4) to \(\ln\ln n\) tends to 1. Thus (4)
with \(\alpha<K\) excludes escape; its pointwise finiteness excludes
nontrivial cycles by `PROOF.md`, Section4. It also makes \(W(1)\) finite.
This proves Hloglog(\(\alpha\)) implies C+F and completes the equivalence.
QED.

Thus the coefficient-\(c_*\) formula is pointwise more permissive than the
coefficient-5 formula when their constants are held fixed. The existential
global statements are nevertheless equivalent. They should not be described
as logically strictly weaker conjectures. This applies also to the concrete
log-log coefficient \(\alpha=1/4\).

The same conclusion holds for an eventual bound
\(W(n)\le c_*\log_2(n+1)+o(\ln\ln n)\), provided finiteness is explicitly
required at the remaining finitely many positive odd units. The forward
growth theorem then gives C+F, while H5 implies such an eventual bound with
the error term identically zero.

## 3. The unresolved obligation

The proved reductions do not establish C+F. In particular:

- Haar-almost-everywhere finiteness of \(W\) does not imply \(W(1)<\infty\).
- A finite-cost certificate selecting one inverse path does not bound the
  supremum over all legal inverse words in \(W\).
- Knowing that each terminating ancestor reaches 1 does not bound
  \(\sup(8k-5A)\) uniformly over all those ancestors and paths.
- The basin estimate (1) cannot be applied to an integer whose membership
  in the basin is the question to be proved.

The proposed global bound packages Collatz together with the additional
unproved worst-case inverse-cost statement \(W(1)<\infty\). This note does
not determine whether Collatz alone implies that additional statement, and
therefore makes no claim of a strict logical strengthening of Collatz.

## Verification

The exact eleven checks in (3) are independently implemented in
[check_persistent_defects.py](../persistent-defect-classes/check_persistent_defects.py), function `check_forward_closing_fixture`.
They all pass. The equivalences and basin reduction are proved above;
finite checks are not a substitute for any proposed global estimate.
