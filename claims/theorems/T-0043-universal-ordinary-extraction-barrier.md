# T-0043 — Universal ordinary-extraction barrier for nested affine cylinders

Claim ID: `T-0043`  
Title: Infinite finite-prefix compatibility yields an ordinary integer exactly when the pulled-back high blocks eventually vanish  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-25  
Dependencies: elementary divisibility; applications use the exact affine maps of the relevant branch  
Scope: nested residue systems and every current dyadic affine/collision/refund architecture  
Related counterexample candidates: none

## 1. Nested-modulus theorem

Let

\[
1<M_0\mid M_1\mid M_2\mid\cdots,
\qquad M_n\longrightarrow\infty,
\]

and let

\[
0\le R_n<M_n
\]

be compatible least representatives:

\[
R_{n+1}\equiv R_n\pmod {M_n}.
\tag{1}
\]

Put

\[
q_n={M_{n+1}\over M_n}
\]

and define the appended block `a_n` by

\[
\boxed{
R_{n+1}=R_n+a_nM_n,
\qquad0\le a_n<q_n.}
\tag{2}
\]

Then:

### 1. Completion existence

There is one point in the inverse limit of the residue systems represented by
`(R_n)`.  In the dyadic case it is the convergent `2`-adic series

\[
\boxed{
\widehat R
=R_0+\sum_{n\ge0}a_nM_n.}
\tag{3}
\]

### 2. Nonnegative ordinary extraction

The following are equivalent:

1. one `R in Z_(>=0)` satisfies
   \[
   R\equiv R_n\pmod {M_n}
   \qquad(n\ge0);
   \]
2. the least representatives `R_n` are bounded in the ordinary real order;
3. the sequence `R_n` is eventually constant;
4. the appended blocks satisfy
   \[
   \boxed{a_n=0\quad\text{for all sufficiently large }n.}
   \tag{4}
   \]

When these hold, the eventual constant is the unique ordinary nonnegative
integer in every cylinder.

### 3. Signed ordinary extraction

A negative ordinary integer `-c`, with `c>0`, lies in every cylinder exactly
when

\[
\boxed{M_n-R_n=c}
\]

for every sufficiently large `n`.  Equivalently,

\[
\boxed{a_n=q_n-1\quad\text{for all sufficiently large }n.}
\tag{5}
\]

Thus a compatible path represents a signed ordinary integer exactly when its
new high blocks are eventually all zero or eventually all maximal.  Every other
compatible path is a genuine completion object rather than an ordinary integer.

### Proof

Compatibility and the least-representative ranges give the unique digit
expansion (2).  In particular `R_(n+1)>=R_n`, so `(R_n)` is nondecreasing.
Boundedness is therefore equivalent to eventual constancy, which is equivalent
to (4).

If an ordinary `R>=0` belongs to every cylinder, then once `M_n>R`, its least
residue modulo `M_n` is exactly `R`; hence `R_n=R` eventually.  The converse is
immediate.

If `R=-c<0`, then once `M_n>c`, its least residue is `M_n-c`.  This gives the
stated complement condition, and substitution in (2) gives `a_n=q_n-1`.
Conversely, an eventual maximal tail makes `M_n-R_n` constant and therefore
represents the corresponding negative integer.  ∎

## 2. Pullback theorem for odd-affine path systems

Fix a finite or countable control path in an exact affine system

\[
\boxed{
2^{d_n}x_{n+1}=u_nx_n+c_n,}
\tag{6}
\]

where every `d_n>=1` and every `u_n` is odd.  Put

\[
D_N=\sum_{n=0}^{N-1}d_n.
\]

Composing the first `N` steps gives

\[
2^{D_N}x_N=U_Nx_0+C_N,
\qquad U_N\text{ odd}.
\tag{7}
\]

Therefore exact integrality of the first `N` steps selects one initial residue

\[
\boxed{
x_0\equiv R_N:=-U_N^{-1}C_N\pmod {2^{D_N}}.}
\tag{8}
\]

Choose `R_N` least and nonnegative.  The residues are compatible, because every
state satisfying `N+1` steps also satisfies the first `N`, and (8) is unique.
Hence the nested-modulus theorem applies.

Consequently:

> A fixed infinite legal control path has one ordinary nonnegative initial
> integer if and only if its pulled-back least initial residues eventually stop
> acquiring nonzero high binary blocks.

This is the exact missing inference between finite compatibility and an
ordinary infinite orbit.

## 3. Finite compatibility cannot supply that inference

Every finite prefix of (6) has infinitely many ordinary lifts:

\[
x_0=R_N+2^{D_N}k,
\qquad k\in\mathbb Z.
\]

Finitely branching compactness or König's lemma may select one infinite control
path and therefore one compatible completion.  It does not prove (4).

