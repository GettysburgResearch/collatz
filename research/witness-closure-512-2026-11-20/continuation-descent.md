# Descent on a whole neighborhood of a certified base pair

**Scope.** This note proves an unconditional implication from a specified
finite collection of smaller \(P\)- and \(Q\)-instances to a larger instance
of the original closure problem. It does not assume that all \(P\) and \(Q\)
are true, and it does not prove that these neighborhoods cover every case.
The full claim W512-001 remains **OPEN**.

The definitions and elementary witness operations are those in
[README.md](README.md). In particular,

\[
P(m):\quad27m\in E\Longrightarrow54m+1\in E,
\qquad
Q(m):\quad54m+1\in E\Longrightarrow9m\in E
\]

for positive odd \(m\). Write

\[
\mathcal C(M):\quad128M+1\in E\Longrightarrow64M+1\in E,
\qquad M>0,\quad M\not\equiv0\pmod4.
\]

Thus \(\mathcal C(M)=Q(M)\) for odd \(M\), while
\(\mathcal C(M)=P(M/2)\) when \(M\equiv2\pmod4\). These equalities mean
equivalence of the assertions by the exact trajectory transformations in
W512-020.

| Claim ID | Status | Scope |
|---|---|---|
| W512-060 | PROVED-IN-NOTE | The finite-premise descent theorem below, including its explicit threshold. |
| W512-061 | PROVED-IN-NOTE | Its specialization to every positive \(M\equiv1\pmod{2^{71}}\), with the base case \(M=1\) and smaller-instance premises stated explicitly. |

## 1. A certified base pair

Fix a positive \(M_0\not\equiv0\pmod4\). Suppose witnesses are supplied for

\[
x_0=128M_0+1,\qquad y_0=64M_0+1,
\]

with lengths \(r_s,r_t\) and final exponents \(A_s,A_t\), respectively.
Define their integer invariants

\[
H_s=A_s-2r_s,\qquad H_t=A_t-2r_t,
\qquad d=1-H_s+H_t.
\tag{1}
\]

Padding either witness by exponent-2 loops at 1 leaves its \(H\) unchanged.
No minimality of the supplied witnesses is required.

Consider

\[
M=M_0+2^K u,\qquad u>0\text{ odd}.
\tag{2}
\]

For

\[
K\geq\max(A_s-6,A_t-5),
\tag{3}
\]

the same exact exponent words as at the base give the endpoints

\[
S=1+3^{r_s}2^{e_s}u,
\qquad e_s=K+7-A_s\geq1,
\]

\[
V=1+3^{r_t}2^{e_t}u,
\qquad e_t=K+6-A_t\geq1.
\tag{4}
\]

To check this at every step, if the source base prefix has cumulative exponent
\(A_i\) and endpoint \(x_i\), its lifted endpoint is

\[
x_i+3^i2^{K+7-A_i}u.
\]

The added term is an even integer even at \(i=r_s\), and hence at every
earlier prefix. The endpoint is therefore odd, so the prescribed exponent at
each step is exact. The target proof is identical with the initial shift
\(2^{K+6}u\). All endpoints are positive.

It follows that the original source belongs to \(E\) exactly when \(S\)
does, and the original target belongs to \(E\) exactly when \(V\) does.

## 2. Canonical levels and the available implications

For a fixed positive odd \(u\), define two kinds of assertions:

\[
\mathsf A_j:\quad3^j u\in E,
\qquad
\mathsf B_j:\quad2\cdot3^j u+1\in E.
\]

Assign the levels

\[
\operatorname{lev}(\mathsf A_j)=2j,
\qquad
\operatorname{lev}(\mathsf B_j)=2j-1.
\tag{5}
\]

The normalization identities W512-012--013 give

\[
1+3^r2^e u\in E
\quad\Longleftrightarrow\quad
\begin{cases}
\mathsf A_{r+e/2-1},&e\text{ even},\\
\mathsf B_{r+(e-1)/2},&e\text{ odd}.
\end{cases}
\tag{6}
\]

In both cases the resulting level is \(2r+e-2\). Thus (4) gives source and
target levels

\[
\ell_s=K+5-H_s,
\qquad
\ell_t=K+4-H_t,
\qquad
\ell_s-\ell_t=d.
\tag{7}
\]

For every \(j\geq3\), the two available downward steps are exactly

\[
\mathsf A_j
\xRightarrow{\ P(3^{j-3}u)\ }
\mathsf B_j
\xRightarrow{\ Q(3^{j-3}u)\ }
\mathsf A_{j-1}.
\tag{8}
\]

Each arrow lowers the level by one. The arrows in (8) are conditional on the
displayed individual \(P\)- or \(Q\)-instance. They are not used as
unconditional convergence rules.

The lowest permitted endpoint of this chain is level 4, namely
\(\mathsf A_2\). Reaching it uses \(\mathsf B_3\Rightarrow\mathsf A_2\),
which is precisely \(Q(u)\). No \(P\)- or \(Q\)-instance with a
nonintegral parameter or an exponent \(j<3\) is needed.

## 3. W512-060: an explicit descent theorem

Assume the certified base pair satisfies \(d\geq0\), or equivalently
\(H_s-H_t\leq1\). Define the integer threshold

\[
\boxed{
K_*=
\max\{2,\ A_s-6,\ A_t-5,\ H_t,\ 5-4H_s\}.
}
\tag{9}
\]

For every \(K\geq K_*\) and every positive odd \(u\), let \(M\) be as in
(2). Then the following holds:

