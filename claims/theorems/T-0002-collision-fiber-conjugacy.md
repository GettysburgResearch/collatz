# T-0002 — Arbitrary collision fibers induce partial radix maps

Claim ID: `T-0002`  
Title: Affine conjugacy from a finite shortcut-Collatz collision fiber to a digit-preserving partial radix map  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0001`; the collision identity may be certified using `L-0001`  
Scope: finite collision fibers, including sparse and nonconsecutive fibers  
Related counterexample candidates: none

## Statement

Let

\[
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

Fix integers \(L\ge1\) and \(a\ge0\), and put

\[
M=2^L,\qquad N=3^a.
\]

Assume \(N>M\). Let \(D\) be a nonempty finite subset of
\(\{0,1,\ldots,M-1\}\). Suppose there are integers \(r,s\) such that

\[
0\le r+d<M\qquad(d\in D)
\]

and, for every \(q\ge0\) and every \(d\in D\),

\[
\boxed{
T^L(Mq+r+d)=Nq+s.
}
\tag{1}
\]

Define

\[
c=N-M>0,\qquad \kappa=Ms-Nr,\qquad h=s-r,
\tag{2}
\]

and

\[
\Phi(n)=cn+\kappa.
\tag{3}
\]

Then the following hold.

### 1. Collision normal form

For \(A=cq+h\),

\[
\Phi(Mq+r+d)=MA+cd
\tag{4}
\]

for every \(d\in D\), while

\[
\Phi(Nq+s)=NA.
\tag{5}
\]

### 2. Induced digit-preserving radix map

Define the partial map

\[
\boxed{
H_D(MB+d)=NB+d,
\qquad d\in D.
}
\tag{6}
\]

The congruence class

\[
A\equiv h\pmod c
\tag{7}
\]

is invariant under \(H_D\). For every \(A\) satisfying (7), put

\[
\nu(A)=\frac{NA-\kappa}{c}.
\tag{8}
\]

Then \(\nu(A)\) is an integer. Whenever \(A\bmod M\in D\) and
\(\nu(A)>0\), one block of \(L\) shortcut-Collatz steps satisfies

\[
\boxed{
T^L(\nu(A))=\nu(H_D(A)).
}
\tag{9}
\]

### 3. Counterexample criterion

If there is an infinite sequence

\[
A_{t+1}=H_D(A_t)
\]

such that

- \(A_0\equiv h\pmod c\);
- \(A_0\ge M\);
- \(\nu(A_0)>0\);
- \(A_t\bmod M\in D\) for every \(t\ge0\);

then \(\nu(A_0)\) is a positive-integer Collatz counterexample. In fact,
if \(A_t=MB_t+d_t\), then \(B_t\ge1\) and

\[
A_{t+1}-A_t=cB_t>0.
\tag{10}
\]

Thus the induced states, and consequently the corresponding Collatz block
states, diverge to infinity.

## Definitions

The set

\[
F=r+D=\{r+d:d\in D\}
\]

is called a **collision fiber** at depth \(L\) when (1) holds. It need not be
an interval. Translating a fiber by choosing a different anchor \(r\) changes
the induced digit set but does not change the underlying Collatz collision.
The canonical choice used in the experiments is \(r=\min F\), so that
\(0\in D\).

## Motivation

`T-0001` treated only consecutive fibers
\(D=\{0,1,\ldots,m-1\}\). The proof never uses consecutiveness. Removing that
restriction exposes much larger, sparse collision alphabets. Those alphabets
supply more admissible least digits and a richer carry grammar without changing
the exact lifting argument.

## Proof

Let \(A=cq+h\). For an input branch,

\[
\begin{aligned}
\Phi(Mq+r+d)
&=c(Mq+r+d)+Ms-Nr\\
&=Mcq+cr+cd+Ms-Nr\\
&=M(cq+s-r)+cd\\
&=MA+cd,
\end{aligned}
\]

which proves (4). For the common output,

\[
\begin{aligned}
\Phi(Nq+s)
&=c(Nq+s)+Ms-Nr\\
&=Ncq+cs+Ms-Nr\\
&=N(cq+s-r)\\
&=NA,
\end{aligned}
\]

because \(c+M=N\). This proves (5).

If \(A=MB+d\), then

\[
H_D(A)-A=(NB+d)-(MB+d)=cB,
\]

which proves invariance of (7) and (10).

Since \(N\equiv M\pmod c\) and

\[
\kappa=Ms-Nr\equiv M(s-r)=Mh\pmod c,
\]

we have

\[
NA-\kappa\equiv M(A-h)\pmod c.
\]

The integer \(M\) is a power of two and \(c=N-M\) is odd, so
\(\gcd(M,c)=1\). Hence (8) is integral exactly on the class (7).

Now assume \(A=MB+d\), with \(d\in D\), and put

\[
A'=H_D(A)=NB+d.
\]

The invariant congruence gives

\[
q=\frac{A'-h}{c}\in\mathbb Z.
\]

Using \(A'=cq+h\), (2), and \(h=s-r\),

\[
\begin{aligned}
\nu(A)
&=\frac{N(MB+d)-\kappa}{c}\\
&=\frac{M(NB+d)+cd-\kappa}{c}\\
&=Mq+\frac{Mh+cd-\kappa}{c}\\
&=Mq+r+d.
\end{aligned}
\]

If \(\nu(A)>0\), then \(q\ge0\), because \(q\le-1\) would give
\(Mq+r+d<0\). Therefore the collision hypothesis (1) applies and yields

\[
T^L(\nu(A))=Nq+s.
\]

On the other hand,

\[
\begin{aligned}
\nu(A')
&=\frac{N(cq+h)-\kappa}{c}\\
&=Nq+\frac{Nh-\kappa}{c}\\
&=Nq+s,
\end{aligned}
\]

because

\[
Nh-\kappa=N(s-r)-(Ms-Nr)=s(N-M)=cs.
\]

This proves (9). Iteration proves the counterexample criterion. Since
\(A_0\ge M\), (10) keeps every later induced state at least \(M\), and the
states are strictly increasing. The affine lift (8) is increasing, so the
corresponding Collatz block states are unbounded. ∎

## Dependency audit

- The theorem begins from the exact collision identity (1).
- `L-0001` is one way to verify (1) from parity words and affine constants.
- No infinite existence statement is used.
- `T-0001` is the special case in which \(D\) is an initial interval.

## Gap audit

- A large or dense digit set does not by itself provide an infinite admissible
  orbit.
- Compatible finite digit prefixes may define only an element of the
  \(2\)-adic completion.
- The positivity and finite-integer hypotheses are explicit.
- Translation of a fiber changes the lifting class and must be recorded.

## Adversarial tests

`X-0002` checks the theorem on every member of the length-22, eighteen-branch
fiber and on several lifted values of \(q\). It independently verifies the
normal-form and lifting equations.

## Remaining uncertainty

The finite theorem appears complete but has not been independently
reconstructed. Its counterexample criterion remains conditional on the central
finite-word closure problem.

## Suggested next attack

Treat complete collision fibers, rather than only consecutive runs, as the
vertices of a collision atlas. Optimize not merely cardinality but also carry
cycles, expansion margin, lifting modulus, and compatibility with other charts.
