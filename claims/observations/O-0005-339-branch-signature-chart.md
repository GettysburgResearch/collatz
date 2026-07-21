# O-0005 — A 339-branch mildly supercritical chart

Claim ID: `O-0005`  
Title: A 339-branch signature-tail collision chart at depth 44  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-0005`, `T-0002`, `T-0005`, `X-0003`  
Scope: one finite exact collision fiber  
Related counterexample candidates: none

## Statement

Let \(\mathcal W\) be the set of length-24 parity words with eight ones and
inverse signature

\[
\sigma(w)
\equiv2^{-24}B(w)
\equiv2906
\pmod{3^8}.
\tag{1}
\]

Exact enumeration in `X-0003` gives

\[
|\mathcal W|=339.
\tag{2}
\]

The integer

\[
y=3\,501\,195\,263
\tag{3}
\]

is the least nonnegative solution of

\[
y\equiv2906\pmod{3^8},
\qquad
y\equiv-1\pmod{2^{20}}.
\tag{4}
\]

For each \(w\in\mathcal W\), put

\[
r(w)=\frac{2^{24}y-B(w)}{3^8}.
\tag{5}
\]

Then the 339 integers \(r(w)\) are distinct and lie in the interval

\[
8\,952\,950\,628\,352
\le r(w)\le
8\,952\,950\,645\,559.
\tag{6}
\]

Every one satisfies

\[
\boxed{
T^{44}(2^{44}q+r(w))
=3^{28}q+11\,642\,373\,114\,938
}
\tag{7}
\]

for every \(q\ge0\).

Equivalently, put

\[
M=2^{44}=17\,592\,186\,044\,416,
\]

\[
N=3^{28}=22\,876\,792\,454\,961,
\]

\[
r_0=8\,952\,950\,628\,352,
\qquad
s=11\,642\,373\,114\,938,
\]

and

\[
D=\{r(w)-r_0:w\in\mathcal W\}.
\]

Then

\[
\boxed{
T^{44}(Mq+r_0+d)=Nq+s
\qquad(d\in D),
}
\tag{8}
\]

with

\[
|D|=339,
\qquad
\min D=0,
\qquad
\max D=17\,207.
\tag{9}
\]

The expansion ratio is

\[
\frac NM\approx1.3003950957.
\]

The induced map is

\[
H_D(MB+d)=NB+d,
\qquad d\in D,
\tag{10}
\]

on the lifting class

\[
\boxed{
A\equiv2\,689\,422\,486\,586
\pmod{5\,284\,606\,410\,545}.
}
\tag{11}
\]

## Additional exact geometry

`X-0003` verifies:

1. the 339 offsets occupy all 16 residue classes modulo 16;
2. the difference set contains every integer in
   \[
   [-934,934];
   \]
3. the fiber contains a run of seven consecutive input residues,
   \[
   8\,952\,950\,644\,244,
   \ldots,
   8\,952\,950\,644\,250;
   \]
4. the SHA-256 digest of the newline-separated sorted offsets is
   ```text
   934328989d862bb180e6324fc217fad4cefdc5fe4c2cfdadc255a24ac0ea3e5e
   ```

## Construction

The words in \(\mathcal W\) form the largest equal-signature class found among
the

\[
\binom{24}{8}=735\,471
\]

weight-eight words. Equation (4) appends the shortest common all-odd tail that
makes the full block supercritical: 20 odd steps. Thus every total parity word
is

\[
w1^{20},
\]

of length 44 and weight 28.

`L-0005` gives (5), the first 24 steps, and the common root. Its odd-tail formula
gives the remaining 20 steps and the common output. `L-0001` then gives the
lifted identity for all \(q\).

## Motivation

The theorem `T-0005` proves unbounded alphabets abstractly. This chart shows
that the resulting alphabets can also have nontrivial local geometry: complete
small-modulus projection, a long centered interval in the difference set, and
a consecutive subbundle.

These properties are more relevant to vertical carry closure than cardinality
alone.

## Dependency audit

- The count 339 and the listed geometric properties are finite exhaustive
  outputs of `X-0003`.
- Once the signature class is fixed, every Collatz identity follows
  algebraically from `L-0005` and `L-0001`.
- `T-0002` supplies the induced map and lifting class.

## Gap audit

- No member of this fiber is claimed to have an infinite admissible induced
  orbit.
- Full coverage modulo 16 and a large difference interval do not by themselves
  imply vertical macro-tile closure.
- The set \(D\) is defined algorithmically and also committed as
  `experiments/X-0003-signature-tail-fibers/results/m8-offsets.txt`; the program
  regenerates and checks the file exactly.

## Adversarial tests

`X-0003` traces all 339 words and several lifted values of \(q\), verifies the
CRT root and output, and independently recomputes every geometric statistic.

## Remaining uncertainty

The finite observation awaits independent rerun and reconstruction.

## Suggested next attack

Exploit the full modulo-16 projection and the interval inside \(D-D\) in the
run-length skeleton. Determine whether they permit a finite family of cofactor
relays unavailable in the smaller alphabets.
