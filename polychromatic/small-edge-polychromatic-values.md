# Three exact small edge-polychromatic values

**Author:** Jared Wilder  
**Recovered from:** the Erdős #598 campaign's finite analogue  
**Status:** elementary exact finite theorem; no infinitary transfer claimed

For integers `n>=K>=2`, colour the edges of the complete graph `K_n` with `q` colours. Call the colouring **`K`-polychromatic** if every `K`-vertex subset contains at least one edge of every used colour.

Let

\[
P(n,K)
\]

be the maximum possible number of colours.

The recovered finite campaign yields three exact values:

\[
\boxed{P(4,3)=3,\qquad P(5,3)=2,\qquad P(6,4)=5.}
\]

They admit short proofs independent of the original exhaustive certificate.

## General covering-number upper bound

For any one colour, its edge class must meet every `K`-vertex subset. If `L(n,K)` is the minimum number of edges in a graph on `n` vertices that meets every `K`-subset, then every colour class has at least `L(n,K)` edges. Hence

\[
qL(n,K)\le\binom n2,
\]

so

\[
\boxed{P(n,K)\le\left\lfloor\frac{\binom n2}{L(n,K)}\right\rfloor.}
\]

Equivalently, the complement of a minimum hitting edge set is a graph with no `K`-clique, so

\[
L(n,K)=\binom n2-\operatorname{ex}(n,K_K).
\]

## 1. `P(4,3)=3`

A colour class meeting every 3-subset of `[4]` needs at least two edges: one edge misses the triple on the other three vertices.

Thus

\[
P(4,3)\le\lfloor 6/2\rfloor=3.
\]

For equality, partition the six edges of `K_4` into its three perfect matchings:

```text
{01,23}
{02,13}
{03,12}
```

Every 3-vertex subset contains exactly one edge from each matching. Therefore

\[
\boxed{P(4,3)=3}.
\]

## 2. `P(5,3)=2`

A colour class meeting every triple has complement triangle-free. By Mantel's theorem a triangle-free graph on five vertices has at most six edges, so the colour class has at least

\[
10-6=4
\]

edges. Hence

\[
P(5,3)\le\lfloor10/4\rfloor=2.
\]

For equality, colour the edges of a 5-cycle red and its complement blue. Both colour classes are 5-cycles and therefore triangle-free. Consequently no 3-set is monochromatic, so every 3-set contains both colours. Thus

\[
\boxed{P(5,3)=2}.
\]

This is the small finite **collapse** visible in the recovered campaign: the value drops from 3 at `n=4` to 2 at `n=5`.

## 3. `P(6,4)=5`

A colour class meeting every 4-subset has a `K_4`-free complement. Turán's theorem gives

\[
\operatorname{ex}(6,K_4)=12,
\]

attained by the complete 3-partite graph `K_{2,2,2}`. Therefore every colour class has at least

\[
15-12=3
\]

edges, and

\[
P(6,4)\le\lfloor15/3\rfloor=5.
\]

A 1-factorization of `K_6` partitions its 15 edges into five perfect matchings, each of size three. Every 4-subset of the six vertices contains an edge from every perfect matching: selecting four vertices from three matched pairs forces at least one complete pair by pigeonhole.

Hence every 4-set sees all five colours, proving

\[
\boxed{P(6,4)=5}.
\]

## Scope / provenance

These three values were recovered from a finite analogue constructed inside the Erdős #598 campaign. The original #598 problem is infinitary and involves cardinal-colouring quantifiers. The campaign itself correctly warns that **no finite-to-infinite transfer theorem is supplied**.

Accordingly this file records only the finite combinatorics above. It makes no claim that these values prove, disprove, approximate, or scale to the parent infinitary problem.
