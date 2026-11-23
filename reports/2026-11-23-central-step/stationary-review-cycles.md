# Independent review: complementary denominator capacity

23 November 2026. Reviewer: `stationary_rigidity`.

**Verdict: VERIFIED at the written theorem level, at the exact local bytes
listed below.** The full complementary denominator bound `K<2q` for a
nontrivial positive integer shortcut cycle, its extension `K<=2q` including
the core, and the stated continuous and asymptotic refinements follow from
the supplied hypotheses. No unrestricted cycle exclusion or new Lean
verification follows from this verdict.

## Frozen material and review boundary

The packet is new local work over repository base
`e6ed7f1429ced4b58b85ca9006edd9a3a12ca193`. It was not yet a committed source
head when reviewed; the following SHA-256 digests fix the exact reviewed
material. The review does not extend to later byte changes.

| File | SHA-256 |
| --- | --- |
| `research/central-step-20261123/cycles/COMPLEMENTARY_DENOMINATOR_CAPACITY.md` | `7bcf9b6dcb275795d5f53f171098614bd30f0b65d0462a3c90b3b9399ee4ef0e` |
| `research/central-step-20261123/cycles/README.md` | `d2c2219eb30df65547cc1972afd53422b66aa7168fb8c6ace1328924e614d2bc` |
| `reports/2026-11-23-central-step/cycles-sources.json` | `d3deee40e66f54e6a58aad273814709e0616f1e102d2f136d0a3d307e77c8d5e` |

I independently reconstructed the finite cycle equations, denominator and
primitive-period conditions, convexity argument, monotonicity argument,
exact integer comparisons, continuous envelope, and eventual-cycle
consumer. I directly inspected the primary Monks--Yazinski source at the
framework and signed-control statements used in this packet. The older
repository attempts in the source ledger are explicitly nondependencies
of the elementary theorem and were not rebuilt for this review.

## 1. Rational cycle product and strict midpoint capacity

For the shortcut map, rational parity means parity in the 2-adic integers,
so a reduced rational state has odd denominator. A legal even step
cancels its factor of two in the numerator and preserves that denominator.
If a denominator contains three, a legal odd step strictly decreases its
3-adic valuation. No other prime factor can cancel at an odd step because
`gcd(3y+q,q)=gcd(3,q)` for a reduced state `y/q`. A nonzero positive cycle
cannot consist only of even steps. Its common denominator is therefore
prime to six and remains exactly the same along the cycle.

For least period `L`, the `h` odd states are distinct. Their reduced
numerators are distinct positive odd integers, so after sorting they
satisfy `y_i>=2i-1`. Multiplying the branch ratios telescopes to

\[
 2^L=\prod_{i=1}^h(3+q/y_i).
\]

With `a=q/6`, this gives the sum of `g(i-1/2)`, where
`g(x)=log(1+a/x)`. The displayed second derivative is correct:

\[
 g''(x)=\frac{a(2x+a)}{x^2(x+a)^2}>0.
\]

On each unit interval, strict convexity makes the integral strictly
larger than its midpoint value. This remains valid on the first
interval: `g` is integrable at zero, and integrating the strict symmetric
inequality about `1/2` gives the result without evaluating `g(0)`.
Direct integration yields

\[
 \int_0^h g(x)\,dx
 =h\log(1+a/h)+a\log(1+h/a)
 =h f(a/h),
 \qquad f(t)=(1+t)\log(1+t)-t\log t.
\]

Thus Theorem 1, including its strict inequality, is verified. It applies
to the fully reduced numerical denominator, with no assumption about a
polynomial factor or a favorable distribution of cyclic rotations.

## 2. Ordinary positivity and the legal complementary cycle

The least state of a positive integer cycle must be odd, since an even
least state would have a smaller successor. A periodic positive state
cannot be divisible by three: odd steps leave the divisible-by-three
class and neither branch can return to it. A nontrivial cycle cannot
contain one. Consequently its minimum is at least five.

Writing `K=p+b` for its odd and even counts gives

\[
 2^K\le(16/5)^p.
\]

The comparison used in the packet is exact:
`(16/5)^7<2^12` is equivalent to
`65536=2^16<5^7=78125`. It implies `p/K>7/12` and hence
`0<b/K<5/12`. Both kinds of step occur: an all-even positive cycle would
strictly decrease, and an all-odd positive cycle would strictly increase.

For the complemented word, its odd count is `b`, its complete carry is
positive, and `b<K/2` gives `2^K-3^b>0`. The denominator of the fixed
point after reducing **all** integer gcd factors is exactly

\[
 q=\frac{2^K-3^b}{\gcd(2^K-3^b,C_*)}.
\]

