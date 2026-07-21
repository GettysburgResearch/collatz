# Current integrated state

Last updated: 2026-07-21  
Integrator status: provisional synthesis by `gpt56-pro-01`  
Active issue: `#2 — Bootstrap exact collision-rewrite research program`  
Active draft PR: `#3 — Bootstrap exact collision-rewrite research program`

## Project maturity

The repository now contains two mathematical research sessions on one branch.
No claim has yet received independent review. Complete-looking finite theorems
and identities are therefore recorded as `PROPOSED`.

There is currently **no positive-integer Collatz counterexample** in the
repository.

## Fixed framework

The active work uses the shortcut map

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Parity words are chronological. Digit strings used for rewrite systems are
low-order first. `NOTATION.md` is authoritative.

For a length-\(L\) parity word with \(a\) odd steps,

\[
T^L(n)=\frac{3^a n+B}{2^L}
\]

on its residue class.

## Main conceptual advance: collision fibers, not only intervals

The first session studied consecutive collision bundles. `T-0002` shows that
consecutiveness is irrelevant.

Suppose

\[
T^L(2^Lq+r+d)=3^aq+s
\qquad(d\in D)
\]

for a finite, possibly sparse digit set \(D\). If \(3^a>2^L\), then the
fiber induces the partial expanding radix map

\[
\boxed{
H_D(2^LB+d)=3^aB+d,
\qquad d\in D.
}
\]

One explicit invariant congruence class of induced states lifts exactly to
ordinary positive Collatz integers. An infinite admissible finite-integer orbit
of \(H_D\) would be a Collatz counterexample.

`T-0001` is the special case in which \(D\) is an initial interval.

## Exact collision-fiber recursion

`L-0003` gives an exact recursion for every residue's affine data. If

\[
a_L(r)=\#\text{ odd steps},
\qquad s_L(r)=T^L(r),
\]

then even residues inherit the data of \(r/2\). For an odd residue \(2k+1\),
write

\[
3k+2=2^Lq+u.
\]

Then

\[
a_{L+1}(2k+1)=1+a_L(u),
\]

\[
s_{L+1}(2k+1)=3^{a_L(u)}q+s_L(u).
\]

Collision fibers are exactly the level sets of \((a_L,s_L)\). All tables
through depth \(L\) can be generated in total \(O(2^L)\) arithmetic work.
This reframes fiber growth as an exact even/odd coalescence process.

## Strongest exact charts currently recorded

### O-0001 — Two-branch `64 -> 81` chart

\[
T^6(64q+14)=T^6(64q+15)=81q+20.
\]

It induces

\[
H(64B+d)=81B+d,
\qquad D=\{0,1\},
\]

on the lifting class \(A\equiv6\pmod{17}\).

### O-0002 — Three-branch `512 -> 729` chart

\[
T^9(512q+124+d)=729q+182,
\qquad D=\{0,1,2\}.
\]

A short exact carry tile is

\[
R_1L_{361}L_0\longrightarrow L_2L_2R_1.
\]

It is locally interesting but does not vertically close by itself.

### O-0003 — Six consecutive branches at depth 17

\[
T^{17}(131072q+9090+d)=177147q+12302,
\qquad0\le d\le5.
\]

### O-0004 — Eighteen sparse branches at depth 22

Let

\[
D=\{0,16,20,21,32,34,35,40,42,49,68,69,70,78,79,92,93,94\}.
\]

Then

\[
\boxed{
T^{22}(4194304q+621248+d)=4782969q+708587
\qquad(d\in D).
}
\]

The induced chart is

\[
H(4194304B+d)=4782969B+d,
\qquad d\in D,
\]

with lifting class

\[
A\equiv87339\pmod{588665}.
\]

Its expansion ratio is approximately \(1.1403486729\), while its base-radix
boundary grows at only approximately one new digit per 116 induced steps. The
combination of a richer alphabet and slow boundary motion is a new macro-tile
target.

## Universal local amplification

`L-0004` generalizes the nine-column stack of `L-0002`.

For any coprime radices \(M<N\), every closed carry path

\[
R_cX\longrightarrow ER_c
\]

can be pumped horizontally:

\[
R_cX^m\longrightarrow E^mR_c.
\]

If an induced alphabet contains \(0\) and a nonzero digit \(j\), let \(k\) be
the least positive integer with

\[
M^kj\equiv j\pmod N.
\]

Then there is a finite block \(W_j\) satisfying

