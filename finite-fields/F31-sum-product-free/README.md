# Reproduce the F31 extremal classification

The exact maximum is **8**, with **nine maximizing sets**, for subsets of the nonzero residues modulo 31 containing neither `x+y=z` nor `xy=z`, with repetitions allowed. See [THEOREM.md](THEOREM.md) for the nine sets and the original result's provenance.

This directory now includes a fresh independent Python implementation. Run from this directory:

```sh
python verify_exhaustive.py
```

Python 3.10 or later; standard library only. It reproduces all nine sets in the theorem. [The dated receipt](INDEPENDENT-REPLAY-2026-09-13.json) records the actual result, script hash and theorem-file hash.

## Why the search is exhaustive

1. Directly generate every forbidden vertex set `{x,y,x+y}` and `{x,y,xy}` modulo 31. Omit equations whose right-hand side is zero because zero is outside the domain. Set formation retains repeated-variable constraints as one- or two-vertex prohibitions.
2. Remove hyperedges containing an already smaller forbidden hyperedge; this does not change the permitted subsets.
3. At every search node, branch on including or excluding one remaining vertex. Reject a completed forbidden edge. If all but one vertex of an edge are selected, exclude its remaining vertex.
4. Prune only when selected vertices plus every available vertex cannot reach the best size already witnessed. Retain ties, so all maximum sets are enumerated.

Each permitted subset is covered by the include/exclude branching, and propagation excludes only completions that would violate an explicit equation. Therefore the reported maximum is an upper bound as well as a witnessed lower bound. The nine printed sets are compared with the exact source theorem.

This verification supports the finite theorem over F31. Historical novelty and extensions to other fields are separate questions.

## Focused home and recovered verifiers

The [finite-field extremal-set repository](https://github.com/jaredwilder/finite-field-extremal-sets)
now provides the coherent three-case reading map, exact original verifier
sources, full maximizing layers, provenance hashes and fresh Python/C/C++
verification. This note remains the historical source record.
