# The product-topology sequence version of Béhani's Collatz transfer

**Proposed theorem O11.** Equip the space of all complex sequences indexed by the quotient degrees `n ≥ 3` with its usual product Fréchet topology. The shortcut Collatz transfer is linearly topologically conjugate to a countable product of unilateral backward shifts. This answers Question 4.4 of V. Béhani, *Linear dynamics of an operator associated to the Collatz map*, Proc. Amer. Math. Soc. 152 (2024), 1191–1206, under this topology. The question itself specifies the sequence space, without naming a topology; its preceding sentence identifies the quotient coordinates as n≥3. The zero coordinate matters if all nonnegative degrees are retained.

## A triangular change of coordinates

Write `T(n)=n/2` at even n and `T(n)=(3n+1)/2` at odd n. On all sequences indexed by `I={3,4,...}` define
```
(Ac)(a) = sum of c(j) over j in I with T(j)=a.
```
Each row has at most two terms, so A is continuous in the product topology. For the finite-coordinate linear functionals e_a(c)=c(a), algebraic transposition gives
```
A'e_a = e_(2a) + e_((2a-1)/3) if the second child exists in I,
A'e_a = e_(2a) otherwise.
```
The even child is the unique largest index, with coefficient one. More generally, if a nonzero finite functional has largest index d and leading coefficient b, its image under A' has largest index 2d with coefficient b. Consequently f_(u,k)=(A')^k e_u has largest index 2^k u with coefficient one.

Take the root indices U consisting of 4 and all odd integers at least 3. Every integer in I is uniquely 2^k u with k nonnegative and u in U. For powers of two, take u=4. The finite functionals f_(u,k) form a basis of the finitely supported coordinate dual. Linear independence follows by inspecting the largest leading index in a finite relation. Spanning follows by successively removing the largest nonzero index in a finite functional. This argument uses only finite sums.

The map
```
J(c)(u,k) = f_(u,k)(c) = (A^k c)(u)
```
is a linear topological isomorphism from the entire product to the product of copies of the one-sided sequence space indexed by U. Its coordinates are finite sums. The triangular basis expresses each e_n as a finite combination of the f_(u,k), giving continuous inverse coordinates. Equivalently, a prescribed output array gives each c(n) recursively by increasing n, with diagonal coefficient one. It satisfies `J(Ac)(u,k)=J(c)(u,k+1)`.

## Consequences

Every complex scalar lambda is an eigenvalue. In shift coordinates the full eigenspace consists of `x(u,k)=lambda^k d(u)`, with d an arbitrary sequence indexed by U (using the zeroth power 1 at lambda=0). In contrast the continuous transpose has no eigenvalue, by strict growth of the largest coordinate of every nonzero finite functional. The full spectrum is the complex plane under the usual definition by failure of continuous linear invertibility.

The transfer is topologically mixing. Given two nonempty cylinder opens, sufficiently large shifts separate the coordinate restrictions, so their required values can be prescribed simultaneously. Periodic arrays are dense since any finite coordinate requirements extend to a periodic array by taking a period larger than all time-coordinate differences. The product of independent, identically distributed nondegenerate standard complex Gaussians is invariant and strongly mixing for the common time shift. Its full support follows from the cylinder basis, and strong mixing follows first for finite-coordinate events by independence at large lags, then for Borel events by approximation. Pullback through J gives a full-support Gaussian probability with these properties for A. Birkhoff's theorem applied to a countable basis yields frequent hypercyclicity. These statements do not assume that ordinary Collatz orbits terminate.

For the unreduced space indexed by all positive integers, use all positive odd u, including 1, in the same triangular basis. The same classification and conclusions hold. If the index 0 is included, `(Ac)(0)=c(0)` and no other row uses c(0). The full system splits as the scalar identity times the positive-index shift system. Every orbit then has constant zeroth coordinate, which precludes hypercyclicity and topological mixing on the full space. The quotient or convention therefore has concrete dynamical content.

Source: <https://arxiv.org/pdf/2303.03203>, Section 4, Question 4.4. The conjugacy above is specific to the unrestricted sequence space in the product topology. On a normed subspace its inverse may fail to preserve the space.
