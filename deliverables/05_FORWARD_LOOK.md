# Deliverable 05 - Forward-Look Register
## Downstream issues this Block 9 re-architecture surfaces

Each issue: title, why it matters, when it surfaces, what triggers it.

---

## 1. Cost estimate workbook DD1391_BLOCK9 tab rebuild required

**Why it matters.** The corrected Block 9 face uses canonical sequencing (Primary → Supporting → Subtotal → Contingency → TCC → SIOH → Design → CM → Total Funded → DB Design → Total Project Cost). The current workbook DD1391_BLOCK9 tab still uses the old per-line UNIFORMAT layout. As long as the workbook tab and the Block 9 face disagree, every future paste cycle reopens the same conflict.

**When it surfaces.** Next time scope changes (which will happen on at least three of the five buildings before submission).

**What triggers it.** Any scope addition, deletion, or unit-cost revision in SCOPE_DETAIL flows up through ESTIMATE to DD1391_BLOCK9. If DD1391_BLOCK9 still produces the old per-line UNIFORMAT layout, the operator has to re-translate by hand to the canonical layout every time. That re-translation is the gap where the current PAX .md fell behind the workbook.

**Owner action.** Rebuild the DD1391_BLOCK9 tab in each of the five workbooks to mirror the canonical face: PRIMARY FACILITIES (single line), SUPPORTING FACILITIES (Special Construction Features sub-line for LSH), then the cost rollup ladder. Keep the SCOPE_DETAIL tab as-is (UNIFORMAT lives there for internal traceability).

## 2. PAX .md drift vs. workbook

**Why it matters.** The PAX paste-text file (`SCH_Block9_PAX_AllFiveBuildings.md`) was older than the workbook on three of five buildings (SCH-1024 by ~$540K Total Funded; SCH-3270 by ~$1,018K; SCH-3314 entirely undrafted while the workbook was complete). There is no automated link from workbook to paste-text.

**When it surfaces.** Every workbook revision cycle.

**What triggers it.** Anyone updating ESTIMATE or SCOPE_DETAIL in the workbook without rolling those values into the PAX paste-text file the same day.

**Owner action.** The team-internal cost reference (committed at `.claude/skills/dd-1391/`) carries a verification check that pulls workbook DD1391_BLOCK9 totals and compares them to the PAX paste-text. Run the check before any PAX submission.

## 3. SCH-3314 phasing and swing-space risk

**Why it matters.** Full communications replacement at SCH-3314 will take the building offline for 3-6 months with no MCEN access. Building 3410 has been identified as the swing space. Will Lake DOW assessment was due 15 Apr 2026. Phasing language is required in Block 10 / Section F before submission, and the swing-space DOW affects scope and cost.

**When it surfaces.** Pre-submission review. Could push the SCH-3314 package back to the next FY cycle if not resolved.

**What triggers it.** Any change in the swing-space DOW, the unit's MCEN outage tolerance, or the construction sequencing.

**Owner action.** Pull Will Lake's 15 Apr 2026 DOW result. Decide whether the SCH-3314 Block 10 PS gets phasing language inline or whether SCH-3314 is held back from FY27 submission and rolled to FY28. Anthony to coordinate with the client and Will Lake.

## 4. SCH-3314 FAC code crosswalk

**Why it matters.** SCH-3314 CCN is 61072 (Battalion / Squadron HQ - MARCOR). UFC 3-701-01 with Change 7 (25 Jul 2025) Table 3 has no PUC entry for FAC 6189 (the formal mapping from CCN 61072). FAC 6101 (Small Unit HQ, $634/SF) is being used as the best-supported Table 3 proxy. Pending formal RPAO crosswalk confirmation.

**When it surfaces.** When RPAO posts the formal crosswalk, or when a reviewer pushes back on the FAC 6101 proxy.

**What triggers it.** RPAO communication, reviewer comment, or NAVFAC HQ guidance update.

