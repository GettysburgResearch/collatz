# Reset boundary after the charged return theorem

**Status: the total payment argument is not proved.** The Lean results in
PsiDescent.lean and Oriented.lean remain the new completed statements of
this lane. This note records the attempted global continuation, including
the sharper floor already proved in the newly refreshed PR176. It does not
present that existing floor as a new result.

## Source pins and scope

- [PR176 exact forward floor](https://github.com/GettysburgResearch/collatz/blob/d2303ea3144ba652d089c1ec38ad3879c3ea5ef7/research/lean-global-resolvent-20261121/EXACT_FORWARD_FLOOR.md),
  and its LeastForwardFailure.lean, at
  d2303ea3144ba652d089c1ec38ad3879c3ea5ef7.
- [PR176 mixed certificate order](https://github.com/GettysburgResearch/collatz/blob/d2303ea3144ba652d089c1ec38ad3879c3ea5ef7/research/lean-global-resolvent-20261121/MIXED_CERTIFICATE_DESCENT.md),
  at the same commit.
- [PR177 adjacent-tail normal forms](https://github.com/GettysburgResearch/collatz/blob/23bbf7383b30bff37434fe823b957759bcdf2c1f/research/lean-exact-witness-global-20261121/lean/Collatz/PsiCompletion.lean),
  and its ResetFamily.lean, at
  23bbf7383b30bff37434fe823b957759bcdf2c1f.
- The existing ordinary basin identities are those of PR174,
  7034109ed60a26bc49824e1ed43c239ceca81194, already pinned by this packet.

The formulas below are exact mathematical derivations and an analysis of
their use. They are not additional Lean declarations in this packet.
The temporary local restatement of the symmetric floor was removed after
the latest refresh showed that the stronger relevant result was already
available in PR176.

## 1. Odd-valuation reset of the paired relation

Write the two starting values as (m,3m−1). Suppose

\[
3m-2=2\,4^r v,\qquad r\ge1,\qquad v\text{ odd}.
\]

Integrality also gives v=2 modulo3, hence v=5 modulo6. Put

\[
a=3^{r-1}v.
\]

After exactly2r ordinary shortcut clocks, the pair is

\[
(2a+1,\;6a+1).
\]

Both arms have exactly r odd inputs. Both displayed values are odd.
The next two clocks therefore give, successively,

\[
(3a+2,\;9a+2)
\]

and

\[
\left(\frac{9a+7}{2},\;\frac{27a+7}{2}\right).
\]

The relation offsets have changed from2 to4 to7. In particular, putting

\[
n=\frac{3^{r+1}v+7}{2}
\]

gives the final pair (n,3n−7), after2r+2 clocks and r+2 odd
inputs on each arm.

For r>=3, the new source n is smaller than m. This alone is not a
return to the original reverse-failure predicate:

\[
\neg C(m)\wedge C(3m-1)
\quad\Longleftrightarrow\quad
\neg C(n)\wedge C(3n-7).
\]

The right side is Fail(3,7,n), not Fail(3,1,n). Minimality among
Fail(3,1) bases does not discharge it.

The missing e=1 case is separate. For m=4t, t>0, two clocks give

\[
(m,3m-1)\longmapsto(t,27t-1).
\]

That reset changes the multiplier to27 rather than producing the
offset7 formula above.

## 2. What the exact forward floor does discharge

PR176 already proves that a least forward odd-child failure has the
following exact context. With N=2m−1,

\[
C(m),\qquad \neg C(N),\qquad
\forall j\;(0<j<N\Longrightarrow C(j)).
\]

The value3m−1 is in the same ordinary component as N, so it is also
outside the basin. Every positive value in that component is therefore
at least N. A changed relation need not first be restored to offset1:
a positive bad endpoint below N is already impossible.

Apply this observation to the odd-valuation reset. Its endpoint at
clock2r is

\[
Y=2\,3^r v+1.
\]

The source equation gives

\[
3N=4\,4^r v+1,\qquad 3Y=6\,3^r v+3.
\]

For every r>=2 and positive v,

\[
(4\,4^r-6\,3^r)v>2,
\]

so Y<N. Thus the floor eliminates this entire large odd-valuation
branch without requiring a return to Fail(3,1). This is a consequence
of the already available floor and the displayed trajectory identity,
not a new floor theorem.

The remaining odd valuation cases are e=1 and e=3:

\[
m=0\pmod4,\qquad\text{or}\qquad m=14\pmod{16}.
\]

The even-valuation family has the paired descent already proved in
PsiDescent.lean. Odd m is excluded by the ordinary descent of
N=2m−1=1 modulo4. These observations still leave an infinite set of
ordinary inputs in the two displayed even-base classes. They do not
supply a complete rule selector.

## 3. The newer adjacent-tail state and the two incompatible decreases

PR177 supplies an odd known source u below the full initial basin
interval, with missing partner H(u)=2u+1. The complete even-exponent
branch of3u+1 is already discharged there. Its remaining odd branch is

\[
3u+1=2\,4^d t,\qquad t\text{ odd},
\]

with the exact component identity

\[
C(H(u))\iff C(H(w)),\qquad w=3^d t.
\]

Equivalently,

\[
w=\frac32\left(\frac34\right)^d u
  +\frac12\left(\frac34\right)^d.
\]

This makes the remaining alternatives precise.

- At d=0, w=(3u+1)/2. This is the actual next odd source in its
  supplied certificate, so a certificate prefix is consumed.
  The source value increases, and may leave the known initial interval.
- At d=1, w=(9u+3)/8>u. The source certificate gives membership
  of t=(3u+1)/8; it does not itself give membership of3t.
  If3t is still below the floor, membership is available from that
  interval, but a new certificate is needed.
- At d>=2, w<u for every positive admissible source. If u is
  below the floor, then w is known too. Again, that membership does
  not provide a prefix replacement satisfying the chosen multiset
  decrease when this move is mixed with certificate consumption.

The d=1 block has its own exact affine charge,

\[
8(w+3)=9(u+3).
\]

Consequently a fixed positive source cannot undergo arbitrarily many
consecutive d=1 blocks: k such blocks require2^(3k) to divide u+3.
Likewise, a consecutive d=0 run uses the charge u+1 through
2(w+1)=3(u+1). The two charges have different centers. Their separate
finite-run arguments do not show that alternating resets consume a
single integer resource. They also do not prove that a source remaining
outside the initial interval acquires the next required certificate.

## 4. First missing global replacement lemma

PR176 provides the well-founded Dershowitz–Manna multiset order and a
sound rule-induction kernel. Those tools permit both source-prefix
consumption and replacement by longer prefixes whose inserted states
are below removed states. The missing ingredient is an all-state
selector supplying those actual replacements.

In the adjacent form, a completion would have to justify the d>=1
transition by one of the following actual mechanisms: a certified
replacement leading to the required new source, a direct known endpoint
of the bad component below the floor, or a different child obligation
whose proved rank decreases. None of the refreshed files or the present
charged-return theorem proves such a transition for every live reset
state.

This cannot be supplied by asserting that a larger ternary multiplier
preserves basin membership. The exact source-tail transport in PR176
leaves unbounded targets3^a−1 even at terminal power-of-two sources.
Its Mersenne recursion closes the even exponent fold, but not the
remaining odd exponent family. PR177 additionally proves a two-letter
source-certificate family whose displayed reset exceeds any fixed
linear multiple of the original target. That result concerns its
specified component reset, not every possible proof strategy.

## 5. What the new charge proves, and what it does not

Oriented.lean proves a complete positive conditional rule for every
natural k: k actual guarded22-clock expanding returns, followed by the
P1 exit with r>=k, give the paired ordinary descent

\[
8u\le3m+40,\qquad0<u<m
\]

when m>=9, together with exact endpoint and odd-count identities and
reverse-failure transfer. It also proves a finite binary budget for
consecutive runs of that expanding block.

What remains unproved is universal access to a paying exit, or a common
decreasing resource spanning the other multipliers, offsets, and source
certificate resets. Neither the finite escape bound for one block nor
the full ordinary floor supplies that missing implication by itself.

**The full Collatz theorem and total payment are not proved in this
checkpoint.**
