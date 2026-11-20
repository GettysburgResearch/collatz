# Latest Mersenne five reduction: exact connection and the remaining step

**Outcome: the new reduction does not yet close the Mersenne least-failure
case.** The fixed-defect return theorem applies to actual ordinary paths;
the missing comparison here is between two different ordinary futures.
There is also a precise consequence for the new proportional lifts: their
starting shifted cores must escape every fixed finite family.

## Sources checked

- PR146, commit `fd991063721e9c157d318e40bb20131762f7d750`,
  `research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`.
- PR164, commit `6fa6b429870a9cd53cde0fc77ad64a3c3956199f`, the README
  delta, `continuation-j.md`, `continuation-negative.md`, and
  `continuation-closure.md`.
- This packet's RU2 and FD1--FD3. Their Evertse dependency remains explicit.

The PR146 least-failure height theorem is used only as the named source
interface that supplies the two convergent ordinary values below.
No new proof of that preceding theorem is asserted here.

## 1. The known and unknown values differ by exactly two

Use the latest PR146 notation

\[
e=119+162j,\quad P=2^e,\quad
X=(1024P-2573)/243,\quad h=e+1,
\]

and choose `r=2` for even `j`, `r=1` for odd `j`. Put

\[
B=3^r2^{h-r},\qquad q=(B-1)/5,\qquad
u=U(q),\qquad S=3B/2.
\]

The stated divisibility makes `q` an ordinary positive odd ternary unit.
Since `B` is divisible by four, `q=3 mod4`. Both `q` and `5q` therefore
have first division exponent exactly one. Direct calculation gives

\[
5u=S+1,\qquad U(5q)=S-1=5u-2.
\tag{1}
\]

Under the globally least adjacent-failure hypothesis at `X`, PR146 supplies

\[
q\in C,\qquad S+1=5u\in C,\qquad 5q\notin C.
\tag{2}
\]

Consequently `S-1` is the unknown nonconvergent value in the same future as
`5q`. Proving the particular comparison

\[
S+1\in C\ \Longrightarrow\ S-1\in C
\tag{3}
\]

for these `S` would finish this case. No actual path from `S-1` to `S+1`,
or to any other already certified ordinary state, is supplied by (1).
Replacing a known convergent value by that value minus two is precisely
the first unsupported inference in that attempted shortcut.

The first target shift is `5q+1=B`, and the next is `S`; both have core
one in the pool `{2,3}`. More generally the initial valuation-one run
preserves this core. This known run is exactly the all-valuation-one
degeneracy excluded by RU2. Its length may be large, but it contains no
defect to which FD2 could attach a return count.

After that run, neither the supplied convergence witnesses nor the
least-failure height theorem proves a return of the unknown future to a
fixed finite core family with a bounded number of defects. FD2 says that
only finitely many such bounded-defect returns can exist; it does not
force one to occur. A hypothetical bad future may leave, stay outside,
or return with increasing defect counts. These possibilities do not
contradict RU2, FD2, or the excursion-frequency lower bound.

One may choose a fixed prime pool containing all primes from the two
known certificates for this particular source. That produces a finite
reference set. It still gives no containment or frequent-return theorem
for the distinct future of `5q`.

## 2. The strengthened PR164 domains do not cover this parameter

For this family the adjacent parameter is

\[
k=(X-1)/128=2m,\qquad m=(4P-11)/243.
\]

Since `e>=119`, reduction modulo 16 gives `m=7 mod16`. In particular
`k` is even. Three exact exponent-two steps take the upper arm
`256m+1` to `108m+1=4(27m)+1`, and take the lower arm `128m+1`
to `54m+1`. Removing the ordinary `J(n)=4n+1` equivalence shows that
the required comparison is `P(m)`, not `Q(m)`.

The latest rules have the following exact mismatch:

- W512-070 and W512-072 require the adjacent index to be `-1 mod2048`,
  hence odd. The index `k=2m` fails that condition.
- W512-082 requires the adjacent index to be `3 mod2^119`, hence odd.
- W512-081 concerns `P(m)` but requires `m=1215 mod16384`; this would
  give `m=15 mod16`, whereas the present `m` is `7 mod16`.
- W512-080 concerns `Q(m)`, with `m=95 mod256`, and therefore does not
  supply this `P(m)` call. Its parameter congruence also gives
  `m=15 mod16`.

These are checks of the advertised domains, not a claim that no further
composition or unbounded adaptive transfer could work. The conditional
global closure arguments in `continuation-closure.md` assume all `P`
and `Q` bridges. Importing that assumption here would include the very
comparison still being sought.

## 3. A rigorous consequence for the proportional lifting construction

Fix one ordinary supplied comparison `(q,5q)` and one seed from the new
lifting theorem, with shortcut clock `L` and common odd count `p>=1`.
It produces infinitely many distinct starts `x_b` with

\[
T^L(5x_b)=2^b5q,\qquad T^{L+b}(5x_b)=5q.
\]

For all allowed `b>=2`, the actual accelerated path from `5x_b` to
`5q` has exactly `p` odd transitions and contains a defect: the final
division includes the `b` displayed halvings. Fix a finite prime pool
`P_0` containing 2 and 3, write `s=|P_0|`, and fix any finite set `Q_0`
of starting shifted cores. The terminal shifted core
`R_{P_0}(5q+1)` is fixed. RU2 therefore bounds the number of such lifts
with starting core in `Q_0` by

\[
|Q_0|\bigl(2^{35}(p+2)^2\bigr)^{(p+2)^3(s+1)}.
\tag{4}
\]

Distinct starts give distinct actual paths. Hence the starting shifted
cores of these lifts eventually leave every fixed finite family:

\[
R_{P_0}(5x_b+1)\longrightarrow\infty
\]

along the increasing allowed exponents. FD3 also gives qualitative
finiteness by taking the finite union over defect counts `1,...,p`,
while RU2 supplies the explicit count (4).

Thus producing infinitely many lifts of one hypothetical failed
comparison does not violate shifted-core finiteness. The construction
necessarily moves through unbounded shifted cores. This is an exact
boundary on the proposed use of fixed-defect recurrence; it neither
constructs a Collatz counterexample nor rules out an unproved stronger
source-preserving transfer.

## Required additional statement

To close the current survivor by this route, one still needs an actual
ordinary merger or a proved directed transfer such as (3), or a theorem
forcing the unknown future to have more bounded-defect returns to a fixed
finite core family than FD2 permits. The current known certificates,
parameter contractions, and lower-frequency estimates supply none of
these statements.
