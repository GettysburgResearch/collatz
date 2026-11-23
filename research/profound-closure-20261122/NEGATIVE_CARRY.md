# A terminating complement budget for unbounded affine debt

## Result

The failed-half carry now has a total **arithmetic transition** on every supplied source gap. Its state retains an arbitrary subtractive intercept instead of trying to force every result back into `3^p r−1`. A new terminating macro resolves every exponent and every nonnegative subtractive carry whenever the actual supplied source begins with a sufficiently long run of gap ones.

The quantitative theorem is:

> Let `p,c,L,k,u,y` be natural numbers, with `u>0`, `y>0`,
> `3^p+c ≤ 2^L`, `k ≥ (2^p−1)L`, and
> `y+c=3^p(2^k u−1)`. Then
>
> `T^k(y) ≤ T^k(2^k u−1)`.

There is no bound on `p`, `c`, `u`, or the supplied tail. The ordinary map is

\[
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2.\end{cases}
\]

The stated clock bound is sufficient, not an estimate of the shortest useful prefix. An exact finite algorithm usually returns a much shorter clock. At its stopping clock `K`, every positive target in the corresponding progression satisfies the sharper all-parameter identity

\[
T^K\bigl(3^p(2^K u-1)-c\bigr)=3^K u-d_K,
\qquad d_K\ge1.
\]

`NegativeCarry.lean` proves the ordinary realization, termination of the finite budget, the explicit clock bound, and the transfer into the **same literal-suffix, smaller-rank induction** used in PR177 and PR180. It has 21 public theorem audits. No convergence statement about a negative Collatz map is assumed.

The remaining universal coverage step is explicit: a general complete source certificate is not proved to offer this sufficiently long all-one prefix at a usable carry state. The arbitrary-gap transition can consume an entire supplied certificate and leave a positive terminal integer. This note does not declare those terminal integers convergent.

## Literature route and relation to the latest repository

Yolcu, Aaronson and Heule's [*An Automated Approach to the Collatz Conjecture*](https://emreyolcu.com/research/rewriting-collatz.pdf), especially Definition2.4 and Theorem2.6, distinguish a terminating part of a rewriting process from termination of the complete system. Their mixed binary–ternary construction also preserves the actual arithmetic meaning of a rewrite. The present argument uses this distinction: it proves termination of a finite **credit-acquisition task**, then checks exactly when its result pays for an ordinary target/source comparison. The result here is derived directly; no theorem of that paper is introduced as a Lean axiom.

The baseline is PR185 `276be8154f4e867acc0230466b34d9cb224aacf5`, including `CarryLanguage.lean` in `research/whole-repo-closure-20261122`. That development solved the language `1{2,3}*21` but deliberately left the higher debt states undefined. The current transition has neither a debt-exponent cutoff nor a source-gap alphabet cutoff.

Two newly read results constrain the scope of this extension:

- PR176 `8aeb843bba254f065743b6fa277a70906b51d520`, `SOURCE_ENVELOPE.md`, maximizes the source available from every payable literal prefix deletion. Our rule changes the target by actual ordinary iteration; it does not assert a larger free source envelope.
- PR182 `45354128f890fb479f6c23b547368bcddd9cebe6`, `LITERATURE_CERTIFICATE_BRIDGE.md`, bounds every smaller-rank inserted prefix retaining a specified suffix on its counterfamily. Our rule does not replace that suffix or invent a larger inverse source. It consumes an actual prefix and retains the supplied suffix exactly.

The new clock depends on the unbounded affine state, and the source-prefix guard is real. Thus this result makes no fixed-lookahead or universal source-reset claim of the kinds excluded by the new barriers.

## 1. A positive complement carries the signed arithmetic

For bookkeeping define the negative shortcut on positive integers:

\[
S(d)=\begin{cases}d/2&d\equiv0\pmod2,\\(3d-1)/2&d\equiv1\pmod2.\end{cases}
\]

Let `e_k(d)` count its even steps before clock `k`. If

\[
y+d=2^k z,\qquad d>0,
\]

then the exact physical identity is

\[
\boxed{T^k(y)+S^k(d)=3^{k-e_k(d)}z.}\tag{1}
\]

At each preterminal clock the sum still contains the remaining power of two, so the target and its complement have the same parity. On an even step their sum is halved. On an odd step the `+1` of the positive target cancels the `−1` of the complement, and their sum is multiplied by `3/2`. This proves (1) by induction with no division or sign ambiguity. The Lean statement uses addition throughout, avoiding truncated natural subtraction.

