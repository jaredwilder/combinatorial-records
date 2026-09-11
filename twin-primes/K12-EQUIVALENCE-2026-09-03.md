# K12 — TYPE I / TYPE II SUFFICIENCY FOR TWIN PRIMES

CAMPAIGN: T1 (MSL v1.9, MSL_MODE CLOSE, contract CC1)
STATUS: PROVED over cited hypotheses; COVERS FRAGMENT; standard folklore, not novel.
This record has been corrected three times. The corrections are kept, not erased.

## STATEMENT (TS12, third form)
Decompose the twin sum via the Vaughan / Heath-Brown combinatorial identity into Type I and
Type II sums. Suppose:

  (a) TYPE I: primes in arithmetic progressions have level of distribution theta over
      UNRESTRICTED moduli d. THE THRESHOLD IS NOT theta > 1/2. For a purely combinatorial
      Heath-Brown decomposition the requirement is theta = 1 - eps; theta > 1/2 alone is
      insufficient. A well-factorable sieve reaches that level through a factored modulus
      q = uv instead. [SOURCE: external reading, round 16, UNVERIFIED]; and
  (b) TYPE II: the bilinear sums sum_m sum_k a_m b_k Lambda(mk+2) admit a nontrivial bound
      in the comparable-size range, uniform in the bilinear factors m and k.

Then the Hardy-Littlewood asymptotic count of twin primes follows.

WHICH ENGINE, AND WHEN — the round-11 correction was itself too absolute:
  - If Type II holds across its FULL range (x^eps <= M <= x^{1-eps}), the Heath-Brown
    identity drops every piece into Type I or Type II and the asymptotic follows DIRECTLY.
    No auxiliary sieve. This is the case round 11 described.
  - If Type II is available ONLY in the sub-window x^{1/2-delta} <= M <= x^{1/2+delta} —
    which is the comparable-size range this record actually names in (b) — then the
    Friedlander-Iwaniec or Bombieri asymptotic sieve IS STRICTLY REQUIRED to fill the
    gaps. Under the hypothesis as stated here, S7 is needed after all.
    [SOURCE: external reading, round 16; the exact activation window is flagged by the
    reader as memory-reconstructed, UNVERIFIED]

Neither (a) nor (b) is held. S9 (Zhang / Polymath8) gives (a) only for smooth moduli.
The converse implication is NOT derived and is not claimed.

## CORRECTION LOG
- Round 8: the record called TS12 an EQUIVALENCE; only the forward direction was derived.
  Corrected to IMPLICATION.
- Round 9: the record treated S9 as covering the unrestricted Type I range. It covers only
  smooth moduli. Hypothesis corrected to a CONJUNCTION of two unheld conditions.
- Round 11 (external review, Gemini 3.7 Flash, receipt
  oracle/evidence/ask-gemini/20260903T205509-2dfd851d.json): two defects named.
    (i)  The Friedlander-Iwaniec asymptotic sieve (S7) was cited as the engine. It is not
         needed: with (a) and (b) in hand the asymptotic follows directly. FI's asymptotic
         sieve is for sequences carrying no explicit bilinear identity on the weights (the
         x^2 + y^4 case). S7 is REMOVED from the hypotheses of TS12.
    (ii) "Uniform in the moduli produced by that decomposition" misstated the variable
         roles. Moduli d belong to the Type I convolution; the Type II ranging objects are
         the bilinear factors m and k. Corrected above.

## MAGNITUDE (external review, same receipt)
None of this is new. The bilinear template is standard since Vaughan (1981) and Heath-Brown
(1982), with Bombieri-Friedlander-Iwaniec (1986/87/89) on large moduli. TS12 is conditional
folklore an analytic number theorist would state in one sitting. Recorded here so the
campaign's own ledger carries the outside verdict.

## CITED HYPOTHESES
S7  Friedlander-Iwaniec asymptotic sieve for primes (1998) — REQUIRED under the narrow
    Type II window of (b); see the engine note above. Reinstated in round 16.
