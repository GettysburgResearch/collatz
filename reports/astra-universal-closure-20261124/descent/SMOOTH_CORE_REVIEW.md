# Independent review of the positive first-tower reduction

**VERIFIED at file SHA-256**
`488bd1d4081e92cfe836d85dd1b27201b4787c46ee395b9196508294684613db`
for [SmoothCore.lean](../../../research/astra-universal-closure-20261124/global/SmoothCore.lean).
The two imported repository sources were copied from commit
`26f070c38ad9edd21ed7dac6efaab6554550c2a3`.
All three modules were built in a separate initially empty output directory
using Lean 4.34.1 and the restored Mathlib search path. These were the
compiler invocations, after setting PATH to that toolchain and LEAN_PATH
to the separate output directory followed by the dependency search path.

```sh
lean -o SourceDeletion.olean SourceDeletion.lean
lean -o MinimumFailure.olean MinimumFailure.lean
lean -o SmoothCore.olean SmoothCore.lean
```

All three finished with exit code zero. Fourteen public theorem audits
were printed for the final module. The combined axiom set was
`propext`, `Classical.choice`, `Quot.sound`. The reservoir theorem
uses only `propext`; the two residue exclusions use `propext` and
`Quot.sound`.

The minimum ranges over *all* positive bases supporting a bad power.
Dividing an even base by two, or a base divisible by three by three,
contradicts its minimality. The smaller-base premise gives both good
labels needed at every smaller positive odd comparison in the imported
source deletion argument, so the base itself is good and the first bad
exponent is positive. At the **same** base the earlier powers alone
are guaranteed good. The base 1 is allowed.

For \(3^r w+1=2^m a\) with \(2^m>3^r\), assuming \(a\ge w\)
gives \((2^m-3^r)w\le1\). This forces \(a=w=1\), and
\(3^r+1=2^m\). Modulo 8 the left side is 2 or 4, so \(m<3\).
The only positive possibilities for \(3^r\) are 1 and 3, both good.
When the binary clock is shorter, the preceding power is good and odd,
and its next step is \(2^{m-1}a\), so \(a\) is still good.
This last conclusion does not certify all powers above \(a\).

A separate symbolic propagation checked both arms for every integer
parameter. In the table 1 means an odd input. The linear coefficient
remained even at each step where a parity was taken.

| Inputs for the two paths | Input parity words | Common endpoint |
|---|---|---|
| \(8t+4,8t+5\) | 001, 100 | \(3t+2\) |
| \(8t+6,24t+21\) | 011, 100 | \(9t+8\) |
| \(16t+2,16t+3\) | 0101, 1100 | \(9t+2\) |
| \(48t+8,16t+3\) | 0001, 1100 | \(9t+2\) |
| \(512t+237,4608t+2133\) | 100101100, 100000001 | \(81t+38\) |

For odd \(a\), the four high-exit tests remove the odd classes
3, 5, 7, 9, 13 and 15 modulo 16 for \(3^m a\).
For \(r\ge2\) the last row compares the candidate with its own
two-powers-earlier source and excludes \(3^r w\equiv85\pmod{512}\).

The final equivalence has the precise universal quantifiers printed
in `FrontierMerger`. Under universality, choose the original base at
exponent zero and let the two independent clocks end at 1. In the
reverse direction take the actual first tower, factor its successor
with odd residual, and apply the exclusions above to obtain every guard.
Both alternatives in the proposed destination are already good by
minimality of that very tower. A meeting gives the contradiction.
Existence of a meeting on **every** remaining ordinary input is open.
