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

# Compile all three new modules from source into a fresh output directory.
for module in NonunitExit DisjointGradeCrossing PredictablePhysicalArms; do
    compile "$source_dir" "$module"
done

cat > "$output_dir/PublicAudit.lean" <<'LEAN'
import NonunitExit
import DisjointGradeCrossing
import PredictablePhysicalArms
#print axioms NonunitExit.physical_chain
#print axioms NonunitExit.directed_successor
#print axioms NonunitExit.shadow_lift
#print axioms NonunitExit.denom_iter
#print axioms NonunitExit.shadow_certifies
#print axioms Collatz.DisjointGradeCrossing.opposite_classes
#print axioms Collatz.DisjointGradeCrossing.tie_before_inversion
#print axioms Collatz.PredictablePhysicalArms.affine_step
#print axioms Collatz.PredictablePhysicalArms.next_parameter
#print axioms Collatz.PredictablePhysicalArms.truncate_parameter
#print axioms Collatz.PredictablePhysicalArms.current_eq
#print axioms Collatz.PredictablePhysicalArms.signed_flux
#print axioms Collatz.PredictablePhysicalArms.even_suffix_parent
LEAN
compile "$output_dir" PublicAudit
