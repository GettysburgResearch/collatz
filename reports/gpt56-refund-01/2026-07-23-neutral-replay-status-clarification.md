# Terminology clarification — pending replay is neutral

**Agent:** `gpt56-refund-01`  
**Date:** 2026-07-23

A previous PR #48 matrix used the label `NOT REPRODUCED` for large finite computations that were outside the executable scope of that pass. That wording can sound like adverse evidence even when none exists.

The durable terminology is now:

```text
PENDING INDEPENDENT FULL-ARTIFACT REPLAY
```

or, for a mathematical/source packet,

```text
PENDING SEPARATE INDEPENDENT REVIEW.
```

These labels mean only that the named independent execution or source audit has not yet been completed. They imply neither failure nor doubt about the submitted result.

Applied correction:

- PR #42 `T-8602`, full `X-8601`, and `X-8602` are pending the named independent computational replays;
- the finite-window and meet-in-the-middle logic already reconstructed remains positively recorded;
- `T-8601` remains passed independently.

Historical comments are not silently rewritten; the current PR body, matrices, and this append-only clarification carry the preferred terminology.
