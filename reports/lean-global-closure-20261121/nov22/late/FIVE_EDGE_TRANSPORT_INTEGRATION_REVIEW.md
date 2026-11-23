# Review of exact five-edge transport and the killed-operator selector

Date: 2026-11-22. Reviewer: `global_merger22`.

**Result: VERIFIED, with the stated domains and quantifiers.**

Frozen target: `agent22_certificate/FIVE_EDGE_TRANSPORT.md`.

SHA256:
`0ffaa8cc0a361aa1b9ad69c3c55a5ca4009350eaa97aa07262a0195096118c40`.

The final file was read and hashed. This is a semantic reconstruction of the
written argument, not a new Lean audit. The reviewer contributed the direct
accelerated prefix and the elementary exponent-lifting induction in Section 5.
The original shortcut transport, bounded-routing proof, and certificate lane's
explicit basin selector were separately reconstructed. The collaborator role is
disclosed rather than described as a blind review of the full packet.

## 1. Domains and exact energy recurrences

For the full positive-integer energy, the even inputs contribute exactly one
half of the original energy. On odd inputs the actual relation is
\(T(5n)=5T(n)-2\), with \(n=(2q-1)/3\), giving weight
\(3/(2q-1)\). For the repository energy the domain is already odd and
not divisible by three. Its two residue classes give \(q\equiv2,8\pmod9\)
and no even-input half term. Equations (2) and (3) therefore have the correct
domains and normalizations as extended nonnegative sums.

## 2. Scope of the finite-network obstruction

The signed templates \(-1\mapsto-1\) and
\(-5\mapsto-7\mapsto-10\mapsto-5\) give the positive endpoint ray

\[
(T^{3m}(5n),T^{3m}n)
=(5\,3^{2m}v-5,\ 3^{3m}v-1),\qquad n=2^{3m}v-1.
\]

The ratio of its leading coefficients is \(5/3^m\). If a fixed affine
edge type has a different slope, it contains at most one parameter value
on this ray. This verifies the obstruction to exact closure by finitely
many fixed affine edge types, including reversed orientations.

For the separately stated bounded-routing claim, the permitted generators
are exactly \(x\mapsto5x+b\) and their legal inverses, with \(b\) in a
fixed finite set. Each word has slope \(5^a\), \(a\in\mathbb Z\).
Matching the ray would require \(5=5^a3^m\), impossible for \(m\ge1\).
Each fixed word therefore works at at most one parameter value; finitely
many words of bounded length cannot cover the ray. This does not assert
the same result for an unstated larger graph with additional generators,
or exclude an unbounded routing construction with summable congestion.

## 3. Shortcut amplification

Taking \(v\in30\mathbb N\) puts both the original energy base and the
test target in the odd ternary-unit domain. The target is four modulo
five, so \(E_5(\mathbf1_{\{q\}})=1/q\) with no incoming five-edge term.
The first lifted trajectory hits \(q\) only at the specified clock; the
other trajectory is always zero or three modulo five during that window.
The single original energy base gives the claimed strict ratios.

The strict inequality follows directly from
\((A v-1)/(B v-1)>A/B\) for \(A>B>0\) and \(Bv>1\).
Finite shortcut pullbacks are indeed finitely supported. The theorem
quantifies over a time-dependent family of input point masses; it does
not claim a divergent average for one fixed function.

## 4. Actual accelerated clocks and finite energies

For Section 5's larger lift, \(n=2^{2k}v-1\), the first source has one
halving per odd step through clock \(k\). For the second source the
negative odd template alternates \(-5,-7\), with gaps one and two.
Its accumulated shortcut clock after \(j\) odd steps is
\(j+\lfloor j/2\rfloor<2k\) for \(j\le k\). The remaining binary lift
is even at every relevant endpoint, so these are exact gap counts.

Thus the two formulas in (16) and the modular exclusion of \(q\) on the
second trajectory are valid. They give the accelerated inequalities (17)
with the stated \(k+1\) averaging convention.

Accelerated pullbacks need not have finite support. The note handles this
correctly: every legal parent of \(q\) is \((2^aq-1)/3\), and

\[
\sum_{Ux=q}\frac1x\le\sum_{a\ge1}\frac6{2^aq}=\frac6q.
\]

This implies the harmonic norm bound for composition by \(U\).
The estimate \(E_5(h)\le6\|h\|_{\mathrm{harm}}\) follows because the
reindexed \(h(5n)\) part has coefficient five. Therefore every fixed
accelerated iterate and finite average used in the counterexample has
finite energy despite its potentially infinite support.

## 5. The explicit basin selector and killed-domain conclusion

The exponent construction is valid for every required power of three.
Starting from \(b=1\), the congruence

\[
16^{3^{r-1}}\equiv1+5\,3^r\pmod{3^{r+1}}
\]

follows by cubing inductively. If \(7\,2^b+1=3^r c\), replacing
\(b\) by \(b+4j3^{r-1}\) changes its quotient modulo three to
\(c-5j\equiv c+j\). Choosing \(j\equiv-c\pmod3\) lifts the
divisibility and preserves \(b\equiv1\pmod4\). No external
arithmetic-progression theorem is required.

With \(r=2k+2\), the selected

\[
v=\frac{2(7\,2^b+1)}{3^{2k+1}}
\]

is positive, even, divisible by three, and divisible by five. The last
fact follows from \(b\equiv1\pmod4\). Hence \(v\in30\mathbb N\).
For \(q=6^kv-1\), another \(k\) exact unit gaps give

\[
U^kq=3^{2k}v-1=(7\,2^{b+1}-1)/3.
\]

Its next odd image is seven, with exact gap \(b+1\). The chain
\(7\to11\to17\to13\to5\to1\) has the displayed gaps
\(1,1,2,3,4\). This is a complete actual certificate for \(q\), and
prefixing the known \(n\to q\) segment certifies \(n\). Both exceed
one, so both are nonperiodic.

For the point mass at this nonperiodic target, a full odd trajectory
that has entered a periodic state can never contribute later. Full
\(U\)-pullbacks therefore agree exactly with the zero-extended killed
pullbacks. This is true whether or not \(5n\) is itself nonperiodic.
It proves (23) on the same killed domain used by the Dirichlet note,
without an unproved nonperiodicity or Collatz assumption.

The construction repairs the distinction between shortcut and accelerated
composition; it does not infer one operator bound from a theorem about the
other. The resulting obstruction is to a uniform bound over arbitrary
finitely supported inputs. It does not rule out additional estimates for
the particular canonical Green potential. No correction is required to
the final frozen argument.
