# A direct all-word carry invariant attempt

Date: 23 November 2026. **Status: the positive integer-cycle exclusion is
OPEN.** This pass tried to prove it by one local invariant of the complete
binary carry. The certificate sought would apply at every word length and
to the full numerical denominator. An exact dual identity rules out the
specific invariant class below, even after retaining nonnegative integer
quotients and their values below five. No theorem excluding all cycles is
claimed, and no new Lean theorem is counted.

The new result is an obstruction to a precisely stated universal proof
mechanism. It is not evidence for an integer counterexample. The rational
family used to demonstrate the obstruction has its full numerical gcd
computed explicitly; every member is nonintegral.

## 1. The complete arithmetic retained by the attempt

For a shortcut word `w` of length `A` and weight `p`, with ones at `d_j`, use

\[
 D=2^A-3^p>0,\qquad C=\sum_{j<p}2^{d_j}3^{p-1-j}.
\]

The exact cyclic system is

\[
 (L_w x)_i=2x_{i+1}-3^{w_i}x_i=w_i.
 \tag{PC1}
\]

Its determinant, up to sign, is the whole `D`. A nontrivial positive
integer cycle is equivalent to a primitive nontrivial word with `D|C`.
This is the existing full-word interface, not a new reduction.

The earlier owned carry construction starts `c^(0)=w` and applies

\[
 b_i=c_i\bmod2,\qquad
 c_i'=\frac{c_i+3^{w_i}b_i-2b_{i+1}}2.
 \tag{PC2}
\]

Its invariant alphabet is `c_i in {-1,0}` when `w_i=0`, and
`c_i in {-1,0,1,2}` when `w_i=1`. If `x` is an integral solution of
`L_w x=c`, then `b_i=x_i mod2` and

\[
 x_i'=\lfloor x_i/2\rfloor,\qquad L_w x'=c'.
 \tag{PC3}
\]

For a positive integer cycle every `x^(t)` is therefore nonnegative and
eventually zero. This sign information is retained below; the attempt
does not replace the actual integer quotients by arbitrary signed carry
configurations.

Every state of a nontrivial positive integer cycle is at least five.
Indeed none can be divisible by three, since both inverse branches of a
multiple of three, when integral, remain divisible by three; a cyclic
orbit containing such a state would have no odd edge. The only smaller
positive possibilities prime to three are `1,2,4`, and each belongs to or
immediately enters the known `1,2` shortcut cycle. Also

\[
 2^A=\prod_{\text{odd phases }i}(3+1/x_i)<4^p,
 \qquad\text{hence } A<2p.
 \tag{PC4}
\]

## 2. A finite certificate that would have proved the unrestricted claim

Record the truncated actual quotient

\[
 h_i=\min(x_i,5),\qquad s_i=(w_i,c_i,h_i).
\]

The label `5` means `x_i>=5`; it is not the value five. Carry parity
restricts this alphabet to 21 states. An allowed local transition consists
of three input states `s_0,s_1,s_2`, two output states `t_0,t_1`, and four
**nonnegative ordinary integers** `x_0,...,x_3` such that

\[
 2x_{i+1}-3^{w_i}x_i=c_i\quad(0\le i<3),
 \qquad h_i=\min(x_i,5),
 \tag{PC5}
\]

and the outputs are given by (PC2) and
`h_i'=min(floor(x_i/2),5)`. This retains actual integrality, positivity,
the horizontal equation, and the simultaneous halving step on that local
window.

Seek two real functions `V,F` on ordered pairs of alphabet states with

\[
 R(s,t):=V(s_0,s_1)-V(t_0,t_1)
           +F(s_1,s_2)-F(s_0,s_1)\le0
 \tag{PC6}
\]

for every such allowed local transition. The flux `F` telescopes around
any cyclic row. Thus

\[
 E_V(x,c)=\sum_iV(s_i,s_{i+1})
 \quad\Longrightarrow\quad E_V(x',c')\ge E_V(x,c).
 \tag{PC7}
\]

This is an all-length statement. It does not enumerate possible periods,
bound the exponent tuple, or select a denominator factor.

For a hypothetical nontrivial cycle, the initial states and final zero
states have the fixed labels

\[
 a_0=(0,0,5),\quad a_1=(1,1,5),\qquad
 z_0=(0,0,0),\quad z_1=(1,0,0).
\]

Put

\[
 \delta_{bc}=V(a_b,a_c)-V(z_b,z_c).
 \tag{PC8}
\]

If one could choose `V,F` satisfying (PC6) and

\[
 \sum_{i<A}\delta_{w_iw_{i+1}}>0
 \tag{PC9}
\]

for every primitive nontrivial positive word, (PC7) would contradict the
eventual zero row. This would directly exclude unrestricted positive
integer cycles. One may restrict (PC9) to words whose rational cycle has
all states at least five, since the other words are already impossible
integer candidates by (PC4) and the known core.

The search was for a universal certificate of (PC6)--(PC9), not for a
finite list of cycles.

## 3. Exact obstruction, with positivity included

**Proposition.** Every pair `V,F` satisfying (PC6) obeys

\[
 \boxed{2\delta_{11}+3\delta_{01}+3\delta_{10}\le0.}
 \tag{PC10}
\]

