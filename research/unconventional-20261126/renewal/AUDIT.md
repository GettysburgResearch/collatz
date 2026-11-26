# Independent audit of PR201's finite record-renewal argument

**Scope.** The audited file is the record-renewal README at
[94ce06ccbd312ccd0ce4450b567cc514a2f0b54a](https://github.com/GettysburgResearch/collatz/blob/94ce06ccbd312ccd0ce4450b567cc514a2f0b54a/research/killed-green-head-closure-20261124/record-renewal/README.md),
SHA-256 c92c6736011df30adf404b886da75f8a88a4688b2af0a99c6e2a28f9d37ae5a2.
The claims reviewed are Theorems D, G, Q and their explicitly
conditional corollaries. One range typo in section 5.2 is described
below. This audit does not transfer a bounded record-gap hypothesis
to unrestricted actual trajectories.

**Finite-prefix parsing and the dimension.** For a reversed complete
ladder word set $A_j=2^{S_j}/3^j$. Its endpoint $A_m<1$ is strictly
larger than each nonempty proper prefix value. Every subsequent
complete block or partial block has all its nonempty prefix ratios
strictly below one. Thus in an arbitrary prefix of $b\ge J$ letters
of an infinite concatenation with block lengths at most $J$, the
first block end occurs and is the unique maximum over these $b$
nonempty prefix ratios. Removing it reduces the problem to the same
statement. Stop when fewer than $J$ letters remain. The selected
blocks are forced solely by the prefix read, without knowing its
completion. Their total length exceeds $b-J$. For a whole finite
critical word, cutting at its unique nonempty maximum leaves a
possibly empty critical suffix, so the same rule parses the finite
word into complete reversed blocks.

At fixed depth and clock the ternary congruence fixes the carry
modulo $3^b$. The bounded real inverse offset bounds its possible
integer lifts uniformly in $b$. Equal carries give equal words:
subtract the last term $3^{b-1}$ of the reversed carry, take its
dyadic valuation to get the last gap, divide it out and repeat;
the final unextracted first gap is fixed by the total clock.
Equivalently the paper's positive ordinary inverse decoder works.
There are only $O(b)$ clocks. The prefix mass and word-count
arguments give the claimed Hausdorff and box dimensions despite
these possible overlaps. For the full tree the rotation lower bound
and raw composition count give $\theta$ as claimed.

**Ladder tail and sharp truncation.** Caravenna's paper defines the
strict ascending ladder epoch and height; Remark 1 on printed
page 6 gives
$\Pr(T_1>n)\sim2E(H_1)/(\sigma\sqrt{2\pi n})$ for centered steps
of finite nonzero variance. The tilted independent geometric gaps
of PR201 meet these hypotheses. Their nonempty partial sums cannot
equal zero since $\log_2 3$ is irrational. The strict loss at
length one makes $\sum_m N_m e^{-Hm}<1$. Splitting the exponentially
weighted truncation above and below a fixed fraction of $J$
proves D5 as written. The [three-term pressure proof](PRESSURE.md)
now strengthens D5 and gives an independent first-maximum
factorization.
[Caravenna, author's paper, Remark 1](https://fcaraven.github.io/download/papers/llt.pdf)

**Actual bounded-gap conclusions.** Finite adjacent-state clusters
in either contracting coordinate give a finite graph of recurring
labelled transitions. The late actual path visits every remaining
label infinitely often, so each label is on a loop. Composing that
loop fixes a negative rational $-C/(3^m-2^s)$ of dyadic valuation
zero. A wrong rational gap either loses dyadic integrality at once
or creates an even value from which the next gap loses it. It
cannot return to an odd rational. The full recurring path must
therefore have genuine signed rational gaps. Agreement from one
positive source across arbitrarily many native steps is impossible
by $2^s\mid(dq-a)$ with $a/d<0$. This establishes G.

For Q, compactness of the **finite** block alphabet supplies the
two-sided recurrent languages and their continuous ternary coding.
A rational unit's backward shadow has bounded real size and bounded
odd denominator, so it lies on a negative signed cycle. Arbitrarily
long actual matches to its past must eventually depart on the same
positive trajectory. Bounded gaps allow finitely many words through
a second subsequent record and preserve the increasing ternary
precision. A wrong gap produces a dyadically nonintegral rational
phase, which contracts forward in the ternary metric while its
dyadic valuation decreases by each successive native clock. For
the phase $-1$, the wrong-gap value $-2/2^e$, $e\ge2$, ranges in
$[-1/2,0)$; the narrower interval printed in section 5.2 omits
$e>3$. The lower bound $-1/2$ used to force positivity after two
more steps is valid. The Baire argument on a minimal compact
two-sided subsystem supplies a rational fiber in the countable
case. These steps give the stated result with this interval fix.

**Replay.** The old exact JavaScript counters, first 32 ladder counts
and depth-256 count reproduce. The recorded JSON includes metadata
absent from standard output, and the expressly illustrative floating
roots differ in their last machine places. The source control script
has SHA-256 ae8a3591b8599d5de7638deb4d9ad116ccb1f40b153762e6c062fb0cc740b557;
the stored JSON has SHA-256 6843ea7590fba998deeb94d68e1dab67b0ba2039314edfe1cebff2810252484a.
The current replay stdout has SHA-256
d1a478b46633fc63233fdafa00624693926a2b193f83a411d708d07fb7091f7f.
No full Collatz theorem follows from this audit.
