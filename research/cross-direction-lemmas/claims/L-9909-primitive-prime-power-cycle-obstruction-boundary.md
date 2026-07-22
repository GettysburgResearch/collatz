# L-9909 -- Primitive-prime-power boundary for accelerated cycle obstructions

Claim ID: `L-9909`
Title: Zsigmondy prime powers do not universally obstruct primitive accelerated cycle words
Status: `PROPOSED / EXACT METHOD BOUNDARY`
Authoring agent: `gpt56-synthesis-01-wave22-completion-master`
Reviewing agents: `gpt56-synthesis-01-wave22-zsigmondy-cycle-obstruction`; `gpt56-synthesis-01` (independent reconstruction); `gpt56-synthesis-01-wave22-h-sunit-transfer` and `l9909-gap-cold-audit` (independent Matveev, continued-fraction, and full-order audits)
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `L-9904` and `L-9906`; Zsigmondy's primitive-divisor theorem; Matveev's explicit logarithmic-form bound (rational specialization)
Scope: nonempty accelerated valuation words over `Z_(>=1)` and prime-power divisors of their exact fixed-point denominator
Related counterexample candidates: none; the construction below silences selected denominator prime powers but does not satisfy the full cycle divisibility condition

## Source freeze and purpose

For a nonempty accelerated valuation word

\[
 w=(a_0,\ldots,a_{k-1}),\qquad a_i\geq 1,
\tag{1}
\]

put

\[
 A_0=0,\qquad A_j=\sum_{i<j}a_i,\qquad A=A_k,
\tag{2}
\]

and

\[
 D_w=2^A-3^k,
 \qquad
 C_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}.
\tag{3}
\]

Call a word **mixed** when it contains at least one letter `1` and at least
one letter at least `2`. By `L-9904`, every nontrivial positive cycle word is
mixed.

`L-9904` proves the complete certificate equivalence

\[
 w\text{ is a positive exact accelerated cycle itinerary}
 \quad\Longleftrightarrow\quad
 D_w>0\text{ and }D_w\mid C_w.
\tag{4}
\]

It also reduces powers and rotations to primitive necklaces. `L-9906`
shows that commuting characteristic-zero block constructions reduce to the
same primitive-root mechanism.

A tempting next step is to factor `D_w`, take a Zsigmondy prime (or prime
power) of a top cyclotomic factor, and try to prove that it cannot divide the
irregular prefix sum `C_w` when `w` is primitive. This claim records the exact
limit of that strategy. Zsigmondy gives useful order information, but that
order information does **not** force nonvanishing of `C_w`, even at the full
prime-power exponent, even for primitive mixed words, and even when the raw
word parameters cross the cycle-search frontiers recorded in issue #9.

The result is a method-boundary theorem, not a cycle construction and not a
disproof of the Collatz conjecture.

## 1. The numerator as a closed multiplicative-walk sum

Work in any residue ring in which `6` is invertible. Define

\[
 t_i={2^{a_i}\over3},
 \qquad
 P_0=1,
 \qquad
 P_j=\prod_{i<j}t_i={2^{A_j}\over3^j}.
\tag{5}
\]

Then

\[
 \boxed{
 C_w=3^{k-1}S_w,
 \qquad
 S_w:=\sum_{j=0}^{k-1}P_j.}
\tag{6}
\]

If a prime `p` divides `D_w`, then

\[
 \prod_{i=0}^{k-1}t_i={2^A\over3^k}\equiv1\pmod p.
\tag{7}
\]

Thus the denominator condition closes the multiplicative walk, whereas the
numerator condition asks for the *additive* sum of its successive vertices to
vanish. Multiplicative order controls (7); it does not generally control the
sum in (6).

## 2. Exactly what cyclotomic factorization supplies

Let

\[
 d=\gcd(A,k),\qquad A=\alpha d,\qquad k=\beta d,
 \qquad \gcd(\alpha,\beta)=1,
\tag{8}
\]

and put

\[
 X=2^\alpha,\qquad Y=3^\beta.
\tag{9}
\]

Then

\[
 \boxed{
 D_w=X^d-Y^d=\prod_{r\mid d}\Phi_r(X,Y),}
\tag{10}
\]

where `Phi_r(X,Y)` is the homogeneous cyclotomic polynomial.

### Proposition 1 -- primitive divisor and exception audit

Assume `D_w>0` and `d>1`. There is a prime `p` dividing `D_w` such that

\[
 \operatorname{ord}_p(XY^{-1})=d.
\tag{11}
\]

Consequently `d | p-1` and `p` divides neither `6` nor `d`. If

\[
 e=\nu_p(D_w),
\tag{12}
\]

then `XY^(-1)` also has exact order `d` modulo `p^e`.

#### Proof

Since `D_w>0`, one has `X>Y`, and `gcd(X,Y)=1`. Zsigmondy's theorem supplies
a primitive prime divisor of `X^d-Y^d` except when either

