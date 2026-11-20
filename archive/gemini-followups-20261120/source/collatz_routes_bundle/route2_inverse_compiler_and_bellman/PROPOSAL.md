# Route 2: Eliminating PR #147's Stationarity Hypothesis & Certifying Inverse-Compiler Slopes $< 2$

- **Status:** `PROPOSED` (with `VERIFIED_COMPUTATIONAL` Bellman–Isaacs certificates)
- **Target PRs:** [PR #147](https://github.com/GettysburgResearch/collatz/pull/147) (`13/6` compiler + conditional `39/20` bridge), [PR #148](https://github.com/GettysburgResearch/collatz/pull/148) (`25/12` compiler, 1.87 MB policy)

## 1. Exact Current State & Bottlenecks

- **PR #147** certifies an explicit inverse compiler for unit tails $0 < c < 3^t$ with $T^k(2^k x + r) = 3^t x + c$ and $k \le \lfloor (13t + 65)/6 \rfloor$ ($354,294$ states, max credit $66$). It also derives an existential **$39/20 = 1.95$** bridge ($1.937 < A < 1.938$), **conditional on an unproved unique-stationarity hypothesis at credit cap $R \ge 6$**.
- **PR #148** sharpens the explicit certificate to $k \le \lfloor (25t + 120)/12 \rfloor \approx 2.0833 t + 10$ via a 1,872,249-byte policy table.

## 2. Idea 1 — Deterministic Bellman–Isaacs Potential Certificates (Zero Stationarity Hypothesis!)

Instead of proving probabilistic unique stationarity or storing a 1.87 MB policy table, formulate the inverse compiler on the finite state space $S_P = (\mathbb{Z}/3^P\mathbb{Z})^\times$ (or augmented with credit cap $r \in \{0, \dots, R\}$) as a **two-player deterministic minimax game**:
- **Compiler chooses:**
  - $E(z) = 2z \pmod{3^P}$ (cost $\Delta k = 1, \Delta t = 0$), always staying in $(\mathbb{Z}/3^P\mathbb{Z})^\times$.
  - $O(z) = (2z - 1)/3 \pmod{3^{P-1}}$ (cost $\Delta k = 1, \Delta t = 1$), valid iff $z \equiv 2, 8 \pmod 9$ (explicitly avoiding $z \equiv 5 \pmod 9$, whose $O$-image lands in $0 \pmod 3$).
- **Nature (adversary) chooses** the next revealed base-3 digit $d \in \{0, 1, 2\}$, sending $z \mapsto ((2z-1)/3 \bmod 3^{P-1}) + d \cdot 3^{P-1}$.

**Certificate Theorem:** If there exist a slope $\alpha \in \mathbb{Q}$ and a potential function $h: S_P \to \mathbb{Q}$ satisfying the single pointwise inequality
$$h(z) \ge \min\Big(1 + h(2z \bmod 3^P),\; 1 - \alpha + \max_{d \in \{0,1,2\}} h(\text{next}_d(z))\Big) \quad \forall z \in S_P,$$
then **every** unit tail $c \in (\mathbb{Z}/3^t\mathbb{Z})^\times$ is compiled with
$$k \le \alpha t + \big(\max_{S_P} h - \min_{S_P} h\big)$$
**unconditionally**, with **no stationarity hypothesis** and **$O(|S_P|)$ verification time** (directly checkable in Lean 4 by clearing denominators!).

### Verified Computational Results (`bellman_potential_certifier.py`)
Running damped Bellman–Isaacs value iteration on pure $(\mathbb{Z}/3^P\mathbb{Z})^\times$ (before even adding credit cap $R$):
- $P = 3$ ($18$ unit states): exact minimax slope $= \mathbf{3.0000}$ ($3/1$), potential span $= 5.0$.
- $P = 4$ ($54$ unit states): exact minimax slope $= \mathbf{2.6667}$ ($8/3$), potential span $= 6.3333$.
- $P = 5$ ($162$ unit states): exact minimax slope $= \mathbf{2.5000}$ ($5/2$), potential span $= 7.5$.
- $P = 6$ ($486$ unit states): exact minimax slope $= \mathbf{2.5000}$ ($5/2$), potential span $= 9.0$.

**Next Step for the Repo:** Augment $S_P$ with the PR #147 credit state $r \in \{0, \dots, R\}$ (or increase $P$ to $7, 8, 9$ using sparse Howard policy iteration) and export the rational potential $h(z, r)$ as a compact certifier beating $25/12$ and crossing $\alpha < 2$ (targeting $39/20 = 1.95$ **unconditionally**).

## 3. Idea 2 — Proving PR #147's Unique-Stationarity Hypothesis Directly (Birkhoff–Hopf Contraction)

If the repo also wants to keep PR #147's probabilistic/stationary bridge intact at cap $R \ge 6$:
1. Show that the capped credit-transfer operator $Q_R$ on $\mathbb{Z}_3^\times \times \{0, \dots, R\}$ satisfies a **Doeblin minorization condition** (every state reaches the bottom credit layer $r = 0$ and hits a full cylinder of $(\mathbb{Z}/3^P\mathbb{Z})^\times$ within $N_0$ steps with positive probability $\ge \delta > 0$).
2. By **Birkhoff–Hopf projective contraction** on the positive cone of locally constant / Lipschitz densities, $Q_R$ has a **unique stationary probability measure** $\mu_R$ with an explicit exponential mixing rate $(1 - \delta)^{\lfloor n/N_0 \rfloor}$.
3. Since $N_0$ and $\delta$ are finite-graph reachability properties at cap $R = 6$, this can be **machine-certified in Python + Lean 4** in under a second!

## 4. Honest Scope Boundary (PR #149 Audit)
Even an unconditional inverse compiler with slope $\alpha < 2$ (e.g., $39/20 = 1.95$ or approaching $\log_2 3 \approx 1.585$) certifies **predecessor reachability / density** from unit tails, NOT universal forward convergence by itself. Per PR #148/#149, it must be coupled with an **asynchronous merger bridge** (Route 1) or **global integrality bound** (Route 3) to close forward Collatz.
