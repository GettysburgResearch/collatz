# Physical five blocks and an ordinary carry controller

**Status: PROPOSED exact local theorems and explicit obstructions to a
specified closing argument. The physical forward-five law remains OPEN.**
No result here proves the Collatz conjecture. The positive result is a
two-odd-step commutation with multiplication by five, including an infinite
family with a fully specified first-hit certificate for both arms. The
negative results concern a particular ordinary carry controller and
particular candidate ranks; they do not rule out other closure proofs.

## Normalization and source boundary

Throughout,

\[
T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n,\end{cases}
\qquad C=\{n\in\mathbb Z_{>0}:T^j(n)=1\text{ for some }j\ge0\}.
\]

For odd positive integers, put
\(U(n)=(3n+1)/2^{v_2(3n+1)}\). The notation
\(I_a(z)=(2^a z-1)/3\) denotes a *legal* positive odd inverse of \(U\),
only when its displayed value is an integer and \(a\ge1\). For convergent
\(n\), let \(\tau(n)\) be its first shortcut hitting time of 1 and
\(\omega(n)\) the number of odd inputs before that first hit. Thus
\(\omega(1)=0\); no extra turns around the \(1,2\) cycle are counted.
Write \(n\sim m\) only when actual forward iterates of the two positive
ordinary integers meet, at possibly different finite clocks.

The outstanding physical law is

\[
x\text{ odd},\quad 3\nmid x,\quad x\in C
\quad\Longrightarrow\quad 5x\in C.                 \tag{F5}
\]

The following frozen sources fix the boundary of the present contribution.
All links identify the full inspected head; statements at later heads are
outside this comparison.

