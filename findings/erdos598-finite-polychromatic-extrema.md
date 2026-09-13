# Exact finite polychromatic extrema extracted from the Erdős #598 campaign

**Status:** exact finite mathematics only. No transfer to the canonical infinite/cardinal problem is claimed.

## Finite model

Fix integers `N`, `k`, `K` with `k <= K <= N`.

Color the `k`-subsets of `[N]`. A used color class is called **good** if every `K`-subset of `[N]` contains at least one `k`-subset of that color.

Let

\[
L(N,K,k)
\]

be the minimum size of a good color class, and let

\[
P(N,K,k)
\]

be the maximum number of colors in a coloring for which every used color is good.

Every used color class has size at least `L`, and the color classes are disjoint, so the universal counting bound is

\[
P(N,K,k)\le
\left\lfloor
\frac{\binom Nk}{L(N,K,k)}
\right\rfloor.
\]

The three parameter points below attain this bound exactly.

## Theorem

Under the finite semantics above,

\[
\boxed{L(4,3,2)=2,\qquad P(4,3,2)=3,}
\]

\[
\boxed{L(5,3,2)=4,\qquad P(5,3,2)=2,}
\]

and

\[
\boxed{L(6,4,2)=3,\qquad P(6,4,2)=5.}
\]

In all three cases,

\[
P(N,K,k)
=
\left\lfloor\frac{\binom Nk}{L(N,K,k)}\right\rfloor.
\]

## `(4,3,2)`

A two-edge family such as

\[
\{12,34\}
\]

meets every three-subset of `[4]`, so `L<=2`. A one-edge family misses the complementary three-subset omitting both of its endpoints, hence `L=2`.

The six edges of `K_4` split into the three perfect matchings

\[
\{12,34\},\quad
\{13,24\},\quad
\{14,23\}.
\]

Every triple contains exactly one edge from each matching, so all three color classes are good. The counting bound gives

\[
P\le\lfloor6/2\rfloor=3,
\]

therefore `P=3`.

## `(5,3,2)`

A good edge family is exactly an edge set meeting every triple, equivalently its complement graph has no triangle.

A three-edge graph on five vertices cannot meet every triple: its complement has seven edges, and every triangle-free graph on five vertices has at most six edges. Hence `L>=4`.

A 5-cycle complement example supplies a four-edge good family, so `L=4`.

The ten edges of `K_5` split into a 5-cycle and its complementary 5-cycle. Both classes meet every triple, giving two colors. The counting bound gives

\[
P\le\lfloor10/4\rfloor=2,
\]

hence `P=2`.

## `(6,4,2)`

A two-edge family cannot be good. If the two edges are disjoint, choose a four-set containing one endpoint from each edge and two other vertices; if they share a vertex, choose a four-set avoiding that shared vertex and one suitable remaining endpoint. In particular the naive lift `\{12,34\}` is missed by

\[
\{1,3,5,6\}.
\]

Thus `L>=3`.

Every perfect matching of `K_6` has three edges and meets every four-set: a four-set cannot avoid all three matching edges, because choosing at most one endpoint from each matched pair gives at most three vertices. Hence `L=3`.

A one-factorization of `K_6` partitions all fifteen edges into five perfect matchings, for example

\[
\begin{aligned}
M_1&=\{16,25,34\},\\
M_2&=\{26,13,45\},\\
M_3&=\{36,24,15\},\\
M_4&=\{46,35,12\},\\
M_5&=\{56,14,23\}.
\end{aligned}
\]

Thus `P>=5`; the counting bound gives

\[
P\le\lfloor15/3\rfloor=5,
\]

so `P=5`.

## Why this record exists

The raw campaign contained conflicting historical rows for the `(6,4,2)` point. One route reported `L=4` and only three colors. A later deterministic certifier exhaustively enumerated all subfamilies of the fifteen edges and returned

`L(6,4,2)=3`, `P(6,4,2)=5`,

with the one-factorization witness above. The latter is also immediately confirmed by the elementary perfect-matching argument, so the older `L=4` row is stale.

## Scope boundary

These are **finite exact extremal values** under the declared finite coloring semantics. The original campaign investigated an infinite/cardinal problem around Erdős #598, but its attempted finite-to-infinite transfer was explicitly rejected. Nothing in this note certifies an infinite-cardinal statement.

`verify_erdos598_finite.py` independently enumerates the finite good-family minima and validates the witness partitions.
