#!/usr/bin/env python3
from itertools import combinations

EXPECTED = {
    (0, 1, 4, 9, 11),
    (0, 2, 7, 8, 11),
    (0, 2, 7, 10, 11),
    (0, 3, 4, 9, 11),
}


def is_golomb(marks):
    diffs = [b - a for a, b in combinations(marks, 2)]
    return len(diffs) == len(set(diffs))


def rulers_of_length(L):
    out = set()
    for interior in combinations(range(1, L), 3):
        marks = (0,) + interior + (L,)
        if is_golomb(marks):
            out.add(marks)
    return out


def main():
    for L in range(4, 11):
        got = rulers_of_length(L)
        assert not got, (L, got)
    got11 = rulers_of_length(11)
    assert got11 == EXPECTED, (got11, EXPECTED)
    for ruler in EXPECTED:
        diffs = [b - a for a, b in combinations(ruler, 2)]
        assert len(diffs) == 10
        assert len(set(diffs)) == 10
    print("PASS")
    print("minimum_length=11")
    print("normalized_optima=4")
    for r in sorted(EXPECTED):
        print(r)


if __name__ == "__main__":
    main()
