# Exact Schur–Roth classification in `Z/31Z`

**Author:** Jared Wilder  
**Public mathematical routing:** 2026-09-14  
**Authority:** exact finite computer-assisted theorem

## Theorem

Let `A` be a subset of the cyclic group

\[
\mathbb Z/31\mathbb Z.
\]

Assume simultaneously:

1. `A` is **sum-free in the standard group sense**,
   \[
   (A+A)\cap A=\varnothing,
   \]
   with repeated summands allowed;
2. `A` contains no **nontrivial three-term arithmetic progression**: there are no three distinct `x,y,z in A` with
   \[
   x+z=2y\pmod{31}.
   \]

Then

\[
\boxed{|A|\le6.}
\]

The bound is sharp. More precisely:

\[
\boxed{
\begin{aligned}
\#\{A:|A|=6,\ A\text{ valid}\}&=330,\\
\#\{A:|A|=7,\ A\text{ valid}\}&=0.
\end{aligned}}
\]

Under multiplication by the 30 units of `Z/31Z`, the 330 extremal six-sets form exactly

\[
\boxed{12\text{ orbits}},
\]

namely two orbits of size 15 and ten orbits of size 30.

One extremal set is

```text
{1, 3, 7, 15, 20, 24}.
```

## Exact finite proof

The forbidden property is hereditary: every subset of a valid set is valid. Therefore it is enough to establish:

- at least one valid six-set exists;
- every seven-set is invalid.

The release exhaustively checks every set in both critical layers:

\[
\binom{31}{6}=736,281,
\qquad
\binom{31}{7}=2,629,575.
\]

The exact search returns:

```text
valid 6-sets: 330
valid 7-sets: 0
```

so the maximum is exactly 6.

The unit action on the 330 extremizers is then enumerated exactly, yielding 12 orbits: two of size 15 and ten of size 30.

## Independent verification

This result was not certified by a single implementation path.

The source release records:

- exhaustive coverage of all 736,281 six-subsets;
- exhaustive coverage of all 2,629,575 seven-subsets;
- two independent Python decision paths with different reconstruction/loop structure;
- a separately compiled independent C verifier reproducing the extremal counts and orbit classification;
- a stable digest for the sorted list of all 330 extremizers.

That extremizer-list digest is

```text
SHA-256
8fdf96cadc52fee0a0b6f8543a15d993489bf00ac12a2ac312cff93cccef2605
```

The original MathFire 7 release also preserves the orbit representatives, stabilizers, proof receipt, and independent-verifier receipts.

## Novelty boundary

A separate systematic novelty search covered exact and broadened terminology, general web indexes, arXiv-focused searches, OEIS, and nearby literature on sum-free sets, progression-free sets, complete/saturating 3-AP-free sets, `W`-avoidance, and related multiple-linear-equation problems.

No searched source stated this exact combination of:

- maximum 6 in `Z/31Z`;
- exactly 330 extremal six-sets;
- zero seven-sets;
- exactly 12 unit-dilation orbits.

The defensible wording is therefore:

> **To the best of our knowledge after systematic search, this exact finite theorem and classification are new.**

That novelty statement is not part of the mathematical certificate and does not exclude unpublished or unindexed prior work.

## Why this file exists

The theorem was originally embedded in a deterministic mathematics-engine release. That is provenance, not an appropriate human mathematical front door. This file promotes the finite theorem itself independently of the surrounding MathFire benchmark/tooling claims.
