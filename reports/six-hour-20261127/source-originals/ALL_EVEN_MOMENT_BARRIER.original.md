# Why every even independent-segment moment misses the cubic threshold in the full binary model

Fix a near-critical mechanical slope and arbitrary intercept and entrance/exit bits. Let S be the full set of binary layer paths of length a, with no extra forced-zero cap. For every fixed even q≥2, the actual quantized segment counting measure F at any grid precision h satisfies
[
 \int|\widehat F|^q\ \gg_q\ 3^{(q-1)(1/3+1/1200)a}.
 \tag{1}
]
Frequency averaging is normalized. The assertion concerns the unnormalized actual source contribution from one conditioned segment, in the notation of FOUR_BRIDGE_BINARY_CYCLE_BOUND.md. It holds at every sufficiently large a, uniformly in fixed bits, intercept, and the same compact slope bracket. It excludes a uniformly subcubic count obtained solely by raising the individual even moment order, or by using Hölder with different such even orders at the several segments. It leaves the mixed product of transforms at the same frequencies, restriction to a smaller family, and other architectures open.

## Transfer proof

For q=2k let A_{2k} count ordered 2k-tuples in S with equality of the two coordinatewise sums of k bits. This implies equality of the two k-sums of ordinary segment numerators, at every k; no converse involving a carry is needed for this lower bound. A fixed ordinary k-sum fixes the sum of the k unquantized circle contributions modulo one, since 3^n R_Z≡−dB mod 2^m in the raw segment notation. Hence the k corresponding quantized contributions add to at most k consecutive residues: summing k within-cell remainders costs an integer carry between 0 and k−1. Within each ordinary k-sum fibre Cauchy gives a grid collision contribution at least its squared population divided by k. Overlap between different fibres can only increase the grid energy. In particular ∫|F̂|^{2k}≥A_{2k}/k. For k=2 this sharpens the four-copy obstruction: the grid and ordinary energies differ by at most a constant factor whenever the imported upper separation applies.

Given the common grade j∈{0,…,k} of the two k-vectors, a descending transition from grade s to j has binom(s,j)² choices, while an ascending transition has binom(k−s,j−s)² choices. These are the full aggregate transitions for coordinatewise equality. The same three short mechanical return words from UNRESTRICTED_BINARY_FOURTH_MOMENT.md can be used, with no projection to grade zero at their ends. The finite checker higher_moment_barrier.py multiplies the exact integer matrices at k=1 and k=3 on positive vectors; the previously supplied k=2 product handles q=4. It yields
[
 A_2\gg3^{(21/50)a},\qquad
 3^{(201/200)a}\ll A_4\ll3^{(5031/5000)a},\qquad
 A_6\gg3^{(16749/10000)a}.
]
Both partial end words are bounded. A bounded entrance/exit fragment containing both mechanical letters makes every grade-to-grade transfer positive, justifying both fixed cut bits. The q=6 certificate only counts genuine coordinatewise equalities, whose six grade differences could otherwise also generate nonzero ternary carries.

For all larger k form the multivariate character polynomial P(v)=Σ_{z∈S}exp(2πi⟨v,z⟩) on the a-dimensional torus, using the a contributing bits; the single fixed terminal bit contributes the same constant to each path. Then ∫|P|^{2k}=A_{2k} exactly by ordinary orthogonality on this auxiliary torus. Convexity of q↦log∫|P|^q gives
[
 A_{2k}\ge A_6^{k-2}/A_4^{k-3},\qquad k\ge3.
]
The base-three exponential slope between q=4 and q=6 is at least (16749/10000−5031/5000)/2=6687/20000>1/3+1/1200. Also 16749/10000>5(1/3+1/1200), 201/200>3(1/3+1/1200), and 21/50>1/3+1/1200. Equation (1) follows. No assumption about the sixth quantized sum's converse or the exact fractional Fourier moments is used.

For the standard nearly whole-word architecture of r equally long real segments, Hölder with even orders q_j obeying Σ1/q_j=1 pays at least 3^{(r−1)(1/3+1/1200)a} in the product of its individual norms, while Y≈3^{(r−1)a} up to the usual small placement slack. More generally take durations a_j≤h/θ+O(1) at common binary precision h, a finite number of fixed cuts, and pay full ordinary population on the unselected margins of total odd length L. With this unweighted full-population choice those margins grow at least as 3^{(21/50)L} up to bounded end factors. Then Σ a_j/q_j≤h/θ+O(1) implies that the product-plus-margins costs at least 3^{(1/3+1/1200)(L+Σa_j−h/θ)} up to constants. This is a limitation of these estimates. A genuinely smaller joint convolution atom need not approximate the Hölder upper bound.

Weaver Paper 145 §12 credits a different general population floor for independent segments. Here the floor above 1/3 uses this particular six-grade coordinate equality model at orders 2,4,6, positive return cones, and a torus moment interpolation. It does not certify any all-width cycle.
