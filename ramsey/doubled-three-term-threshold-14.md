# Exact two-colour threshold for `{2a, a+b, 2b}`

**Author:** Jared Wilder  
**Status:** exact finite Ramsey-type theorem  
**Historical novelty:** not claimed

There are two equivalent parameter conventions in the historical estate. This note records both so the values **14** and **7** are not mistaken for conflicting results.

## Convention A — endpoint of the coloured interval

Colour the integers `[1,M]` with two colours. Ask for the least `M` such that every colouring contains integers `1 <= a < b` with

\[
2b\le M
\]

and

\[
\{2a,\;a+b,\;2b\}
\]

monochromatic.

The exact threshold is

\[
\boxed{M=14}.
\]

### Lower bound: 13 is avoidable

There are exactly **16** two-colourings of `[1,13]` avoiding every monochromatic triple of the required form.

One witness, written as colours of `1,2,...,13`, is

```text
0101000110100
```

so `M=13` does not force the configuration.

### Upper bound: 14 forces it

There are `2^14 = 16384` two-colourings of `[1,14]`. Exhaustive enumeration finds **zero** avoiding colourings.

Hence every two-colouring of `[1,14]` contains `a<b` with `2b<=14` such that `2a`, `a+b` and `2b` all receive the same colour.

## Convention B — endpoint for `a,b`

A different campaign writes `N` for the largest allowed value of `b` and colours the sum window `[2,2N]`. Its question is:

> what is the least `N` such that every two-colouring of `[2,2N]` contains `1<=a<b<=N` with `{2a,a+b,2b}` monochromatic?

Under this convention the exact threshold is

\[
\boxed{N=7}.
\]

This is the same theorem as `M=14`, with `M=2N`.

A direct replay gives:

- `N=6`: exactly **4** avoiding colourings of `[2,12]`;
- one witness is

```text
c(2..12) = 1,0,1,0,0,0,1,1,0,1,0;
```

- `N=7`: **0** avoiding colourings of `[2,14]`.

The historical `N=33` bound came from an unnecessarily indirect van-der-Waerden route. Even the immediate `W(2,3)=9` argument improves it to `N=9`; exhaustive search gives the exact `N=7`.

## Relation to three-term progressions

The triple `(2a,a+b,2b)` is itself a three-term arithmetic progression, since

\[
2(a+b)=2a+2b.
\]

The special feature is that its endpoints are constrained to be even and arise as `2a,2b`.

A historical route also tried to invoke Hindman/Galvin–Glazer machinery. That does not by itself settle the relevant `A+A` statement: finite-sums theorems supply sums of **distinct** selected elements, whereas `A+A` includes the diagonal values `2a`. The diagonal is a genuine logical distinction and should not be silently erased.

## Verification

The companion script `verify_doubled_three_term_threshold_14.py` enumerates all two-colourings for the coloured-interval convention and checks:

- `M=13`: exactly 16 avoiding colourings;
- the displayed witness is one of them;
- `M=14`: zero avoiding colourings.

The `N=6,7` formulation was independently recomputed from the same definition before this clarification was added.

## Provenance

Recovered from two different buried sources: the raw-session transcript audit and the worked counterexample queue. Their numbers initially looked different because they used different endpoint parameters. The live publication now reconciles them explicitly.
