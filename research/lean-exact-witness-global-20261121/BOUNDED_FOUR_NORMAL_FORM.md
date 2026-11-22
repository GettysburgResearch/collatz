# One canonical endpoint for the entire bounded-four source problem

## Formal result

`lean/Collatz/BoundedFourNormalForm.lean` proves that the repository's remaining
`LowIntervalStep` is equivalent to one source-prefix obligation with endpoint
**11** and the fixed complete tail **[1,2,3,4]**. Its prefix is nonempty and may
have arbitrary length. The original complete-source induction hypothesis is
preserved exactly.

The new universal statement is an exact factorization of every supplied
complete certificate with gaps at most four. It does not assume Collatz, a
carry-capture theorem, an ordinary-merger selector, or convergence of any
unverified terminal carry. `ElevenIntervalStep` remains the single named,
unproved obligation in the resulting conditional global theorem
`collatz_of_eleven_prefix`.

## 1. Literal-word normal form

Write `2^[k]` for a word of k copies of the gap two. For every complete supplied
certificate `Certificate q W` with all gaps at most four, exactly the following
classification is sufficient:

1. `q` and `W` have one of the finite terminal forms in the table below; or
2. for some literal word `P` and natural k,

   \[
   \operatorname{Prefix}(q,P,11),\qquad
   W=P\mathbin{+\!+}[1,2,3,4]\mathbin{+\!+}2^{[k]}.
   \]

The factorization theorem permits `P=[]`. The interval reduction below closes
that case explicitly and leaves only **nonempty P** in its unbounded premise.

| Terminal source | Complete word before arbitrary terminal two padding |
|---:|---|
| 1 | `[]` |
| 3 | `[1,4]` |
| 5 | `[4]` |
| 13 | `[3,4]` |
| 17 | `[2,3,4]` |
| 45 | `[3,2,3,4]` |
| 69 | `[4,3,4]` |

This classification follows from exact integrality, not a search through
certificate lengths. Reading the final source edges backward from one:

\[
1\ \longleftarrow\ 5\ \longleftarrow\ 13\ \longleftarrow\ 17
\ \longleftarrow\ 11.
\]

The gaps along this displayed backward chain are 4, 3, 2, 1. The alternative
bounded-four predecessors are 3 above 5, 69 above 13, and 45 above 17. Each
alternative is divisible by three, so it cannot have an odd predecessor at
any positive gap: the equation `3n+1=2^a q` is impossible when `3 | q`.
At one, gap two is the terminal self-loop. Once state 11 is reached, the
entire remaining prefix is retained without any restriction on its length.

`certificate_normal_form` proves this argument by induction on the supplied
word. Its induction step uses the exact source edge from
`certificate_cons_iff`; it does not replace the certificate with a witness
chosen from an existence statement. Consequently every source greater than
69 with a bounded-four complete certificate passes through the same ordinary
state 11. `above_core_passes_eleven` retains the exact word and its padding.

The normalized language is itself cofinal. `cofinal_eleven_prefixes` proves
that for every N there are q>N and a **nonempty** prefix P over gaps 1 through
4 with `Prefix q P 11`. It applies the existing cofinal predecessor theorem
to the certified unit 11, retains `[1,2,3,4]`, and splits that exact supplied
tail. Its certificate identity `81u+133=1024` forces the split endpoint to be
11. Thus the normal form still supplies arbitrarily large known sources; it
has not collapsed the global task to a bounded collection of source values.

## 2. Cancellation and elimination of padding

The common graded multiset remains

\[
\Gamma(e;W)=
\bigl(\{2e+1\}\text{ if }e>0\bigr)
\uplus\{2a:a\in W\}.
\]

The fixed tail contributes the same grades `{2,4,6,8}` to every canonical
source. Thus `canonical_rank_cancel` proves, for arbitrary e, f, P, Q, and k,

\[
\begin{aligned}
&\Gamma(f;Q[1,2,3,4]2^{[k]})
   \prec\Gamma(e;P[1,2,3,4]2^{[k]})\\
&\hspace{35mm}\Longleftrightarrow\quad
\Gamma(f;Q)\prec\Gamma(e;P).
\end{aligned}
\]

