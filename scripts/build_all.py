"""Generic workbook builder for all five Schwab buildings.
Builds COVER, BLOCK9, BLOCK10, BACKUP, RATES, REFERENCES tabs.
Math chain: BACKUP back-solves Locked TPC -> Unit Cost ($/SF, 2 dp).
PAX rollup applies Cont 10% / SIOH 8% / DBD 4% / P&D 6% NON ADD.
Workbook TPC = Locked TPC at $000 by construction.
"""
import openpyxl, re, os
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill

B = Font(bold=True)
THIN = Side(style="thin")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
HDR = PatternFill("solid", fgColor="D9D9D9")
LOCK = PatternFill("solid", fgColor="FFF2CC")

BUILDINGS = [
    {
        "id": "1024", "fi": "BU26PPE70M", "pax": 387356, "rpuid": 148675, "ccn": 14345,
        "infads": "MULTI PURPOSE BEQ/BOQ/CO HQS",
        "title": "Repair Bldg 1024, Armory Expansion & Admin Conversion",
        "uic": "M67400 (SH)", "gsf": 84861, "prv": 96523347, "lsh": 2413084,
        "locked_tpc": 10413140, "unit_cost": 99.32,
        "out": "1024_G_CEPBKUP_BU26PPE70M_POM26_20260319.xlsx",
        "narr_src": "working/1024.txt",
    },
    {
        "id": "3213", "fi": "BU26PPE72M", "pax": 387624, "rpuid": 48879, "ccn": 61010,
        "infads": "COMPANY HQ",
        "title": "Repair Bldg 3213, Convert to CLB-4 Headquarters",
        "uic": "M67400 (SH)", "gsf": 13484, "prv": 10893334, "lsh": 272333,
        "locked_tpc": 5397928, "unit_cost": 324.00,
        "out": "3213_G_CEPBKUP_BU26PPE72M_POM26_20260320.xlsx",
        "narr_src": "working/3213.txt",
    },
    {
        "id": "3237", "fi": "BU26PPE73M", "pax": 387622, "rpuid": 51473, "ccn": 44112,
        "infads": "WAREHOUSE/ARMORY",
        "title": "Repair Bldg 3237, Warehouse Partition Multi-Unit Storage",
        "uic": "M67400 (SH)", "gsf": 30973, "prv": 26636215, "lsh": 665905,
        "locked_tpc": 1455526, "unit_cost": 38.04,
        "out": "3237_G_CEPBKUP_BU26PPE73M_POM26_20260309.xlsx",
        "narr_src": "working/3237.txt",
    },
    {
        "id": "3270", "fi": "BU26PPE74M", "pax": 387568, "rpuid": 1174058, "ccn": 21451,
        "infads": "AUTO ORGANIZATIONAL SHOP CAB",
        "title": "Repair Bldg 3270",
        "uic": "M67400 (SH)", "gsf": 25390, "prv": 39507617, "lsh": 987690,
        "locked_tpc": 3527753, "unit_cost": 112.46,
        "out": "3270_G_CEPBKUP_BU26PPE74M_POM26_20260319.xlsx",
        "narr_src": "working/3270.txt",
    },
    {
        "id": "3314", "fi": "BU26PPE71M", "pax": 387433, "rpuid": 50931, "ccn": 61072,
        "infads": "BATTALION SQUADRON HEADQUARTERS",
        "title": "Repair Bldg 3314, Convert to 4th MarRegt Regimental HQ",
        "uic": "M67400 (SH)", "gsf": 28699, "prv": 29826797, "lsh": 745670,
        "locked_tpc": 1949383, "unit_cost": 54.98,
        "out": "3314_G_CEPBKUP_BU26PPE71M_POM26_20260318.xlsx",
        "narr_src": "working/3314.txt",
    },
]


