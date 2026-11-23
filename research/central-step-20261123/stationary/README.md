# A fast equivalent flow on the same ordinary component

Read [FAST_EQUIVALENT_FLOW.md](FAST_EQUIVALENT_FLOW.md).

The constructive result replaces a specified positive bounded harmonic
flow by one equivalent flow with an exponential joining-time tail.
It keeps every ordinary state and branch, all nonspine inverse kernels,
and the entire inverse law at the original root unchanged. The new
spine values approach their capacity geometrically.

For the original empirical measure on `N` distinct states and every
deterministic selection of finite inverse clocks, the new moving inverse
law has total-variation error at most `D/N`, with `D` fixed for the
source. Their collision probabilities are therefore in ratio
`1+O(N^(-1/2))` uniformly at every finite quotient, including arbitrary
growing residue precisions. No compatibility rate between the inverse
clock and residue precision is required for this comparison.

The new law is explicit. Its whole-path density is `rho^tau/Z`, where
`tau` is first joining time, and its graph formula rescales each
off-spine branch by its first attachment index. The old fixed-root
boundary results transfer with their exact source qualifications. Every
fixed inverse cone retains its reciprocal floor up to a root-dependent
constant; no global uniform reciprocal floor is asserted.

The direct source-box consumer still retains its full cross-box term.
No bound on that term or on the original stationary collision law was
obtained. Thus the coalescence-rate interface can be supplied by a
choice of equivalent flow, while the arithmetic collision upper and
full Collatz remain open. This packet has written-proof scope and adds
no Lean module.
