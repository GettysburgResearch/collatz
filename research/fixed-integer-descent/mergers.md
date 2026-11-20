# Adaptive reductions to one smaller tripling comparison

**Status: PROPOSED, unconditional local theorems; the universal coverage step is OPEN.** All maps below use the shortcut Collatz convention

\[
T(x)=x/2\quad(x\text{ even}),\qquad T(x)=(3x+1)/2\quad(x\text{ odd}).
\]

Write \(x\sim y\) when the two positive ordinary orbits meet at independently chosen finite clocks, and let \(P(n)\) mean \(n\sim3n\). The results concern exact ordinary paths and strictly smaller positive parameters. They do not use a probability model.

The source comparison is PR #146 at `7d04c4dd756cfe495eb3eee78eba35a99085cd2a`, particularly [`THREE_RAY_SMALLER.md`](https://github.com/GettysburgResearch/collatz/blob/7d04c4dd756cfe495eb3eee78eba35a99085cd2a/research/upper-bit-mergers/THREE_RAY_SMALLER.md), [`THREE_RAY_CLOCKS.md`](https://github.com/GettysburgResearch/collatz/blob/7d04c4dd756cfe495eb3eee78eba35a99085cd2a/research/upper-bit-mergers/THREE_RAY_CLOCKS.md), and [`THREE_RAY.md`](https://github.com/GettysburgResearch/collatz/blob/7d04c4dd756cfe495eb3eee78eba35a99085cd2a/research/upper-bit-mergers/THREE_RAY.md). That source already proves the same elementary negative-one exit mechanism in another pair family, the exclusion of least failures congruent to seven modulo eight, and an obstruction to a uniform bounded ordinary clock. The additions here are three explicit one-demand reductions with adaptive valuation guards, their smaller parameters, and a compact further residue exclusion. No global priority claim is made for these elementary identities.

## FM-001: an adjacent-pair exit

For an even positive integer \(z\), put

\[
k=v_2(z),\qquad t=z/2^k,\qquad
\operatorname{Good}(z)\ :\Longleftrightarrow\ t\equiv3^k\pmod4.
\]

**Lemma.** Let \(x>1\) be odd and suppose \(\operatorname{Good}(x+1)\). Then \(x-1\) and \(x\) meet after exactly the same displayed clock \(k+2\), where \(k=v_2(x+1)\). The assertion does not claim that this is their first meeting.

**Proof.** Write \(x=2^k t-1\). The first \(k\) inputs on the upper path are odd. On the lower path, the first step halves, and the next \(k-1\) inputs are odd. Thus at time \(k\) the two values are

\[
W-1,\quad3W-1,\qquad W=3^{k-1}t.
\]

The guard is precisely \(W\equiv3\pmod4\). The next step gives \(U=(W-1)/2\) and \(3U+1\). Here \(U\) is positive and odd. One further step sends both to \((3U+1)/2=(3^k t-1)/4\). Both prefixes have exactly \(k\) odd inputs. All values are ordinary positive integers. ∎

This lemma permits unbounded \(k\), and the specified clock grows with that valuation.

## FM-002: three adaptive induction rules

Each row of the table states an implication \(P(a)\Rightarrow P(n)\). Under its guard, \(a\) is a positive ordinary integer strictly below \(n\). In row F exclude \(n=1\); that base parameter already satisfies \(P(1)\), witnessed by \(3\to5\to8\to4\to2\to1\).

| Rule | Guard on \(n\) | Sole smaller demand \(a\) | Adjacent upper entry \(x\) used in FM-001 |
|---|---|---|---|
| G | \(n\) odd, \(n\equiv2\pmod3\), \(\operatorname{Good}(3n+1)\) | \((2n-1)/3\) | \(3n\) |
| F | \(n>1\), \(n\equiv1\pmod{16}\), \(\operatorname{Good}(9n+7)\) | \((3n+1)/4\) | \((27n+13)/8\) |
| H | \(n\equiv3\pmod{16}\), \(\operatorname{Good}(9n+5)\) | \((3n-1)/8\) | \((27n+7)/8\) |

