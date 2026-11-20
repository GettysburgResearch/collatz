# Independent review: guarded clocks and certified CRT sources

**Verdict: VERIFIED at the claims and file hashes identified below.** This
review does not prove a Collatz closure theorem. It verifies an obstruction
to a bounded-clock method and the construction of genuine convergent upper
antecedents witnessing that obstruction.

Reviewer: the separate `critical_source_proof` agent. The proof was
reconstructed directly, and `check_guarded_clock.py` was written without
importing either author's checker. Review date: 2026-11-20.

## Frozen review boundary

The sources were local proposed manuscripts, not yet immutable GitHub
commits. Their SHA-256 hashes freeze the actual inspected bytes:

| Manuscript | SHA-256 | Reviewed claims |
|---|---|---|
| `GUARDED_CLOCK_OBSTRUCTION.md` | `6ebeea93c0be7e9848e71e9f36c0a6e554a081200be77c6509273791a91a817a` | G1--G4: guarded graph, source CRT ordinary-clock obstruction, genuine certified upper instances, bounded low-ceiling consequence |
| `BASIN_CRT_DENSITY.md` | `20f2aad14abfac6c5a238674bb649c7b40c53465ac882c0c097a51a9d42cabbf` | The all-progression existence lemma and its explicit first-hit certificate construction |

The first manuscript was read at
`collatz-deep/research/deep-reverse-closure-20261120/`; the second at
`agent_ordered_arithmetic/`. These verdicts do not automatically extend
to later revisions or neighboring assertions.

Throughout,

\[
T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n,\end{cases}
\qquad C=\{n>0:T^j(n)=1\text{ for some finite }j\}.
\]

## 1. The ordinary short-meeting obstruction

The exact assertion is that, for an integer \(L\ge1\) and \(N>1\)
with

\[
N\equiv1\pmod{3^L},\qquad N\equiv-1\pmod{2^L},
\]

there is no smaller positive \(y<N\) satisfying
\(T^iN=T^jy\) with \(0\le i,j\le L\). This statement concerns actual
integer meetings and permits unrelated forward clocks on the two arms.

The binary congruence gives, for every such \(i\),
\(N=2^iu-1\) and \(T^iN=3^iu-1\). Consider the actual reverse word of
length \(j\) from that meeting to \(y\), containing \(q\) odd-input
inverses. Its elementary inverse maps are \(v\mapsto2v\) and
\(v\mapsto(2v-1)/3\).

If \(q\le i\), apply the same affine word to \(-1\). The two paths
differ initially by \(3^iu\), so the available factors of three ensure
integrality at every reverse odd operation on the comparison path. This
comparison does not require positive ordinary legality. Its endpoint is
\(-M\), where \(1\le M\le2^{j-q}\): doubling doubles the magnitude,
whereas the odd inverse cannot increase it at a negative integer of
magnitude at least one. Consequently

\[
y=2^j3^{i-q}u-M
\ge2^{j-q}(2^q3^{i-q}u-1)
\ge2^iu-1=N.
\]

The last inequality uses \(j\ge q\) and \(3^{i-q}\ge2^{i-q}\).

If \(q=i+d\) with \(d\ge1\), split the forward word from \(y\) after
its first \(d\) odd inputs, at clock \(J\). Its suffix has exactly
\(i\) odd inputs. The preceding equal-odd-count comparison expresses
the suffix starting value as

\[
w=2^bN+c,\qquad b\ge0,\quad0\le c\le2^b-1.
\]

The full inverse prefix is an affine function of \(N\), with slope
\(\alpha=2^{J+b}/3^d>0\). Replace \(N\) by 1. Since
\(3^d\mid N-1\), the same successive divisibility check shows that
every intermediate comparison value is integral. Starting at
\(2^b+c>0\), each integral inverse remains positive, giving an endpoint
\(\beta\ge1\). Replacing \(N\) by \(-1\) starts at
\(c-2^b\le-1\); even without asserting integrality on this second
comparison, both inverse maps preserve the half-line \(( -\infty,-1]\).
Its endpoint is \(\beta-2\alpha\le-1\). Thus
\(\alpha\ge(\beta+1)/2\ge1\), and

\[
y=\alpha(N-1)+\beta\ge N.
\]

All divisions and sign conditions in this reconstruction are justified;
there is no random-parity premise.

An undirected ordinary walk reduces to a forward arm followed by a
backward arm by cancelling a backward edge immediately followed by a
forward edge. Determinism of \(T\) makes the pair a literal retracing.
Repeated cancellation leaves no backward-then-forward pair. Both
remaining clocks are bounded by the original total length, so the
short-meeting statement indeed forbids every undirected ordinary walk
of length at most \(L\) to a smaller state. This includes walks with
arbitrary intermediate heights.

## 2. The guarded obstruction is genuinely directed

For a fixed eligible upper \(X=128h+1\), the extra arrows are exactly

\[
64j+1\longrightarrow128j+1,
\quad j>0,\quad4\nmid j,\quad128j+1<X.
\]

They are not reversible edges. The obstruction to an arbitrary directed
path uses only its **first** extra arrow, so subsequent choices and
heights cannot invalidate the reasoning.

For \(H\ge1\), take \(L=H+6\) and a CRT source as in Section 1. Put

\[
h=(N-1)/27,\quad X=128h+1,
\quad Y=64h+1,\quad z=(3N-1)/4.
\]

Here \(h>0\), \(h\equiv2\pmod4\), and the exact shortcut words give
\(T^6Y=N\) and \(T^9X=z<N\). The four odd valuations of \(X\) are
\((2,2,2,3)\), so this is precisely the fourth-gap-three domain.

If the first extra arrow is encountered after at most \(H\) ordinary
edges, its strict guard gives \(j<h\). Its lower endpoint has the
literal six-step path

