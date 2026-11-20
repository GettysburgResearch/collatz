# Forward tripling of the basin of one

Let $T$ be the positive shortcut Collatz map. Write $C$ for the set of starts that reach $1$. The following are equivalent.

1. All positive integers reach $1$.
2. For every $x\in C$, the number $3x$ belongs to $C$.
3. For every $x\in C$ with $x\equiv1\pmod{16}$ or $x\equiv71\pmod{128}$, the number $3x$ belongs to $C$.
4. For every odd $x\in C$ divisible by three, the number $3x$ belongs to $C$.
5. For every $x\in C$ with $x\equiv1\pmod{16}$, the number $3x$ belongs to $C$.
6. For every $k\ge0$, if $16k+1$ reaches $1$, then $32k+1$ reaches $1$.

This compares a single basin in one direction. It still requires proving the implication at the indicated inputs. There is also an unconditional geometric interpretation. Join $n$ and $T(n)$ by an undirected edge and add a directed edge $n\to3n$. The directed distance from $1$ to $n$ lies between $\log_3 n$ and $36\log_2 n$. These paths may traverse ordinary edges backwards and contain forward triplings. They do not bound the ordinary stopping time.

## A path to the difficult residue

Write $x\leadsto y$ when the allowed moves take $x$ to $y$. For $h\ge1$ put $g(h)=h-1$, using it only when the resulting vertex is positive. The ordinary step $T(2h-1)=3h-1$ exchanges $g(2h)$ and $g(3h)$ in either direction. Thus $g(4h)$ is two ordinary edges from $g(9h)$. A separate move uses one forward tripling,
$$
 g(8h)\longrightarrow 3(8h-1)\longrightarrow 4(9h-1)
 \longrightarrow 2(9h-1)\longrightarrow g(9h).
$$
The last three arrows are ordinary steps. Combining this path with the exchanges gives $g(12h)\leadsto g(4h)$ in seven edges. Its only tripling source is $8h-1$.

Consider $n=4h-1$, and factor $h=2^v u$ with $u$ odd. Write $w=3^v u$. A series of $v$ exchanges connects $g(4w)$ and $n$. We connect the odd part $u$ to $g(4w)$. The powers of three permute the odd residues modulo $16$ in two cycles of length four, meeting $3$ and $5$, respectively. Hence some $0\le j\le3$ makes $Y=9\cdot3^jw$ congruent to $3$ or $5$ modulo $16$. On either class, $Y$ and $Y-1$ meet under $T$ in at most four steps on each arm. Indeed the starts $16k+2,16k+3$ meet at $9k+2$ in four steps; $8k+4,8k+5$ meet at $3k+2$ in three.

Starting at $u$, triple $v+j+2$ times to reach $Y$. Cross the ordinary path to $Y-1$, then exchange twice to $g(4\cdot3^jw)$. Use the seven-edge paths $j$ times to reach $g(4w)$, and make the last $v$ exchanges to $n$. The path cost is at most $2v+8j+12\le2v+36$.

For the distance bound, use strong induction. An even $n$ costs one move from $n/2$. For $n\equiv1\pmod4$ with $n\ge5$, two ordinary steps reach $a=(3n+1)/4\le4n/5$. The difficult residue costs at most $2v+36$ moves from $u$, and $n/u=4\cdot2^v-1/u\ge2^{v+1}$. Each case therefore adds at most $36\log_2(n/a)$ moves from its smaller input $a$ (taking $a=u$ in the last case). This proves the upper bound. A single allowed move increases the vertex by a factor of at most three, which proves the lower bound. Any ordinary-orbit-invariant set containing $1$ and closed under forward tripling must contain every vertex reached by these paths. Applying this to $C$ proves the equivalence of statements 1 and 2.

## Restricting the directed comparisons

Suppose only the two residue classes in statement 3 are known. A forward tripling at any odd $x=3s$ can be replaced by two forward triplings in class $1\pmod{16}$. To see the orientation, write $J(t)=t+1$ and identify values linked by ordinary edges. The identity $J(4t)\sim J(3t)$ follows from $T^2(4t+1)=3t+1$. We also have
$$
 J(9t)\sim J(16t)\ \longrightarrow\ 3(16t+1)\sim J(18t).
$$
The arrow is the permitted forward tripling. The right-hand merger follows from $T^2(3(16t+1))=4(27t+2)$ and $T(18t+1)=27t+2$. Since $s$ is odd, $3s\sim J(9s)$ and $9s\sim J(27s)$. Use the displayed path with $t=s$ and $2s$, then $J(36s)\sim J(27s)$. This gives a directed path from $3s$ to $9s$.

In the strong induction at $n=4h-1>3$, the start $3u$ is already smaller than $n$. Thus the path may start there and every subsequent tripling in the initial string has an odd source divisible by three. The case $n=3$ reaches $1$ directly. In choosing $j$, stop at the first $z=3^i w$ for which $9z\equiv3\pmod{16}$ or $9z\equiv5\pmod8$ or $z\equiv1\pmod{16}$. One of the first four choices works as before. In the last case use $6z$ in place of $9z$. It is reached by doubling $3z$, and $6z-1,6z$ meet for $z=16t+1$ at $27t+2$ after five ordinary steps. One exchange takes $g(6z)$ to $g(4z)$.

