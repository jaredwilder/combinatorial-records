# Covering design C(13,6,3) — two 21-block witnesses and the strengthened target-20 structure

**Estate source:** MSL Pass-3 + final September-2 singular synthesis  
**Point set:** `{0,1,...,12}`  
**Status:** exact witnesses + necessary structure; **no 20-block UNSAT certificate is claimed**

A `(13,6,3)` covering is a family of 6-subsets of 13 points in which every 3-subset is contained in at least one block.

The recovered estate contains two independently validated 21-block coverings. Each was checked against all

\[
\binom{13}{3}=286
\]

triples, with zero missing triples.

The September-2 source audit also reported that the two incidence structures are non-isomorphic to one another and were separated from the repository benchmark used in that audit. That is **not** promoted here to a globally exhaustive novelty/classification claim; archive-wide isomorphism classification remains a separate task.

The strongest late synthesis materially improves the original target-20 reduction below: the old `r_x>=8` / 16-excess package is superseded by **`r_x>=9` and only three possible global point-degree multisets**.

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

## Strengthened necessary structure of any hypothetical 20-block cover

### Point degree is at least 9

Fix a point `x`. Every triple `{x,y,z}` must lie in a block through `x`. Delete `x` from all blocks containing it. The resulting `r_x` five-subsets of the other 12 points cover every pair, hence form a `C(12,5,2)` cover.

Using the exact value

\[
C(12,5,2)=9,
\]

we obtain

\[
\boxed{r_x\ge9\quad\text{for every }x.}
\]

This supersedes the older pair-counting lower bound `r_x>=8`.

### Only three global point-degree multisets survive

Twenty 6-blocks contain exactly

\[
\sum_x r_x=20\cdot6=120
\]

point incidences. The compulsory baseline is now `13*9=117`, leaving only three excess degree units. Therefore the point-degree multiset must be exactly one of

\[
\boxed{(12,9^{12})},
\]

\[
\boxed{(11,10,9^{11})},
\]

or

\[
\boxed{(10,10,10,9^{10})}.
\]

In particular, every hypothetical 20-cover has at least **10 degree-9 points**, and each degree-9 point induces an optimal nine-block `C(12,5,2)` neighborhood.

### Pair multiplicity is at least 3

Fix a pair `{x,y}`. There are 11 triples containing it, while a 6-block containing the pair covers only four choices of the third point. Thus

\[
\boxed{r_{xy}\ge3.}
\]

Globally,

\[
\sum_{\{x,y\}}r_{xy}=20\binom62=300,
\]

so

\[
\boxed{\sum_{\{x,y\}}(r_{xy}-3)=300-3\binom{13}{2}=66.}
\]

For an individual point,

\[
\sum_{y\ne x}(r_{xy}-3)=5r_x-36,
\]

which is `9,14,19,24` when `r_x=9,10,11,12`, respectively.

### Every degree-9 point has at least three multiplicity-3 neighbors

If `r_x=9`, then

\[
\sum_{y\ne x}r_{xy}=45.
\]

Write `e_y=r_xy-3>=0`. The twelve integers `e_y` sum to 9, so at most nine are positive. Therefore at least three vanish:

\[
\boxed{r_x=9\Longrightarrow \#\{y:r_{xy}=3\}\ge3.}
\]

Consequently the three global degree patterns force at least 18, 17, or 15 distinct multiplicity-3 pairs, respectively (count degree-9 endpoints and divide by at most two per pair).

### Exact local geometry around a multiplicity-3 pair

Take `{x,y}` with `r_xy=3`. Delete `x,y` from the three blocks containing the pair. We obtain three 4-subsets of the remaining 11 points whose union must be all 11 points.

Those sets carry 12 incidences on 11 points. Hence exactly one point occurs twice and the other ten occur once. Equivalently:

\[
\boxed{\text{exactly one pair of the three 4-subsets intersects in one point; the other two pairwise intersections are empty.}}
\]

So among the original three 6-blocks through `{x,y}`, exactly two share one additional point `z`, while the third shares no point beyond `{x,y}` with either of those two.

## Correct exact-close program

The public frontier represented by this archive remains

\[
20\le C(13,6,3)\le21.
\]

A certified target-20 impossibility proof immediately closes the value at 21. The strengthened search should therefore:

1. anchor a degree-9 point (every global pattern has at least ten);
2. enumerate/classify optimal nine-block `C(12,5,2)` neighborhoods up to isomorphism;
3. lift those nine local blocks to the nine 6-blocks containing the anchor;
4. choose only eleven further blocks not containing it;
5. branch on the three global degree multisets;
6. enforce pair multiplicity, exact degree budgets, and the degree-9 excess equation;
7. branch early on guaranteed multiplicity-3 pairs and their exact three-block intersection template;
8. quotient by the automorphism group of the anchored neighborhood;
9. emit a replayable UNSAT certificate or independently checkable exhaustive log.

The archive's earlier raw MILP attempt did **not** prove infeasibility. Search failure is not a certificate. Until target 20 is actually eliminated, **`C(13,6,3)=21` is not claimed**.

## Reproducibility

The two block lists above are sufficient for independent checking of the upper bound: enumerate every 3-subset of `{0,...,12}` and verify that at least one displayed block contains it. No appeal to the original search procedure is needed.
