# Trying to turn controlled pair fusion into an actual Collatz proof

**A positive proof attempt with an exact finite obstruction.** The underlying map throughout this note is the genuine shortcut map. No changed map, simulated fresh orbit, or unproved independence of component labels is used. The attempt was to make the summable-boundary argument close by replacing its artificial translations with genuine, certified orbit mergers. The finite lemma below identifies why the most direct replacement fails. It does not rule out source-dependent arithmetic control after the finite binary window.

## 1. The proposed closing mechanism

The [prior sibling zero-one theorem](DYADIC_BOUNDARY_ZERO_ONE.md) would give full convergence if the actual component-boundary fractions on dyadic shells were summable. Papers [212](https://rstation.ai/problems/collatz/papers/212/v1) and [225](https://rstation.ai/problems/collatz/papers/225/v1) obtain exponentially contracting **controlled** pair processes: occasional affine replacements change one arm's effective odd count in a direction that reduces the gap. Their replacements are charged to the places where the coloring changes. That charge is essential; the controller does not already consist entirely of ordinary Collatz edges.

The attempted upgrade was:

1. Choose a replacement with the needed nonzero odd-count effect.
2. Certify that the replaced and original values belong to the same actual component by a finite ordinary merger.
3. Retain the controller's negative drift while treating every replacement as color-preserving.

If these steps were available on the controller's current binary cylinders with the claimed fresh-bit law and a bounded certification cost, the resulting exponential fusion tail would supply summable shell variation and close the proof. The problem is the simultaneous demand for a nonzero odd-count effect, a complete finite merger certificate, and still-unread fair bits.

## 2. A finite martingale identity on an actual binary cylinder

At some fixed common depth, let the two current values be affine functions of an unread positive integer,

\[
 X(z)=u+3^A z,\qquad Y(z)=v+3^Bz,
\]

and put \(g=B-A\). Work on complete finite binary periods of the unread integer; if necessary translate those periods upward so that every actual state under consideration is positive. After exposing each new low bit, reparametrize the remaining high part. Both slopes are still odd powers of three.

Let \(\Delta_i\) be the difference between the two effective odd counts after \(i\) further **ordinary synchronous** steps, including the initial difference \(g\). Conditional on any exposed prefix, each arm's next parity is fair. They need not be independent. Their difference \(\xi_i\) lies in \(\{-1,0,1\}\), and

\[
 \mathbb E(\xi_i\mid\text{prefix})=0,
 \qquad \mathbb E(\xi_i^2\mid\text{prefix})\le1.
\]

This is an exact count on the two possible next bits. Therefore, on every complete depth-\(t\) period,

\[
 \mathbb E\Delta_t=g,\qquad
 \mathbb E\Delta_t^2\le g^2+t.                                  \tag{1}
\]

No assertion about independent arm parities or about a natural-density limit is required.

An **affine fusion** means equality of the two entire endpoint affine functions, so that it certifies a merger for every positive completion of that prefix. Equality of their slopes then implies equality of their effective odd counts. Let \(\tau\) be the first such fusion date. Subsequent common steps retain equality, so \(\Delta_t=0\) on \(\{\tau\le t\}\). Cauchy–Schwarz and (1) give the finite inequality

\[
 |g|=|\mathbb E(\Delta_t\mathbf1_{\{\tau>t\}})|
 \le\sqrt{(g^2+t)\Pr(\tau>t)},
\]

and hence, whenever \(g\ne0\),

\[
 \boxed{\qquad \Pr(\tau>t)\ge\frac{g^2}{g^2+t}.\qquad}          \tag{2}
\]

In particular the current cylinder cannot be completely certified by any finite common merger deadline. In the consistent infinite fair-bit model, (2) also forces infinite expected certification time. Almost-sure eventual fusion is compatible with that fact. The sharper polynomial tail theory is part of [Leen's synchronization manuscript](https://doi.org/10.5281/zenodo.23268751); (2) is only the elementary finite obstruction needed for this attempted controller.

The zero-initial-gap case does not provide an escape for distinct affine forms. If \(A=B\) and \(u\ne v\), expose a fixed word making both arms halve \(\nu_2(|u-v|)\) times. Their offset then becomes odd, so the next parities differ and the effective gap is \(+1\) or \(-1\). This word has fixed positive cylinder probability. Applying (2) conditionally thereafter gives \(\Pr(\tau>t)\ge c/(t+1)\) for some comparison-dependent \(c>0\) and all sufficiently large \(t\). Thus **every pair of distinct such affine forms has infinite expected ordinary affine-fusion time**. This elementary conclusion is weaker than the existing sharp tail results and is used here only to audit the proposed certification cost.

## 3. Why finite lookahead does not remove the obstruction

One can refine a current cylinder to smaller cylinders that have complete ordinary merger certificates. What cannot be retained for free is the original conditional law at the earlier cut. If the earlier effective difference is \(g\ne0\), the later zero difference on certified refinements must be balanced by the uncertified refinements in (1). Ignoring those refinements discards the signed odd-count contribution that makes the conditional mean equal to \(g\).

This is the first unsupported step in the proposed full proof: after selecting on a future merger certificate, treating all of its determining bits as still fresh would reintroduce a false conditional expectation. Waiting for a complete certificate also lacks a finite mean bound in the nonzero-gap fair-bit state, by (2). The controlled process in the cited papers obtains its drift by charging genuine color-changing replacements; it cannot simply delete that charge because ordinary pairs eventually fuse on a density-one set.

The distinction is not merely between a finite and an infinite computation. A density-one merger statement gives no summable error automatically. The charging argument runs many prefix tests on each dyadic shell, and its input size and multiplicity losses must both be paid. This is exactly where the prior papers retain a comparison-dependent logarithmic exponent.

## 4. Independent clocks still require a specific ordinary source

Allow the two future clocks to be \(r\) and \(s\). On a fixed pair of parity cells, the endpoint slopes on the original unread variable are

\[
       3^{A+a}/2^r,
       \qquad 3^{B+b}/2^s.
\]

An affine identity forces \(r=s\) and \(A+a=B+b\), by unique factorization. If either condition fails, the endpoint difference is a nonconstant affine function and has at most one ordinary zero. Thus bounded independent-clock searches add only finitely many isolated completions to the finitely many identity cells. They cannot certify every completion of a still nonzero-gap cylinder. The [finite affine uniqueness kernel](BoundaryEnergy.lean) checks the underlying two-point algebra; the factoring lane gives the broader multiplier version.

This does **not** preclude a source-specific ordinary merger whose clock grows with the source. The new [semiprime representative reduction](../SEMIPRIME_REPRESENTATIVES.md) is exactly such a construction: an actual integer is fixed first, and its finite merger is found by arithmetic search. There is no fixed-cylinder or uniform-clock promise. Such certificates can evade the affine identity obstruction, but no bound obtained in this pass makes their costs summable across all source shells.

## 5. Two additional closing attempts and their first missing input

**A terminal return estimate.** A random-walk bridge can have a smaller survival probability than an unrestricted excursion, suggesting a summable count of adjacent sources that reach different small targets. That suggestion cannot be used without a full-component condition. The genuine visit-to-five indicator has exact halving, exists in a nontrivial natural density, and therefore has infinite harmonic boundary by the prior zero-one lemma. Its single exceptional edge is precisely where a fixed-target label ceases to describe a full component. A bound based only on two capped arrivals would also apply to the [one-edge calibration](ONE_EDGE_COLLISION_SPLIT.md), which rigorously splits the collision mass. A successful estimate must use what happens after the minima, not merely that the minima or marked arrivals are small.

**A least-component mass comparison.** If a least bad component began at height \(m\), its mass could be compared with a tail of the minimum law. The explicit Mazur formal witness inspected by the root lane has the form \(1/(256r\,3^{132rC})\), with a chosen predecessor seed \(r\) and fixed mixing constant \(C\). This is a separate fixed-target positive lower bound, not a uniform polylogarithmic floor in \(m\). It is too small to contradict the available super-polylogarithmic minimum-law upper tails. No missing inequality between those quantities was supplied by this pass.

The formula follows directly from `eta / (32 * U.parentSourcePotential)`, `U.parentSourcePotential = r`, `eta = 9*(2/3)/(16*3^m)` and `m = 132*r*C+1` in `GeneralTargetPositiveDensity.lean`, from the [original version 1.1 source archive](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/positive-lower-density-collatz-predecessors-v1.1-source.zip). The inspected module has SHA-256 `5e23daa11fc9bd22ce0bc6d303ce8f56057aa8a194e8a201f8404521ed31b667`. This is a source inspection, not a claim of a complete fresh rebuild of the imported development.

## What remains open after this attempt

The actual odd equation has not yielded a summable component-boundary estimate. The useful surviving direction is an **ordinary, source-dependent** control theorem with quantitative cost or a canonical moving-target density theorem. Both must distinguish full component fate from a finite exceptional terminal label. The finite identities above locate the cost that an attempted controller must account for; they are not a proof that all such controllers are impossible and not a substitute for the missing one-eighth lower bound.
