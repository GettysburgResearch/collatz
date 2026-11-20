# When an ordinary meeting extends to an affine certificate

**PROPOSED, unconditional.** This note concerns the positive shortcut map
\(T(n)=n/2\) for even inputs and \(T(n)=(3n+1)/2\) for odd inputs.
It does not assume convergence of an input whose trajectory has not been
established. A *cylinder certificate* for a pair of affine arms is a pair
of fixed legal parity words that gives identical endpoint functions on
one binary parameter class, for every positive lift in that class.

The distinction matters for the current proof attempt. PR146 proves that
every prescribed parameter class for a compatible pair has a successful
subclass. That statement does not say that each fixed ordinary parameter
belongs to a successful subclass. The latter statement can already fail
for two starts known to reach 1.

## 1. The exact criterion inside the known basin

For a positive integer known to reach 1, define its stopping defect
\[
 \kappa(x)=d(x)-2a(x),
\]
where \(d\) is the first hitting time of 1 and \(a\) counts odd inputs
strictly before that hit. The identity
\[
 \kappa(x)=i-2s_i(x)+\kappa(T^i(x))                 \tag{1}
\]
holds at every clock, including after entry into \(1\leftrightarrow2\).
This invariant was independently reconstructed in PR149 and also occurs
with opposite sign in PR148; it is not new here.

Fix positive integer slopes \(a,c\) whose quotient has no prime factors other
than 2 and 3, integer offsets \(b,d\), and an ordinary parameter \(t_0\)
for which \(x=at_0+b>0\) and \(y=ct_0+d>0\) both reach 1. Put
\[
 A=v_2(a)-v_2(c),\qquad C=v_3(c)-v_3(a).
\]

**Theorem AC1.** A cylinder certificate containing \(t_0\) exists if
and only if
\[
                 \kappa(x)-\kappa(y)=A-2C.        \tag{2}
\]
The certificate's physical clock difference must be \(A\), and its
odd-count difference must be \(C\).

**Proof.** A word of length \(i\) with \(p\) odd inputs sends its
starting argument \(z\) to \((3^p z+B)/2^i\), with an integer offset
\(B\). Equality of the two affine endpoint functions forces
\[
       a3^p2^j=c3^q2^i.
\]
Unique factorization gives \(i-j=A\) and \(p-q=C\). Applying (1) at
the common endpoint proves (2).

Conversely, choose \(j\) sufficiently large, and set \(i=j+A\), so
both arms have already reached the 1--2 cycle. Because
\(\kappa(x)\equiv d(x)\pmod2\), condition (2) gives
\(d(x)-d(y)\equiv A\pmod2\). The two cycle phases at these clocks
therefore agree. Equation (1) then forces \(s_i(x)-s_j(y)=C\).
The resulting two actual words have the same endpoint at \(t_0\) and
the same slope as functions of the parameter. Their affine endpoint
functions are thus identical.

To retain their legality, take \(j\) still larger if necessary and put
\(h=i-v_2(a)=j-v_2(c)\ge0\). For every parameter
\(t\equiv t_0\pmod{2^h}\), the first starting argument agrees with
\(x\) modulo \(2^i\), and the second agrees with \(y\) modulo
\(2^j\). These congruences preserve the entire respective parity
words. Positive starts stay positive. This proves the certificate for
every positive lift. QED.

If the slopes have different prime-to-six parts, equality of affine
slopes is impossible, independently of the values of \(\kappa\).
That incompatibility is the classification already proved in PR146.

## 2. The multiplication-by-three test has ordinary exceptions

For the arms \(n,3n\), Theorem AC1 becomes
\[
      \text{cylinder certificate at }n
      \quad\Longleftrightarrow\quad
      \kappa(3n)-\kappa(n)=2,                     \tag{3}
\]
provided both starts reach 1. The clocks must be equal and the first
arm must contain exactly one more odd input than the second.

For example, \(\kappa(1)=0\), \(\kappa(3)=1\), and
\(\kappa(9)=1\). Thus neither the parameter 1 nor the parameter 3
admits such a cylinder certificate, although both corresponding pairs
meet at independent clocks. The pair 3,9 even agrees at every common
clock at least 13; its odd counts then agree as well. It consequently
fails the required odd-count difference by one.

Since \(\kappa(2^r x)=r+\kappa(x)\), all parameters \(2^r\) and
\(3\cdot2^r\), \(r\ge0\), give infinite families of these known
convergent exceptions. A larger search horizon cannot turn any of them
into a cylinder certificate for this particular pair of affine arms.

This does not reject the ordinary multiplication-by-three criterion.
That criterion permits different clocks and arbitrary pointwise
certificates. It rejects a proposed completeness argument that silently
replaces ordinary meeting by membership in an affine-success cylinder.

