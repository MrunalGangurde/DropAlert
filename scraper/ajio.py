import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

HEADERS = {"User-Agent": os.getenv("USER_AGENT", "Mozilla/5.0"),
    "Accept-Language": "en-US,en;q=0.9"
}

def clean_price(text):
    return int(''.join(filter(str.isdigit, text)))

def get_product_data(url):
    """Scrape product title, price, and image from Ajio"""
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find("h1")
    price = soup.select_one("div.price")
    image = soup.select_one("img")

    if not (title and price and image):
        return None

    return {
        "title": title.text.strip(),
        "price": clean_price(price.text),
        "image": image["src"]
    }