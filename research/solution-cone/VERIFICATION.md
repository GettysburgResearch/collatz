# VERIFICATION.md — solution-cone packet verification trail

**Integrator:** fable-01 · 2026-07-21

## What actually happened (full honesty)

The packet was produced by a 12-prover parallel campaign with a designed
adversarial-verification stage (2 independent verifier agents per proof —
reconstruction lens + refutation lens — plus a repair round). The 12
provers completed. **The verification stage did not run: all 24 verifier
agents failed on a session usage limit before doing any work.** The
campaign's internal "CONFIRMED" labels were an artifact of an empty
verdict list and have been discarded; they appear nowhere in this packet.

Consequently:

- Every mathematical claim (L-9701, T-9701..T-9704, L-9705..L-9708) is an
  **UNREVIEWED author-agent draft**, status at most PROPOSED, and should
  be treated with the skepticism due a proof nobody has checked.
- The two experiments (X-9701, X-9702) and the literature note (M-9701)
  are likewise single-author artifacts.

## What HAS been verified in this pass

The integrator (fable-01, main session) ran every claim's committed
verification snippet locally, single pass, 2026-07-21:

```text
l-9701  exit 0  — l2 norm sqrt(2)/adjoint checks + 3n-1 control passed
t-9701  exit 0  — truncated kernel dim = component count (N = 2000)
t-9702  exit 0  — extreme-ray finite sanity checks (N = 5000)
t-9703  exit 0  — cube-root-of-unity eigenvector exists on {5,7,10}
                  U-component; lambda = i excluded; interior-support
                  bookkeeping as specified
t-9704  exit 0  — cycle-measure fixed points exact; duality pairing exact
l-9705  exit 0  — kappa(s) formula matches; F*F diagonal on truncations
l-9706  exit 0  — single-valued functional equation coefficientwise
l-9707  exit 0  — Abelian bounds + component-partition identity
l-9708  exit 0  — T-components(<=5000) = 2; U-components(<=5000) = 3
x-9701  exit 0  — identity checker + spurious(N) accounting
x-9702  exit 0  — condensed control-map suite
m-9701  exit 0  — 3n-1 control identity spot-check
```

Logs: `experiments/snippets/results/*.log`. These are **finite
computational consistency checks only** — they raise confidence that the
statements are not trivially wrong; they are not proofs and they do not
substitute for mathematical review.

## What remains to be done (reviewer entry points)

1. Independent mathematical reconstruction of each proof, hardest first:
   T-9703 (the depth-cocycle well-definedness argument is the crux),
   T-9704 (the conservativity/mass-transport step), T-9702 (the
   infinite-sum extremality decomposition), L-9706 (coefficientwise
   cancellation of fractional powers).
2. The designed 2-verifier adversarial round can be re-run when session
   capacity allows; the prover outputs are cached in the session workflow
   journal (run id wf_c6b5dadd-96f) for exact resumption.
3. M-9701's retrieval-based attributions must be audited under the issue
   #7 literature protocol before any KNOWN/APPARENTLY-NEW classification
   is relied upon.

No claim in this packet may be promoted past PROPOSED until (1) happens,
per README §7 — and the author requests that reviewers begin by trying to
refute T-9703 and T-9704, which carry the packet's most useful content.
