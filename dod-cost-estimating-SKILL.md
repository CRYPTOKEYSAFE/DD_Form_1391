---
name: dod-cost-estimating
description: >
  DoD/MILCON facility cost estimating skill per UFS 3-740-05 and UFC 3-701-01.
  Triggers for: cost estimate, ROM, DD 1391 Block 9, SIOH, ACF, escalation, LSH, PRV,
  contingency, program adders, "build me a cost estimate", "recalculate costs", or any
  reference to a building cost estimate (e.g., "1024 cost estimate", "3314 estimate").
  Also triggers for: DB-RFP scope reference, scope by discipline, FEAD package, scope table,
  Teams scope post, or any request to extract or organize scope from the five Camp Schwab
  buildings (SCH-1024, SCH-3213, SCH-3237, SCH-3270, SCH-3314).
  Also triggers for: JDDG, JED Cost Estimating Guide, JES, JEGS, radon, NAVRAMP,
  Okinawa climate scope, unit cost source hierarchy, or any Japan-specific estimating requirement.
  Always read this SKILL.md first then load reference files as needed.
  CRITICAL: All outputs must be factual and sourced from project files. No speculation,
  no inference, no values from memory. If unconfirmed, stop and say so before delivering.
---

# DoD Cost Estimating -- OMEGA APEX v26.0
# Updated: 03 April 2026 -- DRAWING REFERENCE PROTOCOL, ARCHIVE SEARCH METHODOLOGY, SCH-3213 FIRE ALARM CONFIRMED FACTS
#
# v26.0 ADDITIONS (03 Apr 2026):
# 1. G-43: DMS filename is never a drawing number. Before any drawing reference goes into a
#    client-facing deliverable, confirm the sheet number printed on the title block. Use the
#    sheet number in the message. DMS filenames (e.g., 11804, 11819) are local identifiers
#    that do not appear on the physical drawing and are meaningless to the recipient.
# 2. G-44: Archive sheet search protocol. Do not build full-set contact sheets at low resolution
#    to find a specific sheet. Instead: identify the approximate page range from a known adjacent
#    sheet, then extract targeted pages at 5x resolution directly. Contact sheets below 400px
#    cell height cannot reliably resolve Japanese sheet numbers.
# 3. G-45: Detector coverage claims require the fire alarm layout AND the scope drawing read
#    together in the same session. One without the other is insufficient to support a coverage
#    statement. Do not state "both sides have coverage" or similar without this cross-check.
# 4. G-46: "Site surveys" language requires a specific survey document on file with a confirmed
#    date, scope, and performing organization. No document on file means no mention in the
#    deliverable. This applies to all survey types: fire alarm, structural, environmental, MEP.
# 5. G-47: Device identifications not confirmed from a drawing this session must be attributed
#    to whoever described them. Never state a device type as confirmed fact if the identification
#    came from a colleague's message rather than a drawing read.
# 6. G-48: Factual claims carried forward from a prior session must be flagged as prior-session
#    sourced until re-verified in the current session. Flag format: "(prior session -- not
#    re-verified this session)". Remove flag only after direct drawing confirmation.
# 7. SCH-3213 fire alarm facts locked from 03 Apr 2026 drawing reads:
#    Sheet 20-20 (11804.tif) = スプリンクラー配管平面図 (Sprinkler Piping Plan). Circle symbols
#    in room interiors are sprinkler heads. Alarm valve detail shows ウォーターモータゴング
#    (Water Motor Gong) at FL+2600 -- sprinkler system component, not fire alarm.
#    Sheet 15-19 (11819.tif) = 自動火災報知設備配線図 (1st Floor Fire Alarm System Layout).
#    Sheet 14-19 (S2P1 page 12 of AsBuilt archive) = 自動火災報知設備系統図 (Fire Alarm System
#    Diagram). Legend confirmed: plain circle = Fixed Temperature Spot Type (定温式スポット型感知器)
#    1st class 75°C; circle with bar = Rate-of-Rise Detector Spot Type (差動式スポット型感知器)
#    2nd class; square = Optical Smoke Detector Spot Type (光電式煙感知器) 2nd class;
#    Fire Alarm Bell (火災警報ベル) DC24V 15mA φ150; Manual Fire Alarm Box = P-TYPE 1st CLASS.
#    System upgraded from bells to horn/strobes at unknown date after 1983 (per Robert Beller
#    message 03 Apr 2026 -- field condition, not drawing-confirmed).
# 8. SCH-3213 detector positions from Sheet 15-19 (03 Apr 2026 read):
#    Class Room No.2 (研修室No.2): 1 detector at corridor threshold near Y2 gridline.
#    Dehumid Storag No.1 (保管室No.1): NO dedicated interior detector. Corridor coverage only.
#    Spare and Tools Room (部品及び工事室): NO dedicated interior detector. Corridor coverage.
#    Admin No.1 (管理室No.1): 1 detector inside room.
#    Admin No.2 (管理室No.2): 1 detector inside room.
#    Crypto Room (解読室): 1 detector inside room.
#    Radio Testing Room (検査室): 1 detector inside room.
#    Maintenance Room (整備室): 6 detectors on loop (large bay).
# 9. FY26 Budget Rate for Japan Yen: 150.4415 JPY/USD (DoD FCF,D appropriation, FY26
#    President's Budget). This is the budget formulation rate, not the H.10 live rate.
#    PARAMETERS B33 still requires Federal Reserve H.10 pull within 30 days of submission.
# 10. New project files catalogued: FY26_Budget_Rates.pdf (DoD Foreign Currency Fluctuation
#     Rates, FY26 President's Budget rates table).
#
# Previous: v25.0 (27 March 2026) -- JAPAN DISTRICT INTEGRATION (JDDG v9, JED COST ESTIMATING GUIDE, RADON, OKINAWA SCOPE FRAMEWORK)
#
# v25.0 ADDITIONS (27 Mar 2026):
# 1. Japan District authority stack added: JDDG v9 (Apr 2025), JED Cost Estimating Guide (Nov 2025),
#    JES, JEGS. These are the mandatory local layer under UFC/UFS for all Japan District work.
# 2. JED Cost Estimating Guide (Nov 2025) catalogued as project file. 80 pages. Key sections:
#    01.8 (cost sources and pricing data), 01.13 (Excel restrictions for JED A-E work),
#    02.2.2 (exchange rate: budget vs local), 02.2.3 (Japan MLIT labor), 02.2.9.5 (metric UOM).
# 3. Unit cost source hierarchy established: Tier 1 = Japan-market databases (Sekisan Shiryo,
#    Kensetsu Bukka) and vendor quotes per JED 01.8; Tier 2 = RS Means/DoD Cost Book with ACF.
#    Current Camp Schwab ROMs use Tier 2; rationale documented.
# 4. Okinawa environmental and climate scope framework added: radon (JDDG 9.11.2, 19.11,
#    NAVRAMP), humid environment (JDDG 9.5.2, 12.17), corrosion-resistant materials, JEGS Ch.19.
# 5. Camp Schwab NAVRAMP RPC: unknown publicly. Default RPC 2 (Screening) per NAVRAMP guidebook.
#    PWD ENV confirmation required. Yellow flag. M67400-0004 is strictly UFS/UFC site code for ACF,
#    NOT a NAVRAMP RPC. These are separate designations from separate systems.
# 6. Radon evaluation mandatory intake question added (Q27). Conversion buildings (SCH-1024,
#    SCH-3213) almost certainly triggered due to occupancy change plus Okinawa radon history.
# 7. Section F Item 11 renovation vs. replacement narrative requirement added per JDDG 2.9.1.
# 8. Design phase mapping: Level 3 ROM maps to JDDG Programming/Parametric/Concept band.
# 9. Metric/SI documentation: JED requires metric UOM for assemblies (02.2.9.5); JDDG makes
#    metric default. Current ROMs use US customary (RS Means basis). FEAD converts downstream.
# 10. New guardrails G-37 through G-42 installed.
# 11. Current estimates do NOT carry corrosion-resistant envelope, radon, or JDDG-cited humid
#     environment scope. These are documented gaps, not errors in the current ROM products,
#     which were scoped before JDDG integration. FEAD engineers will address in DB-RFP design.
#
# Previous: v24.0 (27 March 2026) -- ARMORY BACKUP POWER FINDING, STALE PRODUCT GUARDRAIL, OCONUS UNIT COST REVIEW
#
# v24.0 ADDITIONS (27 Mar 2026):
# 1. G-35: Downstream deliverable stale flag -- when PRV methodology changes, all deliverables
#    containing PRV-derived ratios must be identified and rebuilt or flagged before further use.
#    Root: ERC infographic delivered 26 Mar shows SCH-3213 at 47.6% (AE Worksheet PRV basis).
#    v23.0 corrected PRV to formula method ($11,887,376). Correct ratio is 43.7%. Product is stale.
# 2. G-36: OCONUS unit cost review -- RS Means FY24 CONUS direct costs require review before
#    locking any unit cost where OCONUS execution conditions materially affect the price.
# 3. Armory backup power regulatory chain locked: no blanket generator mandate for Marine Corps
#    armories. Conditional on Installation CO determination. Active examples confirmed.
# 4. SCH-3213 open items added: overhead door unit cost review ($5,500/EA potentially understated),
#    workbench scope decision pending (potential $14,120 Base Direct addition).
# 5. ERC infographic stale notation added to ERC table.
#
# v23.0 CRITICAL CORRECTIONS (26 Mar 2026):
# ROOT CAUSE: All estimates except SCH-1024 used AE Worksheet "PRV at EOY" as "iNFADS confirmed."
# The AE Worksheet PRV is a snapshot frozen at the evaluation date. The Property Record "Current PRV"
# is the live system of record, recalculated by RPAO at EOY. These are different numbers from the
# same system. The skill never distinguished between them. This caused stale PRV values in four
# estimates, incorrect LSH, and an incorrect ERC threshold determination for SCH-3213.
#
# CORRECTIONS APPLIED:
# 1. All five current iNFADS Property Record PRVs locked from Anthony's direct pull (26 Mar 2026)
# 2. SCH-3213 reclassified as CONVERSION building (Field Maint Shop to CLB-4 BN HQ) -- formula method
# 3. SCH-3237 FAC 4421 GSF corrected to 19,304 SF per Property Record (19 Feb 2026)
# 4. ERC threshold analysis section added with full policy chain
# 5. New guardrails G-29 through G-33 installed
# 6. PRV Verification Protocol rewritten with Property Record vs AE Worksheet distinction
# 7. UFS 3-701-01 (2 Feb 2026) noted as superseding UFC 3-701-01 and all changes
#
# CONVERSION BUILDINGS: SCH-1024 and SCH-3213 both use formula PRV with post-conversion FAC codes.
# The DD 1391 programs what the building will be, not what it was. Property record PRV reflects the
# old use and does not govern for conversion projects.
#
# Previous: v23.0 (26 March 2026) -- PRV SOURCE HIERARCHY, ERC THRESHOLD ANALYSIS, CONVERSION BUILDING METHODOLOGY
# All five PAX backup files read cell-by-cell, value-by-value. Every formula, format, fill,
# font color, PARAMETERS row, Section F text, UNIFORMAT code, and locked financial value
# extracted directly from the gold standard files and committed to this skill.
# No value in this skill is from memory. All values sourced from the files as of 21-25 Mar 2026.
#
# GOLD STANDARD FILES (project directory, read 21-22 Mar 2026):
#   1024_G_CEPBKUP_BU26PPE70M_POM26_20260319.xlsx  -- SCH-1024 v11 (19 Mar 2026)
#   3213_G_CEPBKUP_BU26PPE72M_POM26_20260320.xlsx  -- SCH-3213 v6 (20 Mar 2026)
#   3237_G_CEPBKUP_BU26PPE73M_POM26_20260309.xlsx  -- SCH-3237 v4 (09 Mar 2026)
#   3270_G_CEPBKUP_BU26PPE74R_POM26_20260319.xlsx  -- SCH-3270 v9 (19 Mar 2026)
#   3314_G_CEPBKUP_BU26PPE71M_POM26_20260318.xlsx  -- SCH-3314 v3 (18 Mar 2026)
#
# Previous: v21.0 (23 March 2026) -- SCH-1024 mechanical deep dive and drawing inventory locked
# Previous: v20.0 (22 March 2026) -- DB-RFP SCOPE REFERENCE XLSX DELIVERABLES locked
# Previous: v19.0 (21 March 2026) -- all 5 CEPBKUP files locked at APEX OMEGA level
# Previous: v18.0 (20 March 2026) -- SCH-3314 v3 locked; delivery method corrected to DB
# PRV methodology: UFC 3-701-01 Equation 3-1 full formula enforced for ALL buildings (since v11)
# Formula error history: prior versions used Q×PUC×ACF only -- missing HF, PD, SIOH, CF -- corrected v11+
# Largest scope: SCH-3213 v6 (20 Mar 2026) -- 73 items / 11 groups / 6 UNIFORMAT codes
# Color standard: SCH-3270 v9 (19 Mar 2026) -- gold standard for all color/fill decisions
# Multi-FAC PRV architecture: SCH-1024 v11 (19 Mar 2026) -- 4-FAC formula method, 9 UNIFORMAT codes
# Section F language: SCH-3314 v3 (18 Mar 2026) -- F-1 through F-13 label format in col A
# Cosmetic reference: SCH-3270 v9 -- PRIMARY cosmetic gold standard for 4-column ESTIMATE layout
#
# v22.0 ADDITIONS (25 Mar 2026):
# SCH-3314 Block 10/11 audit against v3 estimate scope. Root cause: Block 10 FL1 paragraph
# described removing condensing units and evaporator coils from main floor spaces (not in scope).
# Block 10 FL2 paragraph described evaporator coil removal (not in scope -- carried from Decision
# Point 2 slide language predating the current estimate). Both corrected. Block 11 Current
# Situation paragraph was missing scope justification for diffusers, exhaust fans, and guard room
# ventilation. Addition drafted. New guardrail G-27 added: Block 10/11 language must be verified
# line-by-line against the current estimate SCOPE_DETAIL before any version is submitted.
# Language carried from decision slides or prior 1391 versions is a recurring error vector.
# Maximo WO 18843573 confirmed and locked for SCH-3314 AHU replacement (both units).
# SCH-3314 DMS drawing set (3314_Full_DMS_Drawings.pdf) confirmed as MC-124 package -- NOT 3314.
# HEU Floor 2 count remains open pending mechanical engineer (G-F) confirmation from drawing 111374.
# ACP exclusion basis reconfirmed from FMB refrigeration/A/C maintenance (Camp Schwab) communication.
# Ductless splits in duty/bunk rooms confirmed less than 5 years old (G-F FMB, 25 Mar 2026).
#
# v21.0 ADDITIONS (23 Mar 2026):
# SCH-1024 mechanical deep dive session. All 1024 source documents fully rasterized and read:
#   1024_Drawings.pdf (33 sheets, DMS legacy package -- full inventory below)
#   M67400HE1024AE_WORKSHEET.pdf (17 pages, iNFADS AE Worksheet, site visit 2/16/2023)
#   1024_HE_Plus.pdf (3 pages) + 1024_FL3and4_HE_Plus.pdf (1 page) -- Markon CUI floor plans
#   BUILDER SMS Final 4 Equipment Details Report (70 components, RPUID NFA100000443601, 7/6/2023)
# Mechanical condition report delivered: SCH1024_Mechanical_Condition_Report_MAR26.docx
# PRV delta ($90.1M iNFADS vs $96.5M formula) documented and explained -- mission partner briefed.
# New open scope gaps identified for 1024 estimate. See SCH-1024 section for full detail.
# CCN 44110 (867 SF) allocation gap identified -- not mapped to discrete FAC row in PARAMETERS.

---

## CRITICAL METHODOLOGY CORRECTION -- READ FIRST

### PRV Formula Error Corrected in This Version

All prior versions of this skill used an incomplete PRV formula:

  **WRONG (prior versions):** PRV = Q × PUC × ACF

  **CORRECT (this version):** PRV = Q × PUC × ACF × HF × PD × SIOH × CF

This is UFC 3-701-01 Equation 3-1. The four missing multipliers are not optional.
The error was discovered during cross-building audit on 10 March 2026.

**Impact by building:**
- 3270: iNFADS governs. LSH correct. No change.
- 3213: iNFADS governs. LSH correct. No change.
- 3237: iNFADS governs. LSH correct. Narrative cross-check needed correction only.
- 1024: FORMULA method. LSH understated by $460,845. MUST BE CORRECTED.
- 3314: Not yet drafted. Must use full Eq 3-1 if formula method required.

**Rule:** Any building using formula PRV (no confirmed iNFADS value) MUST apply all
seven factors of Equation 3-1. There are no exceptions. The cross-check table in
Section F Item 11 must also reflect the full equation when cited.

---

## PERMANENT GUARDRAILS -- Lessons Locked From Build History (v12)

These errors have occurred in prior builds and are now permanently prohibited.
Every rule below has a root cause. Read them before touching any workbook.

### G-1: Sub-PRV rows NEVER include ACF

**Root cause:** SCH-1024 v8/v9 coded each FAC sub-PRV as `GSF × PUC × ACF`.
This applied ACF at the sub-PRV level, which meant the full Eq 3-1 combined factor
was then effectively applied to an already-ACF-inflated base, OR ACF was double-counted.

**Rule:** Sub-PRV rows = `GSF × PUC` only. No other factor.
ACF and HF/PD/SIOH/CF are applied ONCE to the summed total, in the Total PRV row.
Formula: `Total PRV = (Σ GSF_i × PUC_i) × ACF × HF × PD × SIOH × CF`

---

### G-2: "Table 3" is PUC source only -- NEVER cite it as LSH authority

**Root cause:** Multiple prior Section F Item 7 narratives cited "UFC 3-701-01 Table 3" as
the LSH authority. Table 3 contains Plant Unit Costs (PUCs). It has nothing to do with LSH.

**LSH authority citations (use all three):**
- UFC 3-701-01 w/Change 7 (25 Jul 2025), **Equation 3-1** -- PRV formula authority
- NAVFAC 11010.44E CH-1 -- LSH rate (2.5%) authority
- MCO 11000.12 (08 Sep 2014) -- Marine Corps LSH program requirement

**PUC authority citation (use this for scope unit costs and PRV cross-check):**
- UFC 3-701-01 w/Change 7 (25 Jul 2025), **Table 3** -- PUC authority only

Never cite Table 3 in the LSH context. Never omit MCO 11000.12 from LSH citations.

---

### G-3: 10 U.S.C. § 2802 belongs in Classification of Work only

**Root cause:** Prior Item 3 (ACF) narratives appended "per 10 U.S.C. § 2802" to the ACF
citation. That statute is the MILCON project authorization authority. It does not govern
ACF selection, PRV calculation, or any cost methodology element.

**Rule:** Cite 10 U.S.C. § 2802 ONLY in the Classification of Work section (DD1391_BLOCK9)
where it governs the Construction classification line. Remove it from ACF, scope, and
methodology citations in Section F and ESTIMATE column C.

---

### G-4: UFC 3-730-01 always includes year "(2024)"

**Root cause:** Prior Section F Item 8 entries cited "UFC 3-730-01" without the year.
The (2024) edition is the current governing document for DB Design 4%.

**Rule:** Always cite as "UFC 3-730-01 (2024)". No exceptions.

---

### G-5: Section F must have EXACTLY 13 items -- Item 13 is Version History

**Root cause:** Multiple prior workbooks were delivered with 12 Section F items.
The pre-delivery checklist required 13, but the version history item was omitted.

**Item 13 is mandatory.** Its text: reference the version history in Section E, state the
current version row uses a live =B18 formula, and note the version count or date range.

**Rule:** Run the Section F item count check BEFORE delivery. `count == 13` is a hard gate.
A workbook with 12 Section F items fails the pre-delivery checklist. Do not deliver.

---

### G-6: Z10 scan covers ALL 4 tabs -- not ESTIMATE only

**Root cause:** In SCH-1024 v10, "Z10" was cleared from ESTIMATE and PARAMETERS during build
but remained in DD1391_BLOCK9 C16 note text ("Z10-applied subtotal"). Only found on final scan.

**Rule:** Z10 scan = all four tabs (ESTIMATE, SCOPE_DETAIL, PARAMETERS, DD1391_BLOCK9),
all columns. Zero occurrences required. "General Requirements" is the correct term everywhere.

---

### G-7: Property patching sequence is LOCKED -- see G-13 for full expanded sequence

**Root cause:** In SCH-1024 v10 build, recalc.py was run first (all values calculated),
then openpyxl properties were set and saved, which cleared all calculated values.

**Rule:** See G-13 for the complete 8-step build sequence. G-13 supersedes and extends G-7.
The core prohibition remains: never run recalc.py before app.xml is patched.
Never re-save with openpyxl after recalc. If any fix is needed after recalc:
re-open, fix, save, re-patch app.xml, re-run recalc, re-run G-13 XML patch, re-verify.

---

### G-8: Arial and Cambria in styles.xml are pre-existing residuals -- not a build defect

**Root cause:** openpyxl preserves all font definitions from the source file in styles.xml
even if those fonts are not applied to any active cells. Uploading from a workbook that
previously had Arial or Cambria formatting will leave those entries in the style table.

**Rule:** The delivery standard is that all ACTIVE CELLS use Calibri only.
Residual unused font entries in styles.xml from the source file are acceptable.
The check is: no cell-level font other than Calibri. Not: no font name other than Calibri
anywhere in styles.xml. Document this distinction in pre-delivery notes if it appears.

---

### G-9: Combined factor (1.23606) must appear as a dedicated named row in PARAMETERS

**Root cause:** Prior formula-method workbooks computed Total PRV in a single dense formula
without surfacing the combined factor. This made the Section F Item 11 narrative impossible
to verify by inspection and obscured the Equation 3-1 chain.

**Rule:** For any formula-method building, PARAMETERS must have:
- Individual rows for HF, PD, SIOH (Eq 3-1), CF -- each labeled, each with authority citation
- One combined factor row: `=HF × PD × SIOH × CF` with label "Combined Factor (HF×PD×SIOH×CF)"
- The combined factor drives the Total PRV formula: `=(Σ sub-PRVs) × ACF × combined_factor_cell`
This architecture makes every Equation 3-1 factor independently auditable. Use SCH-1024 v10
PARAMETERS rows 52-56 as the reference architecture.

---

### G-10: When CCN has no Table 3 PUC entry, document proxy selection explicitly in Section F

**Root cause:** SCH-3314 intake revealed that CCN 61072 (Battalion Squadron HQ) exists in
UFC 3-701-01 Table 2 as FAC 6189 (Squadron/Battalion HQ Mid Level, 24,000 SF ref, $575/SF)
but FAC 6189 has no Table 3 entry -- no published PUC. The correct proxy (FAC 6101, Small Unit
HQ, $634/SF, 44,000 SF ref) was selected based on building function and scale, not the larger
FAC 6102 (Large Unit HQ, $473/SF, 69,000 SF ref) which matched the wrong echelon.

**Rule:** When a building's CCN does not have a direct FAC-to-Table 3 PUC mapping:
1. Check Table 2 for the closest functional description and its FAC code.
2. Verify whether that FAC code has a Table 3 entry. If not, it cannot be used.
3. Select the nearest Table 3 FAC by: (a) functional description match, (b) reference size
   closest to the building's actual GSF. Err toward the smaller reference size when in doubt.
4. Document in Section F Item 11: "CCN [X] (description) has no direct Table 3 PUC entry in
   UFC 3-701-01 C7. FAC [Y] (description, $X/SF) applied as best-supported proxy pending formal
   RPAO/iNFADS FAC crosswalk confirmation."
5. If iNFADS PRV is available, it governs regardless -- proxy selection only affects the
   Section F cross-check narrative, not the LSH calculation.

**Never use FAC 6102 for a battalion-scale building.** FAC 6102 reference size is 69,000 SF
(Brigade/Division HQ). A 28,699 SF battalion building is demonstrably not that echelon.

---

### G-11: Tab header format is strictly prescribed -- all 4 tabs, every build

**Root cause:** SCH-3314 v1-v2 was delivered with headers missing LEVEL 3 and PAX ID on
three of the four tabs. Multiple rework cycles resulted. The correct format was already
established in SCH-1024 v10 but was not locked as a rule.

**Required header text by tab (pipe separators: two spaces, pipe, two spaces):**

| Tab | Header format |
|-----|--------------|
| ESTIMATE | `SCH-XXXX  |  ROM COST ESTIMATE  |  LEVEL 3  |  FY27  |  PAX ID XXXXXX  |  Fi Web XXXXXXX` |
| SCOPE_DETAIL | `SCH-XXXX  |  SCOPE DETAIL & QUANTITY TAKEOFF  |  BASE YEAR FY24 CONUS DIRECT COSTS  |  Fi Web XXXXXXX` |
| PARAMETERS | `SCH-XXXX  |  COST ESTIMATE PARAMETERS  |  LEVEL 3 ROM  |  FY27  |  PAX ID XXXXXX  |  Fi Web XXXXXXX` |
| DD1391_BLOCK9 | `SCH-XXXX  |  COST ESTIMATE PARAMETERS  |  LEVEL 3 ROM  |  FY27  |  PAX ID XXXXXX  |  Fi Web XXXXXXX` |

Notes:
- SCOPE_DETAIL intentionally omits PAX ID and FY. Match SCH-1024 v10 exactly on this tab.
- DD1391_BLOCK9 uses the PARAMETERS header format, NOT "DD FORM 1391 BLOCK 9" format.
- Separator is always "  |  " (two spaces, pipe, two spaces). No dashes. No em dashes.
- Header row is always dark navy (FF1B2A4A), white bold 12pt Calibri, merged across all columns, height 19.5pt (18pt on SCOPE_DETAIL row 1).
- Pre-delivery check: open data_only=True and verify ws.cell(1,1).value on all 4 tabs before delivering.

---

### G-12: SCOPE_DETAIL tab has NO freeze pane

**Root cause:** SCH-3314 v1-v2 had a freeze pane set at A4 on SCOPE_DETAIL. When the file
opened, Excel scrolled to the saved active cell (row 13), hiding rows 4-12 above the viewport.
All seven section headers and data rows 5-11 appeared to be missing from the top of the sheet.
SCH-1024 v10 SCOPE_DETAIL has no freeze pane -- it was never set on this tab.

**Rule:** SCOPE_DETAIL must have NO freeze pane. Remove any pane element from sheetView
on sheet2.xml before delivery. ESTIMATE, PARAMETERS, and DD1391_BLOCK9 freeze at A2.
Confirm post-patch with: `pane = root.find(f'.//{ns}pane')` must return None on SCOPE_DETAIL.

---

### G-13: Post-recalc XML patch is mandatory -- LibreOffice corrupts boolean attributes

**Root cause:** LibreOffice recalc.py saves boolean XML attributes as the string "true" instead
of the integer "1". Excel and some viewers silently ignore "true" for wrapText, so column C
text displays as a single non-wrapping line regardless of row height. This was the root cause
of the SCOPE_DETAIL text overflow. The same corruption affects customHeight, customWidth,
and the absence of dyDescent -- all of which affect row and column rendering.

**Mandatory post-recalc patch -- run this on all worksheets after every recalc.py call:**

```python
import zipfile, lxml.etree as ET

ns = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
nsAC = 'http://schemas.microsoft.com/office/spreadsheetml/2009/9/ac'

# 1. Fix styles.xml: wrapText="true" -> "1", applyAlignment="true" -> "1"
# 2. Fix each worksheet XML:
#    - Every row: customHeight="true" -> "1", add dyDescent="0.25"
#    - Remove extraneous row attributes (customFormat, hidden, outlineLevel, collapsed)
#    - Every col: customWidth="true" -> "1"
#    - sheetFormatPr: add dyDescent="0.25", remove zeroHeight/outlineLevelRow/outlineLevelCol
#    - SCOPE_DETAIL: remove pane element entirely
#    - All other tabs: set correct freeze pane (A2) if not already set
```

**The correct boolean token in OOXML for on/off attributes is "1" (not "true").**
The correct dyDescent value is "0.25" matching SCH-1024 v10 (Excel 2016+ default).

**Locked build sequence (replaces G-7):**
```
1. Build all tabs (openpyxl)
2. Set openpyxl properties (creator, lastModifiedBy, title) -- BEFORE save
3. Save with wb.save()
4. Patch docProps/app.xml (Company, Manager) via zip/lxml
5. Run recalc.py (90-second timeout minimum)
6. Run post-recalc XML patch (G-13 patch script above)
7. Verify: zero None values, wrapText all "1", no "true" booleans, freeze panes correct
8. Deliver
```

Step 6 is new and mandatory. Never deliver without running it.

---

### G-14: Separator discipline -- "  |  " everywhere, zero dashes

**Root cause:** SCH-3314 v2 section headers and legend text used " - " and " -- " as
separators in multiple places. Both are prohibited. The standard separator across all
headers, labels, and inline text is "  |  " (two spaces, pipe, two spaces).

**Rule:**
- Header titles: always "  |  " between segments
- SCOPE_DETAIL legend row 2: always "  |  " between color key entries
- Section headers within tabs: no dashes of any kind
- No em dashes (--) anywhere in any cell in any tab
- Pre-delivery: grep all cell values across all 4 tabs for " -- " and "\u2014". Zero hits required.

---

### G-15: When inserting rows and renumbering, ALL merge cell references must be updated

**Root cause:** SCH-3314 v3 build inserted a new version history row by shifting existing rows
up. Row 38 was the old Section F header, which carried a `<mergeCell ref="A38:C38"/>` spanning
all three columns. After the shift, the new v3 version history row landed at row 38 and inherited
that full-row merge. Columns B and C were absorbed into column A, so the Total Funded value and
Date/Notes text appeared blank in Excel even though the cell data was correct.

**Rule:** Any time rows are renumbered or new rows are inserted:
1. Extract ALL `<mergeCell ref="..."/>` entries before the operation.
2. After renumbering, update every merge ref that references a shifted row number.
3. Explicitly verify that no version history row (or any data row) has a full-span merge
   (e.g., `A38:C38`) that would collapse B and C.
4. Pre-delivery merge audit: parse `<mergeCells>` and confirm that no content row has a
   merge spanning columns A through C unless it is intentionally a section header.

---

### G-16: Version history B column values must always be hardcoded -- never a formula

**Root cause:** SCH-3314 v3 version history row B38 was built with `=B18` (live formula
referencing Total Funded). In some Excel environments this renders blank, particularly when the
row is freshly inserted or the file opens with calculation set to manual. v1 and v2 version rows
both use hardcoded values. The live formula provides no benefit -- the version history is a
historical record, not a live tracker.