**Proof of G.** The integer \(a=(2n-1)/3\) is odd and \(T(a)=n\). If \(P(a)\), then

\[
n\sim a\sim3a=2n-1\sim3n-1.
\]

Apply FM-001 to \(x=3n\).

**Proof of F.** Put \(u=3a\). The residue guard gives \(a\equiv1\pmod4\), so \(u\equiv3\pmod4\), and \(x=(3u+1)/2\) is odd. The two ordinary chains, with the indicated one smaller comparison, give

\[
n\sim a\overset{P(a)}\sim u\longrightarrow x,
\]

\[
3n\longrightarrow2u-1\longrightarrow3u-1\longrightarrow x-1.
\]

Here the first relation \(n\sim a\) is the two-step path \(T^2(n)=a\). Write \(9n+7=2^L t\) with \(t\) odd. The residue guard ensures \(L\ge4\), and

\[
x+1=3\cdot2^{L-3}t.
\]

The condition \(\operatorname{Good}(x+1)\) is \(3t\equiv3^{L-3}\pmod4\), equivalently \(t\equiv3^L\pmod4\), exactly the stated guard. FM-001 applies.

**Proof of H.** Put \(u=3a\). The first four ordinary steps from \(n\) have word `OOEE` and endpoint \((9n+5)/16=T(a)\), so \(n\sim a\). After the one smaller comparison,

\[
n\sim a\overset{P(a)}\sim u\sim3u+1=x-1.
\]

The last equivalence follows by taking an odd step from \(u\) and doubling its image. Meanwhile

\[
3n\longrightarrow(9n+1)/2\longrightarrow2u+1\longrightarrow3u+2=x.
\]

Writing \(9n+5=2^L t\) gives \(L\ge4\) and again \(x+1=3\cdot2^{L-3}t\). The same congruence proves \(\operatorname{Good}(x+1)\). ∎

These rules give a deterministic, finite descent of the *demand parameter whenever a guard succeeds*. They do not prove that a guard always succeeds. For example none of G, F, H applies to \(n=9\).

## FM-003: eight compact whole-class certificates

An additional direct rule J is

\[
n\equiv25\pmod{64},\quad a=(9n-1)/32
\quad\Longrightarrow\quad P(a)\Rightarrow P(n).
\]

Together with the initial cases of G, F and H, the following eight rows give exact affine proofs. Write \(n=r+mu\), \(u\ge0\). In the row \(r=1,m=64\), use \(u\ge1\), with the separately verified base \(n=1\). Read the words left to right. `E` and `O` are the respective ordinary shortcut branches, `D` doubles, `I` is the positive odd preimage \((2x-1)/3\), and `M` uses \(P(a)\) to triple the one displayed smaller parameter. The words contain exactly one `M`.

| \(r\) | \(m\) | Word from \(n\) | Word from \(3n\) | Sole smaller parameter | Common endpoint |
|---:|---:|---|---|---|---|
| 17 | 48 | `IMOEOE` | `OOEEI` | \(32u+11\) | \(54u+19\) |
| 25 | 64 | `OEOOEEIM` | `OOEOEEI` | \(18u+7\) | \(54u+21\) |
| 51 | 64 | `OOEEIMOE` | `OEOOEEI` | \(24u+19\) | \(54u+43\) |
| 1 | 64 | `OEMOOEE` | `OOEEEO` | \(48u+1\) | \(81u+2\) |
| 29 | 96 | `IMOEOOE` | `OOOEEI` | \(64u+19\) | \(162u+49\) |
| 67 | 128 | `OOEEIMOOE` | `OEOOOEEI` | \(48u+25\) | \(162u+85\) |
| 5 | 192 | `IMOEOOOE` | `OOOOEEI` | \(128u+3\) | \(486u+13\) |
| 81 | 128 | `OEMOOOEE` | `OOEEOEO` | \(96u+61\) | \(243u+155\) |

Every division and parity condition holds coefficientwise in \(u\). The smaller parameter has positive slope and intercept, its slope is smaller than \(m\), and its intercept is smaller than \(r\), apart from the stated base exception where it becomes strictly smaller for \(u\ge1\). Thus each row works for arbitrarily large ordinary parameters, not just the sampled starts.

