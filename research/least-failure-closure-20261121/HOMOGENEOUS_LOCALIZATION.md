# What prescribed-endpoint localization preserves

**PROPOSED, elementary ordinary-path result.** A paired prefix with equal
odd count and equal shortcut clock preserves complete homogeneous
five-transport recognizability exactly. In particular, placing every
comparison in one sufficient residue class does not make the endpoint
certificate compatible with this compiler.

The comparison source is PR146 at
`fd991063721e9c157d318e40bb20131762f7d750`,
`research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`.
The decoder source is `HOMOGENEOUS_FIVE_TRANSPORT.md`, SHA256
`f2872fad5c04e3aba9219f4b54576ef438d2922d7dcad9b0a8423974c4d2c31b`,
HT1–HT2. The elementary paired ladder used below comes from PR166 at
`5996b9f525ca50978bc34f423192c36a87765bf3`, FL1.

## LC1. Exact cancellation of a paired prefix

Write \(T\) for the ordinary shortcut map. Suppose positive odd inputs
\(x,5x\) follow actual prefixes of the same shortcut length \(L\),
with the same number \(p\) of odd inputs, ending at \(q,5q\), where
\(q\) is odd. Let the corresponding accelerated words be
\(\alpha,\alpha^*\). Suppose the source prefix does not hit 1 before its
endpoint, and a first-hit word \(\beta\) for \(q\to1\) is supplied.
If \(q=1\), take \(\beta\) to be the empty word.

Call a source word \(w\) **homogeneously recognizable** when the HT1
decoder supplies an actual target word, with the same odd count and clock,
from five times the source to five times its endpoint. For a complete
source witness, this endpoint is 1 and the target endpoint is 5; the
final edge \(5\to1\) is appended afterwards. The empty endpoint word at
\(q=1\) is recognizable, with the empty target word at 5.

**Theorem LC1.** The complete word \(\alpha\beta\) is homogeneously
recognizable if and only if \(\beta\) is. When recognition succeeds,
its target word is exactly \(\alpha^*\beta^*\).

**Proof.** A target suffix \(\beta^*\) can be concatenated with the
given paired prefix, proving sufficiency. Conversely, suppose a complete
homogeneous target word exists. Ordinary dynamics is deterministic, so
its first \(L\) shortcut steps are the supplied prefix from \(5x\) to
\(5q\). That endpoint is odd, and exactly \(p\) odd inputs have been
consumed. Removing this prefix leaves an actual target suffix from
\(5q\) to 5 with exactly the clock and odd count of \(\beta\).
This is precisely recognition of \(\beta\). HT1 uniqueness identifies
the concatenated target word. If \(\beta\) is empty, the given prefix
itself ends at 5 and proves the assertion.

There is no hidden earlier target first hit: a positive ordinary path
that has hit 1 remains in \(\{1,2\}\), whereas the paired endpoint is
\(5q\ge5\). The source hypothesis makes \(\alpha\beta\) its actual
first-hit word. QED.

The proof concerns complete homogeneous transports, not just a chosen
factorization into short blocks. Enlarging the dictionary or allowing a
block to cross the prefix boundary cannot avoid the cancellation.

## LC2. Application to the latest single-progression lift

PR146 uses the paired 71-clock prefix

\[
a=6\,375\,551\,795\longmapsto v=1\,215\,835,
\qquad 5a\longmapsto5v,
\]

with 37 odd inputs on each arm. For its prescribed-endpoint lift,

\[
k=(2^bq-v)/3^{37},\qquad x=a+2^{71}k,
\]

the 71-step endpoints are \(2^bq,2^b5q\), followed by \(b\) halvings.
Thus the full paired prefix has clock \(71+b\) and still 37 odd inputs.
For the nonnegative \(k\) selected by that construction, its earlier
states are at least the corresponding seed states. The seed does not
hit 1 during its prefix; the final halvings first reach 1 only at their
endpoint when \(q=1\). LC1 therefore applies to every such lift of a
supplied first-hit witness.

Consequently the complete homogeneous decoder accepts the lifted witness
exactly when it accepts the prescribed endpoint witness. This also holds
on the refined binary and ternary subprogressions in PR146. Localizing
the physical five-closure criterion to a single progression is valid;
homogeneous certificate recognition on that progression still requires
the full endpoint recognition problem.

The finite seed itself supplies a direct control. Its complete first-hit
data are

| Start | Odd inputs | Shortcut clock |
|---|---:|---:|
| \(v=1\,215\,835\) | 78 | 144 |
| \(5v=6\,079\,175\) | 67 | 129 |
| \(a=6\,375\,551\,795\) | 115 | 215 |
| \(5a=31\,877\,758\,975\) | 104 | 200 |

Both supplied source witnesses fail homogeneous recognition. All four
ordinary paths nevertheless have explicit first-hit certificates. The
checker replays the seed prefixes and these four certificates directly.

## LC3. An infinite known-convergent family inside the covered ladder class

For every integer \(j\ge1\), put

\[
x_j=\frac{7(64^j-1)}9.
\]

The recurrence \(x_1=49\), \(x_{j+1}=64x_j+49\) proves that these
are positive odd integers, all 49 modulo 64, with
\(x_j\equiv j\pmod3\). Hence the indices \(3\nmid j\) give odd
ternary units in the covered ladder class.

The complete ordinary first-hit exponent words are

\[
\begin{aligned}
x_j&:\quad(2,6j-2,1,1,2,3,4),\\
5x_j&:\quad(5,6j-5,1,5,4).
\end{aligned}
\]

Indeed the first two source exponents send \(x_j\) to 7, while the
first two target exponents send \(5x_j\) to 35. Their common prefix
clock is \(6j\), with two odd inputs on each arm. The remaining words
are the literal first-hit words of 7 and 35. All listed exponents are
positive, including \(6j-5\ge1\).

The source certificate has rank 7 and clock \(6j+11\); the target has
rank 5 and clock \(6j+10\). The source-7 suffix fails HT1 recognition,
so LC1 proves that every source \(x_j\) fails it too. At \(j=1\),
the paired prefix is simply

\[
49\to37\to7,\qquad245\to23\to35.
\]

Thus even an infinite family of explicit known-convergent comparisons
inside the covered initial class need not admit complete homogeneous
transport from their supplied first-hit source witnesses. A known-base
table can handle selected endpoints such as 7; that is additional input,
not a consequence of homogeneous prefix compilation.

## LC4. Scope and verification

These results do not contradict five-closure and do not rule out adaptive
transport with different clocks, different odd counts, other endpoints,
or independently certified terminal families. A prescribed-endpoint lift
may retain useful later nonhomogeneous transports. The exact conclusion
is that a homogeneous prefix cannot repair the homogeneous recognition
status of its supplied endpoint certificate.

`check_homogeneous_localization.py` is self-contained. It replays the
71-clock seed, the explicit first-hit witnesses, small-constant lifts
with both successful and unresolved endpoint recognition, the empty
\(q=1\) case, and selected members of the whole symbolic family in LC3.
The universal assertions follow from LC1 and the displayed formulas;
they are not inferred from a census. The script uses explicit checks
which remain active under `python3 -OO`.
