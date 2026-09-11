# Rigidity of optimal balanced-box scalarization

**Author:** Jared Wilder  
**Public proof release:** 2026-09-11

Let `A>=1`, let

```text
q = 2A+1,
```

and let `w=(w_1,...,w_m)` be integer weights such that

```text
x -> w . x
```

is injective on the balanced integer cube

```text
[-A,A]^m ∩ Z^m.
```

## Sharp lower bound

There are `q^m` input vectors. Every output lies in

```text
[-A ||w||_1, A ||w||_1],
```

an integer interval containing at most

```text
2A ||w||_1 + 1
```

integers. Therefore injectivity forces

```text
2A ||w||_1 + 1 >= q^m,
```

or equivalently

```text
||w||_1 >= (q^m-1)/(q-1)
          = 1+q+...+q^(m-1).
```

Balanced positional weights

```text
1,q,q^2,...,q^(m-1)
```

attain equality.

## Rigidity theorem

If equality holds in the lower bound, then, up to coordinate permutation and independent sign changes,

```text
w = (1,q,q^2,...,q^(m-1)).
```

Thus the balanced positional system is not merely optimal: it is the unique optimizer modulo the obvious cube symmetries.

## Proof

Independent sign changes of the coordinates preserve the cube, so replace each weight by its absolute value. Equality gives

```text
2A ||w||_1 + 1 = q^m.
```

The `q^m` distinct outputs therefore fill every integer in the entire interval

```text
[-A||w||_1, A||w||_1].
```

Shift every digit `x_i∈[-A,A]` to `d_i=x_i+A∈{0,1,...,q-1}`. Unique representation of the full interval becomes the generating-polynomial identity

```text
Π_i (1 + z^(w_i) + z^(2w_i) + ... + z^((q-1)w_i))
    = 1 + z + z^2 + ... + z^(q^m-1).            (1)
```

All coefficients are nonnegative integers.

### Step 1: one weight is exactly 1

The coefficient of `z` on the right of (1) is 1. On the left, a term `z` can occur only by choosing `z^(w_i)` from a factor with `w_i=1` and constants from all other factors. Hence exactly one weight equals 1.

After permuting coordinates, let `w_1=1`. Divide (1) by

```text
1+z+...+z^(q-1).
```

We obtain

```text
Π_{i=2}^m (1 + z^(w_i) + ... + z^((q-1)w_i))
    = 1 + z^q + z^(2q) + ... + z^((q^(m-1)-1)q).   (2)
```

### Step 2: every remaining weight is divisible by q

The right side of (2) has zero coefficient at every exponent not divisible by `q`. The left side has nonnegative coefficients. If some remaining `w_i` were not divisible by `q`, the monomial `z^(w_i)` obtained from that factor and constants from all others would give a positive coefficient at a forbidden exponent. Therefore

```text
q | w_i   for every i>=2.
```

Write `w_i=q v_i` and substitute `y=z^q` into (2). Then

```text
Π_{i=2}^m (1 + y^(v_i) + ... + y^((q-1)v_i))
    = 1 + y + ... + y^(q^(m-1)-1).
```

This is exactly the same problem with `m-1` weights.

Induction yields

```text
{v_2,...,v_m} = {1,q,...,q^(m-2)},
```

so

```text
{w_1,...,w_m} = {1,q,...,q^(m-1)}.
```

Restoring the independent signs proves the theorem.

## Scope

This theorem concerns integer linear scalarizations of the *entire* balanced cube. Sparse-domain encodings can have very different optimal scales because the input cardinality and collision geometry change.

Historical novelty is not claimed; this page supplies a complete standalone proof for the theorem recovered in the estate.
