# Camp Schwab FY26 Portfolio Rollup

Camp Schwab, Okinawa, Japan  |  MCIPAC G-F PPE  |  FY26 FSRM Straddler portfolio  |  Acquisition method: Design-Build (DB) for all five  |  Fund type: O&MMC  |  Programmed FY26, possible Q1 FY27 award  |  Prepared by Anthony L. Potter, Facilities Planner, MCIPAC G-F PPE  |  Estimate date: 29 Apr 2026

## Portfolio summary

| Building | iNFADS Description | GSF | Locked TPC ($) | Items Subtotal Target ($000) | Printed TPC ($000) |
|----------|--------------------|----:|---------------:|-----------------------------:|-------------------:|
| Bldg 1024 | MULTI PURPOSE BEQ/BOQ/CO HQS | 84,861 | 10,413,140 | 8,480 | 10,413 |
| SCH-3213 | COMPANY HQ | 13,484 | 5,397,928 | 4,395 | 5,398 |
| SCH-3237 | WAREHOUSE/ARMORY | 30,973 | 1,455,526 | 1,186 | 1,456 |
| SCH-3270 | AUTO ORGANIZATIONAL SHOP CAB | 25,390 | 3,527,753 | 2,873 | 3,528 |
| SCH-3314 | BATTALION SQUADRON HEADQUARTERS | 28,699 | 1,949,383 | 1,587 | 1,949 |
| **Portfolio totals** | | **183,407** | **22,743,730** | **18,521** | **22,744** |

Combined PRV (iNFADS): $203,387,310. Portfolio Locked TPC = $22,743,730 = $22,744 ($000). All five reconcile delta = 0 against PAX's per-step rollup chain.

## PAX rollup math (per building)

```
TCC = ROUND(Items Subtotal x 1.10)   (Cont 10% PAX-applied)
TFC = ROUND(TCC x 1.08)              (SIOH 8% PAX-applied)
DB  = ROUND(Items Subtotal x 0.04)   (DB 4% PAX-applied to ITEMS, not to TFC)
TPC = TFC + DB                       (additive, not compounded)
PD  = ROUND(Items Subtotal x 0.06)   (NON ADD; informational only)
```

Effective multiplier from items to TPC = 1.10 x 1.08 + 0.04 = 1.228.

| Building | Items ($000) | TCC | TFC | DB | TPC ($000) |
|----------|-------------:|----:|----:|---:|-----------:|
| Bldg 1024 | 8,480 | 9,328 | 10,074 | 339 | 10,413 |
| SCH-3213 | 4,395 | 4,835 | 5,222 | 176 | 5,398 |
| SCH-3237 | 1,186 | 1,305 | 1,409 | 47 | 1,456 |
| SCH-3270 | 2,873 | 3,160 | 3,413 | 115 | 3,528 |
| SCH-3314 | 1,587 | 1,746 | 1,886 | 63 | 1,949 |

## Project identifiers

| Building | PAX ID | Fi Web | RPUID | Primary CCN | Workbook File |
|----------|-------:|--------|------:|------------:|---------------|
| Bldg 1024 | 387356 | BU26PPE70M | 148675 | 14345 | `1024_G_CEPBKUP_BU26PPE70M_POM26_20260319.xlsx` |
| SCH-3213 | 387624 | BU26PPE72M | 48879 | 61010 | `3213_G_CEPBKUP_BU26PPE72M_POM26_20260320.xlsx` |
| SCH-3237 | 387622 | BU26PPE73M | 51473 | 44112 | `3237_G_CEPBKUP_BU26PPE73M_POM26_20260309.xlsx` |
| SCH-3270 | 387568 | BU26PPE74M | 1174058 | 21451 | `3270_G_CEPBKUP_BU26PPE74M_POM26_20260319.xlsx` |
| SCH-3314 | 387433 | BU26PPE71M | 50931 | 61072 | `3314_G_CEPBKUP_BU26PPE71M_POM26_20260318.xlsx` |

## Discipline rollups by building (paste these into PAX Block 9)

