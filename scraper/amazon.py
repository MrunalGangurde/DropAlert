import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

HEADERS = {
    "User-Agent": os.getenv("USER_AGENT", "Mozilla/5.0"),
    "Accept-Language": "en-US,en;q=0.9"
}

def clean_price(text):
    return int(''.join(filter(str.isdigit, text)))

def get_product_data(url):
    """Scrape product title, price, and image from Amazon"""
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find(id="productTitle")
    price = soup.find("span", class_="a-price-whole")
    image_tag = soup.select_one("#imgTagWrapperId img")

    if not (title and price and image_tag):
        return None

    return {
        "title": title.text.strip(),
        "price": clean_price(price.text),
        "image": image_tag["src"]
    }