import requests
from services.db import SessionLocal
from services.models import CryptoPrice

URL = "https://api.coingecko.com/api/v3/coins/markets"

def fetch_coingecko():
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 5,
        "page": 1
    }
    response = requests.get(URL, params=params)
    response.raise_for_status()
    return response.json()

def load_coingecko():
    data = fetch_coingecko()
    db = SessionLocal()

    for coin in data:
        record = CryptoPrice(
            source="coingecko",
            symbol=coin["symbol"],
            name=coin["name"],
            price_usd=coin["current_price"]
        )
        db.add(record)

    db.commit()
    db.close()

