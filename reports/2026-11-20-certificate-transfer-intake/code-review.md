# Updated certificate-transfer attachment: code audit

Status: scoped review and actual finite execution. No full Collatz proof,
universal transfer, or external referee acceptance is claimed.

## Input identity and new scope

The updated ZIP contains the eleven original code files byte for byte,
an updated README, and three new files: `problem2.py`, `conv.c`, and
`conv_dfs.c`. The fifteen original input files are hashed in
`source-manifest.json`. Supplied source bytes were not edited.

The new programs specialize to

\[
x=128m+1,\quad m\ge1,\quad4\nmid m,\qquad w=(x+1)/2=64m+1.
\]

They make certificate splicing and the reverse-transfer residual cases
concrete. Their executed tests do not discharge the universal transfer
obligation. In particular, certifying the antecedent and searching a
bounded prefix of the companion are distinct operations.

## Actual original-source runs

Each requested large run completed within its individual 45-second cap.
The C programs were compiled with `gcc -O2 -Wall -Wextra`. They only
warned about unused `argc` under these flags. Full stdout, copied from the
completed execution-tool outputs, is preserved under `original-runs`;
`execution-record.json` records commands, exit codes, transcript hashes,
and the distinction between originals and the temporary overflow audit.
No execution timestamps or elapsed durations were invented.

### problem2.py

- All 2,000 positive odd sources below 4,000 passed the certificate and
  padded-certificate tests.
- Of 15,000 eligible parameters with `m<=20000`, the bounded splice
  procedure emitted 5,215 valid companion certificates.
- The explicit odd-q family passed for 14,998 eligible values out of
  30,000 odd q below 60,000, with no reported failures.
- The three displayed rank-four cases `s=1,2,3` passed, including the
  two-transfer targets with exponents 25, 52 and 79.
- The first reported still-running examples are x=385, 897, 2305, 2433
  and 2689; all are statements about the chosen finite cut.

`cert(x)` actually follows x to 1, so its successful construction is a
finite certificate of that particular source. The splicer only explores
at most `r+60` odd steps of w, where r is the initial source certificate
length. Returning `None` is a bounded search failure, not a proof that
no merger, no other certificate, or no convergence exists. The source
certificate may be padded by valuation-two loops at 1; a claim to keep
certificate length means the padded certificate's length when padding
is needed, not an unconditional bound by the original first-hit rank.

The scalar function `holds` checks the global exponent identity. Its
mathematical sufficiency depends on strict increasing integer exponents
and the ordinary domain. The separate checker below replays every division,
positivity, exact oddness, and the final value, instead of relying only
on the scalar equation.

The two-transfer pure-power exponent `27s-2` must not be confused with
the first companion's exponent `27s-1`: the second transfer additionally
assumes that the first companion has been certified.

### conv.c, N=3,000,000

There are 2,250,000 eligible parameters. Exact counts from a temporary
output/overflow-instrumented copy are:

| x modulo 512 | Synchronized merger | Landed | Still running |
|---:|---:|---:|---:|
| 129 | 143,082 | 419,333 | 187,585 |
| 257 | 476,678 | 96,429 | 176,893 |
| 385 | 267,879 | 280,773 | 201,348 |
| Total | 887,639 | 796,535 | 565,826 |

The original output rounds these shares to 0.3945, 0.3540 and 0.2515.
It reports no sign mismatch and maximum lead 26 at m=1,657,919.

The program runs both x and w all the way to 1 to compute
`D=lam(x)-lam(w)+1`. Thus these are classifications of completed finite
trajectories, not a method proving that an arbitrary companion terminates.
Its `landed` flag includes membership of the already known cycle
{1,2,4}, not solely a first arrival at 1. In this sample, no nonmerging
case changed its flag solely through the final explicit cycle check.

The guarded copy found peak 825,525,149,213,608 (<2^50), maximum odd count
360 and maximum halving count 599. Before each odd multiplication it
checked the unsigned-128-bit overflow condition. No guard triggered.
The original 64-bit expressions `128*m+1` and `64*m+1` are also safe at
this N. Counter arithmetic is far below signed-int limits. General CLI
arguments are not validated; this safety conclusion applies to the
executed range, not arbitrary requested cutoffs.

### conv_dfs.c, depth 28, list depth 9

