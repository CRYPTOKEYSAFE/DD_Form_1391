# SCH-3213 - DD Form 1391 Block 9
## CLB-4 Battalion Headquarters Conversion
## Camp Schwab, Okinawa, Japan | FY27 | MCIPAC G-F PPE

**PAX ID:** 387624 | **Fi Web:** BU26PPE72M | **iNFADS RPUID:** 48879 | **Primary CCN:** 61010 (Battalion / Squadron HQ - MARCOR, FAC 2171) | **Total Building GSF:** 13,484

All amounts in $000s to three decimal places. Dollar values exactly as in the CEPBKUP workbook (3213_G_CEPBKUP_BU26PPE72M_POM26_20260320.xlsx).

---

## iNFADS-locked row (PAX-auto, NOT operator entered)

This is the row PAX renders at the top of the Block 9 Data items table. The Description, Classification of Work, Work Type, UM, and Quantity come from the iNFADS property record and are not operator-editable. Unit Cost and Total are PAX-calculated.

```
Description:                COMPANY HQ
Classification of Work:     C
Work Type:                  RM
UM:                         SF
Quantity:                   1.00
Unit Cost ($):              5,397,928.00
Total Cost ($000):          5,398
```

Total = Total Project Cost (rounded to nearest $1,000) = $5,398K. PAX back-calculates Unit Cost from Total / Quantity at 1.00 SF.

## Operator-entered Block 9 cost estimate

```
9. COST ESTIMATES                           UNIT COST
ITEM                       U/M | QUANTITY | $000 | $000

PRIMARY FACILITIES                                 3,751.126
 BATTALION HEADQUARTERS BUILDING (Conversion/   SF | 13,484 | 278.176 | ( 3,751.126 )
 Alteration; CCN 61010)

SUPPORTING FACILITIES                                 272.333
 SPECIAL CONSTRUCTION FEATURES          LS |     |     | (  272.333 )
  (Life Safety and Health upgrades, 2.5% of
   iNFADS PRV $10,893,334 per NAVFAC 11010.44E
   CH-1 and MCO 11000.12)

SUBTOTAL                                      4,023.459
CONTINGENCY (10.0% of Primary Facilities, per                     375.113
 FSRM program direction; UFS 3-740-05 (2 Feb 2026), Level 3 ROM)
TOTAL CONTRACT COST                                 4,398.572
SUPERVISION, INSPECTION AND OVERHEAD (8.0% of TCC,                  351.886
 OCONUS FSRM customer-directed)
DESIGN COST (6.0% of TCC, NAVFAC agency-directed)                   263.914
CONSTRUCTION MANAGEMENT (4.0% of TCC, agency-directed)                175.943
TOTAL FUNDED COST                                  5,190.315
DESIGN/BUILD - DESIGN COST (4.0% of Total Funded; UFC 3-730-01            207.613
 (2024); applied AFTER Total Funded per Marine Corps FSRM convention)
TOTAL PROJECT COST                                 5,397.928
TOTAL PROJECT COST (ROUNDED)                            5,398.000
EQUIPMENT FROM OTHER APPROPRIATIONS (NON-ADD)                    (  0.000 )
```

## Math verification

- Primary + Supporting = $3,751.126 + $272.333 = $4,023.459 → Subtotal
- Subtotal + Contingency = $4,023.459 + $375.113 = $4,398.572 → matches workbook Construction Base
- 8.0% × TCC = $351.886 ← matches SIOH
- 6.0% × TCC = $263.914 ← matches Design
- 4.0% × TCC = $175.943 ← matches CM
- Total Funded = $5,190.315 ✓
- DB Design = $207.613 ✓
- TPC = $5,397.928 ✓

## Verification footer

| Source | Total Funded ($000s) | Total Project ($000s) |
|--------|----------------------|------------------------|
| CEPBKUP workbook (20 Mar 2026), DD1391_BLOCK9 tab | 5,190.315 | 5,397.928 |
| Current PAX .md state (consolidated file) | 5,190 | 5,398 (whole $000s rounding) |
| This corrected Block 9 | 5,190.315 | 5,397.928 |
| **Reconciliation vs workbook** | **PASS** | **PASS** |
| **Reconciliation vs current PAX .md** | PASS (totals match within rounding; SCH-3213 PAX .md uses whole-thousand rounding) | PASS |

## What changed cosmetically vs prior PAX entry

