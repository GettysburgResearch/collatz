# Odd prime-power carry gap for the period-four quotient

Date: 2026-07-22

Status: exact arithmetic lemma, scratch-only.  The shared repository is
untouched.  This lemma isolates one remaining polynomial-local inequality
whose proof would exclude every odd prime-power cyclotomic order above the
target cutoff.

## Statement

For an odd prime `p`, put

\[
 W_p(n)=\sum_{r=1}^n p^{\nu_p(r)}.
\]

Let `N=2u+1`, and suppose `p^k>N`.  Define

\[
 V_0(u,p)=W_p(2u+1)-2W_p(u)-1.
\]

Then

\[
 \boxed{2V_0(u,p)+1<\varphi(p^k).}
\tag{1}
\]

Consequently, if one proves the local structural bound

\[
 \operatorname{ord}_{x=0}Q_u^{(5)}(1+x)\pmod p
 \le 2V_0(u,p)+1,
\tag{2}
\]

then `Phi_(p^k)` cannot divide `Q_u^(5)` for any odd prime power
`p^k>2u+1`.  Indeed cyclotomic peeling would force the left side of (2) to
be at least `phi(p^k)`, contradicting (1).

Equation (1) is proved below.  Equation (2) is the remaining polynomial
lemma and is not claimed here.

## Digit formula for `W_p`

If `n=sum_i n_i p^i` is the base-`p` expansion, then

\[
 \begin{aligned}
 W_p(n)
 &=n+(p-1)\sum_{a\ge1}p^{a-1}\left\lfloor{n\over p^a}\right\rfloor\\
 &=n+(p-1)\sum_{i\ge1}i n_i p^{i-1}.
 \end{aligned}
\tag{3}
\]

The first equality counts the extra contribution
`p^a-p^(a-1)` at every integer divisible by `p^a`; interchanging the two
finite sums gives the second.

## Carry proof

Write the base-`p` addition `u+u+1=N` as

\[
 2u_i+c_i=N_i+p c_{i+1},
 \qquad c_0=1.
\tag{4}
\]

Every carry `c_i` belongs to `{0,1}`.  Since `N<p^k`, there is no outgoing
carry at position `k`, so `c_k=0`.  Apply (3) to `N` and `u`.  Their linear
terms cancel in `W_p(N)-2W_p(u)-1`, while (4) gives

\[
 \begin{aligned}
 {V_0(u,p)\over p-1}
 &=\sum_{i=1}^{k-1}i(N_i-2u_i)p^{i-1}\\
 &=\sum_{i=1}^{k-1}i(c_i-pc_{i+1})p^{i-1}\\
 &=\sum_{i=1}^{k-1}c_i p^{i-1}.
 \end{aligned}
\tag{5}
\]

The last line telescopes after shifting the second sum.  Therefore

\[
 0\le V_0(u,p)
 \le(p-1)\sum_{i=1}^{k-1}p^{i-1}
 =p^{k-1}-1.
\tag{6}
\]

For `p=3`, (6) gives

\[
 2V_0+1\le2p^{k-1}-1<2p^{k-1}=\varphi(p^k).
\]

For `p>=5`, it gives

\[
 2V_0+1\le2p^{k-1}-1
 <(p-1)p^{k-1}=\varphi(p^k).
\]

This proves (1).

## Connection to the exact block decomposition

The two level-lowerings can be regrouped as

\[
 Q_u^{(5)}=\sum_{b=0}^u D_{u,b}F_{u-b,b},
\]

where

\[
 D_{u,b}=
 { (q;q)_{2u+1}(q;q)_b^2
  \over
   (q;q)_u(q;q)_{u-b}(q;q)_{2b+1}}
\]

and `F_(N,b)(1)=2^N`.  At `q=1+x` modulo an odd prime, the `b=0` block
has exact valuation `V_0(u,p)`.  Thus (2) asks for a uniform bound on how
far cancellation among the finitely many block states can raise the order
beyond twice this distinguished carry weight.  The arithmetic side of that
strategy is now completely closed by (1).



