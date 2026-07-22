# L-9820 — Quotient-parity lift for the missing padding-address bit

Claim ID: `L-9820`  
Title: The next padding-address bit is one explicit dyadic quotient parity of the ordinary bulk word  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9808`, `L-9810`, `L-9811`, `L-9817`; `PR3/T-0028` for the four padding charts; Christol's theorem only for the automaticity characterization  
Scope: one-bit inversion of a 2-adic isometry and the scale-boundary padding bit  
Related counterexample candidates: none

## Definitions

For `x in 2^h Z_2`, define its dyadic quotient bit by

\[
\operatorname{qbit}_h(x)
=\left(\frac{x}{2^h}\right)\bmod2
\in\{0,1\}.
\tag{1}
\]

Let

\[
\Omega:\mathbb Z_2\longrightarrow\mathbb Z_2
\tag{2}
\]

be a bijective isometry. Given `w in Z_2`, let

\[
s=\Omega^{-1}(w).
\]

For `h>=0`, write

\[
a_h=[s]_{2^h}\in[0,2^h),
\qquad a_0=0,
\tag{3}
\]

for the canonical ordinary representative of the first `h` address bits.

For the inverse bulk, retain the notation of `L-9808`:

\[
A_m=1+2^{e_m}V_m,
\qquad
u_m=-A_m^{-1}V_m,
\qquad
s_m=\Omega^{-1}(u_m).
\tag{4}
\]

## Statement

### 1. Universal one-bit inverse-isometry formula

Suppose an ordinary representative `a_h in [0,2^h)` satisfies

\[
\Omega(a_h)\equiv w\pmod{2^h}.
\tag{5}
\]

Define

\[
\boxed{
\varepsilon_h(w,a_h)
=\operatorname{qbit}_h\bigl(w-\Omega(a_h)\bigr).
}
\tag{6}
\]

Then the unique lift of the inverse address is

\[
\boxed{
a_{h+1}
=a_h+2^h\varepsilon_h(w,a_h)
\in[0,2^{h+1}).
}
\tag{7}
\]

Thus no derivative unit or lookup table is required at one bit: modulo `2`,
the normalized displacement of every isometry is `1`.

### 2. Below the bulk scale, the target is just `-V_m`

`L-9808` gives

\[
u_m\equiv-V_m\pmod{2^{e_m}}.
\tag{8}
\]

Consequently, for every `0<=h<e_m`, if

\[
a_{m,h}=[s_m]_{2^h},
\]

then

\[
\boxed{
\varepsilon_{m,h}
=\operatorname{qbit}_h
\bigl(-V_m-\Omega(a_{m,h})\bigr),
\qquad
a_{m,h+1}=a_{m,h}+2^h\varepsilon_{m,h}.
}
\tag{9}
\]

Starting with `a_(m,0)=0`, recurrence (9) constructs

\[
\boxed{
a_{m,e_m}=[s_m]_{2^{e_m}}
}
\tag{10}
\]

in exactly `e_m` one-bit lifts, using only `V_m mod 2^(e_m)` and finite
evaluations of `Omega`. This is a sequential specification of the finite
inverse permutation in `L-9811`, not a black-box invocation of it.

### 3. The old boundary bit and the universal toggle

Put

\[
H_m=e_m-1,
\qquad
a_m=[s_m]_{2^{H_m}}.
\tag{11}
\]

The previously missing old bit in position `H_m` is

\[
\boxed{
\varepsilon_m
=\operatorname{qbit}_{H_m}
\bigl(-V_m-\Omega(a_m)\bigr).
}
\tag{12}
\]

Equivalently,

\[
[s_m]_{2^{e_m}}=a_m+2^{e_m-1}\varepsilon_m.
\tag{13}
\]

The universal toggle `L-9817/(12)` now gives the next stabilized prefix
without any call to `Omega_(e_m)^(-1)`:

\[
\boxed{
[s_{m+1}]_{2^{e_m}}
=a_m+2^{e_m-1}(1-\varepsilon_m).
}
\tag{14}
\]

### 4. Integer quotient formula for a `PR3/T-0028` chart

Fix one padding chart

\[
\Omega(s)
=\frac{\mu_*+3^{-g_*-7Ps}}{2^{r+1}},
\qquad
P=2^{r-1}.
\tag{15}
\]

For a canonical prefix `a in [0,2^h)`, put

\[
G(a)=g_*+7Pa.
\tag{16}
\]

Assume `G(a)>=0`, as in the physical tower charts. If

\[
\Omega(a)\equiv-V_m\pmod{2^h},
\tag{17}
\]

then the ordinary integer

\[
\boxed{
Q_{m,h}(a)
=\bigl(2^{r+1}V_m+\mu_*\bigr)3^{G(a)}+1
}
\tag{18}
\]

is divisible by `2^(h+r+1)`, and

\[
\boxed{
\varepsilon_{m,h}
=
\left(
\frac{Q_{m,h}(a)}{2^{h+r+1}}
\right)\bmod2.
}
\tag{19}
\]

Only the residue

\[
Q_{m,h}(a)\pmod{2^{h+r+2}}
\tag{20}
\]

is needed. Hence the power `3^G(a)` may be evaluated by ordinary modular
binary exponentiation; the exponentially large full integer is unnecessary.

At the scale boundary `h=e_m-1`, equations (14) and (19) give the promised
single-bit identity

\[
\boxed{
\begin{aligned}
\varepsilon_m
&=
\left(
\frac{
\bigl(2^{r+1}V_m+\mu_*\bigr)
3^{g_*+7Pa_m}+1
}{2^{e_m+r}}
\right)\bmod2,\\
[s_{m+1}]_{2^{e_m}}
&=a_m+2^{e_m-1}(1-\varepsilon_m).
\end{aligned}
}
\tag{21}
\]

The first numerator in (21) is always divisible by `2^(e_m+r)`.

### 5. All four physical chart formulas

For the `q=3,a=7` bulk, `e_m=m+2`. The four instances of (21) are:

| mismatch | `r` | `P` | `7P` | quotient-parity numerator | divisor |
|---:|---:|---:|---:|---|---:|
| 5 | 5 | 16 | 112 | `(64 V_m + mu_*) 3^(g_*+112 a_m) + 1` | `2^(m+7)` |
| 6 | 4 | 8 | 56 | `(32 V_m + mu_*) 3^(g_*+56 a_m) + 1` | `2^(m+6)` |
| 7 | 3 | 4 | 28 | `(16 V_m + mu_*) 3^(g_*+28 a_m) + 1` | `2^(m+5)` |
| 8 | 2 | 2 | 14 | `(8 V_m + mu_*) 3^(g_*+14 a_m) + 1` | `2^(m+4)` |

In each row, divide the displayed numerator by the displayed exact power of
two, take its parity, call the result `epsilon_m`, and use the second line of
(21). The data requirements are exactly:

- `V_m mod 2^(m+2)`;
- the lower prefix `a_m mod 2^(m+1)`;
- the fixed-core data `r,P,mu_*,g_*`;
- modular exponentiation at modulus `2^(m+r+3)`.

No higher bit of `V_m`, no completed inverse bulk, and no inverse counter
permutation is used for this boundary bit.

### 6. Representative and residue warning

Formula (6) is an identity in `Z_2`; formula (19) is its ordinary canonical
implementation. Three distinctions are essential.

1. The exponent in (18) uses the canonical representative
   `a in [0,2^h)`. Replacing it by `a+k 2^h` generally changes the quotient
   parity. The corresponding correction to the high lift bit makes the final
   class (7) invariant, but the naked symbol `epsilon_(m,h)` is
   representative-dependent.
2. `-V_m` may be reduced modulo `2^(h+1)` before (9). Any two compatible
   representatives differ by a multiple of `2^(h+1)`, which changes the
   quotient by an even number and leaves its parity unchanged. Reducing only
   modulo `2^h` discards the very bit being computed.
3. In (18), reducing the numerator modulo `2^(h+r+1)` always gives zero and
   destroys the answer. One must retain one additional bit, as in (20), before
   dividing.

If a nonphysical chart presentation has `G(a)<0`, equation (19) remains valid
2-adically after interpreting `3^G(a)` as an odd modular inverse. The
integer-divisibility wording then applies after clearing that odd denominator.

## Proof

By the isometry property,

\[
D_h(a_h)
=\frac{\Omega(a_h+2^h)-\Omega(a_h)}{2^h}
\in\mathbb Z_2^\times.
\tag{22}
\]

Every odd unit is `1 mod 2`. Therefore, for `epsilon in {0,1}`,

\[
\Omega(a_h+\varepsilon2^h)
\equiv
\Omega(a_h)+\varepsilon2^h
\pmod{2^{h+1}}.
\tag{23}
\]

Condition (5) makes the quotient in (6) integral. Equation (23) matches the
target modulo `2^(h+1)` exactly when `epsilon` is its parity. This proves
(6)--(7).

From `L-9808/(6)` with compiler depth `L=1`,

\[
\nu_2(u_m+V_m)=e_m.
\tag{24}
\]

Thus (8) holds, and replacing `w=u_m` by `-V_m` in every lift with
`h+1<=e_m` does not change its quotient parity. This proves (9)--(10) and
(12)--(13).

`L-9817/(12)` says

\[
s_{m+1}-s_m\equiv2^{e_m-1}\pmod{2^{e_m}}.
\tag{25}
\]

Adding (25) to (13) flips the coefficient of `2^(e_m-1)` and proves (14).

For the physical chart, (17) is equivalent to

\[
-2^{r+1}V_m-\mu_*-3^{-G(a)}
\in2^{h+r+1}\mathbb Z_2.
\tag{26}
\]

Multiplication by the odd unit `-3^G(a)` turns the left side into

\[
\bigl(2^{r+1}V_m+\mu_*\bigr)3^{G(a)}+1
=Q_{m,h}(a).
\]

This proves the asserted divisibility. Moreover,

\[
\frac{Q_{m,h}(a)}{2^{h+r+1}}
=-3^{G(a)}
\frac{-V_m-\Omega(a)}{2^h}.
\tag{27}
\]

The multiplier on the right is odd and hence `1 mod 2`; taking parity proves
(19). Setting `h=e_m-1` and inserting the four values of `r,P` proves
(21) and the table. ∎

## Automaticity corollary and audit

Write the completed address from `L-9811` as

\[
s_\infty=\sum_{j\ge0}d_j2^j,
\qquad d_j\in\{0,1\},
\tag{28}
\]

and recall `H_m=e_m-1=m+sigma-2`. The old quotient bit has the exact
completion-word description

\[
\boxed{
\varepsilon_m=1-d_{H_m}.
}
\tag{29}
\]

Indeed, `L-9811/(7)` gives

\[
\nu_2(s_\infty-s_m)=H_m.
\]

Thus `s_infinity` and `s_m` agree below position `H_m` and have opposite bits
in position `H_m`. By (13), that bit of `s_m` is exactly `epsilon_m`, proving
(29). Equivalently, `L-9817/(12)` toggles `epsilon_m` into the newly stable
completion bit `d_(H_m)` at the next scale.

Because the indices `H_m` run through every integer from `sigma-1` onward,
`L-9810` now implies

\[
\boxed{
(\varepsilon_m)_{m\ge1}
\text{ is not eventually periodic.}
}
\tag{30}
\]

Consequently no autonomous finite-state generator can emit these bits: the
orbit of one state under a deterministic self-map of a finite state set is
eventually periodic, as is every fixed output read from that orbit.

This negative result does **not** rule out 2-automaticity. Finite shifts,
finite prefixes, and bit complementation preserve 2-automaticity in both
directions, so (29) gives the exact equivalence

\[
\boxed{
(\varepsilon_m)_{m\ge1}\text{ is 2-automatic}
\iff
(d_j)_{j\ge0}\text{ is 2-automatic}.
}
\tag{31}
\]

By Christol's theorem this is further equivalent to algebraicity of the
formal digit series

\[
D(X)=\sum_{j\ge0}d_jX^j
\]

over `F_2(X)`. The known transcendence of the 2-adic value `s_infinity` over
`Q` does not decide that separate formal-series question. In particular, the
growing-prefix recurrence (19) is neither a proof nor a disproof of
2-automaticity. Nor does nonperiodicity of the full word by itself decide the
behavior on a proper arithmetic subsequence.

## Motivation

`L-9817` reduces the padding transition to finite logarithmic arithmetic but
isolates one missing datum: the old address bit in position `e_m-1`. The
present lemma shows that this datum is not hidden in high residual precision.
It is exactly one dyadic quotient bit of the positive ordinary bulk `V_m` and
the already-known lower counter prefix.

The striking simplification is (8). At every precision needed for the next
stable scale bit, the geometric inverse compiler has not yet contributed its
first correction, so the full target may be replaced by the single ordinary
word `-V_m`.

## Dependency audit

- `L-9808/(6)` at `L=1` gives the exact congruence (8).
- The abstract one-bit recurrence uses only exact isometry.
- `L-9810` rules out eventual periodicity of the completed address word.
- `L-9811/(7)` identifies the exact completion bit opposite to the old
  quotient bit.
- `L-9817/(12)` supplies the universal scale-boundary toggle.
- `PR3/T-0028` supplies the four values of `r,P` and the exponential chart
  formula.
- Christol's theorem is used only to state the equivalent unresolved formal
  power-series criterion; no automaticity conclusion is imported from it.
- No logarithm, completed address, or residual-cylinder theorem enters the
  quotient-bit proof.

## Gap audit

- Recurrence (9) is sequential finite arithmetic; it is not yet a bounded
  local Collatz rewrite or a finite-state transducer uniform in `m`.
- The nonperiodicity corollary excludes autonomous finite state, but not a
  DFAO that reads the binary digits of the index `m`.
- Modular exponentiation in (18) still needs realization in the physical
  counter/residual grammar.
- The formula assumes the lower prefix is stored, or reconstructs it with
  `e_m-1` earlier quotient-bit steps.
- It advances the padding address; it does not prove compatibility with the
  simultaneous residual cylinder or produce a marked ordinary orbit.

## Adversarial tests

- Using `u_m=-V_m` as an exact equality is false. Only the congruence modulo
  `2^e_m` is used, exactly the precision range of (9).
- The normalized displacement in (22) need not equal `1` in `Z_2`; only its
  parity is universally `1`. Multi-bit lifts require the higher unit data.
- An arbitrary representative of `a mod 2^h` can change the displayed lift
  bit. The canonical convention (3) prevents this ambiguity.
- Computing (18) modulo the divisor rather than twice the divisor erases the
  quotient parity.
- The old bit `epsilon_m` and the new stable bit are opposites; omitting the
  toggle gives `s_m mod 2^e_m`, not `s_(m+1) mod 2^e_m`.

## Remaining uncertainty

None in the one-bit identity, its finite data dependence, or the exclusion of
autonomous finite-state generation. Whether the quotient-bit word is
2-automatic, or becomes automatic on a useful proper subsequence, is exactly
the unresolved formal-series problem described after (31).

For the physical residual interface, `L-9852` gives a separate exact answer:
the bulk-routed address works through `H` bits precisely when the outgoing
tail is congruent to `V_m` modulo `2^H`, and its next physical address bit is
the bit above XOR one residual-defect quotient bit. Propagating that
compatibility cylinder, and the remaining connector block above it, is open.

## Suggested next attack

Adjoin `L-9852`'s residual-defect bit to the scale-level Montgomery zipper and
derive its update under the quadratic bulk recurrence. A closed update would
realize this quotient bit as one physical residual/counter cell; failure of
closure would quantify the extra memory. The separate formal-series
automaticity question in (31) remains available as a secondary attack.
