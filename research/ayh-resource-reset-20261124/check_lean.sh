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
    local source=$1 module=$2
    (
        cd -- "$source"
        "$compiler" -j1 -DwarningAsError=true -o "$output_dir/$module.olean" "$module.lean"
    )
}

for module in SelfEmbedding MixedBaseRigidity PolynomialPump PositivePolynomialBarrier CarryTrace; do
    compile "$source_dir" "$module"
done
for module in ShellCover ForwardSection OffsetDescent; do
    compile "$source_dir/positive-section/vendor" "$module"
done
for module in MarkedCylinders InversePowerRows; do
    compile "$source_dir/positive-section" "$module"
done

cat > "$output_dir/Audit.lean" <<'LEAN'
import SelfEmbedding
import MixedBaseRigidity
import PolynomialPump
import PositivePolynomialBarrier
import CarryTrace
import InversePowerRows
#print axioms AYHSelfEmbedding.certificate
#print axioms AYHSelfEmbedding.every_rule_used
#print axioms AYHSelfEmbedding.source_embeds
#print axioms AYHSelfEmbedding.no_strict_rule
#print axioms AYHSelfEmbedding.no_strict_of_trace
#print axioms AYHSelfEmbedding.certificate41
#print axioms AYHSelfEmbedding.every_rule_used41
#print axioms AYHSelfEmbedding.no_strict_rule_of_zero_stutter
#print axioms MixedBaseRigidity.forwardCollapse
#print axioms MixedBaseRigidity.reverseCollapse
#print axioms MixedBaseRigidity.allRulesEqual
#print axioms PolynomialPump.positive
#print axioms PolynomialPump.support_mono
#print axioms PolynomialPump.dominates
#print axioms PolynomialPump.free_coordinate
#print axioms PolynomialPump.used_of_strict
#print axioms PolynomialPump.pump
#print axioms PositivePolynomialBarrier.no_strict_rule
#print axioms CarryTrace.aggregate
#print axioms CarryTrace.trace_zero
#print axioms CarryTrace.zero_on_return
#print axioms CarryTrace.summand_zero_on_return
#print axioms CollatzShell.MarkedCylinders.section_of_inverse_row
#print axioms CollatzShell.MarkedCylinders.cylinder_predecessor
#print axioms CollatzShell.MarkedCylinders.inverse_power_cost
#print axioms CollatzShell.MarkedCylinders.inv4_not_dvd_sixteen
#print axioms CollatzShell.MarkedCylinders.odd_predecessor
#print axioms CollatzShell.MarkedCylinders.cofinal_marked_power_predecessors
#print axioms CollatzShell.MarkedCylinders.universal_iff_marked_power
LEAN
(
    cd -- "$output_dir"
    "$compiler" -j1 -DwarningAsError=true Audit.lean
)
