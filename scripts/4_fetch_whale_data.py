import json
import requests
import os

# Official Endpoint for Top Addresses
TOP_ADDRESSES_API = "https://api.kaspa.org/addresses/top"

# Known Wallet Tags (We can expand this list manually over time)
KNOWN_WALLETS = {
    "kaspa:precqv0krj3r6uyyfa36ga7s0u9jct0v4wg8ctsfde2gkrsgwgw8jgxfzfc98": "Kaspa Dev Fund",
    "kaspa:qrhlh8g7p2y6r5488k65q64049p5z989354k488664": "Change Address (Exchange?)",
}

def fetch_whale_data():
    try:
        # Fetch the top addresses
        response = requests.get(TOP_ADDRESSES_API, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # The API returns a list of objects. We'll process the top 20-50 to keep the file size manageable.
        # Structure: [{'address': '...', 'balance': 123456789000000}, ...]
        
        whales = []
        for rank, item in enumerate(data[:50], start=1): # Limit to Top 50 for display speed
            addr = item.get('address', 'Unknown')
            # Convert sompi to KAS (1 KAS = 100,000,000 sompi)
            balance = round(item.get('balance', 0) / 100_000_000, 2)
            
            # Check for known tags
            name = KNOWN_WALLETS.get(addr, "Unknown Whale")
            
            whales.append({
                "rank": rank,
                "address": addr,
                "balance": balance,
                "name": name,
                "link": f"https://explorer.kaspa.org/addresses/{addr}"
            })
            
        # Create summary stats
        top_10_holdings = sum(w['balance'] for w in whales[:10])
        
        whale_stats = {
            "top_10_total": f"{top_10_holdings:,.0f}",
            "whales": whales
        }
        
        os.makedirs('data', exist_ok=True)
        with open('data/whale_data.json', 'w') as f:
            json.dump(whale_stats, f, indent=4)
            
    except Exception as e:
        print(f"Error fetching whale data: {e}")

if __name__ == "__main__":
    fetch_whale_data()
