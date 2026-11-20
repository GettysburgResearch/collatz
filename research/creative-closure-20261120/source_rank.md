# A fixed stopping rank does not bound the exceptional carry allowance

**Status: PROPOSED, with elementary deductions and a small exact
finite-state check. No Collatz closure.** This note tests whether the
source-persistent controller in [symbolic_order.md](symbolic_order.md),
CSO-002, can obtain its exceptional-rule allowance from a supplied
antecedent's fixed number of odd inputs. A uniform allowance of that
kind fails, even for the pure-power targets singled out by the latest
reverse-basin source. Source-dependent allowances remain open.

## Pinned source and normalization

The source inspected is PR146 at commit
`e238c63a5d57f96bb063b7472498d1977df51951`:

| File | Git blob | Relevant statement |
|---|---|---|
| [DEEP_REVERSE_BASIN.md](https://github.com/GettysburgResearch/collatz/blob/e238c63a5d57f96bb063b7472498d1977df51951/research/upper-bit-mergers/DEEP_REVERSE_BASIN.md) | `a0e04b11d5452a3838d1c40f0563b92436b6d048` | Its first nonempty antecedent rank is four; that restricted reverse implication is equivalent to convergence of all `3^(27j-1)`, `j>=1`. |
| [BOUNDED_RANK_TRANSFER.md](https://github.com/GettysburgResearch/collatz/blob/e238c63a5d57f96bb063b7472498d1977df51951/research/upper-bit-mergers/BOUNDED_RANK_TRANSFER.md) | `2724f5ae9301629293b8642fa4c1759271977281` | Its bounded lifted-merger test does not establish a partner's stopping certificate when that test fails; fixed-rank templates can require unbounded partner odd counts. |

Use the positive shortcut map `T`, killed at first arrival at 1 when
counting a terminating certificate. Write `o(n)` for the number of odd
inputs before that arrival, when it exists. This notation avoids
confusion with the remaining allowance in CSO-002. Use exactly the
eleven AYH rules, alphabet, ordinary decoder, and attribution fixed in
`symbolic_order.md`.

The initial word below is always the **canonical binary word** for its
ordinary value. Thus its leading one is `c`, its remaining zero/one
digits are `a,b`, and its right boundary is `d`. A complete derivation
means a finite literal derivation to `cd`.

## CSR-001: a schedule-independent first-carry obstruction

### The first ternary token must read the original binary prefix

At any odd binary source greater than 1, the first rewrite is necessarily
`bd -> gd`. Mark the newly created ternary token `g`. Each internal
binary/ternary rule moves this same token one position left, changing
its state among `e,f,g` and emitting a binary digit to its right. Mark
the ternary token on the right-hand side as its continuation.

Every later dynamic event creates its ternary token to the right of the
marked one. There is no rule exchanging two ternary tokens. Until the
marked token reaches `c`, everything to its left is the untouched
initial binary prefix: an interior rule can alter those digits only
when the marked token crosses them. Right-boundary dynamics cannot
reach that prefix through the marked token. No dynamic rule deletes a
ternary token. The only way to delete the marked token is one of
`ce,cf,cg` at the left boundary.

Consequently every complete derivation must make the marked token read
the original binary prefix right to left, in exactly the same order and
states, regardless of all intervening administrative or dynamic choices.
Its transition table is

| Carry state | Read binary zero | Read binary one |
|---|---|---|
| `e` | `e`, emit `0` | `f`, emit `1` |
| `f` | `e`, emit `1` **(exceptional `af -> eb`)** | `g`, emit `0` |
| `g` | `f`, emit `0` | `g`, emit `1` |

The number of exceptional transitions of this first token is therefore
a schedule-independent lower bound on the total exceptional-rule count
of every complete derivation. The assertion does not presuppose that a
complete derivation exists.

### Already exact odd rank two requires unbounded allowance

For `t>=1`, put

\[
 a_t=\frac{2^{6t+4}-7}{9},\qquad
 u_t=\frac{2^{6t+2}-1}{3}.
\]

These are odd integers greater than 1, and

\[
3a_t+1=4u_t,\qquad 3u_t+1=2^{6t+2}.
\]

Thus `U(a_t)=u_t`, `U(u_t)=1`, and `o(a_t)=2` exactly. The binary
expansion of `a_t` is `(111000)^t1`, as follows by summing the geometric
series of these six-digit blocks. Before the last one, and after the
leading one represented by `c`, the prefix is
`11000(111000)^(t-1)`.

The marked token starts in state `g`. Reading a full block right to
left gives `000111`, returns to `g`, and uses `af -> eb` exactly once.
The shortened left block reads `00011`, also returns to `g`, and uses
that rule exactly once. Finally `cg` removes the token. Every complete
derivation from the canonical word for `a_t` therefore contains at least
`t` exceptional carries.

In particular, there is no finite function `K(p)` that bounds the
required canonical-input carry allowance for every convergent source of
exact odd rank `p`. The failure occurs already at `p=2`, independently
of scheduling and without any hypothetical nonconvergent input.

### The actual rank-four antecedents require at least nine carries per block

The family in `DEEP_REVERSE_BASIN.md` is

\[
 k_j=\frac{2(2^{54j}-1)}{81},\qquad
 y_j=128k_j+1=\frac{2^{54j+8}-175}{81},\qquad j\ge1.
\]

The three initial odd/even pairs lead to `54k_j+1`, and
`3(54k_j+1)+1=2^(54j+2)`. Hence `o(y_j)=4` exactly. All these known
certificates have the same seven parities through their last odd input,
`odd, even, odd, even, odd, even, odd`; only the final halving tail grows.

Set `B=2^54` and `R=(B-1)/81=222399981598543`. Let `W` and `V` be the
following fixed 54-bit blocks, including their leading zeros:

```text
W = binary_54(13R)   = 001010010001011000011111100110101101110100111100000011
V = binary_54(13R-2) = 001010010001011000011111100110101101110100111100000001
```

The identity

\[
y_j=3B^j+13R\sum_{i=1}^{j-1}B^i+(13R-2)
\]

shows that its binary spelling is `11 W^(j-1) V`. This is an algebraic
identity for every `j`, not an extrapolation from checked examples.
The marked first token reads `V` with its final one removed, then all
the `W` blocks, then the one remaining initial binary one. The exact
finite-state table is

| Block read right to left | Starting state | Ending state | Exceptional transitions |
|---|---|---|---|
| `V` without its final one | `g` | `e` | 9 |
| `W` | `e` | `e` | 9 |
| `W` | `f` | `e` | 9 |
| `W` | `g` | `e` | 9 |
| Remaining initial `1` | `e` | `f` | 0 |

The final `cf` removes the token. Thus **every complete canonical-input
derivation for this actual rank-four antecedent uses at least `9j`
exceptional carries**. This lower bound concerns one marked token; it
does not claim that `9j` is the minimum total carry count.

### A fixed antecedent-rank allowance also fails on the required pure powers

The stronger issue is the target itself. For every positive integer `t`,
there are infinitely many `j>=1` such that every complete canonical-input
derivation for

\[
 n=3^{27j-1}
\]

requires at least `t` exceptional carries. This assertion does not claim
that any of those derivations exists.

To prove it, set `H=6t+1`. The integer `a_t` above is `1 mod 8` and has
exactly `H` binary digits. Powers of 9 exhaust the residues `1 mod 8`
modulo `2^H`. Indeed successive squaring gives

\[
v_2(9^{2^s}-1)=s+3\qquad(s\ge0),
\]

so 9 has order `2^(H-3)`, the number of such residues. Write `j=2q+1`.
Then

\[
3^{27j-1}=9^{27q+13}.
\]

Since 27 is invertible modulo `2^(H-3)`, infinitely many `q>=0` give
`3^(27j-1) = a_t mod 2^H`. Choose them large enough that the power has
more than `H` bits. Its low `H` digits are exactly `(111000)^t1`.
After the first dynamic rule, the marked token must read all `t` full
blocks before it can even reach the higher prefix. Each block forces
one exceptional transition. The schedule-independent bound follows.

Therefore, for any proposed fixed allowance `K(4)`, choose `t>K(4)`
and one of these indices. Every maximal schedule of the CSO-002
controller started from that target's canonical binary word terminates
with **UNRESOLVED carry budget**. Termination of the controller is
already proved by its natural-number rank; reaching `cd` is excluded
by the marked-token lower bound. This conclusion does not infer
convergence or divergence of the target ordinary orbit.

## What the combination still lacks

Unbounded target odd counts or first-descent deadlines alone would not
disprove a fixed carry allowance: the controller's bound also contains
the source-dependent matrix value `P(w_0)`, which can grow with height.
CSR-001 supplies the needed distinction by proving unbounded **actual
exceptional-rule demand**, even allowing arbitrary interleaving.

The main bounded-rank theorem in `BOUNDED_RANK_TRANSFER.md` also has a
directional condition: its initially certified arm is the lower arm
`x=16k+1`, whereas the deep-reverse family certifies the upper arm
`y=128k+1`. Its bounded lifted-merger deadline cannot simply be reversed.
In either direction, a test excluding lifted mergers does not construct
the ordinary stopping certificate that is still needed.

A useful remaining theorem would have to bound an allowance depending
on the **particular fixed source**, with its growing digit information,
and prove that the allowance suffices for a complete derivation. No such
bound is established here. The argument also does not rule out a new
construction starting from a different mixed representation with its
own justified allowance analysis. It specifically rules out closing
the canonical pure-power family by an allowance depending only on its
supplied antecedent's fixed rank, even if the antecedent's fixed
pre-halving parity template is included.

## Reproducible finite-state check

The universal statements above use the marked-token proof, the displayed
integer identities, and the order of 9. Only the fixed block table is a
finite calculation. The following short exact check was run successfully;
it verifies all four nontrivial rows and four instances of each displayed
binary identity. It is not a convergence census or a proof by sampling.

```python
B = 1 << 54
R = (B - 1) // 81
W, V = format(13 * R, "054b"), format(13 * R - 2, "054b")
# State 0=e, 1=f, 2=g; each value is (next state, exceptional count).
move = {(0, 0): (0, 0), (1, 0): (0, 1), (2, 0): (1, 0),
        (0, 1): (1, 0), (1, 1): (2, 0), (2, 1): (2, 0)}

def scan(word, state):
    count = 0
    for digit in reversed(word):
        state, extra = move[state, int(digit)]
        count += extra
    return state, count

def require(condition):
    if not condition:
        raise ValueError("finite-state check failed")

require(scan(V[:-1], 2) == (0, 9))
for state in range(3):
    require(scan(W, state) == (0, 9))
for j in range(1, 5):
    y = ((1 << (54*j + 8)) - 175) // 81
    require(format(y, "b") == "11" + W*(j - 1) + V)
    require(scan(format(y, "b")[1:-1], 2) == (1, 9*j))
for t in range(1, 5):
    n = ((1 << (6*t + 4)) - 7) // 9
    require(format(n, "b") == "111000"*t + "1")
    require(scan(format(n, "b")[1:-1], 2) == (2, t))
print("PASS: fixed carry table and eight binary-identity examples")
```
