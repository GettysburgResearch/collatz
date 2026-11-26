#!/usr/bin/env bash
# Supply the pinned Mathlib LEAN_PATH and Lean 4.34.1 compiler.
# Every repository-local object is rebuilt in a new temporary directory.
set -euo pipefail
source_dir=$(cd -- "$(dirname -- "$0")" && pwd)
output_dir=$(mktemp -d)
trap 'rm -rf -- "$output_dir"' EXIT
export LEAN_PATH="$output_dir${LEAN_PATH:+:$LEAN_PATH}"
compiler=${LEAN:-lean}
"$compiler" --version
compile() {
    local directory=$1 module=$2
    printf "Compiling %s\n" "$module"
    (
        cd -- "$directory"
        "$compiler" -j1 -DautoImplicit=false -DwarningAsError=true \
            -o "$output_dir/$module.olean" "$module.lean"
    )
}
compile "$source_dir/../unit-exit" NonunitExit
compile "$source_dir/../unit-exit" UnitResidueExchange
compile "$source_dir/../directed-return/vendor" ReverseBasin
for module in DirectedEleven DirectedElevenLocal Residue17Closure; do
    compile "$source_dir/../directed-return" "$module"
done
for module in TwoOddCertificate FiniteHorizon MersenneBarrier MersenneParity \
    LocalResampling MersenneReturnKernel MersenneFirstBad RankThreeFamily \
    OppositeArm QuantitativeReturn FinalProofProposal PublicAudit; do
    compile "$source_dir/../closing-proposal" "$module"
done
for module in TernaryPowerLift WordRank OrdinaryWordRealization \
    PositiveWordDescent SignedSeventeenPotential LiftedLattice SourceProgressCases \
    MersenneTwoCheckpoints MersenneRescueWords MersenneRescueCylinder \
    MersenneProgressCases FinalProgressProposal PublicProgressAudit; do
    compile "$source_dir/../source-progress" "$module"
done
for module in CheckpointUnitExit SignedCycleDilation DifferentCycleAnchors MersenneTwoCenter GuardedResidueCover OddClockFloor ShadowTernaryDigits ShadowTernaryRescue DefectClockFloor FixedRankDeadlines CenterPhaseObstruction ClosingProposal PublicPairedAudit; do
    compile "$source_dir/../paired-reductions" "$module"
done
for module in AllDepthCenter RationalCenterPump AllMersenneCarries FixedCofactorRescue FixedCofactorLeastParent FixedTowerReflection TowerLowerCone TowerSuffixSharp DelayedTowerMerger WideCenterPump UnboundedQueryProposal PublicUnboundedAudit; do
    compile "$source_dir" "$module"
done
