# D-9302 — Adelic natural extension and integer section

**Claim ID:** D-9302  
**Title:** The real and 2-adic survivor codings form one exact `{2,3,infinity}`-solenoid orbit  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `D-9301`; elementary quotient and recurrence algebra  
**Scope:** conceptual natural extension of the `64 -> 81` subsystem; direct reformulation of M1  
**Related counterexample candidates:** none

## Statement

Let

\[
R=\mathbb Z[1/6],
\qquad
\mathbb X_S=
(\mathbb R\times\mathbb Q_2\times\mathbb Q_3)/\Delta R,
\]

where

\[
\Delta R=\{(r,r,r):r\in R\}.
\]

Put

\[
\beta=\frac{81}{64},
\qquad
\rho=\beta^{-1}=\frac{64}{81},
\qquad
d=\frac{17}{81}.
\]

Because `beta` is a unit of `R`, coordinatewise multiplication by `beta` induces an automorphism

\[
\alpha:\mathbb X_S\longrightarrow\mathbb X_S.
\]

Define

\[
\omega=[(d,d,0)]\in\mathbb X_S
\]

and, for `epsilon in {0,1}^N`,

\[
\Phi(\varepsilon)
 =\sum_{t\ge0}\varepsilon_t\alpha^{-t}\omega.
\]

Then:

1. the series converges and has the exact representative
   \[
   \boxed{
   \Phi(\varepsilon)
   =[(x_\infty(\varepsilon),x_2(\varepsilon),0)],
   }
   \]
   where
   \[
   x_\infty(\varepsilon)
   =\sum_{t\ge0}d\varepsilon_t\rho^t\in[0,1],
   \qquad
   x_2(\varepsilon)
   =\sum_{t\ge0}d\varepsilon_t\rho^t\in\mathbb Z_2;
   \]
2. the coding obeys the exact affine shift relation
   \[
   \boxed{
   \Phi(\sigma\varepsilon)
   =\alpha\Phi(\varepsilon)
    -\varepsilon_0\alpha\omega,
   \qquad
   \alpha\omega=[(17/64,17/64,0)];
   }
   \]
3. define the ordinary-integer section
   \[
   \mathcal I=
   \{[(x,n,0)]:0\le x\le1,\ n\in\mathbb Z\}.
   \]
   Then
   \[
   \boxed{
   \Phi(\varepsilon)\in\mathcal I
   \iff x_2(\varepsilon)\in\mathbb Z;
   }
   \]
4. if
   \[
   A=x_2(\varepsilon)\in\mathbb Z,
   \]
   then every tail
   \[
   A_k=x_2(\sigma^k\varepsilon)
   \]
   is an ordinary integer and satisfies
   \[
   \boxed{
   A_{k+1}=\frac{81A_k-17\varepsilon_k}{64};
   }
   \]
5. the real and integer coordinates satisfy the exact orbit identity
   \[
   \boxed{
   A_k
   =\beta^k\bigl(A-x_\infty(\varepsilon)\bigr)
    +x_\infty(\sigma^k\varepsilon).
   }
   \]
   Consequently, if `A >= 2`, then `A_k -> +infinity` exponentially.

Thus the issue-#4 integer-survivor question is the diagonal-intersection problem

\[
\boxed{
\Phi(\{0,1\}^{\mathbb N})\cap\mathcal I.
}
\]

The all-zero and all-one sequences give the trivial intersections represented by `(0,0,0)` and `(1,1,0)`. Finding any point with integer coordinate `A >= 2` would give a divergent orbit of the induced `64 -> 81` system; translating it to an ordinary Collatz counterexample still requires the independently checked chart-class condition from issue #4.

## Definitions

`X_S` is the customary `{2,3,infinity}` S-arithmetic solenoid. Compactness of this quotient is standard background but is not used in the algebraic identities below.

The local absolute values of `beta` are

\[
|\beta|_\infty=\frac{81}{64}>1,
\qquad
|\beta|_2=64>1,
\qquad
|\beta|_3=\frac1{81}<1.
\]

Their product is `1`. This is the hyperbolic product-formula geometry motivating the word *adelic*.

The same rational series is evaluated in two different completions. `x_infinity` and `x_2` are not assumed equal as real numbers; they share only their rational digit formula.

## Motivation

The 2-adic attractor alone hides the archimedean obstruction “is this 2-adic point one finite ordinary integer?” The real coding alone has no obstruction because it fills `[0,1]`. The solenoid records both completions and the shared itinerary simultaneously.

This formulation offers two ambitious routes:

1. prove that the symbolic stable leaf meets the ordinary-integer section only at the trivial endpoints;
2. construct a nontrivial intersection and thereby obtain an explicit induced divergent orbit.

It also identifies the Fourier cusp in `L-9301` as the dual shadow of a hyperbolic S-arithmetic orbit rather than an arbitrary triangular array.

## Proof or construction

### The automorphism

The units of `R=Z[1/6]` include every signed power product of `2` and `3`. Since

\[
\beta=3^4 2^{-6},
\]

both `beta` and `beta^(-1)` preserve `R`. Coordinatewise multiplication therefore preserves the diagonal subgroup `Delta R` and induces the automorphism `alpha` on the quotient.

### Convergence and coordinates

One has

\[
\alpha^{-t}\omega
 =[(d\rho^t,d\rho^t,0)].
\]

