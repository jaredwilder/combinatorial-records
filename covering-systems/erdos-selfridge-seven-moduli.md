# Erdős–Selfridge odd covering systems — exact seven-modulus obstruction

**Author:** Jared Wilder  
**Public routing:** 2026-09-11

The global Erdős–Selfridge / Guy B21 problem asks whether the integers admit a covering system with pairwise distinct odd moduli greater than one. **This note does not solve that problem.**

## Exact finite result

For the fixed modulus family

`{3,5,7,9,11,13,15}`,

there is no choice of one residue class modulo each modulus whose union covers every integer.

Equivalently, reducing modulo

`lcm(3,5,7,9,11,13,15)=45045`,

no choice

`a_3 mod 3, a_5 mod 5, ..., a_15 mod 15`

covers all 45,045 residue classes.

The family is not eliminated by the elementary density condition because

`1/3+1/5+1/7+1/9+1/11+1/13+1/15 > 1`.

## Evidence boundary

The recovered campaign state records two complete finite solvers for this fixed family:

- CP-SAT;
- PySAT.

The original standalone solver/certificate files have not yet been recovered into the current public GitHub surface. This note therefore preserves the exact finite result and its provenance without fabricating missing certificate bytes.

## Scope

This eliminates one concrete dense seven-modulus construction family only. It does not imply that every finite odd distinct-modulus family is impossible and does not settle the global odd-covering-system problem.

Original extraction: `jaredwilder/unpublished-math-papers/erdos-selfridge-odd-covering/`.