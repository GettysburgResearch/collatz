# Every arithmetic progression carries every multiplication-by-five comparison

**PROPOSED.** Let $T$ be the shortcut Collatz map and $C$ the positive integers that reach 1. Fix any positive odd $q$ coprime to three, any modulus $m\ge1$, and **any** residue $a$ modulo $m$. There are infinitely many positive $x\equiv a\pmod m$ and clocks $J$ such that
$$
                         T^J(x)=q,\qquad T^J(5x)=5q.                 \tag{1}
$$
One can also prescribe a finite list of shifts $c_i$, including zero, so that *all* $x+c_i$ reach $q$ at that same clock, and *all* $5(x+c_i)$ reach $5q$ there. The clock and source may depend on the fixed inputs. For each $m,a$ and list, one may choose $x\le Kq$ with a constant independent of $q$.

Consequently Collatz is equivalent to the implication $x\in C\Rightarrow5x\in C$ holding throughout **any one** arithmetic progression, even with finitely many exceptions. If Collatz fails, for every $k$ there are arbitrarily large starting indices for which all $x,x+1,\ldots,x+k-1$ reach 1 and none of $5x,5(x+1),\ldots,5(x+k-1)$ reaches 1. The first index can lie in any specified progression. There are also arbitrarily long blocks where both lists reach 1. Thus bounded gaps between indices satisfying the five implication would suffice. This statement uses every positive integer as an index. To use only odd ternary units, prescribe $x=1\pmod6$ and shifts $0,6,\ldots,6(k-1)$.

The global input is GCM-002, which proves that five-closure on all odd ternary units implies Collatz. PR 166's ladder gives two short return words below. The earlier localization allowed one nested sequence of binary classes. The argument here solves the parity control problem after **every prescribed prefix**. It adapts the equal-slope ordinary merger method to a return with endpoint ratio five. [Global criterion, PR 157](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/merger.md) · [Ladder FL1, PR 166](https://github.com/GettysburgResearch/collatz/blob/5996b9f525ca50978bc34f423192c36a87765bf3/research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md) · [Earlier localization](FIVE_STEP_SEEDS_AND_MULTIPLIERS.md) · [Equal-slope construction](PREFIX_COMPRESSION.md)

## 1. Returning to ratio five after any binary prefix

Start $X=x$, $Y=5x$ and advance both ordinary trajectories at a common clock. After a binary prefix of $h$ bits each arm is an integer affine function of the free parameter with odd slope. Put $s=p_Y-p_X$, the difference in odd counts, and $s_+=\max(s,0)$, $s_-=\max(-s,0)$. The slopes cancel in
$$
                        3^{s_-}Y=5\cdot3^{s_+}X+D,
$$
so $D$ is a fixed integer on the whole cell. Each next parity $i$ of $X$ is freely chosen by fixing one more parameter bit. The other parity is $j=(i+D)\bmod2$. For $t=s+j-i$ the new state is
$$
       s'=t,\qquad 2D'=3^{t_-+j-s_-}D+3^{t_-}j-5\cdot3^{t_+}i.       \tag{2}
$$
The exponent is nonnegative. This follows by substituting $2X'=3^iX+i$ and $2Y'=3^jY+j$. State $(0,0)$ gives the required return throughout the whole refined class.

**Remove a nonzero level.** With even $D$ the choices of two even or two odd inputs give $D/2$ and $(3D+c_s)/2$, respectively, with $c_s=3^{s_-}-5\cdot3^{s_+}$. Its binary valuation is one for odd $|s|$ and two for even $|s|>0$, by reduction modulo eight. If $D$ has valuation at most $v_2(c_s)$, halve until it is odd. For $D=0$ or higher valuation, take the odd choice once and then halve $v_2(c_s)-1$ times. With $D$ odd, choose $i=1$ at $s>0$ and $i=0$ at $s<0$. This lowers $|s|$ by one. The entire procedure uses at most $3|s|$ clocks to reach level zero.

**Remove the remaining offset.** With $s=0$, halve an even nonzero $D$ with bit zero. For odd $D$, take bit one. The new equation is $3Y'=5X'+F$ with $F=(3D-5)/2\ne0$. Use $v=v_2(F)$ zero bits to strip $F$ to its signed odd part $f$, followed by one more zero bit. This last step makes $Y$ odd and $X$ even and returns to level zero with
$$
                            D'=(f+1)/2.                              \tag{3}
$$
For $D\ge3$, $0<D'\le(3D-3)/4$. For $D<0$, $|D'|\le(3|D|+3)/4$. Thus the absolute value falls for $|D|>3$. The same rule takes $D=1,-1$ to zero and $D=3$ to one. At $D=-3$ use the $X$-parities $1101000$. Formula (2) gives in succession
$$
 (-1,-7),\ (-2,-13),\ (-1,-5),\ (-2,-10),\ (-2,-5),\ (-1,-1),\ (0,0).
