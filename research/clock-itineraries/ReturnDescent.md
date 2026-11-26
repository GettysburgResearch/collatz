# Canonical three-odd representatives of every Mersenne source

Write $T(n)=n/2$ for an even input and $T(n)=(3n+1)/2$ for an odd input. Let $M_t=2^t-1$. Two positive integers meet if some ordinary iterates are equal, allowing independent clocks.

## All supplied positive exponents

For every $t>0$, there are positive integers $Y,H$ such that $Y\equiv17\pmod{48}$, $Y<2^H$, $H\le t+2081$, and $Y$ meets $M_t$. The actual orbit of $3Y$ reaches 1 at clock $H$ with exactly three odd departures. In particular, any bad Mersenne source would give a canonical bad lower source with an unconditionally good three-odd upper. [Kernel theorem `mersenne_representative`](ReturnDescentRows.lean)

The row-specific upper clock bound is $H\le\max(18,t+c(t))$. Here $c(t)\le2081$ comes from 81 checked templates indexed by the odd member of the exponent pair, modulo 162. The two peaks for $M_{2a+1}$ and $M_{2a+2}$ meet two ordinary steps after their respective initial ascents. This allows each template to serve both neighboring exponents. [Clock charge and row data](ReturnDescentRows.lean) · [Physical neighbor merger](ReturnDescent.lean)

To discover the rows, vary the gap $e$ in the known upper family $81Y=2^H-15-2^{e+2}$. Use the signed rational $-(15+2^{e+2})/81$ to find a lower prefix reaching $-1$. If that prefix has length $h$ and $p$ odd departures, its positive lift reaches $2^{H-h}3^{p-4}-1$. The next $H-h$ steps reach $3^{H-h+p-4}-1$, the peak of $M_{H-h+p-4}$. Thus one row covers one exponent residue, with exact known cost $h-p+4$. The chosen gap values include values above 48. The upstream bound $e\le48$ applies to a candidate least canonical failure. Each present row is a constructed visitor with its own positive integral source and its own verified upper certificate. [Earlier three-odd shape](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-unconventional-20261126/renormalization/PHASE_RETURN.md)

Lean checks the two physical words at each numerical base, and $2^{162}\equiv1\pmod{243}$ lifts both formulas under $H\mapsto H+162j$. The positive reference computations cover every exponent once its template is available. For the 300 earlier odd exponents below their row starts, Lean checks actual hits of $M_t$ at 1 and uses the canonical source 3233, whose upper hits 1 in 18 clocks and three odd departures. [Full finite coverage](ReturnDescentRows.lean) · [All-height lifting argument](ReturnDescent.lean)

## Pointwise return to a smaller canonical source

Fix $m=11+162j$ and the original hard parent $z=(2^{m+7}-271)/81$. Lean proves $T^7z=M_m$, $z>2^m$, $z\equiv17\pmod{48}$, and that $3z$ reaches 1 at clock $m+7$ using three odd departures. If a supplied $M_t$, $t>0$, meets $M_m$ and $\max(18,t+c(t))\le m$, the original $z$ meets a strictly smaller canonical $Y$, and $3Y$ reaches 1 in at most $m$ clocks with three odd departures. In particular, every merger with $t+2081\le m$ suffices. This implication uses the supplied two paths and makes no leastness assumption. [Kernel theorems `return_of_earlier` and `return_of_gap`](ReturnDescentFixed.lean)

At the preassigned exponents $m=12\cdot 2^{18k}-1$, Lean supplies this three-odd return for 183 of the first 192 positive parameters, including each $2\le k\le79$. The nine parameters outside this particular table are $1,80,113,130,135,138,150,159,180$. The test computes $b=3^{m-d}\bmod2^h$ by modular squaring and verifies both the actual endpoint and the augmented odd count on the two ordinary representatives $3^d b-1$ and $b-1$. Equality of both fields transports the merger to the original peaks. At $k=29$, for example, $d=309$ and $h=22640$. [Complete fixed-parameter table](ReturnDescentFixed.lean)

Every supplied upper certificate transfers. If $3z$ hits 1 at clock $G$ with $p$ odd departures, then $G=m+7+2d$ and $p=3+d$ for some $d$. Running $3Y$ for $H+2d$ steps uses the same $p$ odd departures and saves at least seven clocks. The original triple reaches $2^{m-2}$ after nine steps, which fixes its first upper hit and leaves only laps of the $1,2$ cycle. [Kernel theorem `transfer_upper_hit`](ReturnDescent.lean)

PR 192 proved that each of these original exponents delays a merger with every earlier peak through independent clocks $18k+4$. Its finite repair checker covered the first thirty, with two canonical upper transfers and twenty-eight uses of the leastness floor. The present witnesses give actual three-odd upper hits at the supplied sources. [Prior delayed-source theorem and comparisons](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/descent/PAID_DELAY_REPAIRS.md)

## The first delayed parent

At $k=1$ the supplied exponent is $m=3{,}145{,}727$ and $z=(2^{3{,}145{,}734}-271)/81$. Seven shortcuts reach $2^m-1$ and the next $m$ odd departures reach $3^m-1$. An ordinary block computation from that peak reaches 1 after exactly $24{,}052{,}486$ further steps, with $12{,}029{,}702$ odd departures. Thus $z$ itself reaches 1 at clock $27{,}198{,}220$. An independent variable-run evaluator with 383-bit blocks checked firstness by keeping the completed blocks strictly above 1 and testing every state in the scalar tail. [Independent first-hit replay](mersenne_parent_replay.py)

The file divides the trajectory into 48 segments. A serial native Lean run checked the 48 concrete segment proofs before hitting a recursion limit while joining them. An explicit balanced join was then checked separately for arbitrary checkpoints with exactly these segment lengths. The complete corrected file has a separate, longer verification run. Elaboration computes proposed intermediate numerals. The kernel checks each segment from its stated start, and the ordinary iteration law joins the results. The theorem asserts an exact hit. The separate 383-bit first-hit replay also checks all earlier times. The standalone Lean source has SHA-256 `1a04c04c65dba2cce845498058c66e4429b802e0a28f1ba92d2b52890c508121`. [Long Lean replay](long/ReturnDescentMillion.lean)

To reproduce the independent Lean check from `research/clock-itineraries` with Lean 4.34.1 on the executable path, use a fresh object directory.

```sh
proof_objects=$(mktemp -d)
export LEAN_PATH="$proof_objects${LEAN_PATH:+:$LEAN_PATH}"
for module in TernaryItinerary BasinTransport TowerFrontierAffine ReturnDescent
do
  lean -j1 -DwarningAsError=true -DautoImplicit=false -DElab.async=false \
    -o "$proof_objects/$module.olean" "$module.lean" || exit 1
done
lean -j6 -DwarningAsError=true -DautoImplicit=false -DElab.async=true \
  -o "$proof_objects/ReturnDescentMillion.olean" long/ReturnDescentMillion.lean
```

These statements leave open whether each specified hard source meets an earlier Mersenne at an affordable residue and whether every canonical three-odd parent converges. The representative theorem transfers an actual lower label. A known upper hit alone gives no lower hit.
