# Independent review of the actual odd-edge controller attempt

Reviewer: factoring bridge lane, 2026-11-28.

Reviewed source: `research/astra-collision-factor-bridge-20261128/collision/ACTUAL_ODD_EDGE_CONTROLLER_ATTEMPT.md`.

SHA-256: `6abd2e0aca9861c70fc0378dcba6414259b63693af4689e743629ecc77395bfd`.

**Verdict: Sections 2–4 pass their stated finite affine-cylinder scope.**

Reparametrizing the unread variable as `z=b+2z′` preserves odd powers of three as the two slopes. Each individual next parity is conditionally fair; their difference has conditional mean zero without any independence assumption. Expanding the square therefore gives the stated first and second moments of the effective grade difference. Affine fusion is absorbing and forces that difference to vanish, so Cauchy–Schwarz gives the displayed lower bound on survival.

For equal initial slopes and distinct offsets, let `k=v₂(|u−v|)`. Exactly one residue of the unread variable modulo `2^k` makes both arms take `k` common halvings. Their new offset is odd. Fixing either next bit gives an effective grade gap `+1` or `−1` on a cylinder of probability `2^(−k−1)`. No earlier affine fusion occurs because the nonzero offset is only divided by powers of two. The conditional survival bound then yields a comparison-dependent reciprocal tail and infinite expected affine-fusion time in the consistent infinite fair-bit model.

For independent clocks, equality of the endpoint affine slopes forces equality of the powers of two and of three separately. Every unequal-slope pair of word cells contributes at most one ordinary root. At a fixed largest search deadline, the synchronous survival bound leaves an infinite positive-cylinder family of uncertified completions; adding finitely many isolated roots cannot cover it. This does not exclude source-dependent mergers with clocks that grow with the source.

The appended genuine inverse-edge extension also passes. Retaining `F^r x = F^s z`, a forward edge `F z = y` gives `F^(r+1) x = F^s y`, while a reverse edge `F y = z` gives `F^r x = F^(s+1) y`. Induction therefore turns a length-`K` undirected genuine path into forward merger clocks with `r+s=K`. An affine identity again forces `r=s`, hence a synchronous fusion no later than `K/2`. Fixed ternary legality conditions select odd-stride progressions and leave complete finite binary periods fair. Bounded path searches therefore retain the stated whole-cell obstruction. This does not prohibit isolated ordinary mergers with unequal clocks or source-dependent unbounded certificate lengths.

Section 5 accurately labels the appended Mazur numerical constant as an inspection of the named source module, not a fresh rebuild of that external development. The present review does not independently rebuild or certify that imported analytic development.
