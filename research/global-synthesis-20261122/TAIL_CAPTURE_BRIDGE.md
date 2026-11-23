# Gap-four payment for a larger certified interval

**Status: written arithmetic composition, independently reconstructed.**
This note combines the inverse-chain identity in
[GLOBAL_MERGERS.md, G3](GLOBAL_MERGERS.md) with the complete-source grade and
paid-padding interface in PR183 at
68345f60a4f757acb42a69a4ac95910f8ce26163,
[ARBITRARY_DEBT.md, Section 3](https://github.com/GettysburgResearch/collatz/blob/68345f60a4f757acb42a69a4ac95910f8ce26163/research/profound-step-20261122/mergers/ARBITRARY_DEBT.md)
and its companion
[CarryCapture.lean](https://github.com/GettysburgResearch/collatz/blob/68345f60a4f757acb42a69a4ac95910f8ce26163/research/profound-step-20261122/mergers/CarryCapture.lean).
It is not part of this packet's twenty compiled Lean statements.

The elementary gap-two trace is also already present as
WitnessGlobal.twos_trace in the inherited certificate interface. The new
composition here is its use with the paid grade-four capture rule and the
whole-original-interval comparisons below.

The conclusion is a successful complete-source induction rule for an
infinite family. It neither assumes nor proves that all remaining
certificate queries enter that family.

## 1. Definitions and the supplied induction hypothesis

Use the actual shortcut map
\[
 T(n)=
 \begin{cases}
 n/2,&n\text{ even},\\
 (3n+1)/2,&n\text{ odd}.
 \end{cases}
\]
A positive odd gap \(a\) from \(x\) to \(y\) means
\(3x+1=2^a y\), with \(y\) positive odd. It consumes exactly \(a\)
shortcut clocks. A complete word ends at one. A source with initial even
run \(e\) and complete odd word \(W\) has grade
\[
 \Gamma(e;W)=
 \bigl(\{2e+1\}\text{ if }e>0\bigr)
 \uplus\{2a:a\in W\}.
\]
At the largest grade where multiplicities differ, a strict drop means
the new multiplicity is smaller.

For a fixed old grade \(G\), the existing hypothesis
\(\operatorname{IntervalHyp}(G)\) says: every actual complete certificate
of grade strictly below \(G\), with source \(S'>0\), proves convergence of
every positive target \(z\le2S'+1\). This is a well-founded induction
hypothesis at the supplied grade, not an assumption that every positive
integer already converges.

The exact source interface allows any positive odd core, including a
multiple of three. In the vendored Lean definition, PoweredTrace is
existence of \(b>0\), source \(2^e b\), and a complete GapTrace from \(b\)
to one. No ternary-unit condition is imposed on \(b\).

## 2. The combined capture rule

Suppose:

- \(0\le e\le3\), \(S=2^eR\), and an actual complete certificate for \(R\)
  is \(P\Vert\tau\), with endpoint \(q\) after \(P\).
- All gaps of \(P\) are at most four, and \(P\) contains a gap four.
- \(q=1+3^h v\), where \(h\ge1\) and \(v>0\) is even.
- For some actual target clock \(A\), \(z=T^A(n)>0\) satisfies
  \[
  z\le16(1+4^h v)+1.
  \]
- \(\operatorname{IntervalHyp}(\Gamma(e;P\Vert\tau))\) is available.

Then \(n\) converges to one.

**Proof.** Put
\[
 q_j=1+4^j3^{h-j}v\quad(0\le j\le h),\qquad
 b=q_h=1+4^h v.
\]
Every \(q_j\) is positive odd, and
\[
 3q_{j+1}+1=4q_j\qquad(0\le j<h).
\]
Thus \(b\) has an actual forward prefix of \(h\) gaps equal to two,
ending at \(q\). Appending the supplied literal tail \(\tau\) gives its
complete certificate. The new source
\[
 \boxed{S'=8(1+4^h v)}
\]
has initial even run three and complete odd word
\(2^{[h]}\Vert\tau\), where \(2^{[h]}\) denotes \(h\) copies of the gap
two.

Its new grade is
\[
 \{7\}\uplus\{4\}^{[h]}\uplus\Gamma(0;\tau).
\]
In the old grade, the consumed prefix contributes at least one eight.
All old prefix grades and the old initial-even grade are at most eight.
All newly inserted grades are at most seven. Above eight the two grades
agree because the identical tail cancels; at eight the multiplicity
strictly decreases. Therefore the new complete-source grade is smaller.

The guard is exactly \(0<z\le2S'+1\), so the supplied induction hypothesis
gives convergence of \(z\). The actual prefix \(T^A(n)=z\) transfers it
back to \(n\). No statement about a merely formal residue orbit is used.

The terminal-residue hypothesis \(v=2\bmod3\) from G3 is unnecessary for
this positive result. If it holds, \(b\) is a nonunit and has no further
odd predecessor; it is still a valid complete certified source here.
The corresponding proposed maximum-three rule would be vacuous in that
terminal class, since every cap-three inverse path there consists of gap
twos. The removed gap four is a substantive payment.

For PR183's actual carry compiler, one can take \(A=\sum P\) and use its
exact computed endpoint. The present statement also permits other actual
target clocks, including zero.

## 3. Whole initial-valuation-two and initial-valuation-three families

Take \(P=[4]\). Then
\[
 R=\frac{16q-1}{3}=5+16\cdot3^{h-1}v.
\]
For initial even run two, the old source is
\[
 S=4R=20+64\cdot3^{h-1}v.
\]
The replacement source satisfies
\[
 S'-S=
 \bigl(8\cdot4^h-64\cdot3^{h-1}\bigr)v-12.
\]
At \(h=4\), the coefficient is \(320\), and it increases for
\(h\ge4\): writing \(D_h=8\cdot4^h-64\cdot3^{h-1}\), one has
\(D_{h+1}=3D_h+8\cdot4^h>D_h\) once \(D_h>0\).
Since \(v\ge2\), \(S'>S\).

Consequently **every positive target in the original interval**
\(n\le2S+1\) is captured by the new lower-grade certificate, with \(A=0\).
This is a complete rule for every supplied complete certificate with
\[
 \boxed{e=2,\quad P=[4],\quad q>1\text{ odd},\quad q=1\bmod81.}
\]
For these congruence conditions one can always choose \(h=4\) and
\(v=(q-1)/81>0\) even.

Likewise, for initial even run three,
\[
 S'-8R=
 \bigl(8\cdot4^h-128\cdot3^{h-1}\bigr)v-32.
\]
At \(h=6\) the coefficient is \(1664\), and the same recurrence makes it
increase thereafter. This proves the whole-interval rule
\[
 \boxed{e=3,\quad P=[4],\quad q>1\text{ odd},\quad q=1\bmod729.}
\]
Both rules preserve the supplied tail and use the same grade. They are
not claims that a larger certified source is a smaller physical merger
partner in a different induction.

## 4. Exact compatible examples

### A small capture beyond the old padded interval

Take \(R=37\), \(P=[4]\), \(q=7=1+3\cdot2\). The literal complete tail
of seven is \([1,1,2,3,4]\). The inserted inverse source is \(b=9\),
with gap two to seven, so \(S'=72\).

The actual target path is
\[
 75\longmapsto113\longmapsto170\longmapsto85\longmapsto128.
\]
Padding the retained seven alone gives ceiling \(16\cdot7+1=113\).
The new source gives ceiling \(145\), which captures \(128\).
The grade contribution \(\{7,4\}\) replaces the consumed \(\{8\}\);
the exact tail is unchanged.

### A residual query with an entirely alphabet-four certificate

Take
\[
 h=4,\quad v=74,\quad q=5995,\quad R=31973,\quad e=2.
\]
Then
\[
 S=127892,\quad b=18945,\quad S'=151560.
\]
An actual complete tail of \(q\), all of whose gaps are at most four, is
\[
\begin{split}
\tau=[&1,2,2,1,4,1,1,1,4,4,2,1,1,1,\\
      &1,1,1,2,4,3,3,3,1,2,3,4].
\end{split}
\]
The old complete odd word is \([4]\Vert\tau\); the new one is
\([2,2,2,2]\Vert\tau\).

For comparison, consider every literal cut of the old supplied word,
allowing an initial even pad paid for by the removed prefix. If \(r_j\)
is the retained odd endpoint and \(m_j\) is the maximum of the original
even run two and all removed odd gaps, the largest permissible pad is
\(m_j-1\). Thus the exact envelope in this class is
\[
 E=\max_j 2^{m_j-1}r_j=71944.
\]
The maximum is attained at \(r_j=8993\), with pad three. Its target
ceiling is \(143889\). The new certified interval has ceiling
\[
 2S'+1=303121.
\]

The actual target \(n=255783=2S-1\) belongs to the original active interval
and lies above the entire literal-cut ceiling. Its first target gap is
one. The new source captures it immediately, by the whole-interval rule.

If a separate application requires \(n<R\), the same certificate has
the compatible actual target
\[
 n=31967<R,\qquad T^4(n)=161837,
\]
again above the old ceiling and below the new one.

The old source and full clock are \(127892\) and \(60\); the new ones are
\(151560\) and \(65\). Both increase while the complete-source grade
decreases. The proof therefore uses exactly that multiset grade.

The displayed tails, exact gap valuations, target prefixes, grade
comparison, and literal-cut maximum were replayed with integer arithmetic.
The reproducible control is [tail_capture_replay.py](tail_capture_replay.py);
its [recorded output](../../reports/2026-11-22-global-synthesis/late-capture-fixtures.json)
matches byte for byte under ordinary and optimized Python.
These examples check compatibility; the arbitrary-\(h\) and whole-family
claims follow from the written proof above. No new Lean execution is
claimed for this composition.

## 5. What remains for a complete dispatcher

This result expands the successful lower-grade interval rules beyond
literal cuts. It does not prove that every remaining supplied source and
target has a prefix with this endpoint form and a sufficient capture
bound. The entire cap-three inverse graph can still be finite, as G3
proves. Its finite maximum can pay a particular interval without being
cofinal.

A full theorem still requires coverage of every residual query under the
same rank, or a sound combination with other actual descent rules. The
new family is a proved successful rule for that program; its global
coverage remains OPEN.
