# Debate Desk

An IPO and stock analysis engine. The goal is to tell you whether an IPO is
worth investing in, by having several analysis agents argue the case from the
company's financials. Right now it is the data layer: a FastAPI service that
pulls a company's statements from Yahoo Finance and returns them as clean JSON.

## What works today

- `GET /companies/{ticker}/financials` returns, per reporting year:
  - **Income statement:** revenue, operating income, EBITDA, net income, diluted EPS, interest expense, tax provision
  - **Balance sheet:** total assets, total liabilities, equity, total debt, cash, working capital
  - **Cash flow:** operating cash flow, capex, free cash flow, change in cash
- `GET /health` and `GET /` for status checks.

Tickers use Yahoo Finance symbols, so NSE stocks take the `.NS` suffix
(`RELIANCE.NS`, `TCS.NS`).

## Tech stack

Python, FastAPI, Uvicorn, yfinance, pandas.

## Run locally

The imports expect the project folder to be called `debatedesk`, so clone it
under that name and start the server from the folder above it:

```bash
git clone https://github.com/Mudit13-tech/DEBATE-DESK.git debatedesk
python -m venv .venv && source .venv/bin/activate
pip install fastapi uvicorn pandas yfinance
uvicorn debatedesk.backend.app.main:app --reload
```

Then open http://127.0.0.1:8000/companies/RELIANCE.NS/financials, or
http://127.0.0.1:8000/docs for the interactive API docs.

## Project layout

```
backend/app/
  main.py                    FastAPI app and status routes
  api/routes/companies.py    /companies/{ticker}/financials
  services/financial_data.py Yahoo Finance fetch and row extraction
backend/tests/               scratch scripts for exploring yfinance
```

## Next

The valuation logic and the agents that debate an IPO's merits are still to
come.
