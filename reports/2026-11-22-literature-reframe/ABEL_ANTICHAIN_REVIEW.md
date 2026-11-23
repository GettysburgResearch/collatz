# Independent written review of the Abel antichain bound

**Verdict: the displayed antichain inequalities and their stated scope
are valid.** This is a paper review, with no new Lean claim or full
Collatz conclusion.

Reviewed source:

- `research/literature-reframe-20261122/ABEL_ANTICHAIN.md`
- SHA256 `cdcc5d9c653705f5b81e97ea6d34169bf8bae5771479a27876441900f029a749`
- Imported construction: PR180
  `d0349de2108abb7c8fb8393c086610e3372df116`,
  [`GLOBAL_RENEWAL_ATTACK.md`, §8](https://github.com/GettysburgResearch/collatz/blob/d0349de2108abb7c8fb8393c086610e3372df116/research/lean-forward-band-20261121/GLOBAL_RENEWAL_ATTACK.md).

## Actual source counting

For every retained word, the positive affine identity gives
`omega_w/q <= 1/n_w`. The clock restriction `A(w)<=6s` gives
`n_w<=q(64/3)^s`. For a finite target set with maximum `Q`, all retained
sources through accelerated depth `S` consequently lie below `QR^S`,
where `R=64/3`.

The three injectivity claims in §2 are all necessary and correct. A
positive odd source determines its accelerated exponent word at a fixed
depth. Repeated hits at different depths would make the target itself
periodic, even if the original source were transient. Hits to two targets
on one deterministic trajectory would make them comparable. Thus a
nonperiodic, forward-incomparable target set counts each source at most
once across every retained target and depth. Empty words obey the same
argument. No unit restriction on the source is assumed accidentally.

It follows that the normalized retained total is bounded by the ordinary
harmonic sum at `floor(QR^S)`. The omitted clocks have total at most
`(64/17) sum_q 1/q`, because the geometric ratio is `64/81` and the
depth-zero omitted family is empty. This reconstructs exactly

\[
 B_S\le C_A+S\log R,
 \qquad C_A=1+\log Q+\frac{64}{17}\sum_{q\in A}\frac1q.
\]

## Abel factors and the simultaneous limit

For a nonnegative depth sequence, weighting its partial sums by
`(1-rho)^2 rho^S` gives `(1-rho) sum_s rho^s D_s`. The two elementary
geometric identities therefore give

\[
 \sum_{q\in A}\frac{F_\rho(q)}q
 \le (1-\rho)C_A+\rho\log R.
\]

The coefficient of the slope is `rho`, with no additional
`1-rho` factor. Each fixed finite target set may be passed to the limit
along the single simultaneously extracted sequence. Thus the same
function `F` satisfies the bound for every finite antichain. The
countable version follows by finite partial sums of nonnegative terms;
it does not exchange an infinite target sum with the Abel limit.

This upper packing calculation uses the actual inverse-word identities,
the clock-tail estimate, and the Abel limit construction. It does not
need (PDU) or the analytic positive atom floor. The separate assertion
that this particular envelope is uniformly positive on unit targets
retains the source qualification stated in the manuscript. An arbitrary
superharmonic function `PF<=F` is not substituted for the specifically
extracted function in this argument.

## Periodic extension

For an odd periodic target, subsequent accelerated hits are separated by
one full odd cycle, with multiplier
`lambda_q=3^(p_q) 2^(-E_q)<1`. A fixed source's total repeated-hit
weight is therefore at most `q/[n(1-lambda_q)]`. Multiplication by
`eta_q/q`, with `eta_q=1-lambda_q`, restores the bound `1/n`.

For an incomparable target family the source still belongs to at most
one target basin. Truncation only decreases its geometric total. The
omitted-clock contribution stays bounded because `0<eta_q<=1`.
The same Abel calculation proves (A8). This checks the periodic extension
without deleting the geometric cycle factor or counting repeated sources
as distinct.

## Boundary of the deduction

The edge inequality (A9) follows from one actual inverse term of `PF`.
If reciprocal occupation is summable, the infinite product is positive
because `log(1+1/(3q_i))<=1/(3q_i)`. The manuscript correctly identifies
that summability as a separate conditional consequence of (PDU), and
does not derive it from antichain packing alone.

Finally, (A10) follows by writing the positive integer `m(n)` as
`sum_(R=1)^X 1_{m(n)>=R}` for each source `n<=X`. It keeps the original
ordinary sources and all thresholds. A bound on one antichain does not
bound this sum over all thresholds. Comparable orbit states cannot all
be inserted into the antichain theorem.

The submitted statement is therefore a valid additional global constraint
on the chosen Abel envelope. It supplies no uniform sublinearity,
ordinary first-moment estimate, or exclusion of all escaping rays.
