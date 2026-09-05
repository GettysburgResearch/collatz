# T-9832 -- Oriented completion-criticality master theorem

Claim ID: `T-9832`
Title: Equal-factor returns, maximal runs, selected rational approximants, and reciprocal zero carries obey one sharp two-orientation height wedge
Status: `PROPOSED / SHARP DECOMPOSITION OF ACL-N070`
Authoring agent: `gpt56-synthesis-01-wave22-completion-master`
Reviewing agents: `gpt56-synthesis-01-wave22-h-sunit-transfer`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9801`, `T-9823`, `T-9827`, `T-9829`, `R-9810`; PR #16 at `87478352`; PR #35 at `52d320b6`; PR #38 `ACL-N070` at `5ad96577`
Scope: every coprime expanding binary chart `2<=M<N`
Related counterexample candidates: none; the theorem supplies necessary height bounds only
Related atom: PR #38 `ACL-N070`

## Motivation

Completion arguments in PR #16, PR #35, and the local binary-chart packet use
the same critical constant but in apparently conflicting ways. This theorem
places selected rational approximation, copied factors, physical runs, and
reciprocal zero carries under one product-formula calculation while retaining
the orientation of the divisible numerator. It supplies a reusable sharp
interface without identifying real and completion limits.

## 1. Critical constants and completion

Fix coprime integers

\[
 2\le M<N,
 \qquad C=N-M,
\tag{1}
\]

and put

\[
 \delta=\log_M(N/M),
 \qquad
 \kappa={1\over\delta}
 ={\log M\over\log(N/M)}.
\tag{2}
\]

Write

\[
 \widehat{\mathbf Z}_M
 =\varprojlim_j\mathbf Z/M^j\mathbf Z.
\tag{3}
\]

Since both `N` and `C` are units modulo `M`, the binary completion

\[
 \Phi_{M,N}(\epsilon)
 ={C\over N}\sum_{j\ge0}\epsilon_j(M/N)^j,
 \qquad \epsilon_j\in\{0,1\},
\tag{4}
\]

converges in `widehat Z_M` and is injective.

For a nonzero rational number `z` whose denominator is coprime to `M`, define

\[
 \mathbf Z_{(M)}
 =\left\{{A\over B}\in\mathbf Q:\gcd(B,M)=1\right\}.
\tag{5a}
\]

In lowest terms, its unit group consists of the fractions for which both
numerator and denominator are coprime to `M`. Define

\[
 M^J\parallel_M z
\quad\Longleftrightarrow\quad
 z=M^Ju,
 \qquad u\in\mathbf Z_{(M)}^\times.
\tag{5}
\]

Equivalently, after clearing the denominator coprime to `M`, the remaining
integer quotient is coprime to `M`. For composite `M`, this is stronger than
`M^J|z` and `M^(J+1) not| z`.

If two codes first differ at index `J`, then

\[
 \Phi_{M,N}(\epsilon)-\Phi_{M,N}(\eta)
 =M^J{C\over N^{J+1}}
 \left((\epsilon_J-\eta_J)+MT\right)
\tag{6}
\]

for some `T in widehat Z_M`. The parenthesis is congruent to `+1` or `-1`
modulo every prime divisor of `M`, so

\[
 \boxed{
 \Phi_{M,N}(\epsilon)-\Phi_{M,N}(\eta)
 =M^J u,
 \qquad u\in\widehat{\mathbf Z}_M^\times.}
\tag{7}
\]

This proves both exact divisibility and injectivity for arbitrary composite
`M`.

## 2. Selected periodic approximants

Let

\[
 x={a\over b}\in\mathbf Q\cap\widehat{\mathbf Z}_M,
 \qquad b>0,
 \qquad \gcd(a,b)=1,
\tag{8}
\]

and assume `x=Phi_(M,N)(epsilon)` for a binary completion code `epsilon`.
Necessarily `gcd(b,M)=1`, and injectivity makes this code unique.

Fix a word of length `d>=1`,

\[
 w=\epsilon_0\cdots\epsilon_{d-1}
\tag{9}
\]

and let `eta=w^infinity`. Its completion is the rational number

\[
 Y_w=\Phi_{M,N}(\eta)
 ={CW_w\over N^d-M^d},
\tag{10}
\]

where

\[
 W_w=\sum_{i=0}^{d-1}\epsilon_iM^iN^{d-1-i}.
\tag{11}
\]

Write `Y_w=P/Q` in lowest terms with `Q>0`. Then

\[
 0\le P\le Q,
 \qquad
 Q\mid N^d-M^d,
 \qquad
 \gcd(Q,M)=1,
 \qquad
 Q<N^d.
\tag{12}
\]

Suppose `x ne Y_w`, and the two codes have a common prefix of exact length
`J`, so their first disagreement is at position `J`. Then

\[
 \boxed{M^J\parallel_M(aQ-bP),}
\tag{13}
\]

and consequently

\[
 M^J
 \le|aQ-bP|
 \le Q(|a|+b)
 <N^d(|a|+b).
\tag{14}
\]

Therefore

\[
 \boxed{
 J\le\log_M\!\bigl(Q(|a|+b)\bigr)
 <d\log_MN+\log_M(|a|+b).}
\tag{15}
\]

This is the exact rational-approximation statement for the selected
completion point. Its total ambient precision slope is

\[
 \boxed{\log_MN=1+\delta=1+\kappa^{-1},}
\tag{16}
\]

not `kappa`. Only its excess over the period length has slope `delta`.

If `x=X in Z_(>1)`, then the sharper estimate

\[
 \boxed{
 M^J\le QX-P\le QX<N^dX}
\tag{17}
\]

holds, and hence

\[
 J<d\log_MN+\log_MX.
\tag{18}
\]

The middle inequality in (17) is equality for the all-zero periodic word and
is strict when `Y_w>0`.

If `x=Y_w`, the numerator in (13) is zero and injectivity makes the code
purely periodic. For an ordinary positive integer this can happen only at the
trivial endpoint `x=1`, with the all-one code. Allowing zero adds the all-zero
endpoint.

No real value is assigned to the nonperiodic series (4). Only the periodic
word `w^infinity` is evaluated really, through the explicit rational number
(10).

## 3. Equal-factor return theorem

Suppose an ordinary orbit satisfies

\[
 MX_{n+1}=NX_n-C\epsilon_n,
 \qquad
 X_n\in\mathbf Z_{>1},
 \qquad
 \epsilon_n\in\{0,1\}.
\tag{19}
\]

Then

\[
 X_n\equiv\epsilon_n\pmod M,
 \qquad
 X_{n+1}>X_n,
 \qquad
 X_{n+j}\le(N/M)^jX_n.
\tag{20}
\]

Iteration from time `r` gives

\[
 X_r
 ={C\over N}\sum_{j=0}^{J-1}
 \epsilon_{r+j}(M/N)^j
 +(M/N)^JX_{r+J}.
\tag{20a}
\]

The last term tends to zero in `widehat Z_M`, so every ordinary tail satisfies

\[
 X_r=\Phi_{M,N}(\epsilon_r\epsilon_{r+1}\cdots).
\tag{20b}
\]

This is the completion-code hypothesis needed when Section 2 is applied to an
ordinary state.

Assume equal factors of length `L` begin at `r<t`, and put `d=t-r`. For

\[
 D_i=X_{t+i}-X_{r+i},
\tag{21}
\]

subtraction gives

\[
 MD_{i+1}=ND_i
 \qquad(0\le i<L).
\tag{22}
\]

Hence there is an integer `u>=1` such that

\[
 \boxed{
 D_i=M^{L-i}N^iu
 \qquad(0\le i\le L).}
\tag{23}
\]

No coprimality of `u` with `M` is asserted unless the common factor ends at
exactly length `L`.

Thus a repeated factor is an exact zero-carry chain in the ordinary
orbit-difference cocycle. Its height gives

\[
 M^L\le D_0<X_t\le(N/M)^dX_r,
\tag{24}
\]

so

\[
 \boxed{
 L<\delta d+\log_MX_r,
 \qquad
 d>\kappa\bigl(L-\log_MX_r\bigr).}
\tag{25}
\]

There is simultaneously a selected-rational interpretation. The tail
`epsilon_r epsilon_(r+1)...` agrees with

\[
 (\epsilon_r\cdots\epsilon_{t-1})^\infty
\tag{26}
\]

for at least `d+L` digits, including when the equal factors overlap. Applying
(17) with `x=X_r` gives

\[
 M^{d+L}\le QX_r-P\le QX_r<N^dX_r,
\tag{27}
\]

which reproduces (25). Thus equal-factor recurrence and rational
approximation are two exact descriptions of the same `M`-deep numerator.

Since `X_r<=(N/M)^rX_0`, one also has

\[
 \boxed{
 L<\delta t+\log_MX_0,
 \qquad
 t>\kappa\bigl(L-\log_MX_0\bigr).}
\tag{28}
\]

Let `p_epsilon(L)` denote the number of distinct length-`L` factors occurring
in the one-sided word `epsilon`. Consequently,

\[
 \boxed{
 p_\epsilon(L)\ge
 1+\max\left\{
 0,
 \left\lfloor
 \kappa\bigl(L-\log_MX_0\bigr)
 \right\rfloor
 \right\}.}
\tag{29}
\]

The strict sign in (28) makes the floor valid at an integral endpoint.

### Proof

Because `C congruent N (mod M)` and `N` is a unit modulo `M`, integrality of
(19) gives the first relation in (20). Direct subtraction gives

\[
 X_{n+1}-X_n={C(X_n-\epsilon_n)\over M}>0,
\tag{30}
\]

and dropping the nonnegative correction gives the last relation in (20).

Equation (22), integrality, and `gcd(M,N)=1` force `M^L|D_0`; (23) follows.
The remaining assertions were derived above. For (29), among the first
`p_epsilon(L)+1` length-`L` factors two repeat; their later start is at most
`p_epsilon(L)`, and (28) applies. **QED**

## 4. Exact same-symbol returns and maximal runs

Both symbols occur infinitely often in every orbit (19). Indeed, if the tail
were eventually constant `s`, then `Y_n=X_n-s` would satisfy

\[
 MY_{n+1}=NY_n,
\tag{31}
\]

forcing `Y_n=0` by coprimality, contrary to `X_n>1`.

Let `h<h'` be consecutive occurrences of `s in {0,1}`, and put `g=h'-h`.
Then

\[
 \boxed{
 NX_h-M+s(M-C)=M^gu,
 \qquad \gcd(u,M)=1.}
\tag{32}
\]

Moreover,

\[
 0<NX_h-M+s(M-C)<NX_h.
\tag{33}
\]

Therefore

\[
 \boxed{
 g<\delta h+\log_M(NX_0),
 \qquad
 h>\kappa\bigl(g-\log_M(NX_0)\bigr).}
\tag{34}
\]

For `M=2^a`, (32) is exactly

\[
 v_2\!\left(NX_h-M+s(M-C)\right)=ag,
\tag{35}
\]

recovering the valuation law in `T-9823`.

Now let a finite maximal run of symbol `s` begin at position `p` and have
length `ell`. There is a positive integer `q_0`, coprime to `M`, such that

\[
 \boxed{X_p=s+M^\ell q_0,}
\tag{36}
\]

and throughout the run

\[
 X_{p+j}=s+M^{\ell-j}N^jq_0.
\tag{37}
\]

If `p>0`, the occurrences of `1-s` at `p-1` and `p+ell` are consecutive.
Substituting `h=p-1`, `g=ell+1` in (34) gives the sharp later-run bound

\[
 \boxed{
 \ell<\delta p+\log_MX_0,
 \qquad
 p>\kappa\bigl(\ell-\log_MX_0\bigr).}
\tag{38}
\]

At the initial endpoint `p=0`, the exact statement is instead

\[
 \boxed{M^{\ell_0}\parallel_M(X_0-s_0).}
\tag{39}
\]

The strict inequality in (38) must not be extended to `p=0`. For example, in
the `2->3` chart, `X_0=2^L` has an initial zero run of exactly length
`L=log_2 X_0`.

Adjacent maximal runs obey the general zipper

\[
 \boxed{
 M^{\ell_{k+1}}q_{k+1}
 =N^{\ell_k}q_k+\sigma_k,
 \qquad \sigma_k=2s_k-1.}
\tag{40}
\]

This carries indispensable quotient memory. There is no bound on
`ell_(k+1)` in terms of `ell_k,M,N` alone.

### Proof

For consecutive occurrences `h<h'` of `s`, every intervening symbol is
`1-s`. The first recurrence step gives

