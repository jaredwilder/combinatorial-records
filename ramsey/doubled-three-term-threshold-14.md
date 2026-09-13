# Exact two-colour threshold for `{2a, a+b, 2b}`

**Author:** Jared Wilder  
**Status:** exact finite Ramsey-type theorem  
**Historical novelty:** not claimed

Colour the integers `[1,N]` with two colours. We ask for the least `N` such that every colouring contains integers `1 <= a < b` for which

\[
\{2a,\;a+b,\;2b\}
\]

is monochromatic.

The exact threshold is

\[
\boxed{N=14}.
\]

## Lower bound: 13 is avoidable

There are exactly **16** two-colourings of `[1,13]` avoiding every monochromatic triple of the required form.

One witness, written as colours of `1,2,...,13`, is

```text
0101000110100
```

so `N=13` does not force the configuration.

## Upper bound: 14 forces it

There are `2^14 = 16384` two-colourings of `[1,14]`. Exhaustive enumeration finds **zero** avoiding colourings.

Hence every two-colouring of `[1,14]` contains `a<b` with `2b<=14` such that `2a`, `a+b` and `2b` all receive the same colour.

## Relation to three-term progressions

The triple is the doubled image of the arithmetic progression

\[
a,\frac{a+b}{2},b
\]

when `a+b` is even, and more generally has the fixed affine form `(2a,a+b,2b)`.

A van-der-Waerden route gives a non-sharp bound, but the exact threshold 14 is a separate finite computation.

A historical route also tried to invoke Hindman/Galvin–Glazer machinery. That does not by itself settle the relevant `A+A` statement: finite-sums theorems supply sums of **distinct** selected elements, whereas `A+A` includes the diagonal values `2a`. The diagonal is a genuine logical distinction and should not be silently erased.

## Verification

The companion script `verify_doubled_three_term_threshold_14.py` enumerates all two-colourings for `N=13,14` directly from the definition.

It checks:

- `N=13`: exactly 16 avoiding colourings;
- the displayed witness is one of them;
- `N=14`: zero avoiding colourings.

## Provenance

Recovered from a raw-session transcript audit and independently recomputed before this publication.
