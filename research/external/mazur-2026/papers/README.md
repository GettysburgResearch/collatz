# Source-paper index

The two PDFs reviewed for this import are not redistributed in the repository because no redistribution license was supplied. Their exact fingerprints and canonical public routes are preserved below and in [`../sources.json`](../sources.json).

| Work | Supplied filename | Pages | Bytes | SHA-256 | Canonical PDF |
|---|---|---:|---:|---|---|
| Certified exponent-0.90 predecessor bounds | `Mazur_Certified_x090_Lower_Bounds_for_Collatz_Predecessor_Sets_v2.pdf` | 16 | 170031 | `cbae5d71ead733b380c3325503e46a7094fb4641244853a37dc220207d133a61` | <https://www.proofatlas.ai/papers/collatz-predecessor-090/Mazur_Certified_x090_Lower_Bounds_for_Collatz_Predecessor_Sets_v2.pdf> |
| Natural-density logarithmic-time bounds | `Mazur_Natural_Density_Collatz_Orbits_in_Logarithmic_Time_v2.pdf` | 27 | 253981 | `08a46dd1cdd9183beb2e09af517361f24d3b7945a6ee00db563a944a4a2373cf` | <https://www.proofatlas.ai/papers/natural-density-log-time-collatz/Mazur_Natural_Density_Collatz_Orbits_in_Logarithmic_Time_v2.pdf> |

To replay the byte checks against separately obtained source files:

```bash
python research/external/mazur-2026/check_import.py \
  --pdf-dir /path/to/directory-containing-the-two-pdfs
```

The committed [`../local-check-report.json`](../local-check-report.json) records a successful replay against the exact supplied files in the review environment.
