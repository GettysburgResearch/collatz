# Independent review of ordinary two-arm section guards

**Verdict: VERIFIED for QG1–QG4 at the final bytes below, after one wording
clarification.** The proofs establish the stated least-failure interface,
exact finite return identities, and a changing family avoiding every
fixed clock budget. They do not establish that every fixed ordinary
source eventually activates a guard. No Collatz proof is certified.

## 1. Exact files and sources

Reviewed author files are in
`/workspace/scratch/46eba7b29f50/agent-merger-next/`.

| File | Bytes | SHA256 |
| --- | ---: | --- |
| `Q_SECTION_GUARDS.md` | 15726 | `a8ce19689b31abf002c77d6696e351a1f6db781d35b4c17fb21f834bbf08494b` |
| `check_q_section_guards.py` | 11654 | `449b2ace7d92b86b707a9f8d1d6882bc3b4622b286c8e9531cbd27a94c25ced1` |
| `q_section_guards_report.json` | 1772 | `3bf13c2165566af9b95019db1f27a46590bf1f3d348918cda0006c8fe7274044` |

The original proof reviewed during reconstruction had SHA256
`f41e4defa0b02863a5b3f017d192575ec0725c4a7f031c968792fd059ace8110`.
The final paragraph after the two boxed tripling identities now explicitly
describes 25 modulo 64 and 93 modulo 128 as subprogressions within the
1 and 5 modulo 8 classes, and states that it does not cover either entire
modulo-8 class. I checked the final wording and final hash. The checker
and report were unchanged.

I inspected PR146 at exact head
`7d04c4dd756cfe495eb3eee78eba35a99085cd2a`, files
`research/upper-bit-mergers/THREE_RAY.md` and
`research/upper-bit-mergers/THREE_RAY_SMALLER.md`.
These do contain the stronger finite-exception result and the complete
7 modulo 8 smaller-comparison cover described by the new note. The
earlier head `561d48a4d3a793a59b1cdf0406062ae1a6d47515` is not substituted
for this later source.

The source also already proves that a uniform bound on ordinary edges
cannot suffice in its smaller-tripling proof graph. QG4 addresses a
different, explicitly specified two-arm/floor/section interface. Neither
the existence of fixed-clock obstructions in general nor the source's
earlier lower bound should be presented as a discovery of QG4.

## 2. QG1: the ordinary least failure and orientation

A least positive nonconverger m is odd, and m congruent to 1 modulo 4
would descend in two shortcut steps. Therefore m=2a-1 with a even and
a>=2. The value a is smaller than m and converges, while 3a-1=T(m)
does not. For every b<a, both b and 2b-1 are below m, proving Q(b).
Conversely, universal Q gives strong induction to 1. These statements
use actual ordinary components, with meetings allowed at different clocks.

All four guards have the correct orientation and quantifiers:

- The physical Y arm always has the nonconvergent component. A value,
  or its odd part, below m contradicts minimality.
- A physical meeting X_i=Y_j at independent finite clocks contradicts
  their distinct components.
- If Y_h=3X_h-1 and X_h<a, then 2X_h-1 is a positive smaller preimage
  in the bad component. This is a legitimate decrease even if Y_h itself
  is still above m.
- If X_h=3Y_h-1, the section parameter Y_h is itself bad. The useful
  threshold is oddpart(Y_h)<m, already included in the first guard.

Thus the parameter a, floor m, and physical labels cannot be replaced by
a new canonical base. This distinction is used correctly throughout.

**VERIFIED:** the least-failure description and all stated guards.

## 3. QG2: transducer, return constants, and positive translation

I derived each of the six rows by applying the literal shortcut map to
B and 3^s B+D. When D is even their parities agree; when D is odd they
differ. In the case s=0, D odd, and B odd, the even-step image of the
other arm becomes the smaller-slope base, so the orientation must flip.
The new base is (B+D)/2 and the new defect is (1-3D)/2. No other row
requires a flip. Every displayed division is integral.

