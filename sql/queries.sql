
-- 1. Top 5 Fund Houses by Assets Under Management

SELECT
    fund_house,
    ROUND(SUM(aum_crore),2) AS total_aum_crore
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum_crore DESC
LIMIT 5;

-- 2. Average NAV by Month

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav),2) AS average_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- 3. SIP Year-over-Year Growth

SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;

-- 4. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM investor_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Funds with Expense Ratio below 1%

SELECT
    scheme_name,
    fund_house,
    category,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 6. Top 10 Funds by 5-Year Return

SELECT
    scheme_name,
    fund_house,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 7. Average Expense Ratio by Category

SELECT
    category,
    ROUND(AVG(expense_ratio_pct),2) AS avg_expense_ratio
FROM scheme_performance
GROUP BY category
ORDER BY avg_expense_ratio;

-- 8. Number of Schemes in Each Fund House

SELECT
    fund_house,
    COUNT(*) AS total_schemes
FROM fund_master
GROUP BY fund_house
ORDER BY total_schemes DESC;

-- 9. Average Portfolio Weight by Sector

SELECT
    sector,
    ROUND(AVG(weight_pct),2) AS average_weight
FROM portfolio_holdings
GROUP BY sector
ORDER BY average_weight DESC;

-- 10. Latest Closing Value of Every Benchmark Index

SELECT
    b1.index_name,
    b1.date,
    b1.close_value
FROM benchmark_indices b1
WHERE b1.date = (
    SELECT MAX(b2.date)
    FROM benchmark_indices b2
    WHERE b2.index_name = b1.index_name
)
ORDER BY b1.index_name;