#!/usr/bin/env bash
# From the pinned Mathlib checkout: lake env bash /path/to/this/check_residue17_lean.sh
set -euo pipefail
source_dir=$(cd -- "$(dirname -- "$0")" && pwd)
output_dir=$(mktemp -d)
trap 'rm -rf -- "$output_dir"' EXIT
export LEAN_PATH="$output_dir${LEAN_PATH:+:$LEAN_PATH}"
compiler=${LEAN:-lean}
"$compiler" --version
cd -- "$source_dir"
# Both public declarations print their transitive axioms in the source.
"$compiler" -j1 -DautoImplicit=false -DwarningAsError=true \
    -o "$output_dir/UnitResidueExchange.olean" UnitResidueExchange.lean
