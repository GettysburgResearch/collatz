# Independent review of local affine certificate membership

**Mathematical verdict: VERIFIED on the stated convergent, positive-integer
slope domain, after one explicit domain clarification.** This is an
independent proof reconstruction by a separate agent, not formal
proof-assistant verification or universal convergence evidence.

## Reviewed scope and bytes

The proof is `agent-merger/LOCAL_CERTIFICATE_GRADE.md`, 8,754 bytes,
SHA-256
`d42cac3e95fd2e4cc489491e0cba799ce302cd62618b4f0b35c9df47e0fac5c0`.
The reviewed mathematical claims are LC-1, LC-2, and LC-3, including the
cocycle G1 and constructor G2--G3.

At the root agent's request, I clarified "positive slopes" to "positive
integer slopes" in the definitions. The nonnegative valuations and
ordinary congruence argument need this intended domain. No other proof
text was altered in this review.

The initially inspected checker is `check_local_certificate_grade.py`,
8,192 bytes, SHA-256
`509b2f55c0bb4271c720a6bfbac7073c98d23e9571facd9bb683853e0036f540`.
Any subsequent checker-domain tightening needs its own byte pin below.

## 1. Necessity at a common endpoint other than 1

For a fixed legal shortcut word, its endpoint is affine in the original
parameter, with slope `a_i 3^q_i / 2^l_i`. A binary cylinder has
infinitely many parameters with all initial arms positive, because
the slopes are positive integers. Equality throughout that cylinder
therefore forces equality of the rational slopes.

Taking valuations at two and three yields exactly
`l_i-l_j=u_i-u_j` and `q_i-q_j=v_j-v_i`. The other prime factors give
equality of the residual slopes. These relations have the signs used
in the note.

The cocycle remains valid after the first hit of 1. Its single-step
form is `kappa(n)=1-2(n mod 2)+kappa(T(n))`; at 1 it reads
`0=-1+kappa(2)` and at 2 it reads `1=1+kappa(1)`. Thus complete
cycles and the half-cycle endpoint 2 are both covered. At an arbitrary
common endpoint `z`, subtracting the two cocycles cancels `kappa(z)`.
This establishes necessity without assuming `z=1` or that the paths
stop at their first hit.

## 2. Padded clocks and nonnegative exponents

The adjusted equality is
`kappa(x_i)=C+u_i+2v_i`. Therefore `d(x_i)-u_i` has parity `C`.
Choosing `h` as in G2 makes every `l_i=h+u_i` at least the first-hit
time and leaves an even padding length. The padding `[1,0]` is the
actual shortcut cycle from 1 back to 1.

The claimed common exponent is nonnegative, not merely integral:

\[
h-C=2p(x_i)+2v_i+(l_i-d(x_i))\ge0.
\]

Thus `Q=(h-C)/2=q_i+v_i>=0`. This also covers `h=0`, an empty word
on an arm with `u_i=0`, and different padded lengths among the arms.

For `t=t0+2^h k`, the input difference in arm `i` is divisible by
`2^(h+u_i)=2^l_i`. All parity decisions of its length-`l_i` word
therefore remain legal. The endpoint increment is exactly
`a_*3^(v_i+q_i)k=a_*3^Q k`, as claimed. Every positive input follows
positive ordinary states, so this is not an assertion about a merely
2-adic lift. The same proof covers every integer lift with all starts
positive; in the constructed first-hit cylinder, negative lifts cannot
have positive starts, consistently with G3's endpoint.

## 3. The examples and residual set

I checked the first-hit data for 3, 5, 15, and 45 and reconstructed the
`15+4096k` example. Their defects are respectively 1, 2, 2, and 4.
Adding `r` initial even steps increases the defect by exactly `r`.
Consequently both infinite obstructed parameter families in LC-2
have the stated adjusted-grade mismatch.

These are ordinary convergent pairs outside every local fixed-word
cylinder of the specified affine family. They do not obstruct an
ordinary merger proof using other rules, as the note correctly says.
For any fixed word pair meeting at one of those parameters, equal
endpoint slopes would force equality as affine functions, and local
parity stability would yield a cylinder certificate. This contradicts
LC-1. Thus the isolated-meeting assertion of LC-3 follows, including
when the meeting occurs before 1.

## 4. Independent arithmetic check

I wrote and ran `review_local_arithmetic.py` independently of the
author checker. The completed `local-review-report.json` records:

* 10,548 cocycle prefixes, including positions beyond the first hit;
* 384 affine arms grouped into 28 equal-grade families;
* 22,026 literal lift edges;
* 64 zero-depth, unequal-clock lifts, including an empty arm;
* 64 cylinders with a common endpoint that need not be 1.

All passed. The nonterminal example is
`T(2t+1)=T(6t+4)=3t+2`; at `t=1` the common endpoint is 5.
The zero-depth example is `T^2(4t-3)=3t-2`, with the second arm's
word empty. These directly exercise two otherwise easy-to-miss
boundaries of the construction.

The author checker reconstructs affine coefficients and ordinary
lift paths correctly for the constructor's intended output. During
API review I noted that its initial version accepted an empty arm
list, and could accept constant zero-slope arms with a zero claimed
residual. Those objects are outside the theorem's domain; none is
created by its successful author replay. I reported the issue for
minimal domain validation. This is distinct from a mathematical gap
in LC-1.

## 5. Exact limitations

Every first-hit defect used here is attached to an actually convergent
positive integer. The classifier does not determine defects for
unproved convergers and does not establish the universal triple-ray
meeting claim. It classifies local membership given the finite
first-hit paths, not all ordinary merger methods.

The infinite residual examples show a limitation of the union of these
specific cylinder certificates. They provide no divergent orbit,
nontrivial positive cycle, or obstruction to a systematic additional
ordinary rule. The review does not extend to unrelated source claims,
later edits, or an assumed density estimate for the residual set.

## Final checker delta and disposition

The final checker SHA-256 is
`ebf0fcf5c1b6aee069d4735d10ad8c3be8b0c92e548b1e522d7b8e0b96efdfe2`.
I inspected its domain checks and separately executed the narrow
`local-domain-review-report.json` replay. It now explicitly requires
a nonempty arm list, positive integer slopes and residual, integer
parameter and offsets, nonnegative integer counts/clocks, and integer
parity bits.

The final checker accepts the legitimate zero-depth unequal-clock
certificate above and independently rejects empty arms, a zero-slope
constant arm, and a zero residual with the intended domain errors.
The earlier reported API issue is resolved. The proof retains the
corrected hash pinned at the start of this review.

**Final disposition:** the written equivalence and examples are verified
at the stated domain, and the inspected final checker correctly
reconstructs its finite certificates and enforces the identified
domain boundaries. This does not turn its bounded census into a
proof of the universal Collatz merger claim.
