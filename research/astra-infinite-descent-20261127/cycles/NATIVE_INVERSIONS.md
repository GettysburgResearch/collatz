# An exact conversion between dyadic and ternary crossings on ordinary cycles

Let $T$ be the shortcut map on all integers, $T(z)=z/2$ for even $z$ and $(3z+1)/2$ for odd $z$. On one primitive positive **integer** cycle let $h$ be the shortcut period and $p$ the number of odd phases. Choose $0<u<p$ with $c=uh/p\in\mathbb Z$; this is possible exactly when $\gcd(h,p)>1$. Fix an odd source $x$. Let $y$ be its $u$th subsequent odd phase, reached after $E$ shortcuts. Put $Y=T^c(x)$. The two lags use their literal clocks.

* At the odd clock, set $r=c-E$. A directed dyadic crossing compares $y$ with $2^rx$ and requires the positive order to reverse after the next odd-to-odd transitions, with the powers realigned. Equivalently $r\ge3$ and $y=2^rx+d$ with $0<3d<2^r-1$.
* At the shortcut clock, put $s=N_c(x)-u$, where $N_c(x)$ is the number of odd inputs in the first $c$ shortcuts from $x$. A directed ternary crossing compares $Y$ with $3^sx$ and requires the positive order to reverse after the next shortcuts, with the powers realigned. Equivalently $s\ge2$ and $Y=3^s x+d'$ with $0<3d'<3^s$.

**The same odd sources are directed crossings on both clocks.** At every such source,
\[
 r\ge s\ge2,\qquad s=N_r(d),\qquad d'=T^r(d).
\]
Thus the two positive residuals are linked by the actual shortcut trajectory of an ordinary positive integer. For $r=3$ the only odd residual is $d=1$, and $T^3(1)=2$, $N_3(1)=2$. The linked partners are $y=8x+1$ and $Y=9x+2$. For $r=4$ the possible residuals are $d=1,3$. Both have $s=2$, with $d'=1,2$ respectively.

## Local sign tests

Write $e,f$ for the next odd division counts at $x,y$, so the new dyadic exponent is $r'=r+e-f$. Then
\[
 2^f(y_{\rm next}-2^{r'} x_{\rm next})=3(y-2^r x)+1-2^r.
\]
A directed reversal is exactly the asserted dyadic inequality; it forces $r\ge3$ by integrality. Negative $r$ cannot give this direction.

More generally let $a,b\in\{0,1\}$ be the shortcut bits at the first and second partner. The next ternary exponent is $s'=s+b-a$ since the common comparison window loses its first bit and gains the partner's first bit. If $s\ge0$, put $D=Y-3^s x$ and $D'=3^a T(Y)-3^b3^s T(x)$. Its sign is the sign after realignment. Direct calculation gives
\[
       2D'=3^{a+b}D+3^ab-3^{s+b}a .
\]
A positive-to-negative crossing needs $a=1$ and $0<3D<3^s$. For $b=0$ this follows immediately; for $b=1$ the upper test is $3D<3^s-1$, equivalent on these integers once $s\ge1$. Neither $s=0$ nor $s=1$ can close the inequalities. Conversely $a=1,s\ge2,0<3D<3^s$ always reverses. A negative-to-positive crossing at $s\ge0$ is impossible: if $D\le-1$, the same four cases keep $D'<0$. If $s<0$, swap the lanes and multiply the two comparisons by the corresponding positive ternary powers to reverse both signs. Thus a positive-to-negative crossing needs $s\ge2$, with its smaller partner odd, even if the clock test starts at an arbitrary shortcut state.

## Conversion in both directions

For any integers $d,x$ and $r\ge0$, the first $r$ shortcut bits of $2^rx+d$ equal those of $d$. Successive affine composition gives
\[
 T^r(2^rx+d)=3^{N_r(d)}x+T^r(d).
\]
Also $0\le z<2^jM$ with integer $M>0$ implies $T^j(z)<3^{N_j(z)} M$. For $j\ge1$ the upper endpoint is even: in the even branch the next value is $<2^{j-1} M$, and in the odd branch it is at most $(3(2^jM-1)+1)/2=2^{j-1}(3M)-1$. Induction gives the assertion. Positive and nonpositive integers are each forward invariant.

At a dyadic crossing $r>0$. From $y$ there are exactly $r$ more steps to $Y$. The initial residual $d$ is odd and positive. Its first shortcut obeys $0<T(d)=(3d+1)/2<2^{r-1}$. Applying the cylinder bound over $r-1$ further steps gives $0<d'=T^r(d)<3^{s-1}$, with $s=N_r(d)$. The number of odd inputs between $x$ and $y$ is $u$, so this $s$ is exactly $N_c(x)-u$. The local ternary test proves the forward direction.

Conversely, at a ternary crossing $x$ is odd and $N_c(x)=u+s$ with $s\ge2$. Hence $y$ occurs strictly before $Y$, $r=c-E\ge s$, and its first $r$ shortcuts have $s$ odd inputs. For the signed integer $d=y-2^rx$, the affine identity gives $T^r(d)=d'>0$. Nonpositive invariance gives $d>0$. Write $2^r d'=3^s d+C$, where the ordinary affine carry $C$ is nonnegative. Then $d<2^r/3$. If $3d+1=2^r$, the first shortcut from odd $d$ is $2^{r-1}$ and all the remaining $r-1$ inputs are even, contrary to $s\ge2$. Therefore $3d+1<2^r$, completing the equivalence.

## Separation and scope

For fixed $u$, the sign comparisons are meaningful at every phase: distinct odd phases lie on distinct dyadic rays. Every shortcut phase of an ordinary cycle is prime to three, since an odd step produces a ternary unit and even steps preserve that property; hence distinct shortcut phases also lie on distinct ternary rays. The product of all ratios $y/(2^rx)$ over the $p$ odd phases is one because $\sum E=uh=pc$. Both signs occur by periodicity. Consequently each proper resonant lag has a directed crossing and the opposite crossing, and at the matching shortcut lag the counts $N_c$ attain at least $u+2$ and at most $u-2$. The latter follows by swapping at a negative-to-positive crossing, or by applying the positive crossing bound at complementary lag $h-c$.

Weaver and Wren had already given the dyadic separation-by-lag argument and minimum $8x+1$ crossing, while earlier repository work gave backward ternary inversions and their global counts. The finite affine transport gives the identification of both directed forward clocks at every smaller source and its exact residual update. The existence of many crossings on two clocks therefore does not, on its own, supply independent obstructions. It yields no contradiction for general amplitudes or coprime periods. The sign-invariance argument is specific to integer residuals: e.g. $T(-1/5)=1/5$ with native rational parity. [Weaver, §2, with Wren's separation argument](https://rstation.ai/problems/collatz/papers/114/v1) · [Earlier global order and ternary inversions](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-global-synthesis-20261124/arithmetic/proof.md)

[Lean signed arithmetic kernel](NativeInversion.lean) proves exact transport of all integer paths shifted by a dyadic cylinder, the sharp upper cylinder bound, positive-source necessity, the aligned one-step identities and sign thresholds, and a finite adjacent reversal lemma. The period-to-lag identification and resulting bijection are written proofs.
