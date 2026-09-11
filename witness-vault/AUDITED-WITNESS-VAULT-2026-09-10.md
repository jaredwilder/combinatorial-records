# Audited Witness Vault — 2026-09-10
**Author:** Jared Wilder

This file publishes the 21 concrete witness objects independently revalidated in the 2026-09-01 forensic Erdős release. A witness proves only the exact finite statement attached to it. It does not inherit a stronger campaign status.

## 1. `run5_english_sidon35`
- kind: `Sidon`
- declared size: `35`
- domain: `[1,2000]`
- source: `run5-strategy/results.json:english.best_set.A`
- independent validation: `{"pair_sums": 630, "pass": true}`

```json
[1,2,4,8,13,21,31,45,66,81,97,123,148,182,204,252,290,361,401,475,565,593,662,775,822,916,970,1016,1159,1312,1395,1523,1572,1821,1896]
```

## 2. `run5_english_apfree512`
- kind: `3AP-free`
- declared size: `512`
- domain: `[1,10000]`
- source: `run5-strategy/results.json:english.best_set.B`
- independent validation: `{"checked_pairs": 130816, "pass": true}`
- notes: Ternary-style construction; independently checked, not claimed optimal.

```json
[1,2,4,5,10,11,13,14,28,29,31,32,37,38,40,41,82,83,85,86,91,92,94,95,109,110,112,113,118,119,121,122,244,245,247,248,253,254,256,257,271,272,274,275,280,281,283,284,325,326,328,329,334,335,337,338,352,353,355,356,361,362,364,365,730,731,733,734,739,740,742,743,757,758,760,761,766,767,769,770,811,812,814,815,820,821,823,824,838,839,841,842,847,848,850,851,973,974,976,977,982,983,985,986,1000,1001,1003,1004,1009,1010,1012,1013,1054,1055,1057,1058,1063,1064,1066,1067,1081,1082,1084,1085,1090,1091,1093,1094,2188,2189,2191,2192,2197,2198,2200,2201,2215,2216,2218,2219,2224,2225,2227,2228,2269,2270,2272,2273,2278,2279,2281,2282,2296,2297,2299,2300,2305,2306,2308,2309,2431,2432,2434,2435,2440,2441,2443,2444,2458,2459,2461,2462,2467,2468,2470,2471,2512,2513,2515,2516,2521,2522,2524,2525,2539,2540,2542,2543,2548,2549,2551,2552,2917,2918,2920,2921,2926,2927,2929,2930,2944,2945,2947,2948,2953,2954,2956,2957,2998,2999,3001,3002,3007,3008,3010,3011,3025,3026,3028,3029,3034,3035,3037,3038,3160,3161,3163,3164,3169,3170,3172,3173,3187,3188,3190,3191,3196,3197,3199,3200,3241,3242,3244,3245,3250,3251,3253,3254,3268,3269,3271,3272,3277,3278,3280,3281,6562,6563,6565,6566,6571,6572,6574,6575,6589,6590,6592,6593,6598,6599,6601,6602,6643,6644,6646,6647,6652,6653,6655,6656,6670,6671,6673,6674,6679,6680,6682,6683,6805,6806,6808,6809,6814,6815,6817,6818,6832,6833,6835,6836,6841,6842,6844,6845,6886,6887,6889,6890,6895,6896,6898,6899,6913,6914,6916,6917,6922,6923,6925,6926,7291,7292,7294,7295,7300,7301,7303,7304,7318,7319,7321,7322,7327,7328,7330,7331,7372,7373,7375,7376,7381,7382,7384,7385,7399,7400,7402,7403,7408,7409,7411,7412,7534,7535,7537,7538,7543,7544,7546,7547,7561,7562,7564,7565,7570,7571,7573,7574,7615,7616,7618,7619,7624,7625,7627,7628,7642,7643,7645,7646,7651,7652,7654,7655,8749,8750,8752,8753,8758,8759,8761,8762,8776,8777,8779,8780,8785,8786,8788,8789,8830,8831,8833,8834,8839,8840,8842,8843,8857,8858,8860,8861,8866,8867,8869,8870,8992,8993,8995,8996,9001,9002,9004,9005,9019,9020,9022,9023,9028,9029,9031,9032,9073,9074,9076,9077,9082,9083,9085,9086,9100,9101,9103,9104,9109,9110,9112,9113,9478,9479,9481,9482,9487,9488,9490,9491,9505,9506,9508,9509,9514,9515,9517,9518,9559,9560,9562,9563,9568,9569,9571,9572,9586,9587,9589,9590,9595,9596,9598,9599,9721,9722,9724,9725,9730,9731,9733,9734,9748,9749,9751,9752,9757,9758,9760,9761,9802,9803,9805,9806,9811,9812,9814,9815,9829,9830,9832,9833,9838,9839,9841,9842]
```

