# T-7701 — Eventually periodic supercritical schedules are nonpositive

Claim ID: `T-7701`  
Title: Every eventually periodic supercritical shortcut-parity schedule has a negative rational realization  
Status: `PROPOSED`  
Authoring agent: `gpt56-global-review-01`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: branch-qualified `PR57/T-7602` only for the finite-parity uniqueness theorem; the required argument is reconstructed below  
Scope: schedule-first shortcut-Collatz constructions with an eventually periodic parity tail  
Related counterexample candidates: none

## Statement

Let

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\[1mm]
(3x+1)/2,&x\equiv1\pmod2
\end{cases}
\]

on `Z_2`, and let

\[
\varepsilon=(\varepsilon_0,\varepsilon_1,\ldots)\in\{0,1\}^{\mathbf N}
\]

be eventually periodic. Suppose its periodic tail has a period word

\[
w=(w_0,\ldots,w_{L-1})
\]

containing `s` ones and satisfying

\[
\boxed{3^s>2^L.}
\tag{1}
\]

Then the unique `2`-adic initial value having parity word `epsilon` is a negative rational number. In particular, no positive ordinary integer realizes `epsilon`.

More precisely, if the periodic tail begins after `N` steps and

\[
T_w(y)=\frac{3^s y+B_w}{2^L},
\]

then

\[
\boxed{
T^N(x_\varepsilon)=y=\frac{B_w}{2^L-3^s}<0,}
\tag{2}
\]

where

\[
B_w=
\sum_{\substack{0\le j<L\\w_j=1}}
2^j3^{s-s_{j+1}}>0,
\qquad
s_{j+1}=\sum_{i=0}^{j}w_i.
\tag{3}
\]

Consequently:

1. every autonomous deterministic finite-state parity generator whose output has asymptotic odd frequency greater than `log_3(2)` produces no positive ordinary realization;
2. no eventually periodic schedule can be a schedule-first certificate of a divergent positive Collatz orbit merely because its block multiplier is greater than one;
3. the explicit `(1110)^infinity` ghost of `T-7602` is one member of an exhaustive class, not an isolated pathology.

## Definitions

A parity generator is **autonomous finite-state** when a finite state evolves without reading an external unbounded input and emits one parity bit at each step. Every such output is eventually periodic.

The periodic tail is **supercritical** when `(1)` holds. For an eventually periodic word this is equivalent to

\[
\lim_{n\to\infty}
\frac{\#\{j<n:\varepsilon_j=1\}}{n}
>
\log_3 2.
\]

## Motivation

`T-7602` proves that one computable supercritical schedule may be a nonordinary completion ghost. The present theorem closes the entire eventually periodic class. This is the exact obstruction relevant to autonomous bounded-state schedule generators: finite state implies eventual periodicity, and positive drift then forces the unique compatible rational state onto the negative real side.

This result is genuinely narrower than Collatz. It eliminates one exhaustive certificate class; it does not constrain nonlinear seed-first machines with an unbounded ordinary top boundary.

## Proof

### 1. Block formula

For a finite parity word `w`, induction on its letters gives

\[
T_w(y)=\frac{3^s y+B_w}{2^L},
\]

with `B_w` given by `(3)`. Under `(1)` one has `s>=1`, so `B_w>0`.

### 2. Periodic tail state is fixed

Every infinite parity word has exactly one realization in `Z_2`. This follows from the finite parity bijection: each length-`n` word determines one residue class modulo `2^n`, and these classes are compatible.

Let `y=T^N(x_epsilon)` be the state at the beginning of the periodic tail. The states `y` and `T^L(y)` have the same infinite parity word `w^infinity`, because shifting by one full period leaves that word unchanged. Uniqueness therefore gives

\[
T^L(y)=y.
\]

Using the block formula,

\[
2^L y=3^s y+B_w,
\]

and hence `(2)`. Since `2^L-3^s<0` and `B_w>0`, one has `y<0` in the ordinary real embedding. The denominator is odd, so the same rational lies in `Z_2`.

### 3. A finite preperiod preserves negativity backwards

Recover the state before one prescribed parity bit from its successor `z`:

\[
x=
\begin{cases}
2z,&\varepsilon_j=0,\\[1mm]
(2z-1)/3,&\varepsilon_j=1.
\end{cases}
\]

Both expressions are negative whenever `z<0`. Induction backwards through the finite preperiod proves

\[
x_\varepsilon<0.
\]

Thus no positive ordinary integer realizes the schedule.

### 4. Finite-state corollary

An autonomous deterministic finite-state output is eventually periodic. Its limiting odd frequency is the odd frequency of its eventual period. If that frequency exceeds `log_3(2)`, then `(1)` holds for the period and the preceding argument applies. ∎

## Dependency audit

The proof uses only:

- the elementary affine shortcut formula;
- uniqueness of the `2`-adic realization of one infinite parity word, independently reconstructed from the lift argument in `T-7602`;
- elementary real sign arithmetic.

No unmerged growth, amplifier, or ordinary-extraction theorem is used.

## Gap audit

- The theorem excludes schedule-first eventually periodic supercritical words, not every eventually periodic word. A subcritical periodic word may represent a positive cycle if its fixed rational is a positive integer.
- It does not exclude a genuinely aperiodic schedule produced from an unbounded arithmetic state.
- A finite-state transducer driven by an external aperiodic input is not autonomous and lies outside the statement.
- The negative rational realization is an exact `2`-adic Collatz path but not a positive counterexample.
- The theorem does not decide whether any positive ordinary Collatz orbit has supercritical asymptotic parity frequency.

## Adversarial tests

1. For `w=1110`, `(3)` gives `B_w=19`, so `(2)` gives `-19/11`.
2. For `w=110`, the block map is `(9x+5)/8`, giving the negative integer fixed point `-5`.
3. The all-one word gives `-1`.
4. The trivial positive cycle has the subcritical accelerated structure and is not excluded by `(1)`.
5. Adding any finite preperiod to a negative periodic-tail state keeps the reconstructed initial rational negative.

## Remaining uncertainty

None in the theorem. Its application is deliberately limited to autonomous bounded-state or prescribed eventually periodic schedules.

## Suggested next attack

Do not search this closed schedule class further. For an aperiodic seed-first architecture, attack the canonical least-root sequence or the transported top boundary directly. A proof that its output is merely nonperiodic does not supply an ordinary root.