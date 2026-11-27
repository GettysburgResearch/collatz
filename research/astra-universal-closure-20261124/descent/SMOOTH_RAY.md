# An all-clocks test for affine meetings on one smaller tower

**PROPOSED, with an ordinary counterexample to unrestricted affine coverage.**
Use the shortcut map and the [minimum-core premise](../global/SmoothCore.lean).
At an exit write \(b=3^m a-1\), with odd \(a<w\). Every
\(2^i3^ka\) is good under the minimum-core hypothesis. A possible proof
would physically connect \(b\) to this smaller tower by an identity of
affine path formulas in \(a\). The residue exclusions in the minimum-core
theorem do exactly this on their stated inputs.

Here is an arithmetic criterion for this specific kind of identity when
\(b\) itself is a convergent control. Let \(H(x),O(x)\) count shortcut
steps and odd inputs through the first hit of 1, and put \(D(x)=H(x)-2O(x)\).
Then the following are equivalent for \(k\ge0\).

1. The two affine path formulas from \(b\) and \(c=3^k a\) agree at
   an actual common clock. Equality includes both slope and intercept.
2. \(c\) converges and \(D(c)-2k=D(b)-2m\).

To see necessity, if \(p_b,p_c\) are the numbers of odd inputs up to
clock \(t\), the slopes are equal precisely when \(m+p_b=k+p_c\).
For any convergent \(x\),
\[
 D(x)=D(T^t x)+t-2p_x .
\]
This identity also holds after hitting 1, since the contributions include a
balanced two-step cycle there. Subtract at a common value to obtain the
criterion. For sufficiency the displayed equality implies that
\(H(c),H(b)\) have the same parity, so both orbits are at 1 at the later
of these two hitting times. The identity for \(D\) then gives equality
of slopes. Equal values and equal slopes give equal intercepts.

Leading powers of two and unequal hitting clocks do not enlarge this
particular set of affine identities. Remove the actual \(i\) initial
halvings at \(2^i3^k a\); the affine intercept is zero throughout them.
At the next clock the intercept is \(+1/2\) because \(c\) is odd.
Starting at the even input \(b\), its intercept goes from \(-1\) to
\(-1/2\) in one clock. On either arm the numerator of the reduced dyadic
intercept stays odd from then on, so its denominator doubles each clock.
Equality of intercepts forces equal clocks after removing the leading
halvings. Neither a zero-clock intercept nor an initial zero intercept
can meet the other arm.

There are only finitely many candidate powers to test on each convergent
control. On the actual first-hitting path
\[
 2^{D(c)}
 =c\prod_{z\text{ odd before the hit}}\frac{3+1/z}{4}
 \le c .
\]
Consequently any affine meeting forces
\[
                 (4/3)^k\le a\,2^{2m-D(b)} .
\]
This exclusion of larger \(k\) needs no convergence hypothesis on
unexamined powers: convergence would follow if one met \(b\).

The finite checks below use \(2^m a-1=3^r w\), with \(3\nmid w\) and
\(a<w\). Define \(e=v_2(b)\).

| \(m,a\) | \(r,w\) | \(b,e\) | Required \(D(c)-2k\) | Eligible \(k\) | Attained values at eligible powers |
|---|---|---|---:|---|---|
| 4, 1 | 1, 5 | 80, 4 | −2 | 0–4 | 0, −1, −3, −18, −4 |
| 2, 1081 | 1, 1441 | 9728, 9 | 7 | 0–7 | −10, 4, −15, 4, −5, −3, −3, −13 |
| 5, 20153 | 3, 23885 | 4897178, 1 | −17 | 0–75 | The replay excludes −17 at all 76 powers. |
| 5, 149051 | 3, 176653 | 36219392, 9 | 2 | 0–36 | The replay excludes 2 at all 37 powers. |

In particular the exact exponent-three merger in the minimum-core argument
does not extend to every \(e\equiv3\pmod6\) merely by allowing affine
paths of arbitrary length on the same smaller tower. All four controls
themselves converge. They exclude a universal identity inferred from the
source arithmetic alone. They leave open pointwise meetings, other smaller
bases, and arguments that use the hypothetical bad label essentially.

[Exact finite replay](check_smooth_ray.py)
