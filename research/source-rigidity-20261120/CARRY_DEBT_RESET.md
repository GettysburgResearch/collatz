# Carrying the five multiplier through a supplied convergent spine

**Status: PROPOSED exact ordinary identities and a refuted compiler step.**
The desired physical implication is

\[
x\in C,\quad x\text{ odd},\quad3\nmid x
   \quad\Longrightarrow\quad5x\in C,                 \tag{F5}
\]

where `C` is the basin of 1 for the positive ordinary shortcut map `T`.
The conditional global reduction to (F5) is already proved in **PR157**,
`64361ecca770092d6c8242dc6211e38818af2e50`,
`research/global-closure-20261120/merger.md`, GCM-001–002. This note does
not prove (F5) or give another equivalent condition. It attempts to
compile a supplied ordinary proof `x→1` into a proof for `5x`, retaining
one fixed source and every actual clock.

The precise failure is that two natural exact resets create a new five
question at an antecedent whose convergence is not supplied. Even when
both antecedents are explicitly verified convergent, the reset can
increase their sizes and both of their first-hit clocks simultaneously.
A different rank or an additional ordinary repayment could still work.

The earlier one-odd-event family `x=(4^a−1)/3`, `a≥2`, has
`5x≡1 (mod4)` and the elementary ordinary decrease
`T²(5x)=(15x+1)/4<5x`. A further smaller-partner identity for that
family would not by itself improve least-height coverage. The family
below instead has `x≡5x≡3 (mod4)` and, for the stated large parameters,
its entire displayed target prefix remains above its initial target.

## CD1. The valuation-one case has an exact carry reset

Let `x≡3 (mod4)` be positive. Set

\[
u=\frac{3x+1}{2},\qquad R(x)=\frac{9x+1}{4}.
\]

The following are literal ordinary identities:

\[
T(x)=u,\quad T(5x)=5u-2,
\]

\[
\boxed{\ T^2(x)=R(x)+1,\qquad T^2(5x)=5R(x).\ }       \tag{1}
\]

Both initial inputs on each arm are odd, because `x≡3 (mod4)` implies
`u` odd and `5u−2` odd. Thus a supplied convergent path for `x` supplies
a path for `R(x)+1`. It does **not** supply a path for `R(x)`. Resetting
the five question at `R(x)` therefore has an additional antecedent debt.

This is the `v2(3x+1)=1` branch. The source PR157's synchronized
inverse-lift formula (GCL-002, equation (3a)) concerns exponents at least
two and is not being presented again as a new claim here.

## CD2. Two-odd-event antecedents create arbitrarily deep Mersenne resets

For every integer `r≥0`, put

\[
k=6r+3,\qquad
x_r=\frac{2^{k+2}-5}{9},\qquad
u_r=\frac{2^{k+1}-1}{3}.
\]

These are positive odd integers, and

\[
x_r\equiv3\pmod4,\qquad x_r\equiv2r\pmod3.
\]

Consequently the antecedents eligible for (F5) are exactly those with
`3∤r`. There are infinitely many such `r` in each range below.

The exact supplied path is

\[
x_r\longrightarrow u_r\longrightarrow2^k
       \longrightarrow\cdots\longrightarrow1.       \tag{2}
\]

Its first-hit shortcut clock is `k+2=6r+5`, and it has exactly **two**
odd inputs. Under the odd map `U`, this is `U²(x_r)=1`, with exponent
word `(1,k+1)`.

**Arithmetic.** Since `2^6≡1 (mod9)` and `2^5≡5 (mod9)`, the fraction
for `x_r` is integral. Its residue modulo4 is 3. Modulo27,
`2^(6r+5)=32·64^r≡5+18r`, proving `x_r≡2r (mod3)`. Direct substitution
proves (2). Its intermediate values before 1 are all greater than1, so
the displayed clocks are first-hit clocks.

The reset in (1) is

\[
R(x_r)=2^k-1=:M_r.                                   \tag{3}
\]

It is larger than `x_r`, since

\[
M_r-x_r=\frac{5\cdot2^k-4}{9}>0.
\]

Its actual odd prefix satisfies

\[
U^j(M_r)=3^j2^{k-j}-1\quad(0\le j<k),\qquad
U^k(M_r)=\frac{3^k-1}{2}>1.                           \tag{4}
\]

