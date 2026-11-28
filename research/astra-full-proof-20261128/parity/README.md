# The ordinary upper parity tail at five times the source bit length

**OPEN.** For the shortcut map $T(2u)=u,\ T(2u+1)=3u+2$, let $Q_t(n)$ count odd departures among $n,\ldots,T^{t-1}n$. Write $N=2^k$, $m=5k$, $H=\lceil501m/1000\rceil$. We sought the one-sided estimate
\[
 \liminf_{k\to\infty}N^{-1}\#\{1\le n\le N:Q_m(n)\ge H\}=0. \tag{1}
\]
One source interval, one tail and an unbounded subsequence suffice. We have no proof of (1). A reflected-interval calculation rules out the absolute Fourier estimate one might first try.

## Why (1) would prove Collatz

Every positive start through 64 reaches 1 within 71 shortcuts. A positive nonconvergent orbit therefore stays at or above 65. If $1\le n\le2^k$ is such a source, multiply its actual step ratios to obtain
\[
 1\le T^{5k}n\le 2^{-4k}(196/65)^q,\qquad
 q/(5k)\ge {4\log2\over 5\log(196/65)}>0.5024,\quad q=Q_{5k}(n).
\]
The exact rational certificate for comparison with 0.501 is $196^{501}<2^{800}65^{501}$. Thus every bad source, including every member of a hypothetical nontrivial cycle basin, passes the test at every $k\ge1$ containing it. Mazur's external theorem states that one counterexample forces a positive lower natural density of bad starts. The standard and shortcut maps have the same convergent sources. This proves the implication from (1). We compiled the physical product and finite base locally. Mazur's theorem has an author-reported Lean check. We have not rebuilt its dependency tree. No Gaussian hitting law, component mass exhaustion, or target-independent density constant enters this implication. [Mazur, theorem and source](https://www.proofatlas.ai/proofs/artifact.collatz.nonconvergence_positive_lower_density.v001.html)

Inselmann's Theorem 3.3 controls the centered count through the earlier clock $\kappa_*\log_2 n$, where $\kappa_*=(1-\tfrac12\log_2 3)^{-1}=4.81884\ldots$. PR 213 derives a critical test and supercritical variance criterion with additional fixed-target first-arrival and bridge inputs. Its local-pattern examples exclude stronger fair-coin claims about complete ordinary words. [Inselmann, Theorem 3.3](https://arxiv.org/html/2402.03276v3#S3.Thmtheorem3.3) · [PR 213, critical parity count at cbf7843](https://github.com/GettysburgResearch/collatz/blob/cbf7843dc5a6412dd26eca9495b1327db9d40f33/research/astra-global-rigidity-20261128/mass/CRITICAL_NATIVE_COUNT.md) · [PR 213, local-pattern obstruction](https://github.com/GettysburgResearch/collatz/blob/cbf7843dc5a6412dd26eca9495b1327db9d40f33/research/astra-global-rigidity-20261128/mass/LOCAL_PARITY_BUDGET_OBSTRUCTION.md)

## Why taking absolute values in Fourier space fails

For a binary word $w$ of length $m$, write $d_1<\cdots<d_q$ for its zero-based odd positions. Clearing the forward affine formula gives its unique signed source residue
\[
 r_m(w)=-\sum_{j=1}^q2^{d_j}3^{-j}\pmod {2^m}. \tag{2}
\]
Set $\chi_m(v)=e^{2\pi iv/2^m}$, $u_m=3^{-1}\pmod {2^m}$, and $F_m(z,h)=\sum_w z^{|w|}\chi_m(hr_m(w))$. Splitting by the first bit gives
\[
 F_m(z,h)=F_{m-1}(z,h)+z\chi_m(-hu_m)F_{m-1}(z,hu_m),\qquad F_0=1. \tag{3}
\]
The right frequencies are reduced modulo $2^{m-1}$. The even and odd inverse first steps send a suffix source $r$ to $2r$ and $(2r-1)/3$ modulo $2^m$. Put $G(h)=\sum_{q\ge H}[z^q]F_m(z,h)$ and $D(h)=\sum_{n=1}^N\chi_m(hn)$. The high-weight counts on the two signed intervals are
\[
 C_+=2^{-m}\sum_h G(h)\overline{D(h)},\qquad C_-=2^{-m}\sum_h G(h)D(h). \tag{4}
\]
The zero-frequency term for each is $N\Pr(\mathrm{Bin}(m,1/2)\ge H)=o(N)$.

**Proposed finite theorem, with a locally checked Lean arithmetic kernel.** The negative interval is saturated: $C_-=N$ for every $k\ge1$. Reflect a negative source to $x>0$. Its trajectory becomes the positive minus shortcut $S(x)=x/2$ for even $x$ and $(3x-1)/2$ for odd $x$, with identical parity. All its states are positive and the odd multiplier is at most $3/2$. Hence
\[
 1\le S^{5k}(x)\le 2^{-4k}3^q,\qquad q/(5k)\ge4\log2/(5\log3)>0.5047.
\]
The inequality holds regardless of the fate of the minus trajectory. In particular,
\[
 2^{-m}\sum_{h\ne0}|G(h)D(h)|\ge N[1-\Pr(\mathrm{Bin}(m,1/2)\ge H)].
\]
Even exact magnitudes of both factors at every frequency cannot give an absolute upper bound of $o(N)$. The difference of the two pairings satisfies
\[
 C_+-N=2^{1-m}\sum_h\operatorname{Im}G(h)\operatorname{Im}D(h). \tag{5}
\]
The needed sign concerns the positive arc specifically.

## Where the unresolved Fourier contribution occurs

For $0\le d\le m$, the sum in the positive part of (4) over frequencies factoring modulo $2^d$, including zero, equals
\[
 C^{(d)}=\sum_{n=1}^N\Pr\{\mathrm{Bin}(m-d,1/2)+Q_d(n)\ge H\}. \tag{6}
\]
Restricting to that frequency subgroup averages over all lifts of each residue modulo $2^d$. The initial $Q_d(n)$ still comes from the physical positive source. Each of the $2^{m-d}$ suffix words occurs once among those lifts. For $d\le k$, (6) equals the binomial zero-frequency term by another complete source period.

Let $b_d(n)=T^d(n)\bmod2$. Conditioning on the first remaining bit makes the entire exact-conductor-$2^{d+1}$ contribution
\[
 C^{(d+1)}-C^{(d)}=\sum_{n=1}^N (b_d(n)-\tfrac12)
       \Pr\{\mathrm{Bin}(m-d-1,1/2)=H-1-Q_d(n)\}. \tag{7}
\]
Out-of-range binomial atoms are zero; the desired count is $C^{(m)}$.

For every fixed $0\le c<\kappa_*+0.010$, $C^{(\lfloor ck\rfloor)}=o(N)$. If $c<\kappa_*$, apply Inselmann on $n\ge2^{(1-\eta)k}$ for sufficiently small $\eta>0$, then use binomial concentration on the suffix. For $c\ge\kappa_*$ truncate at $d_0=\lfloor(\kappa_*-\eta)k\rfloor$. Under uniform positive-source sampling $Q_{d_0}-d_0/2=o_{\Pr}(k)$. Deterministically $Q_d-d/2\le Q_{d_0}-d_0/2+(d-d_0)/2$. The threshold is $m/2+0.005k+O(1)$, so the strict inequality for $c$ absorbs the last term, the initial error in probability, and the binomial error after choosing $\eta>0$ small enough. This discharges an initial frequency aggregate using (6). It does not approximate the physical suffix by fair bits. The remaining signed sum of (7) is open.

## Evidence

[ParityTail.lean](ParityTail.lean) was compiled locally in Lean 4.34.1 with warnings as errors. The three public checks reported at its end use only propext, Classical.choice and Quot.sound in their combined axiom set. They cover the finite 64-value base, the per-bad-source inequality, and saturation for the reflected map. The statistical vanishing, external density result and Fourier analysis are not claimed as locally formalized.

[check_parity.py](check_parity.py) checks (2) and (3) at every frequency through depth eight using the order-$2^m$ roots in $\mathbb F_{65537}$. Testing $m+1$ distinct values of $z$ identifies every coefficient modulo that prime. It checks signed Fourier inversion on both arcs at $k=1,2$ and every increment of (7) at $k=3,6,9$. Normal and optimized Python replays agree. These small finite checks do not extrapolate to (1).

[Positive sampling of a Haar-contracting inverse transfer](POSITIVE_SAMPLING.md) gives a sign-aware negative-pole expansion, its exact ordinary diagonal, and an unconditional pointwise bound that still allows escape. [check_sampling.py](check_sampling.py) checks the pole transport, integer-path test and weights for all words through depth eight and positive targets through 48.
