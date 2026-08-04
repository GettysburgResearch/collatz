# Notation and semantic conventions

Last updated: 2026-07-21  
Maintainer for this revision: `gpt56-pro-01`

This file fixes the conventions used by the active collision-rewrite,
negative-renewal, interval, marked-particle, and Hensel counter-stack packet.
Later work should state explicitly when it departs from them.

## Shortcut Collatz map

Throughout the packet,

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

The map is used on all ordinary integers when studying negative templates.
Unless a claim says otherwise, a claimed counterexample variable is an ordinary
positive integer, not a 2-adic or rational point.

## Parity words

A length-\(L\) parity word is

\[
w=t_0t_1\cdots t_{L-1},
\qquad t_i\in\{0,1\},
\]

in chronological order. Thus \(t_0\) is the starting parity. Put

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
\qquad
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

It is **supercritical** when \(N>M\). Choose an anchor \(r\) and offsets
\(D\) such that

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

A finite fixed-length, fixed-weight family whose constants agree modulo
\(3^p\) is a parity collision code of precision \(p\). Its precision surplus
is \(p-a\).

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

For a low-order-first word \(U=(u_0,\ldots,u_{k-1})\), write

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

is a carry macro-tile. Horizontal pumping alone does not prove vertical
closure.

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

## Negative and complementary phase maps

For a positive phase magnitude \(v\), define

\[
P(v)=
\begin{cases}
v/2,&v\text{ even},\\[1mm]
(3v-1)/2,&v\text{ odd},
\end{cases}
\]

so that \(T(-v)=-P(v)\). Define

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

