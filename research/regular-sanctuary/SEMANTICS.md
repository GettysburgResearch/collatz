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

## 7. Finite-horizon safety automata

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
connected structure is intended as data from which to conjecture a smaller
inductive language; every conjecture must return to the exact closure checker.

## 8. Scope cautions

- Fixed-DFA and fixed-block verification is decidable; unrestricted existence
  over all automaton sizes is not claimed decidable.
- Finite words only are admitted.  An infinite LSD stream is a 2-adic object
  and need not encode any positive integer.
- A failed bounded search excludes only its declared skeleton/template class.
- BFS witnesses are shortest by length and LSD-first lexicographic order, not
  necessarily numerically least.
- A regular sanctuary is stronger than a lone divergent orbit; Collatz falsity
  would not automatically imply that such a sanctuary exists.
