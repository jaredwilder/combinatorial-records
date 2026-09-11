# RECEIPT — f(7) >= 24 (OEIS A309370, binary Sidon sets)

**Claim:** there exists a Sidon set S of 24 vectors in {0,1}^7 (all C(24,2)+24 = 300
pairwise coordinatewise integer sums with i <= j distinct, diagonal included).
Therefore f(7) >= 24 for A309370.

**Status:** COMPUTED / VALID / NOT_TARGETED (no Lean formalization). Lower bound only.
The exact value of f(7) remains open; prior solver interval [24, 60] stands (upper bound
CITED from sidon_decide.py docstring, UNCHECKED here). Next route: sidon_decide.py
decision loop at m = 25.

## Replay

```bash
python oracle/evidence/sidon-f7-witness/verify_sidon_d7_24.py
```

Exit 0 with `"all_pass": true` and both hashes below, or the claim does not stand.

## Pinned hashes

| object | sha256 |
|---|---|
| artifact `sidon-search-best.json` (byte-exact) | `6a3528efb05a531903ab4714b8cc0d171402b767f8c5f59a8fece0c2d546c757` |
| witness canonical (`json.dumps(sorted(S))`) | `7d9c89708b4a74d36bcff7954fefd5728467026728bbedad7db79193374272a2` |

## Provenance

- Witness constructed by the sidon search lane; original artifact
  `oracle/runtime/state/sidon-search-best.json` (gitignored runtime state, never durable);
  byte-identical copy pinned here.
- Independent re-verification: MSL session adf91690 (2026-08-31), first /msl run under
  `MSL_CANONICAL_ALIEN_v1_5`. Checker written fresh from the WS1 witness schema, separate
  from the constructor and from `oracle/kbk/engine/sidon_decide.py:verify_sidon`.
  TERMINAL_AUDIT RESULT PASS; TARGET_CLOSED on the lower-bound component only.
- Checker rescued from that session's scratchpad 2026-08-31; checking logic unchanged,
  path resolution made portable (defaults to the pinned sibling artifact, argv override).
- Replay re-run at rescue time: 6/6 checks pass, 300/300 sums distinct, hashes match.
