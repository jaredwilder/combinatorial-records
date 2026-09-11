# Powers of two — exact subset-sum interval and local saturation

**Author:** Jared Wilder  
**Recovered from:** distinct-subset-sums A/B transcript run  
**Public extraction:** 2026-09-11

For `d>=1`, let

\[
P_d=\{1,2,4,\ldots,2^{d-1}\}.
\]

## Theorem 1 — exact subset-sum interval

The subset sums of `P_d` are exactly

\[
\boxed{\{0,1,2,\ldots,2^d-1\}.}
\]

Moreover every integer in that interval has a **unique** representation as a subset sum of `P_d`.

### Proof

This is binary expansion. Every integer `0<=m<2^d` has a unique digit expansion

\[
m=\sum_{i=0}^{d-1}\varepsilon_i2^i,
\qquad \varepsilon_i\in\{0,1\}.
\]

The chosen indices are exactly the corresponding subset of `P_d`.

## Theorem 2 — exact local saturation

No positive integer

\[
x\le2^d-1,
\qquad x\notin P_d,
\]

can be adjoined to `P_d` while preserving distinct subset sums.

Indeed the singleton subset `{x}` in the enlarged set has sum `x`, while Theorem 1 gives a different subset of `P_d` with the same sum.

Thus `P_d` is locally saturated against every new positive element below its total sum.

## Recovered finite object

The historical transcript used

\[
P_{13}=\{1,2,4,\ldots,4096\}.
\]

Its subset sums are exactly

\[
\boxed{\{0,1,\ldots,8191\}},
\]

so no positive `x<=8191` outside `P_{13}` can be added without creating a subset-sum collision.

## Novelty boundary

The theorem is elementary binary numeration, not a novelty claim. It is published because the finite campaign object carried a stronger general theorem that should not remain buried as an isolated witness.
