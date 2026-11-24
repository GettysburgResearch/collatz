# A long ordinary merger on the reverse-closure section

We use the shortcut map $T(x)=x/2$ on even integers and $T(x)=(3x+1)/2$ on odd integers. Put $S(c)=-T(-c)$ for positive $c$. PR 174 at `c92cd473de3b85ceb945702a726d2eb7350a6af8` reduces Collatz to the implication “if $3n-1$ reaches 1, so does $n$” on $n=27j+1$ with $4\nmid j$. Its `research/psi-closure-20261121/routes/cover/NOTES.md`, sections 6 and 10, leaves the obstruction point $(-17,0)$ undecided. This packet addresses both issues. Universal closure remains open.

| Result | Scope and evidence |
|---|---|
| CS1 | An actual smaller partner for every certified instance in (1) below. Core Lean checks the clock and size implication, including the complete ten-step merger. |
| CS2 | Any prescribed radius occurs on this same family, with an actual certificate for the member arm. The construction and the obstruction for both $(-17,0)$ and $(-17,1)$ have written proofs. Lean checks the all-clock disjointness theorem and finite arithmetic tables used by the written proof. |
| CS3 | An explicit obstruction to promoting the four small-cycle partners to a uniform fixed-clock rule. Written proof. |

## A smaller positive partner beyond the protected clocks

For a positive integer $k\equiv148\pmod{256}$, choose ordinary $u>0,e\ge10$ satisfying

$$
       3^{22k-1}u=2^e+7,\qquad n=2^{33k}u-17.                    \tag{1}
$$

Then $3n-1$ reaches $2^e$ in $33k$ steps. More importantly,

$$
 m=2^{21k}u-1<n,\qquad T^{21k+10}(m)=T^{33k+10}(n).           \tag{2}
$$

The factor $2^{-12k}$ is the limiting ratio $m/n$ as $u$ grows for fixed $k$. This supplies a genuine strong-induction step on all these inputs. Formula (2) does not require a convergence hypothesis for its algebra or a uniform bound on the length of a witness from $m$.

For any positive $c,x$ with $x+c=2^r v$, parity lifting gives
$T^r(x)+S^r(c)=3^a v$, where $a$ counts odd inputs along those $r$ steps of $S$ from $c$. For a step, the two numerators have the same parity, and their sum doubles back to $x+c$ or $3(x+c)$. Induct on $r$. The signed cycle on $17$ has length eleven and seven odd inputs. The orbit from 52 starts with $52,26,13,19,28,14,7,10,5,7,\dots$. At $33k$ its endpoint is 7 and its odd count is $22k-2$ for $k\ge1$ because the count at time 33 is 20 and each later block of 33 adds 22. Apply lifting at $c=17,52,1$ respectively. The three endpoints are

$$
 X=3^{21k}u-17,\qquad 3^{22k-1}u-7=2^e,\qquad X+16=3^{21k}u-1.
$$

For $d=k-1$, the known endpoint gives $3^d(X+17)=2^e+7$. Since $3^{256}=1\bmod 1024$, $3^{147}=475\bmod1024$, and $475\cdot69=7\bmod1024$, we get $X\equiv52\bmod1024$. Write $X=1024v+52$. The two ten-step paths at $v=0$ are

```text
52 → 26 → 13 → 20 → 10 → 5 → 8 → 4 → 2 → 1 → 2
68 → 34 → 17 → 26 → 13 → 20 → 10 → 5 → 8 → 4 → 2
```

Each path has three odd steps, so their common endpoint is $27v+2$ on every lift. This proves (2). More generally the transfer applies whenever the member-arm endpoint $Y=T^{33k}(3n-1)$ is divisible by 1024. The same identity $3^{k-1}(X+17)=Y+7$ gives precisely the same residual ten steps. The higher bits of $Y$ and its eventual trajectory are unrestricted. The Lean declarations `member_endpoint` and `ten_even_bridge` give this version. The pure-power choice adds an explicit certificate that the member arm actually reaches 1.

## Inputs carrying the actual witness and any protected radius

For every $L\ge3$, take $k\equiv148\bmod256$ so large that $p=33k\ge L+8$. Put $b=22k-1$. To impose $n\equiv1\bmod3^L$, solve the single congruence

$$
  2^e\equiv18\cdot 3^b(2^p)^{-1}-7\pmod{3^{b+L}}.             \tag{3}
$$

Its right side is a unit. The order of 2 modulo $3^j$ is $2\cdot3^{j-1}$: $4-1$ has 3-adic valuation 1 and cubing $1+3^a t$, $3\nmid t$, raises the valuation of its difference from 1 by exactly one. Hence there are arbitrarily large $e$ satisfying (3). Equation (1) gives a positive integer $u$, and (3) makes $2^p u\equiv18\bmod3^L$. Thus $n\equiv1\bmod27$ and $n\equiv-17\equiv3\bmod4$, so the parameter $j=(n-1)/27\equiv2\bmod4$ is on the original open section.