If \(q\) is even, \(v'=P(v)\) and the orbit shadows the negative phase. If
\(q\) is odd, \(v'=C(v)\) and a mismatch occurs.

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
=[\lceil v/2\rceil,\lceil q/2\rceil).
\]

For odd length,

\[
\mathcal R_1([v,q))
=[\lfloor3v/2\rfloor,\lceil3q/2\rceil).
\]

The new interval length is exactly \(T(n)\).

Two canonical gauges are:

- fixed lower endpoint: \(v=1,\ q=n+1\);
- diagonal: \(v=n+1,\ q=2n+1\).

In the diagonal gauge, \(v-1=n\).

## Ordered particle completion and ordinary spine

Put

\[
x=v-1.
\]

Define

\[
R_0(x)=\left\lfloor\frac x2\right\rfloor,
\qquad
R_1(x)=\left\lceil\frac{3x}{2}\right\rceil.
\]

For the ordered population \([x]=\{1,\ldots,x\}\), each parent has two
children:

\[
2k\longmapsto(0,k),(1,3k),
\]

\[
2k-1\longmapsto(1,3k-2),(1,3k-1).
\]

The branch-\(e\) children form exactly \([R_e(x)]\). A uniformly selected
descendant has branch-word law

\[
\frac{R_w(x)}{2^{|w|}x}
=\mathbb Q_{x+1}([w]).
\]

One child is marked as physical:

\[
\chi(j)=
\begin{cases}
(0,j/2),&j\text{ even},\\[1mm]
(1,(3j+1)/2),&j\text{ odd}.
\end{cases}
\]

Its rank is \(T(j)\). Terminology:

- **escape path:** an unmarked branch of the phase/population tree;
- **ordinary spine:** a marked finite-root lineage following \(\chi\).

The terms must not be interchanged.

## Regular marked configurations

A synchronous endpoint word is

\[
\operatorname{conv}(v,q)
\]

over the alphabet \(\{00,01,10,11\}\), read least-significant position first.
For a regular pair language \(G\),

\[
\operatorname{Len}(G)
=
\{\operatorname{bin}_{\rm LSD}(q-v):\operatorname{conv}(v,q)\in G\}.
\]

`L-0015` proves that \(\operatorname{Len}(G)\) is effectively regular. A
finite-phase regular marked grammar with fixed finite block lengths is therefore
in the regular-sanctuary class of `T-0020`.

## Valuation and cycle-padding notation

The ordinary binary valuation is

\[
\nu_2(q)=\max\{k\ge0:2^k\mid q\}.
\]

For a negative phase \(v\), define

\[
A_v(k)=\sum_{j=0}^{k-1}(P^j(v)\bmod2).
\]

If \(v\) lies on a negative cycle of period \(\ell\) with \(a\) odd phases,
its cycle multiplier is

\[
\Lambda=\frac{3^a}{2^\ell}>1.
\]

A padding counter \(t\ge0\) records \(t\) complete synchronized cycle
circuits before a fixed mismatch type. Put

\[
k_t=k_0+t\ell,
\qquad
g_t=g_0+ta.
\]

## Padded tower block normal form

For a mismatch/recovery type with recovery length \(r\) and recovery odd count
\(b\), let \(\mu_t\) be the unique odd residue

\[
0\le\mu_t<2^{r+1}
\]

satisfying

\[
3^{g_t}\mu_t\equiv-1\pmod{2^{r+1}}.
\]

Define

\[
c_t=\frac{3^{g_t}\mu_t+1}{2^{r+1}},
\]

\[
A_t=2^{k_t}\mu_t,
\qquad
K_t=k_t+r+1,
\]

\[
B_t=3^bc_t,
\qquad
G_t=g_t+b.
\]

Then

\[
0\le A_t<2^{K_t},
\qquad
0\le B_t<3^{G_t},
\]

and one exact Collatz block performs

\[
\boxed{
A_t+2^{K_t}h
\longmapsto
B_t+3^{G_t}h
}
\qquad(h\ge0).
\]

The high tail \(h\) is one ordinary finite integer, not a formal infinite word.

For the four phase-\(-34\) self-return types of the negative eleven-cycle,

\[
\ell=11,
\qquad a=7,
\]

and the finite core periods are \(16,8,4,2\).

## Canonical connector tile

Let a left tower instance have block data \((A,K,B,G)\), and let the next
instance have input data \((\bar A,\bar K)\). The canonical seed is the least
nonnegative solution

\[
\eta\equiv(\bar A-B)3^{-G}\pmod{2^{\bar K}},
\qquad0\le\eta<2^{\bar K}.
\]

Define

\[
\theta=\frac{B+3^G\eta-\bar A}{2^{\bar K}}.
\]

Then

\[
0\le\theta<3^G
\]

and, for every \(z\ge0\),

\[
\boxed{
\eta+2^{\bar K}z
\longmapsto
\theta+3^Gz.
}
\]

The connector preserves the still-higher ordinary tail \(z\) for one
transition.

## Normalized connector prefix

For one tower type, define

\[
\omega_t=
\frac{\mu_t+3^{-g_t}}{2^{r+1}}
\in\mathbb Z_2.
\]

At low precision the canonical connector seed satisfies

\[
\eta\equiv-\omega_t\pmod{2^H}
\]

when the next input anchor is divisible by \(2^H\).

For every \(H\ge1\), the exact Hensel jump

\[
\Delta_H=2^{H+r-1}
\]

preserves the prefix:

\[
\omega_{t+\Delta_H}\equiv\omega_t\pmod{2^H}.
\]

## Corrected 256-step dyadic stage

At scale \(m\), define

\[
t_{m,j}=2^m+j2^{m-8},
\qquad0\le j\le256.
\]

Then

\[
t_{m,256}=t_{m+1,0}.
\]

Put

\[
H_m=m-r-7,
\qquad
J_m=m-r+1.
\]

The exact odometer law is

\[
\nu_2(\omega_{m,j}-\omega_{m,0})
=H_m+\nu_2(j)
\qquad(1\le j\le256).
\]

Thus one stage consists of:

- a stable low prefix;
- an eight-bit finite odometer \(j\);
- one scale overflow after 256 transitions;
- one additional stabilized stage-boundary bit.

The earlier 128-step schedule is called the **one-connector precursor**. It does
not pay the complete two-cylinder residual cost and must not be called a closed
stage.

## Rational frontier and quadratic Hensel bulk

At stage boundaries \(t=2^m\), let \(\mu_*\) be the stabilized finite core and
put

\[
\omega_\infty
=
\frac{\mu_*+3^{-g_0}}{2^{r+1}}.
\]

Define

\[
y_m=3^{-7\cdot2^m},
\qquad
u_m=\frac{y_m-1}{2^{m+2}}.
\]

Then \(u_m\) is an odd 2-adic unit and

\[
\boxed{u_{m+1}=u_m+2^{m+1}u_m^2.}
\]

The stage-boundary prefix decomposes as

\[
\boxed{
\omega_m
=
\omega_\infty
+2^{m-r+1}3^{-g_0}u_m.
}
\]

The three stack tracks are:

1. the periodic rational frontier \(\omega_\infty\);
2. the eight-bit odometer;
3. the moving quadratic bulk \(u_m\).

A finite-prefix implementation may use

\[
U_{m+1}
\equiv
U_m+2^{m+1}U_m^2
\pmod{2^N}
\]

at any precision \(N\) already present. Producing new higher bits remains a
separate forward-generation obligation.

## Residual stack recurrence

For chronological connector data \((G_n,\theta_n,\eta_{n+1},K_{n+2})\), the
ordinary residual high tail is

\[
\boxed{
z_{n+1}
=
\frac{3^{G_n}z_n+\theta_n-\eta_{n+1}}{2^{K_{n+2}}}.
}
\]

The relevant residual slope is

\[
\frac{3^{G_n}}{2^{K_{n+2}}},
\]

not the immediate one-connector slope \(3^{G_n}/2^{K_{n+1}}\).

A valid stage theorem must prove exact divisibility, nonnegativity, and enough
residual capacity after this complete two-cylinder cost.

## Current counter-stack state

The preferred abstract state is

\[
(i,m,j,W,z,n),
\]

where:

- \(i\) is finite tower/phase control;
- \(m\) is the unbounded dyadic scale;
- \(j\in\{0,\ldots,255\}\) is the stage odometer;
- \(W\) is the finite frontier/quadratic-bulk word;
- \(z\) is the ordinary residual tail;
- \(n\) is the explicitly marked ordinary Collatz integer.

A full stage must return the same syntactic track types at scale \(m+1\).

## Prefix-code and pressure notation

For a finite or countable binary prefix code \(\mathcal W\),

\[
\mu_{1/2}([w])=2^{-|w|}
\]

is fair cylinder mass, while

\[
\mu_{3/4}([w])
=\frac{3^{a(w)}}{4^{|w|}}
\]

is the \(3/4\)-odd tilted mass. Their likelihood ratio is

\[
\lambda(w)=\frac{3^{a(w)}}{2^{|w|}}.
\]

For graph edges \(e:i\to j\),

\[
\mathcal A_s(i,j)
=
\sum_{e:i\to j}2^{-L_e}\lambda_e^s.
\]

\(\mathcal A_0\) measures fair 2-adic coverage and \(\mathcal A_1\) measures
tilted Collatz mass.

## Real and 2-adic conventions

For a stationary induced orbit, put

\[
\rho=M/N,
\qquad \lambda=N/M.
\]

The same formal digit series may be interpreted in \(\mathbb Q_2\) and in
\(\mathbb R\), but the limiting identities are different. Every claim must
state the topology used.

For a signed stationary return chain, the normalized aspect ratio is

\[
\Delta=\frac{\operatorname{diam}A}{N-M}.
\]

## Finite words versus adic objects

A **finite canonical word** contains finitely many digits and a terminal marker
`#`. It represents one ordinary nonnegative integer.

A left-infinite or nonterminating digit string may represent a radix-adic
object. Compatibility of all finite suffixes does not imply an ordinary finite
positive integer. In particular, the limit of nested connector prefixes
\(\omega_m\) is not a counterexample unless those bits are generated forward
from one finite ordinary stack.

No candidate may be promoted unless it proves:

1. one finite positive starting integer;
2. exact agreement with the deterministic Collatz trajectory;
3. no unproved infinite left tail or 2-adic oracle;
4. integrality and positivity at every boundary;
5. an infinite selector or grammar defined forever;
6. exact generation of every newly required stack bit;
7. justified net growth after every consumed future cylinder;
8. preservation of the distinguished ordinary spine;
9. unboundedness or permanent avoidance of the terminal cycle.