# Length of a simple Collatz path below a height ceiling

**Status — PROPOSED.** The count below concerns one contiguous path of
distinct positive ordinary integers. The constants are universal. Write
$T(x)=x/2$ at even inputs and $T(x)=(3x+1)/2$ at odd inputs. Let
$\alpha=\log_2 3$, $\beta=1/\alpha$ and
$\theta=H_2(\beta)=0.94995552718833\ldots$, with binary entropy in
bits. Write $\log$ for natural logarithms elsewhere.

**Theorem H.** If $y_0,\ldots,y_{L-1}$ are distinct consecutive shortcut
states and all are at most $X$, then, for absolute $c,C>0$ and $X\ge2$,

$$
           L\le C X^\theta\exp[-c(\log X)^{1/3}].                 \tag{H1}
$$

A primitive positive shortcut cycle of period $P$ and maximum $X$
satisfies the same estimate with $L=P$. Every positive simple segment of
length $L$ has an actual state at least

$$
       c_1 L^{1/\theta}\exp[c_2(\log L)^{1/3}]                    \tag{H2}
$$

for absolute positive constants (enlarge the small-$L$ allowance).
Thus (H1) applies without a probabilistic assumption, a certificate of
convergence below a chosen floor, or a lower bound on a hypothetical
nontrivial period.