The $T$-orbits of $-17$ and $-52$ lie in disjoint finite sets whose magnitudes are below 256. Consequently $n\equiv-17\bmod 2^{L+8}$ prevents the two positive arms from joining at any two clocks separately at most $L$. Indeed the corresponding endpoints are congruent, respectively, to their two distinct signed shadows modulo 256. The following argument proves the stronger conclusion that *every* ordinary walk of length at most $L$ from $n$ ends at a value at least $n$, even if it uses inverse steps and aims at an arbitrary smaller source. Equation (2) supplies a longer walk on the same inputs. In particular, choose ternary precision $L=p=33k$ in (3). The ordinary-walk lower bound below needs only $p$ binary digits, and still applies. If $D(n)$ denotes the least length of *any* ordinary walk to a smaller positive integer, then on these chosen lifts
$$
                  33k<D(n)\le54k+20 .
$$
For simultaneous direct-arm separation the guaranteed two separate clocks are then $p-8$. Taking $e$ between one and two multiplicative orders modulo $3^{55k-1}$ gives $\log_2\log_2 n=55k\log_2 3+O(1)$. This yields actual witness-bearing inputs on the open section with $D(n)$ of order $\log\log n$, and an explicit upper walk within a factor $18/11+o(1)$ of the lower bound.

## The obstruction at the two mixed-adic points

An ordinary walk uses the forward map, backward doubling, and $z\mapsto(2z-1)/3$ when $z\equiv2\bmod3$. At $(-17,z)$ with $z=0,1$, the forward parity uses the first coordinate and inverse-odd legality uses the second. Its affine map has the form $v\mapsto\alpha v+\beta$. We prove $\alpha\ge1$ and the real image $y$ of $z$ satisfies $y\ge z$. A reduced word has $p$ forward steps followed by $q$ backwards, after erasing immediately retraced edges. If it leaves the signed cycle by a backward edge, the reverse tree cannot re-enter it, since the forward map is a function.

The cycle of magnitudes from 17 is
$17,25,37,55,82,41,61,91,136,68,34,17$.
Write $a$ for its forward odd count. While the reverse odd count $i\le a$, the signed shadow is $-B$ for an integer $B>0$. Before the next inverse odd when $i<a$, the current multiplier is divisible by 3 in the 3-adic integers. Thus the second coordinate is congruent to $-B\bmod3$. A legal inverse odd has $B\equiv1\bmod3$ and sends $B$ to $(2B+1)/3$. All such $B$ lie in the $S$-basin of the cycle and are at least 17; all smaller positive magnitudes instead reach 1 or 5. With $p>0$, including a forward-only walk, the multiplier satisfies

$$
 \frac{17\alpha}{B}
 =\frac{\prod_{\rm forward\ odd}(1+1/(2c))}
        {\prod_{\rm inverse\ odd}(1+1/(2b))}.
$$

Here $c$ is the magnitude *after* a forward odd step and $b$ the magnitude *before* an inverse odd step. The forward $c$ list processes the periodic sequence $25,37,55,82,61,91,136$. Every inverse denominator $b$ before the level $i=a$ is distinct: an off-cycle repeat cannot occur in a tree, and a cycle argument can occur only on the single exit edge. Among cycle nodes, only the exit $34\to23$ can be an inverse odd, as the other inverse-odd cycle edges are immediate retracings.

The complete list of eligible off-cycle $b<137$, grouped by the last *forward* edge into the cycle, is

| Last edge | Eligible $b$ |
|---|---|
| $23\to34$ | $31,46,124$ |
| $122\to61$ | $49,73,109$ |
| $50\to25$ | $67,100$ |

The finite calculation iterates $S$ from 1 through 136 until hitting 1, 5 or the cycle, at most 27 steps. A single inverse branch uses only one row. Including the possible cycle argument 34, the sorted denominator arguments therefore dominate $31,34,46,124,137,137,\dots$ coordinatewise. Against the first one through four forward factors, direct rational cross multiplication gives a strictly larger forward product each time. From the fifth factor on, the inverse comparison argument is always 137 or more and the forward argument is at most 136. This bounds *every* prefix, even though a termwise comparison can fail early. If $i<a$, the extra forward factors improve the bound. For $p>0$ we conclude $17\alpha>B\ge17$, including cases with no reverse odds. The second shadow here is $y=(17+z)\alpha-B>z$.

A path continuing past $i=a$ first reaches a level with multiplier $2^m$, where $m=q_0-p\ge1$ by strictness, and integral positive second shadow $y'=(17+z)2^m-B$. Its $B$ lies off-cycle because a reduced reverse part has already left the cycle. Subsequent steps are an ordinary inverse orbit of the positive integer $y'$. The first shadow stays strictly negative with magnitude at least 1 because doubling and $B\mapsto(2B+1)/3$ preserve $B\ge1$ over the reals. If the final multiplier were below 1, its positive integral second shadow $y''$ would satisfy $1\le y''<17+z$, by the difference of the two shadows. For the actual positive prefix $T^t(y'')=y'$ with $o$ odd steps we would need $3^o\ge2^{m+t}$. The following finite supersets include equality.

