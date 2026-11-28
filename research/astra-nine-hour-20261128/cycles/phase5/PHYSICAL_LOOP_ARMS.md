# Full-lap affine arms on positive integers

Let $T$ be the positive integer shortcut. An actual return at $c$ of $n$ clocks and $u$ odd steps gives
$$ T^n(c+2^nt)=c+3^ut                                                        \tag{1}$$
for every integer $t$ whose source is positive. Its $n$-bit parity prefix agrees with the prefix from $c$, by dividing the initial difference through the prescribed steps. The right side is necessarily positive. Conversely the replacements between the two expressions in (1), in either direction when both are positive, preserve forward-orbit intersection. This note tests whether combining such laws at two hypothetical distinct ordinary cycles can force their basins to merge.

### What the actual domains generate

The global equivalence $x\sim 2x$ together with **one rotation of the standard return, centered at two**, already generates the entire ordinary undirected Collatz equivalence on positive integers. Its exact arm is
$$                     2+4t\ \sim\ 2+3t,\qquad t\ge0.                  \tag{2}$$
For odd $y=1+2t$ apply global doubling and (2) to obtain $y\sim 2y=2+4t\sim 2+3t=T(y)$. For even $y$ global doubling alone gives $y\sim T(y)$. Conversely all arrows in these two generators are true shortcut orbit equivalences. Adding any other genuine return arm therefore preserves exactly this same equivalence relation. A successful argument that the enlarged group connects every other cycle to one would already establish the requisite ordinary orbit intersection within (2) and doubling. Algebraic group calculations that erase the domains of these arrows change the problem.

Without global doubling, for growing ordinary cycles every valid full-lap arm centered anywhere on the nonstandard cycle is inaccessible from one. Indeed write $m$ for its minimum, $X_*$ for its maximum. The [two-logarithm estimate](../CONTRACTING_CALENDARS.md) gives $\log m=O(\log n)$. Using $T(x)+1\le (3/2)(x+1)$ on odd steps and $T(x)+1\le x+1$ on even steps along an arc of at most $u$ ones gives
$$                X_*+1\le(m+1)(3/2)^u=o(\min(2^n,3^u)).               \tag{3}$$
Here $u/n\to\log_3 2$, since the positive cycle product bounds $0<n\log2-u\log3\le u/(3m)$ and the minima of distinct ordinary cycles tend to infinity. At all sufficiently large periods, all their centers $c$ therefore satisfy $1<c<\min(2^n,3^u)$. Neither $1\equiv c\bmod2^n$ nor $1\equiv c\bmod3^u$ is possible. The two standard rotations have sources $1,2\bmod4$ and endpoints $1,2\bmod3$, respectively. At one only the first standard rotation applies and it fixes one. Thus one is isolated under these full-lap arms alone.

There is also an algebraic obstruction if the only standard arm retained is the unrotated one at $1$. In $\mathbb Z[1/6]$ modulo $D=2^n-3^u$, every rotated nonstandard map $z\mapsto c+(3^u/2^n)(z-c)$ and its inverse act as the identity. The standard map centered at one multiplies $z-1$ by $3/4$, a unit. If $D\nmid m-1$, these unrestricted maps cannot connect $m$ to one, even before restoring the integral domains. This condition holds eventually by $m=n^{O(1)}$ and $\log D=n\log2+O(\log n)$. The center-two rotation and global doubling do not preserve this particular residue obstruction.

### How far doubling must go to enter a reverse arm

Suppose $b,c$ are positive integer units modulo three. Multiplying $b$ by a power $2^a$ allows entry into the reverse arm of center $c$ only if
$$                           2^a b\equiv c\pmod {3^u}.                \tag{4}$$
Some nonnegative $a<2\cdot 3^{u-1}$ always solves (4). Indeed the order of two modulo $3^u$ is $2\cdot3^{u-1}$ by $v_3(4^k-1)=1+v_3(k)$, so its powers represent every unit. One may add a period to make the corresponding preimage positive if necessary.

If $2^a b\ne c$, there is an absolute effective $C$ such that
$$                  u\le C\max(1,h(b/c))\log\max(3,|a|).             \tag{5}$$
Here $h(b/c)$ is the logarithmic height after reducing common factors. Apply Kunrui Yu's Theorem 1 with field $\mathbb Q$, prime three, the two rational units $2,b/c$ and exponents $a,1$. The nonzero form is $2^a b/c-1$, which has the valuation of $2^a b-c$ since $3\nmid c$. The field hypothesis (1.2) holds since $3\equiv3\bmod4$. In (1.5), (1.8)–(1.10) the first modified height is fixed, the second is $\max(h(b/c),\log3)$, and $B=\max(3,|a|)$. The theorem needs no independence condition here. [Yu, *p-adic logarithmic forms and group varieties II*, Acta Arithmetica 89 (1999), Theorem 1](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf)

In particular for any growing ordinary cycle, entry from $b=1$ into the reverse arm at its minimum requires
$$                          a\ge\exp(c_0 n/\log n)                    \tag{6}$$
eventually, for an absolute effective $c_0>0$ using the effective minimum bound. The minimum of a nonstandard positive cycle is odd and exceeds one, hence it cannot be exactly a power of two. More generally (6) holds with a constant depending on a fixed polynomial height bound for both $b,c$, unless they differ by precisely the indicated power of two. Every low phase $c$ and low starting point $b$ of distinct odd cores satisfy the non-equality. This is a cost in the **number of doublings**, even though the forward and reverse orbit equivalence permits arbitrarily many doublings. The upper bound from the exact group order allows (6). It does not give the missing path from one basin to another.

With merely $h(b/c)=o(n)$ and $u\asymp n$, the qualitative conclusion $a/n\to\infty$ for a nonequal hit in (4) still holds. This follows from the [fixed-place sparse valuation theorem](SPARSE_LOCAL_VALUATIONS.md) with the two terms $2^a b/c,-1$ under a contrary subsequence $a=O(n)$. The proof uses the ordinary rational Subspace Theorem, and applies to bounded signed collections of such terms. Yu's explicit (5) and the qualitative result have different scopes when $h(b/c)$ approaches $n$ sublinearly.
