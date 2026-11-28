# The newer fourth-power Fourier evaluator and the Collatz selector

Date: 2026-11-28. **Additional primary-source inspection.** This note
updates the factoring comparison at PR 365 checkpoint 004. It does not
replace the earlier, separately pinned isotropic evaluator audit.

The complete primary manuscript inspected is
[Arbitrary-corank Fourier simulation at fourth-power conductor](https://github.com/gfreund123/factoring-in-p/blob/c9034e4b6a814f624ae38a976ff49ada333158d3/research/astra-load-bearing-2026-11-28/transforms/notes/arbitrary-corank-fourier.md),
at head `c9034e4b6a814f624ae38a976ff49ada333158d3`, blob
`fff6d5706f87dbe36fc89c248fb12791796d6093`. The
[source intake](CHECKPOINT004_SOURCE_INTAKE.json) records the exact scope.
No external sampler or its finite replay was run in this Collatz pass.

## 1. What the new result actually supplies

For an odd squarefree `N`, the conductor is `Q=N^4`. On a supplied
coherent source disk with Jacobian corank `r` at a prime `p|N`, a mixed
coordinate chart reduces the remaining interference to a joint cubic
Fourier transform on `F_p^r`. Its certified tensor FFT costs
`p^r poly(n,log Q,circuit size)`, including the precision needed for an
exact sample. This is a substantive improvement over enumerating each
frequency separately at cost `p^(2r)`.

The ordinary graph-readout construction introduces `2n−1` uniformly
distributed Fourier labels. They supply a random symmetric Hankel
matrix `A`. For any fixed Hessian `H`, the exact identity

\[
\mathbb E_A p^{\dim\ker(H+A)}=2-p^{-n}
\tag{1}
\]

pays for all coranks. The full experiment includes arbitrary coupled
arithmetic-circuit phases and has an expected-polynomial exact sampler
under its stated `gcd(N,φ(N))=1` promise. The expectation is over the
actual retained graph labels and source disks. It is not a bound for
each prescribed label.

## 2. The two missing interfaces are still explicit

The Collatz one-copy event in
[CRITICAL_GRADE_TAIL.md](../arithmetic/CRITICAL_GRADE_TAIL.md)
retains the full conductor `3^a` of the actual grade, a same-path real
interval, and a grade cutoff. At a critical clock the grade tends to
infinity. The new theorem's local calculation is explicitly at `p^4`.
Setting `p=3` gives modulus 81; setting `N=3^m` to imitate a larger
ternary conductor violates its squarefree hypothesis. The theorem does
not assert the corresponding bounded-degree local reduction at
arbitrary `3^a`. Encoding higher digits in extra registers is a
possible different construction, whose complete consumer would still
need to be proved.

The graph labels also add a genuine quadratic phase. Setting all of
them to zero removes that perturbation, but the exact probability of
this specified event is

\[
Q^{-(2n-1)}.
\tag{2}
\]

For `N=3` this is `81^{-(2n−1)}`. Rejection conditioning on this event
therefore has exponential expected cost in growing `n`. Nor does (1)
become a conditional corank bound at that one matrix: for example,
`H=0,A=0` has `p^r=p^n`. These facts concern the direct specialization
of the supplied sampler, not all possible uses of its retained labels
or all encodings of the Collatz problem.

In particular, expected sampling of the joint experiment does not by
itself evaluate the prescribed full-conductor real/ternary event with
relative precision `o(X/2^h)`. The source itself distinguishes its
sampler from an externally requested strong singular transform.

## 3. An exact Boolean-path check on averaging the extra graph labels

There is a simple path-specific reason not to erase those labels by
unweighted averaging. Let `p` be odd, and for a Boolean word
`b=(b_0,…,b_(n−1))` define the Hankel graph coordinates

\[
G_k(b)=\frac12\sum_{i+j=k}b_i b_j\in\mathbb F_p,
\qquad 0\le k\le2n-2.
\tag{3}
\]

**Lemma.** The map `b↦G(b)` is injective on `{0,1}^n`.

**Proof.** Write `B(t)=Σ_i b_i t^i` and similarly `C(t)` over
`F_p[t]`. Equality of (3) gives `B(t)^2=C(t)^2`. Since this polynomial
ring is an integral domain, `B=C` or `B=−C`. The first case gives
`b=c`. In the second case, a nonzero Boolean coefficient of `C` would
force a coefficient `−1` of `B`, which is neither 0 nor 1 because `p`
is odd. Thus both words are zero, again giving equality. ∎

Consequently, for arbitrary complex path amplitudes `w_b`, a uniform
label `ℓ∈F_p^(2n−1)` satisfies the exact orthogonality identity

\[
\mathbb E_\ell\left|
\sum_{b\in\{0,1\}^n}w_b\,e_p(\ell\cdot G(b))
\right|^2
=\sum_b|w_b|^2.
\tag{4}
\]

All cross-word interference disappears. Thus this particular
unweighted averaging operation retains only the diagonal mass of a
Boolean-path superposition. It cannot substitute for a prescribed
unmasked transform by simply appealing to the average cost (1).
Equation (4) does not rule out a new estimator that uses the labels
with appropriate weights; such an estimator must supply its own
unbiased identity and variance bound at the required rare-event scale.

## 4. Result of this additional import attempt

The fourth-power tensor evaluator is an actual new operation, and the
Hankel moment is a rigorous way to amortize growing corank without an
exponential prefactor. The current Collatz consumer has neither the
required arbitrary-conductor extension nor an efficient removal or
use of the random quadratic graph phase. This additional inspection
therefore supplies no new critical one-copy lower bound. The positive
evaluation obtained in this pass remains the moving precritical
relative law in
[PRECRITICAL_STATIONARY_EVALUATION.md](PRECRITICAL_STATIONARY_EVALUATION.md),
with its exact boundary at the postminimum critical region.

The checkpoint's separate compact Pell-power Dedekind item is indexed
as a reduction to a scalar whose polynomial-time evaluator remains
open. Its full manuscript was not inspected for this note, and no
Collatz implication is imported from that index entry.
