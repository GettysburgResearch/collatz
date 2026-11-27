"""Verify the exact files bound by this continuation's source manifest."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
manifest = json.loads((Path(__file__).with_name("SOURCE_MANIFEST.json")).read_text())
for row in manifest["files"]:
    relative = Path(row["path"])
    if relative.is_absolute() or ".." in relative.parts:
        raise SystemExit("Manifest path escapes the checkout")
    data = (root / relative).read_bytes()
    if len(data) != row["bytes"] or hashlib.sha256(data).hexdigest() != row["sha256"]:
        raise SystemExit("Source identity mismatch: " + row["path"])
print(json.dumps({"files": len(manifest["files"]), "all_hashes_match": True}))
