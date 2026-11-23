# Direct source repair from the actual target's whole-word surplus

Date: 2026-11-22. **Outcome: the universal closing repair was not proved.**
This pass attacks the target-dependent splice itself. It proves a necessary
edit horizon for arbitrarily complicated repairs, then identifies an exact
failure of the attempted grade payment on a globally extremal source. It
does not extend the bounded-language classification.

## Frozen inputs

| Input | Commit | Used statement |
|---|---|---|
| PR177 | `e4ca639326bac73da8c2a698dec8a749e5efbe68` | `research/lean-exact-witness-global-20261121/JOINT_MINIMAL_COUNTEREXAMPLE.md`: simultaneous minimum source grade, maximum source at that grade, least original target, safe source floor and canonical complete word |
| PR180 | `a66a44c9bf058cd7efe1018827ddda9a13297a21` | `research/deep-machinery-20261122/ARITHMETIC_RIGIDITY.md`, §§1–4: actual first-hit clock, full target coefficient invariant, whole-source surplus and unaltered-prefix splice obstruction |
| PR185 | `980d40fc4afeaaf8f2a9256f322acf3e4568e013` | `research/central-obstruction-20261122/EXTREMAL_SOURCE_CLOCK_FAILURE.md`, §§3–4: the all-certificate maxima 1092 at grade at most G and 820 at grade strictly below G |
| PR176 | `00018ce11fa657b5f3fae072e5567a1d93184c2b` | `research/lean-global-resolvent-20261121/overview/whole/SOURCE_TARGET_INDUCTION.md`: a changed target must activate its actual paid source interval, while ordinary descent remains relative to the original target |

The old modules were read at these pins, not recompiled. The new necessary
edit-horizon theorem below is a written arithmetic proof. The finite control
script checks exact integers; it does not prove the imported all-certificate
maximality or the universal closing implication.

## 1. Retain all source and original-target resources

Let the supplied source be \(S=2^e q\), with \(1\le e\le3\), and let
its canonical complete odd word \(W\) have length \(r\) and ordinary
clock \(A\). Write

\[
P=2^A,\qquad Q=3^r,\qquad Qq+C=P,\qquad C>0.
\tag{1}
\]

The actual source first reaches one at clock \(A\) from \(q\). The
original target \(t\) obeys

\[
S+1<t\le2S+1\le16q+1,\qquad
T^{j+1}(S)\le L:=\lfloor(t-1)/2\rfloor.
\tag{2}
\]

Its \(A+1\) source states are distinct and lie below \(L\), giving
\(2A<t\). Put \(x_j=T^j(t)\) and let \(o_j\) count actual odd inputs
before clock \(j\). In a surviving least-bad query every \(x_j\ge t\).
With \(B=3t+1\), PR180's exact finite invariant is

\[
(B-j)2^j x_j\le B3^{o_j}t\qquad(0\le j\le A).
\tag{3}
\]

Since \(B-j>5B/6\), this implies both

\[
\frac56\,2^j x_j<3^{o_j}t,
\qquad
6\,3^{o_A}>5\,2^A>5\,3^r q.
\tag{4}
\]

The simultaneous induction permissions are unchanged: a strict decrease of
the complete source grade pays any *activated* child target; an equal-grade
source must be strictly larger; an ordinary merger must be with a positive
integer below the original \(t\). In particular, the surplus in (4)
does not activate a child interval by itself.

## 2. Attempt: edit a nonlocal initial block and retain an actual target suffix

Choose any cut \(0\le b\le A\). Instead of reusing the target's whole
word, permit an arbitrary altered initial block and retain only the actual
target suffix from \(x_b\) to \(n:=x_A\). Write

\[
H=A-b,\qquad z=o_A-o_b,\qquad
3^z x_b+D=2^H n.
\tag{5}
\]

Try to attach that same suffix to any supplied safe endpoint \(v\le L<t\).
A positive repaired state \(y\) at the cut must satisfy

\[
3^z y+D=2^H v,\qquad y>0.
\tag{6}
\]

The altered initial block may have arbitrary length, number of edits or
description complexity. Equation (6) is necessary before that block's
source-grade payment can even be considered. Both endpoint identities use
the exact same retained target suffix and all its ordinary clocks.

### Necessary edit-horizon theorem

**Every positive integral repair (6) satisfies**

\[
\boxed{(3t+1-b)2^A<(3t+1)3^{o_b}t,}
\tag{7}
\]

and consequently

\[
\boxed{5\,2^A<6\,3^{o_b}t,\qquad o_b\ge r-2.}
\tag{8}
\]

**Proof.** Subtract (6) from (5):

\[
3^z(x_b-y)=2^H(n-v).
\tag{9}
\]

Since \(n\ge t>v\), the difference \(x_b-y\) is positive. Coprimality
of \(2^H\) and \(3^z\) gives

\[
2^H\mid x_b-y,\qquad x_b-y\ge2^H,
\qquad x_b>2^H.
\tag{10}
\]

Multiply the last strict inequality by the positive
\((3t+1-b)2^b\), then use (3). This proves (7). The inequality
\(3t+1-b>5(3t+1)/6\) gives the first part of (8).

