# Product-free and geometric-progression-free subsets of `[50]`

**Author:** Jared Wilder  
**Release class:** exact finite extremal computation  
**Source:** MathFire 8.0.0 Round Eight  
**Status:** `COMPUTATIONALLY_EXACT_FINITE_RESULT`  

## Theorem

Let

\[
A\subseteq\{1,\dots,50\}.
\]

Assume:

1. no `x,y,z∈A` satisfy `xy=z`, with repetitions allowed;
2. no distinct `a<b<c` in `A` satisfy
   \[
   b^2=ac.
   \]

Then

\[
|A|\le 35.
\]

The bound is sharp. There are exactly **240** extremal sets of size `35`.

## Exact reduction

Create one forbidden hyperedge for every multiplicative relation `xy=z` allowed by the declared semantics and every nontrivial three-term geometric progression `a<b<c`, `b²=ac`.

A valid subset is exactly an independent set of this finite hypergraph. Therefore its complement is a transversal and

\[
\alpha=50-\tau.
\]

The frozen campaign computed

\[
\tau=15,
\qquad
\alpha=35.
\]

## Independent computational agreement

The result was reproduced by:

- two independent Python implementations;
- one independent C implementation.

All three agreed on:

- minimum transversal: **15**;
- maximum independent-set size: **35**;
- number of extremizers: **240**.

The MathFire verification bundle reported:

- `4109 / 4109` total tests passed;
- `901 / 901` named adversarial attacks passed;
- `364 / 364` Round-Eight campaigns passed;
- clean-wheel replay: PASS.

## Certificate identity

The source theorem packet records:

- **149** generated forbidden hyperedges;
- minimum transversal `15`;
- maximum `35`;
- `240` extremizers;
- canonical digest
  `cea2d1f707e94d388369a9c61030dd3ce9908b8a0b981419bb90f7cfa4721188`;
- a concrete extremal witness;
- the exact intersection core of all extremizers.

The MathFire product/GP C source was recorded with SHA-256

`f0a81f378618fe1723133fe21d8b1bcd1728ac646efcd5075adfaf2c2983c8e3`.

## Claim boundary

This is a finite theorem about the declared universe `[50]`. It is not an asymptotic theorem, and this release does not assert historical novelty until the finite extremal result is compared against the literature.