**Proof by a finite exact identity.** The accompanying
`positive_carry_dual.json` supplies 34 allowed local transitions, each
with its four explicit nonnegative integer witnesses in (PC5), and a
positive integer coefficient `m_j`. The coefficients sum to 40. Direct
coefficient collection gives the identity

\[
 \sum_{j=1}^{34}m_jR_j
     =2\delta_{11}+3\delta_{01}+3\delta_{10}.
 \tag{PC11}
\]

Every occurrence of `F` cancels. Every other `V` term cancels, leaving
exactly the six terms obtained by expanding the three deltas on the
right. Each summand on the left is nonpositive by (PC6), proving (PC10).
This is a linear identity over the integers, not an inference from a
floating-point solver status. The standalone checker verifies each
horizontal equation, each vertical output, and the complete coefficient
identity using integers and exact fractions. No optimization package is
used by the checker. \(\square\)

The construction first tested the six-state carry alone, then added the
quotient categories and nonnegative integer witnesses to remove that
relaxation. Proposition (PC10) concerns the stronger, positive version.
It does not rule out larger-window invariants, unbounded quotient data,
nonlocal dependence on the word, or an invariant using the complete
original source rather than only these labels.

## 4. The obstruction occurs at unbounded primitive periods above 21

The pair-count obstruction is not confined to a signed cycle or to an
isolated low rational state. Let

\[
 U=11101010,\qquad V=11011010,\qquad W_k=UV^{k-1}\quad(k\ge1).
 \tag{PC12}
\]

Both blocks have length eight and weight five. Their complete numerators
are respectively 283 and 319, and their common denominator is 13. Each
block's affine map is

\[
 f_B(x)=\frac{243x+C_B}{256}.
\]

The interval `I=[283/13,319/13]` is preserved by both maps: each is a
strict contraction with its fixed point at one endpoint of `I`. Every
proper nonempty prefix of either block has multiplier `3^j/2^h>1` and
positive correction. Consequently the fixed point of their complete
composition lies in `I`, every block-boundary point stays in `I`, and
every intermediate cyclic state is at least `283/13>21`.

There is exactly one cyclic occurrence of `111` in `W_k`. The block `V`
has no such occurrence and every block ends in zero. A nontrivial
repetition would repeat every cyclic marker, so `W_k` is primitive.
It has

\[
 A_k=8k,\quad p_k=5k,\quad
 N_{11}=2k,\quad N_{01}=N_{10}=3k,\quad N_{00}=0.
\]

Thus (PC10) forces its initial-minus-final potential difference to be
nonpositive for every `k`. These are primitive positive words of
arbitrarily large length, all above the five-state cutoff. They prevent
(PC9) from following from this local monotonicity mechanism.

### The full numerical gcd of this family

The exact chronological concatenation formula gives

\[
 D_k=256^k-243^k,\qquad
 C_k=319\frac{D_k}{13}-36\,243^{k-1}.
 \tag{PC13}
\]

No prime factor is removed in the following computation. From
`13 C_k=319 D_k-468*243^(k-1)` and `gcd(D_k,6)=1`, one obtains

\[
 \gcd(D_k,C_k)\mid13.
\]

Moreover the geometric-sum identity gives

\[
 D_k/13\equiv k243^{k-1}\pmod{13},
\]

so

\[
 C_k\equiv243^{k-1}(7k-10)\pmod{13}.
\]

Since 243 is invertible modulo 13, this proves the complete formula

\[
 \boxed{\gcd(D_k,C_k)=
   \begin{cases}13&k\equiv7\pmod{13},\\1&\text{otherwise}.
   \end{cases}}
 \tag{PC14}
\]

In particular every member is nonintegral: at `k=1` the reduced
denominator is 13; for `k>=2`, `D_k/13>1`. These are controls for a
proposed universal invariant, not counterexamples to positive-cycle
exclusion. Formula (PC14) is a full numerical calculation for this
specified family, not a bound for arbitrary words.

## 5. The unresolved step and the evidence boundary

The attempted sufficient condition was a monotone energy under binary
digit stripping, together with a positive source-to-zero gap for all
candidate words. The finite integer identity (PC11) prevents that gap
within the stated nearest-neighbor certificate class. The obstruction
persists after local positivity and actual small quotient values are
included, and occurs on unbounded primitive positive words with every
rational state above 21.

A successful continuation of this particular route must use arithmetic
or global source information absent from that certificate class. No such
additional invariant was obtained here. The numerical all-word target
`D not dividing C` remains open. Nothing in this note excludes possible
unbounded ordinary orbits either.

The replay checks the exact dual identity, rejects three damaged
certificates, and checks the explicit full-gcd family at five stated
parameters. The infinite family statements have written proofs above;
the five replays do not establish them by extrapolation. There is no new
large census, no `sorry`, and no claimed Lean formalization of (PC10).

The accompanying `SOURCES.md` records the refreshed repository inputs
and the inspected primary-literature hypotheses. Existing full-word,
Mahler, unit-equation and mixing formulations are credited there. The
local certificate attempt was pursued after those inspections, rather
than repeating their already identified closing gaps.
