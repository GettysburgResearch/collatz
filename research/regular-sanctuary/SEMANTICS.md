# Exact Semantics and Decision Procedures

## 1. Canonical finite words

Bits are processed **least-significant digit first**.  For a finite word

$$
w=w_0w_1\cdots w_{r-1},
$$

define

$$
[w]=\sum_{i=0}^{r-1}w_i2^i.
$$

The canonical positive language is

$$
\mathcal C=\{w\in\{0,1\}^*:w\text{ is nonempty and ends in }1\}.
$$

Thus `1`, `01`, and `101` encode 1, 2, and 5.  Words such as the empty word,
`0`, and `10` are not canonical positive encodings.  In particular, a terminal
zero is forbidden MSB padding; an initial zero is a genuine low bit.

For a complete raw DFA `D`, the candidate language always means

$$
L_D=L(D)\cap\mathcal C.
$$

This intersection is semantic and mandatory.  It prevents padding aliases from
creating false certificates.

## 2. The exact shortcut transducer

The shortcut map is

$$
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
$$

The following deterministic subsequential transducer realizes it.  An entry is
`(next state, emitted LSD-first bits)`; epsilon means no bit is emitted.

| state | input `0` | input `1` | terminal output |
|---|---|---|---|
| `S` | `(E, epsilon)` | `(C2, epsilon)` | undefined |
| `E` | `(E, 0)` | `(E, 1)` | epsilon |
| `C0` | `(C0, 0)` | `(C1, 1)` | epsilon |
| `C1` | `(C0, 1)` | `(C2, 0)` | `1` |
| `C2` | `(C1, 0)` | `(C2, 1)` | `01` |

The even branch deletes the initial zero and copies the remaining bits.

For the odd branch, write `n=1+2m`, so `T(n)=3m+2`.  After the initial one is
consumed, initialize carry `c_0=2`.  If the next bit of `m` is `b`, compute

$$
z=3b+c,
\qquad
y=z\bmod2,
\qquad
c'=\left\lfloor z/2\right\rfloor.
$$

The carry remains in `{0,1,2}`.  At end of input its canonical LSD-first
encoding is emitted: epsilon, `1`, or `01`.

### Correctness invariant

Let `Y_i` be the value of the first `i` emitted output bits, and let `c_i` be
the current carry after processing the first `i` bits of `m`.  Then

$$
3m+2
=
Y_i+2^i\left(3\left\lfloor m/2^i\right\rfloor+c_i\right).
$$

The identity holds initially with `Y_0=0,c_0=2`.  Splitting the remaining
integer into its next bit and suffix proves preservation under the transition
formula.  At end of input the suffix vanishes, and flushing `c_i` gives exactly
`3m+2`.  This proves the odd branch; the even branch is the binary shift.

Changing the odd initial carry from 2 to 1 gives `(3n-1)/2`.  The same checker
then verifies the positive-control cycle

$$
5\longmapsto7\longmapsto10\longmapsto5.
$$

## 3. Exact closure as finite reachability

For a fixed DFA `D`, explore product states

$$
(q_{in},p,q_{out},c_{in},c_{out}),
$$

where:

- `q_in` is the state of `D` after the consumed input prefix;
- `p` is the transducer state;
- `q_out` is the state of `D` after the emitted output prefix;
- `c_in,c_out` are three-state monitors recording empty, last-zero, or
  last-one status.

On an input bit, advance `q_in`, the transducer, the emitted output through
`q_out`, and both monitors.  This graph is finite.  At any canonical input
endpoint, flush the transducer's terminal output and record the endpoint pair

$$
q_{in}\;R_D\;q_{out}.
$$

A canonical endpoint without a terminal output, or one whose flushed output is
noncanonical, is a verifier error.  Such paths are never silently omitted.

Every canonical finite word determines one reachable endpoint pair, and every
recorded pair has a reconstructed canonical word.  Therefore

$$
T(L_D)\subseteq L_D
$$

holds exactly when there is no edge `p R_D q` with `p` accepting and `q`
rejecting.  A violating edge yields a concrete pair `w,T(w)`; no numerical
sampling cutoff is involved.

## 4. Maximal safe acceptance kernel

Fix only the transition skeleton of `D`.  Let

$$
B=\{\delta(q_0,\texttt{1}),\delta(q_0,\texttt{01})\}
$$