For unchanged return, comparing the two physical affine forms gives
q_w=q_v and C_v-3C_w=3^q-2^h. For exchanged return, it gives
q_w=q_v+2 and 3C_v-C_w=3^{q_v+1}+2^h. The initial offset -1 in
the physical Y source is included correctly in both calculations.

The base translation C is strictly positive at every nonempty canonical
return. In the unchanged case C=0 would force both physical words to
have no odd letters, impossible because the initial parities differ.
In the exchanged case the return equation gives
3(C_v-3^{q_v})=C_w+2^h>0. It follows that an expanding affine return
has a negative real fixed point. This conclusion concerns one fixed
return word; it does not exclude a sequence of changing return words.

The thresholds at a return are consequently b<a when the base is the
good physical arm, and oddpart(b)<2a-1 when it is the bad arm. The
statement also correctly requires numerical guard checks outside the
symbolic return state.

**VERIFIED:** the exact synchronized transducer, return identities,
positive translation, and scope of the affine fixed-point observation.

## 4. QG3: finite returns and smaller-tripling implications

All five short return rows have the stated source cylinder, affine base
map, and orientation. For the two new tripling implications, the actual
one-step conversion for odd n is
T(n)=a=(3n+1)/2 and T(3n)=3a-1. The 01100 return at n=25+64u gives
b=11+27u=(3(7+18u)+1)/2. The 001100 return at n=93+128u gives
b=20+27u=(3(13+18u)+1)/2. Thus the two displayed equivalences, including
their reverse directions, follow from ordinary component preservation.
Both comparison parameters are strictly smaller for every u>=0.

The longer return family has exchanged orientation. Its bad physical
arm is b=163957+177147u, and
2a-1-b=78662+84997u>0. Therefore b>a is not a counterexample to the
least-failure guard. For the appended return restricted to
a=121310+1048576u, the value b=122968+1062882u is even and larger than
a, but still smaller than 2a-1. This is another valid guard success.

For a=4, the physical pair is indeed (1,1) at clock 10 while its
symbolic state is (1,-2), and it never makes a later canonical section
return. There is already an independent-clock meeting X_0=Y_8=4,
and the first synchronous meeting is at clock 9, at value 2. The note
does not claim clock 10 is the first meeting. This example correctly
shows why physical equality cannot be replaced by symbolic absorption.

**VERIFIED:** all return formulas and the two specific smaller classes.
The final wording now avoids suggesting that every member of the two
larger modulo-8 classes has been covered.

## 5. QG4: literal finite paths, floor, and no meetings

For H>=3, t>=1, and N=2^H t, the formulas are literal ordinary paths
through output clock H. The powers 2^{H-j} ensure that every input
parity before that clock agrees with the claimed negative reference
pattern. No parity beyond the final output is assumed.

The three bad-arm coefficient classes are respectively
3(9/8)^r, (9/2)(9/8)^r, and (9/4)(9/8)^r relative to N.
Subtracting m=2N-5 gives the claimed positive lower bounds N-2,
(5/2)N-5, and N/4. These prove the raw physical floor for all t>=1.

The independent-clock proof covers small parameters as well as large
ones. The good values X_0 through X_3 lie below m. If i>=4 and
X_i=Y_j, the equation P_i-R_j=1-c_j has right side -6, -9, or -4.
For j>=2 the indicated ternary divisibilities exclude it. For j=0,
the reduced bracket is -7, -5, then positive from i=6 onward; its
positive integer multiple cannot equal -2. For j=1, the bracket is
-5, -7, -5, then positive from i=7 onward; its positive integer
multiple cannot equal -1. This verifies the claim for every H,t in
the theorem, without adding a large-t assumption.

The numerical simultaneous section exclusions also hold for actual
values, separately from the affine state. For Y_j=3X_j-1, the equation
R_j-3P_j=c_j-4 is impossible modulo 9 for j>=2; j=1 would force N=2.
For X_j=3Y_j-1, the equation P_j-3R_j=-3c_j is impossible modulo 9
for j>=3; the remaining equations are 13N=30 and 2N=5. All are
excluded on N>=8.

**VERIFIED:** the raw floor, all independent-clock meetings within the
horizon, both numerical simultaneous-section orientations, and the
corresponding symbolic nonreturn/nonabsorption statements.

