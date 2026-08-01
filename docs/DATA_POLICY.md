# External Data and Artifact Policy

## Principle

External data must be shareable, attributable, immutable enough to verify, and
connected to an exact claim or experiment.

## Small artifacts

Commit directly when reasonable:

- source code;
- compact certificates;
- test vectors;
- manifests;
- independent checkers;
- small exact outputs;
- hashes and summaries.

## Moderate artifacts

Use a tagged GitHub Release when the artifact is immutable and reasonably
sized.

Commit the manifest and checksum to the repository.

## Large artifacts

Use stable external storage or an archival repository.

Commit:

```yaml
artifact_id:
title:
claim_ids:
source_commit:
creator:
created_at:
license:
filename:
size_bytes:
sha256:
production_command:
environment:
seed:
scope:
external_location:
independent_checkers:
limitations:
```

## Generated data

Prefer regeneration scripts over committing large generated data.

When regeneration is expensive, provide:

- a compact proof-carrying certificate;
- an independent verifier;
- a sample;
- exact production metadata;
- immutable hashes.

## Literature

Store:

- citation;
- DOI or stable identifier;
- edition or version;
- theorem number;
- page range;
- exact repository dependency;
- a paraphrase or legally permitted excerpt.

Do not commit copyrighted papers or books without redistribution rights.

## Model transcripts

Raw transcripts are optional and should not be the mathematical dependency.

Preserve instead:

- exact prompt;
- model and date;
- repository starting commit;
- distilled report;
- executed tool logs;
- code and artifacts;
- relevant transcript excerpt when safe.

Review transcripts for privacy and proprietary material before publication.

## Licensing

Every external artifact should state a license or an explicit permission basis.

Unknown licensing is a blocker to redistribution, not necessarily to citing the
source.

## Integrity

Use SHA-256 for committed manifests.

A changed artifact receives a new identifier or version. Do not silently replace
an artifact under an existing hash record.
