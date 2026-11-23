# Fixed-resolution asymptotic envelopes cannot be excessive

**Status: new written theorem; not a Collatz proof.** The finite weighted-row
implication is suitable for a small Lean core. The regularly varying
limits and modular realization below are written mathematics. No
predecessor-density, stationary-density, or unproved Collatz input is used.

This theorem rules out a whole proposed class of global Lyapunov
majorants. It does **not** rule out a sublinear upper bound for the
canonical envelope, or a genuinely nonlocal excessive function. An upper
bound need not itself be excessive, and the canonical envelope can have
different asymptotics on indefinitely finer residue classes.

The final corollary covers **every fixed modulus** using Monks's
published arithmetic-progression theorem. The ternary and mixed
binary–ternary cases have separate elementary proofs here.

## 1. Operator, actual sources, and the theorem

On positive odd integers use
\[
(PF)(q)=\sum_{\substack{e\ge1\\2^e q\equiv1\pmod3}}
  \frac3{2^e}F\!\left(\frac{2^e q-1}{3}\right).
\tag{1}
\]
Every displayed parent is a positive odd ordinary integer. Thus (1)
is the actual inverse operator for
\[
U(n)=(3n+1)/2^{v_2(3n+1)}.
\]
The function \(F\) is nonnegative. The sum is a nonnegative extended
sum; excessivity means that it is finite and \(PF(q)\le F(q)<\infty\)
at every positive odd \(q\).

Fix an integer \(r\ge0\), put \(M=3^r\), and let
\(a:\mathbb Z/M\mathbb Z\to[0,\infty)\) be a finite profile.
Let \(p<1\) be real and let \(L\) be positive at large positive
arguments. The exact regularity assumption needed is
\[
\frac{L((2^e q-1)/3)}{L(q)}\longrightarrow1
\tag{2}
\]
as positive odd \(q\to\infty\) in a legal target progression, for
each of the finitely many odd exponents
\(e=1,3,\ldots,2M-1\).
For example, \(L(x)=(\log(x+2))^b\), finite products of iterated
logarithm powers, and positive constants satisfy (2). A positive
factor is used only through the displayed limit; no general
regular-variation theorem is imported.

Suppose
\[
\frac{F(n)}{n^p L(n)}-a(n\bmod M)\longrightarrow0
\qquad(n\to\infty,\ n\text{ positive odd}).
\tag{3}
\]

### Theorem A — no nonzero fixed-resolution sublinear profile

If \(F\) is excessive for (1), then \(a\equiv0\).

In particular no nonnegative excessive envelope has a nonzero fixed
ternary residue profile of the form (3) for any exponent \(p<1\).
This includes power majorants with \(0<p<1\), and \(p=0\) with a
logarithmic or other factor satisfying (2). It permits zeros in the
profile: positivity only on a few selected residue classes does not
repair the construction.

A conclusion \(a=0\) means only that the normalization in (3) is
too large to give a nonzero limiting profile. It is not a contradiction
to the mere upper bound \(F(n)=O(n^pL(n))\). For instance, a function
could be little-oh of that normalization along every fixed progression,
or fail to have the limits (3).

## 2. One target progression sees every profile residue

Take the actual positive odd targets
\[
q_k=2\cdot3^{r+1}k-1,\qquad k=1,2,\ldots.
\tag{4}
\]
They satisfy \(q_k\equiv-1\pmod{3^{r+1}}\). Every odd exponent
\(e\ge1\) is legal. Its ordinary parent is
\[
n_{e,k}=\frac{2^e q_k-1}{3}
       =2^{e+1}3^r k-\frac{2^e+1}{3},
\tag{5}
\]
so
\[
n_{e,k}\bmod M=z_e:=-\frac{2^e+1}{3}\bmod M.
\tag{6}
\]
The map
\[
e=1,3,\ldots,2M-1\quad\longmapsto\quad z_e
\tag{7}
\]
is a bijection onto all \(M\) residues modulo \(M\).
The exponent \(e=1\) gives \(z_1=-1\bmod M\), the same profile
residue as the target.

