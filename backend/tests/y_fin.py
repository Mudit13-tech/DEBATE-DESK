import yfinance as yf


def get_company_financials(ticker_symbol: str):

    ticker = yf.Ticker(ticker_symbol)

    income = ticker.income_stmt

    print(type(income))
    print(income.index)
    print(income.columns)

    return income