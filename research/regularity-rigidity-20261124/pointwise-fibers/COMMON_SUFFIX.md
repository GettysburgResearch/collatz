# Finite-menu common suffix: reduction to fixed-target one-arm counting

**Status: proposed written theorem, source-qualified by PR146's affine and ratio-five control lemmas.** No universal pointwise inverse estimate or Collatz proof is claimed. An exact BigInt control is supplied separately.

Let $T(n)=n/2$ for even $n$ and $(3n+1)/2$ for odd $n$. At the end of a common-clock prefix from $(x,5x)$, write the endpoints $y,Y$, the respective odd counts $p,p+k$, and the integer relative offset $D$ defined by

$$
3^{k_-}Y=5\,3^{k_+}y+D,\qquad k_+=\max(k,0),\quad k_-=\max(-k,0).
$$

Here and below all finite paths are in the ordinary integers.

## The common-suffix theorem

Fix $K\ge1$, a unit residue $y_0\bmod 3^K$, a finite menu $S$ of states $(k,D)$ with $|k|\le K$, and $B>0$. Retain just the states with $3^{k_-}\mid 5\,3^{k_+}y_0+D$, i.e. those integral on the prescribed ternary class. Assume this retained menu is nonempty.

For every positive odd ternary unit $q$, there is a positive odd unit $y(q)\equiv y_0\pmod {3^K}$, a common finite clock $H(q)$, and a source odd count $a$, such that for every retained state

$$
Y_s(y)=\frac{5\,3^{k_+}y+D}{3^{k_-}},\qquad
T^{H(q)}(y(q))=q,\qquad T^{H(q)}(Y_s(y(q)))=5q.
$$

The companion suffix has exactly $a-k$ odd inputs. All these paths are positive. The constants $a$, $\sup_q H(q)$, and $\sup_q y(q)/q$ are finite and depend only on the fixed menu, ternary class and $B$. The construction pays for the prefix real offset: if the first-arm prefix has offset $0\le\beta\le B$, the concatenated first-arm affine offset is at most $1/2$.

### Proof

Parameterize $y=y_0+3^K t$, initially fixing the parity of $t$ so $y$ is odd. Each companion form has slope $5\,3^{K+k}$ and integer intercept, and the reference form $5y$ has slope $5\,3^K$. Thus all companion forms and the reference have the same part prime to 6 and all slopes are odd. The finite-list version of the affine merger theorem in [PR146, AFFINE_RAYS.md](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/AFFINE_RAYS.md) produces a refined binary class of $t$ on which all of these forms meet at a common clock. The source arm is not among the forms being merged; advance it through the same clock. All its parities are fixed on the refined class.

Now apply the deterministic ratio-five root control of [PR146, FIVE_RETURN_IN_EVERY_CLASS.md, section 1](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/FIVE_RETURN_IN_EVERY_CLASS.md) to the source and the reference. Further refine the binary class to make the source and reference have equal odd counts and endpoint ratio five. Every companion remains merged with the reference. Finally append the common six-clock $A$ block on source residue $49\bmod64$, with map $z\mapsto(9z+7)/64$. Its legality is imposed by six more binary bits (the current source slope is odd); its output is a ternary unit.

Consequently some fixed binary class $t=r+2^h u$, with the total physical clock $h$, has source endpoint $z_0+3^{K+a}u$, reference and all companions endpoint $5(z_0+3^{K+a}u)$, and $3\nmid z_0$. The count on the source is $a$, on the reference also $a$, and on each companion $a-k$, as follows by equating the affine slopes $5\,3^{K+k+a_s}$ and $5\,3^{K+a}$. The signed intercepts may be used during construction, but all starts and paths are positive on sufficiently large positive lifts $u$.

The primitive-root property of 2 modulo $3^{K+a}$ gives a residue of $b$ modulo $L=2\cdot3^{K+a-1}$ for which

$$
2^b q\equiv z_0\pmod{3^{K+a}}.
$$

