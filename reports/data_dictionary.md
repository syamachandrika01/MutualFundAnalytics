# Mutual Fund Analytics - Data Dictionary

## 1. 01_fund_master.csv

| Column             | Data Type | Business Definition            | Source     |
| ------------------ | --------- | ------------------------------ | ---------- |
| amfi_code          | INTEGER   | Unique AMFI scheme code        | AMFI India |
| fund_house         | TEXT      | Asset Management Company (AMC) | AMFI       |
| scheme_name        | TEXT      | Mutual fund scheme name        | AMFI       |
| category           | TEXT      | Fund category                  | AMFI       |
| sub_category       | TEXT      | Fund sub-category              | AMFI       |
| plan               | TEXT      | Direct/Regular plan            | AMFI       |
| launch_date        | DATE      | Scheme launch date             | AMFI       |
| benchmark          | TEXT      | Benchmark index                | AMFI       |
| expense_ratio_pct  | REAL      | Annual expense ratio (%)       | AMFI       |
| exit_load_pct      | REAL      | Exit load percentage           | AMFI       |
| min_sip_amount     | REAL      | Minimum SIP amount             | AMFI       |
| min_lumpsum_amount | REAL      | Minimum lump sum investment    | AMFI       |
| fund_manager       | TEXT      | Fund manager name              | AMFI       |
| risk_category      | TEXT      | Risk category                  | AMFI       |
| sebi_category_code | TEXT      | SEBI category code             | AMFI       |

---

## 2. 02_nav_history.csv

| Column    | Data Type | Business Definition | Source   |
| --------- | --------- | ------------------- | -------- |
| amfi_code | INTEGER   | AMFI scheme code    | mfapi.in |
| date      | DATE      | NAV date            | mfapi.in |
| nav       | REAL      | Net Asset Value     | mfapi.in |

---

## 3. 03_aum_by_fund_house.csv

| Column         | Data Type | Business Definition                  | Source |
| -------------- | --------- | ------------------------------------ | ------ |
| date           | DATE      | Reporting date                       | AMFI   |
| fund_house     | TEXT      | Asset Management Company             | AMFI   |
| aum_lakh_crore | REAL      | Assets under management (lakh crore) | AMFI   |
| aum_crore      | REAL      | Assets under management (crore)      | AMFI   |
| num_schemes    | INTEGER   | Number of schemes                    | AMFI   |

---

## 4. 04_monthly_sip_inflows.csv

| Column                    | Data Type | Business Definition         | Source |
| ------------------------- | --------- | --------------------------- | ------ |
| month                     | DATE      | Reporting month             | AMFI   |
| sip_inflow_crore          | REAL      | Monthly SIP inflow          | AMFI   |
| active_sip_accounts_crore | REAL      | Active SIP accounts         | AMFI   |
| new_sip_accounts_lakh     | REAL      | New SIP accounts            | AMFI   |
| sip_aum_lakh_crore        | REAL      | SIP Assets Under Management | AMFI   |
| yoy_growth_pct            | REAL      | Year-over-year growth (%)   | AMFI   |

---

## 5. 05_category_inflows.csv

| Column           | Data Type | Business Definition  | Source |
| ---------------- | --------- | -------------------- | ------ |
| month            | DATE      | Reporting month      | AMFI   |
| category         | TEXT      | Mutual fund category | AMFI   |
| net_inflow_crore | REAL      | Net inflow in crore  | AMFI   |

---

## 6. 06_industry_folio_count.csv

| Column              | Data Type | Business Definition   | Source |
| ------------------- | --------- | --------------------- | ------ |
| month               | DATE      | Reporting month       | AMFI   |
| total_folios_crore  | REAL      | Total investor folios | AMFI   |
| equity_folios_crore | REAL      | Equity folios         | AMFI   |
| debt_folios_crore   | REAL      | Debt folios           | AMFI   |
| hybrid_folios_crore | REAL      | Hybrid folios         | AMFI   |
| others_folios_crore | REAL      | Other folios          | AMFI   |

