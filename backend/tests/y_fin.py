import yfinance as yf


def get_company_financials(ticker_symbol: str):

    ticker = yf.Ticker(ticker_symbol)
    balance_sheet = ticker.balance_sheet
    cash_flow = ticker.cash_flow
    income = ticker.income_stmt

    print(income.index)

value = get_company_financials("RELIANCE.NS")