# Spectral information in the ordinary Collatz graph

**Status.** Exploratory written proofs, PROPOSED. The shortcut map and all counted vertices are positive ordinary integers. The ternary inverse tree in OP-I1 is explicitly unfolded before it is compared with the ordinary graph. The Collatz conjecture remains open.

| Question | Result | Proof |
|---|---|---|
| Could an escaping component force a new local spectral value? | For any bounded self-adjoint finite-propagation operator given by a local rule with fixed labels modulo $2^a3^b$, the complete spectrum of an acyclic component already occurs in the essential spectrum of the basin of 1. The essential spectrum of the entire graph equals that of this known basin, even allowing infinitely many other cycles. | [OP-L1–L3](LOCAL_SPECTRUM.md) |
| Is the undirected graph expansive? | Its unit subgraph has edge expansion at least $1/7$ and $L_U\ge I/294$. Every component of the full graph has pendant halving chains and essential spectrum containing $[0,4]$. | [OP-G1](CORE_HEAT.md) |
| What does long-time diffusion detect? | On the unit subspace, $P e^{-tL}P^*=(2\sqrt\pi)^{-1}t^{-3/2}Q+O(t^{-5/2})$ in norm, $Q=L_U^{-1}1_H L_U^{-1}$, $H=\{u\equiv5\bmod9\}$. Its diagonal stays uniformly positive; its marked two-point entry detects common-component membership. | [OP-G2–G3](CORE_HEAT.md) |
| Is there arithmetic data in the marked Green entry? | A computable ternary hitting probability in $[1/2,7/8]$ gives its exact product along each good off-cycle forward path. On every good doubling ray the ordinary height exponent is the same, rigorously between 0.387648 and 0.387892. All-odd prefixes arbitrarily far inside the known basin exclude comparability to a single nonincreasing function of height. | [OP-I1–I3](IMPEDANCE.md) |
| Can a numerical height bound hold globally? | Every unit satisfies $G(n,2)/G(2,2)\le 2n^{-0.38764}$. The optimal global upper exponent lies between 0.38764 and 0.387892. The reverse one-step barrier fails even on good all-odd prefixes. | [OP-H1–H2](HEIGHT.md) |
| How many marked entries can be large? | On all ordinary units the number of normalized Green-column entries at least $t$ has order $1/t$. The leading heat coefficient has order $\log(1/t)/t$ for its superlevel counts. The estimates use a finite stopping cut in the physical predecessor tree of 4. | [OP-I4](IMPEDANCE.md) |

The uniform norm asymptotic computes a particular operator and both-scale distribution bounds compute a particular marked column. Neither controls the possibility that the column has zeros at unknown heights. A polynomial lower bound for the marked heat coefficient at every height would imply the stronger uniform logarithmic stopping-time bound. The first missing Collatz inference is strict positivity for every specified ordinary input.

## Replay

Run from the repository root:

~~~sh
python -B research/unconventional-20261126/operator/controls.py
~~~

[The exact checks](controls.py) produce [the recorded JSON](CONTROLS.json). They enumerate all ternary unit residue types at inverse levels four through eight, explicitly construct and replay five large ordinary good-ball copies, enclose the Haar exponent by outward-rounded rational arithmetic, and test the half-line boundary identity at $z=1/2$. The finite controls do not prove the operator-valued limit or local spectral transplants; those have separate analytic proofs above.

## Literature and repository boundaries

- D. Applegate and J. C. Lagarias, *The Distribution of $3x+1$ Trees* (1995), define and analyze the pruned inverse trees after removing multiples of three. Their leaf extrema precede the small branching observations here. The new claims concern local transplants on the ordinary graph, its undirected heat operator, and marked Green distributions. [Author PDF](https://websites.umich.edu/lagarias/doc/3x%2B1trees.pdf)
- T. Mori, *Application of Operator Theory for the Collatz Conjecture*, studies irreducibility of specific operator-algebra representations. The essential-spectrum result here has a narrower class of observables and makes no irreducibility deduction. [Primary paper](https://arxiv.org/abs/2411.08084)
- J. Breuer, S. Denisov and L. Eliaz, *On the Essential Spectrum of Schrödinger Operators on Trees*, show that essential spectrum can be strictly larger than a union of right-limit spectra on general graphs. OP-L3 instead constructs explicit forward-orbit partitions to localize Weyl vectors. [Primary paper](https://arxiv.org/abs/1711.10049)
- J. Dodziuk, *Difference Equations, Isoperimetric Inequality and Transience of Certain Random Walks* (1984), develops graph Cheeger bounds. OP-G1 gives its elementary coarea argument with the present edge normalization. [Author's institutional copy](https://academicworks.cuny.edu/gc_pubs/181/)
- J. H. Schenker and M. Aizenman, *The Creation of Spectral Gaps by Graph Decoration* (2000), use resolvent elimination on attached graphs. Here a continuous-spectrum half-line is attached only at one residue class, and the core gap makes an operator-norm expansion available at zero. [Author PDF](https://users.math.msu.edu/users/schenke6/Reprints/LMPV53P253.pdf)
- R. Lyons and Y. Peres, *Probability on Trees and Networks* (2016), Chapter 2, supplies the standard electrical resistance, flow and hitting-probability principles used in OP-I1. [Authors' book](https://rdlyons.pages.iu.edu/prbtree/)
- PR193, frozen at 4cc06e7d8fdec923eed73a26b1e9d680c9f701d1, studies the additive Fourier–Stieltjes representation of the invariant color. PR200, frozen at 8e6add443b13acbcfd553676898c120183f07377, obtains conditional Fourier cancellation and a Fejér-norm lower bound. The graph-operator estimates here are independent of those Fourier and fixed-root density hypotheses. [PR193 global argument](https://github.com/GettysburgResearch/collatz/blob/4cc06e7d8fdec923eed73a26b1e9d680c9f701d1/research/astra-closure-20261125/global/README.md) · [PR200 Fourier argument](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/global-trace-20261125/FOURIER_RIGIDITY.md)
