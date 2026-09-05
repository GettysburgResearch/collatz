# L-9915 -- Additive one-counter controllers have ultimately periodic output

Claim ID: `L-9915`
Title: A deterministic finite controller with one zero-tested additive counter cannot generate the aperiodic centered tail required by a positive survivor
Status: `PROPOSED / ISOLATED CROSS-DIRECTION OBSTRUCTION`
Authoring agent: `gpt56-synthesis-01-wave22-gap-cold-audit`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: elementary finite functional-graph theory; local `L-9908` only for the centered-Collatz consequence
Scope: deterministic finite control whose sole unbounded register is updated additively and is observed only through zero/nonzero and finitely many fixed residues
Related open atoms: issue #43 `ACL-N076`; issue #40 `ACL-N077`

## 1. Exact machine model

Let `Q` and `Sigma` be finite sets.  An additive one-counter output machine has,
for each sign flag

\[
 z\in\{0,+\},
\]

maps

\[
 F_z:Q\longrightarrow Q,
 \qquad
 \Delta_z:Q\longrightarrow\mathbf Z,
 \qquad
 E_z:Q\longrightarrow\Sigma.
\tag{1}
\]

Starting from `(q_0,c_0)\in Q\times\mathbf Z_{\ge0}`, its unique run is

\[
 z_n=\begin{cases}0,&c_n=0,\\+,&c_n>0,\end{cases}
\tag{2}
\]

\[
 q_{n+1}=F_{z_n}(q_n),
 \qquad
 c_{n+1}=c_n+\Delta_{z_n}(q_n),
 \qquad
 a_n=E_{z_n}(q_n).
\tag{3}
\]

Only infinite **legal** runs, for which every `c_n>=0`, are considered.
Because `Q` is finite, the increments in (1) are automatically bounded.
Allowing a finite auxiliary memory, a phase, or a finite carry alphabet does
not enlarge this model: include it in `Q`.

The model also includes machines that inspect finitely many fixed counter
residues.  Indeed, if the transition or output reads

\[
 c\pmod {m_1},\ldots,c\pmod {m_s},
\tag{4}
\]

put `M=lcm(m_1,...,m_s)` and replace `q` by `(q,c mod M)`.  The residue after
the additive update is determined by the old finite state and increment, so
the enlarged control is still finite and (1)--(3) apply.  Thus the theorem
below already permits every fixed collection of counter residues.

## 2. Periodic-output theorem

### Theorem 1 -- every infinite output is ultimately periodic

For every infinite legal run of (1)--(3), the output word

\[
 a_0a_1a_2\cdots
\]

is ultimately periodic.

More precisely, exactly one of the following arguments applies.

1. If `c_n=0` infinitely often, the complete machine state repeats at two
   zero visits, and the full state and output tails are periodic from the
   first repeated visit.
2. If `c_n=0` only finitely often, the positive-control orbit of `F_+` is
   eventually cyclic.  The output is periodic on that cycle.  The net
   counter increment around it is nonnegative; it may be positive, so the
   counter itself need not be bounded or periodic.

### Proof

First suppose the counter is zero at infinitely many indices.  There are
only finitely many possibilities for `q_n` at such indices, so some

\[
 i<j
\]

satisfy

\[
 (q_i,c_i)=(q_j,c_j)=(q_i,0).
\tag{5}
\]

The update is deterministic on the complete state.  Induction on `t` gives

\[
 (q_{i+t},c_{i+t})=(q_{j+t},c_{j+t})
 \quad(t\ge0),
\tag{6}
\]

and hence `a_(i+t)=a_(j+t)`.  The output is periodic from time `i`, with
period `j-i`.

Now suppose zero occurs only finitely often.  Choose `N` after the last zero.
For every `n>=N`, the flag is `+`, and therefore

\[
 q_{n+1}=F_+(q_n),
 \qquad
 a_n=E_+(q_n).
\tag{7}
\]

Every orbit of a self-map of a finite set is eventually cyclic.  Hence there
are `mu>=0` and `p>=1` such that

\[
 q_{N+\mu+t+p}=q_{N+\mu+t}
 \quad(t\ge0).
\tag{8}
\]

