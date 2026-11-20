# Exact transfer of ordinary convergence certificates

**Status: PROPOSED.** Written proofs of identities and a terminating partial
certificate transformer. This note does **not** prove the remaining
basin-closure implication or Collatz.

The target is the latest PR146 one-sided criterion, pinned at
`6863d298187af8b2619efbf78cc4b0aa8e627393`:

$$
16k+1\to1\quad\Longrightarrow\quad32k+1\to1.
$$

Write
$$
U(n)=\frac{3n+1}{2^{v_2(3n+1)}},\qquad
I_a(z)=\frac{2^a z-1}{3},\qquad R_k(z)=2^kz-1.
$$

All sources and suffix values below are positive odd ordinary integers. An
inverse symbol is used only when it produces such an integer. The relation
`~` means that the actual ordinary forward orbits meet at finite, possibly
different clocks. A convergence certificate is a finite legal valuation word
`(a_0,...,a_(d-1))` taking the source to 1 under U. It includes every gap; no
fresh unspecified bits are supplied to the target.

## 1. A universal carry identity

For every positive odd z and every k>=1,

$$
U^j(R_k(z))=3^j2^{k-j}z-1\quad(0\le j<k),
$$

and

$$
\boxed{U^k(R_k(z))=\operatorname{oddpart}(3^kz-1).}\tag{1}
$$

For j<k-1 the current value is -1 modulo 4, so its next valuation is exactly
one. At j=k-1 its odd numerator is `2(3^k z-1)`, which proves the last step.
This proves the identities with the actual positive values, rather than with a
chosen parity extension.

Suppose `x=I_a(z)`. For k>=1 the same target component is therefore represented
by

$$
\boxed{R_k(x)\sim
\operatorname{oddpart}\big(2^a3^{k-1}z-(3^{k-1}+1)\big).}\tag{2}
$$

This is a closed arithmetic interface for consuming one source-certificate
letter. It also explains why a grammar containing only `R_k` is not closed:
already k=3 produces the new constant carry 5 when the forced factor 2 is
removed. Formula (2), including its carry, must be retained.

For k=1, the special cases simplify considerably:

$$
U(R_1(x))=
\begin{cases}
\operatorname{oddpart}(z-1),&a=1,\\
R_{a-1}(z),&a\ge2.
\end{cases}\tag{3}
$$

The a=1 case has z>1, so the odd part is defined and positive.

## 2. A proved two-state positive grammar

Use state A for `R_1(x)` and state B for `R_2(x)`, with x the current suffix of
the given source certificate. Every rewrite below consumes at least one source
letter. It therefore terminates on a finite certificate, either with a proof
or with an explicitly reported unhandled carry.

### Gap 2 and gap 3

If `a=v2(3x+1)>=2`, then

$$
\boxed{U^2(R_1(x))=U^2(R_2(x))=
\operatorname{oddpart}(9x-1).}\tag{4}
$$

Indeed `U(R_1(x))=(3x-1)/2` and `U(R_2(x))=6x-1`, and taking one more odd step
gives the displayed common value. Combining (3) and (4) yields

$$
R_1(x)\sim R_2(x)\sim R_{a-1}(z).
$$

Thus either state, on source gap 2, becomes A at z; either state, on source
gap 3, becomes B at z. In particular the whole source prefix over {2,3} can
be consumed with just these two states.

There are explicit merger clocks, useful for compiling an actual certificate:

$$
U(R_1(x))=R_{a-1}(z),\qquad
U^a(R_2(x))=U^{a-1}(R_{a-1}(z))\quad(a\ge2).\tag{5}
$$

For a=2 the second identity follows from (1) directly. For a>=3,
`U^2(R_2(x))=3*2^(a-2)z-1`; applying (1) to that last expression proves (5).

### A followed by gaps (1,1)

Let z=U(x), w=U(z), and suppose both source gaps are one. Then

$$
U(R_1(x))=(w-2)/3,
$$

which is a positive odd integer, and

$$
\boxed{U^2(R_1(x))=U(R_1(z))=
\operatorname{oddpart}(w-1).}\tag{6}
$$

Thus state A can delete the first of two consecutive gap-one letters, keeping
state A at z. The second gap is not discarded.

### A followed by gaps (1,b), b>=3: absorption

Let w=U^2(x). Direct substitution gives

$$
U(R_1(x))=I_{b-2}(w),
\qquad
\boxed{U^2(R_1(x))=w.}\tag{7}
$$

