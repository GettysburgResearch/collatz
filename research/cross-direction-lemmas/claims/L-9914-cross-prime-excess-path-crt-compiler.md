# L-9914 -- Lossless cross-prime compiler for accelerated cycle words

Claim ID: `L-9914`
Title: Prime-power excess paths glue uniquely, and their local periods must span a primitive word
Status: `PROPOSED / EXACT CONSTRUCTIVE REDUCTION`
Authoring agent: `gpt56-synthesis-01-wave25-crossprime-cycle`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `L-9904` (complete cycle certificate) and `L-9909`
(full-denominator order bound)
Scope: complete prime-power factorizations of positive accelerated-cycle
denominators
Related counterexample candidates: none; the compiler is lossless, but no
compatible full-denominator local-path tuple is constructed here

## 1. Purpose

For a positive valuation word

\[
 w=(a_0,\ldots,a_{k-1}),\qquad a_i\geq1,
\tag{1}
\]

put

\[
 A_j=\sum_{i<j}a_i,\qquad A=A_k,
\tag{2}
\]

\[
 C_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j},
 \qquad D=2^A-3^k.
\tag{3}
\]

By `L-9904`, one nontrivial positive cycle would be certified by

\[
 D>0,\qquad D\mid C_w,
\tag{4}
\]

followed automatically by positive integral replay with every exact
valuation.  `L-9909` shows that reducing every letter modulo the one global
order `ord_D(2)` is vacuous.  The remaining constructive possibility is to
let different prime powers of `D` see different modular walks.

This claim gives the exact gluing theorem for those walks.  It also proves a
cross-prime obstruction that is absent at any one factor: locally periodic
aliases can support a primitive integer word only when their periods jointly
span the full word length.

No existence inference is made.  Finding the local paths required by the
compiler is still the full cycle problem in a factorized form.

## 2. Excess coordinates and the full order window

Assume throughout that

\[
 D>1,
 \qquad
 D=\prod_{s=1}^{r}Q_s,
 \qquad
 Q_s=p_s^{\nu_s},
\tag{5}
\]

is the complete factorization into pairwise coprime prime powers.  Define

\[
 h_s=\operatorname{ord}_{Q_s}(2),
 \qquad
 H=\operatorname{lcm}_{1\leq s\leq r}h_s
   =\operatorname{ord}_{D}(2).
\tag{6}
\]

Write the total and prefix excesses above the all-one word as

\[
 E=A-k,
 \qquad
 e_j=A_j-j=\sum_{i<j}(a_i-1).
\tag{7}
\]

Then

\[
 0=e_0\leq e_1\leq\cdots\leq e_k=E.
\tag{8}
\]

Corollary 4.4 of `L-9909` gives the decisive strict window

\[
 \boxed{H>E.}
\tag{9}
\]

In particular, a simultaneous residue class modulo all the `h_s` has at
most one representative in `[0,E]`.

## 3. The lossless factorwise compiler

For every `s`, suppose local data are given in the form

\[
 \epsilon_{s,j}\in\mathbf Z/h_s\mathbf Z
 \qquad(0\leq j\leq k).
\tag{10}
\]

Think of `epsilon_(s,j)` as the proposed residue of the prefix excess `e_j`
seen at the prime power `Q_s`.

### Theorem 1 -- exact excess-path CRT reconstruction

There is a positive valuation word of length `k` and total `A` whose prefix
excesses realize all the local data in (10) if and only if the following
conditions hold.

1. **Endpoint conditions:**

   \[
    \epsilon_{s,0}=0,
    \qquad
    \epsilon_{s,k}=E\pmod {h_s}
    \qquad(1\leq s\leq r).
   \tag{11}
   \]

2. **Generalized-CRT compatibility:** for every `j,s,t`,

   \[
    \epsilon_{s,j}\equiv\epsilon_{t,j}
       \pmod {\gcd(h_s,h_t)}.
   \tag{12}
   \]

3. **Window and path conditions:** let `hat e_j` be the unique simultaneous
   CRT representative in `[0,H-1]`.  Then

   \[
    0=\widehat e_0\leq\widehat e_1\leq\cdots
      \leq\widehat e_k=E.
   \tag{13}
   \]

When these conditions hold, the word is unique and is reconstructed by

\[
 \boxed{a_j=1+\widehat e_{j+1}-\widehat e_j.}
\tag{14}
\]

If, in addition, every local path annihilates its prime-power numerator,

\[
 \boxed{
 \sum_{j=0}^{k-1}3^{k-1-j}2^{j+\epsilon_{s,j}}
 \equiv0\pmod {Q_s}
 }
 \qquad(1\leq s\leq r),
\tag{15}
\]

then the reconstructed word satisfies

\[
 \boxed{D\mid C_w.}
\tag{16}
\]

Consequently (5), (11)--(15), and `D>0` are a constructive full positive
cycle certificate.  By `L-9904`, no separate intermediate integrality or
valuation assumptions are needed after (16).

#### Proof

An actual word gives the path (7)--(8).  Reducing `e_j` modulo every `h_s`
immediately gives (11)--(12), and its representative already lies in
`[0,E]`, so uniqueness from (9) gives (13).  Equation (14) is just the
difference of consecutive prefix excesses.

