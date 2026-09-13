#!/usr/bin/env python3
"""Exact verifier for the finite polychromatic extrema extracted from Erdős #598.

Stdlib only; deterministic; exhaustive over all candidate color classes at the
three certified parameter points.
"""

from itertools import combinations
from math import comb


def universe_subsets(n, r):
    return list(combinations(range(n), r))


def good_family(n, k, K, family):
    fam = set(family)
    for X in combinations(range(n), K):
        if not any(e in fam for e in combinations(X, k)):
            return False
    return True


def min_good_size(n, k, K):
    U = universe_subsets(n, k)
    for r in range(1, len(U) + 1):
        for fam in combinations(U, r):
            if good_family(n, k, K, fam):
                return r
    raise RuntimeError("no good family")


def check_partition(n, k, K, classes):
    U = set(universe_subsets(n, k))
    flat = [e for cls in classes for e in cls]
    assert len(flat) == len(set(flat)), "classes overlap"
    assert set(flat) == U, "classes do not partition the k-subsets"
    for cls in classes:
        assert good_family(n, k, K, cls), f"bad class: {cls}"


def main():
    cases = [
        (4, 2, 3, 2, 3),
        (5, 2, 3, 4, 2),
        (6, 2, 4, 3, 5),
    ]
    for n, k, K, expected_L, expected_P in cases:
        L = min_good_size(n, k, K)
        bound = comb(n, k) // L
        assert L == expected_L, (n, k, K, L, expected_L)
        assert bound == expected_P, (n, k, K, bound, expected_P)
        print(f"({n},{k},{K}): L={L}, counting upper bound={bound}")

    P4 = [
        [(0, 1), (2, 3)],
        [(0, 2), (1, 3)],
        [(0, 3), (1, 2)],
    ]
    check_partition(4, 2, 3, P4)

    C5 = [
        [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)],
        [(0, 2), (0, 3), (1, 3), (1, 4), (2, 4)],
    ]
    check_partition(5, 2, 3, C5)

    K6 = [
        [(0, 5), (1, 4), (2, 3)],
        [(1, 5), (0, 2), (3, 4)],
        [(2, 5), (1, 3), (0, 4)],
        [(3, 5), (2, 4), (0, 1)],
        [(4, 5), (0, 3), (1, 2)],
    ]
    check_partition(6, 2, 4, K6)

    naive = [(0, 1), (2, 3)]
    bad_four_set = (0, 2, 4, 5)
    assert not any(e in set(naive) for e in combinations(bad_four_set, 2))

    print("all finite extrema and witness partitions: PASS")


if __name__ == "__main__":
    main()
