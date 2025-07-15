def detect_platform(url):
    """Detect e-commerce platform from URL"""
    if "amazon." in url:
        return "amazon"
    elif "flipkart.com" in url:
        return "flipkart"
    elif "croma.com" in url:
        return "croma"
    elif "tatacliq.com" in url:
        return "tatacliq"
    elif "reliancedigital.in" in url:
        return "reliance"
    elif "myntra.com" in url:
        return "myntra"
    elif "ajio.com" in url:
        return "ajio"
    return None

def check_price_drop(old_price, new_price):
    """Return True if new price is lower than old"""
    if old_price and new_price < old_price:
        return True, old_price - new_price
    return False, 0

def get_affiliate_link(original_url):
    """Append affiliate tag to Amazon link"""
    if "amazon" in original_url:
        tag = "tag=your-affiliate-id"
        join_char = "&" if "?" in original_url else "?"
        return f"{original_url}{join_char}{tag}"
    return original_url