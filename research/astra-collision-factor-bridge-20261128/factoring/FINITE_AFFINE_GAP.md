# A finite-quotient gap bound for bounded Collatz affine charts

**Status.** The estimates below have complete elementary written proofs. They concern finite permutation kernels on odd residues; they are not a statement about every possible ordinary Collatz sampler. The parameters may grow, and their permitted range is explicit. No Lean formalization of trigonometric or spectral steps is claimed.

The motivation is the public reversible small-bias sampler in factoring PR #296:
[coverage-frontier-2026-11-27.md, pinned head](https://github.com/gfreund123/factoring-in-p/blob/2d451e192641f62531aca378f0dc34bcccb81adb/notes/coverage-frontier-2026-11-27.md).
Its modular exponents are cheap to evaluate. An ordinary path certificate has to pay for the unreduced arithmetic map and its actual itinerary.

The [multiplier rigidity theorem](MULTIPLIER_CERTIFICATE_RIGIDITY.md) shows that a nonconstant affine chart admitting two actual source mergers has positive slope in \(2^{\mathbb Z}3^{\mathbb Z}\). Among invertible affine maps of the binary integers, slopes of that form are \(3^r\). This note asks how much finite-residue expansion is possible from uniformly controlled such charts. To make the obstruction stronger, the estimates even permit negative slopes, which the two-source merger theorem itself does not license.

## 1. Conventions

Let \(Q=2^w\), \(w\ge3\), and
\[
U_Q=\{x\bmod Q:x\text{ is odd}\}
\]
with uniform probability. For a permutation \(g\) of \(U_Q\), set
\[
U_gf(x)=f(gx).
\]
Let \(\mu\) be any inverse-symmetric probability on a finite family of such permutations, and \(P=\sum_g\mu(g)U_g\). Define the Poincaré gap by
\[
\gamma(P)=\inf_{\substack{\mathbb Ef=0\\f\ne0}}
 \frac{\langle f,(I-P)f\rangle}{\|f\|_2^2}.
\]
This is zero for a disconnected kernel. No laziness assumption is required for this upper-gap problem. The exact Dirichlet identity is
\[
\langle f,(I-P)f\rangle
=\frac12\sum_g\mu(g)\|U_gf-f\|_2^2.                  \tag{G1}
\]

## 2. Multipliers alone: an exponentially small gap bound

Suppose every generator is
\[
g_{\epsilon,r}(x)=\epsilon3^r x\bmod Q,\qquad
\epsilon\in\{-1,1\},\quad r\in\mathbb Z.
\]
The exponent \(r\) denotes the **chosen unreduced ordinary exponent**, not a short modular name for it. Then
\[
\boxed{\displaystyle
\gamma(P)\le
 \frac{2\pi^2\,\mathbb E_\mu r^2}{2^{\,2(w-2)}}.}      \tag{G2}
\]
In particular, if \(|r|\le R\), replace \(\mathbb E r^2\) by \(R^2\).

**Proof.** The unit group is the direct product
\[
U_Q=\langle-1\rangle\times\langle3\rangle,\qquad
\operatorname{ord}_Q(3)=L=2^{w-2}.
\]
For completeness, the order follows from
\(v_2(3^{2^k}-1)=k+2\), \(k\ge1\), by squaring induction. The two factors are independent because powers of three are \(1\) or \(3\bmod8\), whereas \(-1\equiv7\bmod8\). Their sizes multiply to \(|U_Q|\).

Take the nontrivial character
\[
\chi(-1)=1,\qquad \chi(3)=e^{2\pi i/L}.
\]
It has mean zero and is an eigenfunction of \(P\), with real eigenvalue
\[
\lambda=\mathbb E_\mu\cos(2\pi r/L).
\]
Consequently
\[
\gamma(P)\le1-\lambda
\le\frac12\mathbb E_\mu(2\pi r/L)^2.
\]
This is (G2). Complex test functions are legitimate; alternatively take a nonzero real or imaginary part. \(\square\)

With positive multipliers alone, the two sign cosets are already disconnected. Formula (G2) remains nontrivial on a cyclic coset, and it continues to hold after granting the extra sign operation.

If the unreduced coefficients \(3^{|r|}\) have bit length at most \(B\), then \(R=O(B)\). A constant gap from multipliers alone therefore requires exponentially large ordinary exponent/bit cost in \(w\). Binary modular exponentiation can evaluate the same residue with only \(O(\log R)\) exponent bits. That computational saving does not produce an ordinary affine path with only \(O(\log R)\) odd steps.

## 3. Adding affine translations: a Fourier packet bound

Allow
\[
g(x)=\epsilon_g3^{r_g}x+b_g,\qquad
b_g=m_g/3^{s_g},                                      \tag{G3}
\]
reduced modulo \(Q\), with
\[
\epsilon_g\in\{-1,1\},\quad |r_g|\le R,\quad
0\le s_g\le S,\quad m_g\in2\mathbb Z,\quad |m_g|\le B.
\]
The even numerator makes the translation even modulo \(Q\), so every \(g\) permutes \(U_Q\). Assume the chosen family and weights are inverse-symmetric; the bounds \(R,S,B\) include the displayed representations of the inverses.

Choose integers \(J,m\) with
\[
J\ge\max(R,S),\qquad m\ge1,\qquad
3^{J+m-1+R}<Q/4.                                     \tag{G4}
\]
Then
\[
\boxed{\displaystyle
\gamma(P)\le\frac12
 \left(\frac{\pi R}{m+1}
       +\frac{2\pi B\,3^{J+m-1}}{Q}\right)^2.}         \tag{G5}
\]
A sharper form replaces the square on the right by its \(\mu\)-average with \(R,B\) replaced by \(|r_g|\) and \(|m_g|3^{-s_g}\), respectively.

### Proof

For integers \(j\), define
\[
c_j=
\begin{cases}
\sin\!\left(\dfrac{\pi(j-J+1)}{m+1}\right),
  &J\le j<J+m,\\
0,&\text{otherwise}.
\end{cases}
\]
Use the real Fourier packet
\[
f(x)=\sum_{j=J}^{J+m-1}c_j\cos(2\pi3^j x/Q).           \tag{G6}
\]

For uniform odd \(x\bmod Q\),
\[
\mathbb E e^{2\pi itx/Q}=0
\quad\text{unless }(Q/2)\mid t.
\]
Condition (G4) guarantees that all positive frequencies occurring in \(f\) or its multiplier shifts are distinct and below \(Q/4\). Their sums and nonzero differences cannot be divisible by \(Q/2\). Their cosine and sine functions are therefore mutually orthogonal, each of squared norm \(1/2\). In particular,
\[
\mathbb Ef=0,\qquad \|f\|_2^2=\frac12\sum_jc_j^2>0.    \tag{G7}
\]

First omit \(b_g\). The sign disappears inside cosine, and multiplication by \(3^{r_g}\) shifts the coefficient sequence by \(r_g\). The sine vector with zero boundary values obeys the exact discrete identity
\[
\frac{\sum_j(c_{j-1}-c_j)^2}{\sum_jc_j^2}
=2\left(1-\cos\frac{\pi}{m+1}\right)
\le\frac{\pi^2}{(m+1)^2}.                             \tag{G8}
\]
Telescope a shift of \(|r_g|\) positions and apply the triangle inequality in the coefficient \(\ell^2\) space. By orthogonality,
\[
\frac{\|f(\epsilon_g3^{r_g}\,\cdot)-f\|_2}{\|f\|_2}
\le\frac{\pi|r_g|}{m+1}.                             \tag{G9}
\]

Now restore the translation. Since \(j\ge J\ge s_g\),
\[
3^j b_g\equiv m_g3^{j-s_g}\pmod Q.
\]
Thus the phase added to frequency \(3^{j+r_g}\) is represented by the actual real number
\[
\phi_{g,j}=2\pi m_g3^{j-s_g}/Q.
\]
There is no unaccounted modular inverse in this formula. Orthogonality of the cosine/sine pairs gives
\[
\begin{aligned}
\|f(g\,\cdot)-f(\epsilon_g3^{r_g}\,\cdot)\|_2^2
 &=\sum_jc_j^2(1-\cos\phi_{g,j})\\
 &\le\frac12\left(\max_j|\phi_{g,j}|^2\right)\sum_jc_j^2.
\end{aligned}
\]
Using (G7),
\[
\frac{\|f(g\,\cdot)-f(\epsilon_g3^{r_g}\,\cdot)\|_2}
     {\|f\|_2}
\le\frac{2\pi |m_g|\,3^{J+m-1-s_g}}Q.                 \tag{G10}
\]
Combine (G9), (G10), and (G1), and use \(f\) in the variational definition of the gap. This proves both forms of (G5). \(\square\)

## 4. An explicit growing-parameter regime

Write \(q=\log_3Q\). Suppose
\[
R,S\le q/16,\qquad B\le Q^{1/16}.
\]
Set \(J=\max(R,S)\) and
\[
m=\lfloor q/2\rfloor-J-R-2.
\]
For sufficiently large \(Q\), \(m\ge1\), (G4) holds, and
\(m\ge3q/8-3\). Moreover \(3^{J+m-1}\le Q^{1/2}\). Therefore an absolute constant \(C\) gives
\[
\boxed{\displaystyle
\gamma(P)\le C\frac{R^2}{(\log Q)^2}
              +C\frac{B^2}{Q}.}                    \tag{G11}
\]
The statement is uniform in the number of generators and their probabilities; only the displayed chart budgets enter.

Consequences within this stated regime:

- A fixed finite family has \(\gamma(P)=O(w^{-2})\).
- If \(R=o(w)\), \(S\le(\log_3Q)/16\), and \(B\le Q^{1/16}\), then \(\gamma(P)\to0\).
- The proof does **not** rule out a positive gap when exponent/denominator/translation budgets consume a sufficiently large fraction of the available binary precision. It also does not apply to arbitrary state-dependent pieces, nonlinear residue permutations, or a kernel on changing state spaces.

The large-budget possibilities must be analyzed with their actual ordinary-height, itinerary and transport costs. They are not dismissed by this theorem.

## 5. Where the factoring transfer would have to improve

The small-bias construction in PR #296 uses reversible modular maps with efficient exponent-register arithmetic. Its proof is valuable for its stated factoring target. Restricting it to bounded global native affine charts changes the operator and its spectral gap; (G2) and (G5) quantify that change.

A tempting proposed Collatz argument would combine:

1. a positive spectral gap for the modular sampler;
2. a high-probability actual merger certificate for each sampled transition;
3. a Poincaré inequality for a component label.

The relevant quantity is the ratio of the failed-certificate mass to the **actual** gap of the lifted operator. For a fixed affine family, existing counted fusion estimates before the binary information horizon give an available upper failure estimate of order \(w^{-1/2}\). The gap above is at most order \(w^{-2}\). These bounds do not establish the needed failure \(o(\gamma)\). An upper bound on failure is not a lower bound, so this observation is not itself an impossibility theorem for sharper fusion estimates.

There are several mathematically distinct escape routes:

- construct genuinely growing certificates and prove their ordinary transport, rather than treating a modular reduction as a path;
- produce a sufficiently sharper weighted failure estimate for the small-gap operator;
- use a different state space with an independently verified height-preserving orbit dictionary;
- bypass the sampler and establish the full moving-residue/real-height profile in [POINTWISE_IMPORT_AUDIT.md](POINTWISE_IMPORT_AUDIT.md).

The companion [real high-state obstruction](../arithmetic/HIGH_STATE_AND_PROFILE_OBSTRUCTIONS.md) concerns a different object: doubly stochastic samplers on actual integers, with genuine undirected orbit certificates constrained to stay above a specified height. The present proof concerns finite odd-residue permutation kernels and explicitly tracks their rational affine coefficients. Neither result assumes the other.

## 6. Verification scope

The trigonometric proof above is exact. The accompanying [check_affine_gap.py](check_affine_gap.py) independently checks its finite Fourier-packet identities and Rayleigh bounds for a range of binary moduli, including rational ternary translations and negative exponents. Numerical checks are only a guard against indexing and sign errors; they do not replace the proof or establish asymptotic mixing.

The separate [check_lean.py](check_lean.py) validates the three algebraic merger-rigidity roots and their dependency closure. It does not formalize this spectral theorem.
