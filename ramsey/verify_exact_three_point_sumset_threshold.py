#!/usr/bin/env python3
"""Exhaustive verifier for the exact two-colour threshold N=7.

Colours are assigned to [2,2N]. We ask whether some 1<=a<b<=N has
{2a,a+b,2b} monochromatic.
"""


def has_pattern(bits, N):
    def colour(x):
        return (bits >> (x - 2)) & 1
    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            vals = (2*a, a+b, 2*b)
            if colour(vals[0]) == colour(vals[1]) == colour(vals[2]):
                return True
    return False


def all_forced(N):
    width = 2*N - 1  # integers 2..2N
    for bits in range(1 << width):
        if not has_pattern(bits, N):
            return False, bits
    return True, None


def decode(bits, N):
    return {x: (bits >> (x - 2)) & 1 for x in range(2, 2*N + 1)}


def main():
    forced6, witness6 = all_forced(6)
    forced7, witness7 = all_forced(7)
    assert not forced6
    assert forced7
    expected = {
        2:1,3:0,4:1,5:0,6:0,7:0,
        8:1,9:1,10:0,11:1,12:0,
    }
    bits = sum(c << (x - 2) for x, c in expected.items())
    assert not has_pattern(bits, 6)
    print("N=6: avoiding colouring exists")
    print(decode(bits, 6))
    print("N=7: every colouring forced")
    print("PASS: exact threshold is N=7")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
