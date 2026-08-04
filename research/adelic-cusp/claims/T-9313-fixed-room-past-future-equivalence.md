# T-9313 — Fixed-room past/future equivalence and exact minimum duality

**Claim ID:** T-9313  
**Title:** Ordinary survivors are fixed-room coherent paths, and finite Cantor minima transform exactly into finite survivor minima  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `D-9302`, `D-9303`, `L-9301`; elementary iteration of the tail recurrence  
**Scope:** exact reformulation and finite-depth certificates for the ordinary-integer section  
**Related counterexample candidates:** none

## 1. Prefix polynomial and fixed room

For a binary word

\[
w=(\varepsilon_0,\ldots,\varepsilon_{j-1})
\in\{0,1\}^j,
\]

define

\[
\boxed{
P_j(w)
=
17\sum_{t=0}^{j-1}
\varepsilon_t81^{j-1-t}64^t.
}
\tag{1}
\]

Suppose

\[
A=\Phi(\varepsilon)\in\mathbb Z_{\ge0}
\]

and write

\[
A_j=\Phi(\sigma^j\varepsilon)\in\mathbb Z_{\ge0}.
\]

Iterating

\[
64A_{k+1}=81A_k-17\varepsilon_k
\]

gives

\[
\boxed{
81^jA
=
64^jA_j+P_j(\varepsilon_0,\ldots,\varepsilon_{j-1}).
}
\tag{2}
\]

Thus

\[
\frac{64^jA_j+P_j}{81^j}
\]

is the **same fixed ordinary integer `A` at every depth**.

## 2. Past Cantor coordinate

Let

\[
\eta^{(j)}_r
=
\varepsilon_{j-1-r}
\qquad(0\le r<j)
\tag{3}
\]

be the reversed past word. Its finite triadic coordinate from `D-9303` is

\[
c_j(\eta^{(j)})
\equiv
-17\sum_{r=0}^{j-1}
\frac{81^r}{64^{r+1}}
\eta^{(j)}_r
\pmod{81^j}.
\tag{4}
\]

Multiplication by `64^j` gives

\[
64^jc_j(\eta^{(j)})
\equiv
-P_j(\varepsilon_0,\ldots,\varepsilon_{j-1})
\pmod{81^j}.
\tag{5}
\]

Equation `(2)` therefore implies

\[
\boxed{
A_j
\equiv
c_j(\eta^{(j)})
\pmod{81^j}.
}
\tag{6}
\]

The word-to-class map is injective, so the tail residue records the entire reversed past word.

At the same time, the future word

\[
(\varepsilon_j,\varepsilon_{j+1},\ldots)
\]

puts

\[
A_j\in V_\infty\cap\mathbb Z_{\ge0}.
\]

An ordinary itinerary is therefore a coherent intersection of a triadic past class, a `2`-adic future point, an archimedean window, and one fixed room quotient.

## 3. Archimedean window

Let

\[
x_j=x_\infty(\sigma^j\varepsilon)\in[0,1].
\]

The orbit identity in `D-9302` gives

\[
A_j
=
\left(\frac{81}{64}\right)^j(A-x_0)+x_j.
\]

Consequently

\[
\boxed{
\left(\frac{81}{64}\right)^j(A-1)+1
\le A_j
\le
\left(\frac{81}{64}\right)^jA.
}
\tag{7}
\]

For `A>=2`, every `A_j>1`.

If `A<64^j`, then `(7)` gives `A_j<81^j`, so `A_j` itself is the standard representative of its nontrivial class in `C_j`.

## 4. Converse: fixed-room paths are ordinary survivors

Conversely, fix an integer `A>=0`, a binary sequence `epsilon`, and nonnegative ordinary integers `(A_j)_(j>=0)` satisfying `A_0=A` and

\[
\boxed{
81^jA
=
64^jA_j+P_j(\varepsilon_0,\ldots,\varepsilon_{j-1})
}
\tag{8}
\]

for every `j>=1`.

The prefix polynomials satisfy

\[
P_{j+1}=81P_j+17\varepsilon_j64^j.
\tag{9}
\]

Subtracting `81` times `(8)` at depth `j` from `(8)` at depth `j+1` gives

\[
\boxed{
64A_{j+1}=81A_j-17\varepsilon_j.
}
\tag{10}
\]

Dividing `(8)` by `81^j` gives

\[
A
=
\sum_{t=0}^{j-1}
\frac{17\varepsilon_t64^t}{81^{t+1}}
+
\left(\frac{64}{81}\right)^jA_j.
\tag{11}
\]

In `Q_2`, the final term tends to zero because its `2`-adic valuation is at least `6j`. Hence

\[
\boxed{
A
=
\sum_{t\ge0}
\frac{17\varepsilon_t64^t}{81^{t+1}}
=
\Phi(\varepsilon)
\quad\text{in }\mathbb Z_2.
}
\tag{12}
\]

Thus fixed-room coherence is an exact ordinary-section characterization.

## 5. Infinite equivalence theorem