Here is an elementary justification of the coverage, including the
prime-power order being used. The order of 4 modulo \(3^{r+1}\)
is \(3^r\). Indeed
\[
v_3(4^{3^j}-1)=j+1,
\]
by induction from \(4-1=3\): if \(x=1+3^s u\), with \(s\ge1\)
and \(3\nmid u\), then
\[
x^3-1=3^{s+1}u
       (1+3^s u+3^{2s-1}u^2),
\]
and the parenthetical factor is a ternary unit. Thus the \(3^r\)
powers \(4^j\), \(0\le j<3^r\), are distinct modulo
\(3^{r+1}\) and exhaust the \(3^r\) units congruent to 1 modulo
3. Consequently \(2^{2j+1}=2\cdot4^j\) exhausts the units
congruent to 2 modulo 3. Finally
\[
u\longmapsto-(u+1)/3\bmod3^r
\]
is a bijection from that coset to all residues modulo \(3^r\).
This proves (7), also when \(r=0\).

The symbol \(-1\) here specifies a residue class. **Every target
and every source in the proof is a positive ordinary integer.**
No negative input or 3-adic completion is substituted for (4)--(5).

## 3. The finite-row contradiction

Put \(b=a(-1\bmod M)\) and define
\[
w_e=\frac3{2^e}\left(\frac{2^e}{3}\right)^p
   =\left(\frac3{2^e}\right)^{1-p}>0.
\tag{8}
\]
Because \(n_{e,k}/q_k\to2^e/3\), assumptions (2)--(3) give,
for each of the finitely many odd exponents in (7),
\[
\frac{(3/2^e)F(n_{e,k})}{q_k^pL(q_k)}
       \longrightarrow w_e a(z_e).
\tag{9}
\]
The corresponding normalized target values tend to \(b\).

Keep only these finitely many positive terms in (1), use excessivity,
and take a finite limit:
\[
\sum_{\substack{1\le e\le2M-1\\e\text{ odd}}}
                 w_e a(z_e)\le b.
\tag{10}
\]
No passage of a limit through an infinite parent series has occurred.

The term \(e=1\) is
\[
w_1b=(3/2)^{1-p}b,\qquad (3/2)^{1-p}>1.
\]
Nonnegativity and (10) force \(b=0\). Equation (10) then forces
every term \(w_ea(z_e)\) to vanish. All weights are strictly positive,
and (7) covers every residue. Thus \(a\equiv0\), proving Theorem A.

The finite abstract core is:
\[
a_i\ge0,\quad w_i>0,\quad w_{i_0}>1,\quad
\sum_iw_ia_i\le a_{i_0}
\quad\Longrightarrow\quad a_i=0\ \text{for all }i.
\tag{11}
\]
The self term proves \(a_{i_0}=0\), and each positive summand
is then zero. Formula (11) is the part that can be formalized without
the asymptotic analysis or a library of real powers.

## 4. A quantitative violation on one ordinary progression

The same argument supplies an explicit positive defect for every
nonzero profile, before assuming excessivity. Let
\[
A=\max_{z\bmod M}a(z)>0,\qquad
s=(3/2)^{1-p},\qquad
c_{\min}=(3/2^{\,2M-1})^{1-p},
\]
and put
\[
\Delta_{p,r}=\min(s-1,c_{\min})>0.
\tag{12}
\]
Then
\[
\boxed{
\liminf_{k\to\infty}
 \frac{PF(q_k)-F(q_k)}{q_k^pL(q_k)}
 \ge \Delta_{p,r}A>0.
}
\tag{13}
\]
If a parent sum is infinite, the defect is already positive infinite;
otherwise the displayed differences are well defined.

To prove (13), use the same finite retained row. If the maximum \(A\)
occurs at the base residue, its self term alone gives a normalized
defect at least \((s-1)A\). Otherwise choose an exponent \(e>1\)
whose residue has value \(A\). The retained row minus \(b\)
contains the two nonnegative contributions
\[
(s-1)b+w_e A\ge c_{\min}A.
\]
Taking the finite asymptotic limit gives (13).

