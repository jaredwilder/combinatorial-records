# combinatorial-records

Verified combinatorial computations: a Sidon lower bound with a self-checking witness, 677
covering numbers, an exhaustive circulant Ramsey search, a Sidon divergence threshold, and a
conditional twin-primes equivalence with its barriers written down.

Author: Jared Wilder. First public timestamp: 2026-09-10.

## 1. f(7) >= 24 for binary Sidon sets, with a verifier that runs

`sidon/` holds a 24-vector witness in {0,1}^7 whose 300 pairwise sums are all distinct
(OEIS A309370). Run `sidon/verify_sidon_d7_24.py`; it exits 0. Hashes are SHA-256 pinned and the
result was independently re-verified in a separate session.

**Scope: lower bound only.** Prior work brackets this quantity in [24, 60] and the upper end is
untouched here.

## 2. 677 covering numbers, and an honest null

`covering/covering-firehose.jsonl` carries 677 verified C(v,k,t) rows over v in [5,35], k in
[2,34], t in [1,6]. `covering/covering-bounds.json` validates monotonicity: 43 v-pair comparisons
with 0 violations, 39 t-pair comparisons with 0 violations.

**Correction, made 2026-09-10 after an independent recount, replacing an earlier false statement
in this file.** The first version of this README said zero rows exceed the Schoenheim bound. That
was wrong, and wrong in the direction of underclaiming.

Twelve rows carry status `UNSAT`, covering **two distinct parameter triples**:

| v | k | t | Schoenheim | UNSAT at that size proves |
|---|---|---|---|---|
| 7 | 4 | 2 | 4 | C(7,4,2) >= 5 |
| 7 | 4 | 3 | 11 | C(7,4,3) >= 12 |

So the true covering number **strictly exceeds the Schoenheim bound** for those two triples, which
the computation proves rather than assumes.

**That is not the same as beating the published record.** Schoenheim is a general lower-bound
formula, and the literature value for a given triple may already sit above it. Whether either of
these improves on the La Jolla entry has **not** been checked here and is not claimed.

## 3. Circulant Ramsey exhaustion

`ramsey/circulant-ramsey-exhaustion.json`: R(3,10) searched on n = 40 across 1,048,575 circulant
families with **0 witnesses**; R(4,6) searched on n = 36 across 262,143 families with **0
witnesses**. Negative control passes: the checker accepts a witness at n = 5 for R(3,3) and
rejects n = 6.

**This determines no Ramsey number.** It exhausts one construction family. A circulant witness not
existing says nothing about a general witness existing, and the file says so.

## 4. Sidon divergence at n = 35

`findings/rapid-fire-sidon-c3-divergence-20260729.md`: for n <= 34 the maximum Sidon set size and
the maximum size under an added C3-permutation-free constraint agree. At **n = 35** they part:
8 against 7.

**Novelty unresolved, and for a specific reason recorded at the time:** which C3 variant was used
was never written down. The computation stands; the claim does not, until that is pinned.

## 5. Twin primes, conditional

`twin-primes/` states Type I and Type II sufficiency conditions for the twin prime asymptotic via a
Heath-Brown decomposition, and then names the two hypotheses that are **not** available: Type I
distribution at level 1-epsilon over unrestricted moduli (only smooth-moduli results past 1/2 are
known, from Zhang and Polymath8), and any nontrivial Type II bilinear bound at M ~ N ~ x^(1/2),
where no published bound exists.

**This is folklore, standard since Vaughan and Heath-Brown in 1981-82. It is not new.** It is
published here as a barrier audit with three documented corrections to its own derivation, not as
a discovery.

## 6. Findings

`findings/` carries the per-result verdict files for the Sidon ladder (n = 128 through n = 1000),
the circulant Ramsey elimination, the covering siege, and an R(5,5) lower-certificate note.

## License

Apache-2.0.
