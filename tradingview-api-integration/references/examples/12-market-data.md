# Market Data

- Source: `openapi.json`
- Live Requests: `disabled`

## Table of Contents

- [Get All Market Data](#get-all-market-data)
- [Get Company Profile](#get-company-profile)
- [Get IPO Information](#get-ipo-information)
- [Get Market Indicators](#get-market-indicators)
- [Get TTM Data](#get-ttm-data)
- [Get Current Financial Metrics](#get-current-financial-metrics)
- [Get Quarterly Financials](#get-quarterly-financials)
- [Get Annual Financials](#get-annual-financials)
- [Get Quarterly History](#get-quarterly-history)
- [Get Annual History](#get-annual-history)
- [Get Dividend Data](#get-dividend-data)
- [Get Analyst Recommendations](#get-analyst-recommendations)
- [Get Enterprise Value Metrics](#get-enterprise-value-metrics)
- [Get Credit Ratings](#get-credit-ratings)
- [Get Cash Flow Analysis](#get-cash-flow-analysis)

## Get All Market Data

`GET /api/market-data/{symbol}`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "company": {
      "listed_exchange": "NASDAQ",
      "local_description": "Apple Inc.",
      "cusip": "037833100",
      "isin-displayed": "US0378331005",
      "currency_code": "USD",
      "ceo": "Timothy Donald Cook",
      "isin": "US0378331005",
      "currency-logoid": "country/US",
      "description": "Apple Inc.",
      "sector": "Electronic Technology",
      "web_site_url": "http://www.apple.com",
      "industry": "Telecommunications Equipment",
      "business_description": "Apple, Inc. engages in the design, manufacture, and sale of smartphones, personal computers, tablets, wearables and accessories, and other varieties of related services. It operates through the following geographical segments: Americas, Europe, Greater China, Japan, and Rest of Asia Pacific. The Ame... (605 more chars truncated)",
      "currency_id": "USD",
      "short_description": "Apple Inc.",
      "fundamental_currency_code": "USD",
      "exchange": "Cboe One",
      "timezone": "America/New_York",
      "founded": 1976,
      "country_code": "US",
      "exchange_traded_name": "Cboe One",
      "short-description": "Apple Inc.",
      "local-description": "Apple Inc.",
      "currency-id": "USD",
      "sector-i18n-en": "Electronic Technology",
      "top_revenue_country_code": "US",
      "exchange-listed": "NASDAQ",
      "exchange-listed-symbol": "AAPL",
      "exchange-ticker": "AAPL",
      "country_fund": "United States",
      "country_code_fund": "US",
      "exchange_listed_name": "NASDAQ",
      "description-i18n-en": "APPLE INC",
      "business_description-i18n-en": "Apple, Inc. engages in the design, manufacture, and sale of smartphones, personal computers, tablets, wearables and accessories, and other variety of related services. It operates through the following geographical segments: Americas, Europe, Greater China, Japan, and Rest of Asia Pacific. The Ameri... (601 more chars truncated)",
      "exchange-traded": "Cboe One",
      "country": "United States",
      "currency_fund": "USD",
      "industry-i18n-en": "Telecommunications Equipment",
      "currency": "USD",
      "number_of_employees": 166000
    },
    "ipo": {
      "ipo_offer_date": 345427200
    },
    "indicators": {
      "price_52_week_high": 288.62,
      "market_cap_calc": 4008685001792.9995,
      "earnings_availability": 1,
      "price_percent_change_52_week": 38.4634888438134,
      "earnings_release_date": 1769722200,
      "beta_1_year": 1.1557966,
      "market_cap_basic": 4008685001793,
      "price_52_week_low": 193.25,
      "price_earnings": 34.18988334725069,
      "earnings_release_next_date": 1777581000,
      "price_percent_change_1_week": 5.128402571901587,
      "earnings_release_next_time": 1,
      "earnings_per_share_basic_fh": 4.7083,
      "earnings_release_date_h": [
        1769722200,
        1761856320,
        1753993980
      ],
      "price_annual_sales": 9.743150536234776,
      "beta_5_year": 1.1087966,
      "earnings_per_share_diluted_fh": 4.690300000000001,
      "beta_3_year": 0.8453335,
      "beta_2_year": 1.1140423,
      "earnings_release_calendar_date": 1767139200,
      "earnings_per_share_fh": 4.6899999999999995,
      "beta_10_year": 1.1667725,
      "earnings_release_next_calendar_date": 1774915200,
      "price_book_ratio": 54.143675190042835,
      "earnings_release_time": 1,
      "price_sales_ratio": 9.743150536234776,
      "earnings_per_share_forecast_next_fh": 3.679022,
      "current_ratio": 0.973744664864166,
      "quick_ratio": 0.937561203939224,
      "price_annual_book": 54.143675190042835
    },
    "ttm": {
      "earnings_per_share_basic_ttm": 7.9334,
      "rates_ttm": {
        "time": 1767139200,
        "to_aud": 1.498689,
        "to_cad": 1.373249,
        "to_chf": 0.79277,
        "to_cny": 6.994964,
        "to_eur": 0.851419,
        "to_gbp": 0.74228,
        "to_inr": 89.88764,
        "to_jpy": 156.715248,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "price_earnings_ttm": 34.18988334725069,
      "oper_income_ttm": 141070000000,
      "cost_of_goods_ttm": -229460000000,
      "ebitda_ttm_h": [
        152902000000,
        144748000000,
        141696000000
      ],
      "sale_of_stock_ttm": 0,
      "pre_tax_margin_ttm": 32.4016280356368,
      "capital_expenditures_unchanged_ttm_h": [
        12148000000,
        12715000000,
        12381000000
      ],
      "preferred_dividends_cash_flow_ttm": 0,
      "cash_dividend_coverage_ratio_ttm": 9.30982823195144,
      "non_cash_items_ttm": 14563000000,
      "total_cash_dividends_paid_ttm": -15486000000,
      "changes_in_working_capital_ttm": -8700000000,
      "change_in_accounts_receivable_ttm": -11164000000,
      "net_income_bef_disc_oper_ttm": 117777000000,
      "purchase_of_business_ttm": 0,
      "net_margin_ttm": 27.0368236317683,
      "equity_in_earnings_ttm": 0,
      "sell_gen_admin_exp_other_ttm": -27918000000,
      "sloan_ratio_ttm": -4.801514380551389,
      "earnings_per_share_diluted_ttm": 7.9038,
      "discontinued_operations_ttm": 0,
      "change_in_other_assets_ttm": -6931000000,
      "altman_z_score_ttm": 10.6382004968314,
      "dividend_payout_ratio_ttm": 13.03170626787115,
      "funds_f_operations_ttm": 144172000000,
      "other_financing_cash_flow_sources_ttm": 0,
      "common_dividends_cash_flow_ttm": -15486000000,
      "after_tax_other_income_ttm": 0,
      "pretax_income_ttm": 141147000000,
      "other_investing_cash_flow_uses_ttm": -1031000000,
      "price_free_cash_flow_ttm": 45.9902082357882,
      "total_oper_expense_ttm": -294547000000,
      "capital_expenditures_ttm": -12148000000,
      "cash_f_operating_activities_ttm": 135472000000,
      "enterprise_value_ebitda_ttm": 26.37170868787197,
      "gross_profit_ttm_h": [
        206157000000,
        195201000000,
        190739000000
      ],
      "dep_amort_exp_income_s_ttm": -11832000000,
      "unusual_expense_inc_ttm": 0,
      "issuance_of_stock_net_ttm": -91806000000,
      "return_on_common_equity_ttm": 152.02132328265,
      "price_earnings_growth_ttm": 1.3330112942081678,
      "price_revenue_ttm": 9.1874341494478,
      "other_investing_cash_flow_items_total_ttm": -1031000000,
      "total_revenue_ttm_h": [
        435617000000,
        416161000000,
        408625000000
      ],
      "operating_expenses_ttm": -65087000000,
      "return_of_invested_capital_percent_ttm": 0.7463948363219249,
      "gross_margin_ttm": 47.325288039723,
      "graham_numbers_ttm": 32.66031923925423,
      "other_financing_cash_flow_items_total_ttm": -6075000000,
      "issuance_of_debt_net_ttm": -7604000000,
      "interest_capitalized_ttm": 0,
      "gross_profit_ttm": 206157000000,
      "ebitda_per_share_ttm": 10.323992211936027,
      "other_income_ttm": 77000000,
      "cash_f_investing_activities_ttm": 517000000,
      "capital_expenditures_unchanged_ttm": 12148000000,
      "total_extra_items_ttm": 0,
      "capital_expenditures_other_assets_ttm": 0,
      "free_cash_flow_per_share_ttm": 8.32687613991183,
      "free_cash_flow_ttm": 123324000000,
      "revenue_per_share_ttm": 29.4129999305891,
      "supplying_of_long_term_debt_ttm": 4481000000,
      "purchase_of_stock_ttm": -91806000000,
      "cost_of_goods_excl_dep_amort_ttm": -217628000000,
      "other_investing_cash_flow_sources_ttm": 0,
      "earnings_per_share_diluted_ttm_h": [
        7.9038,
        7.4593,
        6.5782
      ],
      "sell_gen_admin_exp_total_ttm": -65087000000,
      "ebitda_ttm": 152902000000,
      "capital_expenditures_fixed_assets_ttm": -12148000000,
      "operating_cash_flow_per_share_ttm": 9.1471130066016,
      "debt_to_revenue_ttm": 0.2077719648223095,
      "dilution_adjustment_ttm": 0,
      "reduction_of_long_term_debt_ttm": -12087000000,
      "piotroski_f_score_ttm": 9,
      "preferred_dividends_ttm": 0,
      "issuance_of_long_term_debt_ttm": -7606000000,
      "sales_of_business_ttm": 0,
      "purchase_sale_business_ttm": 0,
      "sustainable_growth_rate_ttm": 147.999690369089,
      "non_oper_income_ttm": 77000000,
      "net_income_starting_line_ttm": 117777000000,
      "change_in_accounts_payable_ttm": 8421000000,
      "capex_per_share_ttm": 0.820236866689768,
      "non_oper_interest_income_ttm": 0,
      "purchase_sale_investments_ttm": 13696000000,
      "diluted_net_income_ttm": 117777000000,
      "research_and_dev_ttm": -37169000000,
      "ebitda_margin_ttm": 35.1000993992429,
      "net_income_ttm": 117777000000,
      "cash_flow_deprecation_n_amortization_ttm": 11832000000,
      "pretax_equity_in_earnings_ttm": 0,
      "return_on_equity_adjust_to_book_ttm": 3.3491193072391447,
      "change_in_inventories_ttm": 974000000,
      "other_oper_expense_total_ttm": 0,
      "ebit_ttm": 141070000000,
      "net_income_ttm_h": [
        117777000000,
        112010000000,
        99280000000
      ],
      "issuance_of_short_term_debt_ttm": 2000000,
      "earnings_per_share_ttm": 7.9038,
      "cash_f_financing_activities_ttm": -120971000000,
      "purchase_of_investments_ttm": -30976000000,
      "total_revenue_ttm": 435617000000,
      "sales_of_investments_ttm": 44672000000,
      "zmijewski_score_ttm": -1.3748734798308557,
      "total_non_oper_income_ttm": 77000000,
      "minority_interest_exp_ttm": 0,
      "income_tax_ttm": -23370000000,
      "operating_margin_ttm": 32.3839519577978,
      "other_financing_cash_flow_uses_ttm": -6075000000,
      "ebit_per_share_ttm": 9.525091766869075,
      "free_cash_flow_ttm_h": [
        123324000000,
        98767000000,
        96184000000
      ],
      "cash_flow_deferred_taxes_ttm": 0
    },
    "current": {
      "enterprise_value_current": 4032287001793,
      "total_shares_outstanding_current": 14681100000,
      "price_earnings_current": 34.18988334725069,
      "gross_margin_current": 48.1586855505162,
      "enterprise_value_ebitda_current": 26.37170868787197,
      "total_debt_per_share_current": 6.111196786896953,
      "ebitda_per_share_current": 10.323992211936027,
      "cash_per_share_current": 4.517582156701702,
      "ebitda_margin_current": 37.6095606444253,
      "quick_ratio_current": 0.937561203939224,
      "price_cash_flow_current": 29.542654584563593,
      "book_value_per_share_current": 5.99822,
      "rates_current": {
        "time": 1776729600,
        "to_aud": 1.393534,
        "to_cad": 1.364629,
        "to_chf": 0.778549,
        "to_cny": 6.818957,
        "to_eur": 0.848522,
        "to_gbp": 0.738989,
        "to_inr": 93.10987,
        "to_jpy": 158.831004,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "ebit_per_share_current": 9.525091766869075,
      "debt_to_asset_current": 0.23862303155574702,
      "net_margin_current": 29.2836472912435,
      "ncavps_ratio_current": -10.495965920805313,
      "revenue_per_share_current": 29.4129999305891,
      "dividend_payout_ratio_current": 9.14719954967633,
      "working_capital_per_share_current": -0.289946685313578,
      "market_cap_basic_current": 4008674355000,
      "book_tangible_per_share_current": 5.99821679047723,
      "asset_turnover_current": 1.20438993505506,
      "capex_per_share_current": 0.820236866689768,
      "return_on_invested_capital_current": 74.6394836321925,
      "operating_margin_current": 35.3738278750104,
      "pre_tax_margin_current": 35.4781713458917,
      "price_sales_current": 9.1874341494478,
      "price_book_current": 45.05169867060562,
      "price_free_cash_flow_current": 32.45274643929811,
      "return_on_equity_current": 152.02132328265,
      "long_term_debt_to_assets_current": 0.2021766583969818,
      "long_term_debt_to_equity_current": 0.8695430320898061,
      "float_shares_outstanding_current": 14663394593.4,
      "fiscal_period_end_current": 1767139200,
      "operating_cash_flow_per_share_current": 9.1471130066016,
      "return_on_assets_current": 32.5628782579605,
      "debt_to_equity_current": 1.02629549835582,
      "dividends_yield_current": 0.380882622230361,
      "fiscal_period_current": "2026-Q1",
      "invent_turnover_current": 35.8923822931331,
      "current_ratio_current": 0.973744664864166,
      "free_cash_flow_per_share_current": 8.32687613991183
    },
    "financials_quarterly": {
      "earnings_per_share_fq": 2.84,
      "earnings_per_share_forecast_next_fq": 1.942915,
      "earnings_per_share_diluted_fq": 2.8424,
      "purchase_of_investments_fq": -12693000000,
      "purchase_sale_business_fq": 0,
      "purchase_sale_investments_fq": -2359000000,
      "total_liabilities_shrhldrs_equity_fq": 379297000000,
      "price_cash_flow_fq": 29.89,
      "common_dividends_cash_flow_fq": -3921000000,
      "other_oper_expense_total_fq": 0,
      "sell_gen_admin_exp_other_fq": -7492000000,
      "depreciation_depletion_fq": 3214000000,
      "purchase_of_business_fq": 0,
      "ebitda_per_share_fq": 3.650553707149241,
      "total_receivables_net_fq": 70320000000,
      "ebit_fq": 50852000000,
      "total_cash_dividends_paid_fq": -3921000000,
      "other_investing_cash_flow_sources_fq": 0,
      "change_in_inventories_fq": -211000000,
      "reduction_of_long_term_debt_fq": -2164000000,
      "dilution_adjustment_fq": 0,
      "invent_turnover_fq": 35.8923822931331,
      "fiscal_period_end_fq": 1767139200,
      "fixed_assets_turnover_fq": 9.053851269900653,
      "other_liabilities_total_fq": 52055000000,
      "operating_cash_flow_per_share_fq": 3.64103334180488,
      "shrhldrs_equity_fq": 88190000000,
      "long_term_debt_fq": 76685000000,
      "treasury_stock_common_fq": 0,
      "other_investing_cash_flow_uses_fq": -154000000,
      "return_on_total_capital_fq": 82.4353700154271,
      "capital_expenditures_other_assets_fq": 0,
      "gross_margin_fq": 48.1586855505162,
      "invested_capital_fq": 164875000000,
      "other_receivables_fq": 30399000000,
      "supplying_of_long_term_debt_fq": 0,
      "cash_f_operating_activities_fq": 53925000000,
      "accounts_payable_fq": 70587000000,
      "pretax_equity_in_earnings_fq": 0,
      "ppe_total_gross_fq": 127320000000,
      "fiscal_period_fq": "2026-Q1",
      "current_ratio_fq": 0.973744664864166,
      "preferred_dividends_cash_flow_fq": 0,
      "non_oper_income_fq": 150000000,
      "net_income_bef_disc_oper_fq": 42097000000,
      "capital_expenditures_unchanged_fq": 2373000000,
      "capital_operating_lease_obligations_fq": 0,
      "eps_diluted_growth_percent_fq": 0.18537053254931402,
      "cash_n_equivalents_fq": 36785000000,
      "proceeds_from_stock_options_fq": 0,
      "price_sales_fq": 9.29520962313225,
      "change_in_accounts_payable_fq": 848000000,
      "change_in_accounts_receivable_fq": 2628000000,
      "dividend_payout_ratio_percent_fq": 0.0914719954967633,
      "return_on_invested_capital_fq": 74.6394836321925,
      "operating_expenses_fq": -18379000000,
      "other_income_fq": 150000000,
      "earnings_release_date_fq": 1769722200,
      "goodwill_fq": 0,
      "total_non_current_assets_fq": 221193000000,
      "cash_n_short_term_invest_fq": 66907000000,
      "basic_shares_outstanding_fq": 14748158000,
      "total_assets_to_equity_fq": 4.30090713232793,
      "accum_deprec_total_fq": -77161000000,
      "ncavps_ratio_fq": -10.495965920805313,
      "changes_in_working_capital_fq": 5548000000,
      "other_investments_fq": 77888000000,
      "earnings_release_next_calendar_date_fq": 1774915200,
      "net_margin_fq": 29.2836472912435,
      "earnings_release_calendar_date_fq": 1767139200,
      "working_capital_per_share_fq": -0.289946685313578,
      "common_equity_total_fq": 88190000000,
      "diluted_net_income_fq": 42097000000,
      "short_term_invest_fq": 30122000000,
      "earnings_release_time_fq": 1,
      "sell_gen_admin_exp_total_fq": -18379000000,
      "price_book_fq": 45.5802,
      "book_value_per_share_fq": 5.99822,
      "quick_ratio_fq": 0.937561203939224,
      "long_term_investments_fq": 77888000000,
      "next_earnings_fiscal_period_fq": "2026-Q2",
      "purchase_of_stock_fq": -24701000000,
      "diluted_shares_outstanding_fq": 14810356000,
      "operating_margin_fq": 35.3738278750104,
      "total_debt_fq": 90509000000,
      "long_term_other_assets_total_fq": 93146000000,
      "free_cash_flow_fq": 51552000000,
      "current_port_debt_capital_leases_fq": 11827000000,
      "other_proceeds_from_stock_sales_fq": 0,
      "total_revenue_fq": 143756000000,
      "total_current_liabilities_fq": 162367000000,
      "long_term_debt_excl_capital_lease_fq": 76685000000,
      "sale_of_stock_fq": 0,
      "inventory_work_in_progress_fq": 0,
      "discontinued_operations_fq": 0,
      "provision_f_risks_fq": 0,
      "preferred_stock_carrying_value_fq": 0,
      "investments_in_unconcsolidate_fq": 0,
      "return_on_assets_fq": 32.5628782579605,
      "total_current_assets_fq": 158104000000,
      "capital_lease_obligations_fq": 0,
      "return_on_equity_fq": 152.02132328265,
      "earnings_release_next_trading_date_fq": 1777507200,
      "capex_per_share_fq": 0.160225723135892,
      "issuance_of_debt_net_fq": -8074000000,
      "net_debt_to_ebitda_fq": 0.15436030921766883,
      "book_per_share_fq": 5.99822,
      "free_cash_flow_per_share_fq": 3.4808076186689907,
      "earnings_release_next_date_fq": 1777581000,
      "inventory_progress_payments_fq": 0,
      "enterprise_value_ebitda_fq": 26.6363640135512,
      "net_income_fq": 42097000000,
      "total_non_oper_income_fq": 150000000,
      "tobin_q_ratio_fq": 10.5978138508873,
      "long_term_debt_to_assets_fq": 0.2021766583969818,
      "revenue_fq": 143756000000,
      "debt_to_equity_fq": 1.02629549835582,
      "cost_of_goods_fq": -74525000000,
      "sales_of_investments_fq": 10334000000,
      "inventory_raw_materials_fq": 0,
      "total_equity_fq": 88190000000,
      "cash_f_investing_activities_fq": -4886000000,
      "cost_of_goods_excl_dep_amort_fq": -71311000000,
      "earnings_publication_type_fq": 22,
      "ebitda_margin_fq": 37.6095606444253,
      "accounts_receivables_net_fq": 39921000000,
      "debt_to_asset_fq": 0.23862303155574702,
      "total_non_current_liabilities_fq": 128740000000,
      "pretax_income_fq": 51002000000,
      "minority_interest_exp_fq": 0,
      "cash_flow_deferred_taxes_fq": 0,
      "dep_amort_exp_income_s_fq": -3214000000,
      "long_term_debt_to_equity_fq": 0.8695430320898061,
      "total_debt_per_share_fq": 6.111196786896953,
      "inventory_finished_goods_fq": 5875000000,
      "asset_turnover_fq": 1.20438993505506,
      "total_liabilities_fq": 291107000000,
      "total_extra_items_fq": 0,
      "rates_earnings_fq": {
        "time": 1767139200,
        "to_aud": 1.498689,
        "to_cad": 1.373249,
        "to_chf": 0.79277,
        "to_cny": 6.994964,
        "to_eur": 0.851419,
        "to_gbp": 0.74228,
        "to_inr": 89.88764,
        "to_jpy": 156.715248,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "other_financing_cash_flow_uses_fq": -2960000000,
      "other_investing_cash_flow_items_total_fq": -154000000,
      "common_stock_par_fq": 95221000000,
      "income_tax_fq": -8905000000,
      "other_financing_cash_flow_items_total_fq": -2960000000,
      "sales_of_business_fq": 0,
      "pre_tax_margin_fq": 35.4781713458917,
      "total_debt_to_capital_fq": 0.506488564569472,
      "issuance_of_short_term_debt_fq": -5910000000,
      "revenue_per_share_fq": 9.70645135066301,
      "cash_per_share_fq": 4.517582156701702,
      "earnings_publication_type_next_fq": 12,
      "net_income_starting_line_fq": 42097000000,
      "receivables_turnover_fq": 6.72113619181337,
      "book_tangible_per_share_fq": 5.99821679047723,
      "net_debt_fq": 23602000000,
      "rates_earnings_next_fq": {
        "time": 1774915200,
        "to_aud": 1.44959,
        "to_cad": 1.390975,
        "to_chf": 0.799194,
        "to_cny": 6.899883,
        "to_eur": 0.865524,
        "to_gbp": 0.75643,
        "to_inr": 93.519125,
        "to_jpy": 158.780565,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "minority_interest_fq": 0,
      "earnings_per_share_basic_fq": 2.8544,
      "after_tax_other_income_fq": 0,
      "total_assets_fq": 379297000000,
      "earnings_release_trading_date_fq": 1769644800,
      "cash_f_financing_activities_fq": -39656000000,
      "non_cash_items_fq": 3066000000,
      "ebitda_fq": 54066000000,
      "return_on_tang_assets_fq": 32.56287825796053,
      "total_shares_outstanding_fq": 14702703000,
      "issuance_of_stock_net_fq": -24701000000,
      "earnings_per_share_forecast_fq": 2.673324,
      "other_financing_cash_flow_sources_fq": 0,
      "revenue_forecast_next_fq": 109347054075,
      "capital_expenditures_fq": -2373000000,
      "tangible_assets_fq": 379297000000,
      "price_earnings_fq": 34.5909562488929,
      "deferred_income_current_fq": 9413000000,
      "share_buyback_ratio_fq": 0.4775993924157613,
      "preferred_dividends_fq": 0,
      "rates_fq": {
        "time": 1767139200,
        "to_aud": 1.498689,
        "to_cad": 1.373249,
        "to_chf": 0.79277,
        "to_cny": 6.994964,
        "to_eur": 0.851419,
        "to_gbp": 0.74228,
        "to_inr": 89.88764,
        "to_jpy": 156.715248,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "market_cap_basic_fq": 4019719000200,
      "total_oper_expense_fq": -92904000000,
      "oper_income_fq": 50852000000,
      "non_oper_interest_income_fq": 0,
      "enterprise_value_fq": 4072753330400,
      "working_capital_fq": -4263000000,
      "earnings_release_next_time_fq": 1,
      "return_on_capital_employed_fq": 67.71630865234609,
      "retained_earnings_fq": -2177000000,
      "interest_capitalized_fq": 0,
      "dividend_payout_ratio_fq": 9.14719954967633,
      "total_inventory_fq": 5875000000,
      "other_current_liabilities_fq": 68543000000,
      "dividends_yield_fq": 0.376737381126555,
      "revenue_forecast_fq": 138391007589,
      "ebit_per_share_fq": 3.43354339355516,
      "short_term_debt_excl_current_port_fq": 1997000000,
      "other_current_assets_total_fq": 15002000000,
      "research_and_dev_fq": -10887000000,
      "earnings_fiscal_period_fq": "2026-Q1",
      "funds_f_operations_fq": 48377000000,
      "gross_profit_fq": 69231000000,
      "short_term_debt_fq": 13824000000,
      "dividends_per_share_fq": 0.26,
      "capital_expenditures_fixed_assets_fq": -2373000000,
      "return_on_tang_equity_fq": 152.02132328264966,
      "other_common_equity_fq": -4854000000,
      "paid_in_capital_fq": 95221000000,
      "dps_common_stock_prim_issue_fq": 0.26,
      "equity_in_earnings_fq": 0,
      "unusual_expense_inc_fq": 0,
      "ppe_total_net_fq": 50159000000,
      "cash_flow_deprecation_n_amortization_fq": 3214000000,
      "change_in_other_assets_fq": 2283000000,
      "issuance_of_long_term_debt_fq": -2164000000
    },
    "financials_annual": {
      "dps_common_stock_prim_issue_fy": 1.02,
      "rates_fy": {
        "time": 1759190400,
        "to_aud": 1.512814,
        "to_cad": 1.392758,
        "to_chf": 0.796495,
        "to_cny": 7.120986,
        "to_eur": 0.852195,
        "to_gbp": 0.743937,
        "to_inr": 88.873089,
        "to_jpy": 147.928994,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "net_margin_fy": 26.9150641218182,
      "issuance_of_long_term_debt_fy": -6451000000,
      "earnings_per_share_forecast_fy": 7.381826,
      "cost_of_goods_excl_dep_amort_fy": -209262000000,
      "reduction_of_long_term_debt_fy": -10932000000,
      "price_sales_fy": 9.21061775519571,
      "invent_turnover_fy": 33.9833897262381,
      "purchase_of_investments_fy": -24407000000,
      "paid_in_capital_fy": 93568000000,
      "net_income_fy": 112010000000,
      "oper_income_per_employee_fy": 801506.0240963855,
      "cash_flow_deferred_taxes_fy": 0,
      "diluted_net_income_fy": 112010000000,
      "sale_of_stock_fy": 0,
      "issuance_of_stock_net_fy": -90711000000,
      "ebitda_per_share_fy": 9.64684591764832,
      "depreciation_fy": -8000000000,
      "preferred_stock_carrying_value_fy": 0,
      "dilution_adjustment_fy": 0,
      "other_investing_cash_flow_uses_fy": -1480000000,
      "zmijewski_score_fy": -1.2261588856208425,
      "earnings_per_share_forecast_next_fy": 8.500259,
      "long_term_debt_excl_capital_lease_fy": 89239000000,
      "issuance_of_short_term_debt_fy": -2032000000,
      "return_on_tang_equity_fy": 171.42244974480232,
      "total_shares_outstanding_fy": 14773260000,
      "ppe_total_net_fy": 61039000000,
      "restructuring_charge_fy": 0,
      "earnings_release_date_fy": 1761856320,
      "purchase_sale_business_fy": 0,
      "debt_to_revenue_fy": 0.2700325114559029,
      "total_current_assets_fy": 147957000000,
      "change_in_accounts_payable_fy": 902000000,
      "revenue_fy": 416161000000,
      "sales_of_investments_fy": 53797000000,
      "other_income_fy": -321000000,
      "deferred_tax_assests_fy": 20777000000,
      "number_of_shareholders_fy": 22429,
      "ebitda_per_employee_fy": 871975.9036144578,
      "fiscal_period_end_fy": 1759190400,
      "pretax_equity_in_earnings_fy": 0,
      "issuance_of_debt_net_fy": -8483000000,
      "ebitda_margin_fy": 34.7817311088737,
      "after_tax_other_income_fy": 0,
      "return_on_capital_employed_fy": 69.62359823965588,
      "total_debt_to_capital_fy": 0.603820321315351,
      "capital_expenditures_unchanged_fy": 12715000000,
      "preferred_dividends_cash_flow_fy": 0,
      "short_term_invest_fy": 21158000000,
      "deferred_income_current_fy": 9055000000,
      "earnings_per_share_basic_fy": 7.4931,
      "operating_cash_flow_per_share_fy": 7.42980681315991,
      "other_investments_fy": 77723000000,
      "float_shares_outstanding_fy": 14760953874.42,
      "accounts_payable_fy": 69860000000,
      "total_liabilities_shrhldrs_equity_fy": 359241000000,
      "goodwill_fy": 0,
      "common_stock_par_fy": 93568000000,
      "other_financing_cash_flow_uses_fy": -6071000000,
      "non_oper_interest_income_fy": 0,
      "depreciation_depletion_fy": 8000000000,
      "ebitda_fy": 144748000000,
      "free_cash_flow_fy": 98767000000,
      "income_tax_fy": -20719000000,
      "earnings_publication_type_next_fy": 10,
      "tangible_assets_fy": 359241000000,
      "operating_margin_fy": 31.9707997625919,
      "rates_earnings_fy": {
        "time": 1759190400,
        "to_aud": 1.512814,
        "to_cad": 1.392758,
        "to_chf": 0.796495,
        "to_cny": 7.120986,
        "to_eur": 0.852195,
        "to_gbp": 0.743937,
        "to_inr": 88.873089,
        "to_jpy": 147.928994,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "total_debt_per_share_fy": 7.489454802052983,
      "free_cash_flow_per_share_fy": 6.582405496092323,
      "ppe_gross_machinery_fy": 83420000000,
      "purchase_of_stock_fy": -90711000000,
      "total_assets_fy": 359241000000,
      "total_oper_expense_fy": -283111000000,
      "graham_numbers_fy": 28.95336730416689,
      "funds_f_operations_fy": 136482000000,
      "other_oper_expense_total_fy": 0,
      "return_on_equity_fy": 171.422449744802,
      "proceeds_from_stock_options_fy": 0,
      "dividend_payout_ratio_fy": 13.6637642330877,
      "capital_expenditures_fixed_assets_fy": -12715000000,
      "ncavps_ratio_fy": -9.310808853293045,
      "discontinued_operations_fy": 0,
      "total_non_current_liabilities_fy": 119877000000,
      "current_ratio_fy": 0.893292922218667,
      "gross_margin_fy": 46.9051641071605,
      "operating_lease_liabilities_fy": 10911000000,
      "total_revenue_fy": 416161000000,
      "enterprise_value_ebitda_fy": 26.7933919337055,
      "sloan_ratio_fy": -4.082774516271806,
      "capital_lease_obligations_fy": 692000000,
      "total_non_current_assets_fy": 211284000000,
      "asset_turnover_fy": 1.14926521048133,
      "change_in_inventories_fy": 1400000000,
      "net_debt_fy": 57680000000,
      "price_cash_flow_fy": 34.38,
      "revenue_per_share_fy": 27.7353817941142,
      "inventory_finished_goods_fy": 5718000000,
      "accounts_receivables_net_fy": 39777000000,
      "ppe_total_gross_fy": 137053000000,
      "dividend_payout_ratio_percent_fy": 0.136637642330877,
      "non_cash_items_fy": 12774000000,
      "free_cash_flow_per_employee_fy": 594981.9277108434,
      "income_tax_deferred_fy": 1339000000,
      "income_tax_current_domestic_fy": -13167000000,
      "sales_of_business_fy": 0,
      "invested_capital_fy": 163664000000,
      "cash_flow_deprecation_n_amortization_fy": 11698000000,
      "short_term_debt_fy": 22446000000,
      "net_income_starting_line_fy": 112010000000,
      "total_extra_items_fy": 0,
      "book_value_per_share_fy": 4.99098,
      "long_term_debt_to_assets_fy": 0.250336125330906,
      "income_tax_deferred_foreign_fy": -604000000,
      "quick_ratio_fy": 0.858770399261008,
      "other_proceeds_from_stock_sales_fy": 0,
      "change_in_other_assets_fy": -20273000000,
      "other_short_term_debt_fy": 9558000000,
      "total_cash_dividends_paid_fy": -15421000000,
      "cash_n_short_term_invest_fy": 54697000000,
      "return_on_total_capital_fy": 73.4841309072432,
      "cash_f_investing_activities_fy": 15195000000,
      "total_liabilities_fy": 285508000000,
      "purchase_sale_investments_fy": 29390000000,
      "net_debt_to_ebitda_fy": 0.3984856440158068,
      "dividends_payable_fy": 0,
      "dep_amort_exp_income_s_fy": -11698000000,
      "share_buyback_ratio_fy": 2.2724804068801387,
      "price_earnings_fy": 34.2210314802411,
      "unusual_expense_inc_fy": 0,
      "debt_to_equity_fy": 1.5241072518410999,
      "capital_expenditures_other_assets_fy": 0,
      "common_dividends_cash_flow_fy": -15421000000,
      "net_income_bef_disc_oper_fy": 112010000000,
      "rates_earnings_next_fy": {
        "time": 1790726400,
        "to_aud": 1.393534,
        "to_cad": 1.364629,
        "to_chf": 0.778549,
        "to_cny": 6.818957,
        "to_eur": 0.848522,
        "to_gbp": 0.738989,
        "to_inr": 93.10987,
        "to_jpy": 158.831004,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "number_of_employees_fy": 166000,
      "short_term_debt_excl_current_port_fy": 9558000000,
      "capex_per_share_fy": 0.847401317067582,
      "provision_f_risks_fy": 0,
      "inventory_work_in_progress_fy": 0,
      "purchase_of_business_fy": 0,
      "income_tax_credits_fy": 0,
      "equity_in_earnings_fy": 0,
      "sustainable_growth_rate_fy": 147.999690369089,
      "total_inventory_fy": 5718000000,
      "earnings_release_trading_date_fy": 1761782400,
      "minority_interest_exp_fy": 0,
      "working_capital_fy": -17674000000,
      "accounts_receivables_gross_fy": 39777000000,
      "changes_in_working_capital_fy": -25000000000,
      "cash_per_share_fy": 3.6453251938376363,
      "revenue_per_employee_fy": 2506993.97590361,
      "next_earnings_fiscal_period_fy": "2026",
      "amortization_of_intangibles_fy": -3698000000,
      "book_tangible_per_share_fy": 4.99097694077001,
      "minority_interest_fy": 0,
      "earnings_publication_type_fy": 22,
      "diluted_shares_outstanding_fy": 15004697000,
      "sell_gen_admin_exp_other_fy": -27601000000,
      "net_income_per_employee_fy": 674759.036144578,
      "sell_gen_admin_exp_total_fy": -62151000000,
      "income_tax_current_fy": -22058000000,
      "retained_earnings_fy": -14264000000,
      "total_assets_to_equity_fy": 4.8721874872852,
      "total_current_liabilities_fy": 165631000000,
      "inventory_raw_materials_fy": 0,
      "revenue_forecast_next_fy": 465619085380,
      "total_debt_fy": 112377000000,
      "cost_of_goods_fy": -220960000000,
      "price_book_fy": 51.1843,
      "total_assets_per_employee_fy": 2164102.40963855,
      "market_cap_basic_fy": 3773976999600,
      "cash_dividend_coverage_ratio_fy": 8.85039880682187,
      "other_investing_cash_flow_items_total_fy": -1480000000,
      "cash_f_financing_activities_fy": -120686000000,
      "cash_n_equivalents_fy": 33539000000,
      "inventory_progress_payments_fy": 0,
      "amortization_fy": 3698000000,
      "other_current_assets_total_fy": 14585000000,
      "receivables_turnover_fy": 5.97932471264368,
      "treasury_stock_common_fy": 0,
      "change_in_accounts_receivable_fy": -7029000000,
      "book_per_share_fy": 4.99098,
      "long_term_debt_to_equity_fy": 1.219684537452701,
      "gross_profit_fy": 195201000000,
      "return_on_equity_adjust_to_book_fy": 3.3491193072391447,
      "total_non_oper_income_fy": -321000000,
      "basic_shares_outstanding_fy": 14948500000,
      "operating_expenses_fy": -62151000000,
      "other_financing_cash_flow_sources_fy": 0,
      "working_capital_per_share_fy": -1.19635070390692,
      "long_term_investments_fy": 77723000000,
      "earnings_per_share_diluted_fy": 7.465,
      "eps_diluted_growth_percent_fy": 0.227069498323361,
      "income_tax_current_foreign_fy": -8891000000,
      "debt_to_asset_fy": 0.312817857649879,
      "current_port_debt_capital_leases_fy": 12888000000,
      "return_on_assets_fy": 30.93254683308,
      "other_financing_cash_flow_items_total_fy": -6071000000,
      "amortization_of_deferred_charges_fy": 0,
      "earnings_fiscal_period_fy": "2025",
      "accum_deprec_total_fy": -76014000000,
      "dividends_yield_fy": 0.399279730681907,
      "earnings_per_share_fy": 7.46,
      "income_tax_deferred_domestic_fy": 1943000000,
      "ebit_fy": 133050000000,
      "earnings_release_next_trading_date_fy": 1793232000,
      "earnings_release_next_date_fy": 1793275200,
      "return_on_common_equity_fy": 171.422449744802,
      "cash_f_operating_activities_fy": 111482000000,
      "common_equity_total_fy": 73733000000,
      "research_and_dev_fy": -34550000000,
      "research_and_dev_per_employee_fy": 208132.53012048194,
      "capital_operating_lease_obligations_fy": 11603000000,
      "ebit_per_share_fy": 8.86722337678662,
      "interest_capitalized_fy": 0,
      "revenue_forecast_fy": 415406882375,
      "return_on_tang_assets_fy": 30.93254683307996,
      "ppe_gross_other_fy": 15091000000,
      "fiscal_period_fy": "2025",
      "fixed_assets_turnover_fy": 7.116722102040991,
      "supplying_of_long_term_debt_fy": 4481000000,
      "ppe_gross_buildings_fy": 27337000000,
      "other_investing_cash_flow_sources_fy": 0,
      "enterprise_value_fy": 3890779895620,
      "preferred_dividends_fy": 0,
      "return_on_invested_capital_fy": 70.6326735233099,
      "other_current_liabilities_fy": 51254000000,
      "shrhldrs_equity_fy": 73733000000,
      "pretax_income_fy": 132729000000,
      "oper_income_fy": 133050000000,
      "total_receivables_net_fy": 72957000000,
      "income_tax_payable_fy": 13016000000,
      "pre_tax_margin_fy": 31.8936661532436,
      "other_common_equity_fy": -5571000000,
      "long_term_other_assets_total_fy": 51745000000,
      "total_equity_fy": 73733000000,
      "accrued_expenses_fy": 8919000000,
      "investments_in_unconcsolidate_fy": 0,
      "long_term_debt_fy": 89931000000,
      "capital_expenditures_fy": -12715000000,
      "other_receivables_fy": 33180000000,
      "other_liabilities_total_fy": 29946000000,
      "piotroski_f_score_fy": 8,
      "tobin_q_ratio_fy": 10.505418367057214,
      "total_debt_per_employee_fy": 676969.8795180724,
      "non_oper_income_fy": -321000000
    },
    "history_quarterly": {
      "pretax_equity_in_earnings_fq_h": [
        0,
        0,
        0
      ],
      "cash_f_financing_activities_fq_h": [
        -39656000000,
        -27476000000,
        -24833000000
      ],
      "net_debt_fq_h": [
        23602000000,
        57680000000,
        46326000000
      ],
      "accounts_receivables_net_fq_h": [
        39921000000,
        39777000000,
        27557000000
      ],
      "capital_expenditures_unchanged_fq_h": [
        2373000000,
        3242000000,
        3462000000
      ],
      "change_in_other_assets_fq_h": [
        2283000000,
        1004000000,
        -1327000000
      ],
      "deferred_tax_assests_fq_h": [
        null,
        20777000000,
        null
      ],
      "issuance_of_short_term_debt_fq_h": [
        -5910000000,
        -1967000000,
        3903000000
      ],
      "earnings_fq_h": [
        {
          "Actual": 1.4,
          "Estimate": 0.986396,
          "FiscalPeriod": "2021-Q2",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 1.3,
          "Estimate": 1.010662,
          "FiscalPeriod": "2021-Q3",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 1.24,
          "Estimate": 1.238778,
          "FiscalPeriod": "2021-Q4",
          "IsReported": true,
          "Type": 22
        }
      ],
      "total_liabilities_shrhldrs_equity_fq_h": [
        379297000000,
        359241000000,
        331495000000
      ],
      "cash_n_equivalents_fq_h": [
        36785000000,
        33539000000,
        30465000000
      ],
      "sell_gen_admin_exp_other_fq_h": [
        -7492000000,
        -7048000000,
        -6650000000
      ],
      "earnings_per_share_diluted_fq_h": [
        2.8424,
        1.8479,
        1.5677
      ],
      "interest_expense_on_debt_fq_h": [
        null,
        null,
        null
      ],
      "dilution_adjustment_fq_h": [
        0,
        0,
        0
      ],
      "diluted_net_income_fq_h": [
        42097000000,
        27466000000,
        23434000000
      ],
      "asset_turnover_fq_h": [
        1.20438993505506,
        1.14926521048133,
        1.23245569719517
      ],
      "capital_expenditures_other_assets_fq_h": [
        0,
        0,
        0
      ],
      "earnings_fiscal_period_fq_h": [
        "2026-Q1",
        "2025-Q4",
        "2025-Q3"
      ],
      "total_extra_items_fq_h": [
        0,
        0,
        0
      ],
      "treasury_stock_common_fq_h": [
        0,
        0,
        0
      ],
      "cash_n_short_term_invest_fq_h": [
        66907000000,
        54697000000,
        55372000000
      ],
      "revenue_fq_h": [
        143756000000,
        102466000000,
        94036000000
      ],
      "net_income_bef_disc_oper_fq_h": [
        42097000000,
        27466000000,
        23434000000
      ],
      "discontinued_operations_fq_h": [
        0,
        0,
        0
      ],
      "current_port_debt_capital_leases_fq_h": [
        11827000000,
        12888000000,
        9345000000
      ],
      "non_oper_income_fq_h": [
        150000000,
        377000000,
        -171000000
      ],
      "cash_f_investing_activities_fq_h": [
        -4886000000,
        -2587000000,
        5073000000
      ],
      "ppe_total_gross_fq_h": [
        127320000000,
        137053000000,
        124311000000
      ],
      "pre_tax_margin_fq_h": [
        35.4781713458917,
        32.014521890188,
        29.8087966310775
      ],
      "other_financing_cash_flow_uses_fq_h": [
        -2960000000,
        -265000000,
        -2524000000
      ],
      "ebit_per_share_fq_h": [
        3.43354339355516,
        2.18163704387003,
        1.88665121015744
      ],
      "purchase_sale_business_fq_h": [
        0,
        0,
        0
      ],
      "cash_f_operating_activities_fq_h": [
        53925000000,
        29728000000,
        27867000000
      ],
      "enterprise_value_fq_h": [
        4072753330400,
        3854737555140,
        3052105833320
      ],
      "net_income_starting_line_fq_h": [
        42097000000,
        27466000000,
        23434000000
      ],
      "inventory_progress_payments_fq_h": [
        0,
        0,
        0
      ],
      "fiscal_period_end_fq_h": [
        1767139200,
        1759190400,
        1751241600
      ],
      "sales_of_business_fq_h": [
        0,
        0,
        0
      ],
      "total_debt_fq_h": [
        90509000000,
        112377000000,
        101698000000
      ],
      "long_term_debt_fq_h": [
        76685000000,
        89931000000,
        82430000000
      ],
      "long_term_other_assets_total_fq_h": [
        93146000000,
        51745000000,
        82882000000
      ],
      "deferred_income_current_fq_h": [
        9413000000,
        9055000000,
        8979000000
      ],
      "accounts_payable_fq_h": [
        70587000000,
        69860000000,
        50374000000
      ],
      "earnings_publication_type_fq_h": [
        22,
        22,
        22
      ],
      "accum_deprec_total_fq_h": [
        -77161000000,
        -76014000000,
        -75803000000
      ],
      "quick_ratio_fq_h": [
        0.937561203939224,
        0.858770399261008,
        0.826006235827664
      ],
      "intangibles_net_fq_h": [
        null,
        null,
        null
      ],
      "short_term_debt_fq_h": [
        13824000000,
        22446000000,
        19268000000
      ],
      "total_non_current_assets_fq_h": [
        221193000000,
        211284000000,
        209004000000
      ],
      "ebitda_fq_h": [
        54066000000,
        35554000000,
        31032000000
      ],
      "sell_gen_admin_exp_total_fq_h": [
        -18379000000,
        -15914000000,
        -15516000000
      ],
      "total_inventory_fq_h": [
        5875000000,
        5718000000,
        5925000000
      ],
      "deferred_income_non_current_fq_h": [
        null,
        null,
        null
      ],
      "total_liabilities_fq_h": [
        291107000000,
        285508000000,
        265665000000
      ],
      "investments_in_unconcsolidate_fq_h": [
        0,
        0,
        0
      ],
      "other_investing_cash_flow_sources_fq_h": [
        0,
        0,
        0
      ],
      "book_tangible_per_share_fq_h": [
        5.99821679047723,
        4.99097694077001,
        4.43099090095379
      ],
      "other_investing_cash_flow_items_total_fq_h": [
        -154000000,
        -505000000,
        -340000000
      ],
      "other_proceeds_from_stock_sales_fq_h": [
        0,
        0,
        0
      ],
      "unusual_expense_inc_fq_h": [
        0,
        0,
        0
      ],
      "reduction_of_long_term_debt_fq_h": [
        -2164000000,
        -1250000000,
        -5673000000
      ],
      "ppe_total_net_fq_h": [
        50159000000,
        61039000000,
        48508000000
      ],
      "sales_of_investments_fq_h": [
        10334000000,
        7976000000,
        14024000000
      ],
      "goodwill_fq_h": [
        0,
        0,
        0
      ],
      "change_in_taxes_payable_fq_h": [
        null,
        null,
        null
      ],
      "working_capital_per_share_fq_h": [
        -0.289946685313578,
        -1.19635070390692,
        -1.25391051942683
      ],
      "dep_amort_exp_income_s_fq_h": [
        -3214000000,
        -3127000000,
        -2830000000
      ],
      "inventory_work_in_progress_fq_h": [
        0,
        0,
        0
      ],
      "income_tax_fq_h": [
        -8905000000,
        -5338000000,
        -4597000000
      ],
      "pretax_income_fq_h": [
        51002000000,
        32804000000,
        28031000000
      ],
      "price_cash_flow_fq_h": [
        29.89,
        34.06,
        27.69
      ],
      "cash_flow_deprecation_n_amortization_fq_h": [
        3214000000,
        3127000000,
        2830000000
      ],
      "total_oper_expense_fq_h": [
        -92904000000,
        -70039000000,
        -65834000000
      ],
      "capital_operating_lease_obligations_fq_h": [
        0,
        11603000000,
        0
      ],
      "after_tax_other_income_fq_h": [
        0,
        0,
        0
      ],
      "deferred_charges_fq_h": [
        null,
        null,
        null
      ],
      "income_tax_payable_fq_h": [
        null,
        13016000000,
        null
      ],
      "price_book_fq_h": [
        45.5802,
        51.1843,
        45.3804
      ],
      "preferred_stock_carrying_value_fq_h": [
        0,
        0,
        0
      ],
      "provision_f_risks_fq_h": [
        0,
        0,
        0
      ],
      "cash_per_share_fq_h": [
        4.517582156701702,
        3.6799272639639535,
        3.704263910674337
      ],
      "earnings_per_share_forecast_fq_h": [
        2.673324,
        1.777147,
        1.438019
      ],
      "common_equity_total_fq_h": [
        88190000000,
        73733000000,
        65830000000
      ],
      "current_ratio_fq_h": [
        0.973744664864166,
        0.893292922218667,
        0.867991780045351
      ],
      "change_in_inventories_fq_h": [
        -211000000,
        177000000,
        365000000
      ],
      "deferred_tax_liabilities_fq_h": [
        null,
        null,
        null
      ],
      "preferred_dividends_cash_flow_fq_h": [
        0,
        0,
        0
      ],
      "ncavps_ratio_fq_h": [
        -10.495965920805313,
        -8.766479858880055,
        -9.212167523887222
      ],
      "other_current_liabilities_fq_h": [
        68543000000,
        51254000000,
        62499000000
      ],
      "long_term_debt_to_equity_fq_h": [
        0.8695430320898061,
        1.219684537452701,
        1.2521646665653958
      ],
      "purchase_of_stock_fq_h": [
        -24701000000,
        -20132000000,
        -21075000000
      ],
      "fiscal_period_fq_h": [
        "2026-Q1",
        "2025-Q4",
        "2025-Q3"
      ],
      "short_term_invest_fq_h": [
        30122000000,
        21158000000,
        24907000000
      ],
      "long_term_debt_to_assets_fq_h": [
        0.2021766583969818,
        0.250336125330906,
        0.24866136744143955
      ],
      "oper_income_fq_h": [
        50852000000,
        32427000000,
        28202000000
      ],
      "other_oper_expense_total_fq_h": [
        0,
        0,
        0
      ],
      "ebitda_per_share_fq_h": [
        3.650553707149241,
        2.3920166360673236,
        2.0759719294236443
      ],
      "research_and_dev_fq_h": [
        -10887000000,
        -8866000000,
        -8866000000
      ],
      "cost_of_goods_fq_h": [
        -74525000000,
        -54125000000,
        -50318000000
      ],
      "total_shares_outstanding_fq_h": [
        14702703000,
        14773260000,
        14856722000
      ],
      "retained_earnings_fq_h": [
        -2177000000,
        -14264000000,
        -17607000000
      ],
      "shrhldrs_equity_fq_h": [
        88190000000,
        73733000000,
        65830000000
      ],
      "capital_expenditures_fq_h": [
        -2373000000,
        -3242000000,
        -3462000000
      ],
      "inventory_raw_materials_fq_h": [
        0,
        0,
        0
      ],
      "common_stock_par_fq_h": [
        95221000000,
        93568000000,
        89806000000
      ],
      "interest_capitalized_fq_h": [
        0,
        0,
        0
      ],
      "revenue_forecast_fq_h": [
        138391007589,
        102227074560,
        89562736363
      ],
      "operating_margin_fq_h": [
        35.3738278750104,
        31.646594968087,
        29.9906418818325
      ],
      "gross_profit_fq_h": [
        69231000000,
        48341000000,
        43718000000
      ],
      "operating_cash_flow_per_share_fq_h": [
        3.64103334180488,
        2.00005261171765,
        1.86424045363653
      ],
      "change_in_accrued_expenses_fq_h": [
        null,
        null,
        null
      ],
      "other_financing_cash_flow_sources_fq_h": [
        0,
        0,
        0
      ],
      "ebit_fq_h": [
        50852000000,
        32427000000,
        28202000000
      ],
      "common_dividends_cash_flow_fq_h": [
        -3921000000,
        -3862000000,
        -3945000000
      ],
      "other_investments_fq_h": [
        77888000000,
        77723000000,
        77614000000
      ],
      "other_income_fq_h": [
        150000000,
        377000000,
        -171000000
      ],
      "proceeds_from_stock_options_fq_h": [
        0,
        0,
        0
      ],
      "minority_interest_exp_fq_h": [
        0,
        0,
        0
      ],
      "ebitda_margin_fq_h": [
        37.6095606444253,
        34.6983389612164,
        33.0001276107023
      ],
      "revenue_per_share_fq_h": [
        9.70645135066301,
        6.89374969430372,
        6.2907997020908
      ],
      "return_on_assets_fq_h": [
        32.5628782579605,
        30.93254683308,
        29.943885375965
      ],
      "minority_interest_fq_h": [
        0,
        0,
        0
      ],
      "total_revenue_fq_h": [
        143756000000,
        102466000000,
        94036000000
      ],
      "depreciation_depletion_fq_h": [
        3214000000,
        null,
        null
      ],
      "revenues_fq_h": [
        {
          "Actual": 89584000000,
          "Estimate": 77088700724,
          "FiscalPeriod": "2021-Q2",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 81434000000,
          "Estimate": 73334747261,
          "FiscalPeriod": "2021-Q3",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 83360000000,
          "Estimate": 85054907222,
          "FiscalPeriod": "2021-Q4",
          "IsReported": true,
          "Type": 22
        }
      ],
      "earnings_per_share_fq_h": [
        2.84,
        1.85,
        1.57
      ],
      "earnings_per_share_basic_fq_h": [
        2.8544,
        1.8539,
        1.5724
      ],
      "price_earnings_fq_h": [
        34.5909562488929,
        34.2471813709061,
        30.5676324830501
      ],
      "short_term_debt_excl_current_port_fq_h": [
        1997000000,
        9558000000,
        9923000000
      ],
      "issuance_of_long_term_debt_fq_h": [
        -2164000000,
        -1250000000,
        -1192000000
      ],
      "other_common_equity_fq_h": [
        -4854000000,
        -5571000000,
        -6369000000
      ],
      "issuance_of_debt_net_fq_h": [
        -8074000000,
        -3217000000,
        2711000000
      ],
      "total_equity_fq_h": [
        88190000000,
        73733000000,
        65830000000
      ],
      "other_receivables_fq_h": [
        30399000000,
        33180000000,
        19278000000
      ],
      "return_on_invested_capital_fq_h": [
        74.6394836321925,
        70.6326735233099,
        65.9308549494627
      ],
      "prepaid_expenses_fq_h": [
        null,
        null,
        null
      ],
      "total_non_oper_income_fq_h": [
        150000000,
        377000000,
        -171000000
      ],
      "other_financing_cash_flow_items_total_fq_h": [
        -2960000000,
        -265000000,
        -2524000000
      ],
      "market_cap_basic_fq_h": [
        4019719000200,
        3773976999600,
        2987389659760
      ],
      "invent_turnover_fq_h": [
        35.8923822931331,
        33.9833897262381,
        36.0440033085194
      ],
      "sale_of_stock_fq_h": [
        0,
        0,
        0
      ],
      "capital_expenditures_fixed_assets_fq_h": [
        -2373000000,
        -3242000000,
        -3462000000
      ],
      "long_term_debt_excl_capital_lease_fq_h": [
        76685000000,
        89239000000,
        82430000000
      ],
      "total_non_current_liabilities_fq_h": [
        128740000000,
        119877000000,
        124545000000
      ],
      "total_receivables_net_fq_h": [
        70320000000,
        72957000000,
        46835000000
      ],
      "dividend_payout_ratio_fq_h": [
        9.14719954967633,
        14.0700254342767,
        16.5848057664094
      ],
      "accrued_payroll_fq_h": [
        null,
        null,
        null
      ],
      "long_term_note_receivable_fq_h": [
        null,
        null,
        null
      ],
      "additional_paid_in_capital_fq_h": [
        null,
        null,
        null
      ],
      "gross_margin_fq_h": [
        48.1586855505162,
        47.1776003747585,
        46.4907056871836
      ],
      "diluted_shares_outstanding_fq_h": [
        14810356000,
        14863609000,
        14948179000
      ],
      "earnings_release_date_fq_h": [
        1769722200,
        1761856320,
        1753993980
      ],
      "free_cash_flow_per_share_fq_h": [
        3.4808076186689907,
        1.7819360022185728,
        1.6326403369935563
      ],
      "cost_of_goods_excl_dep_amort_fq_h": [
        -71311000000,
        -50998000000,
        -47488000000
      ],
      "capital_lease_obligations_fq_h": [
        0,
        692000000,
        0
      ],
      "return_on_equity_fq_h": [
        152.02132328265,
        171.422449744802,
        149.813638352774
      ],
      "operating_expenses_fq_h": [
        -18379000000,
        -15914000000,
        -15516000000
      ],
      "non_oper_interest_exp_fq_h": [
        null,
        null,
        null
      ],
      "non_cash_items_fq_h": [
        3066000000,
        4842000000,
        3637000000
      ],
      "net_margin_fq_h": [
        29.2836472912435,
        26.8049889719517,
        24.9202433110724
      ],
      "purchase_sale_investments_fq_h": [
        -2359000000,
        1160000000,
        8875000000
      ],
      "other_liabilities_total_fq_h": [
        52055000000,
        29946000000,
        42115000000
      ],
      "total_current_liabilities_fq_h": [
        162367000000,
        165631000000,
        141120000000
      ],
      "non_oper_interest_income_fq_h": [
        0,
        0,
        0
      ],
      "other_investing_cash_flow_uses_fq_h": [
        -154000000,
        -505000000,
        -340000000
      ],
      "other_intangibles_net_fq_h": [
        null,
        null,
        null
      ],
      "total_debt_per_share_fq_h": [
        6.111196786896953,
        7.560546028895136,
        6.803370497503408
      ],
      "inventory_finished_goods_fq_h": [
        5875000000,
        5718000000,
        5925000000
      ],
      "operating_lease_liabilities_fq_h": [
        null,
        10911000000,
        null
      ],
      "cash_flow_deferred_taxes_fq_h": [
        0,
        0,
        0
      ],
      "net_income_fq_h": [
        42097000000,
        27466000000,
        23434000000
      ],
      "enterprise_value_ebitda_fq_h": [
        26.6363640135512,
        26.5443913224362,
        21.5398164614386
      ],
      "book_value_per_share_fq_h": [
        5.99822,
        4.99098,
        4.43099
      ],
      "long_term_investments_fq_h": [
        77888000000,
        77723000000,
        77614000000
      ],
      "purchase_of_investments_fq_h": [
        -12693000000,
        -6816000000,
        -5149000000
      ],
      "total_current_assets_fq_h": [
        158104000000,
        147957000000,
        122491000000
      ],
      "change_in_accounts_payable_fq_h": [
        848000000,
        19381000000,
        -3875000000
      ],
      "issuance_of_other_debt_fq_h": [
        null,
        null,
        null
      ],
      "changes_in_working_capital_fq_h": [
        5548000000,
        -5707000000,
        -2034000000
      ],
      "total_assets_fq_h": [
        379297000000,
        359241000000,
        331495000000
      ],
      "capex_per_share_fq_h": [
        0.160225723135892,
        0.218116609499079,
        0.23160011664297
      ],
      "basic_shares_outstanding_fq_h": [
        14748158000,
        14815307000,
        14902886000
      ],
      "debt_to_asset_fq_h": [
        0.23862303155574702,
        0.312817857649879,
        0.306785924372917
      ],
      "supplying_of_long_term_debt_fq_h": [
        0,
        0,
        4481000000
      ],
      "preferred_dividends_fq_h": [
        0,
        0,
        0
      ],
      "dps_common_stock_prim_issue_fq_h": [
        0.26,
        0.26,
        0.26
      ],
      "price_sales_fq_h": [
        9.29520962313225,
        9.12401103212459,
        7.35583929842765
      ],
      "equity_in_earnings_fq_h": [
        0,
        0,
        0
      ],
      "paid_in_capital_fq_h": [
        95221000000,
        93568000000,
        89806000000
      ],
      "issuance_of_stock_net_fq_h": [
        -24701000000,
        -20132000000,
        -21075000000
      ],
      "debt_to_equity_fq_h": [
        1.02629549835582,
        1.5241072518410999,
        1.54485796749202
      ],
      "change_in_accounts_receivable_fq_h": [
        2628000000,
        -26269000000,
        2803000000
      ],
      "amortization_fq_h": [
        null,
        null,
        null
      ],
      "funds_f_operations_fq_h": [
        48377000000,
        35435000000,
        29901000000
      ],
      "other_current_assets_total_fq_h": [
        15002000000,
        14585000000,
        14359000000
      ],
      "total_cash_dividends_paid_fq_h": [
        -3921000000,
        -3862000000,
        -3945000000
      ],
      "free_cash_flow_fq_h": [
        51552000000,
        26486000000,
        24405000000
      ],
      "purchase_of_business_fq_h": [
        0,
        0,
        0
      ]
    },
    "history_annual": {
      "issuance_of_long_term_debt_fy_h": [
        -6451000000,
        -9958000000,
        -5923000000
      ],
      "ppe_gross_other_fy_h": [
        15091000000,
        14233000000,
        12839000000
      ],
      "inventory_raw_materials_fy_h": [
        0,
        0,
        0
      ],
      "accum_deprec_construction_fy_h": [
        null,
        null,
        null
      ],
      "additional_paid_in_capital_fy_h": [
        null,
        null,
        null
      ],
      "non_oper_interest_exp_fy_h": [
        null,
        null,
        -3933000000
      ],
      "inventory_finished_goods_fy_h": [
        5718000000,
        7286000000,
        6331000000
      ],
      "revenue_per_share_fy_h": [
        27.7353817941142,
        25.3785429022861,
        24.2392955416986
      ],
      "capex_per_share_fy_h": [
        0.847401317067582,
        0.613119272693996,
        0.69305722854136
      ],
      "price_sales_fy_h": [
        9.21061775519571,
        8.97569261076374,
        7.06332408487157
      ],
      "impairments_fy_h": [
        null,
        null,
        null
      ],
      "cash_flow_deprecation_n_amortization_fy_h": [
        11698000000,
        11445000000,
        11519000000
      ],
      "working_capital_per_share_fy_h": [
        -1.19635070390692,
        -1.54827884710414,
        -0.112025284016571
      ],
      "capital_expenditures_fy_h": [
        -12715000000,
        -9447000000,
        -10959000000
      ],
      "long_term_debt_to_equity_fy_h": [
        1.219684537452701,
        1.6953116769095697,
        1.7144788079683326
      ],
      "diluted_shares_outstanding_fy_h": [
        15004697000,
        15408095000,
        15812547000
      ],
      "debt_to_equity_fy_h": [
        1.5241072518410999,
        2.09058823529412,
        1.99417500724101
      ],
      "common_dividends_cash_flow_fy_h": [
        -15421000000,
        -15234000000,
        -15025000000
      ],
      "inventory_progress_payments_fy_h": [
        0,
        0,
        0
      ],
      "total_extra_items_fy_h": [
        0,
        0,
        0
      ],
      "earnings_per_share_forecast_fy_h": [
        7.381826,
        6.708209,
        6.057597
      ],
      "ppe_gross_leased_prop_fy_h": [
        null,
        null,
        null
      ],
      "income_tax_credits_fy_h": [
        0,
        0,
        0
      ],
      "total_current_assets_fy_h": [
        147957000000,
        152987000000,
        143566000000
      ],
      "restructuring_charge_fy_h": [
        0,
        0,
        0
      ],
      "ebitda_fy_h": [
        144748000000,
        134661000000,
        125820000000
      ],
      "research_and_dev_fy_h": [
        -34550000000,
        -31370000000,
        -29915000000
      ],
      "other_investing_cash_flow_items_total_fy_h": [
        -1480000000,
        -1308000000,
        -1337000000
      ],
      "other_common_equity_fy_h": [
        -5571000000,
        -7172000000,
        -11452000000
      ],
      "accounts_receivables_gross_fy_h": [
        39777000000,
        33410000000,
        29508000000
      ],
      "issuance_of_debt_net_fy_h": [
        -8483000000,
        -5998000000,
        -9901000000
      ],
      "earnings_per_share_basic_fy_h": [
        7.4931,
        6.109,
        6.1607
      ],
      "cash_f_operating_activities_fy_h": [
        111482000000,
        118254000000,
        110543000000
      ],
      "total_non_current_assets_fy_h": [
        211284000000,
        211993000000,
        209017000000
      ],
      "ppe_gross_comp_soft_fy_h": [
        null,
        null,
        null
      ],
      "pretax_equity_in_earnings_fy_h": [
        0,
        0,
        0
      ],
      "cash_f_financing_activities_fy_h": [
        -120686000000,
        -121983000000,
        -108488000000
      ],
      "free_cash_flow_per_share_fy_h": [
        6.582405496092323,
        7.061677644121483,
        6.297783652437523
      ],
      "purchase_sale_business_fy_h": [
        0,
        0,
        0
      ],
      "total_current_liabilities_fy_h": [
        165631000000,
        176392000000,
        145308000000
      ],
      "oper_income_fy_h": [
        133050000000,
        123216000000,
        114301000000
      ],
      "operating_lease_liabilities_fy_h": [
        10911000000,
        10046000000,
        10408000000
      ],
      "short_term_debt_excl_current_port_fy_h": [
        9558000000,
        11455000000,
        7395000000
      ],
      "invent_turnover_fy_h": [
        33.9833897262381,
        30.8954982742161,
        37.9776536312849
      ],
      "total_oper_expense_fy_h": [
        -283111000000,
        -267819000000,
        -268984000000
      ],
      "free_cash_flow_fy_h": [
        98767000000,
        108807000000,
        99584000000
      ],
      "common_equity_total_fy_h": [
        73733000000,
        56950000000,
        62146000000
      ],
      "income_tax_deferred_foreign_fy_h": [
        -604000000,
        -347000000,
        -669000000
      ],
      "purchase_of_business_fy_h": [
        0,
        0,
        0
      ],
      "doubtful_accounts_fy_h": [
        null,
        null,
        null
      ],
      "earnings_fiscal_period_fy_h": [
        "2025",
        "2024",
        "2023"
      ],
      "non_oper_income_fy_h": [
        -321000000,
        269000000,
        3368000000
      ],
      "diluted_net_income_fy_h": [
        112010000000,
        93736000000,
        96995000000
      ],
      "accrued_expenses_fy_h": [
        8919000000,
        null,
        null
      ],
      "accum_deprec_buildings_fy_h": [
        null,
        null,
        null
      ],
      "number_of_employees_fy_h": [
        166000,
        164000,
        161000
      ],
      "basic_shares_outstanding_fy_h": [
        14948500000,
        15343783000,
        15744231000
      ],
      "other_financing_cash_flow_sources_fy_h": [
        0,
        0,
        0
      ],
      "accounts_receivables_net_fy_h": [
        39777000000,
        33410000000,
        29508000000
      ],
      "long_term_other_assets_total_fy_h": [
        51745000000,
        45101000000,
        36245000000
      ],
      "other_proceeds_from_stock_sales_fy_h": [
        0,
        0,
        0
      ],
      "issuance_of_other_debt_fy_h": [
        null,
        null,
        null
      ],
      "total_revenue_fy_h": [
        416161000000,
        391035000000,
        383285000000
      ],
      "capital_lease_obligations_fy_h": [
        692000000,
        752000000,
        859000000
      ],
      "capital_expenditures_unchanged_fy_h": [
        12715000000,
        9447000000,
        10959000000
      ],
      "accum_deprec_comp_soft_fy_h": [
        null,
        null,
        null
      ],
      "capital_operating_lease_obligations_fy_h": [
        11603000000,
        10798000000,
        11267000000
      ],
      "accum_deprec_other_intang_fy_h": [
        null,
        null,
        null
      ],
      "deferred_tax_assests_fy_h": [
        20777000000,
        19499000000,
        17852000000
      ],
      "long_term_investments_fy_h": [
        77723000000,
        91479000000,
        100544000000
      ],
      "issuance_of_short_term_debt_fy_h": [
        -2032000000,
        3960000000,
        -3978000000
      ],
      "enterprise_value_ebitda_fy_h": [
        26.7933919337055,
        26.3785651380132,
        21.9187980596884
      ],
      "book_tangible_per_share_fy_h": [
        4.99097694077001,
        3.76733519942665,
        3.99651165355557
      ],
      "ppe_gross_construction_fy_h": [
        null,
        null,
        null
      ],
      "fiscal_period_fy_h": [
        "2025",
        "2024",
        "2023"
      ],
      "change_in_accounts_receivable_fy_h": [
        -7029000000,
        -5144000000,
        -417000000
      ],
      "net_margin_fy_h": [
        26.9150641218182,
        23.9712557699439,
        25.3062342643203
      ],
      "issuance_of_stock_net_fy_h": [
        -90711000000,
        -94949000000,
        -77550000000
      ],
      "earnings_per_share_diluted_fy_h": [
        7.465,
        6.0836,
        6.134
      ],
      "total_cash_dividends_paid_fy_h": [
        -15421000000,
        -15234000000,
        -15025000000
      ],
      "amortization_of_deferred_charges_fy_h": [
        0,
        0,
        null
      ],
      "current_ratio_fy_h": [
        0.893292922218667,
        0.867312576534083,
        0.988011671759297
      ],
      "accum_deprec_other_fy_h": [
        null,
        null,
        null
      ],
      "total_inventory_fy_h": [
        5718000000,
        7286000000,
        6331000000
      ],
      "income_tax_current_fy_h": [
        -22058000000,
        -32780000000,
        -19765000000
      ],
      "dividend_payout_ratio_fy_h": [
        13.6637642330877,
        16.1088828982839,
        15.3244212585589
      ],
      "non_cash_items_fy_h": [
        12774000000,
        9422000000,
        8606000000
      ],
      "total_assets_fy_h": [
        359241000000,
        364980000000,
        352583000000
      ],
      "changes_in_working_capital_fy_h": [
        -25000000000,
        3651000000,
        -6577000000
      ],
      "operating_margin_fy_h": [
        31.9707997625919,
        31.5102228700756,
        29.8214122650247
      ],
      "ebit_fy_h": [
        133050000000,
        123216000000,
        114301000000
      ],
      "amortization_of_intangibles_fy_h": [
        -3698000000,
        -3245000000,
        -3019000000
      ],
      "long_term_debt_to_assets_fy_h": [
        0.250336125330906,
        0.2645295632637405,
        0.302192675199882
      ],
      "operating_expenses_fy_h": [
        -62151000000,
        -57467000000,
        -54847000000
      ],
      "non_oper_interest_income_fy_h": [
        0,
        0,
        3750000000
      ],
      "operating_cash_flow_per_share_fy_h": [
        7.42980681315991,
        7.67479691681548,
        6.99084088097888
      ],
      "change_in_accrued_expenses_fy_h": [
        null,
        null,
        null
      ],
      "goodwill_gross_fy_h": [
        null,
        null,
        null
      ],
      "short_term_invest_fy_h": [
        21158000000,
        37194000000,
        32715000000
      ],
      "unrealized_gain_loss_fy_h": [
        null,
        null,
        null
      ],
      "reduction_of_long_term_debt_fy_h": [
        -10932000000,
        -9958000000,
        -11151000000
      ],
      "dep_amort_exp_income_s_fy_h": [
        -11698000000,
        -11445000000,
        -11519000000
      ],
      "inventory_work_in_progress_fy_h": [
        0,
        0,
        0
      ],
      "ppe_gross_machinery_fy_h": [
        83420000000,
        80205000000,
        78314000000
      ],
      "amortization_fy_h": [
        3698000000,
        3245000000,
        3019000000
      ],
      "dividends_yield_fy_h": [
        0.399279730681907,
        0.430220817419553,
        0.549033350855674
      ],
      "price_cash_flow_fy_h": [
        34.38,
        29.68,
        24.49
      ],
      "funds_f_operations_fy_h": [
        136482000000,
        114603000000,
        117120000000
      ],
      "minority_interest_exp_fy_h": [
        0,
        0,
        0
      ],
      "intangibles_net_fy_h": [
        null,
        null,
        null
      ],
      "other_intangibles_net_fy_h": [
        null,
        null,
        null
      ],
      "other_financing_cash_flow_uses_fy_h": [
        -6071000000,
        -5802000000,
        -6012000000
      ],
      "investments_in_unconcsolidate_fy_h": [
        0,
        0,
        0
      ],
      "shrhldrs_equity_fy_h": [
        73733000000,
        56950000000,
        62146000000
      ],
      "other_financing_cash_flow_items_total_fy_h": [
        -6071000000,
        -5802000000,
        -6012000000
      ],
      "debt_to_asset_fy_h": [
        0.312817857649879,
        0.32620691544742203,
        0.351491705499131
      ],
      "cash_f_investing_activities_fy_h": [
        15195000000,
        2935000000,
        3705000000
      ],
      "goodwill_amortization_fy_h": [
        null,
        null,
        null
      ],
      "other_oper_expense_total_fy_h": [
        0,
        0,
        0
      ],
      "ebit_per_share_fy_h": [
        8.86722337678662,
        7.9968354296881,
        7.2285002536277
      ],
      "ebitda_per_share_fy_h": [
        9.64684591764832,
        8.739626800068406,
        7.956972396667026
      ],
      "after_tax_other_income_fy_h": [
        0,
        0,
        0
      ],
      "ppe_gross_leases_fy_h": [
        null,
        null,
        null
      ],
      "net_income_starting_line_fy_h": [
        112010000000,
        93736000000,
        96995000000
      ],
      "cash_per_share_fy_h": [
        3.6453251938376363,
        4.229659798956328,
        3.892794753432195
      ],
      "cash_flow_deferred_taxes_fy_h": [
        0,
        0,
        0
      ],
      "income_tax_deferred_fy_h": [
        1339000000,
        3031000000,
        3024000000
      ],
      "other_investing_cash_flow_uses_fy_h": [
        -1480000000,
        -1308000000,
        -1337000000
      ],
      "enterprise_value_fy_h": [
        3890779895620,
        3563697960050,
        2769641171870
      ],
      "dps_common_stock_prim_issue_fy_h": [
        1.02,
        0.98,
        0.94
      ],
      "other_current_liabilities_fy_h": [
        51254000000,
        50071000000,
        57254000000
      ],
      "ppe_gross_buildings_fy_h": [
        27337000000,
        24690000000,
        23446000000
      ],
      "deferred_charges_fy_h": [
        null,
        null,
        null
      ],
      "total_non_current_liabilities_fy_h": [
        119877000000,
        131638000000,
        145129000000
      ],
      "ppe_total_net_fy_h": [
        61039000000,
        55914000000,
        54376000000
      ],
      "purchase_of_investments_fy_h": [
        -24407000000,
        -48656000000,
        -29513000000
      ],
      "return_on_equity_fy_h": [
        171.422449744802,
        157.412507556929,
        171.949511602758
      ],
      "price_earnings_fy_h": [
        34.2210314802411,
        37.4432901571438,
        27.9116400391262
      ],
      "total_non_oper_income_fy_h": [
        -321000000,
        269000000,
        -565000000
      ],
      "accum_deprec_land_fy_h": [
        null,
        null,
        null
      ],
      "preferred_stock_carrying_value_fy_h": [
        0,
        0,
        0
      ],
      "net_income_fy_h": [
        112010000000,
        93736000000,
        96995000000
      ],
      "legal_claim_expense_fy_h": [
        null,
        null,
        null
      ],
      "goodwill_fy_h": [
        0,
        null,
        null
      ],
      "net_debt_fy_h": [
        57680000000,
        53888000000,
        62375000000
      ],
      "notes_payable_short_term_debt_fy_h": [
        null,
        null,
        null
      ],
      "depreciation_depletion_fy_h": [
        8000000000,
        8200000000,
        8500000000
      ],
      "dividends_payable_fy_h": [
        0,
        0,
        0
      ],
      "deferred_tax_liabilities_fy_h": [
        null,
        null,
        null
      ],
      "pretax_income_fy_h": [
        132729000000,
        123485000000,
        113736000000
      ],
      "treasury_stock_common_fy_h": [
        0,
        0,
        0
      ],
      "long_term_debt_fy_h": [
        89931000000,
        96548000000,
        106548000000
      ],
      "equity_in_earnings_fy_h": [
        0,
        0,
        0
      ],
      "other_short_term_debt_fy_h": [
        9558000000,
        11455000000,
        7395000000
      ],
      "preferred_dividends_fy_h": [
        0,
        0,
        0
      ],
      "quick_ratio_fy_h": [
        0.858770399261008,
        0.826006848383147,
        0.944442150466595
      ],
      "ppe_gross_land_fy_h": [
        null,
        null,
        null
      ],
      "total_shares_outstanding_fy_h": [
        14773260000,
        15116786000,
        15550061000
      ],
      "other_current_assets_total_fy_h": [
        14585000000,
        14287000000,
        14695000000
      ],
      "net_income_bef_disc_oper_fy_h": [
        112010000000,
        93736000000,
        96995000000
      ],
      "return_on_assets_fy_h": [
        30.93254683308,
        26.1262077336763,
        27.503126160791
      ],
      "market_cap_basic_fy_h": [
        3773976999600,
        3443452682940,
        2662325943810
      ],
      "asset_turnover_fy_h": [
        1.14926521048133,
        1.08989733305647,
        1.08681228006998
      ],
      "ncavps_ratio_fy_h": [
        -9.310808853293045,
        -10.256346818695455,
        -9.445043334556694
      ],
      "price_book_fy_h": [
        51.1843,
        60.4644,
        42.8399
      ],
      "revenues_fy_h": [
        {
          "Actual": 229234000000,
          "Estimate": 227461939394,
          "FiscalPeriod": "2017",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 265595000000,
          "Estimate": 264521756757,
          "FiscalPeriod": "2018",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 260174000000,
          "Estimate": 259058735507,
          "FiscalPeriod": "2019",
          "IsReported": true,
          "Type": 22
        }
      ],
      "interest_capitalized_fy_h": [
        0,
        0,
        0
      ],
      "prepaid_expenses_fy_h": [
        null,
        null,
        null
      ],
      "earnings_fy_h": [
        {
          "Actual": 2.3025,
          "Estimate": 2.248051,
          "FiscalPeriod": "2017",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 2.9775,
          "Estimate": 2.936966,
          "FiscalPeriod": "2018",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 2.9725,
          "Estimate": 2.919387,
          "FiscalPeriod": "2019",
          "IsReported": true,
          "Type": 22
        }
      ],
      "total_debt_fy_h": [
        112377000000,
        119059000000,
        123930000000
      ],
      "other_investments_fy_h": [
        77723000000,
        91479000000,
        100544000000
      ],
      "income_tax_current_domestic_fy_h": [
        -13167000000,
        -7297000000,
        -11015000000
      ],
      "sales_of_business_fy_h": [
        0,
        0,
        0
      ],
      "ppe_gross_trans_equip_fy_h": [
        null,
        null,
        null
      ],
      "accum_deprec_total_fy_h": [
        -76014000000,
        -73448000000,
        -70884000000
      ],
      "change_in_taxes_payable_fy_h": [
        null,
        null,
        null
      ],
      "discontinued_operations_fy_h": [
        0,
        0,
        0
      ],
      "total_receivables_net_fy_h": [
        72957000000,
        66243000000,
        60985000000
      ],
      "total_liabilities_fy_h": [
        285508000000,
        308030000000,
        290437000000
      ],
      "total_liabilities_shrhldrs_equity_fy_h": [
        359241000000,
        364980000000,
        352583000000
      ],
      "retained_earnings_fy_h": [
        -14264000000,
        -19154000000,
        -214000000
      ],
      "paid_in_capital_fy_h": [
        93568000000,
        83276000000,
        73812000000
      ],
      "sale_of_stock_fy_h": [
        0,
        0,
        0
      ],
      "capital_expenditures_other_assets_fy_h": [
        0,
        0,
        0
      ],
      "short_term_debt_fy_h": [
        22446000000,
        22511000000,
        17382000000
      ],
      "minority_interest_fy_h": [
        0,
        0,
        0
      ],
      "other_investing_cash_flow_sources_fy_h": [
        0,
        0,
        0
      ],
      "other_income_fy_h": [
        -321000000,
        269000000,
        -382000000
      ],
      "ppe_total_gross_fy_h": [
        137053000000,
        129362000000,
        125260000000
      ],
      "interest_expense_on_debt_fy_h": [
        null,
        null,
        -3933000000
      ],
      "cost_of_goods_fy_h": [
        -220960000000,
        -210352000000,
        -214137000000
      ],
      "sell_gen_admin_exp_total_fy_h": [
        -62151000000,
        -57467000000,
        -54847000000
      ],
      "income_tax_fy_h": [
        -20719000000,
        -29749000000,
        -16741000000
      ],
      "revenue_fy_h": [
        416161000000,
        391035000000,
        383285000000
      ],
      "earnings_publication_type_fy_h": [
        22,
        22,
        22
      ],
      "accum_deprec_machinery_fy_h": [
        null,
        null,
        null
      ],
      "cash_n_short_term_invest_fy_h": [
        54697000000,
        65171000000,
        61555000000
      ],
      "purchase_of_stock_fy_h": [
        -90711000000,
        -94949000000,
        -77550000000
      ],
      "preferred_dividends_cash_flow_fy_h": [
        0,
        0,
        0
      ],
      "supplying_of_long_term_debt_fy_h": [
        4481000000,
        0,
        5228000000
      ],
      "ebitda_margin_fy_h": [
        34.7817311088737,
        34.4370708504354,
        32.8267477203647
      ],
      "accum_deprec_leases_fy_h": [
        null,
        null,
        null
      ],
      "current_port_debt_capital_leases_fy_h": [
        12888000000,
        11056000000,
        9987000000
      ],
      "long_term_note_receivable_fy_h": [
        null,
        null,
        null
      ],
      "other_receivables_fy_h": [
        33180000000,
        32833000000,
        31477000000
      ],
      "proceeds_from_stock_options_fy_h": [
        0,
        0,
        0
      ],
      "accounts_payable_fy_h": [
        69860000000,
        68960000000,
        62611000000
      ],
      "dilution_adjustment_fy_h": [
        0,
        0,
        0
      ],
      "other_exceptional_charges_fy_h": [
        null,
        null,
        null
      ],
      "earnings_release_date_fy_h": [
        1761856320,
        1730406900,
        1698957000
      ],
      "accrued_payroll_fy_h": [
        null,
        null,
        null
      ],
      "other_intangibles_gross_fy_h": [
        null,
        null,
        null
      ],
      "sell_gen_admin_exp_other_fy_h": [
        -27601000000,
        -26097000000,
        -24932000000
      ],
      "accum_deprec_trans_equip_fy_h": [
        null,
        null,
        null
      ],
      "change_in_accounts_payable_fy_h": [
        902000000,
        6020000000,
        -1889000000
      ],
      "fiscal_period_end_fy_h": [
        1759190400,
        1727654400,
        1696032000
      ],
      "accum_deprec_leased_prop_fy_h": [
        null,
        null,
        null
      ],
      "common_stock_par_fy_h": [
        93568000000,
        83276000000,
        73812000000
      ],
      "deferred_income_current_fy_h": [
        9055000000,
        8249000000,
        8061000000
      ],
      "book_value_per_share_fy_h": [
        4.99098,
        3.76734,
        3.99651
      ],
      "income_tax_payable_fy_h": [
        13016000000,
        26601000000,
        null
      ],
      "unusual_expense_inc_fy_h": [
        0,
        0,
        0
      ],
      "capital_expenditures_fixed_assets_fy_h": [
        -12715000000,
        -9447000000,
        -10959000000
      ],
      "purchase_sale_investments_fy_h": [
        29390000000,
        13690000000,
        16001000000
      ],
      "provision_f_risks_fy_h": [
        0,
        9254000000,
        15457000000
      ],
      "return_on_invested_capital_fy_h": [
        70.6326735233099,
        58.1864230024333,
        58.950445645799
      ],
      "gross_profit_fy_h": [
        195201000000,
        180683000000,
        169148000000
      ],
      "revenue_forecast_fy_h": [
        415406882375,
        390480701773,
        383094279806
      ],
      "depreciation_fy_h": [
        -8000000000,
        -8200000000,
        -8500000000
      ],
      "income_tax_current_foreign_fy_h": [
        -8891000000,
        -25483000000,
        -8750000000
      ],
      "cash_n_equivalents_fy_h": [
        33539000000,
        27977000000,
        28840000000
      ],
      "cost_of_goods_excl_dep_amort_fy_h": [
        -209262000000,
        -198907000000,
        -202618000000
      ],
      "float_shares_outstanding_fy_h": [
        14760953874.42,
        15102697155.448,
        15536330296.137
      ],
      "total_equity_fy_h": [
        73733000000,
        56950000000,
        62146000000
      ],
      "change_in_other_assets_fy_h": [
        -20273000000,
        3821000000,
        -2653000000
      ],
      "sales_of_investments_fy_h": [
        53797000000,
        62346000000,
        45514000000
      ],
      "deferred_income_non_current_fy_h": [
        null,
        null,
        null
      ],
      "earnings_per_share_fy_h": [
        7.46,
        6.75,
        6.13
      ],
      "income_tax_deferred_domestic_fy_h": [
        1943000000,
        3378000000,
        3693000000
      ],
      "total_debt_per_share_fy_h": [
        7.489454802052983,
        7.727042181398804,
        7.837447060236406
      ],
      "other_liabilities_total_fy_h": [
        29946000000,
        25836000000,
        23124000000
      ],
      "pre_tax_margin_fy_h": [
        31.8936661532436,
        31.5790146662064,
        29.6740023742124
      ],
      "change_in_inventories_fy_h": [
        1400000000,
        -1046000000,
        -1618000000
      ],
      "gross_margin_fy_h": [
        46.9051641071605,
        46.2063498152339,
        44.1311295772076
      ],
      "long_term_debt_excl_capital_lease_fy_h": [
        89239000000,
        95796000000,
        105689000000
      ],
      "number_of_shareholders_fy_h": [
        22429,
        22429,
        22429
      ]
    },
    "dividend": {
      "dividend_type_h": [
        "Quarterly",
        "Quarterly",
        "Quarterly"
      ],
      "dividend_yield_recent": 0.38088262223036073,
      "dividend_ex_date_h": [
        1770638340,
        1762775940,
        1754913540
      ],
      "dividend_amount_recent": 0.25999999,
      "continuous_dividend_payout": 14,
      "dividend_ex_date_recent": 1770638340,
      "dividend_record_date_h": [
        1770638340,
        1762775940,
        1754913540
      ],
      "dividend_payment_date_h": [
        1770897540,
        1763035140,
        1755172740
      ],
      "dividend_payment_date_recent": 1770897540,
      "dividend_amount_h": [
        0.26,
        0.26,
        0.26
      ],
      "continuous_dividend_growth": 13
    },
    "analyst_recommendations": {
      "recommendation_mark": 1.443396,
      "recommendation_total": 53,
      "recommendation_hold": 14,
      "price_target_up_num": 10,
      "price_target_high": 350,
      "price_target_down_num": 0,
      "recommendation_under": 0,
      "price_target_low": 215,
      "price_target_estimates_num": 41,
      "recommendation_over": 11,
      "recommendation_date": "2026-04-16",
      "recommendation_sell": 2,
      "price_target_median": 310,
      "price_target_average": 301.617561,
      "price_target_date": "2026-04-20",
      "recommendation_buy": 26
    },
    "enterprise_value": {
      "sum_for_enterprise_value": 23602000000
    },
    "credit_ratings": {
      "issuer_snp_rating_lt": 740,
      "issuer_snp_rating_st_h": [
        {
          "date": 1398297600,
          "outlook": null,
          "rating": 730
        },
        {
          "date": 856742400,
          "outlook": null,
          "rating": 500
        }
      ],
      "issuer_snp_rating_lt_h": [
        {
          "date": 1366675200,
          "outlook": 0,
          "rating": 740
        },
        {
          "date": 1082073600,
          "outlook": null,
          "rating": 500
        }
      ],
      "issuer_snp_rating_st": 730
    },
    "cash_flow": {
      "operating_cash_flow_per_share": 9.1471130066016,
      "cash_f_operating_activities_fh": 83653000000,
      "cash_f_financing_activities_fh": -67132000000,
      "cash_f_investing_activities_fh": -7473000000
    }
  },
  "msg": "Success"
}
```

## Get Company Profile

`GET /api/market-data/{symbol}/company`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL/company' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "company": {
      "listed_exchange": "NASDAQ",
      "local_description": "Apple Inc.",
      "cusip": "037833100",
      "isin-displayed": "US0378331005",
      "currency_code": "USD",
      "ceo": "Timothy Donald Cook",
      "isin": "US0378331005",
      "currency-logoid": "country/US",
      "description": "Apple Inc.",
      "sector": "Electronic Technology",
      "web_site_url": "http://www.apple.com",
      "industry": "Telecommunications Equipment",
      "business_description": "Apple, Inc. engages in the design, manufacture, and sale of smartphones, personal computers, tablets, wearables and accessories, and other varieties of related services. It operates through the following geographical segments: Americas, Europe, Greater China, Japan, and Rest of Asia Pacific. The Ame... (605 more chars truncated)",
      "currency_id": "USD",
      "short_description": "Apple Inc.",
      "fundamental_currency_code": "USD",
      "exchange": "Cboe One",
      "timezone": "America/New_York",
      "founded": 1976,
      "country_code": "US",
      "exchange_traded_name": "Cboe One",
      "short-description": "Apple Inc.",
      "local-description": "Apple Inc.",
      "currency-id": "USD",
      "sector-i18n-en": "Electronic Technology",
      "top_revenue_country_code": "US",
      "exchange-listed": "NASDAQ",
      "exchange-listed-symbol": "AAPL",
      "exchange-ticker": "AAPL",
      "country_fund": "United States",
      "country_code_fund": "US",
      "exchange_listed_name": "NASDAQ",
      "description-i18n-en": "APPLE INC",
      "business_description-i18n-en": "Apple, Inc. engages in the design, manufacture, and sale of smartphones, personal computers, tablets, wearables and accessories, and other variety of related services. It operates through the following geographical segments: Americas, Europe, Greater China, Japan, and Rest of Asia Pacific. The Ameri... (601 more chars truncated)",
      "exchange-traded": "Cboe One",
      "country": "United States",
      "currency_fund": "USD",
      "industry-i18n-en": "Telecommunications Equipment",
      "currency": "USD",
      "number_of_employees": 166000
    }
  },
  "msg": "Success"
}
```

## Get IPO Information

`GET /api/market-data/{symbol}/ipo`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL/ipo' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "ipo": {
      "ipo_offer_date": 345427200
    }
  },
  "msg": "Success"
}
```

## Get Market Indicators

`GET /api/market-data/{symbol}/indicators`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL/indicators' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "indicators": {
      "price_52_week_high": 288.62,
      "market_cap_calc": 4008685001792.9995,
      "earnings_availability": 1,
      "price_percent_change_52_week": 38.4634888438134,
      "earnings_release_date": 1769722200,
      "beta_1_year": 1.1557966,
      "market_cap_basic": 4008685001793,
      "price_52_week_low": 193.25,
      "price_earnings": 34.18988334725069,
      "earnings_release_next_date": 1777581000,
      "price_percent_change_1_week": 5.128402571901587,
      "earnings_release_next_time": 1,
      "earnings_per_share_basic_fh": 4.7083,
      "earnings_release_date_h": [
        1769722200,
        1761856320,
        1753993980
      ],
      "price_annual_sales": 9.743150536234776,
      "beta_5_year": 1.1087966,
      "earnings_per_share_diluted_fh": 4.690300000000001,
      "beta_3_year": 0.8453335,
      "beta_2_year": 1.1140423,
      "earnings_release_calendar_date": 1767139200,
      "earnings_per_share_fh": 4.6899999999999995,
      "beta_10_year": 1.1667725,
      "earnings_release_next_calendar_date": 1774915200,
      "price_book_ratio": 54.143675190042835,
      "earnings_release_time": 1,
      "price_sales_ratio": 9.743150536234776,
      "earnings_per_share_forecast_next_fh": 3.679022,
      "current_ratio": 0.973744664864166,
      "quick_ratio": 0.937561203939224,
      "price_annual_book": 54.143675190042835
    }
  },
  "msg": "Success"
}
```

## Get TTM Data

`GET /api/market-data/{symbol}/ttm`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL/ttm' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "ttm": {
      "earnings_per_share_basic_ttm": 7.9334,
      "rates_ttm": {
        "time": 1767139200,
        "to_aud": 1.498689,
        "to_cad": 1.373249,
        "to_chf": 0.79277,
        "to_cny": 6.994964,
        "to_eur": 0.851419,
        "to_gbp": 0.74228,
        "to_inr": 89.88764,
        "to_jpy": 156.715248,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "price_earnings_ttm": 34.18988334725069,
      "oper_income_ttm": 141070000000,
      "cost_of_goods_ttm": -229460000000,
      "ebitda_ttm_h": [
        152902000000,
        144748000000,
        141696000000
      ],
      "sale_of_stock_ttm": 0,
      "pre_tax_margin_ttm": 32.4016280356368,
      "capital_expenditures_unchanged_ttm_h": [
        12148000000,
        12715000000,
        12381000000
      ],
      "preferred_dividends_cash_flow_ttm": 0,
      "cash_dividend_coverage_ratio_ttm": 9.30982823195144,
      "non_cash_items_ttm": 14563000000,
      "total_cash_dividends_paid_ttm": -15486000000,
      "changes_in_working_capital_ttm": -8700000000,
      "change_in_accounts_receivable_ttm": -11164000000,
      "net_income_bef_disc_oper_ttm": 117777000000,
      "purchase_of_business_ttm": 0,
      "net_margin_ttm": 27.0368236317683,
      "equity_in_earnings_ttm": 0,
      "sell_gen_admin_exp_other_ttm": -27918000000,
      "sloan_ratio_ttm": -4.801514380551389,
      "earnings_per_share_diluted_ttm": 7.9038,
      "discontinued_operations_ttm": 0,
      "change_in_other_assets_ttm": -6931000000,
      "altman_z_score_ttm": 10.6382004968314,
      "dividend_payout_ratio_ttm": 13.03170626787115,
      "funds_f_operations_ttm": 144172000000,
      "other_financing_cash_flow_sources_ttm": 0,
      "common_dividends_cash_flow_ttm": -15486000000,
      "after_tax_other_income_ttm": 0,
      "pretax_income_ttm": 141147000000,
      "other_investing_cash_flow_uses_ttm": -1031000000,
      "price_free_cash_flow_ttm": 45.9902082357882,
      "total_oper_expense_ttm": -294547000000,
      "capital_expenditures_ttm": -12148000000,
      "cash_f_operating_activities_ttm": 135472000000,
      "enterprise_value_ebitda_ttm": 26.37170868787197,
      "gross_profit_ttm_h": [
        206157000000,
        195201000000,
        190739000000
      ],
      "dep_amort_exp_income_s_ttm": -11832000000,
      "unusual_expense_inc_ttm": 0,
      "issuance_of_stock_net_ttm": -91806000000,
      "return_on_common_equity_ttm": 152.02132328265,
      "price_earnings_growth_ttm": 1.3330112942081678,
      "price_revenue_ttm": 9.1874341494478,
      "other_investing_cash_flow_items_total_ttm": -1031000000,
      "total_revenue_ttm_h": [
        435617000000,
        416161000000,
        408625000000
      ],
      "operating_expenses_ttm": -65087000000,
      "return_of_invested_capital_percent_ttm": 0.7463948363219249,
      "gross_margin_ttm": 47.325288039723,
      "graham_numbers_ttm": 32.66031923925423,
      "other_financing_cash_flow_items_total_ttm": -6075000000,
      "issuance_of_debt_net_ttm": -7604000000,
      "interest_capitalized_ttm": 0,
      "gross_profit_ttm": 206157000000,
      "ebitda_per_share_ttm": 10.323992211936027,
      "other_income_ttm": 77000000,
      "cash_f_investing_activities_ttm": 517000000,
      "capital_expenditures_unchanged_ttm": 12148000000,
      "total_extra_items_ttm": 0,
      "capital_expenditures_other_assets_ttm": 0,
      "free_cash_flow_per_share_ttm": 8.32687613991183,
      "free_cash_flow_ttm": 123324000000,
      "revenue_per_share_ttm": 29.4129999305891,
      "supplying_of_long_term_debt_ttm": 4481000000,
      "purchase_of_stock_ttm": -91806000000,
      "cost_of_goods_excl_dep_amort_ttm": -217628000000,
      "other_investing_cash_flow_sources_ttm": 0,
      "earnings_per_share_diluted_ttm_h": [
        7.9038,
        7.4593,
        6.5782
      ],
      "sell_gen_admin_exp_total_ttm": -65087000000,
      "ebitda_ttm": 152902000000,
      "capital_expenditures_fixed_assets_ttm": -12148000000,
      "operating_cash_flow_per_share_ttm": 9.1471130066016,
      "debt_to_revenue_ttm": 0.2077719648223095,
      "dilution_adjustment_ttm": 0,
      "reduction_of_long_term_debt_ttm": -12087000000,
      "piotroski_f_score_ttm": 9,
      "preferred_dividends_ttm": 0,
      "issuance_of_long_term_debt_ttm": -7606000000,
      "sales_of_business_ttm": 0,
      "purchase_sale_business_ttm": 0,
      "sustainable_growth_rate_ttm": 147.999690369089,
      "non_oper_income_ttm": 77000000,
      "net_income_starting_line_ttm": 117777000000,
      "change_in_accounts_payable_ttm": 8421000000,
      "capex_per_share_ttm": 0.820236866689768,
      "non_oper_interest_income_ttm": 0,
      "purchase_sale_investments_ttm": 13696000000,
      "diluted_net_income_ttm": 117777000000,
      "research_and_dev_ttm": -37169000000,
      "ebitda_margin_ttm": 35.1000993992429,
      "net_income_ttm": 117777000000,
      "cash_flow_deprecation_n_amortization_ttm": 11832000000,
      "pretax_equity_in_earnings_ttm": 0,
      "return_on_equity_adjust_to_book_ttm": 3.3491193072391447,
      "change_in_inventories_ttm": 974000000,
      "other_oper_expense_total_ttm": 0,
      "ebit_ttm": 141070000000,
      "net_income_ttm_h": [
        117777000000,
        112010000000,
        99280000000
      ],
      "issuance_of_short_term_debt_ttm": 2000000,
      "earnings_per_share_ttm": 7.9038,
      "cash_f_financing_activities_ttm": -120971000000,
      "purchase_of_investments_ttm": -30976000000,
      "total_revenue_ttm": 435617000000,
      "sales_of_investments_ttm": 44672000000,
      "zmijewski_score_ttm": -1.3748734798308557,
      "total_non_oper_income_ttm": 77000000,
      "minority_interest_exp_ttm": 0,
      "income_tax_ttm": -23370000000,
      "operating_margin_ttm": 32.3839519577978,
      "other_financing_cash_flow_uses_ttm": -6075000000,
      "ebit_per_share_ttm": 9.525091766869075,
      "free_cash_flow_ttm_h": [
        123324000000,
        98767000000,
        96184000000
      ],
      "cash_flow_deferred_taxes_ttm": 0
    }
  },
  "msg": "Success"
}
```

## Get Current Financial Metrics

`GET /api/market-data/{symbol}/current`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL/current' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "current": {
      "enterprise_value_current": 4032287001793,
      "total_shares_outstanding_current": 14681100000,
      "price_earnings_current": 34.18988334725069,
      "gross_margin_current": 48.1586855505162,
      "enterprise_value_ebitda_current": 26.37170868787197,
      "total_debt_per_share_current": 6.111196786896953,
      "ebitda_per_share_current": 10.323992211936027,
      "cash_per_share_current": 4.517582156701702,
      "ebitda_margin_current": 37.6095606444253,
      "quick_ratio_current": 0.937561203939224,
      "price_cash_flow_current": 29.542654584563593,
      "book_value_per_share_current": 5.99822,
      "rates_current": {
        "time": 1776729600,
        "to_aud": 1.393534,
        "to_cad": 1.364629,
        "to_chf": 0.778549,
        "to_cny": 6.818957,
        "to_eur": 0.848522,
        "to_gbp": 0.738989,
        "to_inr": 93.10987,
        "to_jpy": 158.831004,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "ebit_per_share_current": 9.525091766869075,
      "debt_to_asset_current": 0.23862303155574702,
      "net_margin_current": 29.2836472912435,
      "ncavps_ratio_current": -10.495965920805313,
      "revenue_per_share_current": 29.4129999305891,
      "dividend_payout_ratio_current": 9.14719954967633,
      "working_capital_per_share_current": -0.289946685313578,
      "market_cap_basic_current": 4008674355000,
      "book_tangible_per_share_current": 5.99821679047723,
      "asset_turnover_current": 1.20438993505506,
      "capex_per_share_current": 0.820236866689768,
      "return_on_invested_capital_current": 74.6394836321925,
      "operating_margin_current": 35.3738278750104,
      "pre_tax_margin_current": 35.4781713458917,
      "price_sales_current": 9.1874341494478,
      "price_book_current": 45.05169867060562,
      "price_free_cash_flow_current": 32.45274643929811,
      "return_on_equity_current": 152.02132328265,
      "long_term_debt_to_assets_current": 0.2021766583969818,
      "long_term_debt_to_equity_current": 0.8695430320898061,
      "float_shares_outstanding_current": 14663394593.4,
      "fiscal_period_end_current": 1767139200,
      "operating_cash_flow_per_share_current": 9.1471130066016,
      "return_on_assets_current": 32.5628782579605,
      "debt_to_equity_current": 1.02629549835582,
      "dividends_yield_current": 0.380882622230361,
      "fiscal_period_current": "2026-Q1",
      "invent_turnover_current": 35.8923822931331,
      "current_ratio_current": 0.973744664864166,
      "free_cash_flow_per_share_current": 8.32687613991183
    }
  },
  "msg": "Success"
}
```

## Get Quarterly Financials

`GET /api/market-data/{symbol}/financials-quarterly`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL/financials-quarterly' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "financials_quarterly": {
      "earnings_per_share_fq": 2.84,
      "earnings_per_share_forecast_next_fq": 1.942915,
      "earnings_per_share_diluted_fq": 2.8424,
      "purchase_of_investments_fq": -12693000000,
      "purchase_sale_business_fq": 0,
      "purchase_sale_investments_fq": -2359000000,
      "total_liabilities_shrhldrs_equity_fq": 379297000000,
      "price_cash_flow_fq": 29.89,
      "common_dividends_cash_flow_fq": -3921000000,
      "other_oper_expense_total_fq": 0,
      "sell_gen_admin_exp_other_fq": -7492000000,
      "depreciation_depletion_fq": 3214000000,
      "purchase_of_business_fq": 0,
      "ebitda_per_share_fq": 3.650553707149241,
      "total_receivables_net_fq": 70320000000,
      "ebit_fq": 50852000000,
      "total_cash_dividends_paid_fq": -3921000000,
      "other_investing_cash_flow_sources_fq": 0,
      "change_in_inventories_fq": -211000000,
      "reduction_of_long_term_debt_fq": -2164000000,
      "dilution_adjustment_fq": 0,
      "invent_turnover_fq": 35.8923822931331,
      "fiscal_period_end_fq": 1767139200,
      "fixed_assets_turnover_fq": 9.053851269900653,
      "other_liabilities_total_fq": 52055000000,
      "operating_cash_flow_per_share_fq": 3.64103334180488,
      "shrhldrs_equity_fq": 88190000000,
      "long_term_debt_fq": 76685000000,
      "treasury_stock_common_fq": 0,
      "other_investing_cash_flow_uses_fq": -154000000,
      "return_on_total_capital_fq": 82.4353700154271,
      "capital_expenditures_other_assets_fq": 0,
      "gross_margin_fq": 48.1586855505162,
      "invested_capital_fq": 164875000000,
      "other_receivables_fq": 30399000000,
      "supplying_of_long_term_debt_fq": 0,
      "cash_f_operating_activities_fq": 53925000000,
      "accounts_payable_fq": 70587000000,
      "pretax_equity_in_earnings_fq": 0,
      "ppe_total_gross_fq": 127320000000,
      "fiscal_period_fq": "2026-Q1",
      "current_ratio_fq": 0.973744664864166,
      "preferred_dividends_cash_flow_fq": 0,
      "non_oper_income_fq": 150000000,
      "net_income_bef_disc_oper_fq": 42097000000,
      "capital_expenditures_unchanged_fq": 2373000000,
      "capital_operating_lease_obligations_fq": 0,
      "eps_diluted_growth_percent_fq": 0.18537053254931402,
      "cash_n_equivalents_fq": 36785000000,
      "proceeds_from_stock_options_fq": 0,
      "price_sales_fq": 9.29520962313225,
      "change_in_accounts_payable_fq": 848000000,
      "change_in_accounts_receivable_fq": 2628000000,
      "dividend_payout_ratio_percent_fq": 0.0914719954967633,
      "return_on_invested_capital_fq": 74.6394836321925,
      "operating_expenses_fq": -18379000000,
      "other_income_fq": 150000000,
      "earnings_release_date_fq": 1769722200,
      "goodwill_fq": 0,
      "total_non_current_assets_fq": 221193000000,
      "cash_n_short_term_invest_fq": 66907000000,
      "basic_shares_outstanding_fq": 14748158000,
      "total_assets_to_equity_fq": 4.30090713232793,
      "accum_deprec_total_fq": -77161000000,
      "ncavps_ratio_fq": -10.495965920805313,
      "changes_in_working_capital_fq": 5548000000,
      "other_investments_fq": 77888000000,
      "earnings_release_next_calendar_date_fq": 1774915200,
      "net_margin_fq": 29.2836472912435,
      "earnings_release_calendar_date_fq": 1767139200,
      "working_capital_per_share_fq": -0.289946685313578,
      "common_equity_total_fq": 88190000000,
      "diluted_net_income_fq": 42097000000,
      "short_term_invest_fq": 30122000000,
      "earnings_release_time_fq": 1,
      "sell_gen_admin_exp_total_fq": -18379000000,
      "price_book_fq": 45.5802,
      "book_value_per_share_fq": 5.99822,
      "quick_ratio_fq": 0.937561203939224,
      "long_term_investments_fq": 77888000000,
      "next_earnings_fiscal_period_fq": "2026-Q2",
      "purchase_of_stock_fq": -24701000000,
      "diluted_shares_outstanding_fq": 14810356000,
      "operating_margin_fq": 35.3738278750104,
      "total_debt_fq": 90509000000,
      "long_term_other_assets_total_fq": 93146000000,
      "free_cash_flow_fq": 51552000000,
      "current_port_debt_capital_leases_fq": 11827000000,
      "other_proceeds_from_stock_sales_fq": 0,
      "total_revenue_fq": 143756000000,
      "total_current_liabilities_fq": 162367000000,
      "long_term_debt_excl_capital_lease_fq": 76685000000,
      "sale_of_stock_fq": 0,
      "inventory_work_in_progress_fq": 0,
      "discontinued_operations_fq": 0,
      "provision_f_risks_fq": 0,
      "preferred_stock_carrying_value_fq": 0,
      "investments_in_unconcsolidate_fq": 0,
      "return_on_assets_fq": 32.5628782579605,
      "total_current_assets_fq": 158104000000,
      "capital_lease_obligations_fq": 0,
      "return_on_equity_fq": 152.02132328265,
      "earnings_release_next_trading_date_fq": 1777507200,
      "capex_per_share_fq": 0.160225723135892,
      "issuance_of_debt_net_fq": -8074000000,
      "net_debt_to_ebitda_fq": 0.15436030921766883,
      "book_per_share_fq": 5.99822,
      "free_cash_flow_per_share_fq": 3.4808076186689907,
      "earnings_release_next_date_fq": 1777581000,
      "inventory_progress_payments_fq": 0,
      "enterprise_value_ebitda_fq": 26.6363640135512,
      "net_income_fq": 42097000000,
      "total_non_oper_income_fq": 150000000,
      "tobin_q_ratio_fq": 10.5978138508873,
      "long_term_debt_to_assets_fq": 0.2021766583969818,
      "revenue_fq": 143756000000,
      "debt_to_equity_fq": 1.02629549835582,
      "cost_of_goods_fq": -74525000000,
      "sales_of_investments_fq": 10334000000,
      "inventory_raw_materials_fq": 0,
      "total_equity_fq": 88190000000,
      "cash_f_investing_activities_fq": -4886000000,
      "cost_of_goods_excl_dep_amort_fq": -71311000000,
      "earnings_publication_type_fq": 22,
      "ebitda_margin_fq": 37.6095606444253,
      "accounts_receivables_net_fq": 39921000000,
      "debt_to_asset_fq": 0.23862303155574702,
      "total_non_current_liabilities_fq": 128740000000,
      "pretax_income_fq": 51002000000,
      "minority_interest_exp_fq": 0,
      "cash_flow_deferred_taxes_fq": 0,
      "dep_amort_exp_income_s_fq": -3214000000,
      "long_term_debt_to_equity_fq": 0.8695430320898061,
      "total_debt_per_share_fq": 6.111196786896953,
      "inventory_finished_goods_fq": 5875000000,
      "asset_turnover_fq": 1.20438993505506,
      "total_liabilities_fq": 291107000000,
      "total_extra_items_fq": 0,
      "rates_earnings_fq": {
        "time": 1767139200,
        "to_aud": 1.498689,
        "to_cad": 1.373249,
        "to_chf": 0.79277,
        "to_cny": 6.994964,
        "to_eur": 0.851419,
        "to_gbp": 0.74228,
        "to_inr": 89.88764,
        "to_jpy": 156.715248,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "other_financing_cash_flow_uses_fq": -2960000000,
      "other_investing_cash_flow_items_total_fq": -154000000,
      "common_stock_par_fq": 95221000000,
      "income_tax_fq": -8905000000,
      "other_financing_cash_flow_items_total_fq": -2960000000,
      "sales_of_business_fq": 0,
      "pre_tax_margin_fq": 35.4781713458917,
      "total_debt_to_capital_fq": 0.506488564569472,
      "issuance_of_short_term_debt_fq": -5910000000,
      "revenue_per_share_fq": 9.70645135066301,
      "cash_per_share_fq": 4.517582156701702,
      "earnings_publication_type_next_fq": 12,
      "net_income_starting_line_fq": 42097000000,
      "receivables_turnover_fq": 6.72113619181337,
      "book_tangible_per_share_fq": 5.99821679047723,
      "net_debt_fq": 23602000000,
      "rates_earnings_next_fq": {
        "time": 1774915200,
        "to_aud": 1.44959,
        "to_cad": 1.390975,
        "to_chf": 0.799194,
        "to_cny": 6.899883,
        "to_eur": 0.865524,
        "to_gbp": 0.75643,
        "to_inr": 93.519125,
        "to_jpy": 158.780565,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "minority_interest_fq": 0,
      "earnings_per_share_basic_fq": 2.8544,
      "after_tax_other_income_fq": 0,
      "total_assets_fq": 379297000000,
      "earnings_release_trading_date_fq": 1769644800,
      "cash_f_financing_activities_fq": -39656000000,
      "non_cash_items_fq": 3066000000,
      "ebitda_fq": 54066000000,
      "return_on_tang_assets_fq": 32.56287825796053,
      "total_shares_outstanding_fq": 14702703000,
      "issuance_of_stock_net_fq": -24701000000,
      "earnings_per_share_forecast_fq": 2.673324,
      "other_financing_cash_flow_sources_fq": 0,
      "revenue_forecast_next_fq": 109347054075,
      "capital_expenditures_fq": -2373000000,
      "tangible_assets_fq": 379297000000,
      "price_earnings_fq": 34.5909562488929,
      "deferred_income_current_fq": 9413000000,
      "share_buyback_ratio_fq": 0.4775993924157613,
      "preferred_dividends_fq": 0,
      "rates_fq": {
        "time": 1767139200,
        "to_aud": 1.498689,
        "to_cad": 1.373249,
        "to_chf": 0.79277,
        "to_cny": 6.994964,
        "to_eur": 0.851419,
        "to_gbp": 0.74228,
        "to_inr": 89.88764,
        "to_jpy": 156.715248,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "market_cap_basic_fq": 4019719000200,
      "total_oper_expense_fq": -92904000000,
      "oper_income_fq": 50852000000,
      "non_oper_interest_income_fq": 0,
      "enterprise_value_fq": 4072753330400,
      "working_capital_fq": -4263000000,
      "earnings_release_next_time_fq": 1,
      "return_on_capital_employed_fq": 67.71630865234609,
      "retained_earnings_fq": -2177000000,
      "interest_capitalized_fq": 0,
      "dividend_payout_ratio_fq": 9.14719954967633,
      "total_inventory_fq": 5875000000,
      "other_current_liabilities_fq": 68543000000,
      "dividends_yield_fq": 0.376737381126555,
      "revenue_forecast_fq": 138391007589,
      "ebit_per_share_fq": 3.43354339355516,
      "short_term_debt_excl_current_port_fq": 1997000000,
      "other_current_assets_total_fq": 15002000000,
      "research_and_dev_fq": -10887000000,
      "earnings_fiscal_period_fq": "2026-Q1",
      "funds_f_operations_fq": 48377000000,
      "gross_profit_fq": 69231000000,
      "short_term_debt_fq": 13824000000,
      "dividends_per_share_fq": 0.26,
      "capital_expenditures_fixed_assets_fq": -2373000000,
      "return_on_tang_equity_fq": 152.02132328264966,
      "other_common_equity_fq": -4854000000,
      "paid_in_capital_fq": 95221000000,
      "dps_common_stock_prim_issue_fq": 0.26,
      "equity_in_earnings_fq": 0,
      "unusual_expense_inc_fq": 0,
      "ppe_total_net_fq": 50159000000,
      "cash_flow_deprecation_n_amortization_fq": 3214000000,
      "change_in_other_assets_fq": 2283000000,
      "issuance_of_long_term_debt_fq": -2164000000
    }
  },
  "msg": "Success"
}
```

## Get Annual Financials

`GET /api/market-data/{symbol}/financials-annual`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL/financials-annual' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "financials_annual": {
      "dps_common_stock_prim_issue_fy": 1.02,
      "rates_fy": {
        "time": 1759190400,
        "to_aud": 1.512814,
        "to_cad": 1.392758,
        "to_chf": 0.796495,
        "to_cny": 7.120986,
        "to_eur": 0.852195,
        "to_gbp": 0.743937,
        "to_inr": 88.873089,
        "to_jpy": 147.928994,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "net_margin_fy": 26.9150641218182,
      "issuance_of_long_term_debt_fy": -6451000000,
      "earnings_per_share_forecast_fy": 7.381826,
      "cost_of_goods_excl_dep_amort_fy": -209262000000,
      "reduction_of_long_term_debt_fy": -10932000000,
      "price_sales_fy": 9.21061775519571,
      "invent_turnover_fy": 33.9833897262381,
      "purchase_of_investments_fy": -24407000000,
      "paid_in_capital_fy": 93568000000,
      "net_income_fy": 112010000000,
      "oper_income_per_employee_fy": 801506.0240963855,
      "cash_flow_deferred_taxes_fy": 0,
      "diluted_net_income_fy": 112010000000,
      "sale_of_stock_fy": 0,
      "issuance_of_stock_net_fy": -90711000000,
      "ebitda_per_share_fy": 9.64684591764832,
      "depreciation_fy": -8000000000,
      "preferred_stock_carrying_value_fy": 0,
      "dilution_adjustment_fy": 0,
      "other_investing_cash_flow_uses_fy": -1480000000,
      "zmijewski_score_fy": -1.2261588856208425,
      "earnings_per_share_forecast_next_fy": 8.500259,
      "long_term_debt_excl_capital_lease_fy": 89239000000,
      "issuance_of_short_term_debt_fy": -2032000000,
      "return_on_tang_equity_fy": 171.42244974480232,
      "total_shares_outstanding_fy": 14773260000,
      "ppe_total_net_fy": 61039000000,
      "restructuring_charge_fy": 0,
      "earnings_release_date_fy": 1761856320,
      "purchase_sale_business_fy": 0,
      "debt_to_revenue_fy": 0.2700325114559029,
      "total_current_assets_fy": 147957000000,
      "change_in_accounts_payable_fy": 902000000,
      "revenue_fy": 416161000000,
      "sales_of_investments_fy": 53797000000,
      "other_income_fy": -321000000,
      "deferred_tax_assests_fy": 20777000000,
      "number_of_shareholders_fy": 22429,
      "ebitda_per_employee_fy": 871975.9036144578,
      "fiscal_period_end_fy": 1759190400,
      "pretax_equity_in_earnings_fy": 0,
      "issuance_of_debt_net_fy": -8483000000,
      "ebitda_margin_fy": 34.7817311088737,
      "after_tax_other_income_fy": 0,
      "return_on_capital_employed_fy": 69.62359823965588,
      "total_debt_to_capital_fy": 0.603820321315351,
      "capital_expenditures_unchanged_fy": 12715000000,
      "preferred_dividends_cash_flow_fy": 0,
      "short_term_invest_fy": 21158000000,
      "deferred_income_current_fy": 9055000000,
      "earnings_per_share_basic_fy": 7.4931,
      "operating_cash_flow_per_share_fy": 7.42980681315991,
      "other_investments_fy": 77723000000,
      "float_shares_outstanding_fy": 14760953874.42,
      "accounts_payable_fy": 69860000000,
      "total_liabilities_shrhldrs_equity_fy": 359241000000,
      "goodwill_fy": 0,
      "common_stock_par_fy": 93568000000,
      "other_financing_cash_flow_uses_fy": -6071000000,
      "non_oper_interest_income_fy": 0,
      "depreciation_depletion_fy": 8000000000,
      "ebitda_fy": 144748000000,
      "free_cash_flow_fy": 98767000000,
      "income_tax_fy": -20719000000,
      "earnings_publication_type_next_fy": 10,
      "tangible_assets_fy": 359241000000,
      "operating_margin_fy": 31.9707997625919,
      "rates_earnings_fy": {
        "time": 1759190400,
        "to_aud": 1.512814,
        "to_cad": 1.392758,
        "to_chf": 0.796495,
        "to_cny": 7.120986,
        "to_eur": 0.852195,
        "to_gbp": 0.743937,
        "to_inr": 88.873089,
        "to_jpy": 147.928994,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "total_debt_per_share_fy": 7.489454802052983,
      "free_cash_flow_per_share_fy": 6.582405496092323,
      "ppe_gross_machinery_fy": 83420000000,
      "purchase_of_stock_fy": -90711000000,
      "total_assets_fy": 359241000000,
      "total_oper_expense_fy": -283111000000,
      "graham_numbers_fy": 28.95336730416689,
      "funds_f_operations_fy": 136482000000,
      "other_oper_expense_total_fy": 0,
      "return_on_equity_fy": 171.422449744802,
      "proceeds_from_stock_options_fy": 0,
      "dividend_payout_ratio_fy": 13.6637642330877,
      "capital_expenditures_fixed_assets_fy": -12715000000,
      "ncavps_ratio_fy": -9.310808853293045,
      "discontinued_operations_fy": 0,
      "total_non_current_liabilities_fy": 119877000000,
      "current_ratio_fy": 0.893292922218667,
      "gross_margin_fy": 46.9051641071605,
      "operating_lease_liabilities_fy": 10911000000,
      "total_revenue_fy": 416161000000,
      "enterprise_value_ebitda_fy": 26.7933919337055,
      "sloan_ratio_fy": -4.082774516271806,
      "capital_lease_obligations_fy": 692000000,
      "total_non_current_assets_fy": 211284000000,
      "asset_turnover_fy": 1.14926521048133,
      "change_in_inventories_fy": 1400000000,
      "net_debt_fy": 57680000000,
      "price_cash_flow_fy": 34.38,
      "revenue_per_share_fy": 27.7353817941142,
      "inventory_finished_goods_fy": 5718000000,
      "accounts_receivables_net_fy": 39777000000,
      "ppe_total_gross_fy": 137053000000,
      "dividend_payout_ratio_percent_fy": 0.136637642330877,
      "non_cash_items_fy": 12774000000,
      "free_cash_flow_per_employee_fy": 594981.9277108434,
      "income_tax_deferred_fy": 1339000000,
      "income_tax_current_domestic_fy": -13167000000,
      "sales_of_business_fy": 0,
      "invested_capital_fy": 163664000000,
      "cash_flow_deprecation_n_amortization_fy": 11698000000,
      "short_term_debt_fy": 22446000000,
      "net_income_starting_line_fy": 112010000000,
      "total_extra_items_fy": 0,
      "book_value_per_share_fy": 4.99098,
      "long_term_debt_to_assets_fy": 0.250336125330906,
      "income_tax_deferred_foreign_fy": -604000000,
      "quick_ratio_fy": 0.858770399261008,
      "other_proceeds_from_stock_sales_fy": 0,
      "change_in_other_assets_fy": -20273000000,
      "other_short_term_debt_fy": 9558000000,
      "total_cash_dividends_paid_fy": -15421000000,
      "cash_n_short_term_invest_fy": 54697000000,
      "return_on_total_capital_fy": 73.4841309072432,
      "cash_f_investing_activities_fy": 15195000000,
      "total_liabilities_fy": 285508000000,
      "purchase_sale_investments_fy": 29390000000,
      "net_debt_to_ebitda_fy": 0.3984856440158068,
      "dividends_payable_fy": 0,
      "dep_amort_exp_income_s_fy": -11698000000,
      "share_buyback_ratio_fy": 2.2724804068801387,
      "price_earnings_fy": 34.2210314802411,
      "unusual_expense_inc_fy": 0,
      "debt_to_equity_fy": 1.5241072518410999,
      "capital_expenditures_other_assets_fy": 0,
      "common_dividends_cash_flow_fy": -15421000000,
      "net_income_bef_disc_oper_fy": 112010000000,
      "rates_earnings_next_fy": {
        "time": 1790726400,
        "to_aud": 1.393534,
        "to_cad": 1.364629,
        "to_chf": 0.778549,
        "to_cny": 6.818957,
        "to_eur": 0.848522,
        "to_gbp": 0.738989,
        "to_inr": 93.10987,
        "to_jpy": 158.831004,
        "to_market": 1,
        "to_symbol": 1,
        "to_usd": 1
      },
      "number_of_employees_fy": 166000,
      "short_term_debt_excl_current_port_fy": 9558000000,
      "capex_per_share_fy": 0.847401317067582,
      "provision_f_risks_fy": 0,
      "inventory_work_in_progress_fy": 0,
      "purchase_of_business_fy": 0,
      "income_tax_credits_fy": 0,
      "equity_in_earnings_fy": 0,
      "sustainable_growth_rate_fy": 147.999690369089,
      "total_inventory_fy": 5718000000,
      "earnings_release_trading_date_fy": 1761782400,
      "minority_interest_exp_fy": 0,
      "working_capital_fy": -17674000000,
      "accounts_receivables_gross_fy": 39777000000,
      "changes_in_working_capital_fy": -25000000000,
      "cash_per_share_fy": 3.6453251938376363,
      "revenue_per_employee_fy": 2506993.97590361,
      "next_earnings_fiscal_period_fy": "2026",
      "amortization_of_intangibles_fy": -3698000000,
      "book_tangible_per_share_fy": 4.99097694077001,
      "minority_interest_fy": 0,
      "earnings_publication_type_fy": 22,
      "diluted_shares_outstanding_fy": 15004697000,
      "sell_gen_admin_exp_other_fy": -27601000000,
      "net_income_per_employee_fy": 674759.036144578,
      "sell_gen_admin_exp_total_fy": -62151000000,
      "income_tax_current_fy": -22058000000,
      "retained_earnings_fy": -14264000000,
      "total_assets_to_equity_fy": 4.8721874872852,
      "total_current_liabilities_fy": 165631000000,
      "inventory_raw_materials_fy": 0,
      "revenue_forecast_next_fy": 465619085380,
      "total_debt_fy": 112377000000,
      "cost_of_goods_fy": -220960000000,
      "price_book_fy": 51.1843,
      "total_assets_per_employee_fy": 2164102.40963855,
      "market_cap_basic_fy": 3773976999600,
      "cash_dividend_coverage_ratio_fy": 8.85039880682187,
      "other_investing_cash_flow_items_total_fy": -1480000000,
      "cash_f_financing_activities_fy": -120686000000,
      "cash_n_equivalents_fy": 33539000000,
      "inventory_progress_payments_fy": 0,
      "amortization_fy": 3698000000,
      "other_current_assets_total_fy": 14585000000,
      "receivables_turnover_fy": 5.97932471264368,
      "treasury_stock_common_fy": 0,
      "change_in_accounts_receivable_fy": -7029000000,
      "book_per_share_fy": 4.99098,
      "long_term_debt_to_equity_fy": 1.219684537452701,
      "gross_profit_fy": 195201000000,
      "return_on_equity_adjust_to_book_fy": 3.3491193072391447,
      "total_non_oper_income_fy": -321000000,
      "basic_shares_outstanding_fy": 14948500000,
      "operating_expenses_fy": -62151000000,
      "other_financing_cash_flow_sources_fy": 0,
      "working_capital_per_share_fy": -1.19635070390692,
      "long_term_investments_fy": 77723000000,
      "earnings_per_share_diluted_fy": 7.465,
      "eps_diluted_growth_percent_fy": 0.227069498323361,
      "income_tax_current_foreign_fy": -8891000000,
      "debt_to_asset_fy": 0.312817857649879,
      "current_port_debt_capital_leases_fy": 12888000000,
      "return_on_assets_fy": 30.93254683308,
      "other_financing_cash_flow_items_total_fy": -6071000000,
      "amortization_of_deferred_charges_fy": 0,
      "earnings_fiscal_period_fy": "2025",
      "accum_deprec_total_fy": -76014000000,
      "dividends_yield_fy": 0.399279730681907,
      "earnings_per_share_fy": 7.46,
      "income_tax_deferred_domestic_fy": 1943000000,
      "ebit_fy": 133050000000,
      "earnings_release_next_trading_date_fy": 1793232000,
      "earnings_release_next_date_fy": 1793275200,
      "return_on_common_equity_fy": 171.422449744802,
      "cash_f_operating_activities_fy": 111482000000,
      "common_equity_total_fy": 73733000000,
      "research_and_dev_fy": -34550000000,
      "research_and_dev_per_employee_fy": 208132.53012048194,
      "capital_operating_lease_obligations_fy": 11603000000,
      "ebit_per_share_fy": 8.86722337678662,
      "interest_capitalized_fy": 0,
      "revenue_forecast_fy": 415406882375,
      "return_on_tang_assets_fy": 30.93254683307996,
      "ppe_gross_other_fy": 15091000000,
      "fiscal_period_fy": "2025",
      "fixed_assets_turnover_fy": 7.116722102040991,
      "supplying_of_long_term_debt_fy": 4481000000,
      "ppe_gross_buildings_fy": 27337000000,
      "other_investing_cash_flow_sources_fy": 0,
      "enterprise_value_fy": 3890779895620,
      "preferred_dividends_fy": 0,
      "return_on_invested_capital_fy": 70.6326735233099,
      "other_current_liabilities_fy": 51254000000,
      "shrhldrs_equity_fy": 73733000000,
      "pretax_income_fy": 132729000000,
      "oper_income_fy": 133050000000,
      "total_receivables_net_fy": 72957000000,
      "income_tax_payable_fy": 13016000000,
      "pre_tax_margin_fy": 31.8936661532436,
      "other_common_equity_fy": -5571000000,
      "long_term_other_assets_total_fy": 51745000000,
      "total_equity_fy": 73733000000,
      "accrued_expenses_fy": 8919000000,
      "investments_in_unconcsolidate_fy": 0,
      "long_term_debt_fy": 89931000000,
      "capital_expenditures_fy": -12715000000,
      "other_receivables_fy": 33180000000,
      "other_liabilities_total_fy": 29946000000,
      "piotroski_f_score_fy": 8,
      "tobin_q_ratio_fy": 10.505418367057214,
      "total_debt_per_employee_fy": 676969.8795180724,
      "non_oper_income_fy": -321000000
    }
  },
  "msg": "Success"
}
```

## Get Quarterly History

`GET /api/market-data/{symbol}/history-quarterly`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL/history-quarterly' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "history_quarterly": {
      "pretax_equity_in_earnings_fq_h": [
        0,
        0,
        0
      ],
      "cash_f_financing_activities_fq_h": [
        -39656000000,
        -27476000000,
        -24833000000
      ],
      "net_debt_fq_h": [
        23602000000,
        57680000000,
        46326000000
      ],
      "accounts_receivables_net_fq_h": [
        39921000000,
        39777000000,
        27557000000
      ],
      "capital_expenditures_unchanged_fq_h": [
        2373000000,
        3242000000,
        3462000000
      ],
      "change_in_other_assets_fq_h": [
        2283000000,
        1004000000,
        -1327000000
      ],
      "deferred_tax_assests_fq_h": [
        null,
        20777000000,
        null
      ],
      "issuance_of_short_term_debt_fq_h": [
        -5910000000,
        -1967000000,
        3903000000
      ],
      "earnings_fq_h": [
        {
          "Actual": 1.4,
          "Estimate": 0.986396,
          "FiscalPeriod": "2021-Q2",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 1.3,
          "Estimate": 1.010662,
          "FiscalPeriod": "2021-Q3",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 1.24,
          "Estimate": 1.238778,
          "FiscalPeriod": "2021-Q4",
          "IsReported": true,
          "Type": 22
        }
      ],
      "total_liabilities_shrhldrs_equity_fq_h": [
        379297000000,
        359241000000,
        331495000000
      ],
      "cash_n_equivalents_fq_h": [
        36785000000,
        33539000000,
        30465000000
      ],
      "sell_gen_admin_exp_other_fq_h": [
        -7492000000,
        -7048000000,
        -6650000000
      ],
      "earnings_per_share_diluted_fq_h": [
        2.8424,
        1.8479,
        1.5677
      ],
      "interest_expense_on_debt_fq_h": [
        null,
        null,
        null
      ],
      "dilution_adjustment_fq_h": [
        0,
        0,
        0
      ],
      "diluted_net_income_fq_h": [
        42097000000,
        27466000000,
        23434000000
      ],
      "asset_turnover_fq_h": [
        1.20438993505506,
        1.14926521048133,
        1.23245569719517
      ],
      "capital_expenditures_other_assets_fq_h": [
        0,
        0,
        0
      ],
      "earnings_fiscal_period_fq_h": [
        "2026-Q1",
        "2025-Q4",
        "2025-Q3"
      ],
      "total_extra_items_fq_h": [
        0,
        0,
        0
      ],
      "treasury_stock_common_fq_h": [
        0,
        0,
        0
      ],
      "cash_n_short_term_invest_fq_h": [
        66907000000,
        54697000000,
        55372000000
      ],
      "revenue_fq_h": [
        143756000000,
        102466000000,
        94036000000
      ],
      "net_income_bef_disc_oper_fq_h": [
        42097000000,
        27466000000,
        23434000000
      ],
      "discontinued_operations_fq_h": [
        0,
        0,
        0
      ],
      "current_port_debt_capital_leases_fq_h": [
        11827000000,
        12888000000,
        9345000000
      ],
      "non_oper_income_fq_h": [
        150000000,
        377000000,
        -171000000
      ],
      "cash_f_investing_activities_fq_h": [
        -4886000000,
        -2587000000,
        5073000000
      ],
      "ppe_total_gross_fq_h": [
        127320000000,
        137053000000,
        124311000000
      ],
      "pre_tax_margin_fq_h": [
        35.4781713458917,
        32.014521890188,
        29.8087966310775
      ],
      "other_financing_cash_flow_uses_fq_h": [
        -2960000000,
        -265000000,
        -2524000000
      ],
      "ebit_per_share_fq_h": [
        3.43354339355516,
        2.18163704387003,
        1.88665121015744
      ],
      "purchase_sale_business_fq_h": [
        0,
        0,
        0
      ],
      "cash_f_operating_activities_fq_h": [
        53925000000,
        29728000000,
        27867000000
      ],
      "enterprise_value_fq_h": [
        4072753330400,
        3854737555140,
        3052105833320
      ],
      "net_income_starting_line_fq_h": [
        42097000000,
        27466000000,
        23434000000
      ],
      "inventory_progress_payments_fq_h": [
        0,
        0,
        0
      ],
      "fiscal_period_end_fq_h": [
        1767139200,
        1759190400,
        1751241600
      ],
      "sales_of_business_fq_h": [
        0,
        0,
        0
      ],
      "total_debt_fq_h": [
        90509000000,
        112377000000,
        101698000000
      ],
      "long_term_debt_fq_h": [
        76685000000,
        89931000000,
        82430000000
      ],
      "long_term_other_assets_total_fq_h": [
        93146000000,
        51745000000,
        82882000000
      ],
      "deferred_income_current_fq_h": [
        9413000000,
        9055000000,
        8979000000
      ],
      "accounts_payable_fq_h": [
        70587000000,
        69860000000,
        50374000000
      ],
      "earnings_publication_type_fq_h": [
        22,
        22,
        22
      ],
      "accum_deprec_total_fq_h": [
        -77161000000,
        -76014000000,
        -75803000000
      ],
      "quick_ratio_fq_h": [
        0.937561203939224,
        0.858770399261008,
        0.826006235827664
      ],
      "intangibles_net_fq_h": [
        null,
        null,
        null
      ],
      "short_term_debt_fq_h": [
        13824000000,
        22446000000,
        19268000000
      ],
      "total_non_current_assets_fq_h": [
        221193000000,
        211284000000,
        209004000000
      ],
      "ebitda_fq_h": [
        54066000000,
        35554000000,
        31032000000
      ],
      "sell_gen_admin_exp_total_fq_h": [
        -18379000000,
        -15914000000,
        -15516000000
      ],
      "total_inventory_fq_h": [
        5875000000,
        5718000000,
        5925000000
      ],
      "deferred_income_non_current_fq_h": [
        null,
        null,
        null
      ],
      "total_liabilities_fq_h": [
        291107000000,
        285508000000,
        265665000000
      ],
      "investments_in_unconcsolidate_fq_h": [
        0,
        0,
        0
      ],
      "other_investing_cash_flow_sources_fq_h": [
        0,
        0,
        0
      ],
      "book_tangible_per_share_fq_h": [
        5.99821679047723,
        4.99097694077001,
        4.43099090095379
      ],
      "other_investing_cash_flow_items_total_fq_h": [
        -154000000,
        -505000000,
        -340000000
      ],
      "other_proceeds_from_stock_sales_fq_h": [
        0,
        0,
        0
      ],
      "unusual_expense_inc_fq_h": [
        0,
        0,
        0
      ],
      "reduction_of_long_term_debt_fq_h": [
        -2164000000,
        -1250000000,
        -5673000000
      ],
      "ppe_total_net_fq_h": [
        50159000000,
        61039000000,
        48508000000
      ],
      "sales_of_investments_fq_h": [
        10334000000,
        7976000000,
        14024000000
      ],
      "goodwill_fq_h": [
        0,
        0,
        0
      ],
      "change_in_taxes_payable_fq_h": [
        null,
        null,
        null
      ],
      "working_capital_per_share_fq_h": [
        -0.289946685313578,
        -1.19635070390692,
        -1.25391051942683
      ],
      "dep_amort_exp_income_s_fq_h": [
        -3214000000,
        -3127000000,
        -2830000000
      ],
      "inventory_work_in_progress_fq_h": [
        0,
        0,
        0
      ],
      "income_tax_fq_h": [
        -8905000000,
        -5338000000,
        -4597000000
      ],
      "pretax_income_fq_h": [
        51002000000,
        32804000000,
        28031000000
      ],
      "price_cash_flow_fq_h": [
        29.89,
        34.06,
        27.69
      ],
      "cash_flow_deprecation_n_amortization_fq_h": [
        3214000000,
        3127000000,
        2830000000
      ],
      "total_oper_expense_fq_h": [
        -92904000000,
        -70039000000,
        -65834000000
      ],
      "capital_operating_lease_obligations_fq_h": [
        0,
        11603000000,
        0
      ],
      "after_tax_other_income_fq_h": [
        0,
        0,
        0
      ],
      "deferred_charges_fq_h": [
        null,
        null,
        null
      ],
      "income_tax_payable_fq_h": [
        null,
        13016000000,
        null
      ],
      "price_book_fq_h": [
        45.5802,
        51.1843,
        45.3804
      ],
      "preferred_stock_carrying_value_fq_h": [
        0,
        0,
        0
      ],
      "provision_f_risks_fq_h": [
        0,
        0,
        0
      ],
      "cash_per_share_fq_h": [
        4.517582156701702,
        3.6799272639639535,
        3.704263910674337
      ],
      "earnings_per_share_forecast_fq_h": [
        2.673324,
        1.777147,
        1.438019
      ],
      "common_equity_total_fq_h": [
        88190000000,
        73733000000,
        65830000000
      ],
      "current_ratio_fq_h": [
        0.973744664864166,
        0.893292922218667,
        0.867991780045351
      ],
      "change_in_inventories_fq_h": [
        -211000000,
        177000000,
        365000000
      ],
      "deferred_tax_liabilities_fq_h": [
        null,
        null,
        null
      ],
      "preferred_dividends_cash_flow_fq_h": [
        0,
        0,
        0
      ],
      "ncavps_ratio_fq_h": [
        -10.495965920805313,
        -8.766479858880055,
        -9.212167523887222
      ],
      "other_current_liabilities_fq_h": [
        68543000000,
        51254000000,
        62499000000
      ],
      "long_term_debt_to_equity_fq_h": [
        0.8695430320898061,
        1.219684537452701,
        1.2521646665653958
      ],
      "purchase_of_stock_fq_h": [
        -24701000000,
        -20132000000,
        -21075000000
      ],
      "fiscal_period_fq_h": [
        "2026-Q1",
        "2025-Q4",
        "2025-Q3"
      ],
      "short_term_invest_fq_h": [
        30122000000,
        21158000000,
        24907000000
      ],
      "long_term_debt_to_assets_fq_h": [
        0.2021766583969818,
        0.250336125330906,
        0.24866136744143955
      ],
      "oper_income_fq_h": [
        50852000000,
        32427000000,
        28202000000
      ],
      "other_oper_expense_total_fq_h": [
        0,
        0,
        0
      ],
      "ebitda_per_share_fq_h": [
        3.650553707149241,
        2.3920166360673236,
        2.0759719294236443
      ],
      "research_and_dev_fq_h": [
        -10887000000,
        -8866000000,
        -8866000000
      ],
      "cost_of_goods_fq_h": [
        -74525000000,
        -54125000000,
        -50318000000
      ],
      "total_shares_outstanding_fq_h": [
        14702703000,
        14773260000,
        14856722000
      ],
      "retained_earnings_fq_h": [
        -2177000000,
        -14264000000,
        -17607000000
      ],
      "shrhldrs_equity_fq_h": [
        88190000000,
        73733000000,
        65830000000
      ],
      "capital_expenditures_fq_h": [
        -2373000000,
        -3242000000,
        -3462000000
      ],
      "inventory_raw_materials_fq_h": [
        0,
        0,
        0
      ],
      "common_stock_par_fq_h": [
        95221000000,
        93568000000,
        89806000000
      ],
      "interest_capitalized_fq_h": [
        0,
        0,
        0
      ],
      "revenue_forecast_fq_h": [
        138391007589,
        102227074560,
        89562736363
      ],
      "operating_margin_fq_h": [
        35.3738278750104,
        31.646594968087,
        29.9906418818325
      ],
      "gross_profit_fq_h": [
        69231000000,
        48341000000,
        43718000000
      ],
      "operating_cash_flow_per_share_fq_h": [
        3.64103334180488,
        2.00005261171765,
        1.86424045363653
      ],
      "change_in_accrued_expenses_fq_h": [
        null,
        null,
        null
      ],
      "other_financing_cash_flow_sources_fq_h": [
        0,
        0,
        0
      ],
      "ebit_fq_h": [
        50852000000,
        32427000000,
        28202000000
      ],
      "common_dividends_cash_flow_fq_h": [
        -3921000000,
        -3862000000,
        -3945000000
      ],
      "other_investments_fq_h": [
        77888000000,
        77723000000,
        77614000000
      ],
      "other_income_fq_h": [
        150000000,
        377000000,
        -171000000
      ],
      "proceeds_from_stock_options_fq_h": [
        0,
        0,
        0
      ],
      "minority_interest_exp_fq_h": [
        0,
        0,
        0
      ],
      "ebitda_margin_fq_h": [
        37.6095606444253,
        34.6983389612164,
        33.0001276107023
      ],
      "revenue_per_share_fq_h": [
        9.70645135066301,
        6.89374969430372,
        6.2907997020908
      ],
      "return_on_assets_fq_h": [
        32.5628782579605,
        30.93254683308,
        29.943885375965
      ],
      "minority_interest_fq_h": [
        0,
        0,
        0
      ],
      "total_revenue_fq_h": [
        143756000000,
        102466000000,
        94036000000
      ],
      "depreciation_depletion_fq_h": [
        3214000000,
        null,
        null
      ],
      "revenues_fq_h": [
        {
          "Actual": 89584000000,
          "Estimate": 77088700724,
          "FiscalPeriod": "2021-Q2",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 81434000000,
          "Estimate": 73334747261,
          "FiscalPeriod": "2021-Q3",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 83360000000,
          "Estimate": 85054907222,
          "FiscalPeriod": "2021-Q4",
          "IsReported": true,
          "Type": 22
        }
      ],
      "earnings_per_share_fq_h": [
        2.84,
        1.85,
        1.57
      ],
      "earnings_per_share_basic_fq_h": [
        2.8544,
        1.8539,
        1.5724
      ],
      "price_earnings_fq_h": [
        34.5909562488929,
        34.2471813709061,
        30.5676324830501
      ],
      "short_term_debt_excl_current_port_fq_h": [
        1997000000,
        9558000000,
        9923000000
      ],
      "issuance_of_long_term_debt_fq_h": [
        -2164000000,
        -1250000000,
        -1192000000
      ],
      "other_common_equity_fq_h": [
        -4854000000,
        -5571000000,
        -6369000000
      ],
      "issuance_of_debt_net_fq_h": [
        -8074000000,
        -3217000000,
        2711000000
      ],
      "total_equity_fq_h": [
        88190000000,
        73733000000,
        65830000000
      ],
      "other_receivables_fq_h": [
        30399000000,
        33180000000,
        19278000000
      ],
      "return_on_invested_capital_fq_h": [
        74.6394836321925,
        70.6326735233099,
        65.9308549494627
      ],
      "prepaid_expenses_fq_h": [
        null,
        null,
        null
      ],
      "total_non_oper_income_fq_h": [
        150000000,
        377000000,
        -171000000
      ],
      "other_financing_cash_flow_items_total_fq_h": [
        -2960000000,
        -265000000,
        -2524000000
      ],
      "market_cap_basic_fq_h": [
        4019719000200,
        3773976999600,
        2987389659760
      ],
      "invent_turnover_fq_h": [
        35.8923822931331,
        33.9833897262381,
        36.0440033085194
      ],
      "sale_of_stock_fq_h": [
        0,
        0,
        0
      ],
      "capital_expenditures_fixed_assets_fq_h": [
        -2373000000,
        -3242000000,
        -3462000000
      ],
      "long_term_debt_excl_capital_lease_fq_h": [
        76685000000,
        89239000000,
        82430000000
      ],
      "total_non_current_liabilities_fq_h": [
        128740000000,
        119877000000,
        124545000000
      ],
      "total_receivables_net_fq_h": [
        70320000000,
        72957000000,
        46835000000
      ],
      "dividend_payout_ratio_fq_h": [
        9.14719954967633,
        14.0700254342767,
        16.5848057664094
      ],
      "accrued_payroll_fq_h": [
        null,
        null,
        null
      ],
      "long_term_note_receivable_fq_h": [
        null,
        null,
        null
      ],
      "additional_paid_in_capital_fq_h": [
        null,
        null,
        null
      ],
      "gross_margin_fq_h": [
        48.1586855505162,
        47.1776003747585,
        46.4907056871836
      ],
      "diluted_shares_outstanding_fq_h": [
        14810356000,
        14863609000,
        14948179000
      ],
      "earnings_release_date_fq_h": [
        1769722200,
        1761856320,
        1753993980
      ],
      "free_cash_flow_per_share_fq_h": [
        3.4808076186689907,
        1.7819360022185728,
        1.6326403369935563
      ],
      "cost_of_goods_excl_dep_amort_fq_h": [
        -71311000000,
        -50998000000,
        -47488000000
      ],
      "capital_lease_obligations_fq_h": [
        0,
        692000000,
        0
      ],
      "return_on_equity_fq_h": [
        152.02132328265,
        171.422449744802,
        149.813638352774
      ],
      "operating_expenses_fq_h": [
        -18379000000,
        -15914000000,
        -15516000000
      ],
      "non_oper_interest_exp_fq_h": [
        null,
        null,
        null
      ],
      "non_cash_items_fq_h": [
        3066000000,
        4842000000,
        3637000000
      ],
      "net_margin_fq_h": [
        29.2836472912435,
        26.8049889719517,
        24.9202433110724
      ],
      "purchase_sale_investments_fq_h": [
        -2359000000,
        1160000000,
        8875000000
      ],
      "other_liabilities_total_fq_h": [
        52055000000,
        29946000000,
        42115000000
      ],
      "total_current_liabilities_fq_h": [
        162367000000,
        165631000000,
        141120000000
      ],
      "non_oper_interest_income_fq_h": [
        0,
        0,
        0
      ],
      "other_investing_cash_flow_uses_fq_h": [
        -154000000,
        -505000000,
        -340000000
      ],
      "other_intangibles_net_fq_h": [
        null,
        null,
        null
      ],
      "total_debt_per_share_fq_h": [
        6.111196786896953,
        7.560546028895136,
        6.803370497503408
      ],
      "inventory_finished_goods_fq_h": [
        5875000000,
        5718000000,
        5925000000
      ],
      "operating_lease_liabilities_fq_h": [
        null,
        10911000000,
        null
      ],
      "cash_flow_deferred_taxes_fq_h": [
        0,
        0,
        0
      ],
      "net_income_fq_h": [
        42097000000,
        27466000000,
        23434000000
      ],
      "enterprise_value_ebitda_fq_h": [
        26.6363640135512,
        26.5443913224362,
        21.5398164614386
      ],
      "book_value_per_share_fq_h": [
        5.99822,
        4.99098,
        4.43099
      ],
      "long_term_investments_fq_h": [
        77888000000,
        77723000000,
        77614000000
      ],
      "purchase_of_investments_fq_h": [
        -12693000000,
        -6816000000,
        -5149000000
      ],
      "total_current_assets_fq_h": [
        158104000000,
        147957000000,
        122491000000
      ],
      "change_in_accounts_payable_fq_h": [
        848000000,
        19381000000,
        -3875000000
      ],
      "issuance_of_other_debt_fq_h": [
        null,
        null,
        null
      ],
      "changes_in_working_capital_fq_h": [
        5548000000,
        -5707000000,
        -2034000000
      ],
      "total_assets_fq_h": [
        379297000000,
        359241000000,
        331495000000
      ],
      "capex_per_share_fq_h": [
        0.160225723135892,
        0.218116609499079,
        0.23160011664297
      ],
      "basic_shares_outstanding_fq_h": [
        14748158000,
        14815307000,
        14902886000
      ],
      "debt_to_asset_fq_h": [
        0.23862303155574702,
        0.312817857649879,
        0.306785924372917
      ],
      "supplying_of_long_term_debt_fq_h": [
        0,
        0,
        4481000000
      ],
      "preferred_dividends_fq_h": [
        0,
        0,
        0
      ],
      "dps_common_stock_prim_issue_fq_h": [
        0.26,
        0.26,
        0.26
      ],
      "price_sales_fq_h": [
        9.29520962313225,
        9.12401103212459,
        7.35583929842765
      ],
      "equity_in_earnings_fq_h": [
        0,
        0,
        0
      ],
      "paid_in_capital_fq_h": [
        95221000000,
        93568000000,
        89806000000
      ],
      "issuance_of_stock_net_fq_h": [
        -24701000000,
        -20132000000,
        -21075000000
      ],
      "debt_to_equity_fq_h": [
        1.02629549835582,
        1.5241072518410999,
        1.54485796749202
      ],
      "change_in_accounts_receivable_fq_h": [
        2628000000,
        -26269000000,
        2803000000
      ],
      "amortization_fq_h": [
        null,
        null,
        null
      ],
      "funds_f_operations_fq_h": [
        48377000000,
        35435000000,
        29901000000
      ],
      "other_current_assets_total_fq_h": [
        15002000000,
        14585000000,
        14359000000
      ],
      "total_cash_dividends_paid_fq_h": [
        -3921000000,
        -3862000000,
        -3945000000
      ],
      "free_cash_flow_fq_h": [
        51552000000,
        26486000000,
        24405000000
      ],
      "purchase_of_business_fq_h": [
        0,
        0,
        0
      ]
    }
  },
  "msg": "Success"
}
```

## Get Annual History

`GET /api/market-data/{symbol}/history-annual`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL/history-annual' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "history_annual": {
      "issuance_of_long_term_debt_fy_h": [
        -6451000000,
        -9958000000,
        -5923000000
      ],
      "ppe_gross_other_fy_h": [
        15091000000,
        14233000000,
        12839000000
      ],
      "inventory_raw_materials_fy_h": [
        0,
        0,
        0
      ],
      "accum_deprec_construction_fy_h": [
        null,
        null,
        null
      ],
      "additional_paid_in_capital_fy_h": [
        null,
        null,
        null
      ],
      "non_oper_interest_exp_fy_h": [
        null,
        null,
        -3933000000
      ],
      "inventory_finished_goods_fy_h": [
        5718000000,
        7286000000,
        6331000000
      ],
      "revenue_per_share_fy_h": [
        27.7353817941142,
        25.3785429022861,
        24.2392955416986
      ],
      "capex_per_share_fy_h": [
        0.847401317067582,
        0.613119272693996,
        0.69305722854136
      ],
      "price_sales_fy_h": [
        9.21061775519571,
        8.97569261076374,
        7.06332408487157
      ],
      "impairments_fy_h": [
        null,
        null,
        null
      ],
      "cash_flow_deprecation_n_amortization_fy_h": [
        11698000000,
        11445000000,
        11519000000
      ],
      "working_capital_per_share_fy_h": [
        -1.19635070390692,
        -1.54827884710414,
        -0.112025284016571
      ],
      "capital_expenditures_fy_h": [
        -12715000000,
        -9447000000,
        -10959000000
      ],
      "long_term_debt_to_equity_fy_h": [
        1.219684537452701,
        1.6953116769095697,
        1.7144788079683326
      ],
      "diluted_shares_outstanding_fy_h": [
        15004697000,
        15408095000,
        15812547000
      ],
      "debt_to_equity_fy_h": [
        1.5241072518410999,
        2.09058823529412,
        1.99417500724101
      ],
      "common_dividends_cash_flow_fy_h": [
        -15421000000,
        -15234000000,
        -15025000000
      ],
      "inventory_progress_payments_fy_h": [
        0,
        0,
        0
      ],
      "total_extra_items_fy_h": [
        0,
        0,
        0
      ],
      "earnings_per_share_forecast_fy_h": [
        7.381826,
        6.708209,
        6.057597
      ],
      "ppe_gross_leased_prop_fy_h": [
        null,
        null,
        null
      ],
      "income_tax_credits_fy_h": [
        0,
        0,
        0
      ],
      "total_current_assets_fy_h": [
        147957000000,
        152987000000,
        143566000000
      ],
      "restructuring_charge_fy_h": [
        0,
        0,
        0
      ],
      "ebitda_fy_h": [
        144748000000,
        134661000000,
        125820000000
      ],
      "research_and_dev_fy_h": [
        -34550000000,
        -31370000000,
        -29915000000
      ],
      "other_investing_cash_flow_items_total_fy_h": [
        -1480000000,
        -1308000000,
        -1337000000
      ],
      "other_common_equity_fy_h": [
        -5571000000,
        -7172000000,
        -11452000000
      ],
      "accounts_receivables_gross_fy_h": [
        39777000000,
        33410000000,
        29508000000
      ],
      "issuance_of_debt_net_fy_h": [
        -8483000000,
        -5998000000,
        -9901000000
      ],
      "earnings_per_share_basic_fy_h": [
        7.4931,
        6.109,
        6.1607
      ],
      "cash_f_operating_activities_fy_h": [
        111482000000,
        118254000000,
        110543000000
      ],
      "total_non_current_assets_fy_h": [
        211284000000,
        211993000000,
        209017000000
      ],
      "ppe_gross_comp_soft_fy_h": [
        null,
        null,
        null
      ],
      "pretax_equity_in_earnings_fy_h": [
        0,
        0,
        0
      ],
      "cash_f_financing_activities_fy_h": [
        -120686000000,
        -121983000000,
        -108488000000
      ],
      "free_cash_flow_per_share_fy_h": [
        6.582405496092323,
        7.061677644121483,
        6.297783652437523
      ],
      "purchase_sale_business_fy_h": [
        0,
        0,
        0
      ],
      "total_current_liabilities_fy_h": [
        165631000000,
        176392000000,
        145308000000
      ],
      "oper_income_fy_h": [
        133050000000,
        123216000000,
        114301000000
      ],
      "operating_lease_liabilities_fy_h": [
        10911000000,
        10046000000,
        10408000000
      ],
      "short_term_debt_excl_current_port_fy_h": [
        9558000000,
        11455000000,
        7395000000
      ],
      "invent_turnover_fy_h": [
        33.9833897262381,
        30.8954982742161,
        37.9776536312849
      ],
      "total_oper_expense_fy_h": [
        -283111000000,
        -267819000000,
        -268984000000
      ],
      "free_cash_flow_fy_h": [
        98767000000,
        108807000000,
        99584000000
      ],
      "common_equity_total_fy_h": [
        73733000000,
        56950000000,
        62146000000
      ],
      "income_tax_deferred_foreign_fy_h": [
        -604000000,
        -347000000,
        -669000000
      ],
      "purchase_of_business_fy_h": [
        0,
        0,
        0
      ],
      "doubtful_accounts_fy_h": [
        null,
        null,
        null
      ],
      "earnings_fiscal_period_fy_h": [
        "2025",
        "2024",
        "2023"
      ],
      "non_oper_income_fy_h": [
        -321000000,
        269000000,
        3368000000
      ],
      "diluted_net_income_fy_h": [
        112010000000,
        93736000000,
        96995000000
      ],
      "accrued_expenses_fy_h": [
        8919000000,
        null,
        null
      ],
      "accum_deprec_buildings_fy_h": [
        null,
        null,
        null
      ],
      "number_of_employees_fy_h": [
        166000,
        164000,
        161000
      ],
      "basic_shares_outstanding_fy_h": [
        14948500000,
        15343783000,
        15744231000
      ],
      "other_financing_cash_flow_sources_fy_h": [
        0,
        0,
        0
      ],
      "accounts_receivables_net_fy_h": [
        39777000000,
        33410000000,
        29508000000
      ],
      "long_term_other_assets_total_fy_h": [
        51745000000,
        45101000000,
        36245000000
      ],
      "other_proceeds_from_stock_sales_fy_h": [
        0,
        0,
        0
      ],
      "issuance_of_other_debt_fy_h": [
        null,
        null,
        null
      ],
      "total_revenue_fy_h": [
        416161000000,
        391035000000,
        383285000000
      ],
      "capital_lease_obligations_fy_h": [
        692000000,
        752000000,
        859000000
      ],
      "capital_expenditures_unchanged_fy_h": [
        12715000000,
        9447000000,
        10959000000
      ],
      "accum_deprec_comp_soft_fy_h": [
        null,
        null,
        null
      ],
      "capital_operating_lease_obligations_fy_h": [
        11603000000,
        10798000000,
        11267000000
      ],
      "accum_deprec_other_intang_fy_h": [
        null,
        null,
        null
      ],
      "deferred_tax_assests_fy_h": [
        20777000000,
        19499000000,
        17852000000
      ],
      "long_term_investments_fy_h": [
        77723000000,
        91479000000,
        100544000000
      ],
      "issuance_of_short_term_debt_fy_h": [
        -2032000000,
        3960000000,
        -3978000000
      ],
      "enterprise_value_ebitda_fy_h": [
        26.7933919337055,
        26.3785651380132,
        21.9187980596884
      ],
      "book_tangible_per_share_fy_h": [
        4.99097694077001,
        3.76733519942665,
        3.99651165355557
      ],
      "ppe_gross_construction_fy_h": [
        null,
        null,
        null
      ],
      "fiscal_period_fy_h": [
        "2025",
        "2024",
        "2023"
      ],
      "change_in_accounts_receivable_fy_h": [
        -7029000000,
        -5144000000,
        -417000000
      ],
      "net_margin_fy_h": [
        26.9150641218182,
        23.9712557699439,
        25.3062342643203
      ],
      "issuance_of_stock_net_fy_h": [
        -90711000000,
        -94949000000,
        -77550000000
      ],
      "earnings_per_share_diluted_fy_h": [
        7.465,
        6.0836,
        6.134
      ],
      "total_cash_dividends_paid_fy_h": [
        -15421000000,
        -15234000000,
        -15025000000
      ],
      "amortization_of_deferred_charges_fy_h": [
        0,
        0,
        null
      ],
      "current_ratio_fy_h": [
        0.893292922218667,
        0.867312576534083,
        0.988011671759297
      ],
      "accum_deprec_other_fy_h": [
        null,
        null,
        null
      ],
      "total_inventory_fy_h": [
        5718000000,
        7286000000,
        6331000000
      ],
      "income_tax_current_fy_h": [
        -22058000000,
        -32780000000,
        -19765000000
      ],
      "dividend_payout_ratio_fy_h": [
        13.6637642330877,
        16.1088828982839,
        15.3244212585589
      ],
      "non_cash_items_fy_h": [
        12774000000,
        9422000000,
        8606000000
      ],
      "total_assets_fy_h": [
        359241000000,
        364980000000,
        352583000000
      ],
      "changes_in_working_capital_fy_h": [
        -25000000000,
        3651000000,
        -6577000000
      ],
      "operating_margin_fy_h": [
        31.9707997625919,
        31.5102228700756,
        29.8214122650247
      ],
      "ebit_fy_h": [
        133050000000,
        123216000000,
        114301000000
      ],
      "amortization_of_intangibles_fy_h": [
        -3698000000,
        -3245000000,
        -3019000000
      ],
      "long_term_debt_to_assets_fy_h": [
        0.250336125330906,
        0.2645295632637405,
        0.302192675199882
      ],
      "operating_expenses_fy_h": [
        -62151000000,
        -57467000000,
        -54847000000
      ],
      "non_oper_interest_income_fy_h": [
        0,
        0,
        3750000000
      ],
      "operating_cash_flow_per_share_fy_h": [
        7.42980681315991,
        7.67479691681548,
        6.99084088097888
      ],
      "change_in_accrued_expenses_fy_h": [
        null,
        null,
        null
      ],
      "goodwill_gross_fy_h": [
        null,
        null,
        null
      ],
      "short_term_invest_fy_h": [
        21158000000,
        37194000000,
        32715000000
      ],
      "unrealized_gain_loss_fy_h": [
        null,
        null,
        null
      ],
      "reduction_of_long_term_debt_fy_h": [
        -10932000000,
        -9958000000,
        -11151000000
      ],
      "dep_amort_exp_income_s_fy_h": [
        -11698000000,
        -11445000000,
        -11519000000
      ],
      "inventory_work_in_progress_fy_h": [
        0,
        0,
        0
      ],
      "ppe_gross_machinery_fy_h": [
        83420000000,
        80205000000,
        78314000000
      ],
      "amortization_fy_h": [
        3698000000,
        3245000000,
        3019000000
      ],
      "dividends_yield_fy_h": [
        0.399279730681907,
        0.430220817419553,
        0.549033350855674
      ],
      "price_cash_flow_fy_h": [
        34.38,
        29.68,
        24.49
      ],
      "funds_f_operations_fy_h": [
        136482000000,
        114603000000,
        117120000000
      ],
      "minority_interest_exp_fy_h": [
        0,
        0,
        0
      ],
      "intangibles_net_fy_h": [
        null,
        null,
        null
      ],
      "other_intangibles_net_fy_h": [
        null,
        null,
        null
      ],
      "other_financing_cash_flow_uses_fy_h": [
        -6071000000,
        -5802000000,
        -6012000000
      ],
      "investments_in_unconcsolidate_fy_h": [
        0,
        0,
        0
      ],
      "shrhldrs_equity_fy_h": [
        73733000000,
        56950000000,
        62146000000
      ],
      "other_financing_cash_flow_items_total_fy_h": [
        -6071000000,
        -5802000000,
        -6012000000
      ],
      "debt_to_asset_fy_h": [
        0.312817857649879,
        0.32620691544742203,
        0.351491705499131
      ],
      "cash_f_investing_activities_fy_h": [
        15195000000,
        2935000000,
        3705000000
      ],
      "goodwill_amortization_fy_h": [
        null,
        null,
        null
      ],
      "other_oper_expense_total_fy_h": [
        0,
        0,
        0
      ],
      "ebit_per_share_fy_h": [
        8.86722337678662,
        7.9968354296881,
        7.2285002536277
      ],
      "ebitda_per_share_fy_h": [
        9.64684591764832,
        8.739626800068406,
        7.956972396667026
      ],
      "after_tax_other_income_fy_h": [
        0,
        0,
        0
      ],
      "ppe_gross_leases_fy_h": [
        null,
        null,
        null
      ],
      "net_income_starting_line_fy_h": [
        112010000000,
        93736000000,
        96995000000
      ],
      "cash_per_share_fy_h": [
        3.6453251938376363,
        4.229659798956328,
        3.892794753432195
      ],
      "cash_flow_deferred_taxes_fy_h": [
        0,
        0,
        0
      ],
      "income_tax_deferred_fy_h": [
        1339000000,
        3031000000,
        3024000000
      ],
      "other_investing_cash_flow_uses_fy_h": [
        -1480000000,
        -1308000000,
        -1337000000
      ],
      "enterprise_value_fy_h": [
        3890779895620,
        3563697960050,
        2769641171870
      ],
      "dps_common_stock_prim_issue_fy_h": [
        1.02,
        0.98,
        0.94
      ],
      "other_current_liabilities_fy_h": [
        51254000000,
        50071000000,
        57254000000
      ],
      "ppe_gross_buildings_fy_h": [
        27337000000,
        24690000000,
        23446000000
      ],
      "deferred_charges_fy_h": [
        null,
        null,
        null
      ],
      "total_non_current_liabilities_fy_h": [
        119877000000,
        131638000000,
        145129000000
      ],
      "ppe_total_net_fy_h": [
        61039000000,
        55914000000,
        54376000000
      ],
      "purchase_of_investments_fy_h": [
        -24407000000,
        -48656000000,
        -29513000000
      ],
      "return_on_equity_fy_h": [
        171.422449744802,
        157.412507556929,
        171.949511602758
      ],
      "price_earnings_fy_h": [
        34.2210314802411,
        37.4432901571438,
        27.9116400391262
      ],
      "total_non_oper_income_fy_h": [
        -321000000,
        269000000,
        -565000000
      ],
      "accum_deprec_land_fy_h": [
        null,
        null,
        null
      ],
      "preferred_stock_carrying_value_fy_h": [
        0,
        0,
        0
      ],
      "net_income_fy_h": [
        112010000000,
        93736000000,
        96995000000
      ],
      "legal_claim_expense_fy_h": [
        null,
        null,
        null
      ],
      "goodwill_fy_h": [
        0,
        null,
        null
      ],
      "net_debt_fy_h": [
        57680000000,
        53888000000,
        62375000000
      ],
      "notes_payable_short_term_debt_fy_h": [
        null,
        null,
        null
      ],
      "depreciation_depletion_fy_h": [
        8000000000,
        8200000000,
        8500000000
      ],
      "dividends_payable_fy_h": [
        0,
        0,
        0
      ],
      "deferred_tax_liabilities_fy_h": [
        null,
        null,
        null
      ],
      "pretax_income_fy_h": [
        132729000000,
        123485000000,
        113736000000
      ],
      "treasury_stock_common_fy_h": [
        0,
        0,
        0
      ],
      "long_term_debt_fy_h": [
        89931000000,
        96548000000,
        106548000000
      ],
      "equity_in_earnings_fy_h": [
        0,
        0,
        0
      ],
      "other_short_term_debt_fy_h": [
        9558000000,
        11455000000,
        7395000000
      ],
      "preferred_dividends_fy_h": [
        0,
        0,
        0
      ],
      "quick_ratio_fy_h": [
        0.858770399261008,
        0.826006848383147,
        0.944442150466595
      ],
      "ppe_gross_land_fy_h": [
        null,
        null,
        null
      ],
      "total_shares_outstanding_fy_h": [
        14773260000,
        15116786000,
        15550061000
      ],
      "other_current_assets_total_fy_h": [
        14585000000,
        14287000000,
        14695000000
      ],
      "net_income_bef_disc_oper_fy_h": [
        112010000000,
        93736000000,
        96995000000
      ],
      "return_on_assets_fy_h": [
        30.93254683308,
        26.1262077336763,
        27.503126160791
      ],
      "market_cap_basic_fy_h": [
        3773976999600,
        3443452682940,
        2662325943810
      ],
      "asset_turnover_fy_h": [
        1.14926521048133,
        1.08989733305647,
        1.08681228006998
      ],
      "ncavps_ratio_fy_h": [
        -9.310808853293045,
        -10.256346818695455,
        -9.445043334556694
      ],
      "price_book_fy_h": [
        51.1843,
        60.4644,
        42.8399
      ],
      "revenues_fy_h": [
        {
          "Actual": 229234000000,
          "Estimate": 227461939394,
          "FiscalPeriod": "2017",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 265595000000,
          "Estimate": 264521756757,
          "FiscalPeriod": "2018",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 260174000000,
          "Estimate": 259058735507,
          "FiscalPeriod": "2019",
          "IsReported": true,
          "Type": 22
        }
      ],
      "interest_capitalized_fy_h": [
        0,
        0,
        0
      ],
      "prepaid_expenses_fy_h": [
        null,
        null,
        null
      ],
      "earnings_fy_h": [
        {
          "Actual": 2.3025,
          "Estimate": 2.248051,
          "FiscalPeriod": "2017",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 2.9775,
          "Estimate": 2.936966,
          "FiscalPeriod": "2018",
          "IsReported": true,
          "Type": 22
        },
        {
          "Actual": 2.9725,
          "Estimate": 2.919387,
          "FiscalPeriod": "2019",
          "IsReported": true,
          "Type": 22
        }
      ],
      "total_debt_fy_h": [
        112377000000,
        119059000000,
        123930000000
      ],
      "other_investments_fy_h": [
        77723000000,
        91479000000,
        100544000000
      ],
      "income_tax_current_domestic_fy_h": [
        -13167000000,
        -7297000000,
        -11015000000
      ],
      "sales_of_business_fy_h": [
        0,
        0,
        0
      ],
      "ppe_gross_trans_equip_fy_h": [
        null,
        null,
        null
      ],
      "accum_deprec_total_fy_h": [
        -76014000000,
        -73448000000,
        -70884000000
      ],
      "change_in_taxes_payable_fy_h": [
        null,
        null,
        null
      ],
      "discontinued_operations_fy_h": [
        0,
        0,
        0
      ],
      "total_receivables_net_fy_h": [
        72957000000,
        66243000000,
        60985000000
      ],
      "total_liabilities_fy_h": [
        285508000000,
        308030000000,
        290437000000
      ],
      "total_liabilities_shrhldrs_equity_fy_h": [
        359241000000,
        364980000000,
        352583000000
      ],
      "retained_earnings_fy_h": [
        -14264000000,
        -19154000000,
        -214000000
      ],
      "paid_in_capital_fy_h": [
        93568000000,
        83276000000,
        73812000000
      ],
      "sale_of_stock_fy_h": [
        0,
        0,
        0
      ],
      "capital_expenditures_other_assets_fy_h": [
        0,
        0,
        0
      ],
      "short_term_debt_fy_h": [
        22446000000,
        22511000000,
        17382000000
      ],
      "minority_interest_fy_h": [
        0,
        0,
        0
      ],
      "other_investing_cash_flow_sources_fy_h": [
        0,
        0,
        0
      ],
      "other_income_fy_h": [
        -321000000,
        269000000,
        -382000000
      ],
      "ppe_total_gross_fy_h": [
        137053000000,
        129362000000,
        125260000000
      ],
      "interest_expense_on_debt_fy_h": [
        null,
        null,
        -3933000000
      ],
      "cost_of_goods_fy_h": [
        -220960000000,
        -210352000000,
        -214137000000
      ],
      "sell_gen_admin_exp_total_fy_h": [
        -62151000000,
        -57467000000,
        -54847000000
      ],
      "income_tax_fy_h": [
        -20719000000,
        -29749000000,
        -16741000000
      ],
      "revenue_fy_h": [
        416161000000,
        391035000000,
        383285000000
      ],
      "earnings_publication_type_fy_h": [
        22,
        22,
        22
      ],
      "accum_deprec_machinery_fy_h": [
        null,
        null,
        null
      ],
      "cash_n_short_term_invest_fy_h": [
        54697000000,
        65171000000,
        61555000000
      ],
      "purchase_of_stock_fy_h": [
        -90711000000,
        -94949000000,
        -77550000000
      ],
      "preferred_dividends_cash_flow_fy_h": [
        0,
        0,
        0
      ],
      "supplying_of_long_term_debt_fy_h": [
        4481000000,
        0,
        5228000000
      ],
      "ebitda_margin_fy_h": [
        34.7817311088737,
        34.4370708504354,
        32.8267477203647
      ],
      "accum_deprec_leases_fy_h": [
        null,
        null,
        null
      ],
      "current_port_debt_capital_leases_fy_h": [
        12888000000,
        11056000000,
        9987000000
      ],
      "long_term_note_receivable_fy_h": [
        null,
        null,
        null
      ],
      "other_receivables_fy_h": [
        33180000000,
        32833000000,
        31477000000
      ],
      "proceeds_from_stock_options_fy_h": [
        0,
        0,
        0
      ],
      "accounts_payable_fy_h": [
        69860000000,
        68960000000,
        62611000000
      ],
      "dilution_adjustment_fy_h": [
        0,
        0,
        0
      ],
      "other_exceptional_charges_fy_h": [
        null,
        null,
        null
      ],
      "earnings_release_date_fy_h": [
        1761856320,
        1730406900,
        1698957000
      ],
      "accrued_payroll_fy_h": [
        null,
        null,
        null
      ],
      "other_intangibles_gross_fy_h": [
        null,
        null,
        null
      ],
      "sell_gen_admin_exp_other_fy_h": [
        -27601000000,
        -26097000000,
        -24932000000
      ],
      "accum_deprec_trans_equip_fy_h": [
        null,
        null,
        null
      ],
      "change_in_accounts_payable_fy_h": [
        902000000,
        6020000000,
        -1889000000
      ],
      "fiscal_period_end_fy_h": [
        1759190400,
        1727654400,
        1696032000
      ],
      "accum_deprec_leased_prop_fy_h": [
        null,
        null,
        null
      ],
      "common_stock_par_fy_h": [
        93568000000,
        83276000000,
        73812000000
      ],
      "deferred_income_current_fy_h": [
        9055000000,
        8249000000,
        8061000000
      ],
      "book_value_per_share_fy_h": [
        4.99098,
        3.76734,
        3.99651
      ],
      "income_tax_payable_fy_h": [
        13016000000,
        26601000000,
        null
      ],
      "unusual_expense_inc_fy_h": [
        0,
        0,
        0
      ],
      "capital_expenditures_fixed_assets_fy_h": [
        -12715000000,
        -9447000000,
        -10959000000
      ],
      "purchase_sale_investments_fy_h": [
        29390000000,
        13690000000,
        16001000000
      ],
      "provision_f_risks_fy_h": [
        0,
        9254000000,
        15457000000
      ],
      "return_on_invested_capital_fy_h": [
        70.6326735233099,
        58.1864230024333,
        58.950445645799
      ],
      "gross_profit_fy_h": [
        195201000000,
        180683000000,
        169148000000
      ],
      "revenue_forecast_fy_h": [
        415406882375,
        390480701773,
        383094279806
      ],
      "depreciation_fy_h": [
        -8000000000,
        -8200000000,
        -8500000000
      ],
      "income_tax_current_foreign_fy_h": [
        -8891000000,
        -25483000000,
        -8750000000
      ],
      "cash_n_equivalents_fy_h": [
        33539000000,
        27977000000,
        28840000000
      ],
      "cost_of_goods_excl_dep_amort_fy_h": [
        -209262000000,
        -198907000000,
        -202618000000
      ],
      "float_shares_outstanding_fy_h": [
        14760953874.42,
        15102697155.448,
        15536330296.137
      ],
      "total_equity_fy_h": [
        73733000000,
        56950000000,
        62146000000
      ],
      "change_in_other_assets_fy_h": [
        -20273000000,
        3821000000,
        -2653000000
      ],
      "sales_of_investments_fy_h": [
        53797000000,
        62346000000,
        45514000000
      ],
      "deferred_income_non_current_fy_h": [
        null,
        null,
        null
      ],
      "earnings_per_share_fy_h": [
        7.46,
        6.75,
        6.13
      ],
      "income_tax_deferred_domestic_fy_h": [
        1943000000,
        3378000000,
        3693000000
      ],
      "total_debt_per_share_fy_h": [
        7.489454802052983,
        7.727042181398804,
        7.837447060236406
      ],
      "other_liabilities_total_fy_h": [
        29946000000,
        25836000000,
        23124000000
      ],
      "pre_tax_margin_fy_h": [
        31.8936661532436,
        31.5790146662064,
        29.6740023742124
      ],
      "change_in_inventories_fy_h": [
        1400000000,
        -1046000000,
        -1618000000
      ],
      "gross_margin_fy_h": [
        46.9051641071605,
        46.2063498152339,
        44.1311295772076
      ],
      "long_term_debt_excl_capital_lease_fy_h": [
        89239000000,
        95796000000,
        105689000000
      ],
      "number_of_shareholders_fy_h": [
        22429,
        22429,
        22429
      ]
    }
  },
  "msg": "Success"
}
```

## Get Dividend Data

`GET /api/market-data/{symbol}/dividend`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL/dividend' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "dividend": {
      "dividend_type_h": [
        "Quarterly",
        "Quarterly",
        "Quarterly"
      ],
      "dividend_yield_recent": 0.38088262223036073,
      "dividend_ex_date_h": [
        1770638340,
        1762775940,
        1754913540
      ],
      "dividend_amount_recent": 0.25999999,
      "continuous_dividend_payout": 14,
      "dividend_ex_date_recent": 1770638340,
      "dividend_record_date_h": [
        1770638340,
        1762775940,
        1754913540
      ],
      "dividend_payment_date_h": [
        1770897540,
        1763035140,
        1755172740
      ],
      "dividend_payment_date_recent": 1770897540,
      "dividend_amount_h": [
        0.26,
        0.26,
        0.26
      ],
      "continuous_dividend_growth": 13
    }
  },
  "msg": "Success"
}
```

## Get Analyst Recommendations

`GET /api/market-data/{symbol}/analyst-recommendations`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL/analyst-recommendations' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "analyst_recommendations": {
      "recommendation_mark": 1.443396,
      "recommendation_total": 53,
      "recommendation_hold": 14,
      "price_target_up_num": 10,
      "price_target_high": 350,
      "price_target_down_num": 0,
      "recommendation_under": 0,
      "price_target_low": 215,
      "price_target_estimates_num": 41,
      "recommendation_over": 11,
      "recommendation_date": "2026-04-16",
      "recommendation_sell": 2,
      "price_target_median": 310,
      "price_target_average": 301.617561,
      "price_target_date": "2026-04-20",
      "recommendation_buy": 26
    }
  },
  "msg": "Success"
}
```

## Get Enterprise Value Metrics

`GET /api/market-data/{symbol}/enterprise-value`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL/enterprise-value' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "enterprise_value": {
      "sum_for_enterprise_value": 23602000000
    }
  },
  "msg": "Success"
}
```

## Get Credit Ratings

`GET /api/market-data/{symbol}/credit-ratings`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL/credit-ratings' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "credit_ratings": {
      "issuer_snp_rating_lt": 740,
      "issuer_snp_rating_st_h": [
        {
          "date": 1398297600,
          "outlook": null,
          "rating": 730
        },
        {
          "date": 856742400,
          "outlook": null,
          "rating": 500
        }
      ],
      "issuer_snp_rating_lt_h": [
        {
          "date": 1366675200,
          "outlook": 0,
          "rating": 740
        },
        {
          "date": 1082073600,
          "outlook": null,
          "rating": 500
        }
      ],
      "issuer_snp_rating_st": 730
    }
  },
  "msg": "Success"
}
```

## Get Cash Flow Analysis

`GET /api/market-data/{symbol}/cash-flow`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/market-data/NASDAQ:AAPL/cash-flow' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "cash_flow": {
      "operating_cash_flow_per_share": 9.1471130066016,
      "cash_f_operating_activities_fh": 83653000000,
      "cash_f_financing_activities_fh": -67132000000,
      "cash_f_investing_activities_fh": -7473000000
    }
  },
  "msg": "Success"
}
```
