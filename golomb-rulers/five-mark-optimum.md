# Five-mark Golomb rulers: optimum length 11

**Author:** Jared Wilder  
**Release status:** exact finite classification, independently re-enumerated on promotion

A Golomb ruler is a strictly increasing set of integer marks whose positive pairwise differences are all distinct. After translation and reflection normalization, the five-mark optimum has length

\[
\boxed{11}.
\]

There are exactly four normalized optimal rulers:

```text
(0,1,4,9,11)
(0,2,7,8,11)
(0,2,7,10,11)
(0,3,4,9,11)
```

Each has ten distinct positive differences.

## Exact finite classification

An exhaustive enumeration was rerun during promotion:

- every choice of five marks with endpoints `0,L` was tested for every `4 <= L <= 10`;
- **zero** Golomb rulers exist at those lengths;
- all choices with endpoints `0,11` were then tested;
- exactly the four rulers above survive.

Therefore both the optimum and the complete normalized optimum census are finite exhaustive results, not heuristic-search outputs.

## Difference multisets

For `(0,1,4,9,11)` and `(0,2,7,10,11)`, the positive differences are

```text
{1,2,3,4,5,7,8,9,10,11}.
```

For `(0,2,7,8,11)` and `(0,3,4,9,11)`, they are

```text
{1,2,3,4,5,6,7,8,9,11}.
```

## Scope

This is a small exact finite classification. No historical novelty claim is made here; the purpose of this record is to move a repeatedly recovered exact result out of mixed archive summaries into a stable mathematical home with a reproducible verifier.