1. `d=2` and `X+Y` is a power of two, or
2. `(X,Y,d)=(2,1,6)`.

The first exception cannot occur here: `X` is even, `Y` is odd, so `X+Y` is
an odd integer greater than one and hence is not a power of two. The second
cannot occur because `Y=3^beta>=3`. A primitive divisor has multiplicative
order exactly `d`, which proves (11) and the assertions modulo `p`.

Modulo `p^e`, the order reduces to a multiple of `d`, while
`(XY^(-1))^d=1` because `p^e | X^d-Y^d`. Hence the order modulo `p^e` is
again exactly `d`. **QED**

### The `d=1` gap

When `gcd(A,k)=1`, (10) has no nontrivial outer exponent and classical
Zsigmondy supplies no distinguished prime or order. Word primitivity does
not force `gcd(A,k)>1`; the two notions are independent.

Powering cannot repair this gap. If `q=2^A`, `r=3^k`, and `w^s` is a written
power, `L-9904` gives

\[
 D_{w^s}=(q-r)G_s(q,r),
 \qquad
 C_{w^s}=C_wG_s(q,r),
\tag{13}
\]

where

\[
 G_s(q,r)={q^s-r^s\over q-r}.
\tag{14}
\]

Every new primitive divisor produced by applying Zsigmondy to the outer
exponent `s` lies in the geometric factor `G_s` and therefore divides the
numerator automatically. It disappears when the powered representation is
reduced to its primitive root.

## 3. The uncontrolled prefix coordinate

The order in (11) controls only one of the two exponent directions in (6).
This can be made exact. Choose integers `r,s` with

\[
 \beta r+\alpha s=1,
\tag{15}
\]

and define the units

\[
 z=2^\alpha3^{-\beta},
 \qquad
 q=2^r3^s.
\tag{16}
\]

For each prefix put

\[
 \delta_j=\beta A_j-\alpha j,
 \qquad
 m_j=sA_j+rj.
\tag{17}
\]

A direct exponent calculation gives

\[
 \boxed{P_j=z^{m_j}q^{\delta_j}.}
\tag{18}
\]

A Zsigmondy prime controls `ord_p(z)=d`. It supplies no information about
the independent unit `q` or about the irregular prefix discrepancies
`delta_j`. Therefore `S_w` is not, in general, a univariate cyclotomic sum
in the controlled root `z`.

Even in the favorable special case where `w` can be partitioned into `d`
blocks having common totals `(beta,alpha)`, with block constants
`c_0,...,c_(d-1)`, reduction modulo a top primitive divisor gives a weighted
sum of the form

\[
 c_0+zc_1+\cdots+z^{d-1}c_{d-1}.
\tag{19}
\]

Identical blocks make this the usual vanishing geometric sum and correspond
to the powered case. But a nonconstant coefficient vector can also have a
zero Fourier coefficient. Word primitivity alone does not prevent (19) from
vanishing.

## 4. Full prime-power counterfamily

The preceding loss of control is not merely formal. The next theorem makes a
genuine Zsigmondy prime power divide `C_w` to its full exponent.

### Theorem 2 -- a selected primitive prime power can be completely silent

Fix integers

\[
 g>m\ge1,
 \qquad g>1.
\tag{20}
\]

Choose a primitive prime divisor `p` of

\[
 3^g-2^g,
\tag{21}
\]

put

\[
 e=\nu_p(3^g-2^g),
 \qquad
 H=\operatorname{ord}_{p^{e+1}}(2),
 \qquad
 L=1+gH,
\tag{22}
\]

and form the valuation word

\[
 \boxed{w_{g,m}=L^m1^{g-m}.}
\tag{23}
\]

Then all of the following hold.

1. `w_(g,m)` is a primitive mixed word over the positive integers.
2. Its parameters are

   \[
    k=g,
    \qquad
    A=g(1+mH),
    \qquad
    \gcd(A,k)=g.
   \tag{24}
   \]

3. Its denominator is positive.
4. With `X=2^(1+mH)`, the selected prime is a genuine primitive divisor of
   `X^g-3^g=D_(w_(g,m))`.
5. The exact prime-power valuations agree:

   \[
    \boxed{
    \nu_p(D_{w_{g,m}})=e
    =\nu_p(C_{w_{g,m}}).}
   \tag{25}
   \]

In particular, the full component `p^e || D_(w_(g,m))` does not obstruct
cycle divisibility.

#### Proof

Apply Zsigmondy's theorem to the coprime pair `(3,2)`. Its `g=2` exception
would require `3+2=5` to be a power of two, which it is not, and its isolated
sixth-power exception is the pair `(2,1)`, not `(3,2)`. Hence a primitive
prime in (21) exists for every `g>1`. It is odd and does not divide `6g`.

