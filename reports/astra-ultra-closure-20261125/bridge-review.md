# Independent review of the two minimum-core modules

**VERIFIED for the five public theorems at the source hashes below. Universal closure remains open.**

| Reviewed file | SHA-256 | Public theorems |
|---|---|---:|
| `core/ExponentTransport.lean` | `f5549c2aefd583fb93f2f2608ac829dc0eacfdf1d1d7fde6b9ba0862f0780a70` | 3 |
| `core/TowerLaps.lean` | `a720fdbe7c0736027ce38d1af46012e1a1e569e20271e8364f3526b606ab2028` | 2 |

I reconstructed the ordinary clocks from scratch. The odd inputs on the 5-step path out of \(3(32t+17)\) occur at clocks 0, 1 and 4. The odd input on the 3-step path out of \(9(24t+13)\) occurs at clock 0. Both reach \(81t+44\), even for the smallest parameter \(t=0\). The common endpoint and all earlier values exceed 2, hence every supplied upper hitting clock contains the five-step prefix. Keeping the same remaining path decreases time and odd count by exactly two. The physical lower path takes two clocks from \(32t+17\) to \(24t+13\). Three clocks farther its lower value is \(9t+5\) and its upper value is \(81t+44=9(9t+5)-1\). The proof therefore leaves an exponent-two pair and a subsequent offset of one. A renewed ordinary triple witness with the same or lower certificate cost is an additional requirement.

For the second file, subtraction of the two source equations gives
\[
 (4^k-3^k)t=(3^d-1)3^jw .
\]
The hypotheses force \(t,w>0\). With \(C=3^d-1\), \(B=3^k\) and \(D=4^k-3^k\), positivity of the reference makes \(CB<D\), as follows by multiplying \(Bt<3^jw\) by \(C\) and cancelling \(t\). Since \(D\) is coprime to 3, \(D\mid Cw\). Thus \(CB<D\le Cw\), proving \(3^k<w\). This rules out the positive common-reference construction for \(w=1\) at all positive lap and exponent gaps. It leaves ordinary paths using different initial parity words unrestricted.

Both modules were independently compiled in the bridge review object directory with Lean 4.34.1 and flags `-DwarningAsError=true -DautoImplicit=false`. The ordinary map dependency `SourceDeletion.lean` was recompiled from this checkout. All five public axiom reports listed a subset of `propext`, `Classical.choice` and `Quot.sound`.
