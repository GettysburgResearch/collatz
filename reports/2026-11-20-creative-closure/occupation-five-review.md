# Independent review of the physical five-block packet

**Result:** no material mathematical defect found in the stated C5-001--005
claims at the frozen hashes below. The paired block and supplied rank-two
family are positive local results. The recharge and long-expansion families
refute their specified controller ranks and uniform output bound. They do
not prove the physical forward-five law or full Collatz.

Reviewer: the occupation-lane agent, independently of the five-lane author.
This review reconstructs the written integer arguments and adds a separately
implemented bounded replay. It does not promote imported conditional
criteria into unconditional closure.

## Frozen artifacts

| Artifact | SHA-256 |
|---|---|
| research/creative-closure-20261120/five_closure.md | cde080ac777ab6673029fe8ed769f13f84500c23a59d5111075fb6e44e1261d6 |
| experiments/creative_five_closure.py | c72e23840297d8eac4c988c02a08d7e83129dfc53de00fa8025363ed2141b05c |
| reports/2026-11-20-creative-closure/five-report.json | 0b3cfa27a941fa43f1c9daacb484b5923dcc4537886a53c7fada19e530f32c31 |
| reports/2026-11-20-creative-closure/occupation-five-independent.py | 8b88b52d3781deb19143f01dad95e413b6d945eb78cfe8afd504a847e9d428d4 |
| reports/2026-11-20-creative-closure/occupation-five-independent-report.json | 6877b36d9aaebd4aac73e2de654214eae5e36bf4b0883cf563648e668908e103 |

The independent checker verifies the three author-artifact hashes before
running. It imports no author program or formula helper. Its own physical
step function uses the literal positive shortcut rule, and all verification
gates use exceptions active under optimized Python.

## Mathematical reconstruction

### C5-001: legal paired block and its exact scope

For an odd unit \(q\), the congruence
\(2^\ell q\equiv7\pmod9\), \(\ell\ge6\), makes
\(x=(2^\ell q-7)/9\) an odd positive integer. Reducing modulo 64 gives
\(x=64u+49\). I independently calculated all six shortcut steps:
the lower arm has odd inputs at positions 0 and 2, the upper arm at 0
and 5, with endpoints \(9u+7\) and \(5(9u+7)\). Since
\(9u+7=2^{\ell-6}q\), the remaining common steps are exactly halvings.
This proves both affine identities together with their physical legality,
not only their endpoint algebra.

The intermediate lower odd value is at least 5. The upper endpoint is at
least 5 and all earlier displayed values exceed 1. Thus the first-hit
clock additions are legitimate when the final targets are known to
converge. The actual odd division words are \((2,\ell-2)\) and
\((5,\ell-5)\); all exponents are positive on the stated domain.

The bounded unit-lift argument also checks: the six listed initial clocks
solve the modulo-nine condition. Increasing a clock by six sends its
predecessor \(x\) to \(64x+49\), so a predecessor divisible by three is
replaced by one congruent to 1 modulo three. The result remains larger
than \(q\) and has clock at most 17. In the opposite direction, on the
legal source cylinder, \(x-7(9u+7)=u\ge0\), and subsequent halvings only
decrease the odd target. The reduced target is a ternary unit because
\(9u+7\not\equiv0\pmod3\).

Consequently the local least-failed-antecedent reduction is valid on
\(x\equiv49\pmod{64}\). The note correctly does not turn the existence of
a larger inverse lift into coverage of all failed antecedents.

For two fixed words agreeing on two distinct sources, equality of affine
slopes forces equality of the shortcut clocks and odd-input counts, by
unique factorization of powers of two and three. With two odd inputs,
the constant equation is \(2^j-5\,2^i=12\). Here \(j>i\), the parenthetic
factor \(2^{j-i}-5\) is odd, hence \(i=2\), then \(j=5\).
This is a proof for all positions, independently of the bounded position
census in the production checker.

### C5-002: the supplied family closes for its stated target

At \(q=1\), the required clocks are \(\ell=6r+4\), \(r\ge1\).
The lower arm reaches 1 after its two odd steps, and the upper reaches 5
at the same clock and then follows the exact odd division exponent 4.
This gives \((2,6r+2)\) and \((5,6r-1,4)\) as claimed, with shortcut
first-hit clocks \(6r+4\) and \(6r+8\). The family is allowed to contain
source values divisible by three; the stated forward-five criterion needs
only the unit members. No inference about arbitrary depth-two sources or
the distinct companion \(2x-1\) has been inserted.

### C5-003: scalar carry identities and the exit guard

Writing \(n=10h-1\), I reconstructed the three branches directly:

- If \(3\mid h\), \(m=20h/3-1\) is odd and \(T(m)=n\).
- If \(h\equiv1\pmod3\), \(m=(160h-13)/3\) follows the five-step path
  \(m,80h-6,40h-3,60h-4,30h-2,15h-1\), ending at \(T(n)\).
  It has exactly two odd inputs and adds four to the shortcut first-hit
  clock and one to the odd first-hit clock.
- If \(h\equiv2\pmod3\), \(q=(8h-1)/3\) is odd and
  \(T^2(5q)=n\). Its ternary-unit condition is precisely
  \(h\equiv2,5\pmod9\).