## 3. `run5_msl_sidon35`
- kind: `Sidon`
- declared size: `35`
- domain: `[1,2000]`
- source: `run5-strategy/results.json:msl.best_set.A`
- independent validation: `{"pair_sums": 630, "pass": true}`

```json
[1,2,4,8,13,21,31,45,66,81,97,123,148,182,204,252,290,361,401,475,565,593,662,775,822,916,970,1016,1159,1312,1395,1523,1572,1821,1896]
```

## 4. `run5_msl_apfree512`
- kind: `3AP-free`
- declared size: `512`
- domain: `[1,10000]`
- source: `run5-strategy/results.json:msl.best_set.B`
- independent validation: `{"checked_pairs": 130816, "pass": true}`
- notes: Ternary-style construction; independently checked, not claimed optimal.

```json
[1,2,4,5,10,11,13,14,28,29,31,32,37,38,40,41,82,83,85,86,91,92,94,95,109,110,112,113,118,119,121,122,244,245,247,248,253,254,256,257,271,272,274,275,280,281,283,284,325,326,328,329,334,335,337,338,352,353,355,356,361,362,364,365,730,731,733,734,739,740,742,743,757,758,760,761,766,767,769,770,811,812,814,815,820,821,823,824,838,839,841,842,847,848,850,851,973,974,976,977,982,983,985,986,1000,1001,1003,1004,1009,1010,1012,1013,1054,1055,1057,1058,1063,1064,1066,1067,1081,1082,1084,1085,1090,1091,1093,1094,2188,2189,2191,2192,2197,2198,2200,2201,2215,2216,2218,2219,2224,2225,2227,2228,2269,2270,2272,2273,2278,2279,2281,2282,2296,2297,2299,2300,2305,2306,2308,2309,2431,2432,2434,2435,2440,2441,2443,2444,2458,2459,2461,2462,2467,2468,2470,2471,2512,2513,2515,2516,2521,2522,2524,2525,2539,2540,2542,2543,2548,2549,2551,2552,2917,2918,2920,2921,2926,2927,2929,2930,2944,2945,2947,2948,2953,2954,2956,2957,2998,2999,3001,3002,3007,3008,3010,3011,3025,3026,3028,3029,3034,3035,3037,3038,3160,3161,3163,3164,3169,3170,3172,3173,3187,3188,3190,3191,3196,3197,3199,3200,3241,3242,3244,3245,3250,3251,3253,3254,3268,3269,3271,3272,3277,3278,3280,3281,6562,6563,6565,6566,6571,6572,6574,6575,6589,6590,6592,6593,6598,6599,6601,6602,6643,6644,6646,6647,6652,6653,6655,6656,6670,6671,6673,6674,6679,6680,6682,6683,6805,6806,6808,6809,6814,6815,6817,6818,6832,6833,6835,6836,6841,6842,6844,6845,6886,6887,6889,6890,6895,6896,6898,6899,6913,6914,6916,6917,6922,6923,6925,6926,7291,7292,7294,7295,7300,7301,7303,7304,7318,7319,7321,7322,7327,7328,7330,7331,7372,7373,7375,7376,7381,7382,7384,7385,7399,7400,7402,7403,7408,7409,7411,7412,7534,7535,7537,7538,7543,7544,7546,7547,7561,7562,7564,7565,7570,7571,7573,7574,7615,7616,7618,7619,7624,7625,7627,7628,7642,7643,7645,7646,7651,7652,7654,7655,8749,8750,8752,8753,8758,8759,8761,8762,8776,8777,8779,8780,8785,8786,8788,8789,8830,8831,8833,8834,8839,8840,8842,8843,8857,8858,8860,8861,8866,8867,8869,8870,8992,8993,8995,8996,9001,9002,9004,9005,9019,9020,9022,9023,9028,9029,9031,9032,9073,9074,9076,9077,9082,9083,9085,9086,9100,9101,9103,9104,9109,9110,9112,9113,9478,9479,9481,9482,9487,9488,9490,9491,9505,9506,9508,9509,9514,9515,9517,9518,9559,9560,9562,9563,9568,9569,9571,9572,9586,9587,9589,9590,9595,9596,9598,9599,9721,9722,9724,9725,9730,9731,9733,9734,9748,9749,9751,9752,9757,9758,9760,9761,9802,9803,9805,9806,9811,9812,9814,9815,9829,9830,9832,9833,9838,9839,9841,9842]
```

