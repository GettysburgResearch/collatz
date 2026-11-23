# Fixed affine marked covers require unbounded clocks

Research checkpoint, 2026-11-21 UTC. This is a written mathematical proof,
not an additional Lean-checked theorem. No full Collatz proof is claimed.

## Precise scope

Use the shortcut map

\[
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2.\end{cases}
\]

For a positive integer, write \(d=\lfloor\log_2 n\rfloor\). Call it
marked when it is odd and

\[
(d+1)(n-2^d)\le70\,2^d.
\]

A *fixed affine rule* in this note consists of constants
\(\alpha,\beta\in\mathbb R\) and fixed nonnegative integer clocks \(a,b\).
An application to an integer \(n\) is valid only when

\[
x=\alpha n+\beta\in\mathbb N_{>0},\qquad x<n,
\qquad x\text{ is marked},\qquad T^a(x)=T^b(n).
\]

The source is also required to be marked. The rule may have any additional
residue or word guards. There is no assumption that the affine merger identity
holds on a full residue class: the theorem below works even when a rule is
applied only at isolated verified integer inputs.

**Theorem.** No finite collection of these fixed affine, fixed-clock rules,
even with finitely many separately proved terminal exceptions, supplies a
valid application for every sufficiently large marked positive integer.

More strongly, such a finite collection cannot cover every sufficiently large
member of any unbounded marked family whose initial consecutive odd-run
length tends to infinity.

This does **not** rule out finite parameterized rule schemes with unbounded
clocks, a sequence of administrative rewrites that is not a fixed affine map,
intermediate partners that are not marked, a rank other than ordinary source
size, or the full Yolcu–Aaronson–Heule rewriting architecture.

## 1. Marked-to-marked affine slopes are dyadic

Suppose \(n_j\to\infty\), both \(n_j\) and
\(x_j=\alpha n_j+\beta\) are marked, and \(\alpha>0\). Write
\(d_j=\lfloor\log_2 n_j\rfloor\) and
\(e_j=\lfloor\log_2 x_j\rfloor\). The band condition gives

\[
1\le\frac{n_j}{2^{d_j}}\le1+\frac{70}{d_j+1},\qquad
1\le\frac{x_j}{2^{e_j}}\le1+\frac{70}{e_j+1}.
\]

Both ratios tend to one. Consequently

\[
2^{e_j-d_j}
=\frac{x_j}{n_j}
  \frac{n_j/2^{d_j}}{x_j/2^{e_j}}
\longrightarrow\alpha.
\]

The powers of two form a discrete subset of the positive reals. A sequence
of such powers converging to a positive finite limit is eventually constant.
Therefore \(\alpha=2^z\) for some integer \(z\). If also \(x_j<n_j\),
then \(\alpha\le1\), hence \(z\le0\).

This conclusion uses the shrinking relative width of the marked band. A fixed
non-dyadic slope such as \(729/1024\) can supply useful smaller ordinary
partners, but it cannot map an unbounded sequence of marked sources to marked
partners. It may still be followed by a parameter-dependent marked return.

## 2. A long initial odd run blocks the fixed clocks

Suppose a fixed rule applies to an infinite subsequence of the family in the
theorem. If \(\alpha<0\), positivity of \(x_j\) eventually fails. If
\(\alpha=0\), \(T^a(x_j)\) is constant while \(T^b(n_j)\to\infty\), so
the merger cannot hold. Thus \(\alpha>0\), and section 1 gives
\(\alpha=2^z\), \(z\le0\).

Discard finitely many terms so that every source has at least \(b\) initial
odd steps. Then its exact affine word formula is

\[
T^b(n_j)=\frac{3^b n_j+3^b-2^b}{2^b}.
\]

There are only \(2^a\) possible length-\(a\) partner parity words. Pass to
an infinite subsequence on which that word is fixed. Let \(p\le a\) be its
odd count and \(C\) its integer affine constant. Along this subsequence,

\[
T^a(x_j)=\frac{3^p(\alpha n_j+\beta)+C}{2^a}.
\]

The merger equality holds at infinitely many distinct \(n_j\), so the two
affine coefficients agree:

\[
\frac{3^p 2^z}{2^a}=\frac{3^b}{2^b}.
\]

Unique factorization, after clearing possibly negative powers of two, yields

\[
p=b,\qquad z=a-b.
\]

Since \(p\le a\), we have \(b\le a\), hence \(z\ge0\). Together with
\(z\le0\), this forces

\[
z=0,\qquad a=b=p.
\]

Both arms therefore consist exclusively of odd steps and have the same
length. On that word the map is the same injective affine function
\(y\mapsto (3^a y+3^a-2^a)/2^a\). Equality of the endpoints forces
\(x_j=n_j\), contradicting strict decrease.

## 3. An explicit marked witness family

The already compiled `NewBandFamily.lean` supplies, for every \(j\ge0\),

\[
k_j=64j+31,\quad s_j=2j+8,\quad d_j=66j+39,
\qquad n_j=2^{d_j}+2^{k_j}-1.
\]

These sources are marked and their initial consecutive odd-run length is
\(k_j\to\infty\), since
\(n_j+1=2^{k_j}(2^{s_j}+1)\). Thus they meet the hypotheses in section 2.

If a finite rule collection covered all sufficiently large marked integers,
one of its rules would cover infinitely many \(n_j\). Section 2 gives a
contradiction. Removing finitely many terminal exceptions has no effect.

The existing positive merger for this family has clocks \(k_j+6\) and
\(k_j+8\), which grow with \(j\). It is therefore entirely consistent with
this no-cover theorem and illustrates an essential way to escape it.

## 4. What the finite language search actually showed

`prefix_language_search.py` exhaustively checked the finite identities

\[
T^{14}(2^{14}q+A)
=T^{14-r}(2^{14-r}q+\lfloor A/2^r\rfloor)
\]

for odd \(A<2^{14}\), \(1\le r<14\), and odd positive binary prefixes
\(\lfloor A/2^r\rfloor\). It compared both the affine constant and odd count;
those two finite equalities certify the identity for every ordinary
\(q\ge0\). The stored 392 compressed residue conditions are a bounded
exploratory catalog, not a universal cover. In its JSON, the field `h` is the
compressed *residue modulus exponent*: the certified clocks remain 14 and
14−r after sibling residue conditions are combined.

One independently verified short rule is

\[
T^8(64x+35)=T^2(x),\qquad x\equiv3\pmod4.
\]

Iterating the source constructor from \(x=3\) gives the closed family

\[
n_j=\frac{32\,64^j-5}{9}.
\]

However, \(T^2(n_j)=2^{6j+3}\): every member has exactly two odd steps before
first reaching one. This is an elementary inverse family, not a new advance
toward arbitrary positive inputs. The search is retained as evidence of the
attempt, not promoted as a substantive Collatz completion.

## 5. Relation to the primary literature

Yolcu, Aaronson and Heule, *An Automated Approach to the Collatz Conjecture*,
Journal of Automated Reasoning 67 (2023), use mixed binary–ternary strings and
prove that termination of their full rewriting system is equivalent to
Collatz. Their administrative carries can be repeated an unbounded number of
times; they are not a finite collection of whole-source affine mergers with
fixed clocks. The theorem above therefore does not contradict or dispose of
their approach. It identifies a restriction that must be avoided when turning
local rewrites into lower marked-component certificates.

Primary full paper inspected:
https://emreyolcu.com/research/rewriting-collatz.pdf

No claim of historical novelty is made for the no-cover argument without a
broader literature comparison. Its precise assumptions and proof are supplied
here so that the current project does not inadvertently impose this impossible
finite architecture.
