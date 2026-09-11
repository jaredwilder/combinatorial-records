# Sum-free and product-free subsets of `F_31^×`

**Author:** Jared Wilder  
**Source:** MathFire 10.0.0 actual-final release  
**Status:** complete finite computational classification  
**Novelty posture:** `apparently_new_after_systematic_search` as of 2026-07-27; absolute historical novelty is not claimed.

Let `A` be a subset of the nonzero elements of the prime field `F_31`. Require:

1. **sum-free:** no `x,y,z∈A`, repetitions allowed, satisfy `x+y=z` in `F_31`;
2. **product-free:** no `x,y,z∈A`, repetitions allowed, satisfy `xy=z` in `F_31`.

## Theorem

\[
\boxed{|A|\le 8.}
\]

The bound is sharp. Exactly **9** subsets attain size `8`:

```text
{2,3,7,15,16,24,28,29}
{2,3,10,15,16,21,28,29}
{2,3,12,13,18,19,28,29}
{2,5,9,15,16,22,26,29}
{2,5,11,14,17,20,26,29}
{2,6,7,15,16,24,25,29}
{2,6,11,15,16,20,25,29}
{2,9,10,15,16,21,22,29}
{10,12,13,15,16,18,19,21}
```

There are no valid size-9 subsets.

The ordered extremizer digest is

`9e8335483eecaf3e5e7dcb747053613dabf848c24734126330551d5327901d17`.

## Exact authority

The actual-final MathFire 10.0.0 release used an independent C verifier:

`verification/mixed_sum_product_f31_independent.c`

with recorded source SHA-256

`071114edde1b5928e0813f40978a5439baef062bdb21c1ffb289a093ffe71c1e`.

The independent verifier returned:

- `prime=31`;
- `maximum=8`;
- `extremal_count=9`;
- `next_layer_count=0` / `valid_size_9_count=0`;
- `search_nodes=8421`.

The recorded independent output SHA-256 is

`bb97041645e1a5d3392cb6b1594694587b3a1281a561465d7a96777585f39a25`.

The actual-final ZIP verification also reports all MathFire 10 gates green, including `4403/4403` tests and `1179/1179` named hostile attacks. Those release-engine counts are provenance, not part of the theorem statement.

## Version/provenance note

An earlier Round-Ten development packet in the estate contains a **different** finite-field theorem over `F_73^×` with a third nontrivial-3-AP avoidance condition. That theorem is preserved separately as an earlier campaign result. It must not be confused with this **actual-final MathFire 10.0.0 headline result**, which is the two-condition `F_31^×` classification above.

## Claim boundary

This is a finite theorem for `F_31^×`. It is not an asymptotic theorem for arbitrary prime fields.
