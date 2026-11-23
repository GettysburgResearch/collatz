# Independent review of the full-cycle product control

23 November 2026. Reviewer: the infinite-optimizer agent, separate from
the cycle-construction author. **PASS for Sections 2–4 only.**

Frozen source: `checkpoint17_cycles/CYCLE_PRODUCT_TRANSFER_ATTEMPT.md`,
SHA-256 `61e24999019cde59a10bed34ded33b2b4b7647b5d6d42ba28398b94e911d01a9`.
I reconstructed the proofs from the displayed definitions. This review
does not certify the external incidence or energy literature in Section
1, and it does not claim a new integer-cycle exclusion. No finite census
is needed for the assertions reviewed here.

## 1. Shifted valuations imply multiplicative Sidon

For a proposed product equality, a common index forces equality of the
other indices, because all states are positive and distinct. Otherwise
the two unordered pairs are disjoint. Their largest index L cannot occur
twice: its square exceeds the product of any two smaller positive states.
It therefore occurs once. Set `s=v_2(n_L+d)`. Strict decrease of the
shifted valuations gives, modulo `2^(s+1)`,

`n_L = 2^s-d` and every other participating state `n_j = -d`.

The product containing L is `d^2-d*2^s`; the other is `d^2`.
These residues differ since d is odd. This includes a repeated index
in the smaller pair and supplies the stated Sidon property, including
diagonal products. Positivity is used in excluding the largest square;
the proof does not silently replace integer order by residue order.

## 2. The complete one-rise odd-state set

For `p>=2`, `A>p`, and `2^A>3^p`, the quantities

`D=2^A-3^p`, `C=3^p-2^p`, and `h=2^(A-p)-1`

are positive, with D and h odd. The displayed numerators
`N_i=2^(p-i)*3^i*h-D`, for `0<=i<p`, satisfy

`N_0=C`,
`N_(i+1)-N_i=2^(p-i-1)*3^i*h`,
`3N_i+D=2N_(i+1)` for `i<p-1`, and
`3N_(p-1)+D=2^(A-p+1)N_0`.

Thus they are positive, odd, and strictly increasing. The gap exponents
in these identities are exact, since the receiving numerators are odd.
After the last odd shortcut step the state is `2^(A-p)*t`, where
`t=C/D`; exactly `A-p` ordinary halvings return to t. Reduction by an
odd common denominator factor cannot change any two-adic parity or gap.

The odd states are distinct, so their odd period is p. The shortcut
parity word has one cyclic run of ones and one of zeros and is primitive;
its shortcut period is A. The odd portion increases and the even portion
decreases to t, so t is the minimum of the entire shortcut cycle.

Finally, `v_2(N_i+D)=p-i` holds exactly. Applying the criterion to the
whole numerator set, then dividing all states by the same nonzero D,
preserves every product equality. Hence all `p(p+1)/2` unordered
products are distinct. The ordered energy is
`p+4*p*(p-1)/2 = 2p^2-p`. Both formulas hold for every allowed pair
of parameters, without an asymptotic or sampling qualification.

## 3. Arbitrary floor and period with a nontrivial reduced denominator

Write `alpha=log_2(3)`. Unique factorization proves its irrationality.
For fixed real `H>=1`, the desired condition on
`2^ceil(p*alpha)/3^p` is equivalent to the nonempty open fractional-part
interval

`1-log_2(1+1/(2H)) < {p*alpha} < 1-log_2(1+1/(4H))`.

The stated elementary density proof gives visits above every prescribed
index: a sufficiently small positive fractional part of a signed
multiple yields a finite circular net; translating the net far enough
in the integer index makes all indices positive and arbitrarily large.
The possible negative sign of that small-step index causes no problem,
since the net is finite. Therefore one can impose the requested period
bound together with `(2/3)^p<1/2` and `2^p>4H+1`.

The exact expression

`t=(1-(2/3)^p)/(2^A/3^p-1)`

then gives the strict bounds `H<t<4H`. The earlier minimum calculation
makes every shortcut state exceed H. In addition,

`t+1=2^p*(2^(A-p)-1)/D`

has rational two-adic valuation p because D and the parenthesized
factor are odd. If t were an integer, the positive integer `t+1`
would consequently be at least `2^p`, whereas
`t+1<4H+1<2^p`. This contradiction proves `D` does not divide C,
equivalently that the fully reduced denominator is greater than one.
It is not merely a statement about an unreduced denominator.

These controls have arbitrarily large least period and arbitrary positive
floor, and the full odd-state set is maximally multiplicatively Sidon.
They do not provide a positive integer cycle. Their valid scope is to
test any proposed product-growth consumer that omits the complete
integrality condition.
