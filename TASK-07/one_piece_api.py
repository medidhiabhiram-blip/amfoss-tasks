import aiohttp
import random

API_BASE = "https://api.api-onepiece.com/v2"

async def fetch_grand_line_intel() -> str:
    """Fetches random data regarding characters, bounties, or devil fruits."""
    endpoints = ["characters/en", "fruits/en"]
    selected_endpoint = random.choice(endpoints)
    url = f"{API_BASE}/{selected_endpoint}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as response:
                if response.status == 200:
                    data = await response.json()
                    if not data:
                        return "🌊 The mist clears, but no intel was found on the horizon."
                    
                    item = random.choice(data)
                    
                    if selected_endpoint == "characters/en":
                        name = item.get("name", "Unknown Pirate")
                        bounty = item.get("bounty", "Unknown")
                        size = item.get("size", "N/A")
                        return f"📜 **Intel Received:** Pirate **{name}** | Bounty: **{bounty} Berries** | Height: **{size}**"
                    else:
                        fruit_name = item.get("name", "Unknown Fruit")
                        type_str = item.get("type", "Unknown Class")
                        desc = item.get("description", "No detailed power records exist.")
                        return f"🍇 **Devil Fruit Intel:** **{fruit_name}** ({type_str}) - {desc[:150]}..."
                else:
                    return f"📡 News Coo intercepted a corrupted message (HTTP {response.status})."
    except Exception:
        # Fallback intel if external API is unreachable
        fallbacks = [
            "📜 **Intel Received:** Monkey D. Luffy | Bounty: **3,000,000,000 Berries**",
            "🍇 **Devil Fruit Intel:** Gomu Gomu no Mi (Paramecia/Zoan) - Gives user rubber properties.",
            "📜 **Intel Received:** Roronoa Zoro | Bounty: **1,111,000,000 Berries**"
        ]
        return random.choice(fallbacks)