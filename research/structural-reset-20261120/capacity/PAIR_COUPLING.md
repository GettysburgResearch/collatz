# A physical pair descent with an explicit carry-reset obstruction

**PROPOSED.** The descent blocks and obstruction below are elementary
written proofs. They are not a complete merger selector. The Collatz
conjecture remains open.

## 1. Ordinary graph, sources, and killing

Use the shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

The undirected ordinary merger graph has vertices `N_{>0}` and an edge
between `n` and `T(n)`. Equivalently its physical inverse branches at `y`
are `2y`, and `(2y-1)/3` when `y=2 mod 3`; only positive integral sources
are retained. These are all branches. A component means this complete
graph component, not one selected inverse subtree. Two vertices in a
component have forward iterates equal at finite, possibly different clocks.

Pair states are positive odd pairs `(x,y)`. Each coordinate may move along
a finite path in its own ordinary component. All diagonal pairs are
identified with one absorbing cemetery state: when the coordinates
coincide, a physical merger has been certified. An arbitrary positive
source first reaches its odd part by finitely many legal halvings. No
state is killed merely for being large, divisible by 3, or outside a finite
search range. Statements about this candidate's selected moves do not assert
coverage by every possible pair protocol.

For `x!=y`, set

\[
H(x,y)=\max(x,y),\qquad r(x,y)=v_3(x-y).
\]

The state space is countable with its full power-set sigma algebra. All
costs below are ordinary real-valued functions on this discrete space;
no completion or stationary residue law is used.

## 2. CP-001: one legal map handles all three ternary digits

For a positive odd `n`, define

\[
A(n)=\begin{cases}
(16n+3)/3,&n=0\pmod3,\\
(4n-1)/3,&n=1\pmod3,\\
(2n-1)/3,&n=2\pmod3.
\end{cases}                                                    \tag{1}
\]

Every value is positive, odd, and in the ordinary component of `n`.

For class 2, `T(A(n))=n`. For class 1, `T^2(A(n))=n`. For class 0,
put `J(n)=4n+1`. Then

\[
T^3(J(n))=T(n),\qquad T^2(A(n))=J(n),
\]

so `T^5(A(n))=T(n)`. These identities use actual legal shortcut branches.
In particular the class-0 case is a six-edge physical diagram, not an
illegal odd inverse of a multiple of 3. No convergence hypothesis enters.

If `r(x,y)>=1`, both inputs use the same branch of (1), and

\[
A(y)-A(x)=\frac{c}{3}(y-x),\qquad c\in\{2,4,16\}.                 \tag{2}
\]

Thus `r` decreases by exactly one, and the coordinates remain unequal.
The full common-digit stripping block has exactly `r(x,y)` applications
of (1); it terminates at a positive odd pair of different residues modulo
3. It is finite for every fixed ordinary input pair.

## 3. CP-002: a proper cost decreases throughout the stripping block

Fix a real constant `kappa>log(16/3)`, with natural logarithms, and put

\[
V(x,y)=\log(1+H(x,y))+\kappa r(x,y)\quad(x\ne y),\qquad V(x,x)=0.
                                                                    \tag{3}
\]

Away from the killed diagonal, every sublevel of `V` is finite: `V` is a
proper ordinary pair cost. For a common-digit step,

\[
1+H(A(x),A(y))\le\frac{16}{3}(1+H(x,y)),
\]

and hence

\[
\boxed{V(A(x),A(y))-V(x,y)
       \le\log(16/3)-\kappa<0.}                                    \tag{4}
\]

This is a genuine descent of a proper cost on actual positive integer
pairs. It pays for height growth by consuming a finite, explicitly counted
congruence debt. It does not assert that height itself decreases.

There is also an exact conserved quantity during this mode:

\[
\frac{|x-y|}{2^{v_2(x-y)}3^{v_3(x-y)}}.
                                                                    \tag{5}
\]

Equation (2) proves invariance of (5). More generally every shared legal
affine word made from forward or inverse shortcut branches changes the
difference by a power of 2 times a power of 3. Common-word coupling alone
cannot turn a nonzero difference into zero. A merger needs a different
branch in the two coordinates at some stage.

## 4. CP-003: the exact carry map and a failed closure

At a pair of different residues modulo 3, applying (1) independently is
the simplest fully specified carry proposal. Write

\[
(c_0,b_0)=(16,3),\quad(c_1,b_1)=(4,-1),\quad(c_2,b_2)=(2,-1).
\]

If `x=i mod 3` and `y=j mod 3`, then its new difference is exactly

\[
d'=\frac{c_jy-c_ix+b_j-b_i}{3}.                                    \tag{6}
\]

If `d'=0`, the pair is killed with a finite merger certificate. Otherwise
let `r'=v_3(d')` and follow this carry by exactly `r'` common-digit steps.
This is a complete finite renewal transition back to different ternary
residues. No hidden digit or infinite legality assumption has been dropped.

