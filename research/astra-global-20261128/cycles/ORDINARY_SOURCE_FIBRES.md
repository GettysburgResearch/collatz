# The complete ordinary equal-date fibre has Brownian logarithmic size

Use the shortcut map $T$, let $n$ be uniform on the integer octave $I=[X,2X)$, and let $N=N(X)\to\infty$ with $2^N=o(X)$. Define the genuine source fibre at each date,
\[
       K_j(n)=\#\{m\in I:T^jm=T^jn\}.
\]
With probability tending to one,
\[
 \max_{0\le j\le N}\left|\log K_j(n)-j\log2+k_j(n)\log3\right|
                                        \le C\log(2+N) .                \tag{1}
\]
Here $k_j$ counts true odd departures. In particular the logarithmic size divided by $N$ tends in probability at date $N$ to $a=\log(4/3)/2$. The linearly interpolated path
\[
       \frac{\log K_{\lfloor Ns\rfloor}(n)-aNs}{\sqrt N},
                 \quad 0\le s\le1 ,
\]
converges in law to $-(\log3)B_s/2$ for standard Brownian motion. The path estimate and this one-source limit require no counted-fusion or inverse-density input. The proof uses true integer fibres, elementary concentration and the usual invariance principle for independent fair bits.

More generally take a fixed finite collection $x_i=A_i n+b_i$ with positive odd $A_i$, fixed integer $b_i$ and $A_i/A_l\notin3^{\mathbb Z}$ for $i\ne l$. Count every ordinary integer source in the corresponding octave $[A_iX+b_i,2A_iX+b_i)$ having the same date-$j$ image as $x_i$. Their centred logarithmic fibre processes converge to **independent Brownian motions** with the scale above, under the [joint physical grade theorem](MULTIPLIER_BERNOULLI_JOINING.md) and its stated two-adic logarithm input. These fibres count all starts in the target source octave, not just the progression sampled for their distinguished root.

## Finite translation classes

The $j$ true parity bits are in bijection with source residues modulo $2^j$. Let $i_l$ be these bits, $k_l$ their prior running count, and put
\[
 R_j=\sum_{0\le l<j}i_l\,\frac{2^l}{3^{k_{l+1}}},\qquad
 T^j x=\frac{3^{k_j}}{2^j}(x+R_j).                                    \tag{2}
\]
This follows by induction, including $x\in\mathbb Z_2$ with the rational coefficients embedded there. We also use $R_j$ as a nonnegative real computed from the finite word. In particular $0\le R_j<2^j$. With $r$ the least nonnegative source residue, $z=T^j r$ satisfies $0\le z<3^{k_j}$. For completeness the strict upper follows by induction on stripping the first step from bases of varying size, or as follows. The quotient identity holds for one step: if $r<2^j$ the remaining high binary variable is $u$. An equivalent direct bound starts at a word of length zero and appends a new *source bit* $v$ to its existing $j$ bits. At time $j$ the new state is $z+3^{k_j}v$. If it is even, its half is $<3^{k_j}$. If it is odd, $(3(z+3^{k_j}v)+1)/2\le(3(2\cdot3^{k_j}-1)+1)/2<3^{k_j+1}$. This proves the induction.

