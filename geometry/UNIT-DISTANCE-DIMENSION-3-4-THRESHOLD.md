# Unit-distance graphs: a dimension-3 / dimension-4 density threshold

**Author:** Jared Wilder  
**Recovered from:** session-transcript mathematics sweep  
**Promoted:** 2026-09-13

This note records a clean structural distinction between unit-distance graphs in `R^3` and `R^4`.

## Theorem 1 — unit-distance graphs in R^3 are K_{3,3}-free

Let `G` be a finite unit-distance graph realized by distinct points in `R^3`. Then `G` contains no `K_{3,3}`.

### Proof

Suppose three distinct vertices `a,b,c` had three distinct common neighbors `x,y,z`. Then each common neighbor would lie in

\[
S(a,1)\cap S(b,1)\cap S(c,1),
\]

the intersection of the three unit spheres centered at `a,b,c`.

If `a,b,c` are non-collinear, the intersection of the first two unit spheres is a circle lying in their perpendicular-bisector plane, and intersecting that circle with the third sphere gives at most two points.

If `a,b,c` are collinear and distinct, there is no point equidistant from all three. Indeed, subtracting the equal squared-distance equations for `(a,b)` and `(b,c)` forces the projection of a common point onto the line of the centers to lie simultaneously in two distinct perpendicular-bisector planes.

Thus three distinct common neighbors are impossible. Hence `K_{3,3}` cannot occur. ∎

## Corollary — subquadratic edge count in R^3

By the Kövári–Sós–Turán bound for `K_{3,3}`-free graphs,

\[
e(G)\le \frac12\,2^{1/3}n^{5/3}+O(n).
\]

Since

\[
\frac12\,2^{1/3}=2^{-2/3}\approx0.6299605249,
\]

we obtain

\[
\boxed{e(G)=O(n^{5/3})=o(n^2).}
\]

In particular a claim of `Theta(n^2)` unit-distance edges uniformly for every fixed dimension `d>=3` is false already at `d=3`.

## Theorem 2 — quadratic construction from dimension 4 onward

In `R^4`, take two mutually orthogonal 2-dimensional coordinate planes. On each plane choose points on the circle of radius

\[
1/\sqrt2.
\]

For any point `u` on the first circle and any point `v` on the second,

\[
\|u-v\|^2=\|u\|^2+\|v\|^2=\frac12+\frac12=1.
\]

Thus all cross pairs are unit distances.

With `floor(n/2)` points on one circle and `ceil(n/2)` on the other, the unit-distance graph contains

\[
K_{\lfloor n/2\rfloor,\lceil n/2\rceil}
\]

and therefore has

\[
\left\lfloor\frac{n^2}{4}\right\rfloor
\]

unit-distance edges.

The same construction embeds in every `R^d` for `d>=4`.

## Status / novelty

**PROVED PROSE / CLASSICAL-STYLE EXTREMAL CONSEQUENCE.** No historical novelty claim is made. This was promoted because the exact dimension split and constant had existed only in the transcript-mining layer.
