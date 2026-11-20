# Independent narrow review of the depth-two directed family

**Verdict: VERIFIED for D2-1--D2-4 at the frozen hashes below.** This is an
independent AI proof reconstruction and code inspection, not a formal build or
external referee acceptance. No mathematical correction was needed.

| Reviewed object | SHA-256 |
|---|---|
| `DIRECTED_DEPTH_TWO.md` | `e5ab15633eaa903754f8a905187f5f142885678e41bee9c35fb36eeb3ea14c2c` |
| `check_directed_depth.py` | `13af137eb303778a9e5931b480cf476550c42b056adffb3d8d673d901326a0e3` |
| Root's `review_directed_depth_independent.py` | `6c6fe8450b826cebf11d3ffa13f84bf4d8da7f24e4689c45d87c7c2da53a910e` |

## Attribution-only revision reviewed

The mathematical reconstruction first covered note hash
`5a972cb232126f057e5bcc3cf6ec4ee0abea8572af45d0576ac04859623c86de`.
I then inspected the complete diff to the hash in the table. Its only changes
are a source-refresh attribution paragraph and replacing the introductory
“Let” with “Define”; D2-1--D2-4 and their proofs are byte-for-byte unchanged.
I read the relevant sections of refreshed PR146 at
`e238c63a5d57f96bb063b7472498d1977df51951`, including
`WITNESS_TRANSFER.md`, `BASIN_PHASE.md`, and `BOUNDED_RANK_TRANSFER.md`.
They do contain the overlapping depth-two family/reduction and the broader
lifted-certificate restrictions named in the new preface. The attribution is
accurate. This source inspection is not a new proof review of those entire
external files. The verdict above covers the attribution-only revision with
unchanged mathematics.

## Complete classification and first hitting

For `n=1 mod16`, `v2(3n+1)=2` exactly. Put `u=(3n+1)/4`.
If `U(u)=1`, write `3u+1=2^b`; then

\[
n=(2^{b+2}-7)/9.
\]

The exact order six of `2 mod9` gives `b=2 mod6`. The choice `b=2` is
`n=u=1`, whose **first** odd hitting depth is zero, and is correctly excluded.
Every remaining choice is `b=6m+2`, `m>=1`, producing the stated family with
`n>1` and `u>1`. The shortcut first hitting time is the sum of the two exact
division exponents, `2+(6m+2)=6m+4`.

The four displayed iterates of `z=2n-1` have parities odd, even, odd, even and
end at `2^(6m+1)-1`. All fractions are integers because `B=64^m` is `1 mod9`
and a positive power of two. Thus the restricted convergence statement is
exactly the stated Mersenne family; neither direction assumes unknown
convergence of its members.

## Complete source orbit and target separation

The known source follows

\[
n,\ (8B-2)/3,\ (4B-1)/3,\ 2B,
\]

then only halves to `1` and repeats `1,2`. Its entire forward orbit, including
arbitrarily late clocks, is bounded by `H=(8B-2)/3`. For `B>=64`, the second
listed value exceeds the other three and the eventual cycle values.

The tripled target's first four transitions and its subsequent formula

\[
T^{4+\ell}(3n)=3^{\ell+1}2^{6m-\ell}-1,
\qquad0\le\ell\le6m,
\]

are correct. Every input with `ell<6m` is odd, and these values increase.
The complete asserted target prefix is at least `3B-1`, which exceeds `H` by
`(B-1)/3`. Consequently the no-merger quantifiers are genuinely independent:
**every** good-arm clock `i>=0` is excluded against **every** target clock
`0<=j<=6m+4`. No claim about the target after that prefix is inferred.

## Odd clocks and the final division

The first target odd-event exponents are `1` and `3`. Thereafter the inputs
with `ell=0,...,6m-2` have division exponent one. At `ell=6m-1`, the odd
state is `2*3^(6m)-1`, and its raw numerator is

\[
3(2\,3^{6m}-1)+1=2(3^{6m+1}-1).
\]

Since `6m+1` is odd, `v2(3^(6m+1)-1)=1`; the **raw** numerator therefore
has valuation two. Hence

\[
U^{6m+2}(3n)=(3^{6m+1}-1)/2>1.
\]

All states through that odd clock exceed one, giving first odd hitting depth
at least `6m+3`, if finite. There is no off-by-one substitution between the
shortcut clock and the odd-event clock.

The unrestricted merger-clock obstruction also follows in odd time: already
the odd states through clock `6m+1` lie in the separated shortcut prefix.
The root's independent checker verifies the still stronger separation at
clock `6m+2`. That stronger comparison is valid too, since

\[
(3^{6m+1}-1)/2>H
\iff3^{6m+2}+1>2^{6m+4},
\]

and the latter holds at `m=1` and its main-term ratio increases by `729/64`
with each increment of `m`.

## Code inspection and execution boundary

I inspected both checkers without importing either. The author checker
properly rejects the depth-zero root in its converse enumeration and checks
the last odd transition with division exponent two. Its known-orbit set
contains the whole tail and cycle needed by the independent-clock comparison.

The root checker uses literal shortcut and odd iterations, reconstructs first
hitting by stopping at `1`, and correctly includes the terminal indices in its
separation loops. Both target loops compute one additional literal transition
after checking their last asserted state; their edge totals count those
executed transitions. They do not claim separation at that additional output.
The root checker's stronger last odd-state inequality was reconstructed above.

I did not rerun either checker during this review; execution belongs to the
separate root/author receipts. My completed actions were reading the full
note and both implementations, reconstructing the algebra and quantifiers,
and computing the three file hashes. No full-repository check or external
formalization is covered by this verdict.

The result obstructs a bound depending only on the good arm's **odd-event**
first hitting depth. Its ordinary shortcut hitting time grows with `m`, so it
is not an obstruction to every bound involving that other clock or the source
height. It does not prove universal convergence of the residual Mersenne
family, and the alternative stabilized-label rigidity problem remains OPEN.
