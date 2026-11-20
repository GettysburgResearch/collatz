# Complete recognition of balanced five returns and a broader positive renewal

**PROPOSED.** These are ordinary-integer identities, a complete recognizer
inside a specified return architecture, and an exact finite certificate for
an infinite positive-energy inequality. They do **not** prove universal
five closure or Collatz. The final missing estimate is stated in Section 7.

Use the shortcut map T, given by n/2 on even n and (3n+1)/2 on odd n,
and its accelerated odd map
\(U(n)=(3n+1)/2^{v_2(3n+1)}\). Write
\(I_a(q)=(2^a q-1)/3\) only when this gives a positive odd integer.
An exponent word is listed in forward order.

## 1. Exact dependencies and what changes

The following sources were read at their exact heads.

- PR166, `5996b9f525ca50978bc34f423192c36a87765bf3`,
  `research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md`,
  FL1--FL4, and `LADDER_RENEWAL.md`, R1--R6: the unbounded valuation-two
  ladder, its compiler, and the earlier `.84` coefficient
  \(81744/82925\). Those results remain credited to that source.
- PR163, `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`,
  `research/deep-reverse-closure-20261120/FIVE_SLICE_ENERGY.md`, FE1:
  finite five energy propagates to the full tripling defect. Its external
  rigidity and predecessor dependencies retain their stated status.
- PR146, `fd991063721e9c157d318e40bb20131762f7d750`,
  `research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`,
  “Transport both orbits into one residue class”: paired returns lift
  arbitrary comparisons to a fixed thin source progression. Source
  density alone cannot turn a covered-class estimate into an absolute
  finite energy bound.
- PR162, `2279da37ac612dbe049777354cdedb3c0aa03282`,
  `research/creative-closure-20261120/five_closure.md`, C5-001/002:
  the two-odd-input precursor of the valuation-two ladder.

The new material is a complete finite-input recognition criterion for all
balanced return words; four first-valuation-one return families; an expanded
compiler; and a joint, endpoint-conditioned congestion calculation. The
latter proves a coefficient below `903/1000` for a larger source domain.
It uses compatible ternary endpoint classes instead of summing
incompatible worst cases separately.

## 2. FR1: complete recognition of balanced return words

Let \(w=(a_1,\ldots,a_p)\), \(p\ge1\), all \(a_i\ge1\). Put

\[
A_0=0,\quad A_i=\sum_{h=1}^i a_h,\quad L=A_p,\qquad
B(w)=\sum_{j=0}^{p-1}3^{p-1-j}2^{A_j}.
\]

Its affine inverse is

\[
I_w(q)=\frac{2^Lq-B(w)}{3^p}.
\tag{FR1.1}
\]

Call a word v a **balanced five return** for w if it has the same number
p of odd inputs, the same clock L, and the identity

\[
5I_w(q)=I_v(5q)
\tag{FR1.2}
\]

holds as an affine identity. It then gives an ordinary positive target
path whenever the source path is ordinary positive.

**Theorem FR1.** The return exists if and only if the following finite
algorithm succeeds. It is unique within this architecture.

Start with \(M=5B(w)\), \(d_0=0\). For
\(j=0,\ldots,p-2\), form \(R=M-3^{p-1-j}\). Reject if
\(R\le0\) or R is odd. Otherwise set

\[
k=v_2(R),\qquad d_{j+1}=d_j+k,\qquad M=R/2^k.
\]

Finally require \(M=1\) and \(d_{p-1}<L\). The unique output word is

\[
v=(d_1-d_0,\ldots,d_{p-1}-d_{p-2},L-d_{p-1}).
\tag{FR1.3}
\]

For p=1, the loop is empty and M=1 fails, since B(w)=1. The algorithm
always stops after at most p-1 iterations.

**Proof.** Equality of affine constants in (FR1.2) is exactly
\(B(v)=5B(w)\). In a positive-exponent word with odd positions
\(0=d_0<\cdots<d_{p-1}\), removing the leading term \(3^{p-1}\)
from its correction leaves

\[
2^{d_1}\left(3^{p-2}+3^{p-3}2^{d_2-d_1}+\cdots
+2^{d_{p-1}-d_1}\right).
\]

The factor in parentheses is odd. Therefore the first new exponent is
forced to be the exact valuation in the algorithm. Induction gives both
necessity and uniqueness. Conversely every successful sequence reconstructs
the correction exactly, with all exponents positive and total clock L.

