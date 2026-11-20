# A density budget for label-blind physical renewal

**PROPOSED elementary limitation of one architecture.** This identity
concerns the positive inverse-fiber kernel of paired transport blocks.
It does not construct a nonconstant Collatz invariant, disprove an
estimate restricted to actual invariant labels, or exclude all
ordinary-source compilers.

## DC1. One block and two residue densities

For a legal positive odd word with `p>=1` odd inputs and total shortcut
clock `L`, source and endpoint satisfy

\[
x=(2^Lq-B)/3^p,\qquad B>0,\qquad 3\nmid B.
\tag{1}
\]

Suppose a second legal word with the same `p,L` transports `5x` to
`5q`, so its correction is `5B`. Restrict both source and endpoint
to odd ternary units.

The source word specifies one binary residue modulo `2^(L+1)`. Its
relative binary cylinder measure among odd inputs is `2^(-L)`; the
independent ternary-unit restriction gives the same relative density
among odd ternary units.

On the endpoint side, integrality specifies one unit residue modulo
`3^p`. Of its three lifts modulo `3^(p+1)`, exactly one makes `x`
divisible by three. Thus two of the `2*3^p` unit residues are legal:
the endpoint fraction is exactly `3^(-p)`. Oddness is independent of
these odd moduli. Positivity removes only finitely many endpoints, and
`x/q -> a=2^L/3^p` along each legal class.

## DC2. Exact mean of a finite inverse-fiber kernel

For a finite set `F` of blocks, put

\[
K_s^F(q)=\sum_{w\in F:\ q\text{ legal for }w}(q/x_w(q))^s.
\tag{2}
\]

The positive column-sum estimate for arbitrary endpoint charges with
weight `q^(-s)` has constant `sup_q K_s^F(q)`. Disjoint source
cylinders prevent source double counting. The following averaging
identity itself remains true with multiplicities:

\[
\boxed{\lim_{Q\to\infty}
\frac{\sum_{q\le Q,\ q\text{ odd},\;3\nmid q}K_s^F(q)}
{\#\{q\le Q:q\text{ odd},\;3\nmid q\}}
=\sum_{w\in F}3^{-p_w}(3^{p_w}/2^{L_w})^s.}
\tag{3}
\]

For each block use its exact residue fraction `3^(-p)` and its limiting
ratio. Finite initial exceptions have zero mean. Summing finitely many
convergent means proves (3), without exchanging infinite or signed sums.
At the harmonic exponent,

\[
\boxed{\lim\operatorname{mean}K_1^F=\sum_{w\in F}2^{-L_w}.}
\tag{4}
\]

The right side is the binary cylinder mass for a prefix-free family.

## DC3. Consequence for an infinite pure-transport family

Suppose a possibly infinite prefix-free family has binary cylinder mass
`d=sum_w 2^(-L_w)`, and a label-blind bound `K_s(q)<=C` holds at
every endpoint outside a fixed finite set, such as the known zero
endpoint one. Every finite partial family has the same bound. Apply
(3) to those partial families and take their increasing supremum:

\[
C\ge\sum_w2^{-L_w}(2^{L_w}/3^{p_w})^{1-s}.
\tag{5}
\]

In particular `C>=d` at exponent one. If every physical endpoint also
satisfies `q<=theta*x` for a common `0<theta<1`, its limiting inverse
slope is at least `1/theta`. For `0<s<1`,

\[
\boxed{C\ge theta^{s-1}d.}
\tag{6}
\]

Thus a uniform coefficient below one cannot survive a **Haar-full**
pure-transport cover. At a subcritical exponent and fixed strict height
contraction, the restriction is stronger. It is a cost of controlling
every positive endpoint charge separately, without using which charges
can arise from one actual invariant label.

## What this does not exclude

A countable union of binary cylinders can contain every positive ordinary
integer while having arbitrarily small Haar measure. Enumerate the odd
positive integers and enclose the `j`th in a cylinder of relative measure
at most `epsilon*2^(-j)`. Their union contains every such integer but
has measure at most `epsilon`. Removing redundant prefixes makes the
family prefix-free without changing its union. Therefore all-ordinary
coverage does **not** imply `d=1` in (5). Natural density equals cylinder
mass for the particular expanded ladder only because its infinite tail
is separately controlled; this cannot be presumed for a general adaptive
family.

Actual five defects may vanish on many endpoints. A support-sensitive
bound for those defects need not bound every delta charge and is not
prohibited by (5). Independently certified zero-defect source families
can also be removed before renewal. Their needed coverage or support
estimate is not furnished by this identity.

The result limits adding transport cylinders while retaining a uniform
column-sum constant below one. It leaves source-sensitive, nonlinear,
nonuniform, and separately certified-zero mechanisms available. It does
not assert a Collatz counterexample or an impossibility of proving Collatz.
