# Simultaneous tower descent, physical phase grids, and narrow-band exits

This exploratory packet strengthens finite descent and ordinary-orbit estimates. **Collatz remains open.** The principal fully formalized result supplies one common base whose first 116 ternary multiples all descend below that base. A separate written argument bounds the time an ordinary orbit can remain in a narrow multiplicative band. Neither result excludes every possible counterexample.

We use the shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd},\end{cases}
\]

and the odd map \(U(x)=(3x+1)/2^{v_2(3x+1)}\). A clock for \(T\) is one shortcut step. A step for \(U\) can contain several shortcut steps. All descent statements below concern positive ordinary integers.

## Results and evidence

| Claim | Statement and scope | Evidence |
|---|---|---|
| EC1024 | For every \(w\ge2^{1024}\) and \(r\ge0\), let \(q\) count the odd inputs in the first 1024 steps from \(3^r w\). Then \(T^{1024}(3^r w)<w\) **if and only if** \(q+r\le646\). | Lean, including both exact boundary comparisons. This characterizes one finite clock. |
| TD116 | For every \(a\ge2^{1024}\), more than 8.0234% of the bases \(w=a+i\), \(0\le i<2^{1024}\), satisfy \(0<T^{1024}(3^r w)<w\) for **every** \(0\le r\le115\). | Lean generic counting, physical descent, and exact numerical inequality. |
| TU116 | If \(a\ge2^{1024}\) is odd, more than 2.1538% of \(w=a+6i\), \(0\le i<2^{1023}\), satisfy the same simultaneous descent. Choosing \(a\equiv1\) or \(5\pmod6\) keeps every base eligible for the least smooth-core argument. | Lean generic counting, physical descent, and exact numerical inequality. |
| TM32 | For every fixed odd \(w\) and \(s\ge0\), some \(d<32\) has \(T^7(3^{s+d+1}w)=T^7(3^{s+d}w)\). | Lean finite residue check and ordinary lift. The supplied exponent need not be this adjacent pair. |
| PG | One supplied positive odd orbit either drops below a floor \(m\) or visits an entire approximate grid of dyadic logarithmic phases at distinct times. The error is \(3/q+q/m\) for an appropriate reduced approximant with \(q\le N\). | Lean, including the embedding into actual shortcut clocks. Explicit approximant hypotheses remain visible in the polynomial specialization. |
| CW | For fixed \(2<K<4\) and \(\epsilon>0\), a primitive odd cycle of sufficiently large minimum \(m\), contained in \([m,Km]\), has period \(p\le m^{\log_3(K/2)+\epsilon}\). | Proposed written proof, independently reconstructed; its terminal-congruence step is Lean checked. |
| BX | For fixed \(2<K<K_*\), every sufficiently large odd start \(n\) exits \([n,Kn]\) within \(O_{K,\epsilon}(n^{\log_3(K/2)+\epsilon})\) shortcut steps. Either exit direction is possible. | Written consequence of CW and an external logarithmic-form estimate. No numerical onset is supplied. |
| PE | A sufficiently long physical parity echo forces an actual return; all cuts of an affine parity cylinder have exactly the same source quotient. | Lean. The associated symbolic obstruction is a separate written argument. |

For BX and the cycle-width consequence, Wu–Wang's published estimate gives
\(K_*=2\cdot3^{1/5.1163051}=2.47904859\ldots\).
Using the homogeneous two-logarithm estimate stated in Chudnovsky's 2026 preprints gives the source-qualified value
\(K_*=2\sqrt[3]{3}=2.88449914\ldots\).
The external proof developments were not rebuilt here. These are asymptotic thresholds for **odd** values, not uniform numerical exclusions of all cycles below a given size. See the [full arithmetic argument and sources](arithmetic/README.md).

## Why simultaneous descent is useful

The frozen least smooth-core formulation in PR 192 chooses an exceptional base \(w\) whose smaller bases have convergent ternary towers. A physical endpoint strictly between zero and \(w\) is therefore a useful destination. TD116 and TU116 produce such endpoints for all 116 exponents at the same base, and prove quantitative coverage in every specified block.

The counting proof has no independence assumption between different exponents. At a fixed exponent \(r\), multiplication by \(3^r\) permutes residues modulo \(2^h\), and the first \(h\) physical parity bits give a bijection. If \(p\) is their number of odd inputs, the endpoint estimate

\[
2^hT^h(3^r w)\le3^p(3^r w+2^h)
\]

makes \(3^p(3^r+1)<2^h\) a sufficient condition for descent when \(w\ge2^h\). The failing parity vectors form an explicit binomial tail. A union bound over \(r\) gives the simultaneous statement. On the step-six progression, the first bit is odd and the remaining bits run through all \(2^{h-1}\) words, giving the corresponding shifted binomial tail.

[TowerCertificate.lean](machinery/TowerCertificate.lean) evaluates the finite sums using a proved binomial recurrence and `decide +kernel`. The numerical assertions therefore participate in the same Lean axiom audit as the physical implications. The density statements follow by combining its inequalities with `simultaneous_tail_bound` and `ray_simultaneous_bound`; `full_block_116` and `odd_ray_116` expose the resulting existential endpoints directly.

