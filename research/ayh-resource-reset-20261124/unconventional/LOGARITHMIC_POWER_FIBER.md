# An ordinary exclusion for every base of a fixed perfect power

Let $j=11+162m$, let $M_j=2^j-1$, and let $U_j=3^j-1=T^jM_j$.
For **every** ordinary integer $b\ge0$ take the preassigned parameter
$m=b^{2^{2956}}$. If its original e6 parent $z$, given by
$81z+271=128\cdot2^j$, is no greater than every reverse defect, then $z$
reaches one. In particular it cannot be the least reverse defect. The
base is arbitrary; no representative is changed after $b$ is supplied.
[Kernel-checked theorem](PerfectPowerParents.lean)

For $b=0$ the parent is $3233$, which reaches one in 107 steps.
For positive odd $b$, $m\equiv1\pmod{2^{1141}}$, and the two ordinary
peaks $U_j,U_{j-42}$ meet at the same postpeak clock 1143. For even positive
$b$, they are $U_j,U_{j-63}$ and the common postpeak clock is
$v_2(m)+2960$. These peak identities are unconditional. In particular the
even branch applies to each preassigned $m=6^{2^t}$ for $t\ge2956$,
which approaches zero both dyadically and ternarily. In each branch the
earlier ordinary Mersenne source costs less than $z/2^{40}$. If $z$ were
bad then the earlier source would be bad, giving an even smaller reverse
defect by the quantitative return theorem. There is no claim of an
unconditional Collatz proof for these parents.

## Keeping the unit lost by the approach to zero

Write $K=2957$, $A=3^{162}$ and
$$
 B_s=\frac{A^{2^s}-1}{2^{s+3}}\quad(s\ge0).
$$
These are odd positive integers. Squaring gives
$B_{s+1}=B_s+2^{s+2}B_s^2$. Their residues modulo $2^K$ therefore stabilize
for $s\ge2955$. Let $B$ be this stabilized residue and let
$U_*=3^{-58}B\bmod2^K$ be its least nonnegative representative. All
arithmetic here uses finite integers. A recurrence reducing modulo $2^K$
after each step calculates $B$ in 2955 squarings. [Finite certificate](LogTowerData.lean)

More generally take $m=4^r v$ with $v>0$, $2r\ge2955$, and
$3^r v\equiv1\pmod{2^K}$. The ordinary integer
$$
                 u=\frac{3^{162m}-1}{2^{2r+3}}
                 \equiv vB\pmod{2^K}
$$
retains the significant binary digits. The congruence follows by raising
$1+2^{2r+3}B_{2r}$ to $v$. Set $\ell=r-58$.

The positive anchor $3^{11}-1$ and the rational anchor $3^{-52}-1$ reach
one at postpeak clock 119. Their odd counts are respectively 60 and 52.
The formal verification avoids rationals by lifting the latter from the
positive integer residue $a$ satisfying $3^{52}a=1+2^{119}a_0$,
$0<a<2^{119}$. The four integer identities at $a-1$ and $3^{63}a-1$
appear in the finite certificate. Lifting these 119 steps for the
**actual positive** peaks $U_{j-63},U_j$ yields respectively
$$
               1+4^\ell u,\qquad 1+4^\ell 3^{71}u .
$$
For every nonnegative $x$, $T^2(1+4x)=1+3x$. Following $\ell$ laps
produces $1+U,1+3^{71}U$ with $U=3^\ell u\equiv U_*\pmod{2^K}$.
At $U_*$ the two ordinary endpoints at clock $K$ are equal and their
odd counts are 1513 and 1442. Their difference compensates the initial
factor $3^{71}$, so the same equality holds for every lift of $U_*$.
The total common clock is $119+2\ell+2957=2r+2960$.
[Integer lifts and laps](LogTowerCore.lean) [Ordinary peak theorem](LogTower.lean)

For $b=2^a c$ with $a\ge1$ and $c$ odd, put $D=2^{2956}$,
$r=a2^{2955}$ and $v=c^D$. Repeated squaring gives
$3^r\equiv c^D\equiv1\pmod{2^K}$. Thus every even base supplies the original,
positive parameter on the required band. For an odd base the smaller
modulus suffices. At $m=1$ the exponents 173 and 131 have a common
postpeak endpoint one at clock 1143, with $548$ and $590$ odd steps.
Both augmented grades equal $721$. The multiplier
$3^{162(m-1)}\equiv1\pmod{2^{1143}}$ when $m\equiv1\pmod{2^{1141}}$,
so the equality lifts across the entire odd-base branch.

At $m=0$ itself the first two signed anchors have incompatible augmented
grades. Ordinary lifting at a fixed dyadic depth discards the unit carrying
the 2957-bit certificate, while the valuation-length run along the
$1,2$ cycle extracts it. The displayed cutoff gives a sufficient exponent
for all bases. Optimality of the exponent, and coverage of all $m$, remain
open.
