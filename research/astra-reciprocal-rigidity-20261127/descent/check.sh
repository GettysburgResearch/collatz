#!/usr/bin/env bash
set -eu
: "${LEAN_BIN:=lean}"
build=$(mktemp -d)
trap 'rm -rf "$build"' EXIT
export LEAN_PATH="$build${LEAN_PATH:+:$LEAN_PATH}"
for mod in RampShadow InversePrice PrepaidRamp FibreAttainment PrefixMeaning CoastCollapse; do
  "$LEAN_BIN" -j1 -DwarningAsError=true -DElab.async=false -o "$build/$mod.olean" "$mod.lean"
done
