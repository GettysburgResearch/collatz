# Independent mathematical reconstruction — Reviewer D

All main paths below are frozen at `cd1b3689e8d37fc4232945072e2faf6bd5ee47bd`. PR16 dependencies are frozen at `900ba417c968d8a41bc56a30d3ccc941284d8ce2`; the PR64 affine source is frozen at `88884c3e590b08aeb2018872987e71e14de1fe7b`. Exact blob identities are in [the source record](SOURCES_AND_VALIDATION.md). Arguments here explain review verdicts, not new canonical theorems. **All proposed corrections RP-D-* remain pending review.**

## 1. Signed extraction: the theorem is sound, the illustrative extension is false

For compatible least residues `r_j` modulo nested `K_j` tending to infinity, a nonnegative integer n eventually satisfies `r_j=n`; conversely a constant tail of residues determines n at every earlier modulus. A negative integer `-c`, c>0, eventually has `r_j=K_j-c`. Conversely a constant positive co-representative `K_j-r_j=c` determines `-c`. The recurrence `r_(j+1)=r_j+a_j K_j` translates these into eventual zero or eventual maximal appended digits respectively. Repeated moduli cause no problem: their radix is one and their only digit is zero.

For nested nonempty positive sets, their least elements are nondecreasing. Boundedness forces eventual constancy at m; nestedness puts that same m in every earlier set. An intersection point bounds every minimum. A finite hitting set is equivalent by taking its largest element. None of these implications supplies boundedness for an actual unresolved Collatz architecture.

**FD-01 counterexample.** Let `K_j=2^j` and choose the ordinary integer `-2^J`. For `j<=J`, its canonical residue is 0; for `j>J`, it is `2^j-2^J`. Thus `a_j=0` for j<J and `a_j=1` thereafter. The initial zero run can be arbitrarily long, followed by infinitely many nonzero blocks, yet the completion is ordinary and negative. This is a family of exact signed integers, not a Collatz counterexample.

**RP-D-01 (proposed wording).** Replace “remains nonordinary” by “cannot represent a nonnegative ordinary integer; a negative ordinary integer remains possible when the blocks are eventually maximal.” A nonordinary conclusion requires ruling out both eventual faces.

## 2. Parity cylinders, the completion ghost and periodic tails

For a length-L shortcut word, let `P=2^L`, `Q=3^q` and A be its affine offset. The two lifts of a source modulo `2^L` have equal first L parities, and their time-L values differ by the odd integer `3^q`. They therefore have opposite next parity. This proves the cylinder bijection inductively, including zero residues, and gives injective infinite coding in Z_2.

For the word `1110`, `(P,Q,A)=(16,27,19)`, so its unique periodic 2-adic source is `-19/11`. Literal rational replay gives

```text
-19/11 -> -23/11 -> -29/11 -> -38/11 -> -19/11.
```

Every finite cylinder has infinitely many positive lifts, but none of those facts identifies one positive all-time source. The conditional affine growth formula and the cardinality argument producing many nonordinary high-drift codes are correctly separated from existence of positive divergent trajectories.

For any nonempty periodic block w, shifting its unique infinite code by L leaves the code unchanged. Injectivity yields a fixed point and `(P-Q)x=A`. The denominator is odd and nonzero. For A>0, its real sign is the sign of P-Q, and integer realization requires the entire denominator to divide A. For the all-zero block, A=0 and the unique source is 0. An ordinary positive orbit with a finite preperiod and then periodic parity reaches this fixed point after the actual preperiod; no compactness argument or independent choice of its endpoint is used.

**FD-02.** The later prose/code block inserts “the primitive positive cycle is nontrivial” into a test labeled positive ordinary realization. `w=10`, `A=1`, `P-Q=1` realizes 1; `w=01` realizes 2. Both are positive ordinary realizations. Nontriviality is a further counterexample condition, not an integrality condition.

**RP-D-02 (proposed wording).** Label that code block “positive nontrivial-cycle certificate.” Retain the theorem's explicit all-zero, signed and trivial cases. For the autonomous-controller corollary, say deterministic finite-state evolution, fixed finite emitted blocks, and infinitely productive output. Arbitrary nondeterministic choices are not eventually periodic merely because their control graph is finite. The source packet's fixed-block compilation condition must remain.

The core of the pending periodic synthesis passes this audit. Changing its prose or canonical pending flag remains a separate integration action. The cycle problem itself is not resolved.

## 3. Coefficient-supercritical divergence is a full divergence proof

Put `C_k=3^(q_k)/2^k`, `D_k=log_3 C_k`, `alpha=log_3 2`, and `a=1-alpha`. Direct affine iteration gives

```text
T^k(n) = C_k n + (1/2) sum_(m=1)^k v_(m-1) 3^(D_k-D_m).
```