The inverse value on the left is positive odd and integral because it equals
the actual target step; its valuation is exactly b-2. Consequently this is
an ordinary merger with the already certified suffix. No closure hypothesis
is used. More generally, a source prefix of q>=1 consecutive gap-one letters
followed by b>=3 satisfies

$$
U^{q+1}(R_1(x))=U^{q+1}(x).
$$

This follows from q-1 applications of (6), followed by (7).

### B followed by gaps (1,b), b>=3

Here

$$
U^2(R_2(x))=2^b w-3,
$$

and

$$
\boxed{U^b(R_2(x))=U^{b-2}(R_{b-2}(w)).}\tag{8}
$$

For b=3, the next target step is `oddpart(3w-1)`. For b>=4, it is
`3*2^(b-3)w-1`, and (1) finishes the calculation. Hence a B-state block (1,3)
becomes A at w, while (1,4) becomes B at w. For b>=5 the formula remains valid
but leaves the two-state grammar.

### Terminal state

At x=1, both remaining states are certified: `R_1(1)=1` and
`R_2(1)=3 -> 5 -> 1` under U. A certificate accepted by this finite rule system
therefore yields a proof that its companion reaches 1.

This is a positive, source-dependent, well-founded subgrammar. Its termination
rank is the number of unused letters of the actual source certificate. Its
acceptance is not asserted for every legal certificate.

### Compiling actual certificates

The executable `transform(source, valuation_word, initial_state=1)` accepts a
**supplied finite source certificate** and first validates every stated gap and
the terminal value 1. It performs no search to establish source convergence.
Each rewrite emits the literal two ordinary sources and the merger clocks
proved above. The clock pairs are `(1,0)` for an A single-gap step,
`(a,a-1)` for a B single-gap step, `(2,1)` for (6), `(2,0)` for (7), and
`(b,b-2)` for (8).

Suppose an emitted edge is `U^L(p)=U^R(q)` and the suffix has already certified
`U^D(q)=1`. Since U(1)=1, it follows that

$$
U^{L+\max(D-R,0)}(p)=1.
$$

Starting with the supplied source suffix or the proved root states, this
formula compiles a finite convergence clock for the original target. The
program then extracts exactly that many target valuations and independently
checks the resulting finite target word. A clock may include visits after the
first visit to 1; no claim of minimality is needed. On rejection the output
still contains all established meeting edges and the exact residual ordinary
integer, source suffix, and carry parameters. For example, the input
`source=113, valuation_word=[2,8]` ends at the explicit residual `R_7(1)=127`,
not at an unspecified failure to find a meeting.

## 3. The omitted (1,2) branch is a real new carry

In state A, source gaps (1,2) give

$$
\boxed{U(R_1(x))=
\operatorname{oddpart}\big((w-1)/3\big).}\tag{9}
$$

This is not an R-state, and deleting the factor 3 would be invalid. More
generally, define

$$
B_d(z)=\operatorname{oddpart}\big((z-1)/3^d\big)
$$

when z>1 and `3^d | z-1`. A source gap 2 transports this carry exactly as

$$
B_d(I_2(w))=B_{d+1}(w).
$$

Thus an intervening run of twos accumulates a ternary denominator. If its next
source gap is b>=3, the residual is

$$
\frac{2^{b-2}w-1}{3^{d+1}}.
$$

Only d=0 gives the immediate ordinary inverse in (7). The higher denominator
is not licensed by the given ordinary convergence certificate. At a terminal
w=1, its integrality forces `2*3^d | b-2` by the elementary 3-adic valuation
formula for `2^(b-2)-1`, but this arithmetic constraint alone does not prove
the resulting quotient converges.

For general k>=3, equation (2) is the required carry interface. If a is large
enough to strip the initial forced factor, k=3 produces

$$
2^{a-1}9z-5.
$$

While its remaining binary factor permits it, its actual low-bit carry follows
`5 -> 7 -> 5` under the minus map `c -> oddpart(3c-1)`. This describes a finite
forced prefix. It does not turn the negative cycle into an ordinary positive
counterexample or prove that subsequent positive carries terminate.

## 4. Exhaustive depth-two boundary family

There are no nontrivial x=1 modulo 16 with odd hitting depth one. Indeed if
U(x)=1, then `x=(2^a-1)/3`; the nontrivial integral odd possibilities have even
a>=4 and are 5 modulo 16.

