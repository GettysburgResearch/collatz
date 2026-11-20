# Independent review of the expanding Q returns

Reviewed the adaptive-pair packet's `EXPANDING_RETURNS.md`, `certify_expanding_return.py`,
`expanding_return_certificate.json`, and `verification_report.json` without
importing its implementation. The independent replay is
`check_expanding_return_review.py`; its output is retained in the publication
packet replay receipt. The author's standalone report was reviewed before
the files were assembled into this bundle.

**Finding:** no substantive mathematical error was found in the two affine
cylinders, finite concatenation construction, valuation-pair cycle, or
eventually periodic schedule exclusion. This finding does not establish that
an arbitrary positive source eventually triggers a least-failure guard.

## Full individual cylinders

Let M=2^38, K=3^24, D=K-M=7551629537. The reviewed maps are

$$
F(a)=\frac{Ka+610948284866}{M},\qquad
G(a)=\frac{Ka+613397164994}{M}.
$$

Their source cylinders are respectively

$$
a=210578993150+2Mu,\qquad
a=341135408638+2Mu,\qquad u\ge0.
$$

I rebuilt both physical arms `(a,3a-1)` as affine polynomials in u by applying
the literal shortcut map to their constant and slope coefficients. Every
prescribed input parity is fixed on the entire cylinder. The resulting 39
rows agree with the packet. At clock 38 the endpoints are `(b,3b-1)` with
the displayed F or G value of b. K>M and both constants are positive, hence
b>a for every positive source in either cylinder.

The canonical words agree with the actual selected-base parities, every
reported canonical state satisfies its physical affine identity, and there
is no earlier symbolic or numerical Q section in either orientation. The
independent replay checks all 74 intermediate numerical-section equations
for each macro.

For F, `v2(a+2)=12` on the **whole cylinder**, not only at u=0; for G it is 9.
Indeed the added term 2Mu is divisible by 2^39 and cannot change either
smaller valuation.

The strict minimum of the designated bad-arm margin above the original floor
`2a-1` occurs at clock 18. As affine functions of u, those margins are

$$
5745969920+15000928256u\quad(F),
$$

$$
9308401408+15000928256u\quad(G).
$$

Every even bad-arm run terminates at a fixed odd row within the 38-clock
certificate, including its endpoint. Therefore the odd-part floor guard is
also excluded on every ordinary lift; no unseen endpoint bit is used.

All 39^2=1521 independent-clock equations `X_i(u)=Y_j(u)` were checked as
affine equations. None has a nonnegative real root. This proves the absence
of such meetings for the entire ordinary cylinder, rather than merely at
sampled starting values.

## Finite concatenation and the cross-block boundary

There is an elementary construction of every finite F/G schedule, independent
of the packet's bit decoder. Suppose r blocks have been realized on one
source class modulo `2M^r`, with final good arm

$$
b=b_0+2K^r t.
$$

To append a macro whose source representative is c, solve

$$
K^r t\equiv(c-b_0)/2\pmod M.
$$

Both b0 and c are even and K is odd, so there is exactly one solution t modulo
M. This refines the initial source class to one class modulo `2M^(r+1)` and
leaves the new endpoint even. The positive least representative realizes all
the prescribed blocks; its later positive lifts do as well. Thus arbitrary
finite schedules have infinitely many ordinary positive realizations.

The local bad-arm floor bounds continue to dominate the *original* floor,
because the Q bases increase at every block. Intermediate numerical sections
are absent inside each block. Boundary sections have unchanged orientation
and a larger base.

For independent-clock meetings across different blocks, the individual
macro checks alone are insufficient. The stated large-lift argument repairs
this correctly. Relative to the original source, the slopes on the two arms
at clocks i and j are

$$
3^{q_X(i)}/2^i,\qquad3^{q_Y(j)+1}/2^j.
$$

Equality of these slopes forces i=j by unique factorization. At equal clocks
the local macro analysis already excludes a physical meeting. Every other
pair of clocks therefore excludes at most one rational source lift. A finite
schedule has only finitely many such pairs, so all sufficiently large lifts
avoid every cross-block meeting as well.

