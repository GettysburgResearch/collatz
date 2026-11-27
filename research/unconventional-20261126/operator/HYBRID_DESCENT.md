# A mixed signed root defeats bounded bidirectional slope descent

**Status.** PROPOSED written theorem and exact controls. The criterion below excludes escape if it succeeds at every ordinary integer. The obstruction applies even when a certificate may search a complete undirected neighborhood.

Give a forward edge of the shortcut Collatz map its positive affine slope $1/2$ or $3/2$ according to whether its source is even or odd. Give each reverse traversal the reciprocal slope. Write $P(w)$ for the product on a walk. Edges retain their orientations and multiplicities, including the two edges between 1 and 2. A slope descent from $n$ is a finite walk starting at $n$ with $P(w)<1$.

## OP-D1. The bidirectional criterion detects escape alone

Every vertex of a component containing a positive cycle has a slope descent. Walk to the cycle, traverse it once in its forward direction, and reverse the entrance path. The multiplier is the full-cycle forward slope, strictly below one because the cycle has positive additive carry.

On an escaping component define
$$
 L(n)=n\prod_{j\ge0}\left(1+\frac{1_{\{T^j n\text{ odd}\}}}{3T^jn}\right).
$$
The reciprocal bound on every simple ordinary forward path, e.g. [O2](../renewal/OCCUPATION.md), gives $n\le L(n)\le Cn$ with a uniform finite $C$. Thus $L$ has an attained minimum on that component. Direct cancellation gives $L(Tn)=c(n)L(n)$ on each edge. Starting at a minimizer every walk has $P(w)\ge1$. In particular, every ordinary integer has a bidirectional slope descent if and only if every ordinary trajectory eventually enters a cycle. The assertion does not require identifying the cycle. Testing that one walk exists at one vertex does not rule out escape from that vertex.

## OP-D2. A root with no bidirectional slope descent

Use rational coordinate pairs $(x,y)$ with $x\in\mathbb Z_2$, $y\in\mathbb Z_3$. The parity of $x$ chooses the forward affine map on both coordinates. The inverse maps are $E(z)=2z$ everywhere and $O(z)=(2z-1)/3$ when $y\equiv2\bmod3$. They give the exact preimages of the forward map: $E(x)$ is even in $\mathbb Z_2$ and $O(x)$ is odd there.

Starting at $(-1,1)$, **every finite walk has slope at least one**. Its forward orbit is
$$
            (-1,y_j),\qquad y_j=2(3/2)^j-1 .
$$
The distinct forward points show that the component is acyclic. More directly, deleting immediately retraced edges preserves the slope. On a reduced walk a reverse step cannot be followed by a forward step, by uniqueness of the forward edge. Thus the reduced walk has $j$ forward steps followed by inverse steps.

Every inverse step preserves $x\le-1$. For $0\le i\le j$ inverse steps, the second coordinate is at least $2(3/2)^{j-i}-1\ge1$: both maps increase in the real order, and $E(z)\ge O(z)$ for $z\ge1$. Each inverse step drops the exponent of the second coordinate's dyadic denominator by at least one until it reaches zero. Indeed for $z=b/2^d$ with $d>0$, $O(z)=(b-2^{d-1})/(3\,2^{d-1})$, and ternary legality forces $3\mid b-2^{d-1}$. The $E$ case is immediate. The initial denominator divides $2^j$. Consequently after $j$ inverse steps, if they are taken, the second coordinate is a positive integer. Further legal inverse steps preserve positive integrality. At every endpoint $y-x\ge2$, and common affine updates multiply the coordinate difference by their slope. Since the initial difference is two, this proves the claim.

## OP-D3. Quantitative ordinary and known-basin copies

For radius $R\ge1$, every positive $n$ with
$$
              n\equiv-1\pmod{2^R},\qquad n\equiv1\pmod{3^R}
$$
has no slope descent of length at most $R$. At step $i<R$ the ordinary coordinate agrees with the mixed root's corresponding coordinates modulo at least $2^{R-i}$ and $3^{R-i}$. This identifies the forward parity and inverse legality and propagates by each allowed affine update. In particular every ordinary walk of length at most $R$ has a legal mixed counterpart with the same edge multipliers.

The least positive CRT solution satisfies $n_R\le6^R$ and tends to infinity since $n_R+1$ is a positive multiple of $2^R$. Thus a universal positive certificate of radius at most $(\log n)/\log6$ fails on arbitrarily large ordinary inputs. Each such cylinder occurs arbitrarily far out in every ordinary component by [OP-L1](LOCAL_SPECTRUM.md).

There are explicit known-basin witnesses with a size bound. Choose $j$ in the interval $[2\cdot3^{2R-1},4\cdot3^{2R-1}]$ satisfying
$$
           2^j\equiv-1+3^R2^{1-R}\pmod{3^{2R}}.
$$
Here the power of 2 with negative exponent is interpreted modulo $3^{2R}$. The right-hand side is a unit and 2 generates the units of every $3^k$. For example $v_3(2^{2\cdot3^m}-1)=m+1$ follows from the geometric sum, starting from $2^2-1=3$. Set $n=2^R(2^j+1)/3^R-1$. This is a positive integer satisfying both congruences. Its first $R$ forward steps are odd and reach $2^j$, since the odd affine formula multiplies $n+1$ by $3/2$. Consequently these good witnesses satisfy $\log\log n\le2R\log3+O(1)$. For any $c<1/(2\log3)$, a radius $\lfloor c\log\log n\rfloor$ fails on arbitrarily large known-basin inputs, including all reverse branches.

The mixed pair gives an obstruction in the finite local topology. Whether an ordinary diagonal point can have no bidirectional descent at every radius remains open and, by OP-D1, is exactly the positive escape question. Forward-only coefficient stopping times and their negative rational obstructions are classical; the separate ternary coordinate above protects the root against inverse moves as well. [Terras, original coefficient stopping-time paper](https://doi.org/10.4064/aa-30-3-241-252)
