# Deliverable 01 - LSH Placement Decision
## Where the 2.5%-of-PRV Life Safety and Health adder lives on the face of Block 9

**Date:** 26 April 2026
**Prepared by:** Anthony L. Potter, Facilities Planner, MCIPAC G-F PPE, Booz Allen Hamilton
**Buildings governed:** SCH-1024, SCH-3213, SCH-3237, SCH-3270, SCH-3314 (Camp Schwab portfolio, FY27)

---

## Bottom line up front

The May 2024 CRB manual is silent on LSH placement. Place the LSH allowance on Block 9 as a **Special Construction Features** sub-line under **Supporting Facilities** (manual §3.1, sequencing item 1; defined in §4.9). Description reads "SPECIAL CONSTRUCTION FEATURES - Life Safety and Health Upgrades (2.5% of PRV)". The dollar value is preserved exactly as in the CEPBKUP workbook. Authority for the LSH allowance itself remains NAVFAC 11010.44E CH-1 and MCO 11000.12 (8 Sep 2014); these citations live in the Block 10 standard statement, not on the Block 9 face.

If Rob disagrees with that placement, the fallback rolls LSH inside the Primary Facility line cost (no separate sub-line; Block 10 statement carries the breakout). Both placements preserve the dollar value.

---

## 1. Does the manual address LSH directly?

No. A full-text search across the OCR'd 93-page manual (working/crb_master.txt) for the following terms returned no Block 9 placement guidance:
- "life safety" (one hit on page 56, listing building systems generally)
- "LSH" - zero hits
- "MCO 11000.12" - zero hits
- "NAVFAC 11010.44E" - zero hits
- "Life Safety and Health" - zero hits
- "2.5%" - zero hits in the LSH context
- "program adder" - zero hits

The manual covers MCON (Military Construction) and MCNR (Marine Corps Non-Recurring) projects. The 2.5%-of-PRV LSH allowance is a Marine Corps FSRM (Facilities Sustainment, Restoration, and Modernization) program adder authorized under MCO 11000.12 and NAVFAC 11010.44E CH-1. The CRB manual does not enumerate FSRM-specific cost components.

Inference is required. Documented below.

## 2. What the AF exemplars show

Eielson (F-35A OSS, 2018), Fairford (RC-135 Intel, 2018), Nellis (Red Flag, 2018) - none show an LSH line. The Air Force does not use a LSH program adder. AF absence is not evidence of correct placement. The exemplars do confirm the cosmetic architecture of Block 9 (Primary Facilities → Supporting Facilities → Subtotal → Contingency → Total Contract Cost → SIOH → DB Design → Total Request → Total Request Rounded → Equipment from Other Appropriations).

## 3. Recommended placement: Special Construction Features (Supporting Facilities)

**Rationale, anchored to the manual:**

a. Manual §3.1 sequencing of Supporting Facilities lists "SPECIAL CONSTRUCTION FEATURES - if applicable" as item 1. (CRB Guidelines May 2024, p. 19)

b. Manual §4.9 defines Special Construction Features as "those items that are built into or are part of the facility (e.g., radon gas removal system in the foundation). The SPECIAL CONSTRUCTION FEATURES line-item will be listed under the Supporting Facilities." (CRB Guidelines May 2024, p. 30)

c. LSH represents life-safety / health code compliance work that is built into the facility (sprinkler upgrades, egress improvements, fire alarm modernization, asbestos abatement at the building system level, etc.). It fits the Special Construction Features definition.

d. Placing LSH under Special Construction Features satisfies Rob's directive that there not be a standalone "LSH" line. The line description is the function (Life Safety and Health upgrades), with the 2.5%-of-PRV authority cited in the Block 10 standard statement. This is the same pattern the AF uses for "Sustainability and Energy Measures" (a percentage allowance that lives in the Primary or Supporting section, not on its own row below the subtotal).

e. The dollar value is preserved exactly. No re-computation. The number from the CEPBKUP workbook flows directly to this line.

**What the line looks like on Block 9:**

```
SUPPORTING FACILITIES                  $X,XXX
 SPECIAL CONSTRUCTION FEATURES                 ($X,XXX)
  (Life Safety and Health upgrades, 2.5% of PRV per
   NAVFAC 11010.44E CH-1 / MCO 11000.12)
 [other Supporting Facilities sub-lines as applicable]
```

## 4. Fallback placement: roll LSH inside the Primary Facility line cost

If Rob does not accept Special Construction Features as the home for LSH (objection on grounds that §4.1 says Supporting Facilities are "outside the five-foot line" and LSH is inside the building envelope, even though §4.9 explicitly contradicts that for Special Construction Features):

The fallback is to absorb LSH into the Primary Facility line cost. The Primary Facility line shows the building name with a single dollar value that includes Subtotal + Contingency + LSH. The Block 10 standard statement (PS) discloses the LSH share and authority. No separate LSH sub-line.

Pros: zero risk of a reviewer flagging a free-standing LSH line.
Cons: less auditability on the face of Block 9; reviewers asking "why is this conversion's unit cost so high?" must follow through to Block 10.

## 5. Risk and review notes

- The 8.0% SIOH rate in use across all five Camp Schwab buildings is the OCONUS FSRM customer-directed rate, not the standard 7.3% OCONUS rate per DASD-Con direction (manual §3.4). Camp Schwab is on the Remote OCONUS list which carries 9.0% (manual page 24, line 1014), so the 8.0% sits between the two and is documented in each workbook's Section F-8 / Section F-11.

- The 6.0% Design line and 4.0% Construction Management line are NAVFAC agency-directed adders that the manual does not address (manual §3.5 only addresses DB Design at 4% of Subtotal). These are MARINE CORPS / NAVY norms that do not appear on AF Block 9 examples. If Rob asks why they exist, the answer is NAVFAC 11010.44E CH-1 plus MCIPAC G-F program direction.

- Total Project Cost = Total Funded + DB Design (4% applied AFTER Total Funded per UFC 3-730-01, 2024). The workbook's chain treats DB Design as a post-Total Funded adder, not as 4% of Subtotal as the manual states in §3.5. This is a Marine Corps FSRM convention divergence, not a Block 9 cosmetic issue. Dollar values preserved. The deliverable Block 9 will display DB Design under the proper line label and at the proper position; Block 10 documents the calculation method.

## 6. Supporting page citations from the OCR

Manual pages 19, 30, 32, 24, 22, 23 establish the architecture, the Sub-total definition, the SIOH rate, the Design cost rule, and the Contingency rule.
- p. 19 (line 819) - Block 9 line-item sequencing
- p. 30 (line 1436) - Special Construction Features definition
- p. 32 (line 1425) - Sub-total definition
- p. 24 (line 1014) - Remote OCONUS list including Camp Schwab vicinity (CNMI/Guam/Diego Garcia/etc.)
- p. 22 (line 953) - SIOH rates
- p. 23 (line 1021) - DB Design 4% of Sub-total

A few page citations are flagged as approximate where OCR confidence is reduced; these are noted in the canonical template.
