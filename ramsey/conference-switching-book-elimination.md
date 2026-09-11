# Conference switching cannot realize the target Ramsey-book family

**Author:** Jared Wilder  
**Source campaign:** 2026-07-22  
**Proof completed during public topology audit:** 2026-09-11

## Theorem

Let `N=4m+2 >= 6`, and let `C` be a symmetric conference matrix of order `N`:

- `C=C^T`;
- `C_ii=0`;
- `C_ij in {+1,-1}` for `i!=j`;
- `C^2=(N-1)I`.

Form a graph `G` by declaring `ij` an edge exactly when `C_ij=-1`. The same statement applies after arbitrary diagonal `±1` switching, since a switched matrix is again a symmetric conference matrix.

Then it is impossible that simultaneously

- every edge of `G` has at most `m-1` common neighbours; and
- every non-edge of `G` has at most `m` common non-neighbours.

Consequently no graph in any switching class of any symmetric conference matrix of order `4m+2` simultaneously avoids the book `B_m` while its complement avoids `B_(m+1)`.

For `N=398=4*99+2`, the entire switched symmetric-conference construction class is therefore eliminated from the `B_99 / B_100` Ramsey-book search.

This is a **construction-class impossibility theorem**, not a nonexistence theorem for arbitrary graphs.

## Proof

Let

`r_i = sum_j C_ij`

be the row sums. Because each row contains `N-1=4m+1` entries from `{+1,-1}`, every `r_i` is odd.

For distinct `i,j`, row orthogonality gives

`sum_{k!=i,j} C_ik C_jk = 0`.

The standard four-type count then yields the exact formulas recorded in the original campaign:

- if `C_ij=-1` (so `ij` is an edge), the number of common neighbours is

  `(N-4-r_i-r_j)/4`;

- if `C_ij=+1` (so `ij` is a non-edge), the number of common non-neighbours is

  `(N-4+r_i+r_j)/4`.

Assume the two book-avoidance inequalities hold.

For an edge,

`(N-4-r_i-r_j)/4 <= m-1`.

Using `N=4m+2` gives

`r_i+r_j >= 2`.

For a non-edge,

`(N-4+r_i+r_j)/4 <= m`,

hence

`r_i+r_j <= 2`.

Now define

`s_i = r_i-1`.

Then for every distinct pair `i,j`:

- `C_ij=-1` implies `s_i+s_j >= 0`;
- `C_ij=+1` implies `s_i+s_j <= 0`.

Therefore in **both** cases

`C_ij (s_i+s_j) <= 0`.

Fix `i` and sum over `j`. The diagonal term vanishes because `C_ii=0`, so

`sum_j C_ij(s_i+s_j) <= 0`.      (1)

But write `1` for the all-ones vector. Since

`r = C 1`

and

`C^2=(N-1)I`,

we have

`C r = (N-1) 1`.

Because `s=r-1`,

`C s = C r - C 1 = (N-1)1-r = (N-2)1-s`.

Hence the left side of (1) is exactly

` s_i * sum_j C_ij + (Cs)_i`

`= s_i r_i + (N-2-s_i)`

`= s_i(s_i+1) + N-2-s_i`

`= s_i^2 + N-2`.

Since `N>=6`,

`s_i^2+N-2 > 0`,

contradicting (1).

Therefore the two book-avoidance conditions cannot hold simultaneously. QED.

## Historical note

The recovered campaign card already contained the exact common-neighbour formulas but stopped before assembling them into a contradiction. During the September 11 repository-organization audit, that missing step was reconstructed from the same row sums and the conference identity `C^2=(N-1)I`.

The small `N=6` exhaustive switching check preserved elsewhere is now a regression check rather than the basis of the proof.

## Companion negative search facts

The source campaign also records:

- a Goethals–Seidel length-199 finite-field route that failed every tested sign convention and missed the target book bounds by 12 or 13;
- a two-block circulant near-candidate with maximum excess 2;
- that seed as a strict one-swap local optimum inside the investigated cross-annihilation manifold.

Those are search results, not global impossibility theorems.

Historical novelty of the completed conference-switching theorem remains a separate literature question.
