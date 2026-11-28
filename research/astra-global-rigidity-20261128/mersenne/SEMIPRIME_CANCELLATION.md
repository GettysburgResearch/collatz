# Semiprime ancestors and a four-prime cancellation test without RH

Use the shortcut map $T(2a)=a$, $T(2a+1)=3a+2$. Let $R(n)$ mean that the positive orbit from $n$ visits 1. Let $F(n)$ require this visit within $5(1+\lfloor\log_2n\rfloor)$ shortcuts. Let $F_v(n)$ require a visit to $v$ followed by 1 by that deadline, where $v=5$ or $85$. Each is a finite test except $R$.

For large $Y$ let $\mathcal E(Y)$ contain the integers $Y<m\le2Y$ of the form $m=pq$, with $p,q$ prime and
$$
               (\log Y)^{1.05}<p\le(\log Y)^{1.15}.
$$
The factors are automatically distinct with $p<q$. The prime number theorem, uniformly for the intervals of large primes $Y/p<q\le2Y/p$, and Mertens' theorem give
$$
      |\mathcal E(Y)|\sim \log(1.15/1.05)Y/\log Y.                       \tag{1}
$$

**Semiprime supply.** Every prescribed positive integer $d$ has $\gg Y/\log Y$ distinct coprime cofactors $m\in\mathcal E(Y)$ such that $F_5(dm)=1$, and separately as many with $F_{85}(dm)=1$, whenever $Y\ge\max(Y_0,d^A)$ for absolute constants $A,Y_0$. Every fixed target $y$ prime to three likewise has $\gg_y Y/\log Y$ predecessors in $d\mathcal E(Y)$, allowing the constants $A,Y_0$ to depend on $y$. For any supplied start $s$, take $y=s$ if $3\nmid s$ and otherwise strip powers of two from $s$ and take one odd shortcut. This puts an actual semiprime ancestor, obtained with $d=1$, in the component of $s$.

**Decidable four-prime test.** Take $V=2^k$, $Y=2^{k^2}$ and one fixed $v\in\{5,85\}$. Among all ordered pairs $(D,m)\in\mathcal E(V)\times\mathcal E(Y)$, measure the fraction satisfying
$$
             (D,m)=1,\qquad F(D)=0,\qquad F_v(Dm)=1.                    \tag{2}
$$
If every positive orbit reaches 1 this fraction tends to zero. If even one positive orbit misses 1 the fraction has a strictly positive lower limit. The latter conclusion holds separately for either choice of $v$. The population is the indicated pair of restricted semiprime octaves; no fraction among all four-prime integers is asserted. The equivalence uses the source-qualified Collatz inputs below, including the convergent-basin clock law for the zero limit. None of the number-theoretic steps requires RH.

