# Independent review of the ordinary certificate-carry note

Reviewed mathematical note, before its documentation-only PROPOSED heading
was normalized for publication:
`research/ordinary-basin-closure-20261120/CERTIFICATE_CARRY.md`.
This is an agent-level independent algebra and implementation review, not a
formal proof-assistant verification or promotion of source status.

**Finding: no substantive mathematical error found.** The universal identities,
stated clocks, depth-two classification, growth lower bound, and necessary
division budget are valid with the hypotheses stated in the note. The positive
two-state grammar is a terminating partial transformer; its unhandled carries
remain unproved. In particular the terminal Mersenne branch cannot be accepted
merely because the original source certificate terminates at one.

## 1. Universal carry and the merger clocks

For positive odd z and k>=1, the first k-1 accelerated gaps from 2^k z-1 are
exactly one. The jth state before the last step is
3^j 2^(k-j) z-1. The last odd numerator is 2(3^k z-1), giving
U^k(2^k z-1)=oddpart(3^k z-1). All quantities are positive. Substitution of
x=(2^a z-1)/3 gives equation (2) without dropping its constant carry.

When a>=2, x is 1 modulo four. Then U(2x-1)=(3x-1)/2 and U(4x-1)=6x-1;
their next odd iterates both equal oddpart(9x-1). Also
U(2x-1)=2^(a-1)z-1. Therefore the stated merger clock identity

    U^a(4x-1)=U^(a-1)(2^(a-1)z-1)

already follows by taking a-2 further steps from the common two-step endpoint.
This verifies both the a=2 edge case and every a>=3 case.

For consecutive source gaps (1,1), z=(3x+1)/2 and w=(9x+5)/4. The actual
first target step is (3x-1)/4=(w-2)/3, and its next odd numerator is w-1.
Hence U^2(2x-1)=U(2z-1)=oddpart(w-1), at exactly the stated clocks.

For source gaps (1,b), b>=3, substitution gives
U(2x-1)=(2^(b-2)w-1)/3, a positive ordinary inverse of w with exact gap b-2.
Thus the A-state absorption occurs in two target odd steps. For B, the first
two target steps give 2^b w-3. At b=3 its next odd part is oddpart(3w-1).
At b>=4 its next state is 3*2^(b-3)w-1, after which the universal carry formula
gives U^b(4x-1)=U^(b-2)(2^(b-2)w-1). The stated B-state clocks are correct.

## 2. The unresolved denominator is real

For gaps (1,2), the exact target is oddpart((w-1)/3), so replacing it with
oddpart(w-1) would change the ordinary component. If
B_d(z)=oddpart((z-1)/3^d), then substituting I_2(w) multiplies the numerator
by four and increases the ternary denominator by three. Oddpart removes only
the four, establishing B_d(I_2(w))=B_(d+1)(w).

For a later b>=3 at terminal suffix w=1, integrality is precisely
3^(d+1) | 2^(b-2)-1. The order of two modulo 3^(d+1) is 2*3^d, so the
equivalent condition 2*3^d | b-2 is correct. It imposes a congruence; it does
not establish convergence of the resulting positive quotient.

## 3. Exhaustive depth-two family

Every x=1 modulo 16 has first accelerated gap exactly two. If U^2(x)=1,
with second gap b, then

    x=(2^(b+2)-7)/9.

The powers of two modulo nine have period six and hit seven exactly at
exponents 4 modulo six, so b=6r+2. The r=0 case is x=1 and has first hitting
depth zero. Every r>=1 is positive, is 1 modulo 16, has an intermediate value
strictly above one, and therefore has first hitting depth exactly two.

Writing h=6r+1, the companion has two initial gaps exactly two and reaches
2^h-1. After h-1 further odd steps it is 2*3^(h-1)-1; one more step is
(3^h-1)/2 because h is odd and v2(3^h-1)=1. Both are above one, as are all
earlier states. The lower bound h+3 for its first odd hitting depth is thus
valid, with no assumption that it actually hits one.

The displayed peak formula is just 9x+7=2^(h+3). Its ratio to x grows like
(3/2)^h. If a finite target certificate has m odd steps and total valuation S,
telescoping the exact odd map gives

    2^S = (2x-1) 3^m product_j (1+1/(3n_j)) > (2x-1) 3^m.

Since m>=h+3 and the source budget is h+3, the claimed limiting lower ratio
1+log_2(3) follows. It correctly rules out direct certificate transformations
that preserve or lower either of those two budgets on this family.

## 4. Regression scope

`check_certificate_carry_review.py` is separate code using the actual map U;
it does not import the sibling generator. It checks the stated equalities on
positive inverse-source families, both delicate clock identities, the (1,2)
carry, ternary denominator transport, the exact terminal divisibility test,
and the first twelve depth-two family members through their proved forced
prefixes. It does not follow those Mersennes indefinitely or claim all-source
coverage. The universal conclusions above come from the algebra, not the
finite replay.
