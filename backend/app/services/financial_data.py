import yfinance as yf


def get_company_finData(ticker_symbol : str):
    ticker = yf.Ticker(ticker_symbol)

    income = ticker.income_stmt
    balance

    if "TotalRevenue" in income:
        revenue = income.loc['TotalRevenue']
    else:
        revenue = None

    if "NetIncome" in income.index:
        net_income = income.loc["NetIncome"]
    else:
        net_income = None

    return {
        "ticker": ticker_symbol,
        "revenue": revenue.to_dict() if revenue is not None else None,
        "net_income": net_income.to_dict()
    }