# Exact candidate recognition in the numerator's binary length

23 November 2026. **PROVED finite recognition and height bounds; universal
candidate construction remains OPEN.** The new recognizer accepts or rejects
every supplied triadic candidate in at most the reduced negative numerator's
binary length of paired transitions. It does not simulate the later positive
sector, and does not charge the quadratic logarithmic weight
`F(r)=product_(j<r)(1+3^j)`.

The distinction is essential: this is an exact first-crossing recognizer,
not a claim that the same number of arbitrary complementary parity bits
forces success. Wrong first crossings are rejected immediately.

The [standalone Lean module](NegativeCandidate.lean) proves thirteen public
finite declarations, including the literal negative halving, finite clock
bound, sharp backward-code inequalities, soundness of the executable
checker, and its completeness for literal first-crossing certificates.
The full equality-to-Omega interpretation and polynomial bit-complexity
statement below are written mathematics with explicit inherited inputs.
The [total Python recognizer](negative_candidate.py) emits the actual
ordinary trajectory and, for an odd accepted input, the complete exponent
tuple in the original problem.

## 1. The exact statement

Use the shortcut map

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd}.\end{cases}
\]

Let n be a positive ordinary integer and let a/3^r be a supplied signed
triadic rational. First cancel common factors of three. This takes finitely
many divisions of the supplied numerator; the exponent r may be supplied
in binary, with no a priori bound.

Let Omega(n) be the unique 2-adic point with the complementary shortcut
parity itinerary. The recognizer below decides the statement

\[
                         a/3^r=\Omega(n).                 \tag{1}
\]

For a negative reduced numerator write A=-a>0 and E=bl(A), where
`bl(A)` is its usual positive binary length, so `A<2^E`. The procedure
uses at most E paired transitions. If it accepts, it emits a first-hit
certificate of length at most E+2:

\[
\boxed{\tau(n)\le\operatorname{bl}(A)+2.}               \tag{2}
\]

The only nonnegative accepted rational values are

\[
                    (n,a/3^r)=(1,2),(2,1),(4,1/3).      \tag{3}
\]

The decision algorithm is polynomial in the bit lengths of n, a and the
binary-encoded r. This is a statement about **recognizing a supplied
candidate**, not about constructing one for every n.

## 2. Inherited interface: the forced sign crossing

Two already proved interfaces are used, at frozen source heads.

1. PR177 at `f47a5ec51aa5853f104013a6d5046d6220ff7423`,
   `literature-closure/triadic/FINITE_DUAL_RECOGNITION.md`, proves that an
   all-time complementary triadic candidate for a positive ordinary n
   forces convergence. Its finite sufficient horizon is needed here only
   to justify this implication, not as the runtime of the new algorithm.
   PR176 at `4171e1fe40e41842af9f800bd821084b724cf8f9`,
   `research/lean-global-resolvent-20261121/overview/source-construction/`,
   independently gives the exact rigidity theorem and formal scope.
2. A first hit from n outside {1,2,4} ends with
   `8 -> 4 -> 2 -> 1`. Pulling the complementary terminal value backward
   gives `-1/9 -> 1/3 -> 1 -> 2`. Every earlier complementary inverse
   preserves negativity: it is either y->2y or y->(2y-1)/3. Thus the
   first negative-to-nonnegative crossing of the true dual is exactly

\[
\boxed{(8,-1/9)\longmapsto(4,1/3).}                    \tag{4}
\]

The sign classification and exact denominator interpretation also appear
in PR176's `EXACT_CANDIDATE_RIGIDITY.md` and
`CARRY_CONSTRUCTION_ATTACK.md` at the stated head. They are credited
inputs, not new convergence results.

For a reduced negative true dual, the denominator exponent stays positive
through the entire negative phase. At (8,-1/9) it is two; every earlier
original-even inverse adds one, while an original-odd inverse retains it.

## 3. The new halving observation

At a compatible state `(x,w,r)` with w<0 and r>0, the literal rules are

