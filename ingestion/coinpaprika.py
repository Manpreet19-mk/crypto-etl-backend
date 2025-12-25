"""
CoinPaprika Ingestion Module

NOTE:
CoinPaprika supports API-key based authentication.
Due to temporary authentication issues on the provider side,
public endpoints are used. The architecture supports env-based
API keys if required in future.
"""

import requests
from services.db import SessionLocal
from services.models import CryptoPrice

URL = "https://api.coinpaprika.com/v1/tickers"

def fetch_coinpaprika():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    return response.json()[:5]  # top 5 coins

def load_coinpaprika():
    data = fetch_coinpaprika()
    db = SessionLocal()

    for coin in data:
        record = CryptoPrice(
            source="coinpaprika",
            symbol=coin.get("symbol"),
            name=coin.get("name"),
            price_usd=coin["quotes"]["USD"]["price"]
        )
        db.add(record)

    db.commit()
    db.close()