For an integer `A>=0`, the following are equivalent:

1. `A` belongs to the ordinary section of the survivor attractor;
2. there is a binary itinerary and an ordinary nonnegative tail sequence obeying `(10)` at every shift;
3. there is a binary itinerary and an ordinary nonnegative sequence satisfying `(8)` at every depth;
4. there is one coherent sequence of triadic past classes whose ordinary representatives obey `(7)`, whose predecessor maps recover one fixed room `A`, and whose futures remain in the survivor attractor.

The trivial paths are `A=0` with `000...` and `A=1` with `111...`. Every nontrivial path has `A>=2` and diverging integral tails.

## 6. Exact finite-depth duality

Let `R_j` be the standard depth-`j` survivor residue set in `[0,64^j)`, and let `C_j` be the standard triadic class set in `[0,81^j)`.

Fix a class `c in C_j` with low-to-high triadic word

\[
\eta=(\eta_0,\ldots,\eta_{j-1}),
\]

and put the chronological survivor word

\[
\varepsilon_t=\eta_{j-1-t}.
\]

Define

\[
X_j(\varepsilon)
=
\sum_{t=0}^{j-1}
\frac{17\varepsilon_t64^t}{81^{t+1}}.
\tag{13}
\]

The congruence defining `c` says that

\[
64^jc+P_j(\varepsilon)
\]

is divisible by `81^j`. Put

\[
\boxed{
A(c)
=
\frac{64^jc+P_j(\varepsilon)}{81^j}
=
\left(\frac{64}{81}\right)^jc+X_j(\varepsilon).
}
\tag{14}
\]

Then:

1. `A(c)` is an ordinary integer;
2. replaying the chronological word from `A(c)` gives `j` valid survivor steps and ends at the ordinary tail `c`;
3. the map `c -> A(c)` is exactly the coding bijection `C_j -> R_j` with the word order reversed;
4. for every nontrivial word,
   \[
   0<X_j(\varepsilon)<1,
   \]
   so
   \[
   \boxed{
   A(c)=\left\lceil c(64/81)^j\right\rceil.
   }
   \tag{15}
   \]

### Proof

Integrality is the defining congruence. Equation `(14)` is the fixed-room identity, so the recurrence replay follows by the same subtraction used in `(9)`--`(10)`. Word injectivity on both finite sets makes the correspondence bijective.

For a nontrivial finite word, the real prefix sum is strictly between `0` and the all-one finite sum

\[
1-(64/81)^j<1.
\]

Since `A(c)` is integral, `(15)` follows. QED.

## 7. Exact minimum identity

Define

\[
m_j=\min(C_j\setminus\{0,1\})
\tag{16}
\]

and

\[
M_j=\min(R_j\setminus\{0,1\}).
\tag{17}
\]

The ceiling map in `(15)` is nondecreasing. Therefore

\[
\boxed{
M_j
=
\left\lceil
m_j\left(\frac{64}{81}\right)^j
\right\rceil.
}
\tag{18}
\]

This is an exact identity, not merely a lower bound.

Consequences:

1. `M_(j+1)>=M_j`, because every `(j+1)`-step survivor is a `j`-step survivor;
2. every nontrivial infinite ordinary survivor satisfies
   \[
   \boxed{A\ge M_j}
   \tag{19}
   \]
   for every `j`;
3. the ordinary-section problem is equivalent to
   \[
   \boxed{M_j\longrightarrow\infty.}
   \tag{20}
   \]

Indeed, bounded `M_j` would give one bounded starting room with arbitrarily long deterministic survivor prefixes, hence an infinite ordinary itinerary; conversely an infinite room bounds every `M_j`.

## 8. Why this is the right post-EQ object

All-depth weighted EQ controls the full finite sets statistically. The sequence `M_j` asks for their first nontrivial ordinary point and is sensitive to one exceptional coherent path.

The triadic duality `(18)` turns that first-point problem into a meet-in-the-middle modular subset-sum minimum, enabling exact depths far beyond direct enumeration of all `2^j` survivor starts.

The remaining universal theorem can be stated in any of three equivalent forms:

- `M_j -> infinity`;
- `ceil(m_j(64/81)^j) -> infinity`;
- no fixed room supports coherent past/future equations at every depth.

## 9. Dependency audit

- `D-9302` supplies integral tails and real companion bounds.
- `D-9303` supplies the triadic class formula and word injectivity.
- `L-9301` supplies finite survivor word injectivity.
- The fixed-room identity, converse, ceiling transform, and minimum identity use exact arithmetic only.
- No equidistribution theorem or computation is needed for the abstract result.

## 10. Gap audit

- The theorem does not prove `(20)`.
- A finite exact value of `M_j`, however large, is not universal nonintersection.
- The chart translation from an induced room to an original Collatz seed remains branch-qualified.

## 11. Suggested next attack

Use exact dual minimization to extend certified `M_j` values, while seeking a structural lower bound on the **coherent** subset of `C_j`. Any proof that the coherent ceiling transform grows without bound closes the ordinary section.
