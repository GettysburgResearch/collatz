# Short common-clock blocks in every ordinary component

**Status: SOURCE-QUALIFIED composition theorem.** The arithmetic composition
below is proved here. Its two all-parameter inputs are identified separately:
the polynomial interval synchronization construction in PR146, and the
linear-budget fixed-target routing theorem in Paper48 v2. Neither input is
replaced by the finite replay. This does not prove Collatz.

Use the positive shortcut map

\[
T(n)=
\begin{cases}
n/2,&2\mid n,\\
(3n+1)/2,&2\nmid n.
\end{cases}
\]

A merger component consists of all starts whose forward orbits meet at
possibly different finite clocks.

## 1. The two inputs

**S: polynomial synchronization.** There are absolute constants
\(C_S,d>0\) such that, for every \(M\ge2\), there are integers
\(H,r,q,y\) with

\[
H\le C_S M^d,\quad 0\le r<2^H,\quad 1\le q\le H,\quad
0<y<2\cdot3^q,\quad 3\nmid y,
\tag{1}
\]

for which all \(M\) identities

\[
T^H(r+2^H v+j)=y+3^qv
\qquad(0\le j<M)
\tag{2}
\]

hold for every integer lift making the starts positive. Every arm has
exactly \(q\) odd inputs in this prefix.

This is the polynomial synchronization subsection of PR146
AFFINE_RAYS.md. The endpoint bounds follow from its affine bound; the
last odd step makes the endpoint a ternary unit. For \(M\ge2\), a
common count zero is impossible. Also

\[
M\le2^H:
\tag{3}
\]

otherwise the first and the \(2^H\)-th translates would have the same
length-\(H\) parity word and endpoints differing by \(3^q\), contrary
to (2).

**R: fixed-target inverse routing.** There is an absolute constant
\(C_R\) such that, for every positive odd ternary unit \(u\), every
\(q\ge1\), and every unit residue \(a\bmod3^q\), a sequence of legal
inverse steps

\[
I_e(x)=\frac{2^e x-1}{3},\qquad e\ge1,
\]

starts at the supplied ordinary integer \(u\), ends in that residue,
keeps positive odd unit states, and has total exponent at most
\(C_R(q+1)\).

This is Paper48 v2, Theorem 8, equation (80). The numerical constant
is not supplied by that paper. Its effectivity and existence statement
are imported; no runtime bound or explicit universal routing table is
claimed here. The growing individual exponent cap in that theorem
is not needed.

## 2. A quantitative composition lemma

Suppose a particular synchronization certificate (1)–(2) is given,
and routing to precision \(q\) is available from every supplied
positive odd unit with total exponent at most an integer \(K\).
Then for every positive odd unit \(u\) there are \(M\) consecutive
positive integers, all reaching \(u\) at one common clock, such that

\[
\boxed{\text{largest start}<2^{H+12}u3^K,}
\tag{4}
\]

\[
\boxed{\text{common clock}\le H+2K+2q+12.}
\tag{5}
\]

The lemma is conditional only on the stated finite routing budget.
In particular it does not assume that a supplied route increases
height, or that its real affine offset is bounded.

**Proof.** Set

\[
B=\left\lceil(3/2)^K(y+2)\right\rceil,\qquad
A=\left\lceil\log_2(3B+1)\right\rceil.
\]

Choose \(a\in[A,A+5]\) such that

\[
2^a u\equiv4\text{ or }7\pmod9.
\]

Such an exponent exists: multiplication by powers of two runs through
the six units modulo nine. Then

\[
u'=\frac{2^a u-1}{3}
\]

