# Persistent ordinary representatives and their exact stopping defect

**PROPOSED, unconditional except for the explicitly marked existence input in Section 5.**

This extends the least-representative analysis in PR146 at frozen head
`92820dd336b010215eb8a6eb4878a31b58a67656`,
`research/upper-bit-mergers/PREFIX_REPRESENTATIVES.md`. It does not prove
Collatz or assign a stopping time to an unproved converger.

Use the shortcut map \(T(n)=n/2\) for even \(n\) and
\(T(n)=(3n+1)/2\) for odd \(n\). Let \(\mathcal B\) be the actual basin
of 1, and let \(H=\{n>0:n\equiv1\pmod3\}\).

## 1. A complete invariant for eventual equal-count synchronization in the basin

For \(n\in\mathcal B\), let \(d(n)\) be its first hitting time of 1 and
\(a(n)\) the number of odd inputs strictly before that first hit. Define

\[
\kappa(n)=d(n)-2a(n).
\]

In particular \(\kappa(1)=0\) and \(\kappa(2)=1\).
For every \(n\in\mathcal B\), including \(n=1\),

\[
\kappa(n)=1-2(n\bmod2)+\kappa(T(n)).                 \tag{1}
\]

For \(n\ne1\), this just removes the first step of the first-hit path.
At 1 it reads \(0=-1+\kappa(2)\), so it is still exact on the cycle.
Consequently, if \(s_h(n)\) counts odd inputs in the first \(h\) steps,

\[
\kappa(n)=h-2s_h(n)+\kappa(T^h(n))                  \tag{2}
\]

at every common clock, even after the first hit.

**Theorem 1.** For \(n,m\in\mathcal B\), the following are equivalent:

1. \(\kappa(n)=\kappa(m)\).
2. At some common clock \(h\), both \(T^h(n)=T^h(m)\) and
   \(s_h(n)=s_h(m)\).
3. Both equalities hold at every sufficiently large common clock.

**Proof.** The second statement implies the first by (2), and equality of
the two augmented states persists under the deterministic next step.
Conversely, equal \(\kappa\) implies that \(d(n),d(m)\) have the same
parity, since \(\kappa\equiv d\pmod2\). For
\(h\ge\max(d(n),d(m))\), the two positions on the cycle \(1\leftrightarrow2\)
therefore agree. Equation (2) now gives equal odd counts. QED.

The restriction to the basin is essential. This theorem does not label a
nonconvergent source by a fictitious first-hit defect.

## 2. Exact classification of convergent persistent representatives

For each integer \(k\) for which the set is nonempty, put

\[
m_k=\min\{n\in H\cap\mathcal B:\kappa(n)=k\}.       \tag{3}
\]

The minimum is explicitly over \(n\equiv1\pmod3\), not over all positive
integers. Write \(n=1+3r\). The PR146 filter retains \(r\) at depth \(h\)
if \(0\le r<2^h\) and it is the least index having the pair
\((s_h(1+3r),T^h(1+3r))\).

**Theorem 2.** A source \(n\in H\cap\mathcal B\) is retained at every
eligible depth if and only if \(n=m_{\kappa(n)}\).

**Proof.** If a smaller source \(m\in H\) has the same augmented state at
any depth, it belongs to \(\mathcal B\) because its future agrees with
that of \(n\). Equation (2) gives \(\kappa(m)=\kappa(n)\), contradicting
minimality in (3).

Conversely, if \(m_{\kappa(n)}<n\), Theorem 1 gives the same augmented
state at all sufficiently large depths. At these depths both indices are
eligible, and the smaller one removes \(n\). QED.

Thus persistence does not distinguish a difficult converger from a possible
counterexample. It exactly preserves the least member of each stopping-defect
class within the known basin. No assertion about persistent nonconvergers is
made.

## 3. Every nonnegative class has an explicit least member

**Theorem 3.** For all \(m\ge0\), and all odd \(k\ge3\),

\[
m_{2m}=4^m,\qquad m_1=7,\qquad m_k=5\cdot2^{k-2}.  \tag{4}
\]

**Proof.** Let the odd inputs before the first hit of 1 be
\(u_1,\ldots,u_a\). Multiplying input/output ratios along the actual path gives

\[
\frac{n}{2^{\kappa(n)}}
=\prod_{i=1}^a\frac{4u_i}{3u_i+1}.                 \tag{5}
\]

