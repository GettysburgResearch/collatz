# Mixing two-place countermodels and finite positive shadows

**PROPOSED.** This file constructs countermodels to suggested proof steps, not counterexamples to Collatz. Its purpose is to prevent the occupation route from silently replacing fixed-source arithmetic by stationary local statistics.

## A1. A coherent 2-adic/3-adic stationary model

Take a two-sided independent sequence `(a_j)_{j in Z}` with

`P(a_j=b)=q(1-q)^(b-1)`, b>=1, 0<q<1.

At time zero define

`x_2=-sum_{j>=0} 2^(a_0+...+a_(j-1))/3^(j+1)` in Z_2,

where the empty sum is zero, and

`x_3=sum_{j>=1} 3^(j-1) 2^(-(a_(-1)+...+a_(-j)))` in Z_3.

The first series converges because its 2-adic valuations tend to infinity, and is odd. The second converges because its 3-adic valuations tend to infinity, and is a unit. Direct reindexing gives

`3x_2+1=2^a_0 x_2(shift a)` and

`x_3(shift a)=(3x_3+1)/2^a_0`.

The first successor is odd, so a_0 is exactly v_2(3x_2+1), not an externally inconsistent valuation label. Therefore the joint law is invariant for

`F(x,y)=(U(x),(3y+1)/2^a(x))`.

Past and future labels are independent, so the time-zero joint law is a product of its 2-adic and 3-adic marginals. The joint system is a factor of the two-sided Bernoulli shift and hence mixing. The 2-adic marginal has full support, since every finite valuation word has positive probability and its cylinders shrink to points. It is non-atomic and singular to Haar when q!=1/2, by the distinct almost-sure mean valuation (or the distinct shortcut odd-bit frequency).

In particular choose q=2/3. The mean valuation is 3/2<log_2(3), so the formal multiplicative log drift is positive: `ln(3)-(3/2)ln(2)>0`. This supplies a coherent mixing local model satisfying the escape cost constraint. It is **not** a positive ordinary orbit, and no random valuation law is transferred to a fixed ordinary source.

The 3-adic series and iid geometric framework are classical in the q=1/2 case: Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Section 1.4, Remark 1.13 and its ancient-iteration footnote, https://arxiv.org/html/1909.03562 . The present biased extension is proved directly above; no claim of priority is made for it.

## A2. Exact finite 3-adic laws, without an exponent cutoff

At modulus `3^ell`, the powers of two have period `P=2*3^(ell-1)`. The exact total probability for the exponent class b modulo P, with 1<=b<=P, is

`w_b=q(1-q)^(b-1)/(1-(1-q)^P)`.

These weights sum to one. Thus the infinite transition law is represented exactly, not by truncating unlikely large valuations. Starting from the sole residue modulo one, apply `(3y+1)/2^b` with these weights to obtain the next-level distribution. Multiplication by three makes this independent of the chosen lift of the preceding residue. The resulting laws are projectively consistent and stationary at each level.

The checker verifies this for q=1/2 and q=2/3 through modulus 81, including exact self-stationarity under the full aggregated kernel. As a control, q=1/2 modulo nine reproduces the probabilities with numerators `(0,8,16,0,11,4,0,2,22)` and denominator 63 from Tao's Section 1.4. These checks concern model laws, not empirical laws of arbitrary integers.

## A3. Every finite joint observation has large positive ordinary witnesses

Fix any actual finite F-orbit segment in the profinite model, with valuation word `(a_0,...,a_(K-1))`, total A, desired 2-adic precision R>=1 at every displayed state, and 3-adic precision ell. Require a positive integer n to have the same initial residues as the model modulo `2^(A+R)` and `3^ell`. The Chinese remainder theorem gives one class modulo their product and arbitrarily large positive representatives.

Division by the successive powers of two loses at most A bits; multiplication by three is a 2-adic unit. Hence every such n has the displayed valuation word and matches all K+1 states at precision R. At the ternary place division by two is a unit, so all states also match modulo `3^ell`. Finally each real iterate obeys

`n_j=(3^j n+C_j)/2^(a_0+...+a_(j-1)) >= n/2^A`,

with C_j>=0. Choosing the representative n>=H*2^A keeps every state at least H, for any prescribed H. Thus even exact joint residue consistency plus an arbitrarily high finite real floor does not rule out these local models.

