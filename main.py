# importing important libraries
import streamlit as st
from scraper import amazon,flipkart,croma,tatacliq,myntra,ajio,reliance
from database import init_db,get_latest_price,store_price
from utils import detect_platform,check_price_drop,get_affiliate_link
from email_alert import send_email
from telegram_alert import send_telegram_alert
import os
from dotenv import load_dotenv

load_dotenv()
init_db()

st.set_page_config(page_title = "DropAlert",layout="centered")
st.title("DropAlert - Price Tracker with Alerts")

url = st.text_input("Enter Product URL")
if url:
    platform = detect_platform(url)

    if not platform:
        st.error("Oops,incorrect url.")
    else:
        st.info(f"Platform detected:{platform.capitalize()}")

        try:
            scraper = {
                "amazon": amazon.get_product_data,
                "flipkart": flipkart.get_product_data,
                "croma": croma.get_product_data,
                "tatacliq": tatacliq.get_product_data,
                "myntra": myntra.get_product_data,
                "ajio": ajio.get_product_data,
                "reliance": reliance.get_product_data,
            }[platform]

            data = scraper(url)

            if data:
                st.image(data["image"],width=250)
                st.subheader(data['title'])
                st.write(f"Current Price:Rs.{data['price']}")

                #Load past prices
                old_price = get_latest_price(url)

                if old_price:
                    dropped,diff= check_price_drop(old_price,data["price"])
                    st.write(f"Last tracked price: Rs. {old_price}")

                    if dropped:
                        st.sucess(f"Price droped by Rs.{diff}!")
                        if os.getenv("Email"):
                            send_email(data["price"],url)
                    else:
                        st.info("No price drop detected.")
                else:
                    st.info("First time Product tracking.")

                store_price(url,data["price"])

                affiliate = get_affiliate_link(url)
                st,markdown(f"[Buy Now]({affiliate})",unsafe_allow_html=True)
            else:
                st.error("failed to extract product data.")

        except Exeception as e:
            st.error(f"Error:{str(e)}")