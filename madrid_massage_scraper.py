#!/usr/bin/env python3
"""
Madrid Massage Studio Scraper
Uses Google Places API (text search + details) to find centros de masaje in Madrid.
Saves to CSV on Desktop.
"""

import subprocess
import json
import time
import csv
import os

API_KEY = "AIzaSyDx4a7iq1lt4LItVg44_kDmzvlpK7Ftldo"
OUTPUT_DIR = os.path.expanduser("~/Desktop")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "madrid_massage_studios.csv")

def api_call(url):
    """Make API call via curl subprocess."""
    result = subprocess.run(
        ["curl", "-s", url],
        capture_output=True, text=True, timeout=30
    )
    return json.loads(result.stdout)

def search_places(query, page_token=None):
    """Text search for places."""
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={API_KEY}&language=es"
    if page_token:
        url += f"&pagetoken={page_token}"
    return api_call(url)

def get_place_details(place_id):
    """Get phone, full address, website for a place."""
    url = (
        f"https://maps.googleapis.com/maps/api/place/details/json"
        f"?place_id={place_id}&fields=name,formatted_address,formatted_phone_number,website,rating,user_ratings_total,url&key={API_KEY}"
    )
    return api_call(url)

def scrape_madrid_massage():
    results = []
    seen_ids = set()

    print("🔍 Searching 'centro de masaje Madrid'...")
    data = search_places("centro+de+masaje+Madrid")

    page_count = 0
    while data.get("results") and page_count < 3:  # 3 pages = ~60 results
        page_count += 1
        print(f"  Page {page_count}: {len(data['results'])} results")

        for place in data["results"]:
            place_id = place.get("place_id")
            if place_id in seen_ids:
                continue
            seen_ids.add(place_id)

            name = place.get("name", "")
            address = place.get("formatted_address", "")
            rating = place.get("rating", "")
            ratings_total = place.get("user_ratings_total", "")

            # Get details (phone, website)
            details = get_place_details(place_id).get("result", {})
            phone = details.get("formatted_phone_number", "")
            website = details.get("website", "")
            maps_url = details.get("url", "")

            results.append({
                "name": name,
                "address": address,
                "phone": phone,
                "rating": rating,
                "reviews": ratings_total,
                "website": website,
                "maps_url": maps_url,
            })
            print(f"  ✓ {name} | {phone}")

        # Next page
        next_token = data.get("next_page_token")
        if next_token:
            print("  ⏳ Waiting 2s for next page token...")
            time.sleep(2)
            data = search_places("", page_token=next_token)
        else:
            break

    return results

def save_csv(results):
    path = OUTPUT_FILE
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "name", "address", "phone", "rating", "reviews", "website", "maps_url"
        ])
        writer.writeheader()
        writer.writerows(results)
    return path

if __name__ == "__main__":
    print(f"📍 Madrid Massage Studio Scraper")
    print(f"📁 Output: {OUTPUT_FILE}\n")

    results = scrape_madrid_massage()

    if results:
        path = save_csv(results)
        print(f"\n✅ Done! {len(results)} studios saved to:\n{path}")
    else:
        print("\n❌ No results found. Check API key and billing.")
