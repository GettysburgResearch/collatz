# Can the parent's stopping certificate produce the child's?

**PROPOSED written arithmetic results. Universal transfer OPEN.** Use the
positive ordinary shortcut map $T$ and let $C$ be the basin of 1. PR193's
remaining implication is $36k+8\in C\Rightarrow72k+17\in C$ for every
integer $k\ge0$. Write $u=9k+2$. The left side halves twice to $u$.
The right side follows $8u+1,12u+2,6u+1,9u+2$. We attempted to convert
the supplied certificate of this particular $u$ into a certificate for
the particular child $n=9u+2$.

## Exact height and an inverse for the certificate numerator

The dyadic companion of PR182 satisfies $D(x)=e+2^{1+e}D(Tx)/3$, where
$e=x\bmod2$, and $D(1)=9$. Let $\tau(x)$ be the first shortcut clock at
which $x$ reaches 1, including zero. For every $x\in C$ the reduced
denominator of $D(x)$ is
\[
                           3^{\max(0,\tau(x)-2)}.                  \tag{1}
\]
The unique final two edges of any first hit of length at least two are
$4\to2\to1$. The sole odd preimage of 2 is 1, excluded before the first
hit. The companions of 4, 2 and 1 are 4, 6 and 9 respectively. From
$B/3^j$ with $3\nmid B$, either reverse edge has numerator $2B$ or
$3^{j+1}+4B$ over $3^{j+1}$. Both numerators are units modulo 3.
First-hit times zero and one belong to 1 and 2. By PR182's triadic
equivalence the complete list of integer companions on positive ordinary
sources is therefore $9,6,4$.

For a supplied reduced $A/3^h$, $h>0$, one can decide if *any* positive
source has this companion and recover that source. An even numerator
forces the even physical edge, with next numerator $A/2$. An odd
numerator requires $A=3^h+4B$ for a nonnegative integer $B$ and forces
the odd edge. Continue with denominator exponent $h-1$. At zero require
numerator 4 and set the terminal physical state to 4. Recover each even
predecessor as $2y$, and each odd predecessor as $(2y-1)/3$, requiring
an integer. A failing test excludes the candidate globally. Negative
candidates cannot occur by the positive backward recurrences. For $h=0$
apply the three explicit exceptions above. This takes $h$ decoding
steps and gives no upper bound on a successful child's exponent.

[ParentCertificate.lean](ParentCertificate.lean) proves soundness and
completeness of this executable natural-number decoder on the inductive
physical words terminating at 4, and that their numerators are units
modulo 3. Every such word reaches 4 for the first time, since the subsequent
forward states belong to $\{1,2\}$. Reduction of first hits to this grammar
and identification with the dyadic series use the written argument above.

## Consuming the complete ordinary parent word

