# Covering design C(13,6,3) — two 21-block witnesses and the target-20 structure

**Estate source:** MSL Pass-3 / witness vault  
**Point set:** `{0,1,...,12}`  
**Status:** exact witnesses + necessary structure; **no 20-block UNSAT certificate is claimed**

A `(13,6,3)` covering is a family of 6-subsets of 13 points in which every 3-subset is contained in at least one block.

The recovered estate contains two independently validated 21-block coverings. Each was checked against all

\[
\binom{13}{3}=286
\]

triples, with zero missing triples.

The September-2 source audit also reported that the two incidence structures are non-isomorphic to one another and were separated from the repository benchmark used in that audit. That is **not** promoted here to a globally exhaustive novelty/classification claim; archive-wide isomorphism classification remains a separate task.

## Witness A — `run20_C13_6_3_cover21`

```text
{0,3,4,5,7,9}
{2,5,7,8,9,10}
{1,2,4,8,9,11}
{3,4,5,6,8,11}
{0,1,2,4,6,7}
{0,2,6,8,9,12}
{0,1,2,5,11,12}
{0,1,3,5,8,12}
{1,2,3,4,8,9}
{1,5,6,7,9,12}
{2,6,9,10,11,12}
{0,1,3,9,10,11}
{3,4,6,9,10,12}
{2,3,7,10,11,12}
{0,2,3,5,6,10}
{5,7,8,9,10,11}
{0,4,7,8,10,12}
{1,3,6,7,8,10}
{0,4,8,10,11,12}
{1,2,4,5,10,12}
{0,1,4,6,7,11}
```

Independent estate validation:

```text
triples_total   = 286
triples_covered = 286
missing         = 0
PASS
```

## Witness B — `run23b_C13_6_3_cover21`

```text
{0,1,2,5,6,12}
{0,1,3,7,8,11}
{0,1,4,7,9,10}
{0,1,4,8,10,11}
{0,2,3,4,8,10}
{0,2,3,7,9,12}
{0,2,4,8,11,12}
{0,3,4,5,6,7}
{0,4,5,6,10,12}
{0,5,6,8,9,11}
{1,2,3,4,6,8}
{1,2,3,5,10,12}
{1,2,6,7,9,11}
{1,3,5,8,9,12}
{1,4,5,7,11,12}
{1,6,7,8,10,12}
{2,3,5,7,10,11}
{2,4,5,7,8,9}
{2,5,6,8,9,10}
{3,4,6,9,11,12}
{3,6,9,10,11,12}
```

Independent estate validation:

```text
triples_total   = 286
triples_covered = 286
missing         = 0
PASS
```

## Necessary structure of any hypothetical 20-block cover

The campaign's strongest theorem is not another heuristic search. It is a rigid incidence package that every 20-block solution would have to satisfy.

### Pair multiplicity

Fix a pair `{x,y}`. There are 11 triples containing it:

\[
\{x,y,z\},\qquad z\ne x,y.
\]

A 6-block containing the pair contains only four possible third points. If `r_xy` is the number of blocks containing `{x,y}`, then

\[
4r_{xy}\ge11,
\]

so

\[
\boxed{r_{xy}\ge3.}
\]

### Point degree

Let `r_x` be the number of blocks containing point `x`. Counting pair incidences through `x`,

\[
5r_x=\sum_{y\ne x}r_{xy}.
\]

Since there are 12 other points and each pair multiplicity is at least 3,

\[
5r_x\ge36,
\]

hence

\[
\boxed{r_x\ge8.}
\]

### Global excess budget

Twenty 6-blocks contain exactly

\[
20\cdot6=120
\]

point incidences. The compulsory baseline `r_x>=8` uses

\[
13\cdot8=104.
\]

Therefore any 20-cover must satisfy the exact excess identity

\[
\boxed{\sum_x(r_x-8)=16.}
\]

That leaves very little room for irregular point degrees.

### Degree-eight local profiles

If `r_x=8`, then

\[
\sum_{y\ne x}r_{xy}=40.
\]

The baseline twelve 3's contributes 36, leaving exactly four excess pair incidences. Thus the multiset

\[
\{r_{xy}:y\ne x\}
\]

has exactly one of five forms:

\[
\boxed{(7,3^{11})},
\]

\[
\boxed{(6,4,3^{10})},
\]

\[
\boxed{(5,5,3^{10})},
\]

\[
\boxed{(5,4,4,3^9)},
\]

or

\[
\boxed{(4,4,4,4,3^8)}.
\]

This is the local profile constraint encoded by the estate's `Cover20Degree` formal asset.

## Exact close program

A direct target-20 formulation uses one Boolean variable for each of the

\[
\binom{13}{6}=1716
\]

possible blocks, the 286 triple-cover constraints, and cardinality 20.

The archive's raw MILP attempt did **not** prove infeasibility. Search failure is not a certificate.

The correct next close is therefore:

1. compile the pair multiplicity, point-degree, excess-budget and degree-8-profile theorems into the target-20 instance;
2. add symmetry breaking;
3. solve by SAT / pseudo-Boolean / certified CP;
4. if UNSAT, retain a replayable DRAT/LRAT/VeriPB-style proof certificate.

Only such a certificate (or a mathematical impossibility proof) upgrades this program from a 21-block witness/20-block structural reduction to an exact covering-number determination.

## Reproducibility

The two block lists above are sufficient for independent checking: enumerate every 3-subset of `{0,...,12}` and verify that at least one displayed block contains it.

No appeal to the original search procedure is needed to verify the two upper-bound witnesses.