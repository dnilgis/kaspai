import json
import os

# --- Static Replication of L2 Project Data ---
# Must be manually updated until a new L2 tracking API is found.
L2_PROJECTS = [
    {"name": "Zealous Swap", "tvl": "1.6M", "volume_24h": "17.5K", "category": "DeFi", "network": "Kasplex", "visit": "#"},
    {"name": "LFG.KASPA", "tvl": "82.5K", "volume_24h": "975.3", "category": "DeFi, Meme", "network": "Kasplex", "visit": "#"},
    {"name": "KSPR", "tvl": "26.5K", "volume_24h": "336.7", "category": "DeFi, Meme", "network": "Kasplex", "visit": "#"},
    {"name": "Kaspa Finance", "tvl": "15K", "volume_24h": "340.7", "category": "DeFi", "network": "Kasplex", "visit": "#"},
    {"name": "Moonbound", "tvl": "2.0", "volume_24h": "0.2", "category": "DeFi, Meme", "network": "Kasplex", "visit": "#"},
]

def fetch_l2_data():
    l2_stats = {
        "total_tvl": "1.8M", 
        "total_volume_24h": "19.2K",
        "total_projects": len(L2_PROJECTS),
        "networks_split": "5 / 0 (Kasplex / IGRA)", 
        "projects": L2_PROJECTS
    }
    
    os.makedirs('data', exist_ok=True)
    with open('data/l2_data.json', 'w') as f:
        json.dump(l2_stats, f, indent=4)

if __name__ == "__main__":
    fetch_l2_data()
