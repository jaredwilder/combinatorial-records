# Exact product-free / nontrivial-GP-free classification on `[50]`

**Status:** complete exact finite theorem.  
**Scope:** subsets of `{1,...,50}` only.  
**Historical novelty:** deferred to the later novelty court; the source campaign carried an apparently-new-after-search label, not an absolute priority claim.

## Theorem

Let

\[
A\subseteq\{1,2,\ldots,50\}.
\]

Require simultaneously:

1. **product-free:** there are no `x,y,z in A`, with repeated factors allowed, satisfying
   \[
   xy=z;
   \]
2. **nontrivial geometric-progression-free:** there are no distinct
   \[
   a<b<c
   \]
   in `A` satisfying
   \[
   b^2=ac.
   \]

Then

\[
\boxed{|A|\le35.}
\]

The bound is sharp, and exactly

\[
\boxed{240}
\]

subsets attain size 35.

Equivalently, the forbidden-hypergraph formulation on the 50-element ground set has:

- **149** distinct forbidden hyperedges;
- minimum transversal size **15**;
- maximum independent-set size **35**;
- exactly **240** maximum independent sets.

## Exact computational authority

The source release records agreement of:

- two independent Python implementations;
- an independently written C verifier.

The recovered independent C output is:

```text
limit=50
edge_count=149
minimum_transversal=15
maximum=35
extremal_count=240
nodes=57726
```

and prints an explicit first extremizer

```text
[8,10,13,14,15,16,17,19,21,22,23,24,25,26,27,28,29,30,31,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,50]
```

The source campaign also froze the complete extremal layer by digest beginning

`cea2d1f7...`.

The proof authority is **finite exhaustive computation with independent implementations**, not a claimed general asymptotic theorem.

## Why this was promoted

The theorem was previously public under the broad archive path

`unpublished-math-papers/product-gp-free-50/`.

That is useful provenance but a poor canonical destination for a complete finite extremal classification. This page gives the mathematical result a stable subject-facing identity in `combinatorial-records`.

## Scope boundary

Nothing here classifies the corresponding problem on `[N]` for general `N`, nor a finite-field analogue. Those are separate objects and should not be conflated with this exact `[50]` theorem.
