#!/usr/bin/env bash
set -eu
: "${LEAN_BIN:=lean}"
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
build=$(mktemp -d)
trap 'rm -rf "$build"' EXIT
export LEAN_PATH="$build${LEAN_PATH:+:$LEAN_PATH}"
cd "$here/.."
"$LEAN_BIN" -j1 -DElab.async=false -DwarningAsError=true -o "$build/RampShadow.olean" RampShadow.lean
cd "$here"
for mod in PostWords ConeBounds SignedEscape CollisionCone ScaledRamp ProtectedCone; do
  "$LEAN_BIN" -j1 -DElab.async=false -DwarningAsError=true -o "$build/$mod.olean" "$mod.lean"
done
