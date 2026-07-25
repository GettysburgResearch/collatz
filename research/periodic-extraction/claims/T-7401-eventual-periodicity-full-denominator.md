# T-7401 — Eventually periodic extraction is full-denominator cycle divisibility

**Claim ID:** `T-7401`  
**Title:** Every positive ordinary eventually periodic shortcut-Collatz itinerary enters a positive integer cycle, while every supercritical periodic itinerary is a signed completion ghost  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-complexity-01`  
**Issue:** `#59`  
**Created:** 2026-07-25  
**Dependencies:** elementary shortcut-Collatz affine iteration and the finite parity-cylinder bijection proved below  
**Scope:** all eventually periodic parity itineraries of the shortcut `3x+1` map  
**Related counterexample candidates:** none

## 1. Setup

Let

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\[1mm]
(3x+1)/2,&x\equiv1\pmod2
\end{cases}
\tag{1}
\]

on `Z_2`, and let

\[
w=(\varepsilon_0,\ldots,\varepsilon_{L-1})\in\{0,1\}^L
\tag{2}
\]

be a nonempty finite parity word. Put

\[
s_j=\sum_{i<j}\varepsilon_i,
\qquad
s=s_L,
\tag{3}
\]

and

\[
\boxed{
C_w=\sum_{j=0}^{L-1}
\varepsilon_j\,2^j3^{\,s-s_{j+1}}.}
\tag{4}
\]

Along the branches prescribed by `w`, direct affine composition gives

\[
\boxed{
T^L(x)={3^s x+C_w\over2^L}.}
\tag{5}
\]

If `w` contains a `1`, then `C_w>0`.  If `w=0^L`, then `C_w=0`.

## 2. Finite parity cylinders and infinite injectivity

### Lemma 1 — exact finite parity cylinder

Every binary word of length `n` is realized by exactly one residue class modulo `2^n`.

#### Proof

The assertion is trivial for `n=0`. Suppose a length-`n` word is realized by `r mod 2^n`. Its two lifts modulo `2^(n+1)` are

\[
r,\qquad r+2^n.
\]

Along their common first `j<=n` branches, the affine difference is

\[
T^j(r+2^n)-T^j(r)=3^{s_j}2^{n-j}.
\tag{6}
\]

For `j<n` this difference is even, so the first `n` parity bits agree. At `j=n` it is odd, so the two possible next parity bits are opposite. Hence one lift realizes the extension by `0` and the other realizes the extension by `1`. ∎

### Corollary 1.1 — injective infinite parity coding

Every infinite parity word determines exactly one point of `Z_2`. In particular, two `2`-adic points with the same complete parity word are equal.

#### Proof

The compatible finite cylinders have moduli `2^n` and determine one inverse-limit point. If two points share every cylinder, their difference is divisible by every power of two and is zero. ∎

## 3. Periodic-tail classification

Let

\[
\omega=w^\infty
\tag{7}
\]

be the infinite periodic repetition of `w`, and let `x_w in Z_2` be its unique realization.

### Theorem 1 — exact periodic fixed point

One has

\[
\boxed{
x_w={C_w\over 2^L-3^s}.}
\tag{8}
\]

The denominator is odd and nonzero. Moreover:

1. `x_w` is an ordinary integer if and only if
   \[
   \boxed{|2^L-3^s|\mid C_w.}
   \tag{9}
   \]
2. If `3^s>2^L`, then `x_w<0`; hence the supercritical periodic itinerary has no positive ordinary realization.
3. If `3^s<2^L`, then `x_w>0`; it is a positive ordinary realization exactly when
   \[
   \boxed{2^L-3^s\mid C_w.}
   \tag{10}
   \]
   In that case `x_w` lies on a positive shortcut-Collatz cycle whose period divides `L` and whose parity itinerary is `w^infinity`.
4. The equality `3^s=2^L` never occurs for positive `L`.

#### Proof

The shifted point `T^L(x_w)` has the same infinite parity word `w^infinity` as `x_w`. Corollary 1.1 therefore gives

\[
T^L(x_w)=x_w.
\]

Substituting `(5)` yields

\[
(2^L-3^s)x_w=C_w,
\]

which proves `(8)`. The denominator is odd because `2^L` is even and `3^s` is odd. Unique factorization rules out `2^L=3^s`.

Since an odd rational denominator is a unit in `Z_2`, `(8)` indeed belongs to `Z_2`. It is an ordinary integer exactly when the ordinary denominator divides `C_w`, proving `(9)`. If `w` contains an odd branch then `C_w>0`, so its sign is the sign of `2^L-3^s`; the all-zero case gives only `x_w=0`. This proves the sign statements.

Under `3^s<2^L` and `(10)`, the value `x_w` is a positive integer. It has parity itinerary `w^infinity` by construction and is fixed by `T^L`, so its positive orbit is a cycle. ∎

