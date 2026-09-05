from fastapi import APIRouter
from debatedesk.backend.app.services.financial_data import get_company_financials

router = APIRouter()

@router.get("/companies/{ticker}/financials")
def company_financials(ticker : str):
    data = get_company_financials(ticker)
    return data

