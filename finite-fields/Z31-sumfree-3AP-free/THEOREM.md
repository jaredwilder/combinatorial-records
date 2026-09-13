# Sum-free and nontrivial-3-AP-free subsets of `Z/31Z`

**Author:** Jared Wilder  
**Source:** MathFire Round Seven  
**Status:** complete finite computational classification

Let

\[
A\subseteq \mathbb Z/31\mathbb Z.
\]

Assume:

1. `A` is sum-free in the strong declared sense
   \[
   (A+A)\cap A=\varnothing,
   \]
   with repeated summands allowed;
2. `A` contains no nontrivial three-term arithmetic progression.

## Theorem

\[
\boxed{|A|\le6.}
\]

The bound is sharp.

There are exactly **330** valid six-element subsets and **0** valid seven-element subsets.

A witness is

```text
{1,3,7,15,20,24}
```

## Complete orbit classification under multiplication by units

The 330 extremizers split into exactly **12** orbits under the unit group of `Z/31Z`:

- 10 orbits of size 30;
- 2 orbits of size 15.

Representatives:

```text
{1,3,7,15,20,24}
{1,3,7,15,20,28}
{1,3,7,18,22,24}
{1,3,10,12,26,28}
{1,3,11,13,18,27}
{1,3,11,13,18,28}
{1,3,11,15,20,24}
{1,3,11,15,20,28}
{1,3,11,18,20,28}
{1,4,11,20,25,27}
{1,4,11,20,27,30}
{1,5,14,17,26,30}
```

The last two have stabilizer `{1,30}` and orbit size `15`; the first ten have trivial stabilizer and orbit size `30`.

## Exhaustive proof

The frozen campaign exhaustively checked

\[
\binom{31}{6}=736281
\]

six-subsets and

\[
\binom{31}{7}=2629575
\]

seven-subsets.

The primary exact implementation and two independent replays agreed on:

- maximum `6`;
- valid six-subset count `330`;
- valid seven-subset count `0`;
- orbit count `12`;
- orbit-size multiset `15,15,30,…,30`.

The independent C implementation recorded source SHA-256

`b38600e6225f79838a815bcc2fc5ffa6dcf7e86f8fbec473b3ecc4f4b8370449`.

The sorted valid-six-subset layer has SHA-256

`8fdf96cadc52fee0a0b6f8543a15d993489bf00ac12a2ac312cff93cccef2605`.

The theorem certificate hash is

`376d8ba43f2612561bcb7cd9b918f9889867f9472f53739ee7354737b671f309`.

## Claim boundary

This is an exact theorem for the single cyclic group `Z/31Z`. It is not an asymptotic theorem for general cyclic groups or prime moduli.

## Focused home and recovered verifiers

The [finite-field extremal-set repository](https://github.com/jaredwilder/finite-field-extremal-sets)
now provides the coherent three-case reading map, exact original verifier
sources, full maximizing layers, provenance hashes and fresh Python/C/C++
verification. This note remains the historical source record.
