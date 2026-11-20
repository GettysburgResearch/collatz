# Mathematical audit of the submitted certificate-transfer PDF

Source: the 18-page PDF *Collatz certificates under x -> (x+1)/2: a
density-one theorem and the open remainder*, dated 2026-11-20.
SHA-256: `edd35e567658c48803b43e78011c81644f153fcd73112de42f991b6d4dbaf99e`.

## Narrow verdict

The central density-one theorem has a coherent complete mathematical route.
I reconstructed the certificate characterization, exact cylinder dynamics,
waiting times, embedded walk, square-root excursion contraction, finite-set
recurrence, absorption, and the conversion from Haar measure one to ordinary
relative natural density one. No fatal quantifier or measure gap was found
in that theorem. Optional stopping and visit-time charging are compressed in
the PDF and should be written with localization and conditional expectations;
the independently authored DENSITY_ONE.md does that.

This review is not external referee acceptance or formal verification. The
reconstructed manuscript retains PROPOSED status. Universal transfer is not
proved. The stronger quantitative absorption theorem already appears in
PR146 at e238c63a5d57f96bb063b7472498d1977df51951, in
research/upper-bit-mergers/THREE_RAY_UPPER.md; the submitted density-one
specialization is not a new absorption result relative to that snapshot.

## Page-specific findings

| Pages | Claim | Assessment |
|---|---|---|
| 1--3 | Certificates characterize E | Correct, with the crucial oddness qualifier: E is exactly the odd integers reaching 1. For r=0 the defining equation forces x=1. The backward terminal congruence proves each intermediate value integral; the next positive gap proves oddness; therefore each gap is the full valuation. |
| 3--4 | Starting forms, coalescent cylinders, and exponent shift | Correct. The common forms occur at shortcut clocks differing by one, with equal total odd counts. Removing the powers of two in the common endpoint proves B_i=A_i-1 and the same shift for all later certificate entries. The prior B entries are fixed by the finite cylinder; A_i itself need not be fixed, because the common endpoint's valuation can depend on its unused tail. |
| 4--5 | Signed type table and fair-bit Markov chain | Correct. For Haar-random m, the unread tail remains uniform after any finite digit history, and the driving form has odd slope. Fairness is exact for the residue population. It is not randomness of an individual fixed positive integer's future. |
| 6 | Waiting-time and embedded-walk lemmas | Correct. Equal shortcut parity histories are exactly equality modulo the corresponding power of two. The valuation formula gives the geometric tail. Move directions are fresh fair bits at stopping times determined by already exposed bits. The excursion's expected visit count is 2 per absolute height, including both signs. |
| 7--8 | Proposition 6, contraction coefficient and additive constant | Correct after spelling out bounded stopping and Fatou. The proposed nonnegative supermartingale has conditional mean multiplier at most one; the departure factor is lambda=(3-sqrt(3))/2. Suffix costs are bounded by kappa^h, kappa=sqrt(3/2)(sqrt(3)-1). Conditional entry-time charging, rather than independence of visits and holds, gives the additive series. An exact rational upper bound gives C<53.335<54. |
| 8--9 | Absorbing words | Correct, including signs in the branch delta=1 mod4: signed orientation returns the gap (3 delta+1)/4. Even gaps halve; odd magnitudes greater than one shrink; +/-1 have three-step finishing words. |
| 9--10 | Recurrence and a.s. absorption | Correct for the gap chain sampled after complete departure-and-return excursions. It must not be confused with all physical visits during zero-level holding. The drift yields almost-sure return to a finite set. Finite absorbing words from that set then give a geometric-trial proof of absorption; this also avoids relying on a terse invocation of Levy's zero-one law. No finite expected physical excursion time is assumed. |
| 9--10 | Haar-to-natural-density conversion | Correct. For each fixed depth, the absorbed cylinders are a finite union of residue classes with exactly the asserted relative natural density. Their proportions tend to one, and all lie in G, which proves lower density one. There is no interchange that would make the exceptional set empty. |
| 10 | x=129 is exceptional; grade test | The stated certificate data give iota(129)=-11 and iota(65)=3, contradicting the necessary difference of one. This establishes the example. Merely noting unequal odd counts at the first meeting would not suffice by itself, because later loops can change counts; the grade test resolves that issue. |

## Corrections to wording and evidentiary claims

1. **Page 1: "the two orbits are unrelated" is false literally.** The
   document's own exceptional pair 129,65 has two convergent orbits that
   meet. The correct statement concerns absence of a whole-cylinder affine
   identity with the specified timing and slope relation. The page-10
   sentence "no identity links the two orbits afterwards" needs the same
   qualification.

2. **Pages 1 and 10: infinitude is asserted but not proved in the supplied
   manuscript.** A single exceptional point and any finite census do not
   establish an infinite exceptional family. If an independent companion
   proof supplies this, attribute the additional result separately. This
   is not a gap in the density-one theorem, which permits an arbitrary
   nonempty zero-density complement.

3. **Page 10: "open exactly on the exceptional set" should mean the
   uniform implication over that remainder.** It is not unknown at every
   individual exceptional input; 129 and its partner are explicitly
   settled, as are many numerical examples.

4. **Pages 11--13: numerical checks do not verify every step of an
   infinite stochastic proof.** The excursion experiment explicitly
   discards runs exceeding its cap, so the reported averages are censored
   observations, not rigorous expectation bounds. The proof must carry
   the moment estimates independently, as it can.

5. **Pages 13--18: the two printed programs do not contain every claimed
   experiment or figure generator.** The appendix includes useful chain,
   waiting-time, descent, certificate, grade, and finite-enumeration
   routines, but not the displayed Proposition-6 excursion Monte Carlo,
   the certificate-tuple enumeration, or the chart-generation code.
   I visually checked page 16: some apparent indentation issues in text
   extraction are extraction artifacts, not grounds to call the printed
   code invalid. Use separately reconstructed executable files and actual
   receipts when publishing reproduction claims.

6. **Page 12's approximately 4.8 times bitlength statement is empirical.**
   It is not a universal bound on the remaining deterministic histories or
   on physical stopping time. Keep it labeled as a sampled observation.

7. **Pages 1 and 11's external verification range needs its own source.**
   It is not a dependency of the density theorem and was not independently
   reverified in this audit.

## Exact bound for the additive constant

Let r=897/1000. Rational squaring proves kappa<r and 1/sqrt(2)<708/1000.
Using nu(h)=1 for odd h and nu(h)=2+v2(h) for even h gives

S(r)=3r/(1-r)+r^2/(1-r^2)+sum_(j>=1) r^(2^j)/(1-r^(2^j)).

For j>=6, 2^j>=64(j-5), so the final series tail is at most
r^64/(1-r^64)^2. Exact Fraction evaluation of

(708/1000) * [1+2*(3r/(1-r)+r^2/(1-r^2)
 +sum_(j=1)^5 r^(2^j)/(1-r^(2^j))+r^64/(1-r^64)^2)]

is less than 54 (decimal display: 53.33442994165898). This finite scalar
check was actually executed. No Monte Carlo computation was used to
establish the expectation bound.

## Published reconstruction prepared for parent review

I authored only
research/certificate-transfer-intake-20261120/DENSITY_ONE.md
inside the requested native checkout. It retains PROPOSED status, source
hash, exact PR146 attribution, full localized proof, and the all-integer
gap. I made no commit or push.
