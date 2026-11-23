# A canonical source confined below the original target

## Proved global selection theorem

`lean/Collatz/RootedSourceFloor.lean` proves an unconditional source-selection
statement for **every target t at least 177**. Put

\[
L=\left\lfloor\frac{t-1}{2}\right\rfloor.
\]

There exist an even source S, an exact initial exponent `1≤e≤3`, an odd u,
and a **nonempty** literal prefix P over gaps 1 through 4 such that

\[
\begin{gathered}
S=2^e u,\qquad
\operatorname{Prefix}(u,P,11),\qquad
\operatorname{Certificate}(u,P[1,2,3,4]),\\
L<S\le t-1,\qquad t\le2S+1,\\
\boxed{\forall j\ge0,\quad T^{j+1}(S)\le L.}
\end{gathered}
\]

The theorem is `source_for_every_target`. It assumes no convergence or
descent statement for t. Its source is an actual state on a supplied known
path to 11, and its complete literal certificate is returned explicitly.

For `t≡3 mod4`, `residual_source_for_target` strengthens the location to

\[
S+1<t\le2S+1.
\]

Thus it supplies exactly the remaining low-valuation interval shape,
together with the stronger bound on every future ordinary source state.

## 1. Why every target has such a source

The preceding bounded-four normal-form module proves cofinal nonempty
prefixes ending at 11. Choose a known source q>L with one such supplied
prefix W. The fixed complete tail from 11 has ordinary path

\[
11,17,26,13,20,10,5,8,4,2,1,
\]

followed by the ordinary 1,2 cycle. Its maximum is 26.

Since `L≥88`, the complete chosen path starts above L and eventually stays
below it. Select its **last** ordinary state S above L. It cannot be odd:
an odd positive state has a larger next shortcut state. Therefore S is even,
and its next state is S/2≤L. Hence

\[
L<S\le2L.
\]

Every odd gap of W is at most four. After an odd source edge
`3r+1=2^a u`, its ordinary intermediate even states are
`2^(a−1)u,...,2u`. Consequently S has the form `2^e u` with

\[
1\le e<a\le4.
\]

The source after its e initial halvings follows the literal unused suffix
of W to 11. If that suffix were empty, u would equal 11, and
`S≤2^3·11=88≤L`, a contradiction. This explains both thresholds used in
the proof: 26 is the actual peak of the fixed 11 tail, and 88 excludes a
bare power of two times 11. The target condition `t≥177` gives `L≥88`.

The Lean proof does not assume a maximum or last crossing exists in an
unverified orbit. `safe_or_cut` is a structural induction on the finite
supplied prefix. For every such prefix it proves either that the full
future orbit is below L or that it contains an exact `FloorCut`.
`rooted_floor_cut` rules out the first alternative using q>L.

## 2. The entire original finite path is retained

A `FloorCut q L W` contains

\[
W=F\mathbin{+\!+}[a]\mathbin{+\!+}P,
\]

together with

\[
\operatorname{Prefix}(q,F[a-e],2^e u),\qquad
\operatorname{Prefix}(u,P,11),\qquad 1\le e<a\le4.
\]

The first prefix executes the original source through gap a only as far as
the selected even state. The e remaining halvings are retained in the
child source certificate. No gap is guessed and no independently chosen
certificate is substituted.

`cut_ordinary_clock` proves the actual ordinary clock

\[
T^{\sum F+a-e}(q)=2^e u.
\]

`cut_clock_decomposition` proves

\[
\sum W=(\sum F+a-e)+e+\sum P.
\]

`cut_future_bound` bounds every later ordinary state of that same original
path. The formal predicate `Safe n L` means `∀k, T^k(n)≤L`; its proof here
comes from the finite supplied prefix and the explicitly closed fixed tail.

## 3. The original target floor makes cone returns strictly decreasing

Now suppose `t≡3 mod4`. Then `L=(t−1)/2` is odd. An orbit confined to
`[0,L]` cannot visit L: its next odd shortcut would exceed L. Thus every
state of a safe orbit is strictly below L. This elementary observation is
`safe_strict`.

If v is any odd literal source endpoint after the selected source, both v
and T(v) remain safe. Therefore

\[
3v+1=2T(v)\le2L-2,
\qquad
3v+2\le2L-1=t-2.
\]

It follows that every return satisfying the repository's wider odd-source
cap is an **actual descent below the original target**:

\[
0<z\le3v+2\quad\Longrightarrow\quad z<t.
\]

`original_target_cap_descent` proves this for arbitrary literal
source-prefix consumption. Intermediate target carries are allowed to
have exceeded t; the returned endpoint is compared with the original t.

`target_prefix_cap_closes` adds an actual ordinary target prefix from t to
z. The resulting descent closes under ordinary strong induction on t.
It proves positivity from the actual target path and does not demand a
new source-rank decrease at this terminal step.

### Capture paid by the gap just consumed

There is also an all-gap version. Suppose a safe source state n has

\[
3n+1=2^a u,
\]

and a retained initial exponent e satisfies `e<a`. The padded source
`2^e u` is itself an actual state reached after `a−e` ordinary clocks, so
it is safe. Hence

\[
z\le2(2^e u)+1\quad\Longrightarrow\quad z<t.
\]

This is `consumed_gap_cap_descent`. It has **no bound on a or e**. The
funding gap must be the one just consumed; a larger gap removed much
earlier does not by itself make its maximum padding an actual state of
the current source orbit.

## 4. What the new invariant permits

The source-selection theorem is global and unconditional. It provides a
canonical bounded-four source for every target in the stated range, with
the exact original finite path and a complete source certificate. It also
proves compatibility between ordinary target descent and a broad class of
the existing carry-return cones.

Literal source-prefix consumption preserves the floor invariant. An
arbitrary cofinal source replacement need not preserve it; the replacement
would require its own bound before these floor corollaries could be used.
Likewise, the selector is not a license to reset the source grade freely
in the middle of a grade induction.

The remaining totality statement is that the required actual target carry
reaches one of these return cones, another justified smaller merger, or a
compatible lower-grade query. Neither existence of the selected source nor
exhaustion of its finite supplied prefix establishes that return. No such
universal carry-return premise is added as an axiom or asserted as proved.

## Verification

The module uses the core-only Lean 4.34.1 package and the existing
`BoundedFourNormalForm` result. The source selector, exact clock splitting,
whole-future bounds, and strict original-target descent are structural
proofs. The fixed 11 orbit is checked as a finite forward-closed set. No
numerical search threshold, `sorry`, new axiom, or `native_decide` is used.