be the states reached by the two forbidden shortcut-cycle encodings.  Form the
reverse-reachable set

$$
U=\operatorname{Pre}_{R_D}^{*}(B).
$$

Then

$$
F_{max}=Q\setminus U
$$

is the unique largest accepting-state set that both rejects `1`,`01` and is
forward closed under `R_D`.

Indeed, every state in `B` must be rejected.  If `p R_D q` and `q` must be
rejected, closure forces `p` to be rejected as well, proving every valid
accepting set is contained in `F_max`.  Conversely, the complement of a
reverse-closed set is forward closed, so `F_max` itself is safe.  The skeleton
supports a sanctuary exactly when a canonical word reaches `F_max`.

This removes the exponential search over acceptance masks.  The test suite
checks the result against all masks for every labeled two-state skeleton.

## 5. Short-witness state bound

Let `D` have `q` states and suppose `L_D` is nonempty.  Choose an accepted
canonical word `v1`, and let `p` be the state reached after `v`.  A shortest
word reaching `p` has length at most `q-1`.  Replacing `v` with that word and
appending `1` reaches the same accepting endpoint and remains canonical.
Hence `L_D` contains a word of length at most `q`.

Conditional on the published verification that every positive integer below
`2^71` converges, a sanctuary must therefore have at least 72 raw DFA states.
This published-range consequence is used only to prune search.  It is not used
by the certificate verifier.

## 6. Fixed-block normalization

Suppose a regular language `L` avoids `{1,2}` and satisfies

$$
T^B(L)\subseteq L
$$

for a fixed positive `B`.  Define

$$
K=\bigcup_{i=0}^{B-1}T^i(L).
$$

Each image is regular because the shortcut map is subsequential, and
`T(K) subset K`.  If a member of `{1,2}` occurred in an intermediate image,
further iteration around the trivial cycle would put `1` or `2` into
`T^B(L) subset L`, a contradiction.  Thus `K` is a one-step regular sanctuary.

Fixed blocks may compress a description or suggest phase automata, but they do
not enlarge the existential class of regular sanctuaries.

## 7. Odd-core equivalence

For odd `n`, define

$$
U(n)=\frac{3n+1}{2^{\nu_2(3n+1)}}.
$$

Regular shortcut sanctuaries exist exactly when regular nonempty odd languages
`O` with `U(O) subset O` and `1 notin O` exist.

In one direction, intersect a shortcut sanctuary `L` with the regular language
of odd canonical words.  The intersection is nonempty because repeated
shortcut halving takes every positive integer to its odd part.  For odd
`n in L`, the value `U(n)` occurs after `nu_2(3n+1)` shortcut steps, so it
remains in the odd core.

Conversely, dyadically saturate an odd language:

$$
\operatorname{Sat}_2(O)=\{2^k n:k\geq0,\ n\in O\}.
$$

Its LSD-first language is the regular language `0* O`.  Even members map one
level down the saturation, while for odd `n`

$$
T(n)=2^{\nu_2(3n+1)-1}U(n).
$$

Thus the saturation is shortcut invariant and excludes `{1,2}` exactly when
`O` excludes `1`.  This is an existence equivalence, not a claim that every
unsaturated `L` equals the saturation of its odd core.

The experiment now implements a seven-state transducer for the totalized map
`U(odd_part(n))` and an exact DFA lift for `0* O`.  Odd-core search remains
conjecture-generation machinery: every proposed lift is passed back to the
unchanged standard shortcut verifier, which remains the certificate boundary.

## 8. Dyadic-cylinder basin density

Every residue class modulo every fixed power of two contains infinitely many
integers reaching a power of two.

Fix `A>0`, `0<=r<2^A`, and write `n=r+2^Aq`.  The first `A` parity decisions
are fixed by `r`.  If `a` of them are odd, then

$$
T^A(n)=3^a q+s,
\qquad s=T^A(r),
$$

where `T(0)=0` is used only for this formula.  If `a=0`, then `r=s=0` and a
power-of-two `q` works.  If `a>0`, inspect the last odd step: immediately after
it the constant trajectory is `2 modulo 3`, and all remaining halvings keep it
nonzero modulo three.  Hence `s` is a unit modulo `3^a`.

The residue 2 generates the units modulo `3^a`; equivalently its order is
`2*3^(a-1)`.  Choose arbitrarily large `k` with
`2^k=s modulo 3^a` and put