\[
T^6(64j+1)=27j+1<N.
\]

Appending that path to the preceding ordinary walk contradicts Section 1
at length at most \(H+6=L\). If no extra arrow occurs, reaching any
smaller endpoint within \(H\) edges directly contradicts the same
theorem. Thus every guarded path from \(N\) to any smaller state has
more than \(H\) ordinary edges before its first extra arrow or its
arrival, respectively.

The strict inequality is necessary for this proof: when \(j=h\), the
six-step endpoint is \(N\) itself. The checker preserves this negative
control. No assertion is made that such a finite path fails to exist
altogether.

Starting an atlas at \(Y\) instead of \(N\) does not evade the uniform
bound: prepend the six ordinary edges from \(N\) back to \(Y\).
Likewise, an ordinary arrival at the known \(X\) can be followed by its
nine-step path to \(z<N\). These are fixed changes of the clock bound,
whereas the obstructing precision \(H\) is arbitrary. This observation
does not apply to an endpoint justified only by an unbounded portion of
the supplied certificate; such a procedure is among the deliberately
unexcluded source-dependent possibilities.

## 3. Actual certified upper antecedents

The basin lemma is elementary and sufficient. Given any residue
\(r\pmod{2^a3^b}\), choose a positive representative \(w\) of the binary
class with \(1\le w\le2^a\). Its first \(L_0=a+1\) shortcut inputs
contain \(q\ge1\) odd inputs. On its complete binary cylinder,

\[
T^{L_0}n=(3^qn+B)/2^{L_0},
\quad B\ge0,\quad3\nmid B.
\]

The last odd contribution to \(B\) is a power of two and every earlier
odd contribution is divisible by three, proving the unit condition.
Since two generates the units modulo \(3^{q+b}\), there are arbitrarily
large exponents \(A\) with

\[
2^{L_0+A}\equiv B+3^qr\pmod{3^{q+b}}.
\]

Then
\(n=(2^{L_0+A}-B)/3^q\) is a positive integer in both prescribed
congruence classes. Its exact binary prefix ends at \(2^A\), and
\(A\) subsequent halvings reach one. Thus this is an actual ordinary
certificate, with all exponents finite, rather than a completion point
or an infinite binary itinerary.

Applied to

\[
z\equiv-1\pmod{2^{L-2}},\qquad
2z\equiv1\pmod{3^{L+1}},
\]

the lemma gives infinitely many \(z\in C\). The associated
\(N=(4z+1)/3\) satisfies the two source congruences. Therefore \(X\)
also belongs to \(C\), with its four-odd-input prefix followed by the
supplied certificate for \(z\).

This does not require a positive natural or harmonic density theorem.
The lemma gives infinitely many basin members in each fixed arithmetic
progression, and that is its precise density meaning. It neither
certifies the companion \(N\) nor asserts that it fails to converge.
The obstruction remains a method obstruction on genuine convergent
upper antecedents.

## 4. Bounded ceilings and exact computational controls

For a source \(N\), an added arrow whose upper is at most \(cN\)
satisfies

\[
T^6(64j+1)\le(27cN+101)/128.
\]

When \(c<128/27\), this is smaller than \(N\) for sufficiently large
\(N\). A uniformly bounded-clock atlas at such a ceiling would
therefore supply a uniformly bounded ordinary walk to a smaller state,
contrary to Section 1. The special ceiling \(3N\) works for \(N\ge5\).
No argument here excludes adaptive or certificate-dependent unbounded
ordinary clocks.

The separate exact checker supplies the following controls:

- For \(L=1,\ldots,9\), three CRT sources at each precision, all forward
  roots \(T^iN\) with \(0\le i\le L\), and **complete** predecessor
  layers through depth \(L\): 27 instances, 7,830 predecessor nodes
  counted with root and depth. Every tested positive predecessor is at
  least its original \(N\). Parent lists include both possible ordinary
  predecessors with exact legality checks.
- 14,846 eligible earlier-arrow identity checks. Small index ranges are
  exhausted and larger ones are explicitly only boundary/interior
  samples; the universal identity is established by the proof.
- Exact counterexamples when each CRT condition is dropped: \(15<23\)
  with \(T(15)=23\), and \(T(28)=14<28\).
- Five genuine certified instances, for \(H=1,2,4,8,16\). Their
  arithmetic is represented as integer-affine expressions in a symbolic
  power of two. Every short prefix parity, integrality condition,
  positivity condition, and absence of an early first hit is checked
  exactly. The terminal power-of-two halving run is compressed by its
  explicit exponent, not replayed or silently assumed.

The largest displayed compressed certificate has
\(E=8119465379982947549\) in \(2^E\), terminal halving count
\(8119465379982947528\), and exact upper odd rank 24. This is not a
claim to have executed that many shortcut steps. Modular exponentiation
and rational-affine identities verify the compressed certificate in
finite time.

Commands actually executed successfully:

```bash
python -B agent_critical_source/check_guarded_clock.py --output agent_critical_source/guarded_clock_report.json
python -OO -B agent_critical_source/check_guarded_clock.py --compare agent_critical_source/guarded_clock_report.json
```

The report comparison is byte-for-byte. The complete predecessor-tree
transcript hash is
`61113ad88ac6d196bd84edc817df9eac3bf9568e8351a54cddbb8adc36037b81`.
No universal theorem is inferred from these finite controls.

## 5. Remaining mathematical obligation

The verified obstruction rules out a finite atlas of bounded ordinary
words as the proposed global guarded closure mechanism, already in the
fourth-gap-three family. It leaves open a source- or certificate-dependent
selector with arbitrarily long finite ordinary paths. Proving that such a
selector terminates and reaches a justified convergent endpoint is still
necessary; the CRT basin lemma does not provide that selector.