If \(o_b\le r-3\), then \(3^{o_b}\le Q/27\), so (1), (2) and (8)
would give

\[
5Qq<5P<6\,3^{o_b}t
\le\frac{2Q}{9}(16q+1)<5Qq,
\tag{11}
\]

where the last strict inequality is \(32q+2<45q\), valid for every
positive integer \(q\). This contradiction proves \(o_b\ge r-2\).
\(\square\)

Because the supplied source gaps are at most four, \(A\le4r\).
Therefore \(b\ge o_b\ge r-2\ge A/4-2\). Any such repair must extend
through a positive fraction of an unbounded source horizon. This applies
even if the altered block itself is not a fixed schema or finite-state
language. It is a necessary condition, not a claim that repairs extending
that far are impossible or that one then exists.

For an attempted same-grade permutation with the initial exponent retained,
the complete odd count is still \(r\). Retaining the target suffix also
forces \(o_b\ge o_A-r\), because that suffix has \(o_A-o_b\) odd events.
The total whole-word surplus demands many altered odd events, while (8)
forces their scope to reach far into the actual word. Neither count supplies
the missing integrality and grade-preserving completion.

## 3. Exact check of the proposed positive completion

The attempted next step was:

> Once the cut is late enough and a positive integral repaired state exists,
> use its certified endpoint and the target's odd surplus to complete a
> source at a permitted grade that captures the actual target at that cut.

This implication is false if justified only by the preceding finite
arithmetic and extremal-source premises. The previously published record
source makes the failure exact, and permits arbitrary new prefix complexity
in the final grade comparison.

Use PR185's all-certificate extremal source

\[
S=1092=4\cdot273,\qquad
W=[2,3,3,3,1,2,3,4],\qquad t=2047.
\tag{12}
\]

Here \(A=21\), \(r=8\), every supplied future source state is at most
\(546<L=1023\), and

\[
x_A=378350,\qquad o_A=18,
\]
\[
6\,3^{18}=2324522934
>5\,2^{21}=10485760
>5\,3^8\cdot273=8955765.
\tag{13}
\]

The exact finite calculation checks every cut \(b\in[0,21]\) and every
ordinary safe suffix endpoint of the supplied source. For \(b<18\),
(6) has no positive integer solution. At the first feasible cut,

\[
b=18,\quad o_b=15,\quad x_b=112103,
\qquad y=7,\quad v=26,
\tag{14}
\]

with the same three-odd-step suffix

\[
112103\to168155\to252233\to378350,
\qquad 7\to11\to17\to26.
\tag{15}
\]

The repaired state seven has complete odd word \([1,1,2,3,4]\).
Keeping initial exponent two gives the strictly lower-grade source
\(S'=28\): grade eight agrees and the multiplicity of grade six drops
from four to one. But the required activation is false:

\[
\boxed{x_b=112103\not\le2S'+1=57.}
\tag{16}
\]

Adding a third initial halving is not free: it introduces grade seven,
absent from the old grade, while grade eight remains equal. That particular
certificate is therefore more expensive, despite its smaller lower-grade
counts.

More strongly, PR185's written all-certificate maximality theorem states
that **every** complete powered source at grade at most the old grade is
at most 1092, irrespective of its word length, permutation, initial
exponent or terminal padding. Consequently no complicated new prefix at
any permitted grade can fix (16): every such interval has ceiling at most
2185. At every feasible cut \(18\le b\le21\), the actual target is at
least 112103. Thus the failed activation is not an artifact of choosing
the small repaired source seven.

The computation here verifies only the finite affine/physical statements
and the location of the first feasible cut. It does not infer global grade
maximality by enumeration; that is the explicitly imported all-word result.
The example is not a JointBadQuery or a Collatz counterexample: its target
first descends below 2047 at clock 58. It refutes the attempted source-clock
splice selector based on the displayed finite data, not the full mixed
induction framework with unrestricted future ordinary descent.

## 4. The first unresolved closing step

The full multiplier surplus does not pay the numerical child interval.
The exact missing inequality is

\[
T^b(t)\le2S'+1
\tag{17}
\]

for an actually complete source \(S'\) at a strictly lower grade, or at
the same grade with the permitted larger-source tie. A proof may instead
use an actual merger with a positive integer below the original \(t\).
The edited-prefix construction above guarantees neither alternative.

Equation (8) rules out short repairs before grade is considered. The
record calculation then shows that arbitrarily complicated prefix
completion, with the same original grade resource, cannot activate any
of the feasible copied-tail repairs through the whole source clock in
that example. Replacing the original \(t\) by the larger current
\(x_b\) as the induction reference would erase the very inequality that
fails; no such reset is made here.

A successful universal argument must therefore use additional actual
future target information, a different complete-word construction that
changes the retained tail as well, or another original-target merger
mechanism. No theorem guaranteeing one of those alternatives was obtained
in this pass. The positive full-surplus statement, the actual floor and
the exact complete source remain intact; their proposed conversion into
a paid universal repair is the unfinished step.
