# High-odd-grade inverse returns of adjacent ordinary pairs

**PROPOSED.** This packet concerns the positive shortcut map, with one date for either halving or the update \(x\mapsto(3x+1)/2\). It gives a finite description, valid at every clock, of the actual dyadic source cylinders taking adjacent pairs to adjacent pairs at the same odd grade with a bounded number of even departures. The extreme expanding cylinders have an explicit ordinary inverse. The case of unbounded even grade and global convergence remain open.

## 1. The centered determinant

Start the two ordinary arms at \(x,x+1\). Let \(U_i=T^i(x)+1\), \(V_i=T^i(x+1)+1\), and let \(a_i,b_i\) count the original **even** departures before date \(i\). Write \(\epsilon_i=U_i\bmod2,\eta_i=V_i\bmod2\). Then

\[
  2U_{i+1}=3^{1-\epsilon_i}U_i+\epsilon_i,\qquad
  2V_{i+1}=3^{1-\eta_i}V_i+\eta_i .
\]

For \(D_i=3^{b_i}V_i-3^{a_i}U_i\) we have \(D_0=1\) and

\[
  2D_{i+1}=3D_i+\eta_i3^{b_{i+1}}-\epsilon_i3^{a_{i+1}},
  \qquad \eta_i\equiv \epsilon_i+D_i\pmod2.                 \tag{1}
\]

Consider any finite return with \(a_t=b_t=e\) and \(V_t-U_t=s\in\{-1,1\}\). For every earlier date,

\[
                           |D_i|\le 3^e.                              \tag{2}
\]

Indeed the endpoint has absolute determinant \(3^e\). Each of the two terms following \(3D_i\) in (1) lies in \([0,3^e]\) before their difference is taken. Backward application of (1) preserves the interval in (2).

In a run of \(r\) simultaneous original odd departures we have \(2^r D_{i+r}=3^rD_i\). For \(D_i\ne0\), the final determinant is a nonzero integer divisible by \(3^r\). Hence **every such run has length at most \(e\)**. For \(D_i=0\) the entire run stays on the exact relation \(3^{b_i}V=3^{a_i}U\).

## 2. A finite description with arbitrary repetitions

Keep states \((a,b,D)\) with \(0\le a,b\le e\) and \(|D|\le3^e\). Start at \((0,0,1)\). Choose \(\epsilon\in\{0,1\}\), infer \(\eta\) modulo two from (1), and update by (1), discarding states outside the bounds. Accept \((e,e,s3^e)\). Every accepted state path of length \(t\) occurs on exactly one residue class of positive starts modulo \(2^t\). Prescribing the first arm's ordinary parities gives one binary cylinder by the usual parity-word bijection. Induction using the parity congruence in (1) forces the second arm's actual departures on that same cylinder. The terminal formula gives the signed gap at every positive representative.

Delete each self-loop corresponding to \(D=0,\epsilon=\eta=0\). The remaining graph has no directed cycle. Each event with \(\epsilon+\eta>0\) increases \(a+b\). At fixed counts, a remaining step has \(D\ne0\) and increases \(|D|\) by a factor of \(3/2\). At most \(2e\) dates are active, and at most \(2e+1\) intervening nonzero runs each last at most \(e\) dates. Every compressed path therefore has length

\[
                              c\le 2e^2+3e.                          \tag{3}
\]

Each visit to \(D=0\) along this compressed path is an independent site for inserting any nonnegative number of simultaneous original odd departures. The source-cylinder argument proves ordinary realizability for **every** choice of the inserted lengths. An accepting path cannot terminate at zero. Leaving zero consumes one even departure on each arm, since their centered parities agree there. There are at most \(e\) free sites. In fact, for a nonempty set of free sites there are at most \(e-1\): unequal counts at a zero are necessary because equal counts would be an actual merger. At least one solo even departure is therefore required on each arm outside the balanced set of simultaneous departures, using equality of the final counts.

Let \(F_{e,s}(z)\) count the signed ordinary source cylinders by their native clock. An exact finite sum is

\[
               F_{e,s}(z)=\sum_{P} z^{c(P)}(1-z)^{-h(P)},           \tag{4}
\]

where \(P\) ranges over compressed paths to the indicated sign and \(h(P)\) counts their zero sites. In particular the clock coefficients are eventually polynomial for each fixed even grade. Equation (4) counts dyadic **source residues**. Distinct paths may give overlapping ternary **target residues**.