The word (23) contains both `L` and `1`. Viewed cyclically, it has exactly two
transitions between these two symbols. If it were a proper `r`-th power with
`r>=2`, a nonconstant cyclic root would have at least two transitions and
the powered word would have at least `2r>=4`, a contradiction. Thus the word
is primitive and mixed. Summing its letters proves (24).

Because `p` is odd, `H` exists and `H>=2`. Hence

\[
 X=2^{1+mH}>3,
\tag{26}
\]

so

\[
 D_{w_{g,m}}=X^g-3^g>0.
\tag{27}
\]

By the definition of `H`,

\[
 X=2^{1+mH}\equiv2\pmod {p^{e+1}}.
\tag{28}
\]

Consequently

\[
 D_{w_{g,m}}=X^g-3^g
 \equiv 2^g-3^g\pmod {p^{e+1}}.
\tag{29}
\]

The right side has exact `p`-adic valuation `e`, so the denominator in (29)
does as well. Moreover,

\[
 {X\over3}\equiv {2\over3}\pmod p,
\tag{30}
\]

and the latter has order `g` because `p` is primitive for (21). Thus `p` is
a genuine primitive divisor of the top factor for the *new* pair `(X,3)`,
not merely an inherited divisor.

Every letter in (23) is congruent to `1` modulo `H`. Therefore, modulo
`p^(e+1)`,

\[
 2^{a_i}\equiv2,
 \qquad
 P_j={2^{A_j}\over3^j}\equiv\left({2\over3}\right)^j.
\tag{31}
\]

Let `z=2/3`. From (21)--(22),

\[
 \nu_p(z^g-1)=e,
 \qquad
 \nu_p(z-1)=\nu_p(-1/3)=0.
\tag{32}
\]

Hence

\[
 \nu_p\left(1+z+\cdots+z^{g-1}\right)
 =\nu_p\left({z^g-1\over z-1}\right)=e.
\tag{33}
\]

Equations (31) and (33), with congruence retained modulo `p^(e+1)`, give

\[
 \nu_p(S_{w_{g,m}})=e.
\tag{34}
\]

Multiplication by the `p`-adic unit `3^(g-1)` in (6) proves the numerator
part of (25). **QED**

### Simultaneous finite-set strengthening

Let `P` be any finite set of prime divisors of `3^g-2^g`, put

\[
 e_p=\nu_p(3^g-2^g),
\]

and replace `H` in (22) by

\[
 \operatorname{lcm}_{p\in P}
 \operatorname{ord}_{p^{e_p+1}}(2).
\tag{35}
\]

The same proof gives

\[
 \nu_p(D_{w_{g,m}})=\nu_p(C_{w_{g,m}})=e_p
 \qquad(p\in P).
\tag{36}
\]

Thus any prescribed finite collection of primitive divisors can be silenced
simultaneously. The new denominator can have additional prime factors; (36)
does not claim that all of them are silent.

## 5. Frontier parameters

Theorem 2 is not confined to short or structurally inadmissible words. Take

\[
 m=92,
 \qquad
 g>72,000,000,000.
\tag{37}
\]

The primitive root is the word itself, its odd-step length is `k=g`, and

\[
 \#\{i:a_i\ge2\}=m=92.
\tag{38}
\]

By the local-minimum formula in `L-9904`, these are exactly the primitive
odd-step and local-minimum parameters that would apply *if* the word were a
cycle certificate. Hence the failure of the selected prime-power obstruction
persists beyond both coarse lower-bound filters recorded in issue #9.

Nothing here asserts that the remaining prime powers of `D_w` divide `C_w`.
In fact, Theorem 3 and Corollary 3.1 below prove that at least one remaining
prime power always obstructs this lifted family. The word is not a cycle
candidate.

## 6. Why lifting and Wieferich cases do not repair the inference

The exponent `e` in Theorem 2 is arbitrary. In particular, the proof does
not assume that the Zsigmondy divisor occurs squarefreely. If a primitive
prime has a Wieferich-type lift with `e>1`, choosing
`H=ord_(p^(e+1))(2)` makes every letter indistinguishable from `1` through
the exact modulus needed to preserve `e`, but not an extra power. Equations
(29) and (33) then give the same full-exponent equality.

Primes shared between lower cyclotomic factors, including primes associated
with divisors of `d`, have weaker order information and require the usual
LTE bookkeeping. They cannot restore the failed implication for the genuine
top primitive prime already handled by Theorem 2. They may, of course, be
the *other* prime factors that obstruct a particular word.

## 7. Relation to `L-9904` and `L-9906`

The counterfamily does not contradict primitive-root collapse. Its words are
primitive over the integer alphabet. They only *look* like the constant word
`1^g` after reduction modulo `p^(e+1)`, because

\[
 2^L\equiv2^1\pmod {p^{e+1}}.
\tag{39}
\]

The lossless decoder in `L-9904` is a characteristic-zero, exact-integer
statement. It is not injective after reduction modulo an odd prime power,
where powers of two are periodic. Likewise, `L-9906` proves that exact affine
commutation over characteristic zero forces a common word root. Accidental
commutation or identity modulo `p^e` does not invoke that theorem.

