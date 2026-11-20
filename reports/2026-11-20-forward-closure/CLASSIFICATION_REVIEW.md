# Independent audit: persistent classes and the exact closure boundary

**Verdict: VERIFIED WITH ONE DOMAIN CLARIFICATION.** This review is
independent of the root and merger agents' derivations. It concerns the
two files below as read during this turn, not later edits or the whole
repository.

- PERSISTENT_DEFECT_CLASSES.md:
  SHA-256 90b0974909e24030bade3c412491fc1632767df1496eb3557441d3c7d8698764
- AUDIT_FORWARD_DEFECT.md:
  SHA-256 a0b2710c8361a32e3d690dc4de17a8174be4d894e62fce2f1a2c02af3ecc483b

Both were read from
/workspace/scratch/c6766c1207a3/collatz_work/merger_next/.

## Persistent stopping-defect classes

The cocycle kappa(n)=d(n)-2a(n) is exact at 1 and 2 as well as before the
first hit. Equal kappa implies equal parity of the first-hit clocks, so
the two eventual cycle positions and accumulated odd counts agree at every
sufficiently large common clock. Conversely, an equal augmented state gives
equal kappa. This validates the basin-restricted synchronization theorem
and the identification of persistent convergers with the least H-member
of their defect class.

The nonnegative minima follow from the exact product
n/2^kappa=product 4u/(3u+1). A nonempty odd-input product has a last odd
input at least five, contributing at least 5/4. Equality is possible only
for initial doublings of five. Thus the claimed even classes, odd classes
at least three, and exceptional class m_1=7 have the stated minima.

The negative-defect first-hit inequality has the correct strict sign:
2^d>3^a n and a=(d-kappa)/2 give equation (7). The optional sub-two inverse
path hypothesis produces arbitrarily negative odd H-members; the +2
doubling operation and one +3 sibling operation then cover every integer
defect. The input remains source-qualified. No unconditional existence of
all negative classes was inferred.

The Fibonacci estimate is valid for the full shortcut map. A target
divisible by three has one predecessor at every depth. Targets 1 mod 3
have only the doubling branch; targets 2 mod 3 have the doubling branch
and one odd branch. This gives the stated recurrences and
N_j(1)+N_j(2)<=F_{j+3}. The bound applies to all sources first hitting one
by j, hence also to the selected diagonal rows. Synchronization with a
row already on the cycle only changes the hitting-clock bound by at most
one. Dyadic padding preserves the relevant clock margin.

This review checks the local algebra using the quoted PR146 filter and
tail criterion. It does not re-audit the external PR146 result or the
external UQ(6) input.

## Closing-bound equivalence

For a **positive odd unit** t in the basin of one, concatenation of its
reversed first-hit path with any legal inverse word at t gives
W(1)>=W(t)+8a(t)-5d(t). Therefore W(1)<infinity forces W(t)<infinity and
gives (A). The paragraph before (A) should explicitly say positive odd
unit, matching the inverse-word argument and the claimed global domain.
An even-unit extension is also true, but needs the additional observation
W(2x)<=W(x)+5.

I independently replayed the eleven odd unit inputs below 33 and checked
2^(5d-8a-1)<=t^5 whenever 5d-8a>1. The table and additive constant one
are correct. Positive R drift down to the first t<33 then proves
W(n)<=5 log_2 n+W(1)+1 on every odd unit in the actual basin.

Consequently all the proposed global closing bounds are equivalent to
the conjunction of Collatz and W(1)<infinity. This includes the
critical-height bound with constant error and the loglog bound with
coefficient 1/4: each implies Collatz and finite W(1), while the conjunction
gives the coefficient-five bound and hence every displayed larger
right-hand side after adjusting its constant.

This does not establish whether Collatz alone implies W(1)<infinity.
Nor does W(1)<infinity alone control a hypothetical disjoint
nonconvergent component. These two limitations remain explicit.

The arithmetic addendum has been amended to describe **larger allowable
error terms**, rather than logically weaker existential hypotheses, and
links the forthcoming CLOSURE_BOUNDARY.md.
