# Route 3: a proved repayment across a genuinely adverse mode change

**Status: PROPOSED pending independent mathematical review.** The positive
results here cross a mode mismatch that the parent alignment theorem did not
handle. They do not establish a complete cover of ordinary inputs. The
precision does not force the required future parity word; that remains a
real condition of every certificate.

Use the same R, z_a, A and w_a=1^a0 as pass 4. Put

    P_a=2^(a+1), Q_a=3^a, d_a=Q_a-P_a, c_a=Q_a-2^a,
    g_a(n)=(Q_a n+c_a)/P_a,
    rho_a=Q_a/P_a, kappa_a=Q_a/P_a^2.

For a>=2, g_a expands positive numbers, d_a,c_a are positive, and
r_a=c_a/d_a lies in (1,5]. The component rank still contracts under its own
word: R_a(g_a^k(n))=kappa_a^k R_a(n).

## 1. T-A3-1101: exactly what a different mode does to a stored resonance

For a,b>=2, a!=b, define

    Delta_ab=d_b c_a-d_a c_b=2^a 3^b-2^b 3^a.

Direct affine composition gives

    z_b(g_a^k(n))
      = rho_a^k z_b(n)
        + Delta_ab*(Q_a^k-P_a^k)/(P_a^k d_a).          (1)

Here v3(Delta_ab)=min(a,b), d_a and P_a are ternary units, and Q_a^k-P_a^k
is also a ternary unit. If v3(z_b(n))=t>min(a,b), then the first term has
valuation t+ak and the second exactly min(a,b). They cannot cancel. Hence

    v3(z_b(g_a^k(n)))=min(a,b).                        (2)

This is an exact destruction of the old high ternary precision at a mode
change, not a statement that the rank necessarily falls there. It explains
why the parent alignment certificate could not be iterated automatically.
After a further legal w_b^ell,

    v3(z_b(g_b^ell g_a^k(n)))=min(a,b)+b*ell.           (3)

That newly accumulated precision can repay the old loss. The proof below
quantifies the required amount while retaining the SAME ordinary rank.

## 2. T-A3-1102: an all-parameter two-mode repayment theorem

Fix a,b>=2, a!=b, k>=1, and t>=2b+4. Suppose one positive ordinary n realizes
w_a^k followed by w_b^ell, satisfies v3(z_b(n))=t, and

    ell>=t+ak+4.                                      (4)

Then

    R(g_b^ell g_a^k(n)) < R(n)/16,                     (5)

while both block groups increase the ordinary number. This is not the parent
aligned case: the initial active mode is a, but the uniquely minimizing
component is b!=a. If the two groups are the exact maximal modules, (5) is
a two-A-step certificate. A longer second module only improves the component
bound, so a prefix meeting (4) also suffices.

### Proof

The high ternary precision t>=2b+4 makes b the unique minimizing component of
R at n, by the parent's elementary high-precision minimum lemma. Its proof
does not depend on the source's dyadic mode. Briefly it forces h(n)=b,
v3(n)=0,v3(n-1)=1 and, if b>=3,v3(n+5)=2. The fixed alternative components
are at least n^2/12, whereas R_b(n)<4*3^(2b-t)n^2<=4n^2/81<n^2/12.
The collapse theorem excludes every other moving index.

Write y=g_a^k(n). Since g_a^k(n)+r_a=rho_a^k(n+r_a),

    z_b(y)/z_b(n)
       <=rho_a^k*(n+max(r_a,r_b))/(n+r_b)
       <=(7/3)rho_a^k <3rho_a^k                       (6)

for n>=2. Equations (2), (3), and the exact component contraction yield

    R_b(g_b^ell(y))/R_b(n)
       <9 rho_a^(2k) 3^(t-min(a,b)) kappa_b^ell.

Use rho_a<2^a, kappa_b<1/4, 3^t<4^t and 9<16. The last expression is
strictly less than 16*4^(ak+t-ell), which is at most 1/16 by (4).
Since R(n)=R_b(n) and the final envelope is at most its b component, (5)
follows. In fact (3) is now high enough to make b the final unique minimum
too. All comparisons are exact; no asymptotic source size is assumed.

### Ordinary nonvacuity at every parameter tuple

Prescribe the finite shortcut word w_a^k w_b^ell 0. Its unique dyadic cylinder
sets the first two maximal modes and counts exactly: a!=b ends the first
group and the final even endpoint ends the second. Independently impose

    z_b(n)=3^t mod 3^(t+1).

