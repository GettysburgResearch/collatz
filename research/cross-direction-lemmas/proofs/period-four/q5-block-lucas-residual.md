# The two-level block decomposition and its root-of-unity carry states

Date: 2026-07-22

Status: scratch-only theorem checkpoint.  The shared repository was not
edited.  The identities and local valuations below hold for every index.
The final uniform cyclotomic cutoff is **not** claimed.

## 1. Exact block decomposition

Put

\[
 C_{u,a}(q)=\frac{(q;q)_{2u+1}(q;q)_a}
 {(q;q)_u(q;q)_{u-a}(q;q)_{2a+1}}.
\]

The two already proved level-lowering identities give

\[
 Q_u^{(5)}=\sum_{a=0}^u q^{a(a+1)}C_{u,a}Q_a^{(3)},
 \qquad
 Q_a^{(3)}=\sum_{b=0}^a q^{b(b+1)}C_{a,b}(q;q)_b.
\]

Set `a=b+c` and `N=u-b`.  Direct cancellation of the factorials gives

\[
 C_{u,a}C_{a,b}(q;q)_b
 =\frac{(q;q)_{2u+1}(q;q)_b^2}
 {(q;q)_u(q;q)_{N-c}(q;q)_c(q;q)_{2b+1}}.
\]

Consequently

\[
 \boxed{Q_u^{(5)}(q)=\sum_{b=0}^u D_{u,b}(q)F_{u-b,b}(q)}                 \tag{1}
\]

where

\[
 D_{u,b}=\frac{(q;q)_{2u+1}(q;q)_b^2}
 {(q;q)_u(q;q)_{u-b}(q;q)_{2b+1}}
 =C_{u,b}(q)(q;q)_b,                                                     \tag{2}
\]

and

\[
 F_{N,b}=\sum_{c=0}^N
 q^{(b+c)(b+c+1)+b(b+1)}{N\brack c}_q.                                  \tag{3}
\]

Thus every apparent cancellation in the middle index has already been
summed into a Rogers--Szego-type block `F`.  Notice the important unit
identity

\[
 F_{N,b}(1)=2^N.                                                         \tag{4}
\]

## 2. Exact q-Lucas block reduction

Let `zeta` be a primitive `m`-th root and write `N=Am+R`, with
`0<=R<m`.  The root-of-unity q-Lucas identity is

\[
 {Am+R\brack Cm+d}_{\zeta}
 =\binom AC{R\brack d}_{\zeta}.
\]

The phase in (3) is unchanged when `c` is replaced by `c+m`.  Summing the
ordinary binomial coefficient over `C` therefore proves

\[
 \boxed{F_{Am+R,b}(\zeta)=2^A F_{R,b}(\zeta).}                           \tag{5}
\]

This remains valid over any field of characteristic prime to `m` that
contains `zeta`.  In odd characteristic the scalar `2^A` is nonzero.  Hence
root cancellation in the `F` part reduces to the finite state

\[
 (R,\ b\bmod m),\qquad 0\le R<m.                                        \tag{6}
\]

Equation (5) concerns values.  It does not, by itself, assert equality of
root multiplicities for the large and residual blocks.

## 3. A proved residual zero, and its exact simplicity

Let `0<=R<m` be odd and put

\[
 A_0=2b+R+1.
\]

If

\[
 \zeta^{A_0}=-1,                                                        \tag{7}
\]

then complementation `c <-> R-c` in (3) cancels every pair, because

\[
 E(R-c)-E(c)=(R-2c)A_0
\]

and `R-2c` is odd.  Equivalently, in residue language,

\[
 m\equiv0\pmod4,
 \qquad 2b+R\equiv m/2-1\pmod m.                                       \tag{8}
\]

This residual zero is exactly simple.  Here is a proof that does not rely
on the finite scan.  With the Rogers--Szego polynomial

\[
 H_R(t;Q)=\sum_{c=0}^R{R\brack c}_Q t^c,
\]

reciprocity of the Gaussian polynomial gives the exact two-variable form

\[
 F_{R,b}(q)=q^{2b(b+1)}H_R(q^{A_0};q^{-1}).                              \tag{9}
\]

For odd `R`, symmetry makes `H_R(-1;Q)=0` identically in `Q`.  It remains
to show that the root in the `t` variable is simple at `Q=zeta^{-1}`.
Write `R=2h+1`,

\[
 E_h=H_{2h}(-1;Q),\qquad D_h=\partial_tH_{2h+1}(-1;Q).
\]

The standard Rogers--Szego recurrence

\[
 H_{n+1}(t;Q)=(1+t)H_n(t;Q)-t(1-Q^n)H_{n-1}(t;Q)
\]

gives

\[
 E_h=\prod_{i=1}^h(1-Q^{2i-1}),
 \qquad
 D_h=E_h+(1-Q^{2h})D_{h-1},\quad D_0=1,
\]

and hence

\[
 D_h=\sum_{j=0}^h
 \left(\prod_{i=1}^j(1-Q^{2i-1})\right)
 \left(\prod_{r=j+1}^h(1-Q^{2r})\right).                               \tag{10}
\]

