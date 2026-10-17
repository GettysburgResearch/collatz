# L-0004 — Carry-cycle pumping for every collision chart

Claim ID: `L-0004`  
Title: Finite mixed-radix carry cycles and a universal zero-output stack amplifier  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0001`; applications to Collatz charts use `T-0002`  
Scope: exact finite mixed-radix rewrites and parameterized finite horizons  
Related counterexample candidates: none

## Statement

Let \(1<M<N\) be coprime. Use low-order-first digit constructors

\[
L_x(y)=My+x,
\qquad
R_c(y)=Ny+c,
\]

with \(0\le x<M\) and \(0\le c<N\). The local normalization rule is

\[
R_cL_x\longrightarrow L_eR_q
\quad\Longleftrightarrow\quad
Nx+c=Mq+e.
\tag{1}
\]

### 1. Carry-cycle pumping

Fix an output word

\[
E=(e_0,e_1,\ldots,e_{k-1}),
\qquad0\le e_i<M,
\]

and an initial carry \(c_0\in\{0,1,\ldots,N-1\}\). Recursively define
\(c_{i+1}\) as the least nonnegative residue satisfying

\[
c_{i+1}\equiv M^{-1}(c_i-e_i)\pmod N,
\tag{2}
\]

and put

\[
x_i=\frac{Mc_{i+1}+e_i-c_i}{N}.
\tag{3}
\]

Then \(0\le x_i<M\), and (1) holds at every column. If

\[
c_k=c_0,
\tag{4}
\]

then, for the input word \(X=(x_0,\ldots,x_{k-1})\),

\[
\boxed{
R_{c_0}X\longrightarrow E R_{c_0}.
}
\tag{5}
\]

The cycle can be pumped horizontally:

\[
\boxed{
R_{c_0}X^m\longrightarrow E^mR_{c_0}
}
\tag{6}
\]

for every \(m\ge0\).

### 2. Universal zero-output cycle

Let \(D\subseteq\{0,1,\ldots,M-1\}\) be the admissible alphabet of a
partial radix map

\[
H_D(MB+d)=NB+d,
\qquad d\in D.
\tag{7}
\]

Assume \(0,j\in D\) with \(j\ne0\). Let \(k\) be the least positive integer
such that

\[
M^k j\equiv j\pmod N.
\tag{8}
\]

Take \(E=0^k\), \(c_0=j\), and construct \(W_j=X\) from (2)--(3). Then

\[
\boxed{
R_jW_j\longrightarrow L_0^kR_j.
}
\tag{9}
\]

If \(W_j(x)\) denotes the word followed by a nonnegative high-order context
\(x\), then

\[
W_j(x)=M^kx+\frac{j(M^k-1)}{N}.
\tag{10}
\]

For \(m\ge0\), define

\[
S_{m,j}(x)=L_jW_j^m(x).
\tag{11}
\]

The next \(km+1\) induced steps are all defined, and

\[
\boxed{
H_D^{km+1}(S_{m,j}(x))
=N^{km}(Nx+j).
}
\tag{12}
\]

Thus every nontrivial collision fiber, translated so that its least digit is
zero, possesses an exact finite-horizon stack amplifier.

## Definitions

For a low-order-first word \(U=(u_0,\ldots,u_{k-1})\), write

\[
[U]_M=\sum_{i=0}^{k-1}u_iM^i.
\]

The notation \(U^m\) denotes \(m\) concatenated copies.

## Motivation

`L-0002` found one nine-column zero-output cycle for the `64 -> 81` chart.
The present lemma shows that this is not an isolated gadget. Carry pumping is a
universal algebraic feature of every coprime radix pair, and the zero-output
amplifier exists for every induced collision chart with at least two digits.
The real research question is therefore not whether local stacks exist, but
whether several pumped tiles can close vertically into one finite, infinite
orbit.

## Proof

Equation (2) makes the numerator in (3) divisible by \(N\). Since
\(0\le c_i<N\), \(0\le e_i<M<N\), and \(0\le c_{i+1}<N\), that numerator is
strictly greater than \(-N\) and strictly less than \(MN\). A negative
multiple of \(N\) in this interval is impossible, so
\(0\le x_i<M\). Rearranging (3) gives (1).

Following the \(k\) local rules moves the carry from \(c_0\) to \(c_k\) and
emits \(E\). Under (4), this proves (5). Concatenating the same closed carry
path proves (6).

For the zero-output specialization, (2) becomes

\[
c_{i+1}\equiv M^{-1}c_i\pmod N.
\]

Condition (8) is exactly the statement that this carry orbit returns to
\(j\), proving (9). The numerical equality represented by (9) is

\[
N W_j(x)+j=M^k(Nx+j).
\tag{13}
\]

Putting \(x=0\) gives

\[
N[W_j]_M+j=M^kj,
\]

which proves (10). Repetition of (9) gives

\[
H_D(S_{m,j}(x))=M^{km}(Nx+j).
\tag{14}
\]

The low \(km\) base-\(M\) digits in (14) are zero. Each is admissible, and a
zero step replaces one factor \(M\) by one factor \(N\). After \(km\)
additional steps, (12) follows. ∎

## Dependency audit

- The carry theorem is independent of Collatz and uses only coprime integer
  radices.
- `T-0002` is required only to lift an induced-map amplifier back to a finite
  Collatz block.
- `L-0002` is the case \((M,N,D,j,k)=(64,81,\{0,1\},1,9)\).

## Gap audit

- Equation (12) is finite-horizon only.
- Repeating \(W_j\) infinitely would define an infinite base-\(M\) word, not
  automatically an ordinary integer.
- General output cycles (5) can emit admissible words, but vertical closure of
  those words is an additional two-dimensional compatibility problem.
- The cycle length can be enormous; local existence is not the correct quality
  measure by itself.

## Adversarial tests

`X-0002` reconstructs the zero cycles from modular arithmetic, verifies every
local rule, checks (10)--(12) on several contexts, and recovers the nine-column
block of `L-0002` exactly.

## Remaining uncertainty

The finite lemma appears complete but has not been independently reviewed.

## Suggested next attack

Build a finite **macro-tile grammar** from several carry cycles (5). A
successful grammar must arrange that the emitted admissible words of one row
serve as the controlled input structure of later rows while a finite
high-order boundary is regenerated rather than replaced by an adic tail.