Applying `E_+` proves the same equality for the outputs.

For completeness, let

\[
 D=\sum_{h=0}^{p-1}\Delta_+
       (q_{N+\mu+h})
\tag{9}
\]

be the net counter displacement around the control cycle.  At corresponding
cycle phases,

\[
 c_{N+\mu+kp}=c_{N+\mu}+kD.
\tag{10}
\]

If `D<0`, the right side is eventually negative, contradicting legality of
the infinite run.  Thus `D>=0`.  When `D=0`, the complete state is eventually
periodic; when `D>0`, the counter grows linearly while the finite control and
output remain periodic.  This proves the theorem. **QED**

## 3. Centered forced-tail consequence

### Corollary 2 -- the additive one-counter centered architecture is empty

Suppose integers `B_n>=0` and bits `e_n\in{0,1}` satisfy the exact centered
tail recurrence

\[
 64B_{n+1}=81B_n+e_n-e_{n+1}
 \quad(n\ge0),
\tag{11}
\]

and suppose `B_0>=1`.  The bit word `(e_n)` cannot be the output of a machine
in Section 1 on an infinite legal run.

### Proof

Theorem 1 makes `(e_n)` ultimately periodic.  The lasso theorem in local
`L-9908` then forces the only nonnegative integral tail to have `B_n=0` and a
constant bit from the start of the lasso.  This contradicts `B_0>=1`; also,
`L-9908` independently gives strict growth from every positive `B_0`, so the
tail cannot later enter zero. **QED**

The periodic-output theorem itself is independent of `L-9908`.  That claim is
invoked only to translate ultimate periodicity into the centered-Collatz
exclusion.

## 4. Exact relation to the open atoms

This result closes one sharply specified subcase of each atom; it does not
claim either full atom.

- **Issue #43, `ACL-N076`.** A frozen quotient-refund selector is excluded if
  its purported causal invariant reduces to finite control plus one additive
  counter and reads that counter only through zero and fixed residues.  Even
  a counter with positive linear drift emits an ultimately periodic stage
  word.  General quotient-refund rules may inspect the exact unbounded
  quotient or its canonical top boundary and therefore lie outside the
  theorem.
- **Issue #40, `ACL-N077`.** A centered forced-tail controller is excluded if
  its finite carry/nucleus plus height register has the model (1)--(4).
  Retaining a numerical counter is not enough when the controller never reads
  genuinely unbounded content.  The full atom additionally demands a
  canonical most-significant boundary and finite-support closure; those are
  deliberately not represented by a zero-tested additive counter.

## 5. Escape boundary

The proof uses only that, away from zero, the finite control follows one
fixed self-map.  It does **not** apply when any of the following is present:

1. an update depending nonlinearly on the counter, such as multiplication,
   division with an exact remainder, or an unbounded counter-dependent jump;
2. inspection of the counter magnitude, most-significant digit, changing
   modulus, canonical top boundary, or any other genuinely unbounded content;
3. two or more independent unbounded registers, a pushdown stack, tape, or
   another unbounded data structure;
4. an unbounded control alphabet or output rule;
5. unresolved nondeterminism, oracle choices, or a selector that consults
   future cylinder data.

Some of these extensions may still fail for separate arithmetic reasons.
They are simply not ruled out by this finite-control argument.  In
particular, the theorem must not be paraphrased as saying that every
"finite nucleus plus one quotient" architecture is periodic: it applies only
when the quotient is an additively updated counter with the restricted
observations in Section 1.

## 6. Adversarial checks

- **Growing counter is not confused with growing information.** A positive
  cycle displacement `D>0` is allowed.  It makes `c_n` unbounded but leaves
  the emitted word periodic.
- **Zero resets are covered.** Infinitely many resets force repetition of an
  exact state `(q,0)`, not merely a modular alias.
- **Finite residues add no power.** They are absorbed into the finite control
  before the functional-graph argument.
- **No completion comparison is used.** The machine theorem is purely
  combinatorial.  The ordinary centered conclusion enters only through the
  already separated rational lasso theorem of `L-9908`.
- **No divergent orbit is claimed.** The result is a negative architecture
  lemma and supplies no positive seed.
