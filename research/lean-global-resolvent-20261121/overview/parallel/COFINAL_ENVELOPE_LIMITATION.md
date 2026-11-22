# The literal-cut envelope has a sharp cofinal halving boundary

**Status:** written consequence of the proved PR177 cofinal predecessor theorem and checkpoint8's exact envelope theorem. No new Lean theorem is claimed. This concerns the literal-cut envelope and the blanket `LowEnvelopeEntry` selector. It does not prove or refute `LowEnvelopeMerger`, and it does not identify a cofinal family surviving every other published source rewrite.

## Statement

For arbitrarily large positive odd integers \(q\), there is an actual complete odd certificate \(A\), with every gap in \(\{1,2,3,4\}\), such that for initial even exponent three,

\[
S=8q,\qquad E(3,q,A)=4q=S/2.
\tag{1}
\]

Moreover every nonempty literal prefix \(W\) of this supplied certificate satisfies

\[
2^{\operatorname{total}(W)}>2\cdot3^{|W|}.
\tag{2}
\]

Thus the compensated noncontracting-prefix rule does not apply to these words. The general lower bound \(E\ge S/2\) is attained cofinally: the low alphabet alone cannot provide a positive uniform improvement in that fraction, or force \(E/S\to1\).

If \(2^d\le q<2^{d+1}\), the target

\[
t=2^{d+4}-1
\tag{3}
\]

belongs to the literal-envelope residual strip

\[
2E+1=8q+1<t\le16q+1=2S+1.
\tag{4}
\]

Its actual shortcut orbit stays above that envelope for every time
\(0\le R\le d+4\). In particular, any witness of `TargetHitsEnvelope` for this state has \(R>d+4\). There is no uniform constant forward lookahead that proves the blanket entry selector on all its low states.

## Construction using an actual complete source

Fix an arbitrary height \(N\). Apply PR177's `cofinal_predecessors` at terminal source one and empty tail. It supplies a positive odd ternary unit \(p>N\) with a finite complete odd certificate over gaps at most four. This is an existing basin witness; the construction assumes no convergence of an arbitrary input.

List the actual odd states in this certificate, including its terminal one. Choose a state \(v\) of maximum ordinary value, and keep its literal suffix certificate \(B\). Then

\[
v\ge p>N,
\qquad
u\le v\quad\text{for every state }u\text{ in that suffix.}
\]

The state \(v\) is a ternary unit: the initial state \(p\) is a unit, and every subsequent state satisfies \(2^a u=3x+1\), which excludes divisibility by three. It is also odd.

Choose one additional inverse edge by

\[
a=\begin{cases}4,&v\equiv1\pmod3,\\3,&v\equiv2\pmod3,\end{cases}
\qquad q=(2^a v-1)/3.
\tag{5}
\]

The quotient is an integer. Its numerator is odd and the divisor is odd, so \(q\) is odd. Since \(v>0\), both choices give \(q\ge2v\). The identity

\[
3q+1=2^a v
\]

is an exact odd edge because \(v\) is odd. Therefore \(A=[a]\mathbin{+\!+}B\) is a complete certificate for \(q\), still over the alphabet at most four. Every proper odd endpoint of \(A\) is at most \(v\le q/2\). The values \(q\) are cofinal because \(q\ge2v>2N\).

## Exact envelope calculation

With initial exponent \(e=3\), every removed low gap satisfies \(a-1\le3\). Thus the maximal rank-paid initial exponent after any nonempty literal cut is still exactly three. Every such cut consequently has powered source

\[
2^3u\le8v\le4q.
\]

The empty-prefix option halves the initial powered source and attains \(2^{3-1}q=4q\). Checkpoint8's maximality theorem therefore gives (1), including attainment.

For any nonempty prefix with endpoint \(u\), the actual certificate identity is

\[
3^{|W|}q+\operatorname{correction}(W)
=2^{\operatorname{total}(W)}u.
\]

Its correction is positive. Since \(0<u\le q/2\),

\[
3^{|W|}q
<2^{\operatorname{total}(W)}u
\le2^{\operatorname{total}(W)}q/2,
\]

which proves (2). This verification uses the supplied word and its actual endpoints; it does not infer prefix behavior from a density or residue heuristic.

## The residual target and its clock

Choose the unique dyadic octave \(2^d\le q<2^{d+1}\). Integrality gives \(q\le2^{d+1}-1\), so

\[
8q+1\le2^{d+4}-7<2^{d+4}-1=t,
\]

while \(16q+1\ge2^{d+4}+1>t\). This proves (4), including the original low-state near-source exclusion. The target is positive and odd.

Put \(J=d+4\). For the actual ordinary shortcut map,

\[
T^R(2^J-1)=3^R2^{J-R}-1
\qquad(0\le R\le J).
\tag{6}
\]

Each input in the first \(J\) steps is odd, so (6) follows directly by induction. These values strictly increase until time \(J\); in particular they are all at least \(t>2E+1\). Since the constructed source heights are unbounded, the necessary entry clocks are unbounded as well.

## Scope and the unresolved positive step

This family satisfies the low alphabet, \(e=3\), actual complete-source identity, odd target interval, strict prefix coefficient exclusions, and the target's strict exclusion from the maximal literal-cut interval.

It **does not impose** PR177's further retained-even exclusions. In particular, the construction does not force the new odd core to be a multiple of three, or to lie in the surviving unit cells \(q\equiv7\pmod9\) and \(q\equiv19\pmod{27}\). Some or many of these sources can therefore be dispatched by a different existing source rewrite. No cofinality claim is made for the intersection with those remaining cells.

The forward-clock conclusion also **does not rule out a merger at a bounded target time with an arbitrarily long partner clock**. `TargetMergesEnvelope` permits independent clocks and can be strictly more flexible than direct forward entry into the interval. The argument only establishes the stated lower bound for direct target entry.

The prospective global bridge must therefore retain an unbounded target clock, allow an independent partner clock or another source rewrite, or exploit additional surviving residue and source-word structure. No such universal bridge was established in this pass. The precise new obstruction is the sharp cofinal equality (1), together with the actual long-ascent targets (3)--(6), in the scope just specified.

## Provenance

- PR177, commit `a0a0d76f91b4e3846c1b1f0706cad56cb6098317`: `research/lean-exact-witness-global-20261121/lean/Collatz/BoundedGapCofinal.lean`, theorem `cofinal_predecessors`.
- Checkpoint8, commit `03e40fa4d7506ad92682a49c850103b028a11dbe`: the new `SourceEnvelope.lean`, especially `envelope_witness`, `literal_cut_run_bound`, `envelope_maximal`, and `literal_cut_interval_iff`.
- This written follow-up introduces no new analytic hypothesis and assumes neither `LowEnvelopeEntry` nor `LowEnvelopeMerger`.
