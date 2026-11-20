# Expanding ordinary Q returns, finite schedules, and the exact repetition budget

**Status: PROPOSED. Written finite-word and infinite-cylinder proofs; no Collatz proof.**

This packet attempted to close the ordinary adaptive-pair descent in
`research/global-rigidity-20261120/Q_SECTION_GUARDS.md` at PR156 commit
`c5cb84502c7289705d59a8781a65fd845b9b6b14`. The prospective numerical lemma was:
every canonical first return which survives all the stated earlier physical
guards must decrease the returned demand. The two explicit ordinary cylinders
below disprove that unconditional guard-only lemma. They also show why
consuming one negative shadow's binary
precision does not give a resource which survives a change of return word.

The positive conclusion is an exact finite repetition budget for each fixed
expanding return, and for every fixed periodic block of returns. Every finite
schedule of the two displayed returns has positive ordinary realizations;
no fixed positive source can realize an eventually periodic infinite schedule.
The exclusion of every fixed positive aperiodic infinite schedule is not proved.

## 1. Definitions and the physical floor

Use the shortcut map

$$
T(n)=\begin{cases}n/2,&n\text{ even},\$3n+1)/2,&n\text{ odd}.\end{cases}
$$

Write `Q(a)` for eventual merger of `a` and `3a−1`. Put

$$
X_j=T^j(a),\qquad Y_j=T^j(3a-1),\qquad m=2a-1.
$$

For a hypothetical least nonconverger `m`, the first physical arm is in the
component of 1 and the second is not. The designated bad arm and the original
floor remain fixed throughout. The guards under consideration are:

1. `oddpart(Y_j)<m`;
2. a meeting `X_i=Y_j` at independent finite clocks;
3. a same-orientation numerical section `Y_j=3X_j−1` with `X_j<a`;
4. a reversed section whose bad base has odd part below `m`.

An affine canonical state is `(B,3^s B+D)` with an orientation bit recording
which physical arm is `B`. A canonical Q return is `(s,D)=(1,−1)`.
All returns below have unchanged orientation. The sources constructed here
are positive test sources, not asserted nonconvergers.

## 2. Two first returns which survive the complete stated guard interface

Set

$$
M=2^{38}=274877906944,\qquad
K=3^{24}=282429536481,\qquad
d=K-M=7551629537>0.
$$

The two return maps are

$$
F(a)=\frac{Ka+c_F}{M},\quad c_F=610948284866,
\qquad
G(a)=\frac{Ka+c_G}{M},\quad c_G=613397164994.
$$

Their safe ordinary cylinders, with `u` any nonnegative integer, are:

| Return | Source `a` | Returned base `b` |
|---|---:|---:|
| F | `210578993150 + 549755813888 u` | `216364159964 + 564859072962 u` |
| G | `341135408638 + 549755813888 u` | `350507308538 + 564859072962 u` |

The canonical-base parity words are respectively

```text
F: 01111111110101110011011011101111110000
G: 01111111101110110011011011101111110000
```

These digits refer to the canonical base, which may exchange physical arms
inside a word. They must not be treated as the parity word of one fixed arm.

**Theorem 1.** On each complete cylinder in the table:

- the first positive canonical Q return is at clock 38, with unchanged orientation;
- `X_38=b` and `Y_38=3b−1`;
- `b>a`, so this return does not produce a smaller Q parameter;
- `oddpart(Y_j)>2a−1` for every `0≤j≤38`;
- `X_i≠Y_j` for every `0≤i,j≤38`;
- neither numerical orientation is a Q section at any clock `1≤j<38`.

Consequently this is an actual failure of the unconditional guard-only
first-return descent lemma, including its orientation-aware and oddpart versions. It is
not merely an increasing scalar coordinate caught by an earlier physical
descent.

The cylinders do not themselves refute a conditional theorem that uses
additional properties of an actual hypothetical least nonconverger. In
particular the concrete convergent control is not such a nonconverger. What
fails is the asserted numerical descent from precisely the listed guard
survival conditions alone.

### Proof by explicit affine certificate

Represent a value as `(c,q)`, meaning `c+qu`. Every slope through clock 38 is
even, so its parity is independent of `u`. A single exact ordinary step is

$$
(c,q)\longmapsto
\begin{cases}
(c/2,q/2),&c\text{ even},\\
((3c+1)/2,3q/2),&c\text{ odd}.
\end{cases}
$$