**Rule:** Version history B column (Total Funded) must always be a hardcoded integer value.
No formulas. No cross-sheet references. Copy the ROUND()-computed Total Funded value at time of
build and write it as a literal number. This is consistent with v1 and v2 practice and eliminates
any rendering dependency on recalculation state.

---

### G-17: styles.xml Arial font entries must be patched to Calibri -- even if flagged as residual

**Root cause:** SCH-3314 v3 inherited Arial font definitions (fontId 1, 2, 3) from the source
file. Initial G-8 interpretation was that these were residual unused entries -- acceptable per
G-8. However, verification showed the Arial fontIds were actively referenced by xf elements in
cellXfs, meaning active cells were assigned Arial. Excel rendered them as Calibri due to font
substitution, but this is not reliable across all environments.

**Rule:** After every build, scan `<cellXfs>` in styles.xml. For each `<xf>` that references a
fontId, verify that fontId resolves to Calibri. If any active xf points to Arial (or any
non-Calibri font), patch the `<name val="Arial"/>` entry in the font table to `<name val="Calibri"/>`.
The G-8 residual exception applies only to font entries that are NOT referenced by any active xf.
Verification command:
```python
fonts = re.findall(r'<font>(.*?)</font>', styles, re.DOTALL)
arial_ids = [i for i, f in enumerate(fonts) if 'Arial' in f]
active_refs = re.findall(r'<xf[^>]*fontId="(\d+)"', styles)
active_arial = [r for r in active_refs if int(r) in arial_ids]
assert not active_arial, f"Active Arial fontIds: {active_arial}"
```

---

### G-18: "APEX OMEGA" must never appear in any workbook cell

**Root cause:** Every version history row, Section F narrative, and Prepared By line in SCH-3314 v1 through v3 contained the label "APEX OMEGA" (e.g., "v3 APEX OMEGA (18 Mar 2026) - CURRENT"). APEX OMEGA is an internal skill designation. It is not a customer-facing version label and has no meaning to a reviewer, RPAO, or PAX system operator.

**Rule:** Version references in all customer-facing cells use only the version number and date: "v1 (16 Mar 2026)", "v2 (16 Mar 2026)", "v3 (18 Mar 2026) - CURRENT". No "APEX OMEGA" in any cell in any tab. Pre-delivery scan: grep sharedStrings.xml for "APEX OMEGA" -- zero hits required.

---

### G-19: Delivery method for all five Camp Schwab buildings is Design-Build (DB)

**Root cause:** SCH-3314 PARAMETERS had delivery method recorded as "Design-Bid-Build (DBB)" through v3. All five Camp Schwab DPRI consolidation buildings use Design-Build delivery to FEAD. This must be consistent with Block 11 text in the DD Form 1391.

**Rule:** PARAMETERS delivery method cell must read "Design-Build (DB)" for all five buildings. Never "DBB". Never "Design-Bid-Build". Verify PARAMETERS delivery method matches the DD Form 1391 Block 11 delivery method statement before every submission.

---

### G-20: Block 9 adder formulas must be re-verified after every scope addition or row insertion

**Root cause:** SCH-3314 v3 added Group 8 (5 new scope items), which pushed the SUBTOTAL row from B11 to B15 in DD1391_BLOCK9. The Contingency formula was not updated and continued to reference B13 (the last scope item row) instead of B15 (SUBTOTAL). Every adder row below it cascaded stale values. This was not caught until verification against expected math.

**Rule:** After any scope addition or row insertion that shifts DD1391_BLOCK9 row numbers:
1. Identify the new SUBTOTAL row number.
2. Verify Contingency formula references that exact SUBTOTAL row -- not the last scope item row.
3. Verify all adder rows (Design, SIOH, CM) reference the correct ESTIMATE cross-sheet cells.
4. Verify TOTAL FUNDED and TOTAL PROJECT cached values match independently computed expected values.
5. Run the full Block 9 verification table (all rows, expected vs actual, tolerance < $0.50K) before delivery.

---

### G-21: Yellow flags are for genuinely unconfirmed items only -- never for confirmed scope

**Root cause:** SCH-3314 v3 Item 21 (mechanical room overhaul) was yellow-flagged with language "pending mechanical engineer field confirmation." The scope was confirmed by Anthony from drawings and site. Flagging confirmed scope wastes reviewer attention, implies doubt where none exists, and creates unnecessary back-and-forth.

**Rule:** A yellow flag means one thing: the quantity, unit cost, or scope description cannot be confirmed from available drawings, site data, or client input and requires future verification before submission. If the client has confirmed the scope -- verbally, via email, or from drawings -- it is not yellow. When in doubt, ask before flagging. Do not flag preemptively.

---

### G-22: JPY is the only yellow item in a complete estimate

**Root cause:** As the portfolio matured, yellow flags were reduced one by one as scope was confirmed. The only item that is ALWAYS yellow in a complete estimate is the JPY/USD exchange rate in PARAMETERS, because it must be confirmed from Federal Reserve H.10 on the actual date of PAX submission. All other items must be confirmed before the estimate is considered ready to deliver. An estimate with yellow flags beyond JPY is not complete.

**Rule:** A complete, submission-ready estimate has exactly one yellow item: the JPY rate in PARAMETERS. If any scope item, quantity, or unit cost remains yellow at delivery, the estimate is not complete. State this explicitly in Section F Item 10. The JPY cell must have yellow fill and a note: "Confirm from Federal Reserve H.10 on date of PAX submission."

---

### G-23: SCOPE_DETAIL grand total must sum subtotal rows only -- not the full item range

**Root cause:** SCH-3270 v9 build initially used =SUM(G4:G65) for the grand total row. This range included both item rows (D*F formulas) AND subtotal rows (SUM of item ranges), causing double-counting. Base Direct appeared as $1,584,000 instead of $792,000. The error was caught during data_only verification after recalc.

**Rule:** The SCOPE_DETAIL grand total formula must sum ONLY the group subtotal rows -- never a contiguous range that spans both item rows and subtotal rows. Correct pattern:
```
Grand Total = =G{sub1}+G{sub2}+G{sub3}+...+G{subN}
```
where each G{subN} is a group subtotal row containing =SUM(G{first_item}:G{last_item}).

**Verification:** After recalc, load data_only=True and confirm SCOPE_DETAIL grand total = ESTIMATE Base Direct. If they differ, the grand total formula is wrong. Fix before delivery -- never deliver with a Base Direct mismatch.

---

### G-24: LSH must be hardcoded as an integer -- never =PRV x LSH Rate in PARAMETERS

**Root cause:** SCH-3270 v9 PARAMETERS B34 was initially coded as =B33*B23 (PRV $39,507,617 x 0.025 = $987,690.425). The .425 cents propagated into the Construction Base and caused Total Funded to round to $3,392,071 instead of $3,392,070 -- a $1 difference that failed the pre-delivery check.

**Rule:** LSH in PARAMETERS must always be a hardcoded integer dollar value confirmed at build time. Never a live formula referencing PRV and LSH rate. The correct value for SCH-3270 is $987,690 (not $987,690.425). Document the confirmed integer in Section F Item 7 and in PARAMETERS notes. The ESTIMATE LSH row pulls from this hardcoded cell via cross-sheet reference.

---

## PRV VERIFICATION PROTOCOL -- MANDATORY FOR EVERY BUILDING, EVERY TIME

This protocol runs at three points: intake, pre-build, and pre-delivery.
Never skip any step. Never carry forward from a previous building without repeating it.

### Step PRV-1: Determine PRV Method

For each building, answer TWO questions:

**Question 1: Is this a conversion building?**
Compare the Property Record FAC codes against the facility type the DD 1391 programs.
If they match: NON-CONVERSION. Proceed to Question 2.
If they differ: CONVERSION. Skip to PRV-3 (formula method with post-conversion FAC codes).

**Question 2 (non-conversion only): Is a current Property Record PRV available?**
Pull the "Current PRV" from the iNFADS Property Record (NOT the AE Worksheet).
Record the pull date. The pull must be within 30 days of submission.

YES, current Property Record PRV available → Use it. Proceed to PRV-2.
NO, or Property Record appears stale/zero → Use formula method. Proceed to PRV-3.

If uncertain about either question: stop. Verify with RPAO before proceeding. Never assume.

### Step PRV-2: Property Record Method (Non-Conversion Buildings)

1. Record the Property Record "Current PRV" value, RPUID, and pull date.
2. Calculate LSH = Property Record PRV x 0.025. Round to nearest dollar (hardcode per G-24).
3. Calculate formula PRV for cross-check reference ONLY (use full Eq 3-1 per PRV-3).
4. Document all three values in Section F Item 11:
   a. Property Record Current PRV (governing value, with RPUID and pull date)
   b. AE Worksheet PRV at EOY (reference only, with evaluation date)
   c. Formula PRV cross-check (with FAC codes, PUCs, and full Eq 3-1 factors)
5. Document the delta between Property Record and formula PRV with explanation.
6. LSH in estimate = Property Record-based value. Formula cross-check does not change it.
7. Compute ERC ratio = Total Funded / Property Record PRV. Document per G-32.

### Step PRV-3: Formula Method (Conversion Buildings or No Property Record)

**Trigger:** Building is a conversion (DD 1391 FAC differs from Property Record FAC)
OR no current Property Record PRV is available.

Apply UFS 3-701-01 Equation 3-1 in full. All seven factors. No exceptions.
Use POST-CONVERSION FAC codes for conversion buildings.

```
PRV = Q x PUC x ACF x HF x PD x SIOH x CF

Where:
  Q    = Building GSF per FAC code (from Property Record total, allocated to post-conversion FACs)
  PUC  = Unit cost from UFS 3-701-01 Table 3 (current edition only)
  ACF  = Area Cost Factor from UFS 3-701-01 Table 4-1 (site-specific)
  HF   = Historical Factor (1.0 if not on NRHP; confirm per RPAO)
  PD   = Productivity Differential (1.09 non-medical)
  SIOH = Supervision, Inspection and Overhead (1.08)
  CF   = Contractor Factor (1.05)
```

**Camp Schwab confirmed values (M67400-0004, non-medical, non-historical):**

| Factor | Value | Authority |
|--------|-------|-----------|
| ACF    | 1.85  | UFS 3-701-01, Table 4-1, OCONUS, M67400-0004 |
| HF     | 1.0   | Non-historical; buildings not on NRHP |
| PD     | 1.09  | Non-medical, UFS 3-701-01 |
| SIOH   | 1.08  | UFS 3-701-01 |
| CF     | 1.05  | UFS 3-701-01 |
| **Combined (HF x PD x SIOH x CF)** | **1.23606** | Product of above four |

**For multi-FAC buildings:** Calculate each FAC sub-PRV independently (GSF_i x PUC_i),
sum all sub-PRVs to get Q x PUC, then apply ACF x HF x PD x SIOH x CF to the total.
Never blend PUCs across FAC codes. Never apply multipliers to only some FACs.

```
Total PRV = (SUM GSF_i x PUC_i) x ACF x HF x PD x SIOH x CF
LSH       = Total PRV x 0.025
```

**For conversion buildings, document in Section F Item 11:**
a. Post-conversion FAC codes with GSF allocation and PUC for each
b. Formula PRV result (governing value)
c. Property Record Current PRV (reference, with RPUID, pull date, and pre-conversion FACs)
d. AE Worksheet PRV at EOY (reference, with evaluation date)
e. Explanation: "Property Record reflects pre-conversion facility type [X]. DD 1391
   programs post-conversion facility type [Y]. Formula PRV governs per G-30."
f. ERC ratio = Total Funded / Formula PRV. Document per G-32.

### Step PRV-4: Pre-Delivery PRV Verification Checklist

Run this for EVERY building before delivery. Check all boxes.

**All buildings (regardless of method):**
- [ ] PRV pull date recorded and within 30 days of submission
- [ ] Property Record Current PRV recorded (even for conversion buildings, as reference)
- [ ] AE Worksheet PRV recorded as reference with evaluation date
- [ ] Conversion test completed (G-30): Property Record FAC vs DD 1391 facility type
- [ ] ERC ratio computed (G-32): Total Funded / governing PRV
- [ ] ERC ratio documented in Section F Item 11
- [ ] If ERC ratio > 40%: flagged as MONITORING
- [ ] If ERC ratio > 50%: flagged as ERC TRIGGERED, FEAD coordination documented
- [ ] Section F Item 11 lists all three PRV values with sources and dates

**Non-conversion buildings (Property Record method):**
- [ ] Property Record Current PRV confirmed with RPUID and pull date
- [ ] LSH = Property Record PRV x 0.025 (hardcoded integer per G-24)
- [ ] Formula cross-check calculated using FULL Eq 3-1 (all 7 factors)
- [ ] Delta between Property Record and formula documented with explanation
- [ ] PUCs in cross-check read directly from UFS 3-701-01 Table 3 (not memory)

**Conversion buildings (Formula method):**
- [ ] Post-conversion FAC codes confirmed and documented
- [ ] FAC proxy selection documented per G-10 if applicable
- [ ] All 7 Equation 3-1 factors confirmed and documented
- [ ] HF, PD, SIOH, CF individually listed in PARAMETERS tab
- [ ] Sub-PRVs calculated independently before combined factor applied
- [ ] Combined factor (1.23606) stated in Section F Item 7
- [ ] Total PRV verified by independent hand calculation before entry
- [ ] LSH verified by independent hand calculation (Total PRV x 0.025)
- [ ] Section F Item 11 states "formula method" and identifies building as conversion
- [ ] Property Record PRV documented as reference (not governing)

---

## ERC THRESHOLD ANALYSIS -- CAMP SCHWAB PORTFOLIO (26 Mar 2026)

### Policy Chain (all confirmed from primary sources)

| Authority | Threshold | Citation |
|-----------|-----------|----------|
| UFC 4-010-01 | AT/FP mandatory when renovation cost >50% of replacement cost per UFC 3-701-01 | Para 1-6.2.1 |
| UFC 1-200-02 | HPSB/sustainability for renovation >=10,000 GSF, >$3M, >=50% ERC | Table 1-1, Change 03 (08 Jul 2025) |
| BULLETIN 3302 | "Renovations of more than 50 percent Plant Replacement Cost (PRC) will require AT Standoff for Explosive Weight II" | Para 4.a.(2)(f).3, MCIPAC-MCBBBul 3302, 9 Sep 2022 |
| JDDG v9 | References ">=50% ERC" in modified sustainability thresholds table. Defers to UFC framework. | April 2025 (current version) |
| UFC 3-701-01 Ch.5 | Replacement cost is "distinctly different from the PRV calculation defined in Chapter 3" | Section 5-1.1 |

**Replacement Cost vs PRV:** UFC 4-010-01 uses "replacement cost" as the denominator. PRV
(Equation 3-1) is a conservative proxy because it is typically lower than facility-specific
replacement cost (per UFC 3-730-01), making the ratio higher (more likely to trigger). Using
PRV as the denominator is the more conservative approach. Document the proxy use in Section F.

**Separate trigger: occupancy reclassification.** Conversion from low-occupancy to inhabited
use triggers AT/FP compliance regardless of cost ratio (UFC 4-010-01). Evaluate SCH-1024
and SCH-3213 for this trigger independently.

**BULLETIN 3302 supersedes MCIPAC Policy Letter 3-19.** Signed CG MCIPAC-MCB Camp Butler,
9 Sep 2022. Full text reviewed. Enhanced MGB/SOB standoff requirements are discretionary
for renovations unless they cross the 50% PRC line (Para 6.a). SOB designation (50-199
occupants) requires written request to MCIPAC-MCBB Director of Installation Protection.

### Current ERC Ratios (locked 26 Mar 2026, corrected per v23.0)

| Building | Total Funded | PRV (governing) | PRV Method | ERC Ratio | Status |
|----------|-------------|-----------------|------------|-----------|--------|
| SCH-1024 | $10,012,635 | $96,523,347 | Formula (post-conversion) | 10.4% | CLEAR |
| SCH-3213 | $5,190,315 | $11,887,376 | Formula (2-FAC, partial conversion) | 43.7% | MONITORING |
| SCH-3237 | $1,399,544 | $27,656,160 | Property Record | 5.1% | CLEAR |
| SCH-3270 | $3,392,070 | $45,526,139 | Property Record | 7.5% | CLEAR |
| SCH-3314 | $1,874,407 | $29,826,797 | Property Record | 6.3% | CLEAR |

No building exceeds 50%. SCH-3213 is in MONITORING range at 43.7%.
Headroom to 50% trigger: $5,943,688 (50% of $11,887,376) minus $5,190,315 = $753,373.
+30% scenario: $5,190,315 x 1.3 = $6,747,410 / $11,887,376 = 56.8%. Breaches 50%.
SCH-3213 is ERC SENSITIVE per G-32. Every scope addition must be evaluated for ERC impact.

**STALE PRODUCT WARNING (per G-35):** The delivered ERC infographic
(ERC_Threshold_Analysis_Camp_Schwab_26MAR2026.html and .pdf) shows SCH-3213 at 47.6%.
That figure used the AE Worksheet PRV of $10,893,334 and predates the v23.0 formula PRV
correction. The correct ratio is 43.7% (formula PRV $11,887,376). Both files must be
rebuilt before further distribution. Do not use the current HTML or PDF for any submission
or briefing without first updating them to reflect 43.7%.

### Current iNFADS Property Record PRVs (Anthony's direct pull, 26 Mar 2026)

| Building | Property Record PRV | RPUID | AE Worksheet PRV | Delta | Notes |
|----------|-------------------|-------|-----------------|-------|-------|
| SCH-1024 | $72,207,194 | 148675 | $90,145,407 | ($17,938,213) | Pre-conversion FACs. Formula governs. |
| SCH-3213 | $9,929,006 | 48879 | $10,893,334 | ($964,328) | Pre-conversion FAC 2171. Formula governs. |
| SCH-3237 | $27,656,160 | 51473 | $26,636,215 | +$1,019,945 | Property Record governs. |
| SCH-3270 | $45,526,139 | 1174058 | $39,507,617 | +$6,018,522 | Property Record governs. |
| SCH-3314 | $29,826,797 | 50931 | $29,826,797 | $0 | Property Record governs. Unchanged. |

### Formula PRV Computations (Conversion Buildings)

**SCH-1024 (Armory/BEQ Conversion, 4 post-conversion FAC codes):**
FAC 7210: 66,151 SF x $480/SF = $31,752,480
FAC 4421: 8,802 SF x $692/SF = $6,090,984
FAC 6102: 2,766 SF x $473/SF = $1,308,318
FAC 4427: 7,142 SF x $428.28/SF = $3,058,776
Q x PUC Total: $42,210,558 x ACF 1.85 x Combined 1.23606 = **$96,523,347**
LSH: $96,523,347 x 2.5% = **$2,413,084**

**SCH-3213 (CLB-4 BN HQ Partial Conversion, 2-FAC per G-34):**
Source: Property Record utilization breakdown (18 Feb 2026, RPUID 48879)
HQ side (FAC 6101): 5,148 SF x $634/SF = $3,263,832
Bay side (FAC 2171): 8,336 SF x $232.17/SF = $1,935,369
Q x PUC Total: $5,199,201 x ACF 1.85 x Combined 1.23606 = **$11,887,376**
LSH: $11,887,376 x 2.5% = **$297,184**
FAC basis: HQ side converts to BN HQ (renovation installs offices, vaults, SIPR, HVAC).
Bay side retains physical maintenance bay characteristics (roll-up doors inspected/repaired,
structural spans and slab unchanged). Post-conversion mission does not change the replacement
cost of the bay. FAC 2171 PUC applies per G-34. See G-10 for FAC 6101 proxy selection.

---

## Japan District Authority Integration -- JDDG v9 and JED Cost Estimating Guide

### Authority Hierarchy for Japan District Work

For all projects executed through USACE Japan Engineer District (JED), including MCIPAC G-F
FSRM work at Camp Schwab, the governing authority hierarchy is:

**Federal layer (DoD-wide):**
- UFS 3-701-01 (current edition) -- PRV, PUC, ACF, Equation 3-1
- UFC 3-730-01 (2024) -- Programming Cost Estimates; DB Design 4%
- UFS 3-740-05 (2 Feb 2026) -- Construction Cost Estimating (non-mandatory supplement)
- UFC 4-010-01 -- AT/FP minimum standards
- UFC 3-310-04 -- Seismic evaluation and retrofit

**District layer (Japan-specific, mandatory per JDDG 1.5):**
- JDDG v9.0 (April 2025) -- Japan District Design Guide; design criteria, Okinawa-specific
  technical requirements, environmental, ERC/renovation thresholds, design phase deliverables
- JED Cost Estimating Guide (Nov 2025) -- estimate preparation, software (MCACES/MII, PACES),
  cost sources, markup structure, QC process, submittal requirements
- JES (Japan Edited Specifications) -- project specifications; used first per JDDG 1.6,
  then UFGS where JES not available
- JEGS (Japan Environmental Governing Standards) -- environmental obligations (asbestos,
  lead, PCBs, AFFF, contaminated soils, radon)

**Rule:** Every estimate and Section F narrative for Japan District work must cite JDDG 1.5
and the JED Cost Estimating Guide as cost estimate authorities alongside UFS 3-701-01 and
UFC 3-740-05. The district layer does not replace the federal layer; it adds Japan-specific
requirements that sit directly under it.

### Unit Cost Source Hierarchy

The JED Cost Estimating Guide (Section 01.8) establishes the following cost source priority:

**Tier 0: Vendor quotations** -- most accurate; required for items over $10,000 USD and
specialized/not readily available items. Must include company name, POC, quote number, date.

**Tier 1: Japan-market construction cost databases** -- Sekisan Shiryo (Keizai Chosa Kai),
Kensetsu Bukka (Kensetsu Bukka Chosa Kai), or equivalent. JED 01.8 states these "shall be
the default cost source in the absence of more accurate information such as a vendor quote."

**Tier 2: US cost databases with location adjustment** -- RS Means / DoD Cost Book with ACF.
Used when Japan-market databases do not cover the scope item or when the estimate basis
is parametric (ROM-level) using CONUS direct costs.

**Current Camp Schwab portfolio position:** All five estimates use Tier 2 (RS Means FY24
CONUS direct costs with ACF 1.85). This is appropriate for Level 3 ROM products where
the cost basis is parametric and the ACF bridges CONUS-to-OCONUS pricing. When FEAD
engineers develop the detailed DB-RFP estimates in MCACES/MII, they will use Tier 0/1
sources per JED 01.8 with Japan MLIT labor rates (JED 02.2.3). The ROM products
provide the programming-level cost envelope; the JED-compliant detailed estimate follows
in the design phase.

**Documentation requirement:** Section F Item 9 must state the unit cost tier used and
the rationale. For Tier 2 estimates: "Unit costs are FY24 CONUS direct costs from RS Means,
adjusted to OCONUS via ACF 1.85. Japan-market database pricing (JED 01.8 Tier 1) will be
applied by FEAD estimator during DB-RFP detailed estimate development."

### Metric / SI Units

JDDG makes metric (SI) the default for all Japan District projects (JDDG 1.5, 1.6).
JED Cost Estimating Guide requires metric UOM for assemblies (Section 02.2.9.5).
Dual dimensioning is prohibited except by explicit JED approval.

**Current Camp Schwab portfolio position:** Level 3 ROMs use US customary (SF, LF, EA)
because the cost basis is RS Means FY24 CONUS, which publishes in US customary units.
ACF 1.85 bridges the pricing gap. This is consistent with parametric/programming-level
products where the source data is US-origin.

**Downstream requirement:** When FEAD develops the DB-RFP estimate in MCACES/MII,
all quantities convert to metric per JED 02.2.9.5 and JDDG metric standard. Scope
reference packages delivered to FEAD should note the US customary basis and flag
the conversion requirement in the building identity header.

### Design Phase Mapping

JDDG Chapter 2 ties design phases to specific cost estimate deliverables:

| JDDG Phase | Design % | OMEGA Level | JED Cost Estimate Requirement |
|------------|----------|-------------|-------------------------------|
| Programming Charrette | Pre-concept | Level 3 ROM | SF comparisons, basic products (JED 03.8.1) |
| Parametric (15%) | 15% | Level 3 ROM | PACES or MII; summarized costs permitted (JED 03.8.2) |
| Concept (35%) | 35% | Level 3 ROM | Per JED Cost Estimating Guide (JDDG 2.7.4) |
| Intermediate (65%) | 65% | Level 2 | Detailed task analysis in MII (JED 03.8.3) |
| Final (95%) | 95% | Level 1 | Complete MII estimate, detailed QTO (JED 03.8.4) |
| RTA (100%) | 100% | Level 1 | Ready to advertise (JED 03.8.5) |

**Current Camp Schwab portfolio position:** Level 3 ROM maps to the Programming/Parametric/
Concept band. The current CEPBKUP workbooks are programming-level products that establish
the DD 1391 cost envelope. They are not JED A-E contract deliverables and are not subject to
JED 01.13 Excel restrictions (which apply to A-E firms under JED contract). The FEAD engineer's
MCACES/MII estimate at Concept (35%) and beyond must comply with JED submittal requirements.

### Section F Renovation vs. Replacement Narrative (JDDG 2.9.1)

JDDG 2.9.1 requires, for renovations, a narrative on renovation costs compared to replacement
values of existing buildings and associated implementation triggers for:
- Seismic evaluation and retrofit (UFC 3-310-04)
- Antiterrorism (UFC 4-010-01)
- Occupancy reclassification (UFC 4-010-01, independent of cost ratio)

**Section F Item 11 must include this narrative.** The existing ERC threshold analysis provides
the math. The JDDG 2.9.1 requirement adds the narrative cross-walk documenting:
(a) Total Funded vs. governing PRV (ERC ratio, already computed per G-32)
(b) Whether the 50% PRC threshold is breached (BULLETIN 3302, UFC 4-010-01)
(c) Whether seismic evaluation is triggered (UFC 3-310-04: >50% for SDC C, >30% for SDC D/E/F)
(d) Whether occupancy reclassification triggers AT/FP independently of cost ratio
(e) Citation stack: UFS 3-701-01 (PRV), UFC 4-010-01 (AT trigger), UFC 3-310-04 (seismic
    trigger), JDDG v9 Chapter 2.9.1 (Japan District implementation requirement)

For Camp Schwab:
- SCH-1024: conversion from BOQ/BEQ to Armory/Admin. Occupancy reclassification
  likely triggers AT/FP independently. ERC ratio 10.4% (CLEAR).
- SCH-3213: conversion from Field Maint Shop to CLB-4 BN HQ. Occupancy reclassification
  likely triggers AT/FP independently. ERC ratio 43.7% (MONITORING).
- SCH-3237, SCH-3270, SCH-3314: no occupancy reclassification. ERC ratios all CLEAR.

### Okinawa Environmental and Climate Scope Framework

#### Radon (JDDG 9.11.2, 19.11; NAVRAMP)

JDDG 9.11.2: "Radon mitigation is a common requirement for facilities in Okinawa."
Requires conformance with UFC 3-101-01 paragraph 2-5.1: sub-pipe system under slab
designed by plumbing engineer; all systems designed for easy conversion to active
if future testing reveals unacceptable levels (conduits and junction boxes for fan
installation, exterior pipes extended to roof).

JDDG 19.11: "Monitoring of Radon levels will almost always be required by the Installation
for projects in Okinawa and Iwakuni." For Navy/Marine projects, NAVRAMP Guidebook
for Naval Shore Installations applies (separate documents for Family Housing and
Non-Residential). JDDG 19.11 also states monitoring should NOT typically be included
in the construction contract (long-term testing duration, foundation settling period).
What goes in the design package is the mitigation system, not the monitoring.

**Camp Schwab NAVRAMP RPC:** Unknown publicly. Default RPC 2 (Screening) per NAVRAMP
guidebook default rule ("If UIC is not listed, assume RPC 2"). PWD ENV confirmation required.
All visible evidence (active radon mitigation contracts on Kadena and USMC camps, JDDG
language, Oak Ridge National Labs data from MCB Butler) points to RPC 1 or 2, not the
low-risk RPC 3 exemption.

**CRITICAL:** M67400-0004 is the UFS/UFC site code for ACF and pricing. It is NOT a NAVRAMP
RPC. These are separate designations from separate systems. Never conflate them.

**Scope treatment for current estimates:** Radon investigation/testing scope should be
carried in ROMs for new and renovated inhabited facilities on Okinawa, with JDDG 9.11.2
and 19.11 as authority. For conversion buildings with occupancy change (SCH-1024, SCH-3213),
radon evaluation is almost certainly required. Include radon evaluation/mitigation scope
unless PWD ENV explicitly documents RPC 3 and no further action required.

**Current portfolio status:** None of the five estimates currently carry radon scope.
This is a documented gap. Until RPC is confirmed, Section F Item 10 should note:
"NAVRAMP Appendix B initial RPC for Camp Schwab is not in the project record; PWD ENV
confirmation pending. JDDG v9 (9.11.2, 19.11) and NAVRAMP policy require radon
monitoring and, if indicated, mitigation for Okinawa projects. Radon scope placeholder
will be added upon RPC confirmation or carried as a yellow-flagged item."

#### Humid Environment / Corrosion (JDDG 9.5.2, 12.17)

JDDG 9.5.2 defines environmental severity using UFC 1-200-01 ESC and ASHRAE climate zones.
Okinawa is classified as a humid environment. Architectural design must incorporate systems,
materials, and details appropriate to the environmental severity and humidity.

JDDG 12.17 adds special criteria for humid environments. JDDG 12.17.6 provides Okinawa-
specific outdoor design temperatures and cooling coil considerations.

**Scope implications:** Estimates for Okinawa projects must include corrosion-resistant
envelope, coatings, sealants, and enhanced HVAC/dehumidification scope as standard items,
not optional add-ons. Each should have SCOPE_DETAIL items citing JDDG 9.5.2 / 12.17.x.

**Current portfolio status:** None of the five estimates carry explicit JDDG-cited
corrosion-resistant or humid environment scope items. The HVAC replacement scope covers
system replacement but not Okinawa-specific dehumidification as a separate line item.
This is a documented gap for FEAD to address during DB-RFP design development. The ROM
products were scoped before JDDG integration. For future estimate updates or new buildings,
Okinawa humid environment scope must be included from the start.

#### Prefectural Power Infrastructure (JDDG 1.7, Ch.14)

JDDG 1.7 requires designers to account for differences in prefectural infrastructure including
power requirements between Okinawa, Yamaguchi, and Kanagawa. Chapter 14 (Electrical)
figure 6 and table 34 define Okinawa-specific primary/secondary distribution, transformer
configurations, and voltage levels.

