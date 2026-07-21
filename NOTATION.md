# Notation and semantic conventions

Last updated: 2026-07-21  
Maintainer for this revision: `gpt56-pro-01`

This file fixes the conventions used by the active collision-rewrite, negative-renewal, interval, and marked-particle packet. Later work should state explicitly when it departs from them.

## Shortcut Collatz map

Throughout the packet,

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

The map is used on all ordinary integers when studying negative templates. Unless a claim says otherwise, a claimed counterexample variable is an ordinary positive integer, not a 2-adic or rational point.

## Parity words

A length-\(L\) parity word is

\[
w=t_0t_1\cdots t_{L-1},
\qquad t_i\in\{0,1\},
\]

in chronological order. Thus \(t_0\) is the starting parity.

Define

\[
a(w)=\sum_{i=0}^{L-1}t_i
\]

and

\[
B(w)=
\sum_{\substack{0\le j<L\\t_j=1}}
2^j3^{\sum_{i=j+1}^{L-1}t_i}.
\]

Then

\[
T^L(n)=\frac{3^{a(w)}n+B(w)}{2^L}
\]

for every integer following \(w\).

## Affine residue tables and collision fibers

For \(0\le r<2^L\), define

\[
a_L(r)=\#\{0\le t<L:T^t(r)\text{ is odd}\},
\]

\[
s_L(r)=T^L(r).
\]

Then

\[
T^L(2^Lq+r)=3^{a_L(r)}q+s_L(r).
\]

A collision fiber is a level set of

\[
r\longmapsto(a_L(r),s_L(r)).
\]

For a fiber of length \(L\) and odd count \(a\), write

\[
M=2^L,
\qquad N=3^a.
\]

It is **supercritical** when \(N>M\).

Choose an anchor \(r\) and offsets \(D\) such that

\[
T^L(Mq+r+d)=Nq+s
\qquad(d\in D).
\]

Define

\[
c=N-M,
\qquad \kappa=Ms-Nr,
\qquad h=s-r.
\]

The older induced coordinate is

\[
\Phi(n)=cn+\kappa,
\]

with partial map

\[
H_D(MB+d)=NB+d,
\]

invariant class

\[
A\equiv h\pmod c,
\]

and lift

\[
\nu(A)=\frac{NA-\kappa}{c}.
\]

## Inverse signatures and collision codes

For a length-\(L\), weight-\(a\) word, its inverse signature is

\[
\sigma(w)=2^{-L}B(w)\pmod{3^a}.
\]

A finite fixed-length, fixed-weight family whose constants agree modulo \(3^p\) is a parity collision code of precision \(p\). Its precision surplus is \(p-a\).

For chronological concatenation \(uv\),

\[
B(uv)=3^{a(v)}B(u)+2^{|u|}B(v).
\]

## Digit constructors and mixed-radix words

For radix \(M\),

\[
L_d(x)=Mx+d,
\qquad0\le d<M.
\]

For radix \(N\),

\[
R_c(x)=Nx+c,
\qquad0\le c<N.
\]

Strings are low-order first:

\[
L_{d_0}L_{d_1}\cdots L_{d_k}\#
=L_{d_0}(L_{d_1}(\cdots L_{d_k}(0)\cdots)).
\]

For a low-order-first word \(U=(u_0,\ldots,u_{k-1})\),

\[
[U]_M=\sum_{i=0}^{k-1}u_iM^i.
\]

The normalization rule is

\[
R_cL_x\longrightarrow L_eR_q,
\qquad Nx+c=Mq+e.
\]

A closed path

\[
R_cX\longrightarrow ER_c
\]

is a carry macro-tile. Horizontal pumping alone does not prove vertical closure.

## Run-length skeleton

For a nonzero integer \(z\), define divisibility by powers of the whole radix:

\[
\operatorname{ord}_M(z)
=\max\{u\ge0:M^u\mid z\}.
\]

