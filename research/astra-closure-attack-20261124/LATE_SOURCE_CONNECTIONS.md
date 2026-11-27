# Connections to the incoming PR195–198 closing attempts

**Status: source-qualified written deductions and a focused source comparison.** The late GitHub refresh found four additional packets. Their exact commits and consumed files are added to SOURCES.json. The comparisons below reconstruct the relevant interfaces; they are not a whole-branch audit and do not import the other sessions' compiler counts into ours. None closes the universal obligation.

## 1. Guarded mergers on every odd L/P phase

Read PR195 at `a24ef018147a1e16bf314d14085e2d0d6c620d32`, `research/astra-global-closure-20261124/structural/README.md` and `audit/SHADOW_RIGIDITY.md`; and PR196 at `27d03cfe902660e06604eb55bb28ca3d2754ff48`, `research/astra-orbit-cycle-20261124/mergers/TWO_ANCHOR_MERGERS.md`.

PR195's direct long merger has source `n=2^(33k)u-17` with positive `k=148 mod256`, and a further endpoint guard. All such sources are 15 modulo 16. On an infinite actual L/P input, the odd phases are confined to `{3,5,7,9,11}` modulo 16. Thus this source family never applies directly at any of its odd states. This does not rule out a differently constructed inverse predecessor or a more general extension of that family.

PR196's rule writes `n+1=2^H M` with M odd and requires `3^H M=1 mod4`. It merges the half-size source `(n-1)/2` with n at unequal clocks. The complete L/P phase check is:

| Odd phase n | Forced arithmetic | Guard |
|---|---|---|
| L entry | `n=9 mod16`, H=1, M=1 mod4 | Fails |
| L intermediate before another L | `n=11 mod16`, H=2, M=3 mod4 | Fails |
| P entry Q | `Q=3 mod64`, H=2, M=1 mod4 | Holds |
| P intermediate `(3Q+1)/2` | `n=5 mod16`, H=1, M=3 mod4 | Holds |
| L intermediate before P entry Q | `n=87 mod128`, H=3, M=3 mod4 | Holds |

The actual next paid boundary `P(Q)=(9Q+5)/32` already beats the successful partners, including their odd parts. At a P entry, `(Q-1)/2-P(Q)=7(Q-3)/32`. At its intermediate, the half is even with valuation exactly one; its **odd part** is `(3Q-1)/8`, whose excess over P(Q) is `3(Q-3)/32`. For a light intermediate just before a paid entry, `n=(2Q-1)/3`; its half is odd and exceeds P(Q) by `(5Q-79)/96`. Here Q is both 3 modulo 64 and 2 modulo 3, so Q is at least 131. The exceptional P entry Q=3 already reaches one.

Consequently this selector gives no improvement over the paid boundary in the original-floor comparison at any odd L/P phase. It does not resolve PPLLL, PLLPP, or PLLPL after an arbitrarily long initial growth run.

The PR195 rigidity theorem does sharpen a different interface. A finite **total causal deterministic** affine controller with one shrinking real slope and two target odd steps at each source letter's original binary clock retains the exact guard `83 | q+7`. Its proof does not assume commuting transitions or a supplied bound on memory. Our finite-uniform rational-slope obstruction permits horizon-dependent choices, while the new ramp uses different clocks and a slope depending on the initial run. These are different quantifier and timing conditions, so the positive ramp is consistent with the incoming rigidity theorem.

## 2. The critical section does not give an immediate return

Read PR197 at `2fb1f11c959e35eba875338833d84969222dc089`, `research/ayh-resource-reset-20261124/positive-section/CRITICAL_SECTION.md` and `LATEST_SOURCE_CONNECTIONS.md`.

For odd n write `d=floor(log_2 n)`, `e=v_2(3n+1)`. Mark n when `(d+1)(n-2^d)<=70*2^d`. The critical section B additionally requires `0<=5e-(d+1)<=7`. The source proves universal convergence equivalent to convergence on B. Above that surplus range a quarter partner remains in the larger section, reduces the surplus by eight and preserves the next odd endpoint. Within B, a legal further quarter reduction has negative surplus and leaves that larger section. The next odd value is of order `n^(4/5)` but need not return to B.

Two elementary deductions make that return obstruction explicit.

### Every large first endpoint lies outside the mark

For n in B, `n/2^d=1+O(1/d)` and `e=d/5+O(1)`. Put `u=(3n+1)/2^e`. Then for all sufficiently large d,

\[
\lfloor\log_2 u\rfloor=d-e+1,\qquad
\frac{u}{2^{d-e+1}}=\frac{3n+1}{2^{d+1}}\ge\frac32.
\]