As d_b is a unit modulo 3, CRT supplies infinitely many positive ordinary
sources in one arithmetic progression. Each has the exact stated precision
and physical word. The initial source changes with the parameters; no
infinite ordinary trajectory is inferred from this finite construction.

## 3. T-A3-1103: a sharper explicit family, with an unbounded COMMON-rank spike

For every t>=3, consider any positive ordinary n satisfying

    v3(n+5)=t,
    n realizes 1110 (110)^t.

Let y=g_3(n)=(27n+19)/16 and m=g_2^t(y). Then

    n<y<m,
    R(n)=(n+5)^2/3^t,
    R(y)=(y+5)^2/9 > 2*3^(t-2) R(n),                  (7)
    R(m)/R(n) < (81/256)*(27/64)^t < 1/4.             (8)

Thus the SAME common integer rank has an arbitrarily large intermediate
increase and then a proved net decrease. This is not merely a rise in one
nonminimizing component. If the actual second maximal module has ell>=t,
its endpoint obeys the same bound (8).

### Proof of the two exact minima and the spike

Put Z=n+5. Then Z>=3^t and n>=22. Its ternary valuations are
v3(n)=0, v3(n-1)=1, h(n)=2. The rank components are n^2,(n-1)^2/3,Z^2/3^t.
For n>=22 and t>=3 the last is strictly smallest; compare its ratio to the
second with (1/9)*(27/21)^2=9/49 and to the first with 27/484.

At y the four numerator valuations are respectively

    v3(y)=0, v3(y-1)=1, v3(y+5)=2, v3(z_3(y))=5,
    h(y)=3.

These follow by substituting y=(27Z-116)/16 and t>=3. As y>=10,
(y+5)^2/9 is smaller than y^2,(y-1)^2/3,(11y+19)^2/243. For the last
comparison, 11y+19>6(y+5) and 36>27 suffice. Hence both minima in (7) are exact.

Moreover

    R(y)/R(n)=3^(t-2)*[(27-36/Z)/16]^2.

Since Z>=27, its square factor is at least (77/48)^2>2, proving the spike.
The factor is strictly less than (27/16)^2. Each subsequent 110 multiplies
the b=2 component rank by 9/64, yielding (8). The final envelope can only
improve this bound. For t>=1, (81/256)*(27/64)^t<1/4; the stronger t>=3
hypothesis was needed for the exact initial and intermediate minima.

### One explicit ordinary source

At t=3, prescribing the final parity bit 0 gives the progression containing

    n=461479,
    A(n)=778747,
    A^2(n)=1108804,
    R: 7887684528 -> 67383853056 -> 187388721.

The first module is 1110; the second is exactly three copies of 110. The
number grows throughout both block groups, the common rank increases by
more than a factor eight, then ends below one fortieth of its initial value.
The complete progression has modulus 2^(3t+5)*3^(t+1); CRT, not a finite
sample, establishes all its positive lifts. The experiment checks two lifts
for every t=3,...,24, together with 28 general parameter tuples from Section 2.

## 4. A sound end-to-end assembly and its unproved coverage condition

Use Phi from PLATEAUS_AND_SOURCES.md. A certificate may use a nonincreasing
single A step, a two-mode block satisfying Section 2 or 3, or any exactly
replayed lower-Phi merging diagram. Every accepted certificate strictly
lowers the same nonnegative integer Phi. Each block is physically finite;
convergence is preserved by a merging diagram. If such certificates covered
every source n>1 through a PROVED TOTAL selector, well-founded descent would
establish Collatz and exclude all nontrivial cycles.

That cover is not proved. High ternary precision does not force the desired
future dyadic word: CRT permits other next modes at the same precision. For
example n=103 has v3(n+5)=3 and active mode 3, but A(103)=175 has active mode
4, not 2. Independent CRT choices give such alternatives at arbitrarily high
precision. Thus the implication "deep inactive resonance forces its repayment
word" is false without additional hypotheses. The theorem is a certificate
for a specified infinite ordinary family, not a universal mode-selection law.

The mass route's induced operator remains another full closing route. The
power-weight failure in INDUCED_MASS.md does not refute this repayment family,
and the repayment family does not repair the entire operator by itself.
The exact outstanding task is a physically complete treatment of all remaining
unsafe transitions, rather than another iteration of the proved favorable
family without checking its hypotheses.
