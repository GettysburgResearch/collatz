# Exact additional cost when the principal source is highly divisible by three

Use the matching-depth seven-phase setup of `ADAPTIVE_POSITIVE_ANCHORS.md`. Thus $R=7k+a\ge7$, $H=11k+h_0$, $n=2^{H+1}z-17$, $X=2\cdot3^Rz-t$, and $n$ reaches $X$ in exactly $R$ genuine positive odd departures. The symbol $h$ below is an extra odd budget and is separate from the marked phase's physical offset $h_0$. Fix $s\ge1$. The preceding positive-anchor result gives $M_{R+s}(X)=n$ when $3^s\mid n$. The issue here is what happens *past those extra $s$ departures*.

**Theorem 1.** For fixed $s\ge1$ and $h\ge0$, there is some such ordinary class with $3^s\mid n$ and a smaller visitor through $R+s+h$ if and only if the following arithmetic test succeeds.

1. Choose a positive odd $w<17(3/2)^h$. Follow its positive accelerated orbit for exactly $s$ steps to $c=U^s(w)$ and record their total division exponent $E$.
2. Choose an integer $D\ge1$ such that $m=17\cdot2^D-c>0$ and
   \[
                            2^{D+E+h}<3^{s+h}.
   \]
3. The first reflected accelerated visit of $m$ to 17 must occur at odd and physical clocks $(7\ell,11\ell+D)$ for some $\ell\ge0$.

If this succeeds, **each** of the seven phases admits the cheaper visitor on infinitely many cofactors for every sufficiently large lap count $k$. If it fails, **every** phase, cofactor and budget $R$ in the stated domain is protected through $R+s+h$. The positive source $w$ stays inside one fixed finite pool when $h$ is fixed, independently of $s$ and $R$.

For necessity, a strict challenger uses $R+s+j$ odd departures, $1\le j\le h$, by the earlier $s$-step protection. Cut after its first $j$ forward departures at $v$, and after the next $s$ at $u$. Since $3\mid n$, $u$ cannot equal $n$; a positive odd multiple of three has no proper odd predecessor. The remaining $R$ proper departures to $X$ give $u=2^Dn+c$ with $D\ge1$ and $0<c<17\cdot2^D$ by the matching-depth positive displacement theorem. Put $m=17\cdot2^D-c$. Its signed clocks at first 17 satisfy the grade in step 3: append the marked orbit from $t$ to 17 until both compared paths have reached 17, and remove their whole laps after first arrival.

Project the $s$ ordinary inverse exponents at $u$ to the **positive odd anchor $c$**. The full displacement $2^Dn$ is even and divisible by $3^s$. Thus $c=U^s(w)$ for a positive odd $w$, $v=2^D(2^E/3^s)n+w$, and $w<(2^E/3^s)c$. Since every inverse exponent is at least one, the $j$ earlier inverse steps satisfy
\[
                  y+1\ge(2/3)^j(v+1).
\]
The strictly cheaper integer $y$ obeys $y+1\le n$, and hence $2^D 2^E/3^s<(3/2)^j\le(3/2)^h$. This gives step 2 and $w<17(3/2)^h$.

Conversely fix successful data. For any chosen phase and $k\ge\max(1,\ell)$, choose an odd ordinary $n=3^s N$ satisfying
\[
 n\equiv-17\pmod{2^{H+1}},\qquad 2^{D+E}N+w\equiv-1\pmod{3^h}.
\]
These are independent congruences on $N$, so the Chinese remainder theorem gives arbitrarily large positive solutions. They give a positive cofactor $z=(n+17)/2^{H+1}$, automatically coprime to three. The signed path from $m$ first reaches 17 after the prescribed clocks, then follows $k-\ell$ whole laps and the marked prefix. Its positive lift $u=2^D n+c$ has displacement $u+m=2^D(n+17)$ and reaches $X$ in $R$ departures. The actual positive path from $w$ to $c$ lifts to the $s$-step path from $v=2^{D+E}N+w$ to $u$. Finally $3^h\mid v+1$ permits $h$ genuine exponent-one inverses at $v$. Their result satisfies
\[
          y=\frac{2^{D+E+h}}{3^{s+h}}n+(2/3)^h(w+1)-1.
\]
The coefficient is strictly smaller than one and the constant is fixed, so all sufficiently large positive choices give $0<y<n$. No minimization over a longer signed word is used.

