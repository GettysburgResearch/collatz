# Independent review of the exact-clock escape and cycle tests

**Verdict.** VERIFIED as written for the finite arithmetic and conditional implications identified below. The convergence criterion is a mathematical equivalence. Its required upper bound is OPEN.

This review covers PR201's continuation based on commit `73a145ca99448a78219bd149e273f33b6e3fda4b`. SHA-256 fixes the new working-tree files before publication.

| Reviewed file | SHA-256 |
|---|---|
| `research/killed-green-head-closure-20261124/escape-analysis/README.md` | `1718e91e498b7491e7c6a9e939f92609a46b78bb0bb1e355b6588e6c73384b39` |
| `research/killed-green-head-closure-20261124/escape-analysis/controls.py` | `91c7fa2f2ee92a82e536867a12ffdc91c9bd4f48ba9010f0a23706d9400ad9f0` |
| `research/killed-green-head-closure-20261124/escape-analysis/CONTROLS.json` | `b24581bff08881816697cf0fad6159052288a8e70ed28dc21e1300232606e517` |
| `research/astra-three-routes/pass3/FINITE_RECORDS.md`, T-A3-651 section 1, at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` | `82bc394dc7336c43eb38abf13f2bddf837ff227c3d6e85c3bebd3ad327885e3f` |

## Reconstruction

1. **Exact two-gap completion.** For chronological gaps $f,t-f$, substitution into the two successive equations $3x+1=2^f y$ and $3y+1=2^{t-f}z$ gives $9x=2^t z-2^f-3$. The required residue for $2^f$ modulo $3^{K+2}$ is prime to three. The order of two is $2\cdot3^{K+1}$ there, so the given total leaves a positive second gap. Modulo three the congruence gives $2^{t-f}z\equiv1$, hence the intermediate $y$ is integral. Substitution yields the required positive odd source in the specified unit class. This construction keeps the supplied $z$ itself. At one less than the universal cutoff, $z=13,r=1$ forces $f$ divisible by the entire total, impossible for two positive gaps.

2. **Branch counts on one exact row.** On a nonconvergent odd unit ray every state is at least five. Telescoping $2^{A_i}=(q_0/q_i)\prod_{j<i}(3+1/q_j)$ yields the stated spare clock $2i-A_i\ge i\log_2(5/4)-\log_2q_0$. With $i=b-m-2$ and $m\le b/16$, the two-gap total is at least $b/32+17/5-\log_2q_0$ because $\log_2(5/4)>3/10$. Thus it eventually exceeds $b/40$. Each node offers two distinct unit predecessors of cost at most six. At fixed split positions the full source uniquely determines its valuation word, so the $2^m$ sources in each prescribed class are distinct even for periodic terminals. The common suffix has relative carry $1-D_i^{-1}\ge1/(3q_0+1)$. Its affine coefficient is positive, so a nonnegative earlier offset preserves this bound. The terminal chosen for all classes is $q_i$. On an escaping ray $i$ changes with $b$.

3. **Finite gate under convergence.** I checked the recalled counting argument of T-A3-651 through its explicit reciprocal bound. Discarding the final $d$ odd states makes remaining $d$-step endpoints distinct in a simple path. The low-total words are bounded by the composition generating function with $z=4/5$. High-total words have distinct positive odd endpoints below the stated affine cap. Together these give $5X^{39/40}$ and integration gives $200M^{-1/40}$ for paths above $M$. For a simple path the relative carry is at most $\frac13\sum 1/x$. High carry therefore implies a visit to a fixed finite set, with the bound depending on the fixed positive threshold. Under convergence a repeated state would trap the terminal on the $1,2$ cycle, whose only odd state is 1. The forward images of the small gate form a finite set. Any $h(b)\to\infty$ eventually carries every eligible odd terminal in that set to 1. This proves eventual zero for the filtered $M_b$ statistic.

4. **Cycle recognition and the filter using only the recorded row.** On a simple path $D\le e^{200/3}<2^{100}$. Thus the threshold $1-2^{-100}$ requires a repeated state, which makes the actual terminal periodic. For a periodic $q>1$ a suffix containing many complete laps has $D_i\to\infty$, and the interval of allowed $m$ contains the required cycle phase for every sufficiently large $b$. For the separate $R_b$ test, at each large $b$ an escaping ray supplies at least $b/64-1$ distinct terminals above $b/64$. A nontrivial cycle instead supplies a repeated state inside the recorded suffix, retaining exponentially many sources even at one fixed terminal. Under convergence high carry forces the terminal into the finite forward image of the small gate, and a row ending at $q>1$ cannot repeat. Both alternatives in the $R_b$ filter are then eventually empty. No forward iteration beyond the recorded terminal and no inverse atom floor enters this version.

The statistic is finite at each fixed $b,\epsilon$ by the elementary bound $\beta\le(3/2)^b-1$. The max-over-terminals condition poses the unresolved problem of proving a cofinal upper bound for **every** fixed threshold. The quantifiers do not give an asymptotic large-depth lower bound at an arbitrary fixed nonperiodic target.

## Executed control

A fresh `python -X utf8 -B research/killed-green-head-closure-20261124/escape-analysis/controls.py` execution and byte comparison reproduced the pinned JSON. It included 6,760 two-gap cases, three sharp-cutoff exclusions, 480 direct-vs-inverse row comparisons, and 40,336 literal padded sources on four rows. The largest used clock 448 and had 36,864 sources. This review addresses the written arguments and the finite control separately. It makes no claim of a Lean formalization of the infinite dichotomy.
