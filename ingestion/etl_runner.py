from ingestion.coingecko import fetch_coingecko
from ingestion.coinpaprika import fetch_coinpaprika

def run_etl():
    gecko_data = fetch_coingecko()
    paprika_data = fetch_coinpaprika()

    return {
        "coingecko": gecko_data,
        "coinpaprika": paprika_data
    }