The empty product is 1 and occurs precisely for powers of two. All factors
in a nonempty product exceed 1. The last odd input satisfies
\(3u_a+1=2^e\) for an even \(e\ge4\): \(e=2\) would give the already
excluded input 1. Hence \(u_a\ge5\), and its factor is at least \(5/4\).
We have proved the sharper dichotomy

\[
n\ge2^{\kappa(n)},\quad
n\text{ not a power of two}\Longrightarrow
n\ge\frac54\,2^{\kappa(n)}.                       \tag{6}
\]

Equality in the second inequality holds exactly when the only odd input is
5, that is, \(n=5\cdot2^v\) with \(v\ge0\).

For \(k=2m\ge0\), \(2^k=4^m\) lies in \(H\), has defect \(k\), and
attains the first lower bound. For odd \(k\), the only possible power of two
with that defect is \(2^k\equiv2\pmod3\), so it is excluded from \(H\).
For odd \(k\ge3\), \(5\cdot2^{k-2}\in H\) attains the second lower bound
and has defect \(k\). Finally, the only members of \(H\) below 7 are 1
and 4, of defects 0 and 2; the exact path from 7 has \((d,a)=(11,5)\),
so \(m_1=7\). QED.

This adds the entire family \(10,40,160,\ldots\) and the isolated row 7 to
the powers of four identified in PR146.

## 4. Negative classes can contain small, slow, persistent convergers

The following minima are certified by exact enumeration of **all** smaller
members of \(H\). This is bounded evidence supporting particular instances
of (3), not a proof that every negative class is nonempty.

| defect \(k\) | \(m_k\) | first-hit steps \(d\) | odd inputs \(a\) |
|---:|---:|---:|---:|
| -1 | 334 | 45 | 23 |
| -2 | 223 | 46 | 24 |
| -3 | 466 | 55 | 29 |
| -4 | 175 | 52 | 28 |
| -5 | 274 | 59 | 32 |
| -6 | 103 | 56 | 31 |
| -7 | 91 | 59 | 33 |
| -8 | 142 | 66 | 37 |
| -9 | 94 | 67 | 38 |
| -10 | 82 | 70 | 40 |
| -11 | 31 | 67 | 39 |
| -12 | 487 | 90 | 51 |

For example, 31 persists at every eligible depth despite its first-hit time
67. Its index is 10, so it is already eligible at depth 4.

There is a uniform reason negative-defect sources cannot satisfy a short
first-hit condition. For \(a\ge1\), the exact affine endpoint formula at
the first hit gives \(2^d>3^a n\). With \(\lambda=\log_2 3\),

\[
d>\frac{2\log_2 n-\lambda\kappa(n)}{2-\lambda}.     \tag{7}
\]

In particular, every source with negative defect has
\(d> [2/(2-\lambda)]\log_2 n\), with multiplier
\(2/(2-\lambda)=4.81884168\ldots\). This is an exact ordinary-path
inequality; it does not use a probabilistic approximation.

## 5. What an inverse rule of mean cost below two supplies

Here is a precise optional existence input:

> There is an infinite positive odd inverse path \(x_0=1,x_1,\ldots\), with
> every \(x_j\) coprime to three, whose total shortcut cost \(E_j\) satisfies
> \(E_j-2j\to-\infty\).

**Theorem 4.** Under this input, \(m_k\) exists for every integer \(k\).
In particular there are infinitely many negative-defect persistent ordinary
convergers. This does not require universal forward convergence.

**Proof.** Every endpoint reaches 1 by construction. Equation (1) applied
to the actual inverse path gives
\(\kappa(x_j)=E_j-2j\), including any initial loops at 1.

From any positive odd unit \(t\), there is an inverse odd child
\(I_e(t)\equiv1\pmod3\) with \(1\le e\le6\). Indeed this is equivalent
to \(2^e t\equiv4\pmod9\); 2 generates the six units modulo nine. The
child is positive and odd, and its defect is \(\kappa(t)+e-2\).
Thus there are odd members \(n\in H\cap\mathcal B\) of arbitrarily negative
defect.

For such an odd \(n\), multiplication by four preserves \(H\) and increases
\(\kappa\) by 2. Also \(4n+1\) has the same odd-map successor as \(n\),
with two additional shortcut steps and the same odd count. Hence
\(8n+2\in H\cap\mathcal B\) has defect \(\kappa(n)+3\).
This statement also holds at \(n=1\), directly from the path of 10.
Every integer at least two is a nonnegative combination of 2 and 3 (one
use of 3 suffices). Starting at a sufficiently negative odd \(H\)-source
therefore realizes any prescribed integer defect within \(H\). Well-ordering
then supplies (3). QED.

