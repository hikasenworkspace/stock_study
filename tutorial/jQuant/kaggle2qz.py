import pandas as pd
import numpy as np
from datetime import date

today = date.today()
stock_list = pd.read_csv("../../kaggle/data/stock_list.csv")

columns_name = ['Local Code', 'Effective Date', 'Name (English)', 'Section/Products', 'NewMarketSegment', '33 Sector(Code)', '33 Sector(name)', '17 Sector(Code)', '17 Sector(name)', 'Size Code (New Index Series)', 'Size (New Index Series)', 'IssuedShareEquityQuote ModifyDate', 'Close', 'IssuedShareEquityQuote IssuedShare', 'MarketCapitalization', 'prediction_target']

stock_list.columns = columns_name

stock_list.to_csv("data/stock_list_"+str(today) + ".csv", index=False)


columns_name = ['DisclosureNumber', 'base_date (Code)', 'base_date', 'Local Code', 'DisclosedDate', 'DisclosedTime', 'DisclosedUnixTime', 'TypeOfDocument', 'Result_FinancialStatement FiscalPeriodEnd', 'Result_FinancialStatement ReportType', 'CurrentFiscalYearStartDate', 'CurrentFiscalYearEndDate', 'NetSales', 'OperatingProfit', 'OrdinaryProfit', 'Profit', 'EarningsPerShare', 'TotalAssets', 'Equity', 'EquityToAssetRatio', 'BookValuePerShare', 'ResultDividendPerShare1stQuarter', 'ResultDividendPerShare2ndQuarter', 'ResultDividendPerShare3rdQuarter', 'ResultDividendPerShareFiscalYearEnd', 'ResultDividendPerShareAnnual', 'ForecastDividendPerShare1stQuarter', 'ForecastDividendPerShare2ndQuarter', 'ForecastDividendPerShare3rdQuarter', 'ForecastDividendPerShareFiscalYearEnd', 'ForecastDividendPerShareAnnual', 'ForecastNetSales', 'ForecastOperatingProfit', 'ForecastOrdinaryProfit', 'ForecastProfit', 'ForecastEarningsPerShare', 'ApplyingOfSpecificAccountingOfTheQuarterlyFinancialStatements', 'MaterialChangesInSubsidiaries', 'ChangesBasedOnRevisionsOfAccountingStandard', 'ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard', 'ChangesInAccountingEstimates', 'RetrospectiveRestatement', 'NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock', 'NumberOfTreasuryStockAtTheEndOfFiscalYear', 'AverageNumberOfShares']


stock_fn = pd.read_csv("../../kaggle/data/supplemental_files/financials.csv")

