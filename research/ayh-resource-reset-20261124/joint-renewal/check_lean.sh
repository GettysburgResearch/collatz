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

# Rebuild all four local dependencies; reuse only the pinned Mathlib cache.
compile "$source_dir/../positive-section/vendor" ShellCover
compile "$source_dir/../positive-section/vendor" OffsetDescent
compile "$source_dir/../literature-step" PostDescentFibers
compile "$source_dir/../literature-step" FirstPassageMarks
for module in KilledGradeGreen EndpointFibers EntranceGrades AffineGradeRigidity QuartetCollapse TripleGradeProduct MiddleIsolationWindow SubcriticalCurvature; do
    compile "$source_dir" "$module"
done

cat > "$output_dir/PublicAudit.lean" <<'LEAN'
import KilledGradeGreen
import EndpointFibers
import EntranceGrades
import AffineGradeRigidity
import QuartetCollapse
import TripleGradeProduct
import MiddleIsolationWindow
import SubcriticalCurvature
#print axioms CollatzSlopeOccupation.green_step
#print axioms CollatzSlopeOccupation.visits_add_remainder
#print axioms CollatzSlopeOccupation.weighted_band_visits_le
#print axioms CollatzShell.EndpointFibers.entrance_odd_count_unique
#print axioms CollatzShell.EndpointFibers.entrance_endpoint_card
#print axioms CollatzShell.EndpointFibers.entrance_endpoint_card_narrow
#print axioms CollatzShell.EntranceGrades.safe_prefix
#print axioms CollatzShell.EntranceGrades.first_transfer
#print axioms CollatzShell.EntranceGrades.no_entrance_transfer
#print axioms CollatzShell.EntranceGrades.translate_average_l1
#print axioms CollatzShell.EntranceGrades.two_point_slope
#print axioms CollatzShell.EntranceGrades.slope_signature
#print axioms CollatzShell.EntranceGrades.ordered_head_shifts
#print axioms CollatzShell.EntranceGrades.crossed_head_shifts
#print axioms CollatzShell.QuartetCollapse.original_outputs
#print axioms CollatzShell.QuartetCollapse.triple_outputs
#print axioms CollatzShell.QuartetCollapse.double_outputs
#print axioms CollatzShell.QuartetCollapse.residual_profile
#print axioms CollatzTripleGrades.ordered_fair_step
#print axioms CollatzTripleGrades.tie_step_le
#print axioms CollatzTripleGrades.mixed_middle_identity
#print axioms CollatzTripleGrades.middle_window_lower
#print axioms CollatzTripleGrades.sliding_shell_occupation
#print axioms CollatzSlopeOccupation.barrier_line_second
#print axioms CollatzSlopeOccupation.curvature_eq
#print axioms CollatzSlopeOccupation.curvature_le_negative
LEAN
compile "$output_dir" PublicAudit
