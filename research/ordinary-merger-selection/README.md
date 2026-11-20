# Ordinary merger selection: constructive branches and the missing cover

**Collatz remains open.** This packet develops actual smaller-parameter
merger certificates, an unbounded family of successful recursive proofs,
and ordinary reductions for the signed-five target set. It also identifies
exactly where those constructions fall short of a universal selector.
All unqualified arguments use the positive shortcut map

\[
T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n.\end{cases}
\]

Write \(x\sim y\) when two finite forward paths have a common endpoint,
allowing different clocks. The complete ordinary descent obligation is:

\[
\forall N>1\quad\exists\,1\le m<N,\ i,j\ge0:
                         T^i(N)=T^j(m).             \tag{D}
\]

Statement (D) would prove Collatz by strong induction. Conversely, if all
starts reach 1, choose \(m=1\). The new constructions below establish
particular unbounded families of (D), not its universal quantifier.

## 1. A fixed-clock factor-three reduction before forward descent

Set

\[
m=84997906089+2^{37}t,\qquad N=3m,\qquad t\ge0.
\]

Two explicit 37-letter parity words prove

\[
T^{37}(m)=T^{37}(N)=523998152183+3^{25}t.
\]

Thus the partner is exactly \(N/3\), and every nonempty prefix of the
larger arm remains above \(N\). For every prescribed additional horizon
\(L\), an explicit congruence on \(t\) forces the next \(L\) steps to
be odd. This gives infinitely many sources with a 37-step smaller-partner
certificate even though direct forward descent has not occurred by
\(37+L\). Each source is an ordinary positive integer; the source varies
with \(L\). A positive multiple of three has only its doublings as
positive ancestors, so the certificate uses a separate smaller source.

[Full words, legality, rank and transport limitation](THREE_RAY_POSITIVE_FAMILY.md).

## 2. Recursive proofs of the same five-ray question

Let \(E(t)\) mean \(t\sim5t+1\). The all-parameter assertion is
equivalent to Collatz by the pinned PR146 proof. Two exact rules give
\(E(t)\Longleftrightarrow E(s)\) with a smaller positive parameter:

| Guard | Smaller parameter | Physical identity |
|---|---|---|
| \(t\equiv11\pmod{64}\) | \(s=(27t+23)/64\) | \((T^6(t),T^6(5t+1))=(s,5s+1)\) |
| \(t\equiv35\pmod{64}\) | \(s=(9t+5)/64\) | Same identity |
| \(t=4u,\ u\equiv84997906089\pmod{2^{37}}\) | \(s=3u\) | Two initial steps and the actual 37-step merger |

The symbolic terminal family is \(s=(4^m-1)/3\), \(m\ge1\). Its
two arms reach 1 at the common clock \(2m+4\).

**Every nonempty finite word in the first two rules has infinitely many
positive ordinary realizations that end in this terminal family.** If
the composed parameter map is \((3^e t+B)/64^k\), choose

\[
4^m\equiv1+3B\,64^{-k}\pmod{3^{e+1}},\qquad
t=\frac{64^k(4^m-1)/3-B}{3^e}.
\]

The congruence has a class of solutions because powers of four generate
the units congruent to one modulo powers of three. Full-word integrality
enforces every physical parity guard, and all intermediate parameters
strictly decrease. The two original arms meet at 1 at clock
\(6k+2m+4\). This is an unbounded symbolic family, not an inference from
the finite examples.

The accompanying selector returns a finite, independently checkable
meeting certificate or **UNRESOLVED**. Its smallest uncovered parameter
with only the symbolic terminal family is 2, although 2 and 11 do meet.
The decreasing rank proves termination of this partial selector; it does
not prove that every output is successful.

[Proof and compiler](FIVE_RAY_RECURSION.md) ·
[Executable certificates](check_merger_selector.py).

## 3. Reducing all representation lengths at a fixed signed complexity

Let \(S\) be the positive mirror map, with odd branch \((3x-1)/2\).
Consider a positive target \(c=5\,2^b-M\) whose signed magnitude \(M\)
first reaches 5 in \(b+3k\) steps with \(2k\) odd inputs. Define

\[
\mathcal F_k=\{5\,3^{2k-q}-u>0:
          S^{3k}(u)=5,\ \text{the suffix has }q\text{ odd inputs}\}.
\]

The exact shared-prefix calculation proves, for every such representation,

