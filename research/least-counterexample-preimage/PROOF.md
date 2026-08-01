# Least-counterexample preimage and packing attack

**Agent:** `gpt56-pro-56`  
**Issue:** #78  
**Base:** stacked on PR #77 / PR #76  
**Claim namespace:** isolated `66xx`  
**Status:** all theorem-level claims below are **PROPOSED** pending independent reconstruction  

**No proof of the Collatz conjecture is claimed.** This packet attacks only the two exhaustive coefficient-stopping lanes already isolated in PRs #76--#77. It adds no prescribed infinite schedule, inverse-limit construction, or bounded census.

---

## 1. Setup

Use the shortcut Collatz map

\[
T(n)=\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

For one orbit put

\[
x_k=T^k(n),\qquad
v_k=x_k\bmod2,\qquad
q_k=\sum_{i=0}^{k-1}v_i,
\]

\[
\alpha={\log2\over\log3},\qquad
C_k={3^{q_k}\over2^k}=3^{D_k},\qquad
D_k=q_k-\alpha k.
\]

Finite induction gives the exact formula

\[
\boxed{
x_k=C_kn+E_k,
\qquad
E_k={1\over2}\sum_{m=1}^k
v_{m-1}3^{D_k-D_m}.}
\tag{1}
\]

Assume Collatz is false and let `n` be its least positive counterexample. Then

\[
\boxed{x_k\ge n\quad(k\ge0).}
\tag{2}
\]

Retain the imported verified floor from PR #76,

\[
N_*=4\cdot3^{44}+2
=3{,}939{,}083{,}608{,}734{,}444{,}931{,}526,
\qquad n>N_*.
\tag{3}
\]

Define the coefficient stopping time

\[
\tau=\min\{k\ge1:C_k<1\},
\]
with `tau=infinity` if no such index exists.

---

## L-6601: the `485/306` ballot constraint is redundant before the first coefficient crossing

**Status:** `PROPOSED`  
**Dependencies:** definitions above; Angeltveit's theorem only for comparison  

For every proper prefix `k<tau`,

\[
C_k\ge1.
\]

Equality is impossible because a positive power of two is not a positive power of three. Hence

\[
q_k>\alpha k.
\tag{4}
\]

Moreover

\[
\alpha>{306\over485}
\iff
2^{485}>3^{306}.
\tag{5}
\]

Therefore

\[
\boxed{485q_k>306k\qquad(1\le k<\tau)}.
\tag{6}
\]

Thus Angeltveit's ballot inequality adds no extra information on the proper prefixes of a coefficient-first-crossing word. At the crossing itself it does give the fixed window

\[
{306\over485}<{q_\tau\over\tau}<\alpha.
\tag{7}
\]

### Method consequence

Any cofinal proof of the delayed-crossing lane must use ordinary-state information, the affine remainder, endpoint merging, or exact cylinder roots. It cannot obtain a stronger proper-prefix language merely by combining coefficient supercriticality with `485/306`.

---

## T-6602: preimage-amplified first-crossing barrier

**Status:** `PROPOSED`  
**Dependencies:** (1)--(3); exact path-merging identities  
**Scope:** a finite first coefficient crossing of a least counterexample  

Assume `tau=j<infinity`, write

\[
q=q_j,\qquad C=C_j<1,\qquad x=x_j=Cn+E.
\]

Because `j` is the first crossing,

\[
D_m\ge0\quad(1\le m<j),\qquad D_j<0.
\tag{8}
\]

The last bit must be even: an odd step multiplies the coefficient by `3/2` and cannot cross from at least one to below one. Thus `v_(j-1)=0`. Every nonzero summand in (1) is therefore strictly less than `1/2`, and there are exactly `q` such summands. Hence

\[
\boxed{0<E<{q\over2}<{\alpha j\over2}.}
\tag{9}
\]

Now suppose a positive integer `y` has a finite path merging into `x`, with exact affine inverse form

\[
\boxed{y={2^a x-A\over3^b},
\qquad a,b\ge0,\quad A\ge0,\quad3^b>2^a.}
\tag{10}
\]

Then `y` is also a counterexample, because its orbit reaches the nonconvergent state `x`. Minimality gives `y>=n`, and therefore

\[
x\ge{3^bn+A\over2^a}.
\tag{11}
\]

Since `C<1`,

\[
E=x-Cn>(x-n)
\ge
\left({3^b\over2^a}-1\right)n+{A\over2^a}.
\tag{12}
\]

Combining (9) and (12) proves

\[
\boxed{
j>{2\over\alpha}
\left[
\left({3^b\over2^a}-1\right)n+{A\over2^a}
\right].}
\tag{13}
\]

This is an architecture-free way to convert any genuinely smaller merging preimage of the first-crossing endpoint into a linear-in-`n` crossing-time barrier.

### Explicit mod-9 consequences

The standard preimage identities give:

1. If `x=2 or 5 (mod 9)`, then
   \[
   y={2x-1\over3},
   \qquad
   \boxed{j>{n+1\over\alpha}}.
   \tag{14}
   \]

2. If `x=4 (mod 9)`, then
   \[
   y={8x-5\over9},
   \qquad
   \boxed{j>{n+5\over4\alpha}}.
   \tag{15}
   \]

3. If `x=8 (mod 9)`, the shorter merge
   \[
   y={4x-5\over9}
   \]
   gives
   \[
   \boxed{j>{5(n+1)\over2\alpha}}.
   \tag{16}
   \]

Using `n>N_*`, these are respectively larger than approximately

\[
6.2432\cdot10^{21},\qquad
1.5608\cdot10^{21},\qquad
1.5608\cdot10^{22}.
\tag{17}
\]

These bounds do not close the residue classes. They show that the path-merging sieve is not merely computational pruning: on a least counterexample it amplifies the first-crossing gate by ten orders of magnitude on four of the six possible nonzero endpoint classes modulo nine.

### Gap audit

The uncovered endpoint classes `1` and `7 (mod 9)` remain. Even in the covered classes, (13) is a lower bound rather than an impossibility theorem. A full proof needs cofinal merge coverage or an upper mechanism on the first-crossing time.

---

## T-6603: distinct-state packing forces logarithmic mean coefficient surplus

**Status:** `PROPOSED`  
**Dependencies:** exact product identity; no external theorem  
**Scope:** the all-prefix-supercritical lane `C_k>=1` for every `k`  

Assume a positive ordinary orbit satisfies

\[
C_k\ge1\qquad(k\ge1).
\tag{18}
\]

Then `C_k>1`, because equality between powers of two and three is impossible, and (1) gives `x_k>n`.

The orbit cannot repeat. If it entered a positive period, the multiplier around that period would be

\[
\prod_{x_i\ \mathrm{odd}}
{3\over2}\left(1+{1\over3x_i}\right)
\prod_{x_i\ \mathrm{even}}{1\over2}=1,
\]
so its coefficient multiplier would be strictly less than one. Repeating the period would eventually force the global coefficient below one, contrary to (18). Thus all `x_k` are distinct.

The exact stepwise product is

\[
\boxed{
{x_k\over n}
=C_k
\prod_{\substack{0\le i<k\\x_i\text{ odd}}}
\left(1+{1\over3x_i}\right).}
\tag{19}
\]

The odd states in the product are distinct odd integers at least `n`. If `a` is the least odd integer at least `n`, sorting them gives the lower bounds

\[
m_r\ge a+2r\qquad(0\le r<q_k).
\]

Using `log(1+t)<=t` and the integral test,

\[
\begin{aligned}
\log\prod_{r=0}^{q_k-1}
\left(1+{1\over3m_r}\right)
&\le {1\over3}\sum_{r=0}^{q_k-1}{1\over a+2r}\\
&\le {1\over3a}
+{1\over6}\log\left(1+{2q_k\over a}\right).
\end{aligned}
\tag{20}
\]

Consequently

\[
\boxed{
x_k\le
n\,e^{1/(3n)}
\left(1+{2k\over n}\right)^{1/6}
3^{D_k}.}
\tag{21}
\]

### Low-band visit bound

For `H>=0` and `K>=1`, define

\[
N_H(K)=\#\{1\le k\le K:D_k\le H\}.
\]

The corresponding `x_k` are distinct positive integers and every one is at most the right-hand side of (21) with `k=K` and `D_k=H`. Hence

\[
\boxed{
N_H(K)
\le
n\,e^{1/(3n)}
\left(1+{2K\over n}\right)^{1/6}3^H.}
\tag{22}
\]

Thus every fixed coefficient-surplus band has at most `O(K^(1/6))` visits.

### Defect-area lower bound

Since `x_1,...,x_K` are distinct integers strictly larger than `n`,

\[
\prod_{k=1}^Kx_k\ge\prod_{r=1}^K(n+r).
\tag{23}
\]

Multiplying (21) over `1<=k<=K`, while replacing the slowly varying factor by its value at `K`, gives

\[
\boxed{
\sum_{k=1}^KD_k
\ge {1\over\log3}
\left[
\log{(n+K)!\over n!\,n^K}
-{K\over3n}
-{K\over6}\log\left(1+{2K\over n}\right)
\right].}
\tag{24}
\]

In particular, as `K/n -> infinity`,

\[
\boxed{
{1\over K}\sum_{k=1}^KD_k
\ge {5\over6}\log_3(K/n)-O(1).}
\tag{25}
\]

Hence an ordinary all-prefix-supercritical orbit cannot be a merely critical bounded-bank path. It must carry a logarithmically diverging mean coefficient surplus, in addition to the pointwise divergence proved in PR #77.

### Gap audit

This still does not contradict an ordinary orbit. A nonnegative defect walk can have logarithmically growing mean height and can revisit low bands on a sparse sequence. The theorem removes bounded-bank and frequent-low-return candidates; it does not extract or exclude the remaining high-bank ordinary path.

---

## R-6601: a fixed verified floor plus the unconstrained mechanical extremizer cannot close all later crossings

**Status:** `PROPOSED / METHOD BOUNDARY`  
**Dependencies:** elementary continued fractions; PR #76 mechanical extremizer  

Let `q/j<alpha` run through lower continued-fraction convergents. Then

\[
0<\alpha-{q\over j}<{1\over j^2},
\]
so for

\[
C={3^q\over2^j}=\exp[-j\log3(\alpha-q/j)]
\]
one has

\[
0<1-C<{\log3\over j}.
\tag{26}
\]

For the upper-mechanical first-crossing word of length `j` and weight `q`, every proper-prefix defect lies in `(0,1)`, while the final defect lies in `(-alpha,0)`. Every odd contribution to (1) is therefore greater than

\[
{1\over2}3^{-(1+\alpha)}={1\over12}.
\]

There are `q` odd contributions, so its maximal remainder satisfies

\[
E_{\mathrm{mech}}>{q\over12}.
\tag{27}
\]

The largest starting value that can fail descent in that cylinder is therefore at least

\[
{E_{\mathrm{mech}}\over1-C}
>{qj\over12\log3}
\asymp j^2.
\tag{28}
\]

Thus, for every fixed ordinary verification floor `N_*`, the inequality

\[
E_{\mathrm{mech}}<N_*(1-C)
\]
necessarily fails along all sufficiently late lower convergents.

This does **not** construct a paradoxical ordinary root. It proves a limitation of the current gate: repeatedly applying the same fixed floor and the unconstrained maximal remainder cannot cofinally exclude the finite-crossing lane. A successful continuation must introduce at least one genuinely new input:

- a growing lower bound on the actual cylinder root;
- cofinal path-merging/preimage coverage;
- a restriction on near-maximizing words tied to ordinary residues;
- or an architecture-level least-root nonstabilization theorem.

---

## Q-6601: exact remaining offense

The current least-counterexample program has two exhaustive lanes.

### Lane A: all-time supercriticality

PR #77 proves `x_k -> infinity`. T-6603 now forces logarithmically diverging mean surplus and `O(K^(1/6))` visits to every fixed surplus band. The missing theorem must use ordinary arithmetic to exclude the remaining high-bank path; another conditional growth theorem will not suffice.

### Lane B: a finite first crossing

PR #76 gives the Farey gate `j>=217,976,794,617`. T-6602 raises this to linear in the least counterexample on four endpoint residue classes. R-6601 proves that a fixed verification floor plus the unconstrained mechanical maximum cannot close all later convergents.

The next result that would materially change the global status is therefore one of:

1. **cofinal merge theorem:** every sufficiently late first-crossing endpoint admits a smaller merging preimage with a contradiction-producing upper bound, not merely a larger lower gate;
2. **ordinary cylinder theorem:** the least ordinary root of every later first-crossing cylinder exceeds its exact paradoxical threshold;
3. **supercritical nonordinary theorem:** no positive ordinary parity path can satisfy both all-prefix supercriticality and the defect-area requirements of T-6603.

No current repository or audited 2026 literature result proves any of these three statements.

---

## Literature positioning

- Angeltveit 2026 supplies the descent, mod-9 preimage, path-merging, odd-even-even, and `485/306` tools used or audited here.
- Rozier--Terracol v5 (published in *Discrete Mathematics*, 2026) is the primary paradoxical-sequence reference and already contains the finite enumeration neighboring PR #76.
- Niu 2026 was withdrawn because the relevant enumeration/mediant observations duplicated Rozier--Terracol v4; it is not used as a proof dependency.
- Chang 2026 proves map-level balance and isolates a one-bit **orbit-level** mixing problem. It does not provide the individual-orbit balance needed to close Lane A.

The latest literature sharpens the same global boundary rather than supplying a hidden final theorem.