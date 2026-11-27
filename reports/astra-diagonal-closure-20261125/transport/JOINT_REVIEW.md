# Independent mathematical and build review of the transport packet

**VERIFIED at the hashes below** for the finite ordinary transport, crossing and deadline declarations, and for the corresponding written statements. The argument establishes a strict saving on the supplied upper suffix under its hypotheses. The positive carry still requires a certificate of its own and a compatible initial halving run. No unconditional pointwise repair or ordinary convergence theorem follows.

| File in `research/astra-diagonal-closure-20261125/transport/` | SHA-256 reviewed |
| --- | --- |
| `FirstCrossing.lean` | `dd23aa86021d468d397adaa9116e813160195e270e32511033236aae744ba997` |
| `CanonicalDeadline.lean` | `574f07abdd6011bc14130de87fe7332c3fe696121a3a43f0e0dfa5e320c69955` |
| `README.md` | `8a9ffebbc75e706665f77fc395bb672d098c67906782fb19a7b6389b5fd9882b` |
| `check.py` | `4519a6274373b851036038739c2413baaf06abc3a3ab349c4a8d54cd70a05e42` |

## Mathematical reconstruction

- For $y=3^jz$ with $z$ odd and $j>0$, the two first odd branches give strict order $T(y)<3^jT(z)$. Induct under the simultaneous prefix guard $Q_i(z)\le j+Q_i(y)$. The four parity cases update the exponent by the actual parity difference and preserve strict order. At the first equality of grades the ordinary upper endpoint is strictly smaller. A synchronous equal-grade merger must therefore have an earlier *strict* overshoot. The short example at $z=23$ gives first balance at two, strict overshoot at three, and a meeting at five.
- In `floor_budget` the floor is assumed at every physical lower prefix and $q<3M$. At an odd step $(3x+1)/(3x)\le 1+1/(3M)$ by the supplied floor. The formal linear budget $(3M-q)2^H T^H z\le3M3^qz$ suffices. The upper hit supplies the separate bound $3^{j+Q_H(y)}z\le2^H$. With the two odd-count bounds this contradicts $3\cdot3^D<2M$ unless an actual lower value goes below $M$. For integral $x$, $x<\lceil z/2^{40}\rceil$ implies $2^{40}x<z$, including the divisible case.
- In the second alternative of `drop_or_exact_suffix`, the terminal surplus is strictly positive. Unit-sized increments locate the first balance at $0<t<H$. Both endpoints are actual iterates at $t$, and the remaining path of length $H-t$ is exactly the original upper hit's suffix. Its cost decreases strictly because the original first upper input is odd. No step treats the positive difference as a specified power of three. The unbounded surplus for a bad lower arm is proved after extending the upper hit by genuine $(1,2)$ laps. Those additional clocks do not improve the original suffix claim.
- `positive_carry_meeting` uses the exact affine lift at a hit of the carry and then the exact laps at one. With $y=2^{h+2k}u$, $u$ odd, $Q_h(c)+k=R+1$, the resulting lower point is $1+3^{R+1}u$ and shares its next step with $3^Ru$. Those $h+2k$ upper turns are all halvings. `align_positive_carry` uses the actually supplied length-$K$ remainder. A general first crossing need not meet the divisibility, hit and grade hypotheses.
- For a unit $n$ and an odd comparator $a$, the two one-step branches give $T(n)=T(3a)$ precisely when $n=9a+1$. This gives $n\equiv10\bmod18$ for existence with any comparator. In the canonical family the parameter in the Lean module satisfies $H=e+9$. The initial seven lower steps end at $2^{H-7}-1$, followed by the prescribed odd run. The even phases at clocks 1, 3, 6 and at the final endpoint are units $2\bmod3$, excluding $10\bmod18$. The upper orbit reaches a positive power of two at nine and first hits one at $H$. At the first balance five the positive carry is one and $v_2(y)=3$ because $17+27v$ is odd by the seed identity. The written all-comparator deadline is valid on the specified ordinary family. It does not assert actual badness for a member.

- I also checked the final paragraph connecting the one-successor criterion to the bounded-cycle branch. Its minimum satisfies $2s+1=3q$, so it is a unit modulo three. The shortcut map preserves units, and the single even phase after any maximal odd run must be the immediate image of an odd input, hence equals $2\bmod3$. No even phase is $10\bmod18$, and no odd phase has that even residue. The one-step criterion excludes every tripled comparator all around the cycle. The separate longer merger is obtained from $3^mu=4v+3$: the two odd runs from $s$ and $2s+1$ have lengths $m$ and $m+1$, ending at $4v+2$ and $12v+8$. Their following two steps go respectively via $2v+1$ and $6v+4$ to the same $3v+2$. This all-lap statement requires the hypothesized bounded cycle. It neither asserts that the cycle exists nor converts the two-step comparison into an immediate merger.

## Independent execution

The run used Lean 4.34.1 `5045d0056413266e57c625dcd7c365b10e377c52` and mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. The local imports were compiled to an independent private output directory before the transport modules. The compile commands executed from the repository root are shown below; `lean` denotes the absolute binary `/workspace/scratch/ae8b5ba301f1/lean_env/lean-4.34.1-linux/bin/lean` and `basepath` denotes the contents of `/workspace/scratch/ae8b5ba301f1/lean_env/lean-path.txt`.

```bash
LEAN_PATH="$basepath" lean -j1 -DwarningAsError=true -DautoImplicit=false -o /tmp/collatz-joint-lean/SourceDeletion.olean research/astra-minimum-source-20261124/arithmetic/SourceDeletion.lean
export LEAN_PATH="/tmp/collatz-joint-lean:$basepath"
lean -j1 -DwarningAsError=true -DautoImplicit=false -o /tmp/collatz-joint-lean/MinimumFailure.olean research/astra-minimum-source-20261124/minimal/MinimumFailure.lean
lean -j1 -DwarningAsError=true -DautoImplicit=false -o /tmp/collatz-joint-lean/CanonicalDeadline.olean research/astra-diagonal-closure-20261125/transport/CanonicalDeadline.lean
lean -j1 -DwarningAsError=true -DautoImplicit=false -o /tmp/collatz-joint-lean/FirstCrossing.olean research/astra-diagonal-closure-20261125/transport/FirstCrossing.lean
python -X utf8 -B research/astra-diagonal-closure-20261125/transport/check.py
```

All four compilations exited zero. An earlier seven-declaration draft of `FirstCrossing` was also compiled; the review table and verdict above refer to the later eight-declaration file. The two final modules printed axiom lists for all eleven public theorems. `drop_or_exact_suffix` and `prescribed_successor_iff` printed `[propext, Classical.choice, Quot.sound]`. The remaining nine each printed `[propext, Quot.sound]`.

The integer program exited zero with 3,840 scale comparisons, of which 3,219 were drops and 621 positive carries. It checked 1,536 carry meetings and the four canonical clocks $H=18,180,342,504$. Each canonical example had its first upper hit at $H$ with three odd inputs, its first balance at five, and two upper odd inputs already spent at the balance. These are finite replay results; the all-parameter deadline is proved by Lean.