Choose its least representative above a fixed lower bound $b_0$, which can ensure $u=(2^b q-z_0)/3^{K+a}$ is sufficiently large for all the positivity conditions even when $q=1$. Then $b<b_0+L$, $y(q)=y_0+3^K(r+2^h u)=O_{S,K,y_0,B}(q)$, and $H=h+b$. Both source and every companion halve $b$ further times to $q$ and $5q$. If the original first-arm prefix has offset $\beta$, the final offset is

$$
2^{-b}\left(\frac{3^a}{2^h}\beta+\frac{C_s}{2^h}\right),
$$

where $C_s$ is the fixed source suffix carry through clock $h$. Enlarge the fixed lower bound $b_0$ to make this at most $1/2$ for every $\beta\le B$. This proves the theorem. All congruences and clocks are chosen before any inverse-prefix family is selected.

## A fixed-target counting reduction

**Scope correction:** the following implication is conditional for a
fixed selected menu. FS cannot hold for every integral menu, even if the
companion endpoints are positive units and the state occurs on a literal
balanced ordinary pair. The necessary offset inequality
$D>-5\,3^{k_+}B$ excludes, for example, $(k,D)=(0,-4)$ when $B=1/2$.
The [exact obstruction and revised open quantifier](../refinement/PAIRED_FIBER_AUDIT.md)
are separate results. The original sufficient implication below is retained;
its hypothesis must be established for a suitable cutoff-compatible menu.

Consider the following *one-arm, finite-state-filtered* estimate, denoted FS. For a fixed ternary class and fixed menu as above, for every positive odd unit $y\equiv y_0\pmod{3^K}$, there exist arbitrarily large balanced pairs $(e,p)$, $p/e\to1/2$, having

$$
G^{1-o(1)},\qquad G=2^e/3^p,
$$

distinct positive odd unit starts $x$ with $T^e(x)=y$, $p$ odd inputs, first-arm real affine offset at most $B$, and relative state of $(x,5x)$ at clock $e$ in the fixed menu. The estimate must hold at the supplied $y$; an average over $y$ is not enough.

**If FS holds, the pointwise paired-fiber target PT of PAIRED_FIBERS.md holds at every positive odd unit $q$.** For a supplied $q$, choose $y(q)$ and the common suffix first, then apply FS at that single fixed $y(q)$. Append the suffix to every selected prefix, keeping all $x$ distinct. Both full paths have clock $e'=e+H$; their total odd counts agree and equal $p'=p+a$, their endpoints are $q,5q$, and the final first-arm real offset is at most $1/2$. The starting and terminal source values are odd, so these words uniquely parse as concatenations of the marked return dictionary. Since

$$
G'=\frac{2^{e'}}{3^{p'}}=\frac{2^H}{3^a}G
$$

differs by a fixed factor, the count is $(G')^{1-o(1)}$, with $p'/e'\to1/2$. This is PT, without a new averaging step or a change of the target $q$.

The unresolved issue is FS itself. Existing one-arm inverse word spreading (rStation paper 37) does not give the fixed-menu joint relative-state condition. A probability estimate for bounded relative states in an unconditioned dyadic-prefix experiment cannot simply be transferred to a fixed ordinary terminal fiber. Nor can the suffix be selected separately for each inverse word without paying for the loss of a common target and clock. Even PT would need an opposing estimate or another rigidity mechanism to complete Collatz.

## Finite exact control

For $K=1$, $y_0=1$, and the integral states with $k\in\{-1,0,1\}$, $-3\le D\le3$, the menu has 16 members, including the reference state. The constructive test in COMMON_SUFFIX_CONTROL.js produced clock 83, binary parameter residue 4483086877358389416883568, source intercept 208724745227658145, and final slope $3^{37}$. The source has 36 odd inputs; the state $k$ companion has $36-k$. The script checked the final affine profiles and 544 literal positive paths (17 arms including the source, 32 lifts each). This finite control does not establish FS or the universal conjecture. No Lean compilation performed.
