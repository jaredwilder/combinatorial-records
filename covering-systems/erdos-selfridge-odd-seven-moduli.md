# Erdős–Selfridge odd covering — exact seven-modulus obstruction

**Author:** Jared Wilder  
**Source campaign:** 2026-07-24  
**Public routing:** 2026-09-11

For the fixed odd, pairwise-distinct moduli

`{3,5,7,9,11,13,15}`,

there is **no choice of one residue class modulo each modulus** whose union covers every integer.

Equivalently, after reducing modulo

`lcm(3,5,7,9,11,13,15)=45045`,

no selection of seven residue classes covers all 45,045 residues.

## Why this finite obstruction is nontrivial

The elementary density necessary condition does not eliminate this family:

`1/3+1/5+1/7+1/9+1/11+1/13+1/15 ≈ 1.0218004218 > 1`.

The obstruction therefore comes from the exact residue-incidence structure, not merely from total density.

## Verification record

The recovered estate state records independent complete certification by two solver formulations:

- CP-SAT;
- PySAT.

The original standalone solver/certificate files were not recovered during the public-repo sweep, so this note does not fabricate them. Recovery of those exact bytes remains a provenance obligation.

## Scope

This is a fixed-family finite impossibility result. It does not imply that every odd distinct-modulus family fails, and it does not settle the global Erdős–Selfridge covering-system problem.

The classical necessary condition `sum 1/n_i >= 1` is background, not a novelty claim.