**Scope implication:** Electrical scope items should carry basis-of-estimate notes referencing
JDDG Ch.14 tables when Okinawa-specific power configurations affect equipment selection
or cost. For the current Camp Schwab estimates, this is FEAD coordination context.

#### JEGS Environmental Framework (JDDG Ch.19)

Environmental obligations for Japan District projects are governed by JEGS (Japan Environmental
Governing Standards). JDDG Ch.19 covers asbestos (19.5), lead/arsenic/cadmium/chromium
(19.6), PCBs (19.7), AFFF (19.8), ODS (19.9), radioactive isotopes (19.10), radon (19.11),
historic/cultural resources (19.12), natural resources (19.13), contamination remediation (19.15).

**Current portfolio status:** Three buildings (SCH-1024, SCH-3213, SCH-3237) carry ACM
scope based on existing surveys (24-25 years old, requiring PWD ENV confirmation). The
current estimates reference the surveys directly but do not cite JEGS as the governing
environmental framework. For completeness, Section F environmental scope references
should note JEGS compliance where applicable.

### ITR and ECIFP as Downstream Process Gates

JDDG Chapter 5 requires Independent Technical Review (ITR) by personnel knowledgeable in
both US and Japanese criteria and construction practices, with signed certifications at each
design phase. JDDG 2.4 and 2.8.6/2.9.6 formalize ECIFP content and timing.

These are downstream requirements that apply when the project enters the JED design phase.
The Level 3 ROM products do not require ITR or ECIFP. However, the ECIFP must capture
critical estimating assumptions tied to JDDG specifics (radon, humid environment HVAC,
Okinawa power, JES). When scope reference packages are handed to FEAD, flag that these
assumptions need to carry forward into the ECIFP.

### JED Cost Estimating Guide -- Excel Usage Note

JED Cost Estimating Guide Section 01.13 states Excel "may not be used for estimate generation
except for partial or basic estimating products" and requires pre-approval by POJ-EDS-V.

**Applicability to current work:** The Camp Schwab CEPBKUP workbooks are MCIPAC G-F
programming-level ROM products, not JED A-E contract deliverables. They are not subject to
JED 01.13 Excel restrictions. The FEAD engineer's MCACES/MII estimate is the JED-compliant
product. The CEPBKUP workbooks feed the DD 1391 programming package; the JED-compliant
detailed estimate follows in the design phase.

### JED Cost Estimating Guide -- Labor Basis Note

JED 02.2.3: Japan MLIT wage rates are the basis for craft labor, not Davis-Bacon or US wage
determinations. Contractor payroll tax and insurance at 23% per MLIT publication (subject to
annual update). This applies to FEAD's detailed estimate, not to the Level 3 ROM (which uses
RS Means CONUS parametric costs with ACF).

---

## Gold Standard

Every estimate matches the five CEPBKUP gold standard files in structure, formula architecture,
tab layout, color palette, border scheme, and methodology documentation. These files were read
cell-by-cell on 21 Mar 2026. Every value below came from the actual files -- not memory.

**GOLD STANDARD FILES (project directory -- read 21 Mar 2026):**

| File | Building | Version | Date | Notes |
|------|----------|---------|------|-------|
| 1024_G_CEPBKUP_BU26PPE70M_POM26_20260319.xlsx | SCH-1024 | v11 | 19 Mar 2026 | 4-FAC formula PRV; 4-column ESTIMATE; 9 UNIFORMAT codes; 67 items / 11 groups |
| 3213_G_CEPBKUP_BU26PPE72M_POM26_20260320.xlsx | SCH-3213 | v6 | 20 Mar 2026 | Largest scope; 73 items / 11 groups / 6 UNIFORMAT codes; iNFADS PRV |
| 3237_G_CEPBKUP_BU26PPE73M_POM26_20260309.xlsx | SCH-3237 | v4 | 09 Mar 2026 | Multi-FAC warehouse/armory; iNFADS PRV; 6 scope groups; 4 UNIFORMAT codes |
| 3270_G_CEPBKUP_BU26PPE74R_POM26_20260319.xlsx | SCH-3270 | v9 | 19 Mar 2026 | PRIMARY COLOR/COSMETIC STANDARD; 42 items / 10 groups / 6 UNIFORMAT codes |
| 3314_G_CEPBKUP_BU26PPE71M_POM26_20260318.xlsx | SCH-3314 | v3 | 18 Mar 2026 | Section F label standard (F-1 through F-13); Group 7 sub-groups 7A/7B/7C |

**CRITICAL: When uncertain about ANY cosmetic, format, formula, or value -- read the gold standard file directly. Never guess.**

**REFERENCE FILES (project directory -- catalogued v25.0):**

| File | Document | Date | Notes |
|------|----------|------|-------|
| JED_Cost_Estimating_Guidance_Combined_2025_Nov.pdf | JED Cost Estimating Guide | Nov 2025 | 80 pages; cost sources, markup structure, QC, submittal requirements |
| Japan_District_Design_Guide_v9_APRIL2025__508_Compliant_.pdf | JDDG v9.0 | Apr 2025 | Design criteria, Okinawa-specific requirements, ERC thresholds, radon, humid environment |
| FY26_Budget_Rates.pdf | DoD Foreign Currency Fluctuation Rates | FY26 | FY26 President's Budget exchange rates. Japan Yen: 150.4415 JPY/USD. Budget formulation rate only -- H.10 governs PARAMETERS B33. |

**3270 is the PRIMARY color and cosmetic gold standard.** When building any new workbook, open
3270_G_CEPBKUP_BU26PPE74R_POM26_20260319.xlsx and match its fills, fonts, row heights, borders,
and column widths exactly. The PARAMETERS row assignments in 3270 differ from the other four
buildings -- see PARAMETERS row table below.

---

## MANDATORY INTAKE -- Ask Before Writing a Single Cell

Before building or recalculating any estimate, obtain confirmed answers to every item
below. Do NOT assume any value. Do NOT carry forward from a previous building without
explicit confirmation. If an answer is missing, stop and ask.

### Required Intake Questions (ask all at once, clearly numbered)

**Building Identity**
1. Building number (e.g., SCH-3314)?
2. PAX ID number?
3. Fi Web project number? (NEVER guess -- must come from Anthony explicitly. Never construct it.)
4. iNFADS RPUID?
5. Supported unit(s)?
6. Delivery method (Design-Build / Design-Bid-Build / DOW)?

**Scope**
7. Is there a confirmed scope document (worklist, BFR, SOW, AE floor plan, existing estimate)?
   If an existing estimate is provided: extract scope items only (description, qty, unit, unit cost,
   notes/authority). Rebuild ALL tabs to v11 APEX OMEGA standard. Do NOT copy formatting,
   formulas, tab structure, or any structural element from the old file.
   If no scope document exists: state that clearly and collect scope items interactively.
8. Total building GSF -- confirmed from iNFADS / AE Worksheet / HE Schedule?
   State the source explicitly. Do not estimate GSF.
   For multi-FAC buildings: provide GSF for EACH FAC code individually, not just total.
   The total must match iNFADS or AE Worksheet. Partial-area SF (e.g., adequate-only)
   must NOT be used for PRV -- use total SF unless RPAO directs otherwise in writing.
9. How many FAC codes apply?
   For each FAC code provide: FAC code number, UFC 2-000-05N description, confirmed PUC
   from UFC 3-701-01 C7 (25 Jul 2025) Table 3, and confirmed GSF.
   Each FAC code has a distinct PUC -- never blend. Confirm each by direct read, not memory.
   Do not use snapshot PUC values from this skill without re-reading Table 3 directly.
10. PRV source -- which applies? (Run Protocol PRV-1 above)
    FIRST: Run the conversion test (G-30).
    a. NON-CONVERSION: Pull current Property Record "Current PRV" from iNFADS.
       Record exact dollar figure, RPUID, and pull date. Pull must be within 30 days
       of submission (G-31). Do NOT use the AE Worksheet "PRV at EOY" (G-29).
    b. CONVERSION: Compute formula PRV using post-conversion FAC codes and current
       UFS 3-701-01 Table 3 PUCs. Requires confirmed post-conversion FAC code(s),
       GSF allocation, and PUC per item 9, PLUS confirmed HF, PD, SIOH, CF per PRV-3.
    For ALL buildings regardless of method: document Property Record PRV, AE Worksheet PRV,
    and formula PRV cross-check in Section F Item 11 with sources and dates.
    Compute ERC ratio (Total Funded / governing PRV) per G-32.
    If neither is confirmed: STOP. Never calculate a PRV from unverified inputs.
11. Are any building areas explicitly excluded from construction scope?
    Source the exclusion to a decision memo, email, or written direction. State the document.
    NOTE: Scope exclusions do NOT reduce PRV. PRV = full building per iNFADS or formula.
12. Does the scope include HAZMAT (asbestos, lead, mold)?
    If yes: provide survey reference (lab name, date, NVLAP accreditation), ACM/LBP type,
    quantities (SF or LF), and confirmed unit costs.
    If no survey on file: no HAZMAT scope. Do not add a HAZMAT placeholder without a survey.

**Estimate Parameters**
13. Base year for unit costs (default FY24 -- confirm)?
14. Target fiscal year (default FY27 -- confirm)?
15. Escalation rate -- confirm 2.1%/yr OSD FY25 still applies, or provide updated rate with source?
16. ACF -- confirm 1.85 for Camp Schwab (UFC 3-701-01 C7, Table 4-1, site M67400-0004)?
    If different installation: provide site code and confirmed ACF.
17. General Requirements -- confirm 10% FSRM program-directed?
18. Contingency -- confirm 10% FSRM program-directed?
19. SIOH -- confirm 8.0% FSRM customer-directed (NOT standard 7.3%)?
    NOTE: This 8.0% is the program adder applied to Construction Base.
    It is SEPARATE from the SIOH factor (1.08) in Equation 3-1 for PRV.
    They are different calculations. Do not confuse them.
20. Design -- confirm 6% NAVFAC agency-directed?
21. CM -- confirm 4% agency-directed?
22. DB Design -- confirm 4% applied AFTER Total Funded (UFC 3-730-01)?
23. LSH rate -- confirm 2.5% per NAVFAC 11010.44E CH-1?
24. Current JPY/USD exchange rate, source, and date?
    (Federal Reserve H.10 or Oanda.com; flag YELLOW in PARAMETERS B33 if not confirmed
    on date of build. JPY column is display-only -- does not affect ROM chain.)
25. Does a previous version exist? If yes, provide Total Funded and Total Project Cost
    for each prior version for delta comparison in Section E version history.
26. Prepared By date -- confirm DD Month YYYY.

**Okinawa / Japan District (ask for all JED-area projects)**
27. NAVRAMP RPC for this installation (1/2/3)?
    Source: PWD ENV or NAVFAC radon program lead. Provide email/date or NAVRAMP Appendix B entry.
    If RPC not confirmed: annotate "NAVRAMP Appendix B not available in project file; default
    planning assumption RPC 2 (Screening) per NAVRAMP guidebook. PWD ENV confirmation required
    before final design/award." Flag YELLOW until confirmed.
    NOTE: M67400-0004 is the UFS/UFC site code for ACF. It is NOT a NAVRAMP RPC.
    These are separate designations from separate systems. Never conflate them.
28. Does the scope involve occupancy change or conversion to inhabited use?
    If yes: radon evaluation almost certainly required per JDDG 9.11.2 and 19.11, regardless
    of RPC. Include radon evaluation/mitigation scope unless PWD ENV explicitly documents
    RPC 3 exemption with no further action required.
29. Has PWD ENV confirmed Camp Schwab's Radon Potential Category?
    If no: carry radon investigation/testing as yellow-flagged scope for any inhabited facility.
    Document in Section F Item 10.

### Rules for Intake
- "Same as last time" is not an answer. Confirm explicitly for each building.
- Scope incomplete = do not build. State exactly what is missing.
- FAC code uncertain = look up UFC 2-000-05N. Confirm. Do not guess.
- PUC uncertain = read UFC 3-701-01 C7 Table 3 directly. Do not use memory.
- Exchange rate not confirmed = flag YELLOW with blank placeholder. Document in Section F Item 10.
- Existing estimate provided in a different format = extract scope items only. Rebuild everything else.
- Fi Web number must come from Anthony. Never construct or guess it.
- PRV source must be stated explicitly: Property Record Current PRV (non-conversion) OR formula
  method with post-conversion FAC codes (conversion). Run G-30 conversion test at intake.
  Formula method MUST use full Equation 3-1. Q×PUC×ACF alone is incomplete and wrong.
- GSF must have a source. For multi-FAC buildings, confirm GSF per FAC, not just total.
  Do not use partial-area SF (adequate-only, scope-only) for PRV.

---

## ROM Formula (LOCKED)

```
Base Direct (FY24 CONUS pre-ACF)
  = SCOPE_DETAIL grand total G cell

× ACF 1.85 (Camp Schwab)
× Compound Escalation Factor  =(1+0.021)^3 = 1.064332 [live formula =(1+B19)^B20]
× (1 + General Requirements 10%)
× (1 + Contingency 10%)
= CONSTRUCTION SUBTOTAL  [ROUND to nearest dollar]

+ LSH (PRV × 2.5%)         [hardcoded confirmed value in PARAMETERS]
= CONSTRUCTION BASE

+ Design  6.0% × Construction Base  [NAVFAC agency-directed]
+ SIOH    8.0% × Construction Base  [OCONUS FSRM customer-directed, NOT 7.3%]
+ CM      4.0% × Construction Base  [agency-directed]
= TOTAL FUNDED COST         [ROUND to nearest dollar]

+ DB Design  4.0% × Total Funded    [UFC 3-730-01; applied AFTER Total Funded -- ALWAYS]
= TOTAL PROJECT COST
```

**Formula notes:**
- ACF and escalation are separate multiplicative steps -- never combine into one factor.
- Construction Subtotal: ROUND(B8*(1+B23),0) -- round to nearest dollar.
- Total Funded: ROUND(B11+B15+B16+B17,0) -- round to nearest dollar.
- DB Design applied AFTER Total Funded. Always. No exceptions. UFC 3-730-01.
- LSH = PRV x 2.5%. PRV = Property Record Current PRV (non-conversion, per G-29/G-30)
  OR formula PRV with post-conversion FAC codes (conversion, per G-30).
  Q x PUC x ACF alone is NOT a valid PRV formula. Always apply HF x PD x SIOH x CF.
- LSH hardcoded in PARAMETERS as a confirmed dollar value.
  Document in Section F Item 11 if LSH is rounded from a non-integer PRV × 0.025 result.
- Compound escalation factor: =(1+B19)^B20 -- live formula in PARAMETERS, not hardcoded.
- Cost/SF in Section C = Total Funded / total building GSF. Systems repair benchmark.
  If LSH is a large fraction of Total Funded (common on targeted repairs at large buildings),
  document that in Section F Item 9 so reviewers are not surprised.
- SIOH 8.0% in the program adder chain and SIOH 1.08 in Equation 3-1 are DIFFERENT.
  8.0% is applied to Construction Base. 1.08 is a PRV multiplier. Do not conflate them.

---

## UFC 3-701-01 Equation 3-1 -- Full Formula Reference

```
PRV = Q × PUC × ACF × HF × PD × SIOH × CF
```

| Factor | Full Name | Camp Schwab Value | Authority |
|--------|-----------|------------------|-----------|
| Q | Quantity (GSF per FAC code) | Per Property Record / AE Worksheet | iNFADS Property Record |
| PUC | Plant Unit Cost | Per FAC code, Table 3 | UFS 3-701-01, current edition only |
| ACF | Area Cost Factor | 1.85 | UFS 3-701-01, Table 4-1, M67400-0004 |
| HF | Historical Factor | 1.0 | Non-historical (not on NRHP) |
| PD | Productivity Differential | 1.09 | Non-medical, UFS 3-701-01 |
| SIOH | Supervision, Inspection, Overhead | 1.08 | UFS 3-701-01 |
| CF | Contractor Factor | 1.05 | UFS 3-701-01 |

**Combined factor for Camp Schwab (HF × PD × SIOH × CF) = 1.0 × 1.09 × 1.08 × 1.05 = 1.23606**

**Multi-FAC calculation sequence:**
```
Step 1: For each FAC_i: sub_i = GSF_i × PUC_i
Step 2: Q×PUC base = Σ sub_i
Step 3: PRV = (Q×PUC base) × ACF × HF × PD × SIOH × CF
Step 4: LSH = PRV × 0.025
```

Do NOT apply the combined factor separately to each FAC. Apply it once to the total after
summing all (GSF × PUC) products. This ensures SIOH and CF are not compounded across FACs.

**When to use formula vs. Property Record PRV (per G-29, G-30):**
- NON-CONVERSION (DD 1391 FAC matches Property Record FAC): Use Property Record Current PRV.
  Pull within 30 days of submission (G-31). Formula is cross-check only.
- CONVERSION (DD 1391 programs a different facility type): Use formula with post-conversion
  FAC codes. Property Record PRV documented as reference only.
- Property Record PRV appears zero or clearly erroneous: Use formula method. Flag to RPAO.
- Never use AE Worksheet "PRV at EOY" as the governing value (G-29).
- RPAO owns the Property Record. Cost estimator owns the DD 1391 estimate. These are
  different purposes. The estimator has the professional obligation to use the correct PRV
  for the facility type being programmed.

---

## Locked Parameters -- Camp Schwab Portfolio

| Parameter | Value | Source / Authority |
|-----------|-------|--------------------|
| ACF | 1.85 | UFC 3-701-01 C7 (25 Jul 2025), Table 4-1 OCONUS, site M67400-0004 |
| Escalation rate | 2.1%/yr | OSD FY25 published construction escalation rate, client-confirmed |
| Escalation base year | FY24 | Client-directed |
| Escalation target year | FY27 | Client-directed |
| Compound escalation factor | =(1+r)^n | Live formula in PARAMETERS =(1+B19)^B20 |
| General Requirements | 10% | FSRM program-directed |
| Contingency | 10% | FSRM program-directed |
| LSH rate | 2.5% | NAVFAC 11010.44E CH-1 |
| SIOH (program adder) | 8.0% | OCONUS FSRM customer-directed, MCIPAC G-F program-directed -- NOT standard 7.3% |
| Design | 6% | NAVFAC agency-directed |
| CM | 4% | Agency-directed |
| DB Design | 4% | Applied AFTER Total Funded | UFC 3-730-01 (2024) |
| HF (PRV Eq 3-1) | 1.0 | Non-historical, not on NRHP |
| PD (PRV Eq 3-1) | 1.09 | Non-medical, UFC 3-701-01 |
| SIOH (PRV Eq 3-1) | 1.08 | UFC 3-701-01 |
| CF (PRV Eq 3-1) | 1.05 | UFC 3-701-01 |
| Combined PRV factor | 1.23606 | HF × PD × SIOH × CF |

Any deviation requires explicit written client direction. Document in Section F Item 11.

---

## Per-Building Locked Reference Data (v19 -- Direct Read from CEPBKUP Files 21 Mar 2026)

### ⚠ ALL VALUES BELOW ARE FROM DIRECT FILE READS ON 21 MAR 2026.
### These are the authoritative locked values. Do not override without explicit direction.

---

### SCH-1024 (Armory / BEQ Conversion -- Multi-FAC Formula PRV)
Status: v11 (19 Mar 2026) -- cosmetic alignment of v10; scope and values unchanged from v10.
4-column ESTIMATE layout (A=row number, B=element, C=amount, D=formula/source).
GSF: 84,861 SF total | First Floor: 26,488 SF | PAX: 387356 | Fi Web: BU26PPE70M
CCN: 14345 (Armory primary) / 72111 (BEQ) / 61010 (Admin/Gym) | RPUID: 148675
Facility ID (iNFADS): NFA100000443601 | Facility Name: Multi Purpose BEQ/BOQ/CO HQS
Site: HE -- Henoko Ammo Area-6010 | Address: 1024 Corrigidor Way, Henoko Okinawa
Built: 1 Nov 1991 | Floors Above Grade: 4 | Height: 47 ft | Construction: PERM
Delivery: Design-Build (DB)
AE Evaluator: G-F AE Staff | Site Visit: 2/16/2023 | AE Worksheet Updated: 15 Jun 2023
PRV at EOY (iNFADS AE Worksheet): $90,145,407 (pre-conversion BEQ/CIF configuration, prior PUC vintage)
Property Record Current PRV: $72,207,194 (RPUID 148675, pull date 26 Mar 2026) -- reference only
PRV delta note: Property Record $72.2M reflects pre-conversion FAC codes at current RPAO calculation.
AE Worksheet $90.1M reflects prior evaluation snapshot. Formula $96.5M uses post-conversion FAC codes
at current UFS 3-701-01 PUCs. Formula governs per G-30 (conversion building). All three values and
deltas documented in Section F Item 11. Mission partner briefed on formula method (23 Mar 2026).
Do not treat the Property Record/AE/formula deltas as discrepancies requiring correction.
They reflect different FAC code vintages and different PUC vintages, which is expected for a conversion.

**PRV Method: FORMULA** (post-conversion; iNFADS RPUID 148675 reflects pre-conversion BEQ/CIF)

**iNFADS CCN breakdown (from AE Worksheet, confirmed 23 Mar 2026):**
| CCN   | Description                  | AE Area (SF) | Estimate FAC | Estimate GSF |
|-------|------------------------------|-------------|--------------|--------------|
| 44111 | General Warehouse            | 10,030 SF   | 4421         | 8,802 SF     |
| 14345 | Armory                       | 993 SF      | 4427         | 7,142 SF     |
| 44110 | General Purpose Warehouse    | 867 SF      | UNRESOLVED   | not mapped   |
| 72411 | Unaccompanied Off H (BEQ)    | 70,633 SF   | 7210         | 66,151 SF    |
| 74044 | Indoor Physical Fit Ctr      | 2,338 SF    | 6102         | 2,766 SF     |

OPEN ITEM -- CCN 44110 (867 SF): Not mapped to a discrete FAC row in PARAMETERS. The total
GSF ties (84,861 SF confirmed), but 44110 is not broken out. Its 867 SF is likely rolled into
4421 (AE shows 10,030 SF for 44111 vs estimate 8,802 SF for FAC 4421 -- 1,228 SF gap).
Confirm with RPAO or PARAMETERS before next estimate revision.

FAC 4427 GSF note: AE worksheet shows CCN 14345 Armory at 993 SF current iNFADS footprint.
Estimate applies FAC 4427 to 7,142 SF (post-conversion programmatic area, not current CCN footprint).
This is correct methodology for formula PRV on a conversion project. Must be documented explicitly
in Section F Item 11 as post-conversion programmatic SF, not the iNFADS CCN 14345 footprint.

**PRV Calculation (v11 gold standard -- confirmed from PARAMETERS tab):**

| FAC | Description | GSF | PUC ($/SF) | PARAMETERS rows | Sub-PRV |
|-----|-------------|-----|-----------|-----------------|---------|
| 7210 | Enlisted Unaccompanied Housing | 66,151 | $480.00 | B36-B38 | $31,752,480 |
| 4421 | General Purpose Warehouse (CIF) | 8,802 | $692.00 | B39-B41 | $6,090,984 |
| 6102 | Large Unit HQ / Admin (gym) | 2,766 | $473.00 | B42-B44 | $1,308,318 |
| 4427 | Small Arms Storage, Installation | 7,142 | $428.28 | B45-B47 | $3,058,775.76 |
| **TOTAL** | | **84,861** | | B38+B41+B44+B47 | **$42,210,558** |

PARAMETERS formulas (locked):
- B38: =B36*B37 (FAC 7210 sub-PRV)
- B41: =B39*B40 (FAC 4421 sub-PRV)
- B44: =B42*B43 (FAC 6102 sub-PRV)
- B47: =B45*B46 (FAC 4427 sub-PRV)
- B48: HF = 1 (hardcoded blue)
- B49: PD = 1.09 (hardcoded blue)
- B50: SIOH Factor = 1.08 (hardcoded blue)
- B51: CF = 1.05 (hardcoded blue)
- B52: Combined Factor = =B48*B49*B50*B51 = 1.23606
- B53: TOTAL PRV = =(B38+B41+B44+B47)*B18*B52
- B54: LSH = =ROUND(B53*B24,0) = 2,413,084

ESTIMATE cross-refs: C4=SCOPE_DETAIL!G100 | C9=PARAMETERS!B54 (LSH)
PARAMETERS compound escalation: B21 = =(1+B19)^B20
PARAMETERS JPY row: B57

```
PRV = $42,210,558 × 1.85 × 1.23606 = $96,523,347
LSH = $96,523,347 × 2.025% = $2,413,084
```

ERC Ratio: $10,012,635 / $96,523,347 = 10.4% -- CLEAR (well below 50%)

**v11 LOCKED VALUES (19 Mar 2026 -- from CEPBKUP file direct read):**
Base Direct: $2,548,659 | Constr Subtotal: $6,072,200 | LSH: $2,413,084
Const Base: $8,485,284 | Design: $509,117.04 | SIOH: $678,822.72 | CM: $339,411.36
Total Funded: $10,012,635 | DB Design: $400,505.40 | Total Project: $10,413,140.40

**UNIFORMAT codes (9 codes):** B20 $123,500 | C10 $184,997 | C30 $87,743 | D20 $90,000 |
D30 $773,000 | D40 $10,000 | D50 $831,600 | E20 $6,600 | F20 $199,499 | G10 $9,000 |
G20 $232,720 | Total check: $2,548,659

**11 scope groups:**
G1 -- ARMORY VAULT CONVERSION (items 1-15, rows 5-19): 28 BEQ rooms to 14 armory vaults
G2 -- ARMORY EXTERIOR (items 2-16, rows 22-24): walkways, landings, concrete pads
G3 -- GYM TO WORKSPACE (items 1-3E, rows 27-32): CLB-4 Commo swing space to 4th MarRegt
G4 -- COMM ROOM AND WEAPONS CLEANING (items 17-21, rows 35-38)
G5 -- ADMIN LAUNDRY CONVERSION (rows 41-44)
G6 -- BATHS TO OSS VAULT (items 1-many, rows 47-69): locker rooms to OSS with SIPR
G7 -- BUILDING GENERAL (rows 72-76): chiller replacement, TAB, life safety
G8 -- BUILDING TELECOM (rows 79-83): TR per UFC 3-580-01, MCIPAC G-6 Policy Ltr 03-2024
G9 -- EXTERIOR (rows 86-89): covered overhangs, pavilion, site work
G10 -- RESTROOMS AND MISCELLANEOUS (rows 92-93)
G11 -- HAZARDOUS MATERIALS (rows 96-98): Bhate 19 Nov 2001; H3: 15% Chrysotile mastic, 8,392 LF

Grand total row: G100. Formula: =SUM(G20,G25,G33,G39,G45,G70,G77,G84,G90,G94,G99)
(sum of group subtotal rows only, NOT =SUM(G4:G99))

**Version history (locked from ESTIMATE tab):**
- Oct 2025: Initial ROM $898,500 -- armory conversion only
- Feb 2026: Expanded scope $10,325,000 -- armory + gym + OSS vault
- v8 (05 Mar 2026): $9,368,055 -- 67-item worklist, 2-FAC PRV (FAC 7210/4427 only)
- v9 (08 Mar 2026): $10,012,635 -- corrected PRV to 4-FAC; NOTE: Eq 3-1 still incomplete in v9
- v10 (10 Mar 2026): $10,012,635 -- PRV corrected per full Eq 3-1; LSH corrected from ~$1,952K to ~$2,413K
- v11 (19 Mar 2026) CURRENT: $10,012,635 -- cosmetic alignment; 4-column ESTIMATE; no value changes

**Section F (13 items, inline ESTIMATE tab):**
Item 9 basis: "LSH is a significant share of Total Funded given Building 1024 total scale (84,861 SF)
relative to the targeted first-floor renovation scope."
Item 12: "Anthony L. Potter  |  Facilities Professional  |  MCIPAC G-F PPE  |  19 Mar 2026"

**HAZMAT:** Bhate Environmental Associates survey (19 Nov 2001), H3 finding: 15% Chrysotile mastic,
8,392 LF building-wide. PWD ENV re-inspection required pre-design.

---

## SCH-1024 MECHANICAL SYSTEMS DATA (BUILDER SMS, 23 Mar 2026)

Source: BUILDER SMS Final 4 Equipment Details Report, RPUID NFA100000443601,
generated 7/6/2023 10:44:07 AM. 70 component records across D20, D30, D40, D50.
This is the authoritative mechanical equipment inventory for Building 1024.

### CHILLED WATER PLANT

Two Trane air-cooled chillers, Mechanical Yard, installed 2014:
- WC-1: TRANE CGAM060A2J02XXD2A1A1A1CXXA1A1A2XXAXXXAXA5X1DXXXLXX | SN U13J38572 | 60 TON | R-410A | CI 69 | RSL 6 (from Jul 2023 survey; ~3 yrs remaining as of Mar 2026)
- WC-2: same model | SN U13J38573 | 60 TON | R-410A | CI 69 | RSL 6
Total chilled water capacity: 120 tons. Both CI 69 (substandard, below 70 threshold).
IN SCOPE: Chiller replacement confirmed in G7 (UNIFORMAT D30, $773,000).

Two EBARA chilled water circulating pumps, 1FL West Mech Room, installed 2014:
- CP-1: 80X65FS2G 61.5 | SN P13744718 | 20 HP | CI 87 | RSL 10
- CP-2: 50X40FS2G 65.5 | SN P13744725 | 7.5 HP | CI 87 | RSL 10
OPEN ITEM: Pump replacement not a discrete line item in v11. Confirm with mechanical engineer whether
CP-1/CP-2 are replaced concurrent with chiller plant or retained.

### VRF / DX CONDENSING UNITS (1FL ROOF)

Five Mitsubishi PUHY-series heat pump condensers, 1FL Roof, all installed 2011:
- ACP-1: PUHY-P450SCM-E2 | SN 9YW00410 | 16 TON | CI 30 | RSL -2 (past RSL as of 2023)
- ACP-2: PUHY-P335SCM-E2 | SN 9YW00699 | 12 TON | CI 30 | RSL -2
- ACP-3: PUHY-P335SCM-E2 | SN 98W00422 | 12 TON | CI 30 | RSL -2
- FAP-1: PUHY-P450SCM-E2 | SN 9YW00411 | 16 TON | CI 30 | RSL -2
- FAP-2: PUHY-P400SCM-E2 | SN 97W00680 | 14 TON | CI 30 | RSL -2
Total VRF/DX capacity: 70 tons. All CI 30 (Poor). All approximately 5 years past RSL as of Mar 2026.
NOT IN SCOPE: None of the five units are in v11 estimate.
OPEN ITEM (HIGH PRIORITY): Mechanical engineer must confirm which zones each unit serves and whether
those zones are occupied under the conversion. All five are failed condition; any zone they serve
that is converted cannot remain on these units. Scope determination required before submission.
NOTE: These are separate from and independent of the chilled water plant (WC-1/WC-2/AHUs).