Every x=1 modulo 16 with odd hitting depth exactly two has valuation word

$$
(2,6r+2),\qquad r\ge1,
$$

and is exactly

$$
\boxed{x_r=\frac{2^{6r+4}-7}{9}.}\tag{10}
$$

Proof: the first gap is exactly 2. If the second gap is b, the suffix is
`(2^b-1)/3`, so x is `(2^(b+2)-7)/9`. Integrality is equivalent to
`b+2=4 modulo 6`. The case b=2 is x=1; all b=6r+2, r>=1, give exact depth two.

Its companion obeys

$$
R_1(x_r)\xrightarrow{U}\frac{2^{6r+3}-5}{3}
\xrightarrow{U}\boxed{2^{6r+1}-1}.\tag{11}
$$

Both displayed valuations are exactly 2. Consequently the PR146 implication,
even restricted to this exhaustive depth-two family, is **equivalent** to
convergence of every Mersenne number `2^(6r+1)-1`, r>=1.

This is a precise unhandled terminal branch of the certificate transformer;
it is not a fixed-clock or arbitrary-positive-lift obstruction.

## 5. The terminal gap produces a provable growth debt

Put h=6r+1, so the known source certificate has two odd steps and total
valuation h+3. From (1), its companion reaches

$$
2\,3^{h-1}-1
$$

after h+1 odd steps, and reaches `(3^h-1)/2>1` after h+2 odd steps. Thus its
odd hitting depth, if finite, is at least h+3. Its actual maximum before then
is at least

$$
\frac23\left(\frac{9x_r+7}{8}\right)^{\log_2 3}-1.
$$

The companion's peak divided by the known source tends to infinity. Including
the terminal valuation in a proposed rank does account for this growth, but
does not make the ordinary height decrease.

There is also a necessary division-budget increase. If the companion has a
certificate of m odd steps and total valuation S, then telescoping gives

$$
2^S=R_1(x_r)\,3^m\prod_{j=0}^{m-1}
\left(1+\frac1{3n_j}\right)>R_1(x_r)3^m.
$$

Since m>=h+3,

$$
S>\log_2 R_1(x_r)+(h+3)\log_2 3.
$$

Along any unbounded set of r for which finite target certificates are given,
the target/source total-valuation ratio therefore has liminf at least
`1+log_2 3`. A direct transfer that preserves or decreases either the number
of odd steps or the total division budget is impossible for this family.
This does not rule out a different ordinal rank with auxiliary arithmetic
lemmas; those lemmas must actually resolve the terminal Mersenne branch.

## 6. Attempt to continue the terminal exponential family

There is a complete reduction for even terminal exponents. For every even
h>=2,

$$
\boxed{U^h(2^h-1)=U^h(2^{h-1}-1)=
\operatorname{oddpart}(3^h-1).}
$$

The first equality to the common value is (1). For the second source, the
preceding odd exponent h-1 gives
`U^(h-1)(2^(h-1)-1)=(3^(h-1)-1)/2`; one more odd step gives the same common
value. Thus every even-exponent Mersenne has a fully ordinary, variable-clock
merger with the preceding odd-exponent Mersenne. This is a genuine decreasing
terminal exponent rule. It leaves the required odd exponents h=1 modulo 6.

The next step after the endpoint in section 5 is also exact. For odd h,
elementary factorization gives

$$
v_2(3^{h+1}-1)=2+v_2(h+1),
$$

so

$$
U\left(\frac{3^h-1}{2}\right)
=\frac{3^{h+1}-1}{2^{2+v_2(h+1)}}.
$$

This does not reduce the exponential parameter. If one writes the new state
as `(3^e-1)/2^d`, its next numerator is
`3^(e+1)+(2^d-3)`. The additional positive carry must be retained. The
factorization of `3^(h+1)-1` into factors with exponent `(h+1)/2` likewise
does not transfer their separate convergence certificates to their product;
that would require a further unproved closure property. No all-exponent
decrease or all-carry well-founded rank was obtained from either calculation.

## Exact remaining proof obligation

The two-state grammar is complete for its stated rules, but the full carry
grammar (2) includes unbounded new offsets and terminal residues. No argument
here proves termination to a certified ordinary suffix for those carries. In
particular, the first unresolved depth-two inputs already ask for all the
Mersennes in (11). Treating the certified suffix 1 as an accepting terminal
regardless of its carry would assume exactly the missing result.
