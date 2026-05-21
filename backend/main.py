from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# allow GitHub Pages to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BusinessInput(BaseModel):
    business_name: str
    industry: str
    country: str
    size: str
    revenue: float
    expense: float
    cash: float
    risk: str
    goal: str


def sextant_engine(data):
    net = data.revenue - data.expense

    risk = "LOW"
    if net < 0:
        risk = "HIGH"
    elif data.expense > data.revenue * 0.7:
        risk = "MEDIUM"

    return {
        "business": data.business_name,
        "net_cashflow": net,
        "risk": risk,
        "message": "Processed by Sextant Engine"
    }


@app.post("/analyze")
def analyze(data: BusinessInput):
    return sextant_engine(data)


@app.get("/health")
def health():
    return {"status": "online"}
