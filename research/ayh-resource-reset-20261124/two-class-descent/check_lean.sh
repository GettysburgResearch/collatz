#!/usr/bin/env bash
# From the pinned Mathlib checkout: lake env bash /path/to/this/check_lean.sh
set -euo pipefail
source_dir=$(cd -- "$(dirname -- "$0")" && pwd)
output_dir=$(mktemp -d)
trap 'rm -rf -- "$output_dir"' EXIT
export LEAN_PATH="$output_dir${LEAN_PATH:+:$LEAN_PATH}"
compiler=${LEAN:-lean}
"$compiler" --version

compile() {
    local directory=$1 module=$2
    (
        cd -- "$directory"
        "$compiler" -j1 -DautoImplicit=false -DwarningAsError=true \
            -o "$output_dir/$module.olean" "$module.lean"
    )
}

# Rebuild the entire local import closure; reuse only the pinned Mathlib cache.
compile "$source_dir/../positive-section/vendor" ShellCover
compile "$source_dir/../positive-section/vendor" OffsetDescent
for module in HighGradeShadow RoundedHeadDescent FrontierCoarea KilledEntryContraction PairedSourceShuffle LargestSlopeProjection; do
    compile "$source_dir" "$module"
done

cat > "$output_dir/PublicAudit.lean" <<'LEAN'
import HighGradeShadow
import RoundedHeadDescent
import FrontierCoarea
import KilledEntryContraction
import PairedSourceShuffle
import LargestSlopeProjection
#print axioms CollatzShell.HighGradeShadow.parity_numer
#print axioms CollatzShell.HighGradeShadow.fixed_weight_residue_injective
#print axioms CollatzShell.HighGradeShadow.oriented_shadow_update
#print axioms CollatzShell.RoundedHeadDescent.simultaneous_bottom
#print axioms Collatz.FrontierCoarea.single_dyadic_floor
#print axioms Collatz.FrontierCoarea.total_incidence_le
#print axioms Collatz.FrontierCoarea.exists_floor_le
#print axioms Collatz.KilledEntryContraction.uniform_weighted_contraction
#print axioms CollatzShell.PairedSourceShuffle.lower_fringe
#print axioms CollatzShell.PairedSourceShuffle.upper_fringe
#print axioms CollatzShell.PairedSourceShuffle.total_fringe
#print axioms CollatzShell.PairedSourceShuffle.sparse_residue_test
#print axioms Collatz.LargestSlopeProjection.endpoint_in_band
#print axioms Collatz.LargestSlopeProjection.same_anchor_span
#print axioms Collatz.LargestSlopeProjection.integer_record_census
LEAN
compile "$output_dir" PublicAudit