Represent the child at the current clock by $v=3^s x+d$ with $x$ the
current parent state. Initially $(s,d)=(2,2)$. For their respective bits
$e,f$, consuming one parent letter gives the exact section
\[
                s'=s+f-e,\qquad 2d'=3^f d+f-3^{s'}e .
\]
Signed $s$ and $d\in\mathbb Z[1/3]$ are allowed. The parent word
strictly shortens, but when it ends the residual child is the ordinary
integer $3^s+d$, whose convergence still needs a proof.

For the zero-only parent words $0^{6j+1}$ one has $u=2^{6j+1}\equiv2\bmod9$.
At exactly the clock where the parent reaches 1 the child reaches
$3^{3j+2}+1$. Its first step halves to $9\cdot4^{3j}+1$ and $4z+1$
then reaches $3z+1$ in two steps. This is formalized for every $j\ge0$.
The no-odd-letter base thus still contains unbounded ordinary terminal
states. There the right arm is 1 modulo $3^{3j}$ and has consumed $3j$
odd bits. Fitting terminal power $2^0=1$ through that congruence recovers
the *different* positive starting source $n-9\cdot2^{6j+1}=2$. It gives
no child certificate. No well-founded replacement controlling these
terminal states and the general word has been established.

## The height cost of completing a nearby source

Fix one ordinary $n>0$, including the child whose convergence is unknown.
Write $x_r=T^r n$ and $P_r$ for the number of odd inputs before clock $r$.
Take $m>n$ in $C$ and let $m=n+2^r k$ at its exact native precision,
so $k$ is positive odd. The common $r$ branches give
$T^r m=x_r+3^{P_r}k$. The next physical parities differ. Thus the exact
dyadic companion precision is $v_2(D(m)-D(n))=r+P_r$ by finite splitting,
since each companion has its physical source's parity. Also $\tau(m)>r$
because $2^{\tau(m)}\ge m>2^r$. At large $r$ its reduced denominator
exponent in (1) exceeds $r+P_r\log_2 3-2$, as
$2^{\tau(m)}\ge 3^{P_{\tau(m)}(m)}m>3^{P_r}2^r$.

**Bounded-odd-tail estimate.** For every fixed $n>0$, integer $Q\ge0$
and real $A>0$, there is an $r_0(n,Q,A)$ such that every such distinct
lift with $r\ge r_0$ and at most $Q$ odd inputs from clock $r$ to its
first hit satisfies
\[
                              k>\exp(Ar).                           \tag{2}
\]
The same lower bound holds if an initially prescribed common precision is
less than the exact one: at the higher exact precision the lift quotient
decreases and the remaining odd count cannot increase. A negative
nonzero adjustment preserving positivity is impossible once $2^r>n$.

For the fixed ordinary source, at every pair of consecutive shortcuts with
$b$ odd inputs, $3T^2(x)\le3^b x$. For bit pairs $00,01,10,11$ the
two-clock outputs are $x/4,(3x+2)/4,(3x+1)/4,(9x+5)/4$ respectively,
and the last pair has $x\ge3$. An extra single step satisfies
$T(x)\le3^{x\bmod2}x$. Iteration gives
\[
                       x_r\le\sqrt3\,n\,3^{P_r-r/2}.                \tag{3}
\]
Both the two-clock inequality and its iteration through an arbitrary
number of pairs are machine checked.

If the lift tail has length $t$ and $q\le Q$ odd inputs at positions
$0\le d_0<\cdots<d_{q-1}<t$, its endpoint 1 gives
\[
  2^t-k3^{P_r+q}-3^q x_r-\sum_{i=0}^{q-1}2^{d_i}3^{q-1-i}=0.       \tag{4}
\]
Only the first term is positive. Any proper nonempty subsum omitting that
term is negative; any proper subsum containing it is positive. The gcd
is 1 by $2^t$ and the odd term $k3^{P_r+q}$. The maximal absolute entry
$H=2^t$ is at least $k3^{P_r}$. The product of all parts outside the
prime set $\{2,3\}$ is at most $kx_r$.

Evertse's Corollary 1 on primitive nondegenerate integer zero sums gives,
for each $0<\epsilon<1$, a lower bound $c_{Q,\epsilon}H^{1-\epsilon}$
for that product. Use the fixed primes $\{2,3\}$ and the finitely many
dimensions corresponding to $3,\ldots,Q+3$ tuple entries. Use coefficient
1 in the finite-exception theorem, then absorb the finitely many positive
exceptional ratios into the constant. Combining with (3) gives
\[
 k^\epsilon\ge {c_{Q,\epsilon}\over\sqrt3\,n}3^{r/2-\epsilon P_r}
             \ge {c_{Q,\epsilon}\over\sqrt3\,n}3^{(1/2-\epsilon)r}.
\]
Choosing $\epsilon$ small enough in terms of $A$ proves (2). The bound
takes no limit in which $Q$ grows. The same inequality gives a uniform
finite-input consequence. Fix $Q,A$ and $0<\delta<1/2$. For all
sufficiently large $r$, there are no distinct lifts of this type with both
$n\le3^{(1/2-\delta)r}$ and $k\le3^{Ar}$. Taking
$0<\epsilon<\delta/(A+1)$ makes those upper bounds contradict the
display. The cutoff on $n$ matters when applying this across different
parents.
[Evertse, *On sums of S-units and linear recurrences*, Compositio Math.
53 (1984), Corollary 1, printed p. 227, (9)–(12)](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

In particular, a proposed small-exponent completion to a power of two
has a genuine equality alternative. For every fixed $n>0$ and $B>0$,
all sufficiently late congruences
\[
 2^t\equiv x_r\pmod {3^{P_r}},\qquad 0\le t\le Br
\]
are literal equalities. Indeed (3) puts $0<x_r<3^{P_r}$ at large $r$,
so $k=(2^t-x_r)/3^{P_r}$ is nonnegative. A positive $k$ would give the
distinct certified lift $n+2^r k$ reaching $2^t$ at clock $r$ with a
zero-odd tail, while $k\le 2^{Br}$ contradicts (2). If that lift had hit
1 before this clock it would violate $\tau(m)>r$, already proved.

After its first odd step the target endpoint is a ternary unit. The
primitive-root construction does give powers of two in its class, but
allows exponents of order $3^{P_r}$. The known parent's certificate has
not supplied linear-size exponents on arbitrarily late clocks of its
particular child. Such a construction would prove that the child itself
hits a power of two. Proving its existence is the unclosed part of this
attempt.

## Pins and replay

* PR182, 234fd2ece3a17c8950dce452291198705b4e6e60,
  research/high-variance-closure-20261124/ordinary-arithmetic/DYADIC_COMPANION.md and TRIADIC_SEPARATION.md.
* PR193, 67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e,
  research/astra-global-resolution-20261124/rewriting/SEVEN_RETURN.md and arithmetic/RESIDUAL_GHOST.md.
* Prior use of Evertse's Corollary 1 in a different geometry,
  301b84491ffafe283bd63d104c1b60ddf0e97f06,
  research/astra-closure-attack-20261124/CYCLE_EXTENSION.md, §1.

The [finite checker](check.py) tests first-hit heights, the decoder, dyadic
agreement, the two-clock bound, the terminal residuals and the primitive
zero-sum identity on actual lifted paths. Neither (2) nor universal
existence of a child certificate is a finite check.