For each seven-edge descent at an earlier $z$, consider its tripling source $8z-1$. If $z\equiv3\pmod4$, the source is $23\pmod{32}$ and already meets its triple by ordinary steps. At the starts $23,69$ the common endpoint is $20$ after five steps with three and two odd steps, respectively. Adding $32t,96t$ adds $27t$ to both endpoints. If $z\equiv1\pmod4$, earlier stopping excluded $z\equiv5\pmod8$ and $z\equiv1\pmod{16}$. The remaining possibility is $z\equiv9\pmod{16}$, so $8z-1\equiv71\pmod{128}$. Its needed tripling is allowed by assumption. This constructs a path to $n$ from an already convergent integer with every directed step justified by statement 3. It proves that statement 3 suffices.

## Narrowing the second residue

Using the first-stop rule, the complete list of troublesome indices $i$ is short. For starting residues $w=1,5,7,11,13,15\pmod{16}$ there are none. For $w=9\pmod{16}$ the only one is $i=0$. For $w=3\pmod{16}$ the only one is $i=1$. This follows by iterating multiplication by three modulo 16 up to the first stop.

If $w\equiv9\pmod{16}$, the target already has a smaller ordinary representative. For every $w\equiv1\pmod4$ the starts $3w-1,9w-1$ meet after two ordinary steps at $(9w-1)/4$. Thus $g(4w)\sim g(9w)\sim g(3w)\sim g(2w)$. Undoing the $v$ exchanges gives the smaller integer $2h-1$ in the component of $n$.

In the remaining case $w\equiv3\pmod{16}$ put $z=3w$. The only troublesome source is $8z-1$, since the seven-edge descent from $g(4z)$ to $g(4w)$ uses the intrinsic merger at $8w-1\equiv23\pmod{32}$. We have $z\equiv9\pmod{16}$. Hence $g(4z)\sim g(9z)\sim q=(9z-1)/16$ by four halvings. The smaller odd preimage of $q$ is
$$
 b=(2q-1)/3=(3z-3)/8.
$$
Indeed $q\equiv2\pmod3$ and $b$ is an odd positive integer. For $0\le v\le3$, substituting $z=3^{v+1}u$ gives
$$
 n-b=\big((32\cdot2^v-9\cdot3^v)u-5\big)/8>0,
$$
since the four coefficients $32\cdot2^v-9\cdot3^v$ are $23,37,47,13$. The induction hypothesis at $b$ gives membership at $g(4z)$ and hence at $n$ without the troublesome tripling. For $v\ge4$, the remaining source $8z-1=24\cdot3^v u-1$ is $-1\pmod{243}$ and $71\pmod{128}$. These two congruences select exactly $5831\pmod{31104}$. Thus the extra class in statement 3 could already be replaced by this single class modulo 31104. The following ordinary word removes it entirely.

## Discharging the last residue with forward triplings

For $x=31104t+5831$, $t\ge0$, start at $3x$ and read the following word left to right.

```
ODDDDIDDDDIVVOEEOEEOEOODDIVVOEEI
```

Here $O$ and $E$ are the ordinary odd and even steps, $D$ doubles, and $I$ is the ordinary odd preimage $m\mapsto(2m-1)/3$. Each $V$ divides by three. The final value is $x$. The four quotients at the $V$ steps, in order, are
$$
 5308416t+995175,\quad1769472t+331725,\quad
 373248t+69975,\quad124416t+23325.
$$
All are positive odd multiples of three. Read the word backwards to obtain a directed path $x\leadsto3x$ with four permitted **forward** triplings at those quotients. Every other edge is ordinary. For a direct check of the word, propagate its affine pair $(a,b)$ representing $at+b$. The updates for $O,E,D,I,V$ are $(3a/2,(3b+1)/2)$, $(a/2,b/2)$, $(2a,2b)$, $(2a/3,(2b-1)/3)$ and $(a/3,b/3)$. At every $O,E$ the slope is even and the offset has the prescribed parity. At every $I$ the slope is divisible by three and the offset is $2\pmod3$. The successive pairs at the four $V$ steps are the coefficients displayed above, and the last pair is $(31104,5831)$.

The earlier construction used only forward triplings at odd multiples of three and the extra comparison just discharged. Hence statement 4 implies full convergence. The two $J$ paths previously proved that statement 5 implies statement 4. Full convergence implies both restricted closures. Finally the ordinary paths above give $3(16k+1)\sim J(18k)\sim J(24k)\sim J(32k)=32k+1$. Thus statements 5 and 6 concern the same two ordinary components for each $k$. This proves all six equivalences.

For an ordered orbit-invariant $f$, forward monotonicity $f(x)\le f(3x)$ implies $f(1)\le f(n)$ for all $n$ by the same directed paths. Reversing the order gives the reversed conclusion. The unrestricted forward-generation result and its basin corollary have Lean proofs in [HighBit.lean](HighBit.lean). The explicit distances and residue restriction here use the ordinary paths above.

The last target identification has direct ordinary clocks: $T^4(3(16k+1))=T^5(32k+1)=27k+2$ for every $k$. The base paths from $3$ and $1$ have respectively two and three odd inputs, so their shifted endpoints agree. [Lean proof of the target identity](HighBit.lean)
