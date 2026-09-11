# Exact linear measurement lower bound for sparse recovery

**Author:** Jared Wilder  
**Public correction:** 2026-09-11

## Theorem

Let `F` be a field and let

```text
A : F^m -> F^r
```

be linear. Suppose `A` uniquely determines every vector of support at most `s`.
Then

```text
r >= min(m, 2s).
```

This is the exact dimension-sensitive lower bound. The shorter statement `r>=2s` requires the ambient regime `m>=2s`.

## Proof

Unique recovery of all `s`-sparse vectors is equivalent to saying that the kernel of `A` contains no nonzero difference of two `s`-sparse vectors.

Every vector whose support has size at most `min(m,2s)` is such a difference: split its support into two pieces of size at most `s` and put one piece in the first sparse vector and the negative of the other piece in the second.

### Case 1: `m <= 2s`

Then every vector in `F^m` is a difference of two `s`-sparse vectors. Hence `ker(A)={0}` and `A` is injective on all of `F^m`. Therefore

```text
r >= m.
```

### Case 2: `m > 2s`

If `r<2s`, then among any `r+1` columns of a matrix for `A` there is a linear dependence. Since

```text
r+1 <= 2s,
```

this produces a nonzero kernel vector supported on at most `2s` coordinates. Such a vector is a difference of two `s`-sparse vectors, contradicting unique recovery.

Thus

```text
r >= 2s.
```

Combining the two cases gives

```text
r >= min(m,2s).
```

## Sharpness

- If `m<=2s`, `m` measurements are sufficient: take any invertible `m x m` linear map.
- If `m>2s`, `2s` measurements are sufficient whenever the field admits a `2s x m` matrix whose every `2s` columns are independent; over sufficiently large fields a Vandermonde/Reed-Solomon construction supplies one.

Thus the lower bound is sharp in the usual sufficiently-large-field regime.

## Correction boundary

The earlier abstract theorem-bank wording said simply:

```text
At least 2s linear field measurements are necessary to recover every s-sparse vector.
```

That sentence is false when `m<2s`. For example, when `m=s=1`, one measurement recovers every vector although `2s=2`.

The corrected universal statement is `r>=min(m,2s)`.

Historical novelty is not claimed; this is standard spark/dimension linear algebra recorded with exact scope.