## 6. The endpoint parity restriction is necessary

The unqualified all-H theorem is not an odd-part-floor theorem. For
H=3 and t=1, a=6, m=11, and Y_H=20, so
oddpart(Y_H)=5<m although Y_H>m. I independently replayed this exact
counterexample to the stronger unqualified interpretation.

The stated restriction repairs it: t must be odd for H congruent to 1
modulo 3, and even for H congruent to 0 or 2 modulo 3. This makes Y_H
odd. Every earlier even bad-arm value has its next output odd within
the checked horizon, so its odd part is one of the values already
proved above m. Thus the strengthened odd-part assertion is correct
on exactly the stated sufficient domain.

The additional endpoint-parity families are not asserted to form one
nested infinite ordinary witness. For example H=4 requires v_2(a+2)=4,
whereas H=5 with its parity restriction requires v_2(a+2)>=6. These
requirements cannot hold at one source. The signed completion statement
instead concerns the original compatible classes a=-2 modulo 2^H.

**VERIFIED with this essential domain restriction retained.**

## 7. Signed completion and the fixed-source boundary

The signed pair starts at (-2,-7). Its first arm reaches -1, while the
other runs on -7,-10,-5. I reconstructed the initial canonical states
and the three-state defect formula after clock 8. The latter has
exchanged orientation, exponent r+1, and positive defects
5*3^{r+1}-1, 7*3^{r+1}-1, and 10*3^{r+1}-1. The canonical parity
code is exactly 0 followed by seven ones and then repeating 110.

The agreement a=-2 modulo 2^H gives the same physical parity prefixes
and canonical states through H. An ordinary integer in all these
original binary classes must be exactly -2, and the positive least
representatives tend to infinity. No exchange between changing finite
positive sources and one positive all-time source is made.

This excludes a uniform fixed synchronized clock budget for the stated
guards, including finite independent-clock meetings. It does not exclude
an adaptive unbounded terminating procedure or an additional ordinary
argument after a source departs from this code.

## 8. Independent arithmetic and code audit

I inspected the author's checker and ran both normal and `-OO` modes.
Their outputs and the frozen report were byte-identical. The replay
covered 1,520 horizon cases through H=192 and 296,400 literal physical
edges, with 696 parity-qualified odd-part cases. The set intersections
exclude all 19,319,960 counted clock pairs; that count describes pairs
excluded, not the number of pairwise comparisons executed. The seven
return certificates, 512 smaller-tripling cases, orientation examples,
signed controls, and six rejected corruptions also passed.

For an independent implementation, I did not import the author's
transducer. I followed the literal physical arms and their two affine
forms, recovered the canonical exponent by comparing their slope
powers of three, and used the previous orientation only to break an
equal-slope tie. This verified 940 horizon cases through H=96,
93,060 literal edges, 438 parity-qualified odd-part cases, 35 return
word cases, 200 expansion/orientation controls, and 151 signed states.
It separately retained the H=3,t=1 odd-part counterexample and the
independent/synchronous clock distinction at a=4.

The independent evidence files in the reviewer's staging directory are:

| File | Bytes | SHA256 |
| --- | ---: | --- |
| `check_q_independent_review.py` | 7809 | `3b23ee4759a5d25a4a0290581923f5faa8491ec20eaaa0ccf832293c617ef7ae` |
| `q-independent-review-report.json` | 807 | `8d4224a8fcb7048b17b6fd4faae794a29a3835cdb94313e99015b176b4e0d6a1` |

The written elementary arguments establish the unbounded quantifiers.
These finite runs support arithmetic implementation correctness and do
not establish universal guard success.

## Final boundary

No remaining arithmetic or scope gap was found in the final QG1–QG4
claims. The open step is still to prove that every fixed positive even
source eventually activates a legitimate guard, or to supply a different
global closure. Neither the return transducer nor the finite-horizon
family proves that assertion. The source comparison, endpoint domain,
physical orientation, and signed-versus-ordinary distinction must remain
attached when the packet is integrated.
