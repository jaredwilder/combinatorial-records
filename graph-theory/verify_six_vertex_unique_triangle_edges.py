#!/usr/bin/env python3
"""Exhaust all labelled simple graphs on six vertices."""
from collections import Counter
from itertools import combinations

V = range(6)
EDGES = list(combinations(V, 2))
counts = Counter()
maximum = -1

for mask in range(1 << len(EDGES)):
    adj = [[False] * 6 for _ in V]
    m = 0
    for i, (u, v) in enumerate(EDGES):
        if (mask >> i) & 1:
            adj[u][v] = adj[v][u] = True
            m += 1

    ok = True
    for u, v in EDGES:
        if not adj[u][v]:
            continue
        common = sum(adj[u][w] and adj[v][w]
                     for w in V if w != u and w != v)
        if common != 1:
            ok = False
            break

    if ok:
        counts[m] += 1
        maximum = max(maximum, m)

expected = Counter({0: 1, 3: 20, 6: 100})
assert counts == expected, (counts, expected)
assert maximum == 6

print('PASS')
print('distribution:', dict(sorted(counts.items())))
print('maximum edges:', maximum)
