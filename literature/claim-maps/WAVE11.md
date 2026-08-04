# Claim map — wave 11

## New literature-suite claim

| Literature ID | Native interfaces | Status | Effect |
|---|---|---|---|
| `LIT-KTHM-0065` | PR #53 `L-8201/T-8255`; PR #70 `T-8260`; PR #76 `T-6701`; `LIT-KTHM-0060` | `PROPOSED / SOURCE-QUALIFIED FLOOR / SOURCE-AUDITED MATVEEV / EXACT CERTIFICATE` | Excludes all nontrivial `P3` pulse-cycle lifts with fixed support `1..18` and all `P11` lifts with fixed support `1..117` |

## Corrected literature-suite claim

| ID | Correction | Mathematical effect |
|---|---|---|
| `LIT-KTHM-0060` | `B<kr+1` is a bound on Matveev's weighted parameter `B`, not on `B*` | Cutoffs and certificates unchanged |

## Native claims that should consume the result

| Native claim/program | Recommended update |
|---|---|
| PR #53 `L-8201` | Record that every positive-rate fixed support is now proposed excluded after adding the verified-floor argument |
| PR #53 `T-8202/T-8255` | Mark Matveev step `SOURCE-AUDITED`; retain native proof status |
| PR #70 `T-8260` | Mark Matveev step `SOURCE-AUDITED`; retain native proof status |
| PR #76 `T-6701` | Record a new cycle-side consequence of the verified floor |
| Issue #52 | Move the pulse frontier from support `4` to support `18/117`, subject to review |

## First uncovered classes

```text
P3=(1,2):
  support 19 and above;

P11=(1,1,1,2,1,1,4):
  support 118 and above.
```

These are support-density barriers, not merely the next finite enumeration sizes.