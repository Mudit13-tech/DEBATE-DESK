from fastapi import FastAPI

app = FastAPI(
    title = 'Debate-desk',
    description="Financial analysis and multi-agent IPO valuation engine",
    version="0.1.0"
)

@app.get("/")
def root():
    return{
        "project": "Debate-Desk",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return{
        "status": "healthy",
    }

@app.get("/hello/{name}")
def hello(name):
    return {
        "message": f"hello {name}"
    }