Paper 233 proves an ordinary-RH prime-multiplier estimate, an all-semiprime two-prime mismatch law with additional clock inputs, and a pointwise cancellation criterion. We replace the prime multiplier by a product of two distinct primes with a controlled smaller factor. Matomäki and Teräväinen supply an unconditional short-interval lower count for that arithmetic population. A separate shifted second moment is needed for the implication from universal convergence to the zero limit. [Paper 233](https://rstation.ai/problems/collatz/papers/233) · [Matomäki–Teräväinen, Theorem 1.1](https://doi.org/10.1090/tran/8869).

## Transport from all integers to the restricted semiprimes

Put $L=\log Y$, $H=\lceil(\log(3Y))^{2.1}\rceil$, $t=\lfloor(\log_2Y)/4\rfloor$ and $Q=2^t$. Use $w(n)=1$ if $n$ has the indicated factorization with the small-prime band defined using $Y$, also just outside the octave. Let $C(z)\in[0,1]$ be a mark agreeing at any two sources counted-fused by time $t$. Visit indicators and the joint visit to $v$ and 1 by a common later deadline qualify here because all states up to $t$ remain above the fixed tested vertices. Write $E_Z C=Z^{-1}\sum_{Z<n\le2Z}C(n)$ for integer $Z$.

For odd $D\le Y^{1/2}$ put $Z=DY$. The pair theorem on source differences $Dj$, $j\le H$, excludes at most $O(Q\epsilon)$ binary classes, with
$$
          \epsilon=\sqrt{(1+\log(2DH))/\log Y}.
$$
Multiplication of the parameter by $D$ permutes the classes. On any odd parameter class $a\pmod Q$ and an octave of size $\asymp Y$, Brun–Titchmarsh applied at each small prime $p$ gives
$$
 \sum_{n\equiv a\;(Q)}w(n)
  \ll\sum_{p\text{ in band}}\frac{Y}{p\phi(Q)\log(Y/(pQ))}
  \ll\frac{Y}{QL}.                                                     \tag{3}
$$
Here $p$ and $a$ are units modulo $Q$, $pQ\le Y^{1/3}$ eventually and the band's reciprocal prime mass is bounded. All $w(n)$ in the relevant octaves are odd. Thus the weighted cost of replacing $C(Dn)$ by $C(D(n-j))$ is $O(\epsilon Y/L)$, uniformly for $j\le H$. Averaging over $j$ and trimming endpoints gives
$$
 \frac L Y\sum_{m\in\mathcal E(Y)}C(Dm)
   =\frac1Y\sum_{Y<u\le2Y} C(Du) S(u)
     +O(\epsilon+HL/Y),\qquad
 S(u)=\frac LH\sum_{1\le j\le H}w(u+j).                               \tag{4}
$$
To compare the unweighted parameter mark with the full product octave, average $C(Du+i)$ over $0\le i<D$. Each pair $Du,Du+i$ has at most $O(Q\epsilon)$ failed classes, and integer periodic counting costs $O(Q/Y)$, uniformly in $i$. The blocks tile the product octave up to $O(D)$ ends. Therefore
$$
       E_Y[C(Du)]=E_Z C+O(\epsilon+Q/Y).                               \tag{5}
$$
This is the integer averaging argument from Paper 233 §3. [Pair estimate, Paper 209, Theorem 4.2](https://rstation.ai/problems/collatz/papers/209) · [Montgomery–Vaughan, Brun–Titchmarsh](https://doi.org/10.1112/S0025579300004708).

By Matomäki–Teräväinen's Theorem 1.1, for all but $O(Y/(\log Y)^\delta)$ of the parameters $Y<u\le2Y$, the interval $(u,u+(\log u)^{2.1}]$ contains $\gg(\log u)^{1.1}$ products of two primes with $(\log u)^{1.09}<p\le(\log u)^{1.1}$. This interval lies in our $H$-window and this narrower factor range lies in our band uniformly. Hence $S(u)\ge c_0>0$ except on $o(Y)$ parameters. Equations (4) and (5) give
$$
 \frac L Y\sum_{m\in\mathcal E(Y)} C(Dm)
          \ge c_0 E_Z C-O(\epsilon)-o(1).                              \tag{6}
$$
The $o(1)$ is uniform in $D$ and the mark. For each $v=5,85$, let $C$ require both visits by the common deadline $5\lfloor\log_2 Z\rfloor$. The positive ordinary-clock predecessor theorem at $2v$, the distinct odd-part lifts to one octave, and the ordinary-to-shortcut first-clock calculation in Paper 233 §3 give $E_Z C\ge c_1>0$ for large $Z$, with no prime sampling involved. For a fixed unrestricted visit to $3\nmid y$ use the positive ordinary octave bound for that target. Choose a fixed $\kappa<1/2$ sufficiently small so that (6) stays positive for $D\le Y^\kappa$. For general $d=2^eD$, prepend $e$ halvings to the track. The actual deadline from $dm$ gains at least $5e$ relative to the common one from $Dm$, which pays for all $e$ steps.

For coprimality assume $d\le Y^\kappa$. The large factor $q>Y/L^{1.15}$ cannot divide $d$. Deleting small $p\mid d$ costs
$$
   \ll \frac Y L\sum_{p\mid d,\ p>L^{1.05}}\frac1p
   \ll \frac Y L\frac{\log(2d)}{ L^{1.05}\log(L^{1.05})}
   =o(Y/L).
$$
This proves the stated polynomial supply, including coprimality. The marked set may be found by trying semiprimes and running the explicit finite test when the required endpoint has a finite deadline.

## Why a zero-density late-arrival population remains negligible

The local lower count alone cannot transfer a zero-density exception. To bound it define a completely multiplicative function $0\le U\le1$ by $U(p)=1$ at 2, all primes in the small band and all primes above $Y^{2/5}$, and $U(p)=0$ on the other primes. Then $w\le U$ on every octave needed for (4). Mertens gives, uniformly for $x\asymp Y$,
$$
 \prod_{p\le x}\left(1+\frac{U(p)-1}{p}\right)\ll L^{-1},
 \qquad
 \prod_{p\le x}\left(1+\frac{2U(p)-2}{p}\right)\ll L^{-2}.
$$
The reciprocal mass of retained odd primes up to $x$ is bounded, and setting $U(2)=1$ makes the factor at 2 in the second product positive. Apply Matomäki–Radziwiłł II, Lemmas 3.2 and 3.3, to $U$. In Lemma 3.3 take $r_1=r_2=1$, $K=H$ and an interval of length comparable to $Y$. They give
$$
      \sum_{n\asymp Y} U(n)\ll Y/L,\qquad
      \sum_{0<|j|\le H}\sum_{n\asymp Y} U(n)U(n+j)\ll HY/L^2 .
$$
Expand $S(u)^2$. Each diagonal $n$ occurs at most $H$ times, as does each pair $(n,n+j)$. The displayed estimates show $E_Y S^2\ll 1+L/H\ll1$. Consequently (4) and Cauchy–Schwarz give, at $D=1$,
$$
 \frac L Y\sum_{m\in\mathcal E(Y)} C(m)
           \ll \sqrt{E_Y C}+O\!\left(\sqrt{\log(2H)/\log Y}+HL/Y\right).
                                                                            \tag{7}
$$
Taking absolute values is legitimate since $0\le C\le1$, so $C^2\le C$. [Matomäki–Radziwiłł II, Lemmas 3.2–3.3, including the Henriot shifted estimate](https://arxiv.org/pdf/2007.04290).

If all starts reach 1, Leen's convergent-basin clock theorem implies that $o(V)$ integers in the first octave miss the common deadline $5\lfloor\log_2 V\rfloor$. The coefficient in binary rank is $2\log2/\log(4/3)<5$. The common-deadline failure mark agrees under counted fusion at time $t$, since before fusion neither orbit can reach 1. By (7) it occupies $o(|\mathcal E(V)|)$ of the sparse first coordinates. Failure of the actual deadline implies failure of this common one. This proves the zero limit in (2). If $s$ misses 1, use its unit target $y$ in (6) at $D=1$ on the first octave. A positive fraction of $\mathcal E(V)$ physically visit $y$ and miss 1 forever. Apply the proved cofactor supply at each such $D$ in the second octave; $D\le2V=Y^{o(1)}$ and all lower bounds are uniform. Each resulting product has four distinct prime factors and passes $F_v$. This proves the positive lower limit.

There is also a pointwise consequence with at most three distinct primes. If $R(pqr)=R(p)R(q)R(r)$ for every triple of distinct odd primes, identifying truth with 1 and falsehood with 0, then every positive integer reaches 1. Indeed each odd prime $p$ divides a fast triple $pm$ by (6) and coprimality, so every odd prime converges. The hypothesis then makes every such triple converge. With $d=3$, the same supply puts a squarefree triple $3m$ in each supplied component. Conversely universal convergence gives the identity immediately. The multiplicative identity remains unproved.

## Integer controls

For $k=9$, the prefix $553=7\cdot79$ reaches 1 at step 87 against deadline 50. Two coprime restricted semiprimes from the prescribed $2^{81}$ octave give products reaching 1 through 5 at step 309 and through 85 at step 293, with common deadline 455. At $k=14$, $16{,}423=11\cdot1493$ first reaches 1 at step 103 against deadline 75. Its two products reach 1 at steps 1017 and 844, with common deadline 1055. The verifier uses integer comparisons for the factor bands, trial division for the small primes, and Pocklington certificates for the large cofactor primes. These four actual mismatches have terminating prefixes. Only their asymptotic frequencies enter (2). [Verifier](check_semiprime_cancellation.py) · [Exact receipts](semiprime_cancellation_controls.json).
