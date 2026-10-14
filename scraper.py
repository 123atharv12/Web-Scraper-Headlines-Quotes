
import requests
from bs4 import BeautifulSoup
import json

URL = "https://quotes.toscrape.com/"

def scrape_quotes():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        results = []
        for item in soup.select(".quote"):
            quote = item.select_one(".text")
            author = item.select_one(".author")

            if quote and author:
                results.append({
                    "quote": quote.get_text(strip=True),
                    "author": author.get_text(strip=True)
                })

        with open("quotes.json", "w", encoding="utf-8") as file:
            json.dump(results, file, indent=4, ensure_ascii=False)

        print(f"Saved {len(results)} quotes to quotes.json")
        for item in results:
            print(item["quote"], "-", item["author"])

    except requests.RequestException as error:
        print("Request failed:", error)

if __name__ == "__main__":
    scrape_quotes()