**Corollary.** Combine these eight local certificates with the pinned PR #146 theorem that a least failure of \(P\) cannot be \(7\pmod8\). A least failure must be odd and avoid **83 of the 192 odd residue classes modulo 384**. The previous \(7\pmod8\) restriction alone excludes 48 of those classes. The eight rows supply 35 further distinct classes after removing overlaps. The predicate guards in FM-002 additionally supply classes beyond these eight representatives.

The count is finite exact residue arithmetic. It is not the density of actual Collatz counterexamples or a fraction of the conjecture proved.

## FM-004: known convergent seeds have inductive neighborhoods

This clause explains why a certificate calculus may remove known convergers even when direct balanced affine merger certificates cannot. It uses the **finite convergence implication** from the same pinned `THREE_RAY_SMALLER.md`: for integer \(Y\ge3\), all comparisons \(P(t)\) through

\[
81\left\lfloor (Y+1)/4\right\rfloor
\]

imply convergence of every start through \(Y\). This is an inherited theorem, not a new proof of that implication.

**Theorem.** Suppose the ordinary starts \(r\) and \(3r\) are both certified to reach 1, with first hitting times \(\tau_1,\tau_3\). Then an effectively determined integer \(K\) makes the following true for every \(n\equiv r\pmod{2^K}\), \(n>0\): if all \(P(t)\) for \(1\le t<n\) hold, then \(P(n)\) holds. The base representative \(n=r\) is already certified.

One explicit choice is

\[
K=\max\{9,\,\lfloor\log_2 r\rfloor+1,\,\tau_1+22,\,\tau_3+22\}.
\]

**Proof.** On either seed path append eleven full \(1\to2\to1\) cycles, and let \(L_a=\tau_a+22\), \(q_a\) be the total number of odd inputs, for \(a=1,3\). Set \(M=2^K\). Binary lifting gives, for every \(u\ge0\),

\[
T^{L_a}\bigl(a(r+Mu)\bigr)=1+A_a u,
\qquad A_a=a3^{q_a}2^{K-L_a}.
\]

All prefixes are physical since their initial values differ from the seed by a multiple of \(2^{L_a}\). The affine additive constant is nonnegative, so at the original hitting time \(a3^{q_a-11}/2^{\tau_a}\le1/r\). Consequently

\[
A_a/M\le (3/4)^{11}/r\le(3/4)^{11}.
\]

For \(u\ge1\), let \(Y_a=1+A_a u\). Using \(M\ge512\),

\[
81\left\lfloor(Y_a+1)/4\right\rfloor
\le {81\over4}(A_a u+2)
\le {81\over4}\left((3/4)^{11}+{2\over512}\right)Mu
< Mu<n.
\]

The last strict numerical inequality is an exact rational comparison; its left coefficient equals \(15676011/16777216\). If \(Y_a\ge3\), the inherited finite convergence implication applies using only smaller comparisons; \(Y_a=1,2\) needs no hypothesis. Both arms therefore reach 1. ∎

This is an affine-cylinder consequence of a known seed proof and the inherited finite-range implication. It is **not** a proof that every seed converges or that the neighborhoods form an ordinary all-source cover. The explicit depth depends on the supplied hitting times. It does not contradict the source's unbounded ordinary-clock obstruction.

## Remaining obligation and replay

A complete proof would need a well-founded rule that covers every remaining parameter, or a separate theorem excluding the ordinary integers left outside all certified guards. G, F, H and J leave unhandled parameters; a finite search limit is not a proof of a permanent obstruction. In particular, bounded exploratory graph searches at increasing binary precision retained known convergent centers such as 9 and 37. Those are failures of the attempted search, not failures of \(P\).

The companion script [`fixed_integer_mergers.py`](../../experiments/fixed_integer_mergers.py) checks the eight affine identities coefficientwise, the strict smaller-input guards, the residue count, the adaptive path formulas at bounded and very large ordinary inputs, and the exact rational bound in FM-004. It rejects deliberately altered words and invalid smaller-demand assertions. The checker does not decide universal coverage, and its execution is not a proof-assistant verification.