## 3. A finite collection of cylinders necessarily misses a progression

The shortcut formula also defines a map on signed integers. At the
signed parameter \(-1\), the first arm stays at \(-1\), whereas the
second arm follows
\[
                 -3,\ -4,\ -2,\ -1,\ -1,\ldots.
\]
Before clock 3 the endpoints differ. From clock 3 onward their odd
counts differ by two, whereas an affine certificate for \(n,3n\)
requires a difference of one. Therefore no successful cylinder can
contain the 2-adic residue of \(-1\).

**Theorem AC2.** Given any finite collection of cylinder certificates
for \(n,3n\), there is an \(H\ge1\) such that every positive parameter
\(n\equiv-1\pmod{2^H}\) is outside the collection. Adding any finite
set of pointwise terminal parameters cannot complete the cover.

**Proof.** Take \(H\) at least the precision of each of the finitely
many classes. If one class met \(-1\pmod{2^H}\), it would contain
\(-1\) at its own precision. Its word identities, being affine
identities on infinitely many positive lifts, remain identities at
the signed value \(-1\); their parity words are legal there as well.
The preceding calculation rules this out. The omitted progression
contains infinitely many positive integers. QED.

This is a restriction on a finite list of fixed certificates. It does
not rule out an adaptive proof with unbounded word lengths, a finite
program that generates such words, additional merger families, or an
unbounded but proved terminating finite-hitting procedure.

The later PR146 head `7d04c4dd756cfe495eb3eee78eba35a99085cd2a`,
[THREE_RAY_SMALLER.md](https://github.com/GettysburgResearch/collatz/blob/7d04c4dd756cfe495eb3eee78eba35a99085cd2a/research/upper-bit-mergers/THREE_RAY_SMALLER.md),
proves a stronger unbounded-clock obstruction even for a graph augmented
by all smaller tripling comparisons. AC2 is the elementary restriction
specific to finite homogeneous-cylinder tables, not a claim of priority
over that stronger result.

There is also a direct prefix statement. For \(h\ge3\) and positive
\(n\equiv-1\pmod{2^h}\), the two endpoints at clocks
\(3\le i\le h\) are
\[
 T^i(n)=\frac{3^i(n+1)}{2^i}-1,\qquad
 T^i(3n)=\frac{3^{i-1}(n+1)}{2^i}-1.             \tag{4}
\]
They differ, and clocks 0,1,2 also have unequal endpoints. Thus even
ordinary same-clock meeting needs more than \(h\) steps on this
progression. Formula (4) concerns finite prefixes of each ordinary
start; no infinite positive realization of the signed fixed point is
asserted.

## 4. The remaining complete-selector obligation

The constructive family in this packet certifies an actual smaller
ordinary partner. Together with PR146's general construction, it gives
usable successful branches of a selector. To prove Collatz by this
route one still needs a procedure that, for every fixed positive
integer greater than 1, terminates with either a smaller ordinary
partner and two legal meeting paths, or a verified finite path to 1.
The decreasing rank is the starting integer itself.

No such universal termination proof is supplied. Equations (2)--(4)
explain why increasing a fixed table or assuming that every omitted
parameter eventually enters an affine-success class is insufficient.
Neither a zero-density exceptional set nor a changing sequence of
successful ordinary lifts resolves a fixed omitted parameter.

## Sources and verification boundary

- PR146, `561d48a4d3a793a59b1cdf0406062ae1a6d47515`,
  [AFFINE_RAYS.md](https://github.com/GettysburgResearch/collatz/blob/561d48a4d3a793a59b1cdf0406062ae1a6d47515/research/upper-bit-mergers/AFFINE_RAYS.md):
  compatibility classification and arbitrary-class refinement.
- PR146, same head,
  [THREE_RAY.md](https://github.com/GettysburgResearch/collatz/blob/561d48a4d3a793a59b1cdf0406062ae1a6d47515/research/upper-bit-mergers/THREE_RAY.md):
  ordinary multiplication-by-three equivalence.
- PR149, `9dcb3b35a8e407af7635469f5643e9fa2f5a1077`,
  [persistent-defect invariant](https://github.com/GettysburgResearch/collatz/blob/9dcb3b35a8e407af7635469f5643e9fa2f5a1077/research/persistent-defect-classes/README.md):
  identity (1) and synchronization in the known basin, overlapping the
  invariant in PR148, `6ff18e4f63be8f3bece76215fcfe44d83b001d7f`.

The accompanying exact checker reconstructs positive examples, words,
slopes, offsets and lifted legality. It tests bounded instances of
AC1 and the signed obstruction. The unbounded statements above are
written proofs, not consequences of finite execution or formal proofs.
