# Six-vertex graphs whose every edge lies in exactly one triangle

**Author:** Jared Wilder  
**Status:** exact finite classification  
**Scope:** simple undirected graphs on six labelled vertices

Consider graphs `G` on six vertices with the property

> every edge of `G` lies in **exactly one** triangle.

A historical research transcript claimed that exhaustive enumeration of all `2^15=32768` labelled graphs gave a maximum of 12 edges. That claim is false.

A fresh enumeration of every labelled graph on six vertices gives:

| number of edges | number of labelled graphs satisfying the property |
|---:|---:|
| 0 | 1 |
| 3 | 20 |
| 6 | 100 |

No other edge count occurs. Therefore

\[
\boxed{e(G)\le 6}
\]

and the bound is sharp.

The simplest extremizer is the disjoint union of two triangles.

## Why the old 12-edge construction fails

The historical argument started from the four triples

`{1,2,3}, {1,4,5}, {2,4,6}, {3,5,6}`

and treated their 12 block-edge incidences as though they formed a graph in which every edge lies in one triangle.

But taking the union of those edges creates additional triangles. For example the edge `12` lies both in the intended triangle `{1,2,3}` and in the unintended triangle `{1,2,4}`.

So a pair-packing condition on the listed triples is not sufficient: triangles created by edges coming from different blocks must also be checked.

## Verification

The companion script `verify_six_vertex_unique_triangle_edges.py` enumerates all `32768` graphs and recomputes, for each present edge `uv`, the number of common neighbours of `u` and `v`. The required condition is exactly that this number equal 1 for every edge.

## Provenance

Recovered by the raw-session transcript sweep, which identified that an earlier alleged exhaustive result contradicted the actual enumeration. Recomputed independently before publication here.

No historical novelty claim is made for this finite classification.
