# L-6912 — Complete-factor synchronization for the short displacement

**Claim ID:** `L-6912`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-08-01  
**Issue:** #75  
**Dependencies:** corrected `L-6909`; PR #81 `L-6809/L-6812`; elementary CRT  
**Scope:** complete prime-power factorizations of coefficient-first-crossing denominators

## 1. Setup

Let `w` be a coefficient-first-crossing shortcut-parity word of length `j`
and weight `q`. Put

\[
P=2^j,\qquad Q=3^q,\qquad D=P-Q>0,
\]

and write

\[
T_w(r)=s=r+d,\qquad d\ge0.
\]

The corrected bilateral identities are

\[
\boxed{A_w=Dr+Pd=Ds+Qd.}
\tag{1}
\]

By `L-6812/L-6909`,

\[
\boxed{0\le d<E_w:=A_w/P<q/3.}
\tag{2}
\]

Factor the complete denominator into pairwise coprime prime powers

\[
D=\prod_{\nu=1}^{t}M_\nu.
\tag{3}
\]

No factor may be omitted in a certificate.

## 2. Exact gcd profile

For every prime `p` and exponent `e` with `p^e|D`, equation `(1)` gives

\[
A_w\equiv Qd\pmod {p^e}.
\]

Since `gcd(Q,D)=1`,

\[
\boxed{
\min\{\nu_p(A_w),e\}
=
\min\{\nu_p(d),e\}.}
\tag{4}
\]

Consequently,

\[
\boxed{\gcd(D,A_w)=\gcd(D,d).}
\tag{5}
\]

Thus:

```text
d=0:
  gcd(D,A_w)=D; this is the full positive-cycle level.

d>0:
  gcd(D,A_w)<=d<q/3; only a short part of D can occur in A_w.
```

Equation `(5)` is a complete finite-place distinction between cycles and
acyclic near-returns. It does not by itself exclude either case.

## 3. Large prime powers must agree on one ordinary d

For every complete prime-power factor define

\[
\delta_\nu=[A_wQ^{-1}]_{M_\nu}
\in\{0,\ldots,M_\nu-1\}.
\tag{6}
\]

If `w` is a non-descending realization, then

\[
d\equiv\delta_\nu\pmod {M_\nu}
\qquad(1\le\nu\le t).
\tag{7}
\]

Call `M_\nu` **large** when

\[
M_\nu>E_w.
\tag{8}
\]

Because `0<=d<E_w<M_\nu`, equation `(7)` then lifts without ambiguity:

\[
\boxed{\delta_\nu=d
\quad\text{for every large }M_\nu.}
\tag{9}
\]

This gives the exact pairwise obstruction:

\[
\boxed{
M_\mu,M_\nu>E_w
\ \text{and}\ 
\delta_\mu\ne\delta_\nu
\quad\Longrightarrow\quad
\text{canonical descent}.}
\tag{10}
\]

Let

\[
S=\prod_{M_\nu\le E_w}M_\nu
\tag{11}
\]

be the complete small-factor block. Conversely, a short displacement exists
at the congruence level if and only if:

1. all large-factor residues in `(6)` equal one integer `d<E_w`; and
2. the same integer satisfies
   \[
   A_w\equiv Qd\pmod S.
   \tag{12}
   \]

Adding positivity of

\[
r=\frac{A_w-Pd}{D}
\tag{13}
\]

then gives the exact physical near-return by corrected `L-6909`.

Hence complete prime-power compatibility is not a collection of independent
local hits. Every factor must synchronize to one common ordinary integer.

## 4. Unitary block residues

For any unitary divisor `U|D`, put `C=D/U`, so `gcd(U,C)=1`, and define

\[
\delta_U=[A_wQ^{-1}]_U.
\tag{14}
\]

If `U>E_w`, a candidate again forces

\[
\boxed{\delta_U=d.}
\tag{15}
\]

Therefore two complementary unitary blocks `U,C>E_w` reject the word whenever

\[
\delta_U\ne\delta_C.
\tag{16}
\]

This is stronger than checking their prime-power components separately:
several individually small residues can combine to a large CRT residue.