The constant is conservative and can be very small when \(r\) is
large. Its purpose is exact coverage: there is a violating progression
for every finite resolution, rather than an empirical failure of a
few sampled coefficients.

## 5. Why this does not close the canonical-potential route

The actual recent inputs are frozen at:

* PR180 **bfba8feaefb3d0910456cdd92d2afcf9e8785b4d**,
  research/lean-wide-pass-20261122/ENERGY_SYNTHESIS.md:
  \(V=\kappa D\) almost everywhere, every-ordinary-point comparison
  \(V/(2\kappa)\le G\le V\), and the all-prefix-clock estimate.
* PR176 **8aeb843bba254f065743b6fa277a70906b51d520**,
  research/lean-global-resolvent-20261121/overview/parallel/OBSTACLE_ENTRANCE_RENEWAL.md:
  removal of the whole contact-avoiding inverse boundary and exact
  ordinary first-contact expansion.
* PR185 **276be8154f4e867acc0230466b34d9cb224aacf5**,
  research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md:
  the comparable ordinary harmonic flow \(\nu\), its exact
  unchanged-source collision contraction, and its infinite-mass
  qualification.
* PR175 **2bc2ad37b490a5aea63658eaf657bc048da4532e**,
  research/lean-global-closure-20261121/CANONICAL_POTENTIAL_SUPERLEVELS.md
  and LITERATURE_TRANSPORT_ATTEMPT.md: global weighted moments and
  the actual-path correction.
* PR186 **1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493**,
  literature/deep-machinery-20261122/04_returns_operators_and_termination.md:
  the retained-source norm interfaces and cautions about replacing a
  moving atom by fresh endpoint weights. This is research guidance,
  not a theorem used in Sections 1--4.

The theorem in Sections 1--4 uses none of their analytic hypotheses.
It explains why a fixed residue table times one regular growth law
cannot directly supply the missing excessive majorant. PR176 already
proves that every unit cylinder contains subcylinders with arbitrarily
large canonical values; that pointwise spike result has priority. The
new statement is different: it treats regularly varying growth at
infinity, allows zero leading coefficients on some cells, and proves
that a whole fixed-resolution asymptotic profile must vanish.

The canonical envelope itself is not asserted to satisfy (3).
Indeed its least-majorant construction and the finer-cylinder spikes
make an unboundedly refined profile natural. A proof of
\(V(q)=o(q)\) through moving marked targets could still succeed
without any nonzero profile of the excluded form.

## 6. Attempted variable-resolution continuation and the exact gap

One can try letting \(r=r(q)\) increase and approximating the
canonical \(V\) by its finite-cylinder obstacle iterates.
The result above then has two simultaneous losses:

1. Its violating targets are in a progression modulo \(3^{r+1}\),
   while its parent menu can require exponents as large as
   \(2\cdot3^r-1\).
2. The asymptotic limit (9) is taken after fixing that finite menu.
   No uniform estimate is supplied when both its exponents and
   the resolution grow with the ordinary target.

The source-pinned all-clock estimate has precisely an unresolved
resolution cost:
\[
|P^dH(q)|
 \ll \bigl(q(d+t+1)+3^t\bigr)\,\|H\|_{1,3^t}
\]
at a least odd unit of an ordinary component. The rapid \(L^1\)
approximation at finite resolution can pay polynomial costs if
\(3^t\) is controlled by \(q\). It does not control an arbitrary
critical depth while \(q\) is fixed, nor the exponentially large
parent menu in (7).

The corrected harmonic flow also makes the escaping alternative
precise: along a hypothetical escaping odd path \(q_j\),
\(\nu(q_j)\) increases to a finite positive component capacity.
The reverse transition assigning \(q_j\) to its actual predecessor
\(q_{j-1}\) then tends to one, and the total off-path increments are
summable. Positive uniform floors for a fixed short sibling charge only
a convergent reciprocal-orbit sum. Consequently neither the row
obstruction nor the fixed-root contact expansion supplies the needed
uniform arithmetic branching loss.

