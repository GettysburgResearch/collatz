# Literature routes tested at the current obstruction

**Scope: targeted theorem applications and failed closure attempts.**
This is not a review of every Collatz paper. The ordinary source,
clock, dimension, prime support, and quantifiers must match before a
literature theorem can close the remaining implication.

## A concrete application of the Subspace Theorem

The arithmetic lane uses Evertse's *On sums of S-units and linear
recurrences* (1984), Corollary 1, printed p. 227, equations (9)–(12).
For fixed dimension and fixed finite prime set, its primitive,
nondegenerate integer tuples give a lower bound of the form
\(\prod_i (x_i)_{S'}\ge c_\epsilon H^{1-\epsilon}\).
Collective gcd one suffices; pairwise coprimality is not required.
[Primary paper](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

We apply it to the actual three-coordinate prefix and four-coordinate
completion, retaining each entire carry as one coordinate. The
[derivation](arithmetic/README.md) checks the primitive height and every
proper subsum before invoking the theorem. It yields a strong outside-prime
lower bound even for a completion with arbitrarily many odd inputs. It
does not give an upper bound on that carry's outside part.

Expanding all odd positions instead gives unbounded dimension. The genuine
orbit of 1 already supplies
\[
4^j=3^j+\sum_{i=0}^{j-1}4^i3^{j-1-i},
\]
whose individual coordinates have no prime factors outside six. A
dimension-independent conclusion of the needed kind would therefore be
false. The quantitative results of Evertse and Ferretti control exceptional
subspaces for the stated height system and dimension; they do not supply
this missing uniform assertion.
[Primary publication](https://annals.math.princeton.edu/2013/177-2/p04)

## Linear forms do not yet contradict the cycle approximation

PR205 yields \(0<h/p-\log_2 3\ll p^{-100/49}\) on its restricted cycle
branch. The three-band ordering argument makes the full period data
coprime. Wu and Wang's Theorem 1 gives
\[
|a+b\log2+c\log3|\ge H^{-4.1163051-\epsilon}
\]
for sufficiently large \(H=\max(|b|,|c|)\), with the usual nonzero form.
Set \(a=0,b=h,c=-p\) and divide by \(p\log2\). The resulting lower
bound for the rational approximation has exponent
\(5.1163051+\epsilon\), **not** \(4.1163051+\epsilon\).
The exponent \(100/49\) does not conflict with that bound. The late PR200
improvement to \(1000/479\) also does not conflict with it.
This is a comparison with the specified theorem, not a claim that it is
the best available irrationality measure.
[Wu–Wang, Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007)

The mechanical-word exclusion has a much sharper algebraic conclusion in
its special setting: cyclic rotations adjacent in intercept order differ by one 12/21 exchange,
so their carry numerators differ by a pure power of two and three. This
forces \(2^h-3^p=1\). Knight's high-cycle result is relevant to this physical
word class. In the three-band case the normalized word is mechanical but
the physical word need not be. The mixed coefficients \(\{1,2,4\}\) are
the outstanding obstruction; calling the normalized word mechanical does
not remove them.
[Knight, published article](https://doi.org/10.1016/j.disc.2025.114812)

## Complexity controls the wrong side for compression

Dubickas's Theorem 5 gives eventual parity-factor complexity greater than
\(1.70951129L\) for a divergent positive shortcut orbit. The arithmetic
packet obtains stronger conclusions under actual subexponential height
or return assumptions by applying the finite binary parity bijection to
distinct ordinary states. These are lower bounds on complexity, so they
do not force the repeated-word form needed by a compression argument.
[Dubickas, Theorem 5](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C40C0C07FEC20797475BB2899C436C9A/S0017089508004655a.pdf/on_integer_sequences_generated_by_linear_maps.pdf)

Likewise, a fixed program can find a bounded successful witness by finite
search when a witness theorem guarantees one. Small description length
with the clock given is compatible with a large literal powered-word
cost. No computability-to-periodicity implication is used.

## The Alpöge comparison and the precise missing geometric input

The Lean FRO and Mathlib Initiative's statement dated 21 November 2026
certifies the Riemann Hypothesis statement and its proof, including
independent proof checking and comparison with Mathlib's statement.
This is stronger evidence than the older announcement-only status.
We did not rebuild that library and do not use RH or any GRH variant as
a Collatz premise.
[Verification statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)

The 22 November note *An Arakelov-theoretic perspective on the
Alpöge–Claude argument on RH*, §1.2, organizes the slope method around an
injective evaluation map, slopes of its two lattices, and its finite and
infinite height bounds. Its RH-specific geometric inputs are stated
separately, including a zero estimate and an arithmetic Hilbert–Samuel
bound. The note distinguishes explained lemmas from hypotheses. This is
an architectural comparison, not an imported Collatz theorem.
[Exposition, requested version URL](https://hexagonmath.org/pdf/2611.00833v1).
At this retrieval that endpoint served a PDF bearing the imprint
hexagon:2611.00833v3; the citation does not assert byte identity with v1.

For the present Collatz data, the naive polynomial evaluation determinant
can be computed exactly. Take any \(N\) distinct lifts through the same
physical prefix,
\[
m_i=n+2^kt_i,\qquad y_i=T^k m_i=x+3^pt_i,
\]
and write \(V(v)=\prod_{i<j}(v_j-v_i)\) and \(M=N(N-1)/2\).
Then
\[
V(m)=2^{kM}V(t),\qquad V(y)=3^{pM}V(t),\qquad
\frac{|V(y)|}{|V(m)|}=(3^p/2^k)^M.
\]
Every identity follows by subtracting two actual lifted endpoints.
Adding more such samples multiplies the same coefficient excess; it does
not supply a new independent height saving at critical slope. The source
n disappears from the differences. This calculation rules out a
contradiction from that specific determinant comparison alone. It does
not rule out a different evaluation space with a new zero estimate
or divisibility theorem.

Calegari–Dimitrov–Tang's arithmetic holonomicity work illustrates why the
extra structure matters: the published unbounded-denominators theorem
uses analytic uniformization and arithmetic bounds for modular forms.
No corresponding holonomic differential system, uniformization, or
evaluation-injectivity theorem for the exceptional Collatz carry series
has been established here.
[Primary publication](https://doi.org/10.1090/jams/1053)

The resulting research target is specific: obtain an estimate on the
**supplied exceptional ordinary orbit** that is stronger than its existing
affine lifting identities. Neither a different convergent lift at each
precision nor a generic mean theorem supplies that target.
