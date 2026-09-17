# Combinatorial records

Exact finite classifications, witnesses, and structural results in covering designs, Ramsey theory, Sidon sets, finite fields, hereditary families, covering systems, automata, and additive encodings.

## Highlights

| subject | result |
|---|---|
| Rank-2 hereditary families | exact Chvátal theorem: the largest intersecting subfamily equals the largest star |
| Binary Sidon sets | explicit 24-element Sidon subset of `{0,1}^7` |
| Covering numbers | 677 verified `C(v,k,t)` rows in the stated finite range |
| Ramsey circulants | complete elimination of the tested `R(3,10)` order-40 and `R(4,6)` order-36 circulant families |
| Conference switching | impossibility theorem for the symmetric conference Ramsey-book construction class |
| Covering systems | exact seven-modulus obstruction for `{3,5,7,9,11,13,15}` |
| Finite fields | exact extremal classifications in `F_31^×`, `Z/31Z`, and `F_73^×` |
| Product/GP avoidance | exact extremal classification on `[50]` |
| Lonely Runner | theorem collection around the 13-effective-speed problem |
| Automata | finite transition monoids, quotients, and robustness identities |

## Rank-2 hereditary Chvátal theorem

For every finite hereditary family `F` whose members have size at most two,

\[
\boxed{m(F)=\Delta(F)},
\]

where `m(F)` is the maximum size of a pairwise-intersecting subfamily and `Δ(F)` is the largest full star.

The complete proof is [`erdos701-hereditary-rank2-star.md`](erdos701-hereditary-rank2-star.md).

## Binary Sidon witness

`sidon/` contains a 24-vector subset of `{0,1}^7` with all unordered pair sums distinct.

```bash
python sidon/verify_sidon_d7_24.py
```

The broader `f(7)` interval and exact search are now presented in [`binary-sidon-f7`](https://github.com/jaredwilder/binary-sidon-f7).

## Covering designs

`covering/covering-firehose.jsonl` contains 677 verified covering-number rows over

```text
v in [5,35]
k in [2,34]
t in [1,6].
```

Two exact lower-bound separations in the finite data are

\[
C(7,4,2)\ge5
\]

against the Schoenheim bound 4, and

\[
C(7,4,3)\ge12
\]

against the Schoenheim bound 11.

The `C(13,6,3)` program has its own repository: [`covering-13-6-3`](https://github.com/jaredwilder/covering-13-6-3).

## Ramsey construction classes

The circulant search checks:

- **1,048,575** order-40 circulant families for the `R(3,10)` condition, with no witness;
- **262,143** order-36 circulant families for the `R(4,6)` condition, with no witness.

These are complete eliminations of those construction families at those orders.

The conference-switching note proves that for `N=4m+2`, diagonal switching of the symmetric conference construction cannot simultaneously avoid the corresponding `B_m` and complementary `B_(m+1)` books.

A cleaner combined presentation is in [`ramsey-construction-class-eliminations`](https://github.com/jaredwilder/ramsey-construction-class-eliminations).

## Seven-modulus covering obstruction

No choice of one residue class for each modulus in

\[
\{3,5,7,9,11,13,15\}
\]

covers all integers.

Modulo the least common multiple, this is an exact finite obstruction on 45,045 residue classes. The density sum exceeds one, so simple density alone cannot prove the result.

## Finite-field classifications

Three complete finite classifications are collected under `finite-fields/`:

- simultaneous sum/product avoidance in `F_31^×`;
- sum-free and nontrivial-3-AP-free subsets of `Z/31Z`;
- simultaneous sum/product/nontrivial-3-AP avoidance in `F_73^×`.

The full maximizing layers and independent compiled verifiers are now in [`finite-field-extremal-sets`](https://github.com/jaredwilder/finite-field-extremal-sets).

## Other directories

| path | contents |
|---|---|
| `lonely-runner/` | finite and structural work for 13 effective speeds |
| `ramsey-r55/` | 41-vertex `(5,5)` Ramsey structure and extension lemmas |
| `covering/`, `covering-designs/` | covering-number tables, witnesses, and structural restrictions |
| `erdos500/` | Turán `(3,4)` deletion/inheritance material |
| `multiplicative/product-gp-free-50/` | exact product/GP-free classification on `[50]` |
| `automata/` | finite transition monoids and quotient calculations |
| `additive-encodings/` | additive-encoding constructions and theorems |
| `witness-vault/` | concrete finite witness objects |
| `twin-primes/` | conditional Type I / Type II reductions |
| `findings/` | individual finite result notes |

## Focused subject repositories

Several large subjects originally stored here now have dedicated reading surfaces:

- [`finite-field-extremal-sets`](https://github.com/jaredwilder/finite-field-extremal-sets)
- [`binary-sidon-f7`](https://github.com/jaredwilder/binary-sidon-f7)
- [`covering-13-6-3`](https://github.com/jaredwilder/covering-13-6-3)
- [`ramsey-r55-circulant-41`](https://github.com/jaredwilder/ramsey-r55-circulant-41)
- [`ramsey-construction-class-eliminations`](https://github.com/jaredwilder/ramsey-construction-class-eliminations)
- [`lonely-runner-13`](https://github.com/jaredwilder/lonely-runner-13)
- [`three-resource-transition-monoid`](https://github.com/jaredwilder/three-resource-transition-monoid)

This repository remains the compact cross-subject collection and source archive for the smaller results.

Author: Jared Wilder. License: Apache-2.0.