A genuine next theorem would control the variable-resolution trace at
these near-deterministic moving roots, or transfer the source-retaining
collision energy to a finite reference. This packet proves neither of
those statements and does not identify an infinite ordinary orbit.

## 7. Elementary extension to a mixed binary–ternary modulus

The same conclusion holds for every fixed modulus \(M=2^h3^r\),
on the residue classes containing odd integers. Here assume the affine
slow-variation condition
\[
L(cx+d)/L(x)\longrightarrow1\qquad(c>0,\ d\in\mathbb R)
\tag{14}
\]
whenever the arguments are positive. Only finitely many instances of
(14) are used for a fixed modulus and profile. The finite power and
iterated-logarithm examples above satisfy it.

The following finite residue construction is independent of any global
convergence claim.

### 7.1 Negative finite histories supply every odd mixed residue

Fix an odd residue modulo \(2^h\) and any residue \(b\pmod{3^r}\).
Choose a positive odd integer \(u\) in the binary residue. Follow
\(k=h+1\) actual odd steps from \(u\). This finite operation is always
defined; no termination theorem is used. Let their gaps be
\(a_1,\ldots,a_k\), their total \(A\ge k>h\), and their correction
\(C\), so
\[
2^A U^k(u)=3^k u+C.
\tag{15}
\]
The same gap word has inverse affine expression
\[
x=(2^A y-C)/3^k.
\tag{16}
\]
Choose a negative odd one-step predecessor of \(-1\),
\[
y=-(2^e+1)/3,\qquad e>0\text{ odd},
\]
with
\[
y\equiv 2^{-A}(C+3^k b)\pmod{3^{k+r}}.
\tag{17}
\]
Such an exponent exists by the residue bijection in Section 2, applied
at resolution \(k+r\). Equation (17) makes (16) an integer and gives
\(x\equiv b\pmod{3^r}\). It also gives
\[
x\equiv -C3^{-k}\equiv u\pmod{2^h},
\]
using (15) and \(A>h\). Since \(y<0\) and \(C>0\), \(x<0\).