$$
q=\frac{2^k-s}{3^a}.
$$

For large `k`, this is nonnegative and `T^A(n)=2^k`.  The case `A=0` is the
set of all positives and already contains every power of two.

Therefore no sanctuary contains all sufficiently large integers in even one
dyadic cylinder.  This excludes eventual fixed-modulus predicates and DFA
states accepting every high-bit continuation.  It does not exclude arbitrary
regular languages, which may retain branching dependence on unboundedly high
bits.

## 9. Finite-lasso obstruction

Consider, up to a finite exceptional set, a finite union of exact rays

$$
R_i=\{A_i+B_i2^{h_i k}:k\geq K_i\},
$$

with positive integer values, `h_i>=1`, `B_i>0`, and rational coefficients of
odd denominator.  If the union is shortcut invariant, every orbit in it is
eventually periodic.

Parity on each ray is constant for large `k`, say `epsilon_i`.  The image tail
has the form

$$
C_i+D_i2^{h_i k},
\qquad D_i=\frac{3^{\epsilon_i}}2B_i.
$$

If this image ray meets a target ray infinitely often, their 2-adic limits
force equality of their constant terms.  Removing powers of two from the
remaining equality gives

$$
\operatorname{unit}_2(B_j)
=3^{\epsilon_i}\operatorname{unit}_2(B_i).
$$

This permits an image ray to split among several target rays.  Along a
nonperiodic orbit, all values are distinct.  Finite-intersection source-target
pairs can therefore occur only finitely often; every sufficiently late
transition obeys the displayed unit relation.  A finite set of positive
rational unit parts cannot undergo infinitely many multiplications by three,
so the orbit would eventually contain only even steps.  A positive integer
admits only finitely many consecutive halvings, a contradiction.

The classical decomposition of every slender regular language into finitely
many `u v* w` components turns each component into such a ray:

$$
[uv^kw]=[u]-\frac{2^{|u|}[v]}{2^{|v|}-1}
+2^{k|v|}\left(2^{|u|}[w]
+\frac{2^{|u|}[v]}{2^{|v|}-1}\right).
$$

Consequently a nonempty safe slender regular sanctuary would already contain
a nontrivial positive cycle.  This corollary does not apply to a general
nonslender DFA, and a single pumped lasso inside a branching language need not
be invariant by itself.

## 10. Conditional exact-floor normal form

Assume every positive integer below `2^71` reaches the trivial cycle, and let a
72-state complete raw DFA recognize a nonempty sanctuary.  Its least accepted
integer has a canonical word

$$
w=b_0b_1\cdots b_{70}1
$$

of length exactly 72.  It is odd, since an even least member would map to a
smaller member.  If `alpha=nu_2(3m+1)>=2`, then the odd iterate

$$
U(m)=\frac{3m+1}{2^{\alpha}}<m,
$$

again contradicting minimality.  Hence `alpha=1`, `m=3 modulo 4`, and the LSD
prefix is `b_0b_1=11`.

Let `q_i` be the state after the first `i` of the initial 71 bits, for
`0<=i<=71`.  A repeated `q_i=q_j` would allow deletion of the intervening
block while retaining the final `1`, producing a shorter canonical accepted
word.  Thus these 72 prefix states are distinct and exhaust the machine.  The
final `1` is an accepting gate `a=delta(q_71,1)` back to one of them.

In fact `q_i` has graph distance exactly `i` from the start.  A shorter word
reaching `q_i`, followed by `b_i...b_70 1`, would be a canonical accepted word
of length below 72.  Therefore every transition from `q_i` targets some `q_j`
with `j<=i+1`, while the spine label `b_i` advances from `q_i` to `q_(i+1)`.

If any accepting state `f` has a canonical preimage `v1`, the state after `v`
is some `q_i`.  Replacing `v` by the spine prefix of length `i` gives an
accepted canonical word of length `i+1<=72`; hence `i=71` and `f=a`.
Deleting raw accepting states without canonical preimages therefore preserves
the semantic language and leaves the singleton acceptor `{a}`.  In particular,
`delta(q_i,1)!=a` for `i<71`.

Exhaustion also writes `delta(q_0,0)=q_j`.  If `j>=1`, then

$$
0b_jb_{j+1}\cdots b_{70}1
$$

