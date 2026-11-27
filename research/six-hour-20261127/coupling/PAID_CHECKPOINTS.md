# Ordinary returns on the delayed hard-parent family

Use the shortcut map $T$, the Mersenne number $M_m=2^m-1$, and
$P_m=3^m-1=T^m M_m$. Write $m=11+162j$ and
$81z+271=128\cdot2^m$. The original lower path satisfies
$T^7z=M_m$. The delayed family is $m=12\cdot2^{18k}-1$ with
$j=2(2^{18k}-1)/27$. All sources and endpoints below are positive
ordinary integers. The path statements assume no termination.

## An upper path that falls below the forty-bit threshold

**Lean theorem.** For every $j=50\bmod81$ there is a canonical
$0<W<z$, $W=17\bmod48$, on the lower component of this same $z$.
Its triple reaches an integer $y$ with $2^{40}y<z$. This includes
every delayed $k=64\bmod81$. Explicitly,
\[
 W=(2^{m+13}-28927)/6561,\qquad
 T^{13}W=M_m,\qquad T^{20}(3W)=2^{m-7}+1.
\]
The prefixes have eight and seven odd departures. Each pair of
steps from $4v+1$ reaches $3v+1$. Since $m-7$ is even, another
$m-7$ clocks reach $y=3^{(m-7)/2}+1$. The strict height follows
at exponent $(m-7)/2=100$ by integer arithmetic and persists by
induction. The smallest exponent in the original class is 8111.

For example put $X=2^{m-7}$. The class gives $X=502+19683v$ and
$W=80225+3145728v$. The physical traces at $v=0$ give
$T^{13}(80225)=64255$ and $T^{20}(240675)=503$. Their odd
counts give the affine coefficients at every lift. The original
ordinary residue and the map from the delayed parameter are both
checked in [PaidCheckpoint.lean](PaidCheckpoint.lean).

## Five ordinary post-turn mergers, covering every delayed phase

**Lean theorem.** At every $k\ge13$, the particular integer
$B=27\cdot2^{m-3}-17$ shares its ordinary forward orbit with some
$M_s$ satisfying $0<s$ and $s+40<m$. At
$k=376,1429\bmod2187$ this checkpoint lies on the triple of a
strictly smaller canonical visitor $W$ whose lower path meets
the lower path from the original $z$. The two seed identities are

| $k\bmod2187$ | $j\bmod2187$ | $W$ | $(a,Q_a)$ at $T^aW=M_m$ | $(b,Q_b)$ at $T^b(3W)=B$ |
| ---: | ---: | --- | ---: | ---: |
| 376 | 881 | $(2^{m+18}-1786613)/177147$ | $(18,11)$ | $(21,13)$ |
| 1429 | 1772 | $(2^{m+17}-962197)/177147$ | $(17,11)$ | $(20,13)$ |

The source-specific conclusion uses one of these two seed classes.
The all-$k$ theorem about $B$ by itself does not put $B$ on a
specified lower or upper path. [DelayedTurns.lean](DelayedTurns.lean)

Write $m-3=11d+r$, $0\le r<11$. The ordinary identity
$T^{11}(2048v-17)=2187v-17$ for $v\ge1$ transports $B$ for $d$
complete turns. Over the remaining $r$ clocks the actual point
has the same parity word as the signed integer $-17$. Let $q$ be
the number of odd inputs in those $r$ clocks and $-a$ their signed
endpoint. After the complete $m-3$ clocks the physical position
is $3^n-a$ with $n=7d+3+q$. The following table gives a common
endpoint $T^h(3^n-a)=T^h(P_{n-e})$ on every indicated original
class. The earlier exponent is $s=n-e$.

| $k\bmod5$ | $r$ | $q$ | $a$ | $e$ | $h$ | Odd counts from $3^n-a$, $P_{n-e}$ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 8 | 7 | 136 | 0 | 23 | 10, 10 |
| 1 | 10 | 7 | 34 | 0 | 71 | 37, 37 |
| 2 | 5 | 4 | 41 | 0 | 229 | 113, 113 |
| 3 | 1 | 1 | 25 | 0 | 29 | 14, 14 |
| 4 | 0 | 0 | 17 | 1 | 68 | 29, 30 |

For the proof, start each class at its representative $13\le k_0\le17$.
Here $h\le18k_0$ and $2^{90}=1\bmod11$. Thus the change in
$2^{18k}$ from $k_0$ to $k_0+5t$ is always divisible by $11\cdot2^h$.
The remainder $r$ stays fixed, and $n-e$ changes by a multiple
of $2^h$. As $3^{2^h}=1\bmod2^h$, the ordinary residue
$R=3^{n-e}\bmod2^h$ stays fixed throughout the progression.
All five residues are computed by repeated modular squaring in the
kernel. For $N=R+2^hu$, compare the positive integer starts
$3^eN-a$ and $N-1$. Their endpoints agree at $u=0$ by literal
iteration. Their slopes in $u$ agree by the last column. Hence
every ordinary lift meets at the displayed $h$. Finally all these
earlier exponents satisfy $s+40<m$ by $m=11d+r+3$, $q\le r$
and $d\ge90$. The [independent integer replay](check_paid.py)
prints the [residues and grades](PAID_CONTROLS.json).

## What a least-parent argument may conclude

Write $C(y)$ when $y$ reaches one. Suppose $z$ is the least positive
canonical reverse disagreement, so $\neg C(z)$ and $C(3z)$. Since
the ordinary lower paths meet, $\neg C(W)$. Since $W$ is smaller
and canonical, $\neg C(3W)$. In the positive-turn class its triple
reaches $y$ with $2^{40}y<z$. In either negative-turn class it
meets $M_s$, with $2^{40}M_s<z$. Each alternative therefore
produces a positive nonbasin integer with forty bits of sufficient
height savings. The pinned quantitative-return theorem produces a
canonical reverse disagreement of height at most $2^{40}$ times that
integer, contradicting leastness. Thus the indicated original
parents cannot be least canonical reverse disagreements. This final
application uses the prior quantitative-return theorem. Convergence
of each separate lower source does not follow from that leastness
exclusion.

**Provenance.** PR197 at
`1f0f496fbea37792439feada6106eaaff596bcd1`,
`research/ayh-resource-reset-20261124/closing-proposal/OPPOSITE_ARM_CONTRACTION.md`,
already uses upper positive-cycle contraction on the different
$j=97\bmod162$ Mersenne exponent row. Its
`source-progress/TWO_CHECKPOINT_RESCUE.md` uses the negative-17
cycle and compares earlier Mersenne peaks on that row. Its
`closing-proposal/QuantitativeReturn.lean` supplies the forty-bit
consumer. PR192 at `ed7a6fe30b8602407f77855ceb74ce0489ce9c10`,
`research/astra-unconventional-20261126/descent/POSTPEAK_DELAY.md`
and `PAID_DELAY_REPAIRS.md`, supplies the delayed family, the
all-earlier-peak native delay, thirty paid examples, and one
previous infinite delayed class by a different signed bridge.
The present results give the stated original-parent seed classes
and the simultaneous five-phase physical return from $B$ at every
$k\ge13$. On other original classes, connecting a suitable upper
path to this checkpoint or to another effective return remains open.
