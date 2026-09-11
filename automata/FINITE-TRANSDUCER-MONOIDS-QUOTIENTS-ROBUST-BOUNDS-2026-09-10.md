# Finite Transducer Monoids, Quotients, and Robust Certificate Bounds

**Author:** Jared Wilder  
**Public release:** 2026-09-10

This packet publishes the abstract algebra / coding theory from the Kitchen/Humu programs while withholding the concrete product catalogs, exact resource-machine layouts, and capsule/checkpoint implementations.

## 1. Minimal Fully Abstract Compositional Quotient
Words are observationally equivalent exactly when their canonical summaries agree. The image monoid is the smallest exact compositional summary space: every exact summary interface must contain at least one distinguishable value for each image-monoid element.

## 2. Quotient-Before-Encoding Principle
For exact compositional certificates, behaviorally quotienting the reachable summary space before numeric encoding can be exponentially or unboundedly smaller than directly encoding raw histories or the full universal behavior-table space.

## 3. Log-Depth Ordered Parallel Composition
Because canonical summary composition is associative, an ordered sequence of T block summaries can be reduced by any order-preserving balanced binary tree in ceil(log2 T) composition depth. Permutation is forbidden because the monoid is generally noncommutative.

## 4. Canonical Additive Transducer Monoid
For a deterministic additive transducer, block summaries S_u=(F_u,G_u) form a monoid under (F,G) star (F',G')=(F'∘F, q↦G(q)+G'(F(q))). The summary map from words is a monoid homomorphism.

## 5. Fully Abstract Compositional Block Certificate
Under observation of final semantic state and additive delta for every possible start state, two blocks are behaviorally equivalent exactly when their semidirect summaries are equal. If the delta family is bounded, the entire summary table can be packed injectively into one integer.

## 6. Optimal Heterogeneous Channel Packing
For arbitrary centered channel digits with coordinate bounds A_c, mixed radices 2A_c+1 minimize the full-product output span. Uniform worst-case padding is never smaller and is strictly larger when channel bounds differ.

## 7. Semidirect Order-Aware Block Summary Theorem
For a deterministic additive transducer, every block u has exact summary S_u=(F_u,G_u), where F_u maps each start state to its final state and G_u records the state-conditioned additive delta. Sequential composition obeys F_{uv}=F_v o F_u and G_{uv}=G_u + G_v o F_u.

## 8. Optimal Robust Canonical Certificate Theorem
For a canonical behavior monoid of size N, any q-ary certificate correcting t substitutions and e erasures needs at least ceil(log_q N)+2t+e symbols; a suitable MDS/Reed-Solomon code attains it.

## 9. Fault-Localized Parallel Composition Tree
T ordered verified blocks compose in ceiling(log2 T) depth through robust decode-compose-reencode nodes.

## 10. No Additive Shortcut for Noncommutative Behavior
**Negative theorem.** Ordinary integer addition cannot replace noncommutative behavior composition without identifying some ordered products.

## 11. One-Symbol-Short Ambiguity Theorem
**Negative theorem.** At length k+2t+e-1, unique correction fails in general; an explicit ambiguity is included in the source archive.

## Authority / IP boundary

These statements preserve the abstract mathematical layer. The exact three-resource and four-resource product machines, shared behavior catalogs, capsule formats, checkpoint protocols and other technical implementation details are intentionally not disclosed here.