def extract_block10(path):
    if not os.path.exists(path):
        return ""
    with open(path) as f:
        txt = f.read()
    m = re.search(r'10\.\s*Description of Proposed Construction:(.*?)(?=\n11\.\s*Requirement)', txt, re.DOTALL)
    if not m:
        return ""
    n = m.group(1)
    n = re.sub(r'DD1391C? Form.*?\d{2}-\w{3}-\d{2}\s*', '', n, flags=re.DOTALL)
    n = re.sub(r'1\. Component.*?BU26PPE\d+M\s+[\d,]+\s*\n', '', n, flags=re.DOTALL)
    n = re.sub(r'10\. Description of Proposed Construction:\(Continued\)\s*\n', '', n)
    return n.strip()


def build(bldg):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    # COVER
    c = wb.create_sheet("COVER")
    c["A1"] = "DD FORM 1391 COST ESTIMATE"
    c["A1"].font = Font(bold=True, size=14)
    rows = [
        ("Building", f"SCH-{bldg['id']}" if bldg["id"] != "1024" else "Bldg 1024"),
        ("iNFADS Description", bldg["infads"]),
        ("Primary CCN", bldg["ccn"]),
        ("RPUID", bldg["rpuid"]),
        ("PAX ID", bldg["pax"]),
        ("Fi Web Project Number", bldg["fi"]),
        ("Installation/UIC", bldg["uic"]),
        ("Location", "MARINE CORPS BASE, CAMP SMEDLEY BUTLER (CAMP SCHWAB-6009), HENOKO OKINAWA, JAPAN"),
        ("Project Title", bldg["title"]),
        ("Fund Type", "O&MMC"),
        ("Acquisition Method", "Design-Build (DB)"),
        ("Total Building GSF (iNFADS)", bldg["gsf"]),
        ("PRV (iNFADS)", bldg["prv"]),
        ("LSH (2.5% of PRV)", bldg["lsh"]),
        ("Locked Total Project Cost ($)", bldg["locked_tpc"]),
        ("Locked TPC ($000, printed)", round(bldg["locked_tpc"] / 1000)),
        ("Prepared By", "Anthony L. Potter, Facilities Planner, MCIPAC G-F PPE"),
        ("Signing Officer (PWO)", "CDR Justus K. O'Connor"),
        ("Government Client", "Bil Hawkins, P.E., PMP, Deputy PWO"),
        ("Reviewer", "Robert W. Kaye, RA, Planning Director NAVFAC FEAD"),
    ]
    for i, (k, v) in enumerate(rows, start=3):
        c.cell(i, 1, k).font = B
        c.cell(i, 2, v)
    c.column_dimensions["A"].width = 38
    c.column_dimensions["B"].width = 80

    # BACKUP
    bk = wb.create_sheet("BACKUP")
    bk["A1"] = "BACKUP - Locked TPC back-solver (drives BLOCK9 face)"
    bk["A1"].font = Font(bold=True, size=12)
    bk["A3"] = "INPUTS (locked)"; bk["A3"].font = B; bk["A3"].fill = HDR
    bk.cell(4, 1, "Locked TPC ($)").font = B
    bk.cell(4, 2, bldg["locked_tpc"]).fill = LOCK
    bk["B4"].number_format = '"$"#,##0'
    bk.cell(5, 1, "GSF (iNFADS, locked Quantity)").font = B
    bk.cell(5, 2, bldg["gsf"]).fill = LOCK
    bk["B5"].number_format = '#,##0'
    bk.cell(6, 1, "PRV ($, iNFADS)").font = B
    bk.cell(6, 2, bldg["prv"]).fill = LOCK
    bk["B6"].number_format = '"$"#,##0'
    bk.cell(7, 1, "LSH ($, 2.5% of PRV)").font = B
    bk.cell(7, 2, "=B6*0.025").fill = LOCK
    bk["B7"].number_format = '"$"#,##0'
    bk.cell(8, 1, "Multiplier (1.10 x 1.08 x 1.04)").font = B
    bk.cell(8, 2, 1.23552).fill = LOCK
    bk["B8"].number_format = '0.00000'

    bk["A10"] = "PAX ENTRY (what Anthony types into Block 9)"; bk["A10"].font = B; bk["A10"].fill = HDR
    bk.cell(11, 1, "Unit Cost ($/SF) - calibrated to land Locked TPC at $000").font = B
    bk["B11"] = bldg["unit_cost"]
    bk["B11"].number_format = '"$"#,##0.00'
    bk["B11"].fill = LOCK
    bk.cell(12, 1, "Items Table Subtotal (raw $) = GSF x UC").font = B
    bk["B12"] = "=B5*B11"; bk["B12"].number_format = '"$"#,##0'
    bk.cell(13, 1, "Items Table Subtotal ($000)").font = B
    bk["B13"] = "=ROUND(B12/1000,0)"; bk["B13"].number_format = '#,##0'

    bk["A15"] = "PAX ROLLUP (computed from items table subtotal, raw $)"
    bk["A15"].font = B; bk["A15"].fill = HDR
    rollup = [
        ("Subtotal ($)", "=B12"),
        ("Contingency (10.0%)", "=B16*0.10"),
        ("Total Contract Cost", "=B16+B17"),
        ("SIOH (8.0%)", "=B18*0.08"),
        ("Total Funded Cost", "=B18+B19"),
        ("Design-Build Design (4.0%)", "=B20*0.04"),
        ("Total Project Cost ($)", "=B20+B21"),
        ("Total Project Cost ($000)", "=ROUND(B22/1000,0)"),
        ("Planning and Design (6.0%) (NON ADD)", "=B22*0.06"),
    ]
    for i, (k, v) in enumerate(rollup, start=16):
        bk.cell(i, 1, k).font = B
        cc = bk.cell(i, 2, v); cc.number_format = '"$"#,##0'
    bk["B23"].number_format = '#,##0'

    bk["A26"] = "RECONCILIATION"; bk["A26"].font = B; bk["A26"].fill = HDR
    bk.cell(27, 1, "Workbook TPC ($)")
    bk["B27"] = "=B22"; bk["B27"].number_format = '"$"#,##0'
    bk.cell(28, 1, "Locked TPC ($)")
    bk["B28"] = "=B4"; bk["B28"].number_format = '"$"#,##0'
    bk.cell(29, 1, "Delta ($)")
    bk["B29"] = "=B27-B28"; bk["B29"].number_format = '"$"#,##0;[Red]"$"-#,##0'
    bk.cell(30, 1, "Workbook TPC ($000)")
    bk["B30"] = "=B23"; bk["B30"].number_format = '#,##0'
    bk.cell(31, 1, "Locked TPC ($000, printed)")
    bk["B31"] = "=ROUND(B4/1000,0)"; bk["B31"].number_format = '#,##0'
    bk.cell(32, 1, "Delta ($000) - MUST BE 0").font = B
    bk["B32"] = "=B30-B31"; bk["B32"].number_format = '#,##0;[Red]-#,##0'
    bk["B32"].font = B
    bk.column_dimensions["A"].width = 50
    bk.column_dimensions["B"].width = 18

    # BLOCK9
    b9 = wb.create_sheet("BLOCK9")
    b9["A1"] = "9. Cost Estimates"; b9["A1"].font = Font(bold=True, size=12)
    for j, h in enumerate(["Item", "UM", "Quantity", "Unit Cost", "Cost ($000)"], start=1):
        cc = b9.cell(3, j, h)
        cc.font = B; cc.fill = HDR; cc.border = BOX
        cc.alignment = Alignment(horizontal="center")
    b9["A4"] = "PRIMARY FACILITY"; b9["A4"].font = B
    b9["E4"] = "=BACKUP!B13"; b9["E4"].number_format = '#,##0'; b9["E4"].font = B
    primary_label = f"  {bldg['infads']} FAC#{bldg['id']} (Conversion / Alteration)"
    b9["A5"] = primary_label
    b9["B5"] = "SF"; b9["B5"].alignment = Alignment(horizontal="center")
    b9["C5"] = "=BACKUP!B5"; b9["C5"].number_format = '#,##0'
    b9["C5"].alignment = Alignment(horizontal="right")
    b9["D5"] = "=BACKUP!B11"; b9["D5"].number_format = '#,##0.00'
    b9["D5"].alignment = Alignment(horizontal="right")
    b9["E5"] = "=ROUND(C5*D5/1000,0)"; b9["E5"].number_format = '#,##0'
    b9["E5"].alignment = Alignment(horizontal="right")
    for r in range(3, 6):
        for col in range(1, 6):
            b9.cell(r, col).border = BOX

    rows9 = [
        (7, "Subtotal", "=BACKUP!B13", True),
        (8, "Contingency (10.0%)", "=ROUND(BACKUP!B17/1000,0)", False),
        (9, "Total Contract Cost", "=ROUND(BACKUP!B18/1000,0)", True),
        (10, "Supervision, Inspection and Overhead (8.0%)", "=ROUND(BACKUP!B19/1000,0)", False),
        (11, "Total Funded Cost", "=ROUND(BACKUP!B20/1000,0)", True),
        (12, "Design-Build - Design Cost (4.0%)", "=ROUND(BACKUP!B21/1000,0)", False),
        (13, "TOTAL PROJECT COST", "=BACKUP!B23", True),
    ]
    for r, lab, fml, bold in rows9:
        b9.cell(r, 1, lab)
        b9.cell(r, 5, fml).number_format = '#,##0'
        if bold:
            b9.cell(r, 1).font = B
            b9.cell(r, 5).font = B
        if r == 13:
            b9.cell(r, 1).fill = HDR
            b9.cell(r, 5).fill = HDR
    b9["A14"] = "Planning and Design (6.0%) (NON ADD)"
    b9["E14"] = "=ROUND(BACKUP!B24/1000,0)"; b9["E14"].number_format = '"("#,##0")"'
    b9["A15"] = "Equipment from Other Appropriations (NON ADD)"
    b9["E15"] = 0; b9["E15"].number_format = '"("#,##0")"'

    b9["A17"] = "Classification of Work"; b9["A17"].font = B
    b9["A18"] = "  Construction"
    b9["E18"] = "=E13"; b9["E18"].number_format = '#,##0'
    b9["A19"] = "Special Interest Codes"; b9["A19"].font = B
    b9["A20"] = "  Restoration and Modernization"
    b9["E20"] = "=E13"; b9["E20"].number_format = '#,##0'

    b9.column_dimensions["A"].width = 60
    b9.column_dimensions["B"].width = 6
    b9.column_dimensions["C"].width = 12
    b9.column_dimensions["D"].width = 12
    b9.column_dimensions["E"].width = 14

    # BLOCK10
    b10 = wb.create_sheet("BLOCK10")
    b10["A1"] = "10. Description of Proposed Construction"
    b10["A1"].font = Font(bold=True, size=12)
    b10["A3"] = extract_block10(bldg["narr_src"])
    b10["A3"].alignment = Alignment(wrap_text=True, vertical="top")
    b10.column_dimensions["A"].width = 110
    b10.row_dimensions[3].height = 800

    # RATES
    rt = wb.create_sheet("RATES")
    rt["A1"] = "RATES (PAX Associated Costs and project parameters)"
    rt["A1"].font = Font(bold=True, size=12)
    rt["A3"] = "PAX Associated Costs (pre-loaded by operator)"
    rt["A3"].font = B; rt["A3"].fill = HDR
    rates = [
        ("Contingency", 0.10, "FSRM program-directed; CRB Guidelines May 2024 (REV #15)"),
        ("Supervision Inspection and Overhead (SIOH)", 0.08, "OCONUS FSRM customer-directed for MCIPAC G-F"),
        ("Design Build (DBD) - REQUIRED", 0.04, "UFC 3-730-01 (2024) - applied after Total Funded Cost"),
        ("Planning and Design (P&D) (NON ADD)", 0.06, "Does not roll into TPC"),
    ]
    for i, (k, v, src) in enumerate(rates, start=4):
        rt.cell(i, 1, k).font = B
        cc = rt.cell(i, 2, v); cc.number_format = "0.0%"
        rt.cell(i, 3, src)
    rt["A9"] = "Project parameters"; rt["A9"].font = B; rt["A9"].fill = HDR
    params = [
        ("Area Cost Factor (ACF)", 1.85, "UFC 3-701-01 w/Change 7 (25 Jul 2025), Table 4-1, M67400-0004 OCONUS Okinawa"),
        ("LSH Rate (% of PRV)", 0.025, "Local direction at startup"),
        ("JPY/USD Planning Rate", 150.4415, "FY26 budget planning rate"),
        ("JPY/USD H.10 Rate (live)", "", "Verify Federal Reserve H.10 on date of PAX submission"),
        ("Escalation (annual)", 0.021, "OSD FY25 published rate"),
        ("General Requirements", 0.10, "FSRM program-directed"),
    ]
    for i, (k, v, src) in enumerate(params, start=10):
        rt.cell(i, 1, k).font = B
        cc = rt.cell(i, 2, v)
        if isinstance(v, float) and v < 1:
            cc.number_format = "0.0%"
        rt.cell(i, 3, src)
    rt.column_dimensions["A"].width = 38
    rt.column_dimensions["B"].width = 14
    rt.column_dimensions["C"].width = 80

    # REFERENCES
    rf = wb.create_sheet("REFERENCES")
    rf["A1"] = "REFERENCES (authority cites)"
    rf["A1"].font = Font(bold=True, size=12)
    rf.cell(3, 1, "Document").font = B; rf["A3"].fill = HDR
    rf.cell(3, 2, "Date / Edition").font = B; rf["B3"].fill = HDR
    rf.cell(3, 3, "Authority for").font = B; rf["C3"].fill = HDR
    refs = [
        ("MCO 11000.5", "03 Jun 2016", "Real Property FSRM Program"),
        ("MCO 11000.12", "08 Sep 2014", "Real Property Facilities Manual"),
        ("CRB Guidelines (REV #15)", "May 2024", "Block 9 line-item sequencing"),
        ("UFC 3-701-01 with Change 7", "25 Jul 2025", "PUC and ACF tables, Equation 3-1 PRV formula"),
        ("UFC 3-730-01", "2024", "Design-Build contracting; DB Design 4% applied after TFC"),
        ("JED Cost Estimating Guide", "Nov 2025", "Cost estimating methodology"),
        ("Japan District Design Guide v9", "April 2025", "Okinawa-specific design criteria"),
    ]
    for i, (k, d, src) in enumerate(refs, start=4):
        rf.cell(i, 1, k).font = B
        rf.cell(i, 2, d)
        rf.cell(i, 3, src)
    rf["A12"] = "NOT CITED"; rf["A12"].font = B; rf["A12"].fill = HDR
    rf["A13"] = "NAVFAC 11010.44E"
    rf["B13"] = "INACTIVE"
    rf["C13"] = "Inactivated by 1987 issuance; not citable"
    rf.column_dimensions["A"].width = 32
    rf.column_dimensions["B"].width = 18
    rf.column_dimensions["C"].width = 70

    order = ["COVER", "BLOCK9", "BLOCK10", "BACKUP", "RATES", "REFERENCES"]
    wb._sheets = [wb[n] for n in order]
    wb.save(bldg["out"])

    # Math verification
    sub_raw = bldg["gsf"] * bldg["unit_cost"]
    cont = round(sub_raw * 0.10)
    tcc = sub_raw + cont
    sioh = round(tcc * 0.08)
    tfc = tcc + sioh
    dbd = round(tfc * 0.04)
    tpc = tfc + dbd
    tpc_k = round(tpc / 1000)
    locked_k = round(bldg["locked_tpc"] / 1000)
    delta_k = tpc_k - locked_k
    return tpc, tpc_k, locked_k, delta_k


if __name__ == "__main__":
    print(f"{'Bldg':<6} {'GSF':>8} {'UC($/SF)':>10} {'Wbk TPC raw':>14} {'Wbk $000':>10} {'Locked $000':>12} {'Delta':>6}")
    for b in BUILDINGS:
        tpc, tpc_k, locked_k, delta_k = build(b)
        print(f"{b['id']:<6} {b['gsf']:>8,} {b['unit_cost']:>10.2f} {tpc:>14,} {tpc_k:>10,} {locked_k:>12,} {delta_k:>6}")
