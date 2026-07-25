# T-0044 — Finite algebraic-nucleus rigidity for the six-branch extraction tree

Claim ID: `T-0044`  
Title: Every finite algebraic self-section of the complete six-branch tree is the original expanding forward map  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-26  
Dependencies: `L-0040`; elementary six-branch arithmetic reconstructed below  
Scope: finite-control algebraic or semialgebraic sections carrying the complete six-branch subtree  
Related counterexample candidates: none

## 1. The fixed extraction tree

Put

\[
P=3^{12}=531441,
\qquad
Q=2^{19}=524288,
\qquad P>Q,
\tag{1}
\]

and

\[
\mathcal A=
\{229376,258048,290304,326592,367416,413343\}.
\tag{2}
\]

For the six types use the exact source and output data

\[
(r_i)=(294912,331776,438784,297024,6472,466033),
\tag{3}
\]

\[
(c_i)=(298936,336303,444771,301077,6561,472392).
\tag{4}
\]

They satisfy

\[
\boxed{Qc_i=Pr_i+a_i.}
\tag{5}
\]

A legal ordered pair \(i\to j\) has the high-tail equation

\[
\boxed{Qk'=Pk+c_i-r_j.}
\tag{6}
\]

For every ordered pair, let \(\kappa_{ij}\in\{0,\ldots,Q-1\}\) be the unique residue making the right side divisible by \(Q\), and put

\[
\lambda_{ij}={P\kappa_{ij}+c_i-r_j\over Q}.
\tag{7}
\]

Then the complete child cylinder is

\[
\boxed{
 k=\kappa_{ij}+Qt,
 \qquad
 k'=\lambda_{ij}+Pt,
 \qquad t\in\mathbb Z_{\ge0}.}
\tag{8}
\]

Every one of the 36 cylinders is nonempty.

## 2. Algebraic section hypothesis

Let \(\Omega\) be a finite control set. At each reachable state \((\omega,i)\), suppose there is a nonconstant real algebraic branch

\[
f_{\omega,i}(X)
\tag{9}
\]

defined and analytic for all sufficiently large positive real \(X\), such that

\[
\boxed{f_{\omega,i}(n)\in\mathbb Z_{>0}}
\tag{10}
\]

for every sufficiently large integer \(n\).

Assume every state carries all six physical children. For a child type \(j\), let the successor control be \(\omega'=\tau(\omega,i,j)\). Allow initially a state-dependent permutation \(\pi_{\omega,i}\) of the six output symbols. Require the exact self-section identity

\[
\boxed{
Q f_{\omega',j}(\lambda_{ij}+Pt)
=
P f_{\omega,i}(\kappa_{ij}+Qt)
+a_{\pi_{\omega,i}(j)}}
\tag{11}
\]

for every sufficiently large integer \(t\).

This is the broad finite algebraic version of a recursive extraction proof: each complete child cylinder is to be re-encoded as the same six-branch ordinary language using one of finitely many algebraic section coordinates.

## Theorem

Under the hypotheses above, every reachable section is affine and in fact

\[
\boxed{
f_{\omega,i}(X)=PX+c_i,}
\tag{12}
\]

and every symbol permutation is the identity:

\[
\boxed{\pi_{\omega,i}(j)=j.}
\tag{13}
\]

Thus the only finite algebraic nucleus is the original forward image

\[
PX+c_i.
\]

It is expanding and supplies no contracting, bounded, seed-preserving, or least-root-descending extraction. The same conclusion holds for finite semialgebraic/Nash nuclei satisfying the stated tail-integrality condition.

## 3. Algebraic branches become polynomials

By `L-0040`, every section in (9)--(10) is a polynomial in \(\mathbb Q[X]\). Write

\[
f_{\omega,i}(X)
=L_{\omega,i}X^{d_{\omega,i}}+\text{lower terms},
\qquad L_{\omega,i}\ne0.
\tag{14}
\]

Equation (11) holds on infinitely many integers, hence as a polynomial identity in \(t\).

Comparison of degrees gives

\[
d_{\omega',j}=d_{\omega,i}
\tag{15}
\]

along every edge. Call the common edge degree \(d\). Comparison of leading coefficients gives

\[
Q L_{\omega',j}P^d
=
P L_{\omega,i}Q^d,
\]

or

\[
\boxed{
L_{\omega',j}
=L_{\omega,i}\left({Q\over P}\right)^{d-1}.}
\tag{16}
\]

From every reachable state, following edges in the finite control graph eventually enters a directed cycle. Around a cycle of length \(s\), (16) gives

\[
L=L\left({Q\over P}\right)^{s(d-1)}.
\tag{17}
\]

Since \(L\ne0\) and \(P\ne Q\),

\[
\boxed{d=1.}
\tag{18}
\]

Degree equality propagates this conclusion back through every transient state.

Consequently

\[
f_{\omega,i}(X)=v_{\omega,i}X+s_{\omega,i}.
\tag{19}
\]

Because the values are integral on all sufficiently large integers, first differences show

\[
v_{\omega,i},s_{\omega,i}\in\mathbb Z.
\tag{20}
\]

Eventual positivity makes each slope positive.

For degree one, (16) becomes

\[
v_{\omega',j}=v_{\omega,i}.
\tag{21}
\]

Thus one common positive integer slope \(v\) occurs on every reachable component.

## 4. The digit alphabet has no affine symmetry

We need one elementary property of \(\mathcal A\).

### Lemma

If residues \(w,t\pmod Q\) satisfy

\[
t+w\mathcal A=\mathcal A\pmod Q,
\tag{22}
\]

then

\[
\boxed{w\equiv1,\qquad t\equiv0\pmod Q.}
\tag{23}
\]

### Proof

The alphabet has exactly one odd element,

\[
a_5=413343,
\]

and five even elements. Therefore \(w\) must be odd and \(t\) even. The unique odd element must map to itself:

\[
t+wa_5\equiv a_5\pmod Q.
\tag{24}
\]

Let \(S=\sum_i a_i\). Summing the affine permutation gives

\[
6t+wS\equiv S\pmod Q.
\tag{25}
\]

Substitution of \(t=(1-w)a_5\) gives

\[
(1-w)(6a_5-S)\equiv0\pmod Q.
\tag{26}
\]

Directly,

\[
6a_5-S=594979,
\]

which is odd. Since \(Q\) is a power of two, (26) forces \(w\equiv1\pmod Q\), and then (24) forces \(t\equiv0\pmod Q\). ∎

## 5. Affine normalization

Substituting (19) into (11) and using (6) gives

\[
v(c_i-r_j)+Qs_{\omega',j}-Ps_{\omega,i}
=a_{\pi_{\omega,i}(j)}.
\tag{27}
\]

For fixed \((\omega,i)\), reduction modulo \(Q\), together with

\[
r_j\equiv-P^{-1}a_j\pmod Q,
\]

shows that the six right-hand symbols form an affine image of \(\mathcal A\) with multiplier

\[
w\equiv vP^{-1}\pmod Q.
\]

The lemma forces

\[
\boxed{v\equiv P\pmod Q}
\tag{28}
\]

and forces every \(\pi_{\omega,i}\) to be the identity. Write

\[
\boxed{v=P+mQ}
\tag{29}
\]

for one integer \(m\).

Define normalized section carries

\[
\boxed{
h_{\omega,i}=s_{\omega,i}-c_i-mr_i.}
\tag{30}
\]

Using (5), (27), and (29), direct simplification gives

\[
\boxed{
Qh_{\omega',j}
=Ph_{\omega,i}-ma_i.}
\tag{31}
\]

The right side depends on the current type \(i\), but not on the selected child \(j\).

Let \(H\) be the finite nonempty set of normalized carry values occurring after at least one transition. Every parent has all six children, and all six siblings receive the same carry value. Hence every \(h\in H\) occurs with every current type. Therefore

\[
\boxed{
T_i(H)\subseteq H,
\qquad
T_i(h)={Ph-ma_i\over Q},
\qquad0\le i\le5.}
\tag{32}
\]

## 6. Extremal rigidity

Let

\[
h_- =\min H,
\qquad
h_+=\max H.
\]

### Case \(m>0\)

Since \(T_i(h_+)\le h_+\) for every \(i\),

\[
(P-Q)h_+\le ma_i
\]

for every \(i\), so

\[
h_+\le {m a_{\min}\over P-Q}.
\tag{33}
\]

Similarly \(T_i(h_-)\ge h_-\) for every \(i\) gives

\[
h_-\ge {m a_{\max}\over P-Q}.
\tag{34}
\]

Because \(a_{\max}>a_{\min}\), equations (33)--(34) force \(h_->h_+\), impossible.

### Case \(m<0\)

Write \(m=-n\), with \(n>0\). The same maximum/minimum argument gives

\[
h_+\le-{n a_{\max}\over P-Q},
\qquad
h_-\ge-{n a_{\min}\over P-Q},
\]

again forcing \(h_->h_+\).

### Case \(m=0\)

Now

\[
T_i(h)={P\over Q}h.
\tag{35}
\]

If \(H\) contained a positive value, its maximum would map to a larger value because \(P/Q>1\). If it contained a negative value, its minimum would map to a smaller value. Hence

\[
\boxed{H=\{0\}.}
\tag{36}
\]

Therefore

\[
m=0,
\qquad
v=P,
\qquad
s_{\omega,i}=c_i,
\]

which proves (12)--(13). ∎

## 7. What exhaustive class has been eliminated

The theorem rules out every extraction proof having all of the following features:

1. finitely many control states;
2. one algebraic or semialgebraic section formula at each state/type;
3. ordinary integer output for every sufficiently large tail parameter;
4. exact self-replication of the complete six-branch subtree;
5. no additional unbounded stack, quotient, or most-significant-boundary register.

The class contains all finite affine, polynomial, rational, Nash, and algebraic-function section nuclei satisfying the hypotheses. Enlarging the formula class from rational to algebraic does not create a hidden descent: integrality collapses it back to a polynomial, graph cycles collapse the degree to one, and the digit arithmetic collapses the affine map to the original forward image.

This is genuinely weaker than Collatz. It eliminates only a uniform recursive extraction architecture for one strict six-branch subsystem. A single survivor may still live in a proper, genuinely infinite-state sublanguage.

## 8. Consequence for the global blocker

A successful proof of bounded least roots in this chart cannot arise from a finite tame algebraic self-similarity of the complete tree. It must use at least one of:

- a genuinely unbounded ordinary quotient or stack;
- a source-specific global height/product relation;
- a direct digit-escape theorem;
- a proper nonuniform sublanguage containing one written root;
- or a finite positive-cycle certificate bypassing extraction.

This narrows the search without pretending to decide the least-root sequence itself.

## Dependency audit

- `L-0040` supplies algebraic-to-polynomial collapse.
- All six-branch arithmetic and affine rigidity are reconstructed in this file.
- No numerical experiment or external Diophantine theorem is used.

## Gap audit

- The theorem does not prove that the least roots diverge.
- It assumes a section formula is integer-valued on every sufficiently large integer tail, not merely on a sparse selected subset.
- It carries the complete six-branch subtree; proper sublanguages are outside scope.
- Pushdown, transcendental, and genuinely unbounded-state sections remain possible.
- No ordinary survivor or Collatz counterexample is claimed.
