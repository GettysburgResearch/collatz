#!/usr/bin/env bash
set -euo pipefail

# Reuse an existing checkout/cache at the pinned Mathlib revision.
# No toolchain installer or cache downloader is invoked by this script.
: "${MATHLIB_DIR:?Set MATHLIB_DIR to the existing pinned Mathlib checkout}"
band_lean_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
band_mathlib_root="$(cd -- "$MATHLIB_DIR" && pwd)"
band_mathlib_pin=d13f23b723b8a846827a245b89c10fc7d3f11612
band_mathlib_head="$(git -C "$band_mathlib_root" rev-parse HEAD)"
if [[ "$band_mathlib_head" != "$band_mathlib_pin" ]]; then
  printf 'Mathlib revision mismatch: expected %s, got %s\n' "$band_mathlib_pin" "$band_mathlib_head" >&2
  exit 1
fi
if ! git -C "$band_mathlib_root" diff --quiet HEAD --; then
  printf 'Mathlib has tracked working-tree changes; use a clean pinned checkout.\n' >&2
  exit 1
fi
band_lean_version="$(lean --version)"
if [[ "$band_lean_version" != *"4.34.1"* ]]; then
  printf 'Expected Lean 4.34.1; found %s\n' "$band_lean_version" >&2
  exit 1
fi

cd -- "$band_lean_root"
sha256sum --check vendor.sha256
sha256sum --check core.sha256
mkdir -p .build

band_mathlib_modules=(
  Mathlib.Order.Interval.Finset.Nat
  Mathlib.Tactic.Ring
  Mathlib.Tactic.Linarith
  Mathlib.Data.Fintype.Pigeonhole
  Mathlib.Data.Fintype.BigOperators
  Mathlib.Algebra.Order.Archimedean.Basic
  Mathlib.Data.Rat.Floor
  Mathlib.Analysis.SpecialFunctions.Log.Base
  Mathlib.NumberTheory.DiophantineApproximation.Basic
  Mathlib.Data.Nat.Factorization.Basic
  Mathlib.Data.Int.ModEq
)
# Include any additional direct Mathlib imports used by the requested modules.
for band_module in "$@"; do
  if [[ ! "$band_module" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    printf 'Expected a flat Lean module name, got %s\n' "$band_module" >&2
    exit 1
  fi
  while IFS= read -r band_line; do
    if [[ "$band_line" =~ ^import[[:space:]]+(Mathlib\.[A-Za-z0-9_.]+)[[:space:]]*$ ]]; then
      band_mathlib_modules+=("${BASH_REMATCH[1]}")
    fi
  done < "$band_module.lean"
done
(
  cd -- "$band_mathlib_root"
  lake build "${band_mathlib_modules[@]}"
)
band_mathlib_path="$(cd -- "$band_mathlib_root" && lake env printenv LEAN_PATH)"
printf '%s\n' "$band_mathlib_path" > .build/mathlib-path
export LEAN_PATH="$band_lean_root/.build:$band_lean_root/vendor:$band_lean_root:$band_mathlib_path"

printf 'Checking compatible arithmetic extraction BandCore\n'
lean -j1 -DwarningAsError=true -o .build/BandCore.olean BandCore.lean

for band_module in ShellCover ForwardSection SectionDynamics RisingReturns; do
  printf 'Checking imported %s\n' "$band_module"
  lean -j1 -DwarningAsError=true -o ".build/$band_module.olean" "vendor/$band_module.lean"
done

# New modules are compiled in the explicitly supplied dependency order.
# With no module arguments this builds only the pinned import route.
for band_module in "$@"; do
  if [[ ! "$band_module" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    printf 'Expected a flat Lean module name, got %s\n' "$band_module" >&2
    exit 1
  fi
  printf 'Checking new %s\n' "$band_module"
  lean -j1 -DwarningAsError=true -o ".build/$band_module.olean" "$band_module.lean"
done

printf 'Band-return Lean build completed.\n'
