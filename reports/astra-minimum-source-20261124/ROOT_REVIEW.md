# Coordinator review: the original minimum source

## Verdict and scope

**VERIFIED at the stated elementary and kernel boundaries; universal closure OPEN.** The reviewed object is the new `research/astra-minimum-source-20261124/` packet. Its final source manifest and clean-commit execution are bound in the replay receipt. This verdict does not extend to every theorem in the source PRs or to a universal successful descent selector.

Four GPT-6.2 Astra agents were used in this continuation: three initial research lanes and a fresh final attempt on the surviving branch. The coordinator separately reconstructed the five-case induction, actual-basin reduction, the `-21 mod 8192` row, and the adaptive source normalization. The mathematical checks below are independent of agreement among agents.

## Reconstruction of the minimum

The domain is positive ordinary integers, with the shortcut map. `Good n` is literally `∃ h, run h n = 1`. The zero-step boundary of invariance is handled: when n=1, its next state 2 reaches 1. Thus the basin label is invariant on actual edges in both directions.

If no positive odd tripling disagreement existed, the complete smaller-source table and induction would make every positive label equal to that of 1. A positive counterexample therefore supplies a nonempty ordinary set; `Nat.find` constructs its least member q. Both orientations and all ternary valuations are included. No hypothetical unitality is inserted into the minimum.

I checked each table edge, the integral and odd smaller value, and its strict inequality at every nonbase residue. The only comparison sources are n/3, (4n-1)/9 and (8n+1)/9. Each is odd and satisfies 9v≤8n+1. The induction at n≤q has v<n≤q, so the queried equality is available. The larger cutoff has 9v≤8n+1<9q and retains its strict boundary. Consequently q itself is good and 3q is bad. Every smaller odd triple is good; an induction stripping twos proves the same for smaller even multiples of three. `MinimumFailure.lean` includes this final even-multiple step in its compiled theorem.

In particular 9q≤8N+1 for every positive counterexample N, and q<N for the least one. A cutoff proof with ≤ in place of < would be invalid; the packet does not make that change. This minimum removes the former obligation to keep every replacement prime to three, but it does not permit a comparison at q itself.

## Component-preserving rows

For q=8192t-21 and x=6912t-17, t≥1, I derived the row from the literal signed reference paths and independently replayed positive parameters 1,2,3,4,17,1000 and 10^20. The lower path has five steps and three odd inputs. The tripled replacement path has eight steps and three odd inputs. The original upper path has thirteen steps and six odd inputs. Both upper endpoints are exactly 2187t-5. The strict difference q-x=1280t-4 is positive; x is always a positive odd ternary unit. The subsequent Lean proofs use positive bases and cover every parameter. The signed references are only a device for finding those words.

I separately checked the swapped row q=3007+4374t, x=2815+4096t by actual traces, including a parameter 10^20. The endpoints are reversed: T^12 x=T(3q), T^12(3x)=Tq. The difference is 192+278t. The unit restriction t≠2 mod3 is needed only for the older unit minimum; the new odd minimum licenses every t. The universal lift is kernel checked.

The common-cycle contraction uses individual hitting clocks of the known reference a and 3a. Sufficient binary precision is max(3,t+2,s+2), not just the lower-arm clock. This produces x=a+3(q-a)/4. All positivity, parity and unit statements have the displayed hypotheses. It does not assume arbitrary a and 3a converge.

An early proposed row h=18, base=232103, p=10, s=13, g=4, endpoint 52283 was discarded: its required original-source congruence fails modulo 3 because 2^4·52283 is 2 modulo 3, whereas 3q+1 is 1. No result in the packet uses that row. A failure of a restricted synchronous landing menu was also not promoted to a general obstruction: the unequal-clock `-21` row explicitly resolves its previously troublesome mixed class.

## Adaptive original-source checks

For n=3q=3^h w=2^m a-1 with h≥3, z=2^h w-1<q follows from 3·2^h<3^h, not from an asymptotic estimate. The h-step all-odd identity reaches n-1. Also n+1 is good for every m≥1 because its one-step image is Tq. If 3^m a is 1 mod4, the adjacent exponent endpoints physically merge and the bad component has the representative z<q.

On the other side, h≥3 and m≥3 give U=(3^(m-1)a-1)/4. The residue makes this integral; 3∤a follows from n+1≡1 mod3. Then (4U+1)/9=3^(m-3)a has exactly the required ternary valuation and no dyadic factor. Substitution into the earlier canonical formula gives B(U)=2^m a-1=n. Its parent is good because 4U is in the component of n-1; its child is in the original bad component. Thus N≤B(U)=3q<3N on this stated branch. This is not a global replacement of the earlier canonical bound for every failed source.

The renewal lane's complementary row has s=147+256t. Literal paths from s-1 and 9s-1 meet at 47+81t after eight steps, with four and two odd inputs. For the actual factorization at depth m≥2, (3q-3)/4 reaches s-1 and is positive and below q on the specified class. This is a true-exit test at an unbounded clock. Neither this row nor the first parity test covers every possible exit.

## Further second-run proof

The final fresh lane supplied a positive reduction inside the remaining first-exit branch. I independently checked its arithmetic, its actual clocks, the CRT existence argument, and the imported actual-basin hypotheses. When m is 1,2,3, the parent U=(3^(m-1)a-1)/4 has 0<U<q; the inequality reduces to (4·2^m-3^m)a>1, whose coefficient is respectively 5,7,5. It is essential that the formal minimum covers every smaller multiple of three, since U need not be odd. The known good integer is 3U, while the bad next odd state is y=6U+1. If y+1=2^ell b and 3^ell b=1 mod4, the adjacent endpoint merger gives exact clocks m+ell+3 and ell+1 from 3q and 3U.

I independently replayed q=1485: n=4455, m=3, a=557, h=4, U=1253, y=7519, ell=5, b=235. Both actual paths reach 14276. I also constructed and replayed fifteen CRT combinations with ell=7,8,9,12,17 and h=3,4,8. Each has the exact two valuations and s=3a=199 mod256, rather than the earlier class 147. The congruences have coprime moduli; extending their one positive solution gives infinitely many ordinary inputs with the same guards. The actual-basin Lean theorem itself requires no unproved CRT assumption. The family construction remains a written argument. The opposite second-exit residue and m≥4 are not discharged.

## Latest PR201 and the missing inequality

I read the new exact-row argument at PR201 `2978d84f8a1fda9083593b26c6bf724d5976d859`, `escape-analysis/README.md`, including its actual suffix and two-gap correction. Its exponential family has total shortcut clock 2b. On any such path in a bad component, telescoping gives x=v·4^b/∏(3+1/y_i). All bad odd inputs satisfy y_i≥5, so x≥v(5/4)^b. Our minimum gives v>q. At b≥5 these sources are larger than 3q. Thus neither the multiplicity nor relaxing the source residue to 0 mod3 creates a smaller bad root on that row. I do not infer an opposing estimate for PR201's maximum from this observation.

The remaining obligation is pointwise at one fixed q: force an actual good representative or a smaller bad multiple/odd disagreement on every surviving branch. The complete minimum theorem gives a stronger premise for that attack; the descent families do not discharge its universal quantifier. The final verification documents exact proof and execution scope and does not label the conjecture solved.
