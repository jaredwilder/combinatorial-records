# A cyclic extremal witness for R(4,5)

**Author:** Jared Wilder  
**Recovered from:** session-transcript mathematics sweep  
**Promoted:** 2026-09-13

Consider the undirected circulant graph on `Z/24Z` with connection set

\[
S=\pm\{1,2,4,8,9\}.
\]

Thus distinct vertices `u,v` are adjacent exactly when

\[
v-u\pmod{24}\in S.
\]

## Exact finite statement

The graph has:

- 24 vertices;
- degree 10;
- 120 edges;
- **no `K_4`**;
- **no independent set of size 5**;
- maximum clique size 3;
- maximum independent-set size 4.

Therefore it is a concrete cyclic `(4,5)` Ramsey graph on 24 vertices and witnesses

\[
R(4,5)\ge25.
\]

Combined with the classical exact value `R(4,5)=25`, it is an extremal witness.

## Reproducibility

The connection set alone determines the full graph. A direct verifier can enumerate all `C(24,4)=10626` four-subsets for cliques and all `C(24,5)=42504` five-subsets for independent sets.

No probabilistic search or stored adjacency matrix is needed.

## Status / novelty

**EXACT FINITE WITNESS.** This is not presented as a new value of `R(4,5)`; the value 25 is classical. The point of this record is to preserve a clean cyclic extremal construction that had previously existed only inside the transcript-mining layer.