For an affine target `y=A r+B` over a source odd block `r=2^k u−1`, put `d=A−B>0`. Then `y+d=2^k A u`, so

\[
T^k(y)+S^k(d)=A3^{k-e_k(d)}u,
\qquad T^k(r)=3^k u-1.
\]

Whenever `A≤3^p` and `e_k(d)≥p`, positivity of `S^k(d)` gives the desired endpoint comparison. This is `paid_complement_bound`; positive intercepts are permitted as well as subtractive carries.

## 2. Only a finite halving budget is needed

One must not assume that every orbit of `S` converges. That is unnecessary. The task is to obtain a prescribed finite number of even steps.

If `d>1`, write

\[
d-1=2^s v,\qquad v\text{ odd}.
\]

The next `s` auxiliary steps are odd, and

\[
S^s(d)=3^s v+1
\]

is even. These odd steps do not decrease `d`. Their number is finite because each reduces the exponent of two in `d−1` by one. The next even step halves the result.

This gives an elementary terminating machine: stop when the required even-step budget is complete or when the complement becomes one. Before stopping, the lexicographic pair

\[
(\text{remaining even budget},\ \nu_2(d-1))
\]

decreases at every step. An even step lowers the first coordinate, regardless of the valuation reset. An odd step preserves that coordinate and lowers the second. The fixed value one is an explicit stop, not an unhandled infinite odd run. `budget_or_one` proves this total finite alternative.

For debts, the unwanted stop cannot happen early. If initially `d≥2^p`, then before `p` even steps its value is at least its initial value divided by `2^e`, where `e<p`; odd steps do not decrease it. It therefore remains above one. Consequently

\[
\boxed{d\ge2^p\ \Longrightarrow\ \exists K:\ e_K(d)=p.}\tag{2}
\]

`finite_even_budget` proves (2). This conclusion remains valid whether the auxiliary trajectory later converges, cycles, or grows without bound.

### An explicit clock

Suppose also `d≤2^L`. The first odd block followed by its even step takes at most `L` clocks. Its resulting value is at most `2^(2L)`. The next block can therefore be bounded using height `2L`, then `4L`, and so on. Induction gives

\[
\boxed{K\le L+2L+\cdots+2^{p-1}L=(2^p-1)L.}\tag{3}
\]

`bounded_even_budget` proves this inequality. For a debt `3^p r−c`, the complement is `3^p+c≥2^p`, so one may take `L=ceil(log₂(3^p+c))`. The first-clock certificate below computes the exact block sequence instead of using this conservative bound.

## 3. An exact transition for every supplied source gap

Suppose the current actual source and target satisfy

\[
3r+1=2^a u,\qquad y+c=3^p r,\qquad p\ge1.
\]

Set

\[
d=c+3^{p-1},\quad e=e_a(d),\quad
p'=(p-1)+(a-e),\quad c'=S^a(d).
\]

Then

\[
\boxed{T^a(y)+c'=3^{p'}u.}\tag{4}
\]

Indeed, the source edge gives `y+d=2^a 3^(p−1)u`, and (1) applies. `gap_carry_transport` proves (4) for every gap size and every exponent `p≥1`.

This is the precise repair of the earlier restricted debt representation. For `p≥3`, dividing the old intercept by its small power of two produces a larger odd complement. The new state keeps that complement; it does not pretend it is one. All transitions remain physically meaningful.

If a transition reaches `p'=0`, its positive target is below the actual new source `u` and is eligible for the interval handoff. Otherwise the transition may be composed with the next supplied source gap. This is a complete arithmetic semantics, not a proof that a successful handoff must occur before the source certificate ends.

## 4. The original complete-source rank is retained

Let the complete supplied certificate be

\[
\operatorname{GapTrace}(2^k u-1,1,[1]^k\mathbin{+\!+}\tau),
\qquad k>0.
\]

Splitting the actual certificate yields its actual source endpoint `q=T^k(2^k u−1)` and the literal suffix `GapTrace q 1 τ`. The proved target comparison gives a positive target endpoint at most `q`, hence inside `[1,2q+1]`.

The old grade multiset is the suffix multiset plus `k` copies of grade two. Removing those copies strictly decreases the existing highest-differing-multiplicity rank. Nothing is inserted, and the suffix is unchanged. `one_prefix_grade_drop` and `paid_debt_interval_rule` check this transfer directly against PR180's `IntervalHyp` interface.