\[
 NX_h-M+s(M-C)
 =M\{X_{h+1}-(1-s)\}.
\tag{40a}
\]

During the intervening block, the translated state obeys

\[
 M\{X_{i+1}-(1-s)\}
 =N\{X_i-(1-s)\}.
\tag{40b}
\]

At `h'`, its residue modulo `M` is `2s-1`, a unit. Coprimality therefore
gives (32), and the two strict inequalities in (33) follow by subtracting
`M` when `s=0` and `C` when `s=1`. Iteration and the ordinary growth bound
give (34).

For a maximal run, the first `ell` completion digits say that `M^ell` divides
`X_p-s`; the next opposite digit makes the quotient a unit, proving (36).
Translating by `s` turns every step inside the run into multiplication by
`N/M`, which proves (37). The flanking occurrences of `1-s` prove (38) from
(34). Finally, at the boundary between two adjacent runs,

\[
 s_k+N^{\ell_k}q_k
 =1-s_k+M^{\ell_{k+1}}q_{k+1},
\tag{40c}
\]

which is exactly (40). **QED**

## 5. Reciprocal completion zero carries

The phase zero-carry theorem has the opposite orientation.

Let `b>=0`, `r>=1`, `t>=0`, `0<theta<1`, `H>=0`, and let `z ne 0` be an
integer satisfying

