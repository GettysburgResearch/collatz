# An unrestricted inverse-clock obstruction and its sharp ordinary escape

**Status: proposed elementary proof and bounded exact replay.** Use the ordinary shortcut map
$T(x)=x/2$ on even inputs and $T(x)=(3x+1)/2$ on odd inputs. Write
$p_j(x)$ for the number of odd inputs among the first $j$ steps.
All witnesses and all endpoints in the statements are positive ordinary integers.
A signed helper is used only in the proof.

## A uniform two-congruence barrier

Let $H,A\ge1$, $n>1$, $2^H\mid n+1$, and $3^A\mid n-1$.
If $0<x<n$, $0\le h\le H$, and $T^t(x)=T^h(n)$, then
$$
                         p_t(x)\ge h+A+1 .
$$
There is no restriction on $t$. If $H=v_2(n+1)\ge2$, the same lower bound
$H+A+1$ holds at forward clock $H+1$, whose target-side odd count is $H$.

**Proof.** Through clock $H$ the input follows odd branches, giving
$T^h(n)+1=(3/2)^h(n+1)$. For positive inputs every odd step multiplies the
shifted value $x+1$ by $3/2$, while each even step decreases it.
Thus any competing word has $a=p_t(x)>h$. Suppose $s=a-h\le A$;
put $e=t-h\ge s\ge1$. The competing affine word is
$F(z)=(3^a z+C)/2^t$, $C\ge0$. Define the integer
$$
          b=x-2^e(n-1)/3^s .
$$
Direct substitution of the meeting equation gives
$$
             F(b)=2(3/2)^h-1.                                      \tag{1}
$$
For $h=0$, the whole inverse word from the actual endpoint $n$ can be
replayed at 1. At an even inverse the difference doubles; at an odd inverse
the difference is multiplied by $2/3$. The original difference $n-1$
is divisible by $3^a$, guaranteeing integrality at each odd inverse.
Every integral inverse of a positive integer is positive. The recomputed
start is $b\ge1$. Equation $1$ yields $2^t=3^a b+C\ge3^a$, and thus
$x=b+(2^t/3^a)(n-1)\ge n$.

Now $h\ge1$. Since $n$ is odd, $2^{e+1}\mid x-b$. Hence the first
$e+1\le t$ branches at $b$ are legal for the signed integer extension of
$T$. Indeed two integers in the same class modulo $2^L$ have equal parities
through $L$ steps, as their difference loses at most one binary factor per
step. If $b\le0$, then $T^{e+1}(b)\le0$, since the nonpositive integers are
forward invariant. Either real affine branch is increasing. From any starting
number at most zero, any remaining word of length $h-1$ ends at most
$(3/2)^{h-1}-1$: compare with the all-odd word started at zero, whose
nonnegative intermediate values make its odd branch the larger choice. This
contradicts $1$. Thus $b\ge1$.

If $b=1$, the first $e+1$ branches follow $1,2,1,2,\ldots$, with at most
$\lceil(e+1)/2\rceil$ odd steps. The last $h-1$ branches contribute at
most $h-1$ more, so $s\le\lfloor e/2\rfloor$, whence
$2^e\ge 4^s\ge3^s$. If $b\ge2$, $1$ gives
$3^a b\le2^t F(b)<2^{t+1}(3/2)^h$, yielding $2^e>3^s$.
Both cases give $x=b+(2^e/3^s)(n-1)\ge n$, a contradiction.

For the extra clock, put $M=(n+1)/2^H$, odd by exact valuation.
Then $Z=T^{H+1}(n)=(3^H M-1)/2\equiv1\pmod3$, so $2Z$ is its only positive
predecessor. Also $Z\ge n$, since $(3/2)^H\ge2$. Any smaller start reaching
$Z$ must take at least one step and the final step is even from $T^H(n)$.
Apply the preceding bound at $H$. ∎

## Exact finite search layers without a reserve