## 3. The extremal cylinders and their complete ordinary inverses

The complete finite recursion (1)–(3) gives the following signed generating functions. The supplied standard-library script computes the finite graph and separately checks its coefficients against literal native trajectories through clock 15.

| Even grade on each arm | Positive final gap | Negative final gap |
|---:|---|---|
| 0 | \(1\) | \(0\) |
| 1 | \(z^2\) | \(0\) |
| 2 | \(z^4\) | \(0\) |
| 3 | \(z^5+z^6\) | \(0\) |
| 4 | \(3z^7+2z^8\) | \((z^6+z^7)/(1-z)\) |

Thus at **every** clock \(t\ge9\) the largest possible common odd grade for an adjacent-to-adjacent return is exactly \(t-4\), and exactly two dyadic source residues attain it. They reverse the order. Both begin with an even departure on the first arm and an odd one on the second. A freely chosen run of simultaneous odd departures follows. The two respective pairs of fixed suffixes in chronological ordinary parity notation are

| Family | Lower-start arm suffix | Upper-start arm suffix | Inserted odd dates |
|---|---|---|---:|
| A | `001101` | `011000` | \(t-7\) |
| B | `00011` | `01000` | \(t-6\) |

For a target pair \((y,y+1)\) the complete reversed identification is \(T^t(x)=y+1,\ T^t(x+1)=y\). Evaluate both formal suffixes at the common centered origin \(U=V=0\) (ordinary value \(-1\)). The upper-start suffix has offset \(1/64\) for A and \(-1/32\) for B; the lower-start suffix adds one to that value. Before the suffix, starting the first arm formally at \(-2\) and the second at \(-1\) puts both at this centered origin after the initial mixed step and all inserted departures. The complete affine slope on each arm is \(3^{t-4}/2^t\). Consequently

| Family | Necessary and sufficient ternary condition | Positive ordinary starting pair |
|---|---|---|
| A | \(3^{t-4}\mid 64y-1\) | \(x+2=2^{t-6}(64y-1)/3^{t-4}\), then \(x,x+1\) |
| B | \(3^{t-4}\mid 32y+1\) | \(x+2=2^{t-5}(32y+1)/3^{t-4}\), then \(x,x+1\) |

These criteria apply for every positive \(y\) and \(t\ge9\). Under the stated divisibility the displayed source is positive. The integer source solves the exact affine endpoint equality, so reduction modulo \(2^t\) puts it in the prescribed first-arm parity cylinder. Equation (1) forces the second arm. Each family is nested at the target, with maximum clock respectively \(4+v_3(64y-1)\) and \(4+v_3(32y+1)\) when the valuation is at least five.

The return gives a physical descent test for a least positive source failing to reach one. Such a source \(n>1\) is odd and \(n\equiv3\pmod4\), since any other parity gives a smaller iterate. Put \(y=(3n-1)/2\), so that \(y+1=Tn\), while the even \(y\) descends immediately below \(n\). If either

\[
               3^7\mid32n-11 \qquad\text{or}\qquad 3^7\mid16n-5, \tag{5}
\]

then the corresponding return applies at \(t=12\): \(64y-1=3(32n-11)\), \(32y+1=3(16n-5)\). The inverse slope \(2^{12}/3^8<2/3\) makes the upper target's positive predecessor \(x<n=(2y+1)/3\) in both formulas. Its path meets the actual path of \(n\), contradicting leastness. Thus neither divisibility in (5) holds at a least failure. This excludes two ordinary residue families by explicit ancestors. An arbitrary least failure need not satisfy (5).

## 4. Scope and source pins

PR 214 at `504d29d399efa941a62006d1ea4635385ce6bb5f`, `research/astra-critical-rigidity-20261128/ordinary/ADJACENT_CYCLE_CLOSURE.md`, gives the static carry description of equally graded adjacent returns and their periodic rational centers. Its `PAIRED_SOURCE_GRADES.md` and `CROSS_GRADE_CLOCK.md` bound unmatched clocks using **odd** departures. Our backward bound (2) treats sparse **even** departures and permits an arbitrarily long shared-odd run exactly on the centered proportionality. The results here use direct finite arithmetic. No density or outside formalization enters the proofs.

The finite grade-four classification uses complete exact enumeration of the bounded graph. The run bound, positive lift, and generating function (4) are written all-scale proofs. The first open step in this descent approach is to control paired returns with unbounded even grades or to combine them with valid forward mergers on the remaining positive sources.