The test is finite and effective for each supplied $s,h$, even without a stopping conjecture for the reflected map. The range of $w$ is explicit, its $s$ ordinary steps are finite, and step 2 bounds $D$. If step 3 succeeds, the first-arrival path has $7\ell$ distinct positive reflected odd states; telescoping their factors as in the extra-budget note gives
\[
                 1\le17\cdot2^D(7\ell+1)(2048/2187)^\ell.
\]
After a computable cutoff the right side is strictly below one and decreases, by its exact consecutive-term ratio. Thus only finitely many reflected odd clocks need be inspected for each $D$. The implementation uses this bound and stops earlier at a first 17 or repeated state.

## Uniform conclusions over unbounded $s$

For each fixed $h$ in the table, the stated set of $s\ge1$ is **complete**: every listed rank has infinitely many ordinary counterexamples to protection on every phase at sufficiently large lap count; no other positive rank admits any.

| Extra $h$ beyond $R+s$ | Every $s$ permitting a strict visitor on some cofactor |
|---:|---|
| 0 | none |
| 1 | none |
| 2 | none |
| 3 | 1 |
| 4 | 1, 2, 3 |
| 5 | 1, 2, 3, 4, 7, 9 |
| 6 | 1 through 9, 25, 27 |

In particular, **for all $s\ge1$ with $3^s\mid n$, $M_{R+s+2}(X)=n$.** Every $s\ge2$ is protected through $R+s+3$. The nonmonotone sets in the table refer to $s$ together with the budget $R+s+h$.

For fixed $h\le6$, follow the complete finite ordinary pool $w<17(3/2)^h$. Each actually reaches 1. Once a state equals 1 its next exponent is two, so each further step multiplies $2^E/3^s$ by $4/3$. Stop that row once the displayed step-2 inequality fails even at $D=1$ while at 1; it can never hold again. This proves the bounded finite calculation covers **all** $s\ge1$. The largest last inspected ranks for $h=1,2,3,4,5,6$ were respectively 7, 41, 41, 42, 44, 45. The $h=0$ assertion is the preceding unbounded $s$-step protection theorem, or follows from the same test. The test enumerates all successful triples internally. Its frozen JSON records the successful ranks and selected actual CRT witnesses for the last permitted rank of each nonempty row; the separate independent replay checks every successful tuple on every marked phase.

For example, at $h=6$, $s=27$, the true positive path from $w=27$ reaches $c=1619$ after 27 odd departures and 37 divisions. The corresponding $D=9$, $m=7085$ reaches reflected 17 for the first time after $(28,53)$ clocks. At the 17 phase take $R=28$, $z=4440689058311830$. The ordinary principal source $156242856158448409148716482543$ is beaten by $126578090011795928556638166783$ with 61 odd departures to the same terminal. This example asserts strict improvement, not that this visitor is the least among all 61-step paths.

**Fixed-root implication.** At any fixed $h$, if successful ranks $s$ were unbounded, at least one *fixed ordinary* $w<17(3/2)^h$ would have a non-eventually-periodic trajectory. Otherwise every orbit in this finite pool eventually follows a positive cycle, and the inverse multiplier over each whole cycle is strictly greater than one. For each $w$, $2^E/3^s$ would therefore tend to infinity, eventually contradicting step 2 even at $D=1$. Finiteness of the pool gives a common cutoff. The table checks the small pools directly. No premise that arbitrary positive starts converge is used, and the existence of such an unbounded set of successful ranks is open here.