**Owner action.** Open a query to RPAO asking for the formal CCN 61072 → FAC mapping. Until resolved, FAC 6101 proxy is documented in CEPBKUP ESTIMATE Section F-11.

## 5. SCH-3270 PRV deviation

**Why it matters.** SCH-3270 uses iNFADS confirmed PRV $39,507,617 (RPUID 1174058). UFC 3-701-01 formula PRV would be ~$47,028,000 (FAC 2141 at $810/SF, 25,390 SF, full Eq 3-1 multipliers). Delta is $7.52M (16%). iNFADS predates the C7 PUC update cycle. iNFADS governs per UFC 3-701-01 Section 3-2.1, but the delta affects LSH ($188K) and may surface on review.

**When it surfaces.** Any review where the PRV is cross-checked against the formula method, or any iNFADS update that closes the delta.

**What triggers it.** RPAO updating the iNFADS record, or a reviewer pushing back on the iNFADS-vs-formula question.

**Owner action.** Section F Item 11 of the SCH-3270 workbook documents the delta. Same applies to SCH-3213 (~$2.9M PRV delta) and SCH-3314 (~$11.8M PRV delta). Be ready to walk a reviewer through the iNFADS-governs argument with the manual cite.

## 6. SCH-3213 PAX entry format misalignment

**Why it matters.** The current SCH-3213 PAX entry uses whole-thousand rounding while the rest of the portfolio uses three-decimal precision. The corrected Block 9 brings SCH-3213 in line. PAX may or may not accept the change without a re-validation step.

**When it surfaces.** Next PAX submission for SCH-3213.

**What triggers it.** PAX reviewer or system-level rounding rule.

**Owner action.** Submit corrected SCH-3213 Block 9 with three-decimal precision and confirm PAX accepts. If PAX rejects, revert to whole-thousand for that one building only and document the exception.

## 7. JPY/USD exchange rate verification

**Why it matters.** Every workbook PARAMETERS tab carries a JPY/USD rate placeholder (1.56 or 1.57) that is display-only but flagged for verification before submission. The ROM chain is USD-only, so the rate does not affect the dollar values shown on Block 9. Still required for completeness of the workbook record.

**When it surfaces.** Day of PAX submission.

**What triggers it.** Submission cutoff.

**Owner action.** Pull the Federal Reserve H.10 release for the day of submission and update each workbook PARAMETERS tab JPY rate. Re-save. No effect on Block 9 face.

## 8. Next CRB cycle may surface findings beyond Block 9

**Why it matters.** The May 2024 CRB manual covers Block 9, Block 10 (statements), Block 12 (checklist), Appendix C (cybersecurity), and supplemental data. The current correction addresses Block 9 only. The CRB may flag Block 10 PS statements (paired Primary Facility statements with functions provided), Block 12 checklist completeness, or Appendix C cybersecurity calculations.

**When it surfaces.** First CRB review cycle on the corrected packages.

**What triggers it.** CRB reviewer comments.

**Owner action.** Pre-emptively walk Block 10 statements for each building against manual §5.3 (Primary Facilities Statements) and §5.4 (Supporting Facilities Statements). Confirm cybersecurity features and commissioning per §3.6 / Appendix C are addressed in the workbook before the next package goes out.

## 9. The recurring loop

**Why it matters.** Each scope cycle: cost estimate workbook updates → PAX paste-text goes stale → Block 9 face goes stale with it → reviewer comments come in on the stale picture → Anthony has to bridge competing interpretations against a manual that is partially silent. The team-internal cost reference at `.claude/skills/dd-1391/` is the durable artifact that breaks the loop. It captures the manual rules, the locked program adder rates, the LSH placement decision, the verification gates, and the canonical face. Future cycles start from the rulebook, not from memory.

**When it surfaces.** Every revision.

**What triggers it.** Scope change, reviewer comment, or fiscal-year cycle.

**Owner action.** Use the project-scoped reference for any future work in this repo. The user-level copy at `~/.claude/skills/dd-1391/` follows Anthony across other 1391 projects.
