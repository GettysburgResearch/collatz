# The last-contact source survives the strict-Green resolvent positively

**Status:** exact written source-preserving identities. This note tests the
new contact-section contraction against the companion strict-Green
resolvent. It identifies their actual common domain and shows why their
combination does not yet eliminate the last escaping excursion.

## 1. Operators and original sources

Use the nonperiodic odd-unit domain of
`CONTACT_RETURN_FINITE_REFERENCE.md`. Let

\[
\omega(n)=\frac1{3n+1},\qquad \lambda(n)=1-\omega(n),\qquad
L a(q)=\sum_{U(n)=q}a(n),\qquad
T a=L(\lambda a).
\]

All paths are killed when they first enter a periodic orbit. Set

\[
S=\sum_{j\ge0}L^j,\qquad S_T=\sum_{j\ge0}T^j,\qquad
K=SLD,\qquad Da=\omega a.
\]

The companion `STRICT_GREEN_VOLTERRA.md` proves, on
\(X_s=\ell^1(\mathcal N,n^{-s})\) for \(39/40<s\le1\), that
\(K\) is compact and \(I+K\) has the bounded inverse \(R(1)\).
It also proves

\[
\|S\eta\|_s\le C_s\|\eta\|_1,
\qquad C_s=\frac{5s}{s-39/40},
\tag{1}
\]

for every finite original source mass \(\eta\ge0\). No statement here
requires raw \(L\) to be bounded on \(X_s\).

For a retained path \(q_0=x,q_1,\ldots,q_\ell=q\), write

\[
\Lambda_i(x)=\prod_{r=0}^{i-1}\lambda(q_r),\qquad \Lambda_0=1.
\]

The actual-path occupation bound in the pinned source gives
\(\delta\le\Lambda_i\le1\), with \(\delta=\exp(-200/3)\).

## 2. Exact positive action on the Green cone

**Proposition.** For every \(\eta\ge0\) with finite ordinary total mass,
put \(u=S\eta\) and \(w=S_T\eta\). Then both belong to \(X_s\), and

\[
\boxed{\delta u\le w\le u,\qquad
(I+K)w=u,\qquad R(1)S\eta=S_T\eta.}
\tag{2}
\]

**Proof.** The nonnegative source kernels are

\[
u(q)=\sum_{x\preceq q}\eta(x),\qquad
w(q)=\sum_{x\preceq q}\eta(x)\Lambda_{x,q}.
\tag{3}
\]

Here each original source occurs once at its unique physical hitting
depth; \(\preceq\) includes the source itself. The path-product bound
immediately proves \(\delta u\le w\le u\). Equation (1) proves both
norms finite.

For one source \(x\), the contribution to \(Kw(q_\ell)\) is

\[
\eta(x)\sum_{i=0}^{\ell-1}\omega(q_i)\Lambda_i(x)
=\eta(x)\sum_{i=0}^{\ell-1}
  \bigl(\Lambda_i(x)-\Lambda_{i+1}(x)\bigr)
=\eta(x)(1-\Lambda_\ell(x)).
\tag{4}
\]

The time-zero endpoint is retained in \(w\) and excluded from \(K\),
exactly as in the companion resolvent. Summing (4) over unchanged
original sources is justified by nonnegativity and gives \(w+Kw=u\).
Applying the established inverse on \(X_s\) proves the last identity.
\(\square\)

The inverse \(R(1)\) need not preserve positivity on every positive
element of \(X_s\). Proposition (2) shows that it **does** preserve
positivity, with a uniform positive lower comparison, on the exact cone
\(S(\ell^1_+)\) containing finite last-contact sources. A sign
contradiction cannot be obtained on that cone.

## 3. Applying the identity to the actual last-contact measure

The pinned PR176 last-contact theorem uses

\[
\eta(x)=\nu(x)\,
\mathbf1_{\{x\text{ is a last contact on an escaping path}\}}.
\tag{5}
\]

It proves \(\eta\in\ell^1\), with total mass equal to the sum of
escaping component capacities, and identifies \(S\eta\) with the
ordinary flow \(\nu\) on the post-last-contact future sector. Hence
(2) applies without renormalizing or resampling \(\eta\):

\[
\boxed{\delta S\eta\le R(1)S\eta\le S\eta.}
\tag{6}
\]

If that sector has positive capacity, the resolvent carries it to a
positive weighted transport potential. The strict-Green immigration
correction has finite \(X_s\)-norm and an entire resolvent while this
conditional positive sector remains present. These statements are
algebraically compatible.

At a last contact \(x\), the next-contact map is undefined. Thus the
contact operator \(J\) kills the atom \(\eta(x)\) after one induced
step. If its actual orbit escapes, ordinary transport retains that very
same atom at every later physical step. Formula (4) subtracts only the
summable multiplicative correction; it does not remove the original
escaping atom.

## 4. Why convergence in the weighted space does not decide absorption

For a conditional escaping orbit \(q_j=U^j(x)\), all its states are
distinct positive integers, so \(q_j\to\infty\). For every \(s>0\),

\[
\|L^j\delta_x\|_s=q_j^{-s}\longrightarrow0,
\qquad \|L^j\delta_x\|_{\ell^1}=1.
\tag{7}
\]

Even this exact weighted norm decay of an unchanged ordinary atom is
compatible with escape. The complete weighted occupation
\(\sum_jq_j^{-s}\) is finite for \(s>39/40\) by the imported actual-path
count. Its unweighted occupation is infinite.

Therefore the norm convergence of the strict-Green physical-clock
approximations, including the stronger convergence for \(s<1\), cannot
by itself imply ordinary absorption. It controls a summably weighted
correction in a norm that already sends a high escaping atom to zero.
The contact contraction also has an explicit exit sector. Combining
these two valid forms of convergence does not identify that sector with
periodic absorption.

## 5. Variable contact thresholds

For each fixed \(M\), the contact theorem gives
\(J_M(\nu^2\mathbf1_{\{V\le M\}})\le\rho_M
\nu^2\mathbf1_{\{V\le M\}}\), where
\(1-\rho_M=3\delta\gamma/(64M)\). Its finite reference mass is bounded
by \(2(M/\delta)^2\). Neither estimate is uniform as \(M\to\infty\).

On an escaping forward path, harmonicity gives
\(\nu(q_j)\ge\nu(q_0)>0\); consequently
\(\sum_j\nu(q_j)^2=\infty\). Thus the uncut reference naturally fails
to be finite on exactly the sector that remains to be excluded. The
weighted Green map keeps that sector finite by multiplying its
occupation by \(q_j^{-s}\), which brings back the distinction in (7).

The successful deductions are a finite contact reference, exact
source-preserving contact contraction, and a bounded invertible
correction of its ordinary occupation. A full absorption argument still
needs an estimate that controls the unweighted terminal excursion or
forces its last-contact source measure to vanish.