## 5. `run8_english_sidon22`
- kind: `Sidon`
- declared size: `22`
- domain: `[1,500]`
- source: `run8-sidon500-v3/results.json:english.best_set`
- independent validation: `{"pair_sums": 253, "pass": true}`

```json
[4,21,31,66,97,143,169,225,228,237,312,332,351,379,383,437,448,462,485,492,498,500]
```

## 6. `run8_msl_sidon21`
- kind: `Sidon`
- declared size: `21`
- domain: `[1,500]`
- source: `run8-sidon500-v3/results.json:msl.best_set`
- independent validation: `{"pair_sums": 231, "pass": true}`

```json
[1,4,8,13,21,31,45,66,81,97,123,148,182,204,252,290,361,401,456,489,495]
```

## 7. `run9_english_apfree150`
- kind: `3AP-free`
- declared size: `150`
- domain: `[1,2000]`
- source: `run9-apfree2000-v3/results.json:english.best_set`
- independent validation: `{"checked_pairs": 11175, "pass": true}`

```json
[1,2,4,5,11,13,14,28,29,31,32,37,38,40,41,82,84,85,91,92,94,95,110,112,113,118,121,122,244,246,247,253,257,271,274,275,280,281,283,284,325,326,328,329,334,335,337,338,353,355,356,362,364,497,499,515,730,731,733,734,739,740,742,743,757,758,760,761,766,769,770,811,812,814,815,820,821,823,824,838,839,841,842,848,850,851,973,974,977,1004,1009,1012,1054,1055,1058,1063,1064,1066,1067,1081,1082,1084,1085,1090,1091,1093,1094,1175,1253,1468,1496,1541,1567,1573,1576,1577,1630,1657,1703,1705,1709,1711,1714,1721,1729,1730,1732,1742,1756,1758,1769,1810,1819,1823,1867,1868,1874,1876,1892,1948,1951,1955,1957,1958,1969,1972,1973,1982,1985,1999]
```

## 8. `run9_msl_apfree150`
- kind: `3AP-free`
- declared size: `150`
- domain: `[1,2000]`
- source: `run9-apfree2000-v3/results.json:msl.best_set`
- independent validation: `{"checked_pairs": 11175, "pass": true}`

```json
[1,2,4,5,10,11,13,28,29,31,32,37,38,41,82,85,86,91,92,94,95,109,110,112,113,118,119,121,122,244,245,247,253,254,256,257,271,272,274,275,280,283,326,328,329,334,335,337,338,352,353,356,362,365,491,524,527,598,604,607,730,731,733,734,739,740,742,743,757,758,760,761,766,767,769,770,811,812,814,815,820,824,838,841,842,847,848,850,851,974,976,982,985,986,1000,1001,1009,1054,1055,1057,1058,1063,1064,1066,1067,1081,1082,1085,1091,1094,1135,1174,1541,1547,1551,1552,1559,1568,1631,1660,1688,1702,1706,1709,1733,1737,1739,1740,1742,1783,1801,1807,1815,1816,1868,1894,1901,1903,1904,1945,1949,1952,1956,1958,1975,1976,1978,1982,1984,1985]
```

## 9. `run20_C13_6_3_cover21`
- kind: `C(13,6,3) covering`
- declared size: `21`
- domain: `points 0..12`
- source: `run20-frontier-C13-6-3/results.json:best_obj`
- independent validation: `{"missing": 0, "pass": true, "triples_covered": 286, "triples_total": 286}`
- notes: All 286 triples independently checked covered.

