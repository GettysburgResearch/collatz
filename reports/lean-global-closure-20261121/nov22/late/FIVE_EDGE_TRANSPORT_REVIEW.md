# Independent review: exact five-edge transport

Date: 2026-11-22. Reviewer: global_analytic22.

**Verdict: VERIFIED within the written theorem's stated scope.**

Reviewed source:

* agent22_certificate/FIVE_EDGE_TRANSPORT.md
* SHA256 0ffaa8cc0a361aa1b9ad69c3c55a5ca4009350eaa97aa07262a0195096118c40

This review reconstructs the new written mathematics. It does not add a
Lean audit, revalidate upstream analytic hypotheses, or claim a bound for
the particular canonical Green potential. This final review includes the
accelerated-map and killed-domain extension, reconstructed after the
earlier shortcut-only version. Its basin selector is proved by elementary
integer lifting and imports no arithmetic-progression sufficiency theorem.

## Exact recurrence and domain

For even input, simultaneous shortcut transport sends a five-pair to
another five-pair. For odd input \(n\), the transported pair is
\((5q-2,q)\), with \(q=(3n+1)/2\) and reciprocal weight
\(1/n=3/(2q-1)\). This gives the exact whole-positive recurrence, with
the coefficient \(1/2\) on its even part.

For odd ternary-unit inputs the two source classes are \(1,5\pmod6\).
Their target classes are respectively \(2,8\pmod9\), so the restricted
energy has no even-input term. The statements are valid for extended
nonnegative sums. They concern absolute differences, not squares.

## Affine slopes and routing

All four parity/offset entries in the two transport tables follow from
substitution into the ordinary shortcut definition. The odd-offset
entries have slopes \(15\) and \(5/3\) relative to the transported base.

For \(k=3m\), the signed templates \(-1\) and
\(-5,-7,-10\) have respectively \(k\) and \(2m\) odd inputs. The finite
ordinary lift therefore gives

\[
T^k(2^kv-1)=3^kv-1,\qquad
T^k(5(2^kv-1))=5\,3^{2m}v-5.
\]

Both initial ordinary arguments are positive for the stated \(m,v\ge1\);
their actual forward trajectories remain positive. The source does not
assume convergence of a signed trajectory. Its reference to
CollatzSignedCarry.finite_signed_lift has the correct namespace.

The resulting leading ratios \(5/3^m\) are distinct. An affine type with
a different slope intersects a fixed parameter ray at at most one
parameter. A finite collection cannot cover every ray.

A word in finitely many translated-five generators and their legal
inverses has slope \(5^a\) for an integer \(a\). Matching a transported
ray would require \(5=5^a3^m\), impossible for \(m\ge1\). There are only
finitely many bounded-length words, and each can serve at most one
parameter on such a ray. The theorem properly leaves unbounded routing
with a possible weighted-congestion argument open.

## Failure of a general uniform energy bound

For \(v\in30\mathbb N_{>0}\), both \(n=2^kv-1\) and \(5n\) are odd
ternary units. The endpoint \(q=3^kv-1\) is also an odd ternary unit
and is \(4\pmod5\). Therefore the point mass \(f=\mathbf1_{\{q\}}\)
has exactly \(E_5(f)=1/q\).

The lifted \(n\)-trajectory reaches \(q\) exactly at time \(k\) in the
prefix \(0,\ldots,k\). Every state of the lifted \(5n\)-trajectory in
that prefix is \(0\) or \(3\pmod5\), so none equals \(q\). The single
original energy base \(n\) therefore gives

\[
\frac{E_5(f\circ T^k)}{E_5(f)}\ge\frac qn>(3/2)^k,
\qquad
\frac{E_5(A_{k+1}f)}{E_5(f)}
\ge\frac{q}{(k+1)n}>\frac{(3/2)^k}{k+1}.
\]