\[
\begin{array}{c|ccc}
&x'&w'&r'\\\hline
x\text{ odd}&(3x+1)/2&w/2&r\\
x\text{ even}&x/2&(w+3^{r-1})/2&r-1.
\end{array}                                             \tag{5}
\]

Both divisions are integral because x and w have opposite parity. If the
new numerator is still negative, then in **either** row

\[
\boxed{2|w'|\le|w|.}                                  \tag{6}
\]

The odd-original row is equality. In the even-original row,
`2|w'|=|w|-3^(r-1)<|w|`. The denominator factor is actually cancelled
at that step; retaining a fixed denominator would conceal this stronger
integer decay.

Thus a negative continuation through clock k satisfies

\[
                         2^k|w_k|\le A.                \tag{7}
\]

Since a negative integer numerator has absolute value at least one,
there cannot be a negative state at clock E. By that clock the procedure
must have found a parity failure, a nonnegative numerator, or an exhausted
denominator. No bound on r is needed for this argument.

For a true candidate, write K=the first original hit of 8. At that clock
the reduced numerator is -1. Equation (7) gives

\[
                  2^K\le A,\qquad K<E,\qquad
                  \tau=K+3\le E+2.                    \tag{8}
\]

This is the binary clock theorem. It uses no asymptotic approximation,
ordinary-orbit density, or assumption about the existence of a candidate.

## 4. A sharp numerator-denominator constraint

There is an additional strong filter on every successful reduced negative
candidate. Let b be the number of original-even inputs before the first
hit of 8. Denominator persistence gives r=b+2. Let D_K be the complete
complementary carry along that K-step prefix:

\[
D_0=0,\qquad D_{j+1}=3^{1-e_j}D_j+(1-e_j)2^j,
\quad e_j=T^j(n)\bmod2.
\]

The terminal dual is -1/9, so its finite affine identity gives exactly

\[
\boxed{A=2^K+9D_K.}                                   \tag{9}
\]

If the b even positions are d_0<...<d_(b-1), then d_j>=j, and

\[
D_K=\sum_{j<b}3^{b-1-j}2^{d_j}
\ge\sum_{j<b}3^{b-1-j}2^j=3^b-2^b.
\]

Using K>=b in (9) gives

\[
\boxed{A\ge3^r-2^{r+1}.}                              \tag{10}
\]

Equality holds exactly when K=b, so all original inputs before 8 were
even. These are precisely

\[
n=2^{r+1},\qquad \Omega(n)=\frac{2^{r+1}-3^r}{3^r},
\quad r\ge2.                                           \tag{11}
\]

In particular,

\[
\boxed{3^r\le9A,\qquad r\le\log_3 A+2,\qquad r\le E+1.} \tag{12}
\]

For the first inequality, `3^r-2^(r+1)>=3^(r-2)` for r>=2. The last
also follows immediately from r=b+2<=K+2<=E+1.

The Lean `NegativeCode` starts at `(A,r,K)=(1,2,0)` and has the literal
backward updates

\[
(A,r,K)\mapsto(2A,r,K+1),\qquad
(A,r,K)\mapsto(2A+3^r,r+1,K+1).
\]

It proves (8), (10), and the power form of (12) by induction on this
complete code. The equality characterization in (11) is written scope.

## 5. The total algorithm and both directions of correctness

After reduction, do the following.

1. For a>=0, accept exactly the three pairs in (3).
2. For a<0, reject if r<2 or r>E+1. Only now compute 3^r, and reject if
   `3^r>A+2^(r+1)`.
3. Start `(x,w,j)=(n,a,r)`. For at most E transitions, require w<0,
   j>0, and complementary parity, then perform (5).
4. At the first nonnegative numerator, accept exactly the reduced state
   `(x,w,j)=(4,1,1)`. Reject every other crossing, including zero.
   Reject a negative integral endpoint j=0.
5. On acceptance append the two ordinary steps `4->2->1` and the dual
   steps `1/3->1->2`. Emit the complete ordinary path.

**Soundness.** Each performed branch is integral and has complementary
parity. An accepted crossing extends to the standard complementary cycle.
Pulling this exact finite word backward shows that the supplied rational
has the complementary itinerary forever. Thus it is Omega(n). The
ordinary coordinate gives an actual hit, not a 2-adic limiting witness.
The Lean theorem `negativeSeek_sound` proves the ordinary hit and clock
bound directly, without using either inherited rigidity theorem.

**Completeness.** Suppose the supplied candidate equals Omega(n).
The inherited finite triadic theorem forces convergence of this particular
n. The forced terminal segment then gives (3) or (4), and (8), (10),
(12) show that no preliminary filter can reject it. In the negative case
all required parity tests pass, the denominator stays positive, and the
first crossing is the exact accepted state within E transitions. The Lean
theorems `negativePath_clock` and `negativeSeek_complete` prove the funded
replay of every such literal first-crossing certificate. The implication
from Omega equality to that certificate is the explicitly written,
source-dependent part of completeness.

**Termination.** If the recognizer has neither rejected nor accepted
earlier, every state through E would have a negative integer numerator
at positive exponent. Equation (7) would give `1<=A/2^E<1`. Therefore
the implementation's fuel-exhaustion exception is unreachable on valid
inputs. This conclusion is proved for all inputs; finite controls merely
check the implementation.

For odd accepted n, list the clocks of the odd states, including the
terminal one:

\[
0=A_0<A_1<\cdots<A_s=\tau.
\]

The emitted tuple satisfies the user's exact complete identity

\[
3^s n+\sum_{j<s}3^{s-1-j}2^{A_j}=2^{A_s}.
\]

## 6. Runtime, and what this does not imply about construction

Reduction performs at most O(bl(|a|)) divisions by three. The comparison
`r>E+1` occurs before exponentiation, so a huge binary-encoded exponent
does not trigger creation of a huge integer. For a surviving negative
candidate, r=O(E), and 3^r has O(E) bits. During at most E transitions the
negative numerator shrinks, and the ordinary state has at most
`bl(n)+E` bits because each shortcut step is at most doubling.

Consequently the arithmetic, comparisons, normalization and explicit
output all have polynomial bit cost in the supplied input size. The
statement is **O(E) trajectory transitions**, not O(E) bit operations.
The Python implementation uses arbitrary-precision integers and the
standard library only.

The short clock is not a replacement for the old congruence-only horizon.
For example `n=24, a=-1, r=2` passes its first three complementary tests,
but its first crossing is `(12,1/3)`, so it is rejected immediately.
Accepting a long prefix after a wrong crossing would lose the new theorem.

For any proposed bound A<=M, the successful exponents are now restricted
to `2<=r<=log_3 M+2`, and each supplied pair can be recognized using its
own binary numerator length. This removes the old F(r) charge from exact
candidate verification. It does not prove that any numerator bound M
contains a successful candidate for an arbitrary n, nor a bound M
computable from the complete witness of x in the original question.

The remaining construction is still concrete: from the unrestricted
source certificate for x, produce A,r whose negative trace for
`n=(x+1)/2` passes the parity tests and reaches exactly `(4,1,1)` at its
first crossing. No such universal transformation is asserted here.
Input witness lengths and exponents, and eventual output lengths and
exponents, remain unrestricted.

## 7. Evidence and scope

The formal module has thirteen public audited theorems. All compile under
Lean 4.34.1 with warnings treated as errors; their transitive axiom sets
are subsets of `propext`, `Classical.choice`, and `Quot.sound`.

The Python controls use sixteen independently computed finite source
trajectories, their unreduced candidate presentations, 64 wrong candidates,
two wrong crossings, a binary exponent of size 10^100, and sixteen sharp
power-of-two equality cases. Normal and optimized Python runs are compared
byte for byte. The ordinary output tuple is checked by its full integer
identity, not only by a parity hash.

These controls do not prove completeness or universal candidate existence.
The symbolic proofs above supply the former; the latter remains open.
Execution receipts and frozen hashes are kept in the associated report
directory, separate from this scientific note.
