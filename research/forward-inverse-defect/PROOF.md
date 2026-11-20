# A rational inverse potential and its forward defect

**Status: PROPOSED, unconditional.** The claims below have elementary proofs.
They do not establish the pointwise bound in Section 6 and do not resolve
Collatz. Finite replay checks the stated arithmetic interfaces, not that
missing bound.

Use the shortcut map

$$T(n)=\begin{cases}n/2&n\ {\rm even},\\(3n+1)/2&n\ {\rm odd},\end{cases}$$

and the odd map

$$U(n)=\frac{3n+1}{2^{g(n)}},\qquad g(n)=v_2(3n+1).$$

The inverse state space is $X=\mathbb Z_3^\times$. An inverse letter $g\ge1$
is legal at $z$ when

$$I_g(z)=(2^g z-1)/3\in X.$$

An inverse word has length $k$, total exponent $A$, and score $8k-5A$.
Every intermediate state, including the last, must be a ternary unit.
Define

$$W(z)=\sup\bigl(\{0\}\cup
 \{8k-5A:\text{a legal inverse word from }z\}\bigr)
 \ \in\mathbb Z_{\ge0}\cup\{\infty\}. \tag{1}$$

The supremum is over all finite words. At a positive ordinary odd unit,
every such word is an actual positive ordinary inverse path. In particular,
the definitions do not replace an ordinary seed by a different lift.

The rational slope $8/5$ is strictly above $\log_2 3$, since $2^8>3^5$.
It is deliberately below the entropy threshold used in Paper 150.
None of the proofs here imports that paper's critical barrier, stationary
classification, or asymptotic probability estimates. The relationship to
that prior potential is recorded in the provenance note.

## 1. Finite observability and the Bellman inequality

Let $W_N$ restrict (1) to words of length at most $N$.
Only words with $A\le(8k-1)/5$ can improve the default value zero.
There are finitely many such words, and legality of a length-$k$ word,
including its unit endpoint, is determined modulo $3^{k+1}$.
Consequently $W_N$ is a nonnegative integer-valued locally constant
function, measurable modulo $3^{N+1}$.

Concatenation gives, in the extended order,

$$W(z)\ge 8-5g+W(I_gz) \qquad(g\text{ legal}). \tag{2}$$

In fact $W$ is the least nonnegative extended-valued function satisfying
all these inequalities: telescoping any such function along a word
dominates that word's score, and then dominates (1).
This is an inequality for **every** legal inverse action. It is distinct
from a minimum-cost certificate choosing one favorable action.

## 2. An elementary exponentially small Haar tail

Let $h$ be normalized Haar probability on $X$. Set $\lambda=6/5$ and

$$q_g=\frac{\lambda^{8-5g}}3.$$

Then

$$\sum_{g\ge1}q_g
 =\frac{6^8}{3\cdot5^3(6^5-5^5)}
 =\frac{1679616}{1744125}<1. \tag{3}$$

For every integer $B\ge1$,

$$h\{W\ge B\}\le(5/6)^B. \tag{4}$$

**Proof.** For a word $w=(g_1,\ldots,g_k)$, let $F_w$ undo its inverse
letters:

$$F_w(y)=f_{g_1}\circ\cdots\circ f_{g_k}(y),\qquad
 f_g(y)=\frac{3y+1}{2^g}.$$

Its full legal source domain is exactly $F_w(X)$.
Each $f_g$ maps $X$ into $X$, and $F_w$ has ternary scaling factor
$3^k$ times a unit. Additive Haar measure of $X$ is $2/3$; normalizing
therefore gives

$$h(F_w(X))=3^{-k}. \tag{5}$$

Take all positive-letter words whose score first reaches $B$ at the last
letter. This word family is prefix-free. Every source with $W\ge B$
admits one of these words. Give letters the subprobability weights $q_g$.
The prefix-free inequality says

$$\sum_{w\ {\rm first\ crossing}}\prod_{i=1}^{|w|}q_{g_i}\le1.$$

For example, adjoin a cemetery letter of weight $1-\sum q_g$ and apply
the disjoint-prefix probability bound; finite subfamilies followed by
monotone convergence cover the countable family.
For each crossing word,

$$3^{-|w|}
 =\lambda^{-(8|w|-5A_w)}\prod_i q_{g_i}
 \le\lambda^{-B}\prod_i q_{g_i}.$$

The union bound and (5) prove (4). No independence between arithmetic
source domains is assumed. $\square$

In particular

$$E=\{z:W(z)=\infty\}$$

