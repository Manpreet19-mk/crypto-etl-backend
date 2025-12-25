from sqlalchemy import Column, Integer, String, Float, DateTime
from services.db import Base
from datetime import datetime

class CryptoPrice(Base):
    __tablename__ = "crypto_prices"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)
    symbol = Column(String, index=True)
    name = Column(String)
    price_usd = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