Conversely, (12) is the necessary and sufficient compatibility criterion
for simultaneous congruences with noncoprime moduli.  Thus every
`hat e_j` exists modulo `H`.  Condition (13) and formula (14) give positive
integer letters with

\[
 \sum_{j=0}^{k-1}a_j
 =k+\widehat e_k-\widehat e_0=A.
\]

Their prefix excesses are exactly the `hat e_j`; (9) shows that no other
path in `[0,E]`, and hence no other word, realizes the same local tuple.

Finally, `A_j=j+hat e_j`.  Since powers of two depend only on their exponent
modulo `h_s` in `Z/Q_s Z`, (15) is exactly `C_w=0 (mod Q_s)`.  The prime
powers in (5) are pairwise coprime and complete, so CRT gives (16). **QED**

### Corollary 1.1 -- an order-cover subset already decodes the word

Let `S` be any subset of the prime-power factors and put

\[
 H_S=\operatorname{lcm}_{s\in S}h_s.
\tag{17}
\]

If `H_S>E`, then compatible local excess paths for the factors in `S`
already reconstruct at most one integer word by (11)--(14), with `H_S` in
place of `H`.  Their vanishing proves only

\[
 \prod_{s\in S}Q_s\mid C_w;
\tag{18}
\]

every omitted prime power must still be checked.  Thus an order-cover can
remove word ambiguity without turning a proper-factor hit into a cycle.

## 4. Which locally periodic factors vanish automatically

Fix one factor `Q=p^nu`, put `h=ord_Q(2)`, and reduce every affine letter

\[
 f_a(x)={3x+1\over2^a}
\tag{19}
\]

modulo `Q`.  Suppose the residue word `a_i mod h` has a cyclic period
`d|k`.  Write `k=md`, let `u` be its first `d` letters, and put

\[
 B=\sum_{i=0}^{d-1}a_i,
 \qquad
 \rho=3^d2^{-B}\pmod Q,
 \qquad
 \tau=C_u2^{-B}\pmod Q.
\tag{20}
\]

The values of `B` and `C_u2^(-B)` in (20) depend only on the letter residues
modulo `h`, so every length-`d` block induces the same affine map

\[
 F_u(x)=\rho x+\tau\pmod Q.
\tag{21}
\]

### Proposition 2 -- local geometric silence

Under the preceding hypotheses,

\[
 F_w=F_u^m,
 \qquad
 \rho^m=1\pmod Q,
\tag{22}
\]

and

\[
 C_w2^{-A}
 \equiv
 \tau(1+\rho+\cdots+\rho^{m-1})\pmod Q.
\tag{23}
\]

If

\[
 \rho\not\equiv1\pmod p,
\tag{24}
\]

then `rho-1` is a unit modulo `Q`, the geometric sum in (23) vanishes, and

\[
 \boxed{Q\mid C_w.}
\tag{25}
\]

If (24) fails, periodicity alone does not prove (25); the exact valuation of
the geometric sum and the block translation must be retained.

#### Proof

Congruent letters modulo `h` induce identical maps (19) modulo `Q`, which
proves the first identity in (22).  The full multiplier is
`3^k2^(-A)=1 (mod Q)` because `Q|D`, proving the second.  Iterating the
affine map (21) gives (23).  Under (24), `rho-1` is invertible modulo the
prime power, and

\[
 1+\rho+\cdots+\rho^{m-1}
 ={\rho^m-1\over\rho-1}=0\pmod Q.
\]

Since `2` is a unit modulo `Q`, this proves (25). **QED**

Proposition 2 is the precise factorwise mechanism behind a local powered
alias.  Different factors may use different residue blocks and different
periods.  The next theorem records the global compatibility cost.

## 5. Local periods must span a primitive word

For every full prime-power factor `Q_s`, let `d_s|k` be the least cyclic
period of

\[
 (a_0,\ldots,a_{k-1})\pmod {h_s}.
\tag{26}
\]

### Theorem 3 -- cross-prime period-span obstruction

Put

\[
 t=\operatorname{lcm}_{1\leq s\leq r}d_s.
\tag{27}
\]

Then `t|k` and `t` is an exact integer period of the word:

\[
 \boxed{a_{i+t}=a_i\qquad(i\bmod k).}
\tag{28}
\]

Consequently, if `w` is primitive, then

\[
 \boxed{\operatorname{lcm}_s d_s=k.}
\tag{29}
\]

The same conclusion follows from any order-cover subset `S` with `H_S>E`:
a primitive word requires `lcm_(s in S)d_s=k`.

#### Proof

Every `d_s` divides `k`, so their least common multiple does as well.  Since
`t` is a multiple of `d_s`, (26) gives

\[
 a_{i+t}\equiv a_i\pmod {h_s}
 \qquad\hbox{for every }s.
\tag{30}
\]

Therefore `H` divides `a_(i+t)-a_i`.  Positivity and total excess give

\[
 1\leq a_i\leq E+1,
 \qquad
 |a_{i+t}-a_i|\leq E<H.
\tag{31}
\]