## 4. Eventually periodic positive itineraries

Let an infinite parity word have the form

\[
\eta=u\,w^\infty
\tag{11}
\]

for a finite prefix `u` and a nonempty period block `w`.

### Theorem 2 — eventual periodicity means eventual cycling

If a positive ordinary integer `x_0` realizes `(11)`, then after the prefix `u` its state is the periodic fixed point `x_w`. Consequently:

\[
\boxed{
\text{every positive ordinary eventually periodic parity itinerary
is eventually a positive integer cycle.}}
\tag{12}
\]

In particular:

- a supercritical eventual period `3^s>2^L` has no positive ordinary realization;
- a subcritical eventual period can occur positively only if the entire denominator `2^L-3^s` divides `C_w`;
- after this divisibility test, the finite prefix `u` must still be replayed backwards or forwards exactly to verify a positive integer preimage.

#### Proof

Put

\[
y=T^{|u|}(x_0).
\]

Positivity and integrality of the shortcut map imply `y in Z_(>0)`. Its complete tail itinerary is `w^infinity`, so uniqueness gives `y=x_w`. Theorem 1 now forces the subcritical divisibility alternative and shows that `y` is a positive cycle point. ∎

### Corollary 2.1 — autonomous finite-state schedule firewall

Any autonomous finite-state machine emits an eventually periodic parity word. Therefore such a schedule-first machine cannot certify a divergent positive Collatz orbit. If its output is realized by a positive integer at all, that integer eventually enters a positive cycle, and the existence question reduces to the full-denominator test `(10)` plus exact finite-prefix replay.

This corollary concerns machines that prescribe the parity schedule autonomously. It does not cover a seed-first nonlinear machine whose unbounded ordinary state causally generates a genuinely aperiodic itinerary.

## 5. Trivial and signed-cycle audit

The positive shortcut cycle

\[
1\mapsto2\mapsto1
\]

has primitive parity necklace `10` (or its rotation `01`). Powers or rotations of this necklace satisfy `(10)` but do not disprove Collatz.

A positive integer hit from `(10)` is a counterexample candidate only when the primitive positive cycle is not this trivial necklace.

On the supercritical side, divisibility in `(9)` may produce a negative integer cycle. For example, the periodic word `(110)^infinity` has the negative integer seed `-5`. Other supercritical words, such as `(1110)^infinity`, can have nonintegral rational seeds in `Z_2`. Neither case is a positive counterexample.

## 6. Why this closes a genuine global class

This theorem joins the repository's two repeatedly separated blockers:

```text
ordinary extraction of a periodic inverse-limit path
        =
ordinary divisibility of its complete affine denominator.
```

It eliminates **all** eventually periodic schedule-first divergence constructions, not merely periods below a cutoff and not merely one encoding.

The negative result is genuinely weaker than resolving Collatz: positive Collatz orbits may have aperiodic parity words, and the theorem says nothing about them.

The positive branch is immediately certificate-producing rather than conditional:

```text
full denominator divides C_w
+ positive nontrivial primitive cycle
+ exact replay
    -> finite K-candidate packet.
```

There is no intermediate compactness or top-boundary inference left in the periodic class.

## 7. Relation to the current repository frontier

- PRs `#56` and `#57` identify bounded least roots or eventual residue stabilization as the missing ordinary-extraction theorem for aperiodic nested architectures. `T-7401` shows that, once the tail is periodic, that boundary collapses exactly to finite cycle divisibility.
- The periodic ghost `(1110)^infinity` in PR `#57` is one instance of Theorem 1's supercritical case; the theorem covers every period and every finite preperiod.
- Fixed-modulus lassos, periodic PDR witnesses, autonomous finite-state directives, and eventually periodic refund/type schedules cannot produce divergence. They either select a signed ghost or reduce to a positive cycle.
- The unrestricted six-branch, run-core, changing-height refund, H-renewal, and centered systems remain open only in their genuinely aperiodic seed-first regimes.
- The positive-cycle program's final requirement remains exactly the entire denominator and exact physical replay; proper-factor compatibility is not upgraded by this theorem.

## 8. Gap audit

- The theorem does not decide any genuinely aperiodic itinerary.
- It does not bound the least-root sequence of the fixed six-branch machine.
- It does not prove that a nonlinear seed-first machine becomes eventually periodic.
- It does not construct a nontrivial positive cycle.
- It does not resolve Collatz.

## 9. Suggested next attack

After this theorem, no eventually periodic schedule should be treated as a divergent-orbit candidate. The only load-bearing global targets are:

1. prove boundedness or divergence of the canonical least-root sequence for one fixed aperiodic architecture;
2. prove an architecture-specific theorem forcing every infinite type sequence to become eventually periodic, which would eliminate it by this result;
3. close one finite word by the complete divisor `2^L-3^s` and replay a nontrivial positive cycle.
