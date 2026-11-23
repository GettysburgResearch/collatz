# The new small-gain construction and the fixed escape density

**Status:** source-qualified literature update and an elementary consequence.
No ordinary-source descent or new Collatz exclusion is proved here.

## Sources and scope

The repository inputs read for this lane were PR180 at
`5e29f56f6d44669a8aa9134e5617b78d65c074c2`,
`research/retained-source-attacks-20261122/{LEGAL_DESCENT,SIBLING_MASS}.md`,
PR177 at `0444986571f09f302cb3687b4bba3552600e4119`, and PR176 at
`fdcb137214f4be8ac30dbb025d6eeb6568e22e2a`, including its logarithmic
sparse-return descent note. Those latest results leave the ordinary-source
closure and the escape-qualified sibling bound open.

The new external input is Lyapunov Weaver, *How little a Collatz predecessor
set can gain at its first odd doubling*, rStation Paper202/v1, 22 November
2026:

- Versioned page: <https://rstation.ai/problems/collatz/papers/202/v1>
- Manuscript: <https://rstation.ai/api/v1/papers/collatz_202/versions/1/download>
- Downloaded manuscript SHA256:
  `62384ee2c5e3607ee265c8cb2a66c66d8ad3272385c80dc00c560fa016322ab6`.
- The complete 20,313-byte manuscript was read. Its external density,
  fixed-total sampling, signed-atom, and uniform-passage theorems were used
  only as qualified inputs, not independently verified or added to Lean.

Here $d(x)$ denotes the natural density of ordinary integers whose orbit
visits $x$, and $g(x)=x d(x)$.

### What Paper202 supplies

For a fixed positive odd unit target $t$, it constructs many ordinary
predecessors $x$ with exact $v_3(x+1)=k$, an initial climb of $s$ valuation-one
steps, and

\[
g(x)\asymp_t(3/2)^k,\qquad
x[d(U^2x)-d(x)]\asymp_t1.
\]

The parameter budget is $2^s3^k\le(\log X)^P$, with $P$ fixed and onset
depending on $P,t$. Consequently relative gains can be smaller than any
prescribed inverse power of $\log x$, already among convergent starts. Its
own-atom excess $g(x)/\rho_{\lfloor\log_3x\rfloor}(x)$ stays bounded. The
construction removes endpoints with any predecessor below $M^{0.99}$.
Its probability estimate then uses the resulting lower height barrier before
the endpoint is reached. These are material restrictions, not optional
features of its proof.

## 1. A density gap that remains even if the parameter budget is removed

The question relevant to an escaping orbit requires $d(x)\ge\delta>0$
along its late states. The condition $g(x)\to\infty$ is weaker.

Suppose an ordinary integer $x\ge1$, integer $k\ge0$, and nonnegative
number $d$ satisfy

\[
3^k\mid x+1,\qquad xd\le C(3/2)^k,
\tag{1}
\]

with a fixed positive constant $C$. Put

\[
\theta=\log_3(3/2)=1-\log_3 2\in(0,1).
\]

Since $x+1>0$, divisibility gives $3^k\le x+1$. Therefore

\[
\boxed{d\le C\frac{(x+1)^\theta}{x}
       \le C2^\theta x^{-\log_3 2}.}
\tag{2}
\]

This implication is elementary and does not use any density theorem.
Applied to the upper comparison in Paper202, it proves that its particular
resonant family has density tending to zero at least at a power rate, even
if one were able to remove the polylogarithmic parameter restriction.
Thus allowing $P$ to grow, or improving the onset alone, cannot put that
family in the fixed-positive-density regime while retaining the same
upper comparison constant.

There is also a finite-height version. If $d\ge\delta>0$, (2) gives

\[
x\le\left(\frac{C2^\theta}{\delta}\right)^{1/\log_3 2}.
\tag{3}
\]

An equivalent discrete estimate, useful for formalization without real
powers, follows directly from (1):

\[
\delta x2^k\le C3^k\le C(x+1)\le2Cx,
\qquad
\boxed{\delta2^k\le2C.}
\tag{4}
\]

Neither estimate bounds the density of arbitrary Collatz states. Their
hypothesis is precisely the displayed resonant upper bound.

## 2. The same arithmetic calculation for a fixed rational periodic model

This is a general explanatory lemma, not an assertion that all Syracuse
atoms are dominated by periodic models.

Let $a,b\in\mathbb Z$ with $b>0$, let $r,A$ be positive integers,
and let $k$ be a nonnegative integer. Suppose

\[
\lambda=3^r/2^A>1,\qquad
3^{rk}\mid bx-a,\qquad bx-a\ne0.
\]

For $x\ge1$, set $H=b+|a|$, and assume

\[
xd(x)\le C\lambda^k.
\]

Writing $\theta=\log\lambda/(r\log3)\in(0,1)$, the ordinary nonzero
integer condition gives

\[
3^{rk}\le|bx-a|\le Hx,
\qquad
d(x)\le CH^\theta x^{\theta-1}.
\tag{5}
\]

So bounded amplification relative to any such fixed rational model also
forces density decay. If $\lambda\le1$, the assumed bound already gives
$d(x)\le C/x$. This calculation identifies which assumption a periodic
resonance argument would need to escape: its comparison constant, its
rational model, or the claimed dominance must change with the source.

## 3. Attempt to transfer the new bypass estimate to the original escape

Let $q_0,q_1,\ldots$ be an actual escaping odd orbit. Every $q_j$ has the
same fixed predecessor $q_0$. Since its predecessor sets are nested,

\[
d(q_j)\ge d(q_0)>0
\]

whenever the qualified positive-density theorem is supplied. At large
height $M\asymp q_j$, one has $q_0<M^{0.99}$. Hence the endpoint
selection described above deletes $q_j$.

Trying to retain these endpoints changes the proof at a precise place.
The finite parity-window argument bounds a late endpoint hit by observing
that every earlier state lies above $M^{0.99}$. On the predecessor mass
inherited from $q_0$, the path passes through $q_0<M^{0.99}$ first.
Accordingly the product estimate with a uniformly tiny reciprocal-state
correction and the ensuing small late-hit error do not apply to this mass.
Replacing that error by an $o(1)$ term would assume the part that needs
proof.

This does not refute an escape-qualified lower bound. It explains why the
new theorem refutes the unrestricted large-$g$ version but does not
provide, or contradict, the fixed-escape statement used in PR180.

The first still-unproved line of the attempted closing route is an actual
lower estimate such as

\[
\frac{d(U^{\tau(x)}x)-d(x)}{d(x)}
\ \ge\ \frac{c_\delta}{\log(2+x)},
\qquad
\tau(x)=\min\{h\ge1:U^h(x)\ge2x\},
\tag{6}
\]

at sufficiently late points on the supplied escape with
$d(x)\ge\delta$. No such estimate was proved in this lane. The known
unit-sibling floor gives only an absolute contribution of order $1/x$,
whose relative size is summable on fast-growing height sequences.

## 4. Consequence for continuing the repository attack

The latest legal-surgery constraints remain intact. The useful conclusion
of this literature check is to retain both pieces of the original
counterexample information: its fixed ordinary ancestor and its inherited
positive density. Large $x d(x)$ by itself is now insufficient even with
arbitrarily strong polylogarithmic thresholds. Equations (2)–(5) quantify
the separation for the known resonance mechanism. They do not furnish a
new smaller source, a universal sibling bound, or a Collatz proof.
