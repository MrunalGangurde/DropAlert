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
    """Scrape product title, price, and image from Flipkart"""
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.select_one("span.B_NuCI")
    price = soup.select_one("div._30jeq3")
    image = soup.select_one("img._396cs4._2amPTt._3qGmMb")

    if not (title and price and image):
        return None

    return {
        "title": title.text.strip(),
        "price": clean_price(price.text),
        "image": image["src"]
    }