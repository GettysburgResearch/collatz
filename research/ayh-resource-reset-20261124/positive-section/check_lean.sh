#!/usr/bin/env bash
# Run under `lake env` in the pinned Mathlib checkout.
set -euo pipefail
source_dir=$(cd -- "$(dirname -- "$0")" && pwd)
output_dir=$(mktemp -d)
trap 'rm -rf -- "$output_dir"' EXIT
export LEAN_PATH="$output_dir${LEAN_PATH:+:$LEAN_PATH}"
compiler=${LEAN:-lean}
compile() {
    local source=$1 module=$2
    (
        cd -- "$source"
        "$compiler" -j1 -DautoImplicit=false -DwarningAsError=true \
            -o "$output_dir/$module.olean" "$module.lean"
    )
}
for module in ShellCover ForwardSection OffsetDescent; do
    compile "$source_dir/vendor" "$module"
done
for module in MarkedCylinders InversePowerRows CriticalSection; do
    compile "$source_dir" "$module"
done