Starting from `(a,3a−1)` with either displayed affine source, this recurrence
gives the 39 rows recorded in `expanding_return_certificate.json`.
The final rows are exactly the displayed `b,3b−1`. Independently applying
the PR156 canonical transducer to each row verifies the given canonical word,
the final state `(1,−1,0)`, and the absence of any intervening return or
affine absorption.

The floor is `(2A−1)+4Mu`, where `A` is the source intercept in the table.
Subtracting it from each bad-arm row gives positive constant and positive
slope. For each macro, both coordinatewise minima occur at clock 18:

$$
\begin{array}{ll}
F:&Y_{18}-(2a-1)=5745969920+15000928256u,\\
G:&Y_{18}-(2a-1)=9308401408+15000928256u.
\end{array}
$$

Thus all bad-arm values are above the floor. The last bad-arm row is odd for
every `u`; each preceding even run ends at an odd row already present in the
certificate. The odd part of every bad-arm row is therefore another checked
row. This proves the stronger oddpart claim without presuming any unseen
endpoint parity.

For meetings, sort all 78 affine rows `X_0,...,X_38,Y_0,...,Y_38` by their
constant coefficients. On each cylinder all constants are distinct and the
corresponding slopes are nondecreasing in this same order. Hence the order
is strict for every real `u≥0`, excluding all 1,521 independent-clock
cross-arm equalities at once. The exact ordering is stored as
`joint_strict_order` in the certificate summary. The verifier additionally
checks all 1,521 equations directly: every difference `c+qu` has `c≠0`
and either `q=0` or the same sign for `c,q`.

For each of the 37 intermediate clocks and each orientation, the section
equation is again `c+qu=0`. Its constant is nonzero and its slope is zero
or has the same sign. These 74 exact sign checks exclude every nonnegative
real root, including isolated numerical sections invisible to the canonical
state. Finally `K>M` and `c_F,c_G>0` imply `F(a)>a` and `G(a)>a` for
every positive input. This proves every assertion. ∎

The certificate is a finite list of explicit affine identities and signs,
not a test over a finite range of ordinary source integers. Replacing a row,
word, claimed minimum, or affine offset is rejected by the verifier. No
floating-point comparison is used in the certificate validation.

### A convergent positive control

For the concrete source `a=210578993150`, both physical arms reach 1 at
shortcut clock 236. Their first independent-clock meeting when minimizing
the maximum of the two clocks is

$$
X_{65}=Y_{65}=7710330710.
$$

The first physical oddpart descent below the original floor occurs at clock
40; the first literal bad-arm descent occurs at clock 42. The entire exact
orbits to 1 are stored in the certificate. Thus the first-return obstruction
already occurs for an explicitly convergent positive source.

## 3. A fixed negative shadow can be exited, then replenished

For every source in the F cylinder,

$$
v_2(a+2)=12.
$$

This follows from `v2(210578993152)=12` and the source stride `2^39`.
But its returned base is `b=216364159964+2Ku`, so

$$
\frac{b+2}{2}=108182079983+Ku.
$$

Since `K` is odd, for each prescribed `N≥1` one can choose arbitrarily large
nonnegative `u` making `v2(b+2)=N`: solve one linear congruence modulo `2^N`
which gives valuation exactly `N−1` to the right-hand side. All these sources
remain in the full safe cylinder of Theorem 1.

Therefore departure from one finite `−2` shadow does not make its binary
precision a decreasing resource across Q returns. An increasing ordinary
return can replenish that precision to any finite prescribed depth.

Binary length also fails as a decreasing coordinate. Since `K/M>1`, the
interval of parameters for which `a<2^k≤b` has length tending to infinity
as `k→∞`. Hence infinitely many members of this same cylinder increase
binary length at the return. One may additionally impose any fixed congruence
giving a desired `v2(b+2)`; the admissible parameter interval still eventually
contains members of that congruence class.

## 4. Every finite schedule of F and G is ordinarily realizable

The full binary classes for the 38-step words, before requiring an even
returned base, are

$$
a\equiv r_F=210578993150\pmod M,
\qquad
a\equiv r_G=66257501694\pmod M.
$$

At `r_F` the returned base is `216364159964`, which is even. At `r_G`
it is `68077772057`, which is odd. Thus imposing an even returned base
recovers precisely the two safe cylinders of Theorem 1: the F lift parameter
is even, while the G lift parameter is odd.