The tempting assertion that this complete renewal decreases the proper
cost is false on an infinite ordinary family. For every integer `u>=0`,
take

\[
x=18u+3,\qquad y=18u+5.
\]

Their initial ternary depth is zero. The carry gives

\[
A(x)=96u+17,\qquad A(y)=12u+3,
\]

whose difference is `14(6u+1)`, not divisible by 3. Therefore there is no
subsequent stripping credit at all, and

\[
\Delta V=\log\frac{96u+18}{18u+6}>0,
\qquad \frac{96u+18}{18u+6}\longrightarrow\frac{16}{3}.              \tag{7}
\]

No finite exceptional region repairs this failure. The result refutes this
particular reset and this one-block monotone closure, not arbitrary
state-dependent or randomized control of the complete merger graph.

### The concrete remaining interface

A replacement reset must specify actual finite physical paths for both
coordinates, including their clocks and every legality guard. If its
output is unequal with ternary depth `r'`, (4) pays for the next `r'`
stripping steps. The remaining obligation is an amortized inequality for
the complete carry-plus-stripping renewal on its actual transported pair
states. It cannot be inferred from contraction during the stripping mode.

For example, a physical pair kernel `Q` on these renewal states with the
diagonal absorbing and

\[
\mathbb E_Q[V(Z')\mid Z=z]\le V(z)-\epsilon(z),\qquad
\inf_{z\in F}\epsilon(z)>0                                      \tag{8}
\]

for every finite set `F` of off-diagonal states, with `epsilon(z)>0`
everywhere off the diagonal, would close the coupling. Integrability of
the displayed expectation is part of (8). Indeed telescoping gives a
uniform bound on `E V(Z_k)` and finite total expected `epsilon` occupation.
Properness gives tightness off the diagonal, and the positive minimum of
`epsilon` on each finite sublevel then implies
`P(Z_k is off the diagonal)->0`. A positive coalescence probability already
certifies that the two fixed source components coincide. Applied to every
fixed source against 1, this would prove Collatz.

No kernel satisfying (8) is supplied here. Formula (7) is a specific failed
attempt to obtain it. This is a local, actual-state drift target with an
ordinary properness condition, not an assumed vanishing moving-target
inverse sum. It is still a closing obligation, not a new theorem of
convergence.

## 5. CP-004: a physical clock cost for ordinary-distance contraction

Let `a_K=2^K-1`, `b_K=2^K`, with `K>=2`. Their merger-graph distance is
at least `K`, allowing distance infinity. No convergence of `a_K` is
assumed.

To see this, a shortest finite simple graph path has forward orientations
followed by backward orientations: a backward-then-forward switch would
give one vertex two different outgoing edges. Thus a length-`L` path
provides `T^i(a_K)=T^j(b_K)` with `i+j=L`. If `i+j<K`, then

\[
T^i(a_K)=3^i2^{K-i}-1\text{ is odd},\qquad
T^j(b_K)=2^{K-j}\text{ is even},
\]

a contradiction.

Suppose a proposed random pair jump is furnished with physical paths of
lengths `L_x,L_y` in its two coordinates and satisfies

\[
\mathbb E|X'-Y'|\le\rho<1
\]

at every adjacent pair. Integer separation implies
`P(X'=Y')>=1-rho`. At `(a_K,b_K)`, coalescence forces
`L_x+L_y>=K`, and therefore

\[
\mathbb E(L_x+L_y)\ge(1-\rho)K.                                  \tag{9}
\]

In particular bounded-radius or uniformly bounded-mean physical jumps
cannot achieve that uniform ordinary-distance contraction. This justifies
an unbounded, state-dependent renewal budget; it does not obstruct one.

## 6. CP-005: why component closure supplies no prime-height retention

For an escaping positive orbit, every fixed source in the same merger
component has the same forward tail after two finite clocks. Thus the
prime-height dispersion property of the companion adelic packet transfers
to every fixed source in that component; a different ancestor is not a
fresh asymptotic history.

For completeness, under the odd accelerated map the upward logarithmic
increment is at most 1. If `x_j=log_2 n_j` tends to infinity and
`W_N=sum_{j<N}x_j`, then `W_N/N->infinity`. A fixed number of terminal
terms is `O(N)`, because `x_j<=x_0+j`, and is therefore `o(W_N)`; finite
initial terms also have vanishing relative weight. The same bounds hold
for height contributed by any prime set because that height is at most
`x_j`. Finite shifts consequently preserve the weighted dispersion limit,
uniformly over prime sets of bounded cardinality. Count-density assertions
are invariant under finite shifts as well.

Backward closure does put `2^k n_0` in the component for every `k`. These
are supported on the fixed finite prime set consisting of 2 and the prime
divisors of `n_0`. But the retained prime height belongs to a changing
finite preperiod: after `k` halvings, every such source reaches `n_0` and
then has its original tail. This does not give repeated prime retention
on one fixed ordinary escaping history. The missing retention mechanism
cannot be obtained by exchanging that source-dependent preperiod with an
all-time limit.