\[
R_jW_j\longrightarrow L_0^kR_j,
\]

and

\[
H_D^{km+1}(L_jW_j^m(x))=N^{km}(Nx+j).
\]

Therefore **every nontrivial collision fiber has exact finite-horizon stack
amplifiers**. Local pumping is universal; the hard step is finite vertical
closure.

## Global structure of any hypothetical induced orbit

### T-0003 — Dual adic/real coding

For an infinite induced orbit with least digits \(d_t\), input radix \(M\),
output radix \(N\), and \(c=N-M\),

\[
A_0=\frac{c}{N}\sum_{t\ge0}d_t\left(\frac MN\right)^t
\]

holds exactly in \(\mathbb Q_2\).

In the real topology, define

\[
x_t=\frac{c}{N}\sum_{j\ge0}d_{t+j}\left(\frac MN\right)^j.
\]

Then

\[
A_t=C\left(\frac NM\right)^t+x_t
\]

for one \(C>0\), with \(x_t\) bounded between the minimum and maximum digits.
Thus the base-\(M\) word length has asymptotic slope

\[
\lim_{t\to\infty}\frac{\ell_t}{t}
=\log_M(N/M).
\]

The digit itinerary of a nontrivial ordinary-integer orbit cannot be eventually
periodic. A successful grammar must generate genuinely aperiodic boundary
motion.

### T-0004 — Run-length skeleton

Every maximal constant-digit phase has the exact form

\[
d+M^uC
\longmapsto
 d+N^uC.
\]

At the next digit change, an infinite orbit is equivalent to an infinite chain

\[
\boxed{
d_k+N^{u_k}C_k
=d_{k+1}+M^{u_{k+1}}C_{k+1},
}
\]

where \(d_k\in D\), \(d_{k+1}\ne d_k\), \(u_k\ge1\), and
\(M\nmid C_k\).

This is the new global target: construct a finite family of cofactor schemas
closed under these exact `S`-unit carry transitions, together with the lifting
congruence. Individual huge starting values are secondary.

## Computational state

### X-0001 — Consecutive bundles through depth 17

The best consecutive widths found were

```text
L=6..8:   2
L=9..13:  3
L=14..16: 5
L=17:     6
```

### X-0002 — Complete fibers through depth 22

The best full-fiber cardinalities are

```text
L=6..8:    2
L=9..10:   3
L=11..13:  4
L=14..16:  5
L=17..18:  8
L=19..21: 12
L=22:      18
```

`X-0002` uses the exact recursion of `L-0003`, cross-checks every direct trace
through depth 12, verifies the eighteen-branch identity and lifting equations,
reconstructs universal carry pumping, and checks the run-length skeleton on
exact finite trajectories.

These finite observations do not establish unbounded cardinality or an
infinite admissible orbit.

## Central unresolved step

The project still lacks a **finite-boundary regeneration theorem**.

The strongest current formulation is to construct either:

1. a finite macro-tile grammar whose emitted rows close vertically and whose
   high-order boundary remains an ordinary finite word; or
2. a finite family of run-length/cofactor schemas closed under

   \[
   d_k+N^{u_k}C_k
   =d_{k+1}+M^{u_{k+1}}C_{k+1},
   \]

   with an aperiodic but finitely generated exponent schedule.

Compatible finite prefixes, a periodic adic tiling, or a point in an inverse
limit remain insufficient.

## Immediate research priorities

1. **Coalescence algebra.** Use `L-0003` to construct analytic families of
   sparse fibers, rather than merely enumerating them. Determine whether
   supercritical fiber cardinalities are unbounded.
2. **Macro-tile atlas.** Build carry-cycle graphs for the width-3, width-8, and
   width-18 alphabets. Search for vertical relays among several pumped tiles,
   not one self-repairing block.
3. **Run-length schemas.** Seek parameterized positive solutions of the
   `S`-unit skeleton, with cofactors transported by a finite collection of
   exact formulas.
4. **Aperiodic boundary control.** Use the exact slope
   \(\log_M(N/M)\) to organize two-length or `S`-adic schedules. Fixed-period
   travelling stacks cannot suffice.
5. **Multi-chart transitions.** Permit designated transitions between
   collision charts when one chart creates a cofactor or boundary suited to
   another.
6. **Finite-versus-adic audit.** Every construction must explicitly prove that
   one ordinary finite starting word, not only an inverse-limit object, follows
   the entire infinite grammar.