follows the spine suffix into the accepting gate.  Shortcut closure deletes
its first zero and accepts a canonical word of length `72-j<=71`, a
contradiction.  Therefore `delta(q_0,0)=q_0`, and the whole semantic language
has the saturated form `0* O` from the odd-core lemma.

The `11` prefix gives `delta(q_0,1)=q_1` and `delta(q_1,1)=q_2`.  The other
edge from `q_1` cannot also reach `q_2`: if it did, replacing the second bit of
the least word by zero would accept the canonical 72-bit integer `m-2`.
Therefore `delta(q_1,0)!=q_2`.

This normal form is necessary only at the exact conditional floor.  It is not
sufficient for sanctuary closure, the singleton acceptor is a semantics-
preserving normalization rather than a forced raw mask, and the initial `11`
is asserted only for the least accepted integer.

The experiment encodes precisely these necessary transition constraints in a
CEGIS loop.  Z3 proposes a complete transition table; the standard exact
verifier remains the mandatory arbiter.  After a closure failure, the program
recomputes the complete terminal endpoint relation and records one shortest
concrete arithmetic implication `w in L => T(w) in L` for every violating
endpoint pair.  These implications are necessary for every candidate and are
safe to replay from a strictly validated checkpoint.  A timeout or model limit
is explicitly incomplete.  The solver deadline is soft because exact checking
and witness batching finish atomically.  Even a solver-level UNSAT report is
not a proof artifact because this prototype does not emit independently
checkable solver proofs.

## 11. Finite-horizon safety automata

Let

$$
S_0=\mathcal C\setminus\{\texttt{1},\texttt{01}\},
\qquad
S_{d+1}=S_0\cap T^{-1}(S_d).
$$

Every `S_d` is regular and consists exactly of starts avoiding the trivial
cycle during the first `d+1` inspected orbit states.  Any sanctuary is a subset
of every `S_d`.

These automata do not establish infinite survival.  Their minimized strongly
connected structure may suggest new features or transition designs, but
L-9110 shows that a literal quotient cannot repair an empty maximal kernel on
the finer skeleton.  Every redesigned conjecture must return to the exact
closure checker.

## 12. Quotient monotonicity

Let `h'` and `h` be reachable-state maps of finite deterministic skeletons,
with `h'` refining `h`.  Equivalently, a surjective transition homomorphism
`pi` satisfies `h=pi composed with h'`.  Every accepting set `F` on the coarse
skeleton pulls back to `pi^(-1)(F)` on the fine skeleton and expresses exactly
the same canonical language.

It follows that every sanctuary expressible on `h` is expressible on `h'`.
Writing `K_h` for the largest semantic sanctuary kernel available on a
skeleton,