This is the exact failed inference:

> Integer primitivity of a valuation word does not imply aperiodicity of its
> affine summary modulo a primitive denominator prime power.

## 8. Small exact audit

For a concrete instance, take

\[
 g=2,\qquad m=1,\qquad p=5,\qquad e=1.
\tag{40}
\]

Here `5` is primitive for `3^2-2^2`,
`ord_(25)(2)=20`, and Theorem 2 gives

\[
 w=(41,1),\qquad k=2,\qquad A=42.
\tag{41}
\]

Then

\[
 D_w=2^{42}-9\equiv -5\pmod {25},
 \qquad
 C_w=3+2^{41}\equiv5\pmod {25}.
\tag{42}
\]

Thus `5 || D_w` and `5 || C_w`, while `(41,1)` is visibly primitive and
mixed. At the same time,

\[
 D_w-C_w=2^{41}-12>0,
\]

so the full denominator does not divide the positive numerator. This audit
shows both the silent selected factor and the escaping cofactor; it is an
illustration of the general proof, not a bounded search result.

## 9. Exact closure obstruction for the lifted two-run family

Theorem 2 silences a selected prime power, but its particular family cannot
silence the full denominator. This follows from a cut identity that does not
factor `D_w`.

### Theorem 3 -- an unavoidable escaping prime power

Let

\[
 w=L^m1^r,
 \qquad
 L\ge2,
 \qquad
 m,r\ge1,
\tag{43}
\]

and abbreviate

\[
 a=2^L,
 \qquad
 U=a^m.
\tag{44}
\]

Then

\[
 \boxed{
 C_w
 =3^r{U-3^m\over a-3}
  +U(3^r-2^r),}
\tag{45}
\]

and

\[
 \boxed{D_w=U2^r-3^{m+r}.}
\tag{46}
\]

They satisfy the exact identity

\[
 \boxed{
 (a-3)C_w
 =D_w+(a-2)U(3^r-2^r).}
\tag{47}
\]

Consequently, if `D_w | C_w`, then

\[
 \boxed{
 D_w\mid (a-2)(3^r-2^r).}
\tag{48}
\]

Now specialize to

\[
 g=m+r,
 \qquad
 g>m\ge2,
 \qquad
 H\ge2,
 \qquad
 L=1+gH.
\tag{49}
\]

Then

\[
 \boxed{
 D_w>(a-2)(3^r-2^r)>0,}
\tag{50}
\]

and therefore `D_w` does not divide `C_w`. Equivalently, at least one
prime-power component of `D_w` is an unavoidable obstruction.

#### Proof

The constant-letter block `L^m` has affine numerator

\[
 {a^m-3^m\over a-3},
\tag{51}
\]

while the block `1^r` has numerator `3^r-2^r`. Applying the chronological
composition law from `L-9904` gives (45), and the total exponents give (46).
Multiplying (45) by `a-3` and substituting (46) gives (47).

Furthermore,

\[
 \gcd(D_w,U)
 =\gcd(U2^r-3^{m+r},U)=1,
\tag{52}
\]

because `U` is a power of two. If `D_w | C_w`, equation (47) therefore
allows the factor `U` to be cancelled modulo `D_w`, proving (48).

It remains to prove the strict size reversal in (50). Under (49),

\[
 a=2^{1+gH}\ge2^{1+2g}>3^m.
\tag{53}
\]

Hence

\[
 {a^m+a-2\over 3^m+a-2}
 >
 {a^m\over2a}
 ={a^{m-1}\over2}
 \ge2^{(1+2g)(m-1)-1}
 \ge2^{2g}
 >
 \left({3\over2}\right)^r.
\tag{54}
\]

Multiplying the outer terms of (54) by the positive quantity
`2^r(3^m+a-2)` gives

\[
 2^r(a^m+a-2)>3^r(3^m+a-2).
\tag{55}
\]

But direct subtraction shows

\[
 D_w-(a-2)(3^r-2^r)
 =2^r(a^m+a-2)-3^r(3^m+a-2),
\tag{56}
\]

so (55) proves (50). The positive integer on the right of (48) is strictly
smaller than `D_w`, which is impossible. **QED**

The condition `m>=2` is essential to the displayed size proof. The lifted
`m=1` family is nevertheless excluded by a separate, sharper identity.

### Corollary 3.1 -- the lifted one-high-letter boundary

Let `g>1`, `H>=2`, `L=1+gH`, and

\[
 w=L1^{g-1}.
\]

Then `D_w` does not divide `C_w`.

#### Proof

Put `r=g-1` and `a=2^L`. The `m=1` specialization of (45)--(46) gives

\[
 C_w+D_w=(a-2)3^r.
\tag{56a}
\]

If `D_w | C_w`, then `D_w | (a-2)3^r`. Moreover,

