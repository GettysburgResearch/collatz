# Independent review of the smaller-five construction

**Verdict: PASS for the stated conditional theorem SF1–SF4. No full Collatz
proof is certified by this review.**

The reviewed theorem concerns one fixed globally least reverse failure

\[
X=(1024\cdot2^e-2573)/243,\qquad e=119+162j.
\]

It constructs, according to the parity of \(j\), an actual odd ternary
unit \(q<X/13\) such that \(q\) and \(5U(q)\) belong to the basin of 1,
while \(5q\) is in the ordinary component of the failed Mersenne target.
The memberships use the same global minimum and the pinned H2 interval.
They do not assume that every number smaller than a known convergent
source converges.

## Frozen review inputs

| File | SHA-256 |
|---|---|
| `SMALLER_FIVE_FAILURES.md` | `f9ee7dcac226d46816b3ac91ce88996f3932906672084a28063c284eb8e3736c` |
| `check_smaller_five_failures.py` | `2fff9fa3c5acc6c77119379c1503a978690b5558a17e9f8a160dae370ce1739e` |
| `base_119_ordinary_prefix.json` | `ed32671c008009bd15b08859196ac967cedc3172516828b6fec9150cecd80e15` |

These are the files in the sibling `agent_global_reverse_20261121`
directory at review time. No reviewed file was edited by the reviewer.

## Mathematical checks

1. **The actual eligible sources.** The congruence
   \(4\cdot2^e\equiv11\pmod {243}\) holds on the whole exponent
   progression. The two numerators are respectively 27 and 81 modulo
   243, proving the exact powers of three divided out in the source
   formulas. The two modulo-five phases give the remaining divisibility.
   The resulting sources are positive odd ternary units.
2. **The failed targets.** The inverse words yield exactly
   \(5q\xrightarrow{(2,1,2)}2^e-1\) or
   \(5q\xrightarrow{(2,2,1,2)}2^e-1\). These are positive ordinary
   paths. The height identities
   \(160q=9X+23\) and \(40q=3X+5\) imply the common strict bound
   \(q<X/13\), including the additive terms.
3. **The certified successor-five values.** Both phases reach
   \(2^{e-1}+1\), in the stated two or five shortcut clocks. The next
   \(e-1\) clocks reach \(3^{(e-1)/2}+1\). The initial inequality at
   \(e=119\), and the ratio \(3^{81}<2^{162}\), put the endpoint in
   the same H2 interval for every allowed exponent.
4. **The first-valuation-three source.** The exact source word
   \((3,2,1,4)\) reaches \((2^{e-3}+1)/5\). The full binary cylinder
   at offset \(1/5\) forces the ordinary parity block odd, even, even;
   its affine map has slope \(3/8\) and fixes \(1/5\). The resulting
   endpoint and the initial bound at \(e=281\) establish the claimed
   source membership for the entire phase.
5. **The first-valuation-four source.** The exact source word
   \((4,1,2,1,1,2,1)\) reaches
   \((81\cdot2^{e-7}+19)/5\). The full binary cylinder at offset
   \(19/5\) forces the ordinary parity block odd, odd, odd, even, even;
   its affine map has slope \(27/32\) and fixes \(19/5\). The last
   block may end at an even integer, and the note correctly retains an
   ordinary shortcut prefix instead of asserting an extra exact odd
   exponent. The fifth-power bound and the base at \(e=443\) are exact.
   The separate \(e=119\) proof supplies a valid 136-clock ordinary
   prefix ending strictly inside the same H2 interval.
6. **The remaining boundary.** The identities
   \(U(5q)=4(5U(q))-1\) and \(U(5q)=2(5U(q))-1\) are correct. They
   do not give convergence of the shifted targets from convergence of
   \(5U(q)\). The note does not make that inference. Its generic
   reverse-return budget is used only as a boundary: combining it with
   \(q<X/13\) has product \(10126085/299>1\), so no decreasing joint
   scalar cost is claimed.

## Independent replay and scope

`review_smaller_five_failures.py` imports no functions from the author's
checker. It proves the four short source/target words on their required
binary cylinders, independently checks the two rational-offset cycles,
replays the exact induction bases and growth comparisons, and reads and
checks all 136 transitions in the supplied JSON base certificate. It also
prints the input hashes above.

Both of these commands passed:

```text
python3 -B review_smaller_five_failures.py
python3 -OO -B review_smaller_five_failures.py
```

The author's checker was also run independently in normal and `-OO`
modes, with both runs passing. Its bounded 32-exponent replay is used as
implementation evidence, not as the proof of the unbounded claims.

The H2 constant and global reverse criterion are accepted only at the
explicit repository pins in the note; this review does not re-prove their
full affine covers. The review certifies the new conditional construction
and its exact use of those dependencies. It does not certify convergence
of every shifted target, a completed return below the original \(X\), or
a universal physical-five compiler.
