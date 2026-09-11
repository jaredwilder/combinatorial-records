# Linear channel redundancy bounds — exact scope

**Author:** Jared Wilder  
**Public correction:** 2026-09-11

Let a linear code over a field `F` encode `k` data symbols into `n=k+r` transmitted symbols, where `r` is the redundancy and `d` is the minimum distance.

## Lower bounds

The Singleton bound gives

```text
d <= r+1.
```

Therefore:

- correcting `t` arbitrary unknown symbol errors requires `d>=2t+1`, hence

```text
r >= 2t;
```

- detecting every pattern of at most `t` symbol errors requires `d>=t+1`, hence

```text
r >= t;
```

- correcting `t` known erasures also requires `d>=t+1`, hence

```text
r >= t.
```

These lower bounds are field-independent.

## Attainment boundary

Equality in Singleton means the code is MDS. Thus the bounds are attained exactly when an MDS code with the required parameters exists.

Over sufficiently large fields, Reed-Solomon or generalized Reed-Solomon constructions supply the standard sharp examples for supported lengths. Over a fixed small field, however, an MDS code of the desired length and dimension need not exist.

Accordingly, the correct statement is:

> `2t` redundancy is the universal linear lower bound for correcting `t` arbitrary errors, and `t` is the universal linear lower bound for detecting `t` errors or correcting `t` erasures. These bounds are attained for parameter ranges admitting suitable MDS codes; they are not unconditionally attained over every field and length.

## Correction boundary

The earlier abstract theorem-bank wording said that “MDS codes attain these bounds” without a field/length qualifier. The lower bounds were correct; only the unconditional attainability wording was too broad.

Historical novelty is not claimed; these are classical coding-theoretic bounds recorded with exact scope.
