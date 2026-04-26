**To:** Robert W. Kaye, RA - Planning Director, NAVFAC FEAD
**Cc:** Bil Hawkins, P.E., PMP - Deputy PWO, MCB Camp Butler G-F
**From:** Anthony L. Potter - Facilities Planner, MCIPAC G-F PPE, Booz Allen Hamilton
**Subject:** Camp Schwab FY26 Block 9: Proposed PAX Coding Change for the 5-Building FSRM Portfolio

Rob,

I sat down with the PAX 1391 Processor for the Camp Schwab FY26 portfolio (SCH-1024, SCH-3213, SCH-3237, SCH-3270, SCH-3314), looked at how Block 9 is coded today, and put together a proposed change that lines up the entry method with the May 2024 Consistency Review Board Guidelines. SCH-1024 is the worked example. The change is in draft only and nothing has been entered or modified in PAX yet, since we are in the pencils-down editing moratorium for the FY26 cycle. Dollar values do not change; Total Funded Cost and Total Project Cost stay consistent with the cost estimate workbook to the dollar.

There are three attachments. The CRB Guidelines manual (May 2024). A Word-doc walkthrough that steps through SCH-1024 and lists the renamed scope lines. A one-page diagram that shows the SCH-1024 entry side by side, before and after the change.

Here is what is in PAX today for SCH-1024. The Block 9 Data items table holds 18 rows. The top row is the iNFADS-locked building line (MULTI PURPOSE BEQ/BOQ/CO HQS, Quantity 1.00, Unit Cost $10,412,000.00). Below it sit eleven scope rows entered as dollar items, each starting with a UNIFORMAT II Level 2 prefix (B20, C10, C30, D20, D30, D40, D50, E20, F20, G10, G20). The last six rows are the cost rollup adders, also entered as dollar items: Contingency $552K, LSH $2,413K, Planning and Design $509K, SIOH $679K, CM $339K, and DB Design $401K. The Associated Costs dialog has four percent slots (Contingency, Supervision Inspection and Overhead, Design Build, Planning and Design) and all four are presently set to 0.00 percent. Because every adder is already absorbed as a dollar line item, the printed form shows Subtotal $10,412K equal to Total Funded Cost equal to Total Project Cost.

The proposed change moves the rollup adders out of the items table and into the Associated Costs dialog where they belong as percentages. The eleven scope rows lose their UNIFORMAT prefixes and read in plain English. The Associated Costs dialog gets populated: Contingency 10.00 percent, Supervision Inspection and Overhead 8.00 percent, Design Build 4.00 percent, Planning and Design 10.00 percent. The Planning and Design slot covers the NAVFAC 6 percent Design plus the 4 percent Construction Management combined; PAX does not have a CM percent slot, so CM rides under Planning and Design and the breakout is disclosed in the Block 10 narrative.

LSH is the one wrinkle. PAX has no Life Safety and Health slot in the Associated Costs dialog, so the $2,413K (2.5 percent of iNFADS PRV $96,523,347 per NAVFAC 11010.44E CH-1 and MCO 11000.12) cannot ride under a percent. Two options preserve the dollar value. Option A keeps LSH as a single dollar line item in the items table, matching how it sits today. Option B bakes the $2,413K into the scope total with the breakout disclosed in Block 10. The methodology call goes to Bil before PAX entry.

One reconciliation step at entry. The exact Total Project Cost on the printed form after the change cannot be predicted without rendering it, since PAX has not been observed running these percentages against the items table outside of the all-zero state. The cost estimate workbook target is $10,413K rounded ($10,012K Total Funded). After the change, the printed form gets generated and reconciled against the cost estimate workbook. If the numbers do not match, the resolution is one of three: switch the LSH option, tune the percentage rates to match PAX's base, or align the cost estimate workbook to PAX's calculation. The reconciliation gets logged in Section F-11 of the cost estimate workbook.

If the proposed coding reads workable for SCH-1024, the same approach mirrors across SCH-3270, SCH-3213, SCH-3237, and SCH-3314. The percentage rates are identical for all five and the LSH option chosen for SCH-1024 applies to the other four. Open to walking through the example whenever works for you.

V/R,

Anthony Potter
Facilities Planner | MCIPAC G-F PPE
Booz Allen Hamilton

Attachments:
- Consistency Review Board 1391 Development Guidelines (22 May 2024 Edition)
- PAX 1391 Coding Walkthrough, SCH-1024 (Word doc)
- PAX Block 9, SCH-1024 BEFORE and AFTER (one-page diagram)
