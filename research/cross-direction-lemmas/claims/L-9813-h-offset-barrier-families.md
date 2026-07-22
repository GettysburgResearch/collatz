# L-9813 — Word-specific offset barriers for H crossings

Claim ID: `L-9813`  
Title: Exact offset sums certify strict displacement for infinite first-crossing H families  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: the exact H block and cylinder formulas restated below; `L-9807` for context only  
Scope: genuine expanding-to-contracting H word crossings  
Related counterexample candidates: none

## Definitions

For an H letter `r>=0`, put

\[
m_r=\frac{3^{2r+1}}{2^{3r+2}}.
\tag{1}
\]

For an exact word `w`, use the normalized affine data

\[
f_w(x)=M_wx+q_w,
\qquad
M_w=\frac{V_w}{U_w},
\qquad
q_w=\frac{B_w}{U_w},
\tag{2}
\]

and its canonical input/output `A_w,Y_w`. Write

\[
D_w=U_w-V_w,
\qquad
\Delta_w=A_w-Y_w.
\tag{3}
\]

Appending a letter gives the exact offset recurrence

\[
\boxed{q_{ur}=m_rq_u+\frac14.}
\tag{4}
\]

Thus, for `w=(r_0,...,r_(L-1))`,

\[
\boxed{
q_w
=\frac14\sum_{k=0}^{L-1}
\prod_{i=k+1}^{L-1}m_{r_i}.
}
\tag{5}
\]

The displacement has the exact real normal form

\[
\boxed{
\Delta_w=A_w(1-M_w)-q_w.
}
\tag{6}
\]

If the first letter is `s`, exact-cylinder congruence gives

\[
\boxed{
A_w\equiv8^s\pmod{4\cdot8^s},
\qquad A_w\ge8^s.
}
\tag{7}
\]

## Statement

### 1. Two strict word-specific barriers

Let `w` be contracting, so `M_w<1`.

First, the integrality of `Delta_w` gives

\[
\boxed{q_w<1\Longrightarrow 0\le\Delta_w<D_w.}
\tag{8}
\]

Second, if `w` begins with `s`, its exact first residue strengthens this to

\[
\boxed{
q_w<8^s(1-M_w)
\Longrightarrow
0<\Delta_w<D_w.
}
\tag{9}
\]

The second criterion can certify strict displacement even when the terminal
prefix offset is larger than one.

### 2. The original zero-tail family

Put

\[
H=\log(4/3),
\qquad
L=\log(9/8),
\qquad
\alpha=\frac LH,
\tag{10}
\]

and for `s>=3` define

\[
a=\lfloor\alpha s\rfloor,
\qquad n=a+1=\lceil\alpha s\rceil.
\tag{11}
\]

The indexing in (11) is essential: `n`, not `a`, is the least positive
exponent with

\[
(9/8)^s(3/4)^n<1.
\tag{12}
\]

For

\[
o_s=(s,0^a),
\tag{13}
\]

every proper prefix is expanding and the full word is contracting. Moreover,

\[
q_{o_s}=1-(3/4)^n<1,
\tag{14}
\]

so (8) proves

\[
0\le\Delta_{o_s}<D_{o_s}
\qquad(s\ge3).
\tag{15}
\]

Put

\[
D=4^n8^s-3^n9^s,
\qquad K=4^n-3^n.
\tag{16}
\]

The equality boundary is exact:

\[
\boxed{
\Delta_{o_s}=0
\iff
D\mid K.
}
\tag{17}
\]

The exceptional divisibility is absent for a natural-density-one set of
`s`. More precisely, put

\[
R_s=(9/8)^s(3/4)^a=(4/3)^{\{\alpha s\}}.
\tag{18}
\]

Then `D<=K` implies the exponentially thin shrinking target

\[
\boxed{
0<1-\{\alpha s\}
<\frac{8}{7H}8^{-s}.
}
\tag{19}
\]

Consequently `D>K`, and hence `Delta_(o_s)>0`, for a natural-density-one set
of `s`. The completely elementary subfamily