has Haar measure zero. It is nevertheless a dense $G_\delta$ set.
Indeed $I_1(-1)=-1$, so $W(-1)=\infty$. Given any $z\in X$ and
precision $q$, choose a legal inverse word $w$ of length $q$; legal
letters always exist. If its last state is $z_q$, then

$$z-F_w(-1)=3^q2^{-A_w}(z_q+1).$$

Thus $F_w(-1)$ agrees with $z$ modulo $3^q$ and belongs to $E$, because
the word $w$ can be followed by arbitrarily many letters 1.
Finally $\{W\ge B\}$ is open as a union of finite-word legal domains,
and $E=\bigcap_{B\ge1}\{W\ge B\}$.

Every nonempty ternary cylinder therefore meets $E$.
No finite union of cylinders of Haar measure below one covers $E$.
The small Haar tail is not a pointwise exclusion of positive integers.

## 3. Exact propagation on one forward orbit

Suppose $n$ is a positive odd ternary unit, $g=g(n)$, and $n'=U(n)$.
Then $I_g(n')=n$ is a legal inverse edge, so

$$W(n')\ge W(n)+8-5g. \tag{6}$$

Put

$$R(n)=W(n)-5\log_2 n,\qquad
 \delta=8-5\log_2 3>0.$$

If a potential is infinite, read the following inequality in the extended
order, without subtracting two infinite quantities:

$$R(U(n))\ge R(n)+
 \delta-5\log_2\!\left(1+\frac1{3n}\right). \tag{7}$$

This follows by subtracting the exact logarithmic identity

$$\log_2 U(n)-\log_2 n
 =\log_2 3-g+\log_2\!\left(1+\frac1{3n}\right).$$

For every odd $n\ge33$, the increment in (7) is at least

$$\delta_{33}=8-5\log_2(100/33)>0, \tag{8}$$

as witnessed by the integer inequality $100^5<2^8\,33^5$.

If an ordinary orbit is not eventually periodic, its odd values $n_j$
tend to infinity: otherwise a finite set contains a repeated state.
Telescoping (7) then gives

$$R(n_k)\ge R(n_0)+k\delta
 -5\sum_{j<k}\log_2\!\left(1+\frac1{3n_j}\right). \tag{9}$$

The last sum is $o(k)$ by Cesaro averaging. If $W(n_0)$ is finite,

$$\liminf_{k\to\infty}\frac{R(n_k)}k\ge\delta. \tag{10}$$

If it is infinite, (6) makes every subsequent potential infinite.
These assertions retain the actual orbit and its actual inverse past.

## 4. The cycle consequence

Every positive integer at most 32 reaches 1, as the accompanying integer
replay verifies. Hence a different positive cycle would have every odd
value at least 33.

If $W$ were finite at one of that cycle's states, (6) around the cycle
would force it to be finite at every state. Summing (7) around the cycle
would then strictly increase $R$ while returning to the same state,
a contradiction. Equivalently, the reversed cycle has strictly positive
integer score and can be repeated arbitrarily many times.

Thus every state on a nontrivial ordinary positive cycle belongs to $E$.
Finiteness of $W$ on all positive odd ordinary units would exclude such
cycles, but by itself would not exclude escape.

This does not convert $h(E)=0$ into a cycle exclusion. Rational positive
cycles in the same local unit spaces can have $W=\infty$; the separate
rational-cycle construction makes that distinction explicit.

## 5. Critical-height cancellation and a sufficient bound

There is a useful refinement of the coefficient 5 in (9). Write

$$c_*=\frac3{\log_2(3/2)}>5,\qquad
 Z(n)=W(n)-c_*\log_2(n+1). \tag{11}$$

For an actual edge of exponent $g$, put

$$\eta(n,g)=\log_2\!\left(1+\frac{2^g-2}{3(n+1)}\right).$$

The exact identity

$$U(n)+1=\frac{3(n+1)}{2^g}
 \left(1+\frac{2^g-2}{3(n+1)}\right)$$

and (6) give

$$Z(U(n))\ge Z(n)
 +(c_*-5)(g-1)-c_*\eta(n,g). \tag{12}$$

For $g=1$, $\eta=0$ and the increment is nonnegative **exactly**.
For $g\ge2$, it has a positive lower bound, uniform in $g$, once $n$
is sufficiently large. Here is a proof retaining that uniformity.

Since $U(n)\ge1$, $2^g\le3n+1$, hence $0\le\eta(n,g)<1$.
Choose a fixed integer $G$ so large that

$$(c_*-5)(G-1)-c_*>0.$$

For all $g\ge G$ this is a uniform positive lower bound for (12).
For the finitely many $2\le g<G$, $\eta(n,g)\to0$ uniformly as
$n\to\infty$. Choose a floor $M$ making their increments at least
$(c_*-5)/2$. This proves the assertion with a fixed positive gain
$\varepsilon$ per exponent greater than one above $M$.

One fully explicit, deliberately coarse choice is

$$M=56\cdot2^{43},\qquad \varepsilon=1/16. \tag{12a}$$

The integer inequalities $3^{41}<2^{65}$ and $3^7>2^{11}$ imply
$41/8<c_*<21/4$. For $g\ge44$, using $\eta<1$ bounds the increment
strictly above $(43/8)-(21/4)=1/8$.
For $2\le g\le43$, use $\log_2(1+x)\le2x$ for $x\ge0$
(since $\ln2>1/2$). At $n\ge M$ this gives

$$c_*\eta(n,g)
 <\frac72\,\frac{2^{43}}{n+1}<\frac1{16},$$

while $(c_*-5)(g-1)>1/8$. Thus the increment exceeds $1/16$
also in this finite range. This is a uniform exact estimate, not a
floating-point scan over exponents.

An ordinary positive orbit cannot eventually have only exponent 1.
If it did, $n_{j+r}+1=3^r(n_j+1)/2^r$ for every $r$, forcing
$2^r\mid n_j+1$ for every $r$. Therefore an escaping orbit has
infinitely many exponents greater than one after it stays above $M$.
Equation (12) implies

$$Z(n_k)\longrightarrow\infty \tag{13}$$

on every escaping orbit whose potentials remain finite; the infinite
case again propagates automatically.

Consequently the following is a sufficient pointwise closing estimate:

> There is a real constant $C$ such that
> $W(n)\le c_*\log_2(n+1)+C$ for every positive odd ordinary
> ternary unit $n$.

This estimate would exclude escape by (13), exclude nontrivial cycles
by Section 4, and prove Collatz after the initial halvings and, if
necessary, one odd step from a multiple of three.
**The estimate is OPEN.** The Haar tail (4) supplies no such bound.
The coefficient in (11) is chosen to cancel exponent-one growth;
no optimality claim is made among all possible closing estimates.

## 6. Strength and limits of the proposed closing estimates

The stronger estimate

$$W(n)\le5\log_2 n+C \quad\hbox{for every positive odd ordinary unit} \tag{14}$$

would give an explicit logarithmic bound on the first visit below 33.
During $k$ steps staying above that floor, (8), $W(n_0)\ge0$, and (14)
imply

$$k\delta_{33}\le C+5\log_2 n_0. \tag{15}$$

Neither (14) nor the weaker estimate after (13) has been proved here.
They must not be relabeled as consequences of almost-everywhere
finiteness, positive predecessor density, inverse stationary laws, or
finite certificate searches.

The [closure-boundary note](CLOSURE_BOUNDARY.md) identifies their exact
logical strength: existence of either global bound is equivalent to
Collatz together with $W(1)<\infty$. The later
[log-log estimate](LOGLOG_GROWTH.md) allows a larger error term but has
the same existential global equivalence. The formulas are more or less
permissive pointwise; they are not distinct logically weaker conjectures.

Even $W(1)<\infty$ is a substantive uniform statement about all
terminating ancestors. If $U^k(m)=1$, with all intervening odd sources
units, then $8k-5A\le W(1)$. Together with the exact orbit identity this
constrains the number of odd steps relative to the source height and its
accumulated correction. Merely knowing that each such $m$ reaches 1
does not supply this uniform cost bound.

In the opposite direction, arbitrarily large certified finite-word
scores occur even at integers which reach 1 in one odd step. For $q\ge1$
put

$$a=3^{q+1}+1,\qquad n_q=(2^a-1)/3.$$

Here $a$ is even, so $n_q$ is a positive odd integer.
The elementary lifting identity
$v_3(2^{3^{q+1}}+1)=q+2$ gives $v_3(n_q+1)=q+1$.
Thus $q$ inverse letters 1 are legal with unit endpoints,
$W(n_q)\ge3q$, and $U(n_q)=1$.
The extra ternary digit is needed to certify the final unit.

This does not assert that the full value $W(n_q)$ is finite.
The control does not refute either height-normalized bound: its ordinary
heights can be very large. It does refute any claim that a large score
on a certified finite inverse word by itself diagnoses a nonterminating
forward orbit.

## 7. What is proved and what remains to prove

The explicit subprobability calculation, Haar bound, topological density,
forward inequalities, cycle implication, and conditional closing criteria
are proved above. The arithmetic replay is supplementary and bounded.

The remaining mathematical task is a **uniform bound at positive ordinary
integers** on the specified inverse potential, or another argument that
excludes the forward defect growth. No estimate on that exceptional
arithmetic domain is established by this packet.
