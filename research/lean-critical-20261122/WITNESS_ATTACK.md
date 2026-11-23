# A total arithmetic carry compiler and a larger successful source language

**Status: PROVED Lean statements; universal successful dispatch remains OPEN.**
The new module is [WitnessCritical.lean](lean/WitnessCritical.lean). It gives
a physical continuation for every source gap and every positive ternary
debt state. The continuation uses finite trajectories of the positive
`3x-1` map; it assumes nothing about the eventual behavior of that map.

The compiler also produces a concrete positive extension of the latest
literal-tail language: a third state accepts an unbounded number of gap-four
letters, with arbitrary intervening runs of gap two. The entire supplied
source suffix is retained. A separate kernel theorem shows exactly why the
remaining terminal debt cannot simply be declared resolved: it contains an
exact copy of the positive Collatz dynamics.

## 1. Inputs and source boundary

We use the repository's positive shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

`GapTrace(r,u,W)` means the actual sequence of positive-gap equations
\(3r_i+1=2^{a_i}r_{i+1}\), with endpoint \(u\). A complete source
certificate has endpoint one. All orbit conclusions below use the existing
`CollatzShell.step` and `orbit` definitions. No new ordinary Collatz map or
new convergence axiom is introduced.

| Source | Frozen head | Input used or boundary retained |
|---|---|---|
| PR180 | `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d` | `WitnessGlobal.lean` and `WitnessSynthesis.lean`: actual `GapTrace`, whole-source grade, literal-tail splitting, independent orbit clocks, and the failed-half carry \((r,9r+2)\). |
| PR177 | `a0a0d76f91b4e3846c1b1f0706cad56cb6098317` | `BOUNDED_GAP_ATTACK.md`: complete alphabet-four reduction, exact highest-changed-multiplicity order, and its unresolved low-interval coverage. |
| PR185 | `276be8154f4e867acc0230466b34d9cb224aacf5` | `whole-repo-closure-20261122/CARRY_LANGUAGE.md` and `CarryLanguage.lean`: the signed-gap identity and successful language \(1\{2,3\}^*21\); its debt-two/gap-one and gap-four exits remain explicit. |
| PR182 | `45354128f890fb479f6c23b547368bcddd9cebe6` | `LITERATURE_CERTIFICATE_BRIDGE.md`: the sharp proportional loss for every lower-grade reset retaining a specified suffix; unbounded inserted word length does not repair that source-height failure. |
| PR186 | `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493` | `04_returns_operators_and_termination.md`: use exact composition constraints and unbounded resources; a terminating local abstraction does not establish ordinary coverage. |

The only Lean import of the new module is the local `WitnessSynthesis`.
The other sources motivate or delimit the attack; they are not additional
unproved formal premises. The newly refreshed source files were inspected,
not all rebuilt as independent dependencies.

## 2. Reflection through a binary multiple

Define the positive negative-sign companion map

\[
F(c)=\begin{cases}c/2&2\mid c,\\(3c-1)/2&2\nmid c.\end{cases}
\]

Let \(F^a(c)\) be its finite iterate, and let \(K_a(c)\) count its
odd states before the first \(a\) transitions. In Lean these are
`minusStep`, `minusOrbit`, and `minusOdds`. They are computable natural
functions, and \(F^a(c)>0\) for \(c>0\).

### Theorem W1: exact reflected prefix

For \(x,c>0\) and natural \(a,q\),

\[
x+c=2^a q
\quad\Longrightarrow\quad
\boxed{T^a(x)+F^a(c)=3^{K_a(c)}q.}
\tag{W1}
\]

**Proof.** Induct on \(a\). For one step, the sum is even, so
\(x\) and \(c\) have the same parity. If both are even, the new
sum is half the old sum. If both are odd,

\[
\frac{3x+1}{2}+\frac{3c-1}{2}=\frac{3(x+c)}2.
\]

Thus the next binary coefficient is divided by two, and an odd step
multiplies its remaining factor by three. Positivity is preserved on both
sides. Induction gives W1, including the exact count of ternary factors.

This is `reflected_prefix`. It is valid at every finite clock. It does not
identify the infinite behavior of the two maps, and it requires no theorem
about negative Collatz cycles.

## 3. The full carry update has no missing arithmetic transition

Represent an actual positive target by

\[
x=3^p r-c,\qquad p\ge1,\quad c\ge1,\quad x>0.
\tag{W2}
\]

Suppose the supplied source has the next gap
\(3r+1=2^a u\). Put

\[
d=c+3^{p-1},\qquad
c'=F^a(d),\qquad p'=p-1+K_a(d).
\tag{W3}
\]

