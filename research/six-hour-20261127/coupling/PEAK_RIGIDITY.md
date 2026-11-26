# All smaller ordinary visitors in a linear postpeak window

**PROPOSED written theorem.** Use the positive shortcut map $T(2v)=v$,
$T(2v+1)=3v+2$. Let $M_m=2^m-1$ and $P_m=3^m-1=T^mM_m$.
Write $Q_i(y)$ for the number of odd departures during its first $i$
shortcuts. The statement covers every positive integer $m$ and every
**supplied** positive $x<M_m$, with no convergence hypothesis.

Write $x+1=2^n b$, $b$ odd. Let $h,i\ge0$ be two independently
chosen native clocks, the former from $x$ and the latter from $P_m$.

* If $h<n$ and $3i<m$, the two endpoints differ.
* If $h=n+l$ and $2i+\max(i,l)<m$, then equality is possible
  **exactly** as follows. There is a $d\ge0$ with $b=3^d$.
  Set $t=n+d$. Then $t<m$, $l=i$, and
  $T^iP_m=T^iP_t$. At equality
  $Q_i(P_t)=m-t+Q_i(P_m)$.
  Conversely these conditions, even without the cone restriction, give
  the specified merger at the original lower clock $n+i$.
* Consequently, through $I=\lfloor(m-1)/3\rfloor$, every
  $T^iP_m$, $i\le I$, can be tested against **all** smaller starts at
  **all** clocks $h\le v_2(x+1)+I$ by testing just the same-clock
  earlier peaks $P_1,\ldots,P_{m-1}$. All corresponding starts
  are $x=2^{t-d}3^d-1<M_m$, $0\le d\le t$, with the
  original lower clock $t-d+i$. Their cumulative native odd count
  is exactly $m+Q_i(P_m)-d$. A successful comparison produces a
  smaller positive $M_t$ in the same component. The test can return no
  comparison.

## Proof

An even departure sends shifted height $v+1$ to $(v+2)/2$.
An odd departure multiplies it by $3/2$. Thus
$T^h x+1\le(3/2)^{Q_h(x)}(x+1)$, whereas
$T^iP_m+1\ge2^{-i}3^m$. At a meeting, $x+1<2^m$ implies

\[
                      Q_h(x)> m-2i.                           \tag{1}
\]

Indeed $(3/2)^{m-Q_h(x)}<2^i\le(3/2)^{2i}$, including $i=0$.

For any trajectory starting at $a-1$, its endpoint at clock $j$
with grade $p$ is $(3^p a+C_j)/2^j$. Here $C_0=-1$, an even
departure keeps $C_j$, and an odd departure changes it to
$3C_j+2^j$. Induction gives
$-3^j\le C_j<3^j-2^j$ for all $j$, with the strict inequality
already true at zero. In particular $|C_j|\le3^j$.
At the positive peak $P_m$ the first departure is even, so
$C_i$ is odd at every $i$. This last fact also follows at
$i=0$, and every later odd departure adds an even $2^j$.

For $h<n$ the lower endpoint is $2^{n-h}3^h b-1$, and
$Q_h(x)=h$. Equality implies
$3^h\mid C_i+2^i$, since $h<n<m$.
For $i>0$ this integer is odd, and
$-3^i<C_i+2^i<3^i$, contradicting (1) when $3i<m$.
For $i=0$, (1) already contradicts $h<m$. This handles the
entire lower ascent prior to its peak.

At $h=n+l$ the lower postpeak starts at $3^n b-1$.
Write $p=Q_i(P_m)$, $q=Q_l(3^n b-1)$ and use
$C'_l$ for its offset. With $J=\max(i,l)$, equality gives

\[
  2^{J-i}3^{m+p}-2^{J-l}b3^{n+q}
          =2^{J-l}C'_l-2^{J-i}C_i.                         \tag{2}
\]

By (1) and the cone, both $n+q>J$ and $m+p>J$. The right side
is divisible by $3^{J+1}$. Its absolute value is at most $2\cdot
3^J<3^{J+1}$, since $2^{J-j}3^j\le3^J$. Both sides therefore
vanish. The remaining equality has odd factors $3^{m+p}$ and
$b3^{n+q}$. Unique binary valuation gives $i=l$, and then
$b=3^d$ with $d=m+p-n-q\ge0$. Now $2^{n+d}\le2^n3^d<2^m$
implies $t=n+d<m$, and $3^n b-1=P_t$. Positivity excludes
$t=0$. The converse and all stated clock and grade identities follow
by replaying the $n=t-d$ odd departures from $x$ to this same
ordinary peak. Taking $d=0$ gives the cheaper $M_t$.

