# Independent scope review: canonical retracing

Date: 2026-11-22.
Reviewed: `harnack_attack/MOVING_INVERSE_WINDOW.md` and
`harnack_attack/lean/CanonicalRetracing.lean`.

**Verdict: the written retracing deductions are valid, and the Lean
declarations match the claimed finite scalar scope.** This review reads
the arguments and declarations; the author's retained compiler output is
the evidence of compilation. No earlier finite Collatz development was
rerun.

The exact full-path mass is `v_(i-r)/v_i`. Conditioning on the retained
root label gives the stated total variation equality. Summing the
nonnegative increments of `v` over length-r windows counts each increment
at most r times, giving the finite average error bound. The per-root
tail bound follows from `v_(i-r)>=v_L` and `v_i<=C`. Both derivations use
the same bounded ordinary harmonic flow; no independent inverse-source
law is substituted.

For the ordinary one-step stationarity estimate, the `q_0` kernel row is
the only unmatched initial row, and the last actual point is the only
unmatched terminal point. The endpoint contribution is at most `1/(N+1)`;
the remaining failure probabilities telescope to the displayed
`C/(v_0(N+1))` bound. Escape still prevents tightness on ordinary states,
and the note correctly does not infer a Feller compact extension.

For capped words, adjoining the complete-path failure indicator gives
`H(word|I)<=h_b(epsilon)+epsilon*r*log(E)`. This does not require the
capped word to detect a failed path. It is a conditional entropy bound,
not an assertion about metric entropy of a weak limit.

The complete-path-atom clock is nondecreasing under path extension in the
required sense: the maximal depth-r atom cannot increase with r. If
`v_J>(1-epsilon)C`, the actual reversed path from `q_N` has mass greater
than `1-epsilon` through depth `N-J`. This proves the strict lower onset
bound. Combining it with a hypothetical logarithmic-height upper onset
does give the asserted positive lower exponential speed. The note
correctly leaves that upper-onset theorem unproved and makes no claim
that genuine branching must occur near, or immediately after, the
original-source clock.

The Lean file has eight declarations. They formalize a finite telescope,
a capacity-ratio inequality, the sliding-window cost bound, its sum and
mean corollaries, the tail and linear-window bounds, and the uniform
shifted-window mean inequality. Their hypotheses explicitly include the
positive monotone sequence and the required upper bound. The most general
tail inequality does not assume its two indices are ordered; it is still
a valid scalar inequality, and its actual-path consumer supplies the
correct clock order. The imported sliding-window theorem is used at
nonnegative increments.

No declaration in that file proves existence of the canonical flow,
identifies a Markov probability law, proves an entropy inequality, or
constructs a limiting measure. The distinction between the eight scalar
declarations and the written probability/limit arguments is accurately
maintained in the note.