There is no size bound on either prefix, either initial even exponent, or the
common terminal padding. The original highest-changed-grade comparison is
used on both sides.

Positive terminal padding is itself removable. Deleting `k+1` terminal twos
leaves the same represented source and a valid complete certificate, while
strictly lowering its supplied grade. `terminal_padding_interval_rule`
therefore closes the original interval query immediately using the existing
induction hypothesis; its wanted integer is unchanged. The remaining
unbounded obligation needs **no terminal padding parameter**.

## 3. Exact normalization of the remaining interval step

Let `S=2^e q`. The named proposition `ElevenIntervalStep` requests only:

\[
\begin{gathered}
1\le e\le3,\qquad P\ne[],\qquad
\operatorname{Prefix}(q,P,11),\qquad \forall a\in P,\ a\le4,\\
t\text{ odd},\qquad S+1<t\le2S+1,\\
\operatorname{Hyp}\bigl(\operatorname{Interval},
       \Gamma(e;P[1,2,3,4])\bigr)
\quad\Longrightarrow\quad B(t).
\end{gathered}
\]

The fixed tail is a proved ordinary certificate for 11. Appending it to the
given prefix supplies exactly the complete certificate used by the
induction hypothesis. No fresh convergence witness is extracted for a
recursive target.

`low_interval_iff_eleven` proves

\[
\boxed{\operatorname{LowIntervalStep}
       \ \Longleftrightarrow\ \operatorname{ElevenIntervalStep}.}
\]

The forward direction appends the fixed tail and applies the existing
low-interval statement. In the reverse direction, the exact normal form
handles every supplied certificate. A finite terminal motif closes directly;
positive terminal padding closes by its strict grade deletion; an empty
prefix has q=11 and closes directly; the remaining case is exactly the
nonempty-prefix premise above. Source positivity and every ordinary gap are
supplied by the actual certificate and prefix equations.

The terminal numerical bound is forced by this structural classification:

\[
q\le69,\quad e\le3
\quad\Longrightarrow\quad
2S+1\le2\cdot2^3\cdot69+1=1105.
\]

`terminal_core_range` proves convergence of every positive integer in this
fixed terminal range by **kernel `decide`** on a finite hitting predicate.
113 ordinary shortcut clocks suffice; the soundness of the recursive
predicate is proved in the module. This finite base has no coverage
hypothesis, certificate selector, new axiom, or `native_decide`. It is not an
expansion of a general numerical cutoff. It is the explicit terminal case
required to discharge every exceptional motif of the universal normal form.

Finally, the checked corollary is

\[
\operatorname{ElevenIntervalStep}
\quad\Longrightarrow\quad
\forall n>0,\ B(n).
\]

The premise is visible in `collatz_of_eleven_prefix`; it has not been proved
or installed as an assumption elsewhere.

## 4. Consequence for the global symbolic attack

The latest arbitrary-carry and negative-complement results supply exact
ordinary transitions at every source gap. They still require a successful
return criterion. The present theorem gives that search one canonical
literal endpoint: every unbounded bounded-four source query can be expressed
as a nonempty prefix to 11 followed by `[1,2,3,4]`, with the same fixed tail
cancelled from all rank comparisons.

A combined ordinary-descent and source-grade argument must also retain the
original target floor. In a least-counterexample formulation, any actual
merger partner below that original target closes the branch. A later carry
endpoint may exceed the original target, so descent below that endpoint
alone is insufficient. This observation permits the already proved ordinary
descent cases to coexist with grade-funded source rewrites, while keeping
their required inequalities explicit.

Neither source-prefix exhaustion at 11 nor totality of the arithmetic carry
dispatcher proves the remaining `ElevenIntervalStep`. The exact complement
and the original target floor must still yield a funded source return or an
actual smaller ordinary merger. The new normal form replaces the arbitrary
complete-tail boundary with the one proved fixed tail above; it does not
declare that final coverage implication established.

## Verification

The module uses the repository's core-only Lean 4.34.1 environment. It was
compiled with warnings treated as errors, and its named public theorem
declarations are audited independently of their prose descriptions. The
finite terminal base is kernel reduction, while the all-length factorization,
padding deletion, grade cancellation, and residual equivalence are structural
proofs.
