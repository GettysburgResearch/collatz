# Effective classification of cycles in every fixed linear block schema

Research theorem, 2026-11-21 UTC.

**Result.** Every fixed one-parameter schema of repeated Collatz parity
blocks admits an effective, complete classification of its positive ordinary
cycle realizations: a computable finite set of parameter exceptions, followed
either by no cycles or by repetitions of one fixed, explicitly replayable
cycle. The complete cycle denominator is retained throughout.

This is an elementary written proof. Its concrete alphabet-four application
has a separate Lean module. The theorem is a response to PR186 task T08; it
does not assume that arbitrary cycles belong to finitely many such schemas.
No assertion of historical priority is made without a wider comparison.

## 1. Exact input and output

Use the shortcut map on integers,

\[
T(x)=x/2\quad(x\text{ even}),\qquad
T(x)=(3x+1)/2\quad(x\text{ odd}).
\]

Let \(V_1,\ldots,V_r\) be fixed nonempty binary words, written in forward
time order. Let \(a_i,b_i\) be fixed nonnegative integers. The parameter is
an ordinary integer \(k\ge0\), and the prescribed word is

\[
W(k)=V_1^{a_1k+b_1}\cdots V_r^{a_rk+b_r}.
\tag{1}
\]

An empty block can simply be removed. A parameter at which the entire word
is empty is recorded separately: a zero-clock identity is not evidence for a
cycle. More general integer coefficients whose exponents are nonnegative
for all sufficiently large \(k\) reduce to this convention by an explicitly
computed parameter shift and a finite preliminary list.

The output is:

1. A computable cutoff \(K\).
2. Every positive ordinary cycle realization for \(0\le k<K\), including
   its exact source, physical replay, and minimal cycle.
3. For \(k\ge K\), either an exclusion certificate or an identity certificate
   for one fixed cycle, with its original and rotated starting points stated.

There is no promise of practical running time. The cutoff and finite replay
can be very large, but all comparisons are exact rational arithmetic and
every specified search terminates.

## 2. Affine words and complete denominators

The formal branch maps are

\[
F_0(x)=x/2,\qquad F_1(x)=(3x+1)/2.
\]

For a word of length \(L_i>0\) with \(s_i\) ones,

\[
F_{V_i}(x)=\mu_i x+\nu_i,
\quad \mu_i=\frac{3^{s_i}}{2^{L_i}}>0,
\quad \nu_i=\frac{C_i}{2^{L_i}}\ge0.
\tag{2}
\]

Here \(C_i\) is obtained by exact affine composition. A block with no odd
steps has \(C_i=0\) and is fully allowed. Unique factorization gives
\(\mu_i\ne1\) for every nonempty block. Put

\[
c_i=\frac{\nu_i}{1-\mu_i},\qquad
h_i=\mu_i^{b_i},\qquad \lambda_i=\mu_i^{a_i}.
\]

The repeated block has the exact map

\[
F_{V_i}^{a_i k+b_i}(x)
=c_i+h_i\lambda_i^k(x-c_i).
\tag{3}
\]

The multiplier of the complete word is

\[
M(k)=H\Lambda^k,
\qquad H=\prod_i h_i,
\qquad\Lambda=\prod_i\lambda_i.
\tag{4}
\]

If the word is nonempty, \(M(k)\ne1\). Its unique formal periodic point is
\(N(k)/(1-M(k))\), where \(N(k)\) is its complete affine translation.
Equivalently, without normalizing the denominator,