### AIR HANDLING UNITS

Five Carrier central-station 4-pipe AHUs, all installed 2021, all CI 94, RSL 10:
- AHU-1: 39LD08AA-AD-BGK1A2 | SN 4919U30731 | 8,000 CFM | 1FL West Mech Room
- AHU-2: 39LA18AA-AQBGP112 | SN 4919U30730 | 20,000 CFM | 1FL North Mech Room
- AHU-3: 39MMN36W026P7S-33XDE | SN 5019U43781 | 15,000 CFM | 2FL Mech Room
- AHU-4: 39MN21W026P7T33XDE | SN 5119U36627 | 12,000 CFM | 3FL Mech Room
- AHU-5: 39MN21W026P7V33XDE | SN 5119U36621 | 15,000 CFM | 4FL Mech Room
Total AHU installed capacity: 70,000 CFM. 2021 replacements. Excellent condition.
NOT candidates for replacement. Do not include in scope.
AHU-1 (8,000 CFM) serves the residential BEQ corridor zone (aligns with 1996 Air Dist Schedule 8,710 CFM).
AHU-2 (20,000 CFM) was added in 2021 to serve CIF, fitness, and support wing -- not in 1996 schedule.

Air Distribution Schedule cross-reference (DMS Drawing 7821505B, 1996 as-built):
- FL1 schedule total: 8,710 CFM supply / 8,110 CFM return (BEQ residential only; CIF/gym excluded)
- FL2 schedule total: 17,885 CFM (aligns with AHU-3 at 15,000 CFM nameplate)
- FL3 schedule total: ~10,300 CFM (aligns with AHU-4 at 12,000 CFM nameplate)
- FL4 schedule total: ~10,400 CFM (aligns with AHU-5 at 15,000 CFM nameplate)

### HOT WATER BOILERS

Two Maeda forced-draft oil boilers, 1FL Boiler Room, installed 2021:
- BH-1: MF5-N7WA-H | SN 32605G4 | 2,000 MBH | CI 94 | RSL 20
- BH-2: MF5-N7WA-H | SN MF32604F4 | 2,000 MBH | CI 94 | RSL 20
Total heating capacity: 4,000 MBH. 2021 replacements. Not candidates for replacement.

Supporting boiler/mechanical room equipment (all from BUILDER, all confirmed):
- EBARA HW-1 pump (80X65FS2F65.5E, 7.5HP, 2021, CI 94, RSL 13): hot water loop, West Mech Room
- Wendland RT3 storage tank (4,000 gal glass-lined PE, 2005, CI 87, RSL 26): West Mech Room
- Expansion tank HWL TE-1 (105 gal, 2014, CI 87, RSL 15): hot water loop, Boiler Room
- Expansion tank CHWL TE-2 (105 gal, 2014, CI 87, RSL 15): chilled water loop, West Mech Room
- Chemical feeder CF-1 Griswold (5 gal, 2014, CI 87, RSL 10): West Mech Room
- Chemical feeder CF-2 (5 gal, 2014, CI 87, RSL 10): Boiler Room
- Backflow preventer Watts 009M201 1" (2005, CI 87, RSL 10): Boiler Room

### EXHAUST FANS

Ten exhaust fans total. Seven past RSL (1992-1997 vintage, CI 30). Three replaced 2022 (CI 93).
Past RSL fans (do not include in scope unless conversion disturbs served zones):
- EF-1 (1FL Roof): Asahi CFD14, 400 CFM, 1992, CI 30, RSL -3
- EF-2 (1FL Roof): Asahi CFD18, 3,200 CFM, 1992, CI 30, RSL -1
- EF-3 (1FL Roof): Asahi CFD16, 2,500 CFM, 1992, CI 30, RSL -3
- EF-4 (1FL Roof): Asahi CFD14, 650 CFM, 1992, CI 30, RSL -3
- Roof EF (Roof): Asahi FA-10, 250 CFM, 1997, CI 30, RSL -3 (nameplate sun-washed at survey)
- North Wall EF (North Wall): Asahi unknown model, 300 CFM, 1994, CI 30, RSL -3
- South Wall EF (South Wall): Asahi unknown model, 300 CFM, 1994, CI 30, RSL -3
Good condition fans (2022 replacements):
- North Wall EF1: Asahi SW-18, 300 CFM, 2022, CI 93, RSL 13
- South Wall EF1: Asahi SW-18, 300 CFM, 2022, CI 93, RSL 13
- South Wall EF2: Asahi SW-18, 300 CFM, 2022, CI 93, RSL 13
OPEN ITEM: Mechanical engineer to assess whether conversion boundary overlaps any 1992-era fan zones.

### FIRE PROTECTION (MECHANICAL INTERFACE)

Fire alarm -- Monaco M Series (1FL Main Entrance, 2006, CI 67, RSL 5, 279 detectors): Near substandard.
RSL effectively expired as of Mar 2026. Current estimate carries $10,000 under D40 (life safety).
OPEN ITEM: Confirm with James whether NFPA 72 compliance review is triggered by occupancy
reclassification of armory/OSS/weapons cleaning spaces. $10,000 is insufficient for a full
system upgrade. Scope confirmation required before submission.

Fire alarm -- Hochiki (1FL Warehouse, 2010, CI 72, RSL 6, 14 detectors): Warehouse zone only.

Fire pump EBARA PMB278 (1FL Mech Room West, 1992, CI 79, RSL 8, 33 GPM, 4" electric):
1992 vintage. RSL from survey projects expiration ~2031. Evaluate concurrent with fire alarm scope.

Backflow preventers Watts 6" double-check (FBP1 SN 258980 and FBP2 SN unknown, 1FL South Exterior,
2009, CI 60, RSL 8): Fire suppression supply. Both from 2009. Not in scope.

### TERMINAL UNITS AND SPLIT SYSTEMS

Fan coil unit Mitsubishi 3-ton DX (1FL Warehouse, 2011, CI 87, RSL 8): Not in scope.
Three Daikin split heat pumps (HP-1, HP-2, HP-3, North Exterior, 2013, CI 87, RSL 10, 1-ton each,
R-32, models R28TESE/R28PESE): Not in scope. Supplemental units, not main cooling plant.

---

## SCH-1024 DMS DRAWING INVENTORY (23 Mar 2026)

Source file: 1024_Drawings.pdf (33 sheets, project directory)
CRITICAL NOTE: This DMS package is a compilation from two separate legacy as-built contracts.
It does NOT contain conversion design drawings for the SCH-1024 armory/BEQ project.
No conversion design drawings for Building 1024 are in the current project directory.

CONTRACT 1 (Sheets 1-4): Plumbing Repairs for Water Conservation, Various Buildings,
Camps Schwab and Henoko. A-E Contract N62836-96-D-2057, As-Built 25 Oct 1999.
- Sheet 1: Schedule of Drawings, General Notes, Abbreviations, Location Map, Vicinity Map
- Sheet 2 (Drawing 7821505B, W.R. #47, ESR 66-96): AIR DISTRIBUTION SCHEDULE for Bldg 1024
  Camp Henoko and Bldg 3435 Camp Schwab. PRIMARY HVAC reference for Bldg 1024 in this set.
  Contains room-by-room supply/return CFM for all 4 floors of the BEQ (1996 configuration).
  Key totals: FL1 8,710/8,110 CFM; FL2 17,885 CFM; FL3 ~10,300 CFM; FL4 ~10,400 CFM.
  NOTE: "AHU serving the dining area not included in this schedule" (original drawing note).
  NOTE: Pre-dates 2021 AHU replacement. Schedule reflects original BEQ HVAC, not current plant.
- Sheet 3: KEY PLAN Bldg 1024 (BEQ 4-story, Camp Henoko) and B1060 (Henoko Ordnance Operation).
  Fire alarm partial plan for Bldg 1024. A-E Contract N62836-97-D-2052, ESR 66-96.
- Sheet 4: As-Built fire alarm partial plan Bldg 1024 and B1060.

CONTRACT 2 (Sheets 5-33): Central Issue Facility Renovation, Camp Schwab.
Project MC 0515-T (Electrical). As-built by ODB (Okinawa Defense Bureau). Circa 1998.
THIS SET IS FOR THE CIF BUILDING -- NOT BUILDING 1024. Contains:
- Sheets 5-9: Cover sheet, drawing list, location/site maps, elevation, site plan (CIF)
- Sheets 10-14: Receptacle, lighting, feeder/power system plans (CIF)
- Sheet 15: Fire alarm control system legend and notes (CIF)
- Sheets 16-19: Fire alarm plans, lighting system removal, receptacle removal (CIF)
- Sheets 20-21: Japanese mechanical specs and notes (CIF)
- Sheet 22: Air distribution schedule for CIF building (NOT Building 1024)
- Sheet 23: CIF 1st floor duct routing (NOT Building 1024)
- Sheet 24: Japanese mechanical specs continuation (CIF)
- Sheet 25: 1st FL A/C + Vent Plan, CIF building, 1:100 scale. Contains VAV box schedule
  for CIF (VAV: 差圧感応型電動式, 0.36-1.500 m³/min). NOT Building 1024.
- Sheet 26: 2nd-4th FL A/C + Vent Plan, CIF building.
- Sheet 27: CIF 1st floor control plan and equipment schedule.
- Sheet 28: CIF Plumbing Fixture Schedule (TOTO fixtures: WC, lavatory, urinal) + details.
- Sheet 29: CIF 1st FL Plumbing Plan, 1:120 scale.
- Sheet 30: CIF Toilet Area Detail, 1:50 scale.
- Sheet 31: CIF 1st FL Sprinkler Plan, 1:100 scale.
- Sheet 32: CIF Sprinkler Misc Details (equipment list: 14 recessed heads, 112 upright heads).
- Sheet 33: CIF 1st FL Dock Leveler Plan. Equipment: Electro-hydraulic dock leveler,
  5-ton capacity, 1.829 x 1.005m, 3-phase 200V 4.7kW.

---

## SCH-1024 FLOOR PLAN DATA (MARKON CUI, Oct 2025)

Source: 1024_HE_Plus.pdf (FL1-FL2) and 1024_FL3and4_HE_Plus.pdf (FL3-FL4).
Markon / MCB Butler Asset Management Support. CUI. Dated 10/21/2025 (FL1-FL2), 10/17/2025 (FL3-FL4).
NOTE: FL2 header incorrectly labels site as "Camp Schwab." All other sources confirm Henoko. Not an error
in the estimate; do not correct. Match existing iNFADS/AE Worksheet site designation (HE Henoko).

Confirmed rooms by floor relevant to conversion scope:

FL1 (primary conversion floor):
- Mech Room 132 (center building, West): confirmed mechanical room location for AHU-1
- North Mech Room (implied from BUILDER AHU-2 tag): AHU-2 20,000 CFM location
- Boiler Room 146: confirmed boiler plant location (BH-1, BH-2, TE-1, fire pump)
- Armory 175, 176, 177: confirmed armory conversion zone (right wing, center)
- CIF 118: Central Issue Facility space confirmed (right wing)
- Fitness Room 142, Sauna 143, Steam Room (adjacent): gym-to-workspace conversion zone
- Men's Locker 138, Racquet Ball Court 130: OSS vault conversion zone
- Laundry 150, Office 154, Day Room 131: admin conversion zone

FL2: Predominantly BEQ rooms (201-271A series). Mech Room 225, Lounge 227, Laundry 250/259,
Conference Room 261.

FL3: All BEQ rooms (301-354 series). Mech Room 325, Laundry 327, Linen 329, Lounge 330.

FL4: All BEQ rooms (401-454 series). Mech Room 425, Laundry 427, Linen 428, Lounge 430.

Conversion scope footprint confirmation: All G1-G6 conversion groups are contained on FL1.
FL2-FL4 are BEQ residential floors. The conversion does not affect FL2-FL4 room layouts
based on current scope. AHUs on FL2-FL4 (AHU-3, AHU-4, AHU-5) serve those floors independently.

---

## SCH-1024 OPEN ITEMS (23 Mar 2026)

These items are documented as unresolved. All require external input before next estimate revision.
Do not close any of these without a confirmed source.

1. CHILLED WATER PUMPS CP-1/CP-2: Not a discrete line item in current estimate. Confirm with
   mechanical engineer whether replacement is concurrent with chiller R&R or retained.

2. VRF UNITS ACP-1, ACP-2, ACP-3, FAP-1, FAP-2: All CI 30, all past RSL. None in estimate.
   Mechanical engineer must confirm zone assignments and whether conversion-occupied zones depend on
   any of these units. Scope determination required.

3. FIRE ALARM D40 ($10,000 PLACEHOLDER): Monaco M Series CI 67, RSL expired. Mechanical engineer must
   confirm whether NFPA 72 compliance work is triggered by occupancy reclassification. $10,000
   is insufficient if full compliance work is required.

4. EXHAUST FANS (7 PAST RSL): Mechanical engineer to confirm whether conversion boundary overlaps
   any zones served by EF-1, EF-2, EF-3, EF-4, Roof EF, North Wall EF, South Wall EF.

5. CCN 44110 (867 SF) FAC ALLOCATION: Not mapped to a discrete PARAMETERS row. Likely rolled
   into FAC 4421 block but not confirmed. Verify with RPAO or PARAMETERS before next revision.

6. FAC 4427 GSF DOCUMENTATION: 7,142 SF (post-conversion programmatic) vs 993 SF (iNFADS CCN
   14345). Section F Item 11 must explicitly state this is post-conversion programmatic SF.
   Confirm this language is in the current estimate before submission.

7. VAULT COUNT CONFIRMATION: G1 states 28 BEQ rooms to 14 armory vaults. Conversion design
   drawings needed to confirm. No drawings in current project directory confirm this count.

8. WINDOW BARS ROOMS 245-250: 10 EA placeholder. Not confirmed from any drawing in project
   directory. Field count required.

9. JPY RATE (PARAMETERS B57): Must be pulled from Federal Reserve H.10 on PAX submission date.
   Permanent yellow item in all estimates. Do not submit without updating.

10. ABATEMENT HISTORY: PWD Environmental Division confirmation of post-2001 abatement work for
    Building 1024 is a standing requirement across the full package before submission. Bhate
    survey is 24+ years old. The 8,392 LF mastic finding (H3, 15% Chrysotile) in G11 is based
    on that survey. Current conditions unconfirmed.

---

## SCH-1024 ARMORY BACKUP POWER FINDING (Locked 25 Mar 2026)

**Position:** No blanket generator mandate exists for Marine Corps armories. The requirement is
conditional on a written Installation CO determination documented in DD 1391 Block 11.

**Regulatory chain (all sources confirmed):**

| Authority | Finding |
|-----------|---------|
| OPNAVINST 5530.13D | Governs Navy arms, ammunition, and explosives safety. Does not mandate backup power for armories. |
| MCO 5530.14A | Marine Corps physical security manual. No blanket generator requirement for armories. |
| UFC 4-215-01 | Arms and ammunition storage facility design guide. Generator provision is described as conditional, not mandatory. |
| UFC 3-540-01 Change 4 | Emergency power systems. Identifies facility categories requiring emergency power. Armories are not in the mandatory list without additional mission criteria. |

**The conditional trigger:** Installation CO may determine that a specific armory mission requires
backup power (e.g., 24/7 IDS monitoring without grid-tie fail-safe, remote locations with poor
grid reliability). That determination must be written and documented in DD 1391 Block 11. Without
that determination, generator and ATS scope has no documentary basis for inclusion.

**Active installation examples confirming the position (verified 25 Mar 2026):**
- Camp Foster Building 225: active armory, operating without backup generator
- Camp Hansen Building 2203: active armory, operating without backup generator

**Application to portfolio:**
SCH-1024 (armory conversion) does NOT include a generator or ATS in the current v11 estimate.
SCH-3237 (armory wing) does NOT include a generator or ATS in the current v4 estimate.
Both are correctly scoped absent a written Installation CO determination directing otherwise.
If either building's DD 1391 is challenged on backup power during FEAD review, cite this finding.

If an Installation CO determination is made: the scope addition is approximately $45,000-$65,000
Base Direct for a 45kW diesel generator set with ATS and transfer switch gear (RS Means FY24 CONUS,
26 31 16, sized for security lighting and IDS only). This would require a yellow flag and new
Block 11 language citing the CO determination. It does NOT affect the ERC ratio materially for
either building given their current ratios (1024 at 10.4%, 3237 at 5.1%).

---

---

### SCH-3213 (CLB-4 BN HQ Conversion -- Formula PRV, Post-Conversion FAC)
Status: v6 (20 Mar 2026) -- LARGEST SCOPE IN PORTFOLIO. 73 items. Full HVAC + plumbing replacement.
**REQUIRES v7 UPDATE: PRV method change from iNFADS to formula. LSH, all adders, Total Funded,
Total Project, Block 9, and Section F Item 11 must be rebuilt.**
3-column ESTIMATE layout (A=element, B=amount, C=formula/source).
GSF: 13,484 SF | PAX: 387624 | Fi Web: BU26PPE72M | CCN: 61010 (NOT 61071) | RPUID: 48879
Delivery: Design-Build (DB)

**PRV Method: FORMULA (post-conversion per G-30)**
Building is converting from Field Maintenance Shop (Property Record FAC 2171/6102) to
CLB-4 Battalion HQ. DD 1391 programs BN HQ. Property Record PRV reflects the old use.
Formula PRV with post-conversion FAC 6101 (Small Unit HQ) governs per G-30.

Property Record Current PRV: $9,929,006 (RPUID 48879, pull date 26 Mar 2026) -- reference only
AE Worksheet PRV at EOY: $10,893,334 (evaluation date 04 Mar 2024) -- reference only
Property Record FAC codes: 6102 (5,148 SF) + 2171 (8,336 SF) = 13,484 SF

**Post-Conversion Formula PRV (2-FAC per G-30/G-34):**
Source: Property Record utilization breakdown (18 Feb 2026, RPUID 48879)
HQ side (FAC 6101): 5,148 SF x $634/SF = $3,263,832
Bay side (FAC 2171): 8,336 SF x $232.17/SF = $1,935,369
Q x PUC Total: $5,199,201
x ACF 1.85 x Combined 1.23606 = **$11,887,376**
LSH: $11,887,376 x 2.5% = **$297,184**

ERC Ratio: $5,190,315 / $11,887,376 = 43.7% -- MONITORING (below 50%, ERC SENSITIVE per G-32)
Headroom to 50%: $753,373. +30% scenario breaches 50% at 56.8%.

**v6 values (STALE, will change at v7):** LSH currently $272,333 (iNFADS basis).
At v7 with formula PRV: LSH increases to $297,184 (+$24,851). All downstream values change.

PARAMETERS rows (3213-specific): B18=ACF | B19=Escal Rate | B20=Escal Yrs | B21=Compound Escal Factor
=(1+B19)^B20 | B22=GenReq | B23=Contingency | B24=LSH Rate | B25=Design | B26=SIOH | B27=CM |
B28=DB Design | B29=Total GSF | B33=JPY | B38=PRV (**MUST UPDATE to $11,887,376**) | B40=LSH (**MUST UPDATE to $297,184**)

**Mechanical scope basis (MCIPAC-GF/PMO planner, 19 Mar 2026):**
- HVAC: 1984 central chilled water system; 2019 partial replacement only; ductwork/diffusers original 1984 past ASHRAE 30-yr service life. Full replacement.
- Plumbing: 1984 cast iron DWV; 2004 water heater past service life; abandoned hot water system (boiler B-1, piping, tanks EWT-1/2). Full DWV and domestic water replacement.
- Compressed air: appears abandoned -- remove system.
- Roof ventilators RF-1 through RF-6 plus additional: non-functioning. 9 EA field-counted.
- Air curtains: non-functioning. 2 EA confirmed (end of each hallway).
- Overhead roll-up doors: 1980s vintage past life expectancy. 5 EA confirmed per floor plan Sheet 7-36.

**HAZMAT basis (Bhate Environmental Associates 2001, NVLAP accredited PLM):**
ONE confirmed ACM: H2 rose 12x12 floor tile, 570 SF, Corridor 100/Rooms 8 and 23, 4% Chrysotile,
non-friable, good condition. All other samples negative. Survey 25 years old -- re-inspection required.

**v6 LOCKED VALUES (20 Mar 2026 -- from CEPBKUP file direct read):**
Base Direct: $1,731,889 | Constr Subtotal: $4,126,239 | LSH: $272,333
Const Base: $4,398,572 | Design: $263,914.32 | SIOH: $351,885.76 | CM: $175,942.88
Total Funded: $5,190,315 | DB Design: $207,612.60 | Total Project: $5,397,927.60

**UNIFORMAT codes (6 codes -- SUMIF ranges confirmed):**
B20 $33,300 | C10 $340,598 | D20 $436,952 | D30 $605,854 | D50 $211,525 | F10 $103,660
Total check: $1,731,889

NOTE: ESTIMATE uses A-column for row numbers (A5, A6...) and B-column for element text.
Section D header: "D. UNIFORMAT II LEVEL 2 SUMMARY (BASE DIRECT COSTS)"
UNIFORMAT B column label: "Base Direct ($)" not "Base Direct Cost"

**73 items / 11 groups:**
G1 (row 4) -- TELECOM INFRASTRUCTURE MODERNIZATION (D50, items 1-6, rows 5-11)
G2 (row 12) -- S-2 VAULT CONSTRUCTION - TWO VAULT SPACES (C10, rows 13-19)
G3 (row 20) -- SIPR NETWORK RACK INSTALLATION (D50, rows 21-25)
G4 (row 26) -- PATHWAY - BN CONFERENCE ROOM TO S-2 VAULT (C10, rows 27-33)
G5 (row 34) -- CONSTRUCT 6 PRIVATE OFFICES (C10, rows 35-43)
G6 (row 44) -- EOD OFFICE PARTITION (C10, rows 45-52)
G7 (row 53) -- CONSTRUCT SECURE STORAGE - UNIT MAIL ROOM (C10, rows 54-59)
G8 (row 60) -- HAZARDOUS MATERIALS - SURVEY AND ABATEMENT (F10, rows 61-66)
G9 (row 67) -- HVAC FULL SYSTEM REPLACEMENT (D30, rows 68-82)
G10 (row 83) -- PLUMBING FULL REPLACEMENT AND RESTROOM RENOVATION (D20, rows 84-94)
G11 (row 95) -- OVERHEAD DOORS AND AIR CURTAINS (B20, rows 96-98)
Grand total row 99: fill FF1B2A4A (dark navy, white text) -- TOTAL BASE DIRECT COST

**DD1391_BLOCK9 child lines (from CEPBKUP file, confirmed values):**
| Line | Description | Amount ($000s) | UNIFORMAT |
|------|-------------|----------------|-----------|
| 1 | Telecom Infrastructure Modernization | 346.547 | D50 |
| 2 | S-2 Vault Construction -- 2 Vault Spaces | 310.155 | C10 |
| 3 | SIPR Network Rack Installation | 97.466 | D50 |
| 4 | Pathway -- Bn Conference Room to S-2 Vault | 47.000 | C10 |
| 5 | Construct 6 Private Offices | 265.758 | C10 |
| 6 | EOD Office Partition | 68.876 | C10 |
| 7 | Construct Secure Storage -- Unit Mail Room | 45.917 | C10 |
| 8 | Hazardous Materials -- Survey and Abatement | 224.519 | F10 |
| 9 | HVAC Full System Replacement | 1,312.229 | D30 |
| 10 | Plumbing Full Replacement and Restroom Renovation | 960.534 | D20 |
| 11 | Overhead Doors and Air Curtains | 72.125 | B20 |
| Subtotal | | 3,751.126 | |
| Contingency 10% | | 375.113 | |
| LSH 2.5% | | 272.333 | |
| Design 6% | | 263.914 | |
| SIOH 8% | | 351.886 | |
| CM 4% | | 175.943 | |
| TOTAL FUNDED | | 5,190.315 | |
| DB Design 4% | | 207.613 | |
| TOTAL PROJECT | | 5,397.928 | |

**Version history (locked from ESTIMATE tab):**
- v1-v4 (06 Mar 2026): superseded; CCN corrections, HAZMAT additions, CM added
- v5 (19 Mar 2026): Full HVAC, plumbing, overhead doors/air curtains added. Base Direct $1,731,889.
- v6 (20 Mar 2026) CURRENT: Scope confirmed -- items 47, 58, 72, 73 confirmed hard scope. JPY only yellow.

**Section F (13 items, inline ESTIMATE tab -- col A labels, col B text):**
Format: A46="1. Estimate Level" | B46=text (no separate label column; 2-column layout)
Item 12: "Anthony L. Potter  |  Facilities Professional  | MCIPAC G-F PPE  |  20 March 2026"
Note: Item 12 uses single space before MCIPAC (not double pipe space) -- match exactly.

---

## SCH-3213 OPEN ITEMS (27 Mar 2026)

1. V7 REBUILD REQUIRED: PRV method changed from AE Worksheet ($10,893,334) to formula method
   ($11,887,376) per v23.0. LSH increases from $272,333 to $297,184 (+$24,851). All downstream
   values change: Construction Base, Design, SIOH, CM, Total Funded, Total Project, Block 9.
   Do not submit v6 to PAX. Rebuild to v7 using formula PRV before submission.

2. OVERHEAD DOOR UNIT COST (G11): $5,500/EA (RS Means FY24 CONUS, 08 33 23) challenged
   as potentially understated for OCONUS execution. No adjustment documented. A 30% premium
   scenario produces $7,150/EA. If a vendor quote or subject matter expert confirmation is
   obtained, update accordingly and cite in Col J. Per G-36, do not lock without OCONUS
   reasonableness review. See G-36 for full rule.

3. WORKBENCH SCOPE DECISION (Pending): Built-in workbench assemblies in Rooms 112-118 (bay
   side) are steel-framed structures with dedicated Panel L-2 branch circuits and ceiling-level
   busway (PB 500x500x200, PB 500x600x200). Confirmed 80 wall-mounted metal shelves across
   five rooms (Drawing 27-36). Memo delivered to Mechanical Engineer (G-F) March 2026.
   Potential scope addition: ~$14,120 Base Direct for bench demolition, electrical demo,
   busway removal. Client direction required before adding to estimate.

4. ACM RE-INSPECTION: Bhate survey (2001) is 25 years old. Full HVAC and plumbing replacement
   in scope (Groups 9 and 10) will disturb the full building. PWD Environmental Division
   confirmation of current conditions required before finalizing Block 12 language.

5. JPY RATE (PARAMETERS B33): Permanent yellow item. Confirm from Federal Reserve H.10 on
   PAX submission date. FY26 DoD President's Budget rate is 150.4415 JPY/USD (FCF,D
   appropriation table, FY26). This is the budget formulation rate only -- H.10 governs
   for PARAMETERS B33.

6. FLOOR 2 HEU COUNT: Mechanical Engineer (G-F) flagged HEUs on Floor 2 (25 Mar 2026 Teams
   thread). Drawing 111374 is the authoritative source. Count and room locations unconfirmed.
   Affects G5 scope and Block 10 Floor 2 paragraph when resolved.

**SCH-3213 FIRE ALARM CONFIRMED FACTS (03 Apr 2026 drawing reads -- AS-BUILT 1983):**

Sheet 20-20 (DMS file 11804.tif): スプリンクラー配管平面図 (Sprinkler Piping Plan).
Contractor: 現代空調 (Air Conditioning Plumbing and Engineering). Scale 1:100, 昭和58年.
Circle symbols in room interiors are sprinkler heads (上向き/下向き). Alarm valve detail
at lower left shows ウォーターモータゴング (Water Motor Gong) at FL+2600, アラーム弁
(Alarm Valve) 125A at FL+1500, 送水口 (Siamese Connection) 65x65x125A at GL+850.
This drawing is part of the SPRINKLER SYSTEM, not the fire alarm system.

Sheet 15-19 (DMS file 11819.tif): 自動火災報知設備配線図 (1st Floor Fire Alarm System Layout).
Project: シュワブ(57)機器整備場新設電気工事. Scale 1:100, 昭和58年2月. 3 circuit zones.
Wire: HIV1.2x8(E19), HIV1.2x9(E25). Found in S2P1 page 9 of as-built archive.

Sheet 14-19 (S2P1 page 12 of as-built archive): 自動火災報知設備系統図 (Fire Alarm System
Diagram). Same project and contractor. Contains legend. Legend confirmed:
- Plain circle (○): 定温式スポット型感知器 (Fixed Temperature Spot Type) 1st class 75°C
- Circle with bar (日): 差動式スポット型感知器 (Rate-of-Rise Detector Spot Type) 2nd class
- Ditto small: 同上防水型 (Ditto Water-Proof Type)
- Square (■): 光電式煙感知器 (Optical Smoke Detector Spot Type) 2nd class
- Circle with crosshair (⊙): 発信机 (Manual Fire Alarm Box) P-TYPE 1st class
- Circle with dot (◎): 表示灯 (Location Lamp) AC24V
- Bell symbol: 火災警報ベル (Fire Alarm Bell) DC24V 15mA φ150
- Triangle: 終端抵抗 (End of Line Resistor) 10KΩ
- Fire Control Panel: P-TYPE 1st class 5 zones
System has been upgraded from original bells to horn/strobes at unknown date after 1983
(per Robert Beller message 03 Apr 2026 -- field condition, not drawing-confirmed per G-47).

Detector positions from Sheet 15-19 (03 Apr 2026 read at 5x resolution):
- 研修室No.2 (Class Room No.2): 1 detector at corridor threshold near Y2 gridline
- 保管室No.1 (Dehumid Storag No.1): NO dedicated interior detector. Corridor coverage only.
- 部品及び工事室 (Spare and Tools Room): NO dedicated interior detector. Corridor coverage only.
- 管理室No.1 (Admin No.1): 1 detector inside room
- 管理室No.2 (Admin No.2): 1 detector inside room
- 解読室 (Crypto Room): 1 detector inside room
- 検査室 (Radio Testing Room): 1 detector inside room
- 整備室 (Maintenance Room): 6 detectors on loop (large bay, Circuit Zone 3)
FPE field verification required for all rooms affected by proposed partition scope.
EOD partition coverage cannot be confirmed without cross-check against partition wall
position relative to existing detectors (G-45).