- Removed UNIFORMAT codes (prior UNIFORMAT prefixes) from line names.
- Removed discipline-first naming (prior UNIFORMAT-prefixed names).
- Consolidated 6 UNIFORMAT-grouped scope lines into a single Primary Facility line.
- Repositioned LSH from a free-standing line to a Special Construction Features sub-line under Supporting Facilities.
- Decimal precision standardized to 3 places (the prior SCH-3213 PAX entry used whole $000s as a one-off; the corrected Block 9 brings it in line with the rest of the portfolio).

## PAX Block 9 Data item-list mirror (paste-ready)

This is the same canonical architecture above, expressed as rows that paste directly into the PAX Block 9 Data items table. Order matches the canonical face. All totals reconcile.

```
ROW                                                           UM   Qty       Unit Cost ($)        Total ($000)
--------------------------------------------------------------|----|---------|--------------------|-------------
PRIMARY FACILITIES                                            |    |         |                    |  3,751.126
  COMPANY HQ                                                |  SF| 1.00    |         3,751,126.00|  3,751.126
  (Conversion/Alteration; per workbook ESTIMATE tab)          |    |         |                    |
                                                               |    |         |                    |
SUPPORTING FACILITIES                                         |    |         |                    |    272.333
  SPECIAL CONSTRUCTION FEATURES                               |  LS| 1.00    |           272,333.00|    272.333
  (Life Safety and Health upgrades, 2.5% of PRV;               |    |         |                    |
  NAVFAC 11010.44E CH-1 / MCO 11000.12)                        |    |         |                    |
```

**Cost rollup adders via PAX `Associated Costs` button (single path, no double counting).**

The items list above contains scope only (Primary Facility scope plus the LSH Special Construction Features sub-line under Supporting Facilities). The cost rollup adders are entered separately via the Associated Costs button as percent items. PAX exposes four named percent slots; the five workbook adders map onto them by combining NAVFAC Design 6% and Construction Management 4% into Planning and Design 10% (PAX has no native CM slot; the 4% CM rides under P&D). Block 10 narrative carries the Design and CM breakout for review.

| Order | PAX Associated Costs slot | Rate to enter | Workbook adder(s) covered |
|-------|---------------------------|--------------:|---------------------------|
|   1   | Contingency %             | 10.0%         | Contingency 10% |
|   2   | SIOH %                    | 8.0%          | SIOH 8% (OCONUS FSRM customer-directed) |
|   3   | Planning and Design %     | 10.0%         | NAVFAC Design 6% + CM 4% (combined) |
|   4   | Design Build %            | 4.0%          | DB Design 4% (UFC 3-730-01) |

**Items-list Subtotal:** $4,023,459 (Primary scope plus LSH). PAX renders the top-right Total Request after applying the four percent items above to the bases PAX uses internally. The workbook target Total Project Cost is $5,397,928. If the PAX-rendered Total Request and the workbook TPC do not match exactly, the difference is from a base-of-percent mismatch (workbook applies Contingency to Primary scope only; PAX applies Contingency to the items-list Subtotal which includes LSH). Reconcile by adjusting the workbook to match PAX's calculation or by raising the discrepancy to the team for a methodology call. Do not bake the adders into the items list as dollar lines while also entering them as percent items; that double-counts.

## Block 10 paired statement (PRIMARY FACILITY PS)

PRIMARY FACILITY (PS): "This project converts an existing 13,484 SF building into a CLB-4 Battalion Headquarters at Camp Schwab. Scope includes telecom infrastructure modernization per UFC 3-580-01, S-2 vault construction (two GSA Class V vault spaces), SIPR network rack installation per CNSSAM TEMPEST/01-13, secured pathway from Battalion Conference Room to S-2 vault, six private offices, EOD office partition, secure unit mail room per MCO 5110.1, full HVAC system replacement (chiller, AHU, pumps, ductwork, controls; 1984-era system past ASHRAE 30-yr service life), full plumbing system replacement (DWV piping, domestic water distribution, water heater, fixtures, restroom renovation), overhead door and air curtain replacement, and asbestos abatement (Bhate Environmental 2001 H2 finding, 570 SF Chrysotile non-friable, Rooms 8/23 / Corridor 100). Functions provided: CLB-4 Battalion HQ, with secondary support for H&S, CLR-3, 3MLG. The Special Construction Features line under Supporting Facilities is a 2.5%-of-PRV Life Safety and Health upgrade allowance per NAVFAC 11010.44E CH-1 and MCO 11000.12 (08 Sep 2014). PRV deviation: iNFADS confirmed PRV $10,893,334 (RPUID 48879) is used per client direction in lieu of UFC 3-701-01 formula PRV $8,085,190 (formula uses FAC 2171 / 6102 PUC); delta documented in CEPBKUP ESTIMATE Section F Item 11. Equipment included in the Primary Facility unit cost; no equipment from other appropriations."
