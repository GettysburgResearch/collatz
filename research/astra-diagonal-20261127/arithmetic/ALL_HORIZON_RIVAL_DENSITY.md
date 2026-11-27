# An all-depth ordinary density for smaller rivals at a prescribed endpoint

**PROPOSED written theorem.** Prescribe any finite word \(w\) of
positive odd exponents, of length \(s\) and sum \(A\); the empty word
is allowed. Its positive odd realizers form one class modulo
\(D=2^{A+1}\). For its realizer \(n\), put \(y=U^s(n)\), with
\(U(n)=\operatorname{oddpart}(3n+1)\). Ask whether some *positive odd*
\(b<n\) reaches this particular \(y\) after any number of odd steps,
including zero. The relative natural density of this event in the
specified dyadic class exists and is computable. In \([X,2X)\) the
relative frequency differs from it by \(O_w(X^{-\eta})\) for an
absolute computable \(\eta>0\). There is no upper bound on the rival's
excursion height or true travel time.

Write \(2^A y=3^s n+C_w\), with \(C_w\) the ordinary word intercept.
For each rival word \(v\) of length \(r\) and sum \(B\), discard it if
its required ternary class for \(y\bmod3^r\) conflicts with the native
class modulo \(3^{\min(r,s)}\). On compatibility the formal rival is
\[
 b=\rho n+\delta,\qquad
 \rho=2^{B-A}3^{s-r},\qquad
 \delta=(2^{B-A}C_w-C_v)/3^r .                              \tag{1}
\]
Accept the word when \(\rho<1\), or when \(\rho=1\) and \(\delta<0\).
For \(r\le s\) a compatible accepted word gives density one. Otherwise
the answer is the normalized Haar measure in \(\mathbb Z_3\) of the
union, over compatible accepted words \(r>s\), of their individual
\(n\bmod3^{r-s}\) cylinders. Equivalently use the progression parameter
of the native dyadic class, a ternary isometry. Overlaps count only
once. The tail after ternary depth \(J\) is \(O_w(\gamma^J)\), where
\[
                 \gamma=\frac{\sqrt3}{2^{3/2}-1}<1 .
\]
The computation uses a finite sum of exact cylinder lengths at each
truncation and an explicit geometric majorant. The two clocks can have
arbitrarily large positive difference \(r-s\). This is an ordinary
density conclusion about fixed \(w\), not a decision at a supplied
integer surviving all finite tests.

## Finite words, a true first crossing, and the ternary tail

For odd positive \(y\), the integral inverse for word \(v\) exists
exactly when \(2^B y\equiv C_v\bmod3^r\). This last congruence
implies the shorter reverse divisibilities by successively reducing
the cleared equation modulo 3 and canceling powers of two. Alternatively
construct the rational reverse chain from its odd terminal. If the
initial source is integral its forward rational iterates have only
dyadic denominator, while the reverse expressions have only ternary
denominator, so all are integral. An integral reverse step
\((2^e u-1)/3\) from a positive integer \(u\) is positive and odd.
Thus every class counted here is a true ordinary path. Substitution of
the native affine equation gives precisely the stated ternary class
or compatibility failure. For each fixed horizon only finitely many
word sums can contribute at large \(n\). Indeed \(2^B y\le4^r b\)
on a positive rival, and \(y\ge3^s n/2^A\).

For the cutoff argument choose the *least rival depth* among genuine
smaller sources reaching \(y\) at a given \(n\). If this depth is
\(r>0\), every subsequent site through the terminal is at least \(n\).
The initial rival satisfies \(b\ge(2n-1)/3\ge n/2\) for \(n\ge2\).
Multiplying the \(r\) actual edge equations gives
\[
 \frac{2^B y}{3^r}
 = b\prod_{i<r}\left(1+\frac1{3b_i}\right)
 \le n\exp(2r/(3n)).
\]
Consequently \(B\le A+(r-s)\log_2 3+O(r/X)\) in the physical shell.
For \(j=r-s>0\) and \(r\le L=\lfloor c\log X\rfloor\), choose an
absolute \(c>0\) with \(c\log3<1/3\), for example \(c=1/10\).
The elementary separation
\(\lceil j\log_2 3\rceil-j\log_2 3\gg3^{-j}\) follows from the
unequal integers \(2^{\lceil j\log_2 3\rceil}\) and \(3^j\).
It exceeds the displayed \(O(L/X)\) for large \(X\), so
\(B<A+j\log_2 3\), exactly the accepted budget. Conversely, for
every compatible accepted word with \(0<j\le L\),
\(1-\rho\ge 1/(2^A3^j)\) and
\(\delta\le \rho C_w/3^s=O_w(1)\). Equation (1) therefore gives
\(b<n\) uniformly on the full shell. For \(r\le s\) the finitely
many potentially smaller words settle by (1), including ties.