--- (Warehouse / Armory -- Multi-FAC, iNFADS PRV)
Status: v4 (09 Mar 2026) -- CURRENT. NOTE: 4 yellow-flagged items remain open. NOT G-22 complete.
NOT submission-ready. See yellow flags below.
3-column ESTIMATE layout (A=element, B=amount, C=formula/source).
GSF: 30,973 SF | PAX: 387622 | Fi Web: BU26PPE73M | CCN: 44112 | RPUID: 51473
Primary CCN: 44112 (Covered Storage Building). Armory wing CCN: 14345.
Delivery: Design-Build via FEAD (DB)

**PRV Method: Property Record confirmed (non-conversion per G-30)**
Property Record Current PRV: $27,656,160 (RPUID 51473, pull date 26 Mar 2026)
AE Worksheet PRV at EOY: $26,636,215 (evaluation date 04 Mar 2024) -- reference only
LSH: $691,404 (= $27,656,160 x 0.025; hardcode per G-24)
**v4 LSH was $665,905 (based on AE Worksheet PRV). MUST UPDATE at next revision.**

Property Record FAC allocations (confirmed from Property Record 19 Feb 2026):
FAC 4427: 6,406 SF (Armory, CCN 14345)
FAC 4421: 19,304 SF (Covered Storage, CCN 44112) -- corrected from prior 16,895 SF
FAC 6100: 5,263 SF (Admin Office, CCN 61010)
Total: 30,973 SF (confirmed, no gap)

Formula cross-check (Section F Item 11 only -- Property Record governs):
FAC 4427 (6,406 SF x $428.28) + FAC 4421 (19,304 SF x $692) + FAC 6100 (5,263 SF x $982)
= $21,270,196 x ACF 1.85 = $39,349,862 x Combined 1.23606 = $48,638,790
Delta: Property Record $27,656,160 is $20,982,630 lower than formula. This is a significant
delta (43%). Property Record may not yet reflect current PUC cycle for all three FAC codes.
RPAO owns the methodology. Document and move on.

ERC Ratio: $1,399,544 / $27,656,160 = 5.1% -- CLEAR (well below 50%)

PARAMETERS row layout (3237-specific -- confirmed from file):
B7=PAX ID | B8=Fi Web | B9=CCN | B10=Estimate Date | B11=Estimate Level | B12=Delivery Method
B16=Base Yr | B17=Target FY | B18=ACF (1.85) | B19=Escal Rate (0.021) | B20=Escal Yrs (3)
B21=Compound Escal Factor =(1+B19)^B20 | B22=GenReq (0.10) | B23=Contingency (0.10)
B24=LSH Rate (0.025) | B25=Design (0.06) | B26=SIOH (0.08) | B27=CM (0.04) | B28=DB Design (0.04)
B29=Total GSF (30,973) | B33=JPY (156.05 -- Federal Reserve H.10 27 Feb 2026)
B37=RPUID (51473) | B38=PRV iNFADS ($26,636,215) | B39=Implied $/SF check =B38/B29/B18
B40=LSH =ROUND(B38*B24,0)

**v4 LOCKED VALUES (09 Mar 2026 -- from CEPBKUP file direct read):**
Base Direct: $218,320 | Constr Subtotal: $520,149 | LSH: $665,905
Const Base: $1,186,054 | Design: $71,163.24 | SIOH: $94,884.32 | CM: $47,442.16
Total Funded: $1,399,544 | DB Design: $55,981.76 | Total Project: $1,455,525.76

NOTE: Prior skill versions showed Base Direct $217,280 and Total Funded $1,396,620. Those values
are WRONG -- they were from an earlier version. The CEPBKUP file confirms $218,320 and $1,399,544.

**UNIFORMAT codes (4 codes):**
C10 $48,100 | D30 $4,500 | D50 $107,000 | F10 $58,720
Total check: $218,320

**6 scope groups (from SCOPE_DETAIL row structure):**
G1 (row 2) -- STORAGE RECONFIGURATION - Remove/Replace Floor-to-Ceiling Wire Mesh Cage Partitions, Room 101 (C10, rows 3-4)
G2 (row 6) -- TELECOMMUNICATIONS ROOM - INTERIOR CONSTRUCTION - New TR per UFC 3-580-01 (C10, rows 7-9)
G3 (row 11) -- TELECOMMUNICATIONS ROOM - HVAC - Dedicated A/C per UFC 3-580-01 (D30, rows 12)
G4 (row 14) -- TELECOMMUNICATIONS ROOM - ELECTRICAL - Dedicated Panel and Wiring (D50, rows 15-17)
G5 (row 19) -- COMMUNICATIONS INFRASTRUCTURE MODERNIZATION - Full Facility Scope (D50, row 20)
G6 (row 22) -- HAZMAT - ACM MASTIC ABATEMENT - Bhate Environmental Survey 11/29/2001 (F10, rows 23-27)
Grand total row 29: fill FFBDD7EE (light blue column headers fill) -- TOTAL BASE DIRECT COST

SCOPE_DETAIL header row 1: "SCH-3237  |  SCOPE DETAIL & QUANTITY TAKEOFF  |  BASE YEAR FY24 CONUS  |  Level 3 ROM  |  CCN 44112"
NOTE: This tab omits "DIRECT COSTS" and "Fi Web" from the title -- matches the file exactly.
DD1391 tab header row 1: "SCH-3237  |  DD FORM 1391 BLOCK 9  |  LEVEL 3 ROM  |  FY27  |  PAX ID 387622  |  Fi Web BU26PPE73M"
NOTE: 3237 DD1391 tab uses "DD FORM 1391 BLOCK 9" header format, NOT "COST ESTIMATE PARAMETERS".

**YELLOW FLAGS (4 items -- NOT G-22 complete):**
a. Items 1-2: cage dimensions and linear footage not confirmed; pending floor plan and unit layout
b. Item 10: comm infrastructure ROM preliminary; additional site survey required (unit items blocked TR access)
c. Item 12: PWD ENV has not confirmed whether Room 101 flooring was replaced after 2001 Bhate survey
d. JPY rate: 156.05 from Fed H.10 27 Feb 2026 (next release 09 Mar 2026); confirm before PAX submission

**DD1391_BLOCK9 child lines (from CEPBKUP file, confirmed values):**
| Line | Description | Amount ($000s) | UNIFORMAT |
|------|-------------|----------------|-----------|
| [C10] 1 | Storage Reconfiguration - Cage Removal and New Partitions, Room 101 | 64.977 | C10 |
| [C10] 2 | Telecommunications Room - Interior Construction (Walls, Backboards, Door) | 39.203 | C10 |
| [D30] 3 | Telecommunications Room - Dedicated HVAC (Independent 24/7 A/C, UFC 3-580-01) | 9.747 | D30 |
| [D50] 4 | Telecommunications Room - Electrical Infrastructure (Panel, Receptacles, Cable Tray) | 15.161 | D50 |
| [D50] 5 | Communications Infrastructure Modernization (EMT, Cat6 NIPR/SIPR, WAO, Cabinet, Testing) | 216.592 | D50 |
| [F10] 6 | HAZMAT - ACM Mastic Abatement (Bhate Environmental Survey 2001; H2 Chrysotile; Room 101 + Hallway) | 127.183 | F10 |
| Subtotal | | 472.863 | |
| Contingency 10% | | 47.286 | |
| LSH 2.5% | | 665.905 | |
| Design 6% | | 71.163 | |
| SIOH 8% | | 94.884 | |
| CM 4% | | 47.442 | |
| TOTAL FUNDED | | 1,399.544 | |
| DB Design 4% | | 55.982 | |
| TOTAL PROJECT | | 1,455.526 | |
Additional rows: "Planning and Design (0%) (NON ADD): $0" + Classification of Work rows (CRM/SRM both = $1,399.544)

**Formula cross-check (Section F Item 11 -- Property Record governs, this is cross-check only):**
Formula PRV: FAC 4427 (6,406 SF x $428.28) + FAC 4421 (19,304 SF x $692) + FAC 6100 (5,263 SF x $982)
= $21,270,196 x 1.85 ACF = $39,349,862 x Combined 1.23606 = $48,638,790
FAC 4421 GSF corrected to 19,304 SF per Property Record (19 Feb 2026). Prior estimate used 16,895 SF.
Full Eq 3-1 must be cited in updated Section F Item 11 at next revision.

**Section F (13 items -- col A labels, col B text, same 2-column layout as 3213):**
Item 12: "Anthony L. Potter | Facilities Professional | Booz Allen Hamilton - MCIPAC G-F PPE | 09 Mar 2026"

**HAZMAT (Bhate Environmental Survey 11/29/2001, NVLAP accredited, Lab: Analytica Solutions):**
ACM mastic confirmed: H2 -- tan mastic beneath brown floor tile, hallway and Room 1, ~5,590 SF, 5% Chrysotile.
Armory wing (Rooms 115-127, 6,406 SF, CCN 14345) EXCLUDED from construction scope per Decision Point 5.
PRV/LSH still include full building.

**Version history (locked from ESTIMATE tab):**
- v3 FINAL (prior): Total Funded $1,520,939 -- pre-scope confirmation, CCN for TR unresolved
- v4 (09 Mar 2026) CURRENT: $1,399,544 -- 15-item worklist; TR scope UFC 3-580-01 confirmed; Fi Web confirmed

---

---

### SCH-3270 (Auto Organizational Shop -- iNFADS PRV -- PRIMARY COLOR/COSMETIC STANDARD)
Status: v9 (19 Mar 2026) -- CURRENT. Submission-ready. JPY only yellow item (G-22 complete).
4-column ESTIMATE layout: A=row number, B=element, C=amount ($), D=formula/source.
GSF: 25,390 SF | PAX: 387568 | Fi Web: BU26PPE74M | CCN: 21451 | RPUID: 1174058
PUC: $810/SF (FAC 2141 Vehicle Maintenance Shop -- UFC 3-701-01 C7 Table 3, direct read)
Construction year: 2010 | PIS: 04 Jun 2013 | GOJ-owned (FMRA INGRANT ID 1277)
BUILDER NFA ID: NFA200001061770 (BUILDER ID only -- NOT the PAX RPUID)
Supported units: 4th MarRegt (M13201) + CLB-4 (M29030)
Delivery: Design-Build (DB)

**PRV Method: Property Record confirmed (non-conversion per G-30)**
Property Record Current PRV: $45,526,139 (RPUID 1174058, pull date 26 Mar 2026)
AE Worksheet PRV at EOY: $39,507,617 (evaluation date 04 Mar 2024) -- reference only
LSH: $1,138,153 (= $45,526,139 x 0.025; hardcode per G-24)
**v9 LSH was $987,690 (based on AE Worksheet PRV). MUST UPDATE at next revision.**

ERC Ratio: $3,392,070 / $45,526,139 = 7.5% -- CLEAR (well below 50%)

**PARAMETERS row layout (3270-specific -- DIFFERS from 1024/3213/3314):**
CRITICAL: 3270 PARAMETERS has a different row structure. The compound escalation factor is B39
(not B21 as in other buildings). Always read row positions from the file -- do not assume.

B18=ACF (1.85) | B19=Escal Rate (0.021) | B20=Escal Yrs (3) | B21=GenReq (0.10)
B22=Contingency (0.10) | B23=LSH Rate (0.025) | B24=Design (0.06) | B25=SIOH (0.08)
B26=CM (0.04) | B27=DB Design (0.04) | B31=Total GSF (25,390) | B32=RPUID (1174058)
B33=PRV ($39,507,617) | B34=LSH ($987,690) | B35=PUC FAC 2141 ($810)
B39=Compound Escalation Factor = =(1+B19)^B20 (live formula -- row 39, NOT row 21)
B41=JPY rate (BLANK -- yellow; confirm Federal Reserve H.10 at PAX submission)

ESTIMATE cross-refs: C4=SCOPE_DETAIL!G{gt_row} | C9=PARAMETERS!B34 (LSH)
C6 uses escalation: =C5*PARAMETERS!B39 (note: B39 not B21 for this building)

Formula cross-check (Section F Item 11 -- Property Record governs):
25,390 SF x $810/SF = $20,565,900 x ACF 1.85 = $38,046,915 x 1.23606 = $47,027,990
Delta: Property Record $45,526,139 is $1,501,851 (3.2%) lower than formula. Minimal delta.
AE Worksheet was $39,507,617, which was $7,520,373 (16.0%) lower than formula.
Property Record update closed most of the gap. RPAO appears to have applied current PUCs.
iNFADS LSH (Property Record basis): $1,138,153 | Formula LSH: $1,175,700 | Delta: $37,547
BUILDER GSF discrepancy: BUILDER shows 24,529 SF; iNFADS shows 25,390 SF (861 SF delta).
BUILDER = net modeled interior footprint; iNFADS = gross architectural footprint at capitalization.

**v9 LOCKED VALUES (19 Mar 2026 -- from CEPBKUP file direct read):**
Base Direct: $792,000 | Constr Subtotal: $1,886,946 | LSH: $987,690
Const Base: $2,874,636 | Design: $172,478.16 | SIOH: $229,970.88 | CM: $114,985.44
Total Funded: $3,392,070 | DB Design: $135,682.80 | Total Project: $3,527,752.80

**UNIFORMAT codes (6 codes):**
B20 $22,000 | C10 $43,000 | C30 $17,500 | D20 $18,800 | D30 $504,800 | D50 $185,900
Total check: $792,000

Section D header (4-column): "D. UNIFORMAT II LEVEL 2 SUMMARY - Base Direct Cost (FY24 CONUS Pre-ACF)"
UNIFORMAT column D has "Description / Items" header (4th column).
Total check row label: "TOTAL BASE DIRECT COST (FY24 CONUS)" at fill FFD6DCE4.

**42 items / 10 groups:**
G1 (row 4) -- MECHANICAL - HVAC ACP SYSTEM REPLACEMENT - 7 Outdoor Units + 24 Indoor Fan Coils + Infrastructure (D30, rows 5-20)
G2 (row 21) -- MECHANICAL - DOAS FRESH AIR SYSTEMS - 4 Units + Ductwork Evaluation (D30, rows 22-27)
G3 (row 28) -- MECHANICAL - EXHAUST SYSTEMS - 22 General Fans + 10 Hose Reels + Welding Exhaust Restore + RM114 Removal (D30, rows 29-33)
G4 (row 34) -- MECHANICAL - BATTERY ROOM - RM102 Ventilation and Conditioning Upgrade (D30, rows 35-36)
G5 (row 37) -- MECHANICAL - COMPRESSED AIR - RM119 System Inspection and Repair (D30, rows 38-39)
G6 (row 40) -- PLUMBING - Safety Stations and Fixtures (D20, rows 41-43)
G7 (row 44) -- EXTERIOR DOORS - Roll-Up Door Inspection and Repair (B20, rows 45-46)
G8 (row 47) -- ELECTRICAL - LIGHTING REPLACEMENT - 94 Confirmed Fixtures + Motion Sensors (D50, rows 48-53)
G9 (row 54) -- COMMUNICATIONS - Cat6 NIPR Infrastructure + MNS - 70 Drops + Both TRs (D50, rows 55-59)
G10 (row 60) -- ARCHITECTURAL - Interior Repairs and Remediation (C10/C30, rows 61-66)
Grand total row 67: fill FF1B2A4A (dark navy title bar fill) -- "TOTAL BASE DIRECT COST (FY24 CONUS)"

**DD1391_BLOCK9 (6 consolidated UNIFORMAT child lines -- confirmed from file):**
| Line | Description | Amount ($000s) | UNIFORMAT |
|------|-------------|----------------|-----------|
| 1 | Exterior Doors - Roll-up door inspection and repair (22 EA) | 47.650 | B20 |
| 2 | Interior Construction - Wall repair, anchor wire cables, restroom remediation | 93.134 | C10 |
| 3 | Interior Finishes - Ceiling tile replacement (2,500 SF) | 37.904 | C30 |
| 4 | Plumbing - Emergency safety stations and 2F water cooler | 40.719 | D20 |
| 5 | Mechanical HVAC - ACP replacement, DOAS, exhaust systems, battery room, compressed air | 1,093.354 | D30 |
| 6 | Electrical / Communications - Lighting, Cat6 NIPR drops, TR upgrades, MNS | 402.644 | D50 |
| Subtotal | | 1,715.406 | |
| Contingency 10% | | 171.541 | |
| LSH 2.5% | | 987.690 | |
| Design 6% | | 172.478 | |
| SIOH 8% | | 229.971 | |
| CM 4% | | 114.985 | |
| TOTAL FUNDED | | 3,392.070 | |
| DB Design 4% | | 135.683 | |
| TOTAL PROJECT | | 3,527.753 | |

NOTE: 3270 uses 6 consolidated UNIFORMAT child lines in DD1391_BLOCK9 (one per UNIFORMAT code).
The PAX Block 9 manual output uses 42 individual item lines (see PAX Block 9 section below).
These are different formats -- DD1391_BLOCK9 tab = consolidated; PAX manual entry = per item.

Classification of Work rows: Construction $3,392.07 (100% TF) | SRM $3,392.07 (100% SRM)
(NOTE: row 16 = TOTAL FUNDED; row 18 = CLASSIFICATION header; rows 19-20 = Construction/SRM)
No blank row between Total Funded and Classification in 3270 -- different from 3314.

**Version history (locked from ESTIMATE tab):**
- v8 (07 Mar 2026): $2,374,358 -- ACP units only, lighting, telecom
- v9 (19 Mar 2026) CURRENT: $3,392,070 -- full mechanical + DOAS + exhaust + plumbing + doors + comms + architectural

**Section F (13 items -- 4-column layout, item label in col B, text in col C):**
Format: B43="1. Estimate Level" | C43=text (4-column layout; differs from 2-column 3213/3237)
Item 12: "Anthony L. Potter  |  Facilities Professional  |  MCIPAC G-F PPE  |  19 Mar 2026"

---

---

### SCH-3314 (Battalion Squadron HQ -- iNFADS PRV -- SECTION F LABEL STANDARD)
Status: v3 (18 Mar 2026) -- PAX backup confirmed. Submission-ready per G-22. JPY only yellow item.
3-column ESTIMATE layout (A=cost element, B=amount, C=formula/authority).
SCOPE_DETAIL Group 7 uses sub-groups 7A, 7B, 7C (nested under G7 header).
GSF: 28,699 SF | PAX: 387433 | Fi Web: BU26PPE71M | CCN: 61072 | RPUID: 50931
Facility: Battalion Squadron Headquarters | PIS: 21 Jun 2007 | RPA Type: B
Supported: M13200 4MAR REGT 3MARDIV + M29030 CLB-4 | Delivery: Design-Build (DB)

**PRV Method: Property Record confirmed (non-conversion per G-30)**
Property Record Current PRV: $29,826,797 (RPUID 50931, pull date 26 Mar 2026)
AE Worksheet PRV at EOY: $29,826,797 (evaluation date 16 Apr 2020) -- same value, no change
LSH: $745,669.925 (PARAMETERS B40 = =B38*B24 -- LIVE FORMULA, not hardcoded integer)
NOTE: 3314 LSH is NOT hardcoded per G-24. The CEPBKUP file uses a live formula =B38*B24.
This produces $745,669.925. ESTIMATE B10 = =PARAMETERS!B40 = $745,669.925.
Total Funded rounds to $1,874,407. Verify this rounding does not cause a Block 9 mismatch.

ERC Ratio: $1,874,407 / $29,826,797 = 6.3% -- CLEAR (well below 50%)

PARAMETERS row layout (3314-specific -- confirmed from CEPBKUP file):
Rows 3-15: BUILDING IDENTITY section
B4='SCH-3314' | B5='387433' | B6='BU26PPE71M' | B7='61072' | B8='6101' (FAC code)
B9=634 (PUC) | B10='50931' (RPUID) | B11=28699 (GSF) | B13='Design-Build (DB)' | B15='16 March 2026'
Rows 17-29: ESTIMATE PARAMETERS section
B18=ACF (1.85) | B19=Escal Rate (0.021) | B20=Escal Yrs (3)
B21=Compound Escal Factor =(1+B19)^B20 | B22=GenReq (0.10) | B23=Contingency (0.10)
B24=LSH Rate (0.025) | B25=Design (0.06) | B26=SIOH (0.08) | B27=CM (0.04) | B28=DB Design (0.04)
B29=Total GSF (28,699)
Rows 31-33: JPY section
B33=JPY (1.56 -- PLACEHOLDER; YELLOW fill; verify before submission)
Rows 35-53: PRV AND LSH section
B38=PRV iNFADS ($29,826,797) | B39=Implied $/SF check =B38/B29/B18 | B40=LSH =B38*B24
Rows 42-53: PRV FORMULA CROSS-CHECK section (for F-11 only)
B43=$18,195,166 | B44=$33,661,057 | B45=HF 1 | B46=PD 1.09 | B47=SIOH 1.08 | B48=CF 1.05
B49=Combined Factor 1.23606 | B50=Formula PRV $41,607,086 | B51=Delta $11,780,289
B52=Formula LSH $1,040,177 | B53=LSH Delta $294,507

FAC code note: CCN 61072 has no direct Table 3 PUC entry. FAC 6189 exists in Table 2 but has
no Table 3 PUC. FAC 6101 (Small Unit HQ, $634/SF, 44,000 SF ref) is best-supported Table 3 proxy.
FAC 6102 ($473/SF, Large Unit HQ, 69,000 SF ref) MUST NOT be used -- wrong echelon.

**v3 LOCKED VALUES (18 Mar 2026 -- from CEPBKUP file direct read):**
Base Direct: $353,749.40 | Constr Subtotal: $842,811 | LSH: $745,669.925
Const Base: $1,588,480.925 | Design: $95,308.8555 | SIOH: $127,078.474 | CM: $63,539.237
Total Funded: $1,874,407 | DB Design: $74,976.28 | Total Project: $1,949,383.28

NOTE: Prior skill versions show LSH $745,670 (rounded integer). The file actually carries
$745,669.925 as a live formula result. Construction Base = $1,588,480.925 (not $1,588,481).
These are the exact values in the file. Match them precisely.

**UNIFORMAT codes (5 codes -- confirmed from ESTIMATE Section D):**
D30 $303,950 | C10 $26,599.40 | D50 $13,500 | F20 $2,700 | D20 $7,000
Total check: $353,749.40

**23 scope items, 8 groups (SCOPE_DETAIL row structure):**
G1 (row 4) -- HVAC: BUILDING-WIDE DIFFUSERS AND CEILING RESTORATION (rows 5-6, subtotal row 7)
G2 (row 8) -- HVAC: OFFICE DUCT MODIFICATIONS (ROOMS 105/106/107 CLUSTER) (rows 9, subtotal row 10)
G3 (row 11) -- HVAC: EXHAUST FAN REPLACEMENT (rows 12-14, subtotal row 15)
G4 (row 16) -- HVAC: SYSTEM TEST, ADJUST, AND BALANCE (TAB) (rows 17, subtotal row 18)
G5 (row 19) -- HVAC: DUTY GUARD ROOM SYSTEMS (ROOMS 102 AND 103) (rows 20-23, subtotal row 24)
G6 (row 25) -- MASS NOTIFICATION SYSTEM (rows 26, subtotal row 27)
G7 (row 28) -- VAULT AND SECRET STORAGE CONVERSION (3 sub-groups):
  7A (row 29) -- DEMOLITION (rows 30-31, subtotal row 32)
  7B (row 33) -- VAULT CONSTRUCTION AND PHYSICAL SECURITY (rows 34-35, subtotal row 36)
  7C (row 37) -- VAULT ELECTRICAL AND SECURITY INFRASTRUCTURE (rows 38-40, subtotal row 40... NOTE: confirm exact rows)
  NOTE: G7 uses sub-header rows within a parent group header. No single G7 subtotal row.
G8 (row 42) -- HVAC AND PLUMBING: AHU AND MECHANICAL ROOM REPLACEMENT, MECHANICAL ROOM 115 (rows 43-47, subtotal row 48)
Grand total: =SCOPE_DETAIL!G41 (per ESTIMATE B5 formula -- confirm actual grand total row)

**Confirmed building-wide quantities (from drawings and site visit):**
Diffusers: 78 total (FL1: 22, FL2: 56; type C2 ceiling diffuser)
Exhaust fans: 31 total in scope (25 standard + 5 sirocco + FE-7 confirmed $650/EA)
  Sirocco fans: FE-5 (Rm 115), FE-8 (Rm 118-2/3), FE-21 (Rm 221/221A), FE-22 (Rm 221A), FE-28 (Rm 241/242)
HEUs in current estimate: HEU-1 (Rm 102 Duty Hut) and HEU-2 (Rm 103 Duty Room) -- FL1 guard rooms only.
  OPEN ITEM: Mechanical engineer (G-F) flagged HEUs exist on Floor 2 as well (25 Mar 2026 Teams thread). FL2 HEU
  count and room locations are NOT confirmed from available drawings. Drawing 111374 (as-built
  ventilation equipment schedule) is the authoritative source. Mechanical engineer must confirm FL2 HEU
  count before estimate can be updated. When confirmed: add line items to G5 and revise Block 10
  language to "replace fresh air ventilation system throughout, Floors 1 and 2."