**Theorem 2.** For every finite word `w` of length `r≥1` over `{F,G}`,
there is one residue class of initial sources modulo `2M^r` on which the
specified `r` ordinary canonical returns occur, every block lies in its safe
cylinder, and the final base is even. This class contains arbitrarily large
positive integers. All designated bad-arm values and odd parts through
clock `38r` exceed the original floor. For all sufficiently large positive
lifts, there are no independent-clock cross-arm meetings through that clock.

**Proof.** A parity prefix of length `38r` fixes one source class modulo
`M^r`. More explicitly, suppose the first `j` return domains are imposed.
Varying the still free next block of 38 original source bits changes the
current base by `K^j` times that free block. Since `K` is odd, this is
invertible modulo `M`; exactly one next block places the base in the next
prescribed residue `r_F` or `r_G`. This proves the one-class claim inductively.

After the `r` words, one further binary lift flips the final base parity,
again because its coefficient is odd. Requiring that base to be even gives
one class modulo `2M^r`. Every earlier base is even because the next prescribed
source residue is even. Each block therefore belongs to the corresponding
safe cylinder. Taking an arbitrarily large positive representative supplies
a positive ordinary realization. All return bases strictly increase, because
both affine maps have slope greater than one and positive offset. Theorem 1
then places every bad-arm value and odd part above its block's floor, hence
above the original, smaller floor.

Cross-block meetings need a separate argument. With the final free lift
parameter, an X endpoint at clock `i` has a slope of the form
`3^p 2^(38r+1−i)`, and a Y endpoint at clock `j` has slope
`3^(q+1) 2^(38r+1−j)`. Equality of slopes forces `i=j` by unique factorization.
At equal clocks a macro's canonical state excludes equality of both slopes
and offsets. Thus no cross-arm equation is an identity in the lift parameter.
Each of the finitely many equations excludes at most one real lift; taking
the lift larger than every nonnegative root avoids all of them. This proves
the asserted sufficiently-large-lift statement. It does not assert that
per-block checks alone exclude cross-block meetings. ∎

The theorem concerns varying finite sources. It does not use compactness to
produce one positive source for an infinite schedule.

## 5. Exact finite repetition budgets for a fixed positive source

**Theorem 3 (one affine return).** Let

$$
H(a)=\frac{Aa+C}{2^h},\qquad h\ge1,\quad A\text{ odd},\quad A>2^h,\quad C>0,
$$

and put `L(a)=(A−2^h)a+C`. If a fixed positive integer `a` admits `r`
successive integral applications of this same return, then

$$
2^{hr}\mid L(a),\qquad
r\le\left\lfloor\frac{v_2(L(a))}{h}\right\rfloor.
$$

**Proof.** Direct algebra gives `L(H(a))=(A/2^h)L(a)`. After `r`
applications, `A^r L(a)/2^(hr)` is an integer. Since `A` is odd,
`2^(hr)` divides `L(a)`. For positive `a`, the integer `L(a)` is strictly
positive, so its binary valuation is finite. ∎

For F the sole compatible constant-word infinite 2-adic source is

$$
a_*=-\frac{610948284866}{7551629537}<0.
$$

No fixed positive source follows that word forever. Theorem 2 nevertheless
gives arbitrarily deep finite repetitions at varying positive sources. The
certificate contains concrete positive sources for one through four repeats.

For the two safe cylinders the budget can be sharpened to an exact exit
time. Each safe domain is precisely `v2(L_F(a))≥39` or `v2(L_G(a))≥39`,
respectively: the corresponding affine linear form has odd slope, and its
unique zero class modulo `2^39` is exactly the listed safe source class.
Each application decreases that valuation by 38. Thus, for a positive even
source, the exact number of consecutive safe F blocks is
`floor((v2(L_F(a))−1)/38)`, and analogously for G. This is an exact
source-dependent finite exit theorem for either fixed macro, not a theorem
that exit from that macro triggers an ordinary descent.

**Corollary 3.1 (every eventually periodic F/G schedule).** No fixed positive
source can realize an eventually periodic infinite schedule of these two
ordinary returns.

**Proof.** Compose one repeated period of length `s`. The composite has
form `(K^s a+C_w)/M^s`, where `C_w` is a positive integer. Its slope is
greater than one. Apply Theorem 3 to that composite and to the positive
ordinary base at the beginning of the periodic tail. The repetition bound
is finite. ∎

This is a fixed-source theorem. It does not exclude aperiodic infinite return
schedules or prove that every adaptive ordinary pair eventually returns.

## 6. Why the two individual valuation resources do not survive switching

Write

$$
L_F(a)=da+c_F,\qquad L_G(a)=da+c_G.
$$