Finite inverse depth under the ordinary shortcut map preserves finite
support, so every displayed energy is finite. The source correctly
states that the test function changes with the averaging time. The
argument disproves a uniform operator bound for all finitely supported
inputs; it does not prove growth for one fixed input or refute a
canonical-potential-specific estimate.

## Direct accelerated transport and the exact killed domain

The new accelerated argument uses a distinct ray and its own clock.
For \(n=2^{2k}v-1\), \(q=3^k2^kv-1\), and \(0\le j\le k\), I checked

\[
U^j(n)=3^j2^{2k-j}v-1,
\qquad
U^j(5n)=5\,3^j2^{2k-j-\lfloor j/2\rfloor}v+s_j,
\]

where \(s_j=-5\) for even \(j\) and \(-7\) for odd \(j\).
The signed odd template has halving gaps \(1,2\), so its accumulated
shortcut clock is \(j+\lfloor j/2\rfloor<2k\). The finite positive
lift therefore preserves every intervening parity and the odd
endpoints; the halving gaps are exact. The first ray hits \(q\) only
at time \(k\), while the second avoids \(q\) modulo five throughout
the prefix. This gives the stated exponential ratios for actual
\(U\)-powers and \(U\)-Cesàro averages.

The accelerated pullbacks have infinite fibers in general. The source
does not claim that these pullbacks retain finite support. Each legal
inverse has \(x=(2^a q-1)/3\), and \(1/x\le6/(2^a q)\).
Summing the larger set of all \(a\ge1\) gives the correct row bound
\(6/q\). Tonelli and \(E_5(h)\le6\|h\|_{\mathrm{harm}}\) then establish
finiteness of every energy used in the lower-bound argument.

I independently reconstructed the constructive selector in Section 5.2.
The binomial induction gives

\[
16^{3^{r-1}}\equiv1+5\,3^r\pmod{3^{r+1}}.
\]

If \(7\,2^b+1=3^r c\), replacing \(b\) by
\(b+4j3^{r-1}\) changes the quotient modulo three to
\(c-5j\equiv c+j\). Choosing \(j\equiv-c\pmod3\) lifts divisibility
by one power of three and preserves \(b\equiv1\pmod4\).
The base \(b=1,r=1\) is valid. Thus this is a complete elementary
construction, not a presumed distribution of positive Collatz orbits.

For \(r=2k+2\), the selected

\[
v=\frac{2(7\,2^b+1)}{3^{2k+1}}
\]

is divisible by 2, 3, and 5. The extra factor of three comes from the
chosen divisibility power; the factor of five comes from
\(2^b\equiv2\pmod5\). Hence it is a positive multiple of 30.
The additional positive odd prefix satisfies

\[
U^k(q)=3^{2k}v-1=\frac{7\,2^{b+1}-1}{3}.
\]

The next halving gap is exactly \(b+1\), reaching 7. The displayed
tail \(7,11,17,13,5,1\) has gaps \(1,1,2,3,4\). Therefore the full
ordinary words supplied for \(q\) and \(n\) reach one. Since both
exceed one, neither can be periodic under \(U\).

Finally, full \(U\)-pullbacks of the point mass at this nonperiodic
\(q\) equal the zero-extended killed pullbacks: once a trajectory
reaches any periodic vertex, it cannot later visit \(q\). This remains
true if \(5n\) itself is periodic. Thus the final amplification
inequalities apply to the same killed composition operator \(C\)
used in the canonical Dirichlet note, with the same odd-unit
absolute-value five-energy and finite energies.

## Scope conclusion

The exact recurrence, infinitely many slopes, bounded-word obstruction,
and exponential lower bounds follow from the actual positive maps,
with separate proofs for shortcut time, accelerated time, and the
accelerated killed domain. No missing population hypothesis, implicit fixed-time
limit exchange, or omitted source collision was found. The final
discussion correctly distinguishes a squared energy along ordinary
orbit edges from the absolute five-energy across potentially different
components.