AHUs: AC-1 (5,100 CFM, $42,000/EA, SINKO MOD #SH-10 SER #06K-370-01) and AC-2 (14,545 CFM,
  $89,000/EA, SINKO MOD #SH-30 SER #06K-170-02). Both installed 2007. Both captured under
  Maximo WO 18843573 (recommended FY26). WO to be referenced in Section F Item 10 methodology notes.
ACP boundary (confirmed from FMB refrigeration/A/C maintenance, Camp Schwab): ACP-2 replaced by G-F
  (complete). ACP-3/4/5 scheduled for replacement under separate G-F action (NOT in this scope).
  Chiller excluded (good condition). Ductless splits in duty/bunk rooms less than 5 years old
  (confirmed G-F FMB, 25 Mar 2026) -- NOT in scope beyond guard room pair already estimated.
  Coordination: G-F building manager to confirm ACP replacement schedule with G-F FMB shop.
Window bars: 10 EA confirmed (Rooms 245-250)

**DRAWING FILE CLARIFICATION (confirmed 25 Mar 2026):**
3314_Full_DMS_Drawings.pdf is NOT a 3314-specific drawing package. It is a ZIP-packaged
collection containing MC-124 (Schwab Administrative Building) A/C mechanical drawings (sheets 1-29)
and MC-124 electrical drawings (sheets 30-58). Do NOT use this file to verify 3314 mechanical scope.
The actual 3314 as-built ventilation drawings (111374 fan schedule, 111377 ventilation plan) are
referenced in the estimate but are not available in the project directory in a readable format.
For 3314 mechanical drawing verification, the source is the CEPBKUP SCOPE_DETAIL notes and
direct input from the mechanical engineer (G-F).

**BLOCK 10/11 CORRECTIONS (25 Mar 2026 -- per G-27):**
Block 10 FL1 paragraph corrected: removed "removal of condensing unit, evaporator coils, and
associated piping" -- that language was from Decision Point 2 slide and is not in the estimate.
Correct language: AHU replacement (AC-1/AC-2, CHW units), mechanical room overhaul, DHW system,
guard room HVAC (splits + HEU replacement + fresh air system), building-wide diffusers/exhaust
fans/duct mods, TAB, MNS junction box.
Block 10 FL2 paragraph corrected: removed "removal of evaporator coils and associated refrigerant
piping" -- same root cause. Correct FL2 language: HVAC work limited to building-wide diffuser and
exhaust fan replacement; primary scope is vault/secure space reconfiguration.
Block 11 Current Situation addition: sentence added justifying diffuser, exhaust fan, and guard
room ventilation scope drivers -- these were missing from the original submission draft.

**DD1391_BLOCK9 (13 child lines -- confirmed from file, alphabetical by UNIFORMAT):**
| Line | Description | Amount ($000s) | UNIFORMAT |
|------|-------------|----------------|-----------|
| 1 | HVAC - Building-Wide Diffuser and Ceiling Restoration (78 diffusers, 78 ceiling patches) | 97.141 | D30 |
| 2 | HVAC - Office Duct Modifications, Converted Offices Rooms 105/106/107 Cluster | 25.991 | D30 |
| 3 | HVAC - Exhaust Fan Replacement Building-Wide (31 EA: 25 standard + 5 sirocco + 1 FE-7) | 63.678 | D30 |
| 4 | HVAC - Full Building Test, Adjust, and Balance (TAB) After All Work Complete | 38.986 | D30 |
| 5 | HVAC - Duty Guard Room Systems (Rooms 102 and 103): Minisplit R&R, Abandoned Equipment Removal, HEU R&R, Fresh Air | 63.678 | D30 |
| 6 | Mass Notification System (MNS) Junction Box Installation, Mechanical Room 115 | 3.249 | D50 |
| 7 | Vault Demolition: Remove SIPR Network Rack and Existing Vault Door (Rooms 209/210/211/212 Cluster) | 5.848 | F20 |
| 8 | Vault Construction: GSA Class V Vault Door (Corridor 251) and Security Bars on Windows (Rooms 245-250) | 57.612 | C10 |
| 9 | Vault Electrical and Security: SIPR Network Rack Installation and IDS Sensor Raceways (Rooms 245-250) | 25.991 | D50 |
| 10 | HVAC and Plumbing - AHU Replacement and Mechanical Room Overhaul, Mechanical Room 115 (AC-1 5,100 CFM, AC-2 14,545 CFM, Mech Room Peripheral Work) | 368.856 | D30 |
| 11 | Plumbing - Water Heater and DHW Recirculation Pump Replacement, Mechanical Room 115 (WHE 100 gal + 2 EA Inline Pumps) | 15.161 | D20 |
| SUBTOTAL (row 15) | | 766.192 | |
| Contingency 10% (row 16) | | 76.619 | |
| LSH 2.5% (row 17) | | 745.670 | |
| Design 6% (row 18) | | 95.309 | |
| SIOH 8% (row 19) | | 127.078 | |
| CM 4% (row 20) | | 63.539 | |
| TOTAL FUNDED (row 21) | | 1,874.407 | |
| DB Design 4% (row 22) | | 74.976 | |
| TOTAL PROJECT (row 23) | | 1,949.383 | |

NOTE: 3314 DD1391 has no Classification of Work rows in the CEPBKUP file -- only rows 3-23.
No blank row between child lines and SUBTOTAL. SUBTOTAL is row 15.
Contingency formula references B15 (the SUBTOTAL row), not B13 (last child line row).

**Version history (locked from ESTIMATE Section E):**
- v1 (16 Mar 2026): $1,378,343 -- initial ROM; 18 items; 7 groups
- v2 (16 Mar 2026): $1,375,953 -- FE-7 confirmed; window bars 10 EA confirmed
- v3 (18 Mar 2026) CURRENT: $1,874,407 -- Group 8 added (AC-1, AC-2, mech room overhaul, WHE, DHW pumps)

**Section F (13 items -- UNIQUE FORMAT: col A = "F-1" through "F-13" labels; col B = text):**
Section F uses F-1, F-2...F-13 label format (not "1. Estimate Level" etc.).
Row labels: A40="F-1 Estimate Level" through A52="F-13 Version History"
This differs from all other buildings. 3314 Section F starts at row 39 (header) then A40+.
Item 12: " Anthony L. Potter  |  Facilities Professional  |  Booz Allen Hamilton - MCIPAC G-F PPE  |  18 March 2026 "
(note: leading and trailing space characters in the actual cell value -- match exactly)

YELLOW FLAG: Only JPY rate remains (PARAMETERS B33 = 1.56 placeholder).

---

---

## PARAMETERS Tab Row Cross-Reference (Confirmed from CEPBKUP Files 21 Mar 2026)

CRITICAL: Each building's PARAMETERS tab has a different row layout. The compound escalation
factor, JPY row, and LSH row are NOT at the same row numbers across buildings. Always determine
the actual row number before writing any ESTIMATE or DD1391 formula that cross-references PARAMETERS.

| Parameter | SCH-1024 | SCH-3213 | SCH-3237 | SCH-3270 | SCH-3314 |
|-----------|----------|----------|----------|----------|----------|
| ACF | B18 | B18 | B18 | B18 | B18 |
| Escalation Rate | B19 | B19 | B19 | B19 | B19 |
| Escalation Years | B20 | B20 | B20 | B20 | B20 |
| **Compound Escal Factor** | **B21** | **B21** | **B21** | **B39** | **B21** |
| General Requirements | B22 | B22 | B22 | B21 | B22 |
| Contingency | B23 | B23 | B23 | B22 | B23 |
| LSH Rate | B24 | B24 | B24 | B23 | B24 |
| Design | B25 | B25 | B25 | B24 | B25 |
| SIOH (Program Adder) | B26 | B26 | B26 | B25 | B26 |
| CM | B27 | B27 | B27 | B26 | B27 |
| DB Design | B28 | B28 | B28 | B27 | B28 |
| Total Building GSF | B33 | B29 | B29 | B31 | B29 |
| **JPY Rate** | **B57** | **B33** | **B33** | **B41** | **B33** |
| PRV (iNFADS) | B53 (formula) | B38 | B38 | B33 | B38 |
| **LSH** | **B54** | **B40** | **B40** | **B34** | **B40** |
| RPUID | B34 | -- | B37 | B32 | B37/B10 |

**Rules derived from this table:**
- 3270 is the OUTLIER. Its compound escalation factor is B39, not B21. B21 is General Requirements.
  ESTIMATE C6 in 3270 references PARAMETERS!B39, not B21. Do NOT copy formulas from other buildings.
- 1024 JPY is B57 (far down in the PARAMETERS tab, after the full PRV section).
- LSH row varies: B54 (1024), B40 (3213/3237/3314), B34 (3270). Always verify before writing C9/B10.
- When building a new workbook from scratch, document PARAMETERS row assignments in a layout comment
  before writing any code. Use 3270 layout for 3270 only; use the common layout for all others.

---

### G-26: PARAMETERS row layout differs by building -- never assume row numbers

**Root cause:** SCH-3270 v9 has a different PARAMETERS row structure than the other four buildings.
The compound escalation factor is at B39 in 3270 vs B21 in all others. A formula in ESTIMATE or
DD1391 that references PARAMETERS!B21 will get General Requirements (0.10) instead of the
compound escalation factor in the 3270 workbook. This would silently produce wrong values.

**Rule:** Before writing any cross-sheet formula that references PARAMETERS, verify the exact row
number for that parameter in the specific building's PARAMETERS tab. Use the table above.
Do NOT copy formula patterns from one building to another without checking row assignments first.

---

### G-27: Block 10/11 language must be verified line-by-line against the current estimate SCOPE_DETAIL before submission

**Root cause:** SCH-3314 Block 10 FL1 paragraph described "removal of the existing condensing unit,
evaporator coils, and associated piping" -- language carried from the Decision Point 2 slide that
predated the current estimate. The estimate does not include VRF condensing unit or evaporator coil
removal from the main floor spaces. Block 10 FL2 paragraph similarly described "removal of evaporator
coils and associated refrigerant piping" -- also carried from Decision Point 2 scope language, not
present in the estimate. Both errors would have sent a designer to procure work that is not funded.

**Rule:** Before any DD Form 1391 version is submitted or shared with FEAD:
1. Open the current CEPBKUP SCOPE_DETAIL tab.
2. Read every scope group header and every line item description.
3. Verify that Block 10 Description of Proposed Construction accounts for every group -- no group
   omitted, no work described that has no corresponding estimate line item.
4. Verify that Block 11 Current Situation justifies the scope drivers for every major work category.
   If a scope group exists in the estimate but no condition statement supports it in Block 11, add one.
5. Verify that no language from prior decision slides, prior 1391 versions, or scope briefs that
   predates the current estimate has survived into the submission draft. Decision slide language
   frequently describes scope that was later removed, deferred, or reassigned.

**Pattern to watch:** Decision Point slides for this portfolio often described full HVAC system
replacements that were subsequently scoped down (VRF removal, evaporator coil tearout) before
the estimate was built. That slide language migrates into Block 10 drafts and survives undetected
unless the Block 10 is read against the estimate directly.

---

### G-28: Never reference personal names anywhere -- use role titles only

**Root cause:** Prior skill versions referenced individuals by full name throughout open items,
scope confirmations, and methodology notes. Names change when personnel rotate, create PII exposure
risk in shared documents, and add no technical value to a cost estimate or 1391 package.

**Rule:** All references to people in this skill file, in estimates, in Block 10/11 language, in
Section F narratives, and in any other deliverable must use role titles only. Never use a personal
name. Acceptable substitutions:

| Instead of a name | Use |
|---|---|
| Mechanical engineer (site visit, field notes) | Mechanical Engineer (G-F) |
| MCIPAC G-F planner providing scope input | G-F Planner |
| FMB A/C and refrigeration maintenance | FMB Refrigeration/A/C Maintenance |
| Building manager coordinating FMB actions | G-F Building Manager |
| RPAO providing iNFADS data | RPAO |
| AE evaluator on iNFADS worksheet | G-F AE Staff |
| PWD environmental staff | PWD Environmental Division |

This rule applies retroactively. If a name is found anywhere in a deliverable draft or in this
skill file, replace it before delivery. No exceptions.

---

### G-29: Three PRV values exist in iNFADS. Know which one you are using.

**Root cause:** All estimates except SCH-1024 used the AE Worksheet "PRV at EOY" field as
"iNFADS confirmed PRV." The AE Worksheet is a snapshot frozen at the evaluation date. The
Property Record "Current PRV" is a different field, recalculated by RPAO at end-of-year.
When Anthony pulled current Property Record values on 26 Mar 2026, four of five buildings
showed different numbers than the AE Worksheets. SCH-3237 jumped from $26.6M to $27.7M.
SCH-1024 dropped from $90.1M to $72.2M. SCH-3213 dropped from $10.9M to $9.9M.

**The three values:**

| Value | Source | Updates When | Use |
|-------|--------|-------------|-----|
| AE Worksheet "PRV at EOY" | Asset evaluation package | Frozen at evaluation date | Reference only. Never use as governing PRV in an estimate. |
| Property Record "Current PRV" | iNFADS Property Record | RPAO recalculates at EOY | Default governing PRV for non-conversion buildings. |
| Formula PRV (Equation 3-1) | UFS 3-701-01 Table 3 PUCs | Changes with each UFC/UFS update | Governing PRV for conversion buildings. Cross-check for all buildings. |

**Rule:** The AE Worksheet PRV is never the governing value in a DD 1391 estimate. It is
reference material only. For non-conversion buildings, pull the current Property Record PRV.
For conversion buildings, compute formula PRV with post-conversion FAC codes. Document all
three values and their sources in Section F Item 11. Record the iNFADS pull date.

**Pre-delivery check:** Confirm the Property Record PRV pull date is within 30 days of
submission. If the pull is older than 30 days, re-pull before submitting.

---

### G-30: Conversion buildings use formula PRV with post-conversion FAC codes

**Root cause:** SCH-3213 was classified as an iNFADS-method building and used the AE Worksheet
PRV of $10,893,334 (FAC 2171 Field Maintenance Shop at $232.17/SF). The building is being
partially converted to a CLB-4 BN HQ. Initial correction treated the full 13,484 SF as
single-FAC 6101 ($634/SF), producing PRV of $19,548,763 and ERC ratio of 26.6%. Team review
identified that the bay side (8,336 SF) retains its physical maintenance shop characteristics
(tactical vehicle roll-up doors, industrial structural spans, reinforced slab). The renovation
scope on the bay is inspect and repair, not demolition or reconstruction. The physical
construction type of that zone does not change, so its PUC does not change. Corrected to
2-FAC: 6101 (5,148 SF) + 2171 (8,336 SF), PRV $11,887,376, ERC 43.7%.

**The rule:** If the DD 1391 programs a facility type that does not match the current
Property Record FAC codes, the building is a conversion. Use formula PRV. But conversion
does not mean the entire building converts. Allocate FAC codes zone by zone based on
whether the renovation scope physically transforms each zone (see G-34).

**Conversion test (run at intake for every building):**
1. What FAC code(s) does the Property Record show?
2. What facility type does the DD 1391 program?
3. If they match: non-conversion. Use Property Record PRV.
4. If they differ: conversion. Proceed to step 5.
5. For each zone within the building: does the renovation scope physically transform
   that zone into a different construction type? (See G-34 for the test.)
   YES: assign post-conversion FAC code and PUC for that zone's GSF.
   NO: retain existing FAC code and PUC for that zone's GSF.
6. Compute formula PRV using the blended FAC allocation.
7. Source the GSF allocation per zone from the Property Record utilization breakdown.

**Camp Schwab portfolio classification (locked 26 Mar 2026):**

| Building | Property Record FAC | DD 1391 Programs | Classification | FAC Allocation |
|----------|-------------------|-----------------|----------------|----------------|
| SCH-1024 | FAC 4421/7241 (BEQ/CIF) | Armory/Admin/Gym | CONVERSION (multi-FAC) | 4 FAC codes, zone-by-zone |
| SCH-3213 | FAC 2171/6102 (Maint Shop/HQ) | CLB-4 BN HQ | CONVERSION (partial) | 2 FAC: 6101 HQ side + 2171 bay side |
| SCH-3237 | FAC 4427/4421/6100 | Same (Warehouse/Armory) | NON-CONVERSION | Property Record governs |
| SCH-3270 | FAC 2141 | Same (Auto Org Shop) | NON-CONVERSION | Property Record governs |
| SCH-3314 | FAC 6101 proxy (BN SQD HQ) | Same (4th MarRegt HQ) | NON-CONVERSION | Property Record governs |

---

### G-31: PRV must be pulled from the Property Record within 30 days of submission

**Root cause:** AE Worksheet PRVs used in the estimates were snapshots from evaluation dates
ranging from April 2020 (SCH-3314) to March 2024 (SCH-3270). These values were 1 to 6 years
stale. The Property Record values, pulled 26 Mar 2026, differed by up to 20% from the AE
values used in the estimates.

**Rule:** Before any DD 1391 is submitted to PAX:
1. Pull the current Property Record "Current PRV" from iNFADS for every building.
2. Record the exact dollar value and pull date.
3. For non-conversion buildings: if the Property Record PRV differs from the estimate,
   update the estimate before submission. No exceptions.
4. For conversion buildings: record the Property Record PRV in Section F Item 11 as
   reference. Formula PRV governs but the property record value must be documented.
5. The pull date must be within 30 days of submission. If older, re-pull.

---

### G-32: ERC threshold must be computed for every building before DD 1391 submission

**Root cause:** FEAD raised ERC (Existing Requirements Code / Estimated Replacement Cost)
as a portfolio-wide risk during the 25 Mar 2026 RFP review meeting. No one in the meeting
had computed the actual cost-to-PRV ratios. The assertion that ERC triggers would drive
costs above funded levels was made without data.

**The 50% threshold:** Per UFC 4-010-01 Para 1-6.2.1, AT/FP compliance requirements are
mandatory for renovations where project costs exceed 50% of replacement cost per
UFC 3-701-01. Per UFC 1-200-02 Table 1-1, HPSB/sustainability compliance applies to
renovations with cost >$3M and >=50% of ERC. MCIPAC-MCBBBul 3302 (9 Sep 2022) Para
4.a.(2)(f).3 confirms the same 50% threshold (using "Plant Replacement Cost") for Japan.

**What triggers when 50% is exceeded:** Full current code compliance: AT/FP standards
(UFC 4-010-01), seismic retrofit, HPSB/sustainability (UFC 1-200-02), fire protection,
accessibility. In Japan, BULLETIN 3302 adds AT standoff distances for Explosive Weight II.

**Technical note on the denominator:** UFC 4-010-01 uses "replacement cost" as the
denominator. UFC 3-701-01 Chapter 5, Section 5-1.1 states replacement cost is "distinctly
different from the PRV calculation defined in Chapter 3." Replacement cost is a
facility-specific estimate per UFC 3-730-01. In practice, PRV is used as a conservative
proxy because it is typically lower than replacement cost (making the ratio higher and
more likely to trigger). This proxy use must be documented.

**Separate trigger: occupancy reclassification.** Per UFC 4-010-01, conversion from
low-occupancy to inhabited use triggers AT/FP compliance regardless of cost ratio.
Evaluate conversion buildings for this trigger independently.

**Rule:** Before any DD 1391 is submitted:
1. Compute ERC ratio = Total Funded / PRV for every building.
2. PRV = Property Record PRV (non-conversion) or Formula PRV (conversion per G-30).
3. Any building over 40%: flag as MONITORING in Section F Item 11.
   a. Compute +30% scenario: (Total Funded x 1.3) / PRV.
   b. If +30% scenario breaches 50%: flag as ERC SENSITIVE.
   c. Document the dollar headroom to the 50% trigger (50% of PRV minus Total Funded).
   d. Every scope addition must be evaluated for ERC impact before being added.
4. Any building over 50%: flag as ERC TRIGGERED. Coordinate with FEAD. Cost impact
   must be quantified before submission.
5. Document the ratio, PRV source, and policy basis in Section F Item 11.

**BULLETIN 3302 additional provisions:**
- Renovations "will normally be planned in accordance with" UFC 4-010-01 (Para 6.a)
- Enhanced MGB/SOB standoff requirements are discretionary for renovations unless
  they cross the 50% PRC line
- "Significant Occupancy Building" (SOB): 50 to 199 routine occupants, may warrant
  Low Level of Protection. Designation requires written request to MCIPAC-MCBB
  Director of Installation Protection.
- "Mass Gathering Building" (MGB): 200+ occupants. None of the five Camp Schwab
  buildings should trigger MGB.

---

### G-33: UFS 3-701-01 (2 Feb 2026) supersedes UFC 3-701-01 and all changes

**Root cause:** The skill and all five estimates reference "UFC 3-701-01 w/Change 7 (25 Jul
2025)" as the governing pricing guide. As of 2 February 2026, UFS 3-701-01 (Unified
Facilities Supplement) supersedes UFC 3-701-01 and all changes including Change 7. The UFS
reflects FY2025 cost data current as of 1 October 2024. PUC values in Table 3 carry forward.

**Rule:** All new citations in estimates, Section F narratives, and DD 1391 packages use
"UFS 3-701-01 (2 Feb 2026)" as the governing document. Existing estimates update the
citation at next revision only (do not open a completed estimate solely to change the
citation). The C7 Data Tables file in the project directory contains the same PUC values
and remains valid for computation. Note: ACF tables, escalation tables, and the full
Equation 3-1 methodology carry forward unchanged into UFS 3-701-01.

---

### G-34: FAC code for PRV is determined by physical construction type, zone by zone

**Root cause:** SCH-3213 was initially assigned FAC 6101 (Small Unit HQ, $634/SF) for the
full 13,484 SF on the basis that the building is converting to a BN HQ. Team review
identified that the bay side (8,336 SF: Rooms 112-118, maintenance/repair/tool/testing/
receiving/storage) retains tactical vehicle roll-up doors, industrial structural spans,
reinforced slab, and high clear height. The renovation scope for this zone is inspect and
repair (Group 11: overhead door inspection). The physical construction of the bay does not
change. Assigning FAC 6101 ($634/SF) to a zone that costs $232/SF to replace overstated
PRV by $7.7M and understated the ERC ratio by 17 percentage points.

**The principle:** UFS 3-701-01 Table 3 PUCs are construction cost models. Each PUC reflects
what it costs to build that specific type of space: structural systems, envelope, MEP
complexity, interior finishes, clear heights, door configurations. A maintenance bay at
$232/SF is priced for industrial spans and overhead doors. A headquarters at $634/SF is
priced for office-grade HVAC, partitions, IT density, and higher finishes. The PUC is tied
to the physical characteristics of the space, not what mission the occupant performs inside.
MCO 11000.5 Encl 3 Para 1.b.(6) defines PRV using "current building codes, design criteria,
and materials." Materials and design criteria are physical attributes.

**The two-sided test (apply zone by zone within any conversion building):**

Does the renovation scope physically transform this zone into a different construction type?

YES: The post-renovation FAC and PUC apply. The renovation changes the structural
characteristics, MEP systems, interior configuration, or envelope of the space such that
the replacement cost is fundamentally different from the original construction.
Example: SCH-1024 BEQ rooms converting to armory vaults. Scope installs vault doors,
reinforced walls, SIPR raceways, weapons storage infrastructure. The post-renovation
space is physically a different construction type. FAC 4427 ($428/SF) applies.

NO: The existing FAC and PUC apply. The renovation does not alter the structural
characteristics that drive the replacement cost. Cosmetic changes, equipment swaps,
or mission reassignment without physical transformation do not change the PUC.
Example: SCH-3213 maintenance bay repurposed as CLB-4 storage/receiving. Roll-up doors
inspected and repaired, not demolished. Structural spans, slab, clear height unchanged.
The replacement cost of that bay is still a maintenance bay. FAC 2171 ($232/SF) applies.

**Rule:** For every conversion building, walk the floor plan zone by zone. For each zone,
ask: does the scope physically change what this space is? Document the answer and the
FAC assignment for each zone in Section F Item 11. Source the GSF per zone from the
Property Record utilization breakdown (DoDI 4165.14 framework). If the scope changes
during the project life cycle, re-evaluate the FAC assignment for affected zones.

---

### G-35: When PRV methodology changes, flag all downstream deliverables immediately

**Root cause:** v23.0 corrected SCH-3213 PRV from AE Worksheet basis ($10,893,334) to formula
method ($11,887,376). The ERC threshold analysis infographic (ERC_Threshold_Analysis_Camp_Schwab_
26MAR2026.html/pdf) was built the same day using the pre-correction AE Worksheet PRV. It shows
SCH-3213 at 47.6%. The corrected ratio is 43.7%. Both products now sit in the project directory.
Anyone picking up the HTML without knowing the history would distribute the wrong number.

**Rule:** Any time a PRV methodology changes for any building:
1. Identify every deliverable in the project directory that displays a PRV-derived ratio,
   PRV value, LSH value, or ERC percentage for that building.
2. Flag each such file explicitly in the skill as STALE, with the specific field that changed
   and the corrected value.
3. Do not allow a stale product to be distributed or submitted. Rebuild it before the next use.
4. The skill must note the stale product, the stale value, and the correct value in the
   affected building's section.

**Current stale product (27 Mar 2026):**
ERC_Threshold_Analysis_Camp_Schwab_26MAR2026.html and .pdf -- SCH-3213 ratio shown as 47.6%.
Correct ratio: 43.7% (formula PRV $11,887,376 basis, v23.0). Rebuild required before distribution.
The older ERC_Threshold_Analysis__Camp_Schwab_FSRM_Portfolio.pdf also predates both the v23.0
PRV correction and the 26 Mar analysis. Both older products carry stale values.

---

### G-36: RS Means CONUS unit costs require OCONUS reasonableness review before locking

**Root cause:** SCH-3213 Group 11 overhead door replacement was estimated at $5,500/EA using
RS Means FY24 CONUS line item 08 33 23 (commercial overhead sectional steel door, 10x10, with
hardware and operator). The client challenged this as potentially too low for Japanese execution.
A 30% premium scenario produced $7,150/EA. The unit cost was left in the estimate at $5,500
without formal documentation of the OCONUS reasonableness review.

The ACF (1.85) is applied to the total estimate, not to individual line items. It captures the
overall regional cost differential for Camp Schwab. However, some line items are more sensitive
to OCONUS execution conditions than others. Specialty products, licensed trade work, and items
requiring import or freight can run materially higher than CONUS direct.

**Rule:** Before locking any SCOPE_DETAIL unit cost derived from RS Means CONUS:
1. Ask: is this item sensitive to Japanese execution conditions? (specialty trade, imported
   equipment, freight-intensive, or subject to local labor premiums?)
2. If YES: note in the Col J authority field whether a quote, a CONUS+adjustment, or a
   subject matter expert confirmation was used. Do not rely on RS Means CONUS alone.
3. If a quote is available (Hamilton, TQL, vendor-specific): use it and cite it.
4. If only CONUS RS Means is available: note in Section F Item 9 that individual unit costs
   are CONUS direct and that the ACF captures the regional adjustment at the estimate level.
   Flag any line items with known OCONUS sensitivity as yellow pending confirmation.
5. Never increase a unit cost without a source. Never leave a known-underpriced item unflagged.

**Current open item:** SCH-3213 G11 overhead door replacement -- $5,500/EA RS Means CONUS.
No OCONUS adjustment documented. See SCH-3213 open items.

---

## 4 Required Tabs (LOCKED -- no exceptions)

1. ESTIMATE -- ROM chain Sections A-F + inline methodology
2. SCOPE_DETAIL -- every work item (10 columns per v11 spec)
3. PARAMETERS -- all inputs and derived values; single source of truth
4. DD1391_BLOCK9 -- PAX format, $000s, one UNIFORMAT II code per child line

Tab order: ESTIMATE -> SCOPE_DETAIL -> PARAMETERS -> DD1391_BLOCK9
Exactly 4 tabs. No COST_SUMMARY. No METHODOLOGY tab. No fifth tab. No exceptions.

---

## Workbook Architecture -- v11 APEX OMEGA (LOCKED)

### Font
Calibri throughout. ALL tabs, ALL cells, ALL styles.
Arial MUST NOT appear in any cell.

### Color Palette (exact hex -- LOCKED)
| Role | Hex | Usage |
|------|-----|-------|
| Title bar | FF1B2A4A | Very dark navy -- row 1 merged title |
| Section header | FF2E4A7A | Dark navy-blue -- section A/B/C/D/E/F headers |
| Column headers | FFBDD7EE | Light blue -- BLACK text (FF000000) |
| Construction base | FFD9E1EC | Slightly darker gray |
| Subtotals / Total Project | FFD6DCE4 | Light gray |
| Total Funded | FFBDD7EE | Same as column headers (light blue) |
| Parameter label col | FFF2F5FA | Very light blue-gray -- PARAMETERS col A |
| Input value cells | FFEBF5FF | Very light blue -- blue text inputs |
| Calc/formula cells | FFE8EEF6 | Slightly tinted -- PARAMETERS derived rows |
| Block 9 header | FF1F4E79 | Dark navy -- DD1391 headers |
| Stale / warning | FFFF00 | Yellow -- unverified items, JPY rate |

Font Color Convention (LOCKED):
- FF0070C0 blue -- hardcoded user inputs (Qty, Unit Cost, parameter values)
- FF000000 black -- formulas and calculated values (same-tab)
- FF008000 green -- cross-sheet formula pulls
- FFC00000 red italic -- stale/warning text (JPY header, stale flags)
- FF444444 gray -- source notes, documentation text

PatternFill: ALWAYS `PatternFill("solid", fgColor="FF"+hex6, bgColor="FF"+hex6)`
No fill: `PatternFill(fill_type=None)` -- NEVER `fgColor="00000000"` with solid fill.
CRITICAL: Never pass a PatternFill object as a font argument. Fatal styles.xml corruption.

---

## ESTIMATE Tab -- Column Layout

```
Col A  (width 48): Element label
Col B  (width 16): Amount ($)
Col C  (width 58): Formula / Authority
```

### ESTIMATE Tab Row Structure (v11 locked)
- Row 1:  Title bar (merged A1:C1, height 22)
- Row 2:  Blank spacer (height 6) -- NO BORDER
- Row 3:  Section A header (height 18)
- Row 4:  Column headers (height 16)
- Row 5:  1. Base Direct = =SCOPE_DETAIL!G{gt_row} [GREEN]
- Row 6:  2. x ACF = =B5*PARAMETERS!B18 [BLACK]
- Row 7:  3. x Escalation = =B6*PARAMETERS!B21 [BLACK]
- Row 8:  4. x (1+GR) = =B7*(1+PARAMETERS!B22) [BLACK]
- Row 9:  5. x (1+Cont) = =ROUND(B8*(1+PARAMETERS!B23),0) [BLACK]
- Row 10: 6. + LSH = =PARAMETERS!B40 [GREEN]  (row may differ for multi-FAC -- verify)
- Row 11: CONSTRUCTION BASE = =B9+B10 [medium top+bottom border]
- Row 12: Blank spacer (height 6) -- NO BORDER
- Row 13: Section B header
- Row 14: Column headers
- Row 15: Design = =B11*PARAMETERS!B25
- Row 16: SIOH = =B11*PARAMETERS!B26
- Row 17: CM = =B11*PARAMETERS!B27
- Row 18: TOTAL FUNDED = =ROUND(B11+B15+B16+B17,0) [medium top+bottom border]
- Row 19: DB Design = =B18*PARAMETERS!B28
- Row 20: TOTAL PROJECT = =B18+B19 [medium top+bottom border]
- Row 21: Blank spacer -- NO BORDER
- Row 22: Section C header (Cost/SF)
- Row 23: Column headers
- Row 24: Cost/SF = =B18/PARAMETERS!B29
- Row 25: Blank spacer -- NO BORDER
- Row 26: Section D header (UNIFORMAT SUMIF)
- Row 27: Column headers
- Rows 28+: One SUMIF per UNIFORMAT code: =SUMIF(SCOPE_DETAIL!$I:$I,"code",$G:$G)
- Total Check row: =SUM(SUMIF rows) must equal B5 [medium bottom border]
- Blank row
- Section E: Version history
- Section F: Methodology 13 items inline (row height 45)

---

## PARAMETERS Tab -- Row Assignments (LOCKED)

