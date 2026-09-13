# Exact finite-CSP compilation and minimal-no-good convergence

**Author:** Jared Wilder  
**Status:** elementary finite combinatorics / exact algorithmic theorems  
**Historical novelty:** not claimed

These theorems were recovered from mixed research-system sources. Only the separable abstract mathematics is published here.

## 1. Finite CSP compilation theorem

Let a finite-domain CSP have variables

\[
X_1,\ldots,X_n
\]

with finite domains `D_i`, together with any finite family of forbidden partial assignments.

Create one selectable action `(i,a)` for every `a in D_i`.

Impose:

1. a positive coverage obligation saying that at least one `(i,a)` is selected for each variable `i`;
2. pair exclusions forbidding simultaneous selection of `(i,a)` and `(i,b)` for distinct `a,b in D_i`;
3. for every forbidden partial assignment, one hyperedge forbidding simultaneous selection of exactly its variable-value actions.

Then feasible selections are in bijection with satisfying assignments of the original CSP.

### Proof

A feasible selection contains at least one action for each variable by the coverage obligation and at most one by the pair exclusions. Hence it contains exactly one `(i,a_i)` for every `i`, so it determines a unique total assignment.

The hyperedge constraints say precisely that this assignment contains no forbidden partial assignment, hence it satisfies the CSP.

Conversely, a satisfying assignment selects its unique `(i,a_i)` for every variable. It meets every coverage obligation, violates no same-variable pair exclusion, and contains no forbidden-assignment hyperedge. Thus it is feasible.

The two maps are inverse. ∎

## 2. Minimal-no-good representation

For a finite CSP, call a partial assignment a **no-good** if it cannot be extended to a satisfying assignment. Call it **minimal** if every proper subassignment can be extended.

Because the variable/domain universe is finite, the family `M` of minimal no-goods is finite.

A total assignment is satisfying **if and only if** it contains no member of `M`.

### Proof

A satisfying assignment contains no no-good at all. Conversely, if a total assignment is unsatisfying, then the assignment itself is a no-good. Repeatedly delete assigned variable-values while the remainder remains a no-good. Finiteness terminates at an inclusion-minimal no-good contained in the assignment. ∎

## 3. Exact solve–Court–mine convergence theorem

Assume:

- the CSP is finite;
- a proposal solver returns a total assignment avoiding every currently learned no-good, or reports that none exists;
- an exact Court accepts exactly the satisfying assignments;
- whenever the Court rejects a proposal, a complete miner returns a minimal no-good contained in that proposal.

Then the loop

`solve -> Court -> mine -> add no-good -> solve -> ...`

terminates after at most

\[
\boxed{|M|}
\]

rejected proposals, where `M` is the set of all minimal no-goods.

At termination it returns either a satisfying assignment or an exact infeasibility result.

### Proof

Suppose a proposal is rejected. The miner returns a minimal no-good `H` contained in it. `H` cannot already be learned: the proposal solver was required to avoid every learned no-good, while the proposal contains `H`. Thus each rejection adds a previously unseen member of the finite set `M`.

Therefore there can be at most `|M|` rejected proposals.

If the Court accepts, the returned assignment is satisfying by exactness.

Otherwise, after enough rejections, the proposal solver may report that no total assignment avoids the learned no-goods. Since every learned no-good is genuinely nonextendable, no satisfying assignment has been excluded incorrectly. Hence infeasibility is exact. ∎

## 4. No-repeated-minimal-failure corollary

Under the hypotheses above, once a minimal no-good has been learned, no later proposal can contain it.

This is immediate from the proposal solver's avoidance rule.

## 5. Strict progress trichotomy

Every iteration of the exact finite loop ends in exactly one of three productive states:

1. a satisfying assignment is accepted;
2. the learned constraints make the proposal problem infeasible;
3. a new minimal no-good is added.

Hence an iteration cannot return forever to the same finite knowledge state.

## 6. Isolation lower bound for coverage extensions

In any finite coverage system, if an obligation has no admissible incident action, then no feasible solution exists using the current action set.

Any extension that makes the instance feasible must therefore either:

- add at least one admissible action incident to that obligation; or
- change/remove the obligation or admissibility constraints.

This is a direct incidence obstruction, but it is useful as an exact lower bound on what any repair must change.

## 7. Proof-carrying edge suppression

Let a directed or undirected graph be compressed by replacing selected original paths with synthetic edges, and store with every synthetic edge an original path having the same endpoints.

Then every walk in the compressed graph lifts to a walk in the original graph by replacing each synthetic edge by its stored path and concatenating.

Thus such suppression preserves **existence of represented walks**. It does not automatically preserve simplicity, shortest-path length, multiplicity, or any property not guaranteed by the stored path certificates.

## Provenance

The source inventory carried versions of these statements under mixed names including `Finite CSP Compilation Theorem`, `Black-Box Finite Constraint Acquisition Theorem`, `Finite-Court Convergence Theorem`, `No-Repeated-Tuition Corollary`, `Isolation-Driven Architecture Lower Bound`, `Proof-Carrying Suppression Preservation`, and `Strict Alchemical Progress Trichotomy`.

The mathematical statements above have been rewritten in ordinary finite-combinatorics language and proved directly. No product-specific control logic, orchestration architecture, or applied embodiment is included.