Under all-prefix supercriticality, D_k>=0. If D_k visits a band below H infinitely often, it must have infinitely many subsequent odd-step endpoints below H+a: otherwise choose a late low-band visit and take its next odd step. Such a step exists because an infinite even-only continuation would eventually make D negative. This proves the low-band renewal lemma with its quantifiers intact.

Given a target value M, choose H with `3^H n>M`. At every sufficiently late time, either D_k>=H and the multiplicative term exceeds M, or D_k<H and all previously counted low odd endpoints each contribute more than `(1/2)3^(-H-a)` to the nonnegative remainder. Their count tends to infinity. Thus **every** sufficiently late iterate exceeds M, not just a subsequence.

For the stopping equivalence, `n in S_N` exactly when `tau_c(n)>N`. Hence `m_N>B` exactly when all positive n<=B stop by N. Bounded nondecreasing m_N would stabilize at one ordinary never-crossing source. Conversely such a source bounds all m_N. At N=0, `m_0=1`. Finite convergence certificates yield finite source lower bounds; n=1 needs its explicit `10` coefficient 3/4. Endpoint divisibility is a legality test because the associated word has exactly one dyadic source cylinder. None of this proves SC* or the old FC-language crosswalk.

## 4. Finite safety automata: the canonicality boundary matters

Each inverse step has the even preimage 2y and possibly the odd preimage `(2y-1)/3`; both are no larger than 2y. Starting from {1,2}, the depth-d forbidden set is finite with largest element exactly `2^(d+1)`. Its complement among positive integers is therefore cofinite.

For LSD-first canonical words, positivity means a nonempty word ending in 1. Once the prefix length exceeds every forbidden word length, the only residual distinction is its last bit: the empty suffix is accepted in the last-1 residual and rejected in the last-0 residual. Appending a bit moves to its corresponding residual. The two residuals are distinct and form a terminal strongly connected component. Any other directed cycle would admit arbitrarily long prefixes outside this pair, impossible after all forbidden lengths have been exceeded. This proves uniqueness of the cyclic SCC **for this canonical language**, not for arbitrary encodings or regular sanctuaries.

The exact nonclosure witness is `2^(d+2) -> 2^(d+1)`. More generally a cofinite forward-invariant positive set avoiding {1,2} would contain a sufficiently large power of two and then be forced to contain the core. The new finite checker independently constructs and minimizes the automata for d=0,...,10; it is not a replay claim about older automaton files.

## 5. Six-branch rigidity: all six children are load-bearing

The displayed six pairs obey `Qc_i=Pr_i+a_i`. On an i-to-j transition,

```text
Qk' = Pk+c_i-r_j.
```

The canonical digit of k is therefore `[c_i-r_j]_Q`. Recalculation of all 36 entries agrees with the packet, and their residues modulo 2048 are disjoint from those of the six allowed digits. This proves the high-quotient nonclosure lemma, not global exhaustion of the source tree.

For an affine permutation `t+w A=A mod Q`, w must be odd: even w would give a common parity for all images. The unique odd digit `a*=413343` is fixed. Summing all six images and eliminating t gives `(1-w)(6a*-sum A)=0 mod Q`; the second factor is the odd integer 594979. Thus w=1 and t=0 modulo Q. This finite algebra, not a large search, is the alphabet rigidity input.

For a finite affine section machine, coefficient comparison on each infinite child progression makes the positive integer slope common on a reachable component. Alphabet rigidity gives `v=P+mQ`. With `h_(omega,i)=s_(omega,i)-c_i-mr_i`, the exact edge relation is

```text
Q h_child = P h_parent - m a_i.
```

All six children receive the same carry value. Consequently every post-transition carry occurs with every type. The finite set H of these values is invariant under all six maps `(Ph-ma_i)/Q`. Its maximum/minimum inequalities contradict each other for either sign of m; for m=0, expansion by P/Q forces H={0}. Initial transient states also have zero carry by their outgoing edge equation. This gives the original forward coordinate and no alternative contracting complete-tree section. The frozen PR64 source theorem was read to confirm successor-control and label-permutation hypotheses, not assumed from its title.

A nonconstant rational section integer-valued on every late integer is polynomial: coprime numerator and denominator have a polynomial Bezout identity equal to a nonzero integer R, so the denominator evaluated at each such integer divides R. A nonconstant denominator cannot do so. Along section edges, polynomial degrees agree and leading coefficients change by `(Q/P)^(degree-1)`. A reachable finite directed cycle forces degree one. Late integrality then makes slope and intercept integers; positivity makes the slope positive. The affine theorem applies.

