# Combinatorial records

Verified computations, classifications, witnesses, and theorem collections across Sidon sets, covering designs, Ramsey theory, Lonely Runner, finite-field avoidance, automata, multiplicative avoidance, and additive encodings.

Author: Jared Wilder. First public timestamp: 2026-09-10.

This repository continues to grow; the directory tree is the authoritative inventory, while this README summarizes the main mathematical contents.

## Contents at a glance

| directory | contents |
|---|---|
| `lonely-runner/` | **Lonely Runner at 13 effective speeds:** a 42-entry theorem collection. The strongest completed subproblem covers the large-prime canonical class `p>2366`; the remaining 13-speed cases are recorded separately. |
| `ramsey-r55/` | `R(5,5)` structural work, including **untouched-base extension lemmas** for adding one vertex to an existing `(5,5)`-Ramsey colouring. |
| `sidon/` | **`f(7) >= 24`** for binary Sidon sets, with an executable verifier. |
| `covering/`, `covering-designs/` | **677 verified covering-number rows**, monotonicity checks, `C(13,6,3)` 21-block witnesses, and structural restrictions on any hypothetical 20-cover. |
| `erdos500/` | Deletion-density and inheritance lemmas with an indexed theorem collection. |
| `finite-fields/` | Three **complete finite classifications**: simultaneous sum/product/3-AP avoidance in `F_73^×`, simultaneous sum/product avoidance in `F_31^×`, and sum-free + nontrivial-3-AP-free subsets of `Z/31Z`. |
| `multiplicative/product-gp-free-50/` | **Exact finite extremal classification** for product-free and nontrivial-geometric-progression-free subsets of `[50]`. |
| `automata/` | Finite transducer monoids, quotients, robustness bounds, and an abstract Lean identity index. |
| `additive-encodings/` | Additive-encoding theorems and constructions. |
| `witness-vault/` | **21 concrete witness objects** independently rechecked for the public release. |
| `ramsey/` | Complete circulant-family searches for the `R(3,10)` condition at `n=40` and the `R(4,6)` condition at `n=36`, both with zero witnesses in those restricted families. |
| `twin-primes/` | Conditional Type I / Type II reductions identifying the two analytic inputs needed for that route to the twin-prime asymptotic. |
| `findings/` | Individual result notes, including the Sidon computations from `n=128` through `n=1000`. |

## How to read the different result types

The repository contains several ordinary mathematical categories:

- **exact finite classification / optimum** — exhaustive computation establishes the stated finite result;
- **witness / lower bound** — an explicit object proves an existential statement or lower bound;
- **restricted-family exhaustion** — every object in a stated construction family has been checked;
- **theorem / structural lemma** — an ordinary mathematical statement with its stated hypotheses;
- **conditional reduction** — the conclusion follows once the named hypotheses are supplied;
- **literature status** — historical novelty is recorded separately from mathematical correctness.

Some historical files use internal labels such as `LIVE-CERTIFIED`; those mean that a finite/computational certificate is attached, not that the statement has been formalized in a proof assistant.

## 1. Binary Sidon sets: `f(7) >= 24`

`sidon/` contains a 24-vector subset of `{0,1}^7` whose 300 pairwise sums are all distinct (OEIS A309370). Run

```bash
python sidon/verify_sidon_d7_24.py
```

to check the witness. The result was also independently recomputed during the release.

## 2. Covering numbers and two strict Schoenheim separations

`covering/covering-firehose.jsonl` contains 677 verified `C(v,k,t)` rows over

```text
v in [5,35], k in [2,34], t in [1,6].
```

`covering/covering-bounds.json` checks the expected monotonicity relations with zero violations.

A recount corrected an earlier underclaim: twelve UNSAT rows cover **two parameter triples** whose true covering number is strictly above the Schoenheim general lower bound:

| v | k | t | Schoenheim | computation proves |
|---|---|---|---:|---|
| 7 | 4 | 2 | 4 | `C(7,4,2) >= 5` |
| 7 | 4 | 3 | 11 | `C(7,4,3) >= 12` |

Whether either inequality improves the best published table is a separate literature question.

## 3. Circulant Ramsey-family exhaustions

`ramsey/circulant-ramsey-exhaustion.json` checks:

- **1,048,575** circulant families for the `R(3,10)` condition at `n=40`, with zero witnesses;
- **262,143** circulant families for the `R(4,6)` condition at `n=36`, with zero witnesses.

Small known cases are included to confirm that the implementation can both accept and reject examples correctly.

The result is the complete elimination of those **circulant construction families** at those orders. It is not an unrestricted Ramsey-number computation.

## 4. Sidon/C3 divergence at `n=35`

One computation found that for `n<=34`, the maximum Sidon-set size agrees with the maximum under an additional C3-permutation-free constraint, while at **`n=35`** the recorded values separate as `8` versus `7`.

The original record did not preserve the exact C3 variant used in that comparison. The numerical calculation is therefore retained, while the comparison statement awaits reconstruction of that missing definition.

## 5. Twin-prime conditional reductions

`twin-primes/` develops Type I and Type II sufficiency conditions for the twin-prime asymptotic using a Heath-Brown decomposition. It isolates two analytic inputs that are not supplied in the repository:

- Type I distribution at level `1-ε` over unrestricted moduli;
- a nontrivial Type II bilinear bound at `M~N~x^(1/2)`.

The value of the packet is the explicit reduction and identification of those missing analytic estimates, together with corrections to earlier versions of the derivation.

## 6. Result notes

`findings/` contains individual notes for the Sidon sequence computations, circulant Ramsey searches, covering computations, and an `R(5,5)` certificate-related result.

## License

Apache-2.0.