The independent code constructs 11 schedules by the modular-inverse method,
replays their full physical affine arms, and checks every cross-horizon pair
of clocks. It reproduces the packet's exact least FGFG source and its
valuation-pair cycle. In these 11 examples no nonnegative real meeting root
arises, although the general claim only needs the sufficiently-large-lift
argument above.

## Fixed-point valuations and their exact cycle

Define

$$
V_F(a)=v_2(Da+C_F),\qquad V_G(a)=v_2(Da+C_G).
$$

The domain of each macro is exactly the positive residue class where its
own resource is at least 39. The affine identity

$$
DF(a)+C_F=\frac KM(Da+C_F)
$$

gives `V_F(F(a))=V_F(a)-38`, and the analogous identity holds for G.
Consequently r consecutive legal F blocks require
`V_F(a)>=38r+1`. The weaker upper bound `r<=floor(V_F(a)/38)` in the packet
is valid; the `+1` supplies the sharp endpoint-parity version.

However `v2(C_G-C_F)=9`, and the independent FGFG construction has resource
pairs

$$
(47,9)\longrightarrow(9,47)\longrightarrow(47,9).
$$

These are actual positive ordinary sources and actual safe returns. Hence
no function of this ordered valuation pair alone can strictly decrease on
every safe macro: it would strictly decrease around a finite return to the
same pair of resource values. This conclusion concerns that state information;
it does not exclude ranks using further arithmetic data or history.

## Why eventual periodicity really is impossible

For a nonempty macro block of length r, compose its affine maps to obtain

$$
H(a)=\frac{K^r a+B}{M^r},\qquad B>0.
$$

Set E=K^r-M^r>0. Then E is odd and

$$
EH(a)+B=\frac{K^r}{M^r}(Ea+B).
$$

For a positive integer a, `Ea+B` is a nonzero integer with finite 2-adic
valuation. Each legal repetition of this block reduces that valuation by
exactly 38r. It cannot remain integral through infinitely many repetitions.
An eventually periodic schedule has a positive integer at the beginning of
its periodic tail, so the same argument excludes it. Equivalently the only
all-time 2-adic point for a purely repeated block is its negative rational
fixed point `-B/E`.

This is a universal proof for arbitrary period blocks, not an extrapolation
from the finite composite checks in the replay. It does **not** rule out an
aperiodic infinite F/G schedule at a fixed positive source. Arbitrarily long
finite schedules, the resource-pair cycle, and the eventually periodic
exclusion must not be presented as producing either an ordinary infinite
survivor or a full termination theorem.

## Review scope

The final prose review also checked precision replenishment to any prescribed
finite depth, the increase of binary length on infinitely many lifts, the
concrete convergent control, the lack of a common nonconstant affine scaling
form, and the precise limitation of a supplied known-arm clock rank. The
sorted 78-row ordering certificates and the complete supplied control orbits
were independently replayed. Both arms first reach 1 at clock 236; the first
odd-part and literal floor descents occur at 40 and 42, respectively, and the
first independent-clock meeting under the maximum-clock ordering is at
`X_65=Y_65=7710330710`.

Two wording refinements requested during review have been incorporated:

- The examples refute the unconditional numerical assertion that survival of
  exactly the listed guards forces a smaller return. They do not themselves
  refute a conditional theorem using additional full properties of an actual
  hypothetical least nonconverger.
- The general repetition theorem states `h>=1`, so its division by h is defined.

There are no outstanding mathematical corrections from this review. The
written claims preserve the distinction between whole individual cylinders,
sufficiently large lifts of finite schedules, and the remaining infinite
aperiodic case.

The independent checker accepts an optional explicit fixture path and otherwise
reads the neighboring `expanding_return_certificate.json`. It reads the fixture
and emits JSON to stdout only; it does not generate or replace science artifacts.
Normal and `-OO` runs produced byte-identical reports with SHA-256
`5a84602271059d921efe23e9de9b3f8b6a0dd8ce84aaea3d6aec91aa30db926e`.