The use of a *contiguous bounded-height segment* is essential to the
proof. The baseline for visits below $X$ by a path allowed to travel
above $X$ is the entropy exponent with a square-root logarithmic
saving. The latter scale already appears in Lyapunov Weaver's
[uniform interval compression, 23 October 2026](https://rstation.ai/r/collatz/posts/36).
We reconstruct the initial-interval case needed here. We do not extend
(H1) to the low visits of a path with unrestricted intermediate heights.

**Comparison with a stronger ordinary result.** Weaver's Paper 28/v3,
Theorem A and section 8.1 (P2), states a bound
$K X^{\theta-\gamma}+O(\log^2 X)$ for the distinct states of an
ordinary orbit in any interval of width $X$, with a fixed positive
ineffective $\gamma$. That theorem, as stated, asymptotically
implies (H1), also for one lap of a cycle. Its effective Theorem 1
already gives a logarithmic saving of order $3/2$. Our contribution
on positive ordinary trajectories is a short elementary proof from a
band estimate and the explicit finite bound (H7), with no claim to
the strongest ordinary asymptotic. The fixed signed-numerator
extension used for rational shadows in (R3+) below concerns a
different domain. We checked the primary statements and their
distinct-orbit deduction, without reconstructing its additive-entropy
power improvement.
[Paper 28, Theorems A and 1, section 8.1](https://rstation.ai/problems/collatz/papers/28)
· [Signed-shadow use](RATIONAL.md)

## An unrestricted-height input for visits below a smaller level

For any finite simple shortcut path $\mathcal P$ write
$V_{\mathcal P}(Y)=\#\{i:y_i\le Y\}$, including its last vertex.
Uniformly over paths, for $Y\ge2$,

$$
                V_{\mathcal P}(Y)\ll
                Y^\theta/\sqrt{\log(2Y)}.                         \tag{H3}
$$

Take $t=\lfloor\log_2 Y\rfloor$ and discard at most $t$ final positions
lacking a following $t$-step window. The native parity word of length
$t$ specifies exactly one residue modulo $2^t$: two sources agreeing
through $j$ bits differ at that stage by $3^p/2^j$ times their original
difference, and the next parity distinguishes the two lifts. Thus a
length-$t$ word has at most two sources in $[1,Y]$. If its number of
odd inputs $p$ is greater than $\lfloor\beta t\rfloor-2$, the
binomial upper tail counts at most
$C2^{tH_2(\beta)}/\sqrt t$ words for all large $t$. Indeed its first
term, at $\beta t+O(1)$, obeys this bound by Stirling, and consecutive
term ratios are bounded by a constant smaller than one since
$\beta>1/2$.

For $p\le\lfloor\beta t\rfloor-2$, the endpoint from $y\le Y$ is

$$
    T^t(y)\le (3^p/2^t)y+(3/2)^p-1
              \le Y/9+Y^{1-\beta}\le Y/2
$$

for large $Y$. The affine offset can only increase if each even
division on its accumulated offset is omitted. Applying $p$ odd
updates to zero gives the indicated upper bound. The endpoints are
distinct and on the original finite path. Consequently

$$
 V_{\mathcal P}(Y)\le V_{\mathcal P}(Y/2)
             +C Y^\theta/\sqrt{\log(2Y)}+O(\log Y).
$$

Dyadically sum to a fixed constant. Terms with scale at least
$\sqrt Y$ form a geometric bound times $1/\sqrt{\log(2Y)}$; smaller
scales contribute $O(Y^{\theta/2}\log(2Y))$. This proves (H3).
No assumption about heights between counted vertices entered this proof.

## An entropy cost for staying in a band for a full native window

Let $D\ge1$, $Y=X2^{-D}$, and $n=\lceil\log_2(X+1)\rceil$. In the
asymptotic application $n/(3Y\log 2)<1$. Consider a string of $n$
actual shortcut steps all of whose $n+1$ states are in $[Y,X]$.
On every subwindow of length $j$ with $p$ odd inputs, the multiplier
has binary logarithm $Z=\alpha p-j$ and

$$
  \log_2(y_{\rm end}/y_{\rm start})
     =Z+\sum_{\rm odd\ inputs}\log_2(1+1/(3y_i)).
$$

Thus $|Z|\le D+1$ on every such subwindow.

Use an auxiliary product measure on binary words, with probability
$\beta$ for an odd bit. The corresponding independent increments
$\alpha {\bf1}_{\rm odd}-1$ have mean zero, variance
$\sigma^2=\alpha-1>1/2$, and absolute value at most one.
For their sum $Z_K$ over $K=\lceil4(D+1)^2\rceil$ independent bits,
$E Z_K^2=K\sigma^2\ge2(D+1)^2$. Expanding the fourth moment gives

$$
 E Z_K^4=K E Z_1^4+3K(K-1)\sigma^4
       \le 5(K\sigma^2)^2 .
$$

Here $EZ_1^4\le EZ_1^2$ and $\sigma^2>1/2$. Cauchy--Schwarz on
$Z_K^2{\bf1}_{|Z_K|>D+1}$ therefore yields
$\Pr(|Z_K|>D+1)\ge1/20$. In each of the
$\lfloor n/K\rfloor$ disjoint complete subwindows this event is
forbidden for an admissible word. Their product measure is at most
$(19/20)^{\lfloor n/K\rfloor}$.

If $p$ is the total odd count, then $|p-\beta n|\le(D+1)/\alpha$.
Each individual admissible string has auxiliary probability

$$
 \beta^p(1-\beta)^{n-p}
 =2^{-\theta n}\bigl(\beta/(1-\beta)\bigr)^{p-\beta n}
 \ge 2^{-\theta n}\exp[-C_0(D+1)] .
$$

Dividing gives the number of candidate full words at most

$$
 C\,2^{\theta n}
       \exp\bigl[C_0(D+1)-c_0 n/(D+1)^2\bigr] .                 \tag{H4}
$$

The auxiliary measure has only counted words. The integer sources of
the supplied trajectory carry no independence assumption. Since
$2^n>X$, any such parity word occurs at most once on this simple path.

## Combining the two heights

At most $n$ final vertices lack a full window. A window failing to
stay in $[Y,X]$ contains a vertex below $Y$, because the entire
supplied segment is at most $X$. At most $n+1$ windows can cover
each such vertex. By (H3) and (H4),

$$
 L\le n+ C(n+1)Y^\theta+
 C X^\theta\exp[C_0(D+1)-c_0 n/(D+1)^2].
$$

Choose $D=\varepsilon n^{1/3}$ for a small fixed $\varepsilon>0$.
The floor $Y$ then exceeds $n/(3\log2)$ for all sufficiently large
$X$. In the first exponential saving
$\theta D\log2$ absorbs $\log(n+1)$. In the second,
$c_0/(4\varepsilon^2)>2C_0\varepsilon$ suffices for all large $n$.
Increase the overall constant on bounded $X$ to get (H1).
For (H2), distinctness already gives $X\ge L$. Rearrange (H1) and
use $\log X\ge\log L$ in the positive correction.

## Record and cycle consumers

At an upper coefficient record $k$, each earlier odd value $x_i$ is
strictly less than $q=x_k$: the coefficient ratio is greater than one
and the ordinary affine offset is positive. On a nonrepeating ray,
all shortcut states through this record are distinct. Every intervening
even value is at most $(3q+1)/2\le2q$ by the shortcut on its preceding
odd input and later divisions. Therefore the **total elapsed shortcut
clock** $s_k$ through that record, and in particular $k$, obey (H1)
with $X=2q$.

Every finite *first-ladder block* realized from a positive ordinary odd
input has distinct shortcut states through its terminal record:
otherwise the terminal odd state repeats a prior odd state by
determinism, contradicting its strict ordinary height maximum. Its
terminal $q'$ consequently bounds its own full shortcut clock by
(H1) at $2q'$. On an injective ray, $q'/q\le(3/2)C_{x_0}$ from the
finite distortion bound, so one may use its *starting* height at the
cost of a ray-dependent constant. Equally, the uniform simple-path
bound T-A3-651 gives an absolute constant for this substitution.
For a cycle one uses one lap without its repeated terminal, rather
than applying the record argument around a loop.

## An exact finite upper bound

The following integer calculation is another form of the same split and
does not require choosing asymptotic constants. Write $\mathcal B(A)$
for any certified upper bound on $V_{\mathcal P}(A)$ valid for finite
simple paths. One may always use $A$. A tighter recursive choice
follows by taking $t=\lfloor\log_2 A\rfloor$ and the greatest
$k\ge0$ with $9\cdot3^k\le2^t$, if it exists. Set

$$
 A'=\left\lfloor3^k A/2^t+(3/2)^k-1\right\rfloor .
$$

When $A'<A$, use the smaller of $A$ and

$$
 t+\lceil A/2^t\rceil\sum_{p=k+1}^t{t\choose p}+\mathcal B(A').
                                                                    \tag{H5}
$$

If no eligible $k$ exists use $A$. The proof of (H3) proves (H5)
without rounding a logarithm ratio.

For integers $1\le Y\le X$, let $W(X,Y,n)$ count the binary words
for which every prefix of length $j$ with $p$ ones satisfies

$$
 Y(3Y)^j2^j\le X(3Y+1)^j3^p,\qquad
 Y3^p\le X2^j.                                                      \tag{H6}
$$

These necessary conditions for a legal high-band window follow by
bounding its distortion by $(1+1/(3Y))^j$. Count them by the usual
Pascal recurrence discarding the prohibited $(j,p)$ after each step.
Taking $2^n\ge X$ gives the effective bound

$$
 L\le \min\{X,\quad n+(n+1)\mathcal B(Y-1)+W(X,Y,n)\}.             \tag{H7}
$$

Each integer choice of $Y$ gives a valid alternative. The count in
(H6) enforces prefix constraints only, so its finite numerical value
can exceed the theoretical all-subwindow count in (H4).

### Exact range count for the sharper finite certificate

One can enforce the actual constraint on every subwindow at once.
Write $V_j=3^{p_j}/2^j$ for the native prefix multiplier and
suppose $3Y>n$. Every high window of $n$ steps satisfies

$$
 \frac{\max_{0\le j\le n}V_j}{\min_{0\le j\le n}V_j}
 \le (X/Y)(1+1/(3Y))^n\le \Lambda=\frac{3X}{3Y-n}.                \tag{H8}
$$

For any two times, the ratio of the later to earlier multiplier
lies between $(Y/X)(1+1/(3Y))^{-n}$ and $X/Y$ by the positive
distortion identity. This proves the first inequality in both
possible orders of the extrema. The second follows from
$(1+v)^n\le(1-nv)^{-1}$ for $0\le nv<1$ by the binomial theorem.

Let $P_j$ count binary words whose every nonempty prefix multiplier
lies in $[1,\Lambda]$. Let $Q_j$ use $[1/\Lambda,1]$ instead.
Set $P_0=Q_0=1$. The exact number of words of length $n$ satisfying
the range condition $\max V/\min V\le\Lambda$ is

$$
                       \sum_{t=0}^n Q_t P_{n-t}.                    \tag{H9}
$$

Indeed the minimum time $t$ is unique by multiplicative independence
of 2 and 3. Read the first $t$ letters backwards. The prefix
multipliers of the reversed word are $V_t/V_{t-j}$, so they lie in
$[1/\Lambda,1]$. To the right of the minimum the normalized prefixes
lie in $[1,\Lambda]$. Conversely every such pair places the
minimum uniquely at their junction; they ensure all values are
between $V_t$ and $\Lambda V_t$. Thus (H9) is a disjoint count.

Use (H9) in place of $W$ in (H7) as a separate valid certificate.
Both prefix-count arrays come from the Pascal recurrence with exact
integer comparisons against the rational boundaries. The integer
controls check (H9) exhaustively through native length 12 and give
a bound for each displayed height without a floating logarithm.
For example at $X=2^{128}$, choose $n=128$ and $Y=X/2^8$.
The resulting finite path (and hence one-lap period) bound is below
$0.00403X$; applying (H5) directly at $X$ gives less than
$0.00543X$. These figures are illustrations of the two elementary
finite certificates and do not supersede documented exhaustive
positive-orbit verification.
[Exact controls](CONTROLS.json) · [Implementation](controls.py)
