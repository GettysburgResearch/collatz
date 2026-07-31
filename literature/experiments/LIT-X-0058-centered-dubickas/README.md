# LIT-X-0058 — Centered Dubickas source specialization

This standard-library script certifies rational upper and lower bounds for

```text
T(64/81), E(64/81)/81,
T(2/3), and (3-T(2/3))/324.
```

It verifies that the four-phase lift through `81/64=(3/2)^4` strictly improves the direct source constant but remains below the native radius `1/81`.

```bash
python3 run.py --check-results results/canonical.json
```

The script does not prove Dubickas's theorem; it certifies the native numerical specialization only.
