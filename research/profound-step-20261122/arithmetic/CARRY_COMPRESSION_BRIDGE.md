# Carry growth, exact repetitions, and the fixed-source boundary

**Status: written arithmetic reconstruction and bridge test. Full Collatz
remains OPEN.** This note compares the two new finite ordinary mechanisms:
the power-block budget in `BlockCompression.lean` and the arbitrary-debt
identities in the merger packet. It also constructs fully certified sources
with unbounded intermediate debt. No new infinite-orbit or capture premise is
asserted, and no extra Lean theorem is claimed for the construction below.

## 1. The two actual words in the explicit debt family

For \(k\ge1\), the merger note chooses

\[
 v_k=2^{k+2},\qquad r_k=\frac{2^{16k+2}+1}{5},
 \qquad n_k=9r_k+2.
\]

The source follows the parity word \((100)^{5k}\), while the target
follows \((11100)^{3k}\). Both statements concern the first \(15k\)
ordinary shortcut clocks. The exact endpoints satisfy

\[
 u_k=T^{15k}r_k=\frac{3^{5k}2^{k+2}+1}{5},
 \qquad
 z_k=T^{15k}n_k=\frac{3^{9k+2}2^{k+2}+19}{5},
\]

and therefore

\[
 z_k=3^{4k+2}u_k-\frac{3^{4k+2}-19}{5}. \tag{CB-1}
\]

The source has exactly gap three at each of the \(5k\) odd steps,
because every intermediate odd value has numerator divisible by five and
is odd, and its adjacent identity is \(3r_j+1=8r_{j+1}\). The target
word follows from the exact five-clock identity at the rational offset
\(19/5\), with ordinary integer inputs at every clock. This is the
ordinary content of `ordinary_debt_amplification`.

The debt exponent \(4k+2\) grows without bound, but each temporal word
still consists of only **one** power block. This is consistent with the
compression theorem. In fact, for \(k\ge1\),

\[
 \lfloor\log_2 r_k\rfloor=16k-1,
 \qquad \lfloor\log_2 n_k\rfloor=16k+2.
\]

The source version of BC-7, with atom length three, allows
\(15k\le16k+6\). The target version, with atom length five, allows
\(15k\le16k+13\). The source height pays for the long repetitions.
This family does not force its number of power blocks to grow.

## 2. Why one fixed source cannot stay in these two cylinders forever

The affine maps of the two words are

\[
 F_{100}(x)=\frac{3x+1}{8},
 \qquad F_{11100}(x)=\frac{27x+19}{32}.
\]

If an ordinary \(r\ge1\) follows \((100)^j\), iteration gives

\[
 5\,2^{3j}T^{3j}r
 =3^j(5r-1)+2^{3j}.
\]

The actual endpoint is integral and \(3^j\) is odd, so

\[
 2^{3j}\mid5r-1,
 \qquad 3j\le v_2(5r-1). \tag{CB-2}
\]

Similarly, a target \(n\) following \((11100)^j\) must satisfy
\(2^{5j}\mid5n-19\). For \(n=9r+2\),

\[
 5n-19=9(5r-1),
\]

so both words spend the **same fixed finite binary divisibility budget**.
In the combined family this yields

\[
 15k\le v_2(5r-1). \tag{CB-3}
\]

For a fixed positive ordinary \(r\), the right side is finite. Unlimited
residence would force \(5r-1=0\), whose solution is not an ordinary
integer. After the source changes its word, a new block may have a new
displacement budget. Controlling these successive changes, together with
the complete certificate grade, is the additional step required for a
global argument.

## 3. Fully certified sources can also have unbounded intermediate debt

The explicit \(r_k\) above was not given a complete convergence certificate
in the merger note. That distinction matters when a proposed state-space
bound is restricted to complete source certificates. The following modified
family supplies such certificates by a finite elementary construction.

Fix \(k\ge1\) and put \(m=5k+1\). Choose an even integer \(h\ge4\)
such that

\[
 5\,2^h\equiv8\pmod{3^m}. \tag{CB-4}
\]

Such an \(h\) is effectively available without a primitive-root theorem
as a black box. Start with \(h_1=4\). Suppose an even \(h_j\ge4\)
solves (CB-4) modulo \(3^j\), and put
\(R=(5\,2^{h_j}-8)/3^j\). The elementary binomial induction gives

\[
 4^{3^{j-1}}\equiv1+3^j\pmod{3^{j+1}}
 \qquad(j\ge1).
\]

The base case is \(4=1+3\). Cubing the statement for \(j\) gives the
one for \(j+1\), since its remaining binomial terms are divisible by
\(3^{j+2}\). Choose the unique \(t\in\{0,1,2\}\) satisfying
\(R+2t\equiv0\pmod3\), and set