```json
[[0,3,4,5,7,9],[2,5,7,8,9,10],[1,2,4,8,9,11],[3,4,5,6,8,11],[0,1,2,4,6,7],[0,2,6,8,9,12],[0,1,2,5,11,12],[0,1,3,5,8,12],[1,2,3,4,8,9],[1,5,6,7,9,12],[2,6,9,10,11,12],[0,1,3,9,10,11],[3,4,6,9,10,12],[2,3,7,10,11,12],[0,2,3,5,6,10],[5,7,8,9,10,11],[0,4,7,8,10,12],[1,3,6,7,8,10],[0,4,8,10,11,12],[1,2,4,5,10,12],[0,1,4,6,7,11]]
```

## 10. `run23b_C13_6_3_cover21`
- kind: `C(13,6,3) covering`
- declared size: `21`
- domain: `points 0..12`
- source: `run23b-fearless-court/transcript-cover20.json:round1 feedback`
- independent validation: `{"missing": 0, "pass": true, "triples_covered": 286, "triples_total": 286}`
- notes: Independent second 21-block witness.

```json
[[0,1,2,5,6,12],[0,1,3,7,8,11],[0,1,4,7,9,10],[0,1,4,8,10,11],[0,2,3,4,8,10],[0,2,3,7,9,12],[0,2,4,8,11,12],[0,3,4,5,6,7],[0,4,5,6,10,12],[0,5,6,8,9,11],[1,2,3,4,6,8],[1,2,3,5,10,12],[1,2,6,7,9,11],[1,3,5,8,9,12],[1,4,5,7,11,12],[1,6,7,8,10,12],[2,3,5,7,10,11],[2,4,5,7,8,9],[2,5,6,8,9,10],[3,4,6,9,11,12],[3,6,9,10,11,12]]
```

## 11. `run11_distinct_subset_sums14`
- kind: `distinct subset sums`
- declared size: `14`
- domain: `positive integers <=10000`
- source: `run11-erdos-dss-penalty/results.json:english.best_set`
- independent validation: `{"pass": true, "subset_sums": 16384}`
- notes: Powers of 2; mathematically trivial calibration witness.

```json
[1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]
```

## 12. `run19_sidon8_size4`
- kind: `Sidon`
- declared size: `4`
- domain: `[1,8]`
- source: `run19-the-stamp/results.json:best_obj`
- independent validation: `{"pair_sums": 10, "pass": true}`
- notes: Ground-truth optimality receipt exists in campaign harness; object independently Sidon-checked.

```json
[1,2,4,8]
```

## 13. `erdos979_f2_410_collision`
- kind: `two-prime-square representations`
- declared size: `2`
- domain: `n=410`
- source: `raw campaign transcript + fresh recheck`
- independent validation: `{"count": 2, "pass": true}`
- notes: Exact finite collision under unordered-multiset semantics; not a limsup result.

```json
[[7,19],[11,17]]
```

## 14. `erdos930_k2_square_product`
- kind: `two disjoint consecutive intervals`
- declared size: `2`
- domain: `k=2`
- source: `raw campaign transcript + fresh recheck`
- independent validation: `{"pass": true, "product": 144, "square": 144}`
- notes: Exact finite witness only.

```json
[[1,2],[8,9]]
```

## 15. `erdos930_k3_square_product`
- kind: `two disjoint consecutive intervals`
- declared size: `2`
- domain: `k=3`
- source: `raw campaign transcript + fresh recheck`
- independent validation: `{"pass": true, "product": 705600, "square": 705600}`
- notes: Exact finite witness only.

```json
[[1,2,3],[48,49,50]]
```

## 16. `ab_distinct_distances_4x3_grid`
- kind: `12-point planar distinct-distance witness`
- declared size: `12`
- domain: `integer grid / A-B distinct-distances task`
- source: `run12b-erdos-dd-fixedparser MSL result + fresh independent recheck`
- independent validation: `{"distinct_squared_distances": 8, "pass": true, "squared_distances": [1, 2, 4, 5, 8, 9, 10, 13]}`
- notes: The 4x3 grid has exactly 8 distinct nonzero squared distances; improves the English run value 11 in this A/B task. Computational witness, not by itself a canonical Erdős closure.

```json
[[0,0],[1,0],[2,0],[3,0],[0,1],[1,1],[2,1],[3,1],[0,2],[1,2],[2,2],[3,2]]
```

## 17. `erdos1_sumdistinct_5_N13`
- kind: `distinct subset-sum witness`
- declared size: `5`
- domain: `A subset [1,13]`
- source: `erdos1 registry R001/L0 + fresh exhaustive recheck`
- independent validation: `{"A": [6, 9, 11, 12, 13], "N": 13, "constant_ceiling": "13/32", "distinct": true, "subset_sum_count": 32}`
- notes: All 32 subset sums are distinct; forces C<13/32 in the frozen strict-inequality formulation.

