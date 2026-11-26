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

# Rebuild the exact external local certificate and every new local module.
# Only the pinned third-party Mathlib/Lean distribution is reused.
compile "$source_dir/vendor" SingleReturn
for module in HeadRayRouting LateWitnessTracks SymmetricFutureForks FourSuffixClosure; do
    compile "$source_dir" "$module"
done

cat > "$output_dir/PublicAudit.lean" <<'LEAN'
import HeadRayRouting
import FourSuffixClosure
import LateWitnessTracks
import SymmetricFutureForks
#print axioms HeadRayRouting.dyadic_label
#print axioms HeadRayRouting.odd_run_label
#print axioms HeadRayRouting.unit_phase27
#print axioms HeadRayRouting.repeat_phase27
#print axioms HeadRayRouting.exact_head_labels
#print axioms HeadRayRouting.power_label
#print axioms HeadRayRouting.tripling_from_four
#print axioms FourSuffixClosure.tripled_return
#print axioms FourSuffixClosure.constant_label
#print axioms FourSuffixClosure.basin_iff_four
#print axioms Collatz.LateWitnessTracks.projected_head_block
#print axioms Collatz.LateWitnessTracks.parent_residue_bijective
#print axioms Collatz.LateWitnessTracks.parent_test_card
#print axioms Collatz.SymmetricFutureForks.steps_mono
#print axioms Collatz.SymmetricFutureForks.few_poor_centers
#print axioms Collatz.SymmetricFutureForks.one_shift
#print axioms Collatz.SymmetricFutureForks.prefix_shift
#print axioms Collatz.SymmetricFutureForks.fork_parities
#print axioms SingleReturn.singleReturnCover
#print axioms SingleReturn.collatzIffSingleReturn
#print axioms SingleReturn.collatzIffEvenChild
LEAN
compile "$output_dir" PublicAudit
