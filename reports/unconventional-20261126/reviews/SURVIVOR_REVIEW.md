# Independent check of the non-Markov coding and arbitrary-subshift argument

I reviewed the proposed `LOCALIZED_SURVIVOR_PRESSURE.md` at SHA-256 `07aaa763d404b5b034e4b5db0337ad65a99408fdd592179164332959fbc8b58d`, taking O15's finite-mean Markov entropy dichotomy from the separate written proof. The argument preserves an arbitrary closed, two-sided subshift over a finite alphabet. I found no need for a finite-type assumption.

## The stationary entropy calculation

For a stationary ergodic two-sided process with integrable positive gap, write $W_n=E_0^{n-1}$, let $X_j$ be the ternary coding of its future labels, write $B_n=X_0[n]$ and let $\mathcal G$ be its entire label past. Set $\beta=H(E_0\mid X_0,\mathcal G)$. At time $j$, the sigma-fields given by $(X_0,\mathcal G,E_{<j})$ and $(X_j,E_{<j},\mathcal G)$ coincide. This follows by the mutually inverse affine maps along the observed letters. The chain rule gives $H(W_n\mid X_0,\mathcal G)=n\beta$. Meanwhile $(B_n,\mathcal G,E_{<j})$ determines $X_j[n-j]$ and the full past at time $j$. It follows that
$$
 H(W_n\mid B_n,\mathcal G)\le
 \sum_{d=1}^n H(E_0\mid X_0[d],\mathcal G)=n\beta+o(n).
$$
The last convergence uses finite single-letter entropy, which follows from finite mean. Since $B_n$ is determined by $W_n$, the chain identity
$$
 I(W_n;\mathcal G\mid B_n)=I(W_n;\mathcal G)-I(B_n;\mathcal G)
 \le H(W_n)-n h_E=o(n)
$$
is valid. This proves $I(W_n;X_0\mid B_n)=o(n)$ and $H(B_n)/n\to h_E-\beta$. In (7) of O15 the posterior must now condition on the entire label past as well as $X_0$. The signed Bayes identity and $L^1$ log convergence remain valid with that conditional law. The subsequent entropy, fixed-total, typical window and finite-group steps need no conditional Markov property beyond the estimates just replaced. This proves the claimed non-Markov dimension formula.

## Extracting a measure for the actual subshift

Fix a maximizing residue at depth $n$. Extend each distinct word in its fiber to any two-sided element of the closed subshift $S$. Existence is precisely the definition of $\mathcal L_n(S)$. Uniform selection gives a law $\xi_n$ whose full initial ternary codes can differ. They share the residue $B_n$. For an interior time $m\le j\le n-h$, the realized $j$-letter prefix, together with this common constant, determines both the preceding $m$ letters and $X_j[h]$. Thus
$$
 H_{\xi_n}(E_j\mid E_0^{j-1})
 \le H_{\xi_n}(E_j\mid E_{j-m}^{j-1},X_j[h]).
$$
All omitted times together cost at most $(m+h)\log|D|$. The conditional entropy on the right is concave in the joint law, so its time average is bounded by the corresponding conditional entropy for $\nu_n=n^{-1}\sum_{j<n}\sigma^j_*\xi_n$. Any weak limit stays in $S$ and is invariant. For fixed $h,m$ the joined variables in that conditional entropy are finite and locally constant on $S$. Hence the limit gives the same upper bound under $\nu$. Now send $h=m\to\infty$.

For the resulting possibly nonergodic law, its invariant field lies in the completed past-label field. The conditional entropy given $(\mathcal G,X_0)$ consequently averages the same conditional entropies on ergodic components. Each component has entropy rate at most $h(S)$ by the cardinalities of the finite languages. Combining this bound with the dimension formula gives the proposed exponent $\max(0,h(S)-\log3)$. The elementary matching lower bound averages word counts over the $3^n$ ordinary target residues. Starting in a sufficiently large odd representative realizes each compatible word by positive odd states. The elementary unit/doubling argument gives all specified residues inside each ordinary merge component.

A two-point subshift demonstrates the significance of the common-residue qualification. Take the constant exponent sequences $1^\mathbb Z$ and $3^\mathbb Z$. Their distinct exact codes are $-1$ and $1/5$. Both reduce to $2$ modulo three, and both single-letter words are legal at the ordinary endpoint $5$. There is no exact ternary code in this subshift shared by those two words. Precisions of $n-j$ digits suffice for the extraction proof.

For the final bounded-drawdown application, all letters satisfy $e\le\log_2 3+C$. Every admissible finite block extends by constant ones on both sides. Adding an outside one to a tested interval increases its clock sum by one and the linear allowance by $\log_2 3>1$. Thus the actual language is a closed subshift, and its elementary composition count gives the stated strict entropy bound.

The independent control script `review_survivor.py` uses a four-letter marked even shift whose minimal forbidden words include arbitrarily long odd runs between markers. It computes maximum ordinary fibers through eight letters (4, 8, 11, 15, 22, 29, 37, 51) and checks the prefix-determination and conditional entropy steps directly at 141 interior positions. Nineteen comparisons have a strict conditioning gap. Seventy-two finite time-averaged inequalities pass. The two exact rational codes above are checked separately. The finite measurements do not certify the limiting exponent.