\[
 \gcd(D_w,3)=1,
\]

because `D_w=a2^r-3^(r+1)` is nonzero modulo `3`. Hence `D_w | a-2`.
On the other hand,

\[
\begin{aligned}
 D_w-(a-2)
 &=a(2^r-1)-3^{r+1}+2\\
 &\ge2^{2r+3}2^{r-1}-3^{r+1}+2\\
 &=2^{3r+2}-3^{r+1}+2>0.
\end{aligned}
\tag{56b}
\]

The last inequality holds at `r=1`, where `2^5>3^2`, and its left
exponential ratio then grows by the factor `8/3`. Thus `D_w>a-2>0`,
contradicting the divisibility. **QED**

Together, Theorem 3 and Corollary 3.1 exclude the entire lifted family
`w_(g,m)` for every `g>m>=1`. The frontier specialization `m=92` uses the
main `m>=2` branch.

## 10. No self-consistent order or Carmichael alias

The most direct attempt to silence every prime power is to choose a common
letter modulus that is an order multiple for the *new denominator itself*.
That fixed point is impossible whenever the new denominator is larger than
the constant-word denominator it imitates.

### Theorem 4 -- residue-word alias obstruction

Let

\[
 w=(a_0,\ldots,a_{k-1}),
 \qquad
 v=(b_0,\ldots,b_{k-1})
\]

be positive valuation words of the same length, with prefix totals `A_j,B_j`
and totals `A,B`. Let

\[
 D=2^A-3^k>1,
\tag{57}
\]

and let `h` be a positive integer such that

\[
 a_i\equiv b_i\pmod h
 \quad(0\le i<k),
 \qquad
 \operatorname{ord}_D(2)\mid h.
\tag{58}
\]

Then

\[
 \boxed{
 D\mid 2^B-3^k,
 \qquad
 C_w\equiv C_v\pmod D.}
\tag{59}
\]

In particular, if `D | C_w`, then also `D | C_v`; and the hypotheses in
(57)--(58) are already impossible if

\[
 0<|2^B-3^k|<D.
\tag{60}
\]

The same conclusion holds if `h` is assumed to be a multiple of the
Carmichael value `lambda(D)`, since `ord_D(2) | lambda(D)`.

#### Proof

Summing the first congruence in (58), both over each prefix and over the
whole word, gives

\[
 A_j\equiv B_j\pmod h,
 \qquad
 A\equiv B\pmod h.
\tag{61}
\]

The order hypothesis therefore yields

\[
 2^{A_j}\equiv2^{B_j}\pmod D,
 \qquad
 2^A\equiv2^B\pmod D.
\tag{62}
\]

Substitution in the prefix sums (3) proves `C_w = C_v (mod D)`.
The definition of `D` also gives `2^A = 3^k (mod D)`, so the
second congruence in (62) proves `D | 2^B-3^k`. This proves (59), and
(60) is immediate. **QED**

### Corollary 4.1 -- any upward alias must cross at minimal positive drift

Retain Theorem 4 and assume additionally that `A>B`. Then its hypotheses can
hold only if

\[
 2^B<3^k<2^A,
 \qquad
 2^A+2^B\le2\cdot3^k.
\tag{62a}
\]

In particular,

\[
 \boxed{A=\left\lceil k\log_2 3\right\rceil.}
\tag{62b}
\]

#### Proof

The right inequality `3^k<2^A` is `D>0`. If `2^B>3^k`, then

\[
 0<2^B-3^k<2^A-3^k=D,
\]

contradicting (59). Equality is impossible by unique factorization, so
`2^B<3^k`. Divisibility in (59) now forces

\[
 D\le3^k-2^B,
\]

which is equivalent to the second inequality in (62a). In particular,

\[
 3^k<2^A<2\cdot3^k.
\]

Therefore

\[
 k\log_2 3<A<k\log_2 3+1.
\]

The middle quantity `A` is an integer and the endpoints are not integers, so
(62b) follows. **QED**

Thus a recursive order-modulus lift cannot add an arbitrary positive drift
margin. If it exists at all, it must cross the critical line from a
negative-drift residue word and land at the unique least positive total.

### Corollary 4.2 -- exact residual exponent-gap target

Under the hypotheses of Corollary 4.1,

\[
 \boxed{D\mid 2^{A-B}-1.}
\tag{62c}
\]

Since every letter of the positive valuation word `v` is at least one,
`B>=k`. Therefore every upward residue-word alias must satisfy the joint
necessary conditions

\[
 \boxed{
 A=\left\lceil k\log_2 3\right\rceil,
 \qquad
 D=2^A-3^k\le2^{A-k}-1.}
\tag{62d}
\]

#### Proof

Equation (59) and the definition of `D` show that `D` divides both
`2^B-3^k` and `2^A-3^k`. Subtracting gives

\[
 D\mid 2^A-2^B=2^B(2^{A-B}-1).
\]

