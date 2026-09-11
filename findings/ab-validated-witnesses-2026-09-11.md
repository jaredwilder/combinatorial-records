# A/B transcript mine — exact validated finite witnesses

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

These objects were recovered from the A/B transcript layer and independently rechecked during the estate audit. They are finite witnesses, **not record claims**.

## Sidon set — 22 elements in `[1,500]`

```text
[4,21,31,66,97,143,169,225,228,237,312,332,351,379,383,437,448,462,485,492,498,500]
```

Independent validation:

```text
size=22
unordered pair sums with repetition=22*23/2=253
all 253 pair sums distinct=PASS
```

Thus this is a valid 22-element Sidon subset of `[1,500]`. The audit notes that it is below the known exact maximum used by the campaign and is published only as a validated search object.

## Second Sidon set — 21 elements in `[1,500]`

```text
[1,4,8,13,21,31,45,66,81,97,123,148,182,204,252,290,361,401,456,489,495]
```

Validation:

```text
size=21
unordered pair sums with repetition=231
all 231 pair sums distinct=PASS
```

## 3AP-free set A — 150 elements in `[1,2000]`

```text
[1,2,4,5,11,13,14,28,29,31,32,37,38,40,41,82,84,85,91,92,94,95,110,112,113,118,121,122,244,246,247,253,257,271,274,275,280,281,283,284,325,326,328,329,334,335,337,338,353,355,356,362,364,497,499,515,730,731,733,734,739,740,742,743,757,758,760,761,766,769,770,811,812,814,815,820,821,823,824,838,839,841,842,848,850,851,973,974,977,1004,1009,1012,1054,1055,1058,1063,1064,1066,1067,1081,1082,1084,1085,1090,1091,1093,1094,1175,1253,1468,1496,1541,1567,1573,1576,1577,1630,1657,1703,1705,1709,1711,1714,1721,1729,1730,1732,1742,1756,1758,1769,1810,1819,1823,1867,1868,1874,1876,1892,1948,1951,1955,1957,1958,1969,1972,1973,1982,1985,1999]
```

Independent validation checked all `C(150,2)=11175` unordered endpoint pairs and found **zero nontrivial three-term arithmetic progressions**.

## 3AP-free set B — 150 elements in `[1,2000]`

```text
[1,2,4,5,10,11,13,28,29,31,32,37,38,41,82,85,86,91,92,94,95,109,110,112,113,118,119,121,122,244,245,247,253,254,256,257,271,272,274,275,280,283,326,328,329,334,335,337,338,352,353,356,362,365,491,524,527,598,604,607,730,731,733,734,739,740,742,743,757,758,760,761,766,767,769,770,811,812,814,815,820,824,838,841,842,847,848,850,851,974,976,982,985,986,1000,1001,1009,1054,1055,1057,1058,1063,1064,1066,1067,1081,1082,1085,1091,1094,1135,1174,1541,1547,1551,1552,1559,1568,1631,1660,1688,1702,1706,1709,1733,1737,1739,1740,1742,1783,1801,1807,1815,1816,1868,1894,1901,1903,1904,1945,1949,1952,1956,1958,1975,1976,1978,1982,1984,1985]
```

The same exhaustive pair check gives **PASS** with 11,175 endpoint pairs checked.

## Related parametric construction

The mine also contained a 512-element ternary-digit witness. Its general mathematical form has been promoted to

`jaredwilder/additive-combinatorics-campaigns/ternary-cube-3ap-free/`,

where the `2^d`-element construction is proved for every `d` rather than preserved only as a finite object.

## Provenance boundary

These sets are published as exact reproducible finite data. No claim is made that the Sidon sets or the 150-element 3AP-free sets are extremal or historically new.
