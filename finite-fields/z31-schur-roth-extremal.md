# Exact Schur–Roth extremum in `Z/31Z`

**Status:** exact finite computational theorem.  
**Provenance:** recovered from the MathFire 7 release where it was stored as an engine/benchmark result rather than a standalone theorem record.  
**Novelty:** source campaign wording is **apparently new / to the best of our knowledge after systematic search**. No historical priority is claimed here until a dedicated literature court is completed.

## Theorem

Let `A subset Z/31Z`. Require simultaneously:

1. **sum-free:** there are no `x,y,z in A` with `x+y=z` in `Z/31Z` under the release's declared Schur constraint semantics; and
2. **nontrivial 3-AP-free:** there are no distinct-endpoint arithmetic progressions
   \[
   x,z\in A,\quad x\ne z,\quad 2y=x+z,\quad y\in A.
   \]

Then:

\[
\boxed{|A|\le6.}
\]

Moreover:

- there are exactly **330** valid six-element sets;
- there are **no** valid seven-element sets;
- the 330 extremizers fall into exactly **12** orbits under multiplication by units of `Z/31Z`.

## Exhaustive authority

The MathFire 7 source release records exhaustive coverage of

\[
\binom{31}{6}=736281
\]

six-element subsets and

\[
\binom{31}{7}=2629575
\]

seven-element subsets.

The release did not rely on a single implementation path. It records:

- two independent Python decision paths;
- an independent C verifier;
- a stable digest over all 330 extremizers;
- exact verification of the 12 unit-dilation orbits;
- corruption/refusal tests separating mathematical proof status from novelty status and mission routing.

Because the forbidden properties are hereditary, exhaustive nonexistence of a valid seven-set proves that no larger valid set exists either.

## Scope

This theorem is **only for the cyclic group `Z/31Z`** and the exact two forbidden configurations above. It is not a general theorem for arbitrary primes or arbitrary finite abelian groups.

## Why this is here

The theorem was buried inside an engine release. The mathematical content does not become less real because the exhaustive search was originally used as a benchmark for a deterministic discovery system.

This file gives the finite result a stable subject-facing identity independent of MathFire's software architecture.

## Source artifacts named by the release

The recovered integration handoff identifies the original authority artifacts as:

- `docs/NOVEL_RESULT.md`;
- `receipts/round7-novel-result-proof.json`;
- `verification/schur_roth_z31_independent.c`;
- `receipts/schur-roth-z31-c-verifier.txt`;
- `receipts/novelty-clearance.json`.

Those exact bytes should be mirrored beside this theorem record when recovered from the source release. Until then, this page records the theorem and the source's explicit exhaustive-accounting boundary; it does not substitute a new verifier for the original independent C receipt.
