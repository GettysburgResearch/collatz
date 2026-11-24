# External inputs and what was actually used

24 November 2026. The repository-source pins are in SOURCE_INTAKE.json.
This ledger separates original proofs in this packet from external
statements. A source citation is not an independent verification of that
source's entire proof.

| Input | Source and location | Use and review scope |
|---|---|---|
| F, exact-total bounded-offset ternary floor | [rStation Collatz paper 48](https://rstation.ai/problems/collatz/papers/48), displayed v2, Lemma 7 (76) | Statement inspected; external manuscript theorem retained as a hypothesis. Its full analytic proof is not independently rebuilt. |
| Stationary real-cutoff density estimate | [rStation paper 9](https://rstation.ai/problems/collatz/papers/9), v2, Theorem 16 B2 and Appendix C | The stated \(L^p\) estimate is an additional hypothesis used for upper comparisons. It does not follow from F. |
| Canonical ordinary-root inverse law | [rStation paper 19](https://rstation.ai/problems/collatz/papers/19), v2, F1–F3 and F8 | Source-qualified fibre/trace theorem and bounded-selection identity. The packet reconstructs their annulus and upper-frequency consequences without asserting a forward Markov law. |
| Linear forms in \(1,\log2,\log3\) | Qiang Wu and Lihong Wang, [“On the irrationality measure of \(\log3\)”](https://doi.org/10.1016/j.jnt.2014.03.007), Journal of Number Theory 142 (2014), 264–273, Theorem 1 | The actual three-term linear-form statement and proof's change of basis were inspected. The exponent \(4.1163051\), with arbitrary positive slack, controls the two-log rotation; the one-number corollary is not substituted for it. |
| Cyclic hyperbolic-time selection | José F. Alves, Christian Bonatti and Marcelo Viana, [“SRB measures for partially hyperbolic systems whose central direction is mostly expanding”](https://w3.impa.br/~viana/out/mexpanding.pdf), Lemma 3.1 | Classical Pliss selection motivates the cyclic record proof. This packet supplies its own exact finite derivation and constants. |
| Entropy from separated finite laws | Michał Misiurewicz, [“A short proof of the variational principle for a \(\mathbb Z_+^N\) action on a compact space”](https://www.numdam.org/article/AST_1976__40__147_0.pdf), Astérisque 40 (1976), 147–157 | Primary paper inspected; the packet spells out the finite-block entropy averaging needed for its own measures. |
| String attractors and factor complexity | Dominik Kempa and Nicola Prezza, [“At the Roots of Dictionary Compression: String Attractors”](https://arxiv.org/abs/1710.10964), v4 | Primary paper inspected. The circular attractor factor bound is stated and proved in the packet's convention. |
| Continued-fraction criterion | Robert C. Vaughan, [continued-fraction lecture notes](https://personal.science.psu.edu/rcv4/677C02.pdf), Theorem 2.3 (Legendre) | Criterion and proof inspected. This is used only after reducing the physical period/odd-count ratio to lowest terms and checking the strict error inequality. |

No third-party paper text is reproduced. The packet's deductions and
finite programs are included in full for review; external theorems retain
their named source status.