A maximal constant-digit phase begins at

\[
A=d+M^uC,
\qquad M\nmid C,
\]

and evolves as

\[
H_D^t(A)=d+N^tM^{u-t}C
\qquad(0\le t\le u).
\]

The sequence \((d,u,C)\) is the run-length skeleton.

## Negative templates and signed returns

A negative template is a positive magnitude \(u\) such that

\[
T^L(-u)=-v
\]

for a selected negative target magnitude \(v\).

A collision fiber with residues \(r_i\) and output \(s\) gives

\[
u_i=M-r_i,
\qquad v=N-s.
\]

At phase \(-v_i\), write a positive physical state as

\[
n=q-v_i.
\]

An edge \(e:i\to j\) based on

\[
T^{L_e}(-u_e)=-v_j
\]

has cylinder

\[
q\equiv v_i-u_e\pmod{2^{L_e}}
\]

and quotient map

\[
F_e(q)=3^{a_e}\frac{q-v_i+u_e}{2^{L_e}}.
\]

For a stationary chart, the intrinsic signed return equation is

\[
Nq=Mq'+a,
\qquad a=v-u.
\]

## Negative phase and complementary phase maps

For a positive phase magnitude \(v\), define

\[
P(v)=
\begin{cases}
v/2,&v\text{ even},\\[1mm]
(3v-1)/2,&v\text{ odd},
\end{cases}
\]

so that

\[
T(-v)=-P(v).
\]

Define the complementary map

\[
C(v)=
\begin{cases}
3v/2,&v\text{ even},\\[1mm]
(v+1)/2,&v\text{ odd}.
\end{cases}
\]

For the coupled state \(n=q-v\), put

\[
p=q\bmod2,
\qquad r=v\bmod2,
\qquad e=p\oplus r.
\]

One exact step is

\[
q'=\frac{3^eq+p}{2},
\qquad
v'=\frac{3^ev+(2p-1)r}{2}.
\]

If \(q\) is even, \(v'=P(v)\) and the orbit shadows the negative phase. If \(q\) is odd, \(v'=C(v)\) and a mismatch occurs.

## Rounded physical-parity phase maps

Using physical parity

\[
e=n\bmod2,
\]

the lower phase follows

\[
S_0(v)=\left\lceil\frac v2\right\rceil,
\qquad
S_1(v)=\left\lfloor\frac{3v}{2}\right\rfloor.
\]

They satisfy

\[
S_0(v)+S_1(v)=2v.
\]

For a word \(w=e_0\cdots e_{L-1}\), write

\[
S_w=S_{e_{L-1}}\circ\cdots\circ S_{e_0}.
\]

The escape-transform cylinder weight is

\[
\mathbb Q_v([w])
=2^{-|w|}\frac{S_w(v)-1}{v-1}
\qquad(v>1).
\]

## Finite interval gauge

Represent a positive physical state \(n\) by a finite interval

\[
I=[v,q),
\qquad q-v=n,
\qquad v\ge1.
\]

For even length,

\[
\mathcal R_0([v,q))
=
[\lceil v/2\rceil,\lceil q/2\rceil).
\]

For odd length,

\[
\mathcal R_1([v,q))
=
[\lfloor3v/2\rfloor,\lceil3q/2\rceil).
\]

The new interval length is exactly \(T(n)\).

Two canonical gauges are:

- fixed lower endpoint: \(v=1,\ q=n+1\);
- diagonal: \(v=n+1,\ q=2n+1\).

In the diagonal gauge, \(v-1=n\).

## Ordered particle completion

Put

\[
x=v-1.
\]

Define branch population maps

\[
R_0(x)=\left\lfloor\frac x2\right\rfloor,
\qquad
R_1(x)=\left\lceil\frac{3x}{2}\right\rceil.
\]

For an ordered root population

\[
[x]=\{1,\ldots,x\},
\]