For ordinary legality, suppose \(x=I_w(q)\) is positive odd, with an actual
source path to positive odd q. The full numerator
\(2^L(5q)-B(v)=5\cdot3^p x\) is divisible by \(3^p\). Reducing modulo
three yields the last inverse division; divide the remaining congruence
by three and continue. Thus every inverse intermediate is integral. Since
every exponent is positive and every endpoint is positive odd, each
integral inverse intermediate is positive odd. Reversing these inverses
gives precisely the claimed accelerated valuations. This proves actual
ordinary paths, not only rational affine equality. In particular

\[
T^L(x)=q,\qquad T^L(5x)=5q.
\tag{FR1.4}
\]

The theorem classifies all balanced affine returns for the supplied word.
It does not classify every way that 5x might converge.

## 3. FR2: four first-valuation-one families

For r letters equal to one followed by a final letter b,

\[
w=(1^r,b),\quad p=r+1,\quad L=r+b,\quad B(w)=3^{r+1}-2^{r+1}.
\tag{FR2.1}
\]

Here `1^r` denotes a string of letters. FR1 gives the following identities
for every legal positive source path and every final exponent in range.

| r | Range used below | Target word | Source cylinder |
|---:|---:|---|---|
| 3 | b>=6 | (1,2,5,b-5) | x=271 mod512 |
| 5 | b>=6 | (1,2,1,5,1,b-5) | x=575 mod2048 |
| 8 | b>=8 | (1,2,1,2,1,3,3,2,b-7) | x=38399 mod65536 |
| 9 | b>=9 | (1,2,1,2,1,2,4,1,2,b-7) | x=156671 mod262144 |

The last row also has a valid identity at b=8. Section 6 explains why
that larger domain is omitted from this particular contracting kernel.

For instance, the first row has source correction 65, whereas its target
odd positions 0,1,3,8 have correction 27+18+24+256=325=5*65. Its last
target exponent is positive exactly when b>=6. Every row follows from
the same finite integer identity, with the final exponent left symbolic.

The source cylinder formula for a threshold \(b_0\) is

\[
x\equiv-B(w)(3^{r+1})^{-1}\pmod{2^{r+b_0}}.
\tag{FR2.2}
\]

This is the exact ordinary parity cylinder for the first r letters equal
to one and the next exponent at least b_0. It fixes all those branch
decisions, not just the full affine numerator. The usual parity-cylinder
induction proves the converse: inverse branches modulo powers of two fix
the preceding branch, and the odd coefficient three is invertible at every
step.

The new rows are pairwise disjoint because their first non-one letter
occurs at different positions. They are disjoint from the valuation-two
ladder, whose first letter is two. The first example is

\[
271\to407\to611\to917\to43,\qquad
1355\to2033\to1525\to143\to215.
\]

These are accelerated paths, and the second endpoint is 5*43.

There are closed first-hit families for every row. Choose

\[
b\equiv1+3^r\pmod{2\cdot3^r},\qquad b\ge b_0,
\tag{FR2.3}
\]

and take q=1 in (FR1.1). This follows from
\(2^{b-1}=-1\pmod{3^{r+1}}\). The source first-hit word is (1^r,b).
Its five multiple has the target word in the table followed by the letter
four. All these exponent parameters are unbounded. The first exponents
are respectively 28,244,6562,19684. The ordinary integer source is
\(x=(2^{r+b}-3^{r+1}+2^{r+1})/3^{r+1}\).

## 4. FR3: finite-input compilation and exact language scope

Given a complete first-hit exponent word for x, try its nonempty prefixes
in increasing odd length with FR1. When a prefix is accepted, output its
target word and consume that source prefix. Continue on the remaining
suffix. On consuming the whole input append the letter four for 5 to 1.
If no nonempty prefix is accepted at some stage, return `UNRESOLVED`.

Every successful iteration consumes at least one input letter. The
algorithm terminates on every finite certificate, including unresolved
cases. On success it gives an actual first-hit certificate for 5x, with

\[
\omega(5x)=\omega(x)+1,\qquad\tau(5x)=\tau(x)+4.
\tag{FR3.1}
\]

Target prefixes cannot pass through one before reaching 5q>=5, since the
accelerated orbit of one stays at one. Thus no hidden terminal cycles
occur. The input is explicitly checked to be first-hit as well.

The accepted return words form a concatenation-closed, left-unitary
language: if u and uv are accepted, v is accepted. The first assertion
follows by composing the two affine identities. For the second, choose
arbitrarily large ordinary endpoints that realize the entire source word
uv; such endpoints exist in one residue class modulo its power of three.
The ordinary target for u ends at an odd value at its exact clock.
Therefore the uniquely determined target word for uv has the target word
for u as a prefix, and its remaining suffix has exactly v's clock and odd
count. Removing the common prefix gives the required affine identity for
v on infinitely many endpoints, hence identically. FR1 gives uniqueness.