| Source | Frozen full SHA | Inspected path and relation to this note |
|---|---|---|
| PR157 | `64361ecca770092d6c8242dc6211e38818af2e50` | [`research/global-closure-20261120/merger.md`](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/merger.md), GCM-001/002: (F5) is sufficient for full Collatz by a complete directed certificate. That conditional theorem is inherited. |
| PR157 | `64361ecca770092d6c8242dc6211e38818af2e50` | [`research/global-closure-20261120/closing-attempts.md`](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/closing-attempts.md), GCL-001/002: shifted-power inverse-lift obstruction and fixed-word stopping-grade obstruction. The block below does not supply the failed uniform inverse-lift propagator. |
| PR154 | `fe40bb6f88e8094290ef01207d9bf7c4798d35d0` | [`research/structural-reset-20261120/capacity/PAIR_COUPLING.md`](https://github.com/GettysburgResearch/collatz/blob/fe40bb6f88e8094290ef01207d9bf7c4798d35d0/research/structural-reset-20261120/capacity/PAIR_COUPLING.md), CP-001: the elementary physical detour \((16n+3)/3\) for odd multiples of three is inherited. |
| PR158 | `cf49a68bf93e98c97a18dc3d1a4186faf534e422` | [`research/ordinary-basin-closure-20261120/CERTIFICATE_CARRY.md`](https://github.com/GettysburgResearch/collatz/blob/cf49a68bf93e98c97a18dc3d1a4186faf534e422/research/ordinary-basin-closure-20261120/CERTIFICATE_CARRY.md), especially §4: supplied-certificate compilation for the target \(2x-1\), including the depth-two family \((2^{6r+4}-7)/9\). C5-002 gives a positive result for the **different target \(5x\)** on exactly that family. |
| PR158 | `cf49a68bf93e98c97a18dc3d1a4186faf534e422` | [`research/ordinary-basin-closure-20261120/EXPANDING_RETURNS.md`](https://github.com/GettysburgResearch/collatz/blob/cf49a68bf93e98c97a18dc3d1a4186faf534e422/research/ordinary-basin-closure-20261120/EXPANDING_RETURNS.md): fixed-word valuation budgets and a switching resource cycle already obstruct generic height-plus-resource descent. C5-004/005 specialize a different controller and supply explicitly convergent source families; no generic recharge priority is claimed. |
| PR160 | `6d877e718f5ef9d57fe1830912c444359718747a` | [`research/closure-attacks-20261120/merger/PHYSICAL_CERTIFICATE_BOUNDARY.md`](https://github.com/GettysburgResearch/collatz/blob/6d877e718f5ef9d57fe1830912c444359718747a/research/closure-attacks-20261120/merger/PHYSICAL_CERTIFICATE_BOUNDARY.md), PC001–004: fixed-word meeting obstruction, an expanding homogeneous five-pair return, fixed-word budgets, and the scalar semigroup carry. Its expanding return already prevents a universal first-return descent claim. |
| PR160 | `6d877e718f5ef9d57fe1830912c444359718747a` | [`research/closure-attacks-20261120/merger/SINGLE_MULTIPLIER.md`](https://github.com/GettysburgResearch/collatz/blob/6d877e718f5ef9d57fe1830912c444359718747a/research/closure-attacks-20261120/merger/SINGLE_MULTIPLIER.md): a symmetric sufficient five law, explicitly weaker than PR157's directed criterion; a smaller output does not discharge larger oracle calls. |
| PR146 | `e238c63a5d57f96bb063b7472498d1977df51951` | [`research/upper-bit-mergers/BOUNDED_RANK_TRANSFER.md`](https://github.com/GettysburgResearch/collatz/blob/e238c63a5d57f96bb063b7472498d1977df51951/research/upper-bit-mergers/BOUNDED_RANK_TRANSFER.md): bounded known odd-rank transfer for the companion \(2x-1\), with no lifted mergers at source ranks two or three. Its target differs from C5-001/002. |

No assertion of priority over the wider literature is made. All proofs
below are self-contained ordinary-integer calculations; the source table
is needed for attribution and for the conditional significance of (F5),
not to silently add any unproved closure law.

## C5-001: a two-odd-step physical commutation

Let \(q\) be a positive odd integer with \(3\nmid q\), and let
\(\ell\ge6\) satisfy \(2^\ell q\equiv7\pmod9\). Set

\[
R_\ell(q)=\frac{2^\ell q-7}{9}.
\]

Then \(R_\ell(q)\) is positive and odd, and the following are actual
ordinary paths, with exactly two odd inputs on each arm:

\[
T^\ell(R_\ell(q))=q,\qquad
T^\ell(5R_\ell(q))=5q.                              \tag{1}
\]

Equivalently, with \(b=\ell-2\ge4\), all displayed inverse edges are legal
and

\[
\boxed{\quad 5I_2(I_b(q))=I_5(I_{b-3}(5q)).\quad}    \tag{2}
\]

### Proof and complete legality

The defining congruence gives integrality. As \(\ell\ge6\), reduction
modulo 64 gives \(R_\ell(q)=64u+49\), with \(u\ge0\). The complete first
six steps are:

| Clock | Lower arm | Upper arm |
|---:|---:|---:|
| 0 | \(64u+49\) | \(320u+245\) |
| 1 | \(96u+74\) | \(480u+368\) |
| 2 | \(48u+37\) | \(240u+184\) |
| 3 | \(72u+56\) | \(120u+92\) |
| 4 | \(36u+28\) | \(60u+46\) |
| 5 | \(18u+14\) | \(30u+23\) |
| 6 | \(9u+7\) | \(45u+35\) |

The lower odd input positions are 0 and 2; the upper positions are 0 and
5. Every other input in the table is even. Moreover,
\(9u+7=2^{\ell-6}q\), so exactly \(\ell-6\) common halvings complete
(1). This also proves the exact accelerated words \((2,b)\) and
\((5,b-3)\). None of their intermediate values hits 1 before its stated
endpoint: the lower intermediate odd value is \(I_b(q)\ge5\), and the
upper endpoint is at least 5. Thus, whenever \(q\in C\),

\[
\tau(R_\ell(q))=\ell+\tau(q),\qquad
\omega(R_\ell(q))=2+\omega(q),                      \tag{3}
\]

and the corresponding equalities hold on the upper arm if \(5q\in C\).

### A unit lift exists for every unit target

For the following residue-dependent \(\ell_0\), the required congruence
holds:

| \(q\bmod9\) | 1 | 2 | 4 | 5 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|
| \(\ell_0\) | 10 | 9 | 8 | 11 | 6 | 7 |

If \(3\nmid R_{\ell_0}(q)\), use \(\ell=\ell_0\). Otherwise
\(2^{\ell_0}q\equiv7\pmod{27}\). Since \(2^6\equiv10\pmod{27}\),
\(2^{\ell_0+6}q\equiv16\pmod{27}\), so
\(R_{\ell_0+6}(q)\equiv1\pmod3\). This proves the exact guard

\[
6\le\ell\le17,\quad R_\ell(q)>q,\quad
3\nmid R_\ell(q).                                  \tag{4}
\]

The predecessor can therefore be iterated without introducing a multiple
of three. Conversely, on every such legal paired block the smaller target
satisfies \(q\le R_\ell(q)/7\): in the six-step table,
\((64u+49)-7(9u+7)=u\ge0\), and later halvings only reduce \(q\).

This is a legitimate least-failed-antecedent descent on its source class.
If an odd unit \(x\equiv49\pmod{64}\) belongs to \(C\) but \(5x\notin C\),
take the odd part \(q\) of \((9x+7)/64\). Formula (1), with the exact
common halving clock, gives a smaller odd unit \(q\in C\) with
\(5q\notin C\). Consequently a least failed antecedent for (F5), if one
exists, cannot be in that class. An inverse lift (4) is larger, so its
existence does not put an arbitrary failed antecedent into a smaller legal
block.

### Minimal two-odd pattern, without extrapolating a census

Consider two fixed legal shortcut words on odd sources that map
\((x,5x)\) to \((Q(x),5Q(x))\) for at least two distinct \(x\). Equality
of their affine slopes and unique factorization imply that they have the
same clock and the same number of odd inputs. With one odd input, both
affine constants are 1, which cannot differ by a factor of five. With two
odd inputs, write their second positions as \(i,j\ge1\); their constants
are respectively \(3+2^i\) and \(3+2^j\). The necessary equation is

\[
2^j-5\cdot2^i=12.                                  \tag{5}
\]

It gives \(j>i\), then \(i=v_2(12)=2\), and then \(j=5\). Thus (1) is
the unique two-odd-input pattern, up to common trailing halvings. The
minimum clock is six. This classification is an integer proof, not an
inference from the finite position replay in the checker. It concerns a
return to the homogeneous five-pair section; it does **not** assert that
the two arms meet each other.

## C5-002: an infinite supplied rank-two family closes under five

For every \(r\ge1\), define

\[
x_r=\frac{2^{6r+4}-7}{9}.
\]

Both \(x_r\) and \(5x_r\) converge, and their exact first-hit accelerated
valuation words are

\[
\boxed{\quad x_r:\ (2,6r+2),\qquad
5x_r:\ (5,6r-1,4).\quad}                            \tag{6}
\]

In particular,

\[
(\tau(x_r),\omega(x_r))=(6r+4,2),\qquad
(\tau(5x_r),\omega(5x_r))=(6r+8,3).                 \tag{7}
\]

Apply C5-001 with \(q=1\) and \(\ell=6r+4\). The lower arm reaches 1;
the upper arm reaches 5, whose exact final odd valuation is 4. The legal
block already excludes an earlier first hit. For example, \(r=1\) gives
\(113\to85\to1\) and \(565\to53\to5\to1\) under \(U\).

PR158 `CERTIFICATE_CARRY.md` §4 identifies this same source family when
analyzing the companion \(2x_r-1\); that different companion reduces to
a Mersenne obligation. Formula (6) settles the multiplied companion
\(5x_r\) for every parameter. The identity holds even at parameters for
which \(3\mid x_r\); (F5) only needs the unit members.

This does not settle arbitrary depth-two sources
\(I_a(I_b(1))\). The special first valuation \(a=2\) is essential to
(2). In particular, it supplies no recursive rule for an arbitrary next
letter in a known-convergent antecedent's certificate.

## C5-003: a scalar controller with ordinary realizations

To seek a terminating carry repair rather than a single uniform word,
write

\[
n=10h-1,\qquad h\in\mathbb Z_{>0}.
\]

Use the following deterministic controller until its third branch is
reached:

| Condition | Carry action | Exact ordinary realization |
|---|---|---|
| \(h\equiv0\pmod3\) | \(L_0(h)=2h/3\) | \(10L_0(h)-1=I_1(n)\), so \(T(10L_0(h)-1)=n\). |
| \(h\equiv1\pmod3\) | \(L_1(h)=(16h-1)/3\) | \(10L_1(h)-1=A(n)=(16n+3)/3\), where \(T^5(A(n))=T(n)\). |
| \(h\equiv2\pmod3\) | Exit with \(q=(8h-1)/3\) | \(5q=I_2(n)\), so \(T^2(5q)=n\). |

The ordinary endpoints \(n\), \(10L_i(h)-1\), and \(5q\) are positive odd
integers on their respective stated domains. In the middle row \(3\mid n\),
and the inherited physical detour is
exactly

\[
A(n)\longmapsto8n+2\longmapsto4n+1
\longmapsto6n+2\longmapsto3n+1\longmapsto T(n).      \tag{8}
\]

It has two odd inputs. If \(n\in C\) is an odd multiple of three, then
\(\tau(A(n))=\tau(n)+4\) and \(\omega(A(n))=\omega(n)+1\).
The inverse-one row adds one to each first-hit clock.

The exit quotient is always odd. Its exact unit guard is

\[
3\nmid q\quad\Longleftrightarrow\quad
h\equiv2\text{ or }5\pmod9.                        \tag{9}
\]

The residue \(h\equiv8\pmod9\) is a nonunit exit; it cannot be silently
counted as a successful unit selector. More fundamentally, even a unit
exit only proves \(n\sim5q\). Knowing \(n\in C\) proves \(5q\in C\),
and does **not** prove \(q\in C\). That latter inference would assume a
backward-five law. A least failed antecedent proof needs a paired
realization preserving both relevant arms, as in (1), or another justified
membership implication. This scalar controller by itself has neither.

## C5-004: a complete carry renewal recharges the proposed rank

The obstruction here occurs on an explicit infinite family of known
convergers. It therefore cannot be dismissed as a trajectory whose
antecedent is outside the basin of one.

Put \(J(n)=4n+1\). For odd \(n>1\),
\(T^3(J(n))=T(n)\), with one odd input on either side of the meeting.
Consequently \(\tau(J(n))=\tau(n)+2\) and
\(\omega(J(n))=\omega(n)\) when \(n\in C\).
The seed 19 has \((\tau,\omega)=(14,6)\), as certified by

\[
19,29,44,22,11,17,26,13,20,10,5,8,4,2,1.
\]

For \(r\ge0\), let

\[
a=5+243r,\quad
s=J^{2a}(19)=\frac{58\cdot16^a-1}{3},\quad
h=\frac{s+1}{15}=\frac{2(29\cdot16^a+1)}{45},\quad
n=10h-1.                                          \tag{10}
\]

The number \(h\) is an even positive integer because \(a\equiv2\pmod3\).
Moreover \(h\equiv13\pmod{81}\). For the latter statement,
\(v_3(16^{243}-1)=6\), and division by 45 preserves the residue modulo
81 as \(a\) increases by 243. At \(a=5\), \(h=1{,}351{,}498\equiv13\).
Since \(T(n)=s\), the supplied certificate gives

\[
(\tau(n),\omega(n))=(4a+15,7).                     \tag{11}
\]

Writing \(h=81v+13\), the controller takes the complete renewal

\[
h\ \xrightarrow{L_1}\ 432v+69
\ \xrightarrow{L_0}\ h'=288v+46=\frac{32h-2}{9}.   \tag{12}
\]

The middle value has exact 3-adic valuation one. At both endpoints,

\[
v_3(h)=v_3(h')=0,\qquad
v_3(13h-1)=v_3(13h'-1)=1,\qquad h'>h.              \tag{13}
\]

Indeed, \(13h-1=3(351v+56)\) and
\(13h'-1=3(1248v+199)\). Set \(n'=10h'-1=(32n+3)/9\).
The two physical realizations concatenate to

\[
T^6(n')=T(n),\quad
\tau(n')=\tau(n)+5,\quad
\omega(n')=\omega(n)+2.                            \tag{14}
\]

Every input before the displayed meeting exceeds one, so these are
first-hit identities. At \(r=0\), the two ordinary inputs are
\(13{,}514{,}979\) and \(48{,}053{,}259\), with clocks \((35,7)\) and
\((40,9)\).

Thus no rank of the specified form

\[
\alpha\log(1+n)+\beta\tau(n)+\gamma\omega(n)
+A v_3(h)+B v_3(13h-1),                            \tag{15}
\]

where \(\alpha,\beta,\gamma\ge0\), at least one of these three is
positive, and \(A,B\) are arbitrary fixed real coefficients, decreases
on every complete renewal of this controller: it strictly increases on
(10). If all three height/clock coefficients vanish, the two valuation
terms are unchanged and still give no strict decrease on this family.

This is a specified rank obstruction. It does not say that the controller
is nonterminating, that its arbitrary switching itineraries recur, or that
these changing examples form one infinite orbit. PR158 already contains a
different resource-cycle obstruction; the additional feature here is the
explicit known-convergent ordinary family and its exact first-hit clocks.

## C5-005: no uniform output-height bound, even at known odd depth six

There are known-convergent sources \(s\), all with \(\omega(s)=6\), for
which the controller performs any prescribed number \(k\ge1\) of
successive \(L_1\) moves and then takes a unit exit \(q\), with

\[
\frac q s\ \ge\ \frac{28}{195}\left(\frac{16}{3}\right)^k. \tag{16}
\]

In particular no uniform \(q\le K s\) bound holds for this controller on
these supplied convergers, and \(q>s\) for every \(k\ge2\).

### A finite construction for every length

Choose \(c_k=7^{1-k}\pmod9\) in \(\{1,4,7\}\). There is a unique
\(0\le a_k<3^{k+3}\) such that

\[
16^{a_k}\equiv
754^{-1}\bigl(19+5\cdot3^{k+2}c_k\bigr)
\pmod{3^{k+4}}.                                   \tag{17}
\]

Here 754 is prime to three. The right side is 1 modulo three, and 16
generates precisely that subgroup modulo \(3^N\), because
\(v_3(16^{3^j}-1)=j+1\). Thus (17) is a finite, uniquely solvable
base-three digit lift; it is not an unbounded search or a convergence
assumption. Reduction modulo nine gives \(a_k\equiv2\pmod3\).

Use (10) with \(a=a_k\), without imposing \(a=5+243r\), and put

\[
t=\frac{13h-1}{3^k}.
\]

Since

\[
13h-1=\frac{754\cdot16^a-19}{45},
\]

(17) gives \(t\equiv c_k\pmod9\) and
\(v_3(13h-1)=k\). The number \(t\) is positive and odd. The successive
carry values have the exact formula

\[
h_j=\frac{16^j3^{k-j}t+1}{13},\qquad0\le j\le k.   \tag{18}
\]

For \(j<k\), \(h_j\equiv1\pmod3\), so the claimed \(L_1\) move is
legal and proves the formula inductively. At the endpoint \(H=h_k\),

\[
H\equiv7(7^k c_k+1)\equiv2\pmod9.
\]

Therefore \(q=(8H-1)/3\) is an odd ternary unit, with \(q\equiv2\pmod3\).
Concatenating the actual detours and the final inverse-two edge gives

\[
T^{4k+3}(5q)=s,                                   \tag{19}
\]

with exactly \(k+2\) odd inputs. All these inputs before the meeting exceed
one. Since the source is the explicit \(J\)-lift of 19,

\[
(\tau(s),\omega(s))=(4a+14,6),\qquad
(\tau(5q),\omega(5q))=(4a+4k+17,k+8).              \tag{20}
\]

No membership assertion about \(q\) follows from (19), and the checker
does not test its convergence.

Finally,

\[
H=\left(\frac{16}{3}\right)^k\left(h-\frac1{13}\right)+\frac1{13}
\ge\frac{12h}{13}\left(\frac{16}{3}\right)^k,
\quad q\ge\frac73H,\quad s<15h,
\]

which proves (16). The first six finite lifts choose
\(a_k=77,176,392,1526,2012,14405\). These are changing ordinary
convergent witnesses with prescribed finite expansion length. They do not
prove a single orbit expands forever.

## First unsupported steps and useful next obligation

C5-001 is a real paired block, and C5-002 closes the five law on an entire
infinite supplied-certificate family. To extend this into a proof of (F5),
one still needs a complete procedure that reduces **every** failed
antecedent while preserving the two physical arms. The block has no such
coverage theorem. A known first-hit word need not begin with its legal
valuation pattern.

The scalar controller is a separate attempted repair. Its unresolved
termination problem, its nonunit exit cases, its lack of a proof that the
exit quotient is in \(C\), and its failure of a uniform output-height bound
are distinct obligations. A proof of termination alone would not discharge
the others. Equations (12)–(20) eliminate the specified height/clock/debt
ranks and uniform output bound, even on a supplied convergent domain; they
do not eliminate every possible ranking or paired controller.

No tripling invariance, scalar semigroup action on components, random
parity hypothesis, or convergence of an untested quotient is assumed.
Both nontrivial cycles and divergence remain outside the closure proved
here. The implication from a full proof of (F5) to full Collatz remains
the separately pinned PR157 conditional theorem.

## Exact bounded replay

The literal-step production checker is
[`experiments/creative_five_closure.py`](../../experiments/creative_five_closure.py).
Its deterministic report is
[`five-report.json`](../../reports/2026-11-20-creative-closure/five-report.json).
It refuses to overwrite an existing report. To regenerate and compare:

```bash
python -X utf8 -B experiments/creative_five_closure.py --compare reports/2026-11-20-creative-closure/five-report.json
```

The replay checks paired blocks for odd unit \(q\le3001\) and clocks
6 through 25; the bounded unit-lift choice on that same target range;
the first 25 instances of (6), including exact valuations and first-hit
clocks; all carry branches for \(1\le h\le1500\); the first five complete
known-convergent renewals; and prescribed expansion lengths 1 through 6.
Negative controls retain the failed clock-five block, a nonunit initial
paired predecessor requiring the six-step repair, a nonunit carry exit,
and an expanding complete renewal. These checks validate the displayed
finite instances. The proofs above, not a finite replay, establish the
all-parameter identities and obstructions.
