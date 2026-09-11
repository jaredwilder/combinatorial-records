# combinatorial-records

Verified combinatorial computations and theorem banks across Sidon sets, covering designs, Ramsey structure, Lonely Runner, finite-field avoidance, automata, multiplicative avoidance, and additive encodings.

Author: Jared Wilder. First public timestamp: 2026-09-10.
**This repository is written by concurrent release sessions and grows. The directory listing is authoritative; this README is a map of the current mathematical surface.**

## Contents at a glance

| directory | contents |
|---|---|
| `lonely-runner/` | **Lonely Runner at 13 effective speeds:** a 42-entry theorem bank from a 19-round campaign; strongest completed subproblem is the large-prime canonical class `p > 2366`, with the remaining 13-speed frontier recorded separately. |
| `ramsey-r55/` | A pure-mathematics deep dive on `R(5,5)` plus **untouched-base extension lemmas** for adding a vertex to an existing `(5,5)`-Ramsey colouring. |
| `sidon/` | **`f(7) >= 24`** for binary Sidon sets, with an executable verifier. |
| `covering/`, `covering-designs/` | **677 verified covering-number rows**, monotonicity checks, and `C(13,6,3)` witnesses plus target-20 structural constraints. |
| `erdos500/` | A deletion-density and inheritance toolkit with a recovered-theorem index. |
| `finite-fields/` | Three **complete finite classifications**: simultaneous sum/product/3-AP avoidance in `F_73^×`, simultaneous sum/product avoidance in `F_31^×`, and sum-free + nontrivial-3-AP-free subsets of `Z/31Z`. |
| `multiplicative/product-gp-free-50/` | An **exact finite extremal classification** for product-free and nontrivial-GP-free subsets of `[50]`. |
| `automata/` | Finite transducer monoids, quotients and robust bounds; abstract Lean identity index. |
| `additive-encodings/` | An abstract additive-encoding theorem bank. |
| `witness-vault/` | **21 concrete witness objects** independently revalidated in a forensic release. |
| `ramsey/` | Circulant Ramsey-family exhaustions: `R(3,10)` at `n=40` and `R(4,6)` at `n=36`, both with zero witnesses in the searched family. |
| `twin-primes/` | A conditional Type I / Type II reduction package with the two missing analytic hypotheses named explicitly. |
| `findings/` | Per-result verdict files, including the Sidon ladder `n=128` through `n=1000`. |

## Evidence labels

The repository contains several mathematical object classes, and their labels are part of the result rather than generic warning text:

- **exact finite classification / optimum** — exhaustive computation establishes the stated finite universe;
- **witness / lower bound** — the committed object proves the explicit existential or lower-bound statement attached to it;
- **restricted-family exhaustion** — a construction family has been exhausted, with no implication beyond that family unless separately proved;
- **theorem bank / structural lemma** — the statement itself defines the mathematical scope;
- **conditional reduction** — hypotheses and conclusion are both named;
- **novelty status** — historical novelty is tracked separately from mathematical correctness.

For example, `LIVE-CERTIFIED` in the Lonely Runner material denotes an attached finite/computational certificate, not proof-assistant formalization; the `F_73` classification records its own novelty-search status; and the witness vault pins every witness to its exact finite statement.

---

## 1. `f(7) >= 24` for binary Sidon sets

`sidon/` holds a 24-vector witness in `{0,1}^7` whose 300 pairwise sums are all distinct (OEIS A309370). Run `sidon/verify_sidon_d7_24.py`; it exits 0. Hashes are SHA-256 pinned and the result was independently re-verified in a separate session.

This is the lower-bound statement `f(7) >= 24`; the known upper side belongs to a separate question.

## 2. 677 covering numbers and two strict Schoenheim separations

`covering/covering-firehose.jsonl` carries 677 verified `C(v,k,t)` rows over `v in [5,35]`, `k in [2,34]`, `t in [1,6]`. `covering/covering-bounds.json` validates monotonicity: 43 `v`-pair comparisons with 0 violations and 39 `t`-pair comparisons with 0 violations.

A release-day recount corrected an earlier underclaim: twelve UNSAT rows cover **two distinct parameter triples** whose true covering number is strictly above the Schoenheim lower-bound formula:

| v | k | t | Schoenheim | UNSAT at that size proves |
|---|---|---|---:|---|
| 7 | 4 | 2 | 4 | `C(7,4,2) >= 5` |
| 7 | 4 | 3 | 11 | `C(7,4,3) >= 12` |

Whether either inequality improves the best literature table is a separate prior-art question; the computation itself proves the displayed strict separation from the general formula.

## 3. Circulant Ramsey-family exhaustion

`ramsey/circulant-ramsey-exhaustion.json` exhausts 1,048,575 circulant families for the `R(3,10)` condition at `n=40` with **0 witnesses**, and 262,143 circulant families for the `R(4,6)` condition at `n=36` with **0 witnesses**. Negative controls accept a witness at `n=5` for `R(3,3)` and reject `n=6`.

The mathematical statement here is the complete elimination of those circulant construction families at those orders. General Ramsey numbers require unrestricted colourings and are a different statement.

## 4. Sidon divergence at `n = 35`

`findings/rapid-fire-sidon-c3-divergence-20260729.md`: for `n <= 34`, the maximum Sidon-set size and the maximum under an added C3-permutation-free constraint agree. At **`n = 35`** they separate: `8` versus `7`.

The original run did not preserve the precise C3 variant, so the numerical computation is retained while promotion of the comparison statement waits on that semantic detail. That is a scope-resolution issue, not a reason to bury the surrounding Sidon computations.

## 5. Twin-prime conditional reduction package

`twin-primes/` states Type I and Type II sufficiency conditions for the twin-prime asymptotic through a Heath-Brown decomposition, then identifies the two unavailable inputs: Type I distribution at level `1-epsilon` over unrestricted moduli and a nontrivial Type II bilinear bound at `M ~ N ~ x^(1/2)`.

This package is a barrier/reduction audit grounded in classical Vaughan/Heath-Brown machinery, not a historical-novelty claim. Its useful content is the explicit identification of the two analytic seams and three corrections to the derivation.

## 6. Findings

`findings/` carries per-result verdict files for the Sidon ladder (`n = 128` through `n = 1000`), the circulant Ramsey eliminations, the covering siege, and an `R(5,5)` lower-certificate note.

## License

Apache-2.0.
