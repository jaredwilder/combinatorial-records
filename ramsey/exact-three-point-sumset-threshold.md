# Exact two-colour threshold for a three-point sumset pattern

**Author:** Jared Wilder  
**Public promotion:** 2026-09-11

For a 2-colouring `c` of the integer interval `[2,2N]`, ask whether there must exist integers

`1 <= a < b <= N`

such that the three values

\[
\{2a,\ a+b,\ 2b\}
\]

all receive the same colour.

## Exact theorem

The least such `N` is

\[
\boxed{7}.
\]

Equivalently:

- every 2-colouring of `[2,14]` contains a monochromatic set `{2a,a+b,2b}` with `1<=a<b<=7`;
- there exists a 2-colouring of `[2,12]` avoiding every such set with `1<=a<b<=6`.

An avoiding colouring at `N=6` is

```text
c(2)=1  c(3)=0  c(4)=1  c(5)=0  c(6)=0  c(7)=0
c(8)=1  c(9)=1  c(10)=0 c(11)=1 c(12)=0
```

## Relation to the easy van der Waerden bound

Define `d(n)=c(2n)`. A monochromatic 3-term arithmetic progression

`a < m < b`, with `a+b=2m`,

in `d` produces the monochromatic triple

`{2a,2m,2b}={2a,a+b,2b}`

in `c`. Thus `W(2,3)=9` immediately yields the non-sharp upper bound `N<=9`.

The exact exhaustive search improves this to `N=7`, and the explicit colouring above proves sharpness.

## Evidence

The committed verifier `verify_exact_three_point_sumset_threshold.py` exhausts every 2-colouring at `N=6` and `N=7`, checks the displayed avoiding colouring, and confirms that 7 is the first forced value in the searched range.

This is an exact finite Ramsey-type result. No asymptotic statement is attached to it.