For R=1, a valuation word of length K has the single initial odd residue

`r=(2^A-C_K) 3^(-K) mod 2^(A+1)`,

where `C_0=0`, `C_(j+1)=3 C_j+2^(a_0+...+a_(j-1))`. The checker tests this formula independently against inverse branches and ordinary forward replay. It also constructs 9,438 joint positive witnesses, with every displayed state at least 10^20, for all words over {1,2,3} of lengths 1 through 5 and every unit ternary residue through modulus 27. The experiment tests R=1; the general-R conclusion is the mathematical argument above, not an exaggerated computation-coverage claim.

## A4. Occupation-level finite shadows

There is a sequence of finite positive ordinary trajectory segments, all of whose states tend uniformly to infinity with the segment index, whose joint profinite empirical laws converge to the q=2/3 invariant law of A1.

Proof. Choose a generic point of the mixing model. List the countably many finite residue-cylinder indicators. For the first j indicators, choose a trajectory length K_j whose empirical averages approximate their expectations within 1/j. Apply A3 at enough precision to reproduce all of those indicators throughout this finite segment, and choose the real floor H_j tending to infinity. A diagonal argument gives the claimed weak convergence on the compact product space.

The initial integer changes with j and may become enormous. This is not an orbit of one fixed ordinary integer. It proves that even a limiting sequence of high-floor, increasingly long, fully legal positive segments can produce a stationary biased model without providing an all-time ordinary source. No bound on the least compatible source is supplied.

## A5. An exact arithmetic bound when concentration contains repetitions

There is a source-sensitive certificate for one structured subclass. Let a nonempty valuation word w have length k, total A, and affine map

`U^k(n)=(P n+C)/Q`, with `P=3^k`, `Q=2^A`, C>0,

on its legal cylinder. Put `D=Q-P`, which is a nonzero odd integer. Its periodic 2-adic realizer is `x_*=C/D`. Because the word is a sequence of contracting inverse branches, this realizer is odd and has infinite valuation word www... .

If an ordinary positive source n legally repeats w exactly r times, its valuation cylinder agrees with that of x_* modulo `2^(rA+1)`. Consequently

`2^(rA+1) divides D n-C`.

There are precisely two cases. If `D n=C`, the block really closes: `U^k(n)=n`, a positive cycle. This exception must not be removed. Otherwise

`2^(rA+1) <= |D n-C| <= |D| n+C`.

In the expanding case P>Q, positivity excludes the cycle exception and gives the stronger signed lower bound

`n >= (2^(rA+1)-C)/(P-Q)`.

For w=(1), this reads `n>=2^(r+1)-1` and is attained. For w=(1,2), it reads `n>=2^(3r+1)-5`, again attained. Thus these finite expanding shadows require exponentially increasing starting integers; they do not stabilize on a fixed positive source. This is an explicit height consequence of the classical full-denominator periodic realizer formula, not a new cycle-exclusion theorem.

The checker tests the defect divisibility, the source bound, ordinary legality, and retained positive-cycle exceptions for every word over {1,2,3,4} of lengths 1 through 5, one through four repetitions, and two lifts of each cylinder. This is a finite check of the general proof, not coverage of all words.

The useful remaining bridge would turn the diffuse collision concentration of E4 into repetitions strong enough to violate this source bound, or into another equally source-sensitive arithmetic obstruction. Low entropy alone does not establish such repetitions: the biased independent models already show why an entropy deficit is not the same as near-periodicity. No such bridge is claimed here.

## What is refuted, and what remains worth attacking

The following inference is refuted: 'a counterexample occupation limit is invariant, mixing, non-atomic, has all finite local words available, and is compatible at both primes 2 and 3; therefore it must be Haar or have subcritical residue concentration.' A1 supplies the biased stationary model, while A3--A4 show why finite positive-integer consistency does not repair the inference.

A source-specific recurrence estimate from E5 in CONCENTRATION.md is not refuted: the model has no demonstrated fixed positive integer source. Arithmetic control of that fixed source is exactly the missing ingredient. The model also does not refute a genuinely quantitative regularity assumption such as a suitable L^p cylinder bound; it violates the low-growth bounds at issue.

This is a broader occupation-model version of the repository's ordinary-realization warning, not a discovery that finite compatibility is sufficient. It should be used as an adversarial test harness for proposed regularity theorems, not as evidence of a divergent orbit.
