# Checkpoint 4: statistical recovery, an ordinary anchor, and native arithmetic discrepancy

**Open research.** The three packets below are complete written deductions with explicit scope. None proves universal convergence. The requested nine-hour pass continues until 2026-11-28 18:08:39 UTC.

Author source commits: arithmetic `09a5830cfdc99063d39fda85e22a39ca1eddc3f3`; dynamics `02a2d4a30e85174332bccd550caaa78ee987ab2a`; outside `74530394cc927f304de7dc93dcb7fba200e4dde2`. The coordinator independently reconstructed each proof before integration. [Exact finite receipts](CHECKPOINT_04_FINITE.json) and [fresh Lean receipts](CHECKPOINT_04_LEAN.json) identify the sources actually checked.

## 1. What a finite ternary observation retains, and what it cannot recover

[TILTED_INVERSE_INFORMATION.md](../../research/astra-wild-nine-hour-20261128/arithmetic/TILTED_INVERSE_INFORMATION.md) studies iid positive geometric gaps with parameter theta. The observed variable is their n-trit Syracuse cell; K_n is the minimum total gap cost coding that exact cell. This is a specified statistical experiment, not the trajectory distribution of an arbitrary fixed ordinary integer.

For theta in a compact subinterval of (log_3(2),1), the reversed real numerator has a uniform positive fractional moment. At any fixed total and cell, distinct word numerators are spaced by at least one after division by 3^n. If the realized total exceeds K_n by k, summing against every cheaper word and then against the cost difference gives an exponentially decreasing ambiguity bound. The coordinator checked the infinite word sum: all the cheaper-word probabilities sum to one, and the geometric likelihood ratio is exactly (1-theta)^j. No hidden count of all words is omitted.

This bound gives uniformly bounded conditional word entropy and uniformly bounded lost Fisher information. Clipping n/K_n estimates the unknown parameter with squared error O(1/n). The fitted posterior differs from the true posterior by a one-parameter exponential tilt of the ambiguity. Its uniformly bounded exponential moment then gives mean total variation O(n^{-1/2}). This decoder is parameter independent on the chosen compact interval and always returns a word in the supplied cell. It is an existence theorem with countable posterior support, without a practical runtime claim.

The stronger realized-prefix statement follows from the exact conditional entropy chain rule. The full conditional word entropy is the partial sum of the one-letter posterior entropies at successive observation depths. Boundedness makes that nonnegative series summable. Removing any diverging number of final gaps therefore leaves a prefix whose posterior uncertainty tends to zero. This distinguishes distributional recovery of an experiment from agreement with the particular realized word; both are proved in the stated high-tilt range.

The moment calculation uses the same numerator spacing after taking a power tilt of the geometric law. The relevant perpetuity moment is at most one in the displayed parameter chamber. Its equality case only costs a polynomial in depth. The coordinator checked the algebraic threshold, including every order q>1 at theta>=log_3(2), and every q>=2 at theta>=1/2. Positive mass merging supplies the matching lower moment exponent. Counting all words of total at most bn and applying these moments gives the cheap-cost large-deviation upper bound. A change of measure to the geometric law of mean b supplies the local lower bound, retaining both the observed minimum and the realized total. The relative-entropy and testing claims then follow from the same actual observed event.

At the entropy-critical theta, the conclusion changes. The actual prefix posterior is an exact ratio of the full and tail cell densities. The all-cut density inequality gives a lower bound on its negative logarithm by the maximum drawdown of the centered information walk, minus a negligible tail correction. The full-dimension theorem makes that correction o_P(sqrt(n)) for an O(sqrt(n)) terminal allowance. Reversal and the invariance principle give the half-normal limit. A list of exp(t sqrt(n)+o(sqrt(n))) prefixes consequently has limiting success at most 2 Phi(t/sigma)-1. In particular exp(o(sqrt(n))) candidates have success tending to zero. The argument does not assume independence between the maximum and the tail correction.

