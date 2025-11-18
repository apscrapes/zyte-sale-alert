# 📦 Product Sale Alert using Zyte API auto extract feature

A simple beginner-friendly project demonstrating how to use the Zyte API Automatic Extraction feature to scrape structured product data, especially the product price, from an e-commerce product page and trigger notification on your mobile device when the price drops a target set value.

This project is designed as a clean and minimal "Hello World" for Zyte’s extraction capabilities.

---

## Features

- Uses Zyte API automatic product extraction (`product: true`)
- No HTML parsing or selectors required
- Works with most e-commerce product URL
- Extracts:
  - price
  - currency
  - name
  - availability
- Uses `.env` for secrets and API keys
- Lightweight Python setup suitable for beginners
- Uses IFTTT to trigger automatic mobile notification

---

# Setting things up

1. Create IFTTT automation applet 
2. Follow these steps to install and run the project.

---

## 1. Clone the Repository

- git clone https://github.com/apscrapes/zyte-sale-alert.git
- cd zyte-sale-alert

## 2. Create python environment
python3 -m venv venv
source venv/bin/activate
A simple beginner-friendly project demonstrating how to use the Zyte API Automatic Extraction feature to scrape structured product data, especially the product price, from an e-commerce product page.

This project is designed as a clean and minimal "Hello World" for Zyte’s extraction capabilities.

---

## Features

- Uses Zyte API automatic product extraction (`product: true`)
- No HTML parsing or selectors required
- Works with any e-commerce product URL
- Extracts:
  - price
  - currency
  - name
  - availability
- Uses `.env` for secrets
- Lightweight Python setup suitable for beginners

---

# Getting Started

Follow these steps to install and run the project.

---

## 1. Clone the Repository
git clone https://github.com/apscrapes/zyte-sale-alert.git
cd zyte-sale-alert

## 2. Create and Activate a Virtual Environment
pip install -r requirements.txt

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Add Your Zyte API Key
Create a .env file inside the project root and add following 
ZYTE_API_KEY=your_api_key_here
EVENT_NAME-your event name from IFTTT
IFTTT_KEY=your webhook api key from IFTTT

## 5. Set product URL and target price
In src/price_extract_auto.py you can setup product URL you want to track and the target price

## 6. Run the Script
python src/price_extract_auto.py

## Example Output
Price: 51.77

Price: 40.00, Triggering notification

Once the product hits equal or below your target price, IFTTT webhook is called which will trigger the notification on your device with product link so you can straight away open it and order. 

# How It Works

The script sends the following payload to the Zyte API:
```
{
  "url": "<product-url>",
  "product": true
}
```

Zyte automatically:
Identifies the target page as a product detail page
Extracts structured product information

Returns a clean JSON object containing details such as:
- name
- price
- currency
- availability
- SKU
- images
- description

Your script reads the extracted price and prints it.
No selectors, regex, or HTML parsing required.

# Project Structure

zyte-sale-alert/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
│
└── src/
    └── price_extract_auto.py

# Troubleshooting

```ERROR: ZYTE_API_KEY not found in environment.```
Fix:
Ensure .env exists
Ensure key is correct
Close and reopen terminal
Confirm venv is activated

```ModuleNotFoundError: zyte_api```
pip install zyte-api

```Virtual environment not activating```
chmod +x venv/bin/activate
source venv/bin/activate