This rule uses the source induction hypothesis exactly once, on the lower-grade pair `(q,T^k(y))`. It does not infer that all smaller integers converge merely because `q` converges, and it does not choose a fresh convergence witness with uncontrolled rank.

The all-one prefix must be literally supplied. For instance, a physical odd-run identity may end at an even integer, whereas a complete odd-gap certificate cannot continue from that integer with another positive odd gap. The certificate hypothesis enforces this distinction. The numeric comparison theorem itself is valid for every positive `u`.

## 5. Concrete all-parameter identities

### The old failed-half carry

For `C(r)=9r+2`, the complement is `7` and the required budget is two even steps:

\[
7\longmapsto10\longmapsto5\longmapsto7\longmapsto10\longmapsto5.
\]

There are exactly two even steps in five clocks. Therefore, for every `u≥1`,

\[
r=32u-1\quad\Longrightarrow\quad
T^5(9r+2)=243u-5=T^5(r)-4.
\]

When a complete source certificate supplies five literal gap ones, the same lower-grade suffix handoff applies. A concrete compatible example is `u=2`, `r=63`: source endpoint485 and carry endpoint481.

### A formerly unsupported debt exponent

For `p=3,c=1`, the complement28 reaches its third even step in four clocks:

\[
28\longmapsto14\longmapsto7\longmapsto10\longmapsto5.
\]

Thus for every `u≥1`,

\[
T^4\bigl(27(16u-1)-1\bigr)=81u-5=T^4(16u-1)-4.
\]

For the compatible literal-prefix example `u=2`, source31 reaches161 and target836 reaches157. The theorem covers every exponent, not just this example; the displayed case illustrates the new unbounded-state argument.

## 6. Exact residual and a genuine boundary

The universal dispatcher is still unproved. What is now proved is:

1. Every supplied source gap has the exact signed-affine transition (4).
2. Every subtractive debt can be discharged by a sufficiently long supplied source one-run, with the explicit sufficient length (3).
3. A paid prefix transfers to the original smaller-grade literal suffix.

What is not proved is that every complete source word reaches such a paid prefix or another already available handoff. An arbitrary word can end while the target still has positive debt. At terminal source one, the residual is `3^p−c`; the special family `3^p−1` remains part of the repository's older power-of-three reduction. No such convergence premise has been added here.

The broader affine family also has a real obstruction to this particular one-run macro. If the complement is one, its auxiliary orbit stays one and earns no even credit. For every `A≥2` and every source odd-run length,

\[
y=A(2^k u)-1\quad\Longrightarrow\quad
T^k(y)=A3^k u-1>3^k u-1=T^k(2^k u-1).
\]

`unit_complement_overshoot` proves this all-parameter boundary. It rules out describing the auxiliary machine's totality as a total successful Collatz dispatcher. The exact next missing implication is **coverage of a successful source-prefix handoff**, not existence or physical legality of the individual transition.

## Verification and reproduction

`NegativeCarry.lean` imports the prior checked `CarryLanguage.lean` and the pinned Mathlib factorization module. The strict build is Lean4.34.1 with `-j1 -DwarningAsError=true`, Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. The machine receipt records every public axiom audit and the source/log hashes. The only permitted audited axioms are `propext`, `Classical.choice`, and `Quot.sound`.

`negative_budget.py` constructs and independently checks an exact block certificate for any affine state `A r+B` with positive complement `A−B`. It stops on payment or the exceptional fixed complement one. The committed examples include the old carry, exponent-three debt, and a unit-complement obstruction. These examples illustrate the proved infinite families; they are not the proof of universal termination.

All input and proof guards use explicit `ValueError` checks and remain active under optimized Python. The self-test accepts the three valid certificates and rejects four damaged certificates: a missing block, an incorrect endpoint, an incorrect total clock, and falsely claimed payment. It also rejects invalid inputs to the budget, valuation, and certificate builder. Both the self-test and committed-certificate replay pass under normal Python and `python -O`; the four invocations and their exit codes are recorded in `negative_budget_hardening_receipt.json`. This checker hardening leaves the Lean source and Lean receipt unchanged.

```bash
python negative_budget.py --multiplier 27 --intercept -1
python negative_budget.py --multiplier 9 --intercept 2
python negative_budget.py --check negative_budget_examples.json
python negative_budget.py --self-test
python -O negative_budget.py --self-test
```
