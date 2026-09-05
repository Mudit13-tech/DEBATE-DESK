from app.services.financial_data import get_company_finData

data = get_company_finData("RELIANCE.NS")

print(data)