# Termination machinery applied to the complete source–target program

## Result and proof boundary

This pass obtains an exact, unrestricted repetition theorem for **every supplied
ordinary parity block**. If its multiplier is `3^r`, its clock is `K`, and its
correction is `C`, the signed displacement

\[
\Delta(n)=3^r n+C-2^K n
\]

loses exactly `K` binary valuation units whenever that same block is repeated.
This is proved in
[`lean/Collatz/AffineBlockPrecision.lean`](lean/Collatz/AffineBlockPrecision.lean),
including actual positive-gap prefixes, initial even runs, and the ordinary
orbit clock. The block length, correction, initial integer, and number of
repetitions are unrestricted.

An expanding block therefore cannot repeat forever on a positive integer.
This gives a genuine decreasing quantity for the expanding negative-cycle
shadows encountered in the repository. **It does not prove that changing
blocks share a decreasing quantity.** `FloorIntervalStep`, the original
residue implication, and universal Collatz convergence remain unproved.

No earlier source file was changed. There is no new assumed closing theorem.

## 1. The primary theorems selected

These sources were read directly; the subsequent arithmetic tests are derived
here rather than attributed to a termination prover.

| Primary source | The theorem actually used in the attempted instantiation |
|---|---|
| Yolcu, Aaronson, Heule, [*An Automated Approach to the Collatz Conjecture*](https://emreyolcu.com/research/rewriting-collatz.pdf), Theorem 3.17 and Lemma 3.18 | Their eleven-rule mixed binary/ternary system terminates exactly when Collatz converges. Boundary-rule analysis can use relative top termination. Theorems 3.8 and 3.10 exclude natural matrix interpretations for their **unary** system, including its reduced dependency-pair problem; that exclusion is not a theorem about every interpretation of the mixed-base system. |
| Zantema, [*Termination of term rewriting by semantic labelling*](https://pure.tue.nl/ws/portalfiles/portal/4282167/412152.pdf), Theorem 4 | Labelling by a model preserves and reflects termination. The labelled rules still need a termination proof; assigning names to carry states does not provide one. |
| Podelski and Rybalchenko, [*Transition Invariants*](https://swt.informatik.uni-freiburg.de/berit/papers/transition-invariants.pdf), Theorem 1 | A finite union of well-founded relations suffices when it contains the **reachable transitive closure**, not merely the individual program steps. The proof uses finite-color Ramsey. |
| Hyvernat, [*The Size-Change Termination Principle for Constructor Based Languages*](https://pierre-hyvernat.apps.math.cnrs.fr/data/Files/sct.pdf), Proposition 2.7 | Every coherent loop in a safe finite call abstraction must have a decreasing parameter. Constructor information can exclude spurious paths, but this exclusion must be proved sound. |
| Kassing, Vartanyan, Giesl, [*A Dependency Pair Framework for Relative Termination of Term Rewriting*](https://arxiv.org/html/2404.15248v1), Theorems 4.1, 5.3, 5.4 | Annotated dependency pairs provide a sound and complete chain criterion with a nonduplicating base system, together with graph and reduction-pair processors. Removing one component still leaves the other recurrent components to discharge. |
| Kruskal, [*Well-quasi-ordering, the tree theorem, and Vazsonyi's conjecture*](https://www.cs.tau.ac.il/~nachumd/term/Kruskal.pdf), Section 2 | Finite trees labelled in a well-quasi-order are well-quasi-ordered by the specified embedding. An application must connect that embedding to a legal decreasing program transformation. |

### Direct path orders do encounter an actual embedding obstruction

In the mixed-base system, write `L,R` for the boundary symbols. The exact rules
give

```
L t R  ->  L 2 R  ->  L f t R.
```

The rightmost string contains the original as a subword. Thus a strict order
that both orients the rewrite steps and makes insertion of a unary context
strictly increase a term would require both directions of the same strict
comparison. Plain simplification orders cannot orient this system directly.
This calculation does not exclude semantic labelling, dependency pairs, or
interpretations without the subterm property. It identifies the obligation
those stronger methods must handle.

## 2. The exact program state after source exhaustion

The source–target coupling retains

\[
N=2^a q-m,
\qquad m>0.
\]

The supplied source word is finite. Once its actual endpoint is `q=1`, padding
by the genuine source loop of gap two gives the following target updates,
as long as `a>=1`:

\[
\begin{array}{c|cc}
&a'&m'\\ \hline
N\text{ even}&a-1&m/2\\
N\text{ odd}&a+1&2^{a-1}+(3m-1)/2.
\end{array}
\]

These equations preserve `N'=T(N)` exactly. At the even step, `a=1` would
give `N'<=1` because `N=2-m` and `m>0`; a nonreturning branch above a positive
original target cannot silently continue through that boundary.

The ratio `m/2^a` stays unchanged at an even step and increases at an odd step
when `N>1`. Its increase is real-valued and bounded above by one, so it is not
itself descent in a well-founded order. The original certificate and original
target remain metadata; neither can be reset merely because `q=1`.

For example, the actual block `odd,even,odd` sends

\[
N=8k+1\longmapsto9k+2.
\]

At a terminal state with a sufficiently large `a`, this increases all three
raw natural quantities `N,a,m`. Source-word length is already zero. A
size-change graph using only those quantities therefore has no decreasing
thread for this block. Its congruence guard must be used arithmetically.

## 3. A decreasing quantity for every fixed block

Let an ordinary parity block have `r` odd steps, clock `K`, and correction `C`.
For an actual application from `n` to `n'`,

\[
2^K n'=3^r n+C.
\tag{1}
\]

Set `A=3^r`, `B=2^K` and `Delta(n)=A*n+C-B*n`. Direct multiplication gives

\[
\boxed{B\Delta(n')=A\Delta(n).}
\tag{2}
\]

For `j` legal repetitions with actual endpoints `n_0,...,n_j`,

\[
\boxed{2^{Kj}|\Delta(n_j)|=3^{rj}|\Delta(n_0)|.}
\tag{3}
\]

Since powers of two and three are coprime,

\[
\boxed{2^{Kj}\mid |\Delta(n_0)|.}
\tag{4}
\]

If `|Delta(n_0)|=2^H*u` with `u` odd, (3)--(4) yield the exact statement

\[
\boxed{Kj\le H,\qquad
|\Delta(n_j)|=2^{H-Kj}3^{rj}u.}
\tag{5}
\]

The last factor `3^(rj)*u` is odd. Thus the valuation really decreases by the
whole block clock, rather than merely satisfying an upper bound. A convenient
valuation-free consequence is

\[
Kj\le\lfloor\log_2|\Delta(n_0)|\rfloor
\quad\text{when }\Delta(n_0)\ne0.
\tag{6}
\]

When `A>B` and `n_0>0`, the displacement is positive. Hence an expanding
block has no exceptional positive fixed point and cannot repeat forever.
For a general block, the zero-displacement exception is necessary: it means
that the affine block returns its starting value. The proof does not exclude
an unproved positive Collatz cycle by assumption.

### Formal interface

The Lean block is an initial even run `e` followed by an arbitrary supplied
positive-gap list `W`. Its parameters are

\[
K=e+\operatorname{total}(W),\qquad
r=|W|,\qquad C=2^e\operatorname{correction}(W).
\]

This includes an empty odd word and pure initial halvings. The last endpoint
may be even. `Block e W n n'` contains the exact integer factor after the
initial halvings and an existing project `Prefix`; `block_orbit` proves that
its endpoint is the actual ordinary iterate. `repeated_actual_orbit` retains
the clock `K*j` for every intermediate block endpoint.

The principal checked declarations are `repeated_balance`,
`repetition_precision`, `repetition_exact_precision`,
`repetition_clock_bound`, `no_infinite_repetition`, and
`expanding_no_infinite_repetition`.

For the particular block `W=[2,1]`, the correction is seven and
`Delta(n)=n+7`. Therefore every repetition costs exactly three units of
`v_2(n+7)`. The result also applies to the eleven-clock negative-seventeen
cycle in PR185: its expanding multiplier cannot be repeated indefinitely by
one positive integer merely because arbitrarily long positive lifts exist.

## 4. Why the valuation threads have not yet synchronized

Equation (2) is strong enough to orient each fixed-block loop. A new block
has a new affine center and a new displacement. Applying a theorem about
each of these measures separately does not meet the finite, transitive-
closure hypothesis of the transition-invariant theorem.

There are infinitely many relevant centers even in a very simple language.
For `h>=2`, take `h` odd steps followed by one even step. Its affine map is

\[
F_h(n)=\frac{3^h n+(3^h-2^h)}{2^{h+1}},
\qquad
z_h=-\frac{3^h-2^h}{3^h-2^{h+1}}.
\tag{7}
\]

The rational `z_h` has odd denominator and precisely this periodic parity
word: `v_2(z_h+1)=h`, the `h` odd steps take it to `2*z_h`, and the last
halving returns it. The distinct centers approach `-1`. Positive integers
agreeing with `z_h` to sufficiently many binary places realize arbitrarily
many finite repetitions. Every intermediate value in these expanding
blocks exceeds the original positive integer. The finite repetition bound
is nevertheless exactly (5).

A new valuation can also be regenerated to arbitrary size without any
original-target descent during the regenerating block. For `j>=1`, put

\[
t_j=\frac{4\,2^{6j}-13}{9}.
\]

This is a positive integer, and the actual first three steps are
`odd,odd,even`, ending at `2^(6j-1)-1`. They all stay above `t_j`, while

\[
v_2(t_j+1)=2,
\qquad
v_2(T^3(t_j)+1)=6j-1.
\]

The appropriate block displacement `n+5` does decrease in valuation. Thus
this is not a counterexample to size-change methods: it demonstrates why
one must prove transfer of a persistent thread, rather than select a fresh
large valuation after each block. These arithmetic examples do not assert
that every such terminal abstraction is reachable with an extremal supplied
source certificate.

The exact `S=820,q=205,t=1407` witness already retained by the project is a
separate warning about the original clock: the source finishes at clock 21
while the target first falls below 1407 at clock 81. The proof above does not
identify source exhaustion with target return.

## 5. Testing the maximum-source condition

At fixed gap multiset, the total clock `A` and odd count `r` are fixed, so

\[
q=\frac{2^A-C_W}{3^r}.
\]

Maximizing the represented source does minimize `C_W` **among legal
integer permutations**. I tested whether this could turn word embedding or
valuation-thread recurrence into an automatic source improvement.

The basic exchange is already constrained by a growing ternary modulus.
Write

\[
W=U\mathbin{++}[a,b]\mathbin{++}V,
\qquad |U|=k,\quad\operatorname{total}(U)=P.
\]

If swapping `a,b` while retaining the endpoint produces another integer
source `q'`, subtraction of the two exact certificate identities gives

\[
\boxed{3^{k+2}(q'-q)=2^P(2^a-2^b).}
\tag{8}
\]

For distinct `a,b` in `{1,2,3,4}`, the right side has ternary valuation at
most one, whereas the left side is divisible by nine. Consequently **no
single adjacent unequal swap in this alphabet is legal**, even at the
front of the word. Successful multi-letter permutations use cancellations
not visible in the individual exchanges. For example `[3,4,2]` and
`[2,3,4]` have corrections 161 and 53, whose difference 108 is divisible by 27.

Kruskal or Higman embedding does not supply these congruences. Deleting a
letter also changes the odd-count denominator. A pumping argument would
therefore need an embedding that preserves the exact affine endpoint and
the required ternary divisibility, together with a demonstrated rank drop
or equal-grade source increase. No such exhaustive compatibility theorem
was obtained. The already proved maximum-source hypothesis has not been
replaced by unrestricted sorting of the gap word.

## 6. Verification and central status

`AffineBlockPrecision.lean` compiled with Lean 4.34.1 and
`-DwarningAsError=true`. Its proof uses existing literal `Prefix` semantics,
integer multiplication, natural absolute values, and coprimality of powers
of two and three. There is no `sorry`, `native_decide`, custom axiom, or
Collatz assumption. No finite experimental cutoff is used to establish
the repetition theorems. The parent integration performs the aggregate
build and axiom audit.

The new theorem removes indefinite repetition of **one fixed expanding
block** from the candidate bad program. The remaining central step is
still the actual changing-block program with the same original target and
source witness. I did not prove a finite disjunctive transition invariant,
a well-founded multiset of transferable valuation threads, or a
source-maximality contradiction covering all of that program. The
literature results above do not assert any of those missing hypotheses.