The logical gap is real, not a technicality.  For example, take `M_n=2^n` and
choose appended bits

\[
a_n=
\begin{cases}
1,&n\text{ even},\\
0,&n\text{ odd}.
\end{cases}
\]

Every finite prefix has an ordinary nonnegative representative, and the
cylinders are compatible forever.  The appended bits are neither eventually
zero nor eventually one, so the intersection contains no signed ordinary
integer.

Thus there is no valid general theorem of the form

\[
\boxed{
\text{infinite legal path}
\Longrightarrow
\text{ordinary integer}.}
\]

Any successful extraction must use additional arithmetic that proves eventual
zero or maximal high blocks for the specific path.

## 4. Repository-wide audit

The theorem separates what the current architectures do and do not establish.

### Collision fibers, amplifiers, and complete-projection selectors

They prove exact finite branch identities and abundant finite anchors.  By
`L-0039`, even complete low-bit projection does not orient a branch at the
current integer's full source residue.  They do not prove eventual-zero
pullback blocks.

### Fixed-modulus PDR, regular grammars, and periodic lassos

They can prove safety in a residue quotient or identify recurrent completion
states.  Unless a canonical finite top boundary is retained, a recurrent lasso
proves a periodic completion, not an ordinary integer.  In the present theorem,
its missing obligation is again (4) or (5).

### Room, Cantor, logarithmic-full-shift, and branch-isometry programs

They identify one real or `2`-adic point for each infinite directive and may
prove exact local surjectivity.  Local full branches settle existence in the
completion.  They do not imply that the pulled-back ordinary residue digits have
finite support.

### Multiplicative-refund and primitive-core machines

These are the genuinely integer-first constructive lane.  If one explicit
finite state is proved to remain in the exact domain forever, no separate
compactness extraction is needed: its starting integer is already written.
The current claims establish physical replay, growth after legality, intrinsic
markers, and substantial future-cylinder capacity, but not all-time domain
membership.  A directive-first reformulation of the same machine is still
subject to (4).

### Positive-cycle programs

A positive cycle is different.  For a finite accelerated word, the candidate
is the rational fixed point

\[
x={C\over 2^A-3^k}.
\]

Full-denominator divisibility and exact replay are already a finite ordinary
certificate.  No infinite extraction step remains.  This is why the cycle
funnel and the ordinary-refund funnel are the two genuinely distinct global
blockers.

## 5. A precise weaker target

For any one fixed restricted affine machine `M`, define its **ordinary
extraction dichotomy**:

- **positive side:** exhibit one legal control path whose pulled-back blocks are
  eventually zero and whose eventual value satisfies the machine's positivity
  and physical replay gates;
- **negative side:** prove that every infinite legal control path has infinitely
  many nonzero pulled-back blocks.

A positive result gives an explicit ordinary starting integer and therefore a
`K`-candidate whenever the machine's block maps are physically expanding.

A negative result eliminates every ordinary trajectory in that entire machine.
It is genuinely weaker than the Collatz conjecture because it says nothing
about trajectories outside the chosen restricted architecture.

For the repository's common multiplicative-refund funnel, proving the negative
side simultaneously for the fixed six-branch chart, negative-three run chart,
phase-`-34` intrinsic core, and `H` renewal machine would eliminate the complete
current direct-divergence portfolio without proving Collatz.

## 6. Exact consequence for finite-state pullback controllers

Suppose a finite controller emits the appended blocks `a_n` themselves.  Its
output is eventually periodic.  By Sections 1--2, an ordinary nonnegative start
is possible only if the recurrent output cycle is the all-zero cycle; a negative
ordinary start is possible only if it is the all-maximal cycle.

Therefore every recurrent nonzero/nonmaximal SCC in a finite pullback-digit
controller is a completion ghost and may be rejected without further Collatz
analysis.  This does not exclude controllers that retain the exact unbounded
integer or most-significant boundary.

## Strategic conclusion

The repository has made genuine progress in reducing many syntactically
different constructions to one exact question.  But finite-prefix abundance,
large alphabets, positive pressure, conditional growth, and completion-level
surjectivity do not answer that question.

The load-bearing inference is precisely

\[
\boxed{
\text{compatible pulled-back cylinders}
+\text{eventual zero high blocks}
\Longrightarrow
\text{one ordinary positive start}.}
\]

The first premise is abundant.  The second is currently absent.

## Gap audit

- The theorem diagnoses and normalizes the blocker; it does not construct the
  eventual-zero path.
- It does not prove that every current refund machine is empty.
- Zero Haar measure, zero Hausdorff dimension, or sparse source density do not
  imply absence of ordinary integers.
- The positive-cycle denominator problem remains a separate finite route.
- No Collatz counterexample is claimed.