Finally, legal depth-n states occupy at most `6^n` classes modulo `Q^n`. An infinite ordinary progression of fixed difference M occupies `2^(19n-min(v2(M),19n))` classes, eventually more than `6^n`. Thus no infinite progression lies in the all-depth survivor. Any infinite one-dimensional semilinear set contains a progression. A nonempty forward-invariant survivor set is infinite because the positive chart map increases. The semilinear conclusion follows in this exact chart and no larger method class.

## 6. Factor complexity and the full narrow dependency chain

The required source clauses were reconstructed, not accepted wholesale. For the centered 64-to-81 chart,

```text
64 A_(k+1) = 81 A_k - 17 e_k.
```

An ordinary source A_0>=2 stays integral on its actual itinerary, increases strictly, and satisfies `A_k <= (81/64)^k A_0`. These facts follow from the exact recurrence. D-9302's two-completion formula respects their distinction: its real coordinate is in [0,1], whereas its 2-adic coordinate is the candidate ordinary integer. Equality of two section representatives with zero third coordinate forces the diagonal displacement to be zero. No generic solenoid compactness or mixing theorem is being used.

If equal factors of length ell start at r<t, subtracting the two tail recurrences gives a nonzero integer difference divisible by `64^ell`. Therefore

```text
64^ell <= A_t-A_r < A_t <= (81/64)^t A_0,
ell < delta t + log_64 A_0,  delta=log_64(81/64).
```

Overlapping factors are allowed. Strictness comes from `A_r>0`, not from a guessed denominator gap. Among p_e(ell)+1 starting positions there are repeated factors with t<=p_e(ell), yielding the strict complexity lower bound and asymptotic slope at least 1/delta. This independently checks L-9311, T-9316's cone, and the resident repair's pigeonhole step.

For the completion bridge, L-9313 supplies bounded errors and the integer recurrence `64B_(k+1)=81B_k+e_k-e_(k+1)`. Eventual zero appended canonical blocks are equivalent to a nonnegative ordinary B_0. If B_0=0, divisibility of `e_0-e_1` by 64 forces e_0=e_1 and B_1=0, and induction makes the entire word constant. Thus a **nonconstant** word with eventual zero blocks would have B_0>=1. T-9315 then supplies a positive centered power and a nontrivial ordinary room. The recurrence cone contradicts the assumed low complexity. Constants must not be reinserted.

The positive centered-orbit strict-strip assertion in T-9315 is sound. A zero error would force its positive power to be divisible by arbitrarily large powers of 64. At an endpoint error `u_k=+/-1/81`, the integer recurrence forces the next error to be zero (since `|64u_(k+1)|<1`), already impossible. Thus actual positive ordinary centered orbits cannot hit these boundaries.

**FD-04.** T-9316 section 2 correctly excludes nontrivial ordinary survivor itineraries with `ell_j-delta t_j -> infinity`, but then says their appended blocks cannot be eventually zero without retaining the zero-completion exception. The constant word 0-infinity has repetitions `(r,t,ell)=(0,1,j)`, completion zero and every appended block zero. The same holds for 1-infinity. The Thue–Morse consequences remain sound: the repeated blocks at `2^j` and `2*2^j` have length `2^j`, and `81^2<64^3` gives the strict surplus. Shifts and complements remain nonconstant.

**RP-D-04 (proposed wording).** For arbitrary efficient-repeat codes conclude “no nontrivial positive ordinary survivor”; add “if the code is nonconstant” before appended-block nonstabilization. Keep the registry's narrower `clause_used` entry, and do not import the whole source as one verified assertion.

**FD-05.** L-9313's unrestricted real full-shift system has endpoints: with `rho=M/N`, `e=1000...` gives `x_0=1-rho`, `x_1=0`, and `u_0=1/N`; the complementary code gives `-1/N`. Neither current tail is identically constant. Its weak bound `|u|<=1/N`, unique bounded solution, and cylinder arithmetic are valid. These rational examples do not meet T-9315's positive ordinary all-time hypotheses.

**RP-D-05 (proposed wording).** Use a closed strip for arbitrary binary codes, and state a strict strip for codes not eventually constant, or separately for positive ordinary centered orbits. Preserve the exceptional zero and endpoint cases. This source error does not refute the resident nonconstant complexity theorem.

## 7. Additional resident proposed claims

### L-0041: exact append recurrence, two corrections

Appending type i to a word of length n requires exactly

```text
b=[P^(-n)(r_i-S_w)]_Q,
k=(S_w+P^n b-r_i)/Q,
R_(wi)=R_w+Q^n b,
S_(wi)=c_i+Pk.
```

Here k>=0 because a negative numerator multiple of Q would have magnitude less than Q. These recurrences match independent affine composition for every tested finite word. Lexicographic minimization by the appended high block is valid because `0<=R_w<Q^n`.