For two-adic $x$ define
\[
 C_j(x)=\{h\in\mathbb Z:T^j(x+h)=T^j x,\ k_j(x+h)=k_j(x)\}.
\]
Any $h\in C_j(x)$ equals $R_j(x)-R_j(x+h)$ by (2), so $|h|<2^j$. In fact these classes are exactly the fibres of the finite map $r\mapsto(k_j(r),T^j r)$. Write $x=r+2^j u$ and $x+h=r' +2^j(u+d)$ with both residues in the standard range and $d\in\mathbb Z$. At common grade $k$ equality gives $z=z'+3^k d$ for two integers in $[0,3^k)$, hence $d=0$ and $z=z'$. The converse follows from the same formulas. Thus the displacements are exactly the differences $r'-r$ inside one such fibre, and all members keep the high binary tail. Changing the root to a class member translates the class and preserves its cardinality. The map $x\mapsto x+h$ preserves fair Haar measure, and it preserves the tilted first-source parity measure $\mu_p$ **on its class-member domain** as well. Indeed for each source residue the other word has precisely the same length and grade. Its future parity sequence equals the initial root's after date $j$. These matched cylinders and every continuation therefore have identical tilted mass. This partial translation property proves uniform rooting inside each finite class: for any predicate $P$ of a class and its distinguished member,
\[
 \mathbb E P(x,C_j(x))
   =\mathbb E\left[\frac{1}{|C_j(x)|}
                \sum_{h\in C_j(x)} P(x+h,C_j(x)-h)\right].              \tag{3}
\]
Each $h$ in the finite sum can be reversed using its partial measure-preserving translation. Equivalently, (3) follows by partitioning the $2^j$ words into finite equivalence classes, each with a common grade; their displacements order them on the integer line. Distinct words cannot have identical offset at the root. For a fixed word and another word the relation is decided by integrality of $R_j(x)-R_j(x')$ and the source parity residues after translating by it. This description also proves the claimed finite partition directly.

## The size sandwich

At fixed grade $k_j=k$, conditionally uniform under any fixed tilt, there are $\binom jk$ equally likely words and at most $3^k$ possible integers $z=T^j r$. All words giving the same pair $(k,z)$ yield class members: changing $r$ to such an $r'$ keeps the same high binary tail and the same endpoint. Thus for any $M\ge1$,
\[
 \Pr\left\{|C_j|<\binom jk/(M3^k)\mid k_j=k\right\}\le 1/M.          \tag{4}
\]
From (2) the number of nonnegative displacements in the class is at most $1+R_j(x)$. With the uniform-root identity (3), the fraction of members in any finite class having fewer than its size divided by $M$ members weakly to their right is at most $1/M$. In particular
\[
    \Pr\{|C_j(x)|>M(1+R_j(x))\}\le1/M.                               \tag{5}
\]
This holds at every tilt, independently of any asymptotic description of the endpoint.

Now use fair independent parities and set $S_j=j\log 2-k_j\log3$. Its iid increments are $\log2$ or $\log(2/3)$ with mean $a>0$. Choose $0<q<1$ so $\mathbb Ee^{-q(S_1-S_0)}=u<1$, possible by differentiation at zero. From (2),
\[
  (1+R_j)e^{-S_j}\le e^{-S_j}+\sum_{l<j}e^{S_l-S_j}.
\]
Subadditivity of the $q$th power and independence give
$\sup_j\mathbb E[((1+R_j)e^{-S_j})^q]\le 1+(1-u)^{-1}$. Taking a polynomial threshold in $N$ and summing over $j\le N$ bounds $1+R_j\le e^{S_j}(2+N)^C$ at all these dates with probability tending to one. Equations (4)–(5) similarly hold throughout with $M=(2+N)^3$.

We also have $\log\binom{j}{k_j}\ge j\log2-C\log(2+N)$ uniformly over all $j\le N$ except with probability tending to zero. At each individual date the combined fair-binomial mass of the at most $j+1$ grades with probability below $(2+N)^{-4}$ is at most $(j+1)(2+N)^{-4}$. Sum in $j$. Substitution in (4) gives $\log |C_j|\ge S_j-O(\log(2+N))$ on the same event. The upper comes from (5). This proves the dyadic form of (1).

## Full ordinary fibres and entropy

For $n,m\in I$ at large $X$, formula (2) and $R_j<2^N=o(X)$ force equal grades whenever $T^jm=T^jn$ and $j\le N$: the positive ratio $(n+R_j(n))/(m+R_j(m))$ lies strictly between $1/3$ and $3$, and equality of endpoints makes it a power of three. Thus these ordinary displacements are exactly the elements of $C_j(n)$ keeping the other source in $I$. With probability $1-O(2^N/X)$ the root is at distance at least $2^N$ from both octave endpoints, so all its counted displacements stay in $I$ simultaneously. On a fixed odd-step affine progression the analogous boundary fraction is still $O(2^N/X)$, and the ratio remains between the two stated constants with the fixed endpoint shift. The binary prefix law there differs from uniform by $O(2^N/X)$ in total variation. This establishes (1). The standard one-source Donsker theorem or the cited joint grade theorem, followed by the uniform error divided by $\sqrt N$, proves the path limits.

For the full ordinary octave, writing $U$ for its uniform root, the output entropy satisfies
\[
 H(T^N U)=\log |I|-aN+O(\log(2+N))+O(N2^N/X).                          \tag{6}
\]
Indeed the entropy loss is $\mathbb E\log K_N$. For the fair prefix, (4) gives an exponentially decreasing upper tail in the logarithmic deficit from $\log\binom Nk-k\log3$, hence an absolute expected deficit bound. The expected binomial log mass is minus the binomial entropy, bounded by $\log(N+1)$. Equation (5) gives an absolute expected upper excess of $\log |C_N|$ over $\log(1+R_N)$ by the same integration; the fractional moment above bounds the expected positive part of $\log(1+R_N)-S_N$ absolutely. Therefore $\mathbb E\log|C_N|=aN+O(\log(2+N))$. Each true fibre has at most $2^N$ members at large $X$ by the equal-grade reduction and one member per parity word. Binary discrepancy and octave boundary losses thus cost at most $O(N2^N/X)$ in the expectation.

[Paper 19, Sections 5–8](https://rstation.ai/problems/collatz/papers/19/v2) already gives an integer partition, mass transport, moments and conditional coding entropy for coverings of a unit real–ternary seed, with one covering word per represented odd count there. The classes here consist of all ordinary integer translations with the *same* odd count and the same physical endpoint, sampled in their source octave. The growing class-size law, the uniform physical-date estimate and its transfer to unrestricted ordinary octave preimages use precisely that different fibre. A distinguished hypothetical cycle root is outside the typical-source assertion.

## A common fibre for every affine source at once

There is a stronger statement about the *same* perturbation of the shared ordinary input. Fix $r$ odd affine sources as above; their slopes may even coincide for the deterministic estimate. For $n\in I$ let
\[
 K_j^{\rm joint}(n)=\#\{m\in I:T^j(A_im+b_i)=T^j(A_i n+b_i)\ 
                                           (1\le i\le r)\}.
\]
With probability tending to one, simultaneously for $0\le j\le N$,
\[
     \log K_j^{\rm joint}(n)
       =j\log2-\max_i k_j(A_i n+b_i)\log3+O_{\mathbf A,\mathbf b,r}(\log(2+N)).
                                                                          \tag{7}
\]
In particular a single typical input has $\exp(aN+o(N))$ distinct ordinary source perturbations preserving **all** $r$ exact terminal values and therefore every later synchronous orbit at those sources. If the multipliers are pairwise nonsmooth, the centred log common-fibre path, divided by $\sqrt N$, converges to $-(\log3)\max_{i\le r}B_i(s)/2$ for independent standard Brownian motions. The fluctuations of this common size differ from the independent fluctuations of the separately counted fibres.

Here is the lower bound, which cannot be inferred by intersecting large subsets. Work first with a uniform root residue $v\bmod 2^j$ in its standard range. At coordinate $i$ put $k_i=k_j(A_i v+b_i)$, $R_i=R_j(A_i v+b_i)$ and $D_i=3^{k_i}R_i/2^j$. The fractional moment proof above shows $D_i\le(2+N)^C$ except with probability $O_r(N^{-4})$ simultaneously for all coordinates and dates, taking $C$ sufficiently large, since each $A_i$ is odd. Fixed negative offsets are allowed: the parity coding and (2) remain valid for signed integer intermediates, and their absolute contribution $3^{k_i}|b_i|/2^j$ below may be retained in the common line parameters. Write $z_i=T^j(A_i v+b_i)$. Then
\[
      z_i=3^{k_i}(A_i v+b_i)/2^j+D_i .
\]
At each fixed grade vector, choose $u$ maximizing $A_i3^{k_i}$. In the entire range $0\le v<2^j$, all good roots give at most $C(3^{k_*}+N^C)$ possible integer values of $z_u$, where $k_*=\max_i k_i$. This follows from the range of its affine main term, with fixed intercept, and the bound on $D_u$. For each such $z_u$, eliminating $v$ shows $z_i$ lies within $2(2+N)^C$ of
\[
       \frac{A_i3^{k_i}}{A_u3^{k_u}}z_u
             +\frac{3^{k_i}}{2^j}\left(b_i-\frac{A_i}{A_u}b_u\right).
\]
The last quantity includes the fixed intercept difference at the correct scale; it need not be bounded. The slope ratio is at most one. Hence on good roots the total number of integer output vectors at this grade vector is at most $3^{k_*}(2+N)^{C_r}$, with coefficients uniform in the date for the fixed family. There are at most $(1+N)^r$ grade vectors. For any $D>C_r+r+4$, the fraction of all roots in good cells $(\mathbf k,\mathbf z)$ of cardinality below $2^j3^{-k_*}(2+N)^{-D}$ is $O(N^{-3})$ after summing over all grades. The masses here are the original unweighted binary-root masses, so no conditional local central-limit estimate for the grade vector is needed. A summation over dates is harmless.

If $v'$ is in the same cell as $v$, then at every common higher binary tail $q$,
\[
   T^j(A_i(v'+2^jq)+b_i)=z_i+A_i3^{k_i}q
                         =T^j(A_i(v+2^jq)+b_i)
\]
for every coordinate. Thus this many ordinary source shifts work, with $|v'-v|<2^j$. Roots at distance $\ge2^N$ from octave edges keep every such shift. The upper in (7) follows from the fibre of any single coordinate: distinct $m$ give distinct $A_i m+b_i$ and the coordinate source interval is the corresponding full shifted octave there. The earlier one-source path estimate applied simultaneously gives the minimum of those upper bounds. For use in transferring the exceptional probabilities, one can instead apply (5) before rounding. Within the affine source octave, for $X$ large equal physical endpoints force equal grades for every $j\le N$, by the factor-three argument. The resulting actual $K_j^{\rm joint}$ is bounded above by the full two-adic counted class at each coordinate, regardless of octave boundary. All prefix tests depend only on the common $n\bmod2^N$, giving a single $O(2^N/X)$ mass loss. This proves (7) and its functional consequence.

The preceding exceptional estimates may be made $O(N^{-A}+2^N/X)$ for any fixed $A>0$, by increasing the powers in the thresholds (and hence the implicit log-error constant). The loss $2^N/X$ includes roots near an interval endpoint. The trivial $K_j^{\rm joint}\le 2^j$ holds for $j\le N$ at large $X$ by injection into one coordinate's counted class. Integrating the fixed-date version therefore yields
\[
 H((T^N(A_iU+b_i))_{i\le r})
   =\log|I|-N\log2+\log3\ \mathbb E\max_i k_N(A_iU+b_i)
                  +O(\log(2+N)+N2^N/X).                                \tag{8}
\]
Under the additional quantitative rounding condition $\sqrt N\,2^N=o(X)$, the normalized maximum in (8) has the same first moment limit as the Haar maximum. Indeed its range after centring and division by $\sqrt N$ is $O(\sqrt N)$, and the total variation discrepancy is $O(2^N/X)$. The Haar second moments are bounded using $\max_i |2k_N-N|^2\le\sum_i(2k_N-N)^2$ and the native binomials. Uniform integrability and the joint invariance principle now give for a pairwise nonsmooth family
\[
 H((T^N(A_iU+b_i))_{i\le r})
     =\log|I|-aN+\tfrac12(\log3)\sqrt N\,
                       \mathbb E\max_{i\le r}G_i+o(\sqrt N),             \tag{9}
\]
where the $G_i$ are independent standard normals. For $r=1$ this expectation is zero. In particular for two such genuine terminal endpoints $Y_1,Y_2$, the conditional Shannon entropy satisfies
\[
           H(Y_2\mid Y_1)\sim\frac{\log3}{2\sqrt\pi}\sqrt N.             \tag{10}
\]
Here $\mathbb E\max(G_1,G_2)=\tfrac12\mathbb E|G_1-G_2|=1/\sqrt\pi$. The entropy is computed under the shared ordinary source $U$, and the individual output $Y_1$ in this subtraction has the same underlying progression source as its joint marginal.

[NativeSourceFibre.lean](NativeSourceFibre.lean) proves the full natural-number quotient identity and equivalence of counted equal-date fusion to a common high binary quotient and the same explicit low grade/endpoint pair. Its arbitrary finite-list lifting theorem preserves simultaneous genuine terminal equality on any common higher source. Its five public environments compile with propositional extensionality and quotient soundness only. The [integer control](check_native_fibres.py) checks true full-octave joint classes, all tails in finite tilted examples, and exact floor reparametrizations used beyond this binary horizon. [Control output](../../../reports/astra-global-20261128/cycles/NATIVE_FIBRES.json) · [Critical physical pair-word continuation](PRECRITICAL_PAIR_WORDS.md)