\[
 N^{b+r}\mid z,
 \qquad
 |z|\le\theta N^bM^{r+t}+H.
\tag{41}
\]

Then

\[
 \boxed{
 r<\kappa t
 \quad\text{or}\quad
 H>(1-\theta)N^{b+r}.}
\tag{42}
\]

In particular, equality

\[
 H=(1-\theta)N^{b+r}
\tag{43}
\]

still forces `r<kappa t`.

Indeed, divisibility gives `N^(b+r)<=|z|`. If the second alternative in (42)
fails, then

\[
 N^{b+r}
 \le\theta N^bM^{r+t}+(1-\theta)N^{b+r},
\tag{44}
\]

so `N^r<=M^(r+t)`. Equality is impossible because `r>=1` and `M,N` are
coprime. Hence

\[
 r\log(N/M)<t\log M,
\tag{45}
\]

which is `r<kappa t`.

For the reciprocal phase chain at PR #16, let

\[
 s_j\equiv-chM^{j-K}\pmod{N^{j+1}},
 \qquad
 |s_j|\le{1\over2}N^{j+1},
\tag{46}
\]

with `gcd(c,M)=1` and `M not| h`. If `r` consecutive carries vanish from
level `j`, and

\[
 t=K-j-r\ge1,
\tag{47}
\]

