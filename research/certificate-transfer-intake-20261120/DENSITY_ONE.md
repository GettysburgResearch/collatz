# A density-one certificate transfer, reconstructed from the submitted PDF

**Status: PROPOSED, with a complete written reconstruction. Collatz remains
unresolved.** This note reconstructs the density-one theorem in the submitted
18-page manuscript, *Collatz certificates under x -> (x+1)/2: a density-one
theorem and the open remainder*, dated 2026-11-20. The source PDF has SHA-256
`edd35e567658c48803b43e78011c81644f153fcd73112de42f991b6d4dbaf99e`.
The source's pages 2--9 contain the certificate and stochastic arguments.
Here stopping arguments are localized explicitly, the additive constant is
bounded by an exact rational expression, and the ordinary-integer conclusion
is kept separate from the probability-one statement.

This is a reconstruction of submitted work, not a claim to have discovered
the canonical pair process or its absorption theorem. The stronger
quantitative absorption theorem in
[PR146, `THREE_RAY_UPPER.md`](https://github.com/GettysburgResearch/collatz/blob/e238c63a5d57f96bb063b7472498d1977df51951/research/upper-bit-mergers/THREE_RAY_UPPER.md)
at full head `e238c63a5d57f96bb063b7472498d1977df51951` already applies to
this process, after orienting the arms. That source credits Leen and Duran.
The proof below does not use its absorption theorem as a premise. No external
referee acceptance or formal proof-assistant verification is asserted.

## 1. Maps, certificates, and the exact target

On positive integers use the shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

On positive odd integers use
\(S(n)=(3n+1)/2^{v_2(3n+1)}\). A certificate of a positive integer
\(x\) is a strictly increasing integer tuple
\(0=A_0<A_1<\cdots<A_r\), allowing \(r=0\), such that

\[
3^r x+\sum_{j=0}^{r-1}3^{r-1-j}2^{A_j}=2^{A_r}.          \tag{1}
\]

Write \(E\) for the set of integers having such a certificate, and

\[
\mathcal C=\{x=1+128m:m\ge1,\ 4\nmid m\},\qquad
y=(x+1)/2=1+64m.                                         \tag{2}
\]

The unrestricted transfer question is
\(x\in\mathcal C\cap E\Rightarrow y\in E\).
The theorem here establishes it on an explicitly defined subset of relative
natural density one in \(\mathcal C\). It does not establish the unrestricted
question.

### CTD-001. What a certificate means

A positive integer has a certificate if and only if it is odd and its
\(S\)-orbit reaches 1. Every certificate is that orbit's valuation record,
possibly extended by repetitions of \(S(1)=1\), each having valuation 2.
In particular, \(E\) is the **odd** part of the basin of 1, not the whole
positive basin.

To prove the nontrivial direction, set \(a_k=A_k-A_{k-1}\) and define

\[
x_k=\frac{3^k x+\sum_{j<k}3^{k-1-j}2^{A_j}}{2^{A_k}}.
\]

Then \(x_0=x\), \(x_r=1\), and
\(x_k=(3x_{k-1}+1)/2^{a_k}\). Assuming \(x_{k-1}\) is integral,
the terminal equation becomes

\[
2^{A_r-A_{k-1}}
=3^{r-k}(3x_{k-1}+1)
 +\sum_{j=k}^{r-1}3^{r-1-j}2^{A_j-A_{k-1}}.
\]

The left side and the displayed sum are divisible by \(2^{a_k}\).
Since the coefficient \(3^{r-k}\) is odd, \(x_k\) is a positive integer.
Induction proves integrality at every stage. For \(k<r\), the next positive
exponent forces \(3x_k+1\) even, so \(x_k\) is odd; \(x_r=1\) is odd as
well. Hence each \(a_k\) is the full valuation, and these are exactly the
\(S\)-iterates. When \(r=0\), (1) says \(x=1\), so the endpoint case also
has the claimed oddness. The converse follows by unrolling the odd map.
Its deterministic orbit and the valuation-2 loop at 1 prove the final
assertion about all certificates.

## 2. Coalescent cylinders and their certificate rule

Direct shortcut computations, valid for every integer \(m\), give

\[
T^7(1+128m)=2+81m,\qquad T^6(1+64m)=1+27m.              \tag{3}
\]

After writing \(m=m_0+2^n t\), \(0\le m_0<2^n\), the two continued
iterates have forms

\[
X_n(t)=T^{n+7}(x)=\alpha+3^p t,\qquad
Y_n(t)=T^{n+6}(y)=\gamma+3^q t.                         \tag{4}
\]

For the next binary digit write \(t=b+2t'\). Both slopes are odd, so the
parities of \(\alpha+3^p b\) and \(\gamma+3^q b\) are fixed. Applying
one shortcut step gives new integer constants, and multiplies a slope by
3 exactly when the corresponding input is odd. Thus (4) holds inductively
as an identity on the full cylinder, and \(p,q\) count all odd inputs on
the respective arms, including the initial steps in (3).

Call the cylinder \(m_0\pmod{2^n}\) **coalescent** when
\(\alpha=\gamma\) and \(p=q\). Let \(G\subset\mathcal C\) consist
of the ordinary positive inputs belonging to at least one such cylinder.

### CTD-002. Certificate transfer on a coalescent cylinder

Suppose the cylinder is coalescent at depth \(n\) and put \(i=p=q\).
For each of its ordinary positive members,

\[
T^{n+7}(x)=T^{n+6}(y)=N,
\]

so \(x\in E\) if and only if \(y\in E\). Both arms have taken exactly
\(i\) odd steps before reaching \(N\). Removing its remaining
\(v_2(N)\) powers of two reaches the common \(i\)-th odd iterate.
The cumulative valuation records therefore satisfy

\[
A_i=n+7+v_2(N),\qquad B_i=n+6+v_2(N)=A_i-1.            \tag{5}
\]

All later valuation increments agree. Given a certificate
\((A_0,\ldots,A_r)\) for \(x\), extend its loops at 1 if necessary so
that \(r\ge i\). A certificate for \(y\) is then

\[
(B_0,\ldots,B_{i-1},A_i-1,\ldots,A_r-1).               \tag{6}
\]

The initial entries \(B_0,\ldots,B_{i-1}\) are fixed by the finite
parity data of the cylinder. The entry at \(i\) may depend on further
digits through \(v_2(N)\); formula (5) retains that dependence rather
than treating it as fixed.

For example, \(m=6+16j\) gives \(x=769+2048j\) and

\[
T^{11}(x)=T^{10}(y)=92+243j,\qquad i=5.
\]

Here (6) reads
\((0,2,4,6,7,A_5-1,\ldots,A_r-1)\).

## 3. The signed type chain

For (4), put \(a=q-p\). If \(a\ge0\), write
\(Y=3^aX+c\); if \(a<0\), write \(X=3^{-a}Y+c\).
The pair \((a,c)\) is the type. Coalescence is exactly type \((0,0)\).
The initial type in (3) is \((-1,-1)\). After the first two digits of
\(m\), the three allowed classes have the following types:

| \(m\pmod4\) | \(x\pmod{512}\) | Type |
|---:|---:|---:|
| 1 | 129 | \((-3,-1)\) |
| 2 | 257 | \((1,2)\) |
| 3 | 385 | \((-1,-2)\) |

Choose \(m\) according to Haar measure on \(\mathbb Z_2\), equivalently
choose its binary digits independently and fairly. Conditional on any
finite history, the unused tail is again Haar-uniform. An affine form
with odd slope is therefore Haar-uniform, and its next parity is a fair
bit. This also holds when the driving arm is chosen using the known type.
It does not say that a fixed ordinary integer has a random future.

For \(a\ge1\), the transitions are

| Condition | Parities | Next type |
|---|---|---|
| \(c\) even | both even | \((a,c/2)\) |
| \(c\) even | both odd | \((a,(3c+1-3^a)/2)\) |
| \(c\) odd | \(X\) odd, \(Y\) even | \((a-1,(c-3^{a-1})/2)\) |
| \(c\) odd | \(X\) even, \(Y\) odd | \((a+1,(3c+1)/2)\) |

At \(a=0\), even offsets give \((0,c/2)\) or \((0,3c/2)\), and odd
offsets give \((1,(3c+1)/2)\) or \((-1,(1-3c)/2)\). The two possible
transitions have probability \(1/2\). For negative \(a\), exchange
the arms and use the positive-level rules; at a return from \(a=-1\)
to zero, negate the offset to restore \(Y=X+c\). These are direct
identities of the two shortcut branches. Declare \((0,0)\) absorbing.

Call a step with even \(c\) a **hold**, and a step with odd \(c\) a
**move**. Holds preserve \(a\); moves change it by one.

### CTD-003. Holds and the embedded walk

Use the convention \(v_2(0)=+\infty\) when a zero offset occurs at a
nonzero level.

At a nonzero level of height \(h=|a|\), put

\[
\nu(h)=v_2(3^h-1)
=\begin{cases}1,&h\text{ odd},\\2+v_2(h),&h\text{ even}.
\end{cases}                                               \tag{7}
\]

If \(\omega\) is the number of holds before the next move, then

\[
\mathbb P(\omega\ge\nu(h)+k\mid\text{entry state})\le2^{-k},
\qquad \mathbb E(\omega\mid\text{entry state})\le\nu(h)+1.
                                                               \tag{8}
\]

Indeed, two 2-adic inputs have the same first \(k\) shortcut parities
exactly when their difference is divisible by \(2^k\). While their
parities agree, each step multiplies their difference by an odd factor
and divides it by 2. Thus the first differing parity occurs after
\(v_2(Y-X)\) holds. For an oriented pair this is
\(v_2((3^h-1)X+c)\). If \(v_2(c)<\nu(h)\), it equals \(v_2(c)\).
Otherwise, subtracting \(\nu(h)\) leaves the valuation of a Haar-uniform
2-adic integer, whose tail is \(2^{-k}\). The zero difference has
probability zero in the latter case. Formula (7) follows by factoring
\(3^{2m}-1\) and successive squaring. At level zero with nonzero gap
\(c\), the number of holds is exactly \(v_2(|c|)\).

At every move the direction is chosen by a fresh fair bit, including
after a random finite sequence of holds: the next move time is determined
by the past before that bit is exposed. The embedded coordinate \(a\)
is therefore a simple symmetric walk, stopped if absorption occurs.
Starting away from zero it hits zero almost surely. An excursion that
departs from zero returns there almost surely, and the expected number
of visits to each height \(h\ge1\) is 2. To see the last statement on
the signed walk, the probability of reaching \(+h\) before returning
to zero is \(1/(2h)\); from \(+h\), the probability of hitting zero
before revisiting \(+h\) is also \(1/(2h)\). The expected number of
visits to \(+h\) is consequently 1, and the negative side contributes
another 1. The finite holds in (8) do not change this embedded walk.

## 4. A complete excursion contracts the square-root gap

Start from \((0,\delta)\), \(\delta\ne0\). Let \(j_0=v_2(|\delta|)\)
be the number of initial holds. The departure occurs at step \(j_0\).
Let \(\theta>j_0\) be the first subsequent physical time at level zero,
and let \(\delta'\) be its offset. These times are finite almost surely.

### CTD-004. Excursion estimate

Put

\[
\lambda=\frac{3-\sqrt3}{2}<1.
\]

There is an absolute constant \(C<54\) such that, for every nonzero
integer gap,

\[
\mathbb E\sqrt{|\delta'|}\le\lambda\sqrt{|\delta|}+C.     \tag{9}
\]

**Size recursion.** At state \((a,c)\), put \(w=|c|/3^{|a|}\).
The transition table gives

\[
w_{i+1}\le A_iw_i+\tfrac12,                              \tag{10}
\]

where \(A_i=1/2\) for a both-even hold or a move away from zero, and
\(A_i=3/2\) for a both-odd hold or a move toward zero. At a departure
both branches have factor \(1/2\). During the initial level-zero holds
the additive term is zero. Unroll (10) and use subadditivity of the square
root. With \(\Pi_j=\prod_{j\le i<\theta}A_i\), this gives

\[
\sqrt{|\delta'|}
\le\sqrt{\Pi_0}\sqrt{|\delta|}
 +2^{-1/2}\sum_{j=j_0}^{\theta-1}\sqrt{\Pi_{j+1}}.        \tag{11}
\]

**The product term, with localization.** Set

\[
z=\frac{\sqrt3}{2},\qquad g=\sqrt3-1,
\qquad\frac{gz+g^{-1}}2=1,
\qquad gz=\lambda.
\]

Let \(u_i\) count the moves away from zero before time \(i\), including
the departure, and define, up to \(\theta\),

\[
\Psi_i=g^{|a_i|}z^{u_i}
 \prod_{\substack{\ell<i\\\ell\text{ a hold}}}\sqrt{A_\ell}.
                                                               \tag{12}
\]

A hold has mean multiplier
\(\mu=(2^{-1/2}+\sqrt{3/2})/2<1\).
At positive height a move has multiplier \(gz\) or \(g^{-1}\), each
with probability \(1/2\), so its conditional mean multiplier is 1.
At departure the multiplier is \(gz=\lambda\).
Thus (12), stopped at \(\theta\), is a nonnegative supermartingale.
For every deterministic finite time its variables are integrable, for
example from the bound \(\Psi_i\le(3/2)^{i/2}\).

The initial holding length \(j_0\) is deterministic for the fixed gap.
Hence \(\mathbb E\Psi_{j_0+1}\le\lambda\). Apply the ordinary bounded
stopping theorem after this time to \(\theta\wedge M\), for
\(M\ge j_0+1\), and then Fatou as \(M\to\infty\). This yields
\(\mathbb E\Psi_\theta\le\lambda\), without assuming a finite mean
for \(\theta\). On a completed excursion the number of away moves
equals the number of toward moves, so
\(\Psi_\theta=\sqrt{\Pi_0}\). Therefore

\[
\mathbb E\sqrt{\Pi_0}\le\lambda.                        \tag{13}
\]

**The additive term.** Conditional on the history at time \(j+1\), with
height \(h=|a_{j+1}|>0\) and \(j<\theta\), the remaining moves have
some number \(u'\) away and \(u'+h\) toward. Restart (12) with initial
value \(g^h\). The same bounded stopping and Fatou argument, now
conditional on that history, gives

\[
\mathbb E\bigl[\sqrt{\Pi_{j+1}}\mid\mathcal F_{j+1}\bigr]
\le(\sqrt{3/2}\,g)^h=\kappa^h,
\qquad\kappa=\sqrt{3/2}(\sqrt3-1)<1.                    \tag{14}
\]

For \(j+1=\theta\), the suffix is empty and the same formula holds
with \(h=0\). All summands are nonnegative, so conditional expectation
and Tonelli can be used in (11) even before integrability of the full
random sum is known.

Each embedded visit to height \(h\) contributes \(1+\omega\) physical
positions, with conditional expected length at most \(2+\nu(h)\).
To charge this rigorously, sum over the successive entry times to that
height and use (8) conditional on each entry; independence of visit count
and holding lengths is not required. Since the expected number of visits
is 2, the expected cost of all those positions is at most
\(2\kappa^h(2+\nu(h))\). The final zero-level position contributes 1.
Thus one can take

\[
C=2^{-1/2}\left(1+2\sum_{h\ge1}\kappa^h(2+\nu(h))\right).
                                                               \tag{15}
\]

The series converges because \(\nu(h)\le2+\log_2 h\). Combining
(11), (13), and (15) proves (9).

**An exact upper bound for the constant.** For completeness, no Monte Carlo
or decimal approximation is needed for \(C<54\). Set \(r=897/1000\).
The rational inequalities \((433/250)^2<3\) and
\((708/1000)^2>1/2\) give \(\kappa<r\) and
\(2^{-1/2}<708/1000\). The valuation formula gives exactly

\[
\sum_{h\ge1}r^h(2+\nu(h))
=\frac{3r}{1-r}+\frac{r^2}{1-r^2}
 +\sum_{j\ge1}\frac{r^{2^j}}{1-r^{2^j}}.
\]

For \(j\ge6\), use \(2^j\ge64(j-5)\) and
\(1-r^{2^j}\ge1-r^{64}\). Consequently

\[
C<\frac{708}{1000}\left[1+2\left(
 \frac{3r}{1-r}+\frac{r^2}{1-r^2}
 +\sum_{j=1}^{5}\frac{r^{2^j}}{1-r^{2^j}}
 +\frac{r^{64}}{(1-r^{64})^2}
\right)\right]<54.                                      \tag{16}
\]

The last inequality is an exact inequality between displayed rational
numbers. Its value is below 53.335; that decimal is only a display aid.

## 5. Reachability and almost-sure absorption

### CTD-005. An absorbing word from every zero-level gap

From \((0,\delta)\), \(\delta\ne0\), an explicit finite sequence of
allowed transitions reaches \((0,0)\). For even \(\delta\), choose
the both-even transition, halving the gap. For odd \(|\delta|>1\),
two moves give

\[
D(\delta)=\begin{cases}
(3\delta-1)/4,&\delta\equiv3\pmod4,\\
(3\delta+1)/4,&\delta\equiv1\pmod4.
\end{cases}                                               \tag{17}
\]

In the first case use
\((0,\delta)\to(1,(3\delta+1)/2)\to(0,(3\delta-1)/4)\).
In the second use
\((0,\delta)\to(-1,(1-3\delta)/2)\to(0,(3\delta+1)/4)\).
The intermediate offsets are odd, and the signed return convention
gives exactly the displayed signs. Both resulting gaps have smaller
absolute value. From gap 1 use
\((0,1)\to(1,2)\to(1,1)\to(0,0)\); from -1 exchange the arms.
Strict decrease terminates this word construction. Each finite specified
word has positive fair-bit probability.

### CTD-006. Absorption from every finite type

From a nonzero level, the embedded symmetric walk first reaches zero
almost surely, with finite holds almost surely. It is enough to start
from a gap \(\delta\) at zero. Define the successive gap chain by one
**complete departure-and-return excursion**, including its initial
level-zero holds, at every turn. This is not the chain of every physical
time spent holding at zero. Retain zero as an absorbing gap. Strong
Markov gives a Markov chain \((\delta_k)\), and (9) applies at each turn.

Put \(V(\delta)=\sqrt{|\delta|}\),
\(R=(C+1)/(1-\lambda)\), and
\(F=\{\delta\ne0:V(\delta)\le R\}\), a finite set.
Outside \(F\cup\{0\}\), (9) gives conditional drift at most -1.
If \(\sigma\) is the first entry time into this set, then

\[
V(\delta_{k\wedge\sigma})+(k\wedge\sigma)
\]

is a nonnegative supermartingale. Bounded stopping and monotone
convergence of \(k\wedge\sigma\) give
\(\mathbb E\sigma\le V(\delta_0)\) when starting outside the set.
In particular this entry occurs almost surely. From any later finite
state of the type chain, first return to zero and apply the same fact.

For each \(\delta\in F\), choose the absorbing word in CTD-005, and
let \(L\) be the maximum of their finite lengths. At a visit to \(F\),
attempt the chosen word; conditional on the past its success probability
is at least \(2^{-L}\). If it fails without absorption, its resulting
type is finite, and another visit to \(F\) or absorption occurs almost
surely by the preceding paragraph. Repeat at these successive trial
times. Fresh future bits give

\[
\mathbb P(\text{failure in the first }k\text{ trials})
\le(1-2^{-L})^k.
\]

Letting \(k\to\infty\) proves absorption almost surely. This proof
does not require a finite expected physical excursion length and does
not use optional stopping at an unbounded time without localization.

## 6. The ordinary density theorem and its exact boundary

### CTD-007. Density-one transfer

The set \(G\) in Section 2 has relative natural density one in
\(\mathcal C\). For every \(x\in G\), membership in \(E\) transfers
in both directions between \(x\) and \((x+1)/2\), with certificate
transformation (6).

For \(n\ge2\), let \(\rho_n\) be the proportion of residue classes
\(m_0\pmod{2^n}\) with \(4\nmid m_0\) that have coalesced by depth
\(n\). It is exactly the finite-depth absorption probability under
Haar measure conditioned on \(4\nmid m\). CTD-006 applies to each
of the three initial types, so \(\rho_n\to1\).

For a fixed \(n\), these coalescent cylinders form a finite union of
ordinary positive residue classes. Their relative natural density in
\(\mathcal C\) is exactly \(\rho_n\), and their union is a subset
of \(G\). Therefore the lower relative density of \(G\) is at least
\(\rho_n\) for every \(n\), hence is 1. Its upper density cannot
exceed 1. This proves the natural-density conclusion; it does not
identify a probability-zero set with an empty set of ordinary integers.

The exceptional set \(\mathcal C\setminus G\) is nonempty. For
example both 129 and 65 converge, with shortest certificate lengths and
terminal exponents

\[
(r,A_r)=(44,77)\quad\text{and}\quad(8,19),
\]

respectively. The grade \(\iota(n)=A_r-2r\) is independent of added
valuation-2 loops. A coalescent cylinder would force
\(\iota(129)=\iota(65)+1\) by (5)--(6), whereas the actual grades
are -11 and 3. Thus 129 is exceptional for this certificate method even
though its partner reaches 1. The actual two orbits do meet; failure of
a whole-cylinder affine identity must not be called unrelated orbits.

The proof supplies no transfer theorem covering every exceptional positive
input. The original statement remains open on that residual **uniform
problem**, rather than being unknown at each individual exceptional input.
The density-one theorem does not exclude a positive divergent orbit or a
nontrivial positive cycle. It is not a full proof of Collatz.

## 7. Comparison and evidence boundary

The PDF's certificate record and exponent-shift formulation are useful
explicit interfaces to the pair process. Its density-one theorem is a
specialization of the more general absorption result already written in
the pinned PR146 source. That source additionally proves an
\(h^{-1/2}\) physical-clock tail; the qualitative reconstruction here
does not establish an asymptotic tail constant or matching asymptotic.

The PDF's finite arithmetic checks and censored Monte Carlo samples are
supporting experiments. They are not the proofs of (9), CTD-006, or the
all-depth density limit. The present argument separately supplies those
proofs. The exact rational evaluation in (16) is a finite scalar check;
the stochastic conclusions depend on the preceding mathematical argument.
Formalization, human review, and universal positive-integer closure are not
claimed by this note.
