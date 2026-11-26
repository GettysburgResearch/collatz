#!/usr/bin/env bash
# From the pinned Mathlib checkout: lake env bash /path/to/this/check_lean.sh
set -euo pipefail
source_dir=$(cd -- "$(dirname -- "$0")" && pwd)
section_dir="$source_dir/../positive-section"
output_dir=$(mktemp -d)
trap 'rm -rf -- "$output_dir"' EXIT
export LEAN_PATH="$output_dir${LEAN_PATH:+:$LEAN_PATH}"
compiler=${LEAN:-lean}
"$compiler" --version

compile() {
    local source=$1 module=$2
    (
        cd -- "$source"
        "$compiler" -j1 -DautoImplicit=false -DwarningAsError=true \
            -o "$output_dir/$module.olean" "$module.lean"
    )
}

for module in ShellCover ForwardSection OffsetDescent; do
    compile "$section_dir/vendor" "$module"
done
for module in MarkedCylinders InversePowerRows CriticalSection; do
    compile "$section_dir" "$module"
done
for module in TernaryHeadDescent WholeTernaryFiber CriticalCompression BasinCounting \
    TernaryStopping InverseWordCover HeadEdgeTransport; do
    compile "$source_dir" "$module"
done

# The other thirteen new public declarations print their axioms in their own files.
cat > "$output_dir/ContinuationAudit.lean" <<'LEAN'
import TernaryHeadDescent
import WholeTernaryFiber
#print axioms CollatzShell.TernaryHead.head_or_small
#print axioms CollatzShell.TernaryHead.source_contraction
#print axioms CollatzShell.TernaryHead.contraction_factor
#print axioms CollatzShell.TernaryHead.contraction_seven_fifths
#print axioms CollatzShell.TernaryHead.low_basin
#print axioms CollatzShell.TernaryHead.universal_iff_truncate
#print axioms CollatzShell.TernaryHead.whole_fiber
LEAN
(
    cd -- "$output_dir"
    "$compiler" -j1 -DautoImplicit=false -DwarningAsError=true ContinuationAudit.lean
)