## What the reduction preserves

For the PR192 hard parent $z_m=(2^{m+7}-271)/81$,
$m=11+162j$, the supplied lower reaches $M_m$ at native clock 7
with 4 odd departures and then $P_m$ at $7+m$ with $4+m$.
Consequently the actual lower component is retained at any certified
meeting. If $t=11+162j'<m$, the corresponding smaller $z_t$
reaches the same endpoint at clock $7+t+i$ with the same cumulative
grade $4+t+Q_i(P_t)=4+m+Q_i(P_m)$.
The actual upper $3z_m$ reaches $2^{m-2}$ at clock 9 with three
odds, then $2^{t-2}$ after $m-t$ more even steps.
The smaller upper $3z_t$ reaches that latter point at clock 9 with
three odds. Thus every actual hit of 1 from $3z_m$ transfers with
$m-t$ fewer clocks and identical odd count. A general earlier $t$
need not lie on this canonical progression. No such canonical
conclusion is claimed in that case. If instead $2^{40}M_t<z_m$,
the existing quantitative-return theorem can be used under its
leastness hypotheses.

The first unsupported step in the pointwise closing attempt is existence
of **any** earlier $t$ at an affordable clock for the supplied $m$.
The present cone restricts the alternatives without ensuring such
existence, and unrestricted later clocks are outside its conclusion.

## Source boundaries

* PR197, `1f0f496fbea37792439feada6106eaaff596bcd1`,
  `research/ayh-resource-reset-20261124/unconventional/ALL_SOURCE_CLOCKS.md`,
  claims `full_margin`, `full_clock` and `prepeak_clock`. This supplies
  the all-source signed-carry and shifted-height methods. Its upper
  postpeak square is tied to the exceptional signed address and its
  exclusion conclusion differs from the all-exponent classification here.
* PR192, `ed7a6fe30b8602407f77855ceb74ce0489ce9c10`,
  `research/astra-unconventional-20261126/descent/POSTPEAK_DELAY.md`
  and `PAID_DELAY_REPAIRS.md`. These supply the independently clocked
  exceptional window and literal paid comparisons. Their offset
  cancellation for two specified pure peaks is prior work. This proof
  retains arbitrary smaller cofactor $b$ and both clocks until (2).
* PR195, `51d97cbe17054415acaf95e422801a3532545033`,
  `research/astra-unconventional-20261126/renormalization/FIRST_MEETING.md`.
  Its all-time lower bound optimizes the grade of a visitor arriving at a
  specified crest by the other edge. The present assertion classifies the
  short postpeak regime and includes every smaller positive visitor.
* PR200, `ad70a3b831867cb8a74d402a2a1abdc419f5a09b`,
  `research/unconventional-20261126/defects/PREFIX_SWAP_EXCLUSION.md`.
  Its protected adjacent-block swap exclusion requires a floor on the
  original entrance and differs from the forced equality of peak offsets.

## Infinitely many ordinary crests defeat the whole linear window

The finite augmented-class theorem in **PR195,
`51d97cbe17054415acaf95e422801a3532545033`,
`research/astra-global-closure-20261124/round13/trace/FINITE_FAMILY.md`,
“Every actual augmented class is finite”** combines with the classifier.
The prior text applies it to one hard progression. The argument below
uses the same proof for all $P_m$, $m\ge1$.

**Corollary.** Infinitely many actual exponents $m$ have the following
property. For **every** positive $x<M_m$ and every $i,h\ge0$ with
$i\le\lfloor(m-1)/3\rfloor$ and
$h\le v_2(x+1)+\lfloor(m-1)/3\rfloor$, one has
$T^iP_m\ne T^h x$. This gives a pointwise obstruction to universal
descent by these short visits. The exponents produced need not lie
on a prescribed hard progression. The conclusion is compatible with
convergence of every $M_m$.

