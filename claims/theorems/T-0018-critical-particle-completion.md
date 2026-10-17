# T-0018 — Critical particle completion and the ordinary Collatz spine

Claim ID: `T-0018`  
Title: An exact ordered-particle branching completion whose distinguished boundary spine is ordinary Collatz  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-0013`, `T-0017`  
Scope: exact finite particle rewrite system, phase escape measure, and ordinary-integer boundary marker  
Related counterexample candidates: none

## Statement

Put

\[
R_0(x)=\left\lfloor\frac{x}{2}\right\rfloor,
\qquad
R_1(x)=\left\lceil\frac{3x}{2}\right\rceil
\qquad(x\ge0).
\tag{1}
\]

These are the shifted phase maps:

\[
R_e(x)=S_e(x+1)-1.
\tag{2}
\]

For a positive integer \(x\), regard

\[
[x]=\{1,2,\ldots,x\}
\]

as an ordered population of particles. Give every parent particle exactly two children by the following finite local rules.

For \(k\ge1\),

\[
\boxed{
2k
\longmapsto
(0,k),\ (1,3k),
}
\tag{3}
\]

and

\[
\boxed{
2k-1
\longmapsto
(1,3k-2),\ (1,3k-1).
}
\tag{4}
\]

The first coordinate is a branch bit and the second is the child's rank inside that branch.

Then:

### 1. Exact branch populations

For every \(x\ge1\):

- the branch-zero children of the parents in \([x]\) have ranks
  
  \[
  1,2,\ldots,R_0(x)
  \]
  
  exactly once;
- the branch-one children have ranks
  
  \[
  1,2,\ldots,R_1(x)
  \]
  
  exactly once.

Consequently

\[
\boxed{R_0(x)+R_1(x)=2x,}
\tag{5}
\]

and the two branch populations contain exactly \(2x\) children in total.

### 2. Exact finite-word mass conservation

For a binary word

\[
w=e_0e_1\cdots e_{L-1},
\]

let

\[
R_w=R_{e_{L-1}}\circ\cdots\circ R_{e_0}.
\]

After \(L\) particle rewrites, the population in branch cylinder \(w\) is exactly

\[
R_w(x).
\]

Every root particle has exactly \(2^L\) descendants, and

\[
\boxed{
\sum_{|w|=L}R_w(x)=2^Lx.
}
\tag{6}
\]

### 3. Escape measure as a uniform descendant spine

Choose one of the \(2^Lx\) depth-\(L\) descendants uniformly and record only its branch word. Then

\[
\boxed{
\mathbb P_x([w])=\frac{R_w(x)}{2^Lx}.
}
\tag{7}
\]

For the phase \(v=x+1\), this is exactly the Doob escape measure of `T-0017`:

\[
\boxed{
\mathbb P_x([w])
=
\mathbb Q_{x+1}([w]).
}
\tag{8}
\]

Thus the phase-escape process is the size-biased branch projection of a completely finite, mass-conserving particle rewrite tree.

### 4. Distinguished ordinary child

Give every parent \(j\ge1\) one distinguished child:

\[
\boxed{
\chi(j)=
\begin{cases}
(0,j/2),&j\text{ even},\\[1mm]
(1,(3j+1)/2),&j\text{ odd}.
\end{cases}
}
\tag{9}
\]

This child is present in (3)--(4), and its rank is exactly

\[
\boxed{T(j).}
\tag{10}
\]

Iterating distinguished children from a finite root particle \(j\) produces:

- the ordinary shortcut-Collatz trajectory
  
  \[
  j,T(j),T^2(j),\ldots;
  \]
- its unique chronological parity word;
- one marked descendant at every depth.

The ordinary Collatz map is therefore a deterministic marked spine inside the critical particle completion.

### 5. Right-boundary identity

Take the root population \([j]\), and let \(w_L(j)\) be the first \(L\) ordinary Collatz parities of the rightmost particle \(j\). Then

\[
\boxed{
R_{w_L(j)}(j)=T^L(j).
}
\tag{11}
\]

The distinguished child of the rightmost root is again the right boundary of the selected branch population.

### 6. Finite ordinary-boundary certificate

Suppose a finite string-rewrite grammar:

1. begins with one finite marked particle \(j_0\ge1\);
2. implements only the local rules (3)--(4);
3. always sends the marker through the distinguished child (9);
4. proves that the marked ranks are unbounded, or at least never enter the terminal \(1\leftrightarrow2\) cycle.

Then \(j_0\) is a positive-integer Collatz counterexample.

This criterion carries an explicit ordinary boundary marker at every finite stage and cannot silently degenerate into a merely 2-adic path.

## Proof

### One-step population structure

The even parents are \(2,4,\ldots,2\lfloor x/2\rfloor\). Rule (3) gives their branch-zero children the ranks

\[
1,2,\ldots,\left\lfloor\frac{x}{2}\right\rfloor,
\]

proving the branch-zero claim.

For each complete parent pair

\[
2k-1,\ 2k,
\]

rules (4) and (3) give the three consecutive branch-one ranks

\[
3k-2,\ 3k-1,\ 3k.
\]

If \(x\) is odd, the final unpaired parent contributes the next two ranks. Hence the branch-one ranks form exactly

\[
1,2,\ldots,\left\lceil\frac{3x}{2}\right\rceil.
\]

This proves part 1 and (5).

Every parent has exactly two children, so after \(L\) levels every root has \(2^L\) descendants. The branch population recursion is exactly \(R_e\), giving (6) by induction.

Equation (7) is the fraction of all descendants lying in cylinder \(w\). Since

\[
S_w(x+1)-1=R_w(x),
\]

`T-0017` gives

\[
\mathbb Q_{x+1}([w])
=
2^{-L}
\frac{S_w(x+1)-1}{x}
=
\frac{R_w(x)}{2^Lx},
\]

proving (8).

If \(j=2k\), rule (3) contains the child \((0,k)\), whose rank is \(j/2=T(j)\). If \(j=2k-1\), rule (4) contains the right child

\[
(1,3k-1),
\]

whose rank is

\[
3k-1=\frac{3j+1}{2}=T(j).
\]

This proves (9)--(10). Iteration proves the ordinary-spine statement. Applying the same branch maps to the full population \([j]\) proves (11).

Finally, a marked derivation satisfying conditions 1--3 is exactly the deterministic shortcut-Collatz orbit of the finite integer \(j_0\). Condition 4 makes it a counterexample. ∎

## Combinatorial interpretation

Each adjacent parent pair undergoes the rewrite

```text
2 ordered parents
    -> 1 child in branch 0
    -> 3 children in branch 1