\[
x(k)=\frac{C_{W(k)}}{2^{|W(k)|}-3^{\#1(W(k))}}.
\tag{5}
\]

Every divisibility check below concerns this whole quotient, not selected
factors of its denominator.

### Ordinary legality follows from final integrality

For any fixed binary word and any integer initial value, integrality of its
final formal affine value forces all prescribed parities to be correct.
Indeed, at a first incorrect parity the formal state has an odd numerator
over two. If a later formal state is \(u/2^j\), with \(u\) odd and \(j\ge1\),
the next numerator is either \(u\) or \(3u+2^j\), again odd, over
\(2^{j+1}\). Such a state can never become integral. This contradicts final
integrality.

Thus a positive integer value of (5) is an actual positive ordinary cycle
with the stated word. Intermediate positivity follows from the two branch
maps. Conversely an actual cycle satisfies (5).

For an odd-gap example, expand a gap \(g\ge1\) as the shortcut word
\(1\,0^{g-1}\). A positive odd periodic source then makes every expanded
gap exact: the next gap starts odd, including the wrap to the initial state.

## 3. Constant schemas and expanding schemas

If every \(a_i=0\), the word is constant. Compute (5) once, skip the empty
word, and test sign and integrality. Any positive integer result has a finite
physical replay by the preceding lemma. This completely handles the constant
case, including arbitrary fixed blocks between varying blocks later on.

Otherwise set

\[
L_* =\sum_i a_i L_i>0,
\qquad s_* =\sum_i a_i s_i.
\]

Then \(\Lambda=3^{s_*}/2^{L_*}\ne1\). There is no unhandled resonant case.

If \(\Lambda>1\), choose an exact integer \(K\) with
\(H\Lambda^K\ge1\). For every \(k\ge K\), the complete affine translation
is nonnegative and the periodic denominator \(1-M(k)\) is nonpositive.
A nonempty word therefore has no positive periodic point. The finitely many
earlier parameters are checked directly. This argument does not discard
negative integer cycles; they simply fall outside the positive conclusion.

It remains to handle \(0<\Lambda<1\).

## 4. A fixed rotation bounds a periodic point

Define prefix products \(P_0=1\),
\(P_j=\lambda_1\cdots\lambda_j\). Choose an index
\(j\in\{0,\ldots,r-1\}\) at which \(P_j\) is minimal, and rotate the
block list to begin after that index. Keep the exponents attached to their
blocks. This rotation is fixed once and for all, independently of \(k\).

**Rotation lemma.** Every suffix product of the rotated \(\lambda_i\)'s
is at most one.

To prove it, every rotated prefix product is at least \(\Lambda\). Before
wrapping, it is \(P_{j+t}/P_j\), which is at least one unless \(j+t=r\);
in that case it is \(\Lambda/P_j\ge\Lambda\), since \(P_j\le1\).
After wrapping it is \(\Lambda P_i/P_j\ge\Lambda\). Dividing the total
product \(\Lambda\) by a rotated prefix gives the asserted suffix bound.
The proof includes \(\lambda_i=1\), so constant blocks cause no problem.

Relabel this rotated schema as \(1,\ldots,r\), and write

\[
H_i=\prod_{j=i}^r h_j,\qquad
\Lambda_i=\prod_{j=i}^r\lambda_j,
\qquad H_{r+1}=\Lambda_{r+1}=1.
\]

Composing (3) gives the exact translation

\[
N(k)=\sum_{i=1}^r c_i
\left(H_{i+1}\Lambda_{i+1}^k-H_i\Lambda_i^k\right).
\tag{6}
\]

All \(\Lambda_i\) lie in \((0,1]\). Therefore

\[
|N(k)|\le B,
\qquad
B=\sum_{i=1}^r |c_i|(H_i+H_{i+1}),
\tag{7}
\]

where \(B\) is an explicit nonnegative rational independent of \(k\).
Choose \(K_0\) with \(H_1\Lambda^{K_0}\le1/2\). For every \(k\ge K_0\),

\[
|x(k)|=\left|\frac{N(k)}{1-H_1\Lambda^k}\right|\le2B.
\tag{8}
\]

Consequently every positive integer periodic point at this boundary belongs
to the explicitly finite set
\(\{1,\ldots,\lfloor2B\rfloor\}\). If \(B=0\), that set is empty.

Rotation loses no ordinary cycles. An actual cycle can be started at any
block boundary. Conversely an integer periodic point of the rotated word
gives the original cycle by advancing to the original boundary. Neither
direction relies on a merely 2-adic realization.

## 5. Exact power-sum separation gives an effective cutoff

For each possible integer \(m\) in (8), define

\[
E_m(k)=N(k)-m+mH_1\Lambda^k.
\tag{9}
\]

The periodic point equals \(m\) exactly when \(E_m(k)=0\). Equation (6)
makes (9) a finite sum

\[
E_m(k)=\sum_{\rho\in\mathcal R_m} A_\rho\rho^k
\tag{10}
\]

with distinct positive rational bases and nonzero rational coefficients,
after equal bases are grouped and zero coefficients removed. All data are
computed exactly; roots of an unknown quotient recurrence are never assumed
to belong to a prescribed multiplicative group.

If the coefficient dictionary is empty, (9) is an identity. Otherwise let
\(R\) be the largest remaining base and \(A=A_R\ne0\). If it is the only
base, there are no zeros. In the remaining case put

\[
S=\sum_{\rho<R}|A_\rho|>0,
\qquad q=\max_{\rho<R}\rho/R\in(0,1).
\]

Choose a computable \(K_m\) satisfying

\[
2S q^{K_m}\le|A|.
\tag{11}
\]

For \(k\ge K_m\), the other terms have absolute sum at most
\(S q^k R^k\le|A|R^k/2\). They cannot cancel the dominant term.
Thus \(E_m(k)\ne0\) for every such \(k\).

Take \(K\) to be the maximum of \(K_0\) and all these finitely many
\(K_m\). All parameter values \(k<K\) are checked directly with the full
quotient (5). For \(k\ge K\), only identity cases remain. This is an
effective classification, not an ineffective finiteness theorem followed by
an unjustified finite census.

## 6. Identity cases are fixed ordinary cycles

For one fixed rotated schema there is at most one identity value \(m\).
Subtracting identities for \(m\ne m'\) would give

\[
(m-m')(1-H_1\Lambda^k)\equiv0,
\]

which is impossible because \(\Lambda\ne1\).

If a positive integer \(m\) is an identity, every nonempty word in the
schema has final affine value \(m\) at initial input \(m\). The integrality
lemma proves actual legality for every parameter. One chosen nonempty word
therefore gives a finite explicit cycle replay. Its minimal cycle is obtained
by stopping at the first return to \(m\).

There is also an exact blockwise certificate of why the entire schema
stays on that fixed cycle. For a block of length \(L\), multiplier numerator
\(a=3^s\), and translation numerator \(C\), set

\[
D=2^L-a\quad\text{(an odd, possibly negative integer)},
\qquad \Delta=Dx-C.
\]

For an integer boundary state \(x\), formal integrality after \(e\)
repetitions is equivalent to

\[
2^{Le}\mid\Delta.
\tag{12}
\]

Indeed, multiply
\(F^e(x)-C/D=(a/2^L)^e(x-C/D)\) by \(D2^{Le}\); both \(D\) and
\(a\) are odd. Thus if \(\Delta\ne0\), the number of legal repetitions
is at most \(\lfloor v_2(\Delta)/L\rfloor\). If \(\Delta=0\), one block
returns \(x\) to itself and its repeated action is independent of \(e\).

Starting at the identity value \(m\), traverse the fixed block list.
Constant blocks have a fixed finite replay. At the first varying block, the
incoming state is independent of \(k\). Its exponent grows without bound,
so (12) forces \(\Delta=0\). Its output is the same state. Induct through
the list: every varying block fixes its boundary state, and the constant
blocks stitch these states into one fixed ordinary cycle. This also shows
that the original, unrotated boundary state is independent of \(k\).

The identity cycle must be explicitly identified. In the shortcut map it is
the trivial cycle exactly when its state belongs to \(\{1,2\}\). The theorem
does not assume that every algebraically possible identity cycle is trivial.
If a supplied finite schema contained a different positive cycle, its exact
finite replay would be a counterexample, not an exception to suppress.

### A sharper alternative: legality caps instead of power sums

The same lemma (12) also gives a second effective classification algorithm
after the uniform bound (8). For each of its finitely many candidate integers
\(m\), start at \(x=m\) and traverse the block list. Replay constant blocks
literally. A failed constant-block parity excludes the candidate. For a
varying block, compute \(\Delta=Dx-C\).

If \(\Delta=0\), the block fixes its incoming state, so continue with that
same state. At the first \(\Delta\ne0\), write
\(e_{\max}=\lfloor v_2(\Delta)/L\rfloor\). Every legal parameter satisfies

\[
a_i k+b_i\le e_{\max}.
\]

This is an explicit finite upper bound on \(k\), since \(a_i>0\). If no
such block occurs, all outputs are independent of \(k\); checking whether
the final state is \(m\) either excludes the candidate or gives its entire
fixed-cycle family. There is no unbounded search at this stage.

Thus recurrence-quotient finiteness is not needed even to obtain the cutoff.
The separately implemented and independently checked generic compiler uses
the power-sum certificate route in section 5. This sharper legality-cap route
is a written alternative and supplies the especially short worked proof
below; it is not silently substituted for the implemented algorithm.

## 7. Exact alphabet-four application

Use odd-gap words and let

\[
P=(1,1,4,1,1,1,2),\qquad Q=(2).
\]

The signed cycle at \(-41\) from PR176 gives, also by direct composition,

\[
F_P(x)=-41+\frac{2187}{2048}(x+41),
\qquad F_Q(x)=1+\frac34(x-1).
\]

For \(W(k)=P^kQ^k\), \(k\ge1\), the complete periodic point is

\[
x(k)=1+
\frac{42(6561^k-6144^k)}{8192^k-6561^k}.
\tag{13}
\]

This includes the whole denominator
\(2^{13k}-3^{8k}=8192^k-6561^k\). It is positive for every \(k>0\).

**A proof with no finite parameter census.** Set
\(\lambda=6561/8192\), \(\eta=6144/8192\). For every \(k\ge1\),

\[
1<x(k)
<1+42\frac{\lambda^k}{1-\lambda^k}
\le1+42\frac{\lambda}{1-\lambda}
=\frac{277193}{1631}<170.
\]

On the other hand, integrality of the repeated \(P\)-block requires

\[
2048^k(y+41)=2187^k(x+41).
\]

Since 2048 and 2187 are coprime, this forces \(2048\mid x+41\). For a
nonnegative integer source, \(x+41>0\), hence \(x\ge2007\). This directly
contradicts the uniform real bound. `cycle_equation_small`,
`pin_source_large`, and `no_repeated_gap_cycle_uniform` formalize this
argument in Lean, including the exact intermediate gap equations.

**An independent tail-and-finite-prefix proof.** For every \(k\ge17\),

\[
43\,6561^k<8192^k,
\]

because it holds by exact integer comparison at 17 and is preserved when
the two sides are multiplied by 6561 and 8192. Consequently

\[
0<42(6561^k-6144^k)<8192^k-6561^k,
\qquad 1<x(k)<2.
\tag{14}
\]

For \(1\le k\le16\), direct exact reduction gives a nonzero remainder for
the numerator modulo the complete denominator. `FixedBlockDenominator.lean`
proves both this finite part and the universal tail, and then derives a
contradiction from the two repeated-block affine cycle equations. The
census-free theorem above does not depend on these finite checks. Thus:

**There is no positive ordinary cycle with word \(P^kQ^k\), for any
\(k\ge1\), nor with any cyclic rotation of such a word.**

This is an all-parameter exclusion, not a tested finite range.

### The schema can have every prefix coefficient contracting

At the rotation \(Q^kP^k\), for \(k\ge4\), every nonempty gap-prefix has
coefficient strictly below one. All gaps still belong to \(\{1,2,3,4\}\).
The largest multiplier of a prefix of \(P\) is \(9/4\), while its full
multiplier is \(r=2187/2048>1\). After the initial \(k\) gap-twos, any
prefix inside the \(P\)-run has multiplier at most

\[
\frac94\left(\frac34\right)^k r^{k-1}
=\frac{512}{243}\left(\frac{6561}{8192}\right)^k<1.
\]

The strict inequality holds exactly at \(k=4\) and then improves. Prefixes
within the initial \(Q\)-run have multiplier \((3/4)^i<1\).
This shows that the family is not excluded merely by discovering a
noncontracting prefix at that chosen boundary.

These are candidate **cycle words**, not the complete source certificates
ending at one used by PR177. In particular, this calculation neither revives
PR176's already resolved large-terminal-gap source family nor claims to
solve PR177's remaining low-interval source/target comparison.

## 8. Relation to PR186 and remaining universal coverage

PR186's arithmetic section E proposes recurrence-quotient machinery for
exactly (1), with full denominators. The theorem here uses extra structure of
positive affine Collatz words: a fixed cyclic rotation bounds one periodic
point, and the resulting finite positive-base sums have elementary effective
separation. No Subspace theorem, S-unit finiteness theorem,
Corvaja–Zannier theorem, quotient-root-group assertion, or GRH assumption is
needed for this proof.

The simple-denominator observation in PR186 is independently sound: if a
nonzero simple exponential recurrence is a polynomial times a recurrence,
uniqueness of its exponential-polynomial representation forces the polynomial
to be constant. That conditional observation is not used above, so the
restricted full-proof access reported for its external theorem is not a
dependency of this packet.

The remaining global step is explicit. There is no proved finite collection
of schemas (1) covering all possible positive cycles, and no reduction of an
aperiodic ordinary orbit to such a schema. The number of blocks and their
contents are fixed in each application; permitting a new schema for each
candidate is not a uniform exclusion of all candidates. The present theorem
settles every supplied schema effectively, not the full Collatz conjecture.

## 9. Frozen repository inputs and evidence

- PR186, `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493`,
  `literature/deep-machinery-20261122/03_arithmetic_and_logic.md`, section E;
  `06_agent_tasks.md`, T08–T09. These are proposed interfaces, not imported
  Collatz closure claims.
- PR176, `41dc0ff039c13eeaf7f130c56a290212c00bcdef`,
  `research/lean-global-resolvent-20261121/overview/literature/CYCLE_DEFICIT_FAMILIES.md`,
  sections 2 and 7. The signed block is reused; the source-family resolution
  and its remaining scope are retained.
- PR177's exported latest source, as pinned in the accompanying source ledger,
  `research/lean-exact-witness-global-20261121/BOUNDED_GAP_ATTACK.md`.
  Its complete-source alphabet-four reduction does not establish periodic-word
  or all-input coverage for the schema here.
- PR182, `2d478a6588f33a72fc3a5bdc085a928b5cf78737`,
  `COEFFICIENT_PEAKS.md` and the packet README were inspected for the global
  map. Its finite coefficient escape alternative is not an assumption of
  this cycle classification.

The general theorem is a complete written argument, independently checked
at its cyclic-bound and power-sum steps by the sibling rewriting researcher.
The exact generic certificate generator/checker is supplied separately by the
root researcher. The worked denominator theorem has a separate Lean receipt;
the evidence levels must not be conflated.
