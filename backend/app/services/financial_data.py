import yfinance as yf
import pandas as pd


def extract_row(dataframe, row_name):
    if row_name in dataframe.index:
        row = dataframe.loc[row_name].dropna()
        return {
            str(date.date()) : float(value)
            for date,value in row.items()
        }

    return None

def get_company_financials(ticker_symbol : str):
    ticker = yf.Ticker(ticker_symbol)

    income = ticker.income_stmt
    balance_sheet = ticker.balance_sheet
    cash_flow = ticker.cash_flow

    return {
        "ticker" : ticker_symbol,

        "income_statement": {
            "revenue": extract_row(income, "Total Revenue"),
            "operating_income": extract_row(
                income,
                "Operating Income"
            ),

            "ebitda": extract_row(
                income,
                "EBITDA"
            ),

            "net_income": extract_row(
                income,
                "Net Income"
            ),

            "eps": extract_row(
                income,
                "Diluted EPS"
            ),

            "interest_expense": extract_row(
                income,
                "Interest Expense"
            ),

            "tax_provision": extract_row(
                income,
                "Tax Provision"
            )
        },

        "balance_sheet": {
            "total_assets": extract_row(balance_sheet, "Total Assets"),
            "total_liabilities": extract_row(
                balance_sheet,
                "Total Liabilities Net Minority Interest"
            ),
            "equity": extract_row(
                balance_sheet,
                "Stockholders Equity"
            ),
            "total_debt": extract_row(
                balance_sheet,
                "Total Debt"
            ),
            "cash": extract_row(
                balance_sheet,
                "Cash And Cash Equivalents"
            ),
            "working_capital": extract_row(
                balance_sheet,
                "Working Capital"
            )
        },

        "cash_flow": {
            "operating_cash_flow": extract_row(
                cash_flow,
                "Operating Cash Flow"
            ),
            "capital_expenditure": extract_row(
                cash_flow,
                "Capital Expenditure"
            ),
            "free_cash_flow": extract_row(
                cash_flow,
                "Free Cash Flow"
            ),
            "changes_in_cash": extract_row(
                cash_flow,
                "Changes In Cash"
            )
        }
    }

data = get_company_financials("RELIANCE.NS")

print(data)