# Review of the finite-row source cutoff

**VERIFIED** for the exact source cutoff, its forward-enumeration use, and the row quantifiers in `research/killed-green-head-closure-20261124/FINITE_CLOSURE.md`, SHA-256 `52e1b8f33330a28bd13d0b25659af894ac7a4eac401dce54ae2d8c3313259bdb`, a continuation of PR 201 at `73a145ca99448a78219bd149e273f33b6e3fda4b`.

On an actual word with b odd inputs and total 2b the identity is q=(3/4)^b x+β. For 0<ε<1, β≥εq gives ε(3/4)^b x≤(1−ε)β. Each gap g≥1 updates the offset by β↦(3β+1)/2^g, so from β=0 its largest possible value is bounded by (3/2)^b−1. Multiplication by the positive factor (4/3)^b(1−ε)/ε gives

    x ≤ ((1−ε)/ε)(2^b−(4/3)^b) < ((1−ε)/ε)2^b.

The first cutoff can be rounded down for enumerating positive integer sources. Forward evaluation at exactly 2b steps tests the odd count on the inputs at clocks 0 through 2b−1. The endpoint at clock 2b must be an odd unit exceeding one; repetition is tested on the states at clocks 0 through 2b inclusive. Because the start and endpoint are odd, the terminal is the endpoint of exactly b complete odd gaps whenever the odd count equals b. Binning each surviving source by its actual q therefore computes the same maximum as the inverse definition. As a nonempty finite check, at b=1, ε=1/53 the cutoff is 34 and the complete forward scan gives the sole pair (x,q)=(17,13).

The overview correctly permits q to depend on b for the full-conjecture lower bound and keeps one q for all sources counted in a row. It distinguishes exact finite evaluation from the missing cofinal upper bound for each fixed ε. The larger lower bound uses a finite forward test with h(b) tending to infinity. The separate fixed-terminal periodicity statement applies to ordinary units q>1. This review adds no independent verification of the imported directed-cut estimates or the Lean execution record.
