# Guarded dilation correlations and an explicit failed rigidity closure

**22 November 2026. Status: UNSUCCESSFUL CLOSING ATTEMPT.**

This pass tried to apply two specific structure theorems to the actual
invariant escape label: Rudolph's positive-entropy multiplication
rigidity, and Frantzikinakis's structure theorem for strongly stationary
systems. It obtained no exclusion of an escaping ordinary orbit and no
new Lean theorem.

The concrete deductions are an exact finite-depth correlation identity
for every bounded Collatz-invariant label, and an explicit positive
continuous probability density showing that the resulting averaged
dilation equation does **not** imply the separate dilation invariances
needed for the proposed applications. The control is a probability
model, not a Collatz-invariant ordinary sequence or a Collatz
counterexample.

## 1. Actual input and normalization

Use the shortcut map

\[
 T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

Let \(f:\mathbb N_{>0}\to[0,1]\) satisfy \(f(Tn)=f(n)\) exactly.
The intended application is PR182's actual extended canonical escape
label \(\widetilde F\), which is zero on eventually periodic
components and positive on escaping components under that source's
qualified analytic inputs. It obeys

\[
 f(2m)=f(m),\qquad f(2m+1)=f(3m+2).
 \tag{1.1}
\]

The source used here is PR182 at full head
`9dacd610ba7735e89e2e29e4ab01795983317980`:

- [CANONICAL_ESCAPE_LABEL.md](https://github.com/GettysburgResearch/collatz/blob/9dacd610ba7735e89e2e29e4ab01795983317980/research/lean-dyadic-descent-20261121/CANONICAL_ESCAPE_LABEL.md),
  the ordinary component label and its exact invariance;
- [INVARIANT_CORRELATION.md](https://github.com/GettysburgResearch/collatz/blob/9dacd610ba7735e89e2e29e4ab01795983317980/research/lean-dyadic-descent-20261121/INVARIANT_CORRELATION.md),
  polynomial-phase rigidity P1, with its stationary-density and FLOOR
  inputs, and the separate LOG input where pointwise constancy is inferred.

Those source assumptions are retained, not re-certified here. Sections
2--4 need only (1.1) until they explicitly introduce a statistical
hypothesis. Section 5 uses the source-qualified polynomial correlation
result. This attempt targets escape exclusion; it does not settle
nontrivial cycles.

Write

\[
 L_X a=\frac1{H_X}\sum_{n\le X}\frac{a(n)}n,
 \qquad H_X=\sum_{n\le X}\frac1n.
\]

For fixed bounded continuous tests \(\phi_1,\ldots,\phi_d\) and
nonnegative integral offsets \(\mathbf h=(h_1,\ldots,h_d)\), set

\[
 P_{\mathbf h}(n)=\prod_{i=1}^d\phi_i(f(n+h_i)),\qquad
 A(\mathbf h)=\lim_j L_{X_j}P_{\mathbf h}.
\]

All limits below are taken along one subsequence on which the stated
countable collection of bounded averages converges. For the associated
process law, choose tests from a countable dense family and extend by
uniform approximation. Fixed changes of the cutoff by a multiplicative
constant change a bounded logarithmic average by \(o(1)\).

For \(q\ge1\), let

\[
 B_r^q(\mathbf h)
   =\lim_j\frac1{H_{X_j}}\sum_{m\le X_j}
      \frac{P_{\mathbf h}(qm+r)}m.
 \tag{1.2}
\]

Omitting a finite number of nonpositive arguments is harmless. These are
normalized conditional residue averages, so

\[
 B_r^q(\mathbf h)
 =q\lim_j L_{X_j}
       \bigl(1_{n\equiv r\ (q)}P_{\mathbf h}(n)\bigr),
 \qquad
 \frac1q\sum_{r=0}^{q-1}B_r^q(\mathbf h)=A(\mathbf h).
 \tag{1.3}
\]

The logarithmic change of variables gives (1.3): replacing
\(1/(qm+r)\) by \(1/(qm)\) contributes a bounded unnormalized
error, and \(H_{X/q}/H_X\to1\).

## 2. The exact multipoint residue term

Splitting the average of \(P_{2\mathbf h}\) according to the parity
of its base point, (1.1) gives

\[
 \boxed{
 A(2\mathbf h)
   =\tfrac12 A(\mathbf h)
      +\tfrac12 B_2^3(3\mathbf h).
 }
 \tag{2.1}
\]

Indeed, on the even branch every argument is \(2(m+h_i)\). On
the odd branch every argument is \(2(m+h_i)+1\), whose label is
\(f(3m+3h_i+2)\). Thus the odd contribution is one specified
ternary residue average, not the unrestricted average at offsets
\(3\mathbf h\).

Define its actual error by

\[
 E_2^3(\mathbf h)=B_2^3(\mathbf h)-A(\mathbf h).
\]

Then

\[
 2\bigl(A(2\mathbf h)-A(\mathbf h)\bigr)
   =A(3\mathbf h)-A(\mathbf h)+E_2^3(3\mathbf h).
 \tag{2.2}
\]

In Fourier form, with \(e(t)=\exp(2\pi i t)\),

\[
 E_2^3(\mathbf h)
 =\sum_{a=1}^2 e(-2a/3)
      \lim_j L_{X_j}\bigl(e(an/3)P_{\mathbf h}(n)\bigr).
 \tag{2.3}
\]

This is the arithmetic coupling the one-point argument does not
estimate. With one coordinate, PR182's correlation theorem applied to
\(\phi(f)\), followed by a fixed translation, eliminates (2.3).
For two or more coordinates, \(P_{\mathbf h}\) is generally not a
Collatz-invariant label. Applying the one-point theorem to that product
would insert an unproved hypothesis.

There is also an exact finite-depth version. For each
\(0\le r<2^k\), let \(s_k(r)\) be the number of odd steps in
the first \(k\) shortcut iterates in that residue class, and put
\(c_k(r)=T^k(r)\), extending \(T(0)=0\). The usual affine
iterate identity is

\[
 T^k(2^km+r)=3^{s_k(r)}m+c_k(r).
\]

All offsets \(2^kh_i\) follow the same first \(k\) parity bits.
Consequently

\[
 \boxed{
 A(2^k\mathbf h)
 =2^{-k}\sum_{r=0}^{2^k-1}
    B_{c_k(r)}^{3^{s_k(r)}}(3^{s_k(r)}\mathbf h).
 }
 \tag{2.4}
\]

Parity words of length \(k\) are in bijection with residues modulo
\(2^k\), so their odd-step counts have binomial multiplicities.
Writing \(E_r^q=B_r^q-A\), (2.4) becomes

\[
 A(2^k\mathbf h)
 =2^{-k}\sum_{s=0}^k {k\choose s}A(3^s\mathbf h)
    +\mathcal E_k(\mathbf h),
 \tag{2.5}
\]

\[
 \mathcal E_k(\mathbf h)
 =2^{-k}\sum_{r=0}^{2^k-1}
     E_{c_k(r)}^{3^{s_k(r)}}(3^{s_k(r)}\mathbf h).
 \tag{2.6}
\]

Formula (2.6) is an explicit averaged error, rather than an unnamed
mixing assumption. The attempted cancellation did not prove it small.
It receives terms from typical parity words, not only the rare all-odd
word. One-point residue uniformity supplies no estimate for these
shifted products.

## 3. Even cancelling every error does not give strong stationarity

Let \(\mu\) be a stationary law on sequences, and let
\(D_q(x)_j=x_{qj}\) denote decimation. If every multipoint error in
(2.1) vanished, the resulting full law identity would be

\[
 (D_2)_*\mu=\tfrac12\mu+\tfrac12(D_3)_*\mu.
 \tag{3.1}
\]

It is tempting to read (3.1) as invariance under both decimations. The
following explicit control disproves that inference, even for a
stationary Boolean process.

### A positive continuous density with the averaged equation

On the circle \(\mathbb T\), define

\[
 \rho(t)=1+\frac19\sum_{j,k\ge0}
       \left(\frac23\right)^j\left(\frac13\right)^k
       \cos(2\pi 2^j3^k t),
 \qquad d\nu(t)=\rho(t)\,dt.
 \tag{3.2}
\]

The series is absolutely and uniformly convergent. Its total absolute
amplitude is at most

\[
 \frac19\frac1{1-2/3}\frac1{1-1/3}=\frac12.
\]

Therefore \(\rho\) is continuous, \(1/2\le\rho\le3/2\), and
\(\nu\) is a probability measure. Unique factorization makes all
positive frequencies \(2^j3^k\) distinct. With
\(\widehat\nu(n)=\int e(-nt)\,d\nu(t)\),

\[
 \widehat\nu(0)=1,\qquad
 \widehat\nu(\pm2^j3^k)
   =\frac1{18}\left(\frac23\right)^j
                       \left(\frac13\right)^k,
 \tag{3.3}
\]

and every other nonzero Fourier coefficient is zero. Thus for every
integer \(n\),

\[
 \widehat\nu(2n)
   =\tfrac12\widehat\nu(n)+\tfrac12\widehat\nu(3n).
\]

Uniqueness of Fourier coefficients of finite measures gives

\[
 (\times2)_*\nu=\tfrac12\nu+\tfrac12(\times3)_*\nu.
 \tag{3.4}
\]

But \(\widehat\nu(2)=\tfrac23\widehat\nu(1)\ne
\widehat\nu(1)\). Neither separate multiplication invariance follows.

### A stationary Boolean process with every averaged identity

Choose \(U\) uniformly on \(\mathbb T\), independently of
\(\Theta\sim\nu\), and put

\[
 X_n=1_{[0,1/2)}(U+n\Theta),\qquad n\in\mathbb Z.
 \tag{3.5}
\]

This process is stationary because shifting time replaces \(U\) by
\(U+\Theta\), which is still conditionally uniform given
\(\Theta\). Decimating by \(q\) replaces \(\Theta\) by
\(q\Theta\). The law depends linearly on the distribution of
\(\Theta\), so (3.4) proves (3.1) for the **whole process law**,
including every order of correlation. Iteration also gives the binomial
average in (2.5) with zero error.

Nevertheless it is not strongly stationary. To see this quantitatively,
the nonzero Fourier coefficients of
\(b=1_{[0,1/2)}-1/2\) have squared magnitude
\(1/(\pi^2m^2)\) for odd \(m\), and zero for nonzero even
\(m\). Hence

\[
 \operatorname{Cov}(X_0,X_h)
   =\sum_{m\ne0}|\widehat b(m)|^2\widehat\nu(mh).
\]

Using (3.3), the only contributing positive odd \(m\) for
\(h=1,2,3\) are \(3^k\). The geometric sums give

\[
 \operatorname{Cov}(X_0,X_1)=\frac3{26\pi^2},\quad
 \operatorname{Cov}(X_0,X_2)=\frac1{13\pi^2},\quad
 \operatorname{Cov}(X_0,X_3)=\frac1{26\pi^2}.
 \tag{3.6}
\]

The pair law changes under decimation by two. This is a control of the
proposed inference from the averaged identities; no claim is made that
(3.5) satisfies the exact ordinary Collatz equations or all of PR182's
source-qualified conclusions.

## 4. The precise higher-order theorem attempted

The primary source is Nikos Frantzikinakis,
[*The Structure of Strongly Stationary Systems*](https://arxiv.org/pdf/math/0403453),
Definition 3.1 and Theorem 6.6; Theorem 3.6 records Jenvey's ergodic case.
Strong stationarity requires equality of all finite-dimensional laws
under **each** integral decimation. Theorem 6.6 identifies almost every
ergodic component as a product of a Bernoulli system and a totally
ergodic inverse limit of nilsystems. It does not assert that the whole
system is ergodic. Jenvey's conclusion that an ergodic strongly
stationary system is Bernoulli therefore cannot be applied separately
to those components without more hypotheses.

The attempt fails before that theorem can be invoked: (2.6) was not
controlled, and even its complete vanishing supplies (3.1), which the
explicit control shows is weaker than strong stationarity.

There is a further independent limitation. A random variable \(C\)
with any nontrivial law gives the stationary sequence \(X_n=C\) for
all \(n\). It is strongly stationary and has zero shift entropy.
Its ergodic components are one-point systems, compatible with the
structure theorem. Thus even obtaining strong stationarity and zero
entropy would not by themselves eliminate a surviving invariant color.
An ergodicity or ordinary-label measurability argument would still have
to come from the arithmetic.

## 5. Why positive-entropy multiplication rigidity sees only the base

The second primary source is Daniel J. Rudolph,
[*\(\times2\) and \(\times3\) invariant measures and entropy*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/64243AD8323B37089540F911F8CC77EB/S0143385700005629a.pdf/2_and_3_invariant_measures_and_entropy.pdf),
*Ergodic Theory and Dynamical Systems* **10** (1990), 395--406,
DOI [10.1017/S0143385700005629](https://doi.org/10.1017/S0143385700005629).
For relatively prime multipliers, it requires a Borel probability
measure invariant under both maps and ergodic for their generated
semigroup. Positive entropy of either multiplication forces Lebesgue
measure. The averaged relation (3.4) meets neither the separate
invariance requirement nor its intended conclusion.

For the repository's actual label, the source-qualified polynomial
correlation result makes the relevant projection issue even more
explicit. Fix an irrational \(\alpha\), and form the actual joint
empirical measures

\[
 \gamma_X=\frac1{H_X}\sum_{n\le X}\frac1n
                    \delta_{(n\alpha\bmod1,f(n))}.
\]

Suppose \(\gamma_{X_j}\) converges to \(\gamma\), and denote
its label marginal by \(\pi\). For every continuous \(\psi\)
on \([0,1]\), the label \(\psi\circ f\) is again exactly
Collatz invariant. Although P1 is stated for Boolean labels, its use
here has an elementary extension: partition \([0,1]\) into finitely
many intervals and uniformly approximate \(\psi\) by a step function
on that partition. Each fiber indicator of \(f\) is an exactly
invariant Boolean label, so P1 applies to every term. The uniform
approximation error bounds its logarithmic-average error independently
of \(X\); taking that error to zero proves the assertion for
\(\psi\circ f\), including complex \(\psi\). This gives, for
\(k\ne0\),

\[
 \int e(kx)\psi(t)\,d\gamma(x,t)
 =\lim_jL_{X_j}\bigl(e(k\alpha n)\psi(f(n))\bigr)=0.
\]

For \(k=0\) the integral is \(\int\psi\,d\pi\). Fourier
density and uniform approximation therefore prove the exact
source-qualified consequence

\[
 \boxed{\gamma=H_{\mathbb T}\otimes\pi.}
 \tag{5.1}
\]

So the compact base is already Haar, independently of which label law
\(\pi\) remains. Applying multiplication rigidity to that base
cannot determine \(\pi\). On the product model the two formal
maps \((x,t)\mapsto(2x,t)\) and \((x,t)\mapsto(3x,t)\)
preserve (5.1), but any nontrivial label event is invariant. The
extension is not semigroup ergodic when \(\pi\) is not a point
mass. These formal product actions must not be confused with a proved
ordinary identity \(f(3n)=f(n)\).

Moreover, (5.1) yields

\[
 \operatorname{Var}_{\gamma}(t\mid x)
       =\operatorname{Var}_{\pi}(t).
\]

Thus a nonconstant limiting label is precisely **not** a measurable
function of that compact base. Each finite empirical measure is
supported on a graph, but its weak limit need not be. Using the former
fact to assert the latter would remove the entire unresolved label by
assumption.

## Outcome

The direct application of these deep theorems was attempted at their
actual hypotheses. It did not prove those hypotheses for the ordinary
escape label. The exact multipoint errors are (2.3) and (2.6); even
their complete cancellation gives only the weaker averaged equation,
whose proposed strengthening is refuted by (3.2)--(3.6). The actual
joint empirical product law (5.1) identifies the additional invariant
color that base rigidity leaves untouched.

All proofs in this note are written arguments. No theorem here is
reported as Lean checked, no existing validation receipt is relabeled,
and no full Collatz proof is claimed.
