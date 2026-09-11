import json, hashlib, itertools, sys, os

# Checking logic identical to the original session checker (scratchpad/verify_sidon_d7_24.py,
# session adf91690, 2026-08-31). Only the artifact path resolution was changed for rescue:
# default is the pinned sibling copy; pass a path as argv[1] to check another artifact.
PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "sidon-search-best.json")
raw = open(PATH, "rb").read()
obj = json.loads(raw)
S = [tuple(int(c) for c in v) for v in obj["witness"]]
d = obj["d"]

checks = {}
checks["CARDINALITY_24"] = (len(S) == 24)
checks["ALL_LENGTH_d"] = all(len(v) == d for v in S)
checks["ALL_01"] = all(c in (0, 1) for v in S for c in v)
checks["ALL_DISTINCT"] = (len(set(S)) == len(S))

seen = {}
collision = None
n = len(S)
for i in range(n):
    for j in range(i, n):
        s = tuple(S[i][t] + S[j][t] for t in range(d))
        if s in seen:
            collision = {"sum": s, "pair_a": seen[s], "pair_b": (i, j)}
            break
        seen[s] = (i, j)
    if collision:
        break
checks["PAIRWISE_SUMS_DISTINCT"] = (collision is None)
checks["SUM_COUNT"] = (len(seen) == n * (n + 1) // 2)

print(json.dumps({
    "checks": checks,
    "all_pass": all(checks.values()),
    "collision": collision,
    "num_pairs_i_le_j": n * (n + 1) // 2,
    "num_distinct_sums": len(seen),
    "artifact_sha256": hashlib.sha256(raw).hexdigest(),
    "witness_canonical_sha256": hashlib.sha256(
        json.dumps(sorted(S)).encode()).hexdigest(),
}, indent=1))

sys.exit(0 if all(checks.values()) else 1)