S8  Vaughan / Heath-Brown identities for the von Mangoldt function.
S9  Zhang / Polymath8: level beyond 1/2 for smooth moduli only.

## THE UNCONDITIONAL GAP (external reading, round 16; every number a LEAD, UNVERIFIED)
Bombieri-Vinogradov theta = 1/2, unrestricted moduli.
Bombieri-Friedlander-Iwaniec theta = 4/7, fixed residue, well-factorable.
Zhang (2014) theta = 1/2 + 1/1168, smooth moduli only.
Polymath8b theta = 1/2 + 7/300, smooth moduli only.
Maynard (2020, Annals) theta = 3/5, almost all residues.
NO published nontrivial Type II bound exists for sum alpha_m beta_n Lambda(mn+2) with
general bounded coefficients at M ~ N ~ x^{1/2}. Type II is the harder of the two, and
that is consensus rather than theorem.

## BARRIERS ESTABLISHED IN THE SAME CAMPAIGN (all standard; all results)
K6  one-free-variable systems have infinite Cauchy-Schwarz complexity, so Green-Tao-Ziegler
    transference returns no asymptotic for {n, n+2}.
K7  Bombieri's asymptotic sieve: no density-determined sifting procedure detects integers
    with exactly one prime factor.
K13 finiteness of the twin set is compatible with Brun, Chen, and every bounded-gap
    statement, none of which names the gap 2.
K14 no combination of this campaign's survivors, under the derivations on file, entails the
    infinitude of the twin set.
K15 S9 does not cover the unrestricted Type I range.

## FORMAL STATUS
NOT_TARGETED. No kernel backend: S8 is unavailable in the ambient formal library.

## VERIFICATION OF THE EXTERNAL READING (round 14)
The citation leads in the external review were checked by federated retrieval, not trusted.
Corpus: oracle/evidence/twin-primes/corpus-ts12.json (30 papers, 47 patents).
Confirmed present under the exact titles given: Heath-Brown, "Prime Numbers in Short
Intervals and a Generalized Vaughan Identity" (1982); Friedlander-Iwaniec, "Asymptotic
Sieve for Primes" (1998); "On Bombieri's asymptotic sieve" (1978); "Twin primes and the
parity problem" (2017).
NOT verified: the Opera de Cribro chapter numbers the reviewer flagged as memory-cited.
Retrieval noise: most of the 30 papers concern an unrelated sense of "parity" (neural
networks, cellular automata, matroids) and are not relevant to this record.

## CAMPAIGN VERDICT
Fifteen rounds. The Twin Prime Conjecture carries no derivation here. What the campaign
holds is this conditional statement, four standard barrier results, one branch kill, three
self-retractions, and one externally corroborated novelty verdict of zero.

## VERIFICATION, SECOND PASS (round 19)
Corpus: oracle/evidence/twin-primes/corpus-levels.json (30 papers, 21 patents).
CONFIRMED TO EXIST at title level: the Bombieri-Friedlander-Iwaniec series "Primes in
arithmetic progressions to large moduli" I (1986) / II (1987); Maynard's series, same title,
"II: Well-factorable estimates" and "III: Uniform residue classes"; the Kuznetsov/Kloosterman
spectral toolbox (Kuznetsov 1981; "Bilinear forms with Kloosterman sums and applications",
2017). STILL UNVERIFIED: the numeric exponents themselves (4/7, 3/5, 1/2+7/300, the 1-eps
threshold, the FI activation window) - titles corroborate the works, not the numbers.
DIRECTLY ADJACENT PRIOR ART FOUND: "A Generalized Elliott-Halberstam Conjecture Implying
the Twin Prime Hypothesis" (arXiv 2511.14810, 2025) - a published statement of the same
shape as TS12 (a distribution hypothesis implying twin primes). This independently
corroborates the novelty-zero verdict: the sufficiency framing is not merely folklore, it
is in the current literature. One provider in the acquisition crashed with a cp1252 decode
error (non-fatal, logged); the tool should force UTF-8 on cache reads.
