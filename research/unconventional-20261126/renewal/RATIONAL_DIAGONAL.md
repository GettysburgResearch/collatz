# An escaping ordinary ray must leave the rational diagonal at its records

**Status — PROPOSED actual-orbit theorem.** Let $K_2,K_3$ be the
dyadic and ternary cluster sets of the strict coefficient-record
values $q_l$ of a single nonrepeating positive ordinary odd ray.
Let $K_{2,3}$ be their joint cluster set. All use subsequences
of the *same* record values. The ray has cofinal strict coefficient
records by [the simple-path distortion estimate](README.md).
For an odd dyadic point, a finite coefficient upcrossing means a
finite string of genuine odd gaps with $3^m>2^s$, where $s$ is its
native clock. Call a dyadic point periodic when it lies on a cycle
of the native map itself.

**Theorem D.**

1. $K_2$ cannot consist entirely of periodic dyadic points each
   having a finite coefficient upcrossing. In particular it cannot
   consist entirely of negative signed periodic points. If every
   point in $K_2$ is periodic, then some point of $K_2$ is on a
   positive rational cycle and has no finite coefficient
   upcrossing from its phase.
2. If the successive odd record gaps are bounded, $K_3$ contains
   a point outside $\mathbb Q\cap\mathbb Z_2^\times\cap\mathbb Z_3$.
   This excludes an arbitrary collection of odd-numerator,
   odd-denominator rational phases, including a countably infinite
   one. It makes no assumption on $K_2$.
3. Without any bound on record gaps,
   $K_{2,3}$ contains a point outside
   $\{(u,u):u\in\mathbb Q\cap\mathbb Z_2^\times\cap\mathbb Z_3\}$.
   No finiteness, density or positive limiting record mass is assumed.

These conclusions allow a pair of distinct rational local values.
The [symbolic long-gap construction](ESCAPE_OF_MASS.md), for
example, has the singleton local pair $(1,-1)$ and an irrational
dyadic initial source. It is not a positive ordinary realization.

## A finite-alphabet fact

Consider a closed shift-invariant two-sided subshift $Y$ on a finite
alphabet. If the right-infinite ray starting at every point of $Y$
is purely periodic, then $Y$ is finite and consists of periodic
orbits. The same conclusion holds with left and right interchanged.

Indeed let $X$ be the compact set of right-infinite tails in $Y$.
The one-sided shift is onto $X$. It is injective there: two purely
periodic sequences with the same shifted tail agree also at their
first letter, by using a common multiple of their periods. The inverse
map is continuous by compactness. Hence the bit or symbol preceding
a tail in $X$ is determined by its first $k$ letters, for one uniform
finite $k$. Consider the finite directed graph of length-$k$ factors
of $X$ and its actual length-$(k+1)$ transitions. Every vertex has
exactly one incoming edge and at least one outgoing edge. Summing
degrees gives exactly one outgoing edge at every vertex. Thus each
sequence follows one of finitely many simple cycles, proving the
claim. Eventual periodicity of each tail would not give injectivity.

For a one-sided word on a finite alphabet define its two-sided
omega subshift by all limits seen from positions tending to infinity.
Its factors are exactly the factors occurring arbitrarily late,
by compactness and finite alphabet. If this omega subshift is finite
and consists of periodic orbits, the original word is eventually
periodic: take long enough blocks to distinguish all periodic
phases and force unique continuation in that finite subshift. All
other blocks of this fixed length plus one occur finitely often
in the original sequence, so its sufficiently late tail follows
one of the forced periodic cycles.

Native parity words determine their dyadic sources uniquely. For a
fixed length $n$ word of weight $p$, its affine numerator
$3^px+C$ must vanish modulo $2^n$, with $3^p$ invertible there.
Thus equality of infinite native parity words is equality of
dyadic sources. The native map is continuous on $\mathbb Z_2$
because its two parity branches are clopen. In particular eventual
parity periodicity on an ordinary ray would force a repeated
positive integer.

## Dyadic centers and the bounded-clock implication