Here `k` is odd. The first `k−1` odd gaps are one, and the kth gap is two
because `v2(3^k−1)=1`. Thus the odd first-hit clock of `M_r`, if finite,
is at least `k+1`; in particular it cannot be bounded as a function of
the original odd first-hit clock, which is constantly two. This last
failure is unconditional: for every proposed constant bound choose a
larger `r`, and (4) is an actual positive prefix that has not reached1.

The shortcut first-hit clock also increases if it is finite. At clock
`k+1`, the value is `(3^k−1)/2`. Every positive shortcut step is at least
half its input, so reaching1 requires at least the ceiling of its binary
logarithm in further steps. Therefore

\[
d(M_r)\ge k+\lceil\log_2(3^k-1)\rceil
        \ge2k+1>k+2=d(x_r).                          \tag{5}
\]

Neither (4) nor (5) assumes that all `M_r` converge.

A small fully convergent control is `r=1`:

\[
x_1=227,\quad M_1=511,\quad T^2(5\cdot227)=5\cdot511.
\]

Exact first-hit replay gives

| Antecedent | Shortcut clock `d` | Odd count `h` |
|---:|---:|---:|
| 227 | 11 | 2 |
| 511 | 41 | 20 |

Thus even when the new antecedent is supplied with its own finite proof,
this exact reset increases all three coordinates `(source,d,h)`.

## CD3. Following the entire known spine does not automatically repay the carry

Perhaps the first reset is premature. Continue the original two arms
through the whole supplied spine (2). Write

\[
\ell=2r+1,\qquad k=3\ell,\qquad
z_r=\frac{9^{\ell}-1}{8}.
\]

The new value `z_r` is positive, odd, and prime to three. The exact
complete-spine reset is

\[
\boxed{\quad T^{6r+8}(5x_r)=5z_r.\quad}              \tag{6}
\]

The good arm has already reached1 at clock `6r+5`. Formula (6) includes
three subsequent halvings of the other arm. It is not an estimate or a
replacement of one source by a favorable lift.

**Proof.** Equation (1) first gives

\[
T^2(5x_r)=5(2^{3\ell}-1).
\]

For `0≤j≤ell`, the next physical three-step blocks are

\[
T^{3j}\bigl(5(2^{3\ell}-1)\bigr)
  =5\cdot9^j2^{3(\ell-j)}-5.                         \tag{7}
\]

At every nonfinal block, the two first inputs are odd and the third is
even; the exact affine block is `y→(9y+5)/8`. This proves (7) by
induction. At `j=ell`, its endpoint is `5(9^ell−1)`. Since `ell` is odd,
`v2(9^ell−1)=3`, so three more halvings give (6). The total clock is
`2+3ell+3=6r+8`. Modulo3 the value `z_r` is 1, so the new five question
has the correct ternary-unit domain. Its convergence is nevertheless not
provided by the original proof (2). ∎

### The entire displayed target path can increase

For every `r≥5`,

\[
z_r>x_r,
\qquad \frac{z_r}{x_r}\sim\frac{81}{256}
                           \left(\frac{81}{64}\right)^r
                    \longrightarrow\infty.          \tag{8}
\]

Indeed

\[
72(z_r-x_r)=81^{r+1}-256\cdot64^r+31.
\]

At `r=5`, the first two terms already have positive difference because
`3^24>2^38`, following from `531441=3^12>2^19=524288`. Their ratio
increases with `r`, proving the stated strict inequality.

In fact **every nonempty shortcut prefix of the original `5x_r` arm
through clock `6r+8` stays strictly above `5x_r`** for these `r`. Its
first two odd steps increase. Within each block in (7), both odd steps
increase, and the block endpoint `(9y+5)/8` also exceeds its starting
value `y`. During the final three halvings the minimum is the final
value `5z_r`, which exceeds the original source by (8).

This is a delayed descent example for the indicated ordinary path. It
does not exclude a separate smaller merger partner.

### The new antecedent can be worse in both stopping clocks too

For `r≥15`,

\[
z_r>81^r>2^{6r+5}.
\]

The first inequality follows from `(9·81^r−1)/8>81^r`. At `r=15`,
`81^15=3^60>2^95` follows by raising `3^12>2^19` to the fifth power;
the ratio grows afterward. Since any positive first-hit path has
`d(n)≥ceil(log_2 n)`, a finite first-hit clock for `z_r` would satisfy