In the real coordinate, `rho^t -> 0` because `0<rho<1`. In the 2-adic coordinate,

\[
|\rho|_2=\frac1{64}<1.
\]

The third coordinate is identically zero. Hence the series converges in the product before passing to the quotient and has the stated representative.

Moreover,

\[
0\le x_\infty(\varepsilon)
\le\sum_{t\ge0}d\rho^t
=\frac{d}{1-\rho}
=1.
\]

The 2-adic coordinate is exactly `pi_2(epsilon)` from `D-9301`.

### Shift relation

Splitting off the first term gives

\[
\Phi(\varepsilon)
 =\varepsilon_0\omega+\alpha^{-1}\Phi(\sigma\varepsilon).
\]

Multiplying by `alpha` yields

\[
\Phi(\sigma\varepsilon)
 =\alpha\Phi(\varepsilon)-\varepsilon_0\alpha\omega.
\]

Finally,

\[
\beta d
 =\frac{81}{64}\cdot\frac{17}{81}
 =\frac{17}{64},
\]

which gives the displayed representative of `alpha omega`.

### Integer section

If `x_2(epsilon)=n in Z`, the displayed representative of `Phi(epsilon)` already lies in `I`.

Conversely, suppose

\[
[(x_\infty,x_2,0)]=[(y,n,0)]
\]

with `n in Z`. Equality in the quotient means that for some `r in R`,

\[
(x_\infty-y,x_2-n,0)=(r,r,r).
\]

The third coordinate forces `r=0` in `Q_3`. Hence `x_2=n`. The 3-adic coordinate has removed all diagonal-representative ambiguity.

### Integral tail recurrence

Assume `A_0=A=x_2(epsilon)` is an ordinary integer. By `D-9301`,

\[
A_k\equiv\varepsilon_k\pmod{64}
\]

whenever `A_k=x_2(sigma^k epsilon)`. The series identity gives

\[
A_k=d\varepsilon_k+\rho A_{k+1}.
\]

Solving for the tail,

\[
A_{k+1}
=\beta A_k-\beta d\varepsilon_k
=\frac{81A_k-17\varepsilon_k}{64}.
\]

The congruence `A_k ≡ epsilon_k (mod 64)` makes the numerator divisible by `64`, so induction proves that every `A_k` is an ordinary integer.

### Real/integer orbit identity

The real tails obey the same affine recurrence:

\[
x_\infty(\sigma^{k+1}\varepsilon)
=\beta x_\infty(\sigma^k\varepsilon)
 -\frac{17}{64}\varepsilon_k.
\]

Subtracting this from the recurrence for `A_k` gives

\[
A_{k+1}-x_\infty(\sigma^{k+1}\varepsilon)
=\beta\bigl(A_k-x_\infty(\sigma^k\varepsilon)\bigr).
\]

Iteration yields

\[
A_k-x_\infty(\sigma^k\varepsilon)
=\beta^k(A-x_\infty(\varepsilon)),
\]

which is the claimed identity.

If `A >= 2`, then `x_infinity(epsilon) <= 1`, so

\[
A-x_\infty(\varepsilon)\ge1.
\]

Since the tail real coordinate is nonnegative,

\[
A_k\ge\beta^k\longrightarrow+\infty.
\]

QED.

## Dependency audit

- `D-9301` supplies the 2-adic coding, first-digit congruence, and tail shift.
- All solenoid identities are direct quotient algebra.
- The translation from a suitable `A` to a positive Collatz starting integer is not reproved here; it remains a branch-qualified issue-#4 dependency.
- No measure-rigidity, mixing, entropy, or homogeneous-dynamics theorem is invoked.

## Gap audit

- The solenoid reformulation is exact but does not make the integer-section intersection easy.
- Generic orbit-mixing results would not automatically apply to this zero-3-adic-coordinate symbolic stable leaf.
- A nontrivial ordinary integer in `V` must also satisfy one of the chart congruence classes needed for the current Collatz translation.
- The real coordinate in `[0,1]` is not an independent random variable; it is locked to the same digit itinerary as the 2-adic coordinate.
- Compactness of `X_S` is not used as a black box to infer recurrence or intersection.
- Negative ordinary integers may also lie in the section; the divergence conclusion above is stated only for `A >= 2`.

## Adversarial tests

- All-zero digits give `Phi=[(0,0,0)]` and the fixed zero tail.
- All-one digits give `x_infinity=x_2=1`, so `Phi=[(1,1,0)]` and the fixed one tail.
- If two section representatives with third coordinate zero differ by a diagonal element, that element must be zero; this checks the key uniqueness step.
- For a finite-prefix sequence followed by zeros, both coordinates are the same rational number, but it is generally not an ordinary integer. This shows that rationality alone is not the M1 condition.

## Remaining uncertainty

The construction and orbit identity are complete-looking. A reviewer should audit the exact issue-#4 induced-map digit convention and the chart-class translation before using the final divergence sentence in Collatz coordinates.

## Suggested next attack

Study the set

\[
\Phi(\Omega)\cap\mathcal I
\]

as an S-arithmetic shrinking-target or diagonal-intersection problem. Any proposed rigidity theorem must explicitly accommodate the shared symbolic itinerary and the special third coordinate, rather than invoking generic positive-entropy measure rigidity by analogy.