$$
K_h\subseteq K_{h'}.
$$

Thus, once L-9103 computes an empty maximal kernel on a fine safety-
approximant skeleton, no literal deterministic quotient of that skeleton can
make it nonempty.  This applies to SCC merging only when the partition is
transition stable and defines a genuine quotient.  Refining states, adding
features, taking products, or redesigning transitions creates a different
search space and remains open.

## 13. Conditional odd-suffix normal form and clause transport

Every odd canonical word is uniquely `1x`, where

$$
x\in\mathcal C_{\mathrm{suf}}
=\{\epsilon\}\cup\{0,1\}^*1.
$$

Let a complete `p`-state DFA `A` read only `x`, and define `O_A` to contain
the odd values whose suffixes it accepts. Adjoin a new state `s` with

$$
\delta(s,0)=s,\qquad \delta(s,1)=r_0,
$$

where `r_0` is the start of `A`; retain every transition of `A` and do not
make `s` accepting. Under canonical semantics this raw `p+1` state lift
recognizes exactly `Sat_2(O_A)`. It deliberately remains unminimized because
the state count is part of the conditional floor argument.

If `O_A` is nonempty, excludes `1`, and is `U`-invariant, L-9106 makes the
lift a shortcut sanctuary. Conditional on verification below `2^71`, L-9104
therefore gives `p+1>=72`, or `p>=71`. At equality, translating L-9109 gives
71 exhaustive exact-distance suffix states, upper-Hessenberg transitions, a
forced first suffix edge `r_0 --1--> r_1`, and a singleton semantic gate
`r_h` with `2<=h<=70`. These are necessary conditions only. The structured
lift excludes raw gate 0 and does not cover generic work transitions returning
to `s`.

Exact shortcut implications can be transported into this representation.
For a canonical word `w`, let `odd(w)` delete **all** initial LSD zeros and let

$$
\sigma(w)=\operatorname{odd}(w)[1:]
$$

delete the forced odd marker. Membership in any saturated language `0* O`
depends only on `sigma(w)`. Hence every necessary shortcut clause

$$
w\in L\Longrightarrow T(w)\in L
$$

induces the necessary suffix clause

$$
\sigma(w)\in X\Longrightarrow\sigma(T(w))\in X.
$$

For even `w` this is a saturation identity. For odd `w`, the odd part of
`T(w)` is exactly `U(w)`. It is essential to remove every low zero from the
output: deleting only the one division already built into the shortcut map is
wrong whenever `nu_2(3w+1)>1`. The importer first rechecks the full exact
`w -> T(w)` image. It validates even-source clauses as odd-part identities and
rechecks odd-source pairs against the separate exact odd-core transducer.
Imported and locally learned ledgers remain separate, and neither source
model accounting nor solver conclusion is transported. Source status is kept
only as non-authoritative provenance.

L-9113 constructs reset-pattern spines showing an exponential blind spot
specific to concrete antecedent clauses; symbolic transition clauses and
arithmetic contradictions lie outside its bound.  L-9114 then applies the
exact-distance output-length budget and ripple-carry arithmetic to the
1-preferred minimum-length word, ruling out gate 2.  The remaining structured
suffix search range is `3,...,70`.

## 14. Depth-colored refinement features

Let `tau(n)` be the first shortcut time at which `n` reaches `{1,2}`, or
infinity if it never does. At horizon `d`, color a canonical word by its exact
`tau` when `tau<=d`, by `star_d` otherwise, and color every noncanonical word
`bot`. Let `H_d` be the minimal reachable Moore machine for this coloring.

The color truncation that fixes `bot,0,...,d` and identifies `d+1` and
`star_(d+1)` with `star_d` proves that the right congruence of `H_(d+1)`
refines that of `H_d`. The canonical map

$$
\pi_{d+1,d}([w]_{d+1})=[w]_d
$$

is a surjective transition homomorphism compatible with color truncation. It
is strict at every depth: `2^(d+2)` has first-hit time `d+1`, so its word is in
the shallow final-`1` tail but remains a distinguished deep boundary state.

For fixed `d`, the set of values with `tau<=d` is finite and has maximum
`2^(d+1)`. Outside the finite prefix closure of their encodings, residuals
depend only on the final bit. Thus `H_d` has a two-state cyclic tail and an
acyclic boundary. Any accepting set on the bare skeleton either accepts the
final-`1` tail state, making its semantic language cofinite, or rejects it,
making the language finite. The first alternative is unsafe because it
contains large powers of two; the second can be invariant only by containing
an eventual cycle. Conditional on verification below `2^71`, its maximal
kernel is empty through `d=69`.

The colored chain is therefore a feature generator, not a direct sanctuary
template. For a fixed genuinely recurrent skeleton `R`, the reachable products
`R product H_d` retain canonical projections obtained by restricting
`id_R product pi_(d+1,d)`, so L-9110 gives monotone maximal kernels. Popcount
parity is the smallest first control: it is recurrent, nonslender, noncofinite,
and not determined by any fixed low-bit cylinder. Every nonempty product
kernel must still pass the unchanged exact shortcut verifier.

## 15. Scope cautions

- Fixed-DFA and fixed-block verification is decidable; unrestricted existence
  over all automaton sizes is not claimed decidable.
- Finite words only are admitted.  An infinite LSD stream is a 2-adic object
  and need not encode any positive integer.
- A failed bounded search excludes only its declared skeleton/template class.
- Fixed dyadic cylinders and finite-lasso/slender templates are now excluded
  by L-9107 and L-9108 within their exact stated scopes; nonslender regular
  high-bit languages remain open.
- Empty fine-skeleton kernels exclude their literal quotients by L-9110, not
  refinements, augmentations, or independently designed automata.
- The 71-state suffix floor and the `d<=69` colored-kernel corollary are
  conditional on the external verified range; candidate verification is not.
- BFS witnesses are shortest by length and LSD-first lexicographic order, not
  necessarily numerically least.
- A regular sanctuary is stronger than a lone divergent orbit; Collatz falsity
  would not automatically imply that such a sanctuary exists.