Their constant difference is

$$
L_G-L_F=c_G-c_F=2448880128,\qquad v_2(c_G-c_F)=9.
$$

If an F block is followed by a G block, then at its output `b` the G
domain gives `v2(L_G(b))≥38`. Therefore `v2(L_F(b))=9`. The identity
`L_F(b)=(K/M)L_F(a)` forces `v2(L_F(a))=47`, while
`v2(L_G(a))=9`. The same argument with F and G interchanged applies at a
G-to-F switch.

Take an ordinary realization of the finite schedule `F,G,F,G`, which exists
by Theorem 2. At its first three bases the valuation vectors are exactly

$$
(v_2 L_F,v_2 L_G):
\quad(47,9)\longmapsto(9,47)\longmapsto(47,9),
$$

while the bases strictly increase at both steps. These exact vectors are
also replayed in the certificate.

Consequently no function of these two valuations alone can be a strictly
decreasing rank for every allowed F/G return. Adding a term which strictly
increases with ordinary height to any function of these two valuations
cannot repair that rank: over the displayed two-step path the valuation
vector returns to its starting value and height increases. This assertion
does not rule out ranks using additional arithmetic data, orientation,
the full certificate history, or a different form of height dependence.

There is also no nonconstant affine linear form that scales by `K/M`
under both returns. If `L(a)=pa+q` with `p≠0` had that property, comparison
of constants would require simultaneously `q/p=c_F/d` and `q/p=c_G/d`,
which are different. This explains algebraically why the single-word
valuation identity is not a common invariant for the two-word menu.

## 7. The known physical arm gives a finite clock rank, with a precise limit

In a hypothetical least-counterexample argument, `a<2a−1` already reaches
1. Let `tau(a)` be its actual first hitting time. Recording the original
physical X arm gives a decreasing remaining clock rank until it reaches 1,
regardless of canonical orientation changes. For these unchanged 38-step
returns, every block consumes exactly 38 clocks of that supplied certificate.
Thus a fixed known-convergent first arm cannot perform infinitely many such
increasing returns.

This does not turn the rank into a successful selector. Once the known arm
is on the `1,2` cycle, the remaining designated bad arm is still the original
unresolved convergence problem. A process may enter a region with no further
Q sections at all. Proving that the finite known-arm certificate forces an
ordinary merger or a bad-arm descent is the missing closure; the mere
exhaustion of that certificate's clock budget does not establish it.

## 8. Verification and scope

Run:

```bash
python certify_expanding_return.py
```

By default the standard-library verifier reads the committed JSON fixture,
validates its physical affine trajectories,
independently checks every canonical-state relation, checks all 1,521
cross-arm equations per macro and all 74 intermediate numerical section
equations, verifies every oddpart endpoint, constructs finite return schedules,
checks the repetition resource and alternating valuation cycle, and records
the concrete convergent control. It compares the supplied fixture with an
independent exact reconstruction and prints its report to stdout. It rejects
deliberately corrupted affine rows, words, claimed margins, offsets, literal
control orbits, and finite-schedule witnesses. The default run does not modify
the fixture or write a report file. Explicit regeneration is available only
with `python certify_expanding_return.py --write-certificate`.

Files:

- `expanding_return_certificate.json`: all exact affine rows, finite schedule
  witnesses, sorted-order certificates, and concrete orbits to 1;
- `certify_expanding_return.py`: exact arithmetic certificate replay;
- `check_expanding_return_review.py`: separate physical-map and modular-inverse
  reconstruction, which does not import the author's verifier;
- `run_checks.py`: the normal/optimized replay bundle; publication receipts are
  stored under `reports/2026-11-20-ordinary-basin-closure/`.

The exploratory discovery search used floating-point pruning. None of that
pruning is used by a proof or final certificate; all published decisions are
reconstructed with exact integers.

The universal results proved here are finite-word realizability, the exact
single-period repetition bound, and impossibility of positive eventually
periodic schedules in this two-macro system. A complete source-dependent
successful Collatz selector, a universal fixed-source section-avoidance
exclusion, and an aperiodic switching invariant remain unproved.

[TWO_MACRO_NORMALIZATION.md](TWO_MACRO_NORMALIZATION.md) pursues that last
arithmetic issue. It reduces the two-macro subsystem exactly to a ceiling-map
orbit constrained to two consecutive remainder values. That further attack
also does not prove all-source termination; in the intended least-failure
argument, permanent section avoidance remains even if this restricted
subsystem is independently settled.