If the odd record gaps have an unbounded subsequence, take their
starting values $q_l$ along a further convergent dyadic subsequence.
Its limit $x$ has no finite coefficient upcrossing. Any such crossing
at $x$ would be read from a finite native-word cylinder, with the
terminal odd bit included. The same crossing would then occur
from every sufficiently close $q_l$, contradicting first-ladder
lengths tending to infinity.

Suppose now that all points of $K_2$ are periodic and have a finite
upcrossing. The preceding paragraph gives bounded odd gaps, hence
bounded *native* time between successive records, since the clock of
a first-ladder word of length $m$ is $\lfloor m\log_2 3\rfloor$.
Take an arbitrary two-sided native parity omega word of the supplied
ordinary trajectory. Each of the centers realizing it is within a
bounded forward time $c$ of its preceding record. Pass to a subsequence
with $c$ fixed and these record values converging in $\mathbb Z_2$
to $x\in K_2$. The entire right-infinite parity tail from the center
then equals the native tail from $T^cx$, by continuity at every fixed
number of steps. This is purely periodic because $x$ is periodic.
The finite-alphabet fact now makes the original word eventually
periodic, contrary to its nonrepetition. This proves the first
assertion in part 1.

Every periodic dyadic point is rational by the native affine-word
fixed-point identity. A nonzero periodic point of odd starting parity
has a finite odd lap whose multiplier is different from one. The
cycle has one sign because the positive half-line is forward
invariant. On a negative cycle the multiplier on a lap is greater
than one, either from the strictly positive additive carry in its
fixed-point identity or by multiplying the local ratios. Therefore
a periodic odd point with no finite coefficient upcrossing must
belong to a positive rational cycle. This proves the rest of part 1.

## Ternary centers and a purely periodic *past*

For every actual coefficient record, every nonempty backwards suffix
has inverse multiplier $2^s/3^m<1$. Every ternary cluster point
therefore belongs to the compact critical trace $\mathcal R$.
We use the precise signed-rigidity result in PR210, section 4,
at the frozen head linked below: if an odd-numerator, odd-denominator
rational $v\in\mathbb Z_3$ has an infinite backwards critical code,
then $v$ lies on a negative rational odd cycle and *every* such
code is the purely periodic backward cycle code from that phase.
This purity, stronger than eventual periodicity for a general
rational, is essential. [Signed rational rigidity, Theorem R1](https://github.com/GettysburgResearch/collatz/blob/592328fecf8ea2cf41736294856d95f890a1ba98/research/critical-record-rational-rigidity-20261125/README.md)

Assume bounded record gaps and suppose every point of $K_3$ is
a rational dyadic unit. For any two-sided native parity omega
word, its realizing centers lie a bounded native time *before*
some record. Take a subsequence with this offset fixed and those
records converging in $\mathbb Z_3$ to $v\in K_3$. Their backwards
odd-gap suffixes admit a coherent infinite subsequential limit:
for every fixed depth $j$ their clocks are less than
$j\log_2 3$, so only finitely many such prefixes occur. Every
limiting gap script is critical, and its finite inverse congruences
hold at $v$, by taking limits at each fixed depth. The rational
rigidity result identifies it with the genuinely periodic signed
backward code at $v$. Expanding each odd gap into its native bits
therefore gives a purely periodic left-infinite parity tail at
that terminal record. Dropping the fixed offset gives a purely
periodic left-infinite parity tail at the original center.
Its direction is immaterial to the finite-alphabet fact. Thus the
actual word would again be eventually periodic. This proves part 2.

For part 3 suppose all joint limits were rational diagonal points.
Every dyadic record cluster point $x$ occurs in such a pair by
compactness of $\mathbb Z_3$. Its common rational value also lies
in $\mathcal R$ and is a dyadic unit. The same rigidity result
makes it a negative signed periodic point. This contradicts
part 1. In particular any finite list of rational diagonal
neighborhoods, with radii taken sufficiently small, misses
infinitely many records. The proof gives no exclusion for a
specified pair of *different* rational local limits.