then

\[
 Z=M^{K-j}s_j+ch
\tag{48}
\]

is nonzero and divisible by `N^(j+r+1)`. Applying (42) with

\[
 b=j+1,
 \qquad \theta={1\over2},
 \qquad H=|ch|
\tag{49}
\]

gives the sharpened source conclusion

\[
 \boxed{
 r<\kappa t
 \quad\text{or}\quad
 2|ch|>N^{j+r+1}.}
\tag{50}
\]

Equivalently,

\[
 \boxed{
 r<\max\left\{
 \kappa t,
 \log_N(2|ch|)-j-1
 \right\}.}
\tag{51}
\]

This retains the full starting-depth factor discarded by the earlier looser
bound `N^r<=2|ch|`.

## 6. Sharpness of both orientations

The two slopes are sharp for the underlying height-divisibility theorem.

Because `M,N>1` are coprime, `log_M N` is irrational. Put

\[
 J_d=\lfloor d\log_MN\rfloor,
 \qquad z_d=M^{J_d}.
\tag{52}
\]

Then

\[
 M^{J_d}\mid z_d,
 \qquad
 |z_d|<N^d,
\tag{53}
\]

and

\[
 {J_d-d\over d}\longrightarrow\delta.
\tag{54}
\]

Thus the excess agreement slope `delta=kappa^(-1)`, and hence the inverted
return slope `kappa`, cannot be improved using only divisibility and height.

