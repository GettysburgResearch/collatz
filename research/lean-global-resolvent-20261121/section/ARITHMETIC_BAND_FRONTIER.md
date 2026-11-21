# Arithmetic attack on the forward dyadic section

Source: PR 173 at fa0c9e2a2851e6324391e39c17afcb5913185aec.

This is an analysis checkpoint, not a proof of Collatz. No unconditional descent
for every section point was obtained.

## Exact offset coupling

Let T be the shortcut map. Write a section point n=2^d+r with r odd,
0<r<2^d. For 0<=t<=d, let p_t(r) count odd entries in the first t shortcut
steps of r. Then

    T^t(n)=3^{p_t(r)} 2^{d-t}+T^t(r).

This is an exact ordinary-integer identity. The two trajectories have the same
first d parities. It follows by the elementary one-step identity

    T(2u+v)=3^{v mod 2}u+T(v).

If a complete hitting certificate T^h(r)=1 has h<=d, its entire affine word
lifts to n. The endpoint is 3^{p_h(r)}2^{d-h}+1. For r>1, the affine identity
2^h=3^{p_h(r)}r+C, C>=0, gives 3^{p_h(r)}<2^h. Hence the lifted endpoint is
strictly below n. The same conclusion for r=1 follows after its two-step
1,2,1 certificate whenever d>=2.

The marked interval gives r<=70*2^d/(d+1). It supplies no bound h<=d for the
complete certificate, nor even a first-descent clock <=d for r.

## An infinite obstruction even for a much smaller offset

For each integer m>=1 put

    d=4m,
    r=2^{3m}-1,
    n=2^{4m}+2^{3m}-1.

Then n is odd, floor(log2(n))=4m, and n is marked. Indeed

    (4m+1)(2^{3m}-1) <= 70*2^{4m}

follows from 4m+1<=70*2^m. These offsets are on the scale n^(3/4), far narrower
than the section's inverse-logarithmic relative width.

Nevertheless T^t(r)>=r for every t<=4m. During the first 3m steps,

    T^t(r)=3^t 2^{3m-t}-1 >= r.

At t=3m the value is 27^m-1. At any later clock t=3m+s with s<=m, the basic
inequality 2^s T^s(x)>=x gives

    2^s T^t(r) >= 27^m-1 > 16^m-2^m
                  >= 2^s(2^{3m}-1).

The last inequality uses s<=m. Thus even the smaller offset cannot have a
strict-descent certificate fitting into the shared-parity budget d.

Consequently a proof that simply consumes the offset's known convergence
certificate before its binary padding expires cannot cover all marked starts.
One must supply a reset across the first unmatched parity, or a different
well-founded measure that controls the target after that boundary.

## The unmatched-parity boundary

More generally let target=source+M. A single simultaneous shortcut step changes
the difference as follows (while the displayed difference remains nonnegative):

* M even, source even: M'=M/2.
* M even, source odd: M'=3M/2.
* M odd, source odd: M'=(M-2*source-1)/2.
* M odd, source even: M'=(3M+2*source+1)/2.

Only the first two rows consume the source certificate while preserving a pure
multiplicative high-bit debt. The latter two rows introduce source-dependent
additive terms. A multiset measure on the complete source certificate therefore
needs an additional invariant on this difference process. Consuming the source
certificate alone eventually leaves source=1 and an unrestricted surviving
positive target; that is not a contradiction.

## Multi-return proposal

A bound on the number K of complete section returns needed for a strict descent
would close the global theorem, even if each single return can grow arbitrarily.
The existing RisingReturns argument does not disprove this assertion. Its
all-odd prefix has length comparable to log2(n), while the section has relative
width comparable to 70/log2(n), so a typical such prefix has only O(70) marks.
Making arbitrarily many marks in that single prefix by clustering a repeated
rational approximation would need arbitrarily small q*||q log2(3)||. No such
Diophantine premise has been established here. Neither a universal finite K nor
an unconditional all-K counterexample was obtained.