Relate two positive exponents if their peaks meet at a common postpeak
clock with the initial exponent plus subsequent odd count equal.
Advancing the endpoint leaves the equalities intact, so this is an
equivalence relation. Put
\[
  D_h(x)=\frac{2^h(T^h x+1)}{3^{Q_h(x)}(x+1)}
  =\prod_{\substack{a<h\\T^a x\ {\rm even}}}
           \left(1+\frac1{T^a x+1}\right).
\]
Suppose a class reference $P_t$ never repeats. Every other member
$P_m$ meets it at a positive clock $h$ with $D_h(P_m)=D_h(P_t)$.
The reference starts even, so this product is at least $1+3^{-t}$.
The ordinary simple-path reciprocal tail tends uniformly to zero
as its floor increases. For clarity, the elementary argument is as
follows. In any simple segment, count positions at height $\le X$.
With $b=\lfloor\log_2 X\rfloor$ disregard its last $b$ positions.
Prefixes of $b$ bits having more than $3b/5$ odds occupy
$O(2^{bH_2(3/5)})$ residues modulo $2^b$. Each accounts for at most
two of the distinct integers $\le X$. The other $b$-step endpoints
have size at most $X3^{3b/5}/2^b+(3/2)^b$ by the usual carry bound.
Their distinctness gives at most $O(X^{(3/5)\log_2 3}+X^{\log_2(3/2)})$
such positions. All powers are strictly below one, and summing over
dyadic scales gives the uniform reciprocal tail. In particular some
even site in the prefix from each $P_m$ is below a fixed bound
depending only on $t$. Two class members passing through the same
such site must do so at the same clock. Indeed choose a common
clock of meeting beyond both visits. Different visit clocks would
produce a repetition on the common tail. A fixed gate at fixed
clock has finitely many possible positive starts (a preimage
is at most twice the target). This proves finiteness in this case.

If the reference is eventually periodic, fix a cycle phase $z$,
its least period $L$, and its grade $g$. There is an even site
on every positive cycle by strict growth of the all-odd shifted
map. Hence $2^L>3^g$ by the displayed product. Each class member
first visits $z$ at some clock $h$ with grade $q$. The integer
$L(m+q)-gh$ is the same across the class by continuing a
synchronized merger through a common visit to $z$ and removing full
cycle laps. The prefix to its first visit is simple. Thus
$\log D_h(P_m)$ is uniformly bounded by the same elementary
occupation estimate. The identity
\[
 L(m+q)-gh=(L-g\log_2 3)(m+q)
       +g\log_2(z+1)-g\log_2D_h(P_m)
\]
bounds $m$ across this class. Consequently there are infinitely
many finite classes, with infinitely many minima. No minimum has
an earlier matching exponent. The all-source classification proves the
corollary.

**Additional price at a successful meeting.** If $t=m-s<m$ meets
at common clock $i$ with compensated grades, let $p=Q_i(P_m)$.
Then $3^s\le2^{i-p}-1$. To see this, write the translated carry
as $B=2^i(T^i(P_m)+1)-3^{m+p}$. On odd letters it triples and on
even letters at index $j$ it increases by $2^j$. Hence
$B/3^p=\sum_{j\ {\rm even\ departure}}2^j/3^{Q_j(P_m)}$.
The $a$-th even letter, counted from $a=0$, occurs at
$j=a+Q_j$, so its term is at most $2^a$. This proves the upper
bound $B/3^p\le2^{i-p}-1$. The earlier peak has the same
translated carry; its first departure is even so $B\ge3^{p+s}$.
In particular the upper *even* budget, independently of its odd
budget, must grow with the exponent gain. The translated carry
arithmetic is also used in PR197's
`research/ayh-resource-reset-20261124/unconventional/FIRST_ATTACHMENT_CLOCK.md`
at the pin above.

## Evidence

[PeakRigidity.lean](PeakRigidity.lean) checks both independent-clock
directions of necessity on the ordinary `CoreBranching.run` from
PR201, `21bed7ac2b1b1bb4baf0f6cabd53f8b9dd11b58a`,
`research/unconventional-20261126/CoreBranching.lean`. The
[exhaustive replay](check_peak.py) uses literal map iteration
and full clock enumeration at $1\le m\le14$, including all smaller
positive starts. Its [integer results](PEAK_CONTROLS.json) include
the counterexample to unrestricted rigidity $m=3,x=4$:
$T^6(P_3)=4=x$ and $x+1=5$ is outside the claimed smooth form.
Neither this counterexample nor the finite-class argument refutes
unrestricted ordinary descent.
