# A thin ordinary set survives all three coverage shapes

**Exact logical control; not a Collatz counterexample.** The new ordinary
constructions give complete ternary subprogressions, every parameter of the
form `b^(2^2956)`, and density-one coverage in each geometric sequence, with
an error uniform in the base and in translated exponent intervals. Those
three shapes of coverage alone cannot imply that every parameter is covered.
This can be checked on explicit ordinary integers, without a completion or
an uncountable exceptional set.

Let

\[
 E=\{2^{3^k}:k\ge0\},\qquad S=\mathbb N\setminus E.
\]

The set `E` is infinite. Nevertheless `S` has all the following properties.

1. **Every ternary class contains a whole successful subclass.** For every
   `a,h` there are `H>=h` and a residue `r` with `r=a (mod 3^h)` such that
   every nonnegative `m=r (mod 3^H)` belongs to `S`.
2. **Every square, and hence every `b^(2^2956)`, belongs to `S`.**
3. **Every geometric sequence has at most logarithmically many failures
   in any translated exponent interval.** Uniformly in all integer bases
   `b>=0` and all intervals `I` of `N>=2` consecutive nonnegative integers,

   \[
   \#\{n\in I:b^n\notin S\}\le1+\log_3 N.
   \]

   We take `0^0=1`. This is stronger than an error
   `C N/sqrt(log(2N))` for an absolute constant `C`.

For the first assertion, the elementary lifting identity gives

\[
 v_3(2^{3^k}+1)=k+1.
\]

If `a` is not `-1 (mod 3^h)`, its class contains at most one member of `E`:
the valuation of `a+1` fixes `k`. A further ternary digit can avoid that
one integer. If `a=-1 (mod 3^h)` and `h>=1`, two of the three children have
valuation exactly `h`; only one can contain the possible member
`2^(3^(h-1))`. Choose the other child. At `h=0`, the class `0 (mod 3)`
already avoids `E`. This proves the whole-subclass assertion, including
classes near the ternary limit `-1`.

The second assertion follows because every member of `E` has odd binary
valuation `3^k`, whereas a positive square has even binary valuation. Zero
is outside `E` as well.

For the third, `b^n=2^(3^k)` with `n>0` forces `b=2^d` and `dn=3^k`.
Thus `d=3^r` for some `r>=0`, and the successful equality occurs only at
exponents `n=3^(k-r)`. If there are `t` such exponents in an interval of
`N` consecutive integers, the difference between the largest and smallest
is at least `3^(t-1)-1` and at most `N-1`. Therefore
`t<=1+log_3 N`. The bases zero and one and the exponent zero add no failures.

This control does **not** assert that `E` contains a bad Collatz parameter,
or that it satisfies the remaining dynamical constraints in
[UnconventionalProposal.lean](UnconventionalProposal.lean). It identifies
the precise limitation of combining the three coverage conclusions as
set-theoretic statements. To exclude an original least defect, the next
argument must use an additional property of its actual orbit, or prove
pointwise coverage at that specific ordinary parameter.