```json
[6,9,11,12,13]
```

## 18. `erdos213_n4_general_position_integer_distances`
- kind: `planar integer-distance general-position witness`
- declared size: `4`
- domain: `R^2`
- source: `erdos213 raw campaign + fresh exact recheck`
- independent validation: `{"all_integer": true, "concyclic_det": 33264, "no_three_collinear": true, "not_concyclic": true, "pair_distances": [{"d2": 576, "distance": 24, "pair": [0, 1]}, {"d2": 169, "distance": 13, "pair": [0, 2]}, {"d2": 225, "distance": 15, "pair": [0, 3]}, {"d2": 169, "distance": 13, "pair": [1, 2]}, {"d2": 225, "distance": 15, "pair": [1, 3]}, {"d2": 196, "distance": 14, "pair": [2, 3]}], "points": [[-12, 0], [12, 0], [0, 5], [0, -9]], "triple_determinants": [{"det": 120, "triple": [0, 1, 2]}, {"det": -216, "triple": [0, 1, 3]}, {"det": -168, "triple": [0, 2, 3]}, {"det": 168, "triple": [1, 2, 3]}]}`
- notes: All six pairwise distances are integers; no three collinear; four points not concyclic. Solves n=4 only.

```json
[[-12,0],[12,0],[0,5],[0,-9]]
```

## 19. `erdos389_n2_k5_divisibility`
- kind: `consecutive-product divisibility witness`
- declared size: `1`
- domain: `n=2,k=5`
- source: `erdos389 registry + fresh exact recheck`
- independent validation: `{"divides": true, "left": 720, "quotient": 77, "right": 55440}`
- notes: 720 divides 55440 with quotient 77; exact finite witness only.

```json
{"n":2,"k":5,"left_factors":[2,3,4,5,6],"right_factors":[7,8,9,10,11]}
```

## 20. `erdos1142_R001_L1_counterexample`
- kind: `internal-lemma counterexample`
- declared size: `1`
- domain: `n=21,p=5`
- source: `fresh seventh-pass exact audit of erdos1142 R001/L1`
- independent validation: `{"Good": true, "counterexample": true, "differences": [{"difference": 19, "power": 2, "prime": true}, {"difference": 17, "power": 4, "prime": true}, {"difference": 13, "power": 8, "prime": true}, {"difference": 5, "power": 16, "prime": true}], "n": 21, "ord_p_2": 4, "p": 5, "p_divides_n": false, "p_le_n_over_2": true, "primitive_root_condition": true}`
- notes: Refutes campaign lemma Good(n) & p<=n/2 & ord_p(2)=p-1 => p|n. It is not a counterexample to the canonical Erdős #1142 statement.

```json
{"n":21,"p":5}
```

## 21. `erdos930_pell_family_prefix`
- kind: `Pell-generated square-product family prefix`
- declared size: `6`
- domain: `r=2,k=2`
- source: `erdos930 R001/L1 Pell observation + fresh recurrence recheck`
- independent validation: `{"count": 6, "pass": true}`
- notes: Finite prefix of an exact infinite family; theorem proof is recorded in THEOREM_VAULT.csv.

```json
[{"t":2,"x":49,"y":10,"a":24,"disjoint":true,"product":3600,"sqrt":60,"square":true,"expected_sqrt":60},{"t":3,"x":485,"y":99,"a":242,"disjoint":true,"product":352836,"sqrt":594,"square":true,"expected_sqrt":594},{"t":4,"x":4801,"y":980,"a":2400,"disjoint":true,"product":34574400,"sqrt":5880,"square":true,"expected_sqrt":5880},{"t":5,"x":47525,"y":9701,"a":23762,"disjoint":true,"product":3387938436,"sqrt":58206,"square":true,"expected_sqrt":58206},{"t":6,"x":470449,"y":96030,"a":235224,"disjoint":true,"product":331983392400,"sqrt":576180,"square":true,"expected_sqrt":576180},{"t":7,"x":4656965,"y":950599,"a":2328482,"disjoint":true,"product":32530984516836,"sqrt":5703594,"square":true,"expected_sqrt":5703594}]
```
