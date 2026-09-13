# Explicit SQS(20) P15 — rigidity, trade geometry, and repair radius

**Status:** exact finite theorems for one explicit reconstructed 15-pack of pairwise-disjoint Steiner quadruple systems on 20 points.  
**Parent status:** Erdős #835 / the full large-set question is **not** closed by these results.  
**Novelty:** targeted prior-art searches in the source campaign found no exact pack-specific match; historical novelty is intentionally **unclaimed pending specialist review**.

## The finite object

Let

\[
P=\{S_0,\ldots,S_{14}\}
\]

be the explicit reconstructed 15-pack of pairwise-disjoint `SQS(20)` used in the source release. Each system has 285 blocks. Their union therefore contains 4275 of the 4845 four-subsets of the 20-point set, leaving exactly

\[
570
\]

uncovered four-subsets, called the **holes**.

The theorem statements below are about these exact P15 bytes only. They are not claims about all 15-packs of `SQS(20)`.

---

## Theorem A — every 14-subpack uniquely forces the fifteenth system

For every index `i`, the only `SQS(20)` disjoint from all fourteen systems

\[
P\setminus\{S_i\}
\]

is `S_i` itself.

Equivalently:

> **Every 14-subpack of this explicit P15 uniquely determines its fifteenth constituent.**

### Exact certificate architecture

Freeze the other fourteen systems. A replacement for `S_i` can use only:

- the 285 blocks of `S_i`, and
- the 570 holes.

Thus there are 855 binary replacement/removal variables.

For each of the 1140 triples `t` on the 20 points:

- exactly one old block `s(t) in S_i` contains `t`;
- exactly two holes `r_1(t),r_2(t)` contain `t`.

The SQS condition becomes the homogeneous system

\[
x_{r_1(t)}+x_{r_2(t)}-y_{s(t)}=0
\]

for all 1140 triples.

For **each of all 15 choices** of `i`, reduction over `GF(5)` gives:

- matrix size: `1140 x 855`;
- rank: `849`;
- nullity: `6`;
- exhaustive nullspace coefficient search: `5^6 = 15625` vectors;
- nonzero binary nullvectors: `0`.

Any integer binary trade would reduce to a binary solution mod 5. Therefore the zero trade is the only possible replacement.

This is an exact algebraic impossibility certificate, not a MILP timeout.

---

## Theorem B — complete pair-trade classification

For any two systems `S_i,S_j`, form the bipartite graph on their 570 blocks, joining two blocks when they share a triple.

Because every triple occurs exactly once in each SQS, this graph is 4-regular and its connected components are precisely the indecomposable Steiner 3-trades between the two systems.

Exact enumeration of all

\[
\binom{15}{2}=105
\]

constituent pairs yields exactly two component profiles:

### Same reconstruction row

There are **30** such pairs. Their per-side trade volumes are

\[
(30,30,225).
\]

Thus each same-row pair decomposes into two small independent volume-30 trades and one volume-225 component.

### Different reconstruction rows

There are **75** such pairs. Each pair has one indecomposable component of per-side volume

\[
(285).
\]

Hence:

> **The 105 pair unions in this explicit P15 have exactly two Steiner-trade geometries, determined by same-row versus cross-row provenance in the reconstruction.**

---

## Theorem C — repair radius at least three

The 570 holes form the `q=2` residual block graph. Exact enumeration gives component profile

\[
250,\quad 12\times25,\quad 4\times5.
\]

Each of the four 5-vertex components is a `K_5`.

Now retain `m` systems from the P15 and ask whether they can occur inside a full large set of 17 pairwise-disjoint `SQS(20)`. The residual graph would need

\[
q=17-m
\]

colors. Since the four `K_5` components persist when these old constituents are retained,

\[
q\ge5.
\]

Therefore

\[
17-m\ge5,
\qquad
m\le12.
\]

So:

\[
\boxed{\text{any full large set extending from this P15 must replace at least three of its systems.}}
\]

This is a pack-relative theorem. It does not assert that no `LS(SQS(20))` exists.

---

## Structural interpretation

A **gauge trade** redistributes blocks among existing constituents while preserving the same 4275-block union. Such a trade leaves all 570 holes unchanged, and therefore cannot remove the residual `K_5` obstruction.

A genuine escape toward a full large set must therefore be a **physical trade** importing hole blocks and changing the union. Theorems A–C imply that such an escape must couple at least three old constituents.

The source campaign's next mathematically meaningful target was consequently not another naked coloring search, but:

> find or rule out the minimum-support physical Steiner 3-trade that intersects the 570-hole set and couples at least three P15 constituents.

---

## Related exact identity

For the residual triple-vs-block incidence matrix `M` and residual adjacency matrix `A`, the source derives

\[
M^TM=A+4I.
\]

Thus `ker(M)` is exactly the `-4` eigenspace of `A`; algebraically, it is the signed Steiner 3-trade space. This explains why an ordinary Hoffman-bound attack lands automatically on equality and cannot by itself distinguish repair instances.

This identity is useful structural context but is not claimed here as novel.

---

## Authority and missing-byte boundary

The source Library contains the human theorem records and references an exact package with:

- `data/eh15_sqs20.json` — the explicit P15;
- `results/ONE_COORDINATE_RIGIDITY.json`;
- `src/verify_one_coordinate_rigidity.py`;
- pair-trade profile enumeration;
- residual-graph / repair-radius calculations.

The complete 25-file source package has now been recovered and published in
the [Erdős #835 subject home](https://github.com/jaredwilder/erdos835-lean-audit#exact-source-package-and-fresh-replay).
The exact P15, original verifiers and historical receipts are present with
ZIP provenance and file hashes. A fresh replay checks all 15 rigidity systems,
all 105 pair profiles, the spectral-incidence identity and an independent
reconstruction of the four residual K5 obstructions. The original
source-package recovery gap is resolved for this v0.7 package.

## Provenance

Recovered from the J-SPACE v0.7 Erdős #835 rounds 21–40 release, especially:

- `00_TERMINAL_RESULT.md`;
- `01_ROUNDS_31_40_LEDGER.md`;
- `02_ONE_COORDINATE_RIGIDITY.md`;
- `04_REPAIR_RADIUS.md`;
- `06_GOLD_SWEEP.md`.

Those source records explicitly distinguish these closed finite theorems from the still-open global large-set problem.
