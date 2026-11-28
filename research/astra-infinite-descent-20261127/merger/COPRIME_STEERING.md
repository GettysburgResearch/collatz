# Preserving the prime-to-six part of the source progression

**PROPOSED steering construction for an already selected common prefix.** The [finite-profile construction](FINITE_BLOCKS.md) can require the lower source $x$ to belong to an arbitrary fixed arithmetic progression. Its entire finite translate still reaches each ternary-unit target at every sufficiently large supplied common first clock, with one common odd count independent of that clock and target. Its relative-window and counting consequences follow with constants depending on the fixed progression. The proof below handles each factor $n$ coprime to six; the existing source-cylinder construction handles powers of two and three.

The existence of all such progression witnesses has a shorter, fully compiled proof by synchronizing a larger family of translates. That proof even realizes every source residue simultaneously. The construction below instead retains one previously selected common prefix and pays a fixed number of steering slots after it. [AllProgressions.lean](AllProgressions.lean) and [MarkedProgressions.lean](MarkedProgressions.lean)

Write the source modulus as $2^v3^s n$, with $\gcd(n,6)=1$. The case $n=1$ is the earlier theorem. Assume $n>1$. Fix a synchronized prefix of length $H$ as in the finite-profile construction. It writes the lower source as $R+2^H u$ and the shared endpoint as $a+3^p u$ for all $u\ge0$, with $p$ odd departures. Prescribing the source modulo $n$ thus specifies the shared endpoint modulo $n$.

## Ordinary words which can change any residue

For an even step $E$ and an odd step $O$, the two-step words $OE$ and $EO$ have the same length and grade. On the corresponding binary cylinders the final values are $(3z+1)/4$ and $(3z+2)/4$. These are invertible affine maps modulo $n$ since $2,3$ are units.

Starting from any one residue modulo $n$, use exactly $n-1$ such slots. If $S$ is the current nonempty set of reachable residues, the next set is
$$
       S'\ \cup\ (S'+1/4),\qquad S'=(3/4)S+1/4.
$$
We have $|S'|=|S|$. A nonempty proper subset of $\mathbb Z/n\mathbb Z$ cannot be invariant under translation by the unit $1/4$, which generates the whole additive group. Each slot therefore enlarges the set by at least one until it is full. All residues are reachable with exactly $2(n-1)$ steps and $n-1$ odd departures. A particular successful word always defines a nonempty binary cylinder of the free parameter $u$: at each new digit the free affine slope is odd, so flipping the bit toggles the next endpoint parity.

Let $I$ be the multiplicative order of $2$ modulo $n$ and set $K=1+v_3(I)$. Append exactly $K$ odd steps to every steering word. This common suffix is a bijective affine map modulo $n$, so the all-residue steering conclusion still holds. Its ordinary endpoint $w$ satisfies
$$
       w+1=\frac{3^K}{2^K}(z+1),\qquad w\equiv-1\pmod{3^K}.
$$
Here $z$ is the entry to the suffix on its realized binary cylinder. The resulting steering word always has length $W=2(n-1)+K$ and grade $J=n-1+K$.

## Compatibility with the two-gap exponent

Let $L$ be the clock still available for the final two gaps leading into the supplied $y$. The terminal router needs
$$
                           9w+3+2^e=2^L y.
$$
Because of the common suffix, its reduction modulo $3^{K+2}$ requires $2^e\equiv 2^L y+6$. The latter residue is a unit. Choose one exponent $e_0$ solving this common congruence, and prescribe $e\equiv e_0\bmod I$. This fixes the required residue of the terminal $w$ modulo $n$,
$$ w_n=(2^L y-3-2^{e_0})/9\pmod n. $$
Select a steering word sending the shared prefix endpoint's prescribed $n$-residue to $w_n$. It has a binary cylinder $u=u_0+2^W t$. At its end let
$$
R'=R+2^H u_0,\qquad H'=H+W,\qquad p'=p+J.
$$
The lower source is $R'+2^{H'}t$ and the terminal value is $a'+3^{p'}t$ for a definite nonnegative $a'$. Every word gives $a'\equiv-1\bmod 3^K$. For the prescribed source trits $c$, solve $R'+2^{H'}t_0\equiv c\bmod3^s$ and set $A=a'+3^{p'}t_0$. It suffices to require $w\equiv A\bmod3^{p'+s}$.

Put $k=p'+s$. The full required congruence on the unrestricted binary exponent is
$$
           2^e\equiv 2^L y-3-9A\pmod{3^{k+2}}.
$$
Its right side is prime to three; the elementary primitive-root result gives one class of exponents modulo $P=2\cdot3^{k+1}$. Since $k\ge K$ and $A\equiv-1\bmod3^K$, every such exponent lies in the already chosen class $e_0\bmod 2\cdot3^{K+1}$. The greatest common divisor of $I$ and $P$ divides $2\cdot3^{K+1}$. The generalized Chinese remainder theorem therefore adds the constraint $e\equiv e_0\bmod I$. Take the positive solution at most $\operatorname{lcm}(I,P)$.

For every sufficiently large $L$ this gives $0<e<L$ and a positive integer $w=(2^L y-3-2^e)/9$ in the required ternary and $n$-classes. The two ordinary gaps have length $L$ and grade two. The height inequality $2^L y\le16w$ ensures $w>a'$ once $L\ge16(a'+1)$. Use the maximum of $a'$ over the finitely many steering words to make this threshold uniform. Decode $w=a'+3^{p'}t$ to obtain $t>0$ with $t\equiv t_0\bmod3^s$. Since the chosen steering word acts bijectively modulo $n$, the terminal congruence $w\equiv w_n$ gives the specified input residue modulo $n$; multiplication by $3^p$ and $2^H$ is invertible there. The original dyadic cylinder is retained as well.

The initial pattern prefix, the steering bank, and the final router now give one fixed total grade $p+J+2$. Applying the [off-orbit first-arrival leg](FAST_FIRST_HIT_PAIRS.md) adds one more. The grade and clock threshold do not depend on $y$, the terminal clock, or the requested source residue at the prime-to-six and ternary factors when the other fixed prefix data are held fixed. The mixed binary and ternary profile input is now strictly compiled in [BlockClock.lean](BlockClock.lean). The additional prime-to-six steering argument in this note is a written proof. The original elementary ternary router is independently formalized in [TwoGapRouting.lean](TwoGapRouting.lean).

The [finite steering control](check_coprime_steering.py) checks 768 actual word decompositions. It covers $n=5,7$, ternary precisions zero and one, two supplied ordinary profiles, four targets including even target 2, every combined residue, and two terminal clocks per configuration. Checks stay active under optimized Python execution.