Since `d-e` tends to infinity, this violates the shrinking mark allowance `70/(floor(log_2 u)+1)`. Thus the first power-size drop is universally a departure from the marked set at high octaves. It is not a descent within the induction section.

### Long ordinary excursions before any section return

Fix **any** surplus `s in {0,...,7}`. Let e tend to infinity, put `d=5e-1-s` and `r=floor(d/2)`, and choose n in

\[
2^d\le n\le 2^d+\frac{70\,2^d}{d+1},\qquad
3n+1\equiv-2^e\pmod {2^{e+r+1}}. \tag{1}
\]

The congruence is one residue class because 3 is invertible modulo the modulus. The interval contains exponentially many representatives: its length divided by the modulus is of order `2^(d-e-r)/d`, whose logarithm to base two is `(3/10)d-O(log d)`. For sufficiently large d every representative has binary exponent d, exact gap e and surplus s, and belongs to B.

Its first odd endpoint satisfies `u+1=0 mod 2^(r+1)`. The next r odd gaps are all one, and their states are exactly

\[
u_j+1=(3/2)^j(u+1),\qquad 0\le j\le r.
\]

For `0<=j<r` these large states have exact gap one, hence negative section surplus. The next endpoint u itself lies outside the mark as above. Moreover

\[
\frac{\log_2 u_r}{d}\longrightarrow
\frac45+\frac12\log_2(3/2)>1.
\]

Therefore the orbit exceeds its original n before a return to the section is possible; even if the terminal state u_r belongs to the section, it is already larger than n. The argument supplies finite ordinary paths. It makes no claim about the eventual fate of these sources or exclusion of a later return below n.

### Combining with smooth-summand complexity

This same class explains why the new stationary theorem does not close the section by itself. Fix a finite prime set P containing 2 and 3, let t be its size, and write `h_P` as in SOURCE_EXTENSION. There are `O_P(d^t)` positive integer P-units below `2^(2d)`. Thus the number of integers below that height expressible using at most K such summands is at most

\[
(1+O_P(d^t))^K.
\]

Take `K=floor(d/(10t log_2 d))`. This count is `2^(d/10+o(d))`. Each map from n to any of `n,u_0,...,u_r` in (1) is injective. All these states are below `2^(2d)` for large d. A union bound over the `r+2` positions therefore removes at most `2^(d/10+o(d))` candidate sources. There are `2^((3/10)d-O(log d))` candidates in (1), so some remain. Every state of the displayed finite prefix for such a source has `h_P>K`.

Hence every surplus value contains arbitrarily high section sources with a linear-in-d initial excursion above the original floor and positive integer summand complexity at least `c_P d/log d` at **every** state of that prefix. Mark membership alone supplies no uniform low-complexity bound on these prefixes. This is compatible with the stationary theorem and with eventual convergence; a later mechanism is still needed.

## 3. Cycle minimum arcs and reused centers

Read PR198 at `c76acf99ba3fb05e7cc07ca7db7e467954c2d950`, `research/astra-frontier-20261124/{README.md,MINIMUM_ARC.md,LATE_FRONTIER.md}`; and PR196's `cycles/ROTATIONAL_EXCLUSION.md` at the commit above.

At a cycle minimum x, let the first contracting arc have endpoint y, multiplier rho<1, and affine center c. The exact identity is

\[
y-x=(1-\rho)(c-x).
\]

Since y is at least x, c is at least x and `h(c)>=log x`. A lower bound for the length of this arc does not supply a small center or control the remaining windows. PR198's contracting equal-length dictionary result `r_blocks<=K^2` assumes such a tiling by K words. It does not construct a cheap dictionary for an arbitrary cycle.

There is a positive combination with our centers. A rational center of a shortcut word has odd denominator and follows that word under literal rational parity. If two different cyclic boundaries have windows with the same center, their first L parity bits agree, where L is the shorter window length. PR196 R1 then gives the complete-denominator bound

\[
d>\frac{2^A-3^p}{3^{A-L}}.
\]

Its source-qualified all-period R2 consequence forbids such center reuse in a primitive nonstandard ordinary cycle when both windows have length at least `ceil(A/2)-1`. This does not require equal clocks or small center height. There is no proved structural reason for an arbitrary candidate to contain that reuse. The incoming minimum-arc and rotational results therefore strengthen necessary conditions without providing the cheap-window upper bound needed by CYCLE_EXTENSION.

The quarter-section argument, finite-cylinder construction, phase checks, and reused-center implication above are written deductions. No incoming external computation was rerun, and no additional Lean declaration is claimed for this late comparison.
