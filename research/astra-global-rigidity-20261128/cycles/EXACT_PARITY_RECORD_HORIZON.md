# A finite clock for the deepest parity deficit of every positive trajectory

Write \(T(x)=x/2\) at an even input and \(T(x)=(3x+1)/2\) at an odd input. For an ordinary positive integer \(n\) let \(Q_t=Q_t(n)\) count odd departures before native time \(t\), and put
\[
 b_t=2Q_t-t,\qquad h_t=b_t-\min_{0\le i\le t}b_i,
 \qquad \theta=\log_2 3,\quad D=1-\theta/2.
\]
Both the value of \(\min_{t\ge0}b_t\) and its first date are computable by inspecting the actual trajectory only through \(\lceil\log_2(2n)/D\rceil\) shortcuts. This holds on every positive orbit regardless of its fate. More precisely a first strict record at time \(v\), with \(q=Q_v\) and \(k=v-2q>0\), satisfies
\[
      3^k4^v<4n^2 3^v,
      \qquad Dv+\tfrac12\theta k<\log_2(2n).                        \tag{1}
\]
The coefficient \(D^{-1}=4.81884\ldots\) is sharp, with almost full counting exponent for examples in every large octave, under either of two explicit external input packages. The confined-visitor proof below retains its mixing premise. The separate [balanced inverse-block construction](BALANCED_RECORD_ROUTING.md) uses supplied-state finite-policy stationarity and qualitative tilted absolute continuity, without the fine-scale joint-mixing input (J). The upper bound, exact endpoint rounding and finite algorithm below are entirely elementary.

## The largest possible affine correction at a record

Write \(T^t(n)=3^{Q_t}2^{-t}n+e_t\), where \(e_0=0\). The one-step rule is \(e\mapsto e/2\) for an even departure and \(e\mapsto(3e+1)/2\) for an odd departure. The reflected nonnegative integer \(h\) goes to \(\max(h-1,0)\) or \(h+1\), respectively. On every finite parity word,
\[
           0\le e_t\le 2^{h_t}\bigl(1-(3/4)^{Q_t}\bigr).             \tag{2}
\]
At time zero both sides vanish. An even step with \(h_t>0\) halves both sides. With \(h_t=0\) it still halves the correction, leaving the right side unchanged. An odd step preserves (2) because \(1\le2^{h_t}\), so its new correction is at most
\[
 (3/2)2^{h_t}(1-(3/4)^{Q_t})+1/2
       \le 2^{h_t+1}(1-(3/4)^{Q_t+1}).
\]
At a weak running minimum \(h_v=0\), so \(e_v\le1-(3/4)^q<1\) and the physical integer endpoint equals \(\lceil 3^q2^{-v}n\rceil\). At a strict record the final departure must be even and the preceding reflected height is zero. Consequently
\[
 0\le e_v\le\tfrac12(1-(3/4)^q)<\tfrac12,\qquad
 T^v(n)=\left\lfloor3^q2^{-v}n+\tfrac12\right\rfloor .              \tag{3}
\]
The upper inequalities before the strict signs are optimal for the supplied length and grade. On weak records with \(k=v-2q\ge0\), the word \(0^k(10)^q\) attains the weak bound. On strict records with \(k\ge1\), the word \(0^{k-1}(10)^q0\) attains the strict bound. The block \(10\) acts by \(x\mapsto(3x+1)/4\). Each finite word has a positive integer representative by parity coding. These are optimal affine bounds even if the representative is larger than the source cap of a separate counting problem.