```

while a final unpaired odd parent produces two branch-one children. The multipliers \(1/2\) and \(3/2\) are therefore literal population ratios.

The identity

\[
R_0(x)+R_1(x)=2x
\]

is the combinatorial source of the phase martingale and the phase–Kraft identities.

## Strategic consequence

The phase escape transform and the ordinary Collatz boundary are distinct pieces of structure:

- the escape transform chooses a branch by endpoint population size;
- an ordinary starting integer is a **marked root particle**;
- its Collatz trajectory is one distinguished descendant lineage.

A successful rewrite proof must preserve the marked lineage, not merely construct a large or escaping unmarked phase population.

## Gap audit

- The particle completion contains many auxiliary descendants that are not ordinary Collatz steps of their parent labels.
- Positive escape measure for an unmarked branch language does not imply that the language contains the distinguished spine of a finite root.
- The theorem does not construct an unbounded distinguished spine.

## Adversarial tests

`X-0010` verifies the ordered child partitions, the \(2^Lx\) mass identity, the escape path probabilities, and the distinguished ordinary spines over large finite ranges.

## Suggested next attack

Search for a finite or pushdown **marked-particle grammar**. The unmarked particle population may supply expansion and phase potentials, but a separate boundary-marker rule must force the distinguished child indefinitely. This is the string-rewrite form of the ordinary-versus-adic problem.