The conditional covered shares printed for x congruent to 129, 257 and
385 modulo 512 are 0.058833, 0.564167 and 0.220760 respectively.

**Clock conversion:** this program reads bits of `k=4m`. Its depth 28
therefore corresponds to depth 26 in the PDF's parameter m. The smaller
independent comparison at C depth 12 corresponds to m depth 10. These
depths must not be silently identified.

Each accepted leaf carries a literal affine identity with equal slopes
and constants, so it certifies every positive ordinary lift of that
residue class. The finite union has the computed dyadic density. This is
stronger than a random sample, but it is still finite-depth coverage and
does not make the remaining residue cylinders empty.

At the executed depth, the active power-of-three indices are at most 31,
all integer intermediates are far below unsigned-128-bit capacity, and
all shifts are safe. Although the initializer fills `pow3` through index
99 and wraps its unused entries from index 81 onward, those wrapped
entries are never read by this run. Dyadic masses at depth 28 are exactly
representable in binary64; the six-decimal display is rounded.

The CLI lacks bounds checks. Depths below the initial depth four, excessive
shift counts, array bounds and larger active power indices would require
separate guards. None is exercised by the documented run here.

## Independent repair and regression checker

The new repository file
`research/certificate-transfer-intake-20261120/check_certificates.py`
imports no supplied implementation, uses Python exact integers and
Fractions, and raises explicit exceptions on failure. It does not rely
on assertions that disappear under optimization. Its search returns a
literal `UNRESOLVED` status when its declared finite budget is exhausted.

The checker was executed normally and with `-OO`; both runs succeeded
and their deterministic JSON receipts are byte-identical. The receipts
are the root publisher's `science-replay.json` and `science-executions.json`, each pinning the checker's SHA-256.
Its explicit coverage includes:

- 4,000 ordinary source/padded certificate validations, and four rejected
  damaged/domain-invalid certificates.
- 1,500 reverse-transfer sources; 477 emitted certificates and 1,023
  UNRESOLVED outcomes under the stated independent budget.
- Seven symbolic all-lift affine merger families.
- The k=1 control: the two ordinary values become equal at 1 while their
  coefficient/odd counts still differ, so numerical meeting does not imply
  absorption of the canonical affine type.
- 1,000 corrected consecutive fixed-clock examples, including A=3 and A=5.
- Rank-four source and both companion identities for s=1 through 8,
  including the first companion's exact odd count and shortcut clock.
- Eight forward landing obstructions with e=6d+1, retaining a certified
  two-odd-step antecedent and an unbounded family of aligned leads.
- A complete independent partition at k-bit depth 12: 1/256, 128/256 and
  23/256 of the three classes. A separate original-C run agrees.
- Exact transition-versus-affine and ordinary-lift checks for all three
  reverse initial types through m-bit depth 10.
- Exact Fraction evaluation of DENSITY_ONE.md (16), including rational
  root enclosures and the strict constant bound C<53.335<54. This scalar
  verification does not replace the manuscript's stochastic proof.

## Earlier defect retained, not silently rewritten

The original `research3.py`, unchanged in the new ZIP, prints two failures
in its consecutive-number test and nevertheless exits zero. These occur
at A=3 and A=5 because its stored orbits stop at first arrival at 1 and
its comparison uses first occurrence of the target. Continuing the ordinary
map gives T^5(3)=T^5(2)=4 and T^3(5)=T^3(4)=4. The fixed-clock identity
survives; an equal-first-arrival claim would need exceptions.

The prior independent replay of all 100,002 eligible cases in the original
range had zero failures for the corrected fixed-clock statement. The
new small verifier preserves both boundary examples without rewriting
the original submitted script. Several original scripts print failure
counts without nonzero exit status, and some use assertions, so a blanket
claim that every original checker passes under optimization is not made.

## Mathematical status

The certificate interface, conditional splice, finite exact cylinder
identities and sampled classifications are useful and reproducible.
The density-one theorem rests on its written absorption argument, not
these finite programs. Neither density one nor any of the sampled
classifications supplies every fixed ordinary exceptional input with
a certificate. The entire first rank-four family is outside the stated
all-lift merger compiler by the accompanying separate proof; the code
here checks its stated algebra without assuming its unresolved partner
convergence.
