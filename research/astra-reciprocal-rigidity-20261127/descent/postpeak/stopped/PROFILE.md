# The post-ascent first-meeting profile

A common probability model describes the first ordinary smaller-orbit meeting across **all** postpeak choices. Its accuracy holds in total variation through a window growing linearly with the initial ascent. In this experiment \(H\) counts prescribed initial odds; the next original letter is free.

Take independent fair letters \(W_1,W_2,\ldots\) and a Haar-uniform \(N\in\mathbb Z_3\). Let \(w_j=W_1\cdots W_j\), including the empty word at \(j=0\). Declare the model protected through \(j\) exactly when \(w_j\) is maximal in its signed-offset fibre and \(N\) passes every reflected-origin guard in \(p(D_{w_j})\). The protection events decrease. Indeed appending the same letter \(a\) to equal-length words with the same signed offset preserves that equality and their grade difference, because \(C_{vE}=C_v\), \(C_{vO}=3C_v+2^{|v|}\). Any nonmaximal prefix stays nonmaximal, and while two successive prefixes are maximal their deficit sets only grow. Define \(\tau=0\) if protection already fails at \(j=0\), and otherwise let \(\tau\) be the first \(j\) when it fails, or infinity if it never fails.

For ordinary positive integers sampled by relative natural density on the cylinder \(O^H\), analogously set \(\tau_H=0\) if a smaller source has already visited the original orbit through \(H\), and otherwise take the first subsequent post-ascent index of such a visit. Every visitor clock is allowed. The ordinary law of any finite binary tail and truncated \(\tau_H\) exists by the finite-deadline transfer. For \(H\ge400,\ 6(T+1)\le H\), compare the joint laws of the first \(T\) post-ascent bits and the meeting position grouped into bins \(0,\dots,T,>T\). Their total variation distance is at most
\[
                (T+1)\,\epsilon_H,\qquad
                \epsilon_H=2^{5-H/24}+\tfrac23\,2^{-\lfloor H/2\rfloor}.       \tag{1}
\]
In particular it tends exponentially to zero even for the entire window \(T=\lfloor H/6\rfloor-1\). This first takes the ordinary source-height density on each cylinder for the chosen \(H\). The proof does not give the same growing-window distribution in a single prescribed finite integer sample.

Condition on one complete \(T\)-word. Its ordinary and model probabilities are both \(2^{-T}\). For each \(j\le T\), the ordinary conditional probability of survival through \(j\) is \(p_{H,w_j}\), because imposing a further finite dyadic tail does not change any finite ternary test or its all-clock limit. The model conditional probability of the same event is \(p(D_{w_j})\) if the prefix is maximal and zero otherwise. The error at each deadline is bounded by \(\epsilon_H\), using the two sides of the stopped law and the indicated uniform word range. For a nonmaximal prefix both values vanish. Subtract consecutive cumulative probabilities to obtain the exact-position bins; each interior bin has error at most \(2\epsilon_H\) and the two extremes at most \(\epsilon_H\). Half the sum of absolute errors is at most \((T+1)\epsilon_H\). Averaging over complete words proves (1). [Stopped law and transfer](STOPPED_LAW.md)

## A lower tail and an infinite mean

The limiting survival probability through fixed \(j\) is
\[
 S_j=2^{-j}\sum_{\substack{|w|=j\\w\ \mathrm{maximal}}}p(D_w)
 \ \ge\ s\,2^{-j}\binom j{\lfloor j/2\rfloor},
 \qquad s=284051/829440 .
\]
At the central weight every word has a distinct intercept, since its parity word is determined by its integer clock and affine numerator. They give that many distinct signed-offset fibres; each fibre has a maximal member. Each such member has common protection mass at least \(s\). This lower bound is of order \(j^{-1/2}\). By the tail-sum formula the model variable has \(\mathbb E[\tau]=\infty\). The companion synchronization argument excludes an atom at infinity and yields the matching upper tail. [Sharp meeting tails](SYNCHRONIZATION.md)

For the ordinary process, each maximal word of length \(j\le H/6-1\) protects more than one third of its cylinder. Thus
\[
 \mathbb E[\min(\tau_H,T+1)\mid O^H]
       \ \ge\ \tfrac13\sum_{j=0}^T2^{-j}\binom j{\lfloor j/2\rfloor}
       \ \gg\sqrt{H},\qquad T=\lfloor H/6\rfloor-1 .
\]
All these are conditioned source frequencies and source times. An individual forward trajectory can escape to later mergers outside the window. Weaver 178/v1 already gives the protection density on a prescribed pure ascent and a future waiting-time law **from a first meeting to descent** on a different selected family. [Weaver 178/v1 §§7–8](https://rstation.ai/problems/collatz/papers/178/v1)