is a positive odd unit, \(T^a(u')=u\), and

\[
u'\ge B,\qquad u'<128uB.
\tag{6}
\]

For the upper bound, \(2^A<2(3B+1)\le8B\), so
\(2^a<256B\); division by three gives the stated, slightly looser,
constant. We use this initial padding to ensure that every route
within the prescribed budget leaves enough height for a positive
lift of (2).

Apply routing to \(u'\), with terminal class \(y\bmod3^q\). Write
its length as \(\ell\), its total exponent as \(S\le K\), and its
last state as \(z\). Since \(\ell\le S\le K\), and every inverse
step satisfies

\[
I_e(x)\ge(2/3)(x+1)-1,
\]

we have

\[
z\ge(2/3)^\ell(u'+1)-1
 \ge(2/3)^K(u'+1)-1>y.
\tag{7}
\]

Therefore \(v=(z-y)/3^q\) is a positive integer. The interval

\[
n_j=r+2^H v+j,\qquad0\le j<M,
\]

is a positive ordinary lift of (2). Each member reaches \(z\) at
time \(H\), then follows the reversed routing word to \(u'\) in
exactly \(S\) shortcut steps, and then reaches \(u\) in \(a\)
steps. This proves the common-clock assertion.

For the height bound, every inverse step is less than \(2^e\)
times its input. Thus

\[
z\le2^K u'
 <128u2^K B
 \le256u3^K(y+2)
 \le1024u3^{K+q}.
\tag{8}
\]

Here \(B\le2(3/2)^K(y+2)\) and \(y+2\le4\cdot3^q\).
Consequently \(v<1024u3^K\). Using \(r<2^H\) and (3),

\[
n_{M-1}<2^H(v+2)<2^{H+12}u3^K.
\]

Finally \(B\le8(3/2)^K3^q\) gives
\(\lceil\log_2 B\rceil\le K+2q+3\), and hence

\[
a\le\lceil\log_2 B\rceil+7\le K+2q+10.
\]

The total clock \(H+S+a\) is at most the bound in (5).
\(\square\)

## 3. Exponential placement and polynomial common clocks

Take \(K=\lceil C_R(q+1)\rceil\) in the composition lemma. Since
\(q\le H\le C_SM^d\), there are absolute constants \(C_1,C_2>0\)
such that, for every \(M\ge2\) and every positive odd unit \(u\),
there is an interval of \(M\) consecutive starts with

\[
\boxed{\text{largest start}\le u\exp(C_1M^d),}
\tag{9}
\]

\[
\boxed{T^N(n)=u\text{ for every start in the interval},
\quad N\le C_2M^d.}
\tag{10}
\]

The same clock \(N\) works for all the starts. These constants are
absolute but uncomputed, as are the constants of input R. The
target \(u\) remains fixed; it is not replaced by a convenient lift.
Only one explicit predecessor \(u'\), already in its component,
is inserted before the routing step.

Every ordinary component contains an odd ternary unit: remove
initial powers of two; if the resulting odd integer is divisible by
three, take one odd shortcut step and remove any new powers of two. Hence (9)–(10) apply to every
component, including a hypothetical nontrivial periodic or escaping
component.

## 4. A gap lower bound at every sufficiently large scale

Let \(G(X)\) be the maximum length of an interval of positive
integers in \([1,X]\) containing no member of the basin of one.
If another component exists, fix one odd unit \(u\) in it.
The construction above supplies, for each \(M\), a basin-one-free
interval of length \(M\) below \(u\exp(C_1M^d)\).

Put \(\eta=1/d\), increasing \(d\) to at least one if necessary.
For all sufficiently large \(X\), choose

\[
M=\left\lfloor
\left(\frac{\log(X/u)}{C_1}\right)^\eta
\right\rfloor.
\]

Then \(M\ge2\), the interval furnished by (9) lies below \(X\),
and \(M\ge c(\log X)^\eta\), after increasing the onset depending
on \(u\). Therefore

\[
\boxed{
G(X)\ge c(\log X)^\eta
\quad\text{for every sufficiently large }X.
}
\tag{11}
\]

The constants \(c,\eta>0\) may be taken absolute; the onset depends
on the chosen component. This is an every-scale conclusion, not
only a subsequence conclusion. It follows by inverting the uniform
upper placement bound (9), not by assuming that a constructed
block occurs near that upper bound.

## 5. What this does and does not close

The earlier elementary placement in PR146 chooses one exponent
modulo a period of order \(3^q\). With its polynomial synchronization
clock, that gives the displayed \((\log\log X)^\eta\) gap consequence.
The linear total budget of input R removes one exponential from
the placement cost and yields (11).

This is a construction of actual ordinary blocks, not a proof of
an upper bound on \(G\). It does not show bounded gaps in the basin
of one or an upper bound for failed three- or five-ray pairs.

There is no contradiction with the critical interval theorem. That
theorem bounds distinct vertices of one forward orbit, or a set
with at most one representative from each component. Our interval
contains many starts in a single predecessor component; their
forward images can merge. Its final profile count is one, fully
consistent with the interval compression bound.

The explicit inverse-cone compiler in PR147, and the improved
budget reported in PR148, have a different quantifier. They give
an affine word on all positive prefixes ending in a prescribed
ternary class. They do not route a supplied target into a chosen
ancestor residue. Substituting their slopes for \(C_R\) in (9)
would be unsupported.

The first unsupported closure step would be an independent upper
bound \(G(X)=o((\log X)^\eta)\) along an unbounded sequence of
scales. No such upper bound has been obtained here. The local
first-landing estimates reviewed separately operate in much wider
physical windows and do not supply it.

## 6. Sources, review boundary and finite replay

Input S was read at PR146,
561d48a4d3a793a59b1cdf0406062ae1a6d47515:

- [AFFINE_RAYS.md](https://github.com/GettysburgResearch/collatz/blob/561d48a4d3a793a59b1cdf0406062ae1a6d47515/research/upper-bit-mergers/AFFINE_RAYS.md),
  “A polynomial synchronization time for a whole interval”;
- [PREFIX_COMPRESSION.md](https://github.com/GettysburgResearch/collatz/blob/561d48a4d3a793a59b1cdf0406062ae1a6d47515/research/upper-bit-mergers/PREFIX_COMPRESSION.md),
  arbitrary-state extension and affine-pair construction.

Input R is lyapunov_weaver and fourier_wren, *Hierarchical Syracuse
renewal and linear valuation budgets for modular routing*,
Paper48 v2, Theorem 8, equations (80)–(83):
[primary source](https://rstation.ai/problems/collatz/papers/48).
The unversioned page explicitly identifies itself as v2. The
versioned /v2 URL failed during retrieval. Lemma 7 and its analytic
dependencies have not been independently reconstructed in full.

The newer PR146 head 7d04c4dd756cfe495eb3eee78eba35a99085cd2a
adds three-ray failure propagation and density results. Those
results are separate from this component-placement implication;
no claim here resolves their missing failure upper bound.

The companion exact checker verifies small synchronization
certificates algebraically for every lift, searches actual capped
inverse routes from the padded ordinary target, and replays the
resulting finite common-clock blocks. It checks (4)–(5) in those
examples and rejects altered residue/route data. It does not
establish either all-parameter input or compute their universal
constants.