The only multiple of `H` in this interval is zero, proving (28).  If
`t<k`, (28) writes the word as a proper power, contrary to primitivity.
The order-cover variant uses `H_S` in exactly the same argument. **QED**

### Corollary 3.1 -- factor-dependent constant aliases are still trivial

Suppose every prime power sees a constant residue word, although the
constant may depend on the factor:

\[
 a_i\equiv b_s\pmod {h_s}
 \qquad\hbox{for all }i,s.
\tag{32}
\]

Then every `d_s=1`, so Theorem 3 makes `w` a constant integer word.  If it
also satisfies `D>0` and `D|C_w`, then

\[
 w=(2)^k,
\tag{33}
\]

the trivial cycle itinerary.

Indeed, for `w=(a)^k`,

\[
 C_w={2^{ak}-3^k\over2^a-3}={D\over2^a-3}.
\tag{34}
\]

Positive drift forces `a>=2`.  At `a=2`, (34) gives the all-2 word and the
fixed point `1`; for `a>=3`, one has `0<C_w<D`, so divisibility is
impossible.

This closes a stronger alias than the one-global-word construction excluded
in `L-9909`: even factor-dependent constant residues cannot cooperate across
the complete denominator to make a primitive nontrivial word.

### Corollary 3.2 -- proper local powers require an order-sized wrap

Let

\[
 R=\max_i a_i-\min_i a_i\leq E.
\tag{35}
\]

If `h_s>R`, equality modulo `h_s` is injective on the letter alphabet of
`w`.  Hence the local residue period `d_s` is already an exact word period.
For a primitive word, necessarily

\[
 d_s=k.
\tag{36}
\]

Equivalently, a proper local powered alias at a factor of a primitive word
requires

\[
 h_s\leq R\leq E;
\tag{37}
\]

some two letters must differ by a nonzero multiple of that local order.

## 6. Arithmetic sanity check

At

\[
 (A,k)=(13,8),\qquad E=5,\qquad
 D=2^{13}-3^8=1631=7\cdot233,
\tag{38}
\]

the local orders are

\[
 \operatorname{ord}_7(2)=3,qquad
 \operatorname{ord}_{233}(2)=29,qquad
 H=87>5.
\tag{39}
\]

Thus any compatible pair of excess paths modulo `3` and `29` has at most one
lift through the six possible excess values `0,...,5`.  A vanishing path at
only one factor is not enough; vanishing at both reconstructs and certifies
the full denominator condition.  The known exact prime sieve at this packet
finds no path vanishing modulo `233`; (38)--(39) are included only as a small
orientation check for the compiler, not as a new census.

## 7. Boundary audit

1. **Complete factorization.**  Theorem 1 proves `D|C` only when every
   prime-power component of `D` is included.  Corollary 1.1 deliberately
   distinguishes decoding from full certification.
2. **Prime powers, not just primes.**  The moduli are `p^nu || D`, and the
   local order and numerator congruence are taken at that full exponent.
3. **Noncoprime orders.**  The `h_s` need not be coprime.  Condition (12),
   not an ordinary coprime-only CRT slogan, is the exact compatibility test.
4. **Prefix excess, not raw letters.**  Numerator terms contain `A_j`; the
   compiler therefore glues the monotone prefix path.  Gluing unrelated
   letter residues without (13) can produce no positive word.
5. **Positive representative.**  The reconstructed path is selected in
   `[0,E]`.  A CRT class whose least representative exceeds `E` is rejected,
   not wrapped through a negative increment.
6. **Local periodicity is only sufficient in the unit case.**  If
   `rho=1 (mod p)`, the geometric sum need not vanish modulo `p^nu`.
7. **Primitivity.**  Theorem 3 concerns cyclic periods dividing `k`.  A
   period smaller than `k` is a proper written power and must be reduced by
   `L-9904` before cycle bounds are interpreted.
8. **No counterexample.**  No complete compatible tuple satisfying (15) is
   produced.  Modular cancellation at a proper divisor, a 2-adic point, or a
   changing finite family would not meet (4).

## Strongest conclusion

> Prime-dependent cancellation is a legitimate remaining architecture, but
> it is not a collection of independent modular choices.  Complete local
> excess paths must satisfy generalized CRT compatibility at every prefix;
> the strict order window `ord_D(2)>A-k` then reconstructs at most one actual
> positive valuation word.  Locally powered factors can vanish by a genuine
> affine geometric sum, yet a primitive word forces the least local periods
> across any order-cover to have least common multiple exactly `k`.
> Factor-dependent constant aliases collapse to the all-2 trivial cycle.
> What remains is to construct one compatible nonconstant full-factor tuple,
> or prove that every such tuple fails at some prime power.

## Suggested next attack

Build each prime-power solver as a finite automaton with state

\[
 (j,\ e_j\bmod h_s,\ C_j\bmod Q_s),
\]

intersect the automata first on an order-cover subset with `H_S>E`, and apply
the monotone-window reconstruction before touching the remaining factors.
Reject every local-period assignment whose least periods have lcm below `k`.
Only a word surviving those exact gates should be sent to full-denominator
division and the independent replay theorem of `L-9904`.
