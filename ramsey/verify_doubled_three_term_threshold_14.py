#!/usr/bin/env python3
"""Verify the exact two-colour threshold for {2a,a+b,2b}."""


def triples(N):
    out = []
    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            t = (2 * a, a + b, 2 * b)
            if t[-1] <= N:
                out.append(t)
    return out


def avoiding_colourings(N):
    T = triples(N)
    good = []
    for mask in range(1 << N):
        ok = True
        for x, y, z in T:
            cx = (mask >> (x - 1)) & 1
            cy = (mask >> (y - 1)) & 1
            cz = (mask >> (z - 1)) & 1
            if cx == cy == cz:
                ok = False
                break
        if ok:
            good.append(mask)
    return good


g13 = avoiding_colourings(13)
g14 = avoiding_colourings(14)
assert len(g13) == 16, len(g13)
assert len(g14) == 0, len(g14)

witness = '0101000110100'
mask = sum((int(bit) << i) for i, bit in enumerate(witness))
assert mask in g13

print('PASS')
print('avoiding colourings on [13]:', len(g13))
print('avoiding colourings on [14]:', len(g14))
print('witness on [13]:', witness)
