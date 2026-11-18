# What the native parity horizon can resolve

**PROPOSED.** Keep the shortcut map and the constants \(p,h\) of the [critical window bound](CRITICAL_MOMENT.md). Let \(G_L\) consist of length-\(L\) binary words for which \(q_t\ge pt\) at every prefix. The window proof counts uncaptured words without an orbit membership test. The order of magnitude of that particular counting error is sharp:
\[
 |G_L|\asymp 2^{hL} L^{-3/2}.
\]

The upper bound follows from (3) there with the constant barrier zero: for terminal \(d=q_L-pL\ge0\), multiply its probability bound by \(2^{hL}e^{-\lambda d}\) and sum over unit-spaced \(d\). For the lower bound take every word of weight \(q=\lceil pL\rceil\) and rotate it at a minimum of its centered partial sums, considering times \(0,\ldots,L-1\). Its total surplus is positive. Prefixes of the rotated word ending before the old endpoint are nonnegative by minimality, and wrapping prefixes add the positive total surplus to a difference from that same minimum. At most \(L\) words can supply the same rotation. There are at least \(\binom Lq/L\gg2^{hL}L^{-3/2}\) surviving words by Stirling at \(q=pL+O(1)\). The repository's previous entropy-exponent lower bound already used this rotation.

Every such word has exactly one ordinary source in *each* complete interval of \(2^L\) consecutive integers, by the parity bijection. In particular these are actual finite ordinary sources failing every multiplicative capture test \(2\cdot3^{q_t-pt}\le1/c_{u(t)}\) used to prove the upper bound. This says nothing about how many of them lie on one injective orbit.

## A post-horizon experiment with both conditionings explicit

A test of additional ordinary cancellation can restrict first-block words to \(G_L\) with \(q_L=\lceil pL\rceil\). For their source \(x\) in \([2^L,2^{L+1})\), one needs the second block from the actual endpoint \(y=T^L(x)\). The affine identity gives
\[
 y= (3^{q_L}/2^L)x+E_L,\qquad
 0\le E_L=\frac12\sum_{j=1}^L v_{j-1}3^{D_L-D_j}\le\frac32 L .
\]
This locates the second source within an additive \(O(L)\) of a known dilation of the first one. The second word is determined by that ordinary endpoint. An estimate for its splicing probabilities cannot use independent fair bits as a theorem.

As a precise open target, let \(B_L\) count the ordinary sources in this interval whose first and second blocks *both* belong to \(G_L\) with the displayed terminal weight, imposing the two prefix constraints relative to their respective starts. Does \(B_L\le C2^{(h-\epsilon)L}\) hold for some fixed \(\epsilon>0\)? The statement is weaker than controlling arbitrary terminal weights and omits source windows at unbounded translations. Even a proof would not alone exclude a positive divergent orbit.

## Exact translation average and finite observations

Let \(R\) be the set of representatives \(0\le r<2^L\) of the critical terminal-weight words, \(A=|R|\), and \(b_r=T^L(r)\), using \(T(0)=0\) just for the parity enumeration. For integer shell index \(j\), each \(r+j2^L\) follows the same first word and ends at \(b_r+j3^q\). Hence its two-block count is exactly
\[
 B_L(j)=\sum_{r\in R}\mathbf1_R((b_r+j3^q)\bmod 2^L).
\]
As \(j\) runs through all \(2^L\) residue classes, the odd multiplier \(3^q\) permutes the shifts. Consequently \(\sum_j B_L(j)=A^2\), whether or not different \(b_r\)'s coincide. For any \(s>0\), the proportion of shells with \(B_L(j)>sA^2/2^L\) is at most \(1/s\). This average does not give the bound for a prescribed shell.

[Exact checker](check_two_blocks.py). It constructs each first word by lifting the source representative through a dyadic parity extension, then evaluates the actual second block. With the histogram flag it also accumulates every ordered pair of a first endpoint and a second residue and checks the translation sum. The independent enumeration flag tests both blocks by direct iteration of the ordinary starts.

| \(L\) | First count \(A\) | \(B_L(0)\) | \(B_L(1)\) | Largest \(B_L(j)\) over every shell |
|---:|---:|---:|---:|---:|
| 12 | 85 | 1 | 2 | 6 |
| 15 | 476 | 10 | 4 | 19 |
| 18 | 2,652 | 39 | 24 | 50 |
| 21 | 17,637 | 166 | 144 | not enumerated |
| 24 | 108,950 | 714 | 715 | not enumerated |
| 27 | 663,535 | 3,270 | 3,345 | not enumerated |

Exact commands, run from the repository root:

```sh
python -B research/critical-orbit-mellin/check_two_blocks.py --min-length 6 --max-length 18 --histogram --check
python -B research/critical-orbit-mellin/check_two_blocks.py --min-length 19 --max-length 27
```

At (L=27) the translation average is (663535^2/2^{27}), approximately 3280.3. These finite counts do not establish asymptotic cancellation at either fixed shell.

Prior symbolic rotation argument: [fixed-height attack, Proposition 3](../external/mazur-2026/fixed-height-power-saving-attack.md).
