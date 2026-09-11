#!/usr/bin/env python3
"""Exact SAT search for a 20-block C(13,6,3) covering.

A hypothetical 20-block covering has point degrees at least 9, total degree 120,
so (up to relabeling) its point-degree multiset is one of exactly

  A: (12,9^12)
  B: (11,10,9^11)
  C: (10,10,10,9^10).

This script solves each labeled representative exactly.  A solution to any case
is a genuine 20-block covering.  UNSAT for all three cases proves C(13,6,3)>=21;
together with the public 21-block witness, that gives C(13,6,3)=21.

The encoding uses truncated iterative totalizers so all cardinality constraints
remain compact.  Redundant pair-codegree >=3 constraints are included because
every pair has 11 third points and one 6-block containing the pair covers only
4 of them; they materially strengthen SAT propagation.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
import time
from pathlib import Path

from pysat.card import ITotalizer
from pysat.formula import CNF, IDPool
from pysat.solvers import Solver

V = tuple(range(13))
BLOCKS = tuple(itertools.combinations(V, 6))
TRIPLES = tuple(itertools.combinations(V, 3))
PAIRS = tuple(itertools.combinations(V, 2))

PATTERNS = {
    "A": (12,) + (9,) * 12,
    "B": (11, 10) + (9,) * 11,
    "C": (10, 10, 10) + (9,) * 10,
}


def add_totalizer(cnf: CNF, vpool: IDPool, lits: list[int], low: int | None = None,
                   high: int | None = None) -> None:
    """Add low <= sum(lits) <= high with a truncated totalizer."""
    assert low is not None or high is not None
    if not lits:
        if low is not None and low > 0:
            cnf.append([])
        return
    cap = 0
    if low is not None:
        cap = max(cap, low)
    if high is not None:
        cap = max(cap, high + 1)
    cap = min(cap, len(lits))
    tot = ITotalizer(lits=lits, ubound=cap, top_id=vpool.top)
    cnf.extend(tot.cnf.clauses)
    vpool.top = max(vpool.top, tot.top_id)
    # rhs[j] means at least j+1 inputs are true.
    if low is not None and low > 0:
        cnf.append([tot.rhs[low - 1]])
    if high is not None and high < len(lits):
        cnf.append([-tot.rhs[high]])


def build_case(pattern: str) -> tuple[CNF, IDPool, list[int]]:
    degs = PATTERNS[pattern]
    vpool = IDPool(start_from=1)
    block_vars = [vpool.id(("B", b)) for b in BLOCKS]
    bvar = dict(zip(BLOCKS, block_vars))
    cnf = CNF()

    # Exactly 20 blocks.
    add_totalizer(cnf, vpool, block_vars, low=20, high=20)

    # Every triple is covered.
    for t in TRIPLES:
        st = set(t)
        cnf.append([bvar[b] for b in BLOCKS if st.issubset(b)])

    # Exact labeled point degrees for this WLOG degree pattern.
    for x, d in enumerate(degs):
        lits = [bvar[b] for b in BLOCKS if x in b]
        add_totalizer(cnf, vpool, lits, low=d, high=d)

    # Redundant but strong: every pair occurs in at least 3 selected blocks.
    for p in PAIRS:
        sp = set(p)
        lits = [bvar[b] for b in BLOCKS if sp.issubset(b)]
        add_totalizer(cnf, vpool, lits, low=3)

    return cnf, vpool, block_vars


def choose_solver(cnf: CNF, requested: str | None = None) -> tuple[str, Solver]:
    names = [requested] if requested else ["cadical195", "cadical153", "glucose4", "glucose3"]
    errors = []
    for name in names:
        if not name:
            continue
        try:
            return name, Solver(name=name, bootstrap_with=cnf.clauses)
        except Exception as exc:  # pragma: no cover - environment dependent
            errors.append(f"{name}: {exc}")
    raise RuntimeError("no requested SAT solver available: " + "; ".join(errors))


def verify_model(model: list[int], block_vars: list[int], pattern: str) -> list[tuple[int, ...]]:
    pos = set(v for v in model if v > 0)
    chosen = [b for b, v in zip(BLOCKS, block_vars) if v in pos]
    assert len(chosen) == 20
    covered = set()
    for b in chosen:
        covered.update(itertools.combinations(b, 3))
    assert len(covered) == len(TRIPLES)
    got_deg = tuple(sum(x in b for b in chosen) for x in V)
    assert got_deg == PATTERNS[pattern]
    for p in PAIRS:
        assert sum(set(p).issubset(b) for b in chosen) >= 3
    return chosen


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pattern", choices=sorted(PATTERNS))
    ap.add_argument("--solver", default=None)
    ap.add_argument("--dump-cnf", type=Path, default=None)
    ap.add_argument("--json", type=Path, default=None)
    args = ap.parse_args()

    t0 = time.time()
    cnf, vpool, block_vars = build_case(args.pattern)
    build_s = time.time() - t0

    if args.dump_cnf:
        cnf.to_file(str(args.dump_cnf))
        sha = hashlib.sha256(args.dump_cnf.read_bytes()).hexdigest()
    else:
        # Stable digest of the literal clauses without requiring a DIMACS file.
        h = hashlib.sha256()
        for c in cnf.clauses:
            h.update((" ".join(map(str, c)) + " 0\n").encode())
        sha = h.hexdigest()

    solver_name, solver = choose_solver(cnf, args.solver)
    ts = time.time()
    sat = solver.solve()
    solve_s = time.time() - ts
    model = solver.get_model() if sat else None
    solver.delete()

    selected = verify_model(model, block_vars, args.pattern) if sat else []
    result = {
        "problem": "C(13,6,3) target 20",
        "pattern": args.pattern,
        "degree_pattern": PATTERNS[args.pattern],
        "status": "SAT" if sat else "UNSAT",
        "solver": solver_name,
        "primary_block_variables": len(BLOCKS),
        "cnf_variables": vpool.top,
        "cnf_clauses": len(cnf.clauses),
        "cnf_sha256": sha,
        "build_seconds": build_s,
        "solve_seconds": solve_s,
        "selected_blocks": selected,
    }
    text = json.dumps(result, indent=2)
    print(text)
    if args.json:
        args.json.write_text(text + "\n", encoding="utf-8")
    return 10 if sat else 20


if __name__ == "__main__":
    sys.exit(main())
