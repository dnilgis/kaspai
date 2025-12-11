import json
import requests
import os

COINGECKO_API = "https://api.coingecko.com/api/v3/coins/kaspa"

def fetch_market_data():
    try:
        response = requests.get(COINGECKO_API, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        market_data = {
            "price_usd": round(data['market_data']['current_price']['usd'], 4),
            "volume_24h": int(data['market_data']['total_volume']['usd']),
            "market_cap": int(data['market_data']['market_cap']['usd']),
            "ranking": data['market_cap_rank'],
            "price_change_24h": round(data['market_data']['price_change_percentage_24h'], 2)
        }
        return market_data
    except requests.exceptions.RequestException:
        return None

if __name__ == "__main__":
    market_data = fetch_market_data()
    if market_data:
        os.makedirs('data', exist_ok=True)
        with open('data/market_data.json', 'w') as f:
            json.dump(market_data, f, indent=4)