The omitted residue \(h\equiv8\pmod9\) is genuinely a nonunit exit.
Even a unit exit only certifies that the five-multiple lies in the known
basin when \(n\) does. The note explicitly refuses to infer convergence
of the quotient \(q\).

During review, the phrase “all displayed values are positive odd” was
narrowed to the intended inverse endpoints; carry parameters and physical
intermediate vertices can be even. This was a wording correction, not a
change to an identity or domain.

### C5-004: the recharge occurs on known convergers

The identity \(T^3(4n+1)=T(n)\) adds exactly two shortcut clocks and no
odd clocks for odd \(n>1\). The explicit path of 19 has clock \((14,6)\).
Therefore \(s=(58\,16^a-1)/3=J^{2a}(19)\) has clock \((4a+14,6)\).

When \(a=5+243r\), integrality and
\(h=(s+1)/15\equiv13\pmod{81}\) follow from
\(v_3(16^{243}-1)=6\). Division by 45 removes two powers of three,
leaving the required modulo-81 invariance. For \(h=81v+13\), direct
substitution gives \(h\mapsto432v+69\mapsto288v+46\).
The middle value has valuation exactly one; both endpoint pairs of debts
are \((v_3(h),v_3(13h-1))=(0,1)\). The ending carry is larger.

Concatenation of the physical detour and inverse-one edge gives
\(T^6(n')=T(n)\), with three odd inputs versus one on the shorter arm.
Thus shortcut and odd first-hit clocks increase by 5 and 2. All preceding
vertices exceed one. This verifies the specified rank obstruction even
when its valuation coefficients are arbitrary signed real numbers.
It does not establish recurrence of the controller or one infinite
increasing orbit.

### C5-005: finite lifting and unbounded output ratio

The group generated by 16 modulo \(3^N\) has exactly \(3^{N-1}\)
elements, since \(v_3(16^{3^j}-1)=j+1\). It is precisely the subgroup
congruent to 1 modulo three. The target in equation (17) belongs to this
subgroup, so its exponent \(0\le a<3^{k+3}\) exists uniquely.
Modulo nine it forces \(a\equiv2\pmod3\).

The congruence then gives exact debt \(v_3(13h-1)=k\), with
\(t=(13h-1)/3^k\equiv7^{1-k}\pmod9\). The stated formula
\[
h_j=(16^j3^{k-j}t+1)/13
\]
is preserved by each legal \(L_1\) step. At \(j<k\) the next branch is
indeed \(h_j\equiv1\pmod3\), and the final carry is \(2\pmod9\).
The resulting quotient is an odd ternary unit. Combining the physical
detours and final two-step inverse gives the exact ancestor identity and
the first-hit clocks stated in (19)--(20).

Finally \(h-1/13\ge12h/13\), \(q\ge7H/3\), and \(s<15h\), so the
coefficient \(28/195\) in the output ratio is correct. This rules out a
uniform \(q\le Ks\) bound for this controller even at fixed supplied odd
depth six. It does not prove that any tested quotient converges or that
the controller always exits.

## Actual finite replay scope

The author's frozen report was replayed with:

~~~bash
python -X utf8 -B experiments/creative_five_closure.py --compare reports/2026-11-20-creative-closure/five-report.json
~~~

It passed. This is a reproduction of the author's computation, separate
from the independent checks below.

The independent program starts from the ordinary source cylinder rather
than the author's target-indexed loop. It verifies:

- 1024 source-cylinder blocks, including exact odd-input counts and
  absence of an earlier hit of 1;
- a direct search for legal unit predecessors at each of 171 odd unit
  targets through 511, using clocks 6 through 17 rather than the residue
  lookup table;
- seven supplied rank-two parameters \(1,2,7,13,26,41,80\), checking first
  hits on both arms;
- all three carry branches for \(1\le h\le1000\);
- 513 complete recharge instances \(h=81v+13\), \(0\le v\le512\), and
  the known-convergent renewal sources with \(r=0,3,7\);
- exhaustive finite multiplicative orbits for prescribed lengths
  \(1\le k\le7\), totaling 88,533 modular states, establishing the order
  and unique exponent in those finite cases independently of the author's
  ternary digit-lifting algorithm;
- complete physical ancestor paths and first-hit clocks for the first
  five lifted sources, plus exact rational output-ratio inequalities;
- the clock-five failed transfer and the explicitly nonunit exit.

No quotient convergence is tested or inferred. The independent exact
report passes both:

~~~bash
python -X utf8 -B reports/2026-11-20-creative-closure/occupation-five-independent.py --compare reports/2026-11-20-creative-closure/occupation-five-independent-report.json
python -X utf8 -O -B reports/2026-11-20-creative-closure/occupation-five-independent.py --compare reports/2026-11-20-creative-closure/occupation-five-independent-report.json
~~~

The written arguments establish the unbounded local claims and parameter
families. The finite replay checks their implementations and selected
physical instances. The sufficient implication from a full forward-five
law to Collatz remains the separately pinned PR157 theorem; this review
does not claim that its missing universal premise has been supplied.
