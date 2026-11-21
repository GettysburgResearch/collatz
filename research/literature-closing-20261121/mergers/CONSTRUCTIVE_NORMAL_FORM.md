# A global mixed-base normal form and a concrete smaller partner

**Status: the constructive reduction, explicit partner inequalities, and
arbitrary-prefix `f11` merger compiled successfully in Lean 4.34.1; the
ordinary merger needed for universal closure remains OPEN.** The new Lean
source is `MixedBaseNormalForm.lean`. Its focused compile used `-j 1` and
`-DwarningAsError=true` and completed with no diagnostics. See the combined
build receipt for the integrated packet's separate axiom-audit status.

This attack starts from every positive ordinary integer, not a finite set of
residue cells. It produces a finite normal form on the same actual forward
orbit. The complete exceptional grammar then supplies a specific smaller
ordinary candidate, with a strict decrease in the very rank used by the
normalizer. The first missing implication is that the candidate belongs to
the same ordinary Collatz component.

## 1. Literature and current source boundary

Yolcu–Aaronson–Heule, *An Automated Approach to the Collatz Conjecture*,
arXiv:2105.14697v3, Theorem 3.17 and §4.3, give an eleven-rule mixed-base
system whose termination is equivalent to Collatz, and terminating
one-rule-deletion subsystems. Example 4.3 supplies the two-dimensional natural
matrix interpretation used below. Our new work is the explicit ordinary
normal-form interface, its complete exceptional grammar, and the erasure
partner/closing theorem; the matrix itself is credited to that source.

Primary text: <https://arxiv.org/html/2105.14697v3>.

The relevant current repository heads were inspected directly:

| Source | Frozen head | Interface inspected |
|---|---|---|
| PR 177 | `00a611094043afeb256d6532b477c0709e8ed270` | Complete supplied-certificate induction and unbounded gap rewrites; `CollatzGapComparison.Complete` remains unproved. |
| PR 178 | `0bb13b800e4e97f9fd3091b1a3d2e98b49911b7c` | Actual marked returns, common-rank and weighted-rank scope. |
| PR 184 | `366dab89ee9548084ab9b5e4e90ff82abf287a20` | Ordinary smaller-source mergers, source-bounded induction, and lower marked component partners. |

The present construction neither presumes these covers nor combines their
different ranks. It uses one concrete rank throughout its own normalization
and proposed erasure step.

## 2. Canonical ordinary words

The initial symbol `L` represents one; the final symbol `R` represents the
identity. Between them, use five digit maps:

| Symbol | Numeric action |
|---|---:|
| `f` | \(x\mapsto2x\) |
| `t` | \(x\mapsto2x+1\) |
| `0` | \(x\mapsto3x\) |
| `1` | \(x\mapsto3x+1\) |
| `2` | \(x\mapsto3x+2\) |

Read these numeric actions from left to right. Every finite canonical word
has a positive ordinary value. Every positive ordinary integer has a canonical
binary word using only `f,t`, so no completion or missing input domain is
introduced by this representation.

The ordinary shortcut map remains

\[
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2.\end{cases}
\]

Omit the single auxiliary exchange `f1 -> 0t`. The retained rules are

```text
fR -> R       tR -> 2R
f0 -> 0f      f2 -> 1f
t0 -> 1t      t1 -> 2f      t2 -> 2t
L0 -> Lt      L1 -> Lff     L2 -> Lft
```

Every internal or leading exchange preserves ordinary value identically.
The two right-boundary rules apply exactly one shortcut step. Thus every
finite reduction records an actual identity

\[
\operatorname{value}(w_{\rm final})=T^k(\operatorname{value}(w_{\rm initial}))
\]

for a natural clock \(k\), counting just the right-boundary rules. The clock
does not count arithmetic representation changes as orbit steps.

## 3. One concrete rank proves arbitrary-word normalization

For a pair \((x,y)\in\mathbb N^2\), use these affine interpretation maps:

\[
\begin{aligned}
F(x,y)&=(x+y,x),\\
G(x,y)&=(x+3y+1,3x+4y+1),\\
Z(x,y)&=(7x+2y+2,2x+5y+1),\\
O(x,y)&=(2x+y+1,x+y),\\
U(x,y)&=(2x+2y,2x+4y+2).
\end{aligned}
\]

These correspond to `f,t,0,1,2`. For rank evaluation, the rightmost symbol
acts first; this order is intentional and differs from numeric evaluation.
Apply a digit word to \((1,1)\), obtaining \((a,b)\), and put

\[
\mathcal R(w)=a+5b.
\]

For every retained internal rule, the replacement is strictly smaller in
the first coordinate and non-increasing in the second, on **every**
nonnegative input pair. Each left context preserves these two inequalities.
The three leading rules decrease \(a+5b\) directly. The right-boundary
rules decrease the input pairs