| $z$ | All candidates $(m,B)$ with $B\ge17$ |
|---|---|
| 0 | $(1,17),(1,26)$ |
| 1 | $(1,19),(1,28)$ |

To check, enumerate $1\le y''<17+z$. By clock 23 all those starts are in $\{1,2\}$. Thereafter the coefficient is at most $2/y''\le1$ for $y''\ge2$ since every forward additive carry is nonnegative. At $y''=1$ it is at most $3/2$ at all clocks. Before clock 24 the coefficient is below 16, so only $1\le m<4$ enter the finite table. The values 26, 19 and 28 reach the 5-cycle under $S$, and 17 is on the original cycle, so no candidate lies on an eligible off-cycle branch. For $p=0,z=0$ only doublings are legal. For $p=0,z=1$ reverse paths have positive integral shadow with a forward orbit to 1, so their inverse multiplier is at least 1. This last inequality follows from $1\ge\mu y''$ for such a forward prefix with multiplier $\mu$. These cases finish both mixed-adic proofs, with $y\ge z$ also after a level.

For an ordinary source $n\equiv-17\bmod2^L, n\equiv z\bmod3^L, n\ge z$, any walk of length at most $L$ has those same forward parities and legal inverse branches at the two-coordinate shadow. Each forward parity costs at most one binary digit. In the second coordinate forwards preserve given ternary precision and each inverse odd costs at most one ternary digit. Its ordinary endpoint equals $y+\alpha(n-z)\ge n$. This is the precise finite ordinary implication of the mixed-adic statement.

## The first remaining construction problem

At $p=33k$, the positive source $X$ in (1) shadows the rational $7/3^{k-1}-17$ on every subsequent binary clock up to $e$. Each odd step removes exactly one factor of 3 from its reduced denominator until that denominator is 1. A zero numerator cannot occur at positive denominator exponent in reduced form, so an even run before the next odd is always finite. This gives a terminating computation of an integer shadow for each $k$; its sign, size and odd-step density are uncontrolled. The rank $k-1$ decreases on actual odd steps, but by itself gives no bound repaying the original expansion $(2187/2048)^{3k}$.

A second explicit progression is $k\equiv48\bmod64$ and $e\ge8$. Then $X\equiv68\bmod256$, and the two residues 68 and 75 both reach 8 at clock eight with three odd steps. The negative 5-cycle returns from 10 to 10 in three steps with two odd inputs. Thus $m=2^{63k/2}u-10$ is a smaller positive source reaching $X+7$ in $63k/2$ steps and the same endpoint as $n$ eight steps later. Its limiting size ratio is $2^{-3k/2}$. This calculation is a written corollary with exact finite replay.

One extension tests partners reaching $X+17-b$ with $b=1,5,7,10$. The fixed point 1 uses $21k$ odd steps; on the 5-cycle run backwards from the desired phase until $21k$ forward odds have been accumulated, using at most $\lceil63k/2\rceil+2$ steps. Lifting that negative prefix gives a strictly smaller positive partner for sufficiently large $k,u$. The exact finite replay finds at least one equal-count merger by depth 16 on 3,736 of the 16,384 exponent residues $k-1\bmod 2^{14}$.

No fixed depth of that four-partner test covers the remaining classes. For arbitrarily large $k\equiv1\bmod 2^{H+8}$ and $e\ge H+8$, the base $X$ shadows the signed integer $-10$ in the first $H$ steps. The four trial starts then shadow $6,2,0,-3$, respectively. The orbit from $-10$ lies on the negative 5-cycle; the other four orbits are disjoint from it. These bounded orbits separate modulo 256 after extending the initial congruence by eight bits. This refutes a uniform fixed clock for this particular menu, even on certified-member inputs. There is an exact escape clock for *this one obstruction*. For $d=k-1>0$ even and $e>2+v_2(d)$,
$$
 v_2(X+10)=v_2(2^e-7(3^d-1))=2+v_2(d).
$$
Indeed $v_2(3^{2w}-1)=3$ for $w$ odd and each further squaring adds one. The two affine numerators lose exactly one binary digit at each matched shortcut step because the odd multiplier 3 is a binary unit. Thus the first differing parity between $X$ and the signed orbit from $-10$ occurs at precisely clock $2+v_2(d)$. Every fixed such ordinary exponent eventually leaves this repeated negative pattern. Its exit has no established saving uniform in the new signed shadow.

Finding a smaller partner for *each prescribed ordinary input*, including general member witnesses whose endpoint at the selected clock is not a power of two, is open.

[PR 174 source](https://github.com/GettysburgResearch/collatz/blob/c92cd473de3b85ceb945702a726d2eb7350a6af8/research/psi-closure-20261121/routes/cover/NOTES.md) · [PR 146's general chosen-subcylinder merger machinery](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/PREFIX_COMPRESSION.md). The present exponent condition follows from the *given* pure-power witness, without choosing more digits of the given source. Statements above the finite Lean controls are written mathematical proofs, not a Lean formalization of the entire mixed-adic argument.
