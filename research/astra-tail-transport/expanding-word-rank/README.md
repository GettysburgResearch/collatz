# Beyond a fixed dictionary: an expanding-word rank

**PROPOSED pending independent mathematical review. No complete Collatz proof.**
This is a research continuation of PR105 at
`73572fddd9b8b3cbd8fc03c3a992eb0735d0f62c`, not a Reviewer D verdict or a
canonical-status change. Read [PROOF.md](PROOF.md) for every hypothesis.

## The attempted closing step

The preceding packet bounds the surviving mass by a positive remainder for
all future time. Making that remainder vanish still needs an all-source
argument. This continuation tries physical induction instead of extending
the finite clearance census: represent every sufficiently expanding periodic
parity pattern in one computable integer rank, then select a legal pattern
that decreases it.

The rank construction and important infinite families succeed. **Universal
activation does not:** a globally minimizing pattern can be physically
illegal, and the actual exit can increase the new rank without bound. The
failed step is proved false rather than deferred to an unexplained lemma.

## What is established in the manuscript

For a parity word w of length L and q odd steps, write

    T_w(n)=(3^q n+A_w)/2^L,  Z_w(n)=(3^q-2^L)n+A_w,
    g(z)=z^2/3^v3(z), g(0)=0.

The new rank is

    rho(1)=0,
    rho(n)=min(g(n),g(n-1),g(n+5),g(Z_w(n)) over ALL w with 4*3^q>=5*2^L.

The fixed expansion gap 5/4 is essential to the present construction. Every
strictly expanding periodic pattern has a repetition in this dictionary;
not every primitive expanding word is itself included. All forms are unreduced.

| Claim | Result | Limit |
|---|---|---|
| ATT-201 | `n-1<=rho(n)<=R_*(n)<=n^2`; exact minimization is finite, with word length `n*2^L<4M` for any candidate upper bound M. | Not polynomial in source bit length; no physical legality follows from minimization. |
| ATT-202 | `N_rho(X)<250X^(39/40)`, `sum 1/rho<=10000`, `sum 1/rho^2<2`. | Not a sharp spectrum or transported-envelope theorem. |
| ATT-203 | A legal minimizing word gives strict decrease of the SAME rho; all ties are tested. | The total partial selector can return UNRESOLVED. |
| ATT-204 | Exact all-word minima and per-shortcut contraction across arbitrarily long old unsafe `111010` phases. | Explicit high-precision family, not every source or every unsafe path. |
| ATT-205 | An exact exit family has `rho(T(s))/rho(s)>=2^h/4352`; the minimizing word is illegal. | Refutes universal activation and one-step monotonicity, not the valid local certificates. |
| ATT-206 | For every finite K there are ordinary sources whose next K ranks all exceed 16 times the starting rank. | Sources vary with K; not an infinite all-odd orbit or an all-diagram clock lower bound. |

The old R_* rank, its quarter-unsafe operator H, and its weight `1_U/R_*^2`
remain distinct. The parent numerical mass ceiling is NOT inherited by
`1/rho^2`. The larger dictionary buys new descent certificates at the cost of
a weaker proved counting exponent than R_*'s square-root bound.

## A concrete unbounded improvement

For every K>=1 and every e satisfying

    e>=max(13,6K+12), e+4K=5 mod16,
    n=(3^e*64^K-73)/17, s=(3^(e+4K)-73)/17,

the actual path is `T^(6K)(n)=s`, with parity `(111010)^K`, and

    rho(s)/rho(n)=(81/4096)^K.

At every individual step inside this path the new rank is multiplied by
`3/4` on an odd step and `1/4` on an even step. Meanwhile all 2K old A-source
states are quarter-unsafe and the old rank grows by more than `(81/64)^(2K)`.
The global-minimum proof handles EVERY word in the infinite dictionary.
It does not rely on extrapolating a truncated dictionary computation.

At the exit s, however, the unique minimizing pattern begins with 1 while s
is even. With h=e+4K, its actual successor s/2 has a rank ratio at least
`2^h/4352`. Thus the arithmetic difficulty has not vanished: the proof has
isolated it at a precisely controlled phase exit.

## Evidence and review

The two finite implementations reconstruct the same complete payload. Among
4,095 inputs, 1,639 pass the legal-minimizer certificate and 2,456 are explicitly
UNRESOLVED under that rule. These are not convergence success/failure counts.
The family protocol checks 24 sources and 672 physical positions; 60 positions
receive exhaustive all-word evaluation, while larger cases check the written
theorem's premises and literal trajectories. These evidence levels differ.

[Experiment and replay](../../../experiments/X-ATT-003-expanding-word-rank/README.md)
records the 12 resealed tamper controls, independent implementation methods,
and exact digest. Both programs have the same author: they do not constitute
independent mathematical peer review. [Sources and scope](SOURCES_AND_STATUS.md)
fix the earlier dependencies and explicitly unreviewed material.

## The full-proof boundary

A proved total successful selector on the residual sources, allowing finite
unequal-clock physical merging to lower rho, would finish the induction and
exclude both divergent trajectories and nontrivial positive cycles. No such
coverage or termination theorem is established here. An inverse-only search
also fails on positive multiples of three. A general two-sided selector is
not refuted by the forward-only delay theorem.

Do not send this as a complete proof with only routine checking left. Send it
as a new rank construction, its exact positive families, the failed closing
assertion, and a precisely identified remaining all-source obligation.