For the opposite orientation, fix `0<theta<1` and put

\[
 r_t=
 \left\lfloor
 \kappa t+{\log\theta\over\log(N/M)}
 \right\rfloor.
\tag{55}
\]

For all large `t`,

\[
 N^{r_t}\le\theta M^{r_t+t}.
\tag{56}
\]

Taking `z=N^(r_t)`, `b=0`, and `H=0` in (41) gives

\[
 {r_t\over t}\longrightarrow\kappa.
\tag{57}
\]

Thus the coefficient `kappa` in (42) is also best possible. This is sharpness
of the universal wedge, not a claim that an infinite ordinary survivor
attains either boundary.

## 7. Adversarial tests and boundaries of a single-cocycle interpretation

`ACL-N070` asks for one theorem controlling the three orientations, and
Sections 2--6 provide it. What fails is the stronger interpretation that all
clauses use one identical numerator, one raw approximation slope, or a bound
on an adjacent run from its predecessor alone.

### 7.1 Maximal runs require quotient or root height

In the `2->3` chart, for every odd `R>=1`, let

\[
 X_0={2(2^R+1)\over3}.
\tag{58}
\]

Then the ordinary orbit begins with one zero followed by `R` ones:

\[
 X_1=2^R+1,
\tag{59}
\]

\[
 X_{1+j}=1+2^{R-j}3^j
 \qquad(0\le j\le R).
\tag{60}
\]

The states in (60) are odd for `j<R`, while `X_(R+1)=1+3^R` is even. Thus

\[
 (\ell_0,\ell_1)=(1,R)
\tag{61}
\]

with `R` arbitrary. Since every residue modulo two is binary, the positive
orbit continues indefinitely.

Hence no inequality of the form

\[
 \ell_{k+1}\le f(M,N,\ell_k)
\tag{62}
\]

can hold without the carry `q_k`, root height, or another global coherence
variable. This does not contradict the absolute position and height bounds,
because `X_0` itself grows exponentially with `R`.

### 7.2 Reduced denominator alone is insufficient

A constant-zero period has selected rational value `Y=0` and reduced
denominator `Q=1` at every formal period length. Arbitrarily deep initial zero
cylinders are obtained by increasing the ordinary root height. Therefore
approximation quality cannot be bounded solely by the reduced denominator
`Q`; the point height and ambient period scale `N^d` in (15) are essential.

### 7.3 Real and completion limits cannot be identified

For the ordinary `2->3` orbit with `X_0=2`, iteration gives

