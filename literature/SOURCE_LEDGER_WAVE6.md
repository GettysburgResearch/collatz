# Source ledger — literature audit wave 6

Only sources actually located during wave 6 appear here. Inspection level is explicit. No nearby object class is treated as a verbatim theorem for the repository moments.

## S57 — Ernvall-Hytönen, Matala-aho, and Seppälä: completion-safe Padé companions

**Record:** Anne-Maria Ernvall-Hytönen, Tapani Matala-aho, and Louna Seppälä, *Euler's factorial series, Hardy integral, and continued fractions*, Journal de Théorie des Nombres de Bordeaux 35 (2023), no. 3, 897–920; arXiv `2111.13649`.

**Inspected:** full arXiv abstract and source scope.

**Located content:** the same rational Padé polynomials converge `p`-adically toward Euler's factorial series and approach a Hardy integral at the Archimedean place. The Archimedean companion is used, with analytic continuation, to bound the rational numerator polynomial needed in the finite-place irrationality estimate.

**Native use:** model for repairing the completion mistake in withdrawn `PADIC/T-9418`–`T-9421`. The real companion controls coefficients; it is not identified with the `2`-adic target.

## S58 — Krattenthaler: Hankel determinants of polynomial moment deformations

**Record:** Christian Krattenthaler, *Hankel determinants of linear combinations of moments of orthogonal polynomials, II*, Ramanujan Journal 61 (2023), 597–627. DOI `10.1007/s11139-021-00514-8`; arXiv `2101.04225`.

**Inspected:** full open-access theorem statement, introduction, and formal applicability discussion.

**Located content:** a fixed degree-`d` polynomial deformation of a moment functional factors as the base Hankel determinant times one `d x d` determinant of orthogonal-polynomial values, divided by a Vandermonde. The identity admits a formal-series interpretation.

**Native use:** `LIT-KTHM-0046`. It does not apply directly to the `r`-decimated periodic-stack functional; it identifies the exact block generalization to seek.

## S59 — Krattenthaler: rational moment deformations and Uvarov

**Record:** Christian Krattenthaler, *A determinant identity for moments of orthogonal polynomials that implies Uvarov's formula for the orthogonal polynomials of rationally related densities*, arXiv `2103.03969`.

**Inspected:** author abstract and arXiv metadata.

**Located content:** Hankel determinants for rational modifications of a moment density are expressed through orthogonal polynomials and associated Cauchy-transform functions; the result works analytically or formally.

**Native use:** methodological extension if the block periodic-stack functional can be represented by a rational matrix-valued or multiweight deformation. No direct application is claimed.

## S60 — Dolivet and Tierz: biorthogonal Stieltjes–Wigert systems

**Record:** Yacine Dolivet and Miguel Tierz, *Chern–Simons matrix models and Stieltjes–Wigert polynomials*, Journal of Mathematical Physics 48 (2007), 023507. DOI `10.1063/1.2436734`; arXiv `hep-th/0609167`.

**Inspected:** full HTML text, especially Sections 2–3.

**Located content:** an explicit biorthogonal extension of Stieltjes–Wigert polynomials for log-normal weights and unequal monomial lattices, with generating and recurrence formulas.

**Native use:** strong object-class neighbor for the residue-class/decimated quadratic-exponential moments in `LIT-KTHM-0045`. The parameters and determinant normalizations have not been mapped verbatim.

## S61 — mixed multiple orthogonality and block moment matrices

**Record:** Carlos Álvarez-Fernández, Ulises Fidalgo Prieto, and Manuel Mañas, *Multiple orthogonal polynomials of mixed type: Gauss–Borel factorization and the multi-component 2D Toda hierarchy*, Advances in Mathematics 227 (2011), 1451–1525; arXiv `1004.3916`.

**Inspected:** abstract and theorem-level scope.

**Located content:** mixed multiple orthogonal polynomials and their dual linear forms arise from Gauss–Borel factorization of a semi-infinite block moment matrix; determinant formulas, recurrences, Christoffel–Darboux identities, and discrete deformations are developed.

**Native use:** framework for the `r` residue-class functionals

```text
L_h(y^N)=L(x^(rN+h)).
```

No theorem from the source has yet been specialized to the exact q-Gaussian parameters.

## S62 — multiple-orthogonal Christoffel transformations

**Record:** Amílcar Branquinho, Ana Foulquié-Moreno, and Manuel Mañas, *Multiple orthogonal polynomials: Pearson equations and Christoffel formulas*, arXiv `2106.12707`.

**Inspected:** full abstract and scope statement.

**Located content:** the paper develops Christoffel and Geronimus transformations for multiple orthogonal systems, including separate polynomial or rational modifications of component weights and connection formulas for type-I and type-II objects.

**Native use:** candidate machinery for turning `LIT-KTHM-0045` into the block determinant factorization required by `SYN/T-9821`.

## Inspection cautions

- The Euler–Hardy paper supplies a proof pattern, not a theorem about the stack q-series.
- Krattenthaler's scalar polynomial/rational deformation identities do not retain residue classes modulo `r` automatically.
- The biorthogonal and multiple-orthogonal sources confirm that unequal monomial lattices and block Christoffel transformations are standard objects, but the exact periodic-stack parameters and global arithmetic heights remain native work.
- No located source proves the required primitive-height estimate for `SYN/T-9821`.
- No source in this ledger proves irrationality of every fixed period, the balanced nonperiodic directive, or the Collatz conjecture.
