# Recurrent residue classes on one ordinary orbit

**FS-019. PROPOSED ordinary-map obstruction.** Use the shortcut
$T_0(x)=x/2$, $T_1(x)=(3x+1)/2$, with the branch selected by the
parity of the source. Let $d_m$ be the number of residue classes
modulo an odd integer $m\ge3$ visited infinitely often by a single
positive orbit. If that orbit is not eventually periodic, then
$$
  m\le6\cdot3^{2d_m}.
$$
In particular its orbit has infinitely many accumulation points in
$\mathbb Z_p$ for every odd prime $p$. This is a constraint on the
actual forward trajectory that supports any escaping pressure spike.

Form a directed graph from the $d=d_m$ recurrent residues and the
parity-labelled transitions occurring infinitely often. The actual
trajectory eventually uses only this graph because there are finitely
many labelled transitions. Each of its vertices lies on a simple
directed cycle of length at most $d$, by following the tail from that
vertex to a later revisit and removing intermediate loops. Select one
such cycle for each vertex $z$, rotating it to start at $z$.
Composition along it has the form $(3^q x+C_z)/2^l$, where $l\le d$
and $q$ counts the odd inputs. The integer $C_z$ is nonnegative and
at most $3^l-2^l$. Indeed the maximum intercept numerator at time
$j+1$ is at most three times the preceding maximum plus $2^j$,
starting at zero. Consequently, with $D_z=2^l-3^q$,
$$
 D_z z\equiv C_z\pmod m,\qquad
 |D_z|,C_z\le 3^d.
$$
The denominator $D_z$ is odd and nonzero even if $q=0$.
The rational $r_z=C_z/D_z$ is therefore a dyadic integer in the
sense $r_z\in\mathbb Q\cap\mathbb Z_2$.

Every recurrent edge $z\to u$ with parity $e$ satisfies
$2u\equiv3^e z+e\pmod m$. Multiplication by $D_zD_u$ gives
$$
 m\mid 2C_uD_z-3^eC_zD_u-eD_uD_z.
$$
If $m>6\cdot3^{2d}$, the integer on the right vanishes by the size
bounds, hence $r_u=(3^e r_z+e)/2$ in $\mathbb Q$. Exactly one of the
two parities $e$ gives an image in $\mathbb Z_2$. All recurrent edges
leaving $z$ thus use the same bit, and that bit determines a unique
successor modulo odd $m$. The true tail follows a deterministic finite
graph and has eventually periodic parity. If a positive integer $x$
starts its repeating tail word of period $l$, the integers $x$ and
$T^l x$ have identical parity itineraries. Their difference is
divisible by every $2^j$, since the affine numerator of their
$j$-step difference is $3^{q_j}(x-T^l x)$. Thus $x=T^l x$. This
proves the stated necessary bound for a nonperiodic orbit.

For $m=p^k$, each recurrent class contains a $p$-adic accumulation
point by compactness, so a finite set of $h$ such points would give
$d_{p^k}\le h$ for every $k$, contradicting the bound. The estimate
permits unbounded but very sparse support and gives no contradiction
with the upper estimates for first-hit pressure in FS-017.
