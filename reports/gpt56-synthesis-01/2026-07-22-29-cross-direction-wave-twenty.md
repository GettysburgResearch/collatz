# Cross-direction arithmetic wave twenty

**Agent:** `gpt56-synthesis-01`
**Branch:** `agent/gpt56-synthesis-01/29-cross-direction-lemmas`
**Draft PR:** [#34](https://github.com/gfreund123/collatz/pull/34)
**Date:** 2026-07-22
**Status:** three proposed theorems; no counterexample claim

## Purpose

Wave twenty closes one sharply stated auxiliary boundary in each of three
active mathematical directions:

1. replace the cap's fixed mod-64 observation by a growing same-scale affine
   code and locate its exact first failure bit;
2. prove that the canonical combined-moment Pade approximants are not merely
   convergent but form an exact pairwise ultrametric ladder; and
3. retain the missing one-root memory in a binary physical chart by extracting
   one positive odd carry at every maximal run.

All three arguments are symbolic and memory-light.  Bounded exact arithmetic
was used only as a redundant sign and indexing check.

## Live-source reconciliation

The source branches advanced again while this wave was under review.  A
read-only comparison found the new results compatible and complementary:

- `PR3/L-0033` and `T-0039` now isolate an adjacent twelve-bit room frontier.
  Their digits satisfy `h=A+25 mod64`,
  `q=floor(64*ell/T_3)`, so `64A+q` is exactly the top twelve-bit joint-cell
  quotient of `T-9820`.  `T-9825` controls the complementary growing low-bit
  prefix.  Its lane bound also shows that at least three universal lift lanes
  attain all 4096 two-block patterns; this is an abstract carry-fiber no-go,
  not actual-source branching or cofinal filter emptiness.
- `PR33/T-9705` proposes a separate universal exclusion through a
  connector-free Evertse argument.  Wave twenty does not import or promote
  that external proof chain.
- `PR20/L-9418`, `R-9410`, and `T-9422` close the optimized delayed family at
  period nine and retain period ten as the new-method boundary.  The refreshed
  `Q-9413` still lists direct combined-moment Pade; `T-9821`/`T-9826` now
  supply its zero window, nonzero first survivor, odd denominator, and
  automatic nonproportionality, while global reduced height remains open.
- `PR35/T-8809` independently reconstructs the two-color support floors and
  credits local `T-9819`.  `T-9827` adds the maximal-run quotient memory and
  exact ordinary-stabilization interface absent from that theorem.

## T-9825 -- growing cap low-bit affine code

At stabilized scale `m`, put `r_m=m-6` and

```text
C = -9*3^(-7),       beta = 3^14  in Z_2.
```

LTE gives the exact coefficient endpoints

```text
v_2(N_(m,j)-3^7) = (m+2,m-6,m-5,m-6),
v_2(P_m-3^14) = m-6,
P_m = 3^14 + 2^(m-6) mod 2^(m-5).
```

The right connector is stable one bit farther.  The exact base-cell identity
therefore yields the scale-independent affine chart

```text
Z_m = C-3^14 J_m mod 2^(m-6),
J_m = -9*3^(-21)-3^(-14)Z_m mod 2^(m-6).
```

Its first boundary bit is already determined:

```text
Z_m = C-3^14 J_m+2^(m-6)J_m mod 2^(m-5).
```

Thus the chart gains one certified bit per scale, but remains strictly
same-scale.  Applying it to the four joint connector coefficients also proves
that at most one third-symbol lane can cancel three or more Newton-carry bits.
The result removes coefficient drift from the growing low window without
pretending to control the exponentially moving top-six room quotient.

## T-9826 -- canonical Pade ultrametric ladder

The arbitrary-minor sign theorem of `T-9821`, combined with the exact Cramer
column order, gives

```text
sgn(b_(n,k)) = (-1)^k.
```

Every bordered error determinant has the opposite size parity from its base
minor, so all real error coefficients at one order have sign `(-1)^n`.
There is therefore no archimedean cancellation in the evaluated real error.
The real and 2-adic limits are kept separate.

For the rational approximants `R_n=A_n(1)/B_n(1)`, write

```text
E_n = 6{2*zeta*n + 27*S*r*n(n-1)/2}.
```

Since `v_2(H_2-R_n)=E_n` and the radii strictly increase, the ultrametric
equality gives, for every `m>n`,

```text
v_2(R_m-R_n)=E_n.
```

Consequently all canonical projective pairs are pairwise nonproportional.
This discharges the auxiliary nonproportionality clause in `T-9821/(23)` for
the full sequence.  It does not supply the still-missing quadratic upper
bound for primitive global height.

## T-9827 -- maximal-run odd-carry zipper

For any binary chart

```text
U M_(n+1) = V M_n - (V-U) epsilon_n,
U=2^a < V,  V odd,
```

decompose the code into maximal runs with symbol `s_k`, length `ell_k`, and
`sigma_k=2s_k-1`.  Each run starts with one positive odd carry:

```text
M_(p_k) = s_k + U^(ell_k) q_k,
U^(ell_(k+1)) q_(k+1) = V^(ell_k) q_k + sigma_k.
```

The zipper transports exact precision at both kinds of places:

```text
v_2(V^(ell_k)q_k+sigma_k)=a*ell_(k+1),
v_p(U^(ell_(k+1))q_(k+1)-sigma_k)=ell_k*v_p(V)
```

for every `p|V` after the first run.  Conversely, every positive odd zipper
chain reconstructs the complete positive physical orbit.

Composing the run equations gives one nested initial-carry cylinder.  If
`S_N=ell_1+...+ell_N`, its canonical representative is

```text
R_N = -V^(-ell_0) sum_(j<N) sigma_j (U/V)^(S_j)
      mod U^(S_N).
```

The mixed-radix blocks `a_N` in

```text
R_(N+1)=R_N+a_N U^(S_N)
```

have an explicit one-step recurrence.  By `L-9801`, one ordinary positive
root realizes the entire infinite run schedule exactly when `a_N=0`
eventually.  This is the quotient/carry memory absent from phase-only
grammars: full finite-word realizability and one-root infinite coherence are
now separated by a concrete carry-block sequence.

For the physical `4 -> 5` chart the zipper specializes to

```text
4^(ell_(k+1))q_(k+1)=5^(ell_k)q_k+sigma_k,
v_2(...)=2*ell_(k+1),
v_5(4^(ell_(k+1))q_(k+1)-sigma_k)=ell_k.
```

## Review and exact boundaries

- Every claim has a direct proof from previously audited local identities.
- The cap proof uses only elementary two-adic LTE and retains the exact
  same-scale/no-transition boundary.
- The Pade proof keeps `H_infinity` and `H_2` separate and derives a height
  lower bound only; it makes no irrationality claim.
- The zipper records the possible initial odd-prime factor in `q_0`, requires
  odd carries to encode maximality, and uses stabilization as a criterion,
  not as a conclusion.  Its level-`N` cylinder enforces `N` divisibility
  conditions; level `N+1`, not level `N`, supplies the terminal carry parity.
- Redundant exact replay checked the cap endpoints through `m=24`, Pade signs
  and pairwise distances through order four, and the finite `4/5` terminal-
  parity edge `q_0=1` versus `q_0=5 mod4`.
- No theorem constructs or excludes a nontrivial Collatz orbit, proves the
  period-ten value irrational, or closes the cap stitch.

All claims remain `PROPOSED` pending external review.  No `K-####` candidate
is proposed.  The publication-gate memory snapshot was healthy at 9.36 GiB
free with 39.2% of physical memory in use.