Consequently greedy decomposition succeeds exactly when the whole source
word is recognized by FR1, equivalently when any decomposition into
balanced return blocks exists. Thus no better ordering of these same
rules can turn a rejected complete word into an accepted word.

This compiler contains the entire PR166 language, all concatenations of
the four new families, and every other balanced return recognized by FR1.
There is no bound on input rank, letter size, or block count. Its
universality concerns the stated decision procedure, not successful
certification of every five multiple.

For example x=17 has first-hit word (2,3,4), while 5x=85 has first-hit
word (8). The compiler returns `UNRESOLVED`: this true five-closure case
cannot satisfy (FR3.1). A rank-changing or separate terminal rule is
indispensable to a complete compiler extending this architecture.

## 5. FR4: joint endpoint-conditioned positive renewal

Let f take values in a metric space and satisfy f(Tn)=f(n) for every
positive integer. Put d_5(x)=d(f(5x),f(x)), s=21/25, and

\[
E_s(X)=\sum_{\substack{1\le x\le X\\x\text{ odd},\;3\nmid x}}
x^{-s}d_5(x).
\]

Let H be the union of all PR166 ladder cylinders (2^r,b), r>=1,b>=4,
and the four cylinders of Section 3, restricted to ternary units. Let
R_s(X) be the same sum restricted to x outside H.

**Theorem FR4.** For every finite X,

\[
\boxed{E_s(X)\le R_s(X)+\frac{903}{1000}E_s(X/2).}
\tag{FR4.1}
\]

Consequently

\[
E_s(\infty)<\infty\iff R_s(\infty)<\infty,\qquad
E_s(\infty)\le\frac{1000}{97}R_s(\infty)
\quad\text{in the finite case}.
\tag{FR4.2}
\]

The relative natural density of H among odd ternary units is

\[
2\left(\frac1{48}+\frac1{512}+\frac1{2048}
+\frac1{65536}+\frac1{262144}\right)=\frac{18319}{393216}.
\tag{FR4.3}
\]

For the infinite ladder union, the tails lie in successively thinner
powers-of-two cylinders, as in PR166 FL3. Thus this does not interchange
an unjustified infinite union and natural density.

### 5.1 Ordinary endpoints, positive weights, and truncation

Each x in H has a unique indicated block and endpoint q, with
d_5(x)=d_5(q). The endpoint is an odd ternary unit. If q=1, its defect
is zero by the known path from five to one. Otherwise q>=5.

Write a block as a fixed prefix of clock A, with p odd inputs including
the last exponent b, and correction B>0. The inverse sources are

\[
x_b=\frac{2^{A+b}q-B}{3^p},\qquad b\ge b_0.
\tag{FR4.4}
\]

On the ladder, A=2r,p=r+1,B=4^p-3^p. On a new row,
A=r,p=r+1,B=3^p-2^p. For q>=5, substitution at the minimum b gives
x_b/q>2 on every family. For example the smallest of the coarse new-row
bounds is (2^11-665/5)/3^6=1915/729>2, from r=5,b_0=6. The ladder
bound is greater than six. If q=1 the displayed cylinders have x>=49.
Thus q<=x/2 throughout, and x<=X restricts endpoints to q<=X/2.

For a fixed endpoint, integral b lie in one progression modulo
2*3^(p-1). Retaining only its congruence modulo 3^d, d<=p, enlarges
the source set, so is a valid positive upper bound. Deleting sources
divisible by three can only lower the sum.

### 5.2 A finite certificate for the complete infinite inverse sum

These formulas specify the full finite certificate. The companion program
evaluates them using integers and rational numbers only.

Partition endpoints by q modulo729. In each of the 486 unit classes let
q_* be the smallest odd representative at least five. Every eligible
endpoint in the class satisfies q>=q_*.

For a fixed family (p,A,B,b_0), put d=min(p,6), P=2*3^(d-1), and let
b_*>=b_0 be the least solution of

\[
2^{A+b_*}q_*=B\pmod{3^d}.
\tag{FR4.5}
\]

It is unique modulo P, since two has exact order P modulo3^d. For k>=0,
positive comparison gives

\[
x_{b_*+kP}\ge2^{kP}x_{b_*},\qquad
\frac{x_{b_*}}q\ge
\kappa:=\frac{2^{A+b_*}-B/q_*}{3^p}>1.
\]

Hence the family's full inverse column is bounded by

\[
\sum_b(q/x_b)^s\le\frac{\kappa^{-s}}{1-2^{-Ps}}.
\tag{FR4.6}
\]

Apply this separately to ladder indices r=1,...,5 and the four new rows.
For the remaining ladder tail r>=6, integrality implies
2^(b-2)q=1 mod729. Let b_*>=4 be its least solution and put
c=(4/3)(2^(b_*-2)-1/q_*), t=(3/4)^s. The exact ladder formula gives
x_b/q>=c(4/3)^r. Its whole infinite tail is at most