For \(r=s+j\) the number of all budgeted rival words, even before
compatibility, is at most
\[
  2^{3A/2}(2^{3/2}-1)^{-s}
       \left(\frac{3^{3/2}}{2^{3/2}-1}\right)^j .
\]
Indeed sum \(2^{-3B/2}\) over all positive \(r\)-letter words.
A single compatible word has ternary probability \(3^{-j}\).
This proves the claimed exponential Haar tail and an explicit constant
by summing the geometric series.

## The unbounded ordinary horizon

The following finite-image argument appears in the tripling
comparison paper. For any map \(T\) on a set, finite \(I\), and positive
integer \(L\), let \(F=T^L(I)\). Among \(z\in I\) reached from \(I\)
at time at least \(L\), the cardinality is at most \((L+1)|F|\).
Indeed such a path has already encountered \(F\), and \(T^Lz\in F\).
Off \(F\), \(z\) is one of the last \(L\) sites preceding the next hit
of \(F\) in a first-return segment from its most recent hit of \(F\).
Each possible departure point of \(F\) contributes at most \(L\) such
sites, by forward determinism. Count the sites in \(F\) separately.
The path between the two endpoints may leave \(I\) without limit.
[Lean Assurance Lab, paper 228, §3](https://rstation.ai/problems/collatz/papers/228/v1)

Apply this to the ordinary shortcut and \(I=[1,\lceil K_w X\rceil]\),
with \(K_w\) fixed large enough to contain every \(b<n\) and every
native endpoint \(y\) in the shell for large \(X\). Put \(Y=|I|\).
For completeness the \(L\) parity bits give one class modulo \(2^L\).
There are at most \(2^{H_2(3/5)L}\) words with at least \(3L/5\) odd
departures, where \(H_2\) denotes binary entropy. The other words
give endpoints at most \(Y(3^{3/5}/2)^L+(3/2)^L\), by summing the
at most \(1/2\) affine offsets through the remaining slopes at most
\(3/2\). Thus
\[
       |T^L(I)|\ll Y\,2^{-L/40}+2^L+(3/2)^L ,
\]
using \(H_2(3/5)<39/40\), \(3^{3/5}/2<2^{-1/40}\).
For the selected \(c\) this gives \((L+1)|F|=O_w(X^{1-\eta_1})\)
with absolute effective \(\eta_1>0\). Any true rival with \(r>L\)
uses at least \(r\) shortcut steps; its endpoint \(y\in I\) is in this
set. Distinct \(n\) in the prescribed native cylinder have distinct
\(y\), by its positive affine slope. Therefore all arbitrarily late
first crossings together cost \(O_w(X^{-\eta_1})\) in relative mass.

The accepted ternary union through depth \(L-s\) is a union of cells
of modulus \(3^{L-s}\). Its relative shell frequency differs from
its Haar mass by \(O_w(3^L/X)\), counting complete dyadic-ternary
progressions with endpoint error at most one per cell. Every such cell
already supplies a true smaller witness. The first-crossing and
finite-image bounds cover every other actual source. Adding the
geometric Haar tail \(O_w(\gamma^{L-s})\) proves the power saving.
Dyadic summation gives the same density below \(X\), with a smaller
positive exponent if needed.

Mahler's paper treats the complete matched and shallower cylinder
problem and explicitly poses the deeper-horizon sieve. Its finite
\(0\)–\(1\) cylinder rule is consistent with the \(r\le s\) part
above. Deeper words can see new ternary digits of the original
positive integer. The all-depth density here resolves the density
question while retaining a specified native endpoint; it does not
supply a universal coalescence or classify every integer in the
infinite exceptional set.
[Mahler, paper 148, §§1, 9](https://rstation.ai/problems/collatz/papers/148/v1)

## Unit sources with no smaller ancestor

For the empty native word the relative density of odd \(n\) which have
no smaller odd ancestor is at least \(5/12\). Thus at least \(1/12\)
of all odd integers are *ternary units* with this all-depth property.
The same lower densities hold within each fixed odd dyadic class.

To see this, stop a word at the first backward prefix whose multiplier
\(R=2^B/3^r\) is strictly below one. Overlaps of its ternary cylinders
can only lower the union mass. Give the reverse letters the independent
law \(p_2(e)=3/4^e\), \(e\ge1\), which sums to one. Each stopped word
has Haar cylinder mass \(3^{-r}=p_2(w)R^2\). The single first-letter
crossing \(e=1\) contributes \(1/3\). Every other stopped word starts
with \(e\ge2\), and those distinct first-crossing words form a prefix
code. Their total \(p_2\)-mass is at most \(1/4\), so their Haar mass
is at most \(1/4\). This gives \(1-1/3-1/4=5/12\). Ternary nonunits
account for only \(1/3\) of the original population. In each fixed
dyadic class the same conclusions follow by CRT from finite ternary
unions and the unbounded physical tail bound.

## Both pinned inverse floors on large ordinary integers

For *any* fixed odd dyadic class there is a positive relative density of
ordinary \(n\) with both properties
\[
   U^r(b)=n\quad\Longrightarrow\quad b\ge n,\qquad
   U^r(b)=n,\ 3\mid b\quad\Longrightarrow\quad b\ge2n+1
\]
for every positive odd source \(b\) and every \(r\ge0\).
These minima are pinned to the individual physical value \(n\).
One can also require \(n\equiv1\bmod3^K\): as \(K\to\infty\) the
lower limit in \(X\) of the relative frequency in each such combined
class tends to one. Consequently a prescribed finite native future
word by itself cannot rule out either physical inverse floor at its
starting phase. The statement does not impose the floors relative
to the same \(n\) on all *later* phases of that native word.

For a positive rational root \(t=N/d\) in lowest terms, with \(N,d\)
odd and \(3\nmid d\), let
\[
 H_K(t)=\sum_{\substack{|v|=K\\v\ {\rm ternary\ compatible\ at}\ t}}
                     (3^K/2^{B(v)})^2 .
\]
Assume every ternary-compatible inverse word at this root stays
positive. This holds at every ordinary positive odd root, since
\((2^e u-1)/3>0\) when the odd numerator is integral. Then
\(H_K(t)\to0\). Each compatible inverse word gives a positive odd
numerator \(b\) on the denominator-\(d\) lattice, with
\(2^{B(v)}/3^K\ge b/N\). Each numerator occurs at most once at each
depth by forward determinism. For fixed \(b\),
if its forward orbit is nonrecurrent at the target, it occurs at most
once over all depths. If it hits a periodic target, successive periods
multiply \(2^B/3^K\) by the cycle product
\(\prod(1+d/(3b_i))>1\). Its reciprocal contribution tends to zero
also in this case. Dominated convergence uses \(\sum_{b\ge1}(N/b)^2
<\infty\). In the assertion about the two physical floors we use only
the ordinary root \(t=1\), where positivity always holds.

Conditional on a given ternary ball at \(t\bmod3^K\), each compatible
length-\(K\) word gives a Haar-uniform ternary continuation at its
new reverse target: the unused digits enter multiplied by the unit
\(2^B\). For any \(\tau>0\), the unconditional probability that some
finite continuation has multiplier at most \(\tau\), allowing length
zero, is at most \(\tau^2\) when \(\tau<1\), and at most one otherwise.
Indeed stop at its first such prefix, give each word the \(p_2\)-law
above, and use \(3^{-r}=p_2(w)R^2\). Union over the compatible initial
words proves the conditional bound
\[
  \Pr(\exists r\ge K:\ \text{a compatible word at depth }r
           \text{ has }2^B/3^r\le R\mid z=t\bmod3^K)
       \le R^2 H_K(t).                                           \tag{2}
\]

For the second floor the ternary union additionally counts words with
\(2^B/3^r<2\) whose terminal reverse source is divisible by three.
That last condition is one more ternary digit. The physical proof
above applies to the *first failure of either floor*. Before such a
reverse failure all intermediate odd sites are at least \(n\), and
the violating source \(b\) is at least \((2n-1)/3\) if \(r>0\).
Now \(b\le2n\), giving a budget
\(B\le1+r\log_2 3+O(r/X)\). Short depths have the same elementary
integer separation from \(2\cdot3^r\), and the late-visitor proof uses
\(I=[1,4X]\) to contain even the larger candidate sources. For a true
first failure with \(b<n\) use the original budget without the extra
one. Conversely the two corresponding strictly accepted budgets imply
the stated actual inequality for all bounded logarithmic depths, with
an eventual margin from the integers. The case \(r=0\) is just \(3\mid n\)
for a violation of the second floor. Hence the ordinary frequency of
the combined event is its ternary Haar mass on each fixed dyadic and
ternary class. All estimates allow the fixed class in the constant.

At \(t=1\), each compatible nonempty short word has \(2^B/3^r>b\)
where \(b\) is its positive odd inverse source. If it ends at a
multiple of three then \(b\ge3\). Thus no short violation occurs on
the ball \(1\bmod3^K\) at depths \(r<K\), including the extra ternary
digit. At all greater depths exclude *every* multiplier at most two
using (2), with cost at most \(4H_K(1)\to0\). This proves both physical
floors in the asserted positive proportions. A fixed binary future
word merely specifies one of the dyadic classes already allowed.
