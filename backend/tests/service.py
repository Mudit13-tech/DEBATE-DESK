from app.services.financial_data import get_company_financials

data = get_company_financials("RELIANCE.NS")

print(data)