> If each of the \(d\) specified \(P\)- or \(Q\)-instances in the
> consecutive level chain from \(\ell_s\) down to \(\ell_t\) is true,
> then \(\mathcal C(M)\) is true. Every parameter \(p\) in those instances
> satisfies \(p<M/2\).

This is a finite-premise theorem. In particular, if the smaller instances have
already been established by an induction, it supplies the next induction
step. The number of calls is exactly \(d\), independent of \(K\) and \(u\).

### Proof

The bounds involving \(A_s,A_t\) make (4) valid. The condition \(K\geq2\)
preserves \(M\bmod4\), so the larger parameter still belongs to the original
domain. Also

\[
\ell_t=K+4-H_t\geq4,
\qquad \ell_s=\ell_t+d\geq\ell_t.
\]

If \(d=0\), (6) gives the very same canonical integer on both sides: the
level fixes both its type and its index. No \(P\) or \(Q\) assumption is
needed. Membership of the original source and target is equivalent by the
explicit normalizations alone.

Suppose \(d>0\). Then \(\ell_s\geq5\). The largest index in any arrow of
the downward chain is

\[
j_s=\left\lceil\frac{\ell_s}{2}\right\rceil.
\]

The largest required parameter is therefore exactly

\[
\boxed{
p_{\max}=3^{j_s-3}u
=3^{\lfloor(K-H_s)/2\rfloor}u.
}
\tag{10}
\]

The exponent in (10) is nonnegative because \(j_s\geq3\). Put
\(q=\lfloor(K-H_s)/2\rfloor\). The elementary integer inequality
\(3^5=243<256=2^8\) gives

\[
(3^q)^5\leq2^{8q}
\leq2^{4(K-H_s)}
\leq2^{5(K-1)}.
\]

The last inequality is exactly the requirement \(K\geq5-4H_s\) in (9).
Taking fifth roots yields

\[
p_{\max}\leq2^{K-1}u
=\frac{M-M_0}{2}<\frac M2.
\tag{11}
\]

Assuming the indicated finite list of smaller assertions, apply (8) exactly
\(d\) times. This proves the canonical target assertion from the canonical
source assertion. Reversing (6) and the target prefix in (4) proves
\(\mathcal C(M)\). This proves W512-060.

The factor \(1/2\) in (11) makes the induction bookkeeping uniform. A
\(P(p)\) call corresponds to the original parameter \(2p<M\), and a
\(Q(p)\) call corresponds to \(p<M\). Equally, if the induction is on the
odd parameter in the paired assertions, then for even \(M\) every call
satisfies \(p<M/2\), the parameter of the desired assertion \(P(M/2)\).

### Witness reconstruction

The proof is compatible with any supplied source witness. Strip its forced
base prefix to obtain a witness for \(S\), normalize by the explicit
exponent-2 steps and odd-argument \(J\) conversions, and use the indicated
smaller assertions. If witnesses are returned for those calls, reverse the
target normalization and prepend its forced base prefix. W512-011 gives the
resulting witness identity.

Thus the theorem is not limited to the particular witness used to certify
the base. The base witnesses prescribe a valid prefix for the lifted values;
they do not replace the source witness supplied for the larger value.

## 4. W512-061: the neighborhood of \(M_0=1\)

For \(x_0=129\), an exact exponent word to 1 is

```text
2,2,2,1,1,3,1,1,1,2,2,1,2,1,1,2,1,1,1,2,3,1,
1,2,1,2,1,1,1,1,1,3,1,1,1,4,2,2,4,3,1,1,5,4
```

It has \(r_s=44\), \(A_s=77\), and \(H_s=-11\). For \(y_0=65\), the
word

```text
2,2,4,1,1,2,3,4
```

has \(r_t=8\), \(A_t=19\), and \(H_t=3\). These words can be checked
directly by the recurrence \(n_i=(3n_{i-1}+1)/2^{a_i}\); every endpoint is
odd and the final endpoint is 1.

Hence

\[
d=15,\qquad K_*=\max\{2,71,14,3,49\}=71.
\]

For every \(K\geq71\) and positive odd \(u\), the case

\[
M=1+2^K u
\]

reduces to exactly 15 smaller \(P\)- and \(Q\)-instances. The largest
parameter is

\[
3^{\lfloor(K+11)/2\rfloor}u<M/2.
\]

At \(K=71\), the canonical chain starts at \(\mathsf B_{44}\) and ends at
\(\mathsf A_{36}\). Its first call is \(Q(3^{41}u)\), followed by the
successive alternating steps prescribed by (8).

Every positive \(M\equiv1\pmod{2^{71}}\) is either the certified base
\(M=1\), or has the form above with
\(K=\nu_2(M-1)\geq71\) and \(u=(M-1)/2^K\) positive odd. Thus this is
a descent rule for the whole positive punctured neighborhood, not merely a
finite set of sampled lifts. Its conclusion remains conditional on the
specified smaller instances; it does not assert them without proof.

## 5. What this advances, and what it leaves open

The theorem handles an infinite neighborhood even when source and target
base witnesses have very different lengths. It uses the complete finite
words through their affine endpoint formulas and their invariants \(A-2r\).
It therefore supplies a descent mechanism beyond a fixed common-prefix
merger.

Its direction condition \(H_s-H_t\leq1\) is essential to this particular
level argument: the proved \(P\)/\(Q\) pattern (8) runs downward. A base
with the opposite inequality does not acquire an upward implication from
this theorem. Other exact transformations may handle such a base, but their
proofs are separate.

No finite or infinite cover of all positive admissible \(M\) is established
here. The remaining global obligation is to prove that every case reaches a
certified base or a valid smaller-instance rule. W512-001 remains OPEN.
