# Exact mixed additive–multiplicative classification in `F_73^×`

**Status:** complete exact finite theorem.  
**Scope:** the single group `F_73^×`.  
**Historical novelty:** deferred to the later novelty court; the source search found no exact prior match but absolute priority is not claimed here.

## Theorem

Let

\[
A\subseteq\mathbb F_{73}^{\times}.
\]

Require all three conditions, with arithmetic modulo 73:

1. **sum-free:** no `x,y,z in A`, repetitions allowed, satisfy
   \[
   x+y=z;
   \]
2. **product-free:** no `x,y,z in A`, repetitions allowed, satisfy
   \[
   xy=z;
   \]
3. **nontrivial 3-AP-free:** no three distinct `a,b,c in A` satisfy
   \[
   a+c=2b.
   \]

Then

\[
\boxed{|A|\le12.}
\]

The bound is sharp. Exactly three subsets attain size 12:

```text
{13,15,19,31,33,36,37,40,42,54,58,60}
{10,22,24,28,33,36,37,40,45,49,51,63}
{2,3,10,19,24,31,42,49,54,63,70,71}
```

The equivalent forbidden-hypergraph classification has:

- **7,422** distinct forbidden hyperedges;
- minimum transversal size **60**;
- maximum independent-set size **12**;
- exactly **3** maximum independent sets.

The canonical SHA-256 identity of the complete ordered extremal layer is

`50842bb25cfc9f387b70077733000817f4368e16ad29dc9cd010c3ab4fe6dd8a`.

## Exact proof mechanism

Each forbidden equation produces a one-, two-, or three-vertex hyperedge. Valid sets are exactly independent sets of this finite hypergraph.

The primary exact solver:

- removes forced forbidden vertices;
- compiles two-vertex constraints into a compatibility graph;
- retains three-vertex constraints as pair-conditioned exclusions;
- uses exact branch-and-bound;
- uses greedy coloring only as a sound upper bound;
- enumerates the complete maximum layer.

It returns maximum 12 and exactly three extremizers after **271,416** search nodes.

## Independent verification

The source's independently written C++ verifier reconstructs the forbidden relations from scratch and returns exactly:

- modulus `73`;
- edge count `7422`;
- maximum `12`;
- extremal count `3`;
- search nodes `271416`;
- the same three extremal sets.

Recovered source metadata records the independent verifier SHA-256

`c48e0129126d4e884dcab641e1d8bdb8808895442ad8acc9d1c751a644f6546d`

and independent output SHA-256

`a14e941d124ea551ed462681dbd491876d11e6e42d40e64c2024ae6cdea31a5b`.

## Publication history

This theorem previously lived primarily under

`unpublished-math-papers/f73-mixed-avoidance/`

and inside MathFire release material. The mathematical statement is independent of the engine that found it, so this page gives it a stable canonical home beside the separate `F_31^×` exact classification.

## Scope boundary

This does not establish an asymptotic theorem or a formula for arbitrary primes `p`. The exact theorem is the complete `p=73` classification under the three stated constraints.