$$
This proves termination for every fixed state. The word describes parities of $X$, not the binary digits of the original $x$. The odd current slope makes each specified parity an actual binary lift.

**Clock bound.** The return after a prescribed $h$-bit prefix takes total clock $L=O(h+1)$, independently of the prefix. At clock $h$ one has $|s|\le h$ and $|D|\le 2^{O(h+1)}$ by taking a representative below $2^h$ in the defining affine equation. During removal of the nonzero levels (2) gives $|D'|\le(3|D|+6\cdot3^h)/2$, so the zero-level starting offset still has this size bound. At zero level write $d=|D|$, $d'=|D'|$, $b=v+2$. For odd $d>3$ the sign of $F$ in (3) yields
$$
                2^b(d'-3)\le3(d-3).
$$
Indeed for positive $D$ one has $2^b d'=3d-5+2^{v+1}$, and for negative $D$ one has $2^b d'=3d+5-2^{v+1}$. When $d'>3$ the drop in $\log_2(d-3)$ is at least $b-\log_2 3$, which pays for $b$ clocks by the fixed factor $2/(2-\log_2 3)$ since $b\ge2$. An even halving with $d'>3$ drops this logarithm by at least one. The last excursion costs at most $O(1+\log(2+d))$ by the formula for $F$. This gives the claimed bound.

## 2. Prescribing the two endpoints and the full arithmetic progression

Factor the prescribed modulus as $2^h 3^d M$ with $\gcd(M,6)=1$. Section 1 supplies a refined binary class $x=r+2^L t$ with endpoints $z=z_0+3^p t$ and $5z$, where $p$ is the common odd count. Impose the odd part of the starting congruence by choosing $t$ in the appropriate class modulo $3^d M$. The available values of $z$ now form a progression with difference $3^{d+p}M$. Its coefficient is odd, so further binary digits can be prescribed freely.

The following ordinary blocks start from $(z,5z)$ and end at $(F(z),5F(z))$ at their indicated clocks. The residue requirement determines only the displayed number of low bits.

| Required residue of $z$ | Clock | $F(z)$ |
|---|---:|---:|
| $0\bmod2$ | 1 | $E(z)=z/2$ |
| $49\bmod64$ | 6 | $A(z)=(9z+7)/64$ |
| $65\bmod256$ | 8 | $B(z)=(27z+37)/256$ |

Each formula follows by iterating on the stated representative and comparing both slopes on all lifts. For example $T^6(49)=7$, $T^6(245)=35$, with two odd inputs on each arm. The third row gives $7,35$ from $65,325$ with three odd inputs. No lower bound on the last division exponent beyond the fixed prefix is needed.

Modulo $M$ the three affine maps are permutations. Their semigroup contains their inverses by finiteness. The permutations $EA$ and $AE$ have the same slope and differ by the translation $-7/128$. Likewise $EB$ and $BE$ differ by $-37/512$. Their translations generate all residues since $\gcd(7,37)=1$ and $2$ is invertible. Hence one can move any residue to any other by a finite word in the three blocks. All such words can be imposed while retaining the starting progression, since the free slope after each block remains odd.

Take $o=\operatorname{ord}_M(2)$ with $o=1$ for $M=1$, and put $w=1+v_3(o)$. Plan a terminal word consisting of $k=\lceil w/2\rceil$ copies of $A$ followed by $e$ copies of $E$. Modulo $3^w$ the first part has constant value $7/55$, since this is the fixed point of $A$ and its slope is $9/64$. Choose $e$ with $2^{-e}(7/55)\equiv q\pmod{3^w}$. This is possible since $2$ generates the units of every power of three. The terminal word acts bijectively modulo $M$. First use transitivity to move the current residue modulo $M$ to the preimage of $q$ under that word, then apply it. The resulting endpoints are $z',5z'$ on the representative. All positive lifts give $(z'+3^P M u,5(z'+3^P M u))$ with $P$ equal to the initial ternary exponent $d+p$ plus the odd counts of the appended first-arm blocks. In particular $P\ge 2k\ge w$, $z'\equiv q\pmod M$, and $z'\equiv q\pmod{3^w}$.

Now choose arbitrarily large $b$ divisible by $2o$ with $2^b q\equiv z'\pmod{3^P}$. Indeed $v_3(2^{2o}-1)=w$ by factoring $4^o-1$ and repeated cubing. Its powers give every unit congruent to one modulo $3^w$ at precision $3^P$. Also $2^b q\equiv z'\pmod M$. The choices give actual positive lifts with first endpoint $2^bq$, second endpoint $2^b5q$. Halving $b$ times proves (1). All arithmetic, including the case where the progression consists of multiples of three, concerns ordinary positive integers.