\[
R_s\le\frac54
\tag{20}
\]

already has natural density

\[
\frac{\log(5/4)}{\log(4/3)}=0.775660\ldots
\tag{21}
\]

and satisfies `D>K` for every `s>=2`.

### 3. A strict infinite family beyond the `q<1` test

There are infinitely many sufficiently large `s` for which

\[
\frac65<R_s<\frac54.
\tag{22}
\]

For each such `s`, define

\[
v_s=(s,0^{a-1}),
\qquad
u_s=(v_s,3,2),
\qquad
w_s=(u_s,0).
\tag{23}
\]

Then `w_s` is a genuine global first contracting prefix and

\[
\boxed{0<\Delta_{w_s}<D_{w_s}.}
\tag{24}
\]

This family is invisible to the old terminal-zero test because

\[
\boxed{q_{u_s}>1.}
\tag{25}
\]

### 4. Arithmetic filters on the equality boundary

For the integers in (16),

\[
\boxed{
\gcd(D,K)=\gcd(K,9^s-8^s).
}
\tag{26}
\]

If `D|K`, set

\[
v=K/D,
\qquad t=(9^s-8^s)/D.
\]

Then

\[
\boxed{
8^sv-3^nt=1,
\qquad
9^sv-4^nt=1,
\qquad
\gcd(v,t)=1.
}
\tag{27}
\]

One immediate finite-state exclusion is

\[
\boxed{
s\equiv n\not\equiv0\pmod4
\Longrightarrow D\nmid K.
}
\tag{28}
\]

## Proof

Equation (4) follows by composing one normalized H block with `f_u`; iteration
gives (5). Since

\[
Y_w=M_wA_w+q_w,
\]

equation (6) is immediate. If `Delta_w<=-1`, then (6) gives

\[
q_w=A_w(1-M_w)-\Delta_w\ge1,
\]

which proves the lower bound in (8). If (9)'s hypothesis holds, (7) makes the
right side of (6) strictly positive. In both cases, `A_w<U_w` and `q_w>0`
give

\[
\Delta_w<A_w(1-M_w)<U_w(1-M_w)=D_w.
\]

This proves (8)--(9).

The multiplier of the first letter `s` is

\[
m_s=(3/4)(9/8)^s.
\]

Equations (11)--(12) therefore prove the first-crossing assertion for (13).
Repeated use of (4), beginning with the one-letter value `q_s=1/4`, gives
(14), and (8) proves (15).

For (13), direct multiplication gives

\[
U=4^n8^s,
\qquad V=3^n9^s,
\qquad B=8^s(4^n-3^n)=8^sK.
\tag{29}
\]

Thus `Delta=0` is equivalent to `DA=B`. Since `D` is odd,
`gcd(D,8^s)=1`, so an integral canonical fixed point exists exactly when
`D|K`. This proves (17).

Let

\[
\Lambda=nH-sL=H(1-\{\alpha s\})>0.
\]

Then `V/U=exp(-Lambda)` and

\[
D=4^n8^s(1-e^{-\Lambda}).
\]

If `D<=K`, division by `4^n8^s` and `K/4^n<1` give

\[
1-e^{-\Lambda}<8^{-s}.
\]

Hence

\[
0<\Lambda<-\log(1-8^{-s})\le\frac87,8^{-s},
\]

which is (19). The irrationality of `alpha` follows from unique
factorization: a rational relation would equate a nonzero power of `2` with a
power of `3`. Irrational equidistribution now shows that the shrinking target
in (19) has density zero. Indeed, for every fixed `epsilon>0`, all sufficiently
late exceptional points lie in `(1-epsilon,1)`, whose visit density is
`epsilon`.

If `R_s<=5/4`, then `V/U=(3/4)R_s<=15/16`, so

\[
D\ge\frac{4^n8^s}{16}>4^n>K
\qquad(s\ge2).
\]

Equidistribution gives (21).

For the stronger family, irrational density supplies infinitely many hits in
the open interval (22), and `a>=3` for all sufficiently large hits. The
multiplier of `v_s` is exactly `R_s`. Put

\[
k=m_3m_2=\frac{3^{12}}{2^{19}},
\qquad1<k<\frac{65}{64}.
\tag{30}
\]

All prefixes through `v_s` expand, appending `3,2` leaves multiplier `R_sk>1`,
and the final zero gives

\[
M_{w_s}=\frac34R_sk
<\frac34\cdot\frac54\cdot\frac{65}{64}
=\frac{975}{1024}<1.
\tag{31}
\]

The offsets are

\[
q_{v_s}=1-(3/4)^a,
\qquad
q_{u_s}=kq_{v_s}+\frac{499}{1024}.
\tag{32}
\]

Since `a>=3`,

\[
q_{u_s}>
\frac{37}{64}+\frac{499}{1024}
=\frac{1091}{1024}>1,
\]

proving (25). On the other hand,

\[
q_{u_s}<\frac{97}{64},
\qquad
q_{w_s}=\frac34q_{u_s}+\frac14<\frac{355}{256}<2.
\tag{33}
\]

Equations (7), (31), and `s>=3` give

\[
A_{w_s}(1-M_{w_s})
>8^s\frac{49}{1024}
\ge\frac{49}{2}>q_{w_s}.
\]

Criterion (9) proves (24).

Finally, reducing `D` modulo `K` in (16) gives

\[
D\equiv3^n(8^s-9^s)\pmod K.
\]

Because `gcd(3^n,K)=1`, this proves (26). The exact identities

\[
8^sK-3^n(9^s-8^s)=D,
\qquad
9^sK-4^n(9^s-8^s)=D
\]

give (27). If `s congruent to n mod4`, reduction modulo `5` gives `5|D`.
For the three nonzero residue classes, `4^n-3^n` is nonzero modulo `5`, so
`5 does not divide K`; this proves (28). ∎

## Motivation

`L-9807` showed that coarse carry rectangles cannot settle the first mixed-sign
crossing. The present result inserts two genuinely word-specific invariants:
the ordered offset sum and the first exact-cylinder residue. They close strict
displacement on explicit infinite families, including one deliberately beyond
the previous scalar threshold.

## Dependency audit

- The H multiplier, offset recurrence, and first-letter residue are restated
  and used directly.
- Irrational equidistribution of one rotation is the only standard dynamical
  input.
- No instance of the empirical global claim `PR19/C-9501` is assumed.
- The stronger family proves both displacement inequalities directly from
  (6), rather than importing a canonical upper-bound conjecture.

## Gap audit

- Density-one strictness for `(o_s)` does not exclude every exceptional `s`.
- A standard effective lower bound for the linear form `Lambda` would reduce
  the remaining cases to a finite range, but no Baker/Matveev constant or
  external dependency is imported here.
- The congruence filters in (28) cover only part of the shrinking target.
- These are finite H words, not an infinite H or Collatz trajectory.

## Adversarial tests

- Confusing `a` with `n=a+1` breaks both the first-crossing and offset formulas;
  (11)--(14) use the corrected indexing.
- The family `(w_s)` remains expanding after its letter `2` because the product
  `m_3m_2` is greater than one, even though `m_2<1`.
- The proof of strictness uses `q_(w_s)<2`, not the false inequality
  `q_(u_s)<1`.
- Equation (17) does not assert that the divisibility occurs; without an
  instance, no H cycle is claimed.

## Remaining uncertainty

The exact divisibility `D|K` has not been excluded for every `s`. It lies in an
exponentially thin Diophantine target and satisfies the CRT constraints
(26)--(28).

## Suggested next attack

Import an explicit two-logarithm lower bound for
`n log(4/3)-s log(9/8)`, calculate its finite cutoff, and combine it with the
modular sieve in (28). Independently, search for other short suffixes whose
multiplier and offset place them beyond `q<1` while the first-letter barrier
still proves strict displacement.
