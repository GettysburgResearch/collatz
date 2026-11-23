# Independent reconstruction of the pressure/Wiener attack

Reviewer: sibling `global_source`; reviewed 23 November 2026. The reviewer did not develop the pressure note or edit its files. This is a scoped mathematical reconstruction of the new argument, not a replay of the inherited eigenmeasure classification or the literature.

## Result

**Accepted at the written scope stated.** The positive quasimode construction, weighted norm estimate, support separation from the exact kernel, nonclosed-range consequence, and finite analytic equation all reconstruct correctly. No escape-exclusion result is supplied or inferred. No Lean verification is claimed.

## Reconstruction

1. For `0<=t<s-1`, the column estimate uses `n=(2^e q-1)/3<2^e q/3`. Summing the positive geometric majorant gives precisely `3^(s-t)/(2^(s-t)-1)`. At `t=0`, the six legal gap pairs are `(2,4),(1,3),(2,6),(3,5),(4,6),(1,5)` for `q mod9=1,2,4,5,7,8`; `(1,3)` maximizes the geometric sum and yields W4.
2. The lifting identity `3^(m+1) | 2^(3^m)+1` follows by cubing. With `e_k=3^(k+1)+1`, it makes `(q_k+1)/3^k` a positive multiple of six. Hence every displayed `n_j` is an ordinary positive odd unit, the first k exact gaps are one, and the final gap reaches one. The `k=1` pair 227,341 and `k=2` triple 39768215,59652323,89478485 check directly.
3. A root `q_k>1` cannot be periodic because its next odd state is one. This gives uniqueness of each ancestor depth. Along an actual edge, `3/2^a=(U(n)/n)*(3n/(3n+1))`, so the path telescope is `h_q(n)=(q/n)^s Lambda(n,q)^s <=q^s n^(-s)`. The summability uses `s-t>1`; no moment at or above the endpoint is claimed.
4. Every ancestor except the root satisfies the exact fixed-vector recurrence. The root has defect one, because its successor one cannot reach the root. Outside the ancestor set both terms vanish. Thus `(I-A_s)h_q=delta_q` holds on every ordinary unit, including root and terminal states.
5. The source `p_k` contributes `p_k^t(3/2)^(sk)` to the norm. The stated `q_k/p_k<=2(3/2)^k` follows from `(2/3)^k q_k>=2`; the elementary exponential bound in the note proves this for every k>=1. Dividing the exact defect norm `q_k^t` gives W6 with the stated exponent `s-t` and factor `2^t`.
6. Any complex exact fixed vector is zero at one because the cycle multiplier is `(3/4)^s`, then zero throughout the basin by finite predecessor induction. This is stronger than a positivity-only statement. It implies disjoint support from each `f_k`, hence distance exactly one from the kernel. The closed-range estimate for a bounded operator on a Banach space, applied to its quotient by its closed kernel, contradicts the residual limit. Finite positive truncations follow from norm convergence and boundedness of the operator; no uncomputed truncation rate is asserted.
7. A fixed ordinary index meets at most finitely many increasing roots `q_k` on its trajectory. Thus the normalized quasimodes vanish eventually at each fixed coefficient. A common `C n^(-s)` envelope would be summable in the weighted norm and would contradict unit norm by dominated convergence. The distinction between approximate eigenvectors and the canonical fixed coefficient envelope is therefore genuine.
8. At exponent `3n+1`, the infinite series equation has exactly one branch, `e=v2(3n+1)`, with index `U(n)`. The six branch filters are correct. Subtracting `2^(-6s)` times the equation at `z^64` removes all terms with `e>=7` and yields W16. Conversely, any missing formal tail obeys `F(z)=2^(-6s)F(z^64)` and has zero constant term; its least nonzero exponent would be impossible. This proves the converse, without analytic exchanges.
9. At `s=2`, multiplying by 4096 gives the coefficients 9216,2304,576,144,36,9 in W17, with tail coefficient one. The equation is therefore genuinely finite. It is one mixed equation and does not manufacture separate 2-Mahler and 3-Mahler equations.

## Execution and boundary

The reviewer ran `python -X utf8 -B check_pressure_wiener.py`: six exact convergent trajectories, 2,814 exact filter cases, and 24,008 rational coefficient comparisons passed. The checker checks the operator equation on arbitrary signed coefficient polynomials; it does not approximate an infinite eigenmeasure or establish the infinite spectral deductions computationally.

The cited PR177 classification and uniform path-product estimate remain inherited written inputs. The claims about external papers were not independently re-browsed in this review and are outside its acceptance scope. The conclusion that W17 kernel uniqueness would exclude escape is correct conditional on the cited classification; it would not exclude nontrivial cycles.

## Reviewed bytes

- `PRESSURE_WIENER_ATTACK.md`: `5a0d035827f835f437c1d35f37e520da99b162ff6d97ea3e6ce8e91c7ec36a48`
- `check_pressure_wiener.py`: `84171e1740beccd024256bce551989190744836309878f61b884cce1baade3b0`

## Publication formatting binding

The coordinator replaced one trailing LaTeX control-space by `\quad` to pass the whitespace gate. No mathematical statement or argument changed. The original reviewed source hash above remains the review snapshot; the publication source SHA-256 is `4b73c35aabe57a44d96c08c30a4990ee0aecec64f7e9200738cd20b5b4ea2bcd`. The coordinator checked this one-line formatting change.
