from fastapi import FastAPI
from ingestion.etl_runner import run_etl
from services.db import SessionLocal
from services.models import CryptoPrice

app = FastAPI(title="Crypto ETL Backend")

@app.get("/")
def root():
    return {"status": "API is running"}

@app.get("/health")
def health():
    return {"db": "connected"}

@app.post("/etl/run")
def trigger_etl():
    run_etl()
    return {"status": "ETL completed"}

@app.get("/data")
def get_data():
    db = SessionLocal()
    data = db.query(CryptoPrice).all()
    db.close()

    return [
        {
            "source": d.source,
            "symbol": d.symbol,
            "name": d.name,
            "price_usd": d.price_usd,
            "timestamp": d.timestamp,
        }
        for d in data
    ]
from services.db import engine, Base

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

    