\[
T^b(c)\in\mathcal F_k,\qquad
1\le T^b(c)\le5(9^k-8^k).
\]

Thus every target above that bound strictly descends, uniformly in the
unbounded representation length \(b\). The complete first two finite
target sets are

\[
\mathcal F_1=\{1,5\},\qquad
\mathcal F_2=\{1,2,5,7,23,27,28,85\}.
\]

Every qualifying target at these two complexities therefore reaches 1
within \(b+4\) or \(b+70\) steps, respectively. At general complexity,
the sets are nested but no induction proving convergence of all their
members is supplied.

For an escaping orbit, two distinct odd visits to the signed target set,
with odd-clock gap \(d\) after a future tail floor \(F\), must satisfy
\(F\le2^{448}3^{64d}\). The proof cancels two exact phase identities;
it does not assume algebraicity of an unknown limiting correction.
Increasing signed complexity and increasingly separated visits remain
possible under this bound.

[Written proofs STA1–STA4](SIGNED_TARGET_ARITHMETIC.md) ·
[Exact finite reduction replay](check_signed_target_reduction.py).

## 4. Why affine success cylinders cannot be mistaken for a complete cover

For a known converger, let \(\kappa(x)=d(x)-2a(x)\), the stopping
defect used in PR148/149. For compatible integer slopes \(a,c\), a
fixed ordinary parameter with both arms known to converge lies in an
affine merger cylinder exactly when

\[
\kappa(at+b)-\kappa(ct+d)
=v_2(a)-v_2(c)+2\bigl(v_3(a)-v_3(c)\bigr).
\]

For \(n,3n\), the criterion is \(\kappa(3n)-\kappa(n)=2\).
The known convergent parameters \(2^j\) and \(3\cdot2^j\) already
violate this equality. No larger horizon can make them successes of
that particular affine-cylinder test. A finite list of such cylinders
also misses a whole positive progression near the signed fixed point
\(-1\). These statements constrain the proposed certificate
architecture, not ordinary convergence.

[Exact criterion and scope](AFFINE_CERTIFICATE_BOUNDARY.md) ·
[Bounded implementation checks](check_affine_boundary.py).

## 5. Source-qualified improvement in component geometry

Combining PR146's polynomial synchronization construction with Paper48
v2's fixed-target inverse-routing theorem gives the following implication:
for every positive odd ternary-unit target \(u\) and length \(M\), an
interval of \(M\) consecutive ordinary starts below
\(u\exp(CM^d)\) reaches \(u\) at one common clock at most \(CM^d\).
The elementary composition keeps the supplied ordinary target fixed and
pads it before routing so that the final source lift is positive.

Consequently a second component would force the largest gap \(G(X)\)
in the basin of one to satisfy \(G(X)\ge c(\log X)^\eta\) for every
sufficiently large \(X\), with absolute positive \(c,\eta\) and a
component-dependent onset. This removes one exponential from the
earlier elementary placement estimate. The imported analytic routing
theorem and its uncomputed constants remain explicit dependencies.
No opposing upper bound on \(G\) is proved.

[Composition theorem and dependency boundary](COMPONENT_RUN_PLACEMENT.md) ·
[Finite ordinary block replay](verify_run_placement.py).

## Relationship to the latest repository work

The main development used PR146 at
`561d48a4d3a793a59b1cdf0406062ae1a6d47515`. During this pass its head
advanced to `7d04c4dd756cfe495eb3eee78eba35a99085cd2a`. The later head
adds smaller tripling comparisons, propagation to `(x,27x]`, and lower
bounds for permanently failed pairs. Those are credited source results,
not claims of this packet. They still require an opposing upper bound.
The present fixed-clock guard, signed-complexity reduction and component
placement do not establish that upper bound or a complete guard cover.

[Frozen sources, checks and reviews](../../reports/2026-11-20-merger-selection/README.md).

## Reproduction

Each command prints its finite report and leaves the checkout unchanged:

```sh
python -X utf8 -B research/ordinary-merger-selection/check_merger_selector.py
python -X utf8 -B research/ordinary-merger-selection/check_signed_target_reduction.py
python -X utf8 -B research/ordinary-merger-selection/check_affine_boundary.py
python -X utf8 -B research/ordinary-merger-selection/verify_run_placement.py
```

Use `--output PATH` to save a report outside the checkout. The two
assertion-based checkers reject optimized Python rather than silently
disable their checks. These finite replays and repository integrity
checks are separate from the written proofs and from formal verification.