At `Q=zeta^{-1}` every sine magnitude in (10) is positive, since all
factor exponents are below `m`.  After the usual extraction
`1-Q^r = (nonzero positive magnitude) times exp(-pi*i*r/m)` up to one
common phase, the `j`-th summand has exponent sum

\[
 j^2+h(h+1)-j(j+1)=h(h+1)-j.
\]

Thus all `h+1` nonzero summands lie in a sector of angular width
`h*pi/m < pi/2`.  They cannot sum to zero.  Therefore

\[
 D_h(\zeta^{-1})\ne0,                                                    \tag{11}
\]

and (9) proves

\[
 \boxed{\operatorname{mult}_{\Phi_m}F_{R,b}=1}
 \quad\text{under (7).}                                                 \tag{12}
\]

No converse to (7) is asserted here.  Exact scans find no other residual
zeros in the tested box, but turning that observation into all-order
nonvanishing is a separate lemma.

## 4. Frobenius-weighted local valuations

Fix an odd prime `p` with `p` not dividing `m`, and work at a primitive
`m`-th root in characteristic `p`.  Use `y=q^m-1` as local parameter and
define

\[
 W_p(n)=\sum_{r=1}^n p^{v_p(r)},\qquad W_p(0)=0.                         \tag{13}
\]

If `m` does not divide `i`, then `1-q^i` is a unit.  If `i=mr`, then

\[
 1-q^{mr}=1-(1+y)^r
\]

has `y`-order `p^{v_p(r)}` by Frobenius.  Therefore

\[
 \operatorname{ord}_y(q;q)_n=W_p(\lfloor n/m\rfloor).                  \tag{14}
\]

Combining (2) and (14) gives the exact carry weight of every factorial
block:

\[
 \boxed{
 V_{p,m}(u,b)=
 W_p(\lfloor(2u+1)/m\rfloor)-W_p(\lfloor u/m\rfloor)
 -W_p(\lfloor(u-b)/m\rfloor)-W_p(\lfloor(2b+1)/m\rfloor)
 +2W_p(\lfloor b/m\rfloor).}                                          \tag{15}
\]

For `m=1`, (4) is a unit in odd characteristic, so (15) is the exact
Taylor order of the entire `b`-block in (1):

\[
 V_b=W_p(2u+1)-W_p(u)-W_p(u-b)-W_p(2b+1)+2W_p(b).                       \tag{16}
\]

The digit recurrence

\[
 W_p(pn+r)=pW_p(n)+(p-1)n+r,\qquad0\le r<p,                             \tag{17}
\]

makes (16) a finite carry computation.  More explicitly, write
`u=pU+r`, `b=pB+t`, and set

\[
 c=\lfloor(2r+1)/p\rfloor,
 \quad e={\bf1}_{t>r},
 \quad f=\lfloor(2t+1)/p\rfloor.
\]

Then direct substitution in (17) yields the exact one-digit recurrence

\[
\begin{aligned}
 V_b={}&p\{W_p(2U+c)-W_p(U)-W_p(U-B-e)-W_p(2B+f)+2W_p(B)\}\\
      &+(p-1)B+t+f-c-e.                                                 \tag{18}
\end{aligned}
\]

This is the promised carry/borrow state: `c` is the carry in `2u+1`, `e`
the borrow in `u-b`, and `f` the carry in `2b+1`.

## 5. Prime-power boundary and the remaining cancellation lemma

For the `b=0` block put

\[
 V_0=W_p(2u+1)-2W_p(u)-1.                                               \tag{19}
\]

If `p^k` is the least power of `p` strictly above `2u+1`, the standard
base-`p` carry expansion of (19) proves

\[
 0\le V_0\le p^{k-1}-1,
 \qquad 2V_0+1<p^{k-1}(p-1)=\varphi(p^k).                               \tag{20}
\]

Thus the following single structural estimate would close every odd
prime-power order above the cutoff:

\[
 \operatorname{ord}_{q=1}(Q_u^{(5)}\bmod p)\le2V_0+1.                  \tag{21}
\]

Equation (21) is strongly supported by exact data but is **not proved in
this checkpoint**.  Individual block orders (16) do not by themselves
bound the order of their sum: tied leading units can cancel.

In particular, the tempting sharper assertion

\[
 \operatorname{ord}Q_u^{(5)}\le\min_bV_b+1
\]

must not be used without proof.  A two-jet carry audit already has double
leading-state cancellations at `(p,u)=(13,105)` and `(29,675)` (among
others), so a universal one-step argument is false or at least requires
additional states.  The safe next task is to prove (21) by tracking the
finite leading-unit automaton through at most the `V_0`-wide band.

## 6. What is theorem and what remains open

The block identity (1), q-Lucas reduction (5), antisymmetric residual
simplicity (12), local valuation formula (15), and carry recurrence (18)
are all-order theorems.

The converse classification of residual `F` zeros, the multiplicity of a
large block when its residual state vanishes, the cancellation bound (21),
and the full non-dyadic cyclotomic cutoff remain open.



