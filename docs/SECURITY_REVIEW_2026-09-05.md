# Bounded pre-public security review

Reviewed base: `cd1b3689e8d37fc4232945072e2faf6bd5ee47bd` (integration PR #95). This is a limited exposure check, not a comprehensive security certification or permission to change visibility.

## Files and reachable history

A pattern scan covered 68 fetched remote branches (plus the local remote-HEAD alias) and their reachable history: 2,390 commits, 3,832 distinct text blobs, and 40,095,915 bytes. The scanner examined recognized private-key headers, common provider/GitHub token formats, credential-bearing URLs, likely literal secret assignments, chat links, email addresses and local user paths. It skipped 30 binary blobs; no blobs exceeded the 5 MiB per-file limit. Findings were deduplicated by blob version, not treated as unique incidents per commit.

No recognized credential, private-key, literal-secret or chat-link pattern was found. There were no content-pattern findings in the integrated base tree. Six historical local-path matches were inspected: all used the generic `/home/user/` account in two versions of a research document, not an identified personal home directory.

Commit author/committer metadata contains ordinary attribution addresses, including a personal email address. Making the repository public exposes that metadata along with its history. No address is reproduced in this report and no history was rewritten. This remains an owner privacy decision; changing future Git email settings would not remove historical metadata.

## Repository controls observed

- The repository was private and `main` was unprotected.
- GitHub Actions was disabled; default workflow permissions were read-only and workflow PR approval was disabled.
- Team access was owners: Admin; polymath-integrators: Maintain; polymath-contributors: Write.
- No current-main Actions workflow or in-repository Lean build was present.
- This documentation change supplies CODEOWNERS and shared review guidance. CODEOWNERS alone does not enforce approval; owners must configure branch rules at launch.

No settings, membership, workflow configuration, visibility or history changes were made. Organization-wide policy could not be inspected with the available token. The API did not provide a security-feature status, so this report does not assert secret scanning or push protection is enabled.

## Scope limits and follow-up

This scan is not an entropy-based or exhaustive secret detector, dependency vulnerability audit, or review of every contributed program's behavior. It excludes binary contents, issue/PR discussions, attachments, Actions artifacts, LFS payloads, unreachable/deleted history and external hosting accounts. Independent contributors should run unfamiliar code in an isolated environment without repository credentials; see [shared review](REVIEWING.md).

Before public launch, resolve licensing and the metadata privacy decision, enable the intended public branch protections, and complete the final structural-check receipt. Keep the [phone walkthrough](PHONE.md) marked untested until a fresh contributor completes it. The absence of a recognized secret in this bounded scan does not clear every [public-launch gate](PUBLIC_RELEASE_GATES.md).

## Structural checks during preparation

The existing `tools/check_integration_state.py` passed on the integrated base (173 curated local links), and passed after the onboarding edits (180 links before this receipt was added). The new `tools/check_review_integration.py` failed on this Windows environment: automatic CRLF conversion changes byte hashes, and Windows file modes do not reproduce Git executable bits. With exact source bytes, its remaining failure was an executable-bearing preserved subtree. All eight pinned subtree identities and their 73 file contents were independently compared with Git at the integrated base, with no mismatches; this does not replace a complete successful run of the supplied checker.

The final structural gate remains open for an unchanged Linux run or a separately reviewed portability fix. No mathematical verdict is inferred from these checks.
