# Attempt to close the power-of-two section by its offset

Status: the full theorem is OPEN. The accompanying `BandOffset.lean` was
compiled successfully with Lean4.34.1 and warnings treated as errors. Its
11 printed theorem dependencies contain only `propext`, `Classical.choice`,
and `Quot.sound`; see `band-offset-build.json` for the actual command, source
hash, exit code, and axiom output. No convergence hypothesis is an axiom.

## Source and proposed recursion

The source is PR #173, full head
`fa0c9e2a2851e6324391e39c17afcb5913185aec`, specifically
`research/lean-shell-cover/ForwardSection.lean` and `SectionDynamics.lean`.
Its ordinary shortcut map is `T(n)=n/2` for even n and `(3n+1)/2` for odd n.
Every positive ordinary orbit visits an odd point

\[
n=2^d+a,\qquad d=\lfloor\log_2 n\rfloor,
\qquad (d+1)a\le70\,2^d.
\]

The tempting induction uses the smaller source `a` as a convergence witness.
Its complete low-bit prefix is shared with `n` for exactly `d` clocks. If `p_k`
counts odd inputs during the first `k` clocks of the source and `k≤d`, then

\[
T^k(n)=T^k(a)+3^{p_k}2^{d-k}.
\]

The root project's already proved finite affine identity gives
`2^k T^k(a)=3^{p_k}a+C_k`, with `C_k≥0`.

## Positive transfer proved by the new development

If `a>0` and `T^k(a)<a`, the affine identity forces `3^{p_k}<2^k`.
Consequently every lifted input `a+2^k v`, `v≥0`, descends at that same clock:

\[
T^k(a+2^k v)=T^k(a)+3^{p_k}v<a+2^k v.
\]

In particular, when `k≤d`, this transfers descent to `2^d+a`.
An actual supplied certificate `T^k(a)=1` with `a>1` provides the guard whenever
its clock fits inside the available `d` binary digits. The proof uses the
actual ordinary source and exact clock; it does not infer the clock from
basin membership or from the relative size of the offset.

## A uniform thin-band obstruction to the missing clock estimate

More generally let `b,h,u` be natural numbers with `u>0` and

\[
2^{b+h}\le3^b.
\]

For every ordinary clock `j≤b+h`,

\[
T^j(2^b u-1)\ge2^b u-1.
\]

The first `b` steps follow an exact all-odd prefix, with endpoint
`3^b u-1`. Every remaining step divides by at most two. Even an all-halving
suffix of length `h` therefore leaves the trajectory at or above its source.
The proof retains every intermediate clock, not only the last endpoint.

Take `b=4m`, `h=m` and `m≥1`. Define

\[
a_m=2^{4m}-1,\qquad n_m=2^{5m}+2^{4m}-1.
\]

The inequality `2^5<3^4` supplies the general guard. Choosing `u=1` proves
that `a_m` has no strict descent during its first `5m` clocks; choosing
`u=2^m+1` proves the same for `n_m`. The new file also proves:

* `floor(log2 n_m)=5m` exactly;
* `n_m` is odd and satisfies the source's exact marked inequality;
* `2^m (n_m−2^(floor(log2 n_m)))<2^(floor(log2 n_m))`.

Thus the relative width is smaller than `2^(−m)`, an exponentially smaller
fraction in the binary exponent than `70/(5m+1)`. A marked point's small
relative offset does not ensure that the offset descends before the shared
prefix expires. No member is claimed to be a Collatz counterexample.

The parametric lemma also covers `n=2^(qm)+2^(rm)−1` whenever `r<q` and
`2^q≤3^r`, using `b=rm`, `h=(q−r)m`. For any rational width exponent
`δ=(q−r)/q<1−log_3 2`, choices of this kind are available. For sufficiently
large `m` these inputs lie in the source's marked band, while retaining the
same obstruction through their full binary exponent. The arithmetic
no-descent statement is the general Lean theorem; this asymptotic choice of
parameters is explanatory reasoning, not an additional printed Lean theorem.

## Where the full closure attempt still fails

The positive lemma supplies an **ordinary** descent endpoint. It does not
assert that endpoint is marked. Even if every marked point had an ordinary
descent below itself, induction on marked points alone would not apply: the
lower endpoint may be unmarked and its next forced section visit may exceed
the original mark. The source PR's genuine equivalence requires eventual
strict descent **among marked returns**. Closing this route therefore also
requires control of the return overshoot, or a separate legitimate induction
that already supplies convergence of every smaller ordinary input.

Two distinct induction assumptions must not be conflated.

1. If the start itself is the global least hypothetical counterexample and is
   marked, then its positive offset is smaller and hence convergent. That
   gives a finite certificate of unspecified length. The available `d`-step
   coupling cannot consume a certificate that lasts longer than `d`.
2. Starting from the global least hypothetical counterexample and applying
   the forced-visit theorem can reach a much larger marked point. Its offset
   need not be smaller than the original least counterexample, so even the
   source convergence premise is then unavailable.

At the end of the shared prefix the unresolved pair is
`(T^d(a), T^d(a)+3^{p_d})`. The supplied certificate continues on the first
member, but the difference is odd, so the two parity histories separate.
The first missing global inference is a complete certificate transfer across
this ternary difference, or an actual well-founded multi-return recursion
that makes new smaller ordinary queries. No such transfer is assumed.

The source PR's result that first returns can expand arbitrarily rules out
using one-step ordinary size as that rank. The present argument also rules
out obtaining the necessary `d`-step offset guard solely from leading-bit
closeness, even for the much thinner explicit families above.