\[
d(z_r)>6r+5=d(x_r).                                  \tag{9}
\]

If also `r≡3 (mod4)`, then `9^(2r+1)≡57 (mod64)`, so `z_r≡7 (mod8)`.
Its first three shortcut inputs are odd; it cannot reach1 before the
third odd event. Hence any finite odd first-hit clock is at least3,
strictly above `h(x_r)=2`. Restricting to `r≡7,11 (mod12)`, `r≥19`,
keeps the original antecedent prime to three and supplies an infinite
family with all these necessary increases.

A fully convergent explicit instance already occurs at `r=7`:

\[
x=15637498706147,\quad z=25736391511831,\qquad
T^{50}(5x)=5z.
\]

Exact first-hit replay gives

| Antecedent | Shortcut clock `d` | Odd count `h` |
|---:|---:|---:|
| `15637498706147` | 47 | 2 |
| `25736391511831` | 254 | 132 |

Both integers are certified convergent in the companion finite replay.
The reset strictly increases source height, shortcut clock and odd clock.
Consequently **no nonconstant nonnegative weighted combination**

\[
\alpha\log x+\beta d(x)+\gamma h(x),\qquad
\alpha,\beta,\gamma\ge0,
\]

with at least one positive coefficient, decreases on every instance of
this specified full-spine reset. The same conclusion follows for the
first reset from its smaller `227→511` control. This is a concrete
failure of these particular proposed ranks, not a prohibition on all
nonlinear, orientation-sensitive or alternative-certificate ranks.

## What the attempt leaves open

A successful compiler must do something beyond replacing `5x` by the
exact new multiple of five in (1) or (6) and inducting on the supplied
antecedent clocks or height. The new antecedent is not automatically in
`C`; when it is, those proposed resources can all be larger. The actual
first-hit clock of the *unknown target* would decrease along its own
forward orbit if it were finite, but using that clock as an already
well-founded rank would assume the desired convergence.

An ordinary repayment to a different, already certified source, or a
new rank stable under these expansions, remains possible. Neither the
compact conditional certificate in `SINGLE_LAYER_FIVE.md` nor the exact
resets above supply it. The forward-five obligation and full Collatz
remain open.

## Source pins and replay boundary

The broader phenomenon that a bounded odd-event budget on a known arm
need not bound the required budget on its partner is already present in
the concurrent PR146 head `e238c63a5d57f96bb063b7472498d1977df51951`.
Its `BOUNDED_RANK_TRANSFER.md` treats the pair `(x,2x−1)`;
`RANK_THREE_MERSENNE.md` encodes every sufficiently large Mersenne
convergence problem in three-odd-step antecedents; and
`DEEP_REVERSE_BASIN.md` treats the opposite directed family and pure
powers of three. Those source results are not rediscovered here.
The specific addition being recorded is the exact **multiply-by-five
carry reset** (1), its two-odd-event family, the complete-spine reset
(6), and the simultaneous rank increases at explicitly convergent
ordinary controls. The Mersenne odd-prefix calculation is elementary
and shared background, not a claim of a new general transfer theorem.

- PR157 `64361ecca770092d6c8242dc6211e38818af2e50`,
  `research/global-closure-20261120/closing-attempts.md`, GCL-001–002:
  prior one-odd-event antecedents and the inverse-lift synchronized
  formula for gap at least two. CD1–CD3 concern the complementary
  initial gap-one branch and carry its offset through a supplied
  two-odd-event proof.
- PR146 `6863d298187af8b2619efbf78cc4b0aa8e627393`,
  `research/upper-bit-mergers/NEGATIVE_FIVE_CHECKPOINT.md` and
  `FIXED_POINT_EXIT.md`: the ordinary three-step block shadowing the
  signed cycle through `−5` and smaller-partner mechanisms are source
  results. Formula (7) is an application of that block, not a new
  discovery of the signed cycle.
- PR156 Q-section proof, frozen file SHA-256
  `a8ce19689b31abf002c77d6696e351a1f6db781d35b4c17fb21f834bbf08494b`:
  physical orientation, numerical specializations, and fixed-source
  clocks must be retained. No earlier fixed-horizon obstruction is
  being extended by a larger census here.

The checker replays the formulas and the two convergent controls with
exact integers. The family proofs are algebraic and do not assume the
convergence of every reset antecedent.