## 5. Endpoint and source quotient jets

Assume `U|A_w-Q\delta_U`. Define the endpoint jet

\[
\sigma_U
=
\left[
\frac{A_w-Q\delta_U}{U}
\,C^{-1}
\right]_U.
\tag{17}
\]

Similarly, since `P≡Q (mod D)`, define the source jet

\[
\rho_U
=
\left[
\frac{A_w-P\delta_U}{U}
\,C^{-1}
\right]_U.
\tag{18}
\]

For a genuine near-return and every unitary `U`,

\[
\sigma_U\equiv s\pmod U,
\qquad
\rho_U\equiv r\pmod U.
\tag{19}
\]

Let

\[
\mathcal B_j
=
\left\lceil
\frac{q}{3(1-Q/P)}+\frac q3
\right\rceil.
\tag{20}
\]

No descent and `(2)` give

\[
0<r,s<\mathcal B_j.
\tag{21}
\]

Hence, whenever `U>\mathcal B_j`, the two jets lift to exact ordinary values:

\[
\boxed{\delta_U=d,\qquad
\sigma_U=s,\qquad
\rho_U=r.}
\tag{22}
\]

A large factor therefore carries two levels of information:

```text
first residue:
  the common displacement d;

quotient residue:
  the common endpoint/source after dividing out that factor.
```

## 6. Balanced-or-dominant factor dichotomy

Assume

\[
D>\mathcal B_j^3.
\tag{23}
\]

Then one of the following useful alternatives exists.

### Balanced alternative

There is a unitary factorization

\[
D=UV,\qquad U>\mathcal B_j,\quad V>\mathcal B_j.
\tag{24}
\]

### Dominant alternative

There is one complete prime-power factor `W|D` with

\[
c:=D/W\le\mathcal B_j,
\qquad
W>D/\mathcal B_j>\mathcal B_j^2.
\tag{25}
\]

### Proof

If a prime-power component has complementary cofactor at most
`\mathcal B_j`, it gives `(25)`. Otherwise every component has complement
larger than `\mathcal B_j`.

If one component itself exceeds `\mathcal B_j`, use it and its complement for
`(24)`. If every component is at most `\mathcal B_j`, multiply components
until their product `U` first exceeds `\mathcal B_j`. Minimality gives
`U<=\mathcal B_j^2`, and `(23)` gives
`V=D/U>\mathcal B_j`. This proves the dichotomy. ∎

An effective lower bound for `j log 2-q log 3` makes `(23)` automatic
cofinally: `D` is exponential up to a polynomial loss, whereas
`\mathcal B_j` is polynomial. The exact dichotomy itself is source-free.

## 7. The two irreducible complete-factor obstructions

The balanced case requires simultaneous equality of two independently
computable exact jets:

\[
\boxed{
\delta_U=\delta_V=d,\qquad
\sigma_U=\sigma_V=s,\qquad
0\le d<E_w,\quad0<s<\mathcal B_j.}
\tag{26}
\]

A mismatch at either level proves descent.

In the dominant case, the giant prime power `W` determines `d,r,s` exactly by
`(22)`. The remaining obligation is the small-cofactor test

\[
c\mid\frac{A_w-Qd}{W}
\tag{27}
\]

together with the first-crossing and positivity gates.

Thus the complete factor problem has been reduced to:

```text
balanced:
  two large blocks must return exactly the same d and the same quotient jet;

dominant:
  one giant prime power must return small d,r,s,
  and one small cofactor must complete the divisibility.
```

This is the smallest exact local-to-global obstruction left by the complete
factorization. No proper-factor hit or order-cover reconstruction substitutes
for `(26)` or `(27)`.

## 8. Gap audit

- `L-6912` is lossless but does not prove that the synchronized jets never
  occur.
- The cycle level `d=0` remains explicitly included.
- A large prime factor by itself is insufficient when its residue is short.
- The balanced and dominant alternatives are both compatible with all current
  size bounds.
- Closing FC* now requires a theorem excluding `(26)` and `(27)` for the
  rough first-crossing excess paths, not another count of candidate words.