### Theorem W2: every-gap physical continuation

\[
\boxed{c'>0,\qquad T^a(x)+c'=3^{p'}u.}
\tag{W4}
\]

Indeed,

\[
x+d=3^{p-1}(3r+1)=2^a3^{p-1}u,
\]

so W4 is W1. The Lean theorem is `carry_gap_transport`.

The update applies to arbitrary gap sizes and arbitrary positive debts.
In particular, all four remaining source letters are covered, including
every state that escaped the earlier two-state template. The actual target
intercept is carried forward; it is never replaced by a more convenient
intercept. The new exponent is a natural number, but need not decrease.

If \(p'=0\), W4 gives

\[
0<T^a(x)=u-c'<u.
\tag{W5}
\]

This is a successful smaller-endpoint exit. It is sufficient, not necessary:
an endpoint with positive exponent can also lie in the active interval.

The failed short-diamond target initializes in this program exactly. From
\(3r+1=2^a u\),

\[
\boxed{T^a(9r+2)+1=3^{a+1}u.}
\tag{W6}
\]

The proof uses W1 with debt one, since \(F(1)=1\) and every companion
step is odd. `carry_initialization` reproduces the corresponding PR185
identity from the general reflection theorem.

## 4. Total compilation of a finite supplied word

`compileDebt(W,p,c)` is a total recursive function. It applies W3 at each
letter until either the exponent is zero or the supplied word is exhausted.
It returns the **consumed prefix**, final exponent, and final debt. These
two stopping outcomes are distinguished in its correctness theorem.

### Theorem W3: exact prefix, exact remaining suffix

Given `GapTrace(r,u,W)` and W2, the output supplies a decomposition
\(W=P\Vert\tau\), an actual intermediate source \(v\), and

\[
\operatorname{GapTrace}(r,v,P),\qquad
\operatorname{GapTrace}(v,u,\tau),
\]

\[
\boxed{T^{\sum P}(x)+c'=3^{p'}v,\qquad c'>0,}
\tag{W7}
\]

with either \(p'=0\) or \(\tau\) empty. This is
`compiler_complete`, proved by induction on the whole supplied word.
There is no bound on word length, gaps, exponent, debt, or source value.

If \(P\) is nonempty, removing it strictly lowers the existing complete
source grade:

\[
\boxed{\Gamma(0;\tau)\prec\Gamma(0;P\Vert\tau).}
\tag{W8}
\]

`prefix_grade_drop` proves W8 for every nonempty finite prefix, with no
alphabet restriction. Choose its largest gap; at twice that grade its
multiplicity strictly decreases, while all higher multiplicities agree.
The unchanged suffix cancels exactly.

When the compiler exits with exponent zero, W5 puts the actual target in
the retained source's interval. `compiler_interval_rule` applies the
existing lower-grade `IntervalHyp` to that source and its **literal** tail,
then transports its basin conclusion along the physical target prefix.
Intermediate increases in the carry exponent cause no problem for this
composed rule: the rank belongs to the supplied complete source certificate.

This theorem does not assert that every compiler run takes its zero-exponent
exit. Exhausting the source word remains a separate outcome.

## 5. A successful unbounded language with gap four

The new arithmetic continuation identifies a useful third state:

\[
D_1(r)=3r-1,\qquad D_2(r)=9r-1,
\qquad E(r)=3r-2.
\]

For each source gap \(3r+1=2^a u\), the entries in the table are the
actual values of \(T^a\) on the row's target:

| State | Gap 1 | Gap 2 | Gap 3 | Gap 4 |
|---|---|---|---|---|
| \(D_1(r)\) | \(u-1\), success | \(D_1(u)\) | \(D_2(u)\) | \(27u-1\), outside this grammar |
| \(D_2(r)\) | **\(E(u)\)** | \(D_1(u)\) | \(D_2(u)\) | \(27u-1\), outside this grammar |
| \(E(r)\) | \(3u-4\), outside this grammar | **\(E(u)\)** | **\(D_1(u)\)** | **\(D_2(u)\)** |

All entries, including those outside the successful grammar, are instances
of the total update W3. The bold entries are the new successful continuation
through the former debt-two/gap-one exit. In particular,

\[
D_2\xrightarrow{1}E
\xrightarrow{2^*}E
\xrightarrow{4}D_2
\tag{W9}
\]

is an exact cycle of **control states**, with an arbitrary finite run of
source gap twos. The ordinary source changes at every arrow. This is not a
positive Collatz cycle.

`SafeDebtWord` is the inductive grammar containing precisely the displayed
transitions that remain in \(D_1,D_2,E\), followed by the success edge
from \(D_1\). Its initial state for the failed-half problem is \(D_2\),
after W6 consumes a first source gap one.

### Theorem W4: successful dispatch of the complete grammar

For every accepted word \(W\) and every suffix \(\tau\),
`safe_language_compile` proves that the compiler on \(W\Vert\tau\)
consumes **exactly** \(W\), ends at exponent zero and debt one, and never
touches \(\tau\). Therefore, if

\[
\operatorname{GapTrace}(r,1,(1\Vert W)\Vert\tau),
\]

then the physical target \(9r+2\) reaches \(u-1\) after
\(1+\sum W\) shortcut steps, where \(u\) is the actual source of
the literal tail \(\tau\). The unchanged-source induction hypothesis
at the old grade then proves `Basin(9*r+2)`.

This is `safe_carry_interval_rule`. It is an all-word Lean induction.
It permits arbitrarily many gap-four letters through W9 and arbitrarily
long mixtures of the other allowed transitions. For example, every prefix

\[
1\,(1\,2^{[k_1]}\,4)\cdots
  (1\,2^{[k_m]}\,4)\,2\,1
\quad(m,k_1,\ldots,k_m\ge0)
\tag{W10}
\]

is accepted. Each \(2^{[k]}\) here denotes a repeated **gap letter**,
not exponentiation. The previously proved language
\(1\{2,3\}^*21\) is also accepted. This is a compositional enlargement
of the successful source language, rather than a larger finite residue
census.

No hypothesis says that an arbitrary supplied certificate belongs to this
grammar. Its absent transitions are retained explicitly in the table.

## 6. Why terminal debt is a real remaining problem

At source one, the legal supplied gap two is the source cycle
\(3\cdot1+1=2^2\cdot1\). For \(x+c=3^p\), W4 says

\[
\boxed{T^2(x)+c'=3^{p'},\qquad p',c'>0.}
\tag{W11}
\]

`terminal_padding_transport` checks both positivity assertions. If
\(p'=0\), the positive terms on the left would sum to one, which is
impossible. Thus zero-exponent exit is not even the correct terminal
criterion for this source; absorbed targets must be handled separately.

Every positive target occurs in a terminal debt state. For example, take
\(p=x\), \(c=3^x-x>0\). The theorem
`every_target_terminal_debt` proves the general statement

\[
\boxed{\forall x>0\ \exists p,c>0:\quad x+c=3^p.}
\tag{W12}
\]

Combining W11 and W12, repeatedly padding a known source-one certificate
by gap two simulates the actual map \(T^2\) on **every** positive target.
A universal successful terminal-debt theorem therefore requires a genuine
new Collatz argument; finite companion-map calculations do not remove it.

There is also an exact all-exponent check on a proposed exponent rank:

\[
(p,3^p-1)\longmapsto(p,3^p-1),
\qquad
(p,3^p-2)\longmapsto(p,3^p-2)
\quad(p\ge1)
\tag{W13}
\]

under source gap two. These fixed control states represent the already
absorbed targets one and two. `terminal_one_fixed` and
`terminal_two_fixed` prove W13 for every exponent. An argument demanding a
strict decrease of the exponent at every step would fail even on these
convergent examples. This does not rule out a rank on the unabsorbed states.

The finite companion dynamics do not settle this problem by a theorem about
negative-map cycles. After each supplied source gap, the next companion
input is shifted by \(3^{p-1}\); it is not one uninterrupted companion
orbit. Moreover W11 exhibits the retained positive dynamics exactly.

## 7. The next global implication

The new compiler resolves arithmetic coverage of transitions: every actual
source gap produces its exact next debt, exponent, and target clock. It
also closes the explicit larger grammar in section 5 in the existing
complete-source order.

Universal closure still requires a successful selector on the remaining
states. One possible sufficient route is to prove that, before the complete
source word is exhausted, the actual target reaches a lower-grade retained
source interval or admits another certified lower-grade merger. A second
route would solve the residual terminal targets with a new well-founded
argument after the known absorbing targets are removed. W11--W13 state the
precise behavior that either route must preserve.

There is no substitution of a finite control graph for the unbounded debt
variables, no assumption that the source-one residual is bounded, and no
claim that the successful regular language is exhaustive.

## Formal evidence

The module contains sixteen public theorems, each with an explicit
`#print axioms` audit. It uses the same Lean 4.34.1 / pinned Mathlib
environment as the parent packet. The parent replay records the strict
compiler outcome and exact source hash. The mathematical statements above
are kernel-checked where identified; the textual grammar description is
an explanation of the inductive definition, not an empirical coverage
claim. No universal Collatz theorem is introduced.