**FD-03a.** The empty word has canonical root 0, but `S_0=Z_>0` has minimum 1. Thus the displayed minimum-over-word-roots equality needs n>=1. **FD-03b.** Adding `Q^(n+1)h` to the original source changes the pre-final state by `P^n Qh` and its high quotient by `P^n h`; the next output changes by `P^(n+1)h`. The printed quotient increment includes an extra Q even though its final output formula is correct.

**RP-D-03 (proposed wording).** Separate `m_0=1`; use the root-minimum identity only at positive depth; distinguish value and quotient increments. No recurrence is replaced by a new unreviewed one.

### T-0046: necessary overlap, not a cofinal extraction theorem

The affine growth brackets follow by adding `a_min/(P-Q)` or `a_max/(P-Q)` and iterating. For one fixed positive all-time source, its past canonical root is the source after `Q^n>x_0`, and its past cap is the actual current state x_n. A future word of length ell has canonical root x_n whenever `Q^ell>x_n`. Thus past cap equals future root. With `ell_n=1+floor(log_Q x_n)`, the growth bounds give `ell_n/n -> log_Q(P/Q)`.

The finite bridge pairs and this necessary scale are valid. A sequence of unrelated finite bridges is not one ordinary all-time source. In the proposed emptiness target, “covering” must mean: for each candidate x_0, at cofinally many n, exclude **every** integer ell whose band intersects the entire allowed growth interval for x_n. Merely testing one ell per n with the correct limiting ratio can miss an actual survivor's ell_n. This is a quantifier clarification for an open target, not a supplied rejection proof.

### L-0042: polynomiality is valid, application assumptions do not vanish

A convergent Puiseux expansion at infinity gives `f^(k)(x)=O(x^(rho-k))` for each fixed derivative order. Taking integer k>max(rho,0) makes this derivative tend to zero. On k+1 successive integer nodes from a set with gap bound H, every denominator in the divided difference is bounded by products of kH. The stated coarse lattice `(1/((kH)!)^(k+1)) Z` suffices. The mean-value identity forces the divided differences eventually to be zero. Sliding interpolation places the entire late integer-valued sample on one rational polynomial. If f-p were a nonzero algebraic branch, its irreducible polynomial relation could not have infinitely many zeros at Y=0; hence f=p. This is a sound use of algebraicity, not the false analytic identity principle at an accumulation point at infinity.

The standard analytic input is not an empirical assertion. I checked primary context in Tobias Kaiser, *Semialgebraicity of the convergence domain of an algebraic power series*, arXiv:2402.07524v2, Introduction and Preliminaries Fact 2 (including the Puiseux extension). Replacing x by 1/t transfers the local convergent expansion to infinity; termwise differentiation on a smaller sector gives the derivative estimate. No new theorem about Puiseux convergence is claimed. Primary text: <https://arxiv.org/html/2402.07524v2>.

**FD-06.** This proof gives rational polynomiality, not all late-integer integrality or full child coverage. For example, `f(x)=x/2` is integer-valued on the syndetic even inputs but has noninteger slope. More specifically, restrict the six-branch chart to one type i followed only by i. The section `f(k)=Qk+r_i` reproduces that single child's law on the infinite progression of k satisfying `Pk+c_i-r_i=0 mod Q`, yet is not `Pk+c_i`. This is a checkable proper-sublanguage identity section, **not** a contracting section or a survivor construction. It demonstrates why the full-six-child premise cannot be recovered from syndeticity alone.

**RP-D-06 (proposed wording).** State polynomiality as proved. Any subsequent degree/affine-collapse claim must separately retain all relevant complete-tree, tail-domain, positivity, coefficient and section hypotheses. Do not present this example as refuting the actual full-tree theorem or proving a new extraction method.

## 8. Current integrated wrappers and remaining boundaries

The four new reference assemblies and CONVENTIONS correctly separate the section P rank from moving R_*, quarter-safe from nonincreasing-safe sets, norm contraction from dominated-cone bounds, and unsafe return control from safe exit. Finite rank balls bound candidate sources, not intermediate vertices or guaranteed meeting times. Orbitwise injectivity cannot be transferred to an entire inverse basin. These distinctions survive this reading; it is not a new full proof audit of every linked import.

The exact `A_w=0` reasoning in E-INTEGRATION-002 is valid: a first-crossing all-even word is the single bit 0, and `A_w=n+2d=0` has no solution with n>0,d>=0. The restriction is an endpoint guard, not an all-word exclusion. E-INTEGRATION-001 retains other original hypotheses that were not independently re-audited here; no blanket D approval is assigned to it.

Both structural checkers explicitly disclaim mathematical verification. The older checker enforces existing status labels and curated links; it cannot discover FD-01 or FD-02. The newer checker adds blob/subtree pins, path-qualified identities and optimized-verifier guards, but likewise is not a theorem prover. Neither was executed against a full main checkout in this review. No current readiness verdict should confuse these inspection facts with a full-tree run.
