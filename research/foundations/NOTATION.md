# Foundations packet — notation and conventions (99xx namespace)

Packet owner: fable-02. Created: 2026-07-21. Last updated: 2026-07-21.

**Namespace reservation.** This packet uses claim IDs `D-9901…`, `L-9901…`, `Q-9901…`,
`X-9901…` to avoid collision with the active namespaces (`0001`-range: PR #3 / issue #4;
`01xx`: PR #11; `90xx`: PR #6; `91xx`: PR #12; `92xx`: PR #14; `93xx`: PR #16; `94xx`: PR #20;
`95xx`: PR #19; `96xx`: issue #21; `98xx`: issue #29). Per the emergent project convention,
this packet edits no canonical root ledger; everything lives under `research/foundations/`.

**Purpose.** A canonical, adversarially verified layer of the *classical* load-bearing lemmas
that active branches currently either import from literature without in-repo proof or re-prove
piecemeal. Every file follows README §8 and uses the notation below.

Throughout, $\mathbb{Z}^+ = \{1, 2, 3, \dots\}$, $\mathbb{Z}_2$ denotes the 2-adic integers,
$\log_2 3 = \ln 3/\ln 2 \approx 1.5849625$, and
$$\gamma := \log_3 2 = \ln 2/\ln 3 \approx 0.6309298.$$
$\nu_2(n)$ is the 2-adic valuation of $n \neq 0$.

---

## D-9901 — Collatz map
$C: \mathbb{Z}^+ \to \mathbb{Z}^+$,
$$C(n) = \begin{cases} n/2 & n \text{ even} \\ 3n+1 & n \text{ odd.} \end{cases}$$

## D-9902 — Shortcut (Terras) map
$T: \mathbb{Z}^+ \to \mathbb{Z}^+$,
$$T(n) = \begin{cases} n/2 & n \text{ even} \\ (3n+1)/2 & n \text{ odd.} \end{cases}$$
Unless stated otherwise, iteration counts, parity vectors and stopping times refer to $T$.

## D-9903 — Odd part
For $n \in \mathbb{Z}^+$, $\mathrm{odd}(n) := n / 2^{\nu_2(n)}$.

## D-9904 — Syracuse map
$S$ on the positive odd integers:
$$S(x) = \frac{3x+1}{2^{\nu_2(3x+1)}} = \mathrm{odd}(3x+1).$$
The **exponent** of the step at $x$ is $a(x) := \nu_2(3x+1) \ge 1$.

## D-9905 — Orbits and reaching 1
$O_M(n) := (n, M(n), M^2(n), \dots)$ for $M \in \{C, T, S\}$, with $M^0(n) = n$.
"$n$ **reaches 1** under $M$" means $M^k(n) = 1$ for some $k \ge 0$.
**Trivial cycles:** under $C$: $(1,4,2)$; under $T$: $(1,2)$; under $S$: the fixed point $(1)$.

## D-9906 — Parity vector
For $n \in \mathbb{Z}^+$ (or $n \in \mathbb{Z}_2$) and $i \ge 0$:
$$v_i(n) := T^i(n) \bmod 2 \in \{0,1\}, \qquad a_k(n) := \sum_{i=0}^{k-1} v_i(n).$$
$(v_0, \dots, v_{k-1})$ is the **parity vector (word) of length $k$**; $a_k$ counts **odd steps**
among the first $k$.

## D-9907 — Bounded, unbounded, divergent orbits
An orbit $(x_k)$ is **bounded** if $\sup_k x_k < \infty$, **unbounded** otherwise, and
**divergent** if $x_k \to \infty$.

## D-9908 — Nontrivial cycle
A **cycle** of $M$ is a purely periodic orbit; its **length** is the least period. A cycle is
**nontrivial** if it is not the trivial cycle of $M$ (D-9905). For $S$-cycles we write
$x_1 \to x_2 \to \dots \to x_m \to x_1$ (least period $m \ge 1$, all $x_i$ positive odd),
exponents $a_i := \nu_2(3x_i+1) \ge 1$, partial sums $A_0 := 0$, $A_i := a_1 + \dots + a_i$, and
$K := A_m = \sum_{i=1}^m a_i$.

## D-9909 — Collatz counterexample
$n \in \mathbb{Z}^+$ is a **counterexample** if $1 \notin O_C(n)$.
**Collatz conjecture:** no counterexample exists. This project's objective is to construct one;
all claim files must remain neutral and rigorous about which way the truth lies.

## D-9910 — Stopping time
$\sigma(n) := \inf\{k \ge 1 : T^k(n) < n\} \in \mathbb{Z}^+ \cup \{\infty\}$.

---

## Conventions

- Sub-claims inside a file `L-99XX` are numbered `L-99XX.1`, `L-99XX.2`, …
- Statuses per README §7. A file's author sets at most `PROPOSED`; only an independent
  reviewing agent may upgrade to `PROVED`, recording itself under `Reviewing agents:`.
- Math is written in `$…$` / `$$…$$` LaTeX inside Markdown.
- Empty sums are $0$; empty products are $1$.
- Computational checks inside claim files are **finite verification**, never proof; label them so.
- Files are self-contained modulo dependencies explicitly listed in their header; where a
  dependency's file might land later than this one, the needed statement is re-derived inline
  and the overlap is noted in the Dependency audit.

## Packet index

See `FOUNDATIONS.md` (written at packet completion) for the lemma index, statuses, and the
map from each lemma to the active research directions it serves.
