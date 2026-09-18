"""Versioned operation registry. Local, trusted source code only; no upload loader."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from typing import Any

try:
    from . import core, pairs, research, symbols
except ImportError:
    import core, pairs, research, symbols

VERSION = "0.3.0-preview.1"
KERNEL_FILES = ("core.py", "pairs.py", "research.py", "symbols.py", "engine.py")
REGISTRY = {
    "pair": (pairs.pair_config, pairs.pair, "Positive paired trajectories; explicit displayed clocks and raw arrival witnesses"),
    "carry": (pairs.carry_config, pairs.carries, "Exact arithmetic bit columns; odd addition or even halving"),
    "study": (pairs.study_config, pairs.study, "Bounded paired progression; controls, counterexamples and unfinished cases"),
    "research": (research.research_config, research.research, "Shortcut affine drift; distinct ranks and maximal-word module clock"),
    "transport": (research.transport_config, research.transport, "Weighted finite source transport killed at an explicit floor"),
    "blocks": (symbols.blocks_config, symbols.blocks, "Composable parity blocks and complete rational replay"),
    "valuations": (symbols.valuations_config, symbols.valuation_cycle, "Isolated odd-valuation cycle controls"),
}


def normalize_request(request: Any) -> dict:
    if not isinstance(request, dict) or not isinstance(request.get("kind"), str):
        raise ValueError("A request object needs a string kind.")
    try:
        if request["kind"] in REGISTRY:
            return REGISTRY[request["kind"]][0](request)
        return core.normalize_request(request)
    except (TypeError, OverflowError) as exc:
        raise ValueError("Invalid field type in operation request.") from exc


def _disk_manifest() -> dict:
    root = Path(__file__).resolve().parent
    return {name: sha256((root / name).read_bytes()).hexdigest() for name in KERNEL_FILES}


# Loaded code and later on-disk edits must never share a misleading new digest.
_LOADED_MANIFEST = _disk_manifest()


def kernel_manifest() -> dict:
    if _disk_manifest() != _LOADED_MANIFEST:
        raise RuntimeError("Kernel source changed on disk. Restart the server before computing new results.")
    return dict(_LOADED_MANIFEST)


def digest(value: Any) -> str:
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def capabilities() -> dict:
    return {"schema": "collatz-api/v2", "version": VERSION, "maps": core.MAPS,
            "operations": list(core.OPERATIONS) + list(REGISTRY),
            "descriptions": {k: v[2] for k, v in REGISTRY.items()},
            "limits": {**core.LIMITS, "pair_steps": 10000, "raw_support_steps": pairs.RAW_LIMIT,
                       "study_count": 128, "study_work": 300000, "research_bits": 1024,
                       "block_expanded_length": 4096, "max_result_bytes": 16000000},
            "integer_encoding": "decimal strings", "plugin_policy": "trusted local code; restart after changes",
            "jobs": "POST /api/jobs; GET or DELETE /api/jobs/{id}",
            "partial_results": "study and transport preserve completed members/frames on cooperative interruption"}


def execute(request: Any, budget: core.Budget | None = None) -> dict:
    config = normalize_request(request)
    manifest = kernel_manifest()
    budget = budget or core.Budget()
    operation = REGISTRY[config["kind"]][1] if config["kind"] in REGISTRY else core.OPERATIONS[config["kind"]]
    result = operation(config, budget)
    kernel_manifest()  # Detect edits during a job as well.
    return {"schema": "collatz-result/v2", "version": VERSION, "request": config,
            "request_sha256": digest(config), "result_sha256": digest(result),
            "kernel_sha256": digest(manifest), "kernel_files": manifest,
            "baseline": core.BASELINE, "result": result}
