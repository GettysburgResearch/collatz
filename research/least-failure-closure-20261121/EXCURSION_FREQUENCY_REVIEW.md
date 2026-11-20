# Independent review of the excursion-frequency argument

**Disposition: no mathematical gap found in EF1--EF4 at the hashes below.**
This is a written proof review, with source inspection of the finite checker.
It is not a machine-checked proof or a claim to have independently proved
Evertse's external theorem.

## Frozen scope

- `EXCURSION_FREQUENCY.md`:
  `3e9bdc1962a449f95263adaf4745b2aa95228d5807cab479747e7eaa6fc889d1`.
- `check_excursion_frequency.py`:
  `7d3b811f6f2a30e67f437747f31b8cc11d6cf51dd2cb95a34f480ff716bb4c49`.
- The RU2 interface was checked against `MULTISTEP_CORE_RETURNS.md`,
  `a1f939725bb3ffc333255fb57cafa8e95ed8dace8155650b5a608ef34ba20d5b`.
- The elementary cycle input was reread at PR161 commit
  `4a0536b587fc91ee0c7bb1b160c06dda16ddbf23`, file
  `research/source-rigidity-20261120/SHIFTED_SMOOTH_CYCLES.md`, SS1--SS2.

The stated meaning of nonperiodic is “not eventually periodic.” This
ensures every prefix is simple, including when the deterministic orbit
could otherwise have a transient before a repeated cycle.

## Endpoint and counting audit

Inside blocks are counted as blocks of vertices. A block of vertex length
`ell` contains `ell-1` internal valuation-one edges. A gap between two
successive blocks with `g` outside vertices has `g+1` edges. In particular,
an internal defect joining two inside vertices is a gap with `g=0`,
covered by the `r=1` term of `M_H`.

Every such gap has at least one defect: either the blocks were split at
that defect, or the gap crosses the boundary of the fixed core family.
Valuation-one edges preserve the core because both 2 and 3 belong to the
prime pool. Its endpoint cores belong to the fixed finite set `Q`, so RU2
applies to one of `K^2` fixed ordered pairs. Simplicity makes gap starting
states distinct. Counting occurrences as distinct S-unit solutions is
therefore justified.

The outside interiors of separate gaps are disjoint. Initial and final
outside remainders can only increase `C_N`. Consequently the incidence
bound

\[
B\le1+M_H+\lfloor C_N/(H+1)\rfloor
\]

also covers empty inside families within a particular prefix and
truncation at either endpoint.

## Run-clock audit

The shifted recurrence gives `m_{j+1} <= (3/2)m_j` for every actual odd
transition. A valuation-one edge occurs exactly when `v_2(m_j)>=2` and
reduces that valuation by one. Thus a block starting at time `t` has at
most `v_2(m_t)` vertices, not one more than this number. The growth bound
then gives `ell <= h_0 + (alpha-1)t`.

Processing an inside block sends the consumed-vertex clock to at most
`alpha*t+h_0`. Processing an outside vertex adds one. Moving an outside
increment before a block increases this upper envelope, giving exactly

\[
N+1+h\le\alpha^B(C_N+h),\qquad
h=h_0/(\alpha-1).
\]

This establishes EF1 without deleting any finite tail. The integer
conservative clock used in the checker follows by replacing
`alpha-1 < 1` and `h_0 <= ceil(h_0)` in the block-length estimate.

## Asymptotic and constant audit

For fixed `H`, the finite `M_H` disappears after division by `log N`.
A subsequence with bounded `C_N/log N` makes
`log((N+1+h)/(C_N+h))/log N` tend to one. Letting the independently fixed
integer `H` be arbitrarily large proves EF2. No interchange of a
source-dependent finite exception set with a changing prime pool is used.

For EF3, with `m=H+3>=3`, monotonicity of the RU2 bound gives

\[
\log M_H\le2\log K+\log(H+1)
 +(s+1)m^3(35\log2+2\log m).
\]

The exact inequality `2^35 < 3^23`, together with
`log(H+1) <= log m <= (s+1)m^3 log m`, yields the displayed coefficient
`26(s+1)`. If `L=log(N+1)` and `A=log L`, the chosen integer

\[
m=\left\lfloor[A/(104(s+1)\log A)]^{1/3}\right\rfloor
\]

eventually satisfies `m>=3`, `log m<=log A`, and hence
`M_H<=K^2 L^{1/4}=o(L)`. The floor has no effect on the limiting ratio
because `m` tends to infinity.

The split at `C_N=sqrt(N+1)` is sufficient: above it, `C_N/F(N)` tends
to infinity; below it, the logarithm in EF1 is at least
`(1/2+o(1))L`. Thus the claimed conservative constant is

\[
c_s=\frac{1}{2\log\alpha\,[104(s+1)]^{1/3}}.
\]

The fixed set `Q` contributes only the constant `K^2`, and the fixed
source contributes only `h`. Neither changes this limiting coefficient.
Arbitrary fixed finite `Q` therefore requires no additional arithmetic
classification beyond RU2.

## Cycle corollary and remaining boundary

EF4 correctly separates eventual cycles from orbits with no repeated
state. For the pool `{2,3}` and `Q={1}`, PR161 SS2 excludes a nontrivial
cycle lying wholly in the class. Its proof uses a strictly increasing
boundary index above 15 and the complete finite complement below 16;
it does not invoke PR161's separate external S-unit corollary.

Every other positive cycle has at least one outside vertex, making
`C_N` linear after the transient. Combining this with EF3 proves the
strict sufficient convergence condition in EF4. The strict inequality
cannot be weakened to equality by this argument.

The proof supplies a necessary lower growth rate for counterexamples.
It supplies no incompatible upper bound for arbitrary ordinary sources,
and neither the prime pool nor the finite core set may be allowed to
grow with `N` while retaining the stated theorem. The final open
inference is stated accurately.