For fixed starting progression and binary prefix, the terminal $e$ and the modular route can be chosen from finite lists determined by $q\bmod 3^w M$. The resulting $P$, prefix and intercept thus have uniform finite bounds. Choose the least legal $b$ above a fixed bound ensuring a positive lift. Its period has a uniform bound from $2o$ and $3^P$. The affine formula for the source then gives $x\le Kq$. Increasing $b$ through its period gives infinitely many distinct lifts. These constants may be large.

## 3. Simultaneous blocks and the gap to a proof

Include $c_0=0$. The compatible-slope merger theorem successively refines the binary parameter cell so that each $x+c_i$ meets $x$, and each $5(x+c_i)$ meets $5x$, on fixed ordinary words. Within the first group all initial slopes are one, and within the second group they are five. Thus each comparison has equal clocks on its two arms by equality of affine slopes and unique factorization. Preserve the prescribed low bits throughout and refine to at least the largest clock used. The rest of sections 1–2 places the *reference* pair at $q,5q$ at a later common clock. Determinism puts every other start at its specified endpoint at precisely that clock. [Affine merger theorem](AFFINE_RAYS.md#classification-and-a-constructive-bound)

If Collatz fails, PR 157 supplies $q\in C$ with $5q\notin C$. Apply the block result with consecutive shifts. The set of failed indices has upper Banach density one and lower Banach density zero, the latter from the same construction with $q=1$. The existence of a finite bound on gaps between successful comparisons would contradict the failed blocks. Conversely, if Collatz holds every comparison succeeds. In particular any independent proof of five-closure on an entire arithmetic progression finishes the conjecture. The construction proves that failures would be replicated in each progression. It gives no bound on gaps between successes, and the ordinary paths it constructs retain the two different prescribed endpoints. Their convergence relationship remains the open step.

The [exact Python replay](check_five_return_classes.py) constructs compact certificates for fixed, supplied targets and moduli, checks the signed states and modular generators, and follows four prescribed-target examples as literal ordinary paths, including a two-start block. Run `python -B research/upper-bit-mergers/check_five_return_classes.py` from the repository root.

**A quantitative count.** With a single failed odd ternary unit $q_0$, every fixed block length and starting progression have at least $cX^\beta$ failed block starts up to $X$ for all sufficiently large $X$, where
$$
                          \beta=1/\log_2(2^{23}/9)>0.
$$
For any odd ternary unit $q$, choose $L_0\in[6,11]$ with $2^{L_0}q\equiv7\pmod9$. Among $L=L_0,L_0+6,L_0+12$, exactly two values of $x_L=(2^Lq-7)/9$ are ternary units: consecutive differences are $7\cdot2^Lq$ and the next difference is 64 times that, giving the same nonzero step modulo three. Both lie in $49\pmod{64}$ and are smaller than $(2^{23}/9)q$. The first two accelerated odd steps from $x_L$ have exponents $2,L-2$ and end at $q$. On the other arm the length-six block $A$ followed by $L-6$ halvings ends at $5q$. Thus the two children inherit the comparison, and $q$ is uniquely recovered from each child. The $2^k$ distinct nodes at depth $k$ are below $(2^{23}/9)^k q_0$. Choosing $k$ by the height cutoff proves the power bound for failed individual queries. To pass to blocks, the construction in sections 1–3 chooses $x\le Kq$ with its clock also bounded in terms of the prescribed pattern and progression alone, as seen by the finite choices of route and final exponent. Any one chosen $x$ therefore represents at most a bounded number of different $q$, all among its bounded list of iterates. This preserves the exponent in the block count. In particular the sum of $x^{-\beta}$ over failed block starts diverges if Collatz fails, by partial summation.

**Smaller comparisons within each progression.** After the modular blocks in section 2 the common endpoint has odd slope and is a ternary unit. For any $b$ one can refine the free binary digits so that this endpoint has exact binary valuation $b$. Halving $b$ times gives an odd ternary unit $y$ with $x\sim y$ and $5x\sim5y$. The slope of $y$ relative to $x$ is the prefix slope divided by $2^b$. Given any $\epsilon>0$, choose $b$ making this slope less than $\epsilon$. Then $y<\epsilon x$ for every sufficiently large member of this refined progression. This gives genuine descent on a subprogression of *each* prescribed progression. A supplied integer has fixed higher bits, and these subprogressions have not been shown to contain every supplied integer.

## 4. An exact test for finite chains through certified five-comparisons

Here is a separate attempt at constructing a pointwise certificate on a sufficient class. The model allows ordinary affine mergers and multiplication links at selected certified **base points**. A proof for the whole binary neighborhood would still require the multiplication implications at its other points.

Use a free parameter $t$ near zero. The starting and final forms are $q+t,5(q+t)$. Each intermediate form is $n+ct$ with $c>0$. Slopes are positive dyadic rationals. Restricting $t$ to a sufficiently high power of two ensures integrality. The two base anchors below are odd ternary units. If the guards are also required on varied parameters, restrict $t$ to multiples of three as well. An ordinary link is a merger of adjacent forms on fixed ordinary words throughout that class. A multiplication link replaces a form by five times itself, or reverses that operation if reverse use is permitted. At $t=0$ the smaller arm of a multiplication link must be one of the supplied anchors $r$, with both $r$ and $5r$ certified to reach 1. Cost counts multiplication links only. Assume $q$ is a positive odd ternary unit with a supplied path to 1.

For a convergent $n$ put $g(n)=d(n)-2p(n)$ at first arrival, with $d$ clocks and $p$ odd inputs. Write $D(r)=g(5r)-g(r)$ when both paths exist. For each form record its slope with factors two and three removed and its adjusted grade $g(n)-v_2(c)-2v_3(c)$. An ordinary link preserves both quantities by equality of endpoint slopes and additivity of $g$. Conversely equal quantities suffice at convergent base points: append complete $1,2$ cycles to the two first-hit paths to equalize endpoint slopes, then restrict the common parameter so both words remain legal. These claims also hold for dyadic rational slopes after clearing a common binary denominator. [Ordinary affine membership proof, LC-1](https://github.com/GettysburgResearch/collatz/blob/ef4022fa5ae43dd943ecca0b7c84d69af624c5c9/research/pointwise-closure-20261120/LOCAL_CERTIFICATE_GRADE.md)

A forward multiplication link multiplies the residual slope by five and adds $D(r)$ to the adjusted grade. The reverse subtracts $D(r)$. Thus a forward-only chain from $q+t$ to $5(q+t)$ has **exactly one** multiplication link. Even with arbitrary ordinary links before and after, it requires $D(q)=D(r)$. If $5q$ fails to converge, no chain terminating in the certified anchors can certify it.

With the two anchors **1 and 7** and both orientations allowed, the minimum cost when $5q$ converges is exactly
$$
                         |2D(q)-5|.                                   \tag{4}
$$
Their grades are $D(1)=2$ and $D(7)=3$, using the first-hit pairs $(d,p)=(0,0),(4,1),(11,5),(10,3)$ for $1,5,7,35$. If $n_1,n_7$ denote the signed numbers of uses, the endpoint conditions give $n_1+n_7=1$ and $2n_1+3n_7=D(q)$. The sum of their absolute values is (4). To attain it, take all the required positive links first and then all the negative links. The current residual slope is always $5^e$ with $e\ge0$, and $e\ge1$ whenever division is needed. If the current adjusted grade is $I$ and the desired next anchor arm is $z$, use the form $z+5^e2^{g(z)-I}t$. Its two invariants match the previous form, so the ordinary link exists. Apply the selected multiplication link and repeat. The final invariants match $5(q+t)$ by the two count equations. Intersect the finitely many binary neighborhoods. This constructs the chain from the two given hitting paths. Only the individual anchor facts are unconditional on its nonordinary links.

**Finite deadline for a given budget $B$.** A chain of cost at most $B$ requires $g(5q)\ge G=g(q)+\lceil(5-B)/2\rceil$. For any positive $n$ first hitting 1 with grade $g$, its preterminal odd inputs are at least three. Hence $2^{d}\le n(10/3)^p$, so $(6/5)^p\le n2^{-g}$. Since $(6/5)^4>2$, this implies $d\le8\lceil\log_2 n\rceil-7g$. Run $5q$ only through $\max(0,8\lceil\log_2(5q)\rceil-7G)$ clocks. A hit gives the exact grade and cost. If no hit is seen, that budget is impossible regardless of any later orbit behavior.

There is no uniform budget even on one-step sources. Let $q=(4^{m+1}-1)/3$ with $m\ge1$ and $3\nmid(m+1)$. Its first odd jump reaches 1. PR 157's GCL-001 gives $2m+4$ ordinary steps from $5q$ with $2m+1$ odd inputs to $y=(5\cdot9^m-1)/4$. If $5q$ converges this gives $D(q)=2-4m+g(y)<2+\log_2(5/4)-m\log_2(16/9)$, using $g(y)\le\log_2 y$. Hence any successful chain (4) costs at least $1-2\log_2(5/4)+2m\log_2(16/9)$. If $5q$ never converges it has no successful chain of any cost. This shows precisely why permitting a fixed number of these links does not prove closure on the one-step family. [GCL-001, forced ordinary path](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/closing-attempts.md)
