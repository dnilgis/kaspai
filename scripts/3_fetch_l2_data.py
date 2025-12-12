import json
import requests
import os

# CoinGecko Kaspa Ecosystem Endpoint
KRC20_API = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=kaspa-ecosystem&order=market_cap_desc"

def fetch_l2_data():
    projects = []
    total_tvl = 0
    total_vol = 0
    
    try:
        response = requests.get(KRC20_API, timeout=10)
        if response.status_code == 200:
            data = response.json()
            
            for item in data:
                # Filter to ensure we are getting KRC20-like tokens or main ecosystem coins
                if item['id'] == 'kaspa': continue # Skip KAS itself
                
                projects.append({
                    "name": item['name'],
                    "symbol": item['symbol'].upper(),
                    "price": item['current_price'],
                    "tvl": item.get('market_cap', 0), # Using MCAP as proxy for TVL/Size
                    "volume_24h": item['total_volume'],
                    "change_24h": item.get('price_change_percentage_24h', 0),
                    "category": "KRC-20",
                    "network": "Kasplex",
                    "visit": f"https://www.coingecko.com/en/coins/{item['id']}"
                })
                
                total_tvl += item.get('market_cap', 0) or 0
                total_vol += item.get('total_volume', 0) or 0
                
    except Exception as e:
        print(f"CoinGecko KRC20 fetch failed: {e}")
        # FALLBACK: Keep your old manual list if API fails
        projects = [
            {"name": "Nacho the Kat", "symbol": "NACHO", "tvl": 50000000, "volume_24h": 120000, "change_24h": 0, "category": "Meme", "network": "Kasplex", "visit": "#"},
            {"name": "Kasper", "symbol": "KASPER", "tvl": 7500000, "volume_24h": 45000, "change_24h": 0, "category": "Meme", "network": "Kasplex", "visit": "#"}
        ]

    # Format Summary
    l2_stats = {
        "total_tvl": f"{total_tvl / 1_000_000:.1f}M", 
        "total_volume_24h": f"{total_vol / 1_000:.1f}K",
        "total_projects": len(projects),
        "networks_split": f"{len(projects)} / 0 (Kasplex / IGRA)", 
        "projects": projects
    }
    
    os.makedirs('data', exist_ok=True)
    with open('data/l2_data.json', 'w') as f:
        json.dump(l2_stats, f, indent=4)

if __name__ == "__main__":
    fetch_l2_data()
