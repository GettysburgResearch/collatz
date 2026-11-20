# Independent root reconstruction of the rigidity deductions

This is an AI mathematical review, not human referee acceptance or formal
verification. The reviewed note is
`research/grh-certificate-closure-20261120/UNIFORM_J_COMPLETION_ATTEMPT.md`,
SHA-256 `106f476ba879f2855c341152548257f6bc22b35fad5f9d617145136e6378eb1b`.
The self-contained sample checker is
`check_rigidity_interfaces.py`, SHA-256
`bc8d0940b0bfdaa4937467ac57e1f09d5275325b713c2e4367b65594bc13904c`.

## Reconstructed deductions

The distinction between the two high-law regimes is necessary. A global
condition j>=J does not imply that a particular j<J becomes available
at large arguments. The finite-exception source supplies that latter
condition separately. Consequently its finite-image conclusion cannot
be imported under the bare quantifiers without an additional proof.

For j>=J and odd w, both high exponents j and j+1 are legal. Free
tripling and the j-law give `F(3^(j+1)w+3)=F(w)`; the j+1 law gives
`F(3^(j+1)w+1)=F(w)`. Doubling invariance permits division by two in
both arguments. The resulting adjacent equality is on its stated
progression only. It does not extend to every adjacent pair by algebra
alone.

The periodicity argument is valid for the stronger label laws in this
note: doubling makes an eventual period global, invariance under both
2 and 3 strips those prime factors from the period, and CRT supplies
an odd ternary-unit representative for every remaining residue. The
ordinary odd-unit law then identifies every adjacent pair. The given
smooth-indicator example refutes only the isolated inference from
finite image and multiplicative invariance to periodicity. The note
correctly states that it does not satisfy the full law system.

The one-step inverse equation is `2^a n-3^h v=1`. Below n=5 the only
positive odd ternary-unit v is 1; below n=7 the possibilities are 1 and
5. With v=1, every a>=3 gives a value congruent to 7 modulo 8 for a
pure power of three, impossible. Direct checks of a=1,2 leave exactly
the stated solutions. For n=7,v=5, reduction modulo seven forces
h=4 modulo six. It is even, so `5*3^h+1=6 mod8`, incompatible with
a>=3. The two small a also fail. This is an all-exponent congruence
argument, not an inference from a finite exponent scan.

## The source-qualified S-unit step

For a fixed r-step odd path, direct iteration gives

    2^A n = 3^(r+h)v + sum_{i=0}^{r-1}3^(r-1-i)2^(A_i),
    0=A_0<A_1<...<A_r=A.

Fixing r,n,v and dividing by `2^A n` gives a linear equation with
fixed nonzero rational coefficients in a finite-rank multiplicative
group. All its terms are positive. Thus no proper nonempty subsum
vanishes, precisely the nondegeneracy condition in the cited
Evertse--Schlickewei--Schmidt theorem. That theorem yields finitely
many variable tuples. The coordinate `2^-A`, coming from A_0=0,
fixes A. The first coordinate `3^h2^-A` then fixes h; the others
fix the remaining A_i. There is no unidentified scaling freedom.
Summing over finitely many r and v proves the proposed consequence;
the zero-step case is a single source. The application is sound
conditional on the quoted external theorem. It supplies no computed
largest exponent or unbounded-depth exclusion.

## Sample and search evidence

I inspected the self-contained checker. Forward operations verify whole
affine parity and either the exact low unit guard or an allowed high
exponent. Reverse operations verify exact valuation one with a unit
core, or a common ternary valuation at least eight; their odd numerators
make the inverse high-law input odd. Common powers of two and three may
then be removed by the assumed invariances. Positive affine coefficients
prove positivity for every nonnegative parameter. The endpoint
`648t+239=(10368t+3823+1)/16` strictly decreases throughout that class.

The broader search accepts a smaller leading coefficient, which implies
descent only after its intercept-dependent threshold. The final note
retains that qualification. The finite search tables do not prove
all-source coverage. Their raw reports are archived in compressed form;
the scientific replay checks their hashes and selected sample, not every
search certificate. The actual integrated normal/optimized executions
are recorded separately in the publication receipts.

**Verdict:** the scoped elementary deductions and S-unit application
reconstruct; the uniform-J theorem and the global finite-exception
repair remain OPEN. No GRH premise is used in these deductions.