Since the endpoint in (3) is positive, \(3^q2^{-v}n>1/2\). Squaring and using \(2q=v-k\) gives (1). In addition, the endpoint at any strict record satisfies \(T^v(n)\le n2^{-k}(3/4)^q+1/2\) with strict inequality in the correction term. At the first negative crossing it is at most \(\lceil n/2\rceil\). The deterministic product bound \(1\le T^t(n)\le n2^{-t}4^{Q_t}\) gives \(b_t\ge-\log_2 n\). Thus its lattice-valued global minimum exists. Unless that minimum is zero its first attainment is a strict record, and (1) applies. Any new lower record after the displayed uniform clock would violate the same estimate. The cutoff can be found using integer arithmetic alone: stop by the first \(t\) with \(4^t\ge4n^2 3^t\), or use the stronger test \(3^k4^t\ge4n^2 3^t\) to exclude a future first descent to \(-k\). The ratio \((4/3)^t\) increases strictly.

One useful decidable target is \(\mathcal B=\{y\ge1:2Q_s(y)\ge s\ \text{for every }s\ge0\}\). Every source enters it at the first date of its deepest deficit by count additivity. If the minimum is zero the initial state already belongs to it. Each source outside \(\mathcal B\) therefore reaches a strictly smaller integer; its first negative record alone suffices. By the standard parity bijection, the first \(m=\lfloor\log_2N\rfloor\) true bits from \([1,N]\) realize each binary word at most twice. Only \(\binom{m}{\lfloor m/2\rfloor}\) words have every partial sum nonnegative, by reflection. Consequently \(\#(\mathcal B\cap[1,N])\ll N/\sqrt{1+\log N}\). This computes and bounds a necessary search set for a least counterexample and gives no exclusion for every source in that set.

## Sharpness on genuine terminating sources

Use Weaver 211 v1, Theorem 2, with its explicit (J) premise for the lower estimate. For each sufficiently large fixed integer \(B\), set \(M=2B+1\) and \(a=2^M\). This fixed even target is prime to three. In every sufficiently large octave \([X,2X)\), the theorem with \(Y=X/a\) supplies \(\gg_B X^{1-C/B^2}\) odd-unit starts with one common first visit to \(a\) at
\[
 \tau=2\log_{4/3}(X/a)+O_B(1)=D^{-1}\log_2 X+O_B(1),
 \qquad |b_t|\le B\quad(0\le t\le\tau).
\]
The next \(M\) departures all halve the state, ending at one with \(b_{\tau+M}=b_\tau-M<-B\). The terminal value is strictly below all earlier ones, including those in this last string. The subsequent \(1,2\) cycle alternates between this minimum and one more. Thus \(v=\tau+M\) is the exact first lifetime minimum for each supplied positive start, at the sharp leading clock. Taking fixed \(B\) large makes the exponent exceed any prescribed \(1-\epsilon\). Both the external input and this sharpness application are written arithmetic/probability results. [Weaver, *Parity discrepancy before the first Collatz visit to 1*, Theorem 2 and §§4.1–4.2](https://rstation.ai/problems/collatz/papers/211/v1)

Weaver 191 uses tilted records of the logarithmic multiplier to bound affine errors by a geometric sum. Weaver 211 §2.3 already bounds an outward affine offset by \(2^B(1-(3/4)^q)\) on a width-\(B\) discrepancy strip. The elementary arguments here specify the *running* reflected deficit, obtain the strict half-unit for every new record, and use positivity to bound the time of every source's deepest deficit. Weaver 211 §3.4 also treats two-sided bounded discrepancy for the full trajectory. The one-sided lifetime minimum here remains defined on all positive paths. [Weaver, *Collatz first passage in translated intervals*, §2](https://rstation.ai/problems/collatz/papers/191) · [Weaver, Parity discrepancy, §§2.3, 3.4](https://rstation.ai/problems/collatz/papers/211/v1)

## Lean verification scope

[ParityRecordHorizon.lean](ParityRecordHorizon.lean) proves the actual native affine identity, reflected-counter witness, weak and strict correction bounds and the integer strict-record inequality. [GlobalParityMinimum.lean](GlobalParityMinimum.lean) propagates the exact cutoff test and proves that, for every future date, some date in the finite prefix has no larger centered grade. Both modules were freshly compiled and axiom-audited. The optimal correction envelope, logarithmic restatement, counting bound and source-qualified sharpness argument remain written mathematics.