\[
\frac{c^{-s}t^6}{(1-t)(1-2^{-486s})}.
\tag{FR4.7}
\]

There are nine finite-family terms and one infinite-tail term per endpoint
class. A sampled endpoint is not substituted for the class: q_* bounds
all its members, and the retained congruences hold for all of them.

For rational z>=1, define the exact rational upper bound

\[
U(z)=10^{-10}\min\{h\in\{1,\ldots,10^{10}\}:
h^{25}z^{21}\ge10^{250}\}.
\tag{FR4.8}
\]

Then z^(-21/25)<=U(z), by an integer inequality after denominators are
cleared. Substitute these bounds in (FR4.6)--(FR4.7), including
t<=U(4/3). All denominator factors stay positive. Exact addition and
comparison on all 486 classes gives

\[
\boxed{\sup_{\substack{q\ge5\\q\text{ odd},\;3\nmid q}}
\sum_{\substack{x\in H\\x\mapsto q}}(q/x)^s<903/1000.}
\tag{FR4.9}
\]

The largest certified class is q=547 mod729, with q_*=547, and the
decimal display of its bound is approximately0.902889066491. This decimal
is explanatory; all acceptance comparisons are rational. The certificate
is independently reconstructible from these formulas, the table, and
(FR4.8).

Multiply each column bound by q^(-s)d_5(q), sum nonnegatively, and retain
the cutoff of Section5.1 to obtain (FR4.1). At a finite cutoff,
E_s(X/2)<=E_s(X), so (97/1000)E_s(X)<=R_s(X). Monotone limits give
(FR4.2). No infinite quantity is subtracted from itself.

## 6. FR5: every valid return need not preserve column contraction

The row r=9 also permits b=8 algebraically. Including it along with the
other three new families makes a uniform inverse-column bound below one
false at s=21/25.

Choose any sufficiently large odd q with 2^7q=-1 mod3^11. For each
r in {3,5,8,9}, the source

\[
x_r=\frac{2^{r+8}q-(3^{r+1}-2^{r+1})}{3^{r+1}}
\]

is positive odd, is -1 modulo3, and has actual word (1^r,8) to q.
Their source cylinders are disjoint. Since B>0,

\[
\sum_r(q/x_r)^s>
\sum_r\left(\frac{3^{r+1}}{2^{r+8}}\right)^s
>\frac{66+130+363+510}{1000}=\frac{1069}{1000}.
\tag{FR5.1}
\]

Each lower bound is verified by raising to the 25th power and comparing
integers. This is an infinite ordinary family of overloaded inverse
columns, not a finite-start extrapolation.

FR5 rules out this particular uniform-column contraction for the enlarged
kernel. It does not refute an energy inequality using further properties
of the actual invariant label, other weights, or another choice of returns.

## 7. Attempted completion and first unsupported inference

FR4 reduces full `.84` five-energy finiteness to finiteness on a strictly
smaller untreated source set, with a better explicit comparison factor
than the earlier coarse ladder estimate. It does not bound that untreated
energy absolutely. The remaining statement is

\[
\boxed{R_{21/25}(\infty)<\infty
\text{ for the indicator of an arbitrary ordinary orbit component}.}
\tag{OPEN-FR}
\]

Combined with PR163 FE1 and its named source-qualified subcritical rigidity
and predecessor-moment inputs, such a bound would force component
constancy. Those imported inputs are not proved anew here.

The positive density of H does not estimate the unknown label on its
complement. The contraction in (FR4.1) does not force finite energy: the
remainder is present at every scale. PR146's inverse lift puts every
possible failure into even one covered progression at larger height.
The present calculation bounds covered mass using smaller endpoints;
neither statement supplies the missing absolute estimate.

Likewise FR1 is a total recognizer for balanced words, and FR3 is a total
procedure that can return `UNRESOLVED`. The example17 proves that even
the complete balanced architecture requires rank-changing or terminal
rules before it can supply a full five-closure compiler.

## 8. Verification boundary

The companion `five_return_compiler.py` uses explicit failures, so its
checks remain active under optimized Python. A separate exhaustive oracle
compares the greedy recognizer against all4095 positive exponent words of
total clock at most12 and all possible same-clock, same-odd-count target
words. It also checks literal ordinary paths for160 members of the four
new cylinders, symbolic corrections, large first-hit certificates from
every new family, the known ladder specialization, and the complete exact
congestion certificate.

The unbounded results rely on the proofs and fully specified finite
certificate above. Bounded trajectory checks are supporting evidence,
not universal convergence claims. The report states actual executions;
independent review remains required before integration.