each parent has two children:

\[
2k\longmapsto(0,k),(1,3k),
\]

\[
2k-1\longmapsto(1,3k-2),(1,3k-1).
\]

The branch-\(e\) children form exactly \([R_e(x)]\). After \(L\) levels there are \(2^Lx\) descendants in total.

A uniformly selected descendant has branch-word law

\[
\frac{R_w(x)}{2^{|w|}x}
=
\mathbb Q_{x+1}([w]).
\]

## Distinguished ordinary spine

One child of each particle is marked as physical:

\[
\chi(j)=
\begin{cases}
(0,j/2),&j\text{ even},\\[1mm]
(1,(3j+1)/2),&j\text{ odd}.
\end{cases}
\]

Its rank is \(T(j)\). Iterating \(\chi\) from one finite root particle gives the ordinary shortcut-Collatz trajectory of that root.

Terminology:

- **escape path:** an unmarked branch of the phase/population tree;
- **ordinary spine:** a marked finite-root lineage following \(\chi\).

The terms must not be interchanged.

## Valuation and cycle-padding notation

The ordinary binary valuation is

\[
\nu_2(q)=\max\{k\ge0:2^k\mid q\}.
\]

For a negative phase \(v\), define the odd count along \(k\) negative-phase steps by

\[
A_v(k)=\sum_{j=0}^{k-1}(P^j(v)\bmod2).
\]

If \(v\) lies on a negative cycle of period \(\ell\) with \(a\) odd phases, its cycle multiplier is

\[
\Lambda=\frac{3^a}{2^\ell}>1.
\]

A padding counter \(t\ge0\) records \(t\) complete synchronized cycle circuits before a fixed mismatch type. Return towers then have

\[
L_t=L_0+t\ell,
\qquad
a_t=a_0+ta,
\qquad
\lambda_t=\lambda_0\Lambda^t.
\]

## Prefix-code and pressure notation

For a finite or countable binary prefix code \(\mathcal W\), the fair cylinder mass is

\[
\mu_{1/2}([w])=2^{-|w|}.
\]

The \(3/4\)-odd tilted mass is

\[
\mu_{3/4}([w])
=\frac{3^{a(w)}}{4^{|w|}}.
\]

The real block multiplier is their likelihood ratio:

\[
\lambda(w)=\frac{3^{a(w)}}{2^{|w|}}
=\frac{\mu_{3/4}([w])}{\mu_{1/2}([w])}.
\]

For graph edges \(e:i\to j\), define pressure matrices

\[
\mathcal A_s(i,j)
=
\sum_{e:i\to j}2^{-L_e}\lambda_e^s.
\]

\(\mathcal A_0\) measures fair 2-adic coverage. \(\mathcal A_1\) measures tilted Collatz mass.

## Real and 2-adic conventions

For a stationary induced orbit, put

\[
\rho=M/N,
\qquad \lambda=N/M.
\]

The same formal digit series may be interpreted in \(\mathbb Q_2\) and in \(\mathbb R\), but the limiting identities are different. Every claim must state the topology used.

For a signed stationary return chain, the normalized aspect ratio is

\[
\Delta=
\frac{\operatorname{diam}A}{N-M}.
\]

## Finite words versus adic objects

A **finite canonical word** contains finitely many digits and a terminal marker `#`. It represents one ordinary nonnegative integer.

A left-infinite or nonterminating digit string may represent a radix-adic object. Compatibility of all finite suffixes does not imply an ordinary finite positive integer.

No candidate may be promoted unless it proves:

1. one finite positive starting integer;
2. exact agreement with the deterministic Collatz trajectory;
3. no unproved infinite left tail;
4. integrality and positivity at every boundary;
5. an infinite selector or grammar defined forever;
6. justified net growth on every reachable grammar cycle;
7. preservation of the distinguished ordinary spine;
8. unboundedness or permanent avoidance of the terminal cycle.