**SOURCE-QUALIFIED supply of the input.** Use PR147 at frozen head
`b74b2d466f58844a742a6ed6bcdf06844269f361`,
`research/robust-inverse-credit/DERANDOMIZATION.md`, Theorem D3 and Section6.
Its small finite policy calculation is independently reproduced there.
Conditional on the external stationary uniqueness assumption UQ(6), D3
supplies a robust cap-six finite potential with slope \(39/20\). Iterating
its selected legal actions from the ordinary integer 1 gives

\[
E_j-2j\le-j/20+O(1)\longrightarrow-\infty.
\]

No explicit table achieving slope \(39/20\), precision, or maximum credit
is supplied by that existence theorem. The remaining qualification is
UQ(6), including its analytic dependencies. This note does not claim an
unconditional elementary construction of every negative class without this
input or another inverse certificate of slope strictly below two.

## 6. The shifted-power tail criterion leaves a thin diagonal

PR146's shifted-power reduction applies to a convergent lower row \(x\)
when its separation exponent \(j\) satisfies \(j\ge d(x)\). This is a
statement about each fixed row's eventual tail. It is not a uniform
statement on rows \(x=1+3w\) with \(0\le w<2^j\).

**Theorem 5.** Among those \(2^j\) lower rows, at most \(F_{j+3}\) satisfy
\(d(x)\le j\), where \(F_0=0,F_1=1\). Their fraction is
\(O((\varphi/2)^j)\), with \(\varphi=(1+\sqrt5)/2<2\).

**Proof.** Let \(N_h(t)=\#\{n>0:T^h(n)=t\}\). A multiple of three has
only its doubling predecessor, so \(N_h(t)=1\) there. Put
\(A_h=\sup_{t\equiv1(3)}N_h(t)\),
\(B_h=\sup_{t\equiv2(3)}N_h(t)\).
The exact inverse branches give
\(A_{h+1}\le B_h\) and
\(B_{h+1}\le A_h+\max(A_h,B_h,1)\).
Induction from \(A_0=B_0=1\) gives
\(A_h\le F_{h+1}\), \(B_h\le F_{h+2}\).
Every source that has hit 1 by time \(j\) is at 1 or 2 at that time, so
there are at most \(N_j(1)+N_j(2)\le F_{j+3}\) such sources in total,
and no more among the selected rows. QED.

Passing to a same-clock representative at depth \(j\) cannot evade this
obstruction: if the representative has already reached the cycle, the
original source is also on that cycle at depth \(j\), and reaches 1 no later
than \(j+1\). The same exponential bound with an index shift applies.
Dyadic padding does not improve the margin either:
\(d(2^q x)=q+d(x)\), while the separation exponent becomes \(j+q\).

The next missing theorem is therefore not merely convergence of the two
shifted-power families. It must also handle rows before their lower source's
first-hit time, or supply a different merger construction. Theorem2 identifies
the persistent convergent rows exactly; it does not remove the unknown
nonconvergent ordinary rows.

## Verification and sources

The separate [shifted-power rigidity note](SHIFTED_POWER_RIGIDITY.md) proves
that an unequal-clock merger of $3^k+c$ and $3^l+d$, with
$c,d\in\{0,1,2\}$, needs at least $\min(k,l)$ shortcut steps on one arm.
A merger with both clocks below that threshold is a homogeneous identity
and propagates along an explicitly specified progression of exponents.
This provides a certificate-propagation rule, not universal mergers.

`check_persistent_defects.py` checks exact ordinary paths, the augmented-state
identity, all listed negative minima, finite instances of (4), and the
Fibonacci preimage bound. Its stopping cap makes an unresolved finite path a
failure rather than assuming convergence. Its scope is recorded in its output.

- [PR146 frozen prefix-representative packet](https://github.com/GettysburgResearch/collatz/blob/92820dd336b010215eb8a6eb4878a31b58a67656/research/upper-bit-mergers/PREFIX_REPRESENTATIVES.md).
- [PR147 frozen derandomization theorem D3 and sub-two consequence](https://github.com/GettysburgResearch/collatz/blob/b74b2d466f58844a742a6ed6bcdf06844269f361/research/robust-inverse-credit/DERANDOMIZATION.md).

All algebraic proofs in Sections1–4 and6 are local. The inverse mean-cost
existence claim in Section5 retains its external qualification. No claim that
these results settle Collatz is made.
