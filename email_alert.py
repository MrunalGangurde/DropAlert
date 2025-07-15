import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def send_email(price, url):
    """Send a price drop email alert."""
    if not EMAIL or not PASSWORD:
        print("⚠️ Email credentials not set.")
        return

    msg = MIMEText(
        f"💰 The price has dropped to ₹{price}!\n\nBuy now: {url}"
    )
    msg["Subject"] = "📉 DropAlert: Price Drop Notification"
    msg["From"] = EMAIL
    msg["To"] = EMAIL  # You can change this to notify others

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")