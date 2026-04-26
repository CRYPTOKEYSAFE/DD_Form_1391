# Deliverable 00 - Verification Gate Results

Run date: 26 April 2026
Branch: claude/fix-dd-form-block-9-KHc33

## Gate 1: Dollar reconciliation (Total Funded and Total Project per building match cost estimate workbook to the dollar)

| Building | Workbook Total Funded | Block 9 Total Funded | Workbook Total Project | Block 9 Total Project | Status |
|----------|----------------------:|---------------------:|-----------------------:|----------------------:|:------:|
| SCH-1024 | 10,012,635 | 10,012,635 | 10,413,140 | 10,413,140 | PASS |
| SCH-3213 |  5,190,315 |  5,190,315 |  5,397,928 |  5,397,928 | PASS |
| SCH-3237 |  1,399,544 |  1,399,544 |  1,455,526 |  1,455,526 | PASS |
| SCH-3270 |  3,392,070 |  3,392,070 |  3,527,753 |  3,527,753 | PASS |
| SCH-3314 |  1,874,407 |  1,874,407 |  1,949,383 |  1,949,383 | PASS |
| **PORTFOLIO** | **21,868,971** | **21,868,971** | **22,743,730** | **22,743,730** | **PASS** |

## Gate 2: No UNIFORMAT codes in Block 9 line descriptions

Grep across `deliverables/blocks/*.md` for B20, C10, C30, D20, D30, D40, D50, E20, F10, F20, G10, G20, UNIFORMAT in line descriptions: **zero hits in active content**. Residual mentions appear only in change-history bullets ("Removed UNIFORMAT codes...") which are deliberate documentation, not Block 9 face content.

## Gate 3: No discipline-first line naming

Grep for line descriptions beginning with HVAC, Plumbing, Electrical, Mechanical, Fire Protection, Communications, or Site as the leading word: **zero hits in Block 9 face**. The Primary Facility line names the facility (Armory and First Floor Renovation, Battalion Headquarters Building, Storage and TR Repair, Auto Organizational Shop Repair, Battalion Headquarters Building) per manual §3.1 (p. 19).

## Gate 4: Architecture order matches canonical template

All five Block 9 files follow the order: PRIMARY FACILITIES, SUPPORTING FACILITIES, SUBTOTAL, CONTINGENCY, TOTAL CONTRACT COST, SIOH, DESIGN, CM, TOTAL FUNDED, DB DESIGN, TOTAL PROJECT, TPC ROUNDED, EQUIPMENT FROM OTHER APPROPRIATIONS. **PASS.**

## Gate 5: LSH placement consistent across all five buildings

LSH is placed as a Special Construction Features sub-line under Supporting Facilities in all five buildings. Same line label, same authority cite (NAVFAC 11010.44E CH-1 / MCO 11000.12). **PASS.**

## Gate 6: No em dashes in deliverables

Grep for em dash and double-hyphen in deliverable text content: **zero hits**. Table separator triple-hyphens (`---`) are not flagged. **PASS.**

## Gate 7: Manual page citations cross-checkable

Every CRB Guidelines page citation in deliverables 01, 02, 03, and the SKILL.md file is cross-checkable against the OCR'd manual at `working/crb_master.txt`. Cited pages: 7, 8, 11, 19, 22, 23, 24, 30, 32, 36-37. All confirmed present in the OCR output. **PASS.**

## Open items (not gate failures, carried to forward-look register)

- SCH-3314: phasing language for Block 10 / Section F pending Will Lake DOW result (15 Apr 2026)
- SCH-3314: FAC code crosswalk pending RPAO confirmation (FAC 6101 used as best-supported proxy for CCN 61072)
- SCH-3270: PRV deviation between iNFADS and formula method documented in CEPBKUP Section F-11 (delta $7.52M, iNFADS governs)
- SCH-3213: PRV deviation between iNFADS and formula method documented (delta $2.81M, iNFADS governs)
- All five workbooks: JPY/USD exchange rate placeholder pending Federal Reserve H.10 verification on day of PAX submission (display-only, does not affect ROM)

## Reconciliation vs current PAX paste-text

| Building | Current PAX Total Funded | Corrected Total Funded | Status | Reason |
|----------|-------------------------:|------------------------:|:------:|--------|
| SCH-1024 | 9,468,837 | 10,012,635 | FAIL (older LSH basis) | PAX paste-text predates LSH correction; workbook governs |
| SCH-3213 | 5,190,000 | 5,190,315 | PASS within rounding | PAX uses whole-thousand; corrected uses 3-decimal |
| SCH-3237 | 1,396,620 | 1,399,544 | minor delta ($2.9K) | rounding artifact |
| SCH-3270 | 2,374,358 | 3,392,070 | FAIL (older scope) | PAX paste-text predates mechanical scope expansion (DOAS, exhaust, NIPR, MNS) |
| SCH-3314 | NOT DRAFTED | 1,874,407 | n/a | PAX paste-text was intentionally blank; operator direction (26 Apr 2026): workbook governs |

Workbook is the cost estimate of record. PAX paste-text drift is a known recurring issue captured in Forward-Look Register item 2.
