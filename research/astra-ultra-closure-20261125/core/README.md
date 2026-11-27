# A certificate transfer that changes the ternary exponent

**PROPOSED, checked in Lean.** Use the ordinary shortcut map. A certificate of length h starts at its specified positive input and hits 1 at clock h. Its odd count includes the initial input when odd and excludes the endpoint.

Let \(x=32t+17\) and \(Y=24t+13\). The lower orbit reaches \(Y\) after two shortcuts. The two upper paths are

\[
\begin{aligned}
3x=96t+51&\to144t+77\to216t+116\to108t+58\to54t+29\to81t+44,\\
9Y=216t+117&\to324t+176\to162t+88\to81t+44 .
\end{aligned}
\]

Every hitting certificate for \(3x\) passes through the displayed common endpoint because all five preceding values exceed 1. Copy its entire remaining path to the second arm. The new certificate reaches 1 in two fewer clocks and uses exactly two fewer odd inputs. If \(x\) is bad, \(Y\) is bad. Thus a pair consisting of a bad source and a good triple in this class gives a pair consisting of a bad source and a good ninth multiple with lower upper-certificate cost. This applies in particular at \(x=96s+17\) on the PR 197 residue-17 interface.

A least-cost witness among *all* pairs \((b,3^j b)\) with bad lower endpoint and certified upper endpoint cannot itself be one of these exponent-one pairs. To continue the proposed induction one must also reduce the exponent-two output. After three more clocks from its two inputs, the lower value is \(Q=9t+5\) and the upper value is \(9Q-1=81t+44\). The argument supplies the actual remaining certificate at \(9Q-1\). It gives no certificate at \(9Q\). If an intermediate \(3Y\) is independently good, the amount of work in its own certificate need not be bounded by the count just transported. These are the unresolved implications in this induction.

[Ordinary endpoint equality, counts, certificate transport and terminal offset](ExponentTransport.lean)

## The minimum base and whole laps from one good reference

At \(w=1\), every power \(3^r\) with \(r\ge2\) survives both arithmetic filters in the previous minimum-core theorem. Indeed \(3^r\equiv1,3\pmod8\) according to exponent parity. The valuation of \(3^r+1\) is respectively 1 or 2, \(2^{v_2}\le3^r\), and \(85\equiv5\pmod8\). No positive base lies below 1. The remaining target on this slice asks each power to meet an earlier power. Such coverage is equivalent, by induction on the exponent, to convergence of every power of three. The base exponents 0 and 1 reach 1 directly.

The previous prefix merger uses a reference \(u\) reaching 1, a shared initial parity word of length \(h\), and two additional clocks shadowing \(1\to2\to1\). Repeating this last part \(k\) times would multiply a perturbation by \((3/4)^k\). If this mechanism compares the larger and smaller *powers over the same base*, the resulting equality of displacements forces

\[
 3^{j+d}w=u+4^k t,\qquad 3^j w=u+3^k t
\]

with \(d,k,u>0\). To see necessity, cancel the common nonzero derivative \(3^p/2^h\) of the shared initial word. The larger perturbed source must lie above the reference since whole laps contract its displacement and its destination is the smaller power. Coprimality of \(4^k\) and \(3^k\) gives an integral \(t>0\).

In fact these equations force \(w>3^k\). Put \(D=4^k-3^k\) and \(C=3^d-1\). Subtraction gives \(Dt=C3^j w\). Coprimality of \(D\) with 3 shows \(D\mid Cw\), whence \(D\le Cw\). Since \(3^jw=u+3^kt>3^kt\), the same equality gives \(D>C3^k\). In particular no positive integral reference can compare two distinct pure powers this way, with arbitrary prefix length and arbitrary positive lap count. A merger through two separate parity words, two different references or a general common endpoint remains possible.

[Lean proof of the arithmetic bound](TowerLaps.lean) · [Previous minimum-core theorem](../../astra-universal-closure-20261124/global/SmoothCore.lean) · [Previous prefix merger](../../astra-universal-closure-20261124/descent/CorePrefix.lean)

## Replay

Compile the same-checkout `research/astra-minimum-source-20261124/arithmetic/SourceDeletion.lean` into a scratch olean directory on `LEAN_PATH`. Compile both files here using Lean 4.34.1, Mathlib commit `d13f23` and the flags `-DautoImplicit=false -DwarningAsError=true`. The arithmetic bound imports Mathlib directly.
