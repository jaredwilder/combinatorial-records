# Simultaneously sum-free, product-free, and 3-AP-free subsets of `F_73^×`

**Author:** Jared Wilder  
**Source:** MathFire Round Ten  
**Status:** complete finite computational classification  
**Novelty posture:** `apparently_new_after_systematic_search` as of 2026-07-27; absolute historical novelty is not claimed.

Let `A` be a subset of the nonzero elements of the prime field `F_73`. Require all three conditions:

1. **sum-free:** no `x,y,z∈A`, repetitions allowed, satisfy `x+y=z`;
2. **product-free:** no `x,y,z∈A`, repetitions allowed, satisfy `xy=z`;
3. **nontrivial 3-AP-free:** no three distinct `a,b,c∈A` satisfy `a+c=2b`.

All equations are in `F_73`.

## Theorem

\[
\boxed{|A|\le12.}
\]

The bound is sharp. Exactly three subsets attain size `12`:

```text
{13,15,19,31,33,36,37,40,42,54,58,60}
{10,22,24,28,33,36,37,40,45,49,51,63}
{2,3,10,19,24,31,42,49,54,63,70,71}
```

The equivalent minimum forbidden-hypergraph transversal has size

\[
60.
\]

The compiled forbidden hypergraph has exactly

\[
7422
\]

distinct edges.

The canonical SHA-256 identity of the complete ordered extremal layer is

`50842bb25cfc9f387b70077733000817f4368e16ad29dc9cd010c3ab4fe6dd8a`.

## Exact proof mechanism

Each forbidden equation contributes a one-, two-, or three-vertex hyperedge. A valid set is exactly an independent set of the resulting finite hypergraph.

The primary exact solver:

- removes forced forbidden vertices;
- compiles two-vertex constraints into a compatibility graph;
- retains three-vertex constraints as pair-conditioned exclusions;
- performs exact branch-and-bound;
- uses greedy coloring only as a valid upper bound;
- enumerates the complete maximum layer.

It proves maximum `12` and exactly three extremizers after `271,416` search nodes.

## Independent verification

The independent program `verification/mixed_field_p73_independent.cpp` shares no MathFire package code. It independently rebuilds the forbidden relations and exact search and returns the same:

- modulus `73`;
- `7422` forbidden edges;
- maximum `12`;
- exactly `3` extremizers;
- the identical three extremal sets;
- `271,416` search nodes.

Recorded hashes:

- extremal layer SHA-256: `50842bb25cfc9f387b70077733000817f4368e16ad29dc9cd010c3ab4fe6dd8a`;
- independent C++ source SHA-256: `c48e0129126d4e884dcab641e1d8bdb8808895442ad8acc9d1c751a644f6546d`;
- independent output SHA-256: `a14e941d124ea551ed462681dbd491876d11e6e42d40e64c2024ae6cdea31a5b`.

## Claim boundary

This is a complete theorem for the single finite ambient group `F_73^×` under the three declared constraints. It is not an asymptotic theorem for arbitrary primes or finite fields.
