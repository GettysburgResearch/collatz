# The triadic denominator is a stopping statistic

**23 November 2026. Status: exact classification and a complete finite
verifier for a supplied candidate; universal construction remains open.**

The useful consequence of the complementary-parity literature here is a
strong rigidity statement. If a positive ordinary integer and a signed
integer have complementary Collatz parities forever, they must already
be the pair `(1,2)` or `(2,1)`. From this, the reduced power of 3 in a
triadic dual is exactly a statistic of the original orbit: it counts the
original-even inputs before the first visit to 2.

In particular, a proposed dual `a/3^r`, even when not reduced, can be
decided by following the original orbit for fewer than `3(r+1)` steps and
then comparing an exact backward pullback. This is a complete decision
procedure for a supplied candidate. It does not choose a successful `r`
for an arbitrary source. Mere agreement of `3(r+1)` parity bits is not
the decision procedure.

## 1. Literature and the current repository boundary

Use the shortcut map

\[
T(x)=\begin{cases}x/2,&x\text{ even},\\(3x+1)/2,&x\text{ odd}.
\end{cases}                                                    \tag{1}
\]

For odd-denominator rationals, parity means the residue modulo 2.
Monks and Yazinski define the involution `Omega` by complementing the
entire parity vector, and prove that it commutes with `T`. Their example
`Omega(3)=-4/9` makes the need for signed duals explicit. Their Theorem 2.1
relates universal rationality to the divergent-orbit question; their
Theorem 2.5 concerns self-conjugate cycles. Neither theorem is used as a
universal triadic construction here. Primary source:
[The autoconjugacy of the 3x+1 function](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf),
Discrete Mathematics 275 (2004), 219–236,
[DOI](https://doi.org/10.1016/S0012-365X(03)00125-0).

The unique finite-prefix residue and the inverse parity coding are in
Bernstein–Lagarias,
[The 3x+1 conjugacy map](https://websites.umich.edu/lagarias/doc/bernstein.pdf),
Canadian Journal of Mathematics 48 (1996), 1154–1169, especially Section 1
and Appendix A. The algebra below uses exact finite branch equations; no
unproved rationality or real/2-adic identification is imported.

The newest PR178 was read at commit
`e6ed7f1429ced4b58b85ca9006edd9a3a12ca193`, including these files:

| File | Exact blob | Relevant established scope |
|---|---|---|
| `research/global-closure-20261123/duality/TRIADIC_RANK.md` | `ab60fd248086bd8a2b753ea12a7b41387ea5c2de` | Triadic closure, integer rank, and the conservative finite horizon |
| `research/global-closure-20261123/duality/lean/TriadicDualClosure.lean` | `8eed815f2dc89b16da80d759c965244513082ac4` | Formal all-time supplied-candidate closing implication |
| `research/profound-step-20261123/arithmetic/TRIADIC_CONSTRUCTION_ATTEMPT.md` | `f7c43e643036304ff12b01679cc7b0a9d84a0f57` | Corrected terminal candidates and reduced denominator persistence backward |
| `research/profound-step-20261123/arithmetic/FAILURE_POSITION_RESETS.md` | `d0bde1a3c4c9d61f65e3ae1aefbf165c602deae8` | Actual resets and the quadratic cost of the conservative horizon |
| `research/profound-step-20261123/arithmetic/lean/TriadicBoundary.lean` | `cae9ae5a1aafb0ec610c27b04283504dfb12bac4` | Finite corrected-carry and denominator algebra |

The denominator transition itself is already in those sources. The
additional deduction here is the complete integral-pair classification,
its exact implication for the first stopping time, and the resulting
linear-clock candidate decision. No historical priority claim is made
for the elementary consequences.

## 2. Complete integral-pair rigidity

Let `x_i` be positive ordinary integers and `w_i` signed integers. An exact
complementary step is one of

\[
\begin{array}{c|cc}
&2x_{i+1}&2w_{i+1}\\\hline
x_i\text{ odd}&3x_i+1&w_i\\
x_i\text{ even}&x_i&3w_i+1.
\end{array}                                                    \tag{2}
\]

The integral equations impose the opposite input parities. The first
coordinate remains positive. A nonzero second coordinate cannot become
zero: halving an even nonzero integer is nonzero, and `3w+1=0` has no
integer solution.

### 2.1 Exact backward uniqueness of the two terminal pairs

An integral paired predecessor of `(1,2)` can only be `(2,1)`.
The original-odd alternative would require `3x+1=2`; the original-even
alternative gives `x=2` and `3w+1=4`, hence `w=1`.

An integral paired predecessor of `(2,1)` can only be `(1,2)`.
The original-odd alternative gives `3x+1=4` and `w=2`; the original-even
alternative would require `3w+1=2`, which has no integer solution.

Consequently a pair outside

\[
                    \mathcal C=\{(1,2),(2,1)\}              \tag{3}
\]

cannot enter that set along a finite integral paired path. This is a
statement about **both** coordinates. An ordinary Collatz predecessor of
1 or 2 alone is not being claimed unique.

### 2.2 A rank that also works at original coordinate 1

For `w != 0`, put

\[
P(x,w)=x|w|,\qquad
E(x,w)=3P(x,w)+\mathbf1_{x=1}+\mathbf1_{w=1}.                 \tag{4}
\]

Every exact step outside `C` strictly decreases the nonnegative integer
`E`.

For an original-odd step,

\[
                  4P(x',w')=(3x+1)|w|.                     \tag{5}
\]

If `x>1`, the integer product decreases by at least one; multiplication
by 3 pays for either indicator change. If `x=1`, then `x'=2` and the
product is unchanged. Outside `(1,2)` one has `w' != 1`, so the `x=1`
marker disappears without a replacement marker. The old `w=1` marker
is absent because `w` must be even.

For an original-even step,

\[
                  4P(x',w')=x|3w+1|.                       \tag{6}
\]

If `w != 0,1`, then `|3w+1|<4|w|`, including negative `w`, and the
integer product again decreases. If `w=1`, then `w'=2` and the product
is unchanged. Outside `(2,1)` one has `x' != 1`; the `w=1` marker
disappears without a replacement marker. This proves the claim in all
signed cases.

There can therefore be no infinite compatible path outside `C` with
nonzero integer second coordinate. More concretely, any finite path of
more than `E(x_0,w_0)` steps would force a negative rank, unless it
already started in `C`, by Section 2.1.

### 2.3 The zero case and the all-time classification

If `w_0=0`, a compatible step is necessarily original-odd and keeps the
second coordinate zero. An all-time path would satisfy

\[
                  2(x_{i+1}+1)=3(x_i+1)                    \tag{7}
\]

at every clock. Since powers of 2 and 3 are coprime, this forces
`2^k | x_0+1` for every `k`. That is impossible for the fixed positive
ordinary integer `x_0+1`.

Combining this fact, the rank, and backward uniqueness proves

\[
\boxed{\quad
 x_0>0,\ w_0\in\mathbb Z,\ \text{all-time complementary parity}
 \quad\Longrightarrow\quad (x_0,w_0)\in\mathcal C.
 \quad}                                                       \tag{8}
\]

In particular, a negative integer dual is impossible; zero is impossible;
and the only positive ordinary sources with integral duals are 1 and 2.
The proof does not assume that either orbit was eventually periodic.

## 3. The reduced denominator measures the first visit to 2

Suppose one fixed positive ordinary source `n` has an all-time triadic
dual, written in lowest terms as

\[
               \Omega(n)=a/3^r,\qquad
               r>0\Longrightarrow 3\nmid a.                 \tag{9}
\]

Write the current reduced dual as `w/3^j`. While `j>0`, the exact
transitions are

\[
\begin{array}{c|cc}
\text{original branch}&\text{new numerator}&\text{new exponent}\\\hline
\text{odd}&w/2&j\\
\text{even}&(w+3^{j-1})/2&j-1.
\end{array}                                                   \tag{10}
\]

The first numerator stays a unit at 3. For `j>1`, so does the second,
because adding `3^{j-1}` does not change the nonzero residue at 3 and
2 is invertible there. At `j=1` the denominator is exhausted. Thus each
original-even input removes **exactly one** factor of 3 until none
remains; original-odd inputs remove none.

Every positive ordinary orbit has infinitely many original-even inputs:
otherwise it would have an all-odd tail, contradicted by (7) at that
fixed tail source. Consequently the clock `J` immediately after the
`r`-th original-even input exists; take `J=0` when `r=0`. It is the
first clock at which the dual is integral. Applying (8) to the tail
shows `(x_J,y_J)` is `(1,2)` or `(2,1)`.

For `n>1`, this first integral pair must be `(2,1)`. If `J>0` and it
were `(1,2)`, its last original input was even, hence `x_(J-1)=2`.
The rational paired inverse gives

\[
                   y_{J-1}=(2\cdot2-1)/3=1,                \tag{11}
\]

contradicting first integrality. If `J=0`, equation (8) already says
`n=2` when `n>1`.

There was no earlier visit to 1 or 2. Their complementary tails are
uniquely 2 or 1, respectively, which would give an earlier integral
dual. This uniqueness can also be checked directly: along the original
`1,2` tail the complementary value obeys

\[
             4^h(y_{2h}-2)=3^h(y_0-2).                     \tag{12}
\]

If `y_0` has odd denominator and every subsequent value has odd
denominator, divisibility by every `4^h` forces `y_0=2`. The phase at
2 follows by one step. This argument permits negative rational values;
no positivity of the dual is used.

Let `tau(n)` be the first clock with `T^tau(n)(n)=1`. We have proved,
for `n>1`,

\[
\boxed{
 J=\tau(n)-1,\quad x_J=2,\quad y_J=1,\quad
 r=\#\{i<\tau(n)-1:x_i\text{ is even}\}.
}                                                            \tag{13}
\]

There are exactly `r+1` original-even inputs through the first hit of
1, including the final `2 -> 1`. The cases `n=1` and `n=2` give the
reduced duals 2 and 1, both with exponent zero; their first-hit clocks
are 0 and 1. Equation (13) is stated only for `n>1`.

This has an immediate conceptual consequence for approximation attacks:
the exponent of an exact reduced triadic dual is not freely adjustable
approximation slack. It encodes the original source's stopping orbit.
An unreduced presentation only adds redundant factors of 3 to numerator
and denominator.

## 4. A linear-clock, exact candidate verifier

For `n>1`, write `b=r+1` and let `s=tau(n)-b` be the original-odd count
through the first hit of 1. The complete ordinary affine identity has
a nonnegative carry `C`, so

\[
                     3^s n+C=2^{s+b},\qquad
                     3^s\le2^{s+b}.                        \tag{14}
\]

It follows that `s<2b`. Indeed, if `s=2b+d` with `d>=0`, then

\[
               3^s=9^b3^d>8^b2^d=2^{s+b},                 \tag{15}
\]

because `b>0`. Therefore

\[
\boxed{\qquad \tau(n)<3(r+1).\qquad}                       \tag{16}
\]

The inequality holds for `n=1` as well. It also holds for an unreduced
presentation `a/3^r`, since its reduced exponent is at most `r`.

There is a second necessary bound. Equation (14) gives, for `n>1`,

\[
                    n\le2^{r+1}(2/3)^s\le2^{r+1}.          \tag{16a}
\]

It is also true for `n=1` and for unreduced presentations. Thus, if
`n` has bit length `N>=2`, every all-time candidate has `r>=N-2`.
If `n` is not the power `2^(N-1)`, then `n>2^(N-1)` and the stronger
integer bound `r>=N-1` follows. These statements are necessary bounds
on supplied all-time candidates, not assertions that such a candidate
exists for each source.

This gives the following complete finite interface, implemented in
[verify_triadic.py](verify_triadic.py):

1. Given `n>0`, `a` an integer, and `r>=0`, examine the original states
   at clocks `0,...,3(r+1)-1` until the first 1.
2. If none is 1, reject: no all-time triadic dual of reduced exponent
   at most `r` exists for that source.
3. If the first 1 occurs, put the dual value 2 opposite it and pull
   the **same actual prefix** backward, using `y_i=2y_(i+1)` at an
   original-odd input and `y_i=(2y_(i+1)-1)/3` at an original-even
   input.
4. Accept precisely when the resulting exact rational is `a/3^r`.

Necessity is (16) and parity-vector uniqueness. Sufficiency is finite:
the inverse maps impose the appropriate parities, and the complementary
`2,1` cycle extends the paired path forever. Equality is exact, so
negative numerators, zero numerators, and unreduced input fractions need
no heuristic conventions. At `n=1` the comparison is with 2 immediately;
at `n=2` it is with 1 after one original step.

The forward iteration bound depends on `r`, not on the bit length of
`a`. Arithmetic for the exact comparison still has to read that
numerator. A successful denominator selector for every positive source
is **not** obtained: increasing `r` without a supplied successful bound
recovers an unbounded search along the original Collatz orbit.

### Short parity agreement is not this verifier

For example, at `n=1,r=0`, the candidate `a=10` shares the first three
complementary parity bits with the true dual 2:

\[
           1,2,1\quad\text{opposite}\quad10,5,8.
\]

At the next clock the original value is 2 and the candidate value is 4,
so compatibility fails. The verifier rejects 10 by exact backward
equality at clock zero. Thus (16) is a necessary stopping-time bound
for **all-time** candidates, not a claim that `3(r+1)` parity bits alone
certify one.

## 5. Strengthening the existing finite congruence

The pinned PR178 horizon is

\[
\begin{split}
N&=\operatorname{bl}(n),\quad B=\max(1,|a|,3^r),\quad
L=\operatorname{bl}(B),\\
R&=rL,\quad E_0=N+L+R,\quad
H=R+8E_0+2=8N+(9r+8)L+2,
\end{split}                                                   \tag{17}
\]

where `bl(m)` is the least positive `L` with `m<2^L`. For the actual
original prefix, let `b_K` count original-even inputs, and let the
complete complementary carry satisfy

\[
D_0=0,\qquad
D_{i+1}=3^{1-e_i}D_i+(1-e_i)2^i,
\qquad e_i=x_i\bmod2.                                      \tag{18}
\]

The existing sufficient congruence is

\[
              2^H\mid3^{b_H}a+3^rD_H.                       \tag{19}
\]

It imposes every parity in the actual prefix, by exact backward branch
inversion. The new rigidity proves more than its earlier convergence
conclusion:

> **Exact-candidate strengthening.** If (19) holds, then `a/3^r` is the
> actual all-time dual of `n`. More generally this holds for a matching
> prefix of length `K>=H`.

Here is the complete quantitative argument. Until the displayed
denominator is exhausted, the numerator satisfies `|w_i|<=B`. At a
positive denominator level, `L` consecutive original-odd steps would
divide a nonzero integer by `2^L>B`. Hence, by a clock `j<=rL`, either
the displayed denominator is zero or the numerator is zero. There is
no need to stop this count when the original coordinate equals 1.

If the numerator becomes zero, the remaining original prefix must be
all odd. Positivity and `x_j<=n2^j` imply
`x_j+1<=2^(N+R)`, while compatibility implies
`2^(H-j) | x_j+1` and `H-j>N+R`. This is impossible.

Otherwise the pair at `j` is integral with

\[
                    1\le P_j=x_j|w_j|<2^{E_0}.             \tag{20}
\]

Every integral paired step has `P_(i+1)<=P_i`. Outside `C`, every two
steps contract by at least `5/6`:

\[
                       P_{i+2}\le(5/6)P_i.                 \tag{21}
\]

To verify the constant, an original-odd integer `x>1` has `x>=3`, so
the ratio in (5) is at most `5/6`. An original-even step with positive
`w!=1` has odd `w>=3`, giving the same bound; negative `w` gives a
ratio below `3/4`. At `x=1` outside `(1,2)`, the next pair has `x'=2`
and `w'!=1`, so the following step contracts. At `w=1` outside `(2,1)`,
the next pair has `w'=2` and `x'!=1`, so it contracts there. The pair
cannot enter `C` from outside by Section 2.1.

If the integral pair at `j` were outside `C`, its next `8E_0` compatible
steps would give

\[
 P_{j+8E_0}\le(5/6)^{4E_0}P_j
       <(5/6)^{4E_0}2^{E_0}<1,                             \tag{22}
\]

because `6^4>2*5^4`. This contradicts its positive integer product.
All these clocks fit within `H`. Therefore the integral pair is already
in `C`, and pulling back the literal rational branches identifies the
original candidate exactly. This proves the strengthening.

### A prefix-adaptive replacement for the loose denominator-phase bound

One can remove `rL` from the verifier by measuring the actual denominator
clock and actual joint height, without claiming a new uniform bound.
Let `J` be the clock immediately after the `r`-th original-even input,
or zero for `r=0`. It exists unconditionally by (7). Require

\[
 2^J\mid a+D_J,
 \quad t=(a+D_J)/2^J,
 \quad E_J=\operatorname{bl}\bigl(x_J\max(1,|t|)\bigr).       \tag{23}
\]

At this clock the same candidate has integral dual value `t`. Agreement
through

\[
                    H_{\rm adaptive}=J+8E_J+2              \tag{24}
\]

forces the exact all-time dual by (21)–(22). If `t=0`, those remaining
`8E_J+2` compatible steps would force
`2^(8E_J+2) | x_J+1` by the finite form of (7), whereas
`x_J+1<=2^(E_J+1)`. Thus the zero case is excluded at this same finite
horizon. This uses the actual original `x_J` and exact terminal numerator,
instead of multiplying independent worst-case bounds. It is a valid
adaptive parity certificate, separate from the faster exact-equality
decision in Section 4.

No estimate `J=O(N+L+r)` is asserted. The attempted stronger inference
would bound the cumulative divisions by 2 before the `r` denominator
cancellations using a joint height estimate. The separate per-level
argument only gives `rL`; replacing it by a linear expression without
another argument would be unsupported. The exact-equality verifier
bypasses this missing parity-cutoff estimate.

## 6. An all-length control: the cost at powers of two

The functional equation from the complementary even branch is

\[
                  \Omega(2x)=\frac{2\Omega(x)-1}{3}.
\]

Starting with `Omega(1)=2` gives, for every `k>=1`,

\[
\boxed{
 \Omega(2^k)=\frac{b_k}{3^{k-1}},\qquad b_k=2^k-3^{k-1}.
}                                                            \tag{25}
\]

This is reduced at 3, and `|b_k|<=3^(k-1)`. For `k=1` the numerator
is 1; for `k>=2` its residue at 3 is that of `2^k`, hence nonzero.
Its reduced exponent `k-1` agrees with (13), since the original first
hit of 1 occurs at clock `k`.

By Section 5, every candidate passing its own conservative horizon
at this source must be the exact value (25). Therefore it has exponent
`r>=k-1` and numerator `a=b_k*3^(r-k+1)`. Its least possible horizon
in (17) is attained by the reduced presentation:

\[
\boxed{
 H_{\min}(2^k)=8k+10+(9k-1)\operatorname{bl}(3^{k-1}).
}                                                            \tag{26}
\]

The formula also has a direct finite separation proof: if the candidate
and (25) agree for `K` parities, then

\[
                  2^K\mid3^{k-1}a-3^rb_k.                  \tag{27}
\]

For `B,L` in (17), the absolute value of the right side is at most
`2B*3^(k-1)<2^(L+2k)`. Any `K>=H` is at least `L+2k`, forcing that
integer to vanish. Thus the obstruction is uniform over all alternative
numerators and denominator exponents at the source, not just a test of
one proposed construction.

In particular,

\[
H_{\min}(2^k)\ge9k^2+7k+10,
\qquad H_{\min}(2^k)=9\log_2(3)k^2+O(k).                    \tag{28}
\]

The actual stopping time is `k`. Formula (24) gives `k+17` for the
reduced candidate, since `J=k-1`, `x_J=2`, and `t=1`. The exact-equality
verifier from Section 4 uses fewer than `3k` clocks and stops as soon
as the first 1 is observed.

Equations (26)–(28) are limitations of the particular conservative
certificate (17), not lower bounds on Collatz stopping time or on all
possible verifiers. They reinforce why reducing its own denominator
cost matters, while providing no counterexample to full convergence.

### The exact minimum over every source of a given bit length

The same argument gives an all-source statement. By Section 5, any
candidate passing its own conservative horizon is the exact dual, so
(16a) applies. At bit length `N>=2`, it has `r>=N-2` and
`L>=bl(3^r)`. Both factors in the denominator contribution to (17)
increase with `r`. Consequently the minimum horizon among **all**
successful certificates at **all** sources of bit length `N` is

\[
\boxed{
 \min H=8N+2+(9N-10)\operatorname{bl}(3^{N-2}).
}                                                            \tag{29}
\]

The reduced exact dual at `n=2^(N-1)` attains the bound by (25)–(26),
so it is a minimum, not just a lower estimate. This does not assume
convergence of the other sources in the bit-length band. In particular,
every successful such certificate obeys

\[
                 H\ge9N^2-11N+12,                          \tag{30}
\]

and the minimum in (29) is `9 log_2(3) N^2+O(N)`. Therefore a deadline
linear in `N` certifies **no** sufficiently large `N`-bit source under
this conservative criterion. This strengthens the earlier round's
counting limitation for that criterion; it says nothing against the
linear-clock exact-equality verifier in Section 4.

## 7. Formal scope and the remaining source construction

[TriadicRigidity.lean](TriadicRigidity.lean) is self-contained apart from
targeted Mathlib imports. Its eight public statements prove positivity
and nonzero preservation, exact cycle-predecessor rigidity, the complete
rank decrease (4), finite pair rigidity, signed all-time integral-pair
rigidity including zero exclusion, and the integer exponent inequalities
`s<2b` and `s+b<3b` from (14).

The reduced triadic fraction interpretation, equation (13), the complete
affine application (14), the exact candidate verifier proof, the
logarithmic product bound, and the powers-of-two horizon formula have
written proofs above. They are not silently added to the Lean theorem
scope. The 2-adic existence and uniqueness framework is credited to the
primary sources, not encoded as a new axiom.

The unresolved source task is now especially concrete: produce, for
each original positive `n`, some denominator exponent that passes the
complete finite decision. Its reduced value would be the actual number
of original-even inputs before first reaching 2. Neither a generic
rational-approximation theorem nor permission to increase denominator
exponents establishes that this search terminates. This round removes
the quadratic verification overhead for supplied candidates and proves
their exact arithmetic meaning; it does not prove the universal
constructor or full Collatz convergence.