The unreduced denominator is odd and prime to three, hence so is `q`.
The word's affine fixed equation gives its unique rational 2-adic fixed
point, and the finite parity congruences make the word legal. Equivalently,
standard parity coding gives the same point. Its positivity is preserved
under each branch.

The least-period issue is essential and is handled correctly. If the
original parity word were a proper repetition, the corresponding shorter
affine block would have positive slope `3^u/2^d` different from one. A
fixed point of an iterate of that block is its unique fixed point, so the
original ordinary period would be shorter, a contradiction. Complementing
the letters preserves the least word period. Any shorter period of the
complementary state would shorten its parity word as well. Thus the
complementary cycle has least period exactly `K`, and its `b` odd
numerators are indeed distinct.

## 3. Exact proof of `K<2q`

Applying Theorem 1 to the complementary cycle and writing `beta=b/K`
gives

\[
 \log2<\beta\log3+\beta f\bigl(q/(6\beta K)\bigr).
\]

Under the contrary assumption `q<=K/2`, the right side is at most
`G(beta)=beta[log3+f(1/(12 beta))]`. The derivatives and identity used
in the packet are correct:

\[
 f'(t)=\log(1+1/t)>0,\qquad
 f(t)-tf'(t)=\log(1+t),\qquad
 G'(\beta)=\log3+\log(1+1/(12\beta))>0.
\]

At the endpoint,

\[
 \log2-G(5/12)
 =\frac1{12}\log\frac{2^6 5^5}{3^{11}}
 =\frac1{12}\log\frac{200000}{177147}>0.
\]

Since `beta<5/12`, this contradicts the strict lower bound on `G`.
Therefore Theorem 2 is verified with `q>K/2`. The core has `K=2,q=1`,
so the stated all-cycle conclusion is the non-strict `K<=2q`.

## 4. Continuous and large-period refinements

For `0<beta<=1/2`, the right side of the defining equation for `t_beta`
is positive, while `f` increases continuously from zero to infinity.
Implicit differentiation gives

\[
 c'(\beta)
 =-6\frac{\log3+\log(1+t_\beta)}{f'(t_\beta)}<0,
 \qquad c(\beta)=6\beta t_\beta.
\]

The ordinary product implies `beta<=beta_m`, so the direction of the
monotonicity comparison in `q/K>c(beta_m)` is correct. Independently
recomputing the illustrative values at 60 decimal digit arithmetic gave

\[
 c(\beta_5)=0.59302849768392498092832625540295396\ldots,
\]

\[
 c(\beta_0)=0.78640987213390061002038414228052122\ldots.
\]

These values are illustrations; the theorem uses the exact integer
comparison above, not floating point evidence.

For the ordinary cycle with denominator one,

\[
 p f(1/(6p))
 =p\log(1+1/(6p))+\tfrac16\log(6p+1)
 <\tfrac16[1+\log(6p+1)].
\]

This verifies (12) and (13). Along any hypothetical sequence with
`K` tending to infinity, `b/K` tends to `beta_0`, and continuity of `c`
gives the stated lower bound on the liminf of `q/K`. Neither an unbounded
sequence of nontrivial cycles nor an increasing minimum is assumed to
exist.

## 5. Consumer, source attribution, and remaining obligation

A rational orbit with initial odd denominator `Q` does not acquire new
denominator factors under either legal shortcut branch. Thus a separately
proved eventual complementary cycle has denominator `q` dividing `Q`.
If it is paired with a positive ordinary integer cycle, their least
periods agree by the parity argument above and `K<=2q<=2Q` follows. The
packet correctly requires this eventual paired cycle to be established
independently. It does not promote a finite matching prefix to all-time
parity agreement, supply a preperiod bound, or construct a rational dual
for every positive input.

I directly inspected Monks and Yazinski's
[*The autoconjugacy of the 3x+1 function*](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf)
at Theorems 2.3--2.5 and Example 5. The attribution of the self-conjugate
integer-cycle result and the signed control agrees with that primary
source. I also directly checked the branch arithmetic of
`-5 -> -7 -> -10 -> -5` and
`4/5 -> 2/5 -> 1/5 -> 4/5`; their parity words are complementary. This
supports the packet's precise warning against unsigned integrality
forcing complementary integrality.

The new elementary proofs do not import the unresolved complete-word,
Hankel, or residual-denominator estimates listed in the ledger. The README
and ledger agree with the theorem's written status and open scope. No
historical novelty claim is made. All three reviewed files had one final
newline and no trailing whitespace at the listed hashes.

The open line is an upper bound or arithmetic construction strong enough
to force the complementary denominator into the excluded range. The
verified capacity theorem supplies a lower bound; it does not close that
line. This review ran no Lean build, no finite cycle census, and no
repository-wide validator.