For completeness, total integrality in (16) entails integrality at every
inverse letter of the selected word. If \(C'\) is the correction of
its first \(k-1\) letters, then
\[
C=3C'+2^{A-a_k}.
\]
Reducing \(2^Ay-C\) modulo 3 proves that
\((2^{a_k}y-1)/3\) is integral. Substitution reduces the full
integrality assertion to the prefix with one fewer letter; induction
finishes. Every intermediate value is negative and odd, since each
map is \(y\mapsto(2^a y-1)/3\) with \(a\ge1\).
Thus this is an actual finite negative odd history, not merely an
integral terminal affine formula. Its forward path ends at \(y\)
and then at \(-1\).

Consequently the negative predecessor basin of \(-1\) meets every
odd residue class modulo \(2^h3^r\), by an elementary finite
construction.

### 7.2 Lift each finite signed history to positive ordinary rays

Let \(z<0\) be odd and let a finite actual negative gap word carry
\(z\) to \(-1\). Write \(\ell\) for its number of odd steps
and \(B\) for its total shortcut clock. Its affine relation is
\[
-2^B=3^\ell z+C_W.
\tag{18}
\]
For any fixed positive modulus \(M\), set
\[
q_t=-1+2M3^\ell t,\qquad
x_t=z+2^{B+1}Mt,\qquad t=1,2,\ldots.
\tag{19}
\]
Equation (18) gives
\[
2^Bq_t=3^\ell x_t+C_W.
\]
The same integrality induction proves that the inverse gap word is
legal. For sufficiently large \(t\), both ends and every intermediate
value are positive; alternatively, positivity follows successively from
each integral parent of the positive target. Every value is odd.
The word therefore gives
\[
U^\ell(x_t)=q_t,\qquad
q_t\equiv-1\pmod M,\qquad x_t\equiv z\pmod M.
\tag{20}
\]
These are actual positive ordinary trajectories with a common supplied
gap word. Negative history is used only to select finite coefficients
and residues.

A nonnegative excessive function satisfies \(P^\ell F\le F\).
Keep the single physical word in (20) to obtain
\[
F(q_t)\ge 3^\ell2^{-B}F(x_t).
\tag{21}
\]
If (3) holds at modulus \(M\), now with (14), dividing (21)
by \(q_t^pL(q_t)\) and taking a finite-word limit gives
\[
a(-1\bmod M)\ge
 (3^\ell/2^B)^{1-p}a(z\bmod M).
\tag{22}
\]
The coefficient is strictly positive for every real \(p\).

First use the \(e=1\) self-return, with positive targets
\(q=-1+6Mt\) and parents \(-1+4Mt\). Both residues are
\(-1\bmod M\), so excessivity gives
\[
a(-1\bmod M)\ge (3/2)^{1-p}a(-1\bmod M).
\]
For \(p<1\), this forces \(a(-1\bmod M)=0\). Equations
(22) and the coverage proved in Section 7.1 force every profile
coefficient on an odd residue class to vanish.

This proves the mixed-modulus extension. The companion Lean theorem
**CollatzSignedCarry.finite_signed_lift** proves the exact finite
ordinary transport and odd-count identity: instantiate its shortcut
clock with (B), signed seed with (z), and translation parameter
with (2Mt). The supplied signed history has endpoint (-1)
and odd count (ell), giving exactly (19)--(20). The negative
basin residue coverage, real-power limits, and infinite asymptotic
conclusion are written mathematics, not claims made by that Lean theorem.

## 8. Arbitrary fixed moduli via the primary arithmetic-progression theorem

There is a literature bridge from the mixed-modulus result to every
fixed modulus.

Kenneth M. Monks, *The Sufficiency of Arithmetic Progressions for the
\(3x+1\) Conjecture*, Proceedings of the AMS **134** (2006),
2861–2872, Theorem 1.1, proves arithmetic-progression sufficiency.
The author PDF explicitly states on page 2 that the same argument
applies to every negative arithmetic progression for the map on
negative integers:
[author primary text](https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf).

The imported consequence needed here is precisely:
\[
\text{every negative arithmetic progression meets the merger
component of }-1.
\tag{23}
\]
Since \(T(-1)=-1\) for the signed extension
\(T(z)=z/2\) on even integers and \(T(z)=(3z+1)/2\)
on odd integers, every such meeting is a finite actual trajectory to
\(-1\). This is not the separate scaffold \(S(z)=(3z-1)/2\)
on odd inputs. Restricting
the progression to odd integers gives a negative odd representative
in every residue class of any modulus \(M\) that contains odd
integers.

The negative extension is stated by the author, with its repeated proof
omitted. The sign requirement in the supplied proof is compatible with
this use: every admissible inverse step \(y\mapsto2y\) or
\(y\mapsto(2y-1)/3\) preserves negativity, while the modular
admissibility arguments are unchanged. This is an explicit imported
published result, not a claim that arbitrary negative orbits converge
to \(-1\); other negative cycles are permitted.

### Corollary B — no nonzero finite-period profile for any modulus

Let \(M\ge1\) be arbitrary. Suppose a nonnegative excessive
\(F\) satisfies (3) at this modulus, with \(p<1\) and (14).
Then \(a\) vanishes on every residue class containing odd integers.

**Proof.** The physical \(e=1\) self-return in Section 7.2 first
forces \(a(-1\bmod M)=0\). For any odd residue, (23) supplies
a finite negative odd history to \(-1\). The positive lift
(19)--(22) is a separate, exact elementary argument. It forces
that residue's coefficient to vanish. QED.

This corollary imports only (23) from Monks; it does not import a
Collatz convergence conclusion, an ordinary potential estimate, or
the PR180 population argument. The elementary ternary and mixed
binary–ternary versions remain independently proved above.

A bound with a resolution that grows with the target lies outside
the corollary. So does a nonzero leading profile without actual
progression limits. The unresolved critical ordinary trace is not
replaced by a periodic ansatz.
