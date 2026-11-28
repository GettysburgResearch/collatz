# Exact spectral radius of the reciprocal-state operator

**WRITTEN, self-contained theorem; no Lean claim.** This is a short audit of
an outside operator claim, not a Collatz termination argument. It prevents
the present pass from importing an incorrect spectral input.

The audited source is James C. Hateley, *The Collatz Conjecture and the
Spectral Calculus for Arithmetic Dynamics*, Preprints 202511.1440, **v6,
28 January 2026**, equations (1), (3), (7), (11), and Theorem 5.41(2).
[Versioned primary source](https://www.preprints.org/manuscript/202511.1440/v6).
The paper defines the raw map

\[
 C(n)=\begin{cases}n/2&2\mid n,\\3n+1&2\nmid n,\end{cases}
 \qquad (Pf)(n)=\sum_{C(m)=n}\frac{f(m)}m
\]

and the norm \(\|f\|_\sigma=\sum_{n\ge1}|f(n)|n^{-\sigma}\).
Its later claimed nonzero fixed vector in a space embedded in this
weighted \(\ell^1\) is incompatible with these definitions.

## Theorem

For every \(\sigma>0\), this literal operator is bounded on
\(\ell^1_\sigma\) and has spectral radius **exactly \(1/2\)**.
In particular it has no nonzero fixed vector there, or in any vector
subspace contained in it on which the operator has the same meaning.

**Proof.** Positivity and the one-destination structure give the exact
column formula

\[
 \|P^k\|_\sigma
 =\sup_{m\ge1}\frac{m^\sigma}{(C^k m)^\sigma}
                   \prod_{j=0}^{k-1}(C^j m)^{-1}.
 \tag{1}
\]

This also proves boundedness at \(k=1\), since \(Cm\ge m/2\).
For every \(a\ge1\),

\[
 a\,C(a)\,C^2(a)\ge8.\tag{2}
\]

If \(a\) is odd the product is \(a(3a+1)^2/2\ge8\).
If \(4\mid a\) it is \(a^3/8\ge8\). Otherwise write
\(a=2b\) with \(b\) odd; it is \(2b^2(3b+1)\ge8\).
Grouping any segment of length \(L\) into triples shows that its state
product is at least \(2^{L-2}\), including \(L=0,1,2\).

Choose an integer \(J\ge\sigma\). The first \(J\) states satisfy

\[
 \prod_{j=0}^{J-1}C^j(m)\ge
 m^J2^{-J(J-1)/2},
\]

because \(C^j(m)\ge m2^{-j}\). For \(k\ge J\), apply (2) to the
remaining \(k-J\) states. Since \(C^k(m)\ge1\) and
\(m^{\sigma-J}\le1\), equation (1) yields

\[
 \|P^k\|_\sigma\le
 2^{J(J-1)/2+J+2}\,2^{-k}.
\]

Thus the spectral radius is at most \(1/2\). The finitely supported
vector \(h=\delta_1+\delta_2+2\delta_4\) satisfies \(Ph=h/2\), by
the actual cycle \(1\to4\to2\to1\). The radius is therefore exactly
\(1/2\). If \(Pf=f\), the displayed power bound forces \(f=0\).
This last conclusion applies to a fixed vector in any contained space,
without claiming that the spectral radii of two differently normed
spaces must coincide. \(\square\)

## Consequence for the present research pass

Theorem 5.41(2)'s fixed-vector assertion cannot be used for the operator
and embedding as printed. Multiplying the operator by two would move
the known cycle eigenvalue to one, but would define a different operator
and would not establish termination. The exponential decay above holds
without making any assertion about all forward trajectories: the
reciprocal-state factors already suppress every long path. This audit
does not reject unrelated operators or amended normalizations.
