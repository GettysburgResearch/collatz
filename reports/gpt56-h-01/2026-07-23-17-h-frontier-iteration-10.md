# Session report: H frontier iteration 10

**Agent:** `gpt56-h-01`  
**Issue:** #17  
**PR:** #19  
**Status:** new proposed lemmas; no counterexample and no termination proof

## Other work reviewed

This iteration inspected the current global counterexample map in PR #38, the
width-one one-counter construction in PR #49, the H Evertse / renewal transfer
and complexity files in PR #34, and the rational-target/product-formula audit
in PR #13.

The useful transfer was methodological rather than a counterexample import:

- PR #49 shows that a constructive proof needs one finite ordinary state plus
  an all-time definedness invariant, not only an inverse-limit completion.
- PR #34 provides the exact rank bookkeeping needed to make qualitative fresh
  primes quantitative.
- The plastic ordinary-survivor count turns a macro multiplier bound into a
  direct obstruction to one marked ordinary orbit.

## New results

### 1. Polynomial macro-growth barrier (`L-9526`)

For an actual orbit sampled at boundaries of a finite macro family, suppose all
suffix multiplier products satisfy

\[
 A_{j,k}\le C(1+k-j)^\gamma.
\]

The affine toll formula gives sampled states of size `O(k^(gamma+1))`.  Since
they are distinct infinite survivors and the complete survivor set has count
`O(X^sigma)`, `sigma=log_2(rho)`, necessarily

\[
 \gamma\ge1/\sigma-1=1.464965255\ldots .
\]

A finite directed macro grammar whose every directed cycle has multiplier
product at most one has `gamma=0` and is therefore impossible for a
nonperiodic positive orbit.  Thus a physical finite-macro construction must
exploit positive multiplier cycles at a quantitatively nonpolynomial rate.

### 2. Quantitative renewal-prime budget (`T-9516`)

For `N` interior renewals, let `s_N` count all distinct primes at least five in
the adjacent bridge cores.  The exact equation

\[
 -4^bY+3^a(9/8)^RX+(9/8)^R=1
\]

is a nondegenerate three-term S-unit equation in a subgroup of rank at most
`2s_N+3`.  The explicit Evertse--Schlickewei--Schmidt bound gives

\[
 N\le\exp(18^9(2s_N+4)).
\]

Hence `s_N` has an explicit logarithmic lower bound.  The constant is far too
large for direct computation, but this upgrades qualitative infinite prime
support to a proof-producing rate statement.

### 3. Sharp survivor deficit pressure (`T-9517`)

For a hypothetical nonperiodic survivor, define

\[
 c=\log_8 9,
 \quad
 s_n=\lceil cr_n\rceil-r_{n+1}=d_n-o_n,
 \quad
 \theta_n=\lceil cr_n\rceil-cr_n,
\]

and

\[
 \beta_n=\log_8\left(1+\frac1{p_{n+1}-1}\right).
\]

The Toll--Euler identity makes `sum beta_n` finite.  The exact core recurrence
then yields

\[
 D_N-O_N-\Theta_N
 =N\log_8(4/3)+h_N-h_0-B_N.
\]

Consequently

\[
 \liminf D_N/N\ge\log_8(4/3)=0.138345833\ldots .
\]

This improves the finite-chain baseline `log_8(49/37)` to the exact critical
constant on a genuine nonperiodic survivor.  It also gives the exact identity

\[
 D_N-O_N-\Theta_N-N\log_8(4/3)
 =(c-1)K_N+r_0-r_N.
\]

For letters bounded by `R`, positive rounded deficits have lower density at
least `log_8(4/3)/ceil(cR)`.

## Counterexample consequences

The repository's finite compiler and one-counter ideas cannot be imported by
analogy alone.  An H construction now has to provide all of:

1. a physical macro path with suffix multiplier growth beyond the threshold
   of `L-9526`, or an explicitly unbounded macro state;
2. the exact critical rounded-deficit burden of `T-9517`;
3. the quantitative distinct-prime burden of `T-9516`;
4. one positive ordinary initialization whose extension carries eventually
   vanish;
5. an induction proving exact legality and nontermination forever.

The new work does not close this interface.  It does rule out every neutral or
polynomial-growth finite macro grammar, including any attempted repair of the
closed `10/30` compiler that retains only nonpositive multiplier cycles.

## Files

- `research/h-frontier/claims/ITERATION_10.md`
- this report
- updated `research/h-frontier/CLAIM_INVENTORY.md`

No finite computation was required for the three new claims.  The external
constant in `T-9516` remains source-dependent and should receive an independent
rank/convention audit before promotion.