Each positive even input is at least 2, so its ratio of shifted heights is
$(x+2)/(2x+2)\le2/3$. Each positive odd input has ratio exactly $3/2$.
Consequently if $T^t(x)=Y$ with $a$ odd inputs and $0<x<n$, then
$$
       Y+1\le (3/2)^{2a-t}(x+1)\le (3/2)^{2a-t}n .
$$
For an all-odd target prefix $Y=T^h(n)$ with $h\le H$ this gives a strict
inequality $t<2a-h$. Thus every eligible lower source of odd excess $s=a-h$
lies on the finite diagonal
$$
                    h+s\le t\le h+2s-1 .
$$
For each successive $s=1,2,\ldots$, all legal inverse words on this finite
diagonal can be enumerated at the actual $Y$, and checked for $0<x<n$.
No factorization of the given source into a reserved splice is needed.
For an arbitrary endpoint use $t\le 2a+\log_{3/2}(n/(Y+1))$; the displayed
inequality can be tested with integer products. The construction below gives
examples where many initial layers fail but some later layer succeeds.
Termination whenever a smaller inverse source exists is immediate. The proof
does not establish existence at any prescribed endpoint.

## Even the additive overhead at clock zero grows without bound

Fix $E\ge1$, set $M_E=\lfloor 2(3/2)^E-1\rfloor$, and take $D_E$ to be
the largest odd count before the first visit to 1 among those positive
$z\le M_E$ that reach 1. This finite maximum exists (it includes $z=1$).
For
$$
                 A\ge 5D_E+4E+3
$$
and any $n>1$ with $3^A\mid n-1$, **every** lower predecessor reaching $n$
at any clock requires more than $A+E$ odd steps. This statement needs no
hypothesis about the other $z\le M_E$. An explicit termination certificate
for every member of that finite interval supplies a computable $D_E$ for a
particular $E$.

Indeed the clock-zero result excludes $a\le A$. Suppose $a=A+s$,
$1\le s\le E$. For the actual affine word $F$, take the rational starting
value $b=F^{-1}(1)=x-(2^t/3^a)(n-1)$. Then $b<1$: if the displayed
slope is at least one use $x<n$; if it is smaller use
$b=(2^t-C)/3^a\le 2^t/3^a<1$. After any $j$ symbols the difference of the
two formal paths from $x,b$ is
$2^{t-j}3^{p_j(x)}(n-1)/3^a$.
Immediately after the $s$-th odd symbol this is an integer multiple of
$2^{t-j}$. Therefore the formal path from this point is a legal ordinary
signed path to 1. Its initial value $z$ is positive because nonpositive
integers are forward invariant. Also $z\le2(3/2)^s-1$: dominate the path
from $b<1$ by the odd branch on odd symbols and the identity on even
symbols started at 1, using monotonicity and nonnegative comparison values.
This gives $z\le M_E$. There are exactly $A$ remaining odd steps. After
its first visit to 1, this suffix consists of repetitions of the two-step
cycle, so $t\ge 2(A-D_E)$.

On the other hand $F(0)\le(3/2)^a-1$ by the same comparison starting
at zero. Since $A\ge E+1$, $2(3/2)^{A+E}\le3^A<n$. Thus
$x=(2^t/3^a)(n-F(0))<n$ implies $2^t<2\cdot3^a$. From $3^5<2^8$
we obtain $5t<5+8(A+E)$. Combining with the lower bound yields
$2A<10D_E+8E+5$, contrary to the chosen threshold.

In the marked construction below $v_3(n-1)=A$ exactly: cubing increases the
3-adic valuation of $2^{3^{j}}+1$ by one at each step, since
$w^2-w+1\equiv3\bmod9$ whenever $w\equiv-1\bmod3$.
Also $k=2\cdot3^{A-1}>A$, and $2^B(n-1)=3^k u-(2^B+1)$.
Consequently the minimum clock-zero odd count minus $v_3(n-1)$ grows without
bound along explicit families of marked inputs with supplied lower
predecessors. This is a statement about the prescribed target, not about
all later clocks on its orbit.

## A smaller partner at the very next clock