\[
F(1,1)=(2,1)>(1,1),\qquad
G(1,1)=(5,8)>(4,8)=U(1,1).
\]

Consequently every retained rewrite strictly decreases the natural number
\(\mathcal R\). Strong induction on this rank gives a finite normal form
for **every finite canonical word**, without any bound on word length or
ordinary value. The Lean source proves the rule inequalities in arbitrary
contexts and the resulting existence theorem. `normal_form.py` additionally
checks each whole affine coefficient inequality and emits ordinary traces.

The value is allowed to grow during normalization. This is why an induction
on the original ordinary value alone would be the wrong proof here.

## 4. The complete exceptional grammar

The irreducible canonical words are exactly

```text
LR
or
L([ft]* f 1 [012]*)+R.
```

Spaces in the expression only separate its pieces. A nonterminal word is a
nonempty sequence of blocks. Each block consists of a nonempty binary run
ending in `f`, followed by a nonempty ternary run beginning with `1`.

**Proof of necessity.** A nonempty irreducible word cannot begin with a
ternary digit, because one of the leading rules would apply. It cannot end
with a binary digit, because a right-boundary rule would apply. At a binary
to ternary transition, five of the six possible adjacent pairs have retained
exchange rules. The sole unremoved boundary is `f1`. Splitting the word into
maximal binary and ternary runs gives the displayed grammar.

**Proof of sufficiency.** Every word of that grammar begins with a binary
digit and ends with a ternary digit. Its binary to ternary transitions are
all `f1`, and its other adjacent pairs have no retained internal rule. None
of the ten left-hand sides occurs. The empty interior `LR` is also
irreducible.

The Lean module proves the necessary suffix form used by the arithmetic
construction. Its rightmost blocked pair has only ternary digits after it:

\[
w=\texttt{L}\,p\,\texttt{f1}\,v\,\texttt{R},
\qquad v\in\{\texttt0,\texttt1,\texttt2\}^k.
\]

If \(q\ge1\) is the ordinary value after the prefix \(p\), and \(r\) is
the base-three value of \(v\), then

\[
0\le r<3^k,\qquad
\boxed{\operatorname{value}(w)=3^k(6q+1)+r.}\tag{NF}
\]

Every positive ordinary source therefore reaches one or an exact ordinary
endpoint of form (NF), together with its finite representation and clock.
The grammar describes the actual irreducible words, rather than asserting
that every unconstrained triple \((k,q,r)\) is an irreducible encoding.

## 5. A concrete universal smaller-partner candidate

At a blocked pair, erase its ternary `1`:

```text
p f1 v  -->  p f v.
```

For the rightmost pair in (NF), the candidate value is

\[
\boxed{m=3^k(2q)+r<n=3^k(6q+1)+r,}\tag{E}
\]

and \(m>0\). The exact saving is \(3^k(4q+1)\).

This erasure also strictly decreases the **same** matrix rank, in arbitrary
mixed contexts. At an arbitrary suffix interpretation \((x,y)\),

\[
F(O(x,y))-F(x,y)=(2x+y+1,x+y+1).
\]

Both coordinates are positive. Every prefix preserves the strict first
coordinate inequality, so \(\mathcal R(pfv)<\mathcal R(pf1v)\). The Lean
theorem `blocked_erasure_decreases` retains both the ordinary-value and the
rank inequalities.

The erasure is a **candidate merger**, not an allowed arithmetic exchange.
Unlike the retained exchanges, it changes the represented integer. What is
missing is an actual pair of finite ordinary clocks with

\[
T^a(n)=T^b(m).\tag{M}
\]

The conjectural erasure cover permits choosing any one blocked pair of each
nonterminal normal word. The rightmost pair always gives the explicit
candidate (E). It does not posit that every erased pair automatically works.

### A genuine unbounded merger class

The candidate does work for every mixed prefix followed by `f11`:

\[
\texttt{L}\,p\,\texttt{f11R}
\quad\rightsquigarrow\quad
\texttt{L}\,p\,\texttt{f1R}.
\]

For arbitrary \(q=\operatorname{value}(p)\ge1\), the parent and partner
are \(n=18q+4\) and \(m=6q+1\). The parent is even, the partner is odd,
and their actual first shortcut images agree:

\[
\boxed{T(n)=9q+2=T(m).}
\]

This supplies explicit ordinary merger clocks \(a=b=1\), together with
the already proved strict decreases in both value and rank. The new
Lean declaration `terminal_double_one_merger` formalizes the common
endpoint for every finite mixed prefix. It does not assume normality;
in particular it applies to every normal word of this shape.

The same paper calculation covers a rightmost ternary suffix \(v=1^k\)
of any odd positive length. Its ternary value is
\(r=(3^k-1)/2\), which is odd because \(3^k\equiv3\pmod4\). Thus

\[
m=2q\,3^k+\frac{3^k-1}{2}\quad\text{is odd},\qquad
n=3^k(6q+1)+\frac{3^k-1}{2}=3m+1
\]

