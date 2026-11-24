# A minimum bad multiple and actual source descent

**Collatz remains OPEN.** This packet attacks the ordinary closing step by minimizing over all odd tripling disagreements, including multiples of three. Its main reduction and its connection to actual convergence are proved in Lean. It also supplies strict source reductions on infinite classes, including tests whose clocks grow with the input. There is no successful selector on every possible minimum.

Use the shortcut map

\[
 T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

Let \(C(n)\) mean that some finite iterate is 1. Write \(x\sim y\) for a common forward iterate, with different hitting clocks allowed. All sources and endpoints in the conclusions below are positive ordinary integers. Signed numbers used to find a parity pattern are not counterexamples or substitute sources.

## 1. A stronger minimum, with its orientation proved

If a positive counterexample exists, choose the least positive **odd** \(q\) for which \(C(q)\) and \(C(3q)\) differ. The minimum is over both label orientations, and there is no coprimality condition at three. The following conclusions hold:

\[
\begin{gathered}
 C(q),\qquad \neg C(3q),\\
 0<n\le q\ \Longrightarrow\ C(n),\\
 0<n,\quad8n+1<9q\ \Longrightarrow\ C(n),\\
 0<n<3q,\quad3\mid n\ \Longrightarrow\ C(n).
\end{gathered}
\]

Thus \(3q\) is the least bad multiple of three, including even multiples. If \(N\) is the least positive counterexample,

\[
             q<N,\qquad (9q-1)/8\le N\le3q.
\]

Equality at the first numerical bound is permitted. The guaranteed interval uses the **strict** inequality \(8n+1<9q\).

The existence and the orientation of this minimum are elementary consequences of a complete smaller-source table. For even \(n\), use \(n/2\). The five odd cases are

| Odd input | Smaller positive odd source \(z\) | What certifies the label |
|---|---|---|
| \(3\mid n\) | \(n/3\) | Comparison at \(z\) |
| \(n\equiv2\pmod3\) | \((2n-1)/3\) | Ordinary edge \(Tz=n\) |
| \(n\equiv4\pmod9\) | \((8n-5)/9\) | Ordinary path \(T^3z=n\) |
| \(n\equiv7\pmod9\) | \((4n-1)/9\) | \(T^2(3z)=n\), comparison at \(z\) |
| \(n\equiv1\pmod9,\ n>1\) | \((8n+1)/9\) | \(T^4(3z)=Tn\), comparison at \(z\) |

Every queried source satisfies \(9z\le8n+1\). Strong induction therefore needs comparisons only below the prescribed minimum, even when proving \(C(q)\) itself. The minimum cannot have the reverse orientation. Stripping factors of two then extends the minimum bad-multiple conclusion to even multiples.

[SourceDeletion.lean](arithmetic/SourceDeletion.lean) proves the table and its two interval consequences for invariant labels. [MinimumFailure.lean](minimal/MinimumFailure.lean) defines \(C(n)\) as an actual existential hitting statement, proves its invariance, constructs the least disagreement from a positive counterexample, proves the orientation, includes every smaller multiple of three, and proves the first residue exclusion. These conclusions do not assume the analytic inverse-floor input or an unproved tripling law. The complete mathematical argument is in the [arithmetic note](arithmetic/README.md).

## 2. Strict descent in the two actual components

For this minimum, a positive representative of the bad component at most \(q\) gives an immediate contradiction. A smaller odd pair in the two original components, in either order, also contradicts minimality. This permits unequal clocks and exchanged components.

The packet proves the following entire classes, rather than testing finitely many integers in them.

| Source condition | Smaller source or representative | Actual identity |
|---|---|---|
| \(q=8k+7\) | \(6k+5<q\) | \(T^3(3q)=T(6k+5)\) |
| \(q=1+128t,\ t>0\) | \(x=1+96t<q\) | \(x=T^2q\), \(T^5(3x)=T^7(3q)\) |
| \(q=8192t-21,\ t\ge1\) | \(x=6912t-17<q\) | \(x=T^5q\), \(T^8(3x)=T^{13}(3q)\) |
| \(q=3007+4374t,\ t\ge0\) | \(x=2815+4096t<q\) | \(T^{12}x=T(3q)\), \(T^{12}(3x)=Tq\) |

The swapped row needs no exclusion of parameters when the minimum includes all odd sources. Under a unit-only minimum it would need \(t\not\equiv2\pmod3\). This is a substantive reason to change the minimum, not merely a change of notation.

The third row resolves the entire dyadic class previously considered as a difficult mixed-residue direction, without imposing any ternary congruence. Its meeting point is \(2187t-5\); the two identities preserve the original components. It is proved twice, by high-bit lifting and by an independent literal symbolic path.

The second row is part of a general statement. If \(T^t a=T^s(3a)=1\), then sufficiently deep positive binary lifts \(q=a+D\) descend to \(x=a+3D/4\) in both components, using the two different original hitting clocks. A separate 26-step pair and a stable ternary carry give arbitrarily large contraction factors on specified arithmetic progressions. Neither assertion covers arbitrary sources. See the [descent note](descent/README.md) and [independent path note](renewal/README.md).

## 3. An adaptive test at the actual end of an odd run

Set \(n=3q\) and factor this same ordinary number as

\[
 n=3^h w=2^m a-1,\qquad3\nmid w,\quad a\text{ odd},
 \quad m=v_2(n+1).
\]

If \(h\ge3\), then

\[
 z=2^h w-1<q,\qquad T^h z=n-1.
\]

So \(n-1\) is good. Also \(n+1\) is good because \(Tq=T(n+1)\). If \(3^m a\equiv1\pmod4\), the ordinary endpoints \(3^{m-1}a-1\) and \(3^m a-1\) meet after two more steps. This puts \(n\) in the component of \(z<q\), a contradiction. The test works with unbounded \(h\) and \(m\); it follows the fixed source to the end of its entire initial run.

There are additional positive results on both sides of this exit:

- For \(m\ge2\), the same downward merger excludes \(q\equiv2\pmod3\). It also excludes \(q\equiv1\pmod4\) with \(q\equiv0\) or \(3\pmod9\), by smaller comparisons from the table.
- On the other exit side, if \(m\ge2\) and \(s=3^{m-2}a\equiv147\pmod{256}\), then \(T^8(9s-1)=T^8(s-1)\). The smaller source \((3q-3)/4<q\) reaches \(s-1\), so this is another actual bad-component descent. The condition is applied at the actual depth, not at a bounded initial clock.

For \(h\ge3\), a survivor must instead have \(3^m a\equiv3\pmod4\). When also \(m\ge3\), put

\[
 U=(3^{m-1}a-1)/4.
\]

Then \(U\equiv2\pmod9\), \(U\) is good, and its failed child \(9U+2\) has the earlier canonical ordinary representative

\[
                 B(U)=2^m a-1=3q<3N.
\]

This identifies a failed parent on the surviving branch and improves its canonical-source size window from the earlier factor below 171 to 3 **on this branch**. It does not prove that branch empty. The conditions \(h\ge3\), \(m\ge3\), and the surviving exit parity are essential.

## 4. Latest-source connection

The current pinned developments in PR193, PR195, PR197 and PR201 were considered against this same source minimum; [SOURCES.md](SOURCES.md) records their exact versions and the claims used. The late PR201 update supplies an elementary exponential inverse family at exact shortcut clock \(2b\), without the earlier analytic floor. Its opposing upper estimate remains open.

That inverse family does not automatically provide descent. On any exact \((b,2b)\) inverse path in a bad component, with source \(x\), bad odd inputs \(y_i\), and endpoint \(v\),

\[
 x=v\frac{4^b}{\prod_{i<b}(3+1/y_i)}
   \ge v(5/4)^b.
\]

Here every bad odd input is at least 5, since 1 and 3 converge. Under the present minimum, \(v>q\); for \(b\ge5\), these sources exceed \(3q\). Counting many such sources therefore does not give the required smaller bad multiple. A source-preserving result on a genuinely contracting grade, or a different ordinary descent, is still needed.

## 5. Exact remaining closing obligation

The new minimum is now available as a proved premise. What is missing is a proof that **every** such \(q\) admits an ordinary contradiction: for example, that the component of \(3q\) reaches the guaranteed good interval, contains a positive multiple of three below \(3q\), or yields a smaller odd discordance. The listed families supply these conclusions on their precise domains. They do not establish the universal quantifier.

In particular, the surviving canonical branch above still permits \(B(U)=3q\), with both neighboring integers good, without a constructed smaller bad representative. Sources outside that branch's valuation hypotheses also need their own reduction. No count of changing lifts, finite experiment, or conditional tripling comparison is used to assert otherwise.

The Lean modules prove the stated finite and inductive results; the asymptotic progression consequences and canonical-source assembly retain their written-proof boundary. [Verification and independent reviews](../../reports/astra-minimum-source-20261124/VERIFICATION.md) record exact compiler executions, axiom audits, finite controls, and clean-checkout validation. A successful repository validator checks integrity, not the missing universal theorem.
