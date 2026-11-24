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
# Rebuild every local dependency in a fresh temporary object directory.
compile "$source_dir/../unit-exit" NonunitExit
compile "$source_dir/../unit-exit" UnitResidueExchange
compile "$source_dir/vendor" ReverseBasin
for module in DirectedEleven DirectedElevenLocal Residue17Closure \
    InteriorGradeBudget LocalColorCells FixedTritFeatures PublicAudit; do
    compile "$source_dir" "$module"
done