is even, and again \(T(n)=T(m)\). These complete all-parameter classes
discharge genuine portions of the proposed erasure cover. Normal forms
with other terminal ternary suffixes still need merger clocks.

### Exact closing theorem, with the open hypothesis visible

`BlockedErasureCover` states that every nonempty normal form has at least one
erasure with an ordinary merger (M). The module proves

\[
\boxed{\texttt{BlockedErasureCover}\iff\texttt{Universal}.}\tag{C}
\]

For the useful direction, induct on \(\mathcal R(w)\) for arbitrary words.
If a retained rule applies, its child has smaller rank and its convergence
transfers through zero or one actual shortcut step. If the word is a
nonterminal normal form, use the proposed erased partner: it has smaller
rank, and its convergence transfers through (M). The sole empty normal
form represents one. All positive ordinary inputs have binary
representations, finishing the implication. The reverse direction follows
by meeting both positive ordinary inputs at one.

This gives a single explicit all-length arithmetic obligation. Its rank
argument is already compatible with ordinary value growth during the
normalizer. It avoids the invalid inference that a partner smaller than a
later, larger endpoint is automatically smaller than the original source.
It does not establish the open merger assertion (M).

## 6. The first closing attempt and its exact failure

One way to seek (M) is to restore the omitted value-preserving rule
`f1 -> 0t`, then normalize with the ten retained rules. If this always
returned to a smaller rank, it would provide the needed descent without
using erasure. The smallest nonterminal example already defeats that
one-return claim:

| Word | Ordinary value | Matrix rank |
|---|---:|---:|
| `Lf1R` | 7 | 26 |
| restored `L0tR` | 7 | 308 |
| next normal form `Lff1R` | 13 | 40 |

The four ordinary steps are

\[
7\longmapsto11\longmapsto17\longmapsto26\longmapsto13.
\]

Eleven retained rewrites perform that segment and the intervening arithmetic
conversion. Restoring the next blocked pattern eventually normalizes 13 to
one, but the first block has increased both value and rank. Thus the rank
cannot simply be restarted after each missing-rule event.

For the direct erasure candidate, `Lf1R` proposes the partner `LfR`, of
ordinary value two and rank seven. Both reach one, so this particular
merger exists. The calculation supplies no uniform merger for the complete
grammar, whose prefix and ternary suffix are unbounded.

An attempted shortcut was to reverse the missing exchange and add
`0t -> f1`. Its matrix rank also decreases, so it can help minimize a
representation of one fixed value. But restoring `f1 -> 0t` can then be
immediately undone: for example, the normal word `Lf10f1R` becomes
`Lf100tR`, and a leftmost normalization using the reverse rule returns
straight to the original word without taking any ordinary step. The main
normalizer therefore uses exactly the ten retained original rules. This
failed minimization strategy is not silently substituted for a successful
component descent.

The unsupported step is now completely concrete: find an ordinary merger
for at least one blocked-erasure candidate in **each actual normal form**, or construct
a different partner whose decrease can be checked in this one rank. The
matrix inequalities and the normal-form grammar do not furnish those
clocks.

## 7. What the other termination literature does and does not add

Podelski–Rybalchenko, *Transition Invariants*, LICS 2004, require a finite
union of well-founded relations to cover the **transitive closure** of the
program relation. Covering individual edges by independently decreasing
ranks does not satisfy that hypothesis. Here the explicit 7-to-13 return
shows why the omitted-rule segments need their own proof.

Primary source: <https://lics.siglog.org/2004/PodelskiRybalchenko-TransitionInvariant.html>.

The October 2026 Nashida repositories describe additional dimension-free
barriers for some positive-growth matrix classes. Their README explicitly
says those barriers are paper-level, not Lean formalized; the available
Lean claims cover other certificate and residue results. The primary PDFs
were not retrievable in this pass. No Nashida barrier is used as a theorem
or imported as an axiom here.

Primary repositories:
<https://github.com/harappa/collatz-matrix-interpretation-barriers> and
<https://github.com/harappa/collatz-termination-certificate-dichotomy>.

## 8. Evidence and exact limits

The executable checks all ten affine interpretation inequalities, then
replays five selected normal-form returns with actual values, ranks,
individual rewrite steps, and ordinary clocks. Its report preserves the
7-to-13 obstruction and the proposed smaller erasure partners.

```sh
python -X utf8 -B research/literature-closing-20261121/mergers/normal_form.py \
  --output research/literature-closing-20261121/mergers/normal-form-report.json
```

The five traces are examples. The arbitrary-word scope is the written proof
and the 25 public Lean declarations, compiled in the focused run. The full
grammar and the arbitrary odd-length all-ones suffix extension are written
proofs; their formal coverage is the necessary suffix theorem and the
explicit `f11` merger described above. No finite search over normal
forms is used to assert universal merger coverage. Full Collatz remains open.
