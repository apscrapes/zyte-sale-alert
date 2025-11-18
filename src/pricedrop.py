import os
import sys
import requests
from zyte_api import ZyteAPI
from dotenv import load_dotenv

PRODUCT_URL = "https://outdoor.hylnd7.com/product/a1b2c3d4-e5f6-4a7b-8c9d-000000000293"
DESIRED_PRICE = 250

load_dotenv()

# from Zyte API
ZYTE_API_KEY = os.getenv("ZYTE_API_KEY")

# from IFTTT Service applets
EVENT_NAME= os.getenv("EVENT_NAME")
IFTTT_KEY= os.getenv("IFTTT_KEY")


if not ZYTE_API_KEY:
    print("ERROR: ZYTE_API_KEY not found in environment.")
    sys.exit(1)


def trigger_ifttt(event_name, key, value1):
    url = f"https://maker.ifttt.com/trigger/{event_name}/json/with/key/{key}"
    
    payload = {
        "value1": value1,
    }

    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Notification triggered!")
    else:
        print("Error Sending Notification:", response.text)

def main():
    client = ZyteAPI(api_key=ZYTE_API_KEY)

    payload = {
        "url": PRODUCT_URL,
        "product": True,          
    }

    resp = client.get(payload)

    product = resp.get("product") 
    if isinstance(product, list) and product:
        product = product[0]

    if product:
        price = product.get("price")
        price_float = float(price)
        #print("Price:", price_float)
        if price_float <= DESIRED_PRICE:
            trigger_ifttt(EVENT_NAME, IFTTT_KEY, value1 = PRODUCT_URL)

    if not product:
        print("No product extracted. Response preview (top keys):")
        for k in list(resp.keys())[:10]:
            print(" -", k)
        return

if __name__ == "__main__":
    main()
