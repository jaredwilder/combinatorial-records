# Maximum 3-uniform sunflower-free families for `u <= 9`

**Author:** Jared Wilder  
**Recovered from:** divergent-mirror mathematics audit  
**Status:** exact finite table as reported by the exhaustive source; larger displayed witnesses independently rechecked during promotion

Consider a family `F` of 3-subsets of a `u`-element ground set. A forbidden sunflower is a triple of distinct members whose three pairwise intersections are all equal.

The recovered exhaustive table is:

| `u` | number of triples | forbidden sunflower triples | maximum `|F|` |
|---:|---:|---:|---:|
| 3 | 1 | 0 | **1** |
| 4 | 4 | 0 | **4** |
| 5 | 10 | 10 | **6** |
| 6 | 20 | 60 | **10** |
| 7 | 35 | 315 | **12** |
| 8 | 56 | — | **12** |
| 9 | 84 | — | **14** |

The original adapter was hard-capped at `u <= 6`; the `u=7,8,9` values came from a separate exhaustive run recorded in the mirror audit.

## Rechecked witnesses

For `u=8`, a 12-set optimum is

```text
136 137 145 147 156 235 237 245 246 267 356 467
```

It actually uses only the seven points `{1,...,7}`. Hence the eighth point buys nothing and the optimum plateaus from `u=7` to `u=8`.

For `u=9`, a 14-set witness is

```text
057 058 067 068 127 128 134 138 147 234 238 247 567 568
```

During promotion both displayed families were independently checked directly from the definition: among every triple of chosen 3-sets, the three pairwise intersections are never all equal.

The source also displays a size-10 `u=6` witness:

```text
014 015 023 025 034 123 124 135 245 345
```

## Structural observation

The sequence of exact maxima is

```text
1, 4, 6, 10, 12, 12, 14
```

for `u=3,...,9`. In particular, the eighth point produces no gain while the ninth permits two additional triples.

This is a finite extremal record only. The value is still increasing at `u=9`, so nothing here is presented as an asymptotic or global sunflower theorem.

## Authority boundary

- The zero-sunflower property of the displayed `u=8` and `u=9` witnesses was rechecked independently during promotion.
- The optimality assertions for `u=7,8,9` are preserved as exact results reported by the source's exhaustive run; the original exhaustive solver transcript/certificate bytes should be retained or recovered separately if available.
- No literature novelty claim is made by this record.
