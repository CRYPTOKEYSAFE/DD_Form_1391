# Deliverable 02 - Canonical Block 9 Template
## Single template applied to all five Camp Schwab buildings

**Authority:** MCON/MCNR Consistency Review Board Guidelines & DD 1391 Development, May 2024 (REV #15), Section 3 (Primary Facilities), Section 4 (Supporting Facilities). AF MILCON exemplars (Eielson 2018, Fairford 2018, Nellis 2018). UFC 3-730-01 (2024) for DB Design.

**Convention:** All amounts in $000s to three decimal places (Camp Schwab convention). Building IDs in `SCH-####` form. Dollar values preserved exactly from CEPBKUP workbooks (workbook is cost estimate of record ).

---

## Template (face of Block 9)

```
9. COST ESTIMATES                      UNIT COST
ITEM                     U/M | QUANTITY | $000 | $000

PRIMARY FACILITIES                             [P_TOTAL]
 [Building Name] (Conversion/Alteration)   SF | [GSF]  | [PUC] | ([P_LINE])

SUPPORTING FACILITIES                           [S_TOTAL]
 SPECIAL CONSTRUCTION FEATURES        LS |     |    | ([LSH])
  (Life Safety and Health upgrades, 2.5% of PRV per
   NAVFAC 11010.44E CH-1 / MCO 11000.12)

SUBTOTAL                                  [SUBTOTAL]
CONTINGENCY (10.0%)                            [CONT]
TOTAL CONTRACT COST                            [TCC]
SUPERVISION, INSPECTION AND OVERHEAD (8.0%)                [SIOH]
DESIGN COST (6.0% NAVFAC AGENCY-DIRECTED)                 [DESIGN]
CONSTRUCTION MANAGEMENT (4.0%)                       [CM]
TOTAL FUNDED COST                             [TFC]
DESIGN/BUILD - DESIGN COST (4.0% APPLIED AFTER TOTAL FUNDED)        [DBD]
TOTAL PROJECT COST                             [TPC]
TOTAL PROJECT COST (ROUNDED)                        [TPC_R]
EQUIPMENT FROM OTHER APPROPRIATIONS (NON-ADD)               ([EOA])
```

## Line-by-line

| Line | Source | Manual cite | Notes |
|------|--------|-------------|-------|
| PRIMARY FACILITIES (header) | sum of sub-lines | CRB §3.1 (p.19) | Section header. Total at right. |
| Building line (sub-line) | CEPBKUP Subtotal | CRB §3.7 (p.23) | Conversion/Alteration. Quantity = scope-affected GSF. Unit cost = User-Generated. |
| SUPPORTING FACILITIES (header) | sum of sub-lines | CRB §3.1 (p.19) | Section header. Total at right. |
| SPECIAL CONSTRUCTION FEATURES | CEPBKUP LSH | CRB §4.9 (p.30); §3.1 supporting item 1 (p.19) | Life Safety and Health upgrade allowance. Manual silent on LSH; placement per deliverable 01. |
| SUBTOTAL | PRIMARY + SUPPORTING | CRB §4.7.1 (p.32) | Excludes Contingency, SIOH, all Design, CM. |
| CONTINGENCY (10.0%) | CEPBKUP Contingency | CRB §3.3 (p.22) | 10% per FSRM program-direction. Level 3 ROM, UFS 3-740-05 (2 Feb 2026). |
| TOTAL CONTRACT COST | SUBTOTAL + CONTINGENCY | AF exemplars (Eielson, Fairford, Nellis 2018) | Universal DD 1391 convention. |
| SIOH (8.0%) | CEPBKUP SIOH | CRB §3.4 (p.22) | OCONUS FSRM customer-directed rate (NOT standard 7.3%). Documented client deviation. |
| DESIGN (6.0%) | CEPBKUP Design | NAVFAC 11010.44E CH-1 | Marine Corps / Navy agency-directed. Manual §3.5 addresses only DB Design 4%; the 6% design is a Navy/MC program adder. |
| CM (4.0%) | CEPBKUP CM | NAVFAC agency-directed | Manual silent. Standard MC/Navy adder. |
| TOTAL FUNDED COST | TCC + SIOH + DESIGN + CM | DD Form 1391 convention | This is the "fenced" funded amount per Marine Corps FSRM convention. |
| DB DESIGN (4.0%) | CEPBKUP DB Design | UFC 3-730-01 (2024) | Applied AFTER Total Funded per Marine Corps FSRM convention (deviation from manual §3.5 noted; dollar value preserved). |
| TOTAL PROJECT COST | TFC + DBD | DD Form 1391 convention | The all-in number including DB design phase. |
| TOTAL PROJECT COST (ROUNDED) | TPC rounded to nearest $1,000 | AF exemplars | Cosmetic rounding for the budget submission. |
| EQUIPMENT FROM OTHER APPROPRIATIONS (NON-ADD) | $0 for all five | CRB §1.4 (p.7), §8 | None of the five buildings have equipment from other appropriations. Show as "(0)" non-add. |

## Operator vs PAX-auto fields

- **PAX auto-populate (do not enter)**: Parent line at top of Block 9 - Building name, CCN, Class (R), Type (RM), UM, Quantity, Unit Cost - these are pulled from the iNFADS property record connected to the PAX project. **CANNOT be altered.** This is the constraint Anthony confirmed: "I cannot alter that first line remember that so what's locked into iNFADS is there I can't change it."
- **Operator entry**: Everything below the parent line. The full canonical template is operator-typed into the PAX cost estimate child-line interface.

## Architecture order verification

The order strictly follows Section 3.1 of the manual:

1. PRIMARY FACILITIES section → 2. SUPPORTING FACILITIES section → 3. cost rollup (Subtotal → Contingency → TCC → SIOH → Design → CM → Total Funded → DB Design → TPC → TPC Rounded → Equipment from Other Appropriations).

Rob's stated complaint: "Block 9 is not broken down by discipline or broken out by Uniformat. Straight forward Primary Facility(s), Supporting, Contingency and on down to Other Appropriations." This template is exactly that.

## What this template removes from the current state

- UNIFORMAT II Level 2 codes (B20, C10, C30, D20, D30, D40, D50, E20, F10, F20, G10, G20) appearing as line names on Block 9. Removed. UNIFORMAT belongs in the SCOPE_DETAIL tab of the cost estimate workbook, not on the face of Block 9.
- Discipline-first line names (HVAC, Plumbing, Electrical, Mechanical, Fire Protection, Communications, Site). Removed. The Primary Facility line names the facility, not the discipline.
- LSH as a free-standing line between Contingency and Design. Removed. Repositioned as a Special Construction Features sub-line under Supporting Facilities.

## What this template preserves

- Every dollar value from the CEPBKUP workbook to the dollar.
- Every locked program adder rate (ACF 1.85, Escalation 2.1%/yr FY24-FY27, GR 10%, Contingency 10%, LSH 2.5% PRV, Design 6%, SIOH 8%, CM 4%, DB Design 4%).
- All authority citations.

## Cross-reference to AF exemplars (Rob's email attachments)

The canonical face above is built directly from the three Air Force MILCON DD 1391 examples Rob Kaye attached:
- Eielson AFB F-35A OSS/Weapons/Intel Facility (FY18, FTQW180102)
- RAF Fairford EIC RC-135 Intel and Squad Ops Facility (FY18, GKVB163017)
- Nellis AFB Red Flag 5th Gen Facility Addition (FY18, RKMF063004)

Mapping our deliverable lines to the exact AF exemplar line labels:

| Camp Schwab deliverable line | AF exemplar equivalent | Notes |
|------------------------------|------------------------|-------|
| PRIMARY FACILITIES (header) | PRIMARY FACILITIES   | identical, ALL CAPS section header with right-aligned total |
| Sub-line in parens       | Sub-line in parens   | identical convention; Eielson shows OSS/WEAPONS/INTEL ($7,335) and SUSTAINABILITY AND ENERGY MEASURES ($149) within Primary Facilities sub-total $7,484 |
| SUPPORTING FACILITIES (header)| SUPPORTING FACILITIES | identical |
| SPECIAL CONSTRUCTION FEATURES (LSH home) | (not present on AF; AF doesn't use LSH) | manual §3.1 Supporting Facilities item 1; §4.9 definition |
| SUBTOTAL           | SUBTOTAL        | identical |
| CONTINGENCY (10.0%)      | CONTINGENCY (5.0%)   | rate differs (FSRM program-directed for MC; AF uses 5% for Program Final per manual §3.3) |
| TOTAL CONTRACT COST      | TOTAL CONTRACT COST  | identical label |
| SIOH (8.0%)          | SUPERVISION, INSPECTION AND OVERHEAD (X.X%) | rate differs (8.0% MC OCONUS FSRM customer-directed vs 6.5% AF CONUS or 5.7% AF Nellis) |
| DESIGN COST (6.0% NAVFAC)   | (not present on AF)  | NAVFAC agency-directed; manual §3.5 only addresses DB Design 4% |
| CONSTRUCTION MANAGEMENT (4.0%)| (not present on AF)  | NAVFAC agency-directed; manual silent |
| TOTAL FUNDED COST       | (intermediate only)  | MC FSRM intermediate; AF rolls into Total Request |
| DESIGN/BUILD - DESIGN COST (4.0%) | DESIGN/BUILD - DESIGN COST (4.0% OF SUBTOTAL) | rate identical; base differs (MC = 4% of Total Funded; AF/manual §3.5 = 4% of Subtotal). Documented deviation. Dollar value preserved . |
| TOTAL PROJECT COST      | TOTAL REQUEST     | semantic equivalent: budget submission amount inclusive of DB Design |
| TOTAL PROJECT COST (ROUNDED) | TOTAL REQUEST (ROUNDED)| identical convention |
| EQUIPMENT FROM OTHER APPROPRIATIONS (NON-ADD) | EQUIPMENT FROM OTHER APPROPRIATIONS (NON-ADD) | identical label; all five Camp Schwab buildings show $0 |

Net: the canonical face for Camp Schwab matches the AF exemplar architecture with three Marine Corps additions (LSH placement under Special Construction Features; the 6% Design line; the 4% CM line) and one Marine Corps deviation (DB Design timing - applied after Total Funded rather than before Total Request). Dollar values are preserved exactly. The architecture Rob requested ("Primary Facility(s), Supporting, Contingency and on down to Other Appropriations") is delivered.
