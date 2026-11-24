# A reduced-clock prime obstruction for every positive cycle

23 November 2026. Arithmetic author: `cycle_arithmetic6`. The arithmetic
Taylor-series route was identified by `rational_selector6`; Sections 3–4
below independently reconstruct its prime obstruction. See the companion
[RATIONAL_SELECTION.md](RATIONAL_SELECTION.md) for the complete germ
criterion and its source-qualified analytic consumer.

**Status: finite arithmetic core LEAN CHECKED in a development build;
unrestricted-cycle prime and pole implications PROPOSED written theorems.
Full Collatz remains OPEN.** No arithmetic Taylor germ is constructed for
an arbitrary positive ordinary source. The new result applies to every
positive cycle word, without a family or period bound, but is a necessary
constraint rather than an unconditional cycle exclusion.

## 1. Statement and normalization

Use the shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.
\end{cases}
\]

Let a positive ordinary cycle have total shortcut length \(A\) and
\(p\ge1\) odd inputs. Enumerating the odd states cyclically gives

\[
2^{a_i}x_{i+1}=3x_i+1,\qquad x_i\in\mathbb Z_{>0},\qquad
a_i\ge1,\qquad \sum_{i=0}^{p-1}a_i=A.
\tag{1}
\]

Put

\[
g=\gcd(A,p),\qquad u=A/g,\qquad v=p/g,\qquad
D_{\rm red}=2^u-3^v.
\tag{2}
\]

The ordinary cycle equations imply the following alternative:

- Every odd state is one, and the shortcut cycle is the standard
  \(1\mapsto2\mapsto1\) cycle, possibly recorded repeatedly.
- \(D_{\rm red}>1\), it is coprime to six, and it has a prime divisor
  \(\ell\ne2,3\).

For any fixed positive ordinary source eventually entering the second
kind of cycle, write its actual weighted parity series and translated
Taylor series as

\[
e_k=T^k(n)\bmod2,\quad p_k=\sum_{j<k}e_j,\qquad
B_n(z)=\sum_{k\ge0}e_k3^{-p_{k+1}}z^k,
\]
\[
J_n(t)=B_n(2+t)=\sum_{j\ge0}c_jt^j.
\tag{3}
\]

Under eventual periodicity these are a rational function and its actual
Taylor expansion, so every \(c_j\) is rational. For **every** prime
\(\ell\mid D_{\rm red}\), the denominator valuations satisfy

\[
\boxed{\displaystyle
\limsup_{j\to\infty}
\frac{\max\{0,-v_\ell(c_j)\}}{j}
\ \ge\ \frac{v_\ell(D_{\rm red})}{u}>0.}
\tag{4}
\]

Here \(v_\ell(\ell)=1\), with \(v_\ell(0)=+\infty\), and \(c_j\)
is the Taylor coefficient, including the division by \(j!\). In particular
\(J_n\notin\mathbb Z[1/3][[t]]\). Equation (4) retains the entire
\(\ell\)-power in the reduced denominator; it is stronger than just
producing one forbidden denominator prime.

## 2. The finite arithmetic core

### 2.1. Clock positivity and the equality case

Multiplying the actual equations (1), including every state, gives

\[
2^A\prod_i x_i=\prod_i(3x_i+1).
\tag{5}
\]

Every factor on the right is strictly greater than \(3x_i\), hence
\(3^p<2^A\). Positivity also gives \(3x_i+1\le4x_i\), with equality
if and only if \(x_i=1\). Therefore

\[
3^p<2^A\le4^p,
\tag{6}
\]

and \(A=2p\) forces \(x_i=1\) at every index. The conclusion uses
ordinary positivity; it does not infer an integer cycle from a freely
chosen rational word. In the nontrivial case the last inequality in (6)
is strict.

Writing \(A=gu\) and \(p=gv\) in the strict left inequality proves
\(3^v<2^u\), so \(D_{\rm red}\) is positive.

### 2.2. The only positive unit difference

For positive integers \(u,v\),

\[
2^u=3^v+1\quad\Longrightarrow\quad(u,v)=(2,1).
\tag{7}
\]

Indeed, \(3^v\bmod8\) is either one or three. If \(u\ge3\), the
two sides of the proposed equation have different residues modulo eight.
Thus \(u\le2\). Since \(v\ge1\), the right side is at least four;
therefore \(u=2\) and then \(v=1\). No application of Catalan's theorem
or a lower bound for logarithmic forms is needed.

If \(D_{\rm red}=1\), (7) gives \(A=2g=2p\). Section 2.1 then forces
every odd cycle state to be one. Consequently a nontrivial cycle has
\(D_{\rm red}>1\). Since \(u,v>0\), this integer is odd and is not
divisible by three. It consequently has a prime divisor away from two
and three.

### 2.3. Exact Lean attachment

[CycleArithmetic.lean](CycleArithmetic.lean) proves six public theorems:

| Declaration | Formal conclusion |
|---|---|
| `two_pow_eq_three_pow_add_one` | The positive-exponent classification (7) |
| `cycle_product` | Equation (5), derived from all indexed affine equations |
| `cycle_clock_positive` | \(3^p<2^A\) for positive states and \(p>0\) |
| `cycle_clock_two_rigidity` | \(A=2p\) forces every indexed state to be one |
| `reduced_clock_positive` | Strict clock positivity survives a common clock divisor |
| `nontrivial_cycle_reduced_clock_prime` | A nontrivial positive cycle supplies \(\ell\ne2,3\) dividing \(2^u-3^v\) |

The successor map is an explicit permutation of `Fin p`. The file
derives its product identity from the supplied actual equations. This
allows a cyclic successor as required by (1), and in fact proves the
arithmetic statements for any such permutation. The prime theorem does
not need coprimality of \(u,v\); that additional hypothesis is used in
Section 3 to identify the minimal polynomial of the positive pole.

Development verification used Lean 4.34.1 and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`, with one worker and warnings
as errors. That build reused the earlier compiled `CycleCancellation`
dependency. The integration receipt, when present, records the separate
fresh dependency build and public-theorem axiom audit. Sections 3–4,
irreducibility, nonarchimedean radii, and the general rationality theorem
are not advertised as Lean formalizations in this module.

## 3. The pole survives every complete numerator cancellation

This section reconstructs the companion argument, beginning with the
actual cycle word rather than an arbitrary symbolic series.

For the purely periodic cycle, take one full chronological block of
length \(A\), with its actual \(p\) odd inputs. Its weighted parity
series has the form

\[
B_{\rm cyc}(z)=\frac{P(z)}{1-z^A/3^p},\qquad
P(z)=\sum_{k=0}^{A-1}e_k3^{-p_{k+1}}z^k.
\tag{8}
\]

The polynomial \(P\) has nonnegative rational coefficients and is not
zero. Thus at the positive real point

\[
r=3^{p/A}=3^{v/u}>0
\tag{9}
\]

one has \(P(r)>0\). Equation (8) has a genuine pole at \(r\), regardless
of any other polynomial cancellation. A finite actual prefix of length
\(N\) and odd count \(s\) changes the full series to

\[
B_n(z)=P_N(z)+z^N3^{-s}B_{\rm cyc}(z).
\tag{10}
\]

Since \(r>0\), its multiplier is nonzero there. Adding the polynomial
\(P_N\) cannot remove the pole. This is an attachment to the original
ordinary source, with its literal prefix.

The polynomial

\[
F(z)=z^u-3^v
\tag{11}
\]

is irreducible over \(\mathbb Q\), because \(\gcd(u,v)=1\). Here is an
elementary valuation proof sufficient for this binomial. Every root in
\(\overline{\mathbb Q}_3\) has three-adic valuation \(v/u\). If a monic
rational factor has degree \(d>0\), Gauss's lemma makes its coefficients
integers. Its nonzero constant coefficient has valuation \(dv/u\),
which is an integer. Coprimality forces \(u\mid d\); a proper factor
of degree less than \(u\) is impossible.

Write the actual rational function \(B_n=H/Q\) in lowest terms over
\(\mathbb Q[z]\). Because \(r\) is a pole and its minimal polynomial
is \(F\),

\[
F\mid Q,\qquad \gcd(F,H)=1.
\tag{12}
\]

This is where the argument addresses numerical numerator cancellation:
it keeps a specific irreducible factor that cannot cancel at all. A
prime dividing \(F(2)\) need not survive in the value \(B_n(2)=-n\),
which is always an integer. The full Taylor expansion detects the pole
even when that single value is integral.

## 4. The full prime-power cost in the translated Taylor series

Fix any prime \(\ell\mid D_{\rm red}=F(2)\). Sections 1–2 give
\(\ell\ne2,3\). In \(\overline{\mathbb Q}_\ell\), let
\(\alpha_1,\ldots,\alpha_u\) be the roots of \(F\), counted with
multiplicity, and put \(\beta_i=\alpha_i-2\). All \(\alpha_i\) and
\(\beta_i\) are integral at \(\ell\), so \(v_\ell(\beta_i)\ge0\).
The complete product gives

\[
\sum_{i=1}^{u}v_\ell(\beta_i)=v_\ell(F(2))
=v_\ell(D_{\rm red}).
\tag{13}
\]

Consequently some index satisfies

\[
v_\ell(\beta_i)\ge v_\ell(D_{\rm red})/u>0.
\tag{14}
\]

By (12), every root of \(F\) remains a pole over every characteristic
zero completion: otherwise the numerator would vanish at a conjugate
root and have a common factor with \(F\). Therefore \(\beta_i\) is a
genuine pole of \(J_n(t)=B_n(2+t)\). Its \(\ell\)-adic convergence
radius is at most

\[
\ell^{-v_\ell(D_{\rm red})/u}<1.
\tag{15}
\]

The nonarchimedean Cauchy–Hadamard formula now gives (4). In particular
the coefficient denominators contain arbitrarily high powers of this
same \(\ell\). Every prime divisor of \(D_{\rm red}\), with its full
valuation in (4), supplies such an obstruction. No squarefree reduction,
norm substitution for a gcd, or bound on the number of word patterns is
used. The full numerical cycle denominator is
\(2^A-3^p=(2^u)^g-(3^v)^g\); \(D_{\rm red}\) is its specified factor.
The theorem does not assert that every prime or full valuation from
the larger denominator appears in (4). What makes this factor decisive
for the stated obstruction is the proof that its polynomial \(F\)
survives every numerator cancellation. No full-cycle integrality claim
is inferred from a test of a proper factor.

Two consequences distinguish the input required by the companion route:

1. If the coefficients lie in some fixed ring \(\mathbb Z[1/M]\),
   every prime divisor of \(D_{\rm red}\) must divide \(M\). This is
   consistent with any rational cycle, because its rational Taylor
   series has some finite denominator-prime set.
2. If they lie in the particular ring \(\mathbb Z[1/3]\), the cycle
   must be the standard cycle. The same conclusion follows if each
   \(\ell\ne3\) has subexponential denominator growth; a uniform
   bounded-denominator assertion at those primes is more than needed.

The original PR178 Jet hypothesis permits an arbitrary \(M\), and hence
only forces eventual periodicity. The strengthened arithmetic input
\(\mathbb Z[1/3]\), together with all the retained analytic conditions
and limiting-density input, yields the sharper standard-cycle conclusion
in the companion note. The general-density rationality consumer is a
source-qualified dependency, not established by Sections 2–4 here.

## 5. What remains unsupported

For a general positive ordinary source, its actual binary series already
satisfies \(B_n(2)=-n\), but no argument here proves that every Taylor
coefficient \(c_j\) is rational, much less that its denominator is a
power of three. The first unknown derivative remains unknown. The
limiting-density and local analytic hypotheses in the source rationality
consumer also remain explicit.

The result therefore changes the target of the analytic approach: a
complete arithmetic germ with the original ternary denominator ring
would eliminate the nonstandard-cycle branch as well as the nonperiodic
branch covered by that consumer. It does not manufacture the germ.
Equivalently, every hypothetical nonstandard positive integer cycle
must export a definite prime-power denominator cost into its actual
translated coefficients, even though its constant coefficient is an
ordinary integer.

The earlier S-unit, logarithmic-form, and cyclotomic-gcd attacks did not
produce a new universal numerical gcd inequality in this lane. No such
inequality is claimed by relabeling (4): this is a different all-word
necessary constraint, with an explicit missing arithmetic input.

## 6. Frozen sources and inspection boundaries

Repository parent at the start of this round:
`afe6f4d1a661b377c9daa4623bdd732ba478386b`, branch
`research/dyadic-band-descent-20261121`, PR182. The source heads below were
refreshed on 23 November 2026; a listed file inspection does not extend a
verdict to every claim in its PR.

| Source | Exact head | Scope inspected for this lane |
|---|---|---|
| PR175 | `bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17` | `risk25/INTEGER_RESIDUAL_DEGREE.md`, `RESIDUAL_RECURRENCE_LATTICE.md`, and `CYCLOTOMIC_VALUE_SEPARATION_PROPOSED.md`, all read; their final missing numerical gcd is not imported as proved |
| PR178 | `398b3a04da071e96362005792417bd5cf8cc6497` | `arithmetic/FULL_NUMERICAL_SEPARATION.md`, `rigidity/GENERAL_DENSITY_JET.md`, and `rigidity/SCALAR_BOUNDARY_AND_SECOND_CENTER.md`, all read; family-gcd and general-density analytic conclusions retain their written/source-qualified scope |
| PR180 | `7cfd911d35382d9d3bc988060ba88ade78a4267e` | `research/closing-step-20261123/POSITIVE_CYCLE.md` return-lattice and qualified all-cycle defect statements; its predecessor-density hypothesis is not assumed here |
| PR185 | `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d` | Current head refreshed; earlier inspected cyclotomic source boundary remains unchanged |
| PR186 | `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493` | Current head refreshed and `literature/deep-machinery-20261122/03_arithmetic_and_logic.md` consulted for fixed-dimensional arithmetic limitations |

The PR175 files are under
`research/lean-global-closure-20261121/risk25/`. The PR178 files are under
`research/literature-push-20261123/`. Local prior-cycle boundaries were
read in `closure-round5-20261123/CYCLE_EXCLUSION.md`,
`whole-repo-round3-20261123/COMPLETE_CYCLE.md`, and
`literature-round4-20261123/CYCLE_RIGIDITY.md`.

The primary literature relevant to the companion analytic consumer is
Antoine Chambert-Loir and Camille Noûs, *Potentiel et rationalité*,
[arXiv:2305.17210v2](https://arxiv.org/abs/2305.17210v2), 31 August 2026,
[primary PDF](https://arxiv.org/pdf/2305.17210v2). This lane directly read
Section 2.1 and Sections 4.1–4.3, including the actual arithmetic-model,
local-realization, and strict positive-game-value hypotheses and the
conclusion of Theorem 4.3. It did not independently reprove the general
Arakelov rationality theorem. The finite arithmetic and valuation
arguments in Sections 2–4 are given explicitly above; they do not invoke
a stronger S-unit or cycle-exclusion theorem from that paper.