The denominator `D` is odd, so `gcd(D,2^B)=1`; cancelling `2^B` proves
(62c). Since `A>B`, its right side is positive and hence

\[
 D\le2^{A-B}-1\le2^{A-k}-1.
\]

Corollary 4.1 supplies the formula for `A`, proving (62d). **QED**

### Corollary 4.3 -- the residual gap, and hence every upward global alias, is impossible

The joint conditions in (62d) have no integer solution with `k>1`.
Consequently the hypotheses of Theorem 4 cannot hold with `A>B`. (For `k=1`,
the forced value `A=2` gives `D=1`, outside Theorem 4.) Thus the entire
one-global-residue-word upward-alias route is closed.

#### Proof

Put

\[
 \alpha=\log_2 3,
 \qquad
 \delta=A-k\alpha.
\tag{62e}
\]

Unique factorization makes `alpha` irrational, so `0<delta<1`. Dividing the
gap in (62d) by `2^A` gives the useful necessary estimate

\[
 1-2^{-\delta}
 \le 2^{-k}-2^{-A}
 <2^{-k}.
\tag{62f}
\]

We first obtain a proved finite cutoff. Set

\[
 \Lambda=2^A3^{-k}-1={D\over3^k}>0.
\]

The same gap gives

\[
 \Lambda<{1\over2^k-1}<2^{1-k}.
\tag{62g}
\]

The rational specialization of Matveev's explicit theorem, applied with
`(gamma_1,gamma_2)=(2,3)`, `(b_1,b_2)=(A,-k)`, and `B=A`, yields

\[
 \log\Lambda>
 -C_0(1+\log A)\log2\log3,
 \qquad
 C_0=1.4\cdot30^5\cdot2^{4.5}.
\tag{62h}
\]

Here `Lambda!=0`, and the rational logarithmic heights are `log 2` and
`log 3`. Comparing (62g) and (62h) gives

\[
 k-1<C_0\log3\,(1+\log A)
 <9\cdot10^8(1+\log(2k)).
\tag{62i}
\]

For the last inequality, `A<2k` when `k>=4`, because
`alpha<7/4`; also

\[
 C_0\log3
 <{7\over5}\,30^5\cdot24\cdot{11\over10}
 =898128000<9\cdot10^8.
\]

The elementary bounds used here are strict: `sqrt(2)<3/2`, while the
degree-five exponential sum is
`sum_(j=0)^5 (11/10)^j/j!=36015101/12000000>3`, hence
`log 3<11/10`.

Let `K=25000000001`. The exponential series gives `e>27/10`, and

\[
 (27/10)^{26}>(27/10)^{25}>143^5
 =59797108943>2K.
\]

Thus `log(2K)<26`, whereas at `K` the right side of (62i) is less
than `9*10^8*27=24300000000<K-1`. The function

\[
 x\longmapsto x-1-9\cdot10^8(1+\log(2x))
\]

has derivative `1-9*10^8/x>0` for `x>=K`. Hence (62i), and therefore
(62d), is impossible for every `k>=K`.

It remains to give an exact certificate for `1<k<K`. The cases `k=2,3`
are immediate:

\[
 (k,A,D,2^{A-k}-1)=(2,4,7,3),\qquad(3,5,5,3).
\]

Now let `k>=4`. From (62f), using
`-log(1-x)<x/(1-x)` and `log 2>2/3`, one obtains

\[
 0<\delta<-\log_2(1-2^{-k})<2^{1-k}
 \le {1\over2k}.
\tag{62j}
\]

The bound `log 2>2/3` follows at once from the positive atanh series
`log 2=2(1/3+1/(3^3*3)+...)`; and `2^(k-2)>=k` for `k>=4` proves the last
inequality. If `g=gcd(A,k)` and `(p,q)=(A/g,k/g)`, then

\[
 0<{p\over q}-\alpha={\delta\over k}<{1\over2k^2}
 \le {1\over2q^2}.
\]

Legendre's criterion therefore makes `p/q` an upper continued-fraction
convergent of `alpha`. The exact certified prefix needed below is

\[
 \alpha=[1;1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,\ldots].
\tag{62k}
\]

Its upper convergents through the cutoff are:

| index `n` | `p_n` | `q_n` | `q_(n+1)` |
|---:|---:|---:|---:|
| 1 | 2 | 1 | 2 |
| 3 | 8 | 5 | 12 |
| 5 | 65 | 41 | 53 |
| 7 | 485 | 306 | 665 |
| 9 | 24727 | 15601 | 31867 |
| 11 | 125743 | 79335 | 111202 |
| 13 | 301994 | 190537 | 10590737 |
| 15 | 17087915 | 10781274 | 53715833 |
| 17 | 272500658 | 171928773 | 225644606 |
| 19 | 630138897 | 397573379 | 6189245291 |
| 21 | 10439860591 | 6586818670 | 65470613321 |

