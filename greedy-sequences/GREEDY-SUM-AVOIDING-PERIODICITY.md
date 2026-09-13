# Uniform periodicity for a greedy sum-avoiding sequence

**Author:** Jared Wilder  
**Recovered from:** session-transcript mathematics sweep  
**Promoted to static subject record:** 2026-09-13

## Definition

Fix an integer `k>=1`. Start with the seed `{k}` and repeatedly append the least integer larger than the current largest term that is **not** representable as the sum of two earlier terms, where the two summands are allowed to be equal.

Let `A_k` be the resulting greedy sequence.

## Theorem

Put

\[
m=3k-1.
\]

Then

\[
\boxed{
A_k=\{n\ge k:n\bmod m\in\{k,k+1,\ldots,2k-1\}\}.
}
\]

Equivalently, `A_k` is the union of the length-`k` blocks

\[
B_q=[qm+k,\,qm+2k-1]\cap\mathbb Z,
\qquad q=0,1,2,\ldots
\]

with period `3k-1` from the first term onward.

Examples:

```text
k=1  m=2    1,3,5,7,9,11,...
k=2  m=5    2,3,7,8,12,13,17,18,...
k=3  m=8    3,4,5,11,12,13,19,20,21,...
k=4  m=11   4,5,6,7,15,16,17,18,...
k=5  m=14   5,6,7,8,9,19,20,21,22,23,...
```

## Proof

Let

\[
R=\{k,k+1,\ldots,2k-1\}\subset\mathbb Z/m\mathbb Z.
\]

First observe that sums of two residues from `R` lie in the integer interval

\[
[2k,4k-2].
\]

Modulo `m=3k-1`, this becomes

\[
\{2k,\ldots,3k-2\}\cup\{0,\ldots,k-1\},
\]

which is disjoint from `R`. Therefore no sum of two members of the claimed set can itself belong to the claimed set.

It remains to prove greediness: every integer omitted between two consecutive claimed blocks is already forced out by a sum of earlier accepted terms.

The opening block is

\[
B_0=[k,2k-1].
\]

Starting from `k`, every integer through `2k-1` is accepted because the smallest possible sum of two accepted terms is `2k`.

Now suppose the greedy construction has reached and accepted the entire block

\[
B_q=[qm+k,qm+2k-1].
\]

The gap before the next claimed block is

\[
G_q=[qm+2k,\,qm+4k-2].
\]

But

\[
B_0+B_q
=
[k,2k-1]+[qm+k,qm+2k-1]
=
[qm+2k,qm+4k-2]
=
G_q.
\]

Thus **every integer in the whole gap is a sum of two already accepted terms** and is rejected by the greedy rule.

The next integer is

\[
(q+1)m+k=qm+4k-1,
\]

one larger than the largest sum in `B_0+B_q`. More generally, the residue calculation above shows that no sum of any two previously accepted members can land in the residue interval `R`. Hence the entire next block `B_{q+1}` is accepted.

Induction over `q` proves the formula. ∎

## What the transcript audit corrected

An earlier record declared that the `k=2` gap string showed no period. The source of that verdict was a single invalid term: it admitted `11`, although

\[
11=3+8
\]

and both `3` and `8` have already appeared. Removing that term restores the exact period-5 sequence

\[
2,3,7,8,12,13,\ldots
\]

from the start.

The transcript sweep also checked the formula term-for-term for `k=1,...,10`, 300 terms each, with zero mismatches. That computation is useful regression evidence; the theorem above is the general proof.

## Status / novelty

**PROVED PROSE THEOREM.** No historical novelty claim is made here. The result is published because it was genuine standalone mathematics living only in session conversation and deserved a durable subject record.
