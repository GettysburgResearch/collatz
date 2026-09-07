# Contribute from your phone

Connected GitHub tools can provide a reading and authoring route without a local checkout. Actually running experiments requires an execution environment; a claim that a command ran is not an execution receipt.

**Walkthrough status: awaiting a fresh-contributor end-to-end test.** Availability, button names and write actions vary by account and client. This guide does not claim every mobile connection supports every action.

## Get access and connect

Follow [Join and start](../CONTRIBUTING.md#join-and-start). For the direct organization workflow, accept the invitation and confirm that your intended GitHub account can open `GettysburgResearch/collatz`. Public reading and fork contributions, once available, do not require membership.

In ChatGPT or Claude, open the available Apps, Plugins or Connectors settings and connect GitHub using the same GitHub account. Installation selectors: [ChatGPT/Codex](https://github.com/apps/chatgpt-codex-connector/installations/select_target) · [Claude](https://github.com/apps/claude/installations/select_target). Choose GettysburgResearch if offered and follow the repository-selection prompts. Repository access, your personal connection and an organization's app approval are separate requirements; ordinary membership does not grant app-administration rights. Installation alone does not guarantee mobile read/write actions.

**Owner check, separate from personal authorization:** in GettysburgResearch's GitHub **Settings → Third-party Access → GitHub Apps**, configure the relevant app's repository access and resolve pending permission requests. **OAuth application policy** is a separate control for OAuth apps; approve the relevant app if required rather than disabling restrictions globally. See [GitHub's app-access guidance](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/limiting-oauth-app-and-github-app-access-requests-and-installations) and [Claude's integration guide](https://support.claude.com/en/articles/10167454-use-the-github-integration).

Use the official [GitHub connection instructions](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt) and [GitHub app installation guide](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party) for current account-specific steps. This project does not ask you to paste access tokens into a chat, issue or research file.

## Check the connection

Paste this into a new chat with GitHub tools available:

```text
Use the connected GitHub tools to open GettysburgResearch/collatz.
Read README.md, AGENTS.md and CONTRIBUTING.md from current main.
Tell me the exact main commit you read, summarize one research direction,
and identify a small contribution. Do not change files yet.
Report an unavailable read or write capability honestly.
```

A working read does not prove write or execution access. Check the connected account, repository selection and organization approval when access fails. Do not repeatedly reinstall an app without identifying the missing permission.

## Make a first contribution

```text
Work on [my question] in GettysburgResearch/collatz.
Read the relevant program files and check overlapping open PRs.
Follow AGENTS.md and CONTRIBUTING.md. Use a new branch.
Prepare a research note, counterexample, literature connection or review.
State its status, scope, exact dependencies, checks actually run and first gap.
Do not invent execution results or turn finite evidence into a universal claim.
Open a PR against main and return its actual link and commit SHA.
Leave main and other contributors' branches unchanged.
```

Open the returned PR yourself. Confirm its files and author, make sure it contains no private material, and seek review using [shared review](REVIEWING.md). When the available connection cannot write, retain the proposed contribution and use an authorized GitHub authoring environment; a chat response alone is not publication.

## Maintainer acceptance test

A fresh contributor should successfully open the repository, connect the intended account, run the reading prompt, and create a real branch/PR with the writing prompt. Record the client/account limitations and resulting commit before marking this route tested. A phone-only walkthrough does not certify local scientific execution or a complete-checkout validation run.