The all-cut mechanism is explicitly credited to [Weaver 135 v1, Lemma 4](https://rstation.ai/problems/collatz/papers/135/v1), whose primary text the coordinator retrieved. Leen's full entropy dimension remains the named outside analytic input. Bounded ambiguity and spacing at the special theta=3/4 law, and the fair moment spectrum, are credited to Weaver 9; they are not claimed as new here.

Finally, the packet gives a separate fixed-positive-integer statement. For every positive odd a, theta>1/2, p=-log_2(1-theta)>1, and b_theta=theta(1-theta)^(log_2(3)-1),

\[
\sum_{n\ge0} b_\theta^{-n}\mu_{\theta,n}(a\bmod3^n)<\infty.
\]

Coding words at a are exactly its actual positive odd predecessors. Their normalized weights are powers of the true affine multiplier, bounded by (a/x)^p. A nonperiodic target receives each predecessor once; repeated visits to a periodic target form a convergent geometric series. Thus the trace bound holds in either case. The terminal-unit minimum differs from K_n by at most two, by changing the last exponent when necessary. Neither fact transfers a typical-code assertion to one prescribed positive source.

## 2. Two simultaneous congruences isolate an actual boundary source

[MERSENNE_ANCHOR.md](../../research/astra-wild-nine-hour-20261128/dynamics/MERSENNE_ANCHOR.md) fixes B=2^k and a positive anchor d, and considers actual positive integers satisfying

\[
n\equiv d\pmod{B-1},\qquad 2n\equiv d\pmod{2B-1}.
\]

The canonical integer Bd always qualifies and has centered amplitude W(d). Below log_2(n)<=(1-delta)k^2, every competing source requires more than sqrt(delta k)/64 odd departures before any first hit of one. Hence every competing amplitude tends to zero. The constants allow d to vary with log_2(d+1)<=delta k/128.

The proof starts from a genuine first-hit identity, keeping all positive numerator terms. Modulo B-1, expand its coefficients into binary tokens and merge equal occupied positions cyclically. Every merge reduces the token count. Since the count is less than k, the final representative cannot fill the entire circle, and its residue forces exactly one surviving token. Every original token reaches it after at most the total number of merges. The token from the lowest bit of 3^p d therefore localizes every physical odd position to one short cyclic interval.

The coordinator checked the signed representatives carefully. They give t=Lk+r_t and s_i=m_i k+r_i with 0<=m_i<=L, even when some r_i are negative. The resulting rational polynomial P has P(B)=n, one positive leading coefficient, and nonpositive lower coefficients. Clearing all powers of three before reducing modulo either Mersenne number avoids a false unit assumption.

The first congruence forces P(1)=d once the coefficient height is small enough. The second forces 2P(1/2)=d. The latter needs an additional factor 2^L when clearing denominators; this is the decisive height cost, and the theorem charges it in full. The explicit p and d bounds leave enough room below the moduli. Positive d and the physical coefficient signs then force degree one and no lower coefficients, so P(z)=dz and n=Bd.

Both sharpness families are genuine convergent sources, not hypothetical exceptional inputs. For y_E=(340*2^E-7)/9 with E divisible by six, the exact odd gaps are 2,E,8 and W(y_E) tends to 36/85. The anchor 37 has W(37)=8/37. Taking E=2k gives the single-modulus quadratic-height obstruction. Taking k=8 modulo 18, E=k(k+1), and n=2^k y_E satisfies both moduli at log-height k^2+2k+O(1). The coordinator checked the additional divisibility by nine needed after clearing the inverse numerator. Thus the leading constant one on the k^2 scale cannot be increased in this statement.

This is a rigidity theorem, not the missing positive lower estimate. A large collection of ordinary predecessors in a progression need not contain one with sufficiently few odd departures in this paired class. The current agent work is testing that actual existence question separately.

Four new Std-only Lean roots check merge length, ancestry of every original token through an arbitrary merge history, the coefficient inequality, and rigidity of the cleared two-evaluation cone. The initialization, final singleton, size margins, and whole Collatz conclusion remain written arguments.

## 3. A Subspace-Theorem estimate on the native source window

[NATIVE_AFFINE_RECTANGLES.md](../../research/astra-wild-nine-hour-20261128/outside/NATIVE_AFFINE_RECTANGLES.md) proves a uniform arithmetic spacing estimate for A=3^s/2^t, with independently varying 0<=s<=t. Applying the two-dimensional Subspace Theorem to (h3^s,k2^t), where k is a nonzero nearest integer, gives h||hA||>exp(-epsilon t) eventually for every 1<=h<2^t. The real and finite-place factors cancel exactly. A fixed exceptional rational line either stays a positive distance from the diagonal or is the impossible exact diagonal. The zero-nearest-integer case is retained separately as h^2 A.

Continued fractions turn that estimate into absolute rectangle discrepancy exp(o(t)). A genuinely small slope can have one large first denominator. Its short final remainder traverses less than one circle, so its error is O(1+w/A), with the arc width w retained. The later convergent blocks each have bounded grid error and subexponentially bounded multiplicity. The displayed uniform inequality is valid even when the slope shrinks exponentially; the explicit first-denominator term then matters.

The real consumer retains each ordinary source's own actual Collatz word. Physical integrality gives

\[
K(n)/2^t\equiv -n3^{s(n)}/2^t\pmod1.
\]

An arbitrary prescribed arc for each grade can therefore be counted by discarding the grade-selection condition and summing only over t+1 grades. There is no factor 2^t from separately summing all words. The homogeneous floor nA>=c makes the sum of the width-sensitive first-denominator errors O(X max(w_s)) over the original source octave. Uniform reciprocal packing supplies this floor on every simple positive segment. At a supplied terminal integer y, the same product bound permits only O(1) grades on the octave. The resulting anti-concentration remains a statement before conditioning on arrival at y.

The coordinator checked the reciprocal-packing proof: good low-odd-count k-step images land below H/2 and are distinct on the simple segment; the bad words occupy only O(H^{H_2(3/5)}) source residues. Iterating the resulting count inequality gives a uniform reciprocal sum. This is credited as the established packing mechanism, not presented as a new global orbit theorem.

[RATIONAL_SOURCE_SIEVE.md](../../research/astra-wild-nine-hour-20261128/outside/RATIONAL_SOURCE_SIEVE.md) uses the same bound to compare a genuine rational binary source with accurate real probes. Subexponential probe heights and endpoint denominators make their cleared difference a subexponential integer multiplier. An exponential endpoint approximation is impossible unless that difference is zero. This works at arbitrary sparse dates. A three-dimensional version handles fixed algebraic fractional phases. A shared script can still approximate every positive ordinary probe on separate positive-lower-density schedules; its binary source is irrational and the schedules are pairwise eventually disjoint.

The exact classical interface is independently sourced. [Corvaja–Zannier, JTNB 17 (2005)](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.517.pdf), printed p.738, records Pourchet's rational-power antecedent; the integral-vector Subspace Theorem is on printed p.741. [Bilu, Astérisque 317 (2008), Theorem 2.3](https://www.numdam.org/item/AST_2008__317__1_0.pdf), printed p.4, permits algebraic coefficients at each chosen place and gives finitely many proper rational exceptional subspaces. The coordinator retrieved both statements. Their deep proofs and any outside formalizations were not rebuilt here. The onset is ineffective, and the finite controls do not claim to verify it numerically.

The missing global consumer is explicit. These estimates constrain the fractional affine intercept. A proof must still show that a positive-density escaping component forces it into arcs whose total width is small enough. Compact-null correction support alone does not do this after multiplication by a moving large terminal height, and fixed-root nonatomicity does not supply that concentration.

## Formal and publication evidence

All five included project Lean modules and all thirteen registered public roots were freshly compiled and then separately imported, type-checked, and axiom-audited under strict serialized flags. Only `propext`, `Classical.choice`, and `Quot.sound` occur. Cached matching third-party objects were reused. No cold dependency rebuild or independent LeanChecker run is claimed. The new infinite theorems above are written proofs.

Checkpoint 3 was published at `1a4fe2af42ecab3aba5b0ca29c64b3b6558852f1`, exact tree `412ef8110a673404887bae990196a630cd0bf793`, matching local `9fc154850f5a55e66847cc73f3587756acd8d8f2`. Its clean checkout validator passed with empty stderr and stdout SHA-256 `232e04d876fb750c17d09cfd3a2ef9e33c92fabf3f1f7b1aaf19f2a27e6fa9fe`. The published branch was independently read back at that commit. Repository integrity does not certify the mathematics.