The same module strengthens the sufficient parity budget to the exact pointwise criterion EC1024. It preserves the linear term and bounds the additive correction by

\[
3^q n\le2^{1024}T^{1024}(n)\le3^q n+3^{1024}.
\]

The exact integer inequalities
\(3^{646}2^{1024}+3^{1024}<2^{2048}\) and
\(2^{1024}<3^{647}\) decide the two sides uniformly for all allowed bases and ranks. The criterion still requires the physical odd count of the specified trajectory; it does not assert that every such count lies on the descending side. It also does not make the different rank tests independent.

The [fixed-source note](fixed_source/README.md) also gives growing windows \(h=32t\), \(R=2t\), with exceptional fraction at most

\[
(2t+1)\left(\frac{8^{32}}{9^{18}7^{14}}\right)^t.
\]

This tends to zero, but its exceptional set can still contain a particular hypothetical least failure. An explicit ordinary family misses both the finite descent deadline and the seven-clock neighboring-merger test. The family illustrates a failed strengthening; it is not a counterexample to Collatz.

## The narrow-band argument

The new written count follows a trajectory while its odd values stay in \([m,Km]\). Set \(k=\lceil\log_3(Km)\rceil\). After partitioning starting logarithmic heights into finitely many small bins, the possible cumulative division clocks lie in intervals of length slightly larger than \(\log_2K\). For \(2<K<4\), each interval allows at most two integers. Irrational rotation controls the fraction of positions admitting two choices, yielding at most

\[
m^{\log_3(K/2)+\epsilon}
\]

possible length-\(k\) clock words, up to a fixed factor.

One clock word determines the terminal value modulo \(3^k\). Because the band is narrower than \(3^k\), it has at most one terminal in the band. In a primitive cycle, advancing \(k\) odd steps permutes the distinct states even if \(k\) exceeds the period. This supplies CW. A lower bound for the nonzero linear form \(A\log2-p\log3\) then excludes sufficiently large cycles in each band below \(K_*\).

For a general starting integer, an orbit trapped in such a band cannot repeat once the start is sufficiently large. Its distinct endpoints are bounded by the same count, so it must leave. The exact product formula controls the elapsed shortcut clock as well. This proves BX as a written deduction; an upward exit remains fully compatible with an escaping orbit.

The [independent review](machinery/REVIEW_ODD_CYCLES.md) checks the cyclic wraparound, the uniform rotation count, the terminal rather than initial congruence, the external logarithmic-form exponents, and the scope of the exit statement. No priority claim relative to the entire Collatz literature is made. Comparison with the frozen PRs 173, 205 and 206 appears in the arithmetic note.

## What the recent GRH work contributes

Alpöge's November announcement and the independent verification reports concern RH and GRH for all Dirichlet characters. We checked the primary statements and the proposed divisibility mechanism. We did not rebuild that external development or assume a GRH-to-Collatz implication. The [machinery note](machinery/README.md) records the source-qualified scope and explains a precise obstruction to reusing the same affine Collatz cuts as independent divisibility gains.

The local identity is exact: on a physical length-\(L\) parity cylinder,

\[
T^j(x+2^Lk)-T^j(x)=2^{L-j}3^{q_j}k.
\]

Every cut shares the same quotient \(k\); a second cut alone does not create a second independent arithmetic quantity. The proposed import needs a further independent object. This leaves room for a different construction and identifies what the present one does not supply.

## Replay

The packet uses Lean **4.34.1**, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612` with its pinned Lake dependencies. Start with a built checkout of that Mathlib revision. From the repository root:

```bash
python -B research/astra-ultra-closure-20261125/replay_lean.py \
  --lean /path/to/lean-4.34.1/bin/lean \
  --mathlib /path/to/pinned-mathlib \
  --receipt /path/outside/checkout/lean-replay.json
python -B research/astra-ultra-closure-20261125/fixed_source/check_towers.py
python -O -B research/astra-ultra-closure-20261125/fixed_source/check_towers.py
python -X utf8 -B tools/validate.py --regressions \
  --receipt /path/outside/checkout/repository-validation.json
```

The last command requires a clean complete checkout. The Lean driver starts with an empty directory for this packet's compiled modules, orders local imports, compiles with `warningAsError=true` and `autoImplicit=false`, audits every public theorem in the packet's declaration inventory, and rejects dependencies outside `propext`, `Classical.choice`, and `Quot.sound`. It checks source hashes again after compilation. Its dependency identity check does not claim an independent rebuild of all of Mathlib or of external number-theory developments.

Execution receipts and source pins are in [the report directory](../../reports/astra-ultra-closure-20261125/README.md). The Python checker independently reproduces the finite integer calculations and tests the stated finite controls. Repository integrity checks authenticate the retained baseline and bounded regressions; they do not verify the new written analytic argument.

## Next missing statement

The most direct remaining obligation is a **source-dependent lower-base merger for every surviving least base and first bad exponent**. The present coverage theorem, recurring adjacent mergers, and narrow-band exits are compatible with an exceptional base that always escapes the useful cases. Closing that logical gap would require another theorem. Wide cycles and unbounded ordinary trajectories are still permitted by this packet.