### Bldg 1024  |  $10,413 ($000)  |  Items Subtotal: 8,480 ($000)
| UNIFORMAT | Description | Amount ($000) |
|-----------|-------------|--------------:|
| D50 | Electrical / Communications | 2,774 |
| D30 | HVAC / Mechanical | 2,602 |
| G20 | Site Improvements | 794 |
| F20 | Selective Demolition | 645 |
| C10 | Interior Construction | 580 |
| B20 | Exterior Enclosure | 421 |
| D20 | Plumbing | 307 |
| C30 | Interior Finishes | 269 |
| D40 | Fire Protection | 34 |
| G10 | Site Preparation | 31 |
| E20 | Furnishings | 23 |
| **Items Subtotal** | | **8,480** |

### SCH-3213  |  $5,398 ($000)  |  Items Subtotal: 4,395 ($000)
| UNIFORMAT | Description | Amount ($000) |
|-----------|-------------|--------------:|
| D30 | HVAC / Mechanical | 1,537 |
| D20 | Plumbing | 1,109 |
| C10 | Interior Construction | 864 |
| D50 | Electrical / Communications | 537 |
| F10 | Hazardous Material Abatement | 263 |
| B20 | Exterior Enclosure | 85 |
| **Items Subtotal** | | **4,395** |

### SCH-3237  |  $1,456 ($000)  |  Items Subtotal: 1,186 ($000)
| UNIFORMAT | Description | Amount ($000) |
|-----------|-------------|--------------:|
| D50 | Electrical / Communications | 582 |
| F10 | Hazardous Material Abatement | 319 |
| C10 | Interior Construction | 261 |
| D30 | HVAC / Mechanical | 24 |
| **Items Subtotal** | | **1,186** |

### SCH-3270  |  $3,528 ($000)  |  Items Subtotal: 2,873 ($000)
| UNIFORMAT | Description | Amount ($000) |
|-----------|-------------|--------------:|
| D30 | HVAC / Mechanical | 1,832 |
| D50 | Electrical / Communications | 674 |
| C10 | Interior Construction | 156 |
| B20 | Exterior Enclosure | 80 |
| D20 | Plumbing | 68 |
| C30 | Interior Finishes | 63 |
| **Items Subtotal** | | **2,873** |

### SCH-3314  |  $1,949 ($000)  |  Items Subtotal: 1,587 ($000)
| UNIFORMAT | Description | Amount ($000) |
|-----------|-------------|--------------:|
| D30 | HVAC / Mechanical | 1,364 |
| C10 | Interior Construction | 119 |
| D50 | Electrical / Communications | 61 |
| D20 | Plumbing | 31 |
| F20 | Selective Demolition | 12 |
| **Items Subtotal** | | **1,587** |

## Supported units

- Bldg 1024  |  3rd Marine Logistics Group / III MEF
- SCH-3213  |  4th Marine Regiment / III MEF
- SCH-3237  |  4th Marine Regiment / III MEF
- SCH-3270  |  4th Marine Regiment / CLB-4
- SCH-3314  |  4th Marine Regiment / III MEF

## Authority and basis

- ACF 1.85 (UFC 3-701-01 with Change 7, 25 Jul 2025, Table 4-1, OCONUS Okinawa M67400-0004)
- Escalation 2.1%/yr (OSD FY25 published rate); FY24 base to FY27 target; compound factor (1.021)^3 = 1.0643
- General Requirements 10.0% (FSRM program-directed; UFS 3-740-05)
- PAX Associated Costs at submission: Cont 10%, SIOH 8% (OCONUS FSRM customer-directed), DB 4%, P&D 6% NON ADD
- JPY/USD planning rate: 150.4415 (FY26 budget); H.10 live rate at PAX submission

## Personalities

- CDR Justus K. O'Connor - signing officer (PWO)
- Bil Hawkins, P.E., PMP - Deputy PWO at MCB Camp Butler G-F; government client
- Robert W. Kaye, RA - Planning Director, NAVFAC FEAD; reviewer
- Anthony L. Potter - Facilities Planner, MCIPAC G-F PPE, Booz Allen Hamilton contractor
