# Every positive real exponent has a natural boundary

**Proposed theorem.** Give any nonempty union of ordinary components disjoint from 1 the weights in [ORDINARY_SPECTRUM.md](ORDINARY_SPECTRUM.md), and put zero elsewhere. For every real `s>0` the power series

\[
   M_s(z)=\sum_{a(n)>0}a(n)^{s/2}z^n
\]

has the full unit circle as a natural boundary. The same conclusion holds unconditionally for the explicitly forced series on the actual predecessor tree of 5 in [FIVE_SOURCE.md](FIVE_SOURCE.md). This removes the exceptional exponents in the more general support argument by using long intervals in particular ordinary basins.

## The ordinary input

For every positive `m` and every positive `v` coprime to 3 there are arbitrarily large intervals of `m` consecutive ordinary positive integers whose trajectories all reach `v`. This qualitative predecessor-block result is from PR146 `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/AFFINE_RAYS.md`, sections “Classification and a constructive bound” and “Prescribing which component contains the pattern”, with the elementary reduction in `PREFIX_COMPRESSION.md`. We give the needed special case explicitly. No quantitative synchronization estimate is needed.

At any fixed depth after restricting the input to `x=r+2^h t`, each one of the ordinary arms `x+i` is an affine form `3^p t+y` at time `h`. The slope follows by iterating the known parities on this residue. The intercept is integral. Compare any pair of such forms, orienting it as `(X,3^j X+D)` with `j≥0` and integral `D`. The free-parameter slope in `X` is odd. Thus any parity bit of `X` can be prescribed by restricting the parameter by one binary digit. After a shortcut step, the base of the reoriented pair again has odd free-parameter slope after the new digit is removed.

At level `j>0`, an even nonzero offset can be repeatedly halved by prescribing an even base until the offset becomes odd. If the offset is zero, prescribing an odd base first makes it `(1-3^j)/2≠0`. At an odd offset prescribe an odd base. The first arm then has odd input and the second even, so the new level is `j-1` and the offset is `(D-3^(j-1))/2`. This returns the pair to level zero in finitely many steps, with some integral offset.

At level zero a nonzero even offset halves under an even base. For an odd offset choose the parity of the base, swapping the arms after the step if necessary, so the new level-one offset `E` is the even one of `(1+3D)/2` and `(1-3D)/2`. These are consecutive parity classes since their difference is odd; neither is zero. Divide `E` by its full power of 2 using even bases, obtaining its odd part `e`. An odd-base step returns to level zero with offset `(e-1)/2`. For `|D|≥3` the new absolute offset is at most `(3|D|+5)/8<|D|`. For `D=±1` the even choice is 2 and the same operation gives zero. This finite algorithm ties the two entire affine forms. Sequentially tie each further arm to the first by refining the binary class; identities already achieved persist because both arms follow the same map. At some final depth `h` all `m` arms have the same endpoint `z+3^p t` on the whole remaining class.

Choose arbitrarily large `e≥1` satisfying `2^e v ≡3z+1 (mod 3^(p+1))`. The right side and `v` are units and 2 generates the units modulo every positive power of 3. For example, `v₃(4^(3^k)-1)=k+1` by induction using the difference of cubes; the order of 2 modulo 3 is 2, so its order modulo `3^(p+1)` is `2·3^p`. Then `y=(2^e v-1)/3=z+3^p t` for an arbitrarily large positive integer `t`. This `y` is odd and `T(y)=2^(e-1)v`, which reaches `v` after the remaining halvings. Positivity of all initial arms follows by taking the lift large enough.

## The boundary argument

For bad-component support, use `v=1` to obtain arbitrarily long zero intervals. For the inverse tree of 5 use `v=85`: the forward trajectory `85,128,64,32,16,8,4,2,1,2,...` avoids 5, and 5 cannot reach 85. Thus every vertex visiting 85 avoids 5 altogether. Both supports are infinite and unbounded, since they contain the even ray above any supported integer.

For arbitrarily large `L` take such an interval of zeros of length `L`, and let `N_L` be the first supported index after it. There are at least `L` zeros immediately before `N_L`. For `b(n)=n²a(n)` there are constants `0<c≤C<∞` with `b(n)∈{0}∪[c,C]`. This follows from the finite reciprocal-packing estimate on simple ordinary paths and the physical endpoint calculation in [ORDINARY_SPECTRUM.md](ORDINARY_SPECTRUM.md). The bounded coefficients of `B_s(z)=sum b(n)^(s/2)z^n`, along a subsequence of these shifts, have a two-sided right limit that vanishes at all negative indices and has value at least `c^(s/2)>0` at zero.

If `B_s` continued on an open arc, the right-limit boundary distribution would vanish there by localization and shifting against smooth tests. The Cauchy transform of that distribution is identically zero in the exterior because its negative coefficients vanish. On the disk its constant term is the nonzero coefficient at zero. A test distribution supported off an open arc has a Cauchy transform analytic across every compact subarc, so exterior and interior would be equal there and then everywhere in the disk. This is a contradiction. The localization and Cauchy-transform details are in [ORDINARY_SPECTRUM.md](ORDINARY_SPECTRUM.md) and the general right-limit criterion is due to Breuer and Simon. [Primary source](https://web.ma.utexas.edu/mp_arc/c/10/10-29.pdf)

Finally, continuation of `M_s` through any given arc entails continuation of `B_s` through it, by the fractional Euler multiplier integral in [ORDINARY_SPECTRUM.md](ORDINARY_SPECTRUM.md). This proves the theorem, including the physical exponent `s=2`. The ordinary blocks allow both possible labels to occupy unbounded intervals. They give no upper bound on the length of a nonconvergent block and no contradiction from the existence of one.