\[
 \sum_{n\ge0}\epsilon_n(2/3)^n=6
 \qquad\text{in }\mathbf Q_2.
\tag{63}
\]

The real series formed from the identical rational partial sums lies in

\[
 0\le\sum_{n\ge0}\epsilon_n(2/3)^n\le3.
\tag{64}
\]

Thus the two limits differ. Real bounds may be transferred only after a
finite or eventual periodicity argument produces one explicit rational value,
as in `T-9829`. This is precisely the boundary recorded in `R-9810`.

## 8. Verdict on ACL-N070

The atom is resolved by the following qualification:

> There is one two-orientation product-formula theorem. The ordinary
> equal-factor, same-symbol, maximal-run, and selected-periodic-approximant
> clauses share the `M`-deep inequality; the reciprocal phase zero-carry
> clause uses the `N`-deep inequality. Their reciprocal slopes are forced by
> orientation. No theorem identifies their cross-numerators or their real and
> completion values.

The reusable equality-language interface is (28)--(29). The selected rational
approximation interface is (13)--(18). The sharp reciprocal zero-carry
interface is (42)--(51).

## Dependency audit and source mapping

- Local `T-9801` supplies the general equal-factor complexity consequence;
  Section 2 adds the shifted pure-period exact `M`-order.
- Local `T-9823` supplies the `M=2^a` same-symbol valuation and physical
  switch bounds; (32) generalizes it to arbitrary coprime `M,N`.
- Local `T-9827` supplies the power-of-two maximal-run zipper; (36)--(40)
  give its natural full-`M` form.
- Local `T-9829` is the valid periodic-tail cross-place case.
- Local `R-9810` supplies the exact prohibition on nonperiodic real/completion
  transfer.
- PR #16 head `87478352`:
  - `L-9310`, blob `acf0226`, is sharpened by (50);
  - `L-9311`, blob `0aefa71`, is the `64->81` difference-chain instance;
  - `T-9318`, blob `845ab7d`, is the `64->81` complexity instance.
- PR #35 head `52d320b6`:
  - `T-8803`, blob `7a9b4d5`, already contains the periodic-approximant idea;
    the new part here is the shifted pure-period exact `M`-order and the
    extension from `M=2^a`, `N` odd to arbitrary coprime `M,N`;
  - `T-8810`, blob `7435695`, constructs a separate real nearest-integer
    parameter and does not authorize identifying it with the real value of
    the completion series.
- PR #38 head `5ad96577`, `ACL-N070`, is resolved by the qualified
  two-orientation theorem above.

## Gap audit

- Agreement through at least `J` digits gives `M^J` divisibility; exact
  `parallel_M` requires the first disagreement to occur at `J`.
- The equal-factor quotient `u` in (23) need not be coprime to `M` unless the
  repeated factors separate at their next symbol.
- The ordinary and reciprocal numerators are different cocycles.
- Total periodic approximation order has slope `1+kappa^(-1)`; only excess
  order has slope `kappa^(-1)`.
- The adjacent-run family refutes only a predecessor-only run bound, not the
  absolute position/height theorem.
- No nonperiodic real/completion identification is used.
- No Collatz counterexample and no proof of Collatz are claimed.

## Remaining uncertainty

The universal inequalities and sharpness examples are exact. They do not
classify the equality languages at the critical slope, prove that a physical
maximal-run schedule reaches either boundary, or control the distinct
reciprocal numerator by the ordinary one. Those are architecture-specific
questions outside the theorem.

## Suggested next attack

Apply (50) to the deepest physical PR #16 zero-carry blocks while retaining
the starting depth `j`; compare the resulting height alternative with the
ordinary copied-factor lower bound (29), but only after constructing an exact
algebraic bridge between the two separate numerators. In the ordinary lane,
use the selected-periodic numerator to classify finite automata or morphic
languages whose recurrence slope is strictly below `kappa`.
