# Joint Benford statistics along canonical inverse trajectories

For almost every inverse path at each fixed positive odd unit, the
leading significands of its odd states obey Benford's law simultaneously
in all real bases B>1. In each such base the logarithmic phase is
asymptotically independent of the local dyadic and ternary state. For
example the frequency of a state cylinder C together with a significand
in [u,v]⊂[1,B] is ν(C) log_B(v/u). This is a consequence of almost-sure
inverse-word frequencies and summability of the affine corrections.
Earlier work studies Benford statistics for finite forward 3x+1
trajectories under sampling of initial values.

[Fixed-root inverse strong laws](ALMOST-SURE.md)
· [Kontorovich and Miller, *Benford's law, values of L-functions and the 3x+1 problem*](https://arxiv.org/abs/math/0412003).

Fix one path from the full-measure event of the strong laws. Write a_i
for its inverse exponents. Every word has limiting frequency equal to its
probability under the two-sided iid geometric shift (Ω,T,π). Extend the
sample to negative indices arbitrarily. Its empirical shifts converge to
π on the compact space (ℕ∪{∞})^ℤ, where ℕ has the one-point
compactification. Indeed finite words give all finite-dimensional limits
by truncation, since the limiting positive-integer word probabilities
sum to one. Changing finitely many letters does not affect these means.

For a finite list of bases write v=(1/log B_i)_i, and let G be the
closure in the torus of the real line s↦sv mod 1. For a new letter a
let c(a)=(a log 2−log 3)v mod 1. The skew product that shifts the
letters and adds c(a) preserves π times Haar probability on G. This
measure is ergodic. Indeed on a nontrivial character of G, represented
by an integer vector m, one has θ=m·v≠0. If exp(2πiθ log 2)≠1 then
|E exp(2πiθ(a log 2−log 3))|<1 by the positive probabilities of
consecutive a. Correlations in this character subspace vanish as the
lag grows: for finite-window letter functions, independent interior
letters give a power of this modulus, and these functions are dense
in L²(π). Otherwise the character increment is constant
exp(−2πiθ log 3)≠1, since log 2/log 3 is irrational. An invariant
coefficient would then be a Bernoulli-shift eigenfunction at a
nontrivial eigenvalue, excluded by mixing. At the trivial character
invariance gives only constants.

Every invariant probability over π for this skew product equals the
product measure. Averaging its group translates against Haar gives the
product, which is an extreme invariant probability by ergodicity.
Almost every translate must therefore be that product; translating
back gives the same conclusion for the original measure. In particular,
every empirical weak limit over our fixed generic letter sample is the
product regardless of the initial phase in G. To see invariance, assign
c(∞) arbitrarily; its discontinuity lies above a π-null slice, so the
empirical shift identity passes to weak limits.

The true log-height phases differ from this additive cocycle by a
convergent translation in G. Indeed their accumulated discrepancy
is −v times Σ_(i≤q) log(1+1/(3X_i)), which converges since
log X_i/i→log(4/3)>0. A constant translation preserves Haar, and the
vanishing remainder preserves empirical limits. A dyadic/ternary
cylinder of the current state depends on a bounded window of the
surrounding valuations as in the strong-law counting proof. Thus the
joint phase law is Haar on G independent of the state. For one base,
G is the full circle. The whole proof is deterministic on the one
fixed event of generic letters and positive speed, so the conclusions
hold for every choice of bases on that same event.

The one-base law also holds for all intermediate integer states of the
inverse shortcut walk. An edge beginning at an odd parent y and ending
at the odd child of exponent a contributes y,2y,…,2^(a−1)y, followed
by the next edge. For a bounded continuous phase test, truncate this
sum at a=M. Each retained contribution is a rotation of the odd-parent
phase given a fixed letter event, hence averages to its Haar integral
times the corresponding letter probability. The excess per odd edge
has limiting mean E[(a−M)_+] by the established physical clock mean
2 and the bounded truncation law. It vanishes as M increases. The same
argument for the unshortened walk includes 2^a y as one additional
state before each odd child. In both cases unfinished edges have
negligible relative length because S_q/q→2 implies a_q/q→0.
