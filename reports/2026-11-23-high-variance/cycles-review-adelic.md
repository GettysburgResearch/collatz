# Independent review of the adelic lane

Reviewer: `nov23_cycle_ideal`, 23 November 2026.

Reviewed source:
`research/high-variance-20261123/adelic/TWO_PLACE_AND_RENEWAL_ATTEMPT.md`
at SHA256
`eb8983e9d61503e7941eece1d5857a829260160f2afb683a678a0666336dddb3`.

**Result: equations (7), (8), (13), and (16) pass the algebraic review.**
The argument is conditional on its explicitly named retained-orbit and
source-qualified analytic inputs. This review does not verify the
analytic proof of an external manuscript, infer algebraicity of the
real limit, or certify an escaping-orbit exclusion.

## Exact product and fixed-block tail

For the primitive integer vector `(C_j,3^j)`, the real `Y` factor is
`3^j` and its ternary factor is `3^(-j)`. The ternary `X` factor is one
because the final term of `C_j` is a power of two and all earlier terms
are divisible by three. At two, the `Y` factor is one, and the affine
identity gives `|C_j+p3^j|_2=2^(-A_j)` because `q_j` is odd. Therefore
the complete unnormalized product of the six displayed forms is exactly

    |C_j - L 3^j| * 2^(-A_j).

The real series has a positive tail. Expanding that tail gives exactly

    Σ_(k≥0) 2^(A_(j+k)-A_j) / 3^(k+1),

whose first term is `1/3`. No inequality reverses and no local factor
is omitted. Because the vector is primitive, its finite local maximum
norms are one, so the unnormalized `H^(-epsilon)` formulation stated
for the proposed Subspace Theorem application has the right height
normalization. Subtracting a fixed `s` terms leaves the first positive
term at index `j+s`, at least `2^s/3^(s+1)` after the same normalization.
These are (7) and (8). They concern the displayed approximation scheme,
not every possible higher-dimensional application.

## Shell Hölder rearrangement

For fixed finite `r≥1`, the depth-`m` cylinder has Haar measure `3^(-m)`.
Its Hölder factor is `3^(-m(1-1/r))`. Divide the displayed lower/upper
comparison by `q^(1-2/r)3^(-m)` to obtain

    q^(2/r) ≤ C_(r,p) [log(e q)]^((r-1)/r) 3^(m/r).

Raising this to the fixed power `r` and absorbing the constant yields
exactly (13). The `r=1` endpoint is valid. No constant uniform in `r`
is available from the stated premise, so the text correctly does not
let `r` grow. With `m=j+O_p(1)`, the elementary `(3/2)^j` upper bound
has square scale `(9/4)^j`, below `3^j`, as claimed.

## All-ones joint control

The probability of the first `k` gaps all being one is `2^(-k)`. On
that event the geometric sum gives `B_k=(3/2)^k-1=b_k` and the
multiplier is `a_k=(3/2)^k`. In the ternary integers, the multiplier
is divisible by `3^k`, so the entire continued limit is `-1 mod 3^k`.
The independent real tail has a fixed positive chance of lying in
`(0,1/3]`: condition another finite positive limit on a bounded set of
positive probability and choose one sufficiently large first gap.

If `0<R'≤1/3`, then `R>b_k` and

    R ≤ (4/3)a_k - 1 ≤ 2a_k - 2 = 2b_k,

where the second inequality follows from `a_k≥3/2`. Multiplication
of the event probability `c_0 2^(-k)` by `3^k` proves (16) for every
`k≥1`. This is a genuinely joint real/ternary event, not a comparison
of unrelated marginal bounds.

For the essential-supremum consequence (17), the stated density theorem
has the hypothesis `B≥1`. Since `b_1=1/2` and `b_k≥1` for `k≥2`,
invoke that density theorem only for `k≥2`. The probability statement
(16) remains valid for all `k≥1`. This small index restriction leaves
the asymptotic obstruction unchanged. Root applied it explicitly before
(17). The reviewer confirmed that this was the only source change from
the originally reviewed SHA256
`39f37a71310e594f8d83eb259badd5327f5ee649d6524aaff0170f374dcc3bbd` by reversing the exact edit and
matching that previous hash; the current reviewed hash appears above.

The least positive integer in the cylinder is `3^k-1`; divided by
`b_k`, it tends to infinity. Thus the all-ones control does not refute
the separate positive ordinary diagonal estimate. The reviewed text
preserves that distinction.