```
B18: ACF = 1.85
B19: Escalation Rate = 0.021
B20: Escalation Years = 3
B21: Compound Escalation Factor = =(1+B19)^B20
B22: General Requirements = 0.10
B23: Contingency = 0.10
B24: LSH Rate = 0.025
B25: Design = 0.06
B26: SIOH (program adder) = 0.08
B27: CM = 0.04
B28: DB Design = 0.04
B29: Total Building GSF (Property Record confirmed)
B33: JPY/USD rate -- YELLOW fill, red italic -- verify before submission

For Property Record method (non-conversion):
B37: iNFADS RPUID
B38: PRV (Property Record Current PRV -- input, blue; pull date within 30 days per G-31)
B39: Implied $/SF check = =B38/B29/B18 (calc cell, not PRV formula)
B40: LSH = confirmed dollar value (hardcoded integer per G-24)

For formula method (multi-FAC -- rows expand as needed):
B37+: For each FAC: GSF row (blue input), PUC row (blue input), sub-PRV row (=GSF×PUC -- NO ACF)
After all FAC sub-PRV rows:
  HF row         = 1.0 (hardcoded blue input; label: "Historical Factor (HF)")
  PD row         = 1.09 (hardcoded blue input; label: "Productivity Differential (PD)")
  SIOH row       = 1.08 (hardcoded blue input; label: "SIOH Factor (Eq 3-1 PRV multiplier)")
  CF row         = 1.05 (hardcoded blue input; label: "Contractor Factor (CF)")
  Combined row   = =HF×PD×SIOH×CF (formula; label: "Combined Factor (HF×PD×SIOH×CF)")
  Total PRV row  = =(Σ sub-PRVs) × ACF_cell × combined_cell (label: "TOTAL PRV (Sum sub-PRVs x ACF x HF x PD x SIOH x CF)")
  LSH row        = =Total_PRV_cell × B24 (label: "LSH Allowance (=TOTAL PRV x LSH Rate)")

CRITICAL: Sub-PRV rows are GSF × PUC ONLY. ACF is NOT in the sub-PRV formula.
ACF and all Eq 3-1 factors are applied ONCE in the Total PRV row only.
Reference: SCH-1024 v10 PARAMETERS rows 37-51 (sub-PRVs) and 52-56 (Eq 3-1 factors).

ESTIMATE B10 references PARAMETERS LSH row (cross-sheet, green).
DD1391_BLOCK9 adder for LSH references PARAMETERS LSH row / 1000 (cross-sheet, green).
Determine and document exact LSH row number before writing ESTIMATE or DD1391 tab code.
For multi-FAC buildings the LSH row will NOT be B40 -- verify and document the actual row.

---

## SCOPE_DETAIL Tab -- 10 Columns (v11 LOCKED)

```
Col A (width 7):   Item number
Col B (width 10):  Scope group label
Col C (width 60):  Work description (wrap text)
Col D (width 7):   Quantity [BLUE input]
Col E (width 7):   Unit
Col F (width 16):  Unit Cost FY24 CONUS [BLUE input]
Col G (width 14):  Extended Cost = =D*F [BLACK formula]
Col H (width 14):  JPY = =G*PARAMETERS!$B$33 [GREEN cross-sheet]
Col I (width 11):  UNIFORMAT II Level 2 code
Col J (width 48):  Notes / Cost basis (gray 8pt)
```

CRITICAL: Column I on subtotal rows = BLANK. Only item rows get UNIFORMAT codes.
Grand total row G = =sum of all subtotal G cells (not raw item rows).
Yellow fill on rows where qty, unit cost, or scope is unconfirmed.

---

## PAX Block 9 -- Manual UNIFORMAT Output Format (LOCKED 19 Mar 2026)

When PAX Block 9 is produced manually (not from the DD1391_BLOCK9 tab), each scope item
gets its own individual line. This is different from the consolidated UNIFORMAT summary
in the DD1391_BLOCK9 tab. PAX requires one line per scope item.

### Column Format
| Column | Content |
|--------|---------|
| Description | Scope item text (see character limit below) |
| Classification of Work | CRM for all Camp Schwab portfolio items |
| Work Type | RM for all Camp Schwab portfolio items |
| UM | SF |
| Quantity | 1.00 |
| Unit Cost (full $) | Item funded cost in dollars (Base Direct item x TF/BD factor) |
| Total ($000) | Unit Cost / 1000, rounded to 3 decimal places |
| UNIFORMAT | UNIFORMAT II Level 2 code for that item |

### Character Limit -- CRITICAL
PAX truncates the Description field. Confirmed limit: approximately 90 characters for
the description text. PAX prepends the UNIFORMAT code and a separator when displaying,
consuming approximately 6 additional characters ("D30 - ").

**Rule:** Write all PAX descriptions at 90 characters or fewer. Use abbreviations:
- & for "and"
- f&i for "furnished and installed"
- bldg-wide for "building-wide"
- req'd for "required"
- sys for "system"
- mech for "mechanical"
- EA for each
- RM for room number references
- 1F / 2F for first floor / second floor

Never truncate a scope description in a way that loses the identifying information
(room number, quantity, equipment tag). Shorten connecting language, not scope identifiers.

### UNIFORMAT Sort Order
Sort all PAX child lines in alphabetical UNIFORMAT order: B20, C10, C30, D20, D30, D50.
Within each UNIFORMAT group, order does not matter but keep consistent with SCOPE_DETAIL.

### Unit Cost Calculation
Each item's PAX unit cost = (Item Base Direct) x (Total Funded / Total Base Direct)
This proportionally allocates the full funded cost (including all adders) to each item.
The sum of all child line Total ($000) values must equal Total Funded.

### SCH-3270 v9 PAX Block 9 (confirmed 19 Mar 2026 -- 42 lines):
Factor: $3,392,070 / $792,000 = 4.28291667

| Description | Class | Work Type | UM | Qty | Unit Cost (full $) | Total ($000) | UNIFORMAT |
|---|---|---|---|---|---|---|---|
| Inspect & repair overhead roll-up doors; 22 EA; RM105, RM113 & wing rms 101-104 | CRM | RM | SF | 1.00 | $94,224.17 | 94.224 | B20 |
| Repair gypsum & concrete wall damage bldg-wide; patch & paint to match | CRM | RM | SF | 1.00 | $85,658.33 | 85.658 | C10 |
| Resecure anchor wire cables to exterior HVAC units; hardware replacement as req'd | CRM | RM | SF | 1.00 | $34,263.33 | 34.263 | C10 |
| Deep clean all restrooms; mold & mildew remediation; surfaces, fixtures & drains | CRM | RM | SF | 1.00 | $64,243.75 | 64.244 | C10 |
| Replace mold/mildew damaged ceiling tile; 2,500 SF bldg-wide | CRM | RM | SF | 1.00 | $74,951.04 | 74.951 | C30 |
| Replace eyewash & shower stations bldg-wide; RM102 & RM105; per ANSI Z358.1 | CRM | RM | SF | 1.00 | $68,526.67 | 68.527 | D20 |
| Replace 2F electric water cooler; RM214 corridor; EW-1; f&i complete | CRM | RM | SF | 1.00 | $11,992.17 | 11.992 | D20 |
| Replace VRF outdoor condensing unit ACP-1; 50.2 KW/14.3T; f&i complete w/refrig & elec | CRM | RM | SF | 1.00 | $100,648.54 | 100.649 | D30 |
| Replace VRF outdoor condensing unit ACP-2; 26.2 KW/7.4T; f&i complete | CRM | RM | SF | 1.00 | $62,102.29 | 62.102 | D30 |
| Replace VRF outdoor condensing unit ACP-3; 40.0 KW/11.4T; f&i complete | CRM | RM | SF | 1.00 | $83,516.88 | 83.517 | D30 |
| Replace VRF outdoor condensing unit ACP-4; 16.0 KW/4.5T; f&i complete | CRM | RM | SF | 1.00 | $42,829.17 | 42.829 | D30 |
| Replace VRF outdoor condensing unit ACP-5; 40.0 KW/11.4T; f&i complete | CRM | RM | SF | 1.00 | $83,516.88 | 83.517 | D30 |
| Replace VRF outdoor condensing unit ACP-6; 14.0 KW/4.0T; f&i complete | CRM | RM | SF | 1.00 | $40,687.71 | 40.688 | D30 |
| Replace mini-split condensing unit ACP-7; 2.2 KW/0.6T; f&i complete w/startup | CRM | RM | SF | 1.00 | $14,990.21 | 14.990 | D30 |
| Replace indoor VRF fan coils ACP-3 zone; 14 EA ducted cassette; f&i complete | CRM | RM | SF | 1.00 | $167,890.33 | 167.890 | D30 |
| Replace indoor VRF fan coils ACP-4 zone; 3 EA ducted cassette; f&i complete | CRM | RM | SF | 1.00 | $35,976.50 | 35.977 | D30 |
| Replace indoor VRF fan coils ACP-5 zone; 4 EA ducted cassette; f&i complete | CRM | RM | SF | 1.00 | $47,968.67 | 47.969 | D30 |
| Replace indoor VRF fan coils ACP-6 zone; 3 EA ducted cassette; f&i complete | CRM | RM | SF | 1.00 | $35,976.50 | 35.977 | D30 |
| Refrigerant piping; line sets, insulation, fittings & pressure testing; all 7 ACPs | CRM | RM | SF | 1.00 | $85,658.33 | 85.658 | D30 |
| Electrical disconnects & dedicated circuit connections; 7 outdoor ACP units | CRM | RM | SF | 1.00 | $53,964.75 | 53.965 | D30 |
| Redesign air pull infrastructure; supply/return vents, fan power boxes, louvers; 1F&2F | CRM | RM | SF | 1.00 | $77,092.50 | 77.093 | D30 |
| Install new split unit HVAC; 1F & 2F hallways; 2 EA; capacity per designer calc | CRM | RM | SF | 1.00 | $102,790.00 | 102.790 | D30 |
| Replace ACP-1 100% OA packaged unit; RM123; serves main shop areas; f&i complete | CRM | RM | SF | 1.00 | $162,750.83 | 162.751 | D30 |
| Replace ACP-4-3 outside air processing unit; RM104 Office 1; f&i complete | CRM | RM | SF | 1.00 | $68,526.67 | 68.527 | D30 |
| Replace ACP-5-4 outside air processing unit; RM207 Class Room; f&i complete | CRM | RM | SF | 1.00 | $68,526.67 | 68.527 | D30 |
| Replace ACP-6-3 outside air processing unit; RM116 Office 2; f&i complete | CRM | RM | SF | 1.00 | $68,526.67 | 68.527 | D30 |
| DOAS supply ductwork eval & replacement as req'd; all 4 systems; designer to confirm | CRM | RM | SF | 1.00 | $77,092.50 | 77.093 | D30 |
| Replace general exhaust fans bldg-wide; 22 EA; restroom, shop, mech, bay & roof fans | CRM | RM | SF | 1.00 | $282,672.50 | 282.673 | D30 |
| Replace vehicle exhaust hose reel assemblies; 10 EA; RM105 (6 EA) & RM113 (4 EA) | CRM | RM | SF | 1.00 | $214,145.83 | 214.146 | D30 |
| Full removal abandoned dust collection sys RM114; DC unit, ductwork & connections | CRM | RM | SF | 1.00 | $36,404.79 | 36.405 | D30 |
| Repair & restore RM117 welding exhaust sys; fans FE-13, FE-14, FA-1, hood & duct | CRM | RM | SF | 1.00 | $59,960.83 | 59.961 | D30 |
| Battery room RM102 ventilation & conditioning upgrade; split sys ext & exhaust upgrade | CRM | RM | SF | 1.00 | $51,395.00 | 51.395 | D30 |
| Compressed air sys inspection, pressure test & repair as req'd; COM-1 RM119 & dist loop | CRM | RM | SF | 1.00 | $36,404.79 | 36.405 | D30 |
| Replace high bay fixtures; 62 EA various types; f&i complete | CRM | RM | SF | 1.00 | $172,601.54 | 172.602 | D50 |
| Replace 400W MH high bay fixtures SP3-HSR1M-400BH26; 30 EA; lift & rigging req'd | CRM | RM | SF | 1.00 | $231,277.50 | 231.278 | D50 |
| Replace 400W MH fixtures SP-2 w/optical sensors; 2 EA; coordinate w/fire detection | CRM | RM | SF | 1.00 | $27,410.67 | 27.411 | D50 |
| Replace motion sensor lighting fixtures; qty per 1F & 2F survey; wiring & switch legs | CRM | RM | SF | 1.00 | $59,960.83 | 59.961 | D50 |
| Electrical panel work; circuit mods & branch wiring for fixture replacement 1F & 2F | CRM | RM | SF | 1.00 | $42,829.17 | 42.829 | D50 |
| Remove existing Cat5 & Cat3 cabling bldg-wide; 1F & 2F; J-boxes & patch panels | CRM | RM | SF | 1.00 | $32,121.88 | 32.122 | D50 |
| Install Cat6; 70 NIPR drops; 40 EA CLB-4 & 30 EA 4th MarRegt; both TRs complete | CRM | RM | SF | 1.00 | $62,958.88 | 62.959 | D50 |
| TR infrastructure upgrade; patch panels, hubs & 110-blocks; 1F TR & 2F TR complete | CRM | RM | SF | 1.00 | $72,809.58 | 72.810 | D50 |
| Install MNS junction box & Mass Notification System infrastructure bldg-wide | CRM | RM | SF | 1.00 | $94,224.17 | 94.224 | D50 |

Total: $3,392.070K = Total Funded. Verified against PAX PDF BU26PPE74R 18-Mar-26.
Child line count: 42. UNIFORMAT codes verified: B20(1) C10(3) C30(1) D20(2) D30(26) D50(9).

---

## DD1391_BLOCK9 Tab -- v11 Child Line Formula (LOCKED)

```
=SCOPE_DETAIL!G{subtotal_row}*PARAMETERS!$B$18*PARAMETERS!$B$21*(1+PARAMETERS!$B$22)/1000
```

One UNIFORMAT II code per child line. PAX rejects combined codes.
PAX accepts duplicate UNIFORMAT codes across separate child lines -- do not merge them.
No proportional allocation formulas. No ROM accuracy range section.

Subtotal check: =SUM(B4:B{last_child}) must equal ESTIMATE!B8/1000 exactly.

Adder lines (all GREEN, cross-sheet):
- Contingency:   =B{sub_row}*PARAMETERS!B23
- LSH:           =PARAMETERS!{lsh_row}/1000   [verify actual row -- not always B40]
- Design:        =ESTIMATE!B15/1000
- SIOH:          =ESTIMATE!B16/1000
- CM:            =ESTIMATE!B17/1000
- Total Funded:  =ESTIMATE!B18/1000
- DB Design:     =ESTIMATE!B19/1000
- Total Project: =ESTIMATE!B20/1000

Column widths: A=55, B=18, C=50.

---

## Border Architecture (v11 LOCKED)

Apply borders as a separate post-processing pass AFTER all tabs are built.

### Border Types
```python
B_THIN   = Border(left=thin, right=thin, top=thin,   bottom=thin)
B_MED_TB = Border(left=thin, right=thin, top=medium, bottom=medium)
B_MED_T  = Border(left=thin, right=thin, top=medium, bottom=thin)
B_MED_B  = Border(left=thin, right=thin, top=thin,   bottom=medium)
```

### ESTIMATE (3 cols)
- Thin grid on every non-spacer row
- Spacer rows (2, 12, 21, 25, 31+blank, Section E blank): NO border
- B_MED_B: Construction Subtotal (row 9), UNIFORMAT TOTAL CHECK
- B_MED_TB: Construction Base (row 11), Total Funded (row 18), Total Project (row 20)

### SCOPE_DETAIL (10 cols)
- Thin grid on all rows 1 through grand total row
- B_MED_T on each group subtotal row
- B_MED_TB on grand total row

### PARAMETERS (4 cols)
- Thin grid on all non-spacer rows; spacer rows NO border
- B_MED_B on PRV row; B_MED_TB on LSH row

### DD1391_BLOCK9 (3 cols)
- Thin grid on all non-spacer rows
- B_MED_TB on Subtotal, Total Funded, Total Project rows

---

## Section F -- Methodology (13 Items, LOCKED)

No separate methodology tab. Inline as Section F of ESTIMATE tab only.
Label in col A (bold 10pt). Text merged B:C (8-9pt). Row height 45.
Do not mention accuracy percentage ranges. Do not use "Z10." Do not use em dashes.

### Section F Authority Citation Reference (LOCKED -- v12)

This table governs what authority goes in each item. No improvising.

| Item | Content | Required Authority | Prohibited |
|------|---------|-------------------|-----------|
| 1 | Estimate Level | UFS 3-740-05 (2 Feb 2026) | Any accuracy % range |
| 2 | Scope Basis | PAX ID, iNFADS RPUID, source document date | None |
| 3 | ACF | UFC 3-701-01 w/Change 7 (25 Jul 2025), Table 4-1 OCONUS, site M67400-0004 | 10 U.S.C. § 2802 (wrong context) |
| 4 | Escalation | OSD FY25 published rate | "Tri-Service memorandum" |
| 5 | General Requirements | "FSRM program-directed" | "Z10" |
| 6 | Contingency | "FSRM program-directed" + UFS 3-740-05 (2 Feb 2026) | Accuracy % ranges |
| 7 | LSH | UFC 3-701-01 Equation 3-1 + NAVFAC 11010.44E CH-1 + MCO 11000.12 (08 Sep 2014) | "Table 3" as LSH authority |
| 8 | Program Adders | UFC 3-730-01 (2024) for DB Design | UFC 3-730-01 without year |
| 9 | Unit Cost Basis | One sentence per scope group; scope-specific references (UFC 3-580-01, CNSSAM, etc.). State unit cost tier per JED 01.8 (Tier 1 Japan-market or Tier 2 RS Means/ACF) with rationale per G-41. For Okinawa, note humid environment scope basis (JDDG 9.5.2, 12.17) if applicable per G-40. | Vendor product names |
| 10 | Items Requiring Verification | "[ref] -- unknown / resolution" format | None if all clear |
| 11 | Methodology Deviations | Full PRV method, all Eq 3-1 factors, sub-PRV breakdown, LSH delta, iNFADS update status. JDDG 2.9.1 renovation vs. replacement narrative: ERC ratio, 50% PRC threshold, seismic trigger (UFC 3-310-04), occupancy reclassification (UFC 4-010-01), with citation stack per G-39. Radon status per G-38 if Okinawa. | "None" if PRV is formula method |
| 12 | Prepared By | "Anthony L. Potter \| Facilities Professional \| Booz Allen Hamilton - MCIPAC G-F PPE \| DD Month YYYY" | "PPEI" |
| 13 | Version History | Reference Section E; state live =B18 formula for current version | Omitting this item entirely |

1. Estimate Level -- Level 3 ROM per UFS 3-740-05 (2 Feb 2026). Non-mandatory
   supplement; For Information Only. No accuracy percentage ranges cited.
2. Scope Basis -- item count, disciplines, authority: DD Form 1391 PAX ID XXXXXX
   and AE floor plan [date if available]; iNFADS RPUID XXXXXX.
3. Area Cost Factor -- 1.85; UFC 3-701-01 C7 (25 Jul 2025), Table 4-1 OCONUS, M67400-0004.
4. Escalation -- 2.1%/yr; OSD FY25 published rate, client-confirmed; FY24-FY27;
   factor =(1.021)^3 = 1.0643 (live formula in PARAMETERS B21).
5. General Requirements -- 10.0%, FSRM program-directed.
6. Contingency -- 10.0%, FSRM program-directed, Level 3 ROM. UFS 3-740-05 (2 Feb 2026).
7. LSH -- State PRV source and method. If iNFADS: state RPUID and confirmed dollar value.
   If formula: state each FAC's GSF, PUC, sub-PRV, and all Equation 3-1 factors including
   HF (1.0), PD (1.09), SIOH (1.08), CF (1.05), combined factor (1.23606).
   LSH = Total PRV × 2.5% = $XXX. Authority: NAVFAC 11010.44E CH-1; MCO 11000.12.
8. Program Adders -- Design 6% NAVFAC agency-directed. SIOH 8.0% OCONUS FSRM
   customer-directed (NOT standard 7.3% -- note the 8.0% adder is separate from the
   1.08 SIOH factor in Equation 3-1 PRV calculation). CM 4% agency-directed.
   DB Design 4% applied AFTER Total Funded per UFC 3-730-01 (2024).
9. Unit Cost Basis -- FY24 CONUS pre-ACF. One sentence per scope group.
   If LSH is a large share of Total Funded: say so plainly.
10. Items Requiring Verification -- one line per yellow item. Format: "[ref] -- unknown item / resolution action."
    "None" only if all items are confirmed.
11. Methodology Deviations -- Structure (use exactly):
    (a) State which PRV method governs (iNFADS or formula) and cite authority.
    (b) For iNFADS: state full Eq 3-1 cross-check result. List each FAC (GSF × PUC), sum, × ACF × 1.23606.
        State delta vs iNFADS. Identify most plausible explanation (PUC change cycle, etc.).
        Do not say "reason unknown" without providing whatever context is available.
    (c) For formula: list each Equation 3-1 factor individually. State why iNFADS is not available.
    (d) State iNFADS-based LSH vs formula-based LSH and the dollar difference. This is what reviewers care about.
12. Prepared By -- "Anthony L. Potter | Facilities Professional | Booz Allen Hamilton - MCIPAC G-F PPE | DD Month YYYY"
13. Estimate Version History -- chronological; current version row references live =B18 formula.

---

## openpyxl Critical Rules (v11 LOCKED)

### CRITICAL BUG -- Fatal styles.xml Corruption
NEVER pass a PatternFill object as a `font` argument.
Verification: After build, read styles.xml from the zip -- no font name may contain
"openpyxl.styles" or "PatternFill". Any such string = fatal corruption.

### Properties Patching (LOCKED SEQUENCE -- v12 ENFORCED)
Violating this sequence causes calculated values to clear. Root cause documented in G-7.
Correct sequence: build → set properties → patch app.xml → recalc.py → verify → deliver.
1. Set native openpyxl properties BEFORE first save. Do NOT set `keywords`.
2. Patch Company and Manager via zip/lxml edit of docProps/app.xml BEFORE recalc.py.
3. Run recalc.py. Do NOT re-patch the zip AFTER recalc.py.
4. After recalc.py: do NOT re-open and re-save with openpyxl. That clears calculated values.
5. If any fix is required after recalc: re-open → fix → save → re-patch app.xml → re-run recalc → re-verify.
There is no shortcut. This sequence runs every build, every time.

### Other openpyxl Rules
1. All calculation cells must contain real Excel formula strings.
2. Documentation strings beginning with "=" MUST be prefixed with a space character.
3. Cross-sheet refs: =SCOPE_DETAIL!G100, =PARAMETERS!B18 -- exact row/col.
4. insert_rows() does NOT auto-update cross-sheet references -- audit manually.
5. Merged cells do not shift after insert_rows() -- unmerge, re-merge, restore values.
6. Run recalc.py with 60-second timeout minimum.
7. data_only=True load after recalc: zero None values in all key formula cells required.

---

## Build Sequence (Follow in Order -- No Skipping)

### Step 0: Read xlsx SKILL
Read /mnt/skills/public/xlsx/SKILL.md before writing any code.

### Step 1: Complete Intake
All 26 questions answered. Scope confirmed. PRV source confirmed.
Run PRV Verification Protocol PRV-1 through PRV-4 before proceeding.

### Step 2: Extract and Verify Scope
If existing estimate provided: extract description, qty, unit, unit cost, notes only.
Verify sum of all (qty x unit cost) = confirmed Base Direct exactly.

### Step 3: Fact-Check All Inputs
Verify each FAC code, each PUC (direct read -- not memory), PRV (full Eq 3-1 or iNFADS),
LSH, compound factor. State independent calculation of locked output targets.

### Step 4: Build Python Data Module
All scope items, parameters, and verified outputs as constants.
Include full PRV calc chain (all 7 factors) as explicit separate lines. Verify independently.

### Step 5: Determine PARAMETERS Row Numbers
Identify exact LSH row. For multi-FAC formula buildings it will not be B40.
Document this row number before writing ESTIMATE or DD1391 formulas.

### Step 6: Build PARAMETERS Tab
### Step 7: Build SCOPE_DETAIL Tab
### Step 8: Build ESTIMATE Tab
### Step 9: Build DD1391_BLOCK9 Tab
### Step 10: Apply Borders (post-processing pass)
### Step 11: Prefix Documentation Strings
### Step 12: Patch File Properties
### Step 13: Run recalc.py
### Step 14: Verify data_only=True (zero None values)
### Step 15: Final Delivery Check

---

## Pre-Delivery Checklist (Mandatory -- All Items)

**Values**
- [ ] recalc.py: status success, total_errors 0
- [ ] data_only=True: zero None values in all key cells
- [ ] Base Direct = confirmed sum of scope items exactly
- [ ] Construction Subtotal = ROUND(base x 1.85 x esc x 1.10 x 1.10, 0)
- [ ] Construction Base = Construction Subtotal + LSH
- [ ] Total Funded within $1 of target
- [ ] Total Project within $1 of target
- [ ] UNIFORMAT SUMIF total = Base Direct (B5)
- [ ] Block9 subtotal = ESTIMATE!B8/1000

**PRV Verification (run for this building specifically)**
- [ ] PRV method confirmed: iNFADS or formula (state which)
- [ ] If iNFADS: RPUID and confirmed dollar value recorded in PARAMETERS and Section F
- [ ] If formula: all 7 Equation 3-1 factors listed individually in PARAMETERS
- [ ] Formula cross-check uses FULL Equation 3-1 (not Q×PUC×ACF alone)
- [ ] SF used in cross-check is total AE/HE SF per FAC -- not partial or adequate-only
- [ ] PUCs verified by direct read of UFC 3-701-01 current change Table 3 (not memory)
- [ ] LSH = PRV × 2.5% verified by independent calculation
- [ ] LSH value in PARAMETERS matches LSH in ESTIMATE row 10 and DD1391_BLOCK9
- [ ] Section F Item 11 narrative updated with correct SF, full Eq 3-1, and confirmed deltas

**Tab Headers (G-11)**
- [ ] ESTIMATE R1: `SCH-XXXX  |  ROM COST ESTIMATE  |  LEVEL 3  |  FY27  |  PAX ID XXXXXX  |  Fi Web XXXXXXX`
- [ ] SCOPE_DETAIL R1: `SCH-XXXX  |  SCOPE DETAIL & QUANTITY TAKEOFF  |  BASE YEAR FY24 CONUS DIRECT COSTS  |  Fi Web XXXXXXX`
- [ ] PARAMETERS R1: `SCH-XXXX  |  COST ESTIMATE PARAMETERS  |  LEVEL 3 ROM  |  FY27  |  PAX ID XXXXXX  |  Fi Web XXXXXXX`
- [ ] DD1391_BLOCK9 R1: `SCH-XXXX  |  COST ESTIMATE PARAMETERS  |  LEVEL 3 ROM  |  FY27  |  PAX ID XXXXXX  |  Fi Web XXXXXXX`
- [ ] No tab uses "DD FORM 1391 BLOCK 9" format in the title bar

**Freeze Panes (G-12)**
- [ ] SCOPE_DETAIL: NO freeze pane (pane element absent from sheetView in XML)
- [ ] ESTIMATE, PARAMETERS, DD1391_BLOCK9: freeze at A2

**Post-Recalc XML Patch (G-13)**
- [ ] Post-recalc XML patch has been run (NOT skipped)
- [ ] styles.xml: zero occurrences of wrapText="true" -- all "1"
- [ ] All worksheet rows: customHeight="1" (not "true"), dyDescent="0.25" present
- [ ] All worksheet cols: customWidth="1" (not "true")
- [ ] sheetFormatPr: dyDescent="0.25" present on all 4 sheets

**Separator Discipline (G-14)**
- [ ] No " -- " anywhere in any cell in any tab
- [ ] No em dashes anywhere
- [ ] All header segments separated by "  |  " (two spaces, pipe, two spaces)

**Merge Cell Audit (G-15) -- run after ANY row insertion or renumbering**
- [ ] Extract all <mergeCell ref="..."/> entries and verify none span A:C on a version history or data row
- [ ] No content row has a full-span merge unless it is intentionally a section header (navy background)
- [ ] All merge refs that reference renumbered rows have been updated to the new row numbers

**Version History B Column (G-16)**
- [ ] All version history B cells (Total Funded) are hardcoded integers -- no formulas, no =B18, no cross-sheet refs
- [ ] Current version row B value matches ROUND() Total Funded computed at build time

**Color Scheme (G-25)**
- [ ] Read fill hex values from gold standard (SCH-3270 v9) before building -- never guess
- [ ] SCOPE_DETAIL group header rows: FF2E4A7A (dark navy, white text)
- [ ] SCOPE_DETAIL item rows: cols A/B/C/G/H/I/J = no fill (00000000); cols D/E/F = FFEBF5FF
- [ ] SCOPE_DETAIL subtotal rows: cols A/G/H/I/J = FFBDD7EE; cols B-F = no fill
- [ ] SCOPE_DETAIL grand total row: FF1B2A4A (dark navy, white text)
- [ ] ESTIMATE Total Funded: FFBDD7EE; Total Project: FF2E4A7A
- [ ] DD1391_BLOCK9 child lines: no fill; Subtotal/Total Funded: FFBDD7EE; Total Project: FF2E4A7A
- [ ] 18-point color spot-check script passed with zero failures

**Version Label Discipline (G-18)**
- [ ] Zero occurrences of "APEX OMEGA" in sharedStrings.xml
- [ ] All version history labels use format: "v1 (date)", "v2 (date)", "v3 (date) - CURRENT"

**Delivery Method (G-19)**
- [ ] PARAMETERS delivery method reads "Design-Build (DB)"
- [ ] Matches DD Form 1391 Block 11 delivery method statement

**Block 9 Adder Formula Verification (G-20)**
- [ ] Contingency formula references SUBTOTAL row (not the last scope item row)
- [ ] All adder rows verified against independently computed expected values
- [ ] Full Block 9 table verified: all rows, expected vs actual, tolerance < $0.50K

**Yellow Flag Discipline (G-21)**
- [ ] Every yellow-flagged item is genuinely unconfirmed
- [ ] No client-confirmed scope is flagged yellow
- [ ] CCN confirmed in PARAMETERS
- [ ] PRV source documented in Section F Items 7 and 11

**Japan District Compliance (G-37 through G-42)**
- [ ] PARAMETERS includes Japan District authority stack text field (G-37)
- [ ] Section F Item 1 references JDDG and JED Cost Estimating Guide (G-37)
- [ ] Section F Item 9 states unit cost tier with rationale (G-41)
- [ ] Section F Item 11 includes JDDG 2.9.1 renovation vs. replacement narrative (G-39)
- [ ] NAVRAMP RPC confirmed or yellow-flagged at intake (G-38)
- [ ] If Okinawa: radon, humid environment, corrosion scope evaluated (G-38, G-40)
- [ ] JED Cost Estimating Guide in project directory (G-42)

**Workbook**
- [ ] Exactly 4 tabs in correct order
- [ ] Font: Calibri throughout (active cells only -- residual unused style entries acceptable per G-8)
- [ ] UNIFORMAT codes NOT on subtotal rows
- [ ] No accuracy percentage ranges anywhere
- [ ] No em dashes anywhere
- [ ] No vendor names anywhere
- [ ] No "Z10" -- scan ALL 4 TABS (ESTIMATE, SCOPE_DETAIL, PARAMETERS, DD1391_BLOCK9), all columns (per G-6)
- [ ] No "PPEI" -- correct acronym is PPE
- [ ] No "OSD/CAPE Tri-Service memorandum"
- [ ] No "UFC 3-740-05" -- correct is UFS 3-740-05
- [ ] No proportional allocation formulas in DD1391 child lines
- [ ] No "Table 3" in any LSH context -- LSH authority is Equation 3-1 + NAVFAC 11010.44E CH-1 + MCO 11000.12 (per G-2)
- [ ] No "10 U.S.C. § 2802" outside Classification of Work section (per G-3)
- [ ] UFC 3-730-01 cited as "UFC 3-730-01 (2024)" everywhere (per G-4)
- [ ] Borders applied on all data rows; spacer rows clean

**File Properties**
- [ ] Creator = Anthony L. Potter
- [ ] Company = Booz Allen Hamilton
- [ ] zip integrity: testzip() returns None
- [ ] styles.xml font names: Calibri only

**Methodology**
- [ ] Section F has exactly 13 items (per G-5 -- Item 13 Version History is mandatory)
- [ ] Yellow items listed in Item 10
- [ ] PRV deviation documented in Item 11 with full Eq 3-1 cross-check
- [ ] Item 7 LSH cites Equation 3-1, NAVFAC 11010.44E CH-1, and MCO 11000.12 -- NOT "Table 3" (per G-2)
- [ ] Item 3 ACF does NOT cite 10 U.S.C. § 2802 (per G-3)
- [ ] Item 8 cites "UFC 3-730-01 (2024)" (per G-4)
- [ ] Prepared By format correct and date updated
- [ ] JPY rate flagged yellow if unverified

---

## Authority References (LOCKED -- verified Mar 2026)

### VALID -- Use These

**Cost / Pricing**
- UFC 3-701-01 w/Change 7 (25 Jul 2025) -- DoD Facilities Pricing Guide; PUCs, ACF, LSH, Equation 3-1
- UFC 3-730-01 (2024) -- Programming Cost Estimates for Military Construction; DB Design 4%
- UFS 3-740-05 (2 Feb 2026) -- Construction Cost Estimating; non-mandatory; For Information Only
  Cite as UFS not UFC. No accuracy percentage tables. Never cite accuracy ranges.
- NAVFAC 11010.44E CH-1 -- Shore Facilities Planning Manual (NOT "G" suffix)
- 10 U.S.C. Section 2802 -- Military Construction Projects

**Japan District (mandatory local layer per JDDG 1.5)**
- JDDG v9.0 (April 2025) -- Japan District Design Guide; design criteria, Okinawa-specific
  requirements, ERC/renovation thresholds, radon (9.11.2, 19.11), humid environment (9.5.2, 12.17),
  power infrastructure (1.7, Ch.14), environmental (Ch.19)
- JED Cost Estimating Guide (Nov 2025) -- USACE Japan Engineer District Cost Estimating Guide;
  cost sources (01.8), estimate software (MCACES/MII, PACES), markup structure (02.2.6),
  QC process (Ch.04), submittal requirements (Ch.03), metric UOM (02.2.9.5)
- JES (Japan Edited Specifications) -- used first per JDDG 1.6; UFGS where JES not available
- JEGS (Japan Environmental Governing Standards) -- Okinawa environmental obligations
- NAVRAMP Guidebook for Naval Shore Installations -- radon program implementation
- UFC 3-101-01 -- Architecture; radon mitigation requirements (para 2-5.1)
- UFC 3-310-04 -- Seismic Evaluation and Retrofit of Existing Buildings

**Marine Corps Real Property**
- UFC 2-000-05N -- DON/USMC Category Codes and FAC codes
- MCO P11000.5G w/CH-1 -- Real Property Facilities Manual Vol IV
- MCO 11000.12 (08 Sep 2014) -- Marine Corps Facilities Planning and Programming
- MCO 5530.14A -- Physical Security (vault door authority)
- MCO 5110.1 -- Unit Mail (mail room authority)

**Facilities / Systems**
- UFC 4-010-05 -- Sensitive Compartmented Information Facilities
- UFC 3-580-01 -- Telecommunications Building Cabling Systems
- UFC 3-420-01 -- Plumbing Systems
- UFC 3-470-06 -- Asbestos-Containing Materials
- UFC 3-470-03 -- Lead-Based Paint
- UFC 3-601-02 -- Fire Suppression and Alarm Systems
- UFC 3-530-01 -- Interior and Exterior Lighting and Controls
- UFC 3-410-01 -- HVAC Systems
- UFC 3-520-01 -- Interior Electrical Systems
- NFPA 72 -- National Fire Alarm and Signaling Code
- NFPA 101 -- Life Safety Code
- NFPA 14 -- Standpipe and Hose Systems
- ASHRAE 62.1 -- Ventilation for Acceptable Indoor Air Quality
- IPC 2021 -- International Plumbing Code
- IBC Chapter 10 -- Egress requirements
- NEC -- National Electrical Code
- TIA-607-C -- Telecommunications grounding and bonding

**Environmental / Safety**
- 40 CFR Part 61 NESHAP -- Asbestos
- 40 CFR Part 745 -- EPA RRP Rule (lead paint)
- OSHA 1926.1101 -- Asbestos (construction)
- OSHA 1926.62 -- Lead (construction)

**Security / Communications**
- DoD 4525.6-M Ch.5 -- Mail system requirements
- GSA Class V specification -- Vault door standard
- DoDI 5200.08 -- Physical security of SCIF
- CNSSAM TEMPEST/01-13 -- RED/BLACK Installation Guidance

### DO NOT CITE -- CONFIRMED INVALID OR WRONG
- MCO 11000.22 -- Family Housing only
- NAVFAC 11010.44G -- wrong suffix; correct is CH-1
- Any accuracy percentage range for any estimate level
- "OSD/CAPE Tri-Service memorandum" -- cite as "OSD FY25 published rate"
- UFC 3-740-05 -- does not exist; correct designation is UFS 3-740-05
- "Z10" as a formal code -- use "General Requirements"
- Vendor/product names in scope
- "PPEI" -- correct acronym is PPE
- Any UFS 3-740-05 accuracy tables

---

## Absolute Rules (No Exceptions)

1. Never invent a number, reference, scope item, Fi Web number, PRV, PUC, or CCN.
2. If unknown: ask. A gap is not a license to fill in a plausible value.
3. Never cite a document that has not been confirmed to exist in that exact form.
4. Never assume a value carries forward from another building without explicit confirmation.
5. Verify all math before writing. State the independent calculation.
6. Flag every unverified item yellow in SCOPE_DETAIL col F. List all in Section F Item 10.
7. DB Design is always applied AFTER Total Funded. No exceptions.
8. LSH always applies, regardless of scope magnitude.
9. Carry all values to the dollar. Round only in DD 1391 Block 9 ($000s).
10. Exactly 4 tabs every time. No fifth tab. No METHODOLOGY tab. No exceptions.
11. Methodology is inline Section F of ESTIMATE only. Never a separate tab.
12. JPY is display-only. ROM chain is USD only.
13. Exchange rate must have source and date. Never use stale rate silently.
14. All calculation cells must be real Excel formulas. Run recalc.py. Zero errors.
15. Multi-FAC PRV: sum each (GSF × PUC) independently; apply ACF and all Eq 3-1 factors
    to the combined total. Never blend PUCs. Never apply combined factor per-FAC.
16. PRV source must be stated: Property Record Current PRV (non-conversion per G-29/G-30)
    OR formula PRV with post-conversion FAC codes (conversion per G-30).
    Q x PUC x ACF alone is NOT a valid PRV formula. It is missing HF, PD, SIOH, CF.
    AE Worksheet "PRV at EOY" is NEVER the governing value (G-29).
17. All three PRV values must be documented in Section F Item 11: Property Record Current PRV
    (with RPUID and pull date), AE Worksheet PRV (with evaluation date), and formula PRV
    cross-check (with FAC codes, PUCs, and full Eq 3-1). State which governs and why.
    Compute and document the ERC ratio per G-32.
18. UNIFORMAT SUMIF: codes on item rows only; verify SUMIF total = B5 exactly.
19. No proportional allocation formulas in DD1391 child lines.
20. If existing estimate provided in different format: extract scope items only; rebuild to v11 standard.
21. Fi Web number must come from Anthony. Never construct or guess it.
22. Never pass a PatternFill as a font argument -- fatal styles.xml corruption.
23. Borders are a post-processing pass after all tabs are built.
24. Verify styles.xml font names contain only "Calibri" before delivery.
25. If any pre-delivery check fails: fix, re-run recalc.py, re-verify. Never deliver with known failures.
27. Sub-PRV rows for multi-FAC buildings = GSF × PUC only. Never include ACF in a sub-PRV row. (G-1)
28. "Table 3" is PUC authority only. Never cite it as LSH authority. LSH cites Equation 3-1 +
    NAVFAC 11010.44E CH-1 + MCO 11000.12 (08 Sep 2014). (G-2)
29. 10 U.S.C. § 2802 belongs only in Classification of Work. Remove from ACF, scope, and
    methodology citations. (G-3)
30. UFC 3-730-01 always cited as "UFC 3-730-01 (2024)". Never without the year. (G-4)
31. Section F must have exactly 13 items. Item 13 (Version History) is mandatory. Never deliver
    with 12 items. (G-5)
32. Z10 scan covers all 4 tabs, all columns. Zero occurrences required. (G-6)
33. Properties patching sequence is locked: build → properties → patch app.xml → recalc → verify.
    Never run recalc before app.xml patch. Never re-save with openpyxl after recalc. (G-7)
34. For any formula-method building: PARAMETERS must have individual named rows for HF, PD,
    SIOH (Eq 3-1), CF, and combined factor (1.23606). The combined factor row drives Total PRV. (G-9)
35. When a building's CCN has no direct Table 3 PUC entry: select nearest Table 3 FAC by
    function and reference size; document proxy selection in Section F Item 11; never use
    FAC 6102 for a battalion-scale building; never guess or silently apply a PUC. (G-10)
36. Tab headers follow the prescribed format exactly on all 4 tabs. SCOPE_DETAIL omits PAX ID
    and FY. DD1391_BLOCK9 uses the PARAMETERS header format. All use "  |  " separators.
    Read G-11 header table before writing any title bar. Never deliver with missing PAX ID or
    LEVEL 3 in any tab that requires it. (G-11)
37. SCOPE_DETAIL has NO freeze pane. ESTIMATE, PARAMETERS, DD1391_BLOCK9 freeze at A2.
    A SCOPE_DETAIL freeze pane hides rows when the file opens. Verify by reading pane element
    from XML -- must return None on SCOPE_DETAIL. (G-12)
38. Post-recalc XML patch is mandatory after every recalc.py call. LibreOffice writes
    wrapText="true" (ignored by Excel), missing dyDescent, and customHeight="true".
    These cause text overflow and broken row heights. Patch all 4 worksheets and styles.xml
    before delivery. Never deliver without confirming zero "true" booleans in OOXML. (G-13)
39. Separators are "  |  " everywhere. No " -- ", no " - ", no em dashes in any cell.
    Run a grep scan for " -- " and "\u2014" across all 4 tabs before delivery. (G-14)
40. When inserting rows and renumbering, update ALL merge cell references that point to
    shifted rows. Audit <mergeCells> after every row operation. No content row may have a
    full A:C merge unless it is intentionally a section header. (G-15)
41. Version history B column (Total Funded) must always be a hardcoded integer. Never a
    formula or cross-sheet reference. Copy the ROUND() result at build time and write it
    as a literal value. (G-16)
42. Active Arial font xf entries in styles.xml must be patched to Calibri before delivery.
    Verify no active xf references an Arial fontId. G-8 residual exception does not apply
    to fontIds that are actively referenced by any xf. (G-17)
43. "APEX OMEGA" must never appear in any cell in any tab. Version labels are v1, v2, v3
    etc. with date only. Pre-delivery grep of sharedStrings.xml for "APEX OMEGA" required.
    Zero hits required. (G-18)
44. Delivery method for all five Camp Schwab buildings is Design-Build (DB). Never DBB.
    Never Design-Bid-Build. PARAMETERS and DD Form 1391 Block 11 must match. (G-19)
45. After any scope addition or row insertion, re-verify all Block 9 adder formulas.
    Contingency must reference SUBTOTAL row, not the last scope item row. Run full Block 9
    verification table before delivery. (G-20)
46. Yellow flags are for genuinely unconfirmed items only. Client-confirmed scope from
    drawings, site visits, or direct instruction is never flagged yellow. (G-21)
47. A complete, submission-ready estimate has exactly one yellow item: the JPY rate in
    PARAMETERS. Any other yellow flag means the estimate is not complete. (G-22)
48. SCOPE_DETAIL grand total must sum group subtotal rows only -- never a contiguous range
    spanning both item rows and subtotals. Using =SUM(G4:G{last_row}) causes double-counting.
    Use =G{sub1}+G{sub2}+...+G{subN}. Verify data_only Base Direct = ESTIMATE Base Direct after recalc. (G-23)
49. LSH in PARAMETERS must always be a hardcoded integer dollar value. Never =PRV x LSH Rate
    as a live formula. The .425 cent remainder causes Total Funded rounding failures. (G-24)
50. Color fills must exactly match the gold standard. Never invent a fill hex that is not in the
    locked palette. Read fills from SCH-3270 v9 directly if uncertain. Run the 18-point color
    spot-check before every delivery. A fabricated fill requires a full rebuild. (G-25)
51. PARAMETERS row numbers are NOT the same across all five buildings. SCH-3270 has compound
    escalation factor at B39 (not B21), JPY at B41, and other parameters shifted accordingly.
    NEVER copy cross-sheet formula patterns from one building's code to another without verifying
    each PARAMETERS row number in the target building. Use the cross-reference table in G-26. (G-26)
52. SCH-3237 Total Funded is $1,399,544 (Base Direct $218,320). Prior skill versions stated
    $1,396,620 / $217,280 -- those were wrong. Always use the CEPBKUP file values. (G-26)
53. SCH-3237 has 4 yellow-flagged open items as of 09 Mar 2026 and is NOT G-22 complete.
    It is NOT submission-ready without resolving cage dims, comm infrastructure scope, PWD ENV
    ACM confirmation, and the JPY rate. (G-22)
54. Japan District authority stack (JDDG v9, JED Cost Estimating Guide) must be cited in
    PARAMETERS and Section F for all JED-area projects. Omitting the district layer is a
    compliance gap. (G-37)
55. NAVRAMP RPC must be confirmed at intake for all Okinawa projects. Default RPC 2 if
    unconfirmed. M67400-0004 is the ACF site code, NOT a NAVRAMP RPC. Never conflate. (G-38)
56. Section F Item 11 must include JDDG 2.9.1 renovation vs. replacement narrative with
    ERC ratio, 50% PRC threshold, seismic trigger, occupancy reclassification, and full
    citation stack. (G-39)
57. Okinawa humid environment and corrosion scope per JDDG 9.5.2 / 12.17 must be evaluated
    for every estimate. Include, exclude with rationale, or flag for FEAD. (G-40)
58. Unit cost source tier (Tier 1 Japan-market or Tier 2 RS Means/ACF) must be stated in
    Section F Item 9 with rationale per JED 01.8. (G-41)
59. JED Cost Estimating Guide must be in project directory and catalogued in skill file. (G-42)

---

### G-25: Color scheme must exactly match gold standard -- never invent fills

**Root cause:** SCH-3213 v5 used fabricated colors in SCOPE_DETAIL and DD1391_BLOCK9 that did not
match the gold standard (SCH-3270 v9). Specifically: group header rows were given a custom light green
fill (FFE2EFDA) that does not exist in the palette; subtotal rows were given a fabricated light blue
(FFBDD7EE on all columns including B-F); item row columns A/C/G/H/I/J were given incorrect fills;
DD1391_BLOCK9 child lines were given fills that gold standard leaves as no-fill. These errors were
caught on visual inspection and required a full v6 rebuild.

**The correct palette is extracted from the gold standard file by reading it with openpyxl, not by
guessing or recalling from memory.** Before building any new workbook, verify each fill assignment
against the actual hex values in SCH-3270 v9 (or whichever is the current gold standard).

**EXACT FILL ASSIGNMENTS (locked from SCH-3270 v9 direct read 20 Mar 2026):**

| Location | Cell(s) | Fill | Notes |
|----------|---------|------|-------|
| SCOPE_DETAIL group header row | Full merged row | FF2E4A7A | Dark navy, white bold text |
| SCOPE_DETAIL item row col A/B/C | 00000000 | No fill | Plain white/transparent |
| SCOPE_DETAIL item row col D/E/F | FFEBF5FF | Light blue -- blue text input cells |
| SCOPE_DETAIL item row col G/H/I/J | 00000000 | No fill |
| SCOPE_DETAIL subtotal row col A | FFBDD7EE | Light blue fill, no text |
| SCOPE_DETAIL subtotal row col B/C/D/E/F | 00000000 | No fill |
| SCOPE_DETAIL subtotal row col G/H/I/J | FFBDD7EE | Light blue fill |
| SCOPE_DETAIL grand total row | All cols | FF1B2A4A | Dark navy, white bold text |
| ESTIMATE Construction Base | All 3 cols | FFD9E1EC | Slightly darker gray |
| ESTIMATE Total Funded | All 3 cols | FFBDD7EE | Light blue |
| ESTIMATE Total Project | All 3 cols | FF2E4A7A | Dark navy, white text |
| DD1391_BLOCK9 child lines (rows 4-14) | All cols | 00000000 | No fill |
| DD1391_BLOCK9 Subtotal | All cols | FFBDD7EE | Light blue |
| DD1391_BLOCK9 adder rows (contingency, LSH, Design, SIOH, CM) | All cols | 00000000 | No fill |
| DD1391_BLOCK9 Total Funded | All cols | FFBDD7EE | Light blue |
| DD1391_BLOCK9 Classification header | Full merged | FF2E4A7A | Dark navy, white text |
| DD1391_BLOCK9 Classification items | All cols | 00000000 | No fill |
| DD1391_BLOCK9 DB Design row | All cols | 00000000 | No fill |
| DD1391_BLOCK9 Total Project | All cols | FF2E4A7A | Dark navy, white text |
| DD1391_BLOCK9 Locked params header | Full merged | FF2E4A7A | Dark navy, white text |
| DD1391_BLOCK9 locked param rows | All cols | 00000000 | No fill |

**Rule:** If any fill assignment is uncertain, read the gold standard file directly with openpyxl
and extract the exact hex. Do not guess. Do not use placeholder colors. Do not invent a new fill
because it "looks better." The palette is locked and not negotiable.

**Verification command (run before delivery):**
```python
# Spot-check at least these cells against expected hex values before delivering
checks = [
    (ws_sd.cell(grp_header_row, 1).fill.fgColor.rgb, 'FF2E4A7A'),   # group header
    (ws_sd.cell(item_row, 1).fill.fgColor.rgb, '00000000'),          # item col A
    (ws_sd.cell(item_row, 4).fill.fgColor.rgb, 'FFEBF5FF'),          # item col D input
    (ws_sd.cell(subtotal_row, 1).fill.fgColor.rgb, 'FFBDD7EE'),      # subtotal col A
    (ws_sd.cell(subtotal_row, 2).fill.fgColor.rgb, '00000000'),      # subtotal col B (no fill)
    (ws_sd.cell(grand_total_row, 1).fill.fgColor.rgb, 'FF1B2A4A'),   # grand total
    (ws_est.cell(18, 1).fill.fgColor.rgb, 'FFBDD7EE'),               # Total Funded
    (ws_est.cell(20, 1).fill.fgColor.rgb, 'FF2E4A7A'),               # Total Project
    (ws_b9.cell(child_line_row, 1).fill.fgColor.rgb, '00000000'),    # DD1391 child line
    (ws_b9.cell(subtotal_row, 1).fill.fgColor.rgb, 'FFBDD7EE'),      # DD1391 subtotal
    (ws_b9.cell(total_project_row, 1).fill.fgColor.rgb, 'FF2E4A7A'), # DD1391 total project
]
```
All 18+ checks must pass before delivery. Failed color check = rebuild required.

---

### G-37: Japan District authority stack must appear in PARAMETERS and Section F

**Root cause:** v24.0 and prior versions cite UFC/UFS authorities exclusively. JDDG 1.5
mandates all estimate submittals for Japan District work must comply with the JED Cost
Estimating Guide. Omitting the district-layer authorities creates a compliance gap.

**Rule:** For any Japan District project, PARAMETERS must include a locked text field
stating the full cost criteria stack: "UFS 3-701-01 (current), UFC 3-730-01 (2024),
UFS 3-740-05 (2 Feb 2026), JED Cost Estimating Guide (Nov 2025), JDDG v9.0 (Apr 2025)."
Section F Item 1 must reference this stack. Section F Item 9 must state the unit cost
tier (Tier 1 Japan-market or Tier 2 RS Means/ACF) with rationale.

---

### G-38: NAVRAMP RPC confirmation required at intake for all Okinawa projects

**Root cause:** NAVRAMP Appendix B assigns each Navy/Marine Corps installation a Radon
Potential Category (1, 2, or 3). Camp Schwab's RPC is not publicly available. Without
confirmation, radon scope cannot be properly scoped or excluded.

**Rule:** Intake question 27 must be answered for every Okinawa project. If RPC is not
confirmed, carry default RPC 2 (Screening) per NAVRAMP guidebook and flag YELLOW.
Include radon evaluation/mitigation scope for inhabited facilities on that basis.
For conversion buildings with occupancy change, radon evaluation is required regardless
of RPC 1 vs 2. Only RPC 3 (documented by PWD ENV) exempts from routine requirements.
M67400-0004 is the UFS/UFC ACF site code. It is NOT a NAVRAMP RPC. Never conflate.

---

### G-39: Section F Item 11 must include JDDG 2.9.1 renovation vs. replacement narrative

**Root cause:** JDDG 2.9.1 requires a renovation vs. replacement narrative for all renovation
projects in Japan District. The ERC section of the skill provides the math but prior versions
did not require a JDDG-cross-walked narrative in Section F.

**Rule:** Section F Item 11 for any Japan District renovation must include:
(a) ERC ratio (Total Funded / governing PRV) per G-32
(b) 50% PRC threshold assessment (BULLETIN 3302, UFC 4-010-01)
(c) Seismic trigger assessment (UFC 3-310-04: >50% SDC C, >30% SDC D/E/F)
(d) Occupancy reclassification assessment (UFC 4-010-01, independent of cost ratio)
(e) Citation stack: UFS 3-701-01, UFC 4-010-01, UFC 3-310-04, JDDG v9 2.9.1

---

### G-40: Okinawa humid environment and corrosion scope must be addressed

**Root cause:** JDDG 9.5.2 and 12.17 require corrosion-resistant envelope, coatings,
sealants, and enhanced HVAC/dehumidification for Okinawa projects. These are standard
requirements, not optional add-ons. Current Camp Schwab estimates predate JDDG integration
and do not carry this scope.

**Rule:** For any new estimate or major update to an existing estimate for an Okinawa
project, evaluate whether corrosion-resistant and humid environment scope items are
needed. If included, cite JDDG 9.5.2 and/or 12.17.x as the basis. If excluded (e.g.,
existing building envelope not in renovation scope), document the exclusion rationale
in Section F Item 9. For the current five Camp Schwab buildings, this is a FEAD
coordination item to be addressed during DB-RFP design development.

---

### G-41: Unit cost source tier must be documented in Section F

**Root cause:** JED Cost Estimating Guide Section 01.8 establishes a cost source hierarchy
(vendor quotes, Japan-market databases, US cost databases). Prior estimates documented
"RS Means FY24 CONUS" as the basis but did not state the tier or the rationale for using
Tier 2 instead of Tier 1.

**Rule:** Section F Item 9 must state the unit cost tier used for the estimate and provide
the rationale. For Level 3 ROMs using RS Means with ACF: state "Tier 2 per JED 01.8;
parametric CONUS direct costs with ACF. Japan-market database pricing (Tier 1) will be
applied by FEAD estimator during detailed estimate development."

---

### G-42: JED Cost Estimating Guide file must be in project directory and catalogued

**Root cause:** JED_Cost_Estimating_Guidance_Combined_2025_Nov.pdf was present in the
project directory but not catalogued in prior skill versions.

**Rule:** The JED Cost Estimating Guide is a mandatory reference file for Japan District
estimating work. It must be present in the project directory and listed in the skill file.
Current file: JED_Cost_Estimating_Guidance_Combined_2025_Nov.pdf (80 pages, Nov 2025).

---

### G-43: DMS filename is never a drawing number

**Root cause:** 03 Apr 2026 session. Multiple message drafts referenced "Drawing 11804" and
"drawing 11819" as if those were drawing numbers. They are DMS file identifiers local to the
project management system. They do not appear on the physical drawing. The recipient looking
at the drawing will see only the sheet number printed in the title block.

**Rule:** Before any drawing reference goes into a client-facing deliverable, confirm the sheet
number from the title block. Use the sheet number in the message. DMS filenames may be
included parenthetically if the recipient already saw that filename in a shared file (e.g.,
"Sheet 20-20 (11804.tif)") but the sheet number must lead and the filename must be secondary.
Never use a DMS filename as a standalone drawing reference.

---

### G-44: Archive sheet search protocol

**Root cause:** 03 Apr 2026 session. Three low-resolution contact sheet iterations were
required to find Sheet 14-19 in the as-built archive. Full-set contact sheets below
approximately 400px cell height cannot reliably resolve Japanese sheet numbers.

**Rule:** When searching for a specific sheet in a ZIP-format drawing archive:
1. Identify a known adjacent sheet (e.g., Sheet 15-19 is in S2P1 page 9).
2. Extract pages in a 5-page window around that position at 5x resolution.
3. Read title block corners individually at 5x before building any contact sheet.
4. Confirm sheet title and number from the title block before using any content.

---

### G-45: Detector coverage claims require dual drawing cross-check

**Root cause:** 03 Apr 2026 session. The statement "both sides of the proposed EOD partition
wall already have detector coverage" was made based on the fire alarm layout alone, without
cross-referencing the RFP Concept PPT to confirm partition wall position relative to detectors.

**Rule:** Any statement about fire alarm or life safety device coverage relative to proposed
construction requires two drawings read in the same session: (1) the as-built system layout
showing current device positions, and (2) the scope or concept drawing showing proposed wall
locations. Without both, the coverage relationship cannot be stated. Flag for FPE determination.

---

### G-46: Survey language requires a document on file

**Root cause:** 03 Apr 2026 session. "Based on site surveys conducted by the team" appeared
in a draft without any specific survey document on file covering fire alarm devices. The phrase
was picked up from a conversational mention and used as an evidentiary basis.

**Rule:** Survey language in any deliverable requires a specific document on file with:
performing organization, date, and scope. No document means no mention. No exceptions for any
survey type: fire alarm, structural, environmental, MEP, hazmat, or geotechnical.

---

### G-47: Unconfirmed device identifications must be attributed

**Root cause:** 03 Apr 2026 session. "The photo James shared shows a horn/strobe mounted on
the wall" was stated as confirmed fact when the identification came from Robert Beller's
message, not from a drawing read. Correct form: "As noted in your message, the installed
notification appliances are horn/strobes."

**Rule:** If a device type, condition, or installation detail was described by a colleague but
not confirmed by a drawing read this session, attribute it to that person explicitly. Never
restate a colleague's observation as an independently confirmed fact.

---

### G-48: Prior-session facts must be flagged until re-verified

**Root cause:** 03 Apr 2026 session. Construction type, area figures, and concrete
specifications were carried forward from a prior session without re-verification this session.

**Rule:** Any factual claim originating from a prior session that has not been re-confirmed
by a drawing or document read in the current session must be flagged internally as
"(prior session -- not re-verified this session)." Flag is removed only after direct
confirmation. In client-facing content, omit unverifiable prior-session claims or state
the basis explicitly.

---

## DB-RFP SCOPE REFERENCE DELIVERABLES (v20.0 -- 22 Mar 2026)

### Purpose

Five Excel scope reference files were built for the FEAD DB-RFP package development effort.
These are point-in-time extractions from the locked CEPBKUP estimate files, organized by
discipline and work group, intended for use by FEAD engineers building the Design-Build RFP
packages for all five Camp Schwab buildings. They are NOT cost estimate replacements -- they
are scope reference tools derived from the estimates that are attached as supporting documents
to the DD Form 1391 packages.

### Deliverable Files (built 22 Mar 2026)

| File | Building | Source Estimate | Item Count | Groups |
|------|----------|----------------|------------|--------|
| SCH1024_DBRFP_SCOPE_MAR26.xlsx | SCH-1024 Armory / BEQ Conversion | v11 (19 Mar 2026) | 74 | 11 |
| SCH3213_DBRFP_SCOPE_MAR26.xlsx | SCH-3213 CLB-4 BN HQ Conversion | v6 (20 Mar 2026) | 73 | 11 |
| SCH3237_DBRFP_SCOPE_MAR26.xlsx | SCH-3237 Covered Storage / Armory Wing | v4 (09 Mar 2026) | 15 | 6 |
| SCH3270_DBRFP_SCOPE_MAR26.xlsx | SCH-3270 Auto Organizational Shop | v9 (19 Mar 2026) | 42 | 10 |
| SCH3314_DBRFP_SCOPE_MAR26.xlsx | SCH-3314 Battalion Squadron HQ | v3 (18 Mar 2026) | 23 | 10 |

### Structure of Each File

Each xlsx has three sections:

1. BUILDING IDENTITY: PAX ID, Fi Web, CCN, GSF, delivery method, first-draft caveat.
2. SCOPE SUMMARY BY DISCIPLINE: one row per discipline, plain-language summary of what
   that discipline owns in this building. Sourced from ESTIMATE tab Section F and SCOPE_DETAIL
   group headers. No editorializing beyond what the files state.
3. DETAILED SCOPE BY WORK GROUP: one row per scope item. Columns: Scope Group | Item | Group |
   Work Description | Qty | Unit | UNIFORMAT. All values sourced directly from SCOPE_DETAIL tab.

### Source Integrity Rules (PERMANENT)

These rules govern every future rebuild or update of these files:

1. Every scope line item must be sourced directly from the SCOPE_DETAIL tab of the
   corresponding CEPBKUP file. No scope may be invented, inferred, or carried from memory.
   Run openpyxl read against the file before building. Zero exceptions.

2. Scope descriptions may be condensed for column width but must never change the technical
   meaning, quantities, unit types, or authority citations. When in doubt, use the full
   cell text from the file.

3. Summary rows (Scope Summary by Discipline section) must be sourced from ESTIMATE tab
   Section F narratives, UNIFORMAT section descriptions, and SCOPE_DETAIL group headers.
   They must not characterize scope beyond what the source files state. No age characterizations,
   condition assessments, or urgency language unless that exact language appears in the file.
   Exception: scope items that contain explicit condition language (e.g., "END OF SERVICE LIFE,"
   "past ASHRAE 30-yr service life," "2010 vintage approaching EOL") may and should be carried
   through because they came from the file.

4. SCH-1024 is a developing estimate. The xlsx is a point-in-time snapshot from v11 (19 Mar 2026).
   When scope is added to the 1024 estimate, this file must be rebuilt from the updated CEPBKUP.
   Teams channel post for 1024 must note this explicitly.

5. Buildings must never be cross-contaminated. Before delivering any rebuild, verify item
   counts against the table above. A count mismatch means scope from another building leaked in.

6. The xlsx files do not replace the estimates. They are derived from the estimates.
   The estimates are the primary documents attached to the DD Form 1391 packages.

### Build Script Location

Build script: /home/claude/build_xlsx_v2.py (session working directory -- does not persist
between sessions; must be re-uploaded or rebuilt from this skill if a new session is needed).

The summary patch logic is embedded at the bottom of the script before the workbook build loop.
If rebuilding from scratch: read all five CEPBKUP SCOPE_DETAIL tabs first, verify item counts,
then build. Never build from memory or from a prior session's output.

### Teams Channel Posts

Five corresponding Teams channel messages were drafted (22 Mar 2026). Format: paste the
Teams message first, then paste the xlsx content (copy-paste from Excel renders as clean grid
in Teams). Each message acknowledges first-draft status, flags open items by discipline, and
notes that errors and changes are expected throughout the project life cycle.

Key open items flagged in channel posts:
- SCH-1024: chiller tonnage must be verified with FEAD mechanical before specs; HAZMAT LF
  quantities are perimeter estimates requiring FEAD ENV/IH field verification.
- SCH-3213: ACM re-inspection required before design starts (2001 Bhate survey, 25 yrs old).
- SCH-3237: cage dimensions and LF unconfirmed; comm ROM preliminary (additional site survey
  needed); PWD ENV confirmation pending on whether Room 101 flooring was replaced since 2001 survey.
- SCH-3270: two lighting fixtures with optical sensors require fire detection coordination per
  NFPA 72 before execution.
- SCH-3314: ACP-2 replacement handled by G-F PPE separately; ACP-3/4/5 and building chiller
  NOT in scope; coordinate with G-6 and security before vault/SIPR design is developed.

### Factual Output Standard (locked 22 Mar 2026)

Anthony's explicit direction: factual information on this project is non-negotiable. There can
never be speculation. If there is the slightest inclination of a speculative output, stop and
say so before delivering anything. This applies to all scope descriptions, quantities, authority
citations, summary characterizations, and channel post language. If a value is not in a source
file, it does not go in the deliverable.