\[
 h_{j+1}=h_j+2t3^{j-1}.
\]

Then \(2^{h_{j+1}-h_j}\equiv1+t3^j\pmod{3^{j+1}}\), and
\(5\,2^{h_j}\equiv8\equiv2\pmod3\) proves the next congruence.
Thus \(h=h_m\) is even, at least four, and is computed after finitely
many explicit lifts.

Define

\[
 u=\frac{2^h-1}{3},\qquad
 v=\frac{5\,2^h-8}{3^{5k+1}},\qquad
 r=\frac{2^{15k}v+1}{5},\qquad n=9r+2. \tag{CB-5}
\]

Here \(u\) is a positive odd integer because \(h\) is even. The
congruence makes \(v\) a positive integer; moreover \(8\mid v\),
since its numerator is divisible by eight and its denominator is odd.
The identity

\[
 3^{5k}v=5u-1
\]

and \(2^{15k}\equiv3^{5k}\pmod5\) show that \(r\) is integral.
For \(0\le j\le5k\), put

\[
 r_j=\frac{3^j2^{15k-3j}v+1}{5}.
\]

Every numerator is divisible by five: modulo five its first term equals
\(3^{5k}v\). It is odd because \(8\mid v\), so all \(r_j\) are
positive odd integers. The identities

\[
 3r_j+1=8r_{j+1}\quad(j<5k),
 \qquad r_{5k}=u,
 \qquad3u+1=2^h
\]

give the complete, literal ordinary odd-gap certificate

\[
 \boxed{\underbrace{3,\ldots,3}_{5k\text{ gaps}},h}
 \qquad\text{from }r\text{ to }1. \tag{CB-6}
\]

The same formal AC6 identity applies to these integers. After the first
source gap three, the target satisfies
\(T^3(9r+2)=81r_1-1\), a legal carry state with exponent four and debt
one. Subsequent source gaps use the arbitrary-debt rule. After the
\(5k\) gaps, the target again has exponent \(4k+2\), debt
\((3^{4k+2}-19)/5>0\), and

\[
 z-8u-1\ge\frac{4\,3^{4k+2}-26}{5}>0. \tag{CB-7}
\]

Thus no fixed bound on **intermediate** debt exponents covers even all
complete certified sources. The consumed prefix has maximum gap three,
so its paid padding permits only \(e\le2\), whose largest active
interval ends at \(8u+1\). Equation (CB-7) is an actual endpoint
failure of that prefix's capture test, not merely failure of a convenient
coefficient inequality.

The final gap \(h\) is not bounded by four. It remains in the supplied
certificate and is a possible resource for other rules. This construction
does not refute a bound restricted to the residual alphabet-four problem,
does not show failure of eventual capture, and does not produce a failed
Collatz source.

## 4. The target itself has ordinary descent

The debt growth is relative to the faster-decreasing source. For every
instance above with \(k\ge1\), put
\(w=9\,2^{15k-5}v>0\). Then

\[
 5n=32w+19,
 \qquad5T^5n=27w+19,
 \qquad\boxed{n-T^5n=w>0.} \tag{CB-8}
\]

Equivalently the target lies in the residue class \(23\pmod{32}\),
whose exact five-clock map is
\(T^5(32a+23)=27a+20<32a+23\). This is a successful ordinary descent
class. Its convergence follows whenever the requisite smaller ordinary
sources are already covered by a valid induction.

Consequently these families test a fixed intermediate-debt abstraction and
the particular literal-prefix capture rule. They are compatible with a
combined proof using ordinary descent and other compatible ranks. The
power-block budget correctly accounts for their finite residence, but it
does not by itself turn that ordinary descent into a decrease of the
inherited complete-source certificate grade. A successful combined induction
must establish that compatibility rather than substitute one rank for the
other.

## 5. Independent reconstruction scope

The arithmetic lane reconstructed the merger packet's AC1–AC6, the
highest-changed-grade cancellation in AC3, the all-length
\(1\{2,3\}^{*}2\) transport and padding rule, and the explicit ordinary
\(r_k\) valuation recipe. The exact affine constants, gap clocks, retained
tail and padding guard agree. This review concerns those mathematical
arguments; it does not supply their missing universal successful dispatcher.

The fully certified extension (CB-4)–(CB-7) is the additional written
construction of this note. The finite congruence lifting was reconstructed
above, rather than assumed from an external density or existence theorem.
The exact finite carry and compression identities are the separately
compiled Lean inputs. Their successful compilation does not certify the
new written infinite family or the global closing inference.