The final displayed next denominator exceeds `K`, so this list is complete.
The convergent `2/1` cannot occur because `A<2k`. For `8/5`, write
`k=5g`, `A=8g`. Then (62f) would require

\[
 1-(243/256)^g<2^{-5g},
\]

but its left side is at least `13/256>1/32`, a contradiction.

For every remaining row, `q>=41`. The standard two-sided convergent bound
gives, for an upper convergent,

\[
 p-q\alpha>{1\over q+q_{\rm next}}.
\tag{62l}
\]

Across the remaining table, the maximum of `q+q_next` is
`72057431991<2^40`. Hence

\[
 p-q\alpha>2^{1-q}.
\]

But `k=gq`, `A=gp`, so (62j) simultaneously requires

\[
 g(p-q\alpha)=\delta<2^{1-gq}\le2^{1-q},
\]

the final contradiction.

The finite certificate is independently executable at
[`../proofs/L-9909-gap-certificate.py`](../proofs/L-9909-gap-certificate.py).
It uses only Python integer and `Fraction` arithmetic. Specifically, for
`z=(x-1)/(x+1)` it encloses each logarithm by

\[
 2\sum_{j=0}^{N-1}{z^{2j+1}\over2j+1}
 <\log x<
 2\sum_{j=0}^{N-1}{z^{2j+1}\over2j+1}
 +{2z^{2N+1}\over(2N+1)(1-z^2)}
\]

with `N=96`, then performs the continued-fraction interval algorithm and all
cutoff checks exactly. No floating-point census is used. **QED**

### Corollary 4.4 -- the full-denominator order exceeds the total excess

Let `A,k` be positive integers, put

\[
 D=2^A-3^k>1,
 \qquad
 h=\operatorname{ord}_D(2).
\]

Then

\[
 \boxed{h>A-k.}
\tag{62m}
\]

Consequently, for every positive valuation word of length `k` and total
`A`,

\[
 \boxed{a_i\le A-k+1\le h\qquad(0\le i<k).}
\tag{62n}
\]

Thus reduction of the letters modulo the full-denominator order is
letterwise vacuous when positive residues are represented by
`{1,2,...,h}` (so a multiple of `h` is represented by `h`, not by zero).

#### Proof

The denominator `D` is odd, so `h` exists. Suppose instead that
`h<=A-k`. Consider the two positive length-`k` words

\[
 w=(A-k+1,1^{k-1}),
 \qquad
 v=(A-k+1-h,1^{k-1}).
\]

Their corresponding totals are `A` and `B=A-h<A`, and their letters are
componentwise congruent modulo `h`. They therefore satisfy Theorem 4, but
Corollary 4.3 says that such an upward global alias is impossible. This proves
(62m). For `k=1` the same construction is simply `w=(A)`, `v=(A-h)`;
the assumed inequality `h<=A-1` keeps `v` positive. The omitted borderline
`A=2` has `D=1` and is outside the statement.

Finally, positivity of all `k-1` other letters gives
`a_i<=A-(k-1)=A-k+1`, while the integral inequality (62m) gives
`h>=A-k+1`. This is (62n) and proves the positive-residue assertion. **QED**

The common-residue version is obtained by taking `v=c^k`. Thus, if every
letter of `w` is congruent to the same positive integer `c` modulo `h`, then

\[
 D\mid 2^{ck}-3^k.
\]

For the lifted family of Theorem 2, take `c=1`, `h=H`, and `k=g`. If `H`
were an order multiple for its own new denominator, (59) would give

\[
 D_{w_{g,m}}\mid 3^g-2^g.
\tag{63}
\]

But `A=g(1+mH)>=2g`, and for `g>1`,

\[
 D_{w_{g,m}}-(3^g-2^g)
 =2^A+2^g-2\cdot3^g>0.
\tag{64}
\]

For `g=2`, the lower bound `A>=2g` makes the right side at least
`4^2+2^2-2*3^2=2`; for `g>=3`, already `4^g>2*3^g`.
Thus (63) is impossible. No recursive choice with `H` a multiple of
`ord_D(2)` or `lambda(D)` can make the new word look like `1^g`
simultaneously modulo every prime-power factor of its own denominator.

Theorem 4 addresses a single alias word modulo a common order multiple.
Different prime powers could in principle annihilate `C_w` through different
nonconstant modular walks, with no one smaller word representing all of
them. The theorem does not identify or exclude those prime-dependent walks
for an arbitrary word.

## 11. Dependency and gap audit

- The exact cycle criterion is imported only from `L-9904`.
- The cyclotomic normalization uses `d=gcd(A,k)`; it does not assume that
  word primitivity implies `d=1` or `d>1`.
- Both classical positive-base Zsigmondy exceptions are checked explicitly
  for the Collatz pair and for the auxiliary pair `(3,2)`.
- No assumption is made that a primitive divisor is large, unique, or
  squarefree.