For any odd $n>1$, write $n+1=2^H M$ with $M$ odd. If $3^H M\equiv1\pmod4$,
then $m=(n-1)/2$ is an explicit smaller ordinary partner and
$$
        T^{H+1}(m)=T^{H+2}(n)=(3^H M-1)/4,\qquad
        p_{H+1}(m)=p_{H+2}(n)=H .
$$
Indeed the starts have $H-1$ and $H$ initial odd steps, respectively,
to $3^{H-1}M-1$ and $3^H M-1$. At the former value the next two branches
are even, odd, and at the latter they are even, even. This supplies an ordinary
selector on half of the odd integers: at each exact valuation $H$ one of
the two odd classes for $M\pmod4$ works. To justify summing the densities,
the remaining tail $2^K\mid n+1$ has density $2^{-K}$.

## Both the expensive and cheap partners physically exist on marked inputs

Fix $A\ge1,H\ge2$. Set $B=3^{A-1}, k=2B$. Then $k\ge A$,
$2^B\equiv-1\pmod{3^A}$ by induction using cubing, and $3^k>2^{B+k}$ since
$9^B>8^B$. Choose the residue
$r=2^H(3^{-H}\bmod4)-1\pmod{2^{H+2}}$. Select any positive $u$ satisfying
$$
                  3^k u\equiv1+2^B r\pmod{2^{B+H+2}} .
$$
The odd coefficient is invertible. Put $x=2^k u-1$ and
$n=(3^k u-1)/2^B$. Then $n\equiv r\pmod{2^{H+2}}$,
$n\equiv1\pmod{3^A}$, and $x<n$. The $k$ initial odd steps from $x$
are followed by $B$ halvings to $n$. These give a smaller predecessor
at clock zero, with exactly $k$ odds; no optimality is asserted for $k$.

The resulting $n$ fill the positive tail of one progression of step
$2^{H+2}3^k$. In each sufficiently high octave $[2^d,2^{d+1})$, the
marked initial interval $(d+1)(n-2^d)\le70\cdot2^d$ has length exceeding
that step. Thus in every such octave a common positive marked example has
all of the following properties:

* a supplied smaller predecessor at clock zero;
* every smaller partner at every clock through $H+1$ costs more than
  $A$ extra odd steps, independent of the partner's clock;
* the explicit half-size partner at $H+2$ costs zero extra odd steps.

For $A=H=2$ the construction gives $n=5923$ and $x=4159$. The latter reaches
$n$ with six odd steps and three halvings. From $n$, the first four values
after the start are $8885,13328,6664,3332$; from the half-size partner $2961$
the three values are $4442,2221,3332$. At clock three every smaller partner
requires at least five odd steps; at clock four two suffice.

## Relation to the existing packets and remaining obligation

* PR146 at `f431078244e868dc699fad011044f0d5e7f76437`,
  `research/upper-bit-mergers/NEGATIVE_FIVE_CHECKPOINT.md`, proves a distinct
  excess bound around the signed cycle $-5,-7,-10$. Here the binary anchor
  is $-1$ and the ternary anchor is positive $1$; its short positive
  cycle controls the competitor prefix. The special adjacent-Mersenne
  even-even/even-odd identity appears in
  `research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`.
* PR173 at `fa0c9e2a2851e6324391e39c17afcb5913185aec` supplies the
  marked interval used here. We use its definition only.
* PR184 at `366dab89ee9548084ab9b5e4e90ff82abf287a20`,
  `research/lean-band-coupling-20261121/LATEST_CONNECTIONS.md`, requires a
  bound on the inverse odd count for a supplied reserve. The obstruction is
  to **any** fixed excess budget on a fixed initial horizon, even for true
  ordinary mergers. It does not exclude arbitrarily growing reserves or
  choices of later forward clocks.

The positive half-size selector leaves the other class $3^H M\equiv3\pmod4$
open. Neither its coverage nor eventual access to its successful class from
every original source has been proved. A fixed ordinary certificate can cross
the barrier by paying excess or advancing its target clock. The theorem is
not a universal selector, an all-time survivor, or a proof of Collatz.
