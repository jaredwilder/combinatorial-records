# Erdős #701 / Chvátal — exact rank-2 hereditary star theorem

Author: Jared Wilder. Public release: 2026-09-11.

Let `F` be a finite hereditary family whose members all have size at most two. Define

`m(F)=max{|G| : G⊆F is pairwise intersecting}`

and

`Δ(F)=max_x |{A∈F : x∈A}|`.

## Theorem

For every such `F`,

`m(F)=Δ(F)`.

Thus the Chvátal star bound is exact throughout the entire rank-2 hereditary class.

### Proof

The lower bound is immediate: every full star is pairwise intersecting.

For the reverse inequality, let `G⊆F` be pairwise intersecting. If `G` contains a singleton `{x}`, then every member of `G` contains `x`, so `|G|≤Δ(F)`.

Otherwise every member of `G` has size two, so regard `G` as an intersecting edge family in a simple graph. If all edges share a common endpoint, again `|G|≤Δ(F)`. If not, choose `xy,xz∈G` and an edge not containing `x`; pairwise intersection forces that edge to be `yz`. Any further edge intersecting all three of `xy,xz,yz` is one of those three, so `|G|=3`.

Since `F` is hereditary and contains `xy` and `xz`, it also contains `{x}`. Hence the star at `x` contains `{x},xy,xz`, so `Δ(F)≥3=|G|`.

Therefore every pairwise intersecting subfamily has size at most `Δ(F)`.

This is a complete theorem for rank at most two. Historical novelty is a separate literature question.
