# Optional refinement: every counted marked source can be a ternary unit

This appendix strengthens the source set in
`MARKED_PREDECESSOR_POPULATIONS.md`. It is unnecessary for the finite survivor
criterion there. The simpler odd-source theorem and its proof remain valid
unchanged.

**Conclusion.** There is an absolute `gamma_unit > 0` such that every positive
ternary-unit target `a` has, in arbitrarily large octaves, a finite set of
distinct **odd ternary-unit** predecessors satisfying

\[
 2^d\le n,\qquad (d+1)(n-2^d)\le10\,2^d,
 \qquad |P|\ge\gamma_{\rm unit}\frac{2^d}{(d+1)^2},
\]

with one common ordinary shortcut clock to `a`, at most `15(d+1)` after
discarding finitely many initial choices.

The selection below uses the **actual integer target**, including its residue
modulo `3^(s+1)`. It is not asserted to depend only on the target modulo `3^s`.

## A. Retain a logarithmic bound on the final exponent

In the controlled-floor construction, also retain only words whose final
exponent is at most

\[
                  K_h=\lceil4\log_2(h+2)\rceil,
\]

where `h` is the final full word length. Before the one-exponent cylinder
spreading, the last letter is the last letter of the independent terminal
tail. For a positive geometric letter,

\[
                         \Pr(a>K_h)=2^{-K_h}\le(h+2)^{-4}.
\]

The normalized `L1` loss caused by removing these tail words is at most this
probability, whether or not one has already removed the bad-total words.
The prefix operator in Section 2 of the main note has norm at most

\[
                 (d_N+1)(B_*+3^k\rho^{d_N})=O(h).
\]

Thus the added pointwise loss is `O(h(h+2)^(-4))=o(1)`. The joint rejection
of a bad total or an oversized last letter can equivalently be bounded by
the sum `2 exp(-k/1200)+2^(-K_h)`. The same positive cylinder survives with
another fixed positive floor. Prepending the bounded exponent used for
spreading does not change the last exponent.

Consequently there are constants `c_last > 0`, `B >= 1`, `E >= 1`, and `h_0`
such that, for every `h >= h_0` and every unit residue `r modulo 3^h`, the
finite controlled word family has normalized mass at least `c_last`, total
in `[1.9h-E,2.1h+E]`, real offset at most `B`, and final exponent at most
`K_h`. The constants are independent of the residue and of the integer
target later chosen to represent it.

## B. Apply at one extra depth, then delete the final inverse step

Fix an **actual positive odd unit integer** `b`, and apply this refined floor
at depth `h=s+1` to `b modulo 3^(s+1)`. Every contributing word is a genuine
positive odd inverse path from `b`, by the legality argument in Section 1 of
the main note. Write it as `w=v*t`, with `|v|=s` and `1 <= t <= K_(s+1)`.

The source reached after the prefix is

\[
                      x_v=(b-\beta_v)/\omega_v.
\]

It is a positive odd integer. The last inverse step is the integer
`(2^t x_v-1)/3`, so `2^t x_v = 1 (mod 3)` and therefore `3` does not divide
`x_v`. This is the precise reason that truncating the final step gives a
unit source.

Let `V_s(b)` be the **set** of prefixes arising this way; repeated appearances
of the same prefix are counted once. Its definition depends on admissibility
of the full word at `b modulo 3^(s+1)`. Two targets congruent modulo `3^s`
need not give the same unit-source selection.

The normalized weights obey

\[
                        \omega_{v*t}=\omega_v\,3\,2^{-t}.
\]

For one fixed actual unit source `x_v`, permissible final exponents have one
fixed parity. Explicitly,

\[
 \sum_{\substack{t\ge1\\2^t x_v\equiv1\ (3)}}3\,2^{-t}
 =\begin{cases}
 3\sum_{j\ge1}2^{-2j}=1,&x_v\equiv1\pmod3,\\
 3\sum_{j\ge0}2^{-(2j+1)}=2,&x_v\equiv2\pmod3.
 \end{cases}                                                   \tag{B.1}
\]

Additional word, total, and last-exponent restrictions can only reduce these
nonnegative sums. Hence

\[
 c_{\rm last}
 \le\sum_{v\in V_s(b)}\omega_v
          \sum_{\substack{t:\v*t\text{ retained}}}3\,2^{-t}
 \le2\sum_{v\in V_s(b)}\omega_v,
\]

which gives

\[
                     \sum_{v\in V_s(b)}\omega_v\ge c_{\rm last}/2.
                                                                    \tag{B.2}
\]

This is a uniform mass bound at the supplied actual target. It is not a
claim of conditional mixing modulo `3^s`.

Every retained prefix satisfies, with `E'=E+2`,

\[
 1.9s-E'-K_{s+1}\le A(v)\le2.1s+E',\qquad
               0\le\beta_v\le\beta_{v*t}\le B.         \tag{B.3}
\]

The loss in the lower total bound is only `O(log s)`. There are at most `2s`
possible totals in (B.3) once `s` is large.

## C. Run the same marked-band construction

Use the rotation-selected depth `q <= s < 2q` and the actual positive odd
unit parent `b=a_s` of the original supplied target, exactly as in Sections
4--5 of the main note. All prefixes in `V_s(a_s)` have the same bounded-offset
formula and the same one-sided phase correction. Thus the constant-10
section argument is unchanged.

The lower total endpoint has moved by `O(log s)`, which does not affect the
eventual height bounds `s/5 <= d+1 <= s`. Pigeonholing (B.2) among at most
`2s` totals supplies a fixed total with mass at least `c_last/(4s)`.
Its distinct sources are all units, all lie in one octave, and all reach
the original target at the same ordinary clock. The count in Section 6
therefore gives, for example,

\[
                      \gamma_{\rm unit}=c_{\rm last}/(6500C),
       \qquad C=8(1+3B).
\]

The source-unit requirement costs a fixed constant in the final population
bound. No global upper estimate or convergence statement is obtained from
this refinement alone. The upper total bound changes by only a fixed
constant, so `A+e_s <= 3s <= 15(d+1)` still holds at sufficiently large
selected depths, as in the main note.