---

## 7. 07_scheme_performance.csv

| Column             | Data Type | Business Definition           | Source |
| ------------------ | --------- | ----------------------------- | ------ |
| amfi_code          | INTEGER   | AMFI scheme code              | AMFI   |
| scheme_name        | TEXT      | Scheme name                   | AMFI   |
| fund_house         | TEXT      | Fund house                    | AMFI   |
| category           | TEXT      | Category                      | AMFI   |
| plan               | TEXT      | Plan type                     | AMFI   |
| return_1yr_pct     | REAL      | 1-year return (%)             | AMFI   |
| return_3yr_pct     | REAL      | 3-year return (%)             | AMFI   |
| return_5yr_pct     | REAL      | 5-year return (%)             | AMFI   |
| benchmark_3yr_pct  | REAL      | Benchmark 3-year return       | AMFI   |
| alpha              | REAL      | Alpha metric                  | AMFI   |
| beta               | REAL      | Beta metric                   | AMFI   |
| sharpe_ratio       | REAL      | Sharpe ratio                  | AMFI   |
| sortino_ratio      | REAL      | Sortino ratio                 | AMFI   |
| std_dev_ann_pct    | REAL      | Annualized standard deviation | AMFI   |
| max_drawdown_pct   | REAL      | Maximum drawdown              | AMFI   |
| aum_crore          | REAL      | AUM in crore                  | AMFI   |
| expense_ratio_pct  | REAL      | Expense ratio (%)             | AMFI   |
| morningstar_rating | INTEGER   | Morningstar rating            | AMFI   |
| risk_grade         | TEXT      | Risk grade                    | AMFI   |

---

## 8. 08_investor_transactions.csv

| Column             | Data Type | Business Definition      | Source    |
| ------------------ | --------- | ------------------------ | --------- |
| investor_id        | INTEGER   | Investor identifier      | Simulated |
| transaction_date   | DATE      | Transaction date         | Simulated |
| amfi_code          | INTEGER   | AMFI scheme code         | Simulated |
| transaction_type   | TEXT      | SIP, Lumpsum, Redemption | Simulated |
| amount_inr         | REAL      | Transaction amount (INR) | Simulated |
| state              | TEXT      | Investor state           | Simulated |
| city               | TEXT      | Investor city            | Simulated |
| city_tier          | TEXT      | Tier 1/2/3 city          | Simulated |
| age_group          | TEXT      | Investor age group       | Simulated |
| gender             | TEXT      | Investor gender          | Simulated |
| annual_income_lakh | REAL      | Annual income (lakh)     | Simulated |
| payment_mode       | TEXT      | Payment method           | Simulated |
| kyc_status         | TEXT      | KYC verification status  | Simulated |

---

## 9. 09_portfolio_holdings.csv

| Column            | Data Type | Business Definition      | Source  |
| ----------------- | --------- | ------------------------ | ------- |
| amfi_code         | INTEGER   | AMFI scheme code         | AMFI    |
| stock_symbol      | TEXT      | Stock ticker             | NSE/BSE |
| stock_name        | TEXT      | Company name             | NSE/BSE |
| sector            | TEXT      | Industry sector          | NSE/BSE |
| weight_pct        | REAL      | Portfolio weight (%)     | AMFI    |
| market_value_cr   | REAL      | Market value (crore)     | AMFI    |
| current_price_inr | REAL      | Current stock price      | NSE/BSE |
| portfolio_date    | DATE      | Portfolio reporting date | AMFI    |

---

## 10. 10_benchmark_indices.csv

| Column      | Data Type | Business Definition  | Source |
| ----------- | --------- | -------------------- | ------ |
| date        | DATE      | Trading date         | NSE    |
| index_name  | TEXT      | Benchmark index name | NSE    |
| close_value | REAL      | Closing index value  | NSE    |