- The modulus `p^(e+1)` is essential: it preserves the exact valuations of
  both `D_w` and `C_w`, including higher-lifting cases.
- The word-primitivity proof is combinatorial and independent of modular
  primitivity.
- The frontier specialization changes only `g,m`; no finite census is used.
- The simultaneous strengthening silences only the selected old factors.
  It does not claim closure under the additional factors of the new
  denominator.
- Theorem 3 and Corollary 3.1 prove that an additional obstructing prime
  power must exist throughout the lifted family for every `g>m>=1`; they do
  not identify that factor and do not cover arbitrary valuation words.
- Theorem 4 excludes a self-consistent lift of any one residue word through
  a common order or Carmichael modulus. Prime-dependent nonconstant
  cancellation patterns with no global residue word remain outside its
  scope.
- Corollary 4.1 shows that any upward alias escaping the direct size
  contradiction must cross from negative drift and land at
  `A=ceil(k log_2 3)`; Corollary 4.2 then forces the exponentially small gap
  `2^A-3^k<=2^(A-k)-1`.
- Corollary 4.3 excludes that gap for every `k>1`, using Matveev only to
  obtain the explicit cutoff `k<25000000001`. The finite part is not a
  numerical census: Legendre's criterion reduces it to the certified upper
  convergents in (62k), and the linked certificate encloses both logarithms
  by exact rational intervals.
- Corollary 4.4 has no cycle-divisibility hypothesis: for every
  `D=2^A-3^k>1`, it proves `ord_D(2)>A-k`. Hence no positive letter can wrap
  around modulo the full denominator order. This does not control reduction
  modulo the smaller, different orders of individual prime-power factors.
- The Matveev specialization, including the factor
  `1.4*30^5*2^4.5`, is an external theorem. Every subsequent relaxation of
  its constant and every cutoff comparison is displayed explicitly.
- No word in this claim is asserted to satisfy `D_w | C_w`. Producing such a
  word would be an actual nontrivial Collatz cycle certificate and is not
  achieved here.

## Strongest conclusion

> Zsigmondy's theorem and multiplicative-order lifting cannot, by themselves,
> provide a universal prime-power obstruction to the accelerated Collatz
> cycle equation. A primitive mixed valuation word can reduce to a complete
> geometric orbit modulo a genuine top-cyclotomic prime power, making that
> full component divide both the exact denominator and the irregular prefix
> numerator. This remains possible with arbitrarily large primitive odd-step
> length and at least 92 local minima. For the explicit lifted family, however,
> an exact cut identity and size bound prove that some other prime-power factor
> always obstructs, and no self-consistent order/Carmichael choice can silence
> the whole denominator by lifting any one smaller residue word with excess
> drift. In fact the only remaining one-global-alias case would force
> `A=ceil(k log_2 3)` and `2^A-3^k<=2^(A-k)-1`; an explicit Matveev cutoff
> plus an exact continued-fraction certificate excludes that gap for every
> `k>1` (and `k=1` has `D=1`). Equivalently, the full-denominator base-two
> order always exceeds `A-k`, so global positive-residue reduction cannot
> change a single letter. What remains open is the corresponding claim for
> arbitrary primitive mixed words with genuinely prime-dependent nonconstant
> cancellations; by `L-9904`, that claim is precisely the unresolved
> nontrivial-cycle exclusion in factorwise form.

## Source links

- [L-9904 -- primitive-root collapse for compressed accelerated cycles](./L-9904-compressed-cycle-primitive-root.md)
- [L-9906 -- commuting compressed cycle blocks collapse to one primitive root](./L-9906-compressed-cycle-commuting-block-collapse.md)
- [Zsigmondy, *Zur Theorie der Potenzreste* (1892)](https://doi.org/10.1007/BF01692444)
- [Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II* (2000)](https://doi.org/10.1070/IM2000v064n06ABEH000314)
- [Languasco--Luca--Moree--Togbe, Theorem 2.1 (rational specialization of Matveev)](https://doi.org/10.1007/s12188-025-00293-9)

## Suggested next attack

The lifted construction is now closed: selected old factors can be silenced,
but Theorem 3 forces an escaping factor and Theorem 4 forbids an order-modulus
fixed point obtained by lifting one global residue word. Any successful next
route must therefore use prime-dependent, nonconstant cancellation patterns
and information coupling the *entire* factorization of `D_w` to the actual
prefix-discrepancy sequence in (17). Corollaries 4.1--4.3 close the last
single-residue-word upward-lift possibility, including its near-critical
power gap, and Corollary 4.4 shows that full-order residue reduction is always
letterwise trivial. The next viable target must couple the distinct local
orders and cancellations of several prime-power factors. A genuinely
stronger endpoint would be the uniform upper bound

\[
 \gcd(D_w,C_w)<D_w
\tag{65}
\]

for every nontrivial primitive mixed word, proved by a global resultant,
subspace, or cross-prime argument rather than by selecting one Zsigmondy
factor.
