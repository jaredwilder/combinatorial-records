#!/usr/bin/env python3
from itertools import combinations

N = 24
BASE = {1, 2, 4, 8, 9}
S = BASE | {(-x) % N for x in BASE}


def adjacent(u, v):
    return u != v and ((v - u) % N in S)


def is_clique(q):
    return all(adjacent(u, v) for u, v in combinations(q, 2))


def is_independent(q):
    return all(not adjacent(u, v) for u, v in combinations(q, 2))


def main():
    degrees = [sum(adjacent(v, w) for w in range(N)) for v in range(N)]
    edges = sum(degrees) // 2
    k4 = [q for q in combinations(range(N), 4) if is_clique(q)]
    i5 = [q for q in combinations(range(N), 5) if is_independent(q)]
    triangle = next((q for q in combinations(range(N), 3) if is_clique(q)), None)
    independent4 = next((q for q in combinations(range(N), 4) if is_independent(q)), None)
    assert set(degrees) == {10}, degrees
    assert edges == 120, edges
    assert not k4, k4
    assert not i5, i5
    assert triangle is not None
    assert independent4 is not None
    # Existence of a triangle plus absence of K4 gives omega=3.
    # Existence of an independent 4-set plus absence of an independent 5-set gives alpha=4.
    print('PASS')
    print(f'vertices={N} degree=10 edges={edges}')
    print(f'K4=0 independent_5=0 omega=3 alpha=4')
    print(f'triangle_witness={triangle}')
    print(f'independent4_witness={independent4}')


if __name__ == '__main__':